#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location

New Dynamic Skill Structure:
    skill-name/
    ├── SKILL.md (required)
    ├── project.md (project-specific template)
    ├── scripts/
    │   ├── script1.sh
    │   └── script1.sh (paired test)
    ├── tests/
    │   ├── test_script1.sh
    │   └── test_script2.sh
    └── self-healing/
        ├── heal_script1.sh
        └── heal_script2.sh
"""

import sys
import os
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Quick Start

[TODO: How to use this skill]

## Structure

This skill follows the dynamic skill architecture:

### project.md
Contains project-specific details. Other agents in different environments read this to understand how to use the skill in their context. Edit this file to add environment-specific configurations.

### scripts/
Executable scripts paired with tests. Each script should have a corresponding test in tests/.

### tests/
Test scripts that validate the main scripts. If tests fail, run self-healing scripts.

### self-healing/
Scripts that fix common issues. Triggered when tests fail.

## Usage

1. Read project.md to understand environment specifics
2. Run tests/ to verify setup
3. If tests fail, run self-healing/ scripts
4. Execute scripts/ as needed
"""

PROJECT_MD_TEMPLATE = """# Project Specifics

This file contains project-specific details for this skill.

**Purpose:** Any agent trying to use this skill in a different environment should read this file to understand how to use it correctly in their context.

## Environment Details

### Package Manager
[TODO: What package manager does this project use? (npm, pip, cargo, etc.)]

### Dependencies
[TODO: List key dependencies]

### Environment Variables
[TODO: What env vars are needed?]

### Potential Issues
[TODO: What issues might arise in different environments?]

## Customizations

[Add any project-specific customizations here]
"""

EXAMPLE_SCRIPT = '''#!/bin/bash
# Example script for {skill_name}
# Paired with: tests/test_example.sh

echo "Running {skill_name} script..."

# TODO: Add actual script logic here
# This script should be paired with a test in tests/
'''

EXAMPLE_TEST = '''#!/bin/bash
# Test script for example.sh
# If this fails, run self-healing/heal_example.sh

source "$(cd "$(dirname "$0")/.." && pwd)/scripts/example.sh" 2>/dev/null

# TODO: Add test assertions
# Example:
# if command -v example &> /dev/null; then
#     echo "PASS: example command exists"
# else
#     echo "FAIL: example command not found"
#     exit 1
# fi

echo "Tests passed for {skill_name}"
'''

EXAMPLE_HEAL = '''#!/bin/bash
# Self-healing script for {skill_name}
# Run this if tests fail

echo "Running self-heal for {skill_name}..."

# TODO: Add healing logic
# This should fix common issues that cause tests to fail

echo "Self-heal complete"
'''


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with dynamic skill template.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md from template
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create project.md
    project_md_path = skill_dir / 'project.md'
    try:
        project_md_path.write_text(PROJECT_MD_TEMPLATE)
        print("✅ Created project.md (template)")
    except Exception as e:
        print(f"❌ Error creating project.md: {e}")
        return None

    # Create directory structure
    try:
        # Create scripts/ directory
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        
        # Create scripts/example.sh
        example_script = scripts_dir / 'example.sh'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("✅ Created scripts/example.sh")
        
        # Create tests/ directory
        tests_dir = skill_dir / 'tests'
        tests_dir.mkdir(exist_ok=True)
        
        # Create tests/test_example.sh
        example_test = tests_dir / 'test_example.sh'
        example_test.write_text(EXAMPLE_TEST.format(skill_name=skill_name))
        example_test.chmod(0o755)
        print("✅ Created tests/test_example.sh")
        
        # Create self-healing/ directory
        healing_dir = skill_dir / 'self-healing'
        healing_dir.mkdir(exist_ok=True)
        
        # Create self-healing/heal_example.sh
        heal_script = healing_dir / 'heal_example.sh'
        heal_script.write_text(EXAMPLE_HEAL.format(skill_name=skill_name))
        heal_script.chmod(0o755)
        print("✅ Created self-healing/heal_example.sh")

    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # Print next steps
    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nDynamic skill structure created:")
    print("  ├── SKILL.md       # Main skill definition")
    print("  ├── project.md     # Project-specific template")
    print("  ├── scripts/       # Executable scripts")
    print("  ├── tests/         # Test scripts (paired with scripts)")
    print("  └── self-healing/ # Healing scripts (triggered on test failure)")
    print("\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print("2. Edit project.md with project-specific details")
    print("3. Replace example scripts with actual skill scripts")
    print("4. Update tests/ to validate your scripts")
    print("5. Update self-healing/ scripts to fix common issues")
    print("6. Run package_skill.py when ready")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\nSkill name requirements:")
        print("  - Hyphen-case identifier (e.g., 'data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 40 characters")
        print("  - Must match directory name exactly")
        print("\nDynamic Skill Structure:")
        print("  skill-name/")
        print("  ├── SKILL.md")
        print("  ├── project.md")
        print("  ├── scripts/")
        print("  ├── tests/")
        print("  └── self-healing/")
        print("\nExamples:")
        print("  init_skill.py my-new-skill --path skills/public")
        print("  init_skill.py my-api-helper --path skills/private")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print()

    result = init_skill(skill_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
