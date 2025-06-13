import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from llmqa.comparator import LLMComparator


def model_a(prompt: str) -> str:
    return f"A:{prompt}"


def model_b(prompt: str) -> str:
    return f"B:{prompt}"


def model_c(prompt: str) -> str:
    return f"C:{prompt}"


def test_compare_outputs():
    comparator = LLMComparator({
        "gpt": model_a,
        "claude": model_b,
        "cohere": model_c,
    })
    results = comparator.compare("hola")
    assert [r.response for r in results] == ["A:hola", "B:hola", "C:hola"]
