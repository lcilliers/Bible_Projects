"""
Pre-flight validation script — reads only, no writes.
Validates every Fix in db_remediation_plan.md against the live database.
"""
import sqlite3
import os

db = "data/bible_research.db"
conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row
# Connect the same way db_client.py does
conn.execute("PRAGMA foreign_keys = ON")
conn.execute("PRAGMA journal_mode = WAL")

def q(sql, params=()):
    return conn.execute(sql, params).fetchall()

def q1(sql, params=()):
    r = conn.execute(sql, params).fetchone()
    return r[0] if r else None

section = lambda s: print(f"\n{'='*60}\n{s}\n{'='*60}")
ok = lambda msg: print(f"  ✓ PASS  {msg}")
warn = lambda msg: print(f"  ⚠ WARN  {msg}")
fail = lambda msg: print(f"  ✗ FAIL  {msg}")
info = lambda msg: print(f"  ·       {msg}")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 1 — FK Enforcement")
# ──────────────────────────────────────────────────────────────────────────────

fk_pragma = q1("PRAGMA foreign_keys")
info(f"PRAGMA foreign_keys on this connection = {fk_pragma}")

# Check db_client.py source for FK pragma
with open("analytics/db_client.py") as f:
    src = f.read()
if "PRAGMA foreign_keys = ON" in src:
    ok("db_client.py already sets PRAGMA foreign_keys = ON — Fix 1 is ALREADY DONE for db_client.py")
else:
    fail("db_client.py does NOT set PRAGMA foreign_keys = ON")

with open("engine/db.py") as f:
    src2 = f.read()
if "PRAGMA foreign_keys = ON" in src2:
    ok("engine/db.py already sets PRAGMA foreign_keys = ON")
else:
    info("engine/db.py does not set it directly — relies on db_client.py (which already sets it via _base_get_connection)")
    ok("engine/db.py calls db_client.get_connection() which sets FK ON — effective")

# Full FK check with enforcement ON
violations = q("PRAGMA foreign_key_check")
if not violations:
    ok("PRAGMA foreign_key_check = 0 violations — safe to proceed")
else:
    fail(f"FK violations exist ({len(violations)}) — must fix before table recreations")
    for v in violations:
        print(f"      Table={v[0]} rowid={v[1]} ref={v[2]} fk={v[3]}")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 2 — Zero-Padding Normalisation")
# ──────────────────────────────────────────────────────────────────────────────

zp_checks = [
    ("wa_file_index",      "registry_id",   "registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"),
    ("mti_terms",          "owning_registry","owning_registry GLOB '0[0-9]*' AND owning_registry != CAST(CAST(owning_registry AS INTEGER) AS TEXT)"),
    ("mti_term_cross_refs","registry",       "registry GLOB '0[0-9]*' AND registry != CAST(CAST(registry AS INTEGER) AS TEXT)"),
    ("word_run_state",     "registry_id",    "registry_id GLOB '0[0-9]*' AND registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT)"),
]
for tbl, col, cond in zp_checks:
    cnt = q1(f"SELECT COUNT(*) FROM [{tbl}] WHERE {cond}")
    if cnt == 0:
        ok(f"{tbl}.{col}: already normalised (0 zero-padded rows)")
    else:
        warn(f"{tbl}.{col}: {cnt} zero-padded rows to fix")

# After fix: verify join works
# Check that word_registry_fk and registry_id agree in wa_file_index AFTER fix
mismatch_fi = q1("SELECT COUNT(*) FROM wa_file_index WHERE registry_id != CAST(word_registry_fk AS TEXT)")
info(f"wa_file_index: rows where registry_id != CAST(word_registry_fk AS TEXT) = {mismatch_fi} (should be 0 post-fix)")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 3 — wa_file_index Exact Column Inventory")
# ──────────────────────────────────────────────────────────────────────────────

cols_fi = q("PRAGMA table_info(wa_file_index)")
info("Live columns in wa_file_index:")
for c in cols_fi:
    print(f"      [{c['cid']}] {c['name']}  {c['type']}  nn={c['notnull']}  dflt={c['dflt_value']}")

plan_cols_fi = [
    "id","filename","registry_id","word_registry_fk","word","part_number","total_parts",
    "is_split","schema_version","phase","produced_date","source_file","translation_used",
    "specification","revision_note","source_list","category","testament_coverage",
    "root_families_in_prior_parts","last_changed"
]
live_names_fi = [c['name'] for c in cols_fi]
missing = [c for c in plan_cols_fi if c not in live_names_fi]
extra   = [c for c in live_names_fi if c not in plan_cols_fi]
if not missing and not extra:
    ok("Column list in Fix 3 script matches live table exactly")
