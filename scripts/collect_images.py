"""Download README image candidates from a public GitHub repository for visual review."""

import argparse
import base64
from html import unescape
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


MAX_BYTES = 8 * 1024 * 1024
REPO = re.compile(r"^[\w.-]+/[\w.-]+$")
MARKDOWN_IMAGE = re.compile(r"!\[([^]]*)\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
HTML_IMAGE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*['\"]([^'\"]+)['\"][^>]*>", re.I)
ALT = re.compile(r"\balt\s*=\s*['\"]([^'\"]*)['\"]", re.I)


def allowed(url):
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and (host == "github.com" or host == "raw.githubusercontent.com" or host == "user-images.githubusercontent.com" or host.endswith(".githubusercontent.com"))


class SafeRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not allowed(newurl):
            raise ValueError(f"Disallowed redirect: {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


OPENER = build_opener(SafeRedirects)


def request(url, token=None, limit=MAX_BYTES):
    if not allowed(url) and not url.startswith("https://api.github.com/repos/"):
        raise ValueError(f"Disallowed URL: {url}")
    headers = {"User-Agent": "repo-share-skill", "Accept": "application/vnd.github+json"}
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = "Bearer " + token
    with OPENER.open(Request(url, headers=headers), timeout=25) as response:
        if response.length is not None and response.length > limit:
            raise ValueError("Image exceeds 8 MiB")
        data = response.read(limit + 1)
        if len(data) > limit:
            raise ValueError("Image exceeds 8 MiB")
        return data


def candidates(readme, base_url):
    found = []
    for match in MARKDOWN_IMAGE.finditer(readme):
        found.append((unescape(match.group(1)), unescape(match.group(2) or match.group(3))))
    for match in HTML_IMAGE.finditer(readme):
        tag = match.group(0)
        alt = ALT.search(tag)
        found.append((unescape(alt.group(1)) if alt else "", unescape(match.group(1))))
    seen = set()
    ranked = []
    for alt, raw in found:
        url = urljoin(base_url, raw)
        if not allowed(url) or url in seen:
            continue
        seen.add(url)
        hint = (alt + " " + urlparse(url).path).lower()
        if any(word in hint for word in ("badge", "shield", "build-status", "coverage", "logo", "icon", "avatar")):
            continue
        score = sum(word in hint for word in ("screenshot", "screen", "preview", "demo", "photo", "device", "hardware", "product", "ui", "截图", "实物"))
        ranked.append((score, alt, url))
    return sorted(ranked, key=lambda item: item[0], reverse=True)


def image_type(data):
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "gif"
    return None


def collect(repo, output, count, token):
    api = f"https://api.github.com/repos/{repo}/readme"
    info = json.loads(request(api, token, 5 * 1024 * 1024))
    readme = base64.b64decode(info["content"]).decode("utf-8", "replace")
    base_url = info.get("download_url")
    if not base_url or not allowed(base_url):
        raise ValueError("README has no GitHub-hosted download URL")
    output.mkdir(parents=True, exist_ok=True)
    items = []
    for score, alt, url in candidates(readme, base_url):
        if len(items) >= count:
            break
        try:
            data = request(url)
        except (HTTPError, URLError, ValueError, TimeoutError):
            continue
        suffix = image_type(data)
        if not suffix:
            continue
        path = output / f"{repo.replace('/', '-')}-{len(items) + 1}.{suffix}"
        path.write_bytes(data)
        items.append({"file": str(path.resolve()), "source_url": url, "alt": alt, "readme_url": info["html_url"], "score": score, "visual_review_required": True})
    manifest = {"repository": f"https://github.com/{repo}", "images": items}
    (output / f"{repo.replace('/', '-')}-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def self_test():
    base = "https://raw.githubusercontent.com/example/project/main/README.md"
    text = "![UI](docs/screenshot.png) ![build](https://img.shields.io/badge/x-y) <img src='photos/device.jpg' alt='device'>"
    result = candidates(text, base)
    assert len(result) == 2 and result[0][2].startswith("https://raw.githubusercontent.com/")
    assert not allowed("https://localhost/a.png") and not allowed("http://github.com/a.png")
    assert image_type(b"\x89PNG\r\n\x1a\n123") == "png" and image_type(b"<svg>") is None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", help="Public GitHub owner/repo")
    parser.add_argument("--output", type=Path, default=Path("images"))
    parser.add_argument("--count", type=int, default=4)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("self-test passed")
        return 0
    if not args.repo or not REPO.fullmatch(args.repo) or not 1 <= args.count <= 12:
        parser.error("repo must be owner/repo; count must be 1-12")
    try:
        manifest = collect(args.repo, args.output, args.count, os.getenv("GITHUB_TOKEN"))
    except (HTTPError, URLError, ValueError, KeyError, TimeoutError) as error:
        print(f"Cannot collect images: {error}", file=sys.stderr)
        return 1
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
