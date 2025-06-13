from __future__ import annotations

from typing import Callable


class ConsistencyEvaluator:
    """Simple evaluator to check if a model is consistent when answering the same prompt multiple times."""

    def __init__(self, model_call: Callable[[str], str], runs: int = 3):
        self.model_call = model_call
        self.runs = runs

    def check_consistency(self, prompt: str) -> bool:
        responses = [self.model_call(prompt) for _ in range(self.runs)]
        first = responses[0]
        return all(r == first for r in responses)
