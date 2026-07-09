"""N5: backfill M38 mti_term_subgroup links from its own verse_context classifications.

M38 has 7 cluster_subgroups but 0 mti_term_subgroup links. The authoritative
term->subgroup mapping is derivable from M38's verse_context (distinct
mti_term_id x cluster_subgroup_id, live rows). Insert those pairs (not already
present). placement_note records provenance.

DEFAULT IS DRY-RUN. Pass --apply. Single transaction, rowcount asserted.
"""
import argparse
import sqlite3

DB = "database/bible_research.db"
NOTE = "Backfilled from M38 verse_context 2026-06-01 (N5)"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=20); c.row_factory = sqlite3.Row
    cur = c.cursor()
    pairs = cur.execute("""
        SELECT DISTINCT vc.mti_term_id mt, vc.cluster_subgroup_id cs
        FROM verse_context vc JOIN cluster_subgroup g ON g.id=vc.cluster_subgroup_id
        WHERE g.cluster_code='M38' AND vc.mti_term_id IS NOT NULL
          AND vc.cluster_subgroup_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0
    """).fetchall()
    # exclude any already present
    todo = [(r["mt"], r["cs"]) for r in pairs
            if not cur.execute("SELECT 1 FROM mti_term_subgroup WHERE mti_term_id=? AND cluster_subgroup_id=?", (r["mt"], r["cs"])).fetchone()]
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: M38 term->subgroup pairs to insert: {len(todo)} (derived {len(pairs)})")
    if not a.apply:
        for mt, cs in todo[:10]:
            print(f"  term {mt} -> subgroup {cs}")
        c.close(); return
    cur.execute("BEGIN")
    try:
        for mt, cs in todo:
            cur.execute("INSERT INTO mti_term_subgroup (mti_term_id, cluster_subgroup_id, placement_note, delete_flagged, created_at, last_updated_date) VALUES (?,?,?,0,datetime('now'),datetime('now'))", (mt, cs, NOTE))
        n = cur.execute("SELECT COUNT(*) FROM mti_term_subgroup ts JOIN cluster_subgroup cs ON cs.id=ts.cluster_subgroup_id WHERE cs.cluster_code='M38'").fetchone()[0]
        if n != len(todo):
            c.rollback(); raise SystemExit(f"ABORT: M38 links now {n}, expected {len(todo)} — rolled back.")
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: inserted {len(todo)} M38 mti_term_subgroup links (total now {len(todo)}).")
    c.close()


if __name__ == "__main__":
    main()
