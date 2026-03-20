"""
_assess_meaning_tables.py
Read-only assessment of meaning-related fields and tables.

Covers:
  A. wa_term_inventory — meaning field population rates
  B. wa_meaning_parsed — coverage, orphans, quality indicators
  C. wa_meaning_sense  — row counts, orphans, zero-sense entries
  D. wa_meaning_stem   — row counts, orphans, Hebrew coverage
  E. wa_lsj_parsed     — Greek-only coverage and orphans
  F. FK alignment      — parsed_meaning_id ↔ wa_meaning_parsed.id
  G. Parse source gaps — meaning present but no parsed row, and vice-versa
"""

import os
import sqlite3

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")

def hr(label=""):
    width = 72
    if label:
        pad_left = (width - len(label) - 2) // 2
        pad_right = width - len(label) - 2 - pad_left
        print(f"\n{'─' * pad_left} {label} {'─' * pad_right}")
    else:
        print("─" * width)

def row_fmt(label, value, indent=2):
    print(f"{'  ' * indent}{label:<45} {value}")

def section(title):
    print(f"\n{'═' * 72}")
    print(f"  {title}")
    print(f"{'═' * 72}")

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
c = conn.cursor()

# ─────────────────────────────────────────────────────────────────────────────
section("A  wa_term_inventory — meaning field coverage")
# ─────────────────────────────────────────────────────────────────────────────

c.execute("SELECT COUNT(*) FROM wa_term_inventory")
total_terms = c.fetchone()[0]
row_fmt("Total wa_term_inventory rows", total_terms, indent=1)

for lang in ("Hebrew", "Greek"):
    c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language=?", (lang,))
    row_fmt(f"  — {lang}", c.fetchone()[0], indent=1)

hr("meaning (primary source text)")
for col in ("meaning", "meaning_numbered", "short_def_mounce", "lsj_entry"):
    c.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE {col} IS NOT NULL AND TRIM({col}) != ''")
    has = c.fetchone()[0]
    c.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE {col} IS NULL OR TRIM({col}) = ''")
    missing = c.fetchone()[0]
    row_fmt(f"{col} — populated", f"{has:>4}  /  {total_terms}  ({100*has//total_terms}%)", indent=1)
    row_fmt(f"{col} — NULL/empty", f"{missing:>4}", indent=1)

hr("meaning by language")
for col in ("meaning", "short_def_mounce", "lsj_entry"):
    for lang in ("Hebrew", "Greek"):
        c.execute(f"""
            SELECT COUNT(*) FROM wa_term_inventory
            WHERE language=? AND {col} IS NOT NULL AND TRIM({col}) != ''
        """, (lang,))
        has = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language=?", (lang,))
        lang_total = c.fetchone()[0]
        pct = (100 * has // lang_total) if lang_total else 0
        row_fmt(f"{col} [{lang}]", f"{has:>4}  /  {lang_total}  ({pct}%)", indent=1)

hr("lsj_entry vs Greek terms (Greek-only field)")
c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE lsj_entry IS NOT NULL AND TRIM(lsj_entry) != '' AND language != 'Greek'")
non_greek_lsj = c.fetchone()[0]
row_fmt("lsj_entry on non-Greek terms (anomaly)", non_greek_lsj, indent=1)

c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language = 'Greek' AND (lsj_entry IS NULL OR TRIM(lsj_entry) = '')")
greek_no_lsj_entry = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language = 'Greek'")
greek_total_a = c.fetchone()[0]
row_fmt("Greek terms missing lsj_entry", f"{greek_no_lsj_entry:>4}  /  {greek_total_a}", indent=1)

hr("parsed_meaning_id FK field")
c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE parsed_meaning_id IS NOT NULL")
has_pmid = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE parsed_meaning_id IS NULL")
null_pmid = c.fetchone()[0]
row_fmt("parsed_meaning_id populated", f"{has_pmid:>4}  /  {total_terms}  ({100*has_pmid//total_terms}%)", indent=1)
row_fmt("parsed_meaning_id NULL", f"{null_pmid:>4}", indent=1)

# broken FK: parsed_meaning_id points to non-existent wa_meaning_parsed.id
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE ti.parsed_meaning_id IS NOT NULL
      AND NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = ti.parsed_meaning_id)
