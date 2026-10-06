#!/usr/bin/env python3
"""Generate per-tool rule files from skills/gaishi/SKILL.md and validate the repo.

    python3 scripts/sync.py          # regenerate rules/
    python3 scripts/sync.py --check  # fail if rules/ is stale or any manifest is inconsistent
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "gaishi" / "SKILL.md"
REFS = sorted((ROOT / "skills" / "gaishi" / "references").glob("*.md"))
MANIFESTS = [
    (".claude-plugin/plugin.json", ["version"]),
    (".claude-plugin/marketplace.json", ["plugins", 0, "version"]),
    (".codex-plugin/plugin.json", ["version"]),
    (".cursor-plugin/plugin.json", ["version"]),
    ("gemini-extension.json", ["version"]),
]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_skill():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise SystemExit("SKILL.md: missing YAML frontmatter")
    front, body = m.groups()
    meta = {}
    for line in front.splitlines():
        if re.match(r"^\S", line) and ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    version = re.search(r'^\s+version:\s*"?([^"\n]+)"?', front, re.M)
    meta["_version"] = version.group(1) if version else None
    return meta, body.lstrip("\n")


def validate(meta):
    errors = []
    name, desc = meta.get("name", ""), meta.get("description", "")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"invalid skill name: {name!r}")
    if name != SKILL.parent.name:
        errors.append(f"name {name!r} must match directory {SKILL.parent.name!r}")
    if not 1 <= len(desc) <= 1024:
        errors.append(f"description length {len(desc)} not in 1..1024")
    if not meta.get("_version"):
        errors.append("metadata.version missing")
    for path, keys in MANIFESTS:
        node = json.loads((ROOT / path).read_text(encoding="utf-8"))
        for k in keys:
            node = node[k]
        if node != meta["_version"]:
            errors.append(f"{path}: version {node!r} != SKILL.md {meta['_version']!r}")
    return errors


def outputs(meta, body):
    desc = meta["description"]
    when = f"_When to apply: {desc}_\n\n"
    # Rule-file tools cannot load references/ on demand, so inline them as appendices.
    for ref in REFS:
        body = body.replace(f"read `references/{ref.name}`", "read the appendix at the end of this file")
        text = ref.read_text(encoding="utf-8").strip().replace("\n# ", "\n## ", 1)
        body = body.rstrip("\n") + "\n\n---\n\n" + re.sub(r"^# ", "## Appendix: ", text, count=1) + "\n"
    title, _, rest = body.partition("\n")
    plain = f"{title}\n\n{when}{rest.lstrip(chr(10))}"
    gen = "<!-- Generated from skills/gaishi/SKILL.md by scripts/sync.py. Do not edit. -->\n"
    return {
        # Cursor: agent-requested rule (model decides from the description)
        "rules/cursor/gaishi.mdc": (
            f"---\ndescription: {desc}\nglobs:\nalwaysApply: false\n---\n{gen}{plain}"
        ),
        # Windsurf: model-decision rule
        "rules/windsurf/gaishi.md": (
            f"---\ntrigger: model_decision\ndescription: {desc}\n---\n{gen}{plain}"
        ),
        # Cline: plain rule file
        "rules/cline/gaishi.md": f"{gen}{plain}",
        # GitHub Copilot: path-specific instructions file
        "rules/copilot/gaishi.instructions.md": (
            f'---\napplyTo: "**"\n---\n{gen}{plain}'
        ),
        # AGENTS.md-compatible tools (Codex, OpenCode, Aider, Zed, ...): paste into AGENTS.md
        "rules/agents-md/gaishi.md": f"{gen}{plain}",
    }


def main():
    check = "--check" in sys.argv
    meta, body = parse_skill()
    errors = validate(meta)
    for rel, content in outputs(meta, body).items():
        path = ROOT / rel
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                errors.append(f"{rel}: stale (run python3 scripts/sync.py)")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if errors:
        print("\n".join(f"error: {e}" for e in errors))
        sys.exit(1)
    print("ok" if check else "generated rules/")


if __name__ == "__main__":
    main()
