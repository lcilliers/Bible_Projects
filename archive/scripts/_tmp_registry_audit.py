"""Registry-level status audit."""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

print("=" * 140)
print("REGISTRY-LEVEL STATUS AUDIT")
print("=" * 140)

regs = conn.execute("""
    SELECT wr.no, wr.word, wr.phase1_status, wr.session_b_status, wr.verse_context_status,
           wr.cluster_assignment, wr.phase1_term_count, wr.phase1_verse_count
    FROM word_registry wr ORDER BY wr.no
""").fetchall()

header = (f"{'No':>4}  {'Word':20s}  {'Cluster':7s}  {'Phase1':8s}  {'SB Status':22s}  "
          f"{'VC':10s}  {'Grps':>4s}  {'Rel':>5s}  {'SA':>5s}  "
          f"{'DimAI':>5s}  {'Anch':>5s}  {'DS':>3s}  Outstanding")
print(header)
print("-" * 140)

issues = {"dim_incomplete": [], "dim_no_ds": [], "xref_only": []}

for r in regs:
    reg_id = r["no"]
    wr_id = conn.execute("SELECT id FROM word_registry WHERE no=?", (reg_id,)).fetchone()[0]

    grps = conn.execute("""SELECT COUNT(DISTINCT vcg.id) FROM verse_context_group vcg
        JOIN mti_terms mt ON mt.id=vcg.mti_term_id
        JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
          AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
        JOIN wa_file_index fi ON fi.id=ti.file_id
        WHERE fi.word_registry_fk=? AND vcg.delete_flagged=0""", (wr_id,)).fetchone()[0]

    rel = conn.execute("""SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
          AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
        JOIN wa_file_index fi ON fi.id=ti.file_id
        WHERE fi.word_registry_fk=? AND vc.is_relevant=1 AND vc.delete_flagged=0""", (wr_id,)).fetchone()[0]

    sa = conn.execute("""SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
          AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
        JOIN wa_file_index fi ON fi.id=ti.file_id
        WHERE fi.word_registry_fk=? AND vc.is_relevant=0 AND vc.delete_flagged=0""", (wr_id,)).fetchone()[0]

    dim_ai = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE owning_registry_no=? AND dimension_confidence='CLAUDE_AI' AND delete_flagged=0", (reg_id,)).fetchone()[0]
    dim_anc = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE owning_registry_no=? AND manual_override=1 AND delete_flagged=0", (reg_id,)).fetchone()[0]
    dim_total = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE owning_registry_no=? AND delete_flagged=0", (reg_id,)).fetchone()[0]
    ds_set = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE owning_registry_no=? AND dominant_subject IS NOT NULL AND delete_flagged=0", (reg_id,)).fetchone()[0]

    outstanding = []
    if r["phase1_status"] == "Excluded":
        outstanding.append("EXCLUDED")
    else:
        if r["verse_context_status"] != "Complete":
            outstanding.append(f"VC={r['verse_context_status']}")

        if grps == 0:
            owner_count = conn.execute("""SELECT COUNT(*) FROM wa_term_inventory ti
                JOIN wa_file_index fi ON fi.id=ti.file_id
                WHERE fi.word_registry_fk=? AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0""", (wr_id,)).fetchone()[0]
            if owner_count == 0:
                outstanding.append("XREF-only")
                issues["xref_only"].append(reg_id)

        if dim_total > 0 and dim_ai < dim_total:
            outstanding.append(f"DIM({dim_ai}/{dim_total})")
            issues["dim_incomplete"].append(reg_id)
        elif dim_total == 0 and grps > 0:
            outstanding.append("NO-DIM-INDEX")
            issues["dim_incomplete"].append(reg_id)

        if dim_total > 0 and ds_set < dim_total:
            issues["dim_no_ds"].append(reg_id)

    outstanding_str = ", ".join(outstanding) if outstanding else "OK"

    print(f"{reg_id:4d}  {r['word']:20s}  {r['cluster_assignment'] or '':7s}  "
          f"{r['phase1_status'] or '':8s}  {r['session_b_status'] or 'NULL':22s}  "
          f"{r['verse_context_status'] or 'NULL':10s}  {grps:4d}  {rel:5d}  {sa:5d}  "
          f"{dim_ai:5d}  {dim_anc:5d}  {ds_set:3d}  {outstanding_str}")

# Summary
print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)

