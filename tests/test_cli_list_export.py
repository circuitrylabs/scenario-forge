"""Test scenario-forge list and export commands."""

import json
from click.testing import CliRunner
from unittest.mock import patch

from scenario_forge.cli import cli
from scenario_forge.core import Scenario


def test_list_command_empty():
    """Test list command with no scenarios."""
    runner = CliRunner()

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store.return_value.list_all_scenarios.return_value = []

        result = runner.invoke(cli, ["list"])

        assert result.exit_code == 0
        assert "No scenarios found" in result.output


def test_list_command_with_scenarios():
    """Test list command with scenarios."""
    runner = CliRunner()

    mock_scenarios = [
        Scenario("Prompt 1", "target1", ["criteria1"]),
        Scenario("Prompt 2", "target2", ["criteria2", "criteria3"]),
    ]

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store.return_value.list_all_scenarios.return_value = mock_scenarios

        result = runner.invoke(cli, ["list"])

        assert result.exit_code == 0
        assert "Found 2 scenarios" in result.output
        assert "target1" in result.output
        assert "target2" in result.output


def test_export_command_no_rated():
    """Test export command when no rated scenarios exist."""
    runner = CliRunner()

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store.return_value.get_rated_scenarios.return_value = []

        result = runner.invoke(cli, ["export"])

        assert result.exit_code == 0
        assert "No scenarios found with rating >= 0" in result.output


def test_export_command_with_filter():
    """Test export command with minimum rating filter."""
    runner = CliRunner()

    mock_rated_scenarios = [
        {
            "id": 1,
            "prompt": "Test prompt 1",
            "evaluation_target": "target1",
            "success_criteria": ["criteria1"],
            "rating": 3,
            "rated_at": "2024-01-01T12:00:00",
            "backend": "ollama",
            "model": "llama3.2",
        },
        {
            "id": 2,
            "prompt": "Test prompt 2",
            "evaluation_target": "target2",
            "success_criteria": ["criteria2", "criteria3"],
            "rating": 2,
            "rated_at": "2024-01-01T13:00:00",
            "backend": "ollama",
            "model": "llama3.2",
        },
    ]

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store.return_value.get_rated_scenarios.return_value = mock_rated_scenarios

        result = runner.invoke(cli, ["export", "--min-rating", "2"])

        assert result.exit_code == 0

        # Parse JSON output
        exported = json.loads(result.output)
        assert len(exported) == 2
        assert exported[0]["rating"] == 3
        assert exported[1]["rating"] == 2
