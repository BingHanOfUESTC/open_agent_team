#!/usr/bin/env python3
"""Minimal structure validator for generated agent skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_skill.py <skill_dir>", file=sys.stderr)
        return 2

    skill_dir = Path(argv[1])
    skill_md = skill_dir / "SKILL.md"
    errors: list[str] = []

    if not skill_dir.exists() or not skill_dir.is_dir():
        errors.append(f"not a directory: {skill_dir}")
    if not skill_md.exists():
        errors.append("missing SKILL.md")
    else:
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("missing YAML frontmatter start")
        match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            errors.append("missing YAML frontmatter block")
        else:
            frontmatter = match.group(1)
            if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
                errors.append("frontmatter missing name")
            if not re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE):
                errors.append("frontmatter missing description")
            desc = re.search(r"^description:\s*(.+)", frontmatter, re.MULTILINE)
            if desc and len(desc.group(1).strip()) < 40:
                errors.append("description is probably too short for reliable routing")
        body = text[match.end():] if match else text
        if "Gotcha" not in body and "gotcha" not in body and "Failure" not in body:
            errors.append("body should include gotchas or failure modes")
        if len(body.splitlines()) > 500:
            errors.append("SKILL.md body is over 500 lines; consider references/")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
