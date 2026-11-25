"""temp_2551_span_correction_test_run.py -- tests for the correction table of stored span errors (#2551). Runs on a COPY of iba.db that holds the migration span_correction_2551.
Usage: python iba/app/tools/temp_2551_span_correction_test_run.py <db copy>
"""
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import lexical, spancorrection as sc  # noqa: E402

results = []


def case(cid, desc, ok, ev=""):
    results.append((cid, desc, "PASS" if ok else "FAIL", str(ev)[:250]))
    print(f"[{results[-1][2]}] {cid}: {str(ev)[:140]}", file=sys.stderr, flush=True)


def main(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        case("T1", "the table exists with its unique index on the live rows", conn.execute("SELECT 1 FROM sqlite_master WHERE name='uq_span_correction_live'").fetchone() is not None)
        row = conn.execute("SELECT vl.span_id, vl.code_ordinal, vl.verse_id, vl.surface FROM verse_lexical vl WHERE vl.deleted=0 AND vl.surface IS NOT NULL LIMIT 1").fetchone()
        sid, ordn, vid, surf = row["span_id"], row["code_ordinal"], row["verse_id"], row["surface"]
        lexical.build_for_verse_ids(conn, [vid])
        base = conn.execute("SELECT surface, updated_at FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", (sid, ordn)).fetchone()
        case("T2", "with no correction a rebuild leaves the row as it is", base["surface"] == surf, base["surface"])
        conn.execute("INSERT INTO span_correction (span_id, code_ordinal, field, stored_value, corrected_value, reason, escalation_id) VALUES (?,?,?,?,?,?,?)",
                     (sid, ordn, "surface", surf, surf + "-fixed", "test: a corrected surface for the correction table of #2551", 2551))
        lexical.build_for_verse_ids(conn, [vid])
        got = conn.execute("SELECT surface FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", (sid, ordn)).fetchone()[0]
        c = conn.execute("SELECT applied_count, applied_at FROM span_correction WHERE span_id=?", (sid,)).fetchone()
        case("T3", "a live correction whose stored value matches is applied and counted", got == surf + "-fixed" and c["applied_count"] == 1 and c["applied_at"], (got, tuple(c)))
        lexical.build_for_verse_ids(conn, [vid])
        got2 = conn.execute("SELECT surface FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", (sid, ordn)).fetchone()[0]
        case("T4", "a second build keeps the corrected value (the correction is applied again, not lost)", got2 == surf + "-fixed")
        conn.execute("UPDATE span_correction SET stored_value='something else' WHERE span_id=?", (sid,))
        try:
            lexical.build_for_verse_ids(conn, [vid])
            stale = None
        except sc.SpanCorrectionStale as exc:
            stale = str(exc)
        case("T5", "a correction whose stored value no longer matches stops the build and is named", bool(stale) and "review the correction" in stale, stale)
        conn.execute("UPDATE span_correction SET stored_value=?, field='no_such_field' WHERE span_id=?", (surf, sid))
        try:
            lexical.build_for_verse_ids(conn, [vid])
            bad = None
        except sc.SpanCorrectionStale as exc:
            bad = str(exc)
        case("T6", "a correction naming a field the build does not write is refused", bool(bad) and "does not write" in bad, bad)
        conn.execute("UPDATE span_correction SET field='surface', deleted=1 WHERE span_id=?", (sid,))
        lexical.build_for_verse_ids(conn, [vid])
        back = conn.execute("SELECT surface FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", (sid, ordn)).fetchone()[0]
        case("T7", "a deleted correction is not applied: the row returns to the source value", back == surf, back)
        try:
            conn.execute("INSERT INTO span_correction (span_id, code_ordinal, field, stored_value, corrected_value, reason, escalation_id) VALUES (?,?,?,?,?,?,?)", (sid, ordn, "surface", surf, "x", "short", 2551))
            short = False
        except sqlite3.IntegrityError:
            short = True
        case("T8", "a reason under 20 characters is refused by the table", short)
    finally:
        conn.rollback()
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