""")
broken_fk = c.fetchone()[0]
row_fmt("parsed_meaning_id → broken FK", f"{broken_fk}", indent=1)

# ─────────────────────────────────────────────────────────────────────────────
section("B  wa_meaning_parsed — coverage and quality")
# ─────────────────────────────────────────────────────────────────────────────

c.execute("SELECT COUNT(*) FROM wa_meaning_parsed")
total_parsed = c.fetchone()[0]
row_fmt("Total wa_meaning_parsed rows", total_parsed, indent=1)

for lang in ("Hebrew", "Greek"):
    c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE language=?", (lang,))
    row_fmt(f"  — {lang}", c.fetchone()[0], indent=1)

hr("coverage vs wa_term_inventory")
# terms WITH a parsed row
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
""")
covered = c.fetchone()[0]
uncovered = total_terms - covered
row_fmt("Terms WITH parsed row", f"{covered:>4}  /  {total_terms}  ({100*covered//total_terms}%)", indent=1)
row_fmt("Terms WITHOUT parsed row", f"{uncovered:>4}", indent=1)

# breakdown of uncovered by language
for lang in ("Hebrew", "Greek"):
    c.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
        WHERE language=?
          AND NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
    """, (lang,))
    row_fmt(f"  — uncovered [{lang}]", c.fetchone()[0], indent=1)

hr("orphaned wa_meaning_parsed (no matching term_inv)")
c.execute("""
    SELECT COUNT(*) FROM wa_meaning_parsed mp
    WHERE NOT EXISTS (SELECT 1 FROM wa_term_inventory ti WHERE ti.id = mp.term_inv_id)
""")
orphan_parsed = c.fetchone()[0]
row_fmt("Orphaned wa_meaning_parsed rows", orphan_parsed, indent=1)

hr("parse quality indicators")
c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE parse_warnings IS NOT NULL AND TRIM(parse_warnings) != ''")
with_warnings = c.fetchone()[0]
row_fmt("Rows WITH parse_warnings", with_warnings, indent=1)

c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE top_sense_count = 0")
zero_sense = c.fetchone()[0]
row_fmt("Rows with top_sense_count = 0", zero_sense, indent=1)

c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE stem_count = 0 AND language = 'Hebrew'")
heb_no_stems = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE language = 'Hebrew'")
heb_total = c.fetchone()[0]
row_fmt("Hebrew rows with stem_count = 0", f"{heb_no_stems}  /  {heb_total}", indent=1)

c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE has_causative_stem = 1")
causative = c.fetchone()[0]
row_fmt("Rows flagged has_causative_stem", causative, indent=1)

c.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE has_domain_tags = 1")
domain = c.fetchone()[0]
row_fmt("Rows flagged has_domain_tags", domain, indent=1)

# top warnings (if any)
if with_warnings > 0:
    hr("sample parse_warnings (first 10 distinct)")
    c.execute("""
        SELECT DISTINCT parse_warnings FROM wa_meaning_parsed
        WHERE parse_warnings IS NOT NULL AND TRIM(parse_warnings) != ''
        LIMIT 10
    """)
    for r in c.fetchall():
        print(f"  '{r[0]}'")

# ─────────────────────────────────────────────────────────────────────────────
section("C  wa_meaning_sense")
# ─────────────────────────────────────────────────────────────────────────────

c.execute("SELECT COUNT(*) FROM wa_meaning_sense")
total_sense = c.fetchone()[0]
row_fmt("Total wa_meaning_sense rows", total_sense, indent=1)

c.execute("SELECT COUNT(DISTINCT parsed_meaning_id) FROM wa_meaning_sense")
parents_with_senses = c.fetchone()[0]
row_fmt("Distinct parsed_meaning_id values", parents_with_senses, indent=1)

if total_parsed > 0 and parents_with_senses > 0:
    avg_sense = total_sense / parents_with_senses
    row_fmt("Avg senses per parsed entry (populated)", f"{avg_sense:.1f}", indent=1)

hr("orphaned senses (no matching wa_meaning_parsed)")
c.execute("""
    SELECT COUNT(*) FROM wa_meaning_sense s
    WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = s.parsed_meaning_id)
