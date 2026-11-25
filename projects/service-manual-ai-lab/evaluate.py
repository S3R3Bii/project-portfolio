"""Run a disclosed regression suite and emit case-level evidence as JSON."""

from contextlib import closing
import json

from manualqa import build_workflow, connect_index, load_data, retrieve


# Authored examples use fictional manuals. Expected source and value are fixed
# independently of retrieval scores. This is a regression set, not a holdout.
QA_CASES = (
    ("retired-value-trap", "Atlas A1", "What is the retry interval?", "1.4", "retry", "15 minutes"),
    ("retry-paraphrase", "Atlas A1", "How long should I wait before retrying?", "1.4", "retry", "15 minutes"),
    ("different-asset", "Atlas A2", "When can I retry a failed upload?", "2.0", "retry", "20 minutes"),
    ("csv-export", "Atlas A1", "How do I export the report log?", "1.4", "export", "Download CSV"),
    ("json-export", "Atlas A2", "Where can I find the report log?", "2.0", "export", "Export JSON"),
    ("a1-escalation", "Atlas A1", "What should I include in the handoff?", "1.4", "escalation", "{{ticket_id}}"),
    ("a2-escalation", "Atlas A2", "Where should I send repeated upload failures?", "2.0", "escalation", "service queue"),
    ("unknown", "Atlas A1", "How do I reset the administrator password?", None, None, "defer"),
    ("unsupported-retry-detail", "Atlas A1", "What is the retry interval during maintenance?", None, None, "defer"),
    ("unsupported-compound", "Atlas A2", "How do I export the report log and upload it elsewhere?", None, None, "defer"),
    ("underspecified-asset", None, "What is the retry interval?", None, None, "clarify"),
)


def evaluate(data):
    graph = build_workflow(data)
    results = []
    with closing(connect_index(data["manuals"])) as index:
        for name, asset, question, revision, section, expected in QA_CASES:
            response = graph.invoke({"operation": "ask", "asset": asset, "question": question})["result"]
            baseline = retrieve(index, question, asset) if asset else []
            passage = dict(baseline[0]) if baseline else None
            if revision:
                citation = {"asset": asset, "revision": revision, "section": section}
                correct = response.get("citation") == citation and expected in response.get("quote", "")
                baseline_correct = bool(passage and all(passage[k] == v for k, v in citation.items()) and expected in passage["body"])
            else:
                correct = response["status"] == expected
                baseline_correct = not passage
            results.append({
                "case": name, "asset": asset, "question": question, "expected": expected,
                "expected_revision": revision, "expected_section": section,
                "guarded_correct": correct, "baseline_correct": baseline_correct,
                "guarded_response": response, "baseline_passage": passage,
            })
    return {
        "cases": results,
        "totals": {
            "cases": len(results),
            "answerable_cases": sum(row[3] is not None for row in QA_CASES),
            "guarded_correct": sum(row["guarded_correct"] for row in results),
            "baseline_correct": sum(row["baseline_correct"] for row in results),
        },
    }


if __name__ == "__main__":
    print(json.dumps(evaluate(load_data()), indent=2, ensure_ascii=True))
