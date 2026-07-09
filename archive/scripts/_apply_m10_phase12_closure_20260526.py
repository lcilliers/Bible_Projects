"""M10 Phase 12 closure + char_structure flag.

Per v2_8 §15 + researcher direction 2026-05-26:
  - Status: 'Analysis - In Progress' → 'Analysis Completed'
  - char_structure flag: NULL → 'aspect_based' (M10 has 22 'characteristics'
    that are aspects of one master characteristic — sin. Cross-cluster
    char-comparison analytics should filter these out.)

M10's Phase 9 work followed a non-standard tier-batched synthesis path. Per
the researcher: "the segmentation was abandoned, and the attempt to roll up
the analytics into these segments were abandoned." M10 is closed AS-IS, with
the flag set so downstream tools handle it correctly.

§15.2 closure pre-flight notes for M10:
  - Evidence-grounding: PASS for char-scope (4,158 rows, 91.9% E)
  - Completeness: char-scope complete (4,158 rows = 22×189); cluster-scope NOT
    in cluster_finding (M10 used tier-batched path; content is in
    cluster_observation TIER_READING_GUIDE 27 + CLUSTER_SYNTHESIS 23 + 22
    SELF_CHECK_OBSERVATION instead)
  - The char_structure='aspect_based' flag documents that the standard
    "189 cluster-scope rows" expectation does not apply.
"""
import sqlite3
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
conn = sqlite3.connect('database/bible_research.db')
cur = conn.cursor()

current = cur.execute(
    "SELECT status, version, char_structure FROM cluster WHERE cluster_code='M10'"
).fetchone()
print(f"M10 pre: status={current[0]!r} version={current[1]!r} char_structure={current[2]!r}")
assert current[0] == 'Analysis - In Progress', f"Expected 'Analysis - In Progress', got {current[0]!r}"

cur.execute('BEGIN')
try:
    cur.execute(
        "UPDATE cluster SET status='Analysis Completed', "
        "char_structure='aspect_based', last_updated_date=? "
        "WHERE cluster_code='M10' AND status='Analysis - In Progress'",
        (NOW,),
    )
    assert cur.rowcount == 1
    conn.commit()
    print(f"Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

post = cur.execute(
    "SELECT status, char_structure, last_updated_date FROM cluster WHERE cluster_code='M10'"
).fetchone()
print(f"M10 post: status={post[0]!r} char_structure={post[1]!r} last_updated={post[2]!r}")
assert post[0] == 'Analysis Completed'
assert post[1] == 'aspect_based'

print()
print("=== M10 PHASE 12 CLOSURE COMPLETE ===")
print("Cluster status: Analysis Completed")
print("char_structure: aspect_based — exclude from cross-cluster char-comparison analytics")
print("Ready for Session C cluster publication.")
conn.close()
