"""Root + Verse Context Group analysis."""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

# How many roots link to VC groups?
linked = conn.execute("""
    SELECT COUNT(DISTINCT rf.root_code) FROM wa_term_root_family rf
    JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged=0
    JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
      AND mt.status IN ('extracted','extracted_thin') AND mt.delete_flagged=0
    JOIN verse_context_group vcg ON vcg.mti_term_id = mt.id AND vcg.delete_flagged=0
""").fetchone()[0]
total_roots = conn.execute("SELECT COUNT(DISTINCT root_code) FROM wa_term_root_family").fetchone()[0]
print(f"Roots linked to VC groups: {linked}/{total_roots}")

# Sample: AGAP
print()
print("=== Sample: AGAP root (love family) — terms + groups ===")
print()
rows = conn.execute("""
    SELECT rf.root_code, ti.strongs_number, ti.transliteration,
        COALESCE(ti.step_search_gloss, ti.word_analysis_gloss, '') as gloss,
        wr.no as reg, wr.word,
        vcg.group_code, vcg.context_description,
        di.dimension, di.dominant_subject
    FROM wa_term_root_family rf
    JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged=0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
      AND mt.status IN ('extracted','extracted_thin') AND mt.delete_flagged=0
    LEFT JOIN verse_context_group vcg ON vcg.mti_term_id = mt.id AND vcg.delete_flagged=0
    LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id AND di.delete_flagged=0
    WHERE rf.root_code = 'AGAP'
    ORDER BY wr.no, ti.strongs_number, vcg.group_code
""").fetchall()

current_term = None
for r in rows:
    term_key = r["strongs_number"] + "|" + str(r["reg"])
    if term_key != current_term:
        current_term = term_key
        print(f"  {r['strongs_number']:10s} {r['transliteration']:15s} \"{r['gloss']}\" -> reg {r['reg']}({r['word']})")
    if r["group_code"]:
        ds = f" [{r['dominant_subject']}]" if r["dominant_subject"] else ""
        dim = r["dimension"] or "unclassified"
        desc = (r["context_description"] or "")[:70]
        print(f"    {r['group_code']:12s} {dim:30s}{ds}  {desc}")

# Top multi-group roots
print()
print("=== Root -> Dimension profile (top 15 multi-group roots) ===")
print()
root_dims = conn.execute("""
    SELECT rf.root_code, rf.root_gloss, rf.root_language,
        COUNT(DISTINCT vcg.id) as group_count,
        COUNT(DISTINCT wr.no) as reg_count,
        COUNT(DISTINCT di.dimension) as dim_count,
        GROUP_CONCAT(DISTINCT di.dimension) as dimensions,
        GROUP_CONCAT(DISTINCT wr.word) as words
    FROM wa_term_root_family rf
    JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged=0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
      AND mt.status IN ('extracted','extracted_thin') AND mt.delete_flagged=0
    JOIN verse_context_group vcg ON vcg.mti_term_id = mt.id AND vcg.delete_flagged=0
    LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id AND di.delete_flagged=0
    GROUP BY rf.root_code
    HAVING group_count >= 5
    ORDER BY group_count DESC
    LIMIT 15
""").fetchall()

print(f"{'Root':15s}  {'Grps':>4s}  {'Regs':>4s}  {'Dims':>4s}  Words -> Dimensions")
print("-" * 100)
for r in root_dims:
    words = (r["words"] or "")[:30]
    dims = (r["dimensions"] or "")[:50]
    print(f"{r['root_code']:15s}  {r['group_count']:4d}  {r['reg_count']:4d}  {r['dim_count']:4d}  {words:30s} -> {dims}")

# Cross-dimensional roots (4+ dimensions)
print()
print("=== Roots spanning 4+ dimensions (cross-dimensional roots) ===")
print()
cross = conn.execute("""
    SELECT rf.root_code, rf.root_language,
        COUNT(DISTINCT vcg.id) as group_count,
        COUNT(DISTINCT wr.no) as reg_count,
        COUNT(DISTINCT di.dimension) as dim_count,
        GROUP_CONCAT(DISTINCT di.dimension) as dimensions,
        GROUP_CONCAT(DISTINCT wr.word) as words
    FROM wa_term_root_family rf
    JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged=0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
      AND mt.status IN ('extracted','extracted_thin') AND mt.delete_flagged=0
    JOIN verse_context_group vcg ON vcg.mti_term_id = mt.id AND vcg.delete_flagged=0
    LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id AND di.delete_flagged=0
    GROUP BY rf.root_code
    HAVING dim_count >= 4
    ORDER BY dim_count DESC, group_count DESC
""").fetchall()

print(f"{'Root':15s}  {'Lang':8s}  {'Grps':>4s}  {'Regs':>4s}  {'Dims':>4s}  Words")
print("-" * 90)
for r in cross:
    words = (r["words"] or "")[:50]
    dims = r["dimensions"] or ""
    print(f"{r['root_code']:15s}  {r['root_language'] or '?':8s}  {r['group_count']:4d}  {r['reg_count']:4d}  {r['dim_count']:4d}  {words}")
    print(f"  Dimensions: {dims}")
    print()

conn.close()
