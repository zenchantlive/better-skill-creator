<div align="center">

# Better Skill Creator

**A framework for authoring better skills for AI agents**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![GitHub release](https://img.shields.io/github/v/release/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/releases)
[![GitHub issues](https://img.shields.io/github/issues/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/issues)


</div>

---

## What this repo is for

Better Skill Creator helps an agent or skill author build skills that are:

- **discoverable** — the agent can tell when to use the skill
- **reusable** — generic guidance stays in the skill
- **project-aware** — local setup lives in `project.skill.md`
- **testable** — scripts and workflow assumptions can be validated
- **portable** — the same global skill can be used across many repositories

---

## Core idea: keep global and local separate

A reusable skill should stay reusable.

Do **not** edit the global skill for one repository's local paths, commands, or constraints.

Instead:

- the skill ships `project.skill.md.template`
- a setup agent or user creates `project.skill.md` in the **project root**
- future agents read `project.skill.md` before doing substantial work

This gives you:
- a stable global skill
- a project-local context file
- clean reuse across environments

---

## Recommended architecture levels

Not every skill needs every folder.

### 1. Minimal skill

```text
my-skill/
└── SKILL.md
```

### 2. Reference-backed skill

```text
my-skill/
├── SKILL.md
├── project.skill.md.template
└── references/
```

### 3. Operational skill

```text
my-skill/
├── SKILL.md
├── project.skill.md.template
├── references/
├── scripts/
└── tests/
```

### 4. Resilient operational skill

```text
my-skill/
├── SKILL.md
├── project.skill.md.template
├── references/
├── scripts/
├── tests/
└── self-healing/
```

See [`references/skill-architecture-levels.md`](references/skill-architecture-levels.md).

---

## What belongs where

### `SKILL.md`
Use for:
- trigger conditions
- core workflow
- instructions for when to read references
- instructions to look for `project.skill.md` when local context matters

### `project.skill.md.template`
Use for:
- a template the setup agent can copy into the project as `project.skill.md`
- placeholders for exact commands, paths, constraints, and validation rules

### `project.skill.md`
This file lives in the **project**, not in the skill.

Use it for:
- exact local commands
- repo paths
- output locations
- files that must not be modified
- local guardrails and conventions
- validation requirements
- local examples

### `references/`
Use for heavier or conditional documentation.

### `scripts/`
Use for deterministic repeated operations.

### `tests/`
Use for script validation and smoke tests.

### `self-healing/`
Use only for narrow, low-risk remediation.

---

## Repo contents

```text
better-skill-creator/
├── SKILL.md
├── project.skill.md.template
├── references/
│   ├── behavioral-validation-checklist.md
│   ├── completion-gate.md
│   ├── description-writing.md
│   ├── output-patterns.md
│   ├── project-skill-context.md
│   ├── script-test-conventions.md
│   ├── self-healing-rules.md
│   ├── skill-architecture-levels.md
│   ├── skill-testing.md
│   └── workflows.md
├── scripts/
│   ├── package_skill.py
│   └── quick_validate.py
├── reference-skills/
│   └── release-notes-generator/
└── examples/
    └── release-notes-project/
```

---

## How to use this repo

### 1. Start by thinking, not scaffolding

A good skill should be authored deliberately by the agent or human writing it.

Decide:
- what problem the skill solves
- when it should trigger
- whether project-local context is needed
- whether references/scripts/tests are justified

### 2. Write `SKILL.md`

Make the description say **when to use** the skill.

Tell future agents early in the file to:
- look for `project.skill.md` in the project root
- create it from `project.skill.md.template` if missing
- avoid editing the global skill for local setup

### 3. Add `project.skill.md.template` if local setup matters

If commands, paths, or constraints vary by repository, ship a template.

### 4. Add references and scripts only when earned

If a workflow is repeated or fragile, add references/scripts/tests.

### 5. Validate

Use:

```bash
python3 scripts/quick_validate.py <skill_directory>
python3 scripts/package_skill.py <skill_directory> [output_directory]
```

The validator is dependency-free and also catches a few structural problems such as broken SKILL.md links, stale `project.md` references, and missing script/test pairs.

---

## Recommended references in this repo

- [`references/project-skill-context.md`](references/project-skill-context.md)
- [`references/skill-architecture-levels.md`](references/skill-architecture-levels.md)
- [`references/skill-testing.md`](references/skill-testing.md)
- [`references/script-test-conventions.md`](references/script-test-conventions.md)
- [`references/self-healing-rules.md`](references/self-healing-rules.md)
- [`references/behavioral-validation-checklist.md`](references/behavioral-validation-checklist.md)
- [`references/completion-gate.md`](references/completion-gate.md)
- [`references/description-writing.md`](references/description-writing.md)
- [`references/workflows.md`](references/workflows.md)
- [`references/output-patterns.md`](references/output-patterns.md)

---

## Reference skill

The repo includes a canonical reference skill that demonstrates the full pattern without making the reference skill a prerequisite for understanding the framework:

- [`reference-skills/release-notes-generator/`](reference-skills/release-notes-generator/)
- [`examples/release-notes-project/project.skill.md`](examples/release-notes-project/project.skill.md)

What it shows:
- a reusable global skill
- a shipped `project.skill.md.template`
- a project-local `project.skill.md`
- one deterministic script
- one paired test
- one narrow self-healing script

This reference skill is included as proof and calibration, not as a substitute for a strong root `SKILL.md`.

---

## Dry-run result

Using the revised `SKILL.md` and references as the only guidance, an agent can now get to a coherent operational skill without needing a scaffold generator. The main control-plane logic lives in `SKILL.md`; references provide deeper rules; scripts and tests provide proof.

---

## Important philosophy

This repo is intentionally **not** centered around a scaffold generator.

The agent writing the skill should decide:
- what files are actually needed
- what belongs in the global skill
- what belongs in project-local context
- what is worth testing
- whether self-healing is appropriate

Templates and validation can help, but they should not replace judgment.

---

## Contributing

Contributions are welcome, especially improvements to:
- skill structure guidance
- `project.skill.md` patterns
- testing guidance
- worked examples
- validation logic

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE.txt](LICENSE.txt).
