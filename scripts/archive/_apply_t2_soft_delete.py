"""_apply_t2_soft_delete.py — soft-delete Parked (T2) terms that NEVER co-occur with a characteristic.

Approved cleanup (researcher 2026-06-08, items 1+2 of the T2 net-path): a T2 term whose verses NEVER share a
reference with a characteristic-bearing verse cannot be a qualifier (nothing to enhance) and is not a
characteristic itself -> true noise -> soft-delete (delete_flagged=1, reversible). Terms that DO co-occur
(qualifier-candidate or low) are LEFT in place — their disposition (qualifier vs noise) is an L2 verse-read
judgement, not mechanical. §A characteristics already moved.

A verse REFERENCE is characteristic-bearing if any wa_verse_records row at that reference belongs to a term
whose mti_terms.cluster_code is a real cluster (not T2/FLAG) and is not delete_flagged.

Usage:
  python scripts/_apply_t2_soft_delete.py --dry-run --out research/investigations/<file>.md
  python scripts/_apply_t2_soft_delete.py --live    --out research/investigations/<file>.md
"""
import argparse, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    # cluster_code per mti_terms.id (the join key in wa_verse_records is mti_term_id; term_id is NOT mti_terms.id)
    clus = {r["id"]: r["cluster_code"] for r in
            c.execute("SELECT id, cluster_code FROM mti_terms WHERE COALESCE(delete_flagged,0)=0")}

    # single pass over active verse rows: reference -> set of cluster_codes present; mti_id -> set of refs
    char_refs = set()
    refs_by_mti = {}
    for r in c.execute("SELECT reference, mti_term_id FROM wa_verse_records "
                       "WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL AND reference IS NOT NULL"):
        ref = r["reference"]; mid = r["mti_term_id"]
        cc = clus.get(mid)
        if cc is not None and cc not in ("T2", "FLAG"):
            char_refs.add(ref)
        refs_by_mti.setdefault(mid, set()).add(ref)

    # classify active T2 terms
    terms = c.execute(
        "SELECT id, strongs_number, transliteration, gloss, owning_word FROM mti_terms "
        "WHERE cluster_code='T2' AND COALESCE(delete_flagged,0)=0").fetchall()
    never, no_verses, co_occur = [], [], []
    for t in terms:
        refs = refs_by_mti.get(t["id"], set())
        if not refs:
            no_verses.append((t, 0, 0))
        elif refs & char_refs:
            co_occur.append((t, len(refs), len(refs & char_refs)))
        else:
            never.append((t, len(refs), 0))

    targets = never + no_verses  # the soft-delete set
    print(f"char-bearing references: {len(char_refs)}")
    print(f"T2 active: {len(terms)} | never-co-occur: {len(never)} | no-verses: {len(no_verses)} "
          f"| co-occur (KEEP for L2): {len(co_occur)}")
    print(f"=> soft-delete target: {len(targets)}")

    # 3. write the audit list
    L = ["# T2 soft-delete — never-co-occur terms (true noise)", ""]
    L.append("> `scripts/_apply_t2_soft_delete.py`. These T2 terms' verses NEVER share a reference with a "
             "characteristic-bearing verse, so they cannot be qualifiers and are not characteristics -> "
             "soft-deleted (delete_flagged=1, reversible). The §B deep-dive (why STEP suggested them) can still "
             "run on this list. Terms that DO co-occur are LEFT for L2 verse-read disposition.")
    L.append("")
    L.append(f"**Mode: {'DRY-RUN (nothing written)' if a.dry_run else 'LIVE (soft-deleted)'}** — "
             f"target {len(targets)} (never-co-occur {len(never)} + no-verses {len(no_verses)}).")
    L.append("")
    L.append("## Soft-deleted (never co-occur with a characteristic)")
    L.append(""); L.append("| Term | Gloss | Parked-under | n verses |"); L.append("|---|---|---|---|")
    for t, nv, _ in sorted(targets, key=lambda x: (-x[1], x[0]["gloss"] or "")):
        L.append(f"| {t['strongs_number']} {t['transliteration']} | {t['gloss']} | {t['owning_word'] or ''} | {nv} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))

    if a.live:
        ids = [t["id"] for t, _, _ in targets]
        c.executemany("UPDATE mti_terms SET delete_flagged=1, last_changed=datetime('now') WHERE id=?",
                      [(i,) for i in ids])
        conn.commit()
        print(f"LIVE: soft-deleted {len(ids)} T2 terms.")
    print(f"Wrote {a.out}")


if __name__ == "__main__":
    main()