""")
orphan_sense = c.fetchone()[0]
row_fmt("Orphaned wa_meaning_sense rows", orphan_sense, indent=1)

hr("parsed entries with zero sense rows in junction")
c.execute("""
    SELECT COUNT(*) FROM wa_meaning_parsed mp
    WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_sense s WHERE s.parsed_meaning_id = mp.id)
""")
parsed_no_senses = c.fetchone()[0]
row_fmt("Parsed rows with no sense rows", parsed_no_senses, indent=1)

hr("level distribution")
c.execute("""
    SELECT level_code, COUNT(*) AS cnt
    FROM wa_meaning_sense
    GROUP BY level_code
    ORDER BY cnt DESC
    LIMIT 15
""")
for r in c.fetchall():
    row_fmt(f"  level_code = '{r['level_code']}'", r['cnt'], indent=1)

hr("stem labels")
c.execute("SELECT COUNT(*) FROM wa_meaning_sense WHERE is_stem_label = 1")
stem_labels = c.fetchone()[0]
row_fmt("Rows with is_stem_label = 1", stem_labels, indent=1)

c.execute("SELECT COUNT(*) FROM wa_meaning_sense WHERE domain_tag IS NOT NULL AND TRIM(domain_tag) != ''")
domain_tags = c.fetchone()[0]
row_fmt("Rows with domain_tag populated", domain_tags, indent=1)

# ─────────────────────────────────────────────────────────────────────────────
section("D  wa_meaning_stem")
# ─────────────────────────────────────────────────────────────────────────────

c.execute("SELECT COUNT(*) FROM wa_meaning_stem")
total_stem = c.fetchone()[0]
row_fmt("Total wa_meaning_stem rows", total_stem, indent=1)

c.execute("SELECT COUNT(DISTINCT parsed_meaning_id) FROM wa_meaning_stem")
parents_with_stems = c.fetchone()[0]
row_fmt("Distinct parsed_meaning_id values", parents_with_stems, indent=1)

hr("orphaned stems (no matching wa_meaning_parsed)")
c.execute("""
    SELECT COUNT(*) FROM wa_meaning_stem st
    WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = st.parsed_meaning_id)
""")
orphan_stem = c.fetchone()[0]
row_fmt("Orphaned wa_meaning_stem rows", orphan_stem, indent=1)

hr("Hebrew parsed entries without any stem rows")
c.execute("""
    SELECT COUNT(*) FROM wa_meaning_parsed mp
    WHERE mp.language = 'Hebrew'
      AND NOT EXISTS (SELECT 1 FROM wa_meaning_stem st WHERE st.parsed_meaning_id = mp.id)
""")
heb_no_stem_rows = c.fetchone()[0]
row_fmt("Hebrew parsed — no stem rows", f"{heb_no_stem_rows}  /  {heb_total}", indent=1)

hr("stem_type distribution")
c.execute("""
    SELECT COALESCE(stem_type, '(NULL)') AS st, COUNT(*) AS cnt
    FROM wa_meaning_stem
    GROUP BY st
    ORDER BY cnt DESC
