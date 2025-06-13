from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass
class ModelOutput:
    """Simple container for a model name and its generated response."""

    model_name: str
    response: str


class LLMComparator:
    """Utility to compare multiple LLMs on the same prompt."""

    def __init__(self, model_calls: Dict[str, Callable[[str], str]]):
        """`model_calls` is a mapping of model name to callable."""
        self.model_calls = model_calls

    def compare(self, prompt: str) -> List[ModelOutput]:
        """Return the response from each model for the given prompt."""
        outputs = []
        for name, call in self.model_calls.items():
            outputs.append(ModelOutput(model_name=name, response=call(prompt)))
        return outputs
