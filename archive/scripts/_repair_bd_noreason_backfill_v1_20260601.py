"""Backfill the B+D no-reason unclustered terms: delete_flagged=1 + a recorded reason.

Researcher direction 2026-06-01: the B+D terms (cluster_code IS NULL, no
exclusion_reason) are to be marked deleted with the reason
'Bulk deleted, decision not recorded'.

EVIDENCE-SAFE GUARD (the thambos/cha.lah lesson): applies ONLY to terms with no
active verse_context and no active verse records. The ~21 B+D terms that still
carry live evidence are auto-held and reported, never flagged — they need the
separate suspect-review, not a bulk delete.

  B = cluster_code IS NULL, delete_flagged=1, no reason  (flag already set; reason backfilled)
  D = cluster_code IS NULL, delete_flagged=0, status in (delete/excluded), no reason  (flag + reason set)

DEFAULT IS DRY-RUN. Pass --apply to write.
  python scripts/_repair_bd_noreason_backfill_v1_20260601.py
  python scripts/_repair_bd_noreason_backfill_v1_20260601.py --apply
"""
import argparse
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")
REASON = "Bulk deleted, decision not recorded"
OUT = os.path.join("research", "investigations", "repair-bd-noreason-backfill-20260601.md")

# B+D, no reason, evidence-safe (no active verse_context, no active verse records)
SAFE_WHERE = """
  cluster_code IS NULL
  AND (exclusion_reason IS NULL OR TRIM(exclusion_reason) = '')
  AND ( delete_flagged = 1 OR (COALESCE(delete_flagged,0) = 0 AND status IN ('delete','excluded')) )
  AND id NOT IN (SELECT mti_term_id FROM verse_context   WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL)
  AND id NOT IN (SELECT mti_term_id FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL)
"""

# all B+D (no reason) — used to compute the held set = all B+D minus the safe set
ALL_BD_WHERE = """
  cluster_code IS NULL
  AND (exclusion_reason IS NULL OR TRIM(exclusion_reason) = '')
  AND ( delete_flagged = 1 OR (COALESCE(delete_flagged,0) = 0 AND status IN ('delete','excluded')) )
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=15)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    safe_ids = [r["id"] for r in cur.execute(f"SELECT id FROM mti_terms WHERE {SAFE_WHERE}")]
    all_bd = cur.execute(f"SELECT id, strongs_number, transliteration, gloss, status, delete_flagged FROM mti_terms WHERE {ALL_BD_WHERE}").fetchall()
    safe_set = set(safe_ids)
    held = [r for r in all_bd if r["id"] not in safe_set]

    # active-evidence counts for the held set (report)
    def ev(tid):
        vc = cur.execute("SELECT COUNT(1) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        vr = cur.execute("SELECT COUNT(1) FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        return vc, vr

    L = ["# B+D no-reason backfill — delete_flagged=1 + reason", "",
         f"**Mode:** {'APPLY (written)' if a.apply else 'DRY-RUN (no write)'}",
         f"**Reason set:** '{REASON}'",
         f"**To update (evidence-safe):** {len(safe_ids)}",
         f"**Held (active evidence — NOT touched):** {len(held)} — need the suspect review, not a bulk delete.", "",
         "## Held terms (live evidence)", ""]
    for r in held:
        vc, vr = ev(r["id"])
        L.append(f"- id={r['id']} {r['strongs_number']} {r['transliteration'] or ''} — {r['gloss'] or ''} | status={r['status']} del={r['delete_flagged']} active_vc={vc} active_verses={vr}")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    if not a.apply:
        print(f"DRY-RUN: would set delete_flagged=1 + reason on {len(safe_ids)} terms; holding {len(held)} with active evidence.")
        print(f"Report: {a.out}")
        conn.close()
        return

    cur.execute("BEGIN")
    try:
        cur.execute(f"UPDATE mti_terms SET delete_flagged=1, exclusion_reason=?, last_changed=datetime('now') WHERE {SAFE_WHERE}", (REASON,))
        n = cur.rowcount
        if n != len(safe_ids):
            conn.rollback()
            raise SystemExit(f"ABORT: UPDATE affected {n}, expected {len(safe_ids)} — rolled back.")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    print(f"APPLIED: updated {n} terms (delete_flagged=1, reason set). Held {len(held)}.")
    print(f"Report: {a.out}")
    conn.close()


if __name__ == "__main__":
    main()
