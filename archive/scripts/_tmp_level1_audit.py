"""Level 1 Audit v2: Verse Context Integrity — per updated CC directive."""
import sqlite3
import os
import sys
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

print("=" * 60)
print("LEVEL 1 AUDIT v2: Verse Context Integrity")
print("=" * 60)

blocked = False

# ── L1-A1: Contamination check (corrected — mti_terms only) ──
rows = conn.execute("""
SELECT vc.id, vc.mti_term_id, mt.strongs_number, mt.status AS mti_status,
       mt.delete_flagged AS mti_deleted,
       wr.no AS registry_no, wr.word AS registry_word
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
WHERE vc.delete_flagged = 0
AND (
    mt.status NOT IN ('extracted', 'extracted_thin',
                      'extracted_theological_anchor', 'phase2_enrichment')
    OR mt.delete_flagged = 1
)
LIMIT 50
""").fetchall()
c = len(rows)
print(f"\nL1-A1: {c} rows — {'CLEAR' if c == 0 else 'ISSUE: contamination found'}")
if c > 0:
    for r in rows[:10]:
        print(f"  vc={r['id']} mti={r['mti_term_id']} {r['strongs_number']} "
              f"status={r['mti_status']} del={r['mti_deleted']} "
              f"reg={r['registry_no']}({r['registry_word']})")
    blocked = True
if blocked:
    print("\nBLOCKED at L1-A1")
    conn.close(); sys.exit(0)

# ── L1-A2: Groups with zero anchors ──
rows = conn.execute("""
SELECT vcg.id, vcg.group_code, vcg.context_description,
       COUNT(vc.id) AS total_vc_records,
       SUM(CASE WHEN vc.is_anchor = 1 THEN 1 ELSE 0 END) AS anchor_count
FROM verse_context_group vcg
LEFT JOIN verse_context vc ON vc.group_id = vcg.id AND vc.delete_flagged = 0
WHERE vcg.delete_flagged = 0
GROUP BY vcg.id
HAVING anchor_count = 0
""").fetchall()
c = len(rows)
print(f"L1-A2: {c} rows — {'CLEAR' if c == 0 else 'ISSUE: groups with zero anchors'}")
if c > 0:
    for r in rows:
        print(f"  vcg={r['id']} {r['group_code']} vc={r['total_vc_records']} "
              f"desc={r['context_description'][:60]}")

# ── L1-A3: Anchor flag consistency ──
rows = conn.execute("""
SELECT vc.id, vc.mti_term_id, vc.group_id, vc.verse_record_id,
       vc.is_anchor, vc.is_relevant, vc.is_related, vcg.group_code
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.delete_flagged = 0
AND vc.is_anchor = 1 AND vc.is_relevant = 0
""").fetchall()
c = len(rows)
print(f"L1-A3: {c} rows — {'CLEAR' if c == 0 else 'ISSUE'}")

# ── L1-A4: Orphaned verse_context (relevant only) ──
rows = conn.execute("""
SELECT vc.id, vc.mti_term_id, vc.group_id, vc.verse_record_id, vc.is_relevant
FROM verse_context vc
WHERE vc.delete_flagged = 0
AND vc.is_relevant = 1
AND (
    vc.group_id IS NULL
    OR NOT EXISTS (
        SELECT 1 FROM verse_context_group vcg
        WHERE vcg.id = vc.group_id AND vcg.delete_flagged = 0
    )
)
""").fetchall()
c = len(rows)
print(f"L1-A4: {c} rows — {'CLEAR' if c == 0 else 'ISSUE: orphaned relevant records'}")
if c > 0:
    for r in rows[:10]:
        print(f"  vc={r['id']} mti={r['mti_term_id']} group_id={r['group_id']}")

# ── L1-A5: Groups with no verse_context records ──
rows = conn.execute("""
SELECT vcg.id, vcg.group_code, vcg.context_description,
       mt.strongs_number, mt.transliteration,
       wr.no AS registry_no, wr.word AS registry_word
FROM verse_context_group vcg
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE vcg.delete_flagged = 0
AND NOT EXISTS (
    SELECT 1 FROM verse_context vc
    WHERE vc.group_id = vcg.id AND vc.delete_flagged = 0
)
""").fetchall()
c = len(rows)
print(f"L1-A5: {c} rows — {'CLEAR' if c == 0 else 'ISSUE: empty groups'}")
if c > 0:
    for r in rows:
        print(f"  vcg={r['id']} {r['group_code']} {r['strongs_number']} "
              f"reg={r['registry_no']}({r['registry_word']})")

