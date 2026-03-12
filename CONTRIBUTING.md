# Contributing to Better Skill Creator

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/zenchantlive/better-skill-creator/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and why it would be useful
3. Include examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/better-skill-creator.git
cd better-skill-creator

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Test the scripts
python scripts/init_skill.py test-skill --path ./test-output
python scripts/quick_validate.py ./test-output/test-skill
```

## Code Style

- Follow PEP 8 for Python code
- Use clear, descriptive variable names
- Add docstrings to functions
- Keep functions focused and small

## Testing

Before submitting a PR:

1. Run any existing tests
2. Test your changes manually
3. Ensure scripts work across different environments

## Questions?

Feel free to open an issue for any questions or discussions!

---

Thank you for helping make Better Skill Creator better! 💪
