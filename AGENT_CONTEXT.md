# Agent Context: scenario-forge

## Quick Start
```bash
# You're working on: scenario-forge RC1
# Current branch: feat/rating-system
# THE ONE TASK: Implement rating system (see RC1_READY.md)
```

## Mission
Build self-improving AI safety system. Generate scenarios → Save → **RATE** → Export → Learn.

## Current State
- ✅ Core generation (Ollama)
- ✅ SQLite storage (--save flag)
- ✅ List command working
- ✅ Test suite passing
- ✅ Docs coherent with reality
- 🚧 **BLOCKER: Rating system**
- 🚧 Export command (needs ratings first)

## RC1 Critical Path
1. **Read RC1_READY.md** - Has exact implementation plan
2. **Add ratings table** - to datastore.py
3. **Add review command** - to cli.py
4. **Add export command** - JSON only
5. **Test full loop** - generate → save → review → export
6. **Ship RC1**

## Development Flow
```bash
# You're already on feat/rating-system branch

# Quick quality check before starting
uvx ruff check . && uvx ty check && uv run pytest tests/ -v

# Test as you go
uv run pytest tests/test_datastore.py -v  # After ratings table
uv run pytest tests/test_cli.py -v        # After review command

# Manual testing
scenario-forge generate "ai_psychosis" --save
scenario-forge list
scenario-forge review  # NEW - implement this
scenario-forge export  # NEW - implement this
```

## Key Files
- **RC1_READY.md** - START HERE! Implementation plan
- **docs/RC1_CRITICAL_PATH.md** - Why rating matters
- **src/scenario_forge/datastore.py** - Add ratings table
- **src/scenario_forge/cli.py** - Add review/export commands

## Session Log

### Session 2025-01-26 Morning (Coherence & Prep)
- Created MISSION_VISION.md
- Updated all docs to reflect current reality
- Removed promises of unimplemented features
- Created RC1_READY.md with clear plan
- Branch: feat/rating-system
- Ready for: Rating system implementation

### Session 2024-01-26 (Initial Setup)
- Created datastore with save/get/list
- Added --save flag to CLI
- Fixed tests to use isolated databases
- Compressed docs to SCENARIO_FORGE_CORE.md

<!-- Next session: Implement rating system per RC1_READY.md -->