# ── L1-INV1: Empty group detail (789 and 2130) ──
print(f"\nL1-INV1: Empty group detail")
for vcg_id in [789, 2130]:
    r = conn.execute("""
    SELECT vcg.id, vcg.group_code, vcg.context_description,
           vcg.notes, vcg.delete_flagged,
           mt.strongs_number, mt.transliteration, mt.status AS mti_status,
           mt.delete_flagged AS mti_deleted,
           wr.no AS registry_no, wr.word AS registry_word,
           wr.verse_context_status,
           (SELECT COUNT(*) FROM verse_context vc2
            WHERE vc2.group_id = vcg.id) AS total_vc_including_deleted,
           (SELECT COUNT(*) FROM verse_context vc2
            WHERE vc2.group_id = vcg.id AND vc2.delete_flagged = 0) AS active_vc_count,
           (SELECT COUNT(*) FROM verse_context vc2
            WHERE vc2.group_id = vcg.id AND vc2.delete_flagged = 1) AS deleted_vc_count
    FROM verse_context_group vcg
    JOIN mti_terms mt ON mt.id = vcg.mti_term_id
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
        AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    WHERE vcg.id = ?
    """, (vcg_id,)).fetchone()
    if r:
        print(f"  vcg={r['id']} {r['group_code']}")
        print(f"    desc: {r['context_description'][:80]}")
        print(f"    notes: {r['notes']}")
        print(f"    {r['strongs_number']} ({r['transliteration']}) mti_status={r['mti_status']} mti_del={r['mti_deleted']}")
        print(f"    reg={r['registry_no']}({r['registry_word']}) vc_status={r['verse_context_status']}")
        print(f"    vc total(incl deleted)={r['total_vc_including_deleted']} active={r['active_vc_count']} deleted={r['deleted_vc_count']}")

print("\nTier A complete — proceeding to Tier B")

# ── L1-B1: Terms with verses but no verse_context ──
print()
rows = conn.execute("""
SELECT wr.no AS registry_no, wr.word AS registry_word,
       mt.strongs_number, mt.transliteration, mt.status AS mti_status,
       COUNT(DISTINCT vr.id) AS active_verse_count
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
    AND wr.verse_context_status = 'Complete'
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE mt.status IN ('extracted', 'extracted_thin')
    AND mt.delete_flagged = 0
    AND NOT EXISTS (
        SELECT 1 FROM verse_context vc
        WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
    )
GROUP BY wr.no, wr.word, mt.strongs_number, mt.transliteration, mt.status
ORDER BY wr.no, active_verse_count DESC
""").fetchall()
c = len(rows)
print(f"L1-B1: {c} rows — {'CLEAR' if c == 0 else 'ISSUE'}")
if c > 0:
    for r in rows:
        print(f"  reg={r['registry_no']}({r['registry_word']}) {r['strongs_number']} "
              f"{r['transliteration']} status={r['mti_status']} verses={r['active_verse_count']}")

# ── L1-B2: Terms classified but not grouped (relevant only) ──
print()
rows = conn.execute("""
SELECT mt.strongs_number, mt.transliteration,
       wr.no AS registry_no, wr.word AS registry_word,
       COUNT(vc.id) AS vc_records,
       SUM(CASE WHEN vc.is_relevant = 1 THEN 1 ELSE 0 END) AS relevant_records,
       COUNT(DISTINCT vc.group_id) AS group_count
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE vc.delete_flagged = 0
    AND mt.status IN ('extracted', 'extracted_thin')
    AND mt.delete_flagged = 0
GROUP BY mt.strongs_number, mt.transliteration, wr.no, wr.word
HAVING relevant_records > 0 AND group_count = 0
""").fetchall()
c = len(rows)
print(f"L1-B2: {c} rows — {'CLEAR' if c == 0 else 'ISSUE'}")
if c > 0:
    for r in rows:
        print(f"  {r['strongs_number']} {r['transliteration']} "
              f"reg={r['registry_no']}({r['registry_word']}) "
              f"vc={r['vc_records']} relevant={r['relevant_records']}")

# ── L1-B3: Summary coverage (corrected — no group join) ──
print()
stats = conn.execute("""
SELECT
    COUNT(DISTINCT CASE WHEN vc.is_relevant = 1 AND vc.delete_flagged = 0 THEN vc.id END) AS total_relevant,
    COUNT(DISTINCT CASE WHEN vc.is_anchor = 1 AND vc.delete_flagged = 0 THEN vc.id END) AS total_anchors,
    COUNT(DISTINCT CASE WHEN vc.is_relevant = 0 AND vc.delete_flagged = 0 THEN vc.id END) AS total_set_aside,
    COUNT(DISTINCT CASE WHEN vc.delete_flagged = 0 THEN vc.id END) AS total_active_vc_records,
    (SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged = 0) AS total_active_groups,
    COUNT(DISTINCT CASE WHEN mt.status = 'extracted' AND mt.delete_flagged = 0 THEN mt.id END) AS extracted_terms_with_vc,
    COUNT(DISTINCT CASE WHEN mt.status = 'extracted_thin' AND mt.delete_flagged = 0 THEN mt.id END) AS extracted_thin_terms_with_vc
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
""").fetchone()
print("L1-B3: Summary coverage")
print(f"  total_relevant:              {stats['total_relevant']:,}")
print(f"  total_anchors:               {stats['total_anchors']:,}")
print(f"  total_set_aside:             {stats['total_set_aside']:,}")
print(f"  total_active_vc_records:     {stats['total_active_vc_records']:,}")
print(f"  total_active_groups:         {stats['total_active_groups']:,}")
print(f"  extracted_terms_with_vc:     {stats['extracted_terms_with_vc']:,}")
print(f"  extracted_thin_terms_with_vc: {stats['extracted_thin_terms_with_vc']:,}")
print(f"  relevant + set_aside check:  {stats['total_relevant'] + stats['total_set_aside']:,} "
      f"(should = {stats['total_active_vc_records']:,})")

conn.close()
