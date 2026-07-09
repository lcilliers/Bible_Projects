"""_apply_h7563_ingest_missing_69_20260622.py — ingest the 69 truncation-missing rāšāʿ (H7563) verses.

Context: STEP's 60-cap silently truncated H7563 to 180/249 (Psa 46 / Pro 17 / Ecc 6 missing). The
step_client was fixed (forward-walk) on 2026-06-22. This adds ONLY H7563's 69 missing term-in-verse
rows + verse_context shells, mirroring the existing 180 (mti_term 1223, registry 172, M10b, OWNER).

Idempotent + dedup-guarded (wa_verse_records has no UNIQUE index): inserts only references not already
present for mti_term_id=1223. NO set-aside reinstatement (researcher: existing set-asides are legitimate).
ke.mo/G0458 out of scope (researcher decision). verse_id is left NULL here — set next by
_apply_ingest_verse_morphology.py (which also fetches the measure layer for the 3 corpus-absent verses).

  python scripts/_apply_h7563_ingest_missing_69_20260622.py --dry-run | --live
"""
import argparse, os, sqlite3, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
from step_client import StepClient
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-22T00:00:00Z"
MTI_ID = 1223           # H7563 ra.sha "wicked"
# constants copied from the existing 180 H7563 wa_verse_records rows (the template)
CONST = dict(file_id=201, term_inv_id=1348, term_id="H7563", transliteration="ra.sha",
             testament="OT", translation="ESV", mti_term_id=MTI_ID, word_registry_fk=172)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    bmap = {r["short_code"]: r["id"] for r in cur.execute("SELECT id, short_code FROM books")}

    # 1) authoritative STEP pull (fixed client) + existing DB refs
    sc = StepClient()
    step = {r["ref"]: r for r in sc.get_verse_records("H7563")}
    existing = {r["reference"] for r in cur.execute(
        "SELECT DISTINCT reference FROM wa_verse_records WHERE mti_term_id=?", (MTI_ID,))}
    missing = [step[ref] for ref in step if ref not in existing]
    missing.sort(key=lambda r: (r["book_code"], r["chapter"], r["verse_num"]))
    print(f"STEP={len(step)} · DB existing={len(existing)} · to insert={len(missing)}")
    if len(step) != 249:
        print(f"  WARNING: STEP returned {len(step)} (expected 249) — aborting."); return 2

    inserted_vr = []
    for r in missing:
        ref = r["ref"]; b3 = ref.split(" ")[0]; bid = bmap.get(b3)
        if bid is None:
            print(f"  !! no book_id for {ref} (prefix {b3}) — skip"); continue
        vt = r["esv_text"] if r["esv_text"].startswith(ref) else f"{ref} {r['esv_text']}"
        row = dict(CONST, reference=ref, last_changed=STAMP, book_id=bid, chapter=r["chapter"],
                   verse_num=r["verse_num"], target_word=r["target_word"], span_strong_match=1,
                   delete_flagged=0, morph_code=r["morph_code"], stem=(r["stem"] or None),
                   verse_id=None, verse_text=vt, created_at=STAMP, updated_at=STAMP)
        if a.live:
            cols = ",".join(row.keys()); ph = ",".join("?" * len(row))
            cur.execute(f"INSERT INTO wa_verse_records ({cols}) VALUES ({ph})", list(row.values()))
            inserted_vr.append((cur.lastrowid, ref))
        else:
            inserted_vr.append((None, ref))

    print(f"\nStage A — wa_verse_records: {len(inserted_vr)} rows "
          f"({'INSERTED' if a.live else 'would insert'}); books "
          f"{ {b3: sum(1 for _,rf in inserted_vr if rf.split(' ')[0]==b3) for b3 in sorted({rf.split(' ')[0] for _,rf in inserted_vr})} }")

    # 2) verse_context shells (mti_term 1223 -> M10b via the join). is_relevant=1 default for a real occurrence.
    new_vcids = []
    if a.live:
        for vrid, ref in inserted_vr:
            cur.execute("""INSERT INTO verse_context
                (verse_record_id, mti_term_id, is_anchor, is_relevant, is_related, delete_flagged)
                VALUES (?, ?, 0, 1, 0, 0)""", (vrid, MTI_ID))
            new_vcids.append(cur.lastrowid)
        conn.commit()
        with open("outputs/_tmp_h7563_new_vcids.txt", "w") as fh:
            fh.write(",".join(str(v) for v in new_vcids))
        print(f"Stage B — verse_context: {len(new_vcids)} shells inserted; vcids -> outputs/_tmp_h7563_new_vcids.txt")
        # verify: no duplicate (reference, mti_term_id) for H7563
        dup = cur.execute("""SELECT COUNT(*) n FROM (SELECT reference FROM wa_verse_records
            WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0 GROUP BY reference HAVING COUNT(*)>1)""", (MTI_ID,)).fetchone()["n"]
        tot = cur.execute("SELECT COUNT(DISTINCT reference) n FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (MTI_ID,)).fetchone()["n"]
        print(f"  H7563 distinct verses now: {tot} (target 249) · duplicate-reference groups: {dup}")
        print("  integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    else:
        print(f"Stage B — verse_context: would insert {len(inserted_vr)} shells")
        print("\n[DRY-RUN] no changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
