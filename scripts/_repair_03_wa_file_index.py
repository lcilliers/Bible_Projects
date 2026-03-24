"""
Fix 3 — Recreate wa_file_index to register FK to word_registry(id).
No data change — row-for-row copy. No triggers on this table.
"""
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "bible_research.db"
EXPECTED_ROWS = 199


def backup_db(db_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = db_path.parent / f"{db_path.name}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"  Backup written: {bak}")
    return bak


def run():
    print("=" * 60)
    print("FIX 3 — Recreate wa_file_index")
    print("=" * 60)

    backup_db(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = OFF")   # must be OFF during table recreation
    cur = conn.cursor()

    pre_count = cur.execute("SELECT COUNT(*) FROM wa_file_index").fetchone()[0]
    print(f"\n  Pre-recreation row count: {pre_count}")

    try:
        cur.executescript("""
BEGIN TRANSACTION;

CREATE TABLE wa_file_index_new (
    id                           INTEGER PRIMARY KEY,
    filename                     TEXT NOT NULL,
    registry_id                  TEXT NOT NULL,
    word_registry_fk             INTEGER REFERENCES word_registry(id) ON DELETE RESTRICT,
    word                         TEXT NOT NULL,
    part_number                  INTEGER,
    total_parts                  INTEGER,
    is_split                     INTEGER,
    schema_version               TEXT,
    phase                        TEXT,
    produced_date                TEXT,
    source_file                  TEXT,
    translation_used             TEXT,
    specification                TEXT,
    revision_note                TEXT,
    source_list                  TEXT,
    category                     TEXT,
    testament_coverage           TEXT,
    root_families_in_prior_parts TEXT,
    last_changed                 TEXT DEFAULT (datetime('now'))
);

INSERT INTO wa_file_index_new (
    id, filename, registry_id, word_registry_fk, word,
    part_number, total_parts, is_split, schema_version, phase,
    produced_date, source_file, translation_used, specification,
    revision_note, source_list, category, testament_coverage,
    root_families_in_prior_parts, last_changed
)
SELECT
    id, filename, registry_id, word_registry_fk, word,
    part_number, total_parts, is_split, schema_version, phase,
    produced_date, source_file, translation_used, specification,
    revision_note, source_list, category, testament_coverage,
    root_families_in_prior_parts, last_changed
FROM wa_file_index;

DROP TABLE wa_file_index;
ALTER TABLE wa_file_index_new RENAME TO wa_file_index;

CREATE INDEX idx_wa_fi_wrfk ON wa_file_index(word_registry_fk);
CREATE INDEX idx_wa_fi_word  ON wa_file_index(word);
CREATE INDEX idx_wa_fi_reg   ON wa_file_index(registry_id);

COMMIT;
""")
    except Exception as e:
        conn.execute("ROLLBACK")
        conn.close()
        print(f"\n  ✗ FAIL  Exception during recreation: {e}")
        raise SystemExit(1)

    # ── post-verification ─────────────────────────────────────────
    post_count = cur.execute("SELECT COUNT(*) FROM wa_file_index").fetchone()[0]
    fk_count = cur.execute(
        "SELECT COUNT(*) FROM pragma_foreign_key_list('wa_file_index')"
    ).fetchone()[0]
    idx_count = cur.execute(
        "SELECT COUNT(*) FROM sqlite_master "
        "WHERE type='index' AND tbl_name='wa_file_index'"
    ).fetchone()[0]

    conn.close()

    print(f"\n  Post-recreation row count : {post_count}  {'✓' if post_count == EXPECTED_ROWS else '✗ FAIL'}")
    print(f"  Registered FKs            : {fk_count}   {'✓' if fk_count >= 1 else '✗ FAIL'}")
    print(f"  Indexes                   : {idx_count}  (expect 3)")

    if post_count == EXPECTED_ROWS and fk_count >= 1:
        print("\n  ✓ PASS  Fix 3 complete")
    else:
        print("\n  ✗ FAIL  Fix 3 verification failed")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
