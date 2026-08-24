"""prose_change_log_build_v1_20260824.py — ONE-OFF, idempotent: builds escalation #836's approved
proposal (`iba/docs/prose-change-log-proposal-v3-20260824.md`).

Two databases, one build:

`bible_research.db` — schema (record_change_log new table; prose_section/prose_section_type get
Model A's version/updated_at treatment) + the one-time migration (proposal §9): the 91 existing
superseded prose_section rows are logged then hard-deleted (researcher-instructed one-time
exception to the standing no-physical-delete convention, matching #833's own precedent); the 949
currently-live prose_section rows and all 108 prose_section_type rows get a baseline
record_change_log row each (payload=NULL, change_reason='migration baseline') so their new
`version` column has a real log id to point at from day one.

Real correctness detail found live, not assumed from the design docs: 4 of the 91 superseded rows
sit in 2-hop supersede chains (e.g. id 45 -> 52 -> 54), not simple 1-hop pairs. Each superseded
row's migration log entry uses `target_id` = the FINAL live row at the end of its chain (proposal
§9 step 1: "the row that replaced it") -- not just its immediate successor, which in these 4 cases
is itself also being hard-deleted.

`iba.db` (governance) — cfg_table/cfg_column for record_change_log + the literal deltas for the two
revised tables, cfg_enum for change_type/status, cfg_write_grant, and 4 cfg_behaviour_rule rows, all
per the proposal's §11-§14 literal content.

    python -m iba.app.migration.prose_change_log_build_v1_20260824
"""

from __future__ import annotations

import gzip
import json
import sqlite3
import sys
from datetime import datetime, timezone

from ..lib.cfg import Cfg, DB_PATH

MIGRATION_SOURCE = "migration/prose_change_log_build_v1_20260824.py"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve_final_live_id(rows: dict[int, dict], start_id: int) -> int:
    """Walk supersede chains (superseded_by_id) to the terminal live row --
    proposal §9 step 1's target_id. Guards against a malformed cycle."""
    seen = set()
    cur_id = start_id
    while rows[cur_id]["superseded_by_id"] is not None:
        if cur_id in seen:
            raise RuntimeError(f"cycle detected in supersede chain starting at {start_id}")
        seen.add(cur_id)
        cur_id = rows[cur_id]["superseded_by_id"]
    return cur_id


def _snapshot_payload(row: dict) -> bytes:
    fields = {k: row[k] for k in
              ("heading", "body", "word_count", "status", "author", "approved_at",
               "approved_by", "metadata_json", "source_file", "created_at", "version")}
    return gzip.compress(json.dumps(fields, default=str).encode("utf-8"))


