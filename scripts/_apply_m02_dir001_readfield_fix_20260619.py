"""_apply_m02_dir001_readfield_fix_20260619.py — apply directive DIR-20260619-001 (M02 read-field fixes).

Correction A (valence): the 6 M02 burning-heat DIVINE-WRATH occurrences (divine_involvement in
agent/possessor/giver) wrongly tagged valence='sinful' -> 'neutral'. The sinful framing belongs to the
provoking human sin in the verse, not to God's wrath. Co-occurring provoking terms (ka.as/ka.a.s) are NOT
touched. Selected by the directive's authoritative criterion (guarantees After-A = 0).

Correction B (divine_involvement): Exo 4:14 & 2Ki 13:3 cha.rah (H2734) currently have NO divine-involvement
row (= NONE), routing them to C1. INSERT divine-involvement='agent' -> routes to C2 (derived at read time).
experiencer is left at 'other' — already the value every other divine-wrath cha.rah carries (already
consistent with God as subject; changing it would break consistency).

Reversible: pre-run backup; updates keep source_provenance=*_read_api (so a base rerun preserves them);
notes cite the directive. No physical deletes.

  python scripts/_apply_m02_dir001_readfield_fix_20260619.py --dry-run
  python scripts/_apply_m02_dir001_readfield_fix_20260619.py --live
"""
import argparse, os, shutil, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SNAP = os.path.join("backups", "bible_research_pre-m02-dir001_20260619.db")
STAMP = "2026-06-19T00:00:00Z"
NOTE_A = "DIR-20260619-001 corr A: divine-wrath valence sinful->neutral (sinful framing belongs to the provoking human sin, not God's wrath)"
NOTE_B = "DIR-20260619-001 corr B: independent re-read — LORD as agent of the kindled anger (routes C1->C2)"

CRIT_A = """
SELECT vc.id vcid, vr.reference ref, m.strongs_number st, m.transliteration tr,
       vsal.id valence_row_id, vsal.value valence, vsal.source_provenance prov
FROM verse_context vc
JOIN mti_terms m ON m.id=vc.mti_term_id
JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
JOIN ve_lexical vsal ON vsal.verse_context_id=vc.id AND vsal.ve_label='valence' AND COALESCE(vsal.delete_flagged,0)=0
JOIN ve_lexical vdiv ON vdiv.verse_context_id=vc.id AND vdiv.ve_label='divine-involvement' AND COALESCE(vdiv.delete_flagged,0)=0
WHERE m.cluster_code='M02' AND vsal.value='sinful' AND vdiv.value IN ('agent','possessor','giver')
  AND (m.strongs_number LIKE 'H2534%' OR m.strongs_number LIKE 'H2734%' OR m.strongs_number LIKE 'H2740%'
       OR m.strongs_number LIKE 'H7107%' OR m.strongs_number LIKE 'H7110%' OR m.strongs_number LIKE 'G3709%')
ORDER BY vr.book_id, vr.chapter, vr.verse_num"""

# Correction B targets: (reference, strongs-like)
B_TARGETS = [("Exo 4:14", "H2734%"), ("2Ki 13:3", "H2734%")]


def find_b_rows(cur):
    out = []
    for ref, like in B_TARGETS:
        r = cur.execute("""SELECT vc.id vcid, m.strongs_number st
            FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
            JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            WHERE vr.reference=? AND m.cluster_code='M02' AND m.strongs_number LIKE ?""", (ref, like)).fetchone()
        existing = None
        if r:
            existing = cur.execute("""SELECT id, value FROM ve_lexical WHERE verse_context_id=?
                AND ve_label='divine-involvement' AND COALESCE(delete_flagged,0)=0""", (r["vcid"],)).fetchone()
        out.append((ref, r, existing))
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    rows_a = cur.execute(CRIT_A).fetchall()
    print(f"== Correction A — {len(rows_a)} divine-wrath valence rows sinful->neutral ==")
    for r in rows_a:
        print(f"   {r['ref']:10} {r['st']:8} {r['tr']:10} valence={r['valence']} ({r['prov']})")
    rows_b = find_b_rows(cur)
    print(f"\n== Correction B — insert divine-involvement='agent' ==")
    for ref, r, existing in rows_b:
        if not r:
            print(f"   {ref}: TERM NOT FOUND — abort"); return 2
        print(f"   {ref:10} vc={r['vcid']} existing divine-involvement row: {existing['value'] if existing else 'NONE (will INSERT)'}")

    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0

    if not os.path.exists(SNAP):
        os.makedirs("backups", exist_ok=True); shutil.copy2(DB, SNAP); print(f"\nsnapshot: {SNAP}")

    # Correction A: update value + notes, keep source_provenance (valence_read_api) for base-rerun preservation
    for r in rows_a:
        cur.execute("UPDATE ve_lexical SET value='neutral', notes=? WHERE id=?", (NOTE_A, r["valence_row_id"]))
    # Correction B: insert divine-involvement='agent' (ve_nr 8 / T0.1.2), preserved provenance
    nins = 0
    for ref, r, existing in rows_b:
        if existing:
            cur.execute("UPDATE ve_lexical SET value='agent', notes=? WHERE id=?", (NOTE_B, existing["id"]))
        else:
            cur.execute("""INSERT INTO ve_lexical
                (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, delete_flagged, created_at)
                VALUES (?, 8, 'divine-involvement', 'T0.1.2', 'agent', ?, 'divine_involvement_read_api', 0, ?)""",
                (r["vcid"], NOTE_B, STAMP))
            nins += 1
    conn.commit()
    print(f"\nLIVE: corr A updated {len(rows_a)} valence rows; corr B inserted {nins} / updated {len(rows_b)-nins} divine-involvement rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
