"""reading_process_2228_v1_20261023.py -- escalation #2228, the reading process as config (design
outputs/escalation/2228-reading-process-design-v2-20261023.md; researcher 2026-10-23: "D-a - retire started steps,
it has been superceded; D-b - yes. ; D-c - yes; E-d yes").

1. reading and reading_verse (design sec 5): a reading of one scope, its state and gate times; its verses at
   opening. Enum reading_state (open, recorded, synergised, published, withdrawn).
2. The gap types as config (design sec 2): cfg_enum reading_gap_type, and cfg_setting reading.gap_types with
   each type's guide text, phase (recording or synergy) and the table(s) it records into.
3. Work package reading (iba/app/ps/Reading.ps1): steps Open, Record, Check, Synergy, Apply, Publish, Account,
   each with its write grants and its 'refused' route; cfg_report for Account; setting reading.output_dir.
4. The close gate: check kind readings_published -- the escalation that anchors a reading reaches completed or
   closed only when each of its readings is published or withdrawn.
5. D-a: the strand steps are retired (all eight, the work package, their grants and reports, the strand close
   gate, the rule links of Strand-Reading.ps1, which move to Reading.ps1); the four open strands are
   superseded (reading_strand_state 'superseded'), their rows kept and read as table sources.
   lib/strandreading.py stays as the library the reading reuses; its handler and PS script are archived.
6. cfg_utility for the new files and this migration; B:76 names Reading.ps1 for the narrative itself.

Tables are built from their cfg_column rows (lib/db.table_ddl). cfg_* writes through configmaint.apply_logged().
Registers itself (inactive, at its own archive path) in the same transaction. Idempotent. One transaction.

Usage:
    python iba/app/migration/reading_process_2228_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2228-READING-20261023"
MODULE = "reading_process_2228_v1_20261023"
SOURCE = "escalation #2228, reading-process design v2 (outputs/escalation/2228-reading-process-design-v2-20261023.md)"
FILLED = "iba/app/lib/reading.py"
WP = "reading"
SEE = "see lib/reading.py (escalation #2228)"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": FILLED, "inactive": 0}


NEW_TABLES = {
    "reading": ("one row per reading: the work on one scope",
                "#2228: a reading opened from a scope request and served by the escalation that anchors it; it "
                "passes three gates in order (recorded, synergised, published), each checked by Reading.ps1", [
        col("reading", "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
        col("reading", "label", 1, "TEXT", "the reading's short name, lowercase-hyphenated (e.g. anger-bosom); unique",
            nn=1),
        col("reading", "escalation_id", 2, "INTEGER", "the task or issue that anchors the reading; it cannot close "
            "while the reading is not published or withdrawn (check kind readings_published)", nn=1,
            fk="escalation.id"),
        col("reading", "home_cluster", 3, "TEXT", "the cluster its new observations are grounded under (ib_node)",
            nn=1, fk="cluster.cluster_code"),
        col("reading", "request", 4, "TEXT", "the scope request as resolved at opening (JSON, versescope)", nn=1),
        col("reading", "state", 5, "TEXT", "cfg_enum reading_state", nn=1, dflt="'open'", exp="enum.reading_state"),
        col("reading", "gap_file", 6, "TEXT", "the gap JSON written at Open (gate 1's record)"),
        col("reading", "synergy_file", 7, "TEXT", "the synergy JSON written at Synergy (gate 2's record)"),
        col("reading", "synergy_built_at", 8, "TEXT", "when the synergy JSON was built from the tables; Apply refuses "
            "a file that does not carry it"),
        col("reading", "recorded_at", 9, "TEXT", "when gate 1 passed"),
        col("reading", "synergised_at", 10, "TEXT", "when gate 2 passed"),
        col("reading", "published_at", 11, "TEXT", "when gate 3 passed"),
        col("reading", "chapters", 12, "TEXT", "the chapters the reading touched (JSON list of chapter numbers), "
            "filled at Apply"),
        col("reading", "note", 13, "TEXT", "free note"),
        col("reading", "run_id", 14, "TEXT", "the Reading run that last changed the row"),
        col("reading", "created_at", 15, "TEXT", "when the row was written (ISO-8601 UTC)", nn=1, dflt=NOW),
        col("reading", "created_by", 16, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    ]),
    "reading_verse": ("one row per verse in a reading's scope at opening",
                      "#2228: a reading keeps its verses even if the base data moves", [
        col("reading_verse", "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
        col("reading_verse", "reading_id", 1, "INTEGER", "the reading", nn=1, fk="reading.id"),
        col("reading_verse", "verse_id", 2, "INTEGER", "the verse", nn=1, fk="verse.id"),
        col("reading_verse", "routes", 3, "TEXT", "how the scope reached the verse (JSON, versescope routes)"),
        col("reading_verse", "created_at", 4, "TEXT", "when the row was written (ISO-8601 UTC)", nn=1, dflt=NOW),
        col("reading_verse", "created_by", 5, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    ]),
}
NEW_UNIQUE = {"reading": ["label"], "reading_verse": ["reading_id", "verse_id"]}
NEW_INDEX = {"reading_verse": [("idx_reading_verse_verse_id", "verse_id")],
             "reading": [("idx_reading_escalation_id", "escalation_id")]}

GAP_TYPES = {   # type: (phase, records_in, guide)
    "not_read": ("recording", ["ib_observation"],
                 "A verse with no observation and no strand face. Read it in its passage; record what it states "
                 "about the inner being (a new observation), name an existing observation that already covers it, "
                 "or give the reason it holds nothing."),
    "read_in_files_only": ("recording", ["ib_observation"],
                           "A verse the cluster files read (their lines are given) with no observation in the tables. "
                           "Carry the reading into a table: a new observation from what the files say and the verse "
                           "states, an existing observation, or the reason the files' reading holds nothing."),
    "hit_unread": ("recording", ["reading_strand_hit"],
                   "A strand hit with no face and no reason. Give the hit its face (and the observation it goes "
                   "into), or the reason it has none."),
    "meaning_missing": ("recording", ["strong_meaning_tree", "strong_lexicon"],
                        "A word in scope with no meaning senses (or, for Greek, no Mounce entry). Pull it through "
                        "the spine route and name the row, or give the reason it is not needed for this reading."),
    "open_item": ("recording", ["ib_observation", "escalation_thread_item_response"],
                  "An open item that matches the scope: read for what it asks, and record what the reading found "
                  "(an observation, or a response of kind touched). It is not closed here: closing is decided in "
                  "synergy (gate 2)."),
    "observed_no_claim": ("synergy", ["narrative_claim", "ib_observation"],
                          "An observation no current claim rests on: carry it by a claim, or dispose of it (held on "
                          "an item, silent, withdrawn) with a reason. Gate 2's work, from the tables."),
    "claim_not_told": ("synergy", ["narrative_claim_telling"],
                       "A current claim no block tells: tell it in a block, or hold it with a reason. Gate 2's work, "
                       "from the tables."),
}
ENUMS = ([("reading_state", v) for v in ("open", "recorded", "synergised", "published", "withdrawn")]
         + [("reading_gap_type", v) for v in GAP_TYPES]
         + [("reading_strand_state", "superseded"), ("config_module", "reading"),
            ("escalation_requirement_check_kind", "readings_published")])

NARR = ["narrative_claim", "narrative_claim_source", "narrative_claim_telling", "narrative_claim_change"]
REWRITE = ["narrative_update", "narrative_update_ref", "narrative_section", "narrative_claim_telling",
           "narrative_claim_change", "narrative_citation", "narrative_chapter", "verse_meta"]
ITEMS = ["escalation_thread_item", "escalation_thread_item_verse"]
STEPS = [  # step, does, write grants
    ("open", "a reading opened on a scope (the selectors of Verse-Scope.ps1; the 2,500 review applies): its verses "
     "kept, the scope collated, and the gap JSON written, one section per gap type of the recording phase",
     ["reading", "reading_verse"]),
    ("record", "gate 1 work: the gap JSON's records written (new observations grounded and quote-checked, faces on "
     "strand hits, responses on open items, new open items through the open-item tool) and the ids written back "
     "into the file", ["ib_observation", "ib_node", "reading_strand_hit", "reading"] + ITEMS),
    ("check", "the gate the reading is at, checked from the tables: gate 1 (every gap item has an id that exists or "
     "a reason; the verses are then marked analysed) or gate 2 (every observation carried or disposed, every claim "
     "told or held, every matched open item settled)", ["reading", "verse_meta"]),
    ("synergy", "gate 2 input: the synergy JSON built by reading all the tables for the scope (observations, claims, "
     "blocks, matched open items), never memory", ["reading"]),
    ("apply", "gate 2 work: the synergy JSON written -- claims new, edited, withdrawn, each source naming its "
     "observation; dispositions; tellings; blocks rewritten whole; open items settled or carried forward",
     sorted(set(NARR + REWRITE + ["ib_observation", "reading"] + ITEMS))),
    ("publish", "gate 3: the chapters the reading touched published from the database, copied to the "
     "learning4comfort inbox and checked byte-identical", ["narrative_chapter", "reading"]),
    ("account", "the reading from the tables: its state, each gate's gaps (read-only)", []),
]
REPORTS = {"account": "Reading account"}
SETTINGS = [
    ("reading.output_dir", "outputs/reading",
     "where Reading.ps1 writes each reading's gap JSON, synergy JSON and account, one folder per reading (escalation "
     "#2228)"),
    ("reading.gap_types", {k: {"phase": p, "records_in": t, "guide": g} for k, (p, t, g) in GAP_TYPES.items()},
     "the reading's gap types (cfg_enum reading_gap_type): each one's phase (recording: in the gap JSON, gate 1; "
     "synergy: gate 2), the table(s) it records into and the guide text written into its section; adding a gap type "
     "is an enum value and an entry here (escalation #2228, design v2 sec 2)"),
]
UTILITIES = [
    ("reading", "iba/app/lib/reading.py", "reading.py -- the reading process (escalation #2228): a reading of one "
     "scope through three gates -- Open (scope, collation, gap JSON), Record and Check (gate 1), Synergy, Apply and "
     "Check (gate 2, from the tables), Publish (gate 3) -- and Account; reuses strandreading, recordingpass, "
     "narrativeregister, openitem and versecollate.", 0, None),
    ("handlers_reading", "iba/app/handlers/reading.py", "handlers/reading.py -- the run.py handlers for work package "
     "reading (one per Reading.ps1 step); the logic is in lib/reading.py (escalation #2228).", 0, None),
    ("Reading.ps1", "iba/app/ps/Reading.ps1", "PS entry point for the reading process (escalation #2228); every step "
     "dispatches through run.py, work package reading.", 1, "thin wrapper; config is read by the handlers through run.py"),
]
GATE_MSG = ("the escalation that anchors a reading reaches completed or closed only when each of its readings is "
            "published or withdrawn -- #2228 (Reading.ps1 -Step Account lists the gaps)")
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
B76_OLD = "`Strand-Reading.ps1` (the narrative itself: -Step Rewrite)"
B76_NEW = "`Reading.ps1` (the narrative itself: -Step Apply)"
STRAND_NOTE = ("superseded by the reading process (#2228 D-a, researcher 2026-10-23): its rows are kept and read as "
               "table sources; its unread hits and open items are the gaps of the readings that reach them")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    # 1. tables
    for t, (grain, use, cols) in NEW_TABLES.items():
        if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
            ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": grain, "use": use,
                                                    "inactive": 0, "category": "data"}))
        for c in cols:
            if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", t, c["name"]):
                ops.append(("cfg_column", "insert", {}, c))
    for t, key in NEW_UNIQUE.items():
        for i, c in enumerate(key):
            if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", t, c):
                ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": t, "col": c, "ordinal": i}))
    for t, idx in NEW_INDEX.items():
        for name, c in idx:
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", t, name):
                ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": name, "col": c, "ordinal": 0}))
    # 2. enums and settings
    for name, value in ENUMS:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            o = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": o, "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "module": "reading",
                                                      "inactive": 0, "use": use}))
    # 3. work package and steps
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Reading.ps1",
                                                       "runs_over": "none", "chained": 0, "inactive": 0}))
    for i, (step, does, grants) in enumerate(STEPS):
        sid = f"reading.{step}"
        if not has("SELECT 1 FROM cfg_step WHERE step=?", sid):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": sid,
                                                   "handler": f"iba.app.handlers.reading:{step}", "scope": "none",
                                                   "does": f"{does} -- {SEE}", "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", sid):
            ops.append(("cfg_on_fail", "insert", {}, {"step": sid, "condition": "refused", "path": "report-continue",
                                                      "resolver": None, "message": REFUSED, "route": "terminal",
                                                      "inactive": 0}))
        for t in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", sid, t):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": sid, "table_name": t, "database": "iba",
                                                              "inactive": 0}))
        if step in REPORTS and not has("SELECT 1 FROM cfg_report WHERE step=?", sid):
            ops.append(("cfg_report", "insert", {}, {"step": sid, "title": REPORTS[step], "show_toc": 0,
                                                     "footer_text": None, "output_kind": "md", "naming_scheme": "dated",
                                                     "archive_dir": "archive", "inactive": 0}))
    # 4. the close gate
    for action in ("update", "resolve_self_correctable"):
        if not has("SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND check_kind='readings_published'",
                   action):
            ops.append(("cfg_escalation_requirement", "insert", {}, {
                "action": action, "field": "state", "condition_key": "always", "message": GATE_MSG, "active": 1,
                "check_kind": "readings_published"}))
        if has("SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND check_kind='strand_account_clean' AND "
               "active=1", action):
            ops.append(("cfg_escalation_requirement", "update", {"action": action, "check_kind": "strand_account_clean"},
                        {"active": 0}))
    # 5. D-a: the strand steps retired
    if has("SELECT 1 FROM cfg_work_package WHERE name='strand-reading' AND inactive=0"):
        ops.append(("cfg_work_package", "update", {"name": "strand-reading"}, {"inactive": 1}))
    for (sid,) in conn.execute("SELECT step FROM cfg_step WHERE work_package='strand-reading' AND inactive=0").fetchall():
        ops.append(("cfg_step", "update", {"step": sid}, {"inactive": 1}))
    for sid, t in conn.execute("SELECT writer, table_name FROM cfg_write_grant WHERE writer LIKE 'strand_reading.%' "
                               "AND inactive=0").fetchall():
        ops.append(("cfg_write_grant", "update", {"writer": sid, "table_name": t, "database": "iba"}, {"inactive": 1}))
    for sid, cond in conn.execute("SELECT step, condition FROM cfg_on_fail WHERE step LIKE 'strand_reading.%' AND "
                                  "inactive=0").fetchall():
        ops.append(("cfg_on_fail", "update", {"step": sid, "condition": cond}, {"inactive": 1}))
    for (sid,) in conn.execute("SELECT step FROM cfg_report WHERE step LIKE 'strand_reading.%' AND inactive=0").fetchall():
        ops.append(("cfg_report", "update", {"step": sid}, {"inactive": 1}))
    for (ref,) in conn.execute("SELECT rule_ref FROM cfg_rule_scope WHERE scope_kind='ps' AND "
                               "scope_value='Strand-Reading.ps1' AND inactive=0").fetchall():
        ops.append(("cfg_rule_scope", "update", {"rule_ref": ref, "scope_kind": "ps",
                                                 "scope_value": "Strand-Reading.ps1"}, {"inactive": 1}))
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value='Reading.ps1'", ref):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": ref, "scope_kind": "ps",
                                                         "scope_value": "Reading.ps1", "inactive": 0}))
    for ref in ("B:114",):
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value='Reading.ps1'", ref):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": ref, "scope_kind": "ps",
                                                         "scope_value": "Reading.ps1", "inactive": 0}))
    for module, path in (("handlers_strandreading", "iba/app/handlers/archive/strandreading.py"),
                         ("Strand-Reading.ps1", "iba/app/ps/archive/Strand-Reading.ps1")):
        if has("SELECT 1 FROM cfg_utility WHERE module=? AND inactive=0", module):
            ops.append(("cfg_utility", "update", {"module": module}, {
                "inactive": 1, "file_path": path,
                "purpose": conn.execute("SELECT purpose FROM cfg_utility WHERE module=?", (module,)).fetchone()[0]
                + " RETIRED 2026-10-23 (#2228 D-a): superseded by the reading process (Reading.ps1)."}))
    r = conn.execute("SELECT purpose FROM cfg_utility WHERE module='strandreading'").fetchone()
    if r and "#2228" not in r[0]:
        ops.append(("cfg_utility", "update", {"module": "strandreading"}, {
            "purpose": "strandreading.py -- the strand library (escalation #2172): its steps are retired (#2228 D-a) and "
                       "its functions are reused by the reading process (lib/reading.py): observation and hit recording, "
                       "derivation of claims and dispositions, open items, related blocks. gate_message() stays for the "
                       "superseded strands' history."}))
    # 6. B:76, the new files, this migration
    r = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=76").fetchone()
    if r and B76_OLD in r[0]:
        ops.append(("cfg_behaviour_rule", "update", {"id": 76}, {"rule_text": r[0].replace(B76_OLD, B76_NEW)}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2228: the reading process (tables reading, reading_verse; "
                       f"gap types; work package reading and its steps; the readings_published gate) and the strand "
                       f"steps retired (D-a); run_id {RUN_ID}. inactive=1 once applied."}))
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
    open_strands = conn.execute("SELECT COUNT(*) FROM reading_strand WHERE state='open'").fetchone()[0]
    print(f"{len(ops)} cfg write(s); reading tables live: {sorted(t for t in NEW_TABLES if t in live)}; "
          f"open strands: {open_strands}")
    if a.dry_run or (not ops and all(t in live for t in NEW_TABLES) and not open_strands):
        return 0
    try:
        conn.execute("SAVEPOINT reading_process")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for t in NEW_TABLES:
            if t not in live:
                create_sql, index_sql = table_ddl(cfg, t)
                conn.execute(create_sql)
                for sql in index_sql:
                    conn.execute(sql)
        conn.execute("UPDATE reading_strand SET state='superseded', note=COALESCE(note || '; ', '') || ? "
                     "WHERE state='open'", (STRAND_NOTE,))
        conn.execute("RELEASE reading_process")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO reading_process")
        conn.execute("RELEASE reading_process")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); {open_strands} strand(s) superseded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
