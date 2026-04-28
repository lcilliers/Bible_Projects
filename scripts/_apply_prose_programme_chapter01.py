"""
_apply_prose_programme_chapter01.py

One-off routine to apply:
  - DIR-20260421-002 equivalent: relax prose_section.registry_id NOT NULL
  - PATCH-20260421-CATALOGUE-PROSE-TYPES-V1: 7 prose_section_type inserts
  - PATCH-20260421-PROSE-PROGRAMME-CH01-V1: 7 prose_section inserts

Derived from:
  Sessions/Patches/wa-global-dir-002-submission-v1-20260421.md
  Sessions/Patches/wa-prose-catalogue-chapter0-1-v1-20260421.json
  Sessions/Patches/wa-prose-programme-chapter0-1-v1-20260421.json
  wa-directive-instruction-v1_2-20260421.md §10.2 (worked pattern)

Bypasses apply_session_patch.py for three reasons:
  (a) applicator validator rejects registry_id=NULL on prose_section inserts
      (list in scripts/apply_session_patch.py:1326 includes registry_id)
  (b) applicator has no resolver for section_type_id_lookup:{code}
  (c) schema DDL change to relax NOT NULL is not a patch operation

All steps run in a single transaction; rollback on any failure.

Usage: python scripts/_apply_prose_programme_chapter01.py [--dry-run]
"""
from __future__ import annotations
import argparse
import json
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