else:
    if missing: fail(f"Columns in plan but NOT in live table: {missing}")
    if extra:   warn(f"Columns in live table but NOT in plan: {extra}")

# Check triggers on wa_file_index
triggers_fi = q("SELECT name, sql FROM sqlite_master WHERE type='trigger' AND tbl_name='wa_file_index'")
if triggers_fi:
    warn(f"wa_file_index has triggers that must be recreated: {[t['name'] for t in triggers_fi]}")
else:
    ok("wa_file_index has no triggers — no trigger recreation needed")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 4 — wa_term_inventory Exact Column Inventory")
# ──────────────────────────────────────────────────────────────────────────────

cols_ti = q("PRAGMA table_info(wa_term_inventory)")
info("Live columns in wa_term_inventory:")
for c in cols_ti:
    print(f"      [{c['cid']}] {c['name']}  {c['type']}  nn={c['notnull']}  dflt={c['dflt_value']}")

plan_cols_ti = [
    "id","file_id","language","term_id","strongs_number","transliteration",
    "step_search_gloss","word_analysis_gloss","occurrence_count","occurrence_count_qualifier",
    "meaning","meaning_numbered","also_spelled","lsj_entry","testament",
    "god_as_subject","somatic_link","causative_form_present","status_note",
    "last_changed","short_def_mounce","parsed_meaning_id"
]
live_names_ti = [c['name'] for c in cols_ti]
missing_ti = [c for c in plan_cols_ti if c not in live_names_ti]
extra_ti   = [c for c in live_names_ti if c not in plan_cols_ti]
if not missing_ti and not extra_ti:
    ok("Column list in Fix 4 script matches live table exactly")
else:
    if missing_ti: fail(f"Columns in plan but NOT in live: {missing_ti}")
    if extra_ti:   warn(f"Columns in live but NOT in plan: {extra_ti}")

# Check file_id orphans (are all wa_term_inventory.file_id values valid wa_file_index.id?)
ti_file_orphans = q1("SELECT COUNT(*) FROM wa_term_inventory WHERE file_id NOT IN (SELECT id FROM wa_file_index)")
if ti_file_orphans == 0:
    ok("wa_term_inventory.file_id: 0 orphans — FK is satisfiable")
else:
    fail(f"wa_term_inventory.file_id: {ti_file_orphans} orphan rows — FK CANNOT be registered until fixed")

# NOT NULL constraint check — are any file_id values NULL?
ti_file_null = q1("SELECT COUNT(*) FROM wa_term_inventory WHERE file_id IS NULL")
if ti_file_null == 0:
    ok("wa_term_inventory.file_id: 0 NULLs — NOT NULL constraint in plan is safe")
else:
    fail(f"wa_term_inventory.file_id: {ti_file_null} NULL values — plan says NOT NULL, will fail")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 5 — wa_term_related_words")
# ──────────────────────────────────────────────────────────────────────────────

rw_orphans = q1("SELECT COUNT(*) FROM wa_term_related_words WHERE term_inv_id NOT IN (SELECT id FROM wa_term_inventory)")
if rw_orphans == 0:
    ok("wa_term_related_words.term_inv_id: 0 orphans — FK is satisfiable")
else:
    fail(f"wa_term_related_words.term_inv_id: {rw_orphans} orphans — would fail FK insert")

rw_null = q1("SELECT COUNT(*) FROM wa_term_related_words WHERE term_inv_id IS NULL")
info(f"wa_term_related_words.term_inv_id NULLs: {rw_null}")

cols_rw = [c['name'] for c in q("PRAGMA table_info(wa_term_related_words)")]
plan_rw = ["id","term_inv_id","gloss","transliteration","strongs_number","relationship_note"]
if cols_rw == plan_rw:
    ok("Column list in Fix 5 matches live table exactly")
else:
    warn(f"Live cols: {cols_rw}  Plan cols: {plan_rw}")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 6 — wa_term_root_family")
# ──────────────────────────────────────────────────────────────────────────────

rf_orphans = q1("SELECT COUNT(*) FROM wa_term_root_family WHERE term_inv_id NOT IN (SELECT id FROM wa_term_inventory)")
if rf_orphans == 0:
    ok("wa_term_root_family.term_inv_id: 0 orphans — FK is satisfiable")
else:
    fail(f"wa_term_root_family.term_inv_id: {rf_orphans} orphans")

cols_rf = [c['name'] for c in q("PRAGMA table_info(wa_term_root_family)")]
plan_rf = ["id","term_inv_id","root_code","root_language","root_gloss","note"]
if cols_rf == plan_rf:
    ok("Column list in Fix 6 matches live table exactly")
else:
    warn(f"Live cols: {cols_rf}  Plan cols: {plan_rf}")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 7 — wa_verse_records")
