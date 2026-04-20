"""
Fix 4 — Recreate wa_term_inventory to register FK to wa_file_index(id).
parsed_meaning_id is retained (active write target in meaning_parser.py).
"""
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "bible_research.db"
EXPECTED_ROWS = 1529


def backup_db(db_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = db_path.parent / f"{db_path.name}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"  Backup written: {bak}")
    return bak


def run():
    print("=" * 60)
    print("FIX 4 — Recreate wa_term_inventory")
    print("=" * 60)

    backup_db(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = OFF")
    cur = conn.cursor()

    pre_count = cur.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
    print(f"\n  Pre-recreation row count: {pre_count}")

    try:
        cur.executescript("""
BEGIN TRANSACTION;

CREATE TABLE wa_term_inventory_new (
    id                          INTEGER PRIMARY KEY,
    file_id                     INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    language                    TEXT NOT NULL,
    term_id                     TEXT NOT NULL,
    strongs_number              TEXT,
    transliteration             TEXT NOT NULL,
    step_search_gloss           TEXT,
    word_analysis_gloss         TEXT,
    occurrence_count            INTEGER,
    occurrence_count_qualifier  TEXT,
    meaning                     TEXT,
    meaning_numbered            TEXT,
    also_spelled                TEXT,
    lsj_entry                   TEXT,
    testament                   TEXT,
    god_as_subject              INTEGER DEFAULT 0,
    somatic_link                INTEGER DEFAULT 0,
    causative_form_present      INTEGER DEFAULT 0,
    status_note                 TEXT,
    last_changed                TEXT DEFAULT (datetime('now')),
    short_def_mounce            TEXT,
    parsed_meaning_id           INTEGER
);

INSERT INTO wa_term_inventory_new (
    id, file_id, language, term_id, strongs_number, transliteration,
    step_search_gloss, word_analysis_gloss, occurrence_count,
    occurrence_count_qualifier, meaning, meaning_numbered, also_spelled,
    lsj_entry, testament, god_as_subject, somatic_link, causative_form_present,
    status_note, last_changed, short_def_mounce, parsed_meaning_id
)
SELECT
    id, file_id, language, term_id, strongs_number, transliteration,
    step_search_gloss, word_analysis_gloss, occurrence_count,
    occurrence_count_qualifier, meaning, meaning_numbered, also_spelled,
    lsj_entry, testament, god_as_subject, somatic_link, causative_form_present,
    status_note, last_changed, short_def_mounce, parsed_meaning_id
FROM wa_term_inventory;

DROP TABLE wa_term_inventory;
ALTER TABLE wa_term_inventory_new RENAME TO wa_term_inventory;

CREATE INDEX idx_wa_ti_file    ON wa_term_inventory(file_id);
CREATE INDEX idx_wa_ti_id      ON wa_term_inventory(term_id);
CREATE INDEX idx_wa_ti_lang    ON wa_term_inventory(language);
CREATE INDEX idx_wa_ti_strongs ON wa_term_inventory(strongs_number);

COMMIT;
""")
    except Exception as e:
        conn.execute("ROLLBACK")
        conn.close()
        print(f"\n  ✗ FAIL  Exception during recreation: {e}")
        raise SystemExit(1)

    # ── post-verification ─────────────────────────────────────────
    post_count = cur.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
    fk_count = cur.execute(
        "SELECT COUNT(*) FROM pragma_foreign_key_list('wa_term_inventory')"
    ).fetchone()[0]
    idx_count = cur.execute(
        "SELECT COUNT(*) FROM sqlite_master "
        "WHERE type='index' AND tbl_name='wa_term_inventory'"
    ).fetchone()[0]
    # Confirm parsed_meaning_id column still present
    cols = [r[1] for r in cur.execute("PRAGMA table_info(wa_term_inventory)").fetchall()]
    has_parsed = "parsed_meaning_id" in cols

    conn.close()

    print(f"\n  Post-recreation row count : {post_count}  {'✓' if post_count == EXPECTED_ROWS else '✗ FAIL'}")
    print(f"  Registered FKs            : {fk_count}   {'✓' if fk_count >= 1 else '✗ FAIL'}")
    print(f"  Indexes                   : {idx_count}  (expect 4)")
    print(f"  parsed_meaning_id present : {has_parsed}  {'✓' if has_parsed else '✗ FAIL'}")

    if post_count == EXPECTED_ROWS and fk_count >= 1 and has_parsed:
        print("\n  ✓ PASS  Fix 4 complete")
    else:
        print("\n  ✗ FAIL  Fix 4 verification failed")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
