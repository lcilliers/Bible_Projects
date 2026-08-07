"""strengthen_closing_set_rules_20260807.py — re-checked `closing.set`'s 5 method rules against
their exact source text (`WA-interpretation-questions-v1.4` Parts A/B/C, re-read fresh, not
trusted from the prior pass's own paraphrase) per the researcher's direct instruction: "ensure that
each of the closing sections (method rules) have configs that comes out of the interpretive
questions that rules the specific rule_key." 3 of 5 already matched their source completely
(`linkages-q7`, `debate-quality-validation`, `open-decisions`) — 2 were compressed enough to lose
real content:

- `insufficiencies-register` dropped Part B.7's own worked example ("e.g. name etymologies").
- `emergent-questions-log` covered Part C item 6's literary-observation half (B.12) but dropped
  Part B.9's own, separate point: an interpretive fork is NOT a researcher decision awaiting a
  ruling — it is carried forward and resolved (or left open) by what the accumulating evidence
  shows, and "the researcher should decide" is reserved for genuine resourcing/data-curation
  choices, not interpretive questions this instrument exists to answer itself.

Direct-write convention (`cfg_method_rule` has no `configmaint.propose` write-grant). Idempotent:
only updates if the live text still matches the OLD (pre-strengthening) wording, so a re-run after
a researcher's own further edit doesn't clobber it.
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

UPDATES = [
    ("closing.set", "insufficiencies-register",
     "Where required data (e.g. name etymologies) is absent from the base extract, name it as an "
     "insufficiency; do not substitute remembered or external knowledge."),
    ("closing.set", "emergent-questions-log",
     "Interpretive forks and genuine literary/structural observations are carried forward here. "
     "An interpretive fork is NOT a researcher decision awaiting a ruling -- it is named where it "
     "bites, weighed against each new data point as the corpus grows, and answered (or left open) "
     "by what the accumulating evidence actually shows, not settled in the abstract before the "
     "evidence is in. \"The researcher should decide\" is reserved for genuine resourcing/"
     "data-curation choices this instrument cannot make for itself, not for interpretive questions "
     "the study itself exists to answer. Not merged with other passages' logs."),
]


def run(conn: sqlite3.Connection) -> dict:
    counts = {"updated": 0, "unchanged": 0}
    for step, rule_key, new_text in UPDATES:
        row = conn.execute(
            "SELECT rule_text FROM cfg_method_rule WHERE step=? AND rule_key=?",
            (step, rule_key)).fetchone()
        if row is None:
            continue
        if row[0] == new_text:
            counts["unchanged"] += 1
            continue
        conn.execute(
            "UPDATE cfg_method_rule SET rule_text=? WHERE step=? AND rule_key=?",
            (new_text, step, rule_key))
        counts["updated"] += 1
    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("migration result:", result)
    conn.close()
