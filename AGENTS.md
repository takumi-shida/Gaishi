# gaishi — Contributor Notes

- `skills/gaishi/SKILL.md` is the single source of truth. Follow the [Agent Skills spec](https://agentskills.io/specification): `name` must match the directory, description <= 1024 chars.
- Files under `rules/` are generated. After editing SKILL.md run `python3 scripts/sync.py`; CI runs `python3 scripts/sync.py --check`.
- Versions live in `SKILL.md` (`metadata.version`) and must match `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, and `gemini-extension.json`. Bump them together.
- Per-tool manifests only point at `skills/`; do not duplicate skill content into them.
