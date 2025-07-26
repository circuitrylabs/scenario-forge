# Agent Context: scenario-forge

## Quick Start
```bash
# You're working on: scenario-forge - AI safety scenario generator
# Current focus: MVP 0.0 - Get core loop working
# Next task: Check todos with TodoWrite tool
```

## Mission
Build self-improving AI safety system. Generate scenarios → Test → Learn → Improve.

## Current State
- ✅ Core generation (Ollama)
- ✅ SQLite storage (--save flag)
- ✅ Test suite passing
- 🔄 Need: Export, List, Rate commands

## Development Flow
1. **Check todos**: Use TodoWrite tool
2. **Pick task**: Start with highest priority
3. **TDD**: Write test → implement → quality check
4. **Quality**: `uvx ruff check . && uvx ty check && uv run pytest tests/ -v`
5. **Handoff**: Update this file before closing

## Key Files
- `SCENARIO_FORGE_CORE.md` - Full project context
- `MVP_PLAN.md` - What to build next
- `src/scenario_forge/` - Core code
- `tests/` - Test everything

## Commands
```bash
# Generate scenarios
scenario-forge generate "ai_psychosis" --save

# Run tests
uv run pytest tests/ -v

# Quality check
uvx ruff check . && uvx ty check && uv run pytest tests/ -v

# Explore saved scenarios
sqlite3 ~/.scenario-forge/scenarios.db "SELECT * FROM scenarios;"
```

## Agent Instructions
1. **Be direct**: Short responses, focus on code
2. **Use todos**: TodoWrite tool tracks progress
3. **Test first**: Always TDD
4. **Quality matters**: Run checks before marking complete
5. **Update on exit**: Add session summary below

## Session Log
<!-- Add your session summary here before closing -->

### Session 2024-01-26 (Initial Setup)
- Created datastore with save/get/list
- Added --save flag to CLI
- Fixed tests to use isolated databases
- Compressed docs to SCENARIO_FORGE_CORE.md
- Ready for: JSON export command

<!-- Next session starts here -->