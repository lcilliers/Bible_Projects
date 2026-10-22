"""strand_reading_schema_2172_v1_20261022.py -- escalation #2172, build plan v1 section 5 step 1
(outputs/escalation/2172-process-build-plan-v1-20261022.md; researcher 2026-10-22: "Approved: option
A on all five points of the #2172 build plan. Proceed with the build in the section 5 order.").

1. ib_observation gains the October ledger parts as columns (setting, meaning, implication, chain,
   basis, parties) and run_id (design decision 3); stage 'strand-reading', tag 'key-statement' (one
   row per key statement, the October unit) and enum ib_observation.basis (stated / read).
2. narrative_claim_source gains observation_id; source kind 'observation' (design decision 4).
3. reading_strand, reading_strand_strong, reading_strand_hit (build decision 1): a strand, its word
   family, and one row per hit (a strong in a verse) with its face or the reason it has none.
4. narrative_claim_telling tells a claim per block (build decision 2): rebuilt with section_id (the
   block) and passage_id nullable. Each current passage telling is copied to its section (one row
   per claim and section: 'in full' if any passage told it in full, else 'in part' with the parts
   joined, else 'pointer'); the passage rows stay as history at status 'superseded'. The history
   triggers are rewritten to the block: in_narrative = a current, non-pointer telling in a current
   section; a block's text change logs 'telling changed' for every claim it tells.
5. narrative_register.record (a weave recorded from a chapter file) is retired with its write grants:
   the narrative is written in the database and the chapter file is its export (design v2 sec 2).
   EditSection gains a grant on tellings (a renamed block keeps its tellings).

Tables are built from their cfg_column rows (lib/db.table_ddl) and triggers from cfg_trigger, so the
config is the schema. cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at
its own archive path) in the same transaction. Idempotent. One transaction.

Usage:
    python iba/app/migration/strand_reading_schema_2172_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2172-STRAND-SCHEMA-20261022"
MODULE = "strand_reading_schema_2172_v1_20261022"
SOURCE = "escalation #2172, build plan v1 (outputs/escalation/2172-process-build-plan-v1-20261022.md)"
FILLED_STRAND = "iba/app/lib/strandreading.py"
FILLED_MIG = f"iba/app/migration/archive/{MODULE}.py"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None, filled=FILLED_STRAND):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": filled, "inactive": 0}


NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"

OBS_COLS = [  # name, use
    ("setting", "the key statement's setting: who speaks, the verses around it, the genre (October ledger part)"),
    ("meaning", "what the statement means in its setting (October ledger part)"),
    ("implication", "what it implies for the inner being (October ledger part)"),
    ("chain", "the link the verse itself states to another act or state; NULL where the verse states none"),
    ("basis", "cfg_enum ib_observation.basis: stated (the verse states it) or read (Claude's reading, 'I read')"),
    ("parties", "who acts, toward whom, and who else is named"),
    ("run_id", "the Strand-Reading run that wrote or last changed the row"),
]

NEW_TABLES = {
    "reading_strand": ("one row per strand",
                       "#2172: a strand read through the reading process (Strand-Reading.ps1): its word family "
                       "(reading_strand_strong), its hits (reading_strand_hit) and the escalation that is its record", [
        col("reading_strand", "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
        col("reading_strand", "code", 1, "TEXT", "the strand's short name, lowercase-hyphenated (e.g. flesh-body)", nn=1),
        col("reading_strand", "title", 2, "TEXT", "the strand in words", nn=1),
        col("reading_strand", "cluster_code", 3, "TEXT", "the strand's home cluster (its ib_node rows carry it)",
            nn=1, fk="cluster.cluster_code"),
        col("reading_strand", "escalation_id", 4, "INTEGER", "the escalation that is the strand's record; it "
            "cannot close while the account has a gap (cfg_escalation_requirement strand_account_clean)",
            nn=1, fk="escalation.id"),
        col("reading_strand", "state", 5, "TEXT", "cfg_enum reading_strand_state", nn=1, dflt="'open'",
            exp="enum.reading_strand_state"),
        col("reading_strand", "note", 6, "TEXT", "free note"),
        col("reading_strand", "created_at", 7, "TEXT", "when the row was written (ISO-8601 UTC)", nn=1, dflt=NOW),
        col("reading_strand", "created_by", 8, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    ]),
    "reading_strand_strong": ("one row per strong in a strand's word family",
                              "#2172: the word family a strand reads; its hits are every live verse_lexical "
                              "occurrence of these strongs", [
        col("reading_strand_strong", "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
        col("reading_strand_strong", "strand_id", 1, "INTEGER", "the strand", nn=1, fk="reading_strand.id"),
        col("reading_strand_strong", "strong", 2, "TEXT", "the exact Strong's code (suffixed, zero-padded: H0639G)", nn=1),
        col("reading_strand_strong", "note", 3, "TEXT", "why the word is in the family, or which sense"),
        col("reading_strand_strong", "created_at", 4, "TEXT", "when the row was written (ISO-8601 UTC)", nn=1, dflt=NOW),
        col("reading_strand_strong", "created_by", 5, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    ]),
    "reading_strand_hit": ("one row per hit: a strand strong in a verse",
                           "#2172 safeguard 1: every hit has a face, or a stated reason it has none, before "
                           "the strand can close; the observation the hit went into", [
        col("reading_strand_hit", "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
        col("reading_strand_hit", "strand_id", 1, "INTEGER", "the strand", nn=1, fk="reading_strand.id"),
        col("reading_strand_hit", "verse_id", 2, "INTEGER", "the verse", nn=1, fk="verse.id"),
        col("reading_strand_hit", "strong", 3, "TEXT", "the strong as in verse_lexical", nn=1),
        col("reading_strand_hit", "surface", 4, "TEXT", "the English surface of the hit (verse_lexical)"),
        col("reading_strand_hit", "face", 5, "TEXT", "the face the reading gives the hit: its label and words "
            "(e.g. 'A. With his people as a whole'); NULL until read"),
        col("reading_strand_hit", "parties", 6, "TEXT", "who acts in the hit, toward whom"),
        col("reading_strand_hit", "reason", 7, "TEXT", "why the hit has no face (e.g. another sense of the "
            "word); a read hit has a face or a reason"),
        col("reading_strand_hit", "observation_id", 8, "INTEGER", "the observation the hit went into, if any",
            fk="ib_observation.id"),
        col("reading_strand_hit", "run_id", 9, "TEXT", "the Strand-Reading run that read the hit"),
        col("reading_strand_hit", "created_at", 10, "TEXT", "when the row was written (ISO-8601 UTC)", nn=1, dflt=NOW),
        col("reading_strand_hit", "created_by", 11, "TEXT", WHO, nn=1, dflt="'direct edit'"),
    ]),
}
NEW_UNIQUE = {"reading_strand_strong": ["strand_id", "strong"],
              "reading_strand_hit": ["strand_id", "verse_id", "strong"]}
NEW_INDEX = {"reading_strand_hit": [("idx_reading_strand_hit_verse_id", "verse_id"),
                                    ("idx_reading_strand_hit_observation_id", "observation_id")]}

ENUMS = [("ib_observation.stage", "strand-reading"), ("ib_observation.tag", "key-statement"),
         ("ib_observation.basis", "stated"), ("ib_observation.basis", "read"),
         ("narrative_claim_source_kind", "observation"), ("narrative_telling_status", "superseded"),
         ("reading_strand_state", "open"), ("reading_strand_state", "closed"),
         ("reading_strand_state", "withdrawn")]

TELLING_FILLED = ("iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py; "
                  + FILLED_MIG)

IN_NARR = ("(SELECT EXISTS (SELECT 1 FROM narrative_claim_telling t JOIN narrative_section s ON s.id = t.section_id "
           "WHERE t.claim_id = narrative_claim.id AND t.status = 'current' AND t.kind <> 'pointer' AND "
           "s.last_version IS NULL))")

TRIGGERS = {  # (table, name): (ordinal, sql, use)
    ("narrative_claim_telling", "trg_narrative_telling_ai"): (0, f"""CREATE TRIGGER trg_narrative_telling_ai AFTER INSERT ON narrative_claim_telling
