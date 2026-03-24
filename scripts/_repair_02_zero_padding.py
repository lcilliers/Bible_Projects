"""
Fix 2 — Normalise zero-padded registry IDs in 4 tables.
Tables: wa_file_index, mti_terms, mti_term_cross_refs, word_run_state
Type:   UPDATE only — no structural change.
"""
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "bible_research.db"


def backup_db(db_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = db_path.parent / f"{db_path.name}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"  Backup written: {bak}")
    return bak


def run():
    print("=" * 60)
    print("FIX 2 — Zero-Padding Normalisation")
    print("=" * 60)

    backup_db(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # ── pre-counts ────────────────────────────────────────────────
    pre = {}
    pre["wa_file_index"] = cur.execute(
        "SELECT COUNT(*) FROM wa_file_index "
        "WHERE registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"
    ).fetchone()[0]
    pre["mti_terms"] = cur.execute(
        "SELECT COUNT(*) FROM mti_terms "
        "WHERE owning_registry GLOB '[0-9]*' "
        "  AND owning_registry != CAST(CAST(owning_registry AS INTEGER) AS TEXT)"
    ).fetchone()[0]
    pre["mti_term_cross_refs"] = cur.execute(
        "SELECT COUNT(*) FROM mti_term_cross_refs "
        "WHERE registry GLOB '[0-9]*' "
        "  AND registry != CAST(CAST(registry AS INTEGER) AS TEXT)"
    ).fetchone()[0]
    pre["word_run_state"] = cur.execute(
        "SELECT COUNT(*) FROM word_run_state "
        "WHERE registry_id GLOB '[0-9]*' "
        "  AND registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"
    ).fetchone()[0]

    print(f"\n  Pre-fix zero-padded rows:")
    for t, n in pre.items():
        print(f"    {t}: {n}")

    expected_total = 509

    # ── updates ───────────────────────────────────────────────────
    cur.execute(
        "UPDATE wa_file_index "
        "SET registry_id = CAST(CAST(registry_id AS INTEGER) AS TEXT) "
        "WHERE registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"
    )
    cur.execute(
        "UPDATE mti_terms "
        "SET owning_registry = CAST(CAST(owning_registry AS INTEGER) AS TEXT) "
        "WHERE owning_registry GLOB '[0-9]*' "
        "  AND owning_registry != CAST(CAST(owning_registry AS INTEGER) AS TEXT)"
    )
    cur.execute(
        "UPDATE mti_term_cross_refs "
        "SET registry = CAST(CAST(registry AS INTEGER) AS TEXT) "
        "WHERE registry GLOB '[0-9]*' "
        "  AND registry != CAST(CAST(registry AS INTEGER) AS TEXT)"
    )
    cur.execute(
        "UPDATE word_run_state "
        "SET registry_id = CAST(CAST(registry_id AS INTEGER) AS TEXT) "
        "WHERE registry_id GLOB '[0-9]*' "
        "  AND registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"
    )

    conn.commit()

    # ── post-verification ─────────────────────────────────────────
    post = {}
    post["wa_file_index"] = cur.execute(
        "SELECT COUNT(*) FROM wa_file_index "
        "WHERE registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"
    ).fetchone()[0]
    post["mti_terms"] = cur.execute(
        "SELECT COUNT(*) FROM mti_terms "
        "WHERE owning_registry GLOB '[0-9]*' "
        "  AND owning_registry != CAST(CAST(owning_registry AS INTEGER) AS TEXT)"
    ).fetchone()[0]
    post["mti_term_cross_refs"] = cur.execute(
        "SELECT COUNT(*) FROM mti_term_cross_refs "
        "WHERE registry GLOB '[0-9]*' "
        "  AND registry != CAST(CAST(registry AS INTEGER) AS TEXT)"
    ).fetchone()[0]
    post["word_run_state"] = cur.execute(
        "SELECT COUNT(*) FROM word_run_state "
        "WHERE registry_id GLOB '[0-9]*' "
        "  AND registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"
    ).fetchone()[0]

    # Cross-check wa_file_index: registry_id must now equal CAST(word_registry_fk AS TEXT)
    cross_check = cur.execute(
        "SELECT COUNT(*) FROM wa_file_index "
        "WHERE registry_id != CAST(word_registry_fk AS TEXT)"
    ).fetchone()[0]

    conn.close()

    print(f"\n  Post-fix zero-padded rows (all must be 0):")
    all_ok = True
    for t, n in post.items():
        status = "✓" if n == 0 else "✗ FAIL"
        print(f"    {t}: {n}  {status}")
        if n != 0:
            all_ok = False

    cross_status = "✓" if cross_check == 0 else "✗ FAIL"
    print(f"\n  wa_file_index cross-check (registry_id != CAST(word_registry_fk AS TEXT)): {cross_check}  {cross_status}")
    if cross_check != 0:
        all_ok = False

    total_fixed = sum(pre.values())
    print(f"\n  Total rows updated: {total_fixed} (plan expected ~{expected_total})")

    if all_ok:
        print("\n  ✓ PASS  Fix 2 complete")
    else:
        print("\n  ✗ FAIL  Fix 2 encountered errors — inspect above")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
