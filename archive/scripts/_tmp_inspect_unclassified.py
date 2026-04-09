"""Inspect remaining unclassified dimension index groups."""
import sqlite3
import os
from collections import Counter

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

uncl = conn.execute("""
    SELECT di.id, di.group_code, di.strongs_number, di.transliteration, di.gloss,
        di.owning_registry_no as reg, di.owning_registry_word as word,
        di.cluster_assignment, di.context_description,
        di.anchor_count, di.related_count, di.total_verse_count,
        (SELECT rf.root_code FROM wa_term_root_family rf
         JOIN wa_term_inventory ti ON ti.id=rf.term_inv_id AND ti.delete_flagged=0
         WHERE ti.strongs_number=di.strongs_number LIMIT 1) as root_code
    FROM wa_dimension_index di
    WHERE di.dimension IS NULL AND di.delete_flagged=0
    ORDER BY di.total_verse_count DESC
""").fetchall()

no_root = [u for u in uncl if not u["root_code"]]
has_root = [u for u in uncl if u["root_code"]]

print(f"Remaining unclassified: {len(uncl)}")
print(f"  No root link: {len(no_root)}")
print(f"  Has root (ambiguous): {len(has_root)}")

# Verse count distribution
print(f"\n=== Verse count distribution ===")
for label, items in [("No root", no_root), ("Has root (ambiguous)", has_root)]:
    tiny = sum(1 for u in items if u["total_verse_count"] <= 2)
    small = sum(1 for u in items if 3 <= u["total_verse_count"] <= 5)
    medium = sum(1 for u in items if 6 <= u["total_verse_count"] <= 20)
    large = sum(1 for u in items if u["total_verse_count"] > 20)
    print(f"  {label}: 1-2v={tiny}, 3-5v={small}, 6-20v={medium}, 20+v={large}")

# No-root full list
print(f"\n{'='*130}")
print(f"NO ROOT LINK — {len(no_root)} groups")
print(f"{'='*130}")
print(f"{'di':>5}  {'group':12s}  {'strongs':10s}  {'gloss':25s}  {'v':>3s}  {'reg':>4s}  {'word':15s}  description")
print("-" * 130)
for u in no_root:
    gloss = (u["gloss"] or "")[:25]
    desc = (u["context_description"] or "")[:50]
    print(f"{u['id']:5d}  {u['group_code']:12s}  {u['strongs_number']:10s}  {gloss:25s}  "
          f"{u['total_verse_count']:3d}  {u['reg']:4d}  {u['word']:15s}  {desc}")

# Ambiguous root — show root and sibling dims
print(f"\n{'='*130}")
print(f"HAS ROOT (AMBIGUOUS) — {len(has_root)} groups")
print(f"{'='*130}")
print(f"{'di':>5}  {'group':12s}  {'strongs':10s}  {'root':12s}  {'v':>3s}  {'reg':>4s}  {'word':15s}  sibling dims")
print("-" * 130)
for u in has_root[:50]:
    dims = conn.execute("""
        SELECT di2.dimension, COUNT(*) as c
        FROM wa_dimension_index di2
        JOIN mti_terms mt2 ON mt2.id = di2.mti_term_id
        JOIN wa_term_inventory ti2 ON ti2.strongs_number = mt2.strongs_number
          AND ti2.term_owner_type = 'OWNER' AND ti2.delete_flagged = 0
        JOIN wa_term_root_family rf2 ON rf2.term_inv_id = ti2.id
        WHERE rf2.root_code = ? AND di2.dimension IS NOT NULL AND di2.delete_flagged = 0
        GROUP BY di2.dimension ORDER BY c DESC LIMIT 3
    """, (u["root_code"],)).fetchall()
    dim_str = ", ".join(f"{d['dimension'][:20]}({d['c']})" for d in dims) if dims else "no siblings"
    print(f"{u['id']:5d}  {u['group_code']:12s}  {u['strongs_number']:10s}  {u['root_code']:12s}  "
          f"{u['total_verse_count']:3d}  {u['reg']:4d}  {u['word']:15s}  {dim_str}")

if len(has_root) > 50:
    print(f"  ... +{len(has_root)-50} more")

conn.close()
