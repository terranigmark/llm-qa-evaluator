import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from llmqa.hallucination import HallucinationEvaluator


def test_hallucination_score_no_hallucination():
    evaluator = HallucinationEvaluator([
        "la ipa es amarga",
        "la stout es oscura",
    ])
    result = evaluator.evaluate(
        "Describe dos tipos de cerveza",
        "La IPA es amarga y la stout es oscura."
    )
    assert result.score["hallucination"] == 0.0


def test_hallucination_score_with_hallucination():
    evaluator = HallucinationEvaluator(["hecho conocido"])
    result = evaluator.evaluate(
        "Pregunta",
        "Respuesta inventada que no coincide"
    )
    assert result.score["hallucination"] == 1.0
