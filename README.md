# gaishi

Work in English, report in Japanese — an agent skill for Japanese engineers in global tech.

`gaishi` (外資) makes the agent research, analyze, code, and operate tools in English, then report the final result to you in Japanese. The full policy is in [`skills/gaishi/SKILL.md`](skills/gaishi/SKILL.md).

## Install

`skills/gaishi/` follows the open [Agent Skills](https://agentskills.io/specification) format, so one source works across tools. Install separately for each tool you use.

| Tool | How |
| --- | --- |
| Claude Code | `/plugin marketplace add takumi-shida/Gaishi` then `/plugin install gaishi@gaishi` — or `scripts/install.sh claude` |
| Codex (CLI / app) | Plugin: `.codex-plugin/` + `.agents/plugins/marketplace.json` — or `scripts/install.sh codex` (copies to `~/.agents/skills`) |
| Cursor | Plugin: `.cursor-plugin/` — or rule file: `scripts/install.sh cursor` (`.cursor/rules/gaishi.mdc`) |
| Gemini CLI | `gemini extensions install https://github.com/takumi-shida/Gaishi` |
| OpenCode | `scripts/install.sh opencode` (`~/.config/opencode/skills`) |
| GitHub Copilot | `scripts/install.sh copilot` (`.github/instructions/gaishi.instructions.md`) |
| Windsurf | `scripts/install.sh windsurf` (`.windsurf/rules/gaishi.md`) |
| Cline | `scripts/install.sh cline` (`.clinerules/gaishi.md`) |
| Anything reading `AGENTS.md` | `scripts/install.sh agents-md` (appends to `./AGENTS.md`) |
| Claude.ai | Zip `skills/gaishi` and upload under Settings → Skills |

Tools with native skill support install to your user directory by default; add `--project DIR` to install into a project instead. Rule-file tools always install into a project (default: current directory).

Manifest paths and install commands follow the conventions of popular multi-tool skill repos such as [obra/superpowers](https://github.com/obra/superpowers) and [anthropics/skills](https://github.com/anthropics/skills). Codex/Cursor/Gemini/Copilot behavior was not tested against the real tools; please report anything that doesn't load.

## Why it works (and when it doesn't)

Working in English saves tokens on the agent's own notes and instructions. For coding, evidence of an accuracy gain is weak; the gain is clearer for language-heavy steps such as research. Anything shipped to end users (UI copy, page text, slide text) is written in Japanese directly, never drafted in English and translated. Papers, measurements, limits, and what is still unverified are in [`docs/evidence.md`](docs/evidence.md) (Japanese).

## Usage

Ask in Japanese and mention it, e.g. 「gaishi モードでこのバグを調査して」. Tools that load skills on demand activate it from the description; rule-file tools apply it when the model decides it is relevant.

## Repository layout

```
skills/gaishi/SKILL.md      source of truth (Agent Skills format)
skills/gaishi/references/  on-demand checklist for Japanese text in HTML/slides
.claude-plugin/             Claude Code plugin + marketplace
.codex-plugin/              Codex plugin
.agents/plugins/            Codex marketplace
.cursor-plugin/             Cursor plugin
gemini-extension.json      Gemini CLI extension (loads GEMINI.md -> SKILL.md)
rules/                      generated rule files for Cursor, Windsurf, Cline, Copilot, AGENTS.md
scripts/sync.py             regenerate rules/, validate spec + version consistency (--check in CI)
scripts/install.sh          per-tool installer
```

## Development

```bash
python3 scripts/sync.py          # regenerate rules/ after editing SKILL.md
python3 scripts/sync.py --check  # what CI runs
```

## License

MIT
