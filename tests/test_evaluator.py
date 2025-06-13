import sys
from pathlib import Path

# Agregar la carpeta raíz al path para poder importar el paquete llmqa
sys.path.append(str(Path(__file__).resolve().parents[1]))

from llmqa.evaluator import LLMEvaluator


def fake_model(prompt: str) -> str:
    # Responde con un mensaje fijo para fines de prueba
    return "Respuesta de prueba sobre cerveza"


def test_basic_score():
    evaluator = LLMEvaluator(fake_model)
    result = evaluator.evaluate_prompt("Pregunta")
    assert result.score["clarity"] == 1.0
    assert result.score["factuality"] == 0.5

from evaluation.evaluate_responses import evaluate_entry


def test_evaluate_entry_keywords_and_facts():
    expected = {
        "id": "Q1",
        "expected_keywords": ["cuerpo", "tostado"],
        "expected_facts": ["cervezas oscuras"]
    }
    response = {"response": "Las porter son cervezas oscuras con cuerpo tostado."}
    result = evaluate_entry(expected, response)
    assert result["keyword_match"] == 1.0
    assert result["fact_match"] == 1.0
