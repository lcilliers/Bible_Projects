"""prior_capture_config_2305_v1_20261026.py -- escalation #2305 (design
outputs/escalation/2305-prior-work-capture-design-v2-20261026.md, decisions Q1 to Q7 approved 2026-10-26).

1. Table prior_capture_line: the answer to every document line that names a verse (captured, already recorded, not an
   observation), design sec 4. reading_file.capture_status and capture_run_id: where each document stands.
2. Enums: ib_observation.stage prior-capture (Q1), ib_observation.tag unfitted (Q2), prior_capture_line.answer,
   prior_capture_line.reason_class, reading_file.capture_status.
3. Settings prior_capture.stage, prior_capture.unfitted_tag, prior_capture.output_dir.
4. Work package prior-capture (iba/app/ps/Prior-Capture.ps1) with steps prior_capture.prepare, prior_capture.record,
   prior_capture.report (handlers/priorcapture.py), their routed conditions and the record step's write grants.
5. Method rules CP-01 to CP-10 on prior_capture.record (the design's sec 1, 2 and the researcher's rulings).
6. cfg_utility for lib/priorcapture.py, handlers/priorcapture.py, Prior-Capture.ps1 and this script.

Tables and columns are built from their cfg_column rows (lib/db.table_ddl; ALTER for the added columns).
cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.
One transaction.

Usage:
    python iba/app/migration/prior_capture_config_2305_v1_20261026.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2305-PRIOR-CAPTURE-CONFIG-20261026"
MODULE = "prior_capture_config_2305_v1_20261026"
SOURCE = "escalation #2305 (outputs/escalation/2305-prior-work-capture-design-v2-20261026.md)"
FILLED = "iba/app/lib/priorcapture.py (#2305, prior_capture.record)"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"
WP = "prior-capture"
SEE = "see lib/priorcapture.py (escalation #2305)"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None, filled=FILLED):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": filled, "inactive": 0}


T = "prior_capture_line"
GRAIN = "one row per document line that names a verse and per observation it gave (one row for a line that gave none)"
USE = ("#2305: the answer to every line of a study document that names a verse, kept with the capture run so what was "
       "taken from each document, and why the rest was passed over, can be checked line by line (design sec 4). "
       "captured and already recorded rows name the observation; a not an observation row names its reason")
COLS = [
    col(T, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
    col(T, "file_id", 1, "INTEGER", "the document (reading_file)", nn=1, fk="reading_file.id"),
    col(T, "line_no", 2, "INTEGER", "the line in the document, as in reading_ref.line_no", nn=1),
    col(T, "answer", 3, "TEXT", "captured, already recorded or not an observation (design sec 4)", nn=1,
        exp="enum.prior_capture_line.answer"),
    col(T, "reason_class", 4, "TEXT", "on a not an observation line: the class it falls in (design sec 1)",
        exp="enum.prior_capture_line.reason_class"),
    col(T, "reason", 5, "TEXT", "on a not an observation line: why, in words"),
    col(T, "observation_id", 6, "INTEGER", "on a captured or already recorded line: the observation",
        fk="ib_observation.id"),
    col(T, "run_id", 7, "TEXT", "the capture run that wrote the row"),
    col(T, "created_at", 8, "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
    col(T, "created_by", 9, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    col(T, "deleted", 10, "INTEGER", "soft delete: 1 when the answer is no longer live", nn=1, dflt="0"),
]
INDEXES = [("idx_prior_capture_line_file", ["file_id", "line_no"]), ("idx_prior_capture_line_obs", ["observation_id"])]
RF_STATUS = col("reading_file", "capture_status", 12, "TEXT", "#2305: where the document stands in the prior-work "
                "capture: not started, in progress, captured, or nothing to capture", nn=1, dflt="'not started'",
                exp="enum.reading_file.capture_status")
RF_RUN = col("reading_file", "capture_run_id", 13, "TEXT", "#2305: the run that captured the document")
ENUMS = {
    "ib_observation.stage": ["prior-capture"],
    "ib_observation.tag": ["unfitted"],
    "prior_capture_line.answer": ["captured", "already recorded", "not an observation"],
    "prior_capture_line.reason_class": ["heading", "reference list", "hit count", "surface or gloss table",
                                        "scope or method or process record", "pointer with no content",
                                        "weave or quote-check record", "next-steps list"],
    "reading_file.capture_status": ["not started", "in progress", "captured", "nothing to capture"],
    "config_module": ["prior_capture"],
}
STEPS = [  # step, ordinal, kind, does, grants
    ("prior_capture.prepare", 0, "utility", "the prepare JSON of one study document: its lines that name a verse with "
     "the verses resolved, the M- and T-coded occurrences of each verse and the October ids already recorded, for "
     "Claude to fill (read-only)", []),
    ("prior_capture.record", 1, "operations", "the filled prepare JSON written: the observations, their nodes and the "
     "answer to every line, in one transaction; the whole file refused on any problem",
     ["ib_observation", "ib_node", "prior_capture_line", "reading_file"]),
    ("prior_capture.report", 2, "utility", "where the capture stands: documents by status, observations and line "
     "answers by kind (read-only)", []),
]
ON_FAIL = {"refused": ("report-continue", "refused, nothing written -- the reason follows (a usage outcome, not "
                       "recorded as an escalation)")}
SETTINGS = [
    ("prior_capture.stage", json.dumps("prior-capture"), "#2305 Q1: the stage of an observation captured from a "
     "prior document, so the rows stay identifiable as migrated"),
    ("prior_capture.unfitted_tag", json.dumps("unfitted"), "#2305 Q2: the tag of a material observation that fits none "
     "of the eight kinds (reading.observation_parts)"),
    ("prior_capture.output_dir", json.dumps("outputs/prior-capture"), "#2305: where the prepare JSON files and capture "
     "reports are written (versioned per day by lib/filingkit)"),
]
RULES = [  # rule_key, text
    ("CP-01 every-verse-line-is-answered", "Each document is captured whole, in one run: every line that names a verse "
     "gets one answer, captured (with the observation it gave), already recorded (an October ledger id already in "
     "ib_observation, with its observation) or not an observation (with its class and reason: heading, reference "
     "list, hit count, surface or gloss table, scope or method or process record, pointer with no content, weave or "
     "quote-check record, next-steps list). The record is refused while any line is unanswered."),
    ("CP-02 capture-as-written-no-reanalysis", "A prior-work capture records every material observation the document "
     "makes about a verse it names, as written. The verse is not read again, nothing is added, checked, corrected or "
     "rejected; whether an observation is right is not this task's question. Where the document reads beyond the "
     "verse, basis is read."),
    ("CP-03 one-finding-many-nodes", "One finding is one observation; the verses, words, clusters and subgroups it "
     "covers are nodes. A finding's quotations and verse list are its evidence, not further observations. Two "
     "observations are made only where the document says two different things. A finding about other findings is its "
     "own observation, applied to them through traced_observation_id."),
    ("CP-04 no-duplicate-check-across-documents", "Each document is captured on its own, without searching what other "
     "documents gave: the same finding in two documents is two observations, each citing its own document "
     "(researcher, 2026-10-26). The one exception costs no search: an identical live description adds nodes to the "
     "first observation instead of a second."),
    ("CP-05 parts-already-recorded-skipped", "An October ledger id that already has a live observation with that "
     "stable_key is answered already recorded and nothing on it is changed; the parts of those documents October did "
     "not take are captured."),
    ("CP-06 unfitted-tag-for-the-rest", "A material observation that is none of the eight kinds is captured as it "
     "stands with tag unfitted (prior_capture.unfitted_tag), so the rows can be found and sorted later. The wording "
     "is adjusted to the observation structure and the substance is kept."),
    ("CP-07 node-classification-from-the-word", "A node takes its Strong's number, occurrence, cluster and subgroup "
     "from the tables (verse_lexical, cluster_strong, surface_subgroup), never from the document; the document's "
     "disposition (W told, held, data) goes on the node. A word the document names that cannot be placed on one "
     "occurrence is a node without verse_lexical_id and is listed. A node of a finding that names no placeable word "
     "takes the document's cluster. The document's own disposition W, RS (reshapes existing text) and NS (new "
     "structure needed) are written as told with the document's wording in disposition_note; held as held; data as "
     "data (researcher, 2026-10-26, D1 a)."),
    ("CP-09 clusterless-documents-last", "The documents with no cluster are captured last, and only the findings that "
     "have a placeable M- or T-coded word, since a node's cluster cannot be empty (researcher, 2026-10-26, D2 a)."),
    ("CP-10 nodes-on-m-coded-words", "A node is placed on each M-coded word of the verse that the finding's text "
     "names, with that word's own cluster; T-coded words are not noded (a T word that is itself the characteristic "
     "is the T-a case, RA-01) (researcher, 2026-10-26, D3 a)."),
    ("CP-08 chat-sessions-no-api", "The capture is filled by Claude in a chat session on the Sonnet model; no API "
     "route is built or used for it (researcher, 2026-10-26)."),
]
UTILITIES = [
    ("priorcapture", "iba/app/lib/priorcapture.py", "priorcapture.py -- capture of prior study documents into "
     "ib_observation and ib_node: prepare, record and report (#2305, method rules CP-01 to CP-10)", 0, None),
    ("handlers_priorcapture", "iba/app/handlers/priorcapture.py", "priorcapture handler -- work package prior-capture: "
     "steps prior_capture.prepare, prior_capture.record, prior_capture.report (#2305)", 0, None),
    ("Prior-Capture.ps1", "iba/app/ps/Prior-Capture.ps1", "PS entry point of work package prior-capture (#2305): "
     "-Step Prepare|Record|Report -File <document or JSON> [-By]", 1,
     "PS entry point: dispatches through run.py; its settings are the steps' own"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", T):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": T, "grain": GRAIN, "use": USE,
                                                "inactive": 0, "category": "data"}))
    for c in COLS + [RF_STATUS, RF_RUN]:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", c["table_name"],
                   c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for name, cols in INDEXES:
        for i, c in enumerate(cols):
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", T, name, c):
                ops.append(("cfg_index", "insert", {}, {"table_name": T, "name": name, "col": c, "ordinal": i}))
    for name, values in ENUMS.items():
        base = conn.execute("SELECT COALESCE(MAX(ordinal)+1, 0) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        for v in values:
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, v):
                ops.append(("cfg_enum", "insert", {}, {"name": name, "value": v, "ordinal": base, "inactive": 0}))
                base += 1
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {
            "name": WP, "ps_script": "iba/app/ps/Prior-Capture.ps1", "runs_over": "none", "chained": 0,
            "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for step, o, kind, does, grants in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {
                "work_package": WP, "ordinal": o, "step": step,
                "handler": f"iba.app.handlers.priorcapture:{step.split('.', 1)[1]}", "scope": "none",
                "does": f"{does} -- {SEE}", "inactive": 0, "kind": kind}))
        for cond, (path, msg) in ON_FAIL.items():
            if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
                ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": path,
                                                          "resolver": None, "message": msg, "route": "terminal",
                                                          "inactive": 0}))
        for table in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", step, table):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": table, "database": "iba",
                                                              "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": value, "use": use, "module": "prior_capture",
                                                      "inactive": 0}))
    for i, (key, text) in enumerate(RULES):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step='prior_capture.record' AND rule_key=?", key):
            ops.append(("cfg_method_rule", "insert", {}, {
                "step": "prior_capture.record", "rule_key": key, "rule_text": text,
                "source_doc": "#2305 design v2 and researcher rulings 2026-10-26",
                "enforced_by": "iba/app/lib/priorcapture.py", "ordinal": i, "active": 1}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2305: table prior_capture_line, reading_file.capture_status, "
                       f"enums, work package prior-capture, its steps, grants, settings and method rules CP-01 to "
                       f"CP-10; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    rf_cols = {r[1] for r in conn.execute("PRAGMA table_info(reading_file)")}
    print(f"{len(ops)} cfg write(s); {T} live: {T in live}")
    if a.dry_run:
        for t, op, where, set_ in ops:
            what = (set_.get("name") or set_.get("value") or set_.get("module") or set_.get("col")
                    or set_.get("rule_key") or set_.get("step") or set_.get("key") or json.dumps(where))
            print(f"  {op:6} {t:18} {set_.get('table_name', '')} {what}")
        return 0
    try:
        conn.execute("SAVEPOINT prior_capture_config")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if T not in live:
            create_sql, index_sql = table_ddl(cfg, T)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        if "capture_status" not in rf_cols:
            conn.execute("ALTER TABLE reading_file ADD COLUMN capture_status TEXT NOT NULL DEFAULT 'not started'")
        if "capture_run_id" not in rf_cols:
            conn.execute("ALTER TABLE reading_file ADD COLUMN capture_run_id TEXT")
        conn.execute("RELEASE prior_capture_config")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO prior_capture_config")
        conn.execute("RELEASE prior_capture_config")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
