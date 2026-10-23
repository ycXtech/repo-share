# Ready-to-use Chinese writing voices

These are reusable writing approaches distilled from public first-person tech writing and project curation. They are not copies of any author's distinctive voice. Never use a real person's name as a style label, borrow recognizable wording, or imply that the user personally tested a project.

## Select without setup

Choose a voice after verifying the source. The user does not need to upload posts, create a profile, or answer another question. For X short posts, use the user's confirmed seven-paragraph pattern below unless they ask for another format. A long Article should have one coherent dominant voice while keeping its tutorial steps precise.

## Default X short-post style

The user confirmed a specific X-post style and presentation using a Make Maia example. Follow its **seven short paragraphs**, separated by blank lines:

1. Open with a plain-language tension as a question, usually “AI 越来越……，但……吗？”. Make it about the reader's work or judgment, not an announcement headline.
2. Introduce one verified project or update conversationally: “最近看到……”. Do not invent first-hand use.
3. Explain **one** distinctive mechanism in a single short paragraph. Keep only the detail needed to understand the idea.
4. Add one brief human reaction on its own line, in the spirit of “这个设计挺有意思。” Avoid marketing praise.
5. Zoom out to a familiar trend or behavior in one short sentence, such as what AI now makes faster or easier.
6. Turn the update into a deeper, concrete question about understanding, trust, ownership, reliability, or another tension genuinely supported by the source.
7. End with a short invitation to discuss, such as “你们怎么看？”, followed in the same paragraph by 1–2 X hashtags that directly name the post's project, technology, or specific topic. Choose different tags for different posts; avoid generic or unrelated trending tags.

Keep the language natural and easy to read aloud. The short post is an observation with one idea, not a feature list, mini briefing, tutorial, or sales pitch. Include a necessary caveat in the body when omitting it would mislead. For a batch, keep this paragraph rhythm while changing the topic-specific questions and observations; do not copy the same hook verbatim across posts.

**Output form:** Put each complete X post in its own ChatGPT writing block, using `:::writing{variant="social_post" id="<unique five-digit id>"}` on the opening line and `:::` on the closing line. No heading, source, image, explanation, or Markdown code fence goes inside the writing block. Put the verified official URL and any image credit immediately **below** that block as separate notes. When the client does not render writing blocks, still emit this syntax rather than replacing the requested form with a code block or ordinary chat paragraph. Do not claim the UI rendered it unless observable.

Before delivery, check that the seven beats are present, each paragraph is short, and every independent post has its own relevant hashtags inside the copyable writing block. If it sounds like a changelog, press release, or dense specification summary, rewrite around the reader-facing tension. Check X's actual composer count before claiming a post fits; do not rely only on raw character count.

## Topic angles within the confirmed format

Use these angles to choose the central tension; they do not replace the seven-paragraph short-post structure. For a long Article, use the article column instead.

| Voice | Short post | Long Article |
| --- | --- | --- |
| **随口发现** | Lead with a genuinely surprising project detail, then explain why someone might care in conversational Chinese. A light aside is fine when supported by facts. | Start with the interesting detail; move quickly to what the reader can actually do. |
| **直给推荐** | Say who the tool helps and what concrete job it does. Keep the link and relevant restriction easy to spot. No generic praise. | Brief orientation followed by clear prerequisites, steps, and results. |
| **问题切入** | Open with a real task or friction the project addresses; then connect one verified capability to it. Do not invent the user's own frustration. | Show the problem, why this project fits, and a runnable path through it. |
| **拆开讲清** | Explain one non-obvious mechanism or feature in plain language; avoid jargon without explanation. | Build understanding alongside the steps, using screenshots or diagrams only when they are authentic and relevant. |
| **审慎评估** | State the attraction and the condition under which it is useful. Qualify claims that depend on hardware, an API, cost, or untested performance. | Discuss evidence, trade-offs, who should try it, and where it may disappoint before or after the tutorial. |
| **动手笔记** | Use a concrete step and observed result only if this run actually tested them. Otherwise choose another voice. | Report commands and observations from a real run; distinguish them from steps taken solely from official docs. |

Keep the project-specific hook, real benefit, and material caveat; place the original repository link in the separate source note for short posts. The opening and closing questions should arise from the particular update, while the seven-paragraph shape remains consistent. Do not force a joke, emoji, or first-person claim. Before delivery, remove unsupported superlatives, identical hooks across a batch, and claims of personal use that the user did not provide and this run did not verify.

## Public examples behind the approaches

The following examples informed the general patterns above. Read them as evidence of varied ways real people explain tools; never paste their sentences into a generated draft:

- [Tw93, 潮流周刊第 279 期](https://weekly.tw93.fun/posts/279): conversational curation, a specific observation, and a small qualification when a tool does not fit a use case.
- [阮一峰, 科技爱好者周刊第 378 期](https://www.ruanyifeng.com/blog/2025/12/weekly-issue-378.html): compact descriptions that make a tool's job and platform clear.
- [Julia Evans, TIL notes](https://jvns.ca/til/): concrete learning context, useful examples, and open uncertainty.
- [Simon Willison, Highlighted tools](https://simonwillison.net/2025/Sep/4/highlighted-tools/): practical workflows, precise benefits, and honest rough edges.
- [Dan Luu, We only hire the trendiest](https://danluu.com/programmer-moneyball/): explicit comparisons and attention to what evidence does or does not establish.
- [Tom Dörr, repository post archive](https://tom-doerr.github.io/repo_posts/): very brief, utility-first introductions to repositories.
