"""_apply_aramaic_stem_backfill_v1_20260615.py — derive wa_verse_records.stem IN-PLACE from the already-stored
morph_code for (a) Aramaic verbs (A-prefix) and (b) the Hebrew Nithpael 'D' binyan — the two completeness
residues from wa-mode-consistency-check-v1-20260615.md. NO STEP fetch; pure re-derivation from stored data.
Reversible (the affected rows currently have stem NULL/'?D'; restore by NULLing them).

  python scripts/_apply_aramaic_stem_backfill_v1_20260615.py --dry-run
  python scripts/_apply_aramaic_stem_backfill_v1_20260615.py --live
"""
import argparse, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# OSHB Aramaic verb-stem codes (differ from Hebrew: q=Peal not Qal, p=Pael not Piel, h=Haphel not Hiphil)
ARAMAIC_STEM = {"q": "Peal", "Q": "Peil", "u": "Hithpeel", "p": "Pael", "P": "Pual",
                "M": "Hithpaal", "a": "Aphel", "h": "Haphel", "s": "Saphel", "e": "Shaphel",
                "H": "Hophal", "i": "Hithaphel", "t": "Hishtaphel"}
HEB_EXTRA = {"D": "Nithpael"}  # the one Hebrew code missing from the backfill's map


def stem_from(mc):
    """stem from a stored morph_code; '' if not an applicable verb form."""
    if not mc or len(mc) < 3:
        return ""
    lang, cat, binyan = mc[0], mc[1], mc[2]
    if cat != "V":
        return ""
    if lang == "A":
        return ARAMAIC_STEM.get(binyan, "")
    if lang == "H":
        return HEB_EXTRA.get(binyan, "")  # only the previously-unmapped Hebrew codes
    return ""


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=60)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    rows = c.execute(
        "SELECT id, morph_code, stem FROM wa_verse_records "
        "WHERE COALESCE(delete_flagged,0)=0 AND (morph_code LIKE 'AV%' OR morph_code LIKE 'HVD%')"
    ).fetchall()

    plan, skipped = [], []
    for r in rows:
        new = stem_from(r["morph_code"])
        if new and new != (r["stem"] or ""):
            plan.append((r["id"], r["morph_code"], r["stem"], new))
        else:
            skipped.append(r["morph_code"])

    from collections import Counter
    by_stem = Counter(p[3] for p in plan)
    print(f"candidate rows: {len(rows)}  ·  to update: {len(plan)}  ·  unchanged/skip: {len(skipped)}")
    print("  new stems:", dict(by_stem))
    print("  sample:", [(p[1], p[2], "->", p[3]) for p in plan[:8]])

    if a.live:
        for rid, mc, old, new in plan:
            c.execute("UPDATE wa_verse_records SET stem=? WHERE id=?", (new, rid))
        conn.commit()
        print(f"LIVE: wrote stem to {len(plan)} rows.")
    else:
        print("DRY-RUN — no writes.")


if __name__ == "__main__":
    main()
