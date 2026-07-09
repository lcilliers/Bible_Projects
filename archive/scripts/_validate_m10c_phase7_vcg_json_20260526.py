"""Validate the AI's M10c Phase 7 VCG creation JSON against the DB.

Checks per §10.8:
  1. Sub-group set matches DB (5 sub-groups).
  2. Verses per sub-group match DB counts.
  3. Every vc_id in JSON exists in DB, is is_relevant=1, routed to the named sub-group.
  4. Anchor vc_id is member of its VCG's verses array.
  5. No vc_id appears in two VCGs (unless dual-membership flagged).
  6. All 263 cluster verses appear exactly once.
  7. Field name is `verses` (not `key_verses`, `members`, etc.).
"""
from __future__ import annotations
import io, json, sqlite3, sys
from collections import Counter, defaultdict
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
VCG_JSON = REPO / "Sessions" / "Session_Clusters" / "M10c" / "files phase 7" / "wa-cluster-M10c-vcg-creation-v1_0-20260526.json"
CLUSTER = "M10c"


def main() -> int:
    spec = json.loads(VCG_JSON.read_text(encoding="utf-8"))
    print("== Meta ==")
    print(json.dumps(spec.get("_meta", {}), indent=2))

    sg_keys_in_json = [k for k in spec.keys() if k.startswith(f"{CLUSTER}-")]
    print(f"\nSub-groups in JSON: {len(sg_keys_in_json)} -> {sg_keys_in_json}")

    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(f"""
        SELECT cs.subgroup_code, vc.id AS vc_id
        FROM cluster_subgroup cs
        JOIN verse_context vc ON vc.cluster_subgroup_id = cs.id
        WHERE cs.cluster_code='{CLUSTER}' AND COALESCE(cs.delete_flagged,0)=0
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """).fetchall()
    db_by_sg: dict[str, set[int]] = defaultdict(set)
    for r in rows:
        db_by_sg[r["subgroup_code"]].add(r["vc_id"])
    db_subgroups = set(db_by_sg.keys())
    json_subgroups = set(sg_keys_in_json)
    print(f"DB sub-groups: {len(db_subgroups)} -> {sorted(db_subgroups)}")

    issues_total = 0
    extra = json_subgroups - db_subgroups
    missing = db_subgroups - json_subgroups
    if extra:
        print(f"  [ERROR] sub-groups in JSON not in DB: {extra}")
        issues_total += len(extra)
    if missing:
        print(f"  [ERROR] sub-groups in DB not in JSON: {missing}")
        issues_total += len(missing)

    print("\n== Per-sub-group ==")
    print(f"{'Code':<10} {'JSON V':>6} {'DB V':>6} {'#VCGs':>6} {'Anchor OK':>10}  Issues")
    total_json = 0
    total_db = 0
    all_json_vc: list[int] = []
    forbidden_field_hits = 0
    for code in sorted(db_subgroups | json_subgroups):
        sg = spec.get(code, {})
        vcgs = sg.get("vcgs", [])
        sg_vc_ids: list[int] = []
        anchor_ok = True
        for v in vcgs:
            for forbidden in ("key_verses", "members", "representative_verses", "sample_verses"):
                if forbidden in v:
                    forbidden_field_hits += 1
                    print(f"  [ERROR] VCG {v.get('provisional_code')} uses forbidden field '{forbidden}'")
            verses = v.get("verses") or []
            sg_vc_ids.extend(verses)
            anchor = v.get("anchor_vc_id")
            if anchor and anchor not in verses:
                anchor_ok = False
                print(f"  [ERROR] anchor {anchor} not in verses of {v.get('provisional_code')}")
        json_v_set = set(sg_vc_ids)
        db_v_set = db_by_sg.get(code, set())
        n_dup = len(sg_vc_ids) - len(json_v_set)
        only_in_json = json_v_set - db_v_set
        only_in_db = db_v_set - json_v_set
        issues: list[str] = []
        if n_dup:
            issues.append(f"intra-sg-dup={n_dup}")
        if only_in_json:
            issues.append(f"only-in-JSON={len(only_in_json)}")
        if only_in_db:
            issues.append(f"only-in-DB={len(only_in_db)}")
        if not anchor_ok:
            issues.append("anchor-not-in-members")
        if issues:
            issues_total += len(issues)
        print(f"{code:<10} {len(sg_vc_ids):>6} {len(db_v_set):>6} {len(vcgs):>6} {('Y' if anchor_ok else 'N'):>10}  {' '.join(issues) or '-'}")
        if only_in_json:
            print(f"    only-in-JSON sample: {sorted(only_in_json)[:5]}")
        if only_in_db:
            print(f"    only-in-DB sample: {sorted(only_in_db)[:5]}")
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

    if forbidden_field_hits:
        issues_total += forbidden_field_hits

    print(f"\n==> Total issues: {issues_total}")
    return 0 if issues_total == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
