#!/usr/bin/env python3
"""Package a skill folder into a distributable `.skill` archive."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from quick_validate import validate_skill

EXCLUDED_PARTS = {".git", "__pycache__", ".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def should_include(file_path: Path) -> bool:
    if any(part in EXCLUDED_PARTS for part in file_path.parts):
        return False
    if file_path.suffix in EXCLUDED_SUFFIXES:
        return False
    return file_path.is_file()


def package_skill(skill_path: str | Path, output_dir: str | Path | None = None):
    skill_path = Path(skill_path).resolve()

    if not skill_path.exists():
        print(f"❌ Error: skill folder not found: {skill_path}")
        return None
    if not skill_path.is_dir():
        print(f"❌ Error: path is not a directory: {skill_path}")
        return None
    if not (skill_path / "SKILL.md").exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return None

    print("🔍 Validating skill...")
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"❌ Validation failed: {message}")
        return None
    print(f"✅ {message}\n")

    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    archive_path = output_path / f"{skill_path.name}.skill"

    try:
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file_path in skill_path.rglob("*"):
                if not should_include(file_path):
                    continue
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)
                print(f"  Added: {arcname}")
        print(f"\n✅ Successfully packaged skill to: {archive_path}")
        return archive_path
    except Exception as exc:
        print(f"❌ Error creating .skill file: {exc}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/package_skill.py <path/to/skill-folder> [output-directory]")
        print("\nExample:")
        print("  python3 scripts/package_skill.py path/to/my-skill")
        print("  python3 scripts/package_skill.py path/to/my-skill ./dist")
        raise SystemExit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"📦 Packaging skill: {skill_path}")
    if output_dir:
        print(f"   Output directory: {output_dir}")
    print()

    result = package_skill(skill_path, output_dir)
    raise SystemExit(0 if result else 1)


if __name__ == "__main__":
    main()
