import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

print("=" * 70)
print("OQ-001 — H2868 te.ev (mti_id=633)")
print("=" * 70)

# Identify the term
r = c.execute("""
    SELECT id, strongs_number, transliteration, gloss, language,
           status, vc_status, delete_flagged, cluster_code
    FROM mti_terms
    WHERE id = 633
""").fetchone()
if r:
    print(f"mti_terms row 633: {dict(r)}")
else:
    print("MISSING — no mti_terms row id=633")
print()

# Also confirm by strongs
r2 = c.execute("""
    SELECT id, strongs_number, transliteration, gloss, status, vc_status, cluster_code, delete_flagged
    FROM mti_terms WHERE strongs_number='H2868'
""").fetchall()
print(f"mti_terms WHERE strongs_number='H2868': {len(r2)} row(s)")
for r in r2:
    print(f"  {dict(r)}")
print()

# Verse record count (all rows + active rows)
total = c.execute("SELECT COUNT(*) c FROM wa_verse_records WHERE mti_term_id=633").fetchone()['c']
active = c.execute("SELECT COUNT(*) c FROM wa_verse_records WHERE mti_term_id=633 AND COALESCE(delete_flagged,0)=0").fetchone()['c']
print(f"wa_verse_records for mti_term_id=633: total={total}, active (delete_flagged=0)={active}")
print()

# UT count = active verse_records with NO verse_context row (for this mti_term_id)
ut = c.execute("""
    SELECT COUNT(*) c
    FROM wa_verse_records vr
    LEFT JOIN verse_context vc
      ON vc.verse_record_id = vr.id AND vc.mti_term_id = vr.mti_term_id
    WHERE vr.mti_term_id = 633
      AND COALESCE(vr.delete_flagged,0) = 0
      AND vc.id IS NULL
""").fetchone()['c']
print(f"UT verses for mti_term_id=633: {ut}")
print()

# Distribution of vc_status for this term's verse records
print("verse_context distribution for mti_term_id=633:")
for row in c.execute("""
    SELECT
      CASE WHEN vc.id IS NULL THEN 'UT (no vc row)'
           WHEN vc.is_relevant = 1 THEN 'relevant'
           WHEN vc.set_aside_reason IS NOT NULL THEN 'set_aside'
           WHEN vc.is_relevant = 0 AND vc.set_aside_reason IS NULL THEN 'is_relevant=0, no reason'
           ELSE 'other' END AS state,
      COUNT(*) c
    FROM wa_verse_records vr
    LEFT JOIN verse_context vc
      ON vc.verse_record_id = vr.id AND vc.mti_term_id = vr.mti_term_id
    WHERE vr.mti_term_id = 633 AND COALESCE(vr.delete_flagged,0)=0
    GROUP BY 1
"""):
    print(f"  {row['state']:<28} {row['c']}")
print()

if active > 0 and ut > 0:
    print("Sample UT verses for mti_term_id=633 (up to 10):")
    for row in c.execute("""
        SELECT vr.id, vr.reference, vr.target_word, vr.span_strong_match
        FROM wa_verse_records vr
        LEFT JOIN verse_context vc
          ON vc.verse_record_id = vr.id AND vc.mti_term_id = vr.mti_term_id
        WHERE vr.mti_term_id=633 AND COALESCE(vr.delete_flagged,0)=0 AND vc.id IS NULL
        LIMIT 10
    """):
        print(f"  vr_id={row['id']} ref={row['reference']} target={row['target_word']} span_match={row['span_strong_match']}")

print()
print("=" * 70)
print("OQ-002 — G5483 charizō UT count (pre-check said 5, AI saw 4)")
print("=" * 70)

# Find the G5483 mti_term
r5483 = c.execute("""
    SELECT id, strongs_number, transliteration, gloss, status, vc_status, cluster_code, delete_flagged
    FROM mti_terms WHERE strongs_number='G5483'
""").fetchall()
print(f"mti_terms WHERE strongs_number='G5483': {len(r5483)} row(s)")
for r in r5483:
    print(f"  {dict(r)}")
print()

if r5483:
    mti_id = r5483[0]['id']
    total = c.execute(f"SELECT COUNT(*) c FROM wa_verse_records WHERE mti_term_id={mti_id}").fetchone()['c']
    active = c.execute(f"SELECT COUNT(*) c FROM wa_verse_records WHERE mti_term_id={mti_id} AND COALESCE(delete_flagged,0)=0").fetchone()['c']
    print(f"wa_verse_records for mti_term_id={mti_id} (G5483 charizō): total={total}, active={active}")
    print()

    ut = c.execute(f"""
        SELECT COUNT(*) c
        FROM wa_verse_records vr
        LEFT JOIN verse_context vc
          ON vc.verse_record_id = vr.id AND vc.mti_term_id = vr.mti_term_id
        WHERE vr.mti_term_id = {mti_id}
          AND COALESCE(vr.delete_flagged,0) = 0
          AND vc.id IS NULL
    """).fetchone()['c']
    print(f"UT verses for mti_term_id={mti_id}: {ut}")
    print()

    print("verse_context distribution:")
    for row in c.execute(f"""
        SELECT
          CASE WHEN vc.id IS NULL THEN 'UT (no vc row)'
               WHEN vc.is_relevant = 1 THEN 'relevant'
               WHEN vc.set_aside_reason IS NOT NULL THEN 'set_aside'
               WHEN vc.is_relevant = 0 AND vc.set_aside_reason IS NULL THEN 'is_relevant=0, no reason'
               ELSE 'other' END AS state,
          COUNT(*) c
        FROM wa_verse_records vr
        LEFT JOIN verse_context vc
          ON vc.verse_record_id = vr.id AND vc.mti_term_id = vr.mti_term_id
        WHERE vr.mti_term_id = {mti_id} AND COALESCE(vr.delete_flagged,0)=0
        GROUP BY 1
    """):
        print(f"  {row['state']:<28} {row['c']}")
    print()

    print(f"All UT verses for mti_term_id={mti_id} (G5483 charizō):")
    for row in c.execute(f"""
        SELECT vr.id, vr.reference, vr.target_word, vr.span_strong_match
        FROM wa_verse_records vr
        LEFT JOIN verse_context vc
          ON vc.verse_record_id = vr.id AND vc.mti_term_id = vr.mti_term_id
        WHERE vr.mti_term_id={mti_id} AND COALESCE(vr.delete_flagged,0)=0 AND vc.id IS NULL
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """):
        print(f"  vr_id={row['id']} ref={row['reference']} target={row['target_word']} span_match={row['span_strong_match']}")