total_active = sum(1 for r in regs if r["phase1_status"] != "Excluded")
vc_complete = sum(1 for r in regs if r["verse_context_status"] == "Complete")
excluded = sum(1 for r in regs if r["phase1_status"] == "Excluded")

print(f"Total registries: {len(regs)} ({total_active} active, {excluded} excluded)")
print(f"VC Complete: {vc_complete}")
print()

# Dimension review by cluster
print("Dimension Review by Cluster:")
clusters = conn.execute("""
    SELECT cluster_assignment,
        COUNT(*) as total,
        SUM(CASE WHEN dimension_confidence='CLAUDE_AI' THEN 1 ELSE 0 END) as ai,
        SUM(CASE WHEN manual_override=1 THEN 1 ELSE 0 END) as anchored,
        SUM(CASE WHEN dominant_subject IS NOT NULL THEN 1 ELSE 0 END) as ds
    FROM wa_dimension_index WHERE delete_flagged=0
    GROUP BY cluster_assignment ORDER BY cluster_assignment
""").fetchall()

print(f"  {'Cluster':8s}  {'Total':>5s}  {'AI':>5s}  {'Anch':>5s}  {'DS':>5s}  Status")
for c in clusters:
    status = "COMPLETE" if c["ai"] == c["total"] else f"PARTIAL({c['ai']}/{c['total']})"
    ds_gap = c["total"] - c["ds"]
    ds_note = f"  DS-gap({ds_gap})" if ds_gap > 0 else ""
    print(f"  {c['cluster_assignment']:8s}  {c['total']:5d}  {c['ai']:5d}  {c['anchored']:5d}  {c['ds']:5d}  {status}{ds_note}")

# Outstanding
print()
print("Outstanding Issues:")

dim_incomplete = list(set(issues["dim_incomplete"]))
dim_no_ds = list(set(issues["dim_no_ds"]))
xref_only = list(set(issues["xref_only"]))

if dim_incomplete:
    print(f"  Dimension review incomplete: {len(dim_incomplete)} registries")
    # Group by cluster
    from collections import Counter
    cl_counts = Counter()
    for rid in dim_incomplete:
        cl = conn.execute("SELECT cluster_assignment FROM word_registry WHERE no=?", (rid,)).fetchone()[0]
        cl_counts[cl] += 1
    for cl, cnt in cl_counts.most_common():
        print(f"    {cl}: {cnt} registries")

if dim_no_ds:
    print(f"  dominant_subject missing: {len(dim_no_ds)} registries (pre-C16 — not yet assigned)")

if xref_only:
    print(f"  XREF-only registries (0 groups, 0 OWNER terms): {len(xref_only)}")

# C21/C22
print()
print("Remaining dimension clusters (not yet reviewed):")
for cl in ["C21", "C22"]:
    r = conn.execute("""SELECT COUNT(*) as total,
        SUM(CASE WHEN dimension_confidence='CLAUDE_AI' THEN 1 ELSE 0 END) as ai
        FROM wa_dimension_index WHERE cluster_assignment=? AND delete_flagged=0""", (cl,)).fetchone()
    regs_cl = conn.execute("""SELECT no, word FROM word_registry
        WHERE cluster_assignment=? AND phase1_status != 'Excluded' ORDER BY no""", (cl,)).fetchall()
    words = ", ".join(f"{r2['no']}({r2['word']})" for r2 in regs_cl)
    print(f"  {cl}: {r['total']} groups, {r['ai']} AI — {words}")

# New registries needing dimension index
print()
new_regs = conn.execute("""
    SELECT wr.no, wr.word, wr.cluster_assignment FROM word_registry wr
    WHERE wr.verse_context_status = 'Complete' AND wr.phase1_status != 'Excluded'
    AND wr.no NOT IN (SELECT DISTINCT owning_registry_no FROM wa_dimension_index WHERE delete_flagged=0)
    AND wr.no IN (
        SELECT DISTINCT fi2.word_registry_fk FROM wa_file_index fi2
        JOIN wa_term_inventory ti2 ON ti2.file_id=fi2.id AND ti2.term_owner_type='OWNER' AND ti2.delete_flagged=0
    )
    ORDER BY wr.no
""").fetchall()
if new_regs:
    print(f"Registries needing dimension index population: {len(new_regs)}")
    for nr in new_regs:
        print(f"  {nr['no']}({nr['word']}) cluster={nr['cluster_assignment']}")

conn.close()
