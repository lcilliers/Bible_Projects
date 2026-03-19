"""
S1-S4 Post-run Assessment Report
Queries the DB for a consolidated view of what was produced across all 167 words.
"""
import sqlite3
import json

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

SPEC = "Session A v9 Automation"

print("=" * 70)
print("S1-S4 BULK GAP FILL — ASSESSMENT REPORT")
print("=" * 70)

# ── 1. Word Registry Status ───────────────────────────────────────────────
print("\n1. WORD REGISTRY STATUS")
for row in conn.execute("""
    SELECT phase1_status, COUNT(*) AS n
    FROM word_registry
    GROUP BY phase1_status ORDER BY n DESC
""").fetchall():
    print(f"   {row['phase1_status']:20} {row['n']:4}")

# ── 2. wa_file_index coverage ─────────────────────────────────────────────
print("\n2. WA_FILE_INDEX COVERAGE")
fi_total = conn.execute(
    "SELECT COUNT(*) AS c FROM wa_file_index WHERE specification = ?", (SPEC,)
).fetchone()['c']
fi_zero_terms = conn.execute("""
    SELECT COUNT(*) AS c FROM wa_file_index fi
    WHERE fi.specification = ?
    AND NOT EXISTS (SELECT 1 FROM wa_term_inventory ti WHERE ti.file_id = fi.id)
""", (SPEC,)).fetchone()['c']
fi_zero_verses = conn.execute("""
    SELECT COUNT(*) AS c FROM wa_file_index fi
    WHERE fi.specification = ?
    AND NOT EXISTS (SELECT 1 FROM wa_verse_records vr
                   JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                   WHERE ti.file_id = fi.id)
""", (SPEC,)).fetchone()['c']
print(f"   Files initialized:    {fi_total}")
print(f"   Files with 0 terms:   {fi_zero_terms}  (abstract concepts / empty strongs_list)")
print(f"   Files with 0 verses:  {fi_zero_verses}")

# ── 3. MTI Terms ──────────────────────────────────────────────────────────
print("\n3. MTI_TERMS")
mt_total = conn.execute("SELECT COUNT(*) AS c FROM mti_terms").fetchone()['c']
mt_heb = conn.execute("SELECT COUNT(*) AS c FROM mti_terms WHERE language = 'Hebrew'").fetchone()['c']
mt_grk = conn.execute("SELECT COUNT(*) AS c FROM mti_terms WHERE language = 'Greek'").fetchone()['c']
mt_ara = conn.execute("SELECT COUNT(*) AS c FROM mti_terms WHERE language = 'Aramaic'").fetchone()['c']
mt_other = mt_total - mt_heb - mt_grk - mt_ara
xref_total = conn.execute("SELECT COUNT(*) AS c FROM mti_term_cross_refs").fetchone()['c']
print(f"   Total mti_terms:      {mt_total}")
print(f"   Hebrew:               {mt_heb}")
print(f"   Greek:                {mt_grk}")
print(f"   Aramaic:              {mt_ara}")
print(f"   Other/unknown:        {mt_other}")
print(f"   XREF cross-refs:      {xref_total}")

# ── 4. Verse Records ──────────────────────────────────────────────────────
print("\n4. VERSE RECORDS (wa_verse_records, spec-scoped)")
vr_total = conn.execute("""
    SELECT COUNT(*) AS c FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.specification = ?
""", (SPEC,)).fetchone()['c']
vr_ot = conn.execute("""
    SELECT COUNT(*) AS c FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.specification = ? AND vr.testament = 'OT'
""", (SPEC,)).fetchone()['c']
vr_nt = conn.execute("""
    SELECT COUNT(*) AS c FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.specification = ? AND vr.testament = 'NT'
""", (SPEC,)).fetchone()['c']
print(f"   Total verse records:  {vr_total}")
print(f"   OT:                   {vr_ot}")
print(f"   NT:                   {vr_nt}")

# Top 10 by verse count
print("\n   Top 10 words by verse count:")
top_verses = conn.execute("""
    SELECT fi.word, COUNT(vr.id) AS n
    FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.specification = ?
    GROUP BY fi.id ORDER BY n DESC LIMIT 10
""", (SPEC,)).fetchall()
for r in top_verses:
    print(f"   {r['word']:25} {r['n']:5} verses")