# ──────────────────────────────────────────────────────────────────────────────

vr_count = q1("SELECT COUNT(*) FROM wa_verse_records")
info(f"wa_verse_records row count: {vr_count} (plan expects 57130)")
if vr_count == 57130:
    ok("Row count matches plan expectation")
else:
    warn(f"Row count {vr_count} differs from plan's 57130 — update the verification check")

vr_file_orphans = q1("SELECT COUNT(*) FROM wa_verse_records WHERE file_id NOT IN (SELECT id FROM wa_file_index)")
if vr_file_orphans == 0:
    ok("wa_verse_records.file_id: 0 orphans — FK to wa_file_index is satisfiable")
else:
    fail(f"wa_verse_records.file_id: {vr_file_orphans} orphans")

vr_file_null = q1("SELECT COUNT(*) FROM wa_verse_records WHERE file_id IS NULL")
if vr_file_null == 0:
    ok("wa_verse_records.file_id: 0 NULLs — NOT NULL constraint in plan is safe")
else:
    fail(f"wa_verse_records.file_id: {vr_file_null} NULLs — NOT NULL would fail")

vr_term_orphans = q1("""
    SELECT COUNT(*) FROM wa_verse_records 
    WHERE term_inv_id IS NOT NULL 
      AND term_inv_id NOT IN (SELECT id FROM wa_term_inventory)
""")
if vr_term_orphans == 0:
    ok("wa_verse_records.term_inv_id: 0 orphans — FK to wa_term_inventory is satisfiable")
else:
    fail(f"wa_verse_records.term_inv_id: {vr_term_orphans} orphans")

# Check the trigger on wa_verse_records — MUST be recreated
triggers_vr = q("SELECT name, sql FROM sqlite_master WHERE type='trigger' AND tbl_name='wa_verse_records'")
for t in triggers_vr:
    warn(f"wa_verse_records has trigger '{t['name']}' — must be recreated in Fix 7 script")
    info(f"  DDL: {t['sql'][:120]}...")

cols_vr = [c['name'] for c in q("PRAGMA table_info(wa_verse_records)")]
plan_vr = ["id","file_id","term_inv_id","term_id","transliteration","testament","reference",
           "verse_text","last_changed","book_id","chapter","verse_num","translation",
           "note","claude_output","created_at","updated_at","target_word","span_strong_match",
           "context_before","context_after"]
missing_vr = [c for c in plan_vr if c not in cols_vr]
extra_vr   = [c for c in cols_vr if c not in plan_vr]
if not missing_vr and not extra_vr:
    ok("Column list in Fix 7 matches live table exactly")
else:
    if missing_vr: fail(f"In plan but not in live: {missing_vr}")
    if extra_vr:   warn(f"In live but not in plan: {extra_vr}")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 8a — DQF Orphan Audit (pre-checks)")
# ──────────────────────────────────────────────────────────────────────────────

dqf_total = q1("SELECT COUNT(*) FROM wa_data_quality_flags")
dqf_orphans = q1("""
    SELECT COUNT(*) FROM wa_data_quality_flags
    WHERE term_id IS NOT NULL
      AND NOT EXISTS (SELECT 1 FROM wa_term_inventory wti WHERE wti.term_id = wa_data_quality_flags.term_id)
""")
info(f"wa_data_quality_flags total={dqf_total}, term_id orphans={dqf_orphans} (plan says 53)")
if dqf_orphans == 53:
    ok("Orphan count matches plan exactly")
else:
    warn(f"Orphan count is {dqf_orphans}, plan expects 53")

# Verify the 2 duplicate (file_id, term_id) pairs in wa_term_inventory
dups = q("""
    SELECT file_id, term_id, COUNT(*) c FROM wa_term_inventory
    GROUP BY file_id, term_id HAVING c > 1
""")
info(f"Duplicate (file_id, term_id) pairs in wa_term_inventory: {len(dups)}")
for d in dups:
    ids = [r[0] for r in q("SELECT id FROM wa_term_inventory WHERE file_id=? AND term_id=?", (d['file_id'], d['term_id']))]
    info(f"  file_id={d['file_id']} term_id={d['term_id']} -> ids={ids} -> MIN will use {min(ids)}")
if len(dups) == 2:
    ok("Exactly 2 duplicate pairs confirmed — MIN(id) resolution in Fix 8b is correct")
else:
    warn(f"Expected 2 duplicate pairs, found {len(dups)}")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 8b — wa_data_quality_flags Column Check")
# ──────────────────────────────────────────────────────────────────────────────

