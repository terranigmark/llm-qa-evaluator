from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Dict


@dataclass
class PromptResult:
    prompt: str
    response: str
    score: Dict[str, float]


class LLMEvaluator:
    """Herramientas básicas para evaluar respuestas de un LLM."""

    def __init__(self, model_call: Callable[[str], str]):
        """`model_call` debe ser una función que reciba un prompt y devuelva la respuesta del modelo."""
        self.model_call = model_call

    def evaluate_prompt(self, prompt: str) -> PromptResult:
        response = self.model_call(prompt)
        score = self.basic_score(prompt, response)
        return PromptResult(prompt=prompt, response=response, score=score)

    def basic_score(self, prompt: str, response: str) -> Dict[str, float]:
        """Ejemplo de heurística sencilla para puntuar factualidad y claridad."""
        # Nota: En un proyecto real se implementarían verificaciones más complejas
        length_penalty = 1.0 if len(response.split()) > 3 else 0.0
        return {
            "clarity": length_penalty,
            "factuality": 0.5,  # Placeholder
        }

    def evaluate_batch(self, prompts: List[str]) -> List[PromptResult]:
        results = []
        for p in prompts:
            results.append(self.evaluate_prompt(p))
        return results
