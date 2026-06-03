"""Repair the status='delete' / delete_flagged=0 desync — reasoned deletes only, evidence-safe.

Sets delete_flagged=1 for mti_terms that were DECIDED deleted (status='delete')
and carry a documented reason (exclusion_reason), BUT only where doing so
orphans nothing — i.e. the term has no active verse_context and no active
wa_verse_records. Terms with active evidence are auto-held (the two NOT IN
guards) and reported, never flagged.

Soft-delete only (delete_flagged=1); no physical delete; the exclusion_reason is
retained on every row and captured in the change report. Fully reversible.

DEFAULT IS DRY-RUN. Pass --apply to write.

  python scripts/_repair_delete_flag_desync_v1_20260601.py            # dry-run
  python scripts/_repair_delete_flag_desync_v1_20260601.py --apply     # write
"""
import argparse
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")

# The self-guarding selection: reasoned deletes with NO active evidence.
SAFE_WHERE = """
  status = 'delete'
  AND COALESCE(delete_flagged,0) = 0
  AND exclusion_reason IS NOT NULL AND TRIM(exclusion_reason) <> ''
  AND id NOT IN (SELECT mti_term_id FROM verse_context   WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL)
  AND id NOT IN (SELECT mti_term_id FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL)
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write (set delete_flagged=1). Default: dry-run.")
    ap.add_argument("--out", default=os.path.join("research", "investigations", "repair-delete-flag-desync-20260601.md"))
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # the SAFE set that will be flagged
    safe = cur.execute(f"""
        SELECT id, strongs_number, transliteration, gloss, exclusion_reason
        FROM mti_terms WHERE {SAFE_WHERE} ORDER BY strongs_number
    """).fetchall()
    safe_ids = {r["id"] for r in safe}

    # all reasoned deletes (status=delete, del=0, has reason)
    reasoned = cur.execute("""
        SELECT id, strongs_number, transliteration, gloss FROM mti_terms
        WHERE status='delete' AND COALESCE(delete_flagged,0)=0
          AND exclusion_reason IS NOT NULL AND TRIM(exclusion_reason) <> ''
    """).fetchall()
    held = [r for r in reasoned if r["id"] not in safe_ids]  # the unsafe (active evidence)

    # active-evidence counts for the held set (for the report)
    def active_counts(tid):
        vc = cur.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        vr = cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        return vc, vr

    # write the audit report
    L = []
    L.append("# Repair: delete_flag desync (reasoned, evidence-safe)")
    L.append("")
    L.append(f"**Mode:** {'APPLY (written)' if args.apply else 'DRY-RUN (no write)'}")
    L.append(f"**To flag (`delete_flagged=1`):** {len(safe)} terms — `status='delete'`, has reason, no active evidence.")
    L.append(f"**Held back (active evidence — NOT flagged):** {len(held)} terms.")
    L.append("")
    L.append("## Flagged terms (id · strongs · transliteration · reason)")
    L.append("")
    for r in safe:
        reason = (r["exclusion_reason"] or "").replace("\n", " ").strip()
        L.append(f"- {r['id']} · {r['strongs_number']} · {r['transliteration'] or ''} · {reason}")
    L.append("")
    L.append("## Held back — active evidence, require researcher review (NOT flagged)")
    L.append("")
    for r in held:
        vc, vr = active_counts(r["id"])
        L.append(f"- {r['id']} · {r['strongs_number']} · {r['transliteration'] or ''} · {r['gloss'] or ''} — active_vc={vc} active_verses={vr}")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    open(args.out, "w", encoding="utf-8").write("\n".join(L) + "\n")

    if not args.apply:
        print(f"DRY-RUN: would set delete_flagged=1 on {len(safe)} terms; holding back {len(held)} with active evidence.")
        print(f"Report: {args.out}")
        conn.close()
        return

    # APPLY — single transaction, assert the write count matches the safe count.
    cur.execute("BEGIN")
    try:
        cur.execute(f"UPDATE mti_terms SET delete_flagged=1, last_changed=datetime('now') WHERE {SAFE_WHERE}")
        n = cur.rowcount
        if n != len(safe):
            conn.rollback()
            raise SystemExit(f"ABORT: UPDATE affected {n} rows but expected {len(safe)} — rolled back, no change.")
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    # verify
    remaining = cur.execute("""SELECT COUNT(*) FROM mti_terms WHERE status='delete' AND COALESCE(delete_flagged,0)=0
                               AND exclusion_reason IS NOT NULL AND TRIM(exclusion_reason) <> ''""").fetchone()[0]
    print(f"APPLIED: set delete_flagged=1 on {n} terms. Held back {len(held)}.")
    print(f"Remaining (status=delete, del=0, has reason): {remaining}  (should equal held = {len(held)})")
    print(f"Report: {args.out}")
    conn.close()


if __name__ == "__main__":
    main()
