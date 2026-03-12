<div align="center">

# Better Skill Creator

**Stop shipping brittle agent skills. Build skills you can trust.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![GitHub release](https://img.shields.io/github/v/release/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/releases)
[![GitHub issues](https://img.shields.io/github/issues/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/issues)

*Project-aware. Tested. Repairable. Reusable.*

</div>

---

If you build agent skills, you’ve probably seen the pattern:

- they work once, in one repo, under one set of assumptions
- another agent picks them up and gets lost
- local paths and commands leak into the global skill
- scripts ship without tests
- failures turn into guesswork

Better Skill Creator is a framework for building skills that hold up under real use.

It treats skills less like markdown notes and more like small operational systems: aware of their environment, backed by validation, and disciplined enough to survive reuse.

---

## Who this is for

This repo is for:
- AI engineers building reusable agent skills
- developers creating Claude-style skill systems
- teams whose skills keep getting brittle, project-specific, or hard to trust
- anyone who wants skills with real operational discipline instead of prompt-shaped wishful thinking

---

## What makes it different

Better Skill Creator focuses on the parts that usually get skipped:

- **Project awareness** — reusable skills stay clean; local reality lives in project context
- **Rigorous testing** — shipped scripts and workflow assumptions get validated
- **Safe self-healing** — narrow, explicit failures can be repaired without turning the repo into chaos
- **Operational reuse** — the same skill can move between projects without dragging stale assumptions behind it
- **Reference-quality outputs** — the framework is backed by a canonical reference skill, not just theory

---

## Start here

If you want to understand what this repo produces, look at these first:

- **Reference skill:** [`reference-skills/release-notes-generator/`](reference-skills/release-notes-generator/)
- **Example project context:** [`examples/release-notes-project/project.skill.md`](examples/release-notes-project/project.skill.md)
- **Root authoring framework:** [`SKILL.md`](SKILL.md)

That path gives you the fastest read on the system:
1. see the output
2. see how project-local context works
3. then read the framework behind it

---

## The parts that give it teeth

This repo is not just guidance. It comes with tooling that enforces the standard.

### Validation

```bash
python3 scripts/quick_validate.py <skill_directory>
```

The validator checks structural promises such as:
- frontmatter quality
- broken `SKILL.md` links
- stale `project.md` references
- missing `project.skill.md.template`
- missing script/test pairs

### Packaging

```bash
python3 scripts/package_skill.py <skill_directory> [output_directory]
```

The packager validates first, then produces a distributable `.skill` archive.

### CI-backed verification

The repo CI validates:
- the root framework skill
- the canonical reference skill
- the reference skill’s paired test
- the project-side workflow
- the self-healing path

That matters. A skill framework that cannot verify its own reference skill is just decoration.

---

## Core idea

The central move in this repo is simple:

**keep the reusable skill global, and keep project reality local.**

That is what `project.skill.md.template` is for.

The skill ships the template. The project owns the filled-in `project.skill.md`.

That separation is what lets a skill stay reusable without being contaminated by one repository’s commands, paths, or constraints.

---

## What a powerful skill can include

Not every skill needs the full stack. But when the problem demands it, this framework supports skills with:

- `SKILL.md` for activation logic, workflow, and guardrails
- `references/` for deeper guidance
- `scripts/` for deterministic operations
- `tests/` for proof
- `self-healing/` for narrow remediation
- `project.skill.md.template` for project-local adaptation

The point is not to add structure for its own sake.

The point is to give a skill the same qualities you’d want from any serious operational artifact: clarity, reliability, recoverability, and reuse.

---

## Repo layout

```text
better-skill-creator/
├── SKILL.md
├── project.skill.md.template
├── references/
├── scripts/
├── reference-skills/
│   └── release-notes-generator/
└── examples/
    └── release-notes-project/
```

If you want the deeper internals, `references/` covers architecture, testing, self-healing, completion rules, and project-local context patterns.

---

## Why the reference skill matters

The reference skill is the fastest way to judge whether this repo is serious.

It shows:
- a real `SKILL.md`
- project-local context
- a deterministic script
- a paired test
- a self-healing path
- a project-side workflow that actually runs

In other words: not just how the framework talks, but what it can actually produce.

---

## Contributing

Contributions are welcome, especially around:
- stronger validation rules
- sharper reference skills
- safer self-healing patterns
- better testing practices
- cleaner project-local context conventions

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE.txt](LICENSE.txt).
