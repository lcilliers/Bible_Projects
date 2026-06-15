"""_apply_migrate_ve_findings_to_lexical.py (2026-06-15) — retrofit the VE field-value findings OUT of
the finding table INTO ve_lexical (the items-in-verse-level table), leaving only real findings in finding.

Rules (per researcher):
  - one row per VALUE (no delimited lists);
  - only values ACTUALLY present (drop NONE / empty / imputed);
  - keyed on verse_context_id; columns ve_nr · ve_label · related_tier · value · notes (+ source_provenance);
  - where l2_api and l2_mechanical both have a value for the same (verse_context, question), keep l2_api (the read).
Then soft-delete every migrated VERSE l2_api/l2_mechanical finding (the real ones now live in ve_lexical;
the NONE ones are dropped). finding is left holding CLUSTER/GLOBAL real findings + l2_meaning.

Reversible: ve_lexical rows carry created_at='M59-migration' (deletable); the source findings are soft-deleted
(delete_flagged=1), not removed — restore by NULLing them.

  python scripts/_apply_migrate_ve_findings_to_lexical.py --dry-run
  python scripts/_apply_migrate_ve_findings_to_lexical.py --live
"""
import argparse, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "M59-migration-20260615"

# component_title -> ve_nr (the VE grouping). ve_label keeps the specific component_title (readable);
# related_tier keeps the specific question_code (e.g. T3.4.1) so faculty/location members stay distinct.
VE_NR = {
    "Lexical and Semantic Analysis": 1,      # sense
    "Kind": 2,                                # type
    "Co-occurrence": 3,                       # compound
    "Modes of Operation": 4,                  # mode of operation (manner; morph-mode stays a column)
    "Heart": 5, "Mind": 5, "Soul-Level Location": 5, "Spirit-Level Location": 5, "Body — Significance": 5,  # location
    "Origin and Source": 6,                   # origin
    "Perception": 7, "Cognition": 7, "Memory": 7, "Affect": 7, "Creativity": 7, "Volition": 7,
    "Agency": 7, "Moral Evaluation": 7, "Conscience": 7, "Relational Capacity": 7,                          # faculty
    "Divine Nature Reflected": 8,             # attributed_to_God
    "Created Purpose": 9,                     # purpose_equips
    "Typological Significance": 10,           # typology_direction
    "Immediate Response": 11,                 # immediate_response
    "Sustained Effect": 12,                   # produces_effect
    "Verse and Literary Interpretation": 14,  # literary_setting
    "Name and Naming": 15,                    # name_and_naming (extra; outside the 14)
}


def is_none(v):
    return v is None or v.strip() == "" or v.strip().lower() == "none"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # pull all VE field-value findings (l2_api first so it wins the de-dup)
    rows = cur.execute("""
        SELECT f.id fid, f.verse_context_id vc, l.question_id qid, q.component_title field,
               q.question_code qcode, f.finding_value val, f.provenance prov
        FROM finding f
        JOIN finding_question_link l ON l.finding_id = f.id
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        WHERE f.provenance IN ('l2_api','l2_mechanical') AND f.level='VERSE' AND COALESCE(f.delete_flagged,0)=0
        ORDER BY CASE f.provenance WHEN 'l2_api' THEN 0 ELSE 1 END
    """).fetchall()

    seen = set()                 # (vc, qid) already taken (l2_api wins)
    inserts = []
    migrated_fids = []           # all source findings to soft-delete (incl NONE)
    dropped_none = 0
    for r in rows:
        migrated_fids.append(r["fid"])
        if is_none(r["val"]):
            dropped_none += 1
            continue
        key = (r["vc"], r["qid"])
        if key in seen:
            continue             # already have a value for this field on this verse (l2_api kept)
        seen.add(key)
        inserts.append((r["vc"], VE_NR.get(r["field"]), r["field"], r["qcode"], r["val"], r["prov"]))

    print(f"source VE findings: {len(migrated_fids):,}  ·  NONE dropped: {dropped_none:,}  ·  ve_lexical rows to write: {len(inserts):,}")
    unmapped = sorted({r["field"] for r in rows if r["field"] not in VE_NR})
    if unmapped:
        print(f"  WARN unmapped fields (ve_nr NULL): {unmapped}")

    if a.live:
        cur.executemany(
            "INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, source_provenance, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(vc, nr, lab, tier, val, prov, STAMP) for (vc, nr, lab, tier, val, prov) in inserts])
        n_ins = cur.rowcount
        # soft-delete the migrated source findings (+ their question links stay; finding row flagged)
        nd = 0
        for i in range(0, len(migrated_fids), 400):
            ch = migrated_fids[i:i+400]
            cur.execute(f"UPDATE finding SET delete_flagged=1 WHERE id IN ({','.join('?'*len(ch))})", ch)
            nd += cur.rowcount
        conn.commit()
        print(f"LIVE: ve_lexical +{len(inserts):,} rows · soft-deleted {nd:,} source findings")
    else:
        print("DRY-RUN — no writes.")


if __name__ == "__main__":
    main()
