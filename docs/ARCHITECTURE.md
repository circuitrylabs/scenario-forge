# scenario-forge Architecture

## Philosophy

scenario-forge follows the Unix philosophy: **do one thing and do it well**.

That one thing: **Generate high-quality safety evaluation scenarios for AI systems**.

## What scenario-forge IS

A pure scenario generation engine that:
- Creates test cases for AI safety evaluation
- Supports multiple LLM backends (local and cloud)
- Exports scenarios in standard formats
- Maintains reproducibility through seeds/configs

## What scenario-forge IS NOT

- ❌ An evaluation framework
- ❌ A benchmarking tool
- ❌ A prompt engineering suite
- ❌ An AI safety judge

## Core Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        scenario-forge                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐     ┌──────────────┐     ┌──────────────┐  │
│  │   Core      │     │   Backends   │     │  Exporters   │  │
│  │             │     │              │     │              │  │
│  │ Scenario    │────▶│ OllamaBackend│────▶│ JSONExporter │  │
│  │ Generator   │     │ OpenAIBackend│     │ HFExporter   │  │
│  │ Validator   │     │ AnthropicBE  │     │ CSVExporter  │  │
│  └─────────────┘     └──────────────┘     └──────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

```
                    scenario-forge
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
    ▼                    ▼                    ▼
[Evaluation Target]  [Backend]          [Parameters]
"ai_psychosis"       "llama3.2"         temperature=0.7
    │                    │                    │
    └────────────────────┴────────────────────┘
                         │
                         ▼
                 ┌──────────────┐
                 │   Generate   │
                 └───────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │  Scenario   │
                  ├─────────────┤
                  │ prompt      │
                  │ target      │
                  │ criteria    │
                  └─────────────┘
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
    ▼                    ▼                    ▼
[Your Evaluator]   [Export Format]      [Researcher]
```

## Component Details

### Core Types

```python
Scenario                          # The atomic unit
├── prompt: str                   # What to ask the AI
├── evaluation_target: str        # What we're testing
└── success_criteria: str         # Expected safe behavior

Generator (Protocol)              # All generators implement
└── generate(target) -> Scenario  # Single generation interface
```

### Backend Architecture

```
┌─────────────────────┐
│  Backend Protocol   │
├─────────────────────┤
│ generate_scenario() │──────┐
└─────────────────────┘      │
           ▲                 │
           │                 ▼
   ┌───────┴───────┐   ┌──────────┐
   │               │   │          │
┌──┴───┐   ┌───────┴─┐ │  System  │
│Ollama│   │ OpenAI  │ │  Prompt  │
└──────┘   └─────────┘ └──────────┘
```

### Export Pipeline

```
Scenario Collection
        │
        ▼
┌───────────────┐
│ Export Format │
├───────────────┤
│ • JSON        │──────▶ evaluation-suite.json
│ • CSV         │──────▶ test-cases.csv
│ • HuggingFace │──────▶ 🤗 Dataset
│ • Raw Python  │──────▶ scenarios.py
└───────────────┘
```

## Extension Points

### Adding a Backend

1. Implement the `Generator` protocol
2. Place in `src/scenario_forge/backends/`
3. Handle backend-specific configuration

```python
class YourBackend:
    def generate_scenario(self, evaluation_target: str) -> Scenario:
        # Your implementation
        pass
```

### Adding an Exporter

1. Implement the `Exporter` protocol
2. Place in `src/scenario_forge/exporters/`
3. Handle format-specific serialization

```python
class YourExporter:
    def export(self, scenarios: list[Scenario]) -> Any:
        # Your implementation
        pass
```

## Usage Patterns

### CLI Usage (Future)

```bash
# Generate single scenario
scenario-forge generate "medical_advice_boundary"

# Generate batch
scenario-forge generate "ai_psychosis" --count 100 --backend ollama

# Export scenarios
scenario-forge export scenarios.json --format json
```

### Library Usage

```python
from scenario_forge import OllamaBackend

# Generate scenarios
backend = OllamaBackend()
scenario = backend.generate_scenario("harmful_code_generation")

# Use with your evaluation system
response = your_ai_system(scenario.prompt)
safe = your_evaluator(response, scenario.success_criteria)
```

## Design Decisions

1. **Protocol-based backends**: Easy to add new LLM providers
2. **Simple core types**: Just `Scenario`, no complex hierarchies
3. **Pure generation**: No built-in evaluation or judging
4. **Local-first**: Default to Ollama, no API keys required
5. **Research-focused**: Reproducible, exportable, citable

## What We DON'T Do

- ❌ Score or rank AI responses
- ❌ Maintain benchmark leaderboards
- ❌ Provide "correct" answers
- ❌ Judge safety automatically

## Integration Example

```
Your System
     │
     ▼
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   Discord   │────▶│scenario-forge│────▶│ Your Safety  │
│     Bot     │     │  (generates) │     │  Evaluator   │
└─────────────┘     └──────────────┘     └──────────────┘
     ▲                                            │
     └────────────────────────────────────────────┘
                    Feedback Loop
```

## Future Considerations

- Scenario templates for common domains
- Seed-based reproducibility
- Difficulty calibration
- Multi-turn scenario generation

But always: **Generation only. Never evaluation.**
