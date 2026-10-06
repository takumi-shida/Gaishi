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

Why: English text costs fewer tokens than the same content in Japanese, and current models generally perform as well or better when they work in English.

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
