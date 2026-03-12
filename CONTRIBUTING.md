# Contributing to Better Skill Creator

Thanks for contributing.

## What to improve

Useful contributions include:
- clearer skill-authoring guidance
- better `project.skill.md` patterns
- stronger validation logic
- tighter examples of scripts/tests/self-healing
- documentation fixes where philosophy or terminology is off

## Ground rules

1. Keep the distinction between **global skill** and **project-local context** clear.
2. Do not reintroduce scaffold-first workflows as the main model.
3. Prefer small, explicit examples over hype or abstraction.
4. If you add scripts, add or update tests.
5. If you add self-healing, keep it narrow and low-risk.

## Development

```bash
cd better-skill-creator
python scripts/quick_validate.py .
```

If you modify validation logic, test those changes directly.

## Pull requests

Please explain:
- what changed
- why it improves the repo
- whether it changes the skill philosophy, examples, or validator behavior

## Issues

If reporting a problem, include:
- the file(s) involved
- the confusing or incorrect behavior
- what you expected instead
