"""_apply_m03_out_of_scope_setaside_20260620.py — apply the M03 out-of-scope set-aside (DB).

Source of truth: wa-m03-ve-out-of-scope-v1_0-20260619.json (`records` = 69 specific occurrences; homonyms/literal
with NO inner-being content). Governance: GR-PROG-005 (researcher-approved). Mechanism, per the M01 precedent:
  - occurrence-level: verse_context.set_aside_reason on each matched (reference, strong) occurrence;
  - term-level: where ALL of a sub-entry's active M03 occurrences are out-of-scope, also set mti_terms.cluster_code
    = NULL + exclusion_reason (the homonym sub-entry leaves M03 entirely, like M01 H3724B/C/D).
Reversible (set_aside_reason cleared; cluster_code restored). No physical deletes. Dry-run previews.

  python scripts/_apply_m03_out_of_scope_setaside_20260620.py --dry-run | --live
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SRC = "Sessions-v2/M03-Grief/findings/wa-m03-ve-out-of-scope-v1_0-20260619.json"
STAMP = "2026-06-20"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    recs = json.load(open(SRC, encoding="utf-8"))["records"]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # resolve each record to its M03 verse_context
    matched, unmatched = [], []
    for r in recs:
        row = cur.execute("""SELECT vc.id vcid, COALESCE(vc.set_aside_reason,'') sar
            FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
            JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            WHERE vr.reference=? AND m.strongs_number=? AND m.cluster_code='M03' AND COALESCE(vc.delete_flagged,0)=0""",
            (r["reference"], r["strong"])).fetchone()
        (matched if row else unmatched).append((r, row))
    print(f"records: {len(recs)} · matched to an active M03 verse_context: {len(matched)} · unmatched: {len(unmatched)}")
    if unmatched:
        for r, _ in unmatched[:10]:
            print(f"   UNMATCHED {r['reference']:10} {r['strong']:8} {r['term']} ({r['sense']})")

    # term-level: sub-entries whose ALL active M03 occurrences are in the out-of-scope set
    bystrong = {}
    for r, row in matched:
        bystrong.setdefault(r["strong"], 0)
        bystrong[r["strong"]] += 1
    print("\nper sub-entry (out-of-scope matched vs total active M03 occ):")
    term_null = []
    for strong, n_oos in sorted(bystrong.items()):
        total = cur.execute("""SELECT COUNT(*) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
            JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            WHERE m.strongs_number=? AND m.cluster_code='M03' AND COALESCE(vc.delete_flagged,0)=0""", (strong,)).fetchone()[0]
        full = (n_oos == total)
        if full:
            term_null.append(strong)
        print(f"   {strong:8} out-of-scope {n_oos}/{total}  ->  {'TERM-LEVEL cluster_code=NULL (fully out)' if full else 'occurrence-level set_aside only'}")

    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0

    nocc = 0
    for r, row in matched:
        reason = f"M03 out-of-scope (DIR-style set-aside {STAMP}): {r['term']} {r['sense']} — {r['reason']}"
        cur.execute("UPDATE verse_context SET set_aside_reason=? WHERE id=?", (reason, row["vcid"])); nocc += 1
    nterm = 0
    for strong in term_null:
        cur.execute("""UPDATE mti_terms SET cluster_code=NULL,
            exclusion_reason=COALESCE(exclusion_reason||' | ','')||? WHERE strongs_number=? AND cluster_code='M03'""",
            (f"M03 out-of-scope set-aside {STAMP}: homonym/literal, no inner-being content (all occ out-of-scope)", strong))
        nterm += cur.rowcount
    conn.commit()
    print(f"\nLIVE: set_aside_reason on {nocc} occurrences; cluster_code=NULL on {nterm} fully-out sub-entries.")
    print("M03 active focus occ after:", cur.execute("""SELECT COUNT(*) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        WHERE m.cluster_code='M03' AND COALESCE(vc.delete_flagged,0)=0 AND vc.set_aside_reason IS NULL""").fetchone()[0])
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
