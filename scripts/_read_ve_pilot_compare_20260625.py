"""_read_ve_pilot_compare_20260625.py (READ-ONLY) — pilot validation of the RESET fidelity fixes.

For each requested reference, find its M12 term-in-verse unit(s), run the patched engine `derive()`
(the new fidelity + delta logic), and print:
  (A) the EXISTING ve_lexical rows in the DB  (the "before")
  (B) the freshly-derived items              (the "after", with fixes)
so the researcher can validate that the reviewed errors are corrected. No DB writes.

  python -X utf8 scripts/_read_ve_pilot_compare_20260625.py --refs "Psa 24:4,Mat 5:8" [--cluster M12]
"""
import argparse, os, sqlite3, sys
sys.path.insert(0, os.path.dirname(__file__))
import _ve_engine_v2 as eng
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# fields worth foregrounding for the review (the ones the fixes touch)
FOCUS = ["sense", "object", "object-type", "from-source", "quality-bearer", "operation",
         "how", "location", "immediate-response", "cause", "cause_clause", "compound",
         "relational", "experiencer", "valence", "discovery"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refs", required=True)
    ap.add_argument("--cluster", default="M12")
    a = ap.parse_args()
    refs = [r.strip() for r in a.refs.split(",") if r.strip()]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    lex = eng.LexDB(cur)

    for ref in refs:
        units = cur.execute("""
            SELECT vc.id vcid, vc.mti_term_id mti, vr.transliteration translit, m.gloss gloss,
                   m.strongs_number strong, m.cluster_code cluster, vr.reference rref, vr.target_word tw, v.id verse_id,
                   v.verse_text vtext
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            JOIN mti_terms m ON m.id = vc.mti_term_id
            JOIN verse v ON v.reference = vr.reference
            WHERE vr.reference=? AND m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
            ORDER BY vc.id""", (ref, a.cluster)).fetchall()
        if not units:
            print(f"\n===== {ref} — no {a.cluster} unit =====")
            continue
        vtext = units[0]["vtext"]
        print(f"\n{'='*78}\n{ref}  —  {vtext}\n{'='*78}")
        words = eng.load_words(cur, units[0]["verse_id"])
        for u in units:
            coterms = cur.execute("""SELECT DISTINCT vr.transliteration tr, m.gloss gl, m.cluster_code cc, m.strongs_number st
                FROM verse_context vc2 JOIN wa_verse_records vr ON vr.id=vc2.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
                JOIN mti_terms m ON m.id=vc2.mti_term_id
                WHERE vr.reference=? AND m.strongs_number<>? AND COALESCE(vc2.delete_flagged,0)=0""",
                (u["rref"], u["strong"])).fetchall()
            unit = {"ref": u["rref"], "translit": u["translit"], "gloss": u["gloss"], "strong": u["strong"],
                    "cluster": u["cluster"], "tw": u["tw"],
                    "coterms": [(c["tr"], c["gl"], c["cc"], c["st"]) for c in coterms]}
            print(f"\n  --- term: {u['translit']} ({u['strong']}) \"{u['gloss']}\"  [vcid {u['vcid']}] ---")

            # (A) BEFORE — existing rows in DB
            before = cur.execute("""SELECT ve_label, value FROM ve_lexical
                WHERE verse_context_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr, id""", (u["vcid"],)).fetchall()
            bd = {}
            for r in before:
                bd.setdefault(r["ve_label"], []).append(r["value"])
            print("   BEFORE (DB):")
            if before:
                for lbl in sorted(bd):
                    print(f"      {lbl:18} = {' | '.join(str(x) for x in bd[lbl])}")
            else:
                print("      (none in DB yet)")

            # (B) AFTER — fresh derive() with fixes
            items = eng.derive(unit, words, lex)
            ad = {}
            for (it, value, cite) in items:
                ad.setdefault(it, []).append((value, cite))
            print("   AFTER (patched derive):")
            order = [f for f in FOCUS if f in ad] + [f for f in sorted(ad) if f not in FOCUS]
            for it in order:
                for (value, cite) in ad[it]:
                    flag = ""
                    if it in ("object", "from-source", "quality-bearer", "operation"):
                        flag = "  ◀ FIX"
                    if it in ("immediate-response", "cause", "cause_clause") and "[" in str(value):
                        flag = "  ◀ tense"
                    print(f"      {it:18} = {value}{flag}")
                    if cite and it in ("object", "from-source", "quality-bearer", "operation"):
                        print(f"      {'':18}   ({cite})")


if __name__ == "__main__":
    main()
