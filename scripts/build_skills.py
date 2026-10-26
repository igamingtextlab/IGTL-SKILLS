#!/usr/bin/env python3
"""
Validate and package every skill in this repo into dist/<release-file>.skill.

Usage (from the repo root):
    python scripts/build_skills.py            # validate + build all skills
    python scripts/build_skills.py --check    # validate only, build nothing

A skill = a top-level folder that contains SKILL.md.
Every skill folder must be listed in SKILLS below (folder -> release file name).
No third-party dependencies; works on Windows, macOS, Linux (Python 3.8+).
"""

import fnmatch
import re
import sys
import zipfile
from pathlib import Path

# Registry: skill folder name -> file name attached to GitHub releases.
# Keep in sync with the "Skills registry" table in CLAUDE.md.
# NEVER rename an existing release file: README download links depend on it.
SKILLS = {
    "igaming-ai-humanizer": "iGamingTextLab-ai-humanizer.skill",
    "igtl-geo-germany": "iGamingTextLab-geo-germany.skill",
    "igtl-geo-uk": "iGamingTextLab-geo-uk.skill",
}

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
EXCLUDE_DIRS = {"__pycache__", "node_modules", ".git"}
ROOT_EXCLUDE_DIRS = {"evals"}
ROOT_EXCLUDE_FILES = {"README.md"}  # GitHub landing page for the skill, not part of the skill
EXCLUDE_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}
EXCLUDE_GLOBS = {"*.pyc", "*~", "*.swp"}


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser for flat `key: value` pairs."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not m:
        return None
    data, current = {}, None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line[0] in " \t" and current:  # continuation / nested (metadata)
            data[current] = (str(data[current]) + " " + line.strip()).strip()
            continue
        if ":" not in line:
            raise ValueError(f"cannot parse frontmatter line: {line!r}")
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key] = value
        current = key
    return data


def validate(folder):
    errors = []
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md not found"]

    nested = [p for p in folder.rglob("SKILL.md") if p != skill_md
              and not any(part in EXCLUDE_DIRS for part in p.relative_to(folder).parts)]
    if nested:
        errors.append(f"extra SKILL.md files (only one allowed): {[str(p) for p in nested]}")

    text = skill_md.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(text)
    except ValueError as e:
        return [str(e)]
    if fm is None:
        return ["no valid YAML frontmatter (file must start with ---)"]

    extra = set(fm) - ALLOWED_KEYS
    if extra:
        errors.append(f"unexpected frontmatter keys: {sorted(extra)}")

    name = fm.get("name", "").strip()
    desc = fm.get("description", "").strip()
    if not name:
        errors.append("missing 'name'")
    else:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"name '{name}' must be kebab-case, max 64 chars")
        if name != folder.name:
            errors.append(f"name '{name}' must equal folder name '{folder.name}'")
    if not desc:
        errors.append("missing 'description'")
    else:
        if len(desc) > 1024:
            errors.append(f"description too long ({len(desc)} > 1024 chars)")
        if "<" in desc or ">" in desc:
            errors.append("description cannot contain < or >")
    return errors


def excluded(rel):
    parts = rel.parts
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if len(parts) > 1 and parts[1] in ROOT_EXCLUDE_DIRS:
        return True
    if len(parts) == 2 and parts[1] in ROOT_EXCLUDE_FILES:
        return True
    return rel.name in EXCLUDE_FILES or any(fnmatch.fnmatch(rel.name, g) for g in EXCLUDE_GLOBS)


def build(folder, out_name):
    DIST.mkdir(exist_ok=True)
    out = DIST / out_name
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(folder.rglob("*")):
            if not f.is_file():
                continue
            rel = f.relative_to(folder.parent)  # keep <folder>/ as the zip root
            if excluded(rel):
                continue
            z.write(f, rel.as_posix())
            count += 1
    return out, count


def main():
    check_only = "--check" in sys.argv
    found = sorted(p.name for p in ROOT.iterdir()
                   if p.is_dir() and (p / "SKILL.md").exists())
    failed = False

    unregistered = [f for f in found if f not in SKILLS]
    missing = [f for f in SKILLS if f not in found]
    if unregistered:
        print(f"ERROR: skill folders not in SKILLS registry: {unregistered}")
        failed = True
    if missing:
        print(f"ERROR: registry lists folders that don't exist: {missing}")
        failed = True

    for folder_name in found:
        errs = validate(ROOT / folder_name)
        if errs:
            failed = True
            print(f"FAIL  {folder_name}")
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"OK    {folder_name}")

    if failed:
        print("\nValidation failed; nothing built.")
        sys.exit(1)
    if check_only:
        return

    print()
    for folder_name in found:
        out, n = build(ROOT / folder_name, SKILLS[folder_name])
        print(f"BUILT dist/{out.name}  ({n} files, {out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
