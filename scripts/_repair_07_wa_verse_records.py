"""
Fix 7 — Recreate wa_verse_records to register FKs to wa_file_index(id)
        and wa_term_inventory(id).
RISK: 57,130 rows.
APPROACH: isolation_level=None (explicit BEGIN/COMMIT — no auto-transaction
interference), single INSERT...SELECT (no batching), count check before DROP,
hard WAL checkpoint (TRUNCATE) before closing, fresh-connection integrity check.
"""
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "bible_research.db"
EXPECTED_ROWS = 57130


def backup_db(db_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = db_path.parent / f"{db_path.name}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"  Backup written: {bak}")
    return bak


def run():
    print("=" * 60)
    print("FIX 7 — Recreate wa_verse_records")
    print("=" * 60)

    backup_db(DB_PATH)

    # isolation_level=None = autocommit; all transactions are explicit
    conn = sqlite3.connect(str(DB_PATH), isolation_level=None)
    conn.execute("PRAGMA foreign_keys = OFF")
    cur = conn.cursor()

    pre_count = cur.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]
    print(f"\n  Pre-recreation row count: {pre_count}")
    if pre_count != EXPECTED_ROWS:
        conn.close()
        print(f"  ABORT  Pre-count {pre_count} != {EXPECTED_ROWS}")
        raise SystemExit(1)

    # ── Step 1: create new table ──────────────────────────────────
    cur.execute("BEGIN")
    cur.execute("""
CREATE TABLE wa_verse_records_new (
    id                  INTEGER PRIMARY KEY,
    file_id             INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    term_inv_id         INTEGER REFERENCES wa_term_inventory(id) ON DELETE RESTRICT,
    term_id             TEXT,
    transliteration     TEXT,
    testament           TEXT,
    reference           TEXT,
    verse_text          TEXT,
    last_changed        TEXT DEFAULT (datetime('now')),
    book_id             INTEGER REFERENCES books(id),
    chapter             INTEGER,
    verse_num           INTEGER,
    translation         TEXT NOT NULL DEFAULT 'ESV',
    note                TEXT,
    claude_output       TEXT,
    created_at          TEXT,
    updated_at          TEXT,
    target_word         TEXT,
    span_strong_match   INTEGER,
    context_before      TEXT,
    context_after       TEXT
)
""")
    cur.execute("COMMIT")

    # ── Step 2: single INSERT...SELECT ───────────────────────────
    print("  Copying 57130 rows (single INSERT...SELECT) ...")
    cur.execute("BEGIN")
    cur.execute("""
INSERT INTO wa_verse_records_new (
    id, file_id, term_inv_id, term_id, transliteration, testament,
    reference, verse_text, last_changed, book_id, chapter, verse_num,
    translation, note, claude_output, created_at, updated_at,
    target_word, span_strong_match, context_before, context_after
)
SELECT
    id, file_id, term_inv_id, term_id, transliteration, testament,
    reference, verse_text, last_changed, book_id, chapter, verse_num,
    translation, note, claude_output, created_at, updated_at,
    target_word, span_strong_match, context_before, context_after
FROM wa_verse_records
""")
    rows_inserted = cur.rowcount
    print(f"  cur.rowcount after INSERT: {rows_inserted}")

    # ── Step 3: verify count BEFORE committing ────────────────────
    copy_count = cur.execute("SELECT COUNT(*) FROM wa_verse_records_new").fetchone()[0]
    if copy_count != EXPECTED_ROWS:
        cur.execute("ROLLBACK")
        cur.execute("DROP TABLE IF EXISTS wa_verse_records_new")
        conn.close()
        print(f"  ABORT  In-tx count {copy_count} != {EXPECTED_ROWS} — rolled back, original preserved")
        raise SystemExit(1)

    print(f"  In-transaction copy count: {copy_count}  ok")
    cur.execute("COMMIT")

    # ── Step 4: swap, indexes, trigger ────────────────────────────
    cur.execute("BEGIN")
    cur.execute("DROP TABLE wa_verse_records")
    cur.execute("ALTER TABLE wa_verse_records_new RENAME TO wa_verse_records")
    cur.execute("CREATE INDEX idx_wavr_file_term_pos ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num)")
    cur.execute("CREATE INDEX idx_wavr_term_id       ON wa_verse_records (term_id)")
    cur.execute("CREATE INDEX idx_wavr_reference     ON wa_verse_records (reference)")
    cur.execute("CREATE INDEX idx_wavr_book_ch_v     ON wa_verse_records (book_id, chapter, verse_num)")
    cur.execute("CREATE INDEX idx_wa_vr_term         ON wa_verse_records (term_inv_id)")
    cur.execute("""
CREATE TRIGGER IF NOT EXISTS wa_verse_records_updated_at
AFTER UPDATE ON wa_verse_records
BEGIN
    UPDATE wa_verse_records
    SET updated_at = strftime('%Y-%m-%dT%H:%M:%S','now')
    WHERE id = NEW.id;
END
""")
    cur.execute("COMMIT")

    # ── Step 5: hard WAL checkpoint before closing ────────────────
    result = cur.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    print(f"  WAL checkpoint (TRUNCATE): busy={result[0]} log={result[1]} ckpt={result[2]}")

    conn.close()

    # ── Step 6: fresh-connection integrity check ──────────────────
    conn2 = sqlite3.connect(str(DB_PATH), isolation_level=None)
    integrity = conn2.execute("PRAGMA integrity_check").fetchone()[0]
    fresh_count = conn2.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]
    fk_count = conn2.execute(
        "SELECT COUNT(*) FROM pragma_foreign_key_list('wa_verse_records')"
    ).fetchone()[0]
    idx_count = conn2.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='index' AND tbl_name='wa_verse_records'"
    ).fetchone()[0]
    trigger_exists = conn2.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='trigger' AND name='wa_verse_records_updated_at'"
    ).fetchone()[0]
    conn2.close()

    print(f"\n  Fresh-connection integrity  : {integrity}  {'PASS' if integrity == 'ok' else 'FAIL'}")
    print(f"  Fresh-connection row count  : {fresh_count}  {'PASS' if fresh_count == EXPECTED_ROWS else 'FAIL'}")
    print(f"  Registered FKs              : {fk_count}   {'PASS' if fk_count >= 2 else 'FAIL'} (expect >= 2)")
    print(f"  Indexes                     : {idx_count}  (expect 5)")
    print(f"  Trigger recreated           : {bool(trigger_exists)}  {'PASS' if trigger_exists else 'FAIL'}")

    ok = (integrity == "ok" and fresh_count == EXPECTED_ROWS
          and fk_count >= 2 and trigger_exists)
    if ok:
        print("\n  PASS  Fix 7 complete")
    else:
        print("\n  FAIL  Fix 7 verification failed")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
