"""Test CLI --save flag functionality."""

import json
import tempfile
from pathlib import Path

from click.testing import CliRunner
import pytest

from scenario_forge.cli import cli
from scenario_forge.datastore import ScenarioStore


@pytest.fixture
def isolated_db(monkeypatch):
    """Use a temporary database for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Override the home directory for this test
        test_home = Path(tmpdir)
        monkeypatch.setenv("HOME", str(test_home))
        
        # Create the .scenario-forge directory
        (test_home / ".scenario-forge").mkdir()
        
        yield test_home / ".scenario-forge" / "scenarios.db"


def test_generate_without_save_no_storage(isolated_db):
    """Test that generate without --save doesn't store."""
    runner = CliRunner()
    result = runner.invoke(cli, ["generate", "test_target"])
    
    assert result.exit_code == 0
    
    # Should output JSON
    output = json.loads(result.output)
    assert output["evaluation_target"] == "test_target"
    
    # Should NOT save to database
    store = ScenarioStore()
    scenarios = store.list_all_scenarios()
    assert len(scenarios) == 0


def test_generate_with_save_stores(isolated_db):
    """Test that generate with --save stores to database."""
    runner = CliRunner()
    
    # Run with --save
    result = runner.invoke(cli, ["generate", "save_test", "--save"])
    
    assert result.exit_code == 0
    
    # Should still output JSON
    output = json.loads(result.output)
    assert output["evaluation_target"] == "save_test"
    
    # Should save to database
    store = ScenarioStore()
    scenarios = store.list_all_scenarios()
    assert len(scenarios) == 1
    
    # Check the saved scenario
    saved = scenarios[0]
    assert saved.evaluation_target == "save_test"


def test_generate_multiple_with_save(isolated_db):
    """Test that --count with --save stores all scenarios."""
    runner = CliRunner()
    
    result = runner.invoke(cli, ["generate", "multi_test", "--count", "3", "--save"])
    
    assert result.exit_code == 0
    
    # Should output 3 JSON objects (one per line)
    lines = result.output.strip().split('\n')
    assert len(lines) == 3
    
    # All should be saved
    store = ScenarioStore()
    scenarios = store.list_all_scenarios()
    assert len(scenarios) == 3
    
    # Check all are our target
    assert all(s.evaluation_target == "multi_test" for s in scenarios)