BEGIN
  INSERT INTO narrative_claim_change (claim_id, passage_id, change_date, change_kind, passage_after, chapter_id, section_id, note, basis, provenance, created_by)
  SELECT NEW.claim_id, NEW.passage_id, substr(NEW.created_at, 1, 10), 'telling added', s.block_text, s.chapter_id, NEW.section_id, NEW.kind || COALESCE(': ' || NEW.part_told, ''), 'direct edit', 'trigger trg_narrative_telling_ai', 'trigger' FROM narrative_section s WHERE s.id = NEW.section_id AND NEW.status = 'current';
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id = NEW.claim_id;
END""", "a new current telling logs 'telling added' with the block's text, and sets in_narrative (#2110; per block, #2172)"),
    ("narrative_claim_telling", "trg_narrative_telling_status_au"): (1, f"""CREATE TRIGGER trg_narrative_telling_status_au AFTER UPDATE OF status ON narrative_claim_telling WHEN OLD.status IS NOT NEW.status
BEGIN
  INSERT INTO narrative_claim_change (claim_id, passage_id, change_date, change_kind, passage_before, passage_after, chapter_id, section_id, note, basis, provenance, created_by)
  SELECT NEW.claim_id, NEW.passage_id, date('now'), CASE NEW.status WHEN 'current' THEN 'telling added' ELSE 'telling removed' END, CASE NEW.status WHEN 'current' THEN NULL ELSE s.block_text END, CASE NEW.status WHEN 'current' THEN s.block_text END, s.chapter_id, NEW.section_id, 'status: ' || OLD.status || ' -> ' || NEW.status, 'direct edit', 'trigger trg_narrative_telling_status_au', 'trigger' FROM narrative_section s WHERE s.id = NEW.section_id;
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id = NEW.claim_id;
END""", "a telling removed, restored or superseded is logged with its block; in_narrative follows (#2110; per block, #2172)"),
    ("narrative_claim_telling", "trg_narrative_telling_kind_au"): (2, f"""CREATE TRIGGER trg_narrative_telling_kind_au AFTER UPDATE OF kind, part_told ON narrative_claim_telling WHEN OLD.kind IS NOT NEW.kind OR OLD.part_told IS NOT NEW.part_told
