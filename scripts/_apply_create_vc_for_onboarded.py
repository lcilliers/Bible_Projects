"""Create verse_context units for engine-onboarded terms (post-onboard catch-up step).

The engine onboarding creates mti_terms + wa_verse_records but NOT verse_context — so the
reset ve-lexical generator (which reads verse_context) has nothing to work on. This creates
one verse_context per active verse_record for the given registries (the term is the anchor of
its own verse). Idempotent: skips a verse_record that already has a verse_context for that term.

Then run:  python scripts/_apply_generate_ve_lexical_v2.py --live --vcids @<the printed file>

  python scripts/_apply_create_vc_for_onboarded.py --registries 216,217,218,219 [--dry-run]
"""
import argparse, os, sqlite3, datetime

DB = os.path.join("database", "bible_research.db")
OUTDIR = os.path.join("outputs", "integrity"); os.makedirs(OUTDIR, exist_ok=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registries", required=True, help="comma list of word_registry ids")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    regs = [int(x) for x in a.registries.split(",") if x.strip()]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # active verse_records for these registries, that have an mti_term_id and no existing verse_context
    rows = c.execute(f"""
        SELECT vr.id vr_id, vr.mti_term_id, vr.reference, vr.word_registry_fk
        FROM wa_verse_records vr
        WHERE vr.word_registry_fk IN ({','.join('?'*len(regs))})
          AND vr.mti_term_id IS NOT NULL
          AND (vr.delete_flagged=0 OR vr.delete_flagged IS NULL)
          -- only IN-CORPUS verses: the ve-lexical generator derives from the measure layer, which only
          -- exists for verses in the canonical `verse` table (~76% of canon). STEP returns full-Bible
          -- occurrences, so a term's verse_records can point outside the corpus (e.g. anash 2Sa 12:15).
          AND EXISTS (SELECT 1 FROM verse v WHERE v.reference=vr.reference)
          AND NOT EXISTS (SELECT 1 FROM verse_context vc
                          WHERE vc.verse_record_id=vr.id AND vc.mti_term_id=vr.mti_term_id
                          AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL))
        ORDER BY vr.word_registry_fk, vr.id""", regs).fetchall()
    print(f"verse_records needing verse_context: {len(rows)}")
    if a.dry_run:
        for r in rows[:10]: print("  would create vc for", r["reference"], "term", r["mti_term_id"], "reg", r["word_registry_fk"])
        print("  ...(dry-run, no writes)"); return

    new_ids = []
    for r in rows:
        c.execute("""INSERT INTO verse_context
            (verse_record_id, mti_term_id, is_anchor, is_relevant, is_related, triage_status, meaning_provenance, delete_flagged)
            VALUES (?,?,1,1,0,'ACCEPT','onboard_catchup',0)""", (r["vr_id"], r["mti_term_id"]))
        new_ids.append(c.lastrowid)
    conn.commit()
    idfile = os.path.join(OUTDIR, "onboard_catchup_vcids.txt")
    open(idfile, "w").write(",".join(str(i) for i in new_ids))
    print(f"created {len(new_ids)} verse_context rows; ids -> {idfile}")
    print(f"next: python scripts/_apply_generate_ve_lexical_v2.py --live --vcids @{idfile}")
    conn.close()

if __name__ == "__main__":
    main()
