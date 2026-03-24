"""
Fix 6 — Recreate wa_term_root_family to register FK to wa_term_inventory(id).
"""
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "bible_research.db"
EXPECTED_ROWS = 641


def backup_db(db_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = db_path.parent / f"{db_path.name}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"  Backup written: {bak}")
    return bak


def run():
    print("=" * 60)
    print("FIX 6 — Recreate wa_term_root_family")
    print("=" * 60)

    backup_db(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = OFF")
    cur = conn.cursor()

    pre_count = cur.execute("SELECT COUNT(*) FROM wa_term_root_family").fetchone()[0]
    print(f"\n  Pre-recreation row count: {pre_count}")

    try:
        cur.executescript("""
BEGIN TRANSACTION;

CREATE TABLE wa_term_root_family_new (
    id              INTEGER PRIMARY KEY,
    term_inv_id     INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    root_code       TEXT NOT NULL,
    root_language   TEXT,
    root_gloss      TEXT,
    note            TEXT
);

INSERT INTO wa_term_root_family_new (
    id, term_inv_id, root_code, root_language, root_gloss, note
)
SELECT
    id, term_inv_id, root_code, root_language, root_gloss, note
FROM wa_term_root_family;

DROP TABLE wa_term_root_family;
ALTER TABLE wa_term_root_family_new RENAME TO wa_term_root_family;

CREATE INDEX idx_wa_rf ON wa_term_root_family(term_inv_id);

COMMIT;
""")
    except Exception as e:
        conn.execute("ROLLBACK")
        conn.close()
        print(f"\n  ✗ FAIL  Exception during recreation: {e}")
        raise SystemExit(1)

    post_count = cur.execute("SELECT COUNT(*) FROM wa_term_root_family").fetchone()[0]
    fk_count = cur.execute(
        "SELECT COUNT(*) FROM pragma_foreign_key_list('wa_term_root_family')"
    ).fetchone()[0]
    idx_count = cur.execute(
        "SELECT COUNT(*) FROM sqlite_master "
        "WHERE type='index' AND tbl_name='wa_term_root_family'"
    ).fetchone()[0]

    conn.close()

    print(f"\n  Post-recreation row count : {post_count}  {'✓' if post_count == EXPECTED_ROWS else '✗ FAIL'}")
    print(f"  Registered FKs            : {fk_count}   {'✓' if fk_count >= 1 else '✗ FAIL'}")
    print(f"  Indexes                   : {idx_count}  (expect 1)")

    if post_count == EXPECTED_ROWS and fk_count >= 1:
        print("\n  ✓ PASS  Fix 6 complete")
    else:
        print("\n  ✗ FAIL  Fix 6 verification failed")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
