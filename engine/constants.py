"""
constants.py
────────────
Shared constants for the Session A v9 Automation Engine.
"""

# Schema version this engine build requires.
# Bumped 2026-04-19 for DB-wide review migrations M19–M28 (changeplan v1).
# Bumped 2026-04-20 for evidence-flag redesign M29–M31 (coverage-flags-redesign-v1).
# Bumped 2026-04-20 evening for reference-as-DB POC M32 (vocab registry).
# Bumped 2026-04-20 night for reference-as-DB M33-M35 (rules + programme prose + patch types/patterns/labels).
# Bumped 2026-04-20 late for M36 (all addenda marked obsolete; extracts exclude by default).
# Bumped 2026-04-24 for M37 (per-term VC progress fields on mti_terms — vc_status,
# vc_instruction_version, vc_status_updated_at, vc_status_note; per-term model approved
# in alignment analysis v4 §8.1).
# Bumped 2026-04-24 for M38 (vc_status vocabulary cleanup — 'complete' -> 'vc_completed',
# 'approved' dropped; mti_terms.md_version column added for version-gating patch freshness
# per A-02 + A-03 resolutions).
# Bumped 2026-04-24 for M39 (delete NULL-skeleton verse_context rows — legacy pre-M37 seed
# cleanup; resolves coverage false-positives and VCNEW insert collisions).
# Bumped 2026-04-27 for M40-M43 (DB-capture architecture: verse_context.analysis_note,
# wa_prose_section_citations, wa_obs_question_catalogue.review_note, finding_id NULL).
# Bumped 2026-05-06 for M44-M45 (cluster_subgroup table + cluster_finding table).
# Bumped 2026-05-10 for M46 (term-to-sub-group m:n: new mti_term_subgroup join table,
# verse_context.cluster_subgroup_id added, mti_terms.cluster_subgroup_id dropped per
# DEC-1 of m39-subgroup-multi-term-design-v1).
# Bumped 2026-05-10 for M47 (vcg-to-term m:n: new vcg_term join table; drop
# verse_context_group.mti_term_id; absorbs 21 pre-existing cross-term placements).
# Bumped 2026-05-16 for M48 (cluster_finding.vcg_scope column + UNIQUE constraint
# extension for VCG-level Phase 9 scope markers per v2_2 §14).
# Bumped 2026-05-18 for M49 (characteristic + characteristic_subgroup +
# cluster_observation tables; supports many-sub-groups-per-characteristic and
# observation-carry-forward across phases per researcher direction 2026-05-18).
# Bumped 2026-05-18 for M50 (cluster_finding.characteristic_id column + extended
# UNIQUE; Phase 9 findings authored at characteristic scope, not sub-group, per
# researcher direction 2026-05-18 — "sub groups is purely a capacity organiser,
# the evaluating unit is the characteristic").
# Bumped 2026-05-25 for M52 (finding_citation table — polymorphic citations from
# cluster_finding + cluster_observation prose; three types: verse, strongs, cross_char).
# Bumped 2026-05-26 for M53 (cluster.char_structure column — flag non-standard
# clusters like M10 where chars are aspects of one master characteristic;
# tools doing cross-cluster char-comparison analytics filter on this).
# 2026-06-07 reconciliation: constant lagged the DB by one (M54 set the DB to
# 3.28.0 but the constant was left at 3.27.0). Realigned to 3.28.0. See
# research/investigations/wa-migration-control-integrity-v1-20260607.md.
# 2026-06-08: M55 applied (V3_2 schema — L1 verse fields, finding typing, morphology,
# homonym flag; vertical_pass_flag retired). → 3.29.0.
# 2026-06-09: M56 applied (L2 finding system — verse_context finding fields + universal
# finding / finding_question_link / finding_verse_link / finding_revision tables). → 3.30.0.
# 2026-06-10: M57 applied (L2 exploration views v_l2_tier + v_l2_meaning; read-only). → 3.31.0.
# 2026-06-15: M58 applied (word_registry_fk bypass on wa_verse_records + wa_term_inventory). → 3.32.0.
EXPECTED_SCHEMA_VERSION = "3.32.0"

# Sentinel written to word_registry.last_automation_run on successful audit completion.
AUDITED_SENTINEL = "AUDITED"

# Engine version string (written to term_fetch_log / engine_run_log).
ENGINE_VERSION = "1.0.0"

# Meaning parser version (written to wa_meaning_parsed.parse_version).
PARSER_VERSION = "1.0.0"

# In Progress sentinel value for word_registry.phase1_status lock check.
# Corrected 2026-04-19 per RD-DBR-001: data uses 'In Progress' (title case with
# space); prior value 'IN_PROGRESS' never matched actual stored values.
LOCK_SENTINEL = "In Progress"

# Stale lock threshold in seconds (2 hours).
STALE_LOCK_SECONDS = 7200

# Pre-run backup rolling retention count.
BACKUP_RETENTION = 10

# wa_file_index.specification constant for all v9 writes.
SPECIFICATION = "Session A v9 Automation"

# Default strong prefix → language mapping.
LANG_PREFIX = {"H": "Hebrew", "G": "Greek"}

# Derivable HIGH_FREQUENCY_ANCHOR threshold.
HIGH_FREQ_THRESHOLD = 500

# THIN_DATA threshold — terms with occurrence_count below this.
THIN_DATA_THRESHOLD = 20

# SMALL_VERSE_SAMPLE threshold — confirmed verse count below this.
SMALL_VERSE_SAMPLE_THRESHOLD = 5

# Verse/occurrence ratio check threshold (WR-08).
VERSE_OCCURRENCE_RATIO_THRESHOLD = 0.15
VERSE_OCCURRENCE_MIN_COUNT = 20
