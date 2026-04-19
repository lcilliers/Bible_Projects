"""
constants.py
────────────
Shared constants for the Session A v9 Automation Engine.
"""

# Schema version this engine build requires.
EXPECTED_SCHEMA_VERSION = "3.9.0"

# Sentinel written to word_registry.last_automation_run on successful audit completion.
AUDITED_SENTINEL = "AUDITED"

# Engine version string (written to term_fetch_log / engine_run_log).
ENGINE_VERSION = "1.0.0"

# Meaning parser version (written to wa_meaning_parsed.parse_version).
PARSER_VERSION = "1.0.0"

# IN_PROGRESS sentinel value written to word_registry.last_automation_run.
LOCK_SENTINEL = "IN_PROGRESS"

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
