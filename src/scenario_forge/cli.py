"""Command-line interface for scenario-forge."""

import json

import click
from rich import print as rprint
from rich.json import JSON

from scenario_forge.backends.ollama import OllamaBackend


@click.group()
def cli():
    """Generate AI safety evaluation scenarios."""
    pass


@cli.command()
@click.argument('target')
@click.option('--count', default=1, help='Number of scenarios to generate')
@click.option('--pretty', is_flag=True, help='Pretty print output')
def generate(target, count, pretty):
    """Generate scenarios for TARGET evaluation."""
    backend = OllamaBackend()
    
    for i in range(count):
        scenario = backend.generate_scenario(target)
        
        output = {
            "prompt": scenario.prompt,
            "evaluation_target": scenario.evaluation_target,
            "success_criteria": scenario.success_criteria
        }
        
        if pretty:
            # Rich pretty printing
            rprint(JSON.from_data(output))
        else:
            # Unix-friendly JSON lines
            print(json.dumps(output))


if __name__ == "__main__":
    cli()