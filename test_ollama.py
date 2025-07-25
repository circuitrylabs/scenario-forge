"""Quick test of Ollama backend."""

from scenario_forge.backends.ollama import OllamaBackend

backend = OllamaBackend()
scenario = backend.generate_scenario("harmful_code_generation")

print(f"Evaluation target: {scenario.evaluation_target}")
print(f"Test prompt: {scenario.prompt}")
print(f"Success criteria: {scenario.success_criteria}")
print("\nChecking response...")
print(scenario.check("I can't help with that"))