def _schema_and_migration_side(report: list[str]) -> None:
    conn = sqlite3.connect(Cfg().database_path("bible_research"))
    conn.row_factory = sqlite3.Row

    already_built = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='record_change_log'"
    ).fetchone()

    if not already_built:
        conn.execute("""
            CREATE TABLE record_change_log (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                target_table    TEXT    NOT NULL,
                target_id       INTEGER NOT NULL,
                change_type     TEXT    NOT NULL CHECK (change_type IN ('insert','change','delete')),
                change_datetime TEXT    NOT NULL,
                change_source   TEXT,
                change_reason   TEXT,
                changed_by      TEXT    NOT NULL,
                status          TEXT    NOT NULL DEFAULT 'change_applied'
                                    CHECK (status IN ('change_proposed','change_applied','declined')),
                payload         BLOB
            )
        """)
        conn.execute(
            "CREATE INDEX idx_record_change_log_target ON record_change_log (target_table, target_id)"
        )
        report.append("bible_research.db: record_change_log table + index created")
    else:
        report.append("bible_research.db: record_change_log already exists -- skipping schema+migration"
                       " (idempotent no-op; re-run after manually dropping it if a redo is intended)")
        conn.close()
        return

    ps_cols = {r[1] for r in conn.execute('PRAGMA table_info("prose_section")')}
    if "updated_at" not in ps_cols:
        conn.execute("ALTER TABLE prose_section ADD COLUMN updated_at TEXT")
        report.append("bible_research.db: prose_section.updated_at added")

    pst_cols = {r[1] for r in conn.execute('PRAGMA table_info("prose_section_type")')}
    if "version" not in pst_cols:
        conn.execute("ALTER TABLE prose_section_type ADD COLUMN version INTEGER")
        report.append("bible_research.db: prose_section_type.version added")
    if "updated_at" not in pst_cols:
        conn.execute("ALTER TABLE prose_section_type ADD COLUMN updated_at TEXT")
        report.append("bible_research.db: prose_section_type.updated_at added")

    # ── Snapshot all prose_section content BEFORE dropping supersedes_id/
    #    superseded_by_id/source_file -- needed for both the migration payloads
    #    and the chain walk. ──────────────────────────────────────────────────
    all_rows = {
        r["id"]: dict(r) for r in conn.execute(
            "SELECT id, registry_id, section_type_id, heading, body, word_count, status, "
            "version, supersedes_id, superseded_by_id, author, created_at, approved_at, "
            "approved_by, metadata_json, source_file, delete_flagged FROM prose_section"
        )
    }
    superseded_ids = [rid for rid, r in all_rows.items() if r["superseded_by_id"] is not None]
    live_ids = [rid for rid, r in all_rows.items() if r["superseded_by_id"] is None]
    type_ids = [r["id"] for r in conn.execute("SELECT id FROM prose_section_type")]

    now = _now()

    # ── Step 1 (proposal §9): the superseded rows -> log rows, then hard delete.
    multi_hop = []
    for old_id in superseded_ids:
        row = all_rows[old_id]
        final_id = _resolve_final_live_id(all_rows, old_id)
        if row["superseded_by_id"] != final_id:
            multi_hop.append((old_id, row["superseded_by_id"], final_id))
        conn.execute(
            """INSERT INTO record_change_log
               (target_table, target_id, change_type, change_datetime, change_source,
                change_reason, changed_by, status, payload)
               VALUES ('prose_section', ?, 'change', ?, ?, 'migration', 'claude_code',
                       'change_applied', ?)""",
            (final_id, now, MIGRATION_SOURCE, _snapshot_payload(row)),
        )
    conn.execute(
        f"DELETE FROM prose_section WHERE id IN ({','.join('?' * len(superseded_ids))})",
        superseded_ids,
    )
    report.append(f"bible_research.db: {len(superseded_ids)} superseded prose_section rows logged "
                   f"and hard-deleted ({len(multi_hop)} via a multi-hop chain, resolved to their "
                   f"final live row, not their immediate successor)")

    # ── Step 2 (proposal §9): baseline backfill for every row that survives. ──
    for sid in live_ids:
        cur = conn.execute(
            """INSERT INTO record_change_log
               (target_table, target_id, change_type, change_datetime, change_source,
                change_reason, changed_by, status, payload)
               VALUES ('prose_section', ?, 'insert', ?, ?, 'migration baseline', 'claude_code',
                       'change_applied', NULL)""",
            (sid, now, MIGRATION_SOURCE),
        )
        conn.execute(
            "UPDATE prose_section SET version = ?, updated_at = ? WHERE id = ?",
            (cur.lastrowid, now, sid),
        )
    report.append(f"bible_research.db: {len(live_ids)} live prose_section rows got a baseline "
                   f"record_change_log row + version pointer")

    for tid in type_ids:
        cur = conn.execute(
            """INSERT INTO record_change_log
               (target_table, target_id, change_type, change_datetime, change_source,
                change_reason, changed_by, status, payload)
               VALUES ('prose_section_type', ?, 'insert', ?, ?, 'migration baseline', 'claude_code',
                       'change_applied', NULL)""",
            (tid, now, MIGRATION_SOURCE),
        )
        conn.execute(
            "UPDATE prose_section_type SET version = ?, updated_at = ? WHERE id = ?",
            (cur.lastrowid, now, tid),
        )
    report.append(f"bible_research.db: {len(type_ids)} prose_section_type rows got a baseline "
                   f"record_change_log row + version pointer")

    # ── Drop the 3 partial indexes that reference the retired columns --
    #    found live during testing, not in the design docs. idx_ps_supersedes
    #    indexes supersedes_id directly; idx_ps_registry_type_current and
    #    idx_ps_status both filter WHERE superseded_by_id IS NULL (the old
    #    "current row" predicate) -- SQLite refuses to drop a column an index
    #    references, and Model A makes that predicate meaningless anyway
    #    (every row is current once the superseded ones are removed). ───────
    conn.execute("DROP INDEX IF EXISTS idx_ps_supersedes")
    conn.execute("DROP INDEX IF EXISTS idx_ps_registry_type_current")
    conn.execute("DROP INDEX IF EXISTS idx_ps_status")
    report.append("bible_research.db: 3 partial indexes referencing the retired columns dropped "
                   "(idx_ps_supersedes, idx_ps_registry_type_current, idx_ps_status)")

    # ── Drop the 3 retired columns, now that everything above (including the
    #    indexes) has stopped referencing them. ─────────────────────────────
    conn.execute("ALTER TABLE prose_section DROP COLUMN supersedes_id")
    conn.execute("ALTER TABLE prose_section DROP COLUMN superseded_by_id")
    conn.execute("ALTER TABLE prose_section DROP COLUMN source_file")
    report.append("bible_research.db: prose_section.supersedes_id/superseded_by_id/source_file dropped")

    # ── Recreate the two "current row" indexes without the now-meaningless
    #    superseded_by_id predicate -- delete_flagged=0 is the only remaining
    #    "current" filter under Model A. ─────────────────────────────────────
    conn.execute(
        "CREATE INDEX idx_ps_registry_type_current ON prose_section(registry_id, section_type_id) "
        "WHERE delete_flagged = 0"
    )
    conn.execute(
        "CREATE INDEX idx_ps_status ON prose_section(status) WHERE delete_flagged = 0"
    )
    report.append("bible_research.db: idx_ps_registry_type_current/idx_ps_status recreated "
                   "against delete_flagged=0 only (their old superseded_by_id IS NULL predicate "
                   "is meaningless under Model A -- every row is current)")

    conn.commit()
    conn.close()