""")
for r in c.fetchall():
    row_fmt(f"  stem_type = '{r['st']}'", r['cnt'], indent=1)

# ─────────────────────────────────────────────────────────────────────────────
section("E  wa_lsj_parsed — Greek LSJ coverage")
# ─────────────────────────────────────────────────────────────────────────────

c.execute("SELECT COUNT(*) FROM wa_lsj_parsed")
total_lsj = c.fetchone()[0]
row_fmt("Total wa_lsj_parsed rows", total_lsj, indent=1)

# Greek terms in wa_term_inventory
c.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language = 'Greek'")
greek_terms = c.fetchone()[0]
row_fmt(f"Total Greek terms in wa_term_inventory", greek_terms, indent=1)

if greek_terms > 0:
    pct = 100 * total_lsj // greek_terms
    row_fmt("LSJ coverage of Greek terms", f"{total_lsj}  /  {greek_terms}  ({pct}%)", indent=1)

hr("orphaned lsj_parsed (no matching wa_term_inventory)")
c.execute("""
    SELECT COUNT(*) FROM wa_lsj_parsed lsj
    WHERE NOT EXISTS (SELECT 1 FROM wa_term_inventory ti WHERE ti.id = lsj.term_inv_id)
""")
orphan_lsj = c.fetchone()[0]
row_fmt("Orphaned wa_lsj_parsed rows", orphan_lsj, indent=1)

hr("Greek terms WITHOUT lsj_parsed row")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE ti.language = 'Greek'
      AND NOT EXISTS (SELECT 1 FROM wa_lsj_parsed lsj WHERE lsj.term_inv_id = ti.id)
""")
greek_no_lsj = c.fetchone()[0]
row_fmt("Greek terms missing LSJ parse", greek_no_lsj, indent=1)

hr("lsj field population")
for col in ("lsj_gloss", "lsj_domains", "lsj_philosophical_note", "lsj_etymology_note", "lsj_cognate_forms"):
    c.execute(f"SELECT COUNT(*) FROM wa_lsj_parsed WHERE {col} IS NOT NULL AND TRIM({col}) != ''")
    pop = c.fetchone()[0]
    pct = (100 * pop // total_lsj) if total_lsj else 0
    row_fmt(f"{col}", f"{pop:>4}  /  {total_lsj}  ({pct}%)", indent=1)

# ─────────────────────────────────────────────────────────────────────────────
section("F  parse source gap analysis")
# ─────────────────────────────────────────────────────────────────────────────

hr("terms with meaning text but NO parsed row")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE ti.meaning IS NOT NULL AND TRIM(ti.meaning) != ''
      AND NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
""")
meaning_no_parse = c.fetchone()[0]
row_fmt("meaning present, no wa_meaning_parsed", meaning_no_parse, indent=1)

# breakdown by language
for lang in ("Hebrew", "Greek"):
    c.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
        WHERE ti.language=? AND ti.meaning IS NOT NULL AND TRIM(ti.meaning) != ''
          AND NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
    """, (lang,))
    row_fmt(f"  — {lang}", c.fetchone()[0], indent=1)

hr("lsj_entry present but no wa_lsj_parsed row (parse source gap)")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE ti.lsj_entry IS NOT NULL AND TRIM(ti.lsj_entry) != ''
      AND NOT EXISTS (SELECT 1 FROM wa_lsj_parsed lsj WHERE lsj.term_inv_id = ti.id)
""")
lsj_entry_no_parse = c.fetchone()[0]
row_fmt("lsj_entry present, no wa_lsj_parsed row", lsj_entry_no_parse, indent=1)

hr("wa_lsj_parsed exists but lsj_entry IS NULL/empty")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    JOIN wa_lsj_parsed lsj ON lsj.term_inv_id = ti.id
    WHERE ti.lsj_entry IS NULL OR TRIM(ti.lsj_entry) = ''
""")
lsj_parse_no_entry = c.fetchone()[0]
row_fmt("wa_lsj_parsed exists, lsj_entry NULL/empty", lsj_parse_no_entry, indent=1)

hr("raw_lsj in wa_lsj_parsed vs lsj_entry alignment")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    JOIN wa_lsj_parsed lsj ON lsj.term_inv_id = ti.id
    WHERE lsj.raw_lsj IS NULL OR TRIM(lsj.raw_lsj) = ''
