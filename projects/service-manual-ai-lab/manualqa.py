"""Version-aware document QA on a small corpus of fictional service manuals."""

import argparse
from collections import Counter
from contextlib import closing
import json
from pathlib import Path
import re
import sqlite3
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


DATA = Path(__file__).with_name("manuals.json")
SECTIONS = ("overview", "retry", "export", "escalation")
INTENTS = {
    "retry": r"(?:what is (?:the )?)?retry interval|retry upload|how long (?:do i |should i )?wait (?:before retrying|(?:after a )?failed upload)|when can i retry (?:a )?(?:failed )?upload",
    "export": r"export (?:the )?report log|how (?:do|can) i (?:export|download) (?:the )?report log|where (?:is|can i find) (?:the )?report log",
    "escalation": r"escalate (?:upload )?failures|where (?:do i|should i) (?:send|escalate) (?:repeated |consecutive )?upload failures|what should i include in the handoff",
}
NUMBER_WORDS = dict(zip(
    "one two three four five uno dos tres cuatro cinco".split(),
    (1, 2, 3, 4, 5) * 2,
))
UNITS = {"minute": "minute", "minuto": "minute", "hour": "hour", "hora": "hour", "second": "second", "segundo": "second"}


def load_data():
    return json.loads(DATA.read_text(encoding="utf-8"))


def find_manual(manuals, asset, revision):
    return next(m for m in manuals if m["asset"] == asset and m["revision"] == revision)


def route_question(question):
    normalized = " ".join(question.lower().strip().rstrip("?.!").split())
    return next((key for key, pattern in INTENTS.items() if re.fullmatch(pattern, normalized)), None)


def connect_index(manuals):
    index = sqlite3.connect(":memory:")
    index.row_factory = sqlite3.Row
    index.execute("""CREATE VIRTUAL TABLE passages USING fts5(
        body, section UNINDEXED, asset UNINDEXED, revision UNINDEXED,
        status UNINDEXED, locale UNINDEXED
    )""")
    index.executemany("INSERT INTO passages VALUES (?, ?, ?, ?, ?, ?)", (
        (s["text"], s["id"], m["asset"], m["revision"], m["status"], m["locale"])
        for m in manuals for s in m["sections"]
    ))
    return index


def retrieve(index, question, asset, *, section=None):
    terms = re.findall(r"[a-z0-9]+", question.lower())
    stop = {"a", "after", "before", "can", "do", "i", "how", "in", "is", "it", "the", "to", "what", "when", "where", "should", "of"}
    terms = tuple(dict.fromkeys(t for t in terms if t not in stop))
    if not terms:
        return []
    query = " OR ".join(f'"{term}"' for term in terms)
    if section is None:
        # Baseline has the same asset filter but accepts draft and retired versions.
        return index.execute(
            "SELECT * FROM passages WHERE passages MATCH ? AND asset = ? ORDER BY bm25(passages), rowid LIMIT 1",
            (query, asset),
        ).fetchall()
    return index.execute(
        """SELECT * FROM passages WHERE passages MATCH ? AND asset = ? AND section = ?
           AND status = 'released' AND locale = 'en' ORDER BY bm25(passages), rowid""",
        (query, asset, section),
    ).fetchall()


def answer_question(index, manuals, question, asset):
    if not asset:
        return {"status": "clarify", "message": "Select Atlas A1 or Atlas A2 first."}
    section = route_question(question)
    if not section:
        return {"status": "defer", "message": "This question is outside the supported manual workflows."}
    current = [m for m in manuals if m["asset"] == asset and m["locale"] == "en" and m["status"] == "released"]
    if len(current) != 1:
        return {"status": "defer", "message": "A single released source could not be established."}
    hits = retrieve(index, question, asset, section=section)
    if len(hits) != 1:
        return {"status": "defer", "message": "A unique released passage did not match the question."}
    row = hits[0]
    return {
        "status": "cited",
        "quote": row["body"],
        "citation": {"asset": row["asset"], "revision": row["revision"], "section": row["section"]},
    }


