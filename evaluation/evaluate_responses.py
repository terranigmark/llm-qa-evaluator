"""Script sencillo para evaluar las respuestas del modelo.

Lee preguntas y respuestas desde JSON y genera un reporte CSV con un porcentaje
simple de coincidencia de palabras clave y hechos esperados.
"""

from __future__ import annotations

import json
import csv
from pathlib import Path
from typing import List, Dict


def load_json(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def evaluate_entry(expected: Dict[str, str], response: Dict[str, str]) -> Dict[str, float]:
    text = response.get("response", "").lower()
    keyword_hits = sum(1 for kw in expected.get("expected_keywords", []) if kw.lower() in text)
    fact_hits = sum(1 for fact in expected.get("expected_facts", []) if fact.lower() in text)
    keywords_total = len(expected.get("expected_keywords", []))
    facts_total = len(expected.get("expected_facts", []))
    return {
        "id": expected.get("id", ""),
        "keyword_match": keyword_hits / keywords_total if keywords_total else 0,
        "fact_match": fact_hits / facts_total if facts_total else 0,
    }


def main() -> None:
    prompts = load_json(Path("prompts/beer_questions.json"))
    outputs = {item["id"]: item for item in load_json(Path("outputs/gpt4_responses.json"))}
    results: List[Dict[str, float]] = []
    for entry in prompts:
        out = outputs.get(entry["id"], {})
        results.append(evaluate_entry(entry, out))

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    csv_path = results_dir / "evaluation_report.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "keyword_match", "fact_match"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Reporte guardado en {csv_path}")


if __name__ == "__main__":
    main()