BEGIN
  INSERT INTO narrative_claim_change (claim_id, passage_id, change_date, change_kind, passage_after, chapter_id, section_id, note, basis, provenance, created_by)
  SELECT NEW.claim_id, NEW.passage_id, date('now'), 'telling changed', s.block_text, s.chapter_id, NEW.section_id, 'kind: ' || OLD.kind || ' -> ' || NEW.kind || '; part: ' || COALESCE(OLD.part_told, '-') || ' -> ' || COALESCE(NEW.part_told, '-'), 'direct edit', 'trigger trg_narrative_telling_kind_au', 'trigger' FROM narrative_section s WHERE s.id = NEW.section_id;
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id = NEW.claim_id;
END""", "a telling's kind or part changed is logged with its block (#2110; per block, #2172)"),
    ("narrative_claim_telling", "trg_narrative_telling_ad"): (3, f"""CREATE TRIGGER trg_narrative_telling_ad AFTER DELETE ON narrative_claim_telling
BEGIN
  INSERT INTO narrative_claim_change (claim_id, passage_id, change_date, change_kind, passage_before, chapter_id, section_id, note, basis, provenance, created_by)
  SELECT OLD.claim_id, OLD.passage_id, date('now'), 'telling removed', s.block_text, s.chapter_id, OLD.section_id, 'telling row deleted', 'direct edit', 'trigger trg_narrative_telling_ad', 'trigger' FROM narrative_section s WHERE s.id = OLD.section_id;
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id = OLD.claim_id;
END""", "a deleted telling row (the tool never deletes; Untell sets status removed) is still logged (#2110; per block, #2172)"),
    ("narrative_claim_telling", "trg_narrative_telling_move_au"): (4, f"""CREATE TRIGGER trg_narrative_telling_move_au AFTER UPDATE OF section_id ON narrative_claim_telling WHEN OLD.section_id IS NOT NEW.section_id
