"""Test scenario-forge review command."""

from click.testing import CliRunner
from unittest.mock import patch

from scenario_forge.cli import cli


def test_review_command_no_scenarios(isolated_db):
    """Test review command when no unrated scenarios exist."""
    runner = CliRunner()

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store.return_value.get_scenarios_for_review.return_value = []

        result = runner.invoke(cli, ["review"])

        assert result.exit_code == 0
        assert "No unrated scenarios found" in result.output


def test_review_command_with_rating(isolated_db, sample_scenarios):
    """Test reviewing and rating scenarios."""
    runner = CliRunner()

    # Mock scenarios to review
    scenarios_with_ids = [(1, sample_scenarios[0]), (2, sample_scenarios[1])]

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store_instance = mock_store.return_value
        mock_store_instance.get_scenarios_for_review.return_value = scenarios_with_ids

        # Simulate user input: rate first as 3, second as 2
        result = runner.invoke(cli, ["review"], input="3\n2\n")

        assert result.exit_code == 0
        assert "Found 2 scenarios to review" in result.output
        assert "ai_psychosis" in result.output
        assert "harmful_code" in result.output

        # Verify ratings were saved
        assert mock_store_instance.save_rating.call_count == 2
        mock_store_instance.save_rating.assert_any_call(1, 3)
        mock_store_instance.save_rating.assert_any_call(2, 2)


def test_review_command_skip_scenario(isolated_db, sample_scenarios):
    """Test skipping a scenario during review."""
    runner = CliRunner()

    scenarios_with_ids = [(1, sample_scenarios[0])]

    with patch("scenario_forge.cli.ScenarioStore") as mock_store:
        mock_store_instance = mock_store.return_value
        mock_store_instance.get_scenarios_for_review.return_value = scenarios_with_ids

        # Simulate Ctrl+C (abort)
        result = runner.invoke(cli, ["review"], input="\x03")

        assert result.exit_code == 0
        assert "Skipping this scenario" in result.output

        # No rating should be saved
        mock_store_instance.save_rating.assert_not_called()