def audit_manual(manual):
    sections = manual["sections"]
    counts = Counter(section["id"] for section in sections)
    findings = []
    findings.extend(f"missing section: {section}" for section in SECTIONS if not counts[section])
    findings.extend(f"duplicate section: {section}" for section, count in counts.items() if count > 1)
    for position, section in enumerate(sections, 1):
        if re.search(r"\b(?:TODO|TBD|FIXME)\b", section["text"], re.IGNORECASE):
            findings.append(f"unresolved drafting marker: {section['id']} at position {position}")
        if re.search(r"\bsync key\b", section["text"], re.IGNORECASE):
            findings.append(f"nonstandard term: {section['id']} uses 'sync key'; glossary uses 'sync token'")
    return {"status": "revise" if findings else "checks_passed", "findings": findings}


def protected_values(text):
    variables = Counter(re.findall(r"\{\{[^{}]+\}\}", text))
    urls = Counter(re.findall(r"\]\((https?://[^)]+)\)", text))
    body = re.sub(r"\{\{[^{}]+\}\}|https?://[^\s)]+", "", text.lower())
    values = Counter(int(value) for value in re.findall(r"\b[0-9]+\b", body))
    values.update(NUMBER_WORDS[word] for word in re.findall(r"\b\w+\b", body) if word in NUMBER_WORDS)
    durations = Counter(
        (int(amount), UNITS[unit])
        for amount, unit in re.findall(r"\b(\d+) (minute|minuto|hour|hora|second|segundo)s?\b", body)
    )
    codes = Counter(re.findall(r"\b(?:CSV|JSON|A[12])\b", text))
    return {"variables": variables, "links": urls, "values": values, "durations": durations, "codes": codes}


def audit_translation(source, draft):
    findings = []
    if [s["id"] for s in source] != [s["id"] for s in draft]:
        findings.append("section structure or order changed")
    counts = Counter(section["id"] for section in draft)
    by_id = {section["id"]: section["text"] for section in draft}
    for section in source:
        key, text = section["id"], section["text"]
        if counts[key] != 1:
            findings.append(f"{key}: missing or duplicated Spanish section")
            continue
        localized = by_id[key]
        source_values, draft_values = protected_values(text), protected_values(localized)
        findings.extend(f"{key}: {feature} changed" for feature in source_values if source_values[feature] != draft_values[feature])
        if "sync token" in text.lower() and "token de sincronización" not in localized.lower():
            findings.append(f"{key}: glossary term missing")
    return {"status": "revise" if findings else "human_review", "findings": findings}


class WorkRequest(TypedDict, total=False):
    operation: str
    question: str
    asset: str
    revision: str
    draft: str
    result: dict
    trace: list[str]


def build_workflow(data):
    manuals = data["manuals"]

    def ask(state):
        with closing(connect_index(manuals)) as index:
            result = answer_question(index, manuals, state["question"], state.get("asset"))
        return {"result": result, "trace": ["request", "retrieve_released_passage", "citation_gate"]}

    def audit(state):
        selected = find_manual(manuals, state["asset"], state["revision"])
        return {"result": audit_manual(selected), "trace": ["request", "manual_checks"]}

    def localize(state):
        source = find_manual(manuals, "Atlas A1", "1.4")["sections"]
        draft = data["spanish_drafts"][state["draft"]]
        result = audit_translation(source, draft)
        result["draft"] = draft
        return {"result": result, "trace": ["request", "load_spanish_draft", "localization_checks", "review_gate"]}

    workflow = StateGraph(WorkRequest)
    for operation, handler in {"ask": ask, "audit": audit, "localize": localize}.items():
        workflow.add_node(operation, handler)
        workflow.add_edge(operation, END)
    workflow.add_conditional_edges(START, lambda state: state["operation"], ["ask", "audit", "localize"])
    return workflow.compile()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    ask = commands.add_parser("ask")
    ask.add_argument("question")
    ask.add_argument("--asset", choices=("Atlas A1", "Atlas A2"))
    audit = commands.add_parser("audit")
    audit.add_argument("revision", choices=("1.3", "1.4", "1.5"))
    audit.set_defaults(asset="Atlas A1")
    localize = commands.add_parser("localize")
    localize.add_argument("draft", choices=("complete", "altered"))
    outcome = build_workflow(load_data()).invoke(vars(parser.parse_args()))
    print(json.dumps({"result": outcome["result"], "trace": outcome["trace"]}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
