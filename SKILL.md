---
name: repo-share
description: Discover and verify useful public GitHub projects, then draft X posts or illustrated X Articles in ready-to-use natural writing styles. Use for open-source discovery or sharing; not for GitHub account administration or unrelated social copy.
---

# Repo Share

Find projects automatically, verify them at their original sources, then help users discover or share them. A search result is a candidate, not an endorsement. Drafts and images are for the user to review; never publish to X without a separate explicit request.

## Choose the task

- For project discovery or comparison, use **Discovery** and **Verify** below, then answer the request directly.
- For X sharing, read [references/x-writing.md](references/x-writing.md). If the user has not chosen a format, ask whether they want six independent short posts or one long X Article. Do not ask again when their request or previous answer already settles it.
- For an Article, show six short text-only project directions with original repository links first. Stop for the user's choice. On their next reply, continue with the chosen project without restarting discovery unless the topic changed or the information became stale.

## Discovery

- Match the request to `--category`: `all`, `ai`, `hardware`, `tools`, `ai-agents`, `ai-coding`, `local-llm`, `computer-vision`, `robotics`, `smart-home`, `3d-printing`, or `electronics`. For another niche, use `--query` with GitHub search terms or qualifiers.
- Locate `scripts/discover.py` relative to this `SKILL.md` and run it with an available Python 3 executable, for example `python <skill-directory>/scripts/discover.py --category all --limit 12`. Do not assume the current working directory is the skill directory. The script uses GitHub's live Search API, removes duplicate, forked, archived, and unlicensed candidates, and needs only the standard library and network access. An optional `GITHUB_TOKEN` raises API limits; never print or save it.
- For lesser-known active projects, try `--min-stars 100 --max-stars 3000 --sort updated --days 180`. These controls change the candidate pool; they do not prove quality. Search more candidates than the requested final count so weak or imageless projects can be replaced.
- If the user specifies a theme, follow it. Otherwise, for a six-project X batch select two verified AI projects, two open-hardware projects, and two practical tools. Correct the script's topic-based categories after reading each repository. Do not fill missing category slots with unrelated projects or unverified entries.

## Verify

- Inspect the repository README and linked official docs for a concrete use case, installation or deployment path, supported platforms, license, and meaningful recent activity. Check releases or change logs when update claims matter. If instructions, licensing, or required services are unclear, say so or choose another project.
- Surface material constraints: required hardware, external API or model, paid service, operating system, and self-hosting burden. Do not infer “offline,” “free,” or “no API key” from an open-source license.
- Stars and last push are discovery signals, not proof of quality or growth. Describe growth only with a dated source and time window. A public repository without a clear license is not automatically open source.
- Prefer distinct use cases and avoid repeating earlier suggestions when accessible history exists. Never invent a repository, feature, image, download, or hands-on result.

## Discovery-only response

Group verified results by actual use case. For each, give a plain-language purpose, original repository link, license, last push or release date, verified installation entry point, and material caveat. Provide a direct download link only after checking that it exists. If the user asks only for leads, a lighter list is fine when labeled unverified.

If the script reports incomplete results, rate limits, or a partial fetch, disclose the limitation. Narrow the query or retry when the API allows it. The bundled script covers GitHub only; if the user asks for GitLab, Gitee, or another source, search it directly and label provenance. A recurring background collection needs a separately requested schedule.
