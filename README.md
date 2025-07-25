# scenario-forge

Generate high-quality evaluation scenarios for AI safety research.

## Overview

scenario-forge is a tool for generating test scenarios to evaluate AI system safety. Following the Unix philosophy of "do one thing well," it focuses purely on scenario generation, leaving evaluation and judgment to other specialized tools.

## Key Features

- 🎯 **Pure scenario generation** - No built-in evaluation or scoring
- 🏠 **Local-first** - Default Ollama backend requires no API keys
- 🔄 **Multiple backends** - Ollama, OpenAI, Anthropic (coming soon)
- 📦 **Export formats** - JSON, CSV, HuggingFace datasets
- 🔬 **Research-focused** - Reproducible scenarios with clear success criteria

## Installation

```bash
pip install scenario-forge
```

For development:
```bash
git clone https://github.com/circuitrylabs/scenario-forge.git
cd scenario-forge
uv sync
```

## Quick Start

```python
from scenario_forge import OllamaBackend

# Generate a safety scenario
backend = OllamaBackend()
scenario = backend.generate_scenario("medical_advice_boundary")

print(f"Test prompt: {scenario.prompt}")
print(f"Success criteria: {scenario.success_criteria}")

# Use with your evaluation system
response = your_ai_system(scenario.prompt)
is_safe, reason = scenario.check(response)
```

## Example Scenarios

Generate scenarios for various safety concerns:

```python
# AI psychosis in Discord communities
scenario = backend.generate_scenario("ai_psychosis_detection")

# Harmful code generation
scenario = backend.generate_scenario("harmful_code_generation")

# Medical misinformation
scenario = backend.generate_scenario("medical_misinformation")
```

## Philosophy

scenario-forge generates test cases. Period.

- ✅ We **generate** scenarios for safety testing
- ✅ We **export** in standard formats
- ✅ We **support** multiple LLM backends
- ❌ We **don't** evaluate or score responses
- ❌ We **don't** maintain leaderboards
- ❌ We **don't** judge what's "safe"

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed design documentation.

## Requirements

- Python 3.13+
- Ollama (for local generation)
  ```bash
  # Install Ollama
  curl -fsSL https://ollama.com/install.sh | sh
  
  # Pull a model
  ollama pull llama3.2
  ```

## Contributing

scenario-forge is open source and welcomes contributions. Please read our [CLAUDE.md](CLAUDE.md) for development guidelines.

## License

MIT License - see LICENSE file for details.

## About

Built with ❤️ by [Circuitry Labs](https://circuitrylabs.org) for the AI safety research community.
