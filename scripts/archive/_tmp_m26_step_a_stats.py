"""Throwaway stats summary for Step A output."""
import json
import os
import sqlite3
import statistics
from collections import Counter

P = "outputs/markdown/m26-meanings-claude-sonnet-4-6-20260509.jsonl"

rows = [json.loads(l) for l in open(P, encoding="utf-8") if l.strip()]
print(f"Total records: {len(rows)}")
print(f"Distinct vr_ids: {len({r['vr_id'] for r in rows})}")
print(f"Distinct mti_term_ids: {len({r['mti_term_id'] for r in rows})}")

lens = [len(r["meaning"].split()) for r in rows]
ev = [len(r["evidence_quote"].split()) for r in rows]
print(f"meaning words : min={min(lens)} median={statistics.median(lens):.0f} "
      f"max={max(lens)} mean={statistics.mean(lens):.1f}")
print(f"evidence words: min={min(ev)} median={statistics.median(ev):.0f} "
      f"max={max(ev)} mean={statistics.mean(ev):.1f}")
print(f"over-limit  meaning>25w : {sum(1 for x in lens if x>25)}")
print(f"over-limit evidence>15w : {sum(1 for x in ev if x>15)}")

conn = sqlite3.connect(os.path.join("database", "bible_research.db"))
conn.row_factory = sqlite3.Row
term_meta = {
    r["id"]: dict(r) for r in conn.execute(
        "SELECT mt.id, mt.strongs_number, mt.gloss, cs.subgroup_code "
        "  FROM mti_terms mt "
        "  LEFT JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id "
        " WHERE mt.cluster_code='M26' AND COALESCE(mt.delete_flagged,0)=0"
    )
}

sg_counts = Counter()
for r in rows:
    m = term_meta.get(r["mti_term_id"])
    sg = (m["subgroup_code"] if m and m["subgroup_code"] else "UNASSIGNED")
    sg_counts[sg] += 1
print()
print("Verses per sub-group:")
for sg, n in sorted(sg_counts.items()):
    print(f"  {sg:20s} {n}")

# 5 longest meanings (sanity check)
print()
print("5 longest meanings:")
for r in sorted(rows, key=lambda x: -len(x["meaning"]))[:5]:
    print(f"  ({len(r['meaning'].split())}w) {r['strong']:8s} {r['meaning']}")
