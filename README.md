# repo-share

发现值得分享的开源项目，并把它们整理成可以直接修改、配图和发布的中文 X 短帖或长文草稿。

`repo-share` 是一个基于 `SKILL.md` 的 Agent Skill，可供支持这一结构的 AI 工具使用。它按需搜索 GitHub 上的真实项目，核对项目用途、安装入口、许可证和使用门槛，再根据你的目标生成内容。它不需要维护项目数据库，也不要求你先上传自己的帖子来训练写作风格。

## 能做什么

- **自动找项目**：从 GitHub 实时获取候选仓库，支持 AI、开源硬件、实用工具及更细的主题，也可以按你给定的关键词搜索。
- **核对后再推荐**：检查仓库 README 和官方文档，说明项目能做什么、如何开始、许可证、近期活动，以及 API、费用、系统或硬件要求。搜索排名和 Star 数不会直接当作质量保证。
- **写六条独立短帖**：默认从 AI、开源硬件、实用工具各选 2 个项目。每条只讲一个项目，用具体的开头吸引读者，几句话说清亮点、必要限制和仓库链接。你指定主题或数量时，以你的要求为准。
- **写一篇图文长文**：先给你 6 个简短的项目方向及仓库链接；你选中一个后，再写包含前提条件、操作步骤、预期结果和常见问题的长文。
- **准备真实配图**：优先使用你提供的图片，或从项目官方仓库寻找截图、设备照片等素材。每张候选图都要检查内容、清晰度和来源；不能把生成的示意图冒充产品截图。
- **使用内置的自然口吻**：自动选择适合项目的中文表达，也可以指定「随口发现」「直给推荐」「问题切入」「拆开讲清」「审慎评估」或「动手笔记」。不需要上传写作样本。只有实际动手验证过，才会使用亲测口吻。

> Skill 负责发现、核对和起草。发布到 X 由你审阅后决定；它不会自动替你发帖。

## 安装

需要支持 `SKILL.md` 和脚本运行的 AI 工具、Python 3，以及访问 GitHub 的网络连接。项目搜索和仓库图片收集脚本只使用 Python 标准库。

下载本仓库，保留 `SKILL.md`、`references/` 和 `scripts/` 的相对位置，然后按使用的平台安装：

| 平台 | 安装方式 | 调用方式 |
| --- | --- | --- |
| Codex | 放入 `~/.codex/skills/repo-share/`；设置了 `CODEX_HOME` 时使用其中的 `skills` 目录 | 在对话中使用 `$repo-share` |
| Claude Code | 放入 `~/.claude/skills/repo-share/`，或项目的 `.claude/skills/repo-share/` | 使用 `/repo-share` 或描述任务 |
| Claude 聊天 | 将 `repo-share` 文件夹打包为 ZIP，在 Claude 的 Skills 页面上传并启用 | 描述任务，让 Claude 调用该 Skill |
| WorkBuddy | 按 WorkBuddy 的 Skill 导入流程添加包含 `SKILL.md` 的技能包 | 安装后在对话中调用 |

不同平台对脚本执行、联网和图片查看的权限可能不同。如果环境无法运行 Python 或访问 GitHub，实时搜索与自动收集图片就无法完整工作。WorkBuddy 开放平台上架还可能要求额外的展示信息；本仓库的 Skill 包不代表已在其市场上架。

## 怎么用

直接描述你想找的项目或想写的内容，例如：

```text
使用 $repo-share，找 6 个值得分享的开源项目，给我写成独立的 X 短帖。
```

```text
使用 $repo-share，只找本地运行的 AI 工具，先给我 6 个长文方向和仓库链接。
```

```text
使用 $repo-share，介绍一个开源硬件项目，写成适合 X Article 的详细图文教程，口吻用「拆开讲清」。
```

只想找项目、不写 X 内容也可以：

```text
使用 $repo-share，帮我找几个适合初学者的开源智能家居项目，说明安装门槛和许可证。
```

## 内容流程

1. **搜索候选项目**：根据主题调用 GitHub 搜索；默认短帖批次按 AI、开源硬件、实用工具各 2 个来选。
2. **核对项目资料**：AI 助手阅读原仓库和官方资料，排除不相关或信息不足的项目，并明确未验证的部分；你不用逐个挑选项目。
3. **选择内容形式**：短帖写成 6 条互相独立的帖子；长文先展示 6 个纯文字方向，等你选定后再继续。
4. **写作与配图**：用适合项目的口吻写草稿；短帖对应一张真实图片，长文按内容需要安排多张图片，并记录来源。
5. **交给你审阅**：你可以修改文字、换图，再自行决定是否发布。

如果项目没有可用的真实图片，短帖流程会寻找替代项目；长文会说明哪些步骤缺少可用图片。无法实际运行的硬件或软件步骤会明确标为依据官方资料整理，不会写成亲测经历。

## 可选：直接运行搜索脚本

在仓库目录中运行：

```bash
python scripts/discover.py --category all --limit 12
python scripts/discover.py --category ai-agents --limit 10
python scripts/discover.py --query "self hosted" --limit 10
```

搜索脚本返回候选项目的 JSON 信息；它只是发现入口，最终推荐仍需核对原仓库。可设置 `GITHUB_TOKEN` 提高 GitHub API 的请求额度，不要把令牌写入仓库或分享给他人。

从某个仓库的 README 收集图片候选：

```bash
python scripts/collect_images.py owner/repo --output images
```

脚本会保存候选图片及来源清单。下载成功不等于图片适合使用；仍需查看图片内容和相关授权说明。

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Skill 的入口、项目发现与核对规则 |
| [`references/x-writing.md`](references/x-writing.md) | X 短帖、长文和配图流程 |
| [`references/voice-presets.md`](references/voice-presets.md) | 可直接使用的中文写作口吻 |
| [`scripts/discover.py`](scripts/discover.py) | GitHub 项目候选搜索 |
| [`scripts/collect_images.py`](scripts/collect_images.py) | 仓库 README 图片候选收集 |

目前内置脚本只搜索 GitHub。若你指定 GitLab、Gitee 等来源，具备网页检索能力的 AI 助手可以另外检索并标明来源，但这些来源不在脚本的自动搜索范围内。
