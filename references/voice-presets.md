# Ready-to-use Chinese writing voices

These are reusable writing approaches distilled from public first-person tech writing and project curation. They are not copies of any author's distinctive voice. Never use a real person's name as a style label, borrow recognizable wording, or imply that the user personally tested a project.

## Select without setup

Choose a voice after verifying the source. The user does not need to upload posts, create a profile, or answer another question. For X short posts, default to the conversational, curious style below unless the user asks for another voice. For a batch, vary the angle and cadence instead of repeating the same hook. A long Article should have one coherent dominant voice while keeping its tutorial steps precise.

## Default X short-post style

Write like someone sharing one discovery and a thought with other people, not like a product release summary. The user's preferred shape is: **a specific question or tension → a brief discovery → one concrete, plain-language detail → why it makes the writer think → an open question when it genuinely invites discussion**. This is a writing direction, not a rigid template.

- Give each thought room with short paragraphs and line breaks. Use ordinary words; explain a technical term only if the reader needs it. Select one interesting fact instead of stacking model names, parameter counts, benchmarks, and feature lists.
- Let the hook carry a real idea, such as “AI 写得越来越快，开发者还理解自己提交的代码吗？” Do not start with an announcement-style label or cram all facts into one sentence. Avoid marketing claims, generic praise, and stock phrases.
- A small first-person observation or curiosity can make the post feel human, but never claim the user tested, bought, attended, or personally witnessed something without evidence. Do not force “我在想” or “你们怎么看” into every post; use a closing question only when the topic supports one.
- Deliver the **copyable post body alone**. Put the verified repository or official news URL and image credit **below it as separate source notes**, unless the user explicitly asks for the link inside the post. When useful, suggest quoting the official post or placing the link in the first reply. The source remains visible and clickable to the user without making the post read like a citation list.
- Before delivery, read the text aloud mentally: if it sounds like a changelog, press release, dense specification summary, or a single paragraph followed by a bare URL, rewrite it around the reader-facing idea.

| Voice | Short post | Long Article |
| --- | --- | --- |
| **随口发现** | Lead with a genuinely surprising project detail, then explain why someone might care in conversational Chinese. A light aside is fine when supported by facts. | Start with the interesting detail; move quickly to what the reader can actually do. |
| **直给推荐** | Say who the tool helps and what concrete job it does. Keep the link and relevant restriction easy to spot. No generic praise. | Brief orientation followed by clear prerequisites, steps, and results. |
| **问题切入** | Open with a real task or friction the project addresses; then connect one verified capability to it. Do not invent the user's own frustration. | Show the problem, why this project fits, and a runnable path through it. |
| **拆开讲清** | Explain one non-obvious mechanism or feature in plain language; avoid jargon without explanation. | Build understanding alongside the steps, using screenshots or diagrams only when they are authentic and relevant. |
| **审慎评估** | State the attraction and the condition under which it is useful. Qualify claims that depend on hardware, an API, cost, or untested performance. | Discuss evidence, trade-offs, who should try it, and where it may disappoint before or after the tutorial. |
| **动手笔记** | Use a concrete step and observed result only if this run actually tested them. Otherwise choose another voice. | Report commands and observations from a real run; distinguish them from steps taken solely from official docs. |

These are angles, not fill-in-the-blank templates. Keep the project-specific hook, real benefit, and material caveat; place the original repository link in the separate source note for short posts. Do not force a joke, emoji, rhetorical question, or first-person sentence into every draft. Before delivery, remove stock phrases, unsupported superlatives, repetitive openings, and claims of personal use that the user did not provide and this run did not verify.

## Public examples behind the approaches

The following examples informed the general patterns above. Read them as evidence of varied ways real people explain tools; never paste their sentences into a generated draft:

- [Tw93, 潮流周刊第 279 期](https://weekly.tw93.fun/posts/279): conversational curation, a specific observation, and a small qualification when a tool does not fit a use case.
- [阮一峰, 科技爱好者周刊第 378 期](https://www.ruanyifeng.com/blog/2025/12/weekly-issue-378.html): compact descriptions that make a tool's job and platform clear.
- [Julia Evans, TIL notes](https://jvns.ca/til/): concrete learning context, useful examples, and open uncertainty.
- [Simon Willison, Highlighted tools](https://simonwillison.net/2025/Sep/4/highlighted-tools/): practical workflows, precise benefits, and honest rough edges.
- [Dan Luu, We only hire the trendiest](https://danluu.com/programmer-moneyball/): explicit comparisons and attention to what evidence does or does not establish.
- [Tom Dörr, repository post archive](https://tom-doerr.github.io/repo_posts/): very brief, utility-first introductions to repositories.
