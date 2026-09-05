"""rebuild_prose_section_fk_v1_20260905.py — ONE-OFF. Escalation #1452 (approved 2026-09-05):
`prose_section`'s own CREATE TABLE carries `section_type_id INTEGER NOT NULL REFERENCES
"prose_section_type_old"(id)` — a leftover rename artifact from an earlier migration.
`prose_section_type_old` does not exist; every other live reference (the prose_section_ai/au FTS
triggers included) correctly says `prose_section_type`. Harmless while `PRAGMA foreign_keys` is off
(SQLite's project-wide default), but `scripts/apply_session_patch.py` explicitly turns enforcement
on and its prose_section insert path fails outright against this stale FK. Worked around once
already for #1447's 18-row glossary insert (direct INSERT, bypassing the broken FK entirely).

What this does, in bible_research.db, all in one transaction, direct writes (schema evolution is
migration-script territory, matching `retire_cfg_prose_chapter_v1_20260827.py`'s own pattern —
rename / recreate-correctly / copy / drop):

  1. RENAME prose_section -> prose_section_old_20260905 (all 1035 rows, ids preserved).
  2. CREATE prose_section fresh, identical DDL except the FK now targets prose_section_type
     (not prose_section_type_old).
  3. Copy every row across verbatim (explicit column list, ids preserved — prose_section_fts'
     rowid=id linkage and the 3 child link tables' prose_section_id FKs both depend on this).
  4. DROP the renamed old table (this also drops the 5 indexes and 3 triggers that were carried
     onto it by the RENAME — SQLite updates a table's own index/trigger bodies to the new name on
     RENAME, so they must be recreated explicitly afterward, not left assumed-intact).
  5. Recreate the 5 indexes and 3 triggers with identical DDL to what was there before.

prose_section_fts and its shadow tables are untouched — a separate virtual table, unaffected by
the base table's rename/recreate as long as `id` values are preserved (they are).

Idempotent: checks the live FK target before acting; a no-op if already pointing at
prose_section_type.

    python -m iba.app.migration.rebuild_prose_section_fk_v1_20260905
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import Cfg

_NEW_PROSE_SECTION_DDL = """
    CREATE TABLE "prose_section" (
        id                INTEGER PRIMARY KEY,
        registry_id       INTEGER REFERENCES word_registry(id),
        section_type_id   INTEGER NOT NULL REFERENCES "prose_section_type"(id),
        heading           TEXT,
        body              TEXT    NOT NULL,
        word_count        INTEGER NOT NULL DEFAULT 0,
        status            TEXT    NOT NULL,
        version           INTEGER NOT NULL DEFAULT 1,
        author            TEXT    NOT NULL,
        created_at        TEXT    NOT NULL,
        approved_at       TEXT,
        approved_by       TEXT,
        metadata_json     TEXT,
        delete_flagged    INTEGER NOT NULL DEFAULT 0, cluster_code TEXT, characteristic_id INTEGER, cluster_subgroup_id INTEGER, updated_at TEXT,
        CHECK (status IN ('draft','in_review','approved','archived')),
        CHECK (author IN ('claude_ai','claude_code','researcher'))
    )
