<div align="center">

# Better Skill Creator

**Treat Agent Skills like Production Applications**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![GitHub release](https://img.shields.io/github/v/release/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/releases)
[![GitHub issues](https://img.shields.io/github/issues/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/issues)

*A framework for building project-aware, rigorously tested, self-healing skills that can survive real operational use.*

</div>

---

## Why this exists

Most skills are written like notes.

The good ones behave more like software.

They know when to activate. They route an agent through the right references. They carry scripts for deterministic work. They prove themselves with tests. They stay reusable across repositories without leaking local assumptions into the global artifact. And when the failure is obvious and safe to repair, they can heal cleanly instead of collapsing.

That is the standard this repo is built around.

---

## The philosophy

A powerful skill should feel like a small production system:

- **Project-aware** — the skill stays reusable, while local commands, paths, and constraints live in project context
- **Rigorously tested** — shipped scripts and critical workflow assumptions get validated, not merely described
- **Self-healing when safe** — narrow, low-risk failures can be repaired automatically; ambiguous ones must stop and surface
- **Operationally reusable** — the same skill can move across repositories without dragging stale assumptions behind it
- **Usable by another agent** — not just readable, but navigable, actionable, and finishable without guesswork

This repo is about building skills with that level of seriousness.

---

## What Better Skill Creator helps you build

Not every skill needs every moving part.

But when the problem demands it, this framework supports skills with:

- a strong `SKILL.md` that acts as the control plane
- modular `references/` for deeper guidance
- deterministic `scripts/` for repeated operations
- `tests/` that prove those scripts and workflows hold up
- `self-healing/` for narrow remediation paths
- `project.skill.md.template` so project-specific reality lives in the project, not the reusable skill

Think of it as an architecture for turning fragile prompt-docs into durable operational artifacts.

---

## The shape of a serious skill

```text
my-skill/
├── SKILL.md
├── project.skill.md.template
├── references/
├── scripts/
├── tests/
└── self-healing/
```

Not every skill needs the full stack.

Some deserve to stay lean. Others need the full machinery.

This repo helps an agent decide the difference instead of cargo-culting structure for its own sake.

---

## The backbone of the system

### 1. `SKILL.md` is the control plane
It should tell an agent:
- when the skill applies
- what laws and stop conditions govern it
- which references matter next
- which scripts should be used instead of re-derived
- what completion actually means

### 2. `project.skill.md` keeps local reality where it belongs
Reusable skills should not be stained with one repo’s paths, commands, and constraints.

That is why this repo uses:
- `project.skill.md.template` in the skill
- `project.skill.md` in the project

The skill stays portable. The project keeps its own truth.

### 3. Scripts deserve proof
If a skill ships executable behavior, it should be validated like executable behavior.

Tests are not decorative. They are the difference between “documented” and “trusted.”

### 4. Self-healing is a scalpel, not a sledgehammer
A missing output directory? Fine.
A broad rewrite because something “probably” broke? Absolutely not.

This repo treats self-healing as constrained remediation, not magical cleanup.

---

## What’s in this repo

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

## The reference skill

This repo includes a canonical reference skill:

- [`reference-skills/release-notes-generator/`](reference-skills/release-notes-generator/)

And a paired project context example:

- [`examples/release-notes-project/project.skill.md`](examples/release-notes-project/project.skill.md)

It demonstrates the full pattern in motion:
- a law-driven `SKILL.md`
- project-local context
- deterministic scripting
- paired tests
- narrow self-healing
- real validation from a project-side workflow

It exists as proof and calibration — a living specimen of the framework.

---

## Validation and packaging

Use the included tooling to keep skills honest:

```bash
python3 scripts/quick_validate.py <skill_directory>
python3 scripts/package_skill.py <skill_directory> [output_directory]
```

The validator checks core frontmatter quality and structural promises such as:
- broken `SKILL.md` links
- stale `project.md` references
- missing `project.skill.md.template`
- missing script/test pairs

The packager validates first, then produces a distributable `.skill` archive.

---

## The deeper references

This repo is intentionally modular. The root skill routes agents into the right reference at the right moment.

Key references include:

- [`references/project-skill-context.md`](references/project-skill-context.md)
- [`references/skill-architecture-levels.md`](references/skill-architecture-levels.md)
- [`references/skill-testing.md`](references/skill-testing.md)
- [`references/script-test-conventions.md`](references/script-test-conventions.md)
- [`references/self-healing-rules.md`](references/self-healing-rules.md)
- [`references/behavioral-validation-checklist.md`](references/behavioral-validation-checklist.md)
- [`references/completion-gate.md`](references/completion-gate.md)
- [`references/description-writing.md`](references/description-writing.md)

---

## How to use this repo

1. Start with the root [`SKILL.md`](SKILL.md)
2. Let it route you into the right references
3. Add structure only when the problem earns it
4. Validate what you ship
5. Treat the reference skill as calibration, not a shortcut

---

## Contributing

Contributions are welcome, especially around:
- stronger operational patterns
- sharper validation rules
- better reference skills
- better tests and safer self-healing strategies
- cleaner project-local context patterns

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE.txt](LICENSE.txt).