# ── 5. Audit Results ──────────────────────────────────────────────────────
print("\n5. AUDIT RESULTS (word_run_state)")
try:
    for row in conn.execute("""
        SELECT audit_result, COUNT(*) AS n
        FROM word_run_state
        GROUP BY audit_result ORDER BY n DESC
    """).fetchall():
        print(f"   {row['audit_result']:20} {row['n']:4}")
except Exception as e:
    print(f"   (Error: {e})")

# ── 6. Audit Check Breakdown ──────────────────────────────────────────────
print("\n6. AUDIT CHECK BREAKDOWN (checks that fired FAIL/REVIEW)")
try:
    rows = conn.execute("""
        SELECT audit_detail FROM word_run_state
        WHERE audit_detail IS NOT NULL
    """).fetchall()
    check_counts = {}
    for r in rows:
        checks = json.loads(r['audit_detail'])
        for check_id, data in checks.items():
            result = data.get('r', '')
            if result not in ('PASS', ''):
                key = f"{check_id}:{result}"
                check_counts[key] = check_counts.get(key, 0) + 1
    for k, v in sorted(check_counts.items(), key=lambda x: -x[1]):
        print(f"   {k:30} {v:4} words")
except Exception as e:
    print(f"   (Error: {e})")

# ── 7. Quality Flags ──────────────────────────────────────────────────────
print("\n7. QUALITY FLAGS (wa_quality_flags)")
try:
    for row in conn.execute("""
        SELECT qt.flag_code, COUNT(dq.id) AS n
        FROM wa_data_quality_flags dq
        JOIN wa_quality_flag_types qt ON qt.id = dq.flag_id
        JOIN wa_file_index fi ON fi.id = dq.file_id
        WHERE fi.specification = ?
        GROUP BY qt.flag_code ORDER BY n DESC
    """, (SPEC,)).fetchall():
        print(f"   {row['flag_code']:30} {row['n']:4}")
    total_flags = conn.execute("""
        SELECT COUNT(dq.id) AS c FROM wa_data_quality_flags dq
        JOIN wa_file_index fi ON fi.id = dq.file_id
        WHERE fi.specification = ?
    """, (SPEC,)).fetchone()['c']
    print(f"   {'TOTAL':30} {total_flags:4}")
except Exception as e:
    print(f"   (Error: {e})")

# ── 8. Words with 0 terms (abstract concepts) ────────────────────────────
print("\n8. WORDS WITH 0 TERMS (nothing discoverable in ESV)")
zero_term_words = conn.execute("""
    SELECT fi.word, fi.registry_id
    FROM wa_file_index fi
    WHERE fi.specification = ?
    AND NOT EXISTS (SELECT 1 FROM wa_term_inventory ti WHERE ti.file_id = fi.id)
    ORDER BY CAST(fi.registry_id AS INTEGER)
""", (SPEC,)).fetchall()
for r in zero_term_words:
    print(f"   [{r['registry_id']:3}] {r['word']}")
print(f"   Total: {len(zero_term_words)} words")

# ── 9. Words with terms but 0 verses ─────────────────────────────────────
print("\n9. WORDS WITH TERMS BUT 0 VERSES")
zero_verse_words = conn.execute("""
    SELECT fi.word, fi.registry_id, COUNT(ti.id) AS term_count
    FROM wa_file_index fi
    JOIN wa_term_inventory ti ON ti.file_id = fi.id
    WHERE fi.specification = ?
    AND NOT EXISTS (
        SELECT 1 FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id
    )
    GROUP BY fi.id
    HAVING term_count > 0
    ORDER BY CAST(fi.registry_id AS INTEGER)
""", (SPEC,)).fetchall()
for r in zero_verse_words:
    print(f"   [{r['registry_id']:3}] {r['word']}  ({r['term_count']} terms, 0 verses)")
print(f"   Total: {len(zero_verse_words)} words")

# ── 10. Meanings parsed ───────────────────────────────────────────────────
print("\n10. MEANINGS PARSED (wa_meaning_parsed)")
try:
    mp = conn.execute("""
        SELECT COUNT(DISTINCT file_id) AS files, COUNT(*) AS rows
        FROM wa_meaning_parsed mp
        JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.specification = ?
    """, (SPEC,)).fetchone()
    print(f"   Files with parsed meanings: {mp['files']}")
    print(f"   Total meaning rows:         {mp['rows']}")
except Exception as e:
    print(f"   (Error: {e})")

print("\n" + "=" * 70)
conn.close()
