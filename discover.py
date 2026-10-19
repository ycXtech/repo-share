"""Find and classify public GitHub repositories with no third-party packages."""

import argparse
from datetime import datetime, timedelta, timezone
import json
import math
import os
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


FEEDS = {
    "ai": ("topic:artificial-intelligence", "topic:llm"),
    "hardware": ("topic:open-hardware", "topic:arduino"),
    "tools": ("topic:productivity", "topic:developer-tools"),
    "ai-agents": ("topic:ai-agents", "topic:autonomous-agents"),
    "ai-coding": ("topic:ai-coding", "topic:code-assistant"),
    "local-llm": ("topic:llm-inference", "topic:local-llm"),
    "computer-vision": ("topic:computer-vision", "topic:stable-diffusion"),
    "robotics": ("topic:robotics", "topic:robot"),
    "smart-home": ("topic:home-automation", "topic:smart-home"),
    "3d-printing": ("topic:3d-printing", "topic:3d-printer"),
    "electronics": ("topic:open-hardware", "topic:arduino"),
}

SUBCATEGORIES = (
    ("硬件", "机器人", {"robotics", "robot", "ros", "ros2", "drone", "autonomous-vehicle"}),
    ("硬件", "智能家居", {"home-automation", "smart-home", "home-assistant", "iot"}),
    ("硬件", "3D 打印", {"3d-printing", "3d-printer", "reprap"}),
    ("硬件", "开发板与电子", {"arduino", "esp32", "embedded", "microcontroller", "pcb", "electronics"}),
    ("硬件", "其他硬件", {"open-hardware", "hardware", "firmware"}),
    ("AI", "智能体", {"ai-agents", "autonomous-agents", "agentic-ai", "llm-agents", "ai-agent"}),
    ("AI", "编程", {"ai-coding", "code-assistant", "coding-assistant", "copilot"}),
    ("AI", "本地模型", {"llm-inference", "local-llm", "local-ai", "ollama"}),
    ("AI", "视觉", {"computer-vision", "stable-diffusion", "image-generation", "object-detection"}),
    ("AI", "大模型", {"llm", "large-language-model", "language-model", "generative-ai"}),
    ("AI", "其他 AI", {"artificial-intelligence", "machine-learning", "deep-learning", "ai"}),
    ("工具", "效率与自动化", {"productivity", "workflow-automation", "automation"}),
    ("工具", "开发者工具", {"developer-tools", "devtools", "cli", "command-line"}),
)


def classify(repo):
    topics = set(repo.get("topics") or [])
    for group, subcategory, markers in SUBCATEGORIES:
        if topics & markers:
            return group, subcategory
    return "其他", "待核对"


def fetch(query, token, sort):
    url = "https://api.github.com/search/repositories?" + urlencode({
        "q": query, "sort": sort, "order": "desc", "per_page": 100,
    })
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "repo-share-skill",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        with urlopen(Request(url, headers=headers), timeout=25) as response:
            return json.load(response)
    except HTTPError as error:
        if error.code in (403, 429):
            reset = error.headers.get("X-RateLimit-Reset")
            when = datetime.fromtimestamp(int(reset), timezone.utc).isoformat() if reset and reset.isdigit() else "稍后"
            raise RuntimeError(f"GitHub API 限流或拒绝访问（HTTP {error.code}）；重置时间：{when}") from None
        raise RuntimeError(f"GitHub API 请求失败（HTTP {error.code}）") from None
    except URLError as error:
        raise RuntimeError(f"无法连接 GitHub API：{error.reason}") from None


def rank(repo):
    pushed = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
    age_days = max(0, (datetime.now(timezone.utc) - pushed).days)
    return math.log10(repo["stargazers_count"] + 1) * 2 + max(0, 2 - age_days / 240)


def relevant(category, repo):
    if category != "robotics":
        return True
    topics = set(repo.get("topics") or [])
    text = f"{repo.get('name', '')} {repo.get('description') or ''}".lower()
    physical_topics = {"ros", "ros2", "robot-arm", "humanoid-robot", "drone", "rover", "autonomous-vehicle"}
    return bool(topics & physical_topics or re.search(r"\brobots?\b|robotic|rover|drone|autopilot|humanoid|机械臂|机器人", text))


def diverse(repos, limit):
    first, rest, seen = [], [], set()
    for repo in repos:
        subcategory = classify(repo)[1]
        (first if subcategory not in seen else rest).append(repo)
        seen.add(subcategory)
    return (first + rest)[:limit]


