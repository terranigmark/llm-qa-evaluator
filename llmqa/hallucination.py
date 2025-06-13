from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class HallucinationResult:
    prompt: str
    response: str
    score: Dict[str, float]


class HallucinationEvaluator:
    """Heurística simple para detección de alucinaciones."""

    def __init__(self, reference_facts: List[str]):
        # Lista de hechos conocidos contra los que validar las respuestas
        self.reference_facts = [f.lower() for f in reference_facts]

    def evaluate(self, prompt: str, response: str) -> HallucinationResult:
        lower_resp = response.lower()
        matches = [fact for fact in self.reference_facts if fact in lower_resp]
        coverage = len(matches) / len(self.reference_facts) if self.reference_facts else 0.0
        hallucination_score = 1.0 - coverage
        return HallucinationResult(
            prompt=prompt,
            response=response,
            score={"hallucination": hallucination_score},
        )