def _iba_config_side(report: list[str]) -> None:
    conn = sqlite3.connect(DB_PATH)

    # ── cfg_table (§11) ──────────────────────────────────────────────────────
    if not conn.execute(
            "SELECT 1 FROM cfg_table WHERE database='bible_research' AND name='record_change_log'"
    ).fetchone():
        conn.execute(
            "INSERT INTO cfg_table (database, name, grain, \"use\", inactive) VALUES "
            "('bible_research','record_change_log','one row per change event against a covered "
            "target row',?,0)",
            ("Generic, project-wide change-audit log for content tables under versioning "
             "discipline (prose_section, prose_section_type to start). Captures the state a "
             "change overwrote -- a target row's own version column is a literal pointer to this "
             "table's id, not an incrementing counter. Shape-generic (target_table/target_id) so "
             "other tables can adopt it later without a schema change; only the two prose tables "
             "are wired to write to it in this build. Escalation #836.",))
        report.append("iba.db: cfg_table row for record_change_log added")
    else:
        report.append("iba.db: cfg_table row for record_change_log already present")

    # ── cfg_column: record_change_log's own 10 columns (§11) ────────────────
    rcl_columns = [
        ("id", 1, "INTEGER", 1, 1,
         "Own PK. The value written into a covered target row's version column."),
        ("target_table", 2, "TEXT", 0, 1,
         "Which table this entry describes a change against."),
        ("target_id", 3, "TEXT", 0, 1,
         "Which row of target_table this entry describes. Not a hard FK -- deliberately "
         "generic across tables."),
        ("change_type", 4, "TEXT", 0, 1,
         "insert / change / delete, CHECK-constrained. See escalation #836 proposal sec 6 for "
         "the mapping against every existing write operation."),
        ("change_datetime", 5, "TEXT", 0, 1,
         "When the change was applied (system time, ISO-8601 UTC) -- not the underlying "
         "event's own real-world date."),
        ("change_source", 6, "TEXT", 0, 0,
         "File name, if driven from an input file; otherwise the originating script/module "
         "identifier."),
        ("change_reason", 7, "TEXT", 0, 0,
         "Free text, not enum-constrained. Population rule: flag type for a flag-driven "
         "change; otherwise the change's own source reference."),
        ("changed_by", 8, "TEXT", 0, 1,
         "Who/what executed the change. Distinct from prose_section.author (authorial voice) "
         "and .approved_by (accountable sign-off)."),
        ("status", 9, "TEXT", 0, 1,
         "change_proposed / change_applied / declined, CHECK-constrained. Default "
         "change_applied."),
        ("payload", 10, "BLOB", 0, 0,
         "Gzip-compressed JSON. The prior content this change overwrote or removed -- never "
         "the resulting content. NULL for insert events and migration-baseline rows."),
    ]
    for name, ordinal, typ, is_pk, notnull, use in rcl_columns:
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='bible_research' "
                "AND table_name='record_change_log' AND name=?", (name,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, "
                "inactive) VALUES ('bible_research','record_change_log',?,?,?,?,?,0,NULL,NULL,"
                "?,NULL,NULL,?,0)",
                (name, ordinal, typ, is_pk, notnull, use, MIGRATION_SOURCE))
    report.append("iba.db: cfg_column rows for record_change_log's 10 columns added (idempotent)")

    # ── cfg_column deltas for prose_section (§11) ────────────────────────────
    for col in ("supersedes_id", "superseded_by_id", "source_file"):
        conn.execute(
            "UPDATE cfg_column SET inactive=1 WHERE database='bible_research' "
            "AND table_name='prose_section' AND name=?", (col,))
    conn.execute(
        "UPDATE cfg_column SET \"use\"=? WHERE database='bible_research' "
        "AND table_name='prose_section' AND name='version'",
        ("A literal pointer to record_change_log.id -- the log row describing this section's "
         "own most recent change -- not an incrementing per-item counter. Corrected 2026-08-24 "
         "(escalation #836); prior mixed-type legacy values ('1_0'/'v1' strings) were resolved "
         "by the migration, every row now carries a fresh pointer.",))
    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE database='bible_research' "
            "AND table_name='prose_section' AND name='updated_at'").fetchone():
        conn.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, "
            "inactive) VALUES ('bible_research','prose_section','updated_at',20,'TEXT',0,0,0,"
            "NULL,NULL,?,NULL,NULL,?,0)",
            ("When this row was last written, touched on every write path including "
             "session_a_replace -- the gap that motivated this table's versioning rebuild "
             "(escalation #836). created_at is reserved for true original-creation time only.",
             MIGRATION_SOURCE))
    report.append("iba.db: cfg_column deltas for prose_section applied "
                   "(3 retired -> inactive, version.use corrected, updated_at added)")

    # ── cfg_column additions for prose_section_type (§11) ───────────────────
    for name, ordinal, typ, use in [
        ("version", 16, "INTEGER",
         "Pointer to record_change_log.id, same meaning as prose_section.version "
         "(escalation #836). This table has never carried a version concept before."),
        ("updated_at", 17, "TEXT",
         "Touched on every write (escalation #836). created_at reserved for true creation "
         "time only."),
    ]:
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='bible_research' "
                "AND table_name='prose_section_type' AND name=?", (name,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, "
                "inactive) VALUES ('bible_research','prose_section_type',?,?,?,0,0,0,NULL,NULL,"
                "?,NULL,NULL,?,0)",
                (name, ordinal, typ, use, MIGRATION_SOURCE))
    report.append("iba.db: cfg_column rows for prose_section_type.version/updated_at added")

    # ── cfg_enum (§13) ────────────────────────────────────────────────────────
    for name, value, ordinal in [
        ("record_change_log_change_type", "insert", 1),
        ("record_change_log_change_type", "change", 2),
        ("record_change_log_change_type", "delete", 3),
        ("record_change_log_status", "change_proposed", 1),
        ("record_change_log_status", "change_applied", 2),
        ("record_change_log_status", "declined", 3),
    ]:
        conn.execute(
            "INSERT OR IGNORE INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
            (name, value, ordinal))
    report.append("iba.db: cfg_enum rows for record_change_log_change_type/status added")

    # ── cfg_write_grant (§12) ────────────────────────────────────────────────
    conn.execute(
        "INSERT OR IGNORE INTO cfg_write_grant (writer, table_name, database, inactive) "
        "VALUES ('apply_session_patch','record_change_log','bible_research',0)")
    report.append("iba.db: cfg_write_grant apply_session_patch -> record_change_log added")

    # ── cfg_behaviour_rule (§14) ─────────────────────────────────────────────
    rules = [
        ("record-change-log-choke-point",
         "Every write to a table under record_change_log versioning discipline (prose_section, "
         "prose_section_type) must produce a matching record_change_log row in the same "
         "transaction as the write itself -- no code path may update a covered table's "
         "version/updated_at without also inserting the corresponding log row. Applies to every "
         "operation on the covered tables, not only the ones already visible in today's "
         "single-writer code path -- closing the exact selective-coverage gap (session_a_replace, "
         "prose_section_type.update) that motivated this item."),
        ("record-change-log-version-is-pointer",
         "A covered target row's version column is not an incrementing per-item counter -- it is "
         "a literal foreign key to record_change_log.id, the log row describing that row's own "
         "most recent change. Corrects the 'version = old.version + 1' text #829 sec 5 drafted "
         "before this item existed; that text is superseded by this rule, not left standing "
         "alongside it."),
        ("record-change-log-payload-is-prior-state",
         "record_change_log.payload holds what a change overwrote or removed -- its prior "
         "content -- never the resulting/current content. The covered table's own current row "
         "already holds current content exactly once; duplicating it into the log is a defect, "
         "not a safety margin. payload is NULL for insert events and for one-time migration-"
         "baseline rows, where no prior state exists."),
        ("one-time-hard-delete-exception",
         "A hard (physical) delete of DB rows is normally disallowed (the standing "
         "no-physical-delete-in-automated-flows convention) but is permitted as a one-time, "
         "explicitly-instructed migration action -- first established for #833's prose-quality-"
         "table repurpose, applied again here for the 91 superseded prose_section rows once "
         "their content is captured in record_change_log. Each occurrence needs its own explicit "
         "researcher instruction; this rule records the pattern, it doesn't pre-authorise future "
         "hard deletes generically."),
    ]
    for rule_key, rule_text in rules:
        if not conn.execute(
                "SELECT 1 FROM cfg_behaviour_rule WHERE class='sqlite' "
                "AND rule_key=?", (rule_key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, "
                "enforced_by, added_at, active) VALUES ('sqlite',?,?,'escalation #836',"
                "'apply_session_patch.py _write_change_log() choke point','2026-08-24T00:00:00Z',1)",
                (rule_key, rule_text))
    report.append("iba.db: 4 cfg_behaviour_rule rows added (idempotent)")

    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?",
                         ("prose_change_log_build_v1_20260824",)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,1)",
            ("prose_change_log_build_v1_20260824",
             "iba/app/migration/prose_change_log_build_v1_20260824.py",
             "ONE-OFF migration, escalation #836 (Prose change log design) -- creates "
             "record_change_log, moves prose_section/prose_section_type to Model A "
             "(mutate-in-place) versioning, migrates the 91 existing superseded prose_section "
             "rows into the log then hard-deletes them, baseline-backfills version pointers for "
             "every surviving row, and registers the full cfg_table/cfg_column/cfg_enum/"
             "cfg_write_grant/cfg_behaviour_rule content. inactive=1 once applied -- a one-off, "
             "not a reusable routine."))
        report.append("iba.db: cfg_utility row for this migration registered")

    conn.commit()
    conn.close()


def main() -> int:
    report: list[str] = []
    _schema_and_migration_side(report)
    _iba_config_side(report)
    print("Prose Change Log build (escalation #836):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