BEGIN
  INSERT INTO narrative_claim_change (claim_id, passage_id, change_date, change_kind, passage_after, chapter_id, section_id, section_before_id, note, basis, provenance, created_by)
  SELECT NEW.claim_id, NEW.passage_id, date('now'), 'passage moved', s.block_text, s.chapter_id, NEW.section_id, OLD.section_id, 'telling moved to another block', 'direct edit', 'trigger trg_narrative_telling_move_au', 'trigger' FROM narrative_section s WHERE s.id = NEW.section_id AND NEW.status = 'current' AND s.renamed_from_id IS NOT OLD.section_id;
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id = NEW.claim_id;
END""", "a telling moved to another block is logged with where from; a heading renamed in place (the new section's renamed_from_id is the old one) is not a move (#2172)"),
    ("narrative_section", "trg_narrative_section_block_au"): (0, """CREATE TRIGGER trg_narrative_section_block_au AFTER UPDATE OF block_text ON narrative_section WHEN OLD.block_text IS NOT NULL AND OLD.block_text IS NOT NEW.block_text
BEGIN
  INSERT INTO narrative_claim_change (claim_id, passage_id, change_date, change_kind, passage_before, passage_after, chapter_id, section_id, basis, provenance, created_by)
  SELECT t.claim_id, NULL, date('now'), 'telling changed', OLD.block_text, NEW.block_text, NEW.chapter_id, NEW.id, 'direct edit', 'trigger trg_narrative_section_block_au', 'trigger' FROM narrative_claim_telling t WHERE t.section_id = NEW.id AND t.status = 'current';
END""", "a block rewritten writes one row per claim it tells, with the block before and after (#2172)"),
    ("narrative_section", "trg_narrative_section_retire_au"): (1, f"""CREATE TRIGGER trg_narrative_section_retire_au AFTER UPDATE OF last_version ON narrative_section WHEN (OLD.last_version IS NULL) <> (NEW.last_version IS NULL)
BEGIN
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id IN (SELECT claim_id FROM narrative_claim_telling WHERE section_id = NEW.id);
END""", "a block that leaves (or returns to) the current narrative updates in_narrative of the claims it tells (#2172)"),
    ("narrative_passage", "trg_narrative_passage_retire_au"): (2, f"""CREATE TRIGGER trg_narrative_passage_retire_au AFTER UPDATE OF last_version ON narrative_passage WHEN (OLD.last_version IS NULL) <> (NEW.last_version IS NULL)
BEGIN
  UPDATE narrative_claim SET in_narrative = {IN_NARR} WHERE id IN (SELECT claim_id FROM narrative_claim_telling WHERE passage_id = NEW.id);
END""", "a passage that leaves (or returns to) the current narrative recomputes in_narrative of the claims it told; since #2172 a claim is told per block, so this changes nothing unless a block telling changed (test plan 2.9, #2110)"),
    ("narrative_chapter", "trg_narrative_chapter_renumber_au"): (2, """CREATE TRIGGER trg_narrative_chapter_renumber_au AFTER UPDATE OF chapter_no ON narrative_chapter WHEN OLD.chapter_no IS NOT NEW.chapter_no
BEGIN
  INSERT INTO narrative_claim_change (claim_id, change_date, change_kind, chapter_id, note, basis, provenance, created_by)
  SELECT DISTINCT t.claim_id, date('now'), 'renumbered', NEW.id, 'Ch ' || OLD.chapter_no || ' -> Ch ' || NEW.chapter_no, 'direct edit', 'trigger trg_narrative_chapter_renumber_au', 'trigger' FROM narrative_claim_telling t JOIN narrative_section s ON s.id = t.section_id WHERE s.chapter_id = NEW.id AND t.status = 'current';
