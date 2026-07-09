"""Validate the AI's Phase 7 VCG creation JSON against the M10 DB.

Checks:
  1. Sub-group set matches DB (23 sub-groups, no extras, none missing).
  2. Verses per sub-group match DB counts.
  3. Every vc_id in JSON exists in DB, is is_relevant=1, routed to the named sub-group.
  4. Anchor vc_id ∈ its VCG's verses array.
  5. No vc_id appears in two VCGs (unless dual-membership flagged).
  6. All 1,325 cluster verses appear exactly once.
  7. M10-BND has exactly 1 VCG with 5 verses.
"""
from __future__ import annotations
import io, json, sqlite3, sys
from collections import Counter, defaultdict
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
VCG_JSON = REPO / "Sessions" / "Session_Clusters" / "M10" / "files phase 7" / "wa-cluster-M10-vcg-creation-v1-20260523.json"


def main() -> int:
    spec = json.loads(VCG_JSON.read_text(encoding="utf-8"))
    print("== Meta ==")
    print(json.dumps(spec.get("_meta", {}), indent=2))

    sgs = spec["subgroups"]
    print(f"\nSub-groups in JSON: {len(sgs)}")

    # DB state
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    # Per-sub-group DB vc_ids
    rows = conn.execute("""
        SELECT cs.subgroup_code, vc.id AS vc_id
        FROM cluster_subgroup cs
        JOIN verse_context vc ON vc.cluster_subgroup_id = cs.id
        WHERE cs.cluster_code='M10' AND COALESCE(cs.delete_flagged,0)=0
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """).fetchall()
    db_by_sg = defaultdict(set)
    for r in rows:
        db_by_sg[r["subgroup_code"]].add(r["vc_id"])
    db_subgroups = set(db_by_sg.keys())
    json_subgroups = set(sgs.keys())
    print(f"DB sub-groups: {len(db_subgroups)}")

    extra = json_subgroups - db_subgroups
    missing = db_subgroups - json_subgroups
    if extra:
        print(f"  [ERROR] sub-groups in JSON not in DB: {extra}")
    if missing:
        print(f"  [ERROR] sub-groups in DB not in JSON: {missing}")

    # Per-sub-group check
    print("\n== Per-sub-group ==")
    print(f"{'Code':<10} {'JSON V':>6} {'DB V':>6} {'#VCGs':>6} {'Anchor OK':>10}  {'Issues'}")
    total_json = 0
    total_db = 0
    all_json_vc: list[int] = []
    issues_total = 0
    for code in sorted(db_subgroups | json_subgroups):
        sg = sgs.get(code, {})
        vcgs = sg.get("vcgs", [])
        sg_vc_ids: list[int] = []
        anchor_ok = True
        for v in vcgs:
            verses = v.get("verses") or []
            sg_vc_ids.extend(verses)
            anchor = v.get("anchor_vc_id")
            if anchor and anchor not in verses:
                anchor_ok = False
                issues_total += 1
        json_v_set = set(sg_vc_ids)
        db_v_set = db_by_sg.get(code, set())
        n_dup = len(sg_vc_ids) - len(json_v_set)
        only_in_json = json_v_set - db_v_set
        only_in_db = db_v_set - json_v_set
        issues = []
        if n_dup:
            issues.append(f"dup={n_dup}")
        if only_in_json:
            issues.append(f"only-in-JSON={len(only_in_json)}")
        if only_in_db:
            issues.append(f"only-in-DB={len(only_in_db)}")
        if not anchor_ok:
            issues.append("anchor-not-in-members")
        if issues:
            issues_total += len(issues)
        print(f"{code:<10} {len(sg_vc_ids):>6} {len(db_v_set):>6} {len(vcgs):>6} {('Y' if anchor_ok else 'N'):>10}  {' '.join(issues) or '-'}")
        total_json += len(sg_vc_ids)
        total_db += len(db_v_set)
        all_json_vc.extend(sg_vc_ids)

    print(f"\nTotals: JSON={total_json}, DB={total_db}")
    dup_global = Counter(all_json_vc)
    dups = {vc: c for vc, c in dup_global.items() if c > 1}
    if dups:
        print(f"[ERROR] Global duplicates ({len(dups)} vc_ids appear in >1 VCG):")
        for vc, c in list(dups.items())[:10]:
            print(f"  vc_id={vc} appears {c} times")
        issues_total += len(dups)
    else:
        print("No global duplicates.")

    # M10-BND check
    bnd = sgs.get("M10-BND", {})
    bnd_vcgs = bnd.get("vcgs", [])
    if len(bnd_vcgs) != 1 or len(bnd_vcgs[0].get("verses") or []) != 5:
        print(f"[ERROR] M10-BND must have 1 VCG with 5 verses; found {len(bnd_vcgs)} VCG(s) "
              f"with {sum(len(v.get('verses') or []) for v in bnd_vcgs)} verses")
        issues_total += 1

    print(f"\n==> Total issues: {issues_total}")
    return 0 if issues_total == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
