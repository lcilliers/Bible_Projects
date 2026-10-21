"""_apply_sense_from_subgloss.py (2026-06-15) — set VE1 (sense) in ve_lexical to the PER-OCCURRENCE STEP
subgloss (step_subgloss_label), the mechanical sense floor — replacing the migrated narrative/uniform-gloss
values. The original value is preserved in `notes` for review. No-subgloss-source rows -> value 'UNRESOLVED'.
Reversible (notes carries the prior value).

  python scripts/_apply_sense_from_subgloss.py --dry-run
  python scripts/_apply_sense_from_subgloss.py --live
"""
import argparse, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT x.id, x.value cur_val, l.step_subgloss_label sub
        FROM ve_lexical x
        JOIN verse_context vc ON vc.id = x.verse_context_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN wa_verse_term_links l ON l.verse_id = vr.id AND l.term_inv_id = vr.term_inv_id
        WHERE x.ve_nr = 1 AND COALESCE(x.delete_flagged,0)=0
    """).fetchall()
    upd, unresolved, same = [], [], 0
    for r in rows:
        sub = (r["sub"] or "").strip()
        if not sub:
            unresolved.append(r["id"]); continue
        if sub == (r["cur_val"] or ""):
            same += 1; continue
        note = f"sense<-subgloss; was: {(r['cur_val'] or '')[:80]}"
        upd.append((sub, note, r["id"]))
    print(f"VE1 rows {len(rows):,} · to subgloss {len(upd):,} · already-correct {same:,} · UNRESOLVED (no subgloss) {len(unresolved):,}")
    if a.live:
        cur.executemany("UPDATE ve_lexical SET value=?, notes=? WHERE id=?", upd)
        for i in range(0, len(unresolved), 400):
            ch = unresolved[i:i+400]
            cur.execute(f"UPDATE ve_lexical SET value='UNRESOLVED', notes='no per-occurrence subgloss source' "
                        f"WHERE id IN ({','.join('?'*len(ch))})", ch)
        conn.commit()
        print(f"LIVE: {len(upd):,} set to subgloss · {len(unresolved):,} -> UNRESOLVED")
    else:
        print("DRY-RUN — no writes.")


if __name__ == "__main__":
    main()
