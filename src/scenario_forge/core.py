"""Core abstractions for scenario-forge."""


class Scenario:
    """The atomic unit of safety evaluation."""
    
    def __init__(self, prompt: str, evaluation_target: str, success_criteria: str):
        self.prompt = prompt
        self.evaluation_target = evaluation_target
        self.success_criteria = success_criteria
    
    def check(self, response: str) -> tuple[bool, str]:
        """Check if response meets safety criteria."""
        if self.success_criteria.lower() in response.lower():
            return True, f"Response contains: '{self.success_criteria}'"
        return False, f"Missing expected behavior: '{self.success_criteria}'"
