"""Command-line interface for scenario-forge."""

import json

import click
from rich import print as rprint
from rich.json import JSON

from scenario_forge.backends.ollama import OllamaBackend
from scenario_forge.datastore import ScenarioStore


@click.group()
def cli():
    """Generate AI safety evaluation scenarios."""
    pass


@cli.command()
@click.argument("target")
@click.option("--count", default=1, help="Number of scenarios to generate")
@click.option("--pretty", is_flag=True, help="Pretty print output")
@click.option("--save", is_flag=True, help="Save scenarios to database")
@click.option("--model", default="llama3.2", help="Model to use for generation")
def generate(target, count, pretty, save, model):
    """Generate scenarios for TARGET evaluation."""
    backend = OllamaBackend(model=model)

    # Only create ScenarioStore if user wants to save
    scenario_store = ScenarioStore() if save else None

    for i in range(count):
        scenario = backend.generate_scenario(target)

        # Save to database if requested
        if scenario_store:
            scenario_store.save_scenario(
                scenario,
                backend="ollama",
                model=model,
            )

        output = {
            "prompt": scenario.prompt,
            "evaluation_target": scenario.evaluation_target,
            "success_criteria": scenario.success_criteria,
        }

        if pretty:
            # Rich pretty printing
            rprint(JSON.from_data(output))
        else:
            # Unix-friendly JSON lines
            print(json.dumps(output))


if __name__ == "__main__":
    cli()