DB_PATH = Path("database/bible_research.db")
CATALOGUE_PATCH = Path("Sessions/Patches/wa-prose-catalogue-chapter0-1-v1-20260421.json")
PROSE_PATCH = Path("Sessions/Patches/wa-prose-programme-chapter0-1-v1-20260421.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    dst = Path(f"backups/bible_research_backup_{stamp}_PROSE-CHAPTER01.db")
    dst.parent.mkdir(exist_ok=True)
    shutil.copy2(DB_PATH, dst)
    return dst


def run_schema_change(conn: sqlite3.Connection) -> None:
    """Relax prose_section.registry_id NOT NULL via CREATE-copy-RENAME.

    Pre-condition: prose_section is empty (asserted below).
    Post-condition: registry_id is nullable; FK + CHECKs + indexes + triggers
    preserved; prose_section_fts unchanged (standalone virtual table, triggers
    continue to populate it on INSERT).
    """
    # Pre-check: table empty — we must not lose rows
    cnt = conn.execute("SELECT COUNT(*) FROM prose_section").fetchone()[0]
    if cnt != 0:
        raise RuntimeError(
            f"prose_section has {cnt} rows — non-empty table. "
            "Halting: the DDL approach below is only safe for empty tables."
        )

    # Drop triggers so they don't misfire during the rename dance
    for trig in ("prose_section_ai", "prose_section_au", "prose_section_ad"):
        conn.execute(f"DROP TRIGGER IF EXISTS {trig}")

    # New table with registry_id nullable (FK retained; all other constraints retained)
    conn.execute("""
        CREATE TABLE prose_section_new (
            id                INTEGER PRIMARY KEY,
            registry_id       INTEGER REFERENCES word_registry(id),
            section_type_id   INTEGER NOT NULL REFERENCES prose_section_type(id),
            heading           TEXT,
            body              TEXT    NOT NULL,
            word_count        INTEGER NOT NULL DEFAULT 0,
            status            TEXT    NOT NULL,
            version           INTEGER NOT NULL DEFAULT 1,
            supersedes_id     INTEGER REFERENCES prose_section(id),
            superseded_by_id  INTEGER REFERENCES prose_section(id),
            author            TEXT    NOT NULL,
            created_at        TEXT    NOT NULL,
            approved_at       TEXT,
            approved_by       TEXT,
            metadata_json     TEXT,
            source_file       TEXT,
            delete_flagged    INTEGER NOT NULL DEFAULT 0,
            CHECK (status IN ('draft','in_review','approved','archived')),
            CHECK (author IN ('claude_ai','claude_code','researcher'))
        )
    """)

    # Copy (0 rows) — belt and braces in case the pre-check ever loosens
    conn.execute("INSERT INTO prose_section_new SELECT * FROM prose_section")

    # Swap
    conn.execute("DROP TABLE prose_section")
    conn.execute("ALTER TABLE prose_section_new RENAME TO prose_section")

    # Recreate indexes (verbatim from original DDL)
    conn.execute("""
        CREATE INDEX idx_ps_registry_type_current
          ON prose_section(registry_id, section_type_id)
         WHERE delete_flagged = 0 AND superseded_by_id IS NULL
    """)
    conn.execute("""
        CREATE INDEX idx_ps_status
          ON prose_section(status)
         WHERE delete_flagged = 0 AND superseded_by_id IS NULL
    """)
    conn.execute("""
        CREATE INDEX idx_ps_supersedes
          ON prose_section(supersedes_id)
         WHERE supersedes_id IS NOT NULL
    """)

    # Recreate triggers (verbatim — they sync prose_section_fts)
    conn.execute("""
        CREATE TRIGGER prose_section_ai AFTER INSERT ON prose_section
        BEGIN
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
            SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
            FROM prose_section_type pst WHERE pst.id = new.section_type_id;
        END
    """)
    conn.execute("""
        CREATE TRIGGER prose_section_au AFTER UPDATE ON prose_section
        BEGIN
            DELETE FROM prose_section_fts WHERE rowid = old.id;
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
            SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
            FROM prose_section_type pst WHERE pst.id = new.section_type_id;
        END
    """)
    conn.execute("""
        CREATE TRIGGER prose_section_ad AFTER DELETE ON prose_section
        BEGIN
            DELETE FROM prose_section_fts WHERE rowid = old.id;
        END
    """)


def seed_prose_section_types(conn: sqlite3.Connection) -> dict[str, int]:
    """Insert the 7 prose_section_type rows from the catalogue patch.
    Returns {code: new_id} for use in the PROSE section inserts.
    """
    data = json.loads(CATALOGUE_PATCH.read_text(encoding="utf-8"))
    code_to_id: dict[str, int] = {}
    for op in data["operations"]:
        r = op["record"]
        # Guard — code must not already exist
        existing = conn.execute(
            "SELECT id FROM prose_section_type WHERE code = ?", (r["code"],)
        ).fetchone()
        if existing:
            print(f"  [SKIP] prose_section_type code={r['code']!r} already exists at id={existing[0]}")
            code_to_id[r["code"]] = existing[0]
            continue
        cur = conn.execute(
            """INSERT INTO prose_section_type
               (code, label, source_stage, lifecycle_tag, chapter_no,
                description, expected_length_min, expected_length_max, sort_order)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                r["code"], r["label"], r["source_stage"],
                r.get("lifecycle_tag"), r.get("chapter_no"),
                r.get("description"),
                r.get("expected_length_min"), r.get("expected_length_max"),
                r.get("sort_order", 999),
            ),
        )
        code_to_id[r["code"]] = cur.lastrowid
        print(f"  prose_section_type INSERT code={r['code']!r:42s} id={cur.lastrowid}")
    return code_to_id


def seed_prose_sections(conn: sqlite3.Connection, code_to_id: dict[str, int]) -> list[int]:
    """Insert the 7 prose_section rows from the PROSE patch, resolving
    section_type_id from the section_type_id_lookup.code pattern.
    """
    data = json.loads(PROSE_PATCH.read_text(encoding="utf-8"))
    inserted_ids: list[int] = []
    for op in data["operations"]:
        r = op["record"]
        lookup = r.get("section_type_id_lookup") or {}
        code = lookup.get("code")
        if not code:
            raise ValueError(f"{op['op_id']}: no section_type_id_lookup.code")
        stype_id = code_to_id.get(code)
        if not stype_id:
            # Fallback: look it up from DB (defensive)
            row = conn.execute(
                "SELECT id FROM prose_section_type WHERE code = ?", (code,)
            ).fetchone()
            if not row:
                raise ValueError(f"{op['op_id']}: unknown section_type_id_lookup.code={code!r}")
            stype_id = row[0]

        body = r["body"] or ""
        word_count = r.get("word_count") or len(body.split())
        cur = conn.execute(
            """INSERT INTO prose_section
               (registry_id, section_type_id, heading, body, word_count,
                status, version, supersedes_id, author, created_at,
                approved_at, approved_by, metadata_json, source_file, delete_flagged)
               VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, ?, ?, ?, ?, 0)""",
            (
                r.get("registry_id"),  # accepted as NULL after the schema change
                stype_id,
                r.get("heading"),
                body,
                word_count,
                r.get("status", "draft"),
                r.get("version", 1),
                r["author"],
                r.get("created_at", now_iso()),
                r.get("approved_at"),
                r.get("approved_by"),
                r.get("metadata_json"),
                r.get("source_file"),
            ),
        )
        inserted_ids.append(cur.lastrowid)
        print(f"  prose_section INSERT id={cur.lastrowid} code={code!r:42s} heading={r.get('heading')!r}")
    return inserted_ids


def verify(conn: sqlite3.Connection, new_ids: list[int]) -> None:
    print()
    print("=== POST-APPLY VERIFICATION ===")
    # Schema
    cols = conn.execute("PRAGMA table_info(prose_section)").fetchall()
    reg = next((c for c in cols if c[1] == "registry_id"), None)
    assert reg is not None, "registry_id column missing"
    assert reg[3] == 0, f"registry_id still NOT NULL (notnull={reg[3]})"
    print(f"  registry_id: notnull={reg[3]} (0 = nullable) ✓")

    # Row counts
    pt_count = conn.execute("SELECT COUNT(*) FROM prose_section_type").fetchone()[0]
    p_count = conn.execute("SELECT COUNT(*) FROM prose_section").fetchone()[0]
    p_active = conn.execute("SELECT COUNT(*) FROM prose_section WHERE delete_flagged=0").fetchone()[0]
    null_reg = conn.execute("SELECT COUNT(*) FROM prose_section WHERE registry_id IS NULL").fetchone()[0]
    print(f"  prose_section_type total rows: {pt_count}")
    print(f"  prose_section total rows: {p_count} (active={p_active}, null registry_id={null_reg})")

    # FTS sanity — every active row should have a corresponding FTS row
    fts_count = conn.execute("SELECT COUNT(*) FROM prose_section_fts").fetchone()[0]
    print(f"  prose_section_fts rows: {fts_count}")
    if fts_count != p_active:
        print(f"  ⚠ FTS count ({fts_count}) != active prose_section count ({p_active})")

    # Sample
    print()
    print("  Sample of inserted prose_section rows:")
    for row in conn.execute(
        """SELECT ps.id, pst.code, ps.heading, ps.word_count, ps.status
             FROM prose_section ps
             JOIN prose_section_type pst ON pst.id = ps.section_type_id
            WHERE ps.id IN ({})
            ORDER BY ps.id""".format(",".join(map(str, new_ids)))
    ):
        print(f"    id={row[0]} code={row[1]:42s} heading={row[2]:35s} words={row[3]} status={row[4]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not DB_PATH.exists():
        print(f"FATAL: {DB_PATH} not found")
        return 2
    if not CATALOGUE_PATCH.exists():
        print(f"FATAL: {CATALOGUE_PATCH} not found")
        return 2
    if not PROSE_PATCH.exists():
        print(f"FATAL: {PROSE_PATCH} not found")
        return 2

    print(f"[{now_iso()}] prose chapter 0-1 apply — {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print(f"  DB: {DB_PATH}")
    print(f"  catalogue: {CATALOGUE_PATCH}")
    print(f"  prose:     {PROSE_PATCH}")

    if not args.dry_run:
        b = backup_db()
        print(f"  [BACKUP] {b}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        conn.execute("BEGIN")
        print()
        print("=== SCHEMA CHANGE ===")
        run_schema_change(conn)
        print("  prose_section recreated with registry_id nullable; indexes + triggers restored")
        print()
        print("=== SEED prose_section_type (7) ===")
        code_to_id = seed_prose_section_types(conn)
        print()
        print("=== SEED prose_section (7) ===")
        new_ids = seed_prose_sections(conn, code_to_id)

        if args.dry_run:
            # Verify BEFORE rollback so we see the post-apply state
            verify(conn, new_ids)
            conn.execute("ROLLBACK")
            print()
            print("[DRY-RUN] rollback issued — no changes persisted.")
        else:
            conn.execute("COMMIT")
            verify(conn, new_ids)
            print()
            print("✓ ALL CHANGES COMMITTED")
    except Exception as e:
        try:
            conn.execute("ROLLBACK")
        except sqlite3.OperationalError:
            pass
        print()
        print(f"✗ FAILURE — rolled back. Error: {e}")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
