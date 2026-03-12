<div align="center">

# 🛠️ Better Skill Creator

**The definitive framework for building AI agent skills that scale**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![GitHub release](https://img.shields.io/github/v/release/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/releases)
[![GitHub stars](https://img.shields.io/github/stars/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/zenchantlive/better-skill-creator.svg)](https://github.com/zenchantlive/better-skill-creator/issues)

*Transform your AI agent from general-purpose to domain-expert with modular, reusable skill packages.*

[Quick Start](#-quick-start) • [Documentation](#-documentation) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 🎯 Why Better Skill Creator?

AI agents are powerful, but they lack **procedural knowledge** — the "how-to" wisdom that comes from experience. Skills bridge that gap.

**Better Skill Creator** gives you the framework to build skills that are:

| Feature | Description |
|---------|-------------|
| 🧠 **Context-Aware** | Progressive disclosure keeps context windows lean |
| 🔄 **Self-Healing** | Built-in test and repair mechanisms |
| 📦 **Portable** | Package, share, and deploy skills across environments |
| 🎛️ **Configurable** | Dynamic architecture adapts to any project |
| ✅ **Validated** | Automated quality checks before deployment |

---

## 📦 What's Inside

```
better-skill-creator/
├── SKILL.md                    # Core documentation
├── scripts/
│   ├── init_skill.py           # Scaffold new skills instantly
│   ├── package_skill.py        # Package & validate for distribution
│   └── quick_validate.py       # Fast quality checks
└── references/
    ├── workflows.md            # Multi-step process patterns
    └── output-patterns.md      # Output format best practices
```

---

## 🚀 Quick Start

### 1. Download

```bash
# Clone the repo
git clone https://github.com/zenchantlive/better-skill-creator.git

# Or download the latest release
wget https://github.com/zenchantlive/better-skill-creator/releases/download/v1.0.0/better-skill-creator.zip
unzip better-skill-creator.zip
```

### 2. Initialize a New Skill

```bash
python scripts/init_skill.py my-awesome-skill --path ./skills
```

This creates:
```
my-awesome-skill/
├── SKILL.md          # Template with frontmatter
├── project.md        # Environment-specific config
├── scripts/          # Your executable tools
├── tests/            # Paired test files
└── self-healing/     # Auto-repair scripts
```

### 3. Build Your Skill

Edit `SKILL.md` with your domain expertise, add scripts, and validate:

```bash
python scripts/package_skill.py ./skills/my-awesome-skill
```

### 4. Share

The packaged `.skill` file is ready for distribution or installation.

---

## 📖 Documentation

### Core Concepts

#### Dynamic Skill Architecture

Skills aren't just markdown files — they're **complete packages**:

- **SKILL.md** — The brain: instructions and guidance
- **scripts/** — The hands: executable, deterministic tools
- **references/** — The library: detailed docs loaded on demand
- **assets/** — The toolbox: templates, images, boilerplate
- **tests/** — The quality gate: paired with every script
- **self-healing/** — The immune system: auto-repair when things break

#### Progressive Disclosure

Context is precious. Better Skill Creator uses a **three-level loading system**:

1. **Metadata** — Always visible (~100 words)
2. **SKILL.md body** — Loaded when triggered (<5k words)
3. **References** — Loaded only when needed (unlimited)

This means your agent gets exactly the information it needs, when it needs it.

#### Degrees of Freedom

Match specificity to fragility:

| Level | Use When | Example |
|-------|----------|---------|
| **High** | Multiple valid approaches | Text-based instructions |
| **Medium** | Preferred pattern exists | Pseudocode with parameters |
| **Low** | Fragile operations, consistency critical | Specific scripts |

### Scripts Reference

#### `init_skill.py`

Scaffold a new skill with the complete dynamic structure.

```bash
python init_skill.py <skill-name> --path <output-directory>
```

#### `package_skill.py`

Validate and package a skill for distribution.

```bash
python package_skill.py <path/to/skill-folder> [output-directory]
```

Automatically validates:
- YAML frontmatter format
- Required fields (`name`, `description`)
- Directory structure
- File organization

#### `quick_validate.py`

Fast validation without packaging.

```bash
python quick_validate.py <path/to/skill-folder>
```

---

## 💡 Examples

### Minimal Skill (Technique)

```
condition-based-waiting/
└── SKILL.md      # Everything inline, <200 words
```

### Skill with Scripts

```
pdf-editor/
├── SKILL.md
└── scripts/
    ├── rotate_pdf.py
    └── extract_text.py
```

### Full Dynamic Skill

```
bigquery-analytics/
├── SKILL.md
├── project.md
├── scripts/
│   ├── query_runner.py
│   └── schema_inspector.py
├── tests/
│   └── test_query_runner.py
├── self-healing/
│   └── heal_auth.py
└── references/
    ├── finance_schema.md
    └── marketing_schema.md
```

---

## 🎨 Skill Design Patterns

### Pattern 1: High-Level Guide with References

Keep SKILL.md lean, link to details:

```markdown
## Advanced Features

- **Form filling**: See [FORMS.md](references/FORMS.md)
- **API reference**: See [REFERENCE.md](references/REFERENCE.md)
```

### Pattern 2: Domain-Specific Organization

Split by domain to avoid loading irrelevant context:

```
├── SKILL.md          # Navigation only
└── references/
    ├── finance.md    # Revenue, billing
    ├── sales.md      # Pipeline, opportunities
    └── product.md    # Usage, features
```

### Pattern 3: Conditional Details

Basic content inline, advanced content linked:

```markdown
## Editing Documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions

- 🐛 Bug fixes
- 📝 Documentation improvements
- ✨ New script templates
- 🧪 Additional test patterns
- 🌐 Translations

---

## 📋 Roadmap

- [ ] Interactive skill wizard (CLI)
- [ ] Skill registry/discovery system
- [ ] Cross-agent compatibility layer
- [ ] Visual skill builder
- [ ] Automated skill testing framework

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE.txt](LICENSE.txt) file for details.

---

## 🙏 Acknowledgments

Built on principles from:
- Anthropic's skill authoring best practices
- Real-world AI agent development workflows
- Community feedback and contributions

---

<div align="center">

**[⬆ Back to Top](#-better-skill-creator)**

Made with ❤️ for the AI agent community

[Star this repo](https://github.com/zenchantlive/better-skill-creator) • [Report a bug](https://github.com/zenchantlive/better-skill-creator/issues) • [Request a feature](https://github.com/zenchantlive/better-skill-creator/issues)

</div>
