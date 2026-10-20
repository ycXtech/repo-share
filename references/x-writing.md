# X drafts from verified projects

Use the discovery and verification rules in `../SKILL.md`. Produce user-reviewable drafts and image files; X publishing is a separate action. Six is the default batch size. Obey a user-specified theme or count instead of the default AI 2 / open hardware 2 / practical tools 2 split.

## Writing voice

Read [voice-presets.md](voice-presets.md) before writing short posts or the selected Article. Use its conversational default for short posts unless the user asks for another voice. Its built-in voices work without user samples; do not add a style-selection question to the normal workflow. When a user says “像我平时说话” without giving examples, do not claim to know their unique personal style. Apply any corrections they give to later drafts.

## Six independent short posts

1. Verify six different repositories and their practical appeal. Each post covers exactly one project and stands alone; do not turn the batch into a thread.
2. For each post, start with a project-specific question or tension, then introduce the project in plain language, explain one distinctive mechanism or use, and connect it to a human observation or discussion question. Use short paragraphs. Include a material constraint naturally when it changes the point. Leave installation steps and specification lists to Article mode.
3. Aim for an ordinary X post length. Check the actual X composer character count before publishing, especially with Chinese text, links, and emoji; do not claim a draft fits solely from raw string length.
4. Pair each post with one relevant, real image. A software project calls for an actual interface or output screenshot; open hardware calls for an official device, prototype, or demo photo. Accept a user-provided image when its content and usage rights fit, and retain its source as “user-provided.” Otherwise use the image workflow below. Replace a project when no usable image can be found.
5. Show six separate, cleanly copyable post bodies. Put each original repository URL and image source beneath its body as labeled notes, outside the text to copy, unless the user asks for links in the post. Show matching image previews or clickable local image files. Save text plus images when the environment supports files. Let the user make final edits.

## X Article: two stages

**Stage 1 — choose a direction.** Verify six candidate projects. Present exactly six concise, text-only descriptions, each with its original repository URL. Do not collect or show images yet. Ask the user which one interests them; wait for their choice.

**Stage 2 — draft the selected Article.** Recheck the chosen project's current official instructions. Write one long, useful article in this order: project-specific hook → problem it solves → prerequisites and material costs, API, or hardware requirements → actual installation and use steps → expected result → common issues and limitations → original repository URL. Explain commands, configuration, and expected observations so a reader can follow them. Test the key steps in a temporary environment when feasible. For hardware or anything that cannot reasonably be run, follow the official guide and explicitly mark the steps as untested. Never imply hands-on verification when none happened.

Place multiple relevant, real images next to the introduction and steps they illustrate. Use a user-provided image when appropriate. Include an image/source map and say what each image depicts. A cover plus step images is usually useful; choose the count based on what the actual project can support instead of inserting filler. Show the article in a copyable format, with local image files or usable links the user can insert into X Articles.

## Image workflow

1. If the user supplies images, inspect each and match it to a specific project and claim. Do not treat an unrelated image as evidence.
2. For official repository media, locate the script relative to the parent `SKILL.md` and run `python <skill-directory>/scripts/collect_images.py owner/repo --output <draft-folder>/images` (repeat for selected projects). It downloads likely screenshots/photos embedded in the repository README from GitHub-hosted media and writes a per-repository manifest with original URLs. The helper's score and successful download are only candidate selection, not visual approval.
3. Open every candidate image and check that it depicts the right project, is legible, and is useful for this post or step. Check original context and attribution. Reject badges, icons, generic stock art, misleading mockups, unreadable images, and images with unclear reuse terms.
4. If the README lacks suitable media, inspect the project's official docs or publicly available demo. Capture an authentic screenshot with the available browser/computer tool when permitted, recording its page URL and capture date. Do not fabricate a product screenshot or use a generated illustration as product evidence.
5. Confirm the chosen local file opens, is a format X can accept, and belongs to the correct draft. Do not merely paste an external image URL and call it a verified attachment. If no suitable image remains, replace the short-post project; for an Article, tell the user exactly which steps cannot be illustrated instead of inventing images.

For every externally sourced image, keep a source link and a short description. Credit and reuse conditions may vary by repository; inspect relevant license or media notes rather than assuming that the code license covers every image. Do not automatically upload, post, or send these drafts to anyone.
