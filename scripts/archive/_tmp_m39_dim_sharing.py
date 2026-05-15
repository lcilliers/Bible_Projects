"""Dimensional sharing analysis for M39-A and M39-B.

Schema reality:
- wa_dimension_index keys on verse_context_group_id (persists across C→M cluster pivot).
- wa_dimension_index.cluster_assignment uses OLD C-codes (pre-2026-05-04) — ignore.
- To map a VCG to its CURRENT M-cluster, join via verse_context → mti_terms.cluster_code.
- We want: for each M39 sub-group, count distinct OTHER M-clusters that share ≥1 dimension.
"""
import sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row


def header(s):
    print(f"\n{'=' * 72}\n  {s}\n{'=' * 72}")


# Step 1 — get M39 VCGs and their dimensions, by sub-group
header("M39 VCGs and their dimensions, by sub-group")

m39_dim_rows = list(c.execute("""
    SELECT DISTINCT cs.subgroup_code, vcg.id AS vcg_id, vcg.group_code,
           wdi.dimension, wdi.dimension_confidence
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                              AND COALESCE(mts.delete_flagged,0)=0
    JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
    JOIN verse_context_group vcg ON vcg.id = vc.group_id
    LEFT JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
                                    AND COALESCE(wdi.delete_flagged,0)=0
    WHERE mt.cluster_code='M39'
      AND COALESCE(mt.delete_flagged,0)=0
      AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0
    ORDER BY cs.subgroup_code, vcg.group_code
"""))

m39_dims_by_sg = defaultdict(set)         # sg -> set of dimensions
m39_vcgs_by_sg = defaultdict(set)         # sg -> set of vcg_ids
m39_dim_vcgs_by_sg = defaultdict(set)     # sg -> set of (dim, vcg_id) pairs (for joining)
m39_vcgs_without_dim = defaultdict(set)

for r in m39_dim_rows:
    sg = r['subgroup_code']
    m39_vcgs_by_sg[sg].add(r['vcg_id'])
    if r['dimension']:
        m39_dims_by_sg[sg].add(r['dimension'])
        m39_dim_vcgs_by_sg[sg].add((r['dimension'], r['vcg_id']))
    else:
        m39_vcgs_without_dim[sg].add(r['vcg_id'])

for sg in sorted(m39_vcgs_by_sg):
    print(f"\n  {sg}: {len(m39_vcgs_by_sg[sg])} VCG(s), "
          f"{len(m39_dims_by_sg[sg])} distinct dimension(s) attached, "
          f"{len(m39_vcgs_without_dim[sg])} VCG(s) with no dimension row")
    for d in sorted(m39_dims_by_sg[sg]):
        n_vcgs_in_sg = len([1 for x in m39_dim_vcgs_by_sg[sg] if x[0] == d])
        print(f"    {d!r}  ({n_vcgs_in_sg} M39 VCG(s))")


# Step 2 — find which OTHER M-clusters share each dimension
# For each M39 dimension, find all VCGs carrying that dimension, then map to M-cluster
header("OTHER M-clusters sharing each dimension")

other_cluster_share = {}  # sg -> dict[other_cluster] -> set of shared dimensions

for sg, dims in m39_dims_by_sg.items():
    other_cluster_share[sg] = defaultdict(set)
    for dim in dims:
        # Find all VCGs carrying this dimension
        sharing_vcgs = list(c.execute("""
            SELECT DISTINCT wdi.verse_context_group_id AS vcg_id
            FROM wa_dimension_index wdi
            WHERE wdi.dimension = ?
              AND COALESCE(wdi.delete_flagged,0)=0
        """, (dim,)))
        sharing_vcg_ids = [r['vcg_id'] for r in sharing_vcgs]
        # Map each VCG to current M-cluster(s) via verse_context joins
        if not sharing_vcg_ids:
            continue
        placeholders = ','.join('?' * len(sharing_vcg_ids))
        for r in c.execute(f"""
            SELECT DISTINCT mt.cluster_code, vc.group_id
            FROM verse_context vc
            JOIN mti_terms mt ON mt.id=vc.mti_term_id
            WHERE vc.group_id IN ({placeholders})
              AND mt.cluster_code IS NOT NULL
              AND mt.cluster_code != 'M39'
              AND COALESCE(vc.delete_flagged,0)=0
              AND COALESCE(mt.delete_flagged,0)=0
              AND vc.is_relevant=1
        """, sharing_vcg_ids):
            other_cluster_share[sg][r['cluster_code']].add(dim)

