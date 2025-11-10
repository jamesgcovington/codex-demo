# Codex Agents

## Project Goals
- Small Python demos and utilities. Keep changes minimal and well-commented.

## Guardrails
- Never run external network calls.
- Never change shell/profile files (~/.zshrc, ~/.zprofile) or global configs.
- Ask before installing packages or adding dependencies.
- Explain risky actions and provide diffs.

## Approvals (default: ask)
- ✅ Without asking: edit files in this repo, format code, add tests/docs under ./tests or ./docs.
- ❌ Ask first: adding new dependencies, modifying CI, creating/deleting git tags, running shell commands that alter global state.

## Style
- Python 3.11+, black formatting.
- Use clear, small commits with descriptive messages.
