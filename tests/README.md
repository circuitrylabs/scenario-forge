# scenario-forge Test Suite

A comprehensive test suite ensuring AI safety scenario generation works flawlessly.

## Test Organization

### Core Tests
- `test_core.py` - Tests for the `Scenario` class and basic validation
- `test_datastore.py` - SQLite storage and retrieval tests
- `test_rating_system.py` - Rating functionality tests (0-3 scale)

### CLI Tests  
- `test_cli_generate.py` - Tests for `scenario-forge generate` command
- `test_cli_review.py` - Tests for `scenario-forge review` command
- `test_cli_list_export.py` - Tests for `scenario-forge list` and `export` commands

### Integration Tests
- `test_full_workflow.py` - End-to-end workflow tests (generate → save → review → export)

## Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=scenario_forge --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_core.py -v
```

## Test Patterns

### Mocking Ollama
All tests mock the Ollama backend to avoid requiring a running Ollama instance:

```python
from tests.fixtures import mock_ollama_backend

def test_something(mock_ollama_backend):
    # Your test here
```

### Isolated Database
Use the `isolated_db` fixture for tests that need database access:

```python
def test_database_operation(isolated_db):
    store = ScenarioStore()
    # Database is isolated to this test
```

## Coverage Goals
- Minimum: 60% (current)
- Target: 75% (post-RC1)
- Stretch: 90% (v1.0)