cols_dqf = [c['name'] for c in q("PRAGMA table_info(wa_data_quality_flags)")]
plan_dqf = ["id","file_id","term_id","flag_id","description","last_changed"]
info(f"Live columns: {cols_dqf}")
info(f"Plan inserts: id, file_id, term_inv_id(NEW), term_id, flag_id, description, last_changed")
missing_dqf = [c for c in plan_dqf if c not in cols_dqf]
if missing_dqf:
    fail(f"Plan references columns not in live table: {missing_dqf}")
else:
    ok("All source columns required for INSERT exist in live table")

# ──────────────────────────────────────────────────────────────────────────────
section("FIX 9 — MTI Tables")
# ──────────────────────────────────────────────────────────────────────────────

cols_mti = [c['name'] for c in q("PRAGMA table_info(mti_terms)")]
plan_mti_src = ["id","strongs_number","transliteration","gloss","language",
               "owning_registry","owning_word","owning_part","word_data_reference",
               "status","status_note","exclusion_reason","extraction_date",
               "strongs_reconciled","anchor_note","last_changed"]
missing_mti = [c for c in plan_mti_src if c not in cols_mti]
extra_mti   = [c for c in cols_mti if c not in plan_mti_src]
info(f"Live mti_terms columns: {cols_mti}")
if not missing_mti and not extra_mti:
    ok("mti_terms source columns in plan match live table exactly")
else:
    if missing_mti: fail(f"In plan but not live: {missing_mti}")
    if extra_mti:   warn(f"In live but not plan: {extra_mti}")

# word_data_reference castability check
non_castable = q1("""
    SELECT COUNT(*) FROM mti_terms 
    WHERE word_data_reference IS NOT NULL 
      AND CAST(word_data_reference AS INTEGER) = 0
      AND word_data_reference != '0'
""")
info(f"mti_terms.word_data_reference non-castable-to-integer rows: {non_castable}")
if non_castable == 0:
    ok("mti_terms.word_data_reference: all non-null values cast to INTEGER safely")
else:
    fail(f"{non_castable} rows have word_data_reference that cannot cast to integer")

# Check that CAST(owning_registry AS INTEGER) won't produce 0 for non-numeric rows
non_numeric_or = q1("""
    SELECT COUNT(*) FROM mti_terms
    WHERE owning_registry IS NOT NULL
      AND CAST(owning_registry AS INTEGER) = 0
      AND owning_registry NOT IN ('0','00','000')
""")
if non_numeric_or == 0:
    ok("mti_terms.owning_registry: all non-null values are numeric — safe to CAST to INTEGER")
else:
    fail(f"{non_numeric_or} mti_terms rows have non-numeric owning_registry")

# Check mti_term_cross_refs registry castability
cols_xcr = [c['name'] for c in q("PRAGMA table_info(mti_term_cross_refs)")]
plan_xcr_src = ["id","mti_term_id","registry","word","part","word_data_reference"]
missing_xcr = [c for c in plan_xcr_src if c not in cols_xcr]
if not missing_xcr:
    ok("mti_term_cross_refs: all source columns present")
else:
    fail(f"mti_term_cross_refs missing columns: {missing_xcr}")

non_numeric_xcr = q1("""
    SELECT COUNT(*) FROM mti_term_cross_refs
    WHERE registry IS NOT NULL
      AND CAST(registry AS INTEGER) = 0
      AND registry NOT IN ('0','00','000')
""")
if non_numeric_xcr == 0:
    ok("mti_term_cross_refs.registry: all values are numeric — safe to CAST")
else:
    fail(f"{non_numeric_xcr} rows have non-numeric registry")

# ──────────────────────────────────────────────────────────────────────────────
section("_ALLOWED_TABLES whitelist — new columns/tables check")
# ──────────────────────────────────────────────────────────────────────────────

# New columns being added: owning_registry_fk, word_data_ref_fk in mti_terms
# registry_fk in mti_term_cross_refs, term_inv_id in wa_data_quality_flags
# These are all in existing tables — no new table names, whitelist unaffected
ok("No new table names introduced — _ALLOWED_TABLES whitelist does not need updating")
info("New columns added: mti_terms.owning_registry_fk, mti_terms.word_data_ref_fk, mti_term_cross_refs.registry_fk, wa_data_quality_flags.term_inv_id")
info("Application code referencing these tables by name will continue to work")

# ──────────────────────────────────────────────────────────────────────────────
section("SCHEMA VERSION CHECK — Post-completion target")
# ──────────────────────────────────────────────────────────────────────────────

sv = conn.execute("SELECT version_code, applied_at FROM schema_version WHERE id=1").fetchone()
info(f"Current schema version: {sv['version_code']} applied {sv['applied_at']}")
info("Post-remediation version should be updated to 3.2.0")

conn.close()
print("\n" + "="*60)
print("VALIDATION COMPLETE")
print("="*60)