END""", "a renumbered chapter is logged on every claim it tells (spec sec3.1, #2110; per block, #2172)"),
}

KIND_RANK = {"in full": 0, "in part": 1, "pointer": 2}


def plan(conn) -> list[tuple]:
    """Every cfg_* write, in order; each guarded so a re-run finds nothing to do."""
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    # 1. ib_observation parts
    n = conn.execute("SELECT COALESCE(MAX(ordinal), -1) FROM cfg_column WHERE database='iba' AND "
                     "table_name='ib_observation'").fetchone()[0]
    for name, use in OBS_COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='ib_observation' AND name=?", name):
            n += 1
            ops.append(("cfg_column", "insert", {}, col("ib_observation", name, n, "TEXT", use,
                        exp="enum.ib_observation.basis" if name == "basis" else None,
                        filled="iba/app/lib/recordingpass.py (record_strand_observations)")))
    # 2. claim source -> observation
    if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='narrative_claim_source' AND "
               "name='observation_id'"):
        m = conn.execute("SELECT MAX(ordinal) FROM cfg_column WHERE database='iba' AND "
                         "table_name='narrative_claim_source'").fetchone()[0]
        ops.append(("cfg_column", "insert", {}, col(
            "narrative_claim_source", "observation_id", m + 1, "INTEGER",
            "the observation the claim rests on, when source_kind is 'observation' (#2172 design decision 4)",
            fk="ib_observation.id", filled="iba/app/lib/narrativeregister.py; iba/app/lib/strandreading.py")))
    # 3. the strand tables
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
    for name, value in ENUMS:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            o = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": o, "inactive": 0}))
    # 4. tellings per block
    if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='narrative_claim_telling' AND "
               "name='section_id'"):
        for name, o in (("created_by", 8), ("created_at", 7), ("status", 6), ("part_told", 5), ("kind", 4),
                        ("passage_id", 3)):
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": "narrative_claim_telling",
                                                 "name": name}, {"ordinal": o}))
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "narrative_claim_telling",
                                             "name": "passage_id"},
                    {"notnull": 0, "use": "the passage that told the claim before #2172 (history, status "
                     "superseded); NULL on a block telling", "filled_by": TELLING_FILLED}))
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "narrative_claim_telling",
                                             "name": "status"},
                    {"use": "cfg_enum narrative_telling_status: current, removed, superseded (a passage "
                     "telling carried by its block's telling, #2172)"}))
        ops.append(("cfg_column", "insert", {}, col(
            "narrative_claim_telling", "section_id", 2, "INTEGER", "the block (narrative_section) that tells the "
            "claim; one current telling per claim and block (#2172)", nn=1, fk="narrative_section.id",
            filled=TELLING_FILLED)))
        ops.append(("cfg_table", "update", {"database": "iba", "name": "narrative_claim_telling"},
                    {"grain": "one row per claim told in a block (passage rows before #2172 are history)",
                     "use": "The link between a claim and the block (narrative_section) that tells it, many to "
                            "many. escalation #2110, spec sec3.5; per block since #2172"}))
        ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": "narrative_claim_telling",
                                                 "col": "section_id", "ordinal": 1}))
        ops.append(("cfg_unique", "update", {"database": "iba", "table_name": "narrative_claim_telling",
                                             "col": "passage_id"}, {"ordinal": 2}))
        ops.append(("cfg_index", "insert", {}, {"table_name": "narrative_claim_telling",
                                                "name": "idx_narrative_claim_telling_section_id",
                                                "col": "section_id", "ordinal": 0}))
    # Record (a weave recorded from a chapter file) is retired: the narrative is written in the
    # database (Strand-Reading.ps1 -Step Rewrite) and the chapter file is its export
    if has("SELECT 1 FROM cfg_step WHERE step='narrative_register.record' AND inactive=0"):
        ops.append(("cfg_step", "update", {"step": "narrative_register.record"}, {"inactive": 1}))
    for (table,) in conn.execute("SELECT table_name FROM cfg_write_grant WHERE writer='narrative_register.record' "
                                 "AND inactive=0").fetchall():
        ops.append(("cfg_write_grant", "update", {"writer": "narrative_register.record", "table_name": table,
                                                  "database": "iba"}, {"inactive": 1}))
    if has("SELECT 1 FROM cfg_write_grant WHERE writer='narrative_register.tell' AND table_name='narrative_passage' "
           "AND inactive=0"):
        ops.append(("cfg_write_grant", "update", {"writer": "narrative_register.tell", "table_name":
                                                  "narrative_passage", "database": "iba"}, {"inactive": 1}))
    # EditSection: the tellings follow a renamed block, and the chapter is published after the change
    for table in ("narrative_claim_telling", "narrative_chapter"):
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer='narrative_register.edit_section' AND "
                   "table_name=?", table):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": "narrative_register.edit_section",
                                                          "table_name": table, "database": "iba", "inactive": 0}))
    if has("SELECT 1 FROM cfg_table WHERE database='iba' AND name='narrative_passage' AND use NOT LIKE '%#2172%'"):
        ops.append(("cfg_table", "update", {"database": "iba", "name": "narrative_passage"}, {
            "use": "History since #2172: the paragraphs that told claims before the narrative was held as blocks "
                   "(narrative_section.block_text). No longer written; a claim is told by a block "
                   "(narrative_claim_telling.section_id). escalation #2110, spec sec3.2"}))
    for (table, name), (o, sql, use) in TRIGGERS.items():
        r = conn.execute("SELECT sql FROM cfg_trigger WHERE database='iba' AND name=?", (name,)).fetchone()
        row = {"database": "iba", "table_name": table, "name": name, "ordinal": o, "sql": sql, "use": use,
               "inactive": 0}
        if r is None:
            ops.append(("cfg_trigger", "insert", {}, row))
        elif r[0] != sql:
            ops.append(("cfg_trigger", "update", {"database": "iba", "name": name},
                        {"sql": sql, "use": use, "ordinal": o}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": FILLED_MIG, "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2172 build step 1: ib_observation parts, claim source "
                       f"observation, reading_strand tables, tellings per block; run_id {RUN_ID}. inactive=1 "
                       f"once applied."}))
    return ops


def rebuild_telling(cfg: Cfg) -> dict:
    """narrative_claim_telling rebuilt from its (updated) cfg_column rows; the passage tellings copied to
    their blocks. Every trigger that names the table is dropped first and rebuilt from cfg_trigger."""
    conn = cfg.conn
    dependents = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='trigger' AND (tbl_name='narrative_claim_telling' OR "
        "sql LIKE '%narrative_claim_telling%')")]
    for name in dependents:
        conn.execute(f'DROP TRIGGER "{name}"')
    create_sql, index_sql = table_ddl(cfg, "narrative_claim_telling", "narrative_claim_telling__new")
    conn.execute(create_sql)
    old = conn.execute("SELECT t.*, p.section_id AS sec FROM narrative_claim_telling t JOIN narrative_passage p "
                       "ON p.id=t.passage_id ORDER BY t.id").fetchall()
    for r in old:
        conn.execute("INSERT INTO narrative_claim_telling__new (id, claim_id, section_id, passage_id, kind, "
                     "part_told, status, created_at, created_by) VALUES (?,?,?,?,?,?,?,?,?)",
                     (r["id"], r["claim_id"], r["sec"], r["passage_id"], r["kind"], r["part_told"],
                      "superseded" if r["status"] == "current" else r["status"], r["created_at"], r["created_by"]))
    groups: dict[tuple, list] = {}
    for r in old:
        if r["status"] == "current":
            groups.setdefault((r["claim_id"], r["sec"]), []).append(r)
    merged = 0
    for (claim_id, sec), rows in sorted(groups.items()):
        kind = min((r["kind"] for r in rows), key=KIND_RANK.__getitem__)
        parts = []
        for r in rows:
            if kind == "in part" and r["kind"] == "in part" and r["part_told"] and r["part_told"] not in parts:
                parts.append(r["part_told"])
        merged += len(rows) > 1
        conn.execute("INSERT INTO narrative_claim_telling__new (claim_id, section_id, passage_id, kind, part_told, "
                     "status, created_by) VALUES (?,?,NULL,?,?,'current','migration')",
                     (claim_id, sec, kind, " / ".join(parts) or None))
    conn.execute("DROP TABLE narrative_claim_telling")
    conn.execute("ALTER TABLE narrative_claim_telling__new RENAME TO narrative_claim_telling")
    for sql in index_sql:
        conn.execute(sql.replace("narrative_claim_telling__new", "narrative_claim_telling"))
    rebuilt = []
    for (table,) in conn.execute("SELECT DISTINCT table_name FROM cfg_trigger WHERE database='iba' AND inactive=0 "
                                 "AND (table_name IN ('narrative_claim_telling', 'narrative_section') OR sql LIKE "
                                 "'%narrative_claim_telling%')").fetchall():
        for sql in cfg.triggers(table):
            name = sql.split()[2]
            if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='trigger' AND name=?", (name,)).fetchone():
                conn.execute(sql)
                rebuilt.append(name)
    conn.execute(f"UPDATE narrative_claim SET in_narrative = {IN_NARR}")
    return {"passage_rows": len(old), "block_rows": len(groups), "merged_groups": merged,
            "triggers_dropped": len(dependents), "triggers_built": len(rebuilt)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    obs_cols = {r[1] for r in conn.execute("PRAGMA table_info(ib_observation)")}
    src_cols = {r[1] for r in conn.execute("PRAGMA table_info(narrative_claim_source)")}
    tel_cols = {r[1] for r in conn.execute("PRAGMA table_info(narrative_claim_telling)")}
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    in_narr_before = conn.execute("SELECT COUNT(*) FROM narrative_claim WHERE in_narrative=1").fetchone()[0]
    print(f"{len(ops)} cfg write(s); telling per block: {'section_id' in tel_cols}; "
          f"strand tables live: {sorted(t for t in NEW_TABLES if t in live)}")
    if a.dry_run:
        return 0
    result = {}
    try:
        conn.execute("SAVEPOINT strand_schema")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for name, _ in OBS_COLS:
            if name not in obs_cols:
                conn.execute(f'ALTER TABLE ib_observation ADD COLUMN "{name}" TEXT')
        if "observation_id" not in src_cols:
            conn.execute('ALTER TABLE narrative_claim_source ADD COLUMN "observation_id" INTEGER '
                         'REFERENCES "ib_observation"("id")')
        for t in NEW_TABLES:
            if t not in live:
                create_sql, index_sql = table_ddl(cfg, t)
                conn.execute(create_sql)
                for sql in index_sql:
                    conn.execute(sql)
        if "section_id" not in tel_cols:
            result = rebuild_telling(cfg)
        else:      # a re-run with trigger SQL changed in config: bring the live triggers in line
            for (table, name), (o, sql, use) in TRIGGERS.items():
                live_sql = conn.execute("SELECT sql FROM sqlite_master WHERE type='trigger' AND name=?",
                                        (name,)).fetchone()
                if live_sql is None or live_sql[0] != sql:
                    conn.execute(f'DROP TRIGGER IF EXISTS "{name}"')
                    conn.execute(sql)
        conn.execute("RELEASE strand_schema")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO strand_schema")
        conn.execute("RELEASE strand_schema")
        raise
    in_narr_after = conn.execute("SELECT COUNT(*) FROM narrative_claim WHERE in_narrative=1").fetchone()[0]
    print(f"applied (run {RUN_ID}): {result}; claims in the narrative {in_narr_before} -> {in_narr_after}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