def discover(category, keyword, limit, min_stars, max_stars, days, sort, token):
    since = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
    bases = FEEDS["ai"] + FEEDS["hardware"] + FEEDS["tools"] if category == "all" else FEEDS[category]
    if keyword and category == "all":
        bases = ("",)
    stars = f"stars:{min_stars}..{max_stars}" if max_stars is not None else f"stars:>={min_stars}"
    queries = [" ".join(part for part in (
        base, keyword, stars, f"pushed:>{since}",
        "archived:false", "fork:false",
    ) if part) for base in bases]

    found = {}
    warnings = []
    for query in queries:
        try:
            data = fetch(query, token, sort)
        except RuntimeError as error:
            warnings.append(f"{query}: {error}")
            continue
        if data.get("incomplete_results"):
            warnings.append(f"GitHub 标记该查询的结果不完整：{query}")
        for repo in data.get("items", []):
            license_id = (repo.get("license") or {}).get("spdx_id")
            if repo.get("archived") or repo.get("fork") or not license_id or license_id == "NOASSERTION" or not relevant(category, repo):
                continue
            found[repo["id"]] = repo

    if not found and warnings:
        raise RuntimeError("；".join(warnings))
    ranked = sorted(found.values(), key=rank, reverse=True)
    if category == "all" and not keyword:
        groups = ("AI", "硬件", "工具")
        chosen = []
        for i, group in enumerate(groups):
            quota = limit // len(groups) + (i < limit % len(groups))
            chosen.extend(diverse([repo for repo in ranked if classify(repo)[0] == group], quota))
        chosen += [repo for repo in ranked if repo not in chosen][: limit - len(chosen)]
    else:
        chosen = diverse(ranked, limit)
    results = []
    for repo in chosen:
        group, subcategory = classify(repo)
        results.append({
            "name": repo["full_name"],
            "description": repo.get("description") or "",
            "url": repo["html_url"],
            "homepage": repo.get("homepage") or None,
            "releases_url": repo["html_url"] + "/releases",
            "category": group,
            "subcategory": subcategory,
            "topics": repo.get("topics") or [],
            "language": repo.get("language"),
            "license": repo["license"]["spdx_id"],
            "stars": repo["stargazers_count"],
            "last_push": repo["pushed_at"][:10],
        })
    return {
        "source": "GitHub Search API",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "category_query": category,
        "keyword_query": keyword,
        "sort": sort,
        "min_stars": min_stars,
        "max_stars": max_stars,
        "matched_after_filters": len(found),
        "results": results,
        "warnings": warnings,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="Check classification without network access")
    parser.add_argument("--category", choices=("all", *FEEDS), default="all")
    parser.add_argument("--query", default="", help="GitHub search terms/qualifiers, preferably English")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--min-stars", type=int, default=20)
    parser.add_argument("--max-stars", type=int, help="Optional cap for finding less-famous projects")
    parser.add_argument("--days", type=int, default=730, help="Maximum days since last push")
    parser.add_argument("--sort", choices=("stars", "updated"), default="stars")
    args = parser.parse_args()
    if args.self_test:
        assert classify({"topics": ["robotics", "3d-printing"]}) == ("硬件", "机器人")
        assert classify({"topics": ["ai-agents", "llm"]}) == ("AI", "智能体")
        assert classify({"topics": ["developer-tools"]}) == ("工具", "开发者工具")
        assert not relevant("robotics", {"name": "WebSpider", "description": "Visual web crawler", "topics": ["robotics", "rpa"]})
        assert [repo["id"] for repo in diverse([
            {"id": 1, "topics": ["ai-agents"]},
            {"id": 2, "topics": ["ai-agents"]},
            {"id": 3, "topics": ["computer-vision"]},
        ], 2)] == [1, 3]
        print("self-test passed")
        return 0
    if not 1 <= args.limit <= 100 or args.min_stars < 0 or args.days < 1 or (args.max_stars is not None and args.max_stars < args.min_stars):
        parser.error("limit must be 1-100, min-stars >= 0, max-stars >= min-stars, days >= 1")
    try:
        data = discover(args.category, args.query.strip(), args.limit, args.min_stars, args.max_stars, args.days, args.sort, os.getenv("GITHUB_TOKEN"))
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 1
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
