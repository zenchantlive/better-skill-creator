<div align="center">

# 🛠️ Writing Better Skills

**Framework for building project-aware, tested, reusable agent skills**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![GitHub release](https://img.shields.io/github/v/release/zenchantlive/writing-better-skills.svg)](https://github.com/zenchantlive/writing-better-skills/releases)
[![GitHub issues](https://img.shields.io/github/issues/zenchantlive/writing-better-skills.svg)](https://github.com/zenchantlive/writing-better-skills/issues)

</div>

Writing Better Skills is a framework for authoring agent skills that hold up across repositories and repeated use.

It focuses on four failure points common in skill systems:
- project-specific assumptions leaking into reusable skills
- scripts shipped without tests
- brittle workflows with no validation path
- failures that could be repaired safely but are left as manual cleanup

## 👥 Who this is for

- developers building Claude-style or agent skill systems
- AI engineers maintaining reusable operational skills
- teams that want project-aware, testable, maintainable skills instead of one-off prompt docs

## 📦 What it includes

- a root authoring framework in [`SKILL.md`](SKILL.md)
- project-local context support via [`project.skill.template.md`](project.skill.template.md)
- validation tooling in [`scripts/`](scripts/)
- supporting references in [`references/`](references/)
- a canonical reference skill in [`reference-skills/release-notes-generator/`](reference-skills/release-notes-generator/)
- a project-side example in [`examples/release-notes-project/`](examples/release-notes-project/)

## 🧭 Reference skill

The reference skill is the quickest way to inspect the output of the framework:

- [`reference-skills/release-notes-generator/`](reference-skills/release-notes-generator/)
- [`examples/release-notes-project/project.skill.md`](examples/release-notes-project/project.skill.md)

It includes:
- a production-style `SKILL.md`
- project-local context via `project.skill.template.md`
- a deterministic script
- a paired test
- a narrow self-healing script
- a project workflow that runs against real files

## 🔧 Tooling

### Validate a skill

```bash
python3 scripts/quick_validate.py <skill_directory>
```

Checks include:
- frontmatter validity
- broken `SKILL.md` links
- stale `project.md` references
- missing `project.skill.template.md`
- missing script/test pairs


## 🚀 Quick start

```bash
git clone https://github.com/zenchantlive/writing-better-skills.git
cd writing-better-skills

# inspect the reference skill
ls reference-skills/release-notes-generator

# validate the root framework skill
python3 scripts/quick_validate.py .

# validate the reference skill
python3 scripts/quick_validate.py reference-skills/release-notes-generator

# run the reference skill test
python3 reference-skills/release-notes-generator/tests/test_generate_release_notes.py
```

## 🗂️ Project-local context

Reusable skills should not contain repository-specific commands, paths, or constraints.

This repo uses:
- `project.skill.template.md` inside the skill
- `project.skill.md` inside the project

That separation keeps the reusable skill portable while allowing each project to define its own local reality.

## 🧱 Repository layout

```text
writing-better-skills/
├── SKILL.md
├── project.skill.template.md
├── references/
├── scripts/
├── reference-skills/
│   └── release-notes-generator/
└── examples/
    └── release-notes-project/
```

## ✅ Validation in CI

CI validates:
- the root framework skill
- the reference skill
- the reference skill test
- the example project workflow
- the self-healing path

## 🤝 Contributing

Contributions are welcome for:
- validation improvements
- additional reference skills
- safer self-healing patterns
- stronger testing conventions
- project-local context patterns

See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

MIT — see [LICENSE.txt](LICENSE.txt).
