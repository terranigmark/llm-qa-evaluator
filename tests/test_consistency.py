import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from llmqa.consistency import ConsistencyEvaluator


def deterministic_model(prompt: str) -> str:
    return "respuesta fija"


def test_consistency_true():
    evaluator = ConsistencyEvaluator(deterministic_model, runs=3)
    assert evaluator.check_consistency("pregunta")


def test_consistency_false():
    counter = {"n": 0}

    def varying_model(prompt: str) -> str:
        counter["n"] += 1
        return f"{prompt}-{counter['n']}"

    evaluator = ConsistencyEvaluator(varying_model, runs=3)
    assert not evaluator.check_consistency("pregunta")
