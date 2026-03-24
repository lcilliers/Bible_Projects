"""
Fix 9 — Recreate mti_terms and mti_term_cross_refs to add integer FK columns
        alongside the existing TEXT columns (retained for legacy reads).
mti_terms:           adds owning_registry_fk -> word_registry(id)
                     and word_data_ref_fk    -> wa_file_index(id)
mti_term_cross_refs: adds registry_fk        -> word_registry(id)
APPROACH: isolation_level=None, explicit transactions, fresh-connection check.
"""
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "bible_research.db"
EXPECTED_MTI_TERMS = 1380
EXPECTED_MTI_XREFS = 463


def backup_db(db_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = db_path.parent / f"{db_path.name}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"  Backup written: {bak}")
    return bak


def run():
    print("=" * 60)
    print("FIX 9 — Recreate MTI tables")
    print("=" * 60)

    backup_db(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH), isolation_level=None)
    conn.execute("PRAGMA foreign_keys = OFF")
    cur = conn.cursor()

    pre_terms = cur.execute("SELECT COUNT(*) FROM mti_terms").fetchone()[0]
    pre_xrefs = cur.execute("SELECT COUNT(*) FROM mti_term_cross_refs").fetchone()[0]
    print(f"\n  Pre-recreation: mti_terms={pre_terms}, mti_term_cross_refs={pre_xrefs}")

    # ════════════════════════════════════════════════════════════════
    # mti_terms
    # ════════════════════════════════════════════════════════════════
    cur.execute("BEGIN")
    cur.execute("""
CREATE TABLE mti_terms_new (
    id                  INTEGER PRIMARY KEY,
    strongs_number      TEXT,
    transliteration     TEXT NOT NULL,
    gloss               TEXT NOT NULL,
    language            TEXT,
    owning_registry     TEXT,
    owning_registry_fk  INTEGER REFERENCES word_registry(id) ON DELETE RESTRICT,
    owning_word         TEXT,
    owning_part         TEXT,
    word_data_reference TEXT,
    word_data_ref_fk    INTEGER REFERENCES wa_file_index(id),
    status              TEXT,
    status_note         TEXT,
    exclusion_reason    TEXT,
    extraction_date     TEXT,
    strongs_reconciled  INTEGER DEFAULT 0,
    anchor_note         TEXT,
    last_changed        TEXT DEFAULT (datetime('now'))
)
""")
    cur.execute("COMMIT")

    cur.execute("BEGIN")
    cur.execute("""
INSERT INTO mti_terms_new (
    id, strongs_number, transliteration, gloss, language,
    owning_registry, owning_registry_fk,
    owning_word, owning_part,
    word_data_reference, word_data_ref_fk,
    status, status_note, exclusion_reason, extraction_date,
    strongs_reconciled, anchor_note, last_changed
)
SELECT
    id, strongs_number, transliteration, gloss, language,
    owning_registry,
    CASE WHEN owning_registry GLOB '[0-9]*' THEN CAST(owning_registry AS INTEGER) ELSE NULL END,
    owning_word, owning_part,
    word_data_reference,
    CASE WHEN word_data_reference GLOB '[0-9]*' THEN CAST(word_data_reference AS INTEGER) ELSE NULL END,
    status, status_note, exclusion_reason, extraction_date,
    strongs_reconciled, anchor_note, last_changed
FROM mti_terms
""")
    terms_inserted = cur.rowcount

    # Verify count in-transaction before committing
    copy_terms = cur.execute("SELECT COUNT(*) FROM mti_terms_new").fetchone()[0]
    if copy_terms != EXPECTED_MTI_TERMS:
        cur.execute("ROLLBACK")
        cur.execute("DROP TABLE IF EXISTS mti_terms_new")
        conn.close()
        print(f"  ABORT  mti_terms copy count {copy_terms} != {EXPECTED_MTI_TERMS} — rolled back")
        raise SystemExit(1)

    print(f"  mti_terms rowcount={terms_inserted}, in-tx count={copy_terms}  ok")
    cur.execute("COMMIT")

    # Swap
    cur.execute("BEGIN")
    cur.execute("DROP TABLE mti_terms")
    cur.execute("ALTER TABLE mti_terms_new RENAME TO mti_terms")
    cur.execute("CREATE INDEX idx_mti_terms_registry ON mti_terms(owning_registry)")
    cur.execute("CREATE INDEX idx_mti_terms_status   ON mti_terms(status)")
    cur.execute("CREATE INDEX idx_mti_terms_word     ON mti_terms(owning_word)")
    cur.execute("CREATE INDEX idx_mti_terms_strongs  ON mti_terms(strongs_number)")
    cur.execute("CREATE INDEX idx_mti_terms_reg_fk   ON mti_terms(owning_registry_fk)")
    cur.execute("COMMIT")

    # ════════════════════════════════════════════════════════════════
    # mti_term_cross_refs
    # ════════════════════════════════════════════════════════════════
    cur.execute("BEGIN")
    cur.execute("""
CREATE TABLE mti_term_cross_refs_new (
    id                  INTEGER PRIMARY KEY,
    mti_term_id         INTEGER NOT NULL REFERENCES mti_terms(id) ON DELETE CASCADE,
    registry            TEXT NOT NULL,
    registry_fk         INTEGER REFERENCES word_registry(id),
    word                TEXT,
    part                TEXT,
    word_data_reference TEXT,
    UNIQUE (mti_term_id, registry, word, part)
)
""")
    cur.execute("COMMIT")

    cur.execute("BEGIN")
    cur.execute("""
INSERT INTO mti_term_cross_refs_new (
    id, mti_term_id, registry, registry_fk, word, part, word_data_reference
)
SELECT
    id, mti_term_id, registry,
    CASE WHEN registry GLOB '[0-9]*' THEN CAST(registry AS INTEGER) ELSE NULL END,
    word, part, word_data_reference
FROM mti_term_cross_refs
""")
    xrefs_inserted = cur.rowcount

    copy_xrefs = cur.execute("SELECT COUNT(*) FROM mti_term_cross_refs_new").fetchone()[0]
    if copy_xrefs != EXPECTED_MTI_XREFS:
        cur.execute("ROLLBACK")
        cur.execute("DROP TABLE IF EXISTS mti_term_cross_refs_new")
        conn.close()
        print(f"  ABORT  mti_term_cross_refs copy count {copy_xrefs} != {EXPECTED_MTI_XREFS} — rolled back")
        raise SystemExit(1)

    print(f"  mti_term_cross_refs rowcount={xrefs_inserted}, in-tx count={copy_xrefs}  ok")
    cur.execute("COMMIT")

    # Swap
    cur.execute("BEGIN")
    cur.execute("DROP TABLE mti_term_cross_refs")
    cur.execute("ALTER TABLE mti_term_cross_refs_new RENAME TO mti_term_cross_refs")
    cur.execute("CREATE INDEX idx_cross_refs_registry ON mti_term_cross_refs(registry, word)")
    cur.execute("CREATE INDEX idx_cross_refs_term_id  ON mti_term_cross_refs(mti_term_id)")
    cur.execute("COMMIT")

    # ── WAL checkpoint before closing ─────────────────────────────
    result = cur.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    print(f"  WAL checkpoint (TRUNCATE): busy={result[0]} log={result[1]} ckpt={result[2]}")

    conn.close()

    # ── fresh-connection verification ─────────────────────────────
    conn2 = sqlite3.connect(str(DB_PATH), isolation_level=None)
    integrity = conn2.execute("PRAGMA integrity_check").fetchone()[0]
    post_terms = conn2.execute("SELECT COUNT(*) FROM mti_terms").fetchone()[0]
    post_xrefs = conn2.execute("SELECT COUNT(*) FROM mti_term_cross_refs").fetchone()[0]
    terms_fks = conn2.execute("SELECT COUNT(*) FROM pragma_foreign_key_list('mti_terms')").fetchone()[0]
    xrefs_fks = conn2.execute("SELECT COUNT(*) FROM pragma_foreign_key_list('mti_term_cross_refs')").fetchone()[0]
    # Verify new FK columns populated where source values were numeric
    terms_nulls = conn2.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE owning_registry IS NOT NULL AND owning_registry_fk IS NULL"
    ).fetchone()[0]
    xrefs_nulls = conn2.execute(
        "SELECT COUNT(*) FROM mti_term_cross_refs WHERE registry IS NOT NULL AND registry_fk IS NULL"
    ).fetchone()[0]
    conn2.close()

    print(f"\n  integrity check             : {integrity}  {'PASS' if integrity == 'ok' else 'FAIL'}")
    print(f"  mti_terms row count         : {post_terms}  {'PASS' if post_terms == EXPECTED_MTI_TERMS else 'FAIL'}")
    print(f"  mti_terms registered FKs    : {terms_fks}  (expect 2)")
    print(f"  mti_terms fk nulls vs text  : {terms_nulls}  {'PASS' if terms_nulls == 0 else 'WARN'}")
    print(f"  mti_term_cross_refs rows    : {post_xrefs}  {'PASS' if post_xrefs == EXPECTED_MTI_XREFS else 'FAIL'}")
    print(f"  mti_term_cross_refs FKs     : {xrefs_fks}  (expect 2)")
    print(f"  mti_term_cross_refs fk null : {xrefs_nulls}  {'PASS' if xrefs_nulls == 0 else 'WARN'}")

    ok = (integrity == "ok"
          and post_terms == EXPECTED_MTI_TERMS
          and post_xrefs == EXPECTED_MTI_XREFS
          and terms_fks >= 2
          and xrefs_fks >= 1)
    if ok:
        print("\n  PASS  Fix 9 complete")
    else:
        print("\n  FAIL  Fix 9 verification failed")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
