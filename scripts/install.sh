#!/usr/bin/env bash
# Install gaishi for a specific tool.
#   scripts/install.sh <tool> [--project DIR]
# Tools with native SKILL.md support install to the user dir by default (or DIR with --project);
# rule-file tools (cursor, windsurf, cline, copilot, agents-md) always install into a project (default: cwd).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOL="${1:-}"; shift || true
PROJECT=""
while [ $# -gt 0 ]; do
  case "$1" in
    --project) PROJECT="${2:?--project needs a directory}"; shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

put_skill() { # <skills-dir>
  mkdir -p "$1"; rm -rf "$1/gaishi"; cp -R "$REPO/skills/gaishi" "$1/gaishi"; echo "installed skill -> $1/gaishi"
}
put_rule() { # <src> <dest-file>
  mkdir -p "$(dirname "$2")"; cp "$REPO/$1" "$2"; echo "installed rule  -> $2"
}
skill_dir() { # <user-dir> <project-subdir>
  if [ -n "$PROJECT" ]; then echo "$PROJECT/$2"; else echo "$1"; fi
}
P="${PROJECT:-$PWD}"

case "$TOOL" in
  claude)   put_skill "$(skill_dir "$HOME/.claude/skills" .claude/skills)" ;;
  codex)    put_skill "$(skill_dir "$HOME/.agents/skills" .agents/skills)" ;;
  opencode) put_skill "$(skill_dir "$HOME/.config/opencode/skills" .opencode/skills)" ;;
  cursor)   put_rule rules/cursor/gaishi.mdc "$P/.cursor/rules/gaishi.mdc" ;;
  windsurf) put_rule rules/windsurf/gaishi.md "$P/.windsurf/rules/gaishi.md" ;;
  cline)    put_rule rules/cline/gaishi.md "$P/.clinerules/gaishi.md" ;;
  copilot)  put_rule rules/copilot/gaishi.instructions.md "$P/.github/instructions/gaishi.instructions.md" ;;
  agents-md)
    if grep -qs "Generated from skills/gaishi/SKILL.md" "$P/AGENTS.md"; then
      echo "AGENTS.md already contains gaishi; skipping"
    else
      { [ -s "$P/AGENTS.md" ] && printf '\n'; cat "$REPO/rules/agents-md/gaishi.md"; } >> "$P/AGENTS.md"
      echo "appended to $P/AGENTS.md"
    fi ;;
  *)
    echo "usage: $0 {claude|codex|opencode|cursor|windsurf|cline|copilot|agents-md} [--project DIR]" >&2
    echo "Gemini CLI: gemini extensions install https://github.com/takumi-shida/Gaishi" >&2
    exit 2 ;;
esac
