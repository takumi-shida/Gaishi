---
trigger: model_decision
description: Work in English, report in Japanese. Use when the user asks for "gaishi mode" or wants the agent to do all working steps (research, analysis, coding, tool and sub-agent instructions) in English while the final report to the user is written in Japanese. Also use when a Japanese-speaking user wants English-quality research and coding with a Japanese summary.
---
<!-- Generated from skills/gaishi/SKILL.md by scripts/sync.py. Do not edit. -->
# gaishi — Work globally, report locally

_When to apply: Work in English, report in Japanese. Use when the user asks for "gaishi mode" or wants the agent to do all working steps (research, analysis, coding, tool and sub-agent instructions) in English while the final report to the user is written in Japanese. Also use when a Japanese-speaking user wants English-quality research and coding with a Japanese summary._

Behave like a Japanese engineer at a global tech company: the work happens in English, the report to the person you are working for is in Japanese.

```
User (Japanese) -> work in English -> final report in Japanese
```

Why: English text usually costs fewer tokens than the same content in Japanese (the gap is smaller on newer tokenizers), and current models are generally at least as accurate when they work in English. For coding the accuracy gain is small; the main benefit is lower token use on the agent's own notes and instructions.

## Language policy

**English** (everything that is part of the work):

- Web search queries and the sources you read
- Research and analysis notes, plans, intermediate artifacts
- Code, identifiers, comments, commit messages, logs, technical terms
- Instructions to tools and to sub-agents
- Tool arguments: option values, enum values, identifiers, and search parameters stay in English or their original language-neutral form. Never translate them into Japanese.
- Scratch files and drafts you create while working

**Japanese** (everything addressed to the user):

- The final report / answer
- Questions you must ask the user, and blocking-issue reports
- Brief progress notes shown directly to the user (keep them short)

The user writing in Japanese does not change the working language. Stay in English until the final report.

## Keep Japanese-native material in Japanese

Do not translate material whose meaning depends on the Japanese original. Work on it as Japanese, then explain the result in your English notes and the Japanese report.

- Text the task is about: Japanese strings under test, UI copy, user data, documents to summarize or proofread, legal, business, or cultural content specific to Japan
- Search queries aimed at Japanese-language sources (Japanese sites, laws, local services). Search in Japanese there; use English for everything else.
- Ambiguous or domain-specific Japanese terms in the user's request: keep the original in parentheses the first time you note it in English (e.g. `settlement (精算)`), so nothing is lost in translation.

## Deliverables

Work product that ships to end users is not "working text". Write it in the audience language (normally Japanese when the user's request is in Japanese), directly and from the start. Never draft it in English and translate afterwards.

- Examples: UI copy, HTML page text, slide text, documents, alt text, user-facing error messages.
- Code, identifiers, class names, file names, and code comments stay in English.
- For HTML, slides, or any visual output containing Japanese, read the appendix at the end of this file and check the result by rendering it, not just by reading the code.

## Overrides

- If the user explicitly requests another language for a given output (e.g. "write the README in Japanese", "commit messages in Japanese"), follow that for that output.
- If the repository has its own language conventions (docs, comments, commits), follow them over this skill.
- If the user's request is not in Japanese and they have not asked for Japanese, ask once whether to report in Japanese; otherwise report in the user's language.

## Final report (Japanese)

- Lead with the conclusion, then key findings, then what changed or what to do next.
- Keep it concise. Japanese costs more tokens than the same content in English, so report the substance, not the process.
- Write natural Japanese (です・ます調). Do not produce a line-by-line translation of your English notes; restate the substance.
- Write the whole report in Japanese. Do not let English sentences or the wrong script slip in, apart from the items below.
- Keep these in their original form, not translated: code, commands, file paths, identifiers, error messages, URLs, and established technical terms (e.g. API, commit, branch). Add a short Japanese gloss on first use only if the term could be unclear.
- State what was verified and what was not, and any open questions or risks.

## Do not

- Do not claim to control your internal reasoning language. This skill governs the language of written work products and the final report only. Forcing a model to think in a particular language can lower accuracy.
- Do not leave English fragments of working notes in the final report beyond the preserved items above.
- Do not translate quoted source material, code, or error text; quote it as is and explain in Japanese.

## Works with other skills

This is a cross-cutting policy. When another skill (coding, research, data analysis) is active, run it as normal under the English working policy above, then deliver its result as the Japanese final report.

---

## Appendix: Japanese text in HTML, slides, and other visual deliverables

Read this when the deliverable (web page, UI, slide deck, document, image text) contains Japanese text. It is a checklist, not a style guide.

## Write the copy in the audience language, directly

- Write on-screen text (headings, body, buttons, slide bullets, alt text) in Japanese from the start. Do not draft it in English and translate afterwards: translation changes text length and breaks layouts that were sized for the English copy.
- Keep code, class names, ids, file names, and code comments in English.
- If the audience language is not stated, use the language of the user's request and say which one you assumed in the report.

## HTML / CSS

- `<html lang="ja">` and `<meta charset="utf-8">`. For mixed-language pages, mark non-Japanese spans with their own `lang`.
- Font stack with Japanese fallbacks, Latin first only if you want Latin glyphs from it, e.g. `font-family: system-ui, "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Noto Sans JP", "Yu Gothic", Meiryo, sans-serif;`. Never rely on a single font that lacks kana/kanji.
- Japanese has no spaces between words. Do not use `white-space: nowrap` or fixed widths on text that may grow; allow wrapping (`overflow-wrap: anywhere` for long unbroken strings).
- Use `line-height` of about 1.6–1.9 for body text; CJK needs more than Latin.
- Line breaking: the default `word-break: normal` already follows kinsoku rules in modern browsers. `word-break: auto-phrase` breaks at phrase boundaries but is not supported everywhere; use it as progressive enhancement only.
- JavaScript: do not pass non-ASCII strings to `btoa`/`atob` directly; encode as UTF-8 first.

## Slides (HTML, PPTX, PDF)

- Budget text by display width: full-width characters take about one em each. A line that fits 60 Latin characters fits roughly 30 Japanese ones.
- Keep headings short; prefer fewer, shorter bullets over shrinking fonts below a readable size.
- Set an explicit East Asian font (e.g. Noto Sans JP, Yu Gothic, Meiryo) for the deck theme; otherwise renderers substitute inconsistently.
- Text frames must not overflow their shapes; shorten the copy before reducing font size.

## Verify by rendering

Reading the code does not show overflow, tofu (missing glyphs), or bad line breaks. Render the result (headless browser screenshot, or export the slides to images) and look at it before reporting. Report any page or slide you could not render.

## Other Japanese-text pitfalls in code

- Encoding: UTF-8 everywhere, including file I/O and HTTP headers.
- Width: terminal and table alignment must account for full-width characters (East Asian Width). Variation selectors take no columns, and Python's `len()` counts code points, not display width.
- Normalization: choose NFC or NFKC deliberately. NFKC merges compatibility ideographs (e.g. U+FA19 and U+795E) and so can alter text that was only supposed to be reformatted; full-width and half-width forms also differ. Do not normalize text you only display or reformat.
- Sorting and searching: do not assume byte or code-point order matches Japanese reading order.