""")
lsj_no_raw = c.fetchone()[0]
row_fmt("wa_lsj_parsed rows with raw_lsj NULL/empty", lsj_no_raw, indent=1)

hr("terms WITH parsed row but meaning IS NULL/empty")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE (ti.meaning IS NULL OR TRIM(ti.meaning) = '')
      AND EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
""")
parse_no_meaning = c.fetchone()[0]
row_fmt("wa_meaning_parsed exists, meaning NULL", parse_no_meaning, indent=1)

hr("parsed_meaning_id mismatch with wa_meaning_parsed.term_inv_id")
# parsed_meaning_id set, but the wa_meaning_parsed row for that id has a different term_inv_id
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    JOIN wa_meaning_parsed mp ON mp.id = ti.parsed_meaning_id
    WHERE mp.term_inv_id != ti.id
""")
mismatch = c.fetchone()[0]
row_fmt("parsed_meaning_id → wrong term_inv_id", mismatch, indent=1)

# terms where parsed_meaning_id is set but wa_meaning_parsed.term_inv_id != ti.id
# (i.e., FK is cross-linked)
hr("terms whose parsed_meaning_id is NOT set but a wa_meaning_parsed row exists for them")
c.execute("""
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE ti.parsed_meaning_id IS NULL
      AND EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
""")
missing_back_link = c.fetchone()[0]
row_fmt("parsed_meaning_id NULL but parsed row exists", missing_back_link, indent=1)

# ─────────────────────────────────────────────────────────────────────────────
section("G  sample detail lists (first 20 rows)")
# ─────────────────────────────────────────────────────────────────────────────

if meaning_no_parse > 0:
    hr("terms with meaning but no parse — sample")
    c.execute("""
        SELECT ti.id, ti.language, ti.strongs_number, ti.transliteration,
               SUBSTR(ti.meaning, 1, 60) AS meaning_snippet
        FROM wa_term_inventory ti
        WHERE ti.meaning IS NOT NULL AND TRIM(ti.meaning) != ''
          AND NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
        ORDER BY ti.language, ti.id
        LIMIT 20
    """)
    for r in c.fetchall():
        print(f"  id={r['id']:>4}  [{r['language'][:3]}]  {r['strongs_number']:<10}  {r['transliteration']:<20}  '{r['meaning_snippet']}…'")

if missing_back_link > 0:
    hr("wa_meaning_parsed exists but parsed_meaning_id not set — sample")
    c.execute("""
        SELECT ti.id, ti.language, ti.strongs_number, ti.transliteration, mp.id AS mp_id
        FROM wa_term_inventory ti
        JOIN wa_meaning_parsed mp ON mp.term_inv_id = ti.id
        WHERE ti.parsed_meaning_id IS NULL
        LIMIT 20
    """)
    for r in c.fetchall():
        print(f"  ti.id={r['id']:>4}  mp.id={r['mp_id']:>4}  [{r['language'][:3]}]  {r['strongs_number']:<10}  {r['transliteration']}")

if uncovered > 0:
    hr("terms WITHOUT any parsed row — sample (no meaning check)")
    c.execute("""
        SELECT ti.id, ti.language, fi.word, ti.strongs_number, ti.transliteration,
               CASE WHEN ti.meaning IS NULL OR TRIM(ti.meaning)='' THEN 'no-meaning' ELSE 'has-meaning' END AS meaning_status
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.term_inv_id = ti.id)
        ORDER BY ti.language, fi.word, ti.id
        LIMIT 20
    """)
    for r in c.fetchall():
        w = r["word"]
        sn = r["strongs_number"] or ""
        print(f"  id={r['id']:>4}  [{r['language'][:3]}]  {w:<16}  {sn:<10}  {r['transliteration']:<20}  ({r['meaning_status']})")

print()
hr()
print("  Assessment complete.")
hr()
conn.close()
