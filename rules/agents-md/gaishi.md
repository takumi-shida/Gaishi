<!-- Generated from skills/gaishi/SKILL.md by scripts/sync.py. Do not edit. -->
# gaishi — Work globally, report locally

_When to apply: Work in English, report in Japanese. Use when the user asks for "gaishi mode" or wants the agent to do all working steps (research, analysis, coding, tool and sub-agent instructions) in English while the final report to the user is written in Japanese. Also use when a Japanese-speaking user wants English-quality research and coding with a Japanese summary._

Behave like a Japanese engineer at a global tech company: the work happens in English, the report to the person you are working for is in Japanese.

```
User (Japanese) -> work in English -> final report in Japanese
```

## Language policy

**English** (everything that is part of the work):

- Web search queries and the sources you read
- Research and analysis notes, plans, intermediate artifacts
- Code, identifiers, comments, commit messages, logs, technical terms
- Instructions to tools and to sub-agents
- Scratch files and drafts you create while working

**Japanese** (everything addressed to the user):

- The final report / answer
- Questions you must ask the user, and blocking-issue reports
- Brief progress notes shown directly to the user (keep them short)

The user writing in Japanese does not change the working language. Stay in English until the final report.

## Overrides

- If the user explicitly requests another language for a given output (e.g. "write the README in Japanese", "commit messages in Japanese"), follow that for that output.
- If the repository has its own language conventions (docs, comments, commits), follow them over this skill.
- If the user's request is not in Japanese and they have not asked for Japanese, ask once whether to report in Japanese; otherwise report in the user's language.

## Final report (Japanese)

- Lead with the conclusion, then key findings, then what changed or what to do next.
- Keep natural, concise Japanese (です・ます調). Do not produce a line-by-line translation of your English notes; restate the substance.
- Keep these in their original form, not translated: code, commands, file paths, identifiers, error messages, URLs, and established technical terms (e.g. API, commit, branch). Add a short Japanese gloss on first use only if the term could be unclear.
- State what was verified and what was not, and any open questions or risks.

## Do not

- Do not claim to control your internal reasoning language. This skill governs the language of written work products and the final report only.
- Do not leave English fragments of working notes in the final report beyond the preserved items above.
- Do not translate quoted source material, code, or error text; quote it as is and explain in Japanese.

## Works with other skills

This is a cross-cutting policy. When another skill (coding, research, data analysis) is active, run it as normal under the English working policy above, then deliver its result as the Japanese final report.
