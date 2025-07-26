# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Mission

scenario-forge generates high-quality evaluation scenarios for AI safety research. It is a foundational tool for Circuitry Labs' mission to ensure AI systems behave ethically in mission-critical contexts.

## Core Invariants (NEVER violate these)

1. **Safety First**: Every generated scenario must be evaluating FOR safety, never teaching harmful patterns
2. **Reproducibility**: All scenarios must include seed/config for exact reproduction
3. **Transparency**: Generated scenarios must clearly state their evaluation purpose
4. **No Jailbreaks**: Never generate scenarios designed to bypass safety measures

## Architecture Boundaries

### What scenario-forge IS:
- A scenario generation engine for AI safety evaluation
- A multi-backend LLM orchestrator for comparative analysis
- A structured data exporter for research pipelines
- A teaching tool for understanding AI behavior

### What scenario-forge IS NOT:
- A general-purpose prompt engineering tool
- A red-teaming/adversarial attack framework
- A benchmark gaming system
- A closed/proprietary system

## Quality Standards

Every scenario must have:
- **Clear evaluation objective** (what safety property are we testing?)
- **Expected behavior** (what should a safe AI do?)
- **Failure modes** (what would unsafe behavior look like?)
- **Difficulty rating** (how subtle is the safety challenge?)

## Code Standards

- **One concept at a time**: Small, reviewable changes for learning
- **Explicit over implicit**: Clear variable names, obvious flow
- **Tests for safety**: Every scenario generator needs quality tests
- **Type hints everywhere**: This is a Python 3.13+ typed codebase
- **Absolute imports**: Always use `from scenario_forge.module import Thing`, never relative imports
- **Public API design**: Define exports in `__init__.py` files for clean interfaces

## Collaboration Rules

- **10 line limit**: Never write more than 10 lines without user interaction
- **Interface first**: Always discuss/sketch interfaces before implementing
- **Show thinking**: Use comments to explore options before coding
- **Stop asking**: When discussing process/meta topics, make decisions
- **Build WITH**: Code emerges from conversation, not delivered as solution

## Integration Points

- **CIRISAI/CIRISAgent**: Primary consumer for agent ethics verification
- **Export formats**: JSON Schema, HuggingFace datasets, raw prompts
- **Backend adapters**: OpenAI, Anthropic, Local models (llama.cpp)

## Development Commands

### Generate scenarios
```bash
# Single scenario
uv run scenario-forge generate "ai_psychosis"

# Multiple scenarios with pretty output
uv run scenario-forge generate "reality_break" --count 5 --pretty

# Pipe to jq for processing
uv run scenario-forge generate "harmful_code" | jq '.prompt'
```

### Install dependencies
```bash
uv sync
```

### Add new dependencies
```bash
uv add <package-name>
```

### Run tests
```bash
uv run pytest tests/ -v
```

### Format code
```bash
uvx ruff format .
```

### Lint and fix
```bash
uvx ruff check . --fix
```

### Type check
```bash
uvx ty
```

### Pre-commit quality check
```bash
uvx ruff format .
uvx ruff check . --fix
uvx ty
uv run pytest tests/ -v
```

## Project Structure

- `src/scenario_forge/` - Core package
  - `cli.py` - Click-based command line interface
  - `core.py` - Base Scenario class and protocols
  - `backends/` - LLM provider adapters
    - `ollama.py` - Local model integration with few-shot examples
  - `exporters/` - Output format handlers (coming soon)
  - `datastore.py` - SQLite storage for scenarios (coming soon)
  - `rating.py` - ScenarioRating model and review UI (coming soon)
- `tests/` - Test suite with safety validation
- `docs/` - Architecture and design documentation
- `pyproject.toml` - Project configuration with CLI entry point
- `uv.lock` - Dependency lock file

## Contributing

Before submitting changes:
1. Ensure all safety invariants are maintained
2. Add tests for new scenario types
3. Document the safety properties being evaluated
4. Run full test suite including safety validation

## Local Development

Create a `CLAUDE.local.md` (git-ignored) for your personal preferences like:
- Preferred code style beyond project standards
- Personal debugging approaches  
- Local model configurations
- Individual learning notes