# Step 3 — present results, per sub-group
header("RESULT — OTHER clusters sharing dimensions with M39-A / M39-B")
for sg in sorted(other_cluster_share.keys()):
    if sg == 'M39-BOUNDARY':
        continue
    print(f"\n  --- {sg} ---")
    if not other_cluster_share[sg]:
        print(f"    (no other clusters share any dimension)")
        continue
    ranked = sorted(other_cluster_share[sg].items(),
                    key=lambda kv: (-len(kv[1]), kv[0]))
    print(f"    {'cluster':<8} {'shared_dims':<12} dimensions shared")
    for cluster, dims in ranked[:15]:
        dims_str = '; '.join(sorted(dims))
        print(f"    {cluster:<8} {len(dims):<12} {dims_str}")


# Step 4 — cluster-level (T6.7.3): aggregate across both M39 sub-groups
header("RESULT — CLUSTER-level (T6.7.3): M39 dimensional sharing across all sub-groups")
cluster_level = defaultdict(set)
for sg in m39_dims_by_sg:
    if sg == 'M39-BOUNDARY':
        continue
    for cluster, dims in other_cluster_share[sg].items():
        cluster_level[cluster].update(dims)

m39_all_dims = set()
for sg in m39_dims_by_sg:
    if sg == 'M39-BOUNDARY':
        continue
    m39_all_dims.update(m39_dims_by_sg[sg])
print(f"\n  M39 (A+B) has {len(m39_all_dims)} distinct dimensions attached to its VCGs")
print(f"  M39 dimensions: {sorted(m39_all_dims)}")
print(f"\n  Clusters sharing ≥1 dimension with M39: {len(cluster_level)}")
ranked = sorted(cluster_level.items(), key=lambda kv: (-len(kv[1]), kv[0]))
print(f"\n    {'cluster':<8} {'shared_dims':<12} dimensions shared")
for cluster, dims in ranked:
    dims_str = '; '.join(sorted(dims))
    print(f"    {cluster:<8} {len(dims):<12} {dims_str}")

# Quick caveats / coverage check
header("Coverage caveat")
total_vcgs_in_m39 = sum(len(v) for v in m39_vcgs_by_sg.values())
print(f"  M39 VCGs (across A+B+BOUNDARY): {total_vcgs_in_m39}")
total_with_dim = sum(len(m39_dims_by_sg[sg] and m39_vcgs_by_sg[sg]) for sg in m39_vcgs_by_sg)
m39_vcgs_with_dim = set()
for r in m39_dim_rows:
    if r['dimension']:
        m39_vcgs_with_dim.add(r['vcg_id'])
print(f"  M39 VCGs with at least one dimension row: {len(m39_vcgs_with_dim)}")
print(f"  Coverage: {len(m39_vcgs_with_dim) / total_vcgs_in_m39 * 100:.1f}%")
print()
print("  NOTE: wa_dimension_index was populated under the OLD C-cluster schema")
print("        (pre-2026-05-04 pivot). cluster_assignment uses C01-C22 codes.")
print("        Sharing is computed via verse_context_group_id which persists")
print("        across the cluster-taxonomy migration. Dimensions present on a")
print("        VCG remain analytically meaningful regardless of the M-cluster")
print("        the VCG is now reached through.")
