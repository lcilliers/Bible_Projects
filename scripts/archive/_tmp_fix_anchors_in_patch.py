"""Promote first relevant verse per term to is_anchor=1 where the term has no
existing anchor in DB. Resolves R4 integrity for VCNEW Phase 2 patches.
"""
import json, sqlite3, sys
from pathlib import Path

PATCH = Path("Sessions/Session_Clusters/M46/wa-cluster-M46-patch-vcnew-utreview-api-v1-20260514.json")
DB = "database/bible_research.db"

p = json.loads(PATCH.read_text(encoding="utf-8"))
ops = p["operations"]

# Find terms in this patch
terms = sorted(set(o["record"]["mti_term_id"] for o in ops))

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# Per term: does it already have ANY active anchor row in verse_context?
terms_with_existing_anchor = set()
for mti in terms:
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_context "
        "WHERE mti_term_id=? AND is_anchor=1 AND COALESCE(delete_flagged,0)=0",
        (mti,)
    ).fetchone()[0]
    if n > 0:
        terms_with_existing_anchor.add(mti)

print(f"Terms in patch: {len(terms)}")
print(f"Terms with existing anchor: {len(terms_with_existing_anchor)} "
      f"({sorted(terms_with_existing_anchor)})")
print(f"Terms needing first-relevant-as-anchor: "
      f"{sorted(set(terms) - terms_with_existing_anchor)}")

# For each term needing anchor: find the FIRST relevant insert op and set is_anchor=1
promoted = 0
for mti in terms:
    if mti in terms_with_existing_anchor:
        continue
    for op in ops:
        if (op["record"]["mti_term_id"] == mti
                and op["record"].get("is_relevant") == 1):
            op["record"]["is_anchor"] = 1
            promoted += 1
            print(f"  promoted to anchor: mti={mti} vr={op['record']['verse_record_id']}")
            break

print(f"\nPromoted: {promoted}")
PATCH.write_text(json.dumps(p, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Patch updated: {PATCH}")