"""

_COLUMNS = [
    "id", "registry_id", "section_type_id", "heading", "body", "word_count", "status",
    "version", "author", "created_at", "approved_at", "approved_by", "metadata_json",
    "delete_flagged", "cluster_code", "characteristic_id", "cluster_subgroup_id", "updated_at",
]

_INDEXES = [
    'CREATE INDEX idx_prose_section_characteristic_id ON prose_section(characteristic_id) '
    'WHERE characteristic_id IS NOT NULL',
    'CREATE INDEX idx_prose_section_cluster_code ON prose_section(cluster_code) '
    'WHERE cluster_code IS NOT NULL',
    'CREATE INDEX idx_prose_section_cluster_subgroup_id ON prose_section(cluster_subgroup_id) '
    'WHERE cluster_subgroup_id IS NOT NULL',
    'CREATE INDEX idx_ps_registry_type_current ON prose_section(registry_id, section_type_id) '
    'WHERE delete_flagged = 0',
    "CREATE INDEX idx_ps_status ON prose_section(status) WHERE delete_flagged = 0",
]

_TRIGGERS = [
    """CREATE TRIGGER prose_section_ad AFTER DELETE ON prose_section BEGIN
        DELETE FROM prose_section_fts WHERE rowid = old.id;
    END""",
    """CREATE TRIGGER prose_section_ai AFTER INSERT ON prose_section BEGIN
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code,
                                          registry_id, cluster_code, characteristic_id, status)
            VALUES (new.id, new.body, new.heading,
                    (SELECT code FROM "prose_section_type" WHERE id=new.section_type_id),
                    new.registry_id, new.cluster_code, new.characteristic_id, new.status);
        END""",
    """CREATE TRIGGER prose_section_au AFTER UPDATE ON prose_section BEGIN
        DELETE FROM prose_section_fts WHERE rowid = old.id;
        INSERT INTO prose_section_fts(rowid, body, heading, section_type_code,
                                      registry_id, cluster_code, characteristic_id, status)
        VALUES (new.id, new.body, new.heading,
                (SELECT code FROM "prose_section_type" WHERE id=new.section_type_id),
                new.registry_id, new.cluster_code, new.characteristic_id, new.status);
    END""",
]


def _current_fk_target(conn: sqlite3.Connection) -> str | None:
    row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='prose_section'"
    ).fetchone()
    if row is None:
        return None
    sql = row[0]
    if "prose_section_type_old" in sql:
        return "prose_section_type_old"
    if '"prose_section_type"' in sql or "REFERENCES prose_section_type(" in sql:
        return "prose_section_type"
    return "unknown"


def main() -> int:
    cfg = Cfg()
    conn = sqlite3.connect(cfg.database_path("bible_research"))
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        target = _current_fk_target(conn)
        if target != "prose_section_type_old":
            print(f"rebuild_prose_section_fk_v1_20260905: no-op — live FK target is {target!r}, "
                  f"not the stale 'prose_section_type_old'.")
            return 0

        before_count = conn.execute("SELECT COUNT(*) FROM prose_section").fetchone()[0]

        conn.execute("ALTER TABLE prose_section RENAME TO prose_section_old_20260905")
        report.append("prose_section renamed to prose_section_old_20260905")

        conn.execute(_NEW_PROSE_SECTION_DDL)
        report.append("prose_section recreated with FK -> prose_section_type")

        col_list = ", ".join(_COLUMNS)
        conn.execute(
            f"INSERT INTO prose_section ({col_list}) "
            f"SELECT {col_list} FROM prose_section_old_20260905"
        )
        after_count = conn.execute("SELECT COUNT(*) FROM prose_section").fetchone()[0]
        report.append(f"rows copied: {after_count} (source had {before_count})")
        if after_count != before_count:
            raise RuntimeError(
                f"row count mismatch after copy: {after_count} != {before_count}")

        conn.execute("DROP TABLE prose_section_old_20260905")
        report.append("prose_section_old_20260905 dropped (indexes/triggers on it dropped with it)")

        for ddl in _INDEXES:
            conn.execute(ddl)
        report.append(f"{len(_INDEXES)} index(es) recreated")

        for ddl in _TRIGGERS:
            conn.execute(ddl)
        report.append(f"{len(_TRIGGERS)} trigger(s) recreated")

        # Sanity: FTS rowids still line up with the surviving ids (spot-check, not a full diff).
        fts_missing = conn.execute(
            "SELECT COUNT(*) FROM prose_section p "
            "WHERE NOT EXISTS (SELECT 1 FROM prose_section_fts f WHERE f.rowid = p.id)"
        ).fetchone()[0]
        report.append(f"prose_section rows with no matching FTS rowid: {fts_missing} "
                       f"(should be 0 unless it was already 0 pre-rebuild)")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("rebuild_prose_section_fk_v1_20260905:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
