"""
migrate_flag_tables.py — 2026-03-16

Consolidates and normalises all flag tables:

PHASE 2 FLAGS (analytical signals for future meaning-derivation phase):
  1. Create phase2_flag_types — consolidating wa_phase2_flag_types (12 rows)
     and mti_phase2_flags (1 row: THEOLOGICAL_ANCHOR) into a single lookup.
     Adds SOMATIC_EXPRESSION (was buried in quality flags) as a proper phase2 code.
  2. Recreate wa_term_phase2_flags  → FK: phase2_flag_types
  3. Recreate mti_term_flags        → FK: phase2_flag_types; remap flag_id 1 → new THEOLOGICAL_ANCHOR id
  4. Drop wa_phase2_flag_types and mti_phase2_flags

DATA QUALITY FLAGS (two-level: flag_group / flag_code per import entry):
  5. Create wa_quality_flag_types (id, flag_group, flag_code, description)
  6. Populate with 22 codes across 4 groups
  7. Rebuild wa_data_quality_flags: replace free-text flag column with flag_id FK,
     split slash-combined rows, move SOMATIC_EXPRESSION rows to wa_term_phase2_flags
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()
conn.execute("PRAGMA foreign_keys=OFF")

# ─── Inspect slash-combined rows before touching anything ─────────────────────
print("=== Slash-combined rows in wa_data_quality_flags ===")
slash_rows = [dict(r) for r in conn.execute("""
    SELECT dq.id, dq.file_id, dq.term_id, dq.flag, dq.description, dq.last_changed,
           ti.id AS term_inv_id
    FROM wa_data_quality_flags dq
    LEFT JOIN wa_term_inventory ti ON ti.term_id = dq.term_id
    WHERE dq.flag LIKE '%/%'
    ORDER BY dq.id
""").fetchall()]
for r in slash_rows:
    print(f"  id={r['id']}  term_id={r['term_id']}  "
          f"term_inv_id={r['term_inv_id']}  flag={r['flag']!r}")

# ─── Quality flag type definitions ────────────────────────────────────────────
QUALITY_FLAGS = [
    # (flag_group, flag_code, description)
    ("DATA_COVERAGE", "NO_VERSES",
     "No verse records found for this term in the source data"),
    ("DATA_COVERAGE", "THIN_DATA",
     "Fewer verse occurrences than expected; analysis may be limited"),
    ("DATA_COVERAGE", "SMALL_VERSE_SAMPLE",
     "Only a partial sample of available verses was captured"),
    ("DATA_COVERAGE", "NO_WORD_ANALYSIS",
     "No word-level analysis is available for this term"),
    ("DATA_COVERAGE", "UNCERTAIN_MEANING",
     "Meaning is uncertain or disputed"),
    ("DATA_COVERAGE", "ARAMAIC_EQUIVALENT",
     "Term has an Aramaic equivalent; Hebrew coverage is limited"),

    ("IMPORT_STATUS", "STRONGS_RECONCILED",
     "Strong's / STEP code was reconciled or corrected during import"),
    ("IMPORT_STATUS", "OCCURRENCE_COUNT_MISMATCH",
     "Verse occurrence count does not match the STEP source"),
    ("IMPORT_STATUS", "FORMAT_ERROR_IN_SOURCE",
     "Source file contained formatting errors"),
    ("IMPORT_STATUS", "FORMAT_ISSUE_RESOLVED",
     "A previously flagged formatting issue has been resolved"),
    ("IMPORT_STATUS", "PARSE_ERROR",
     "A parsing error occurred during import of this entry"),
    ("IMPORT_STATUS", "TERMS_IN_HEADER_NOT_IN_STEP",
     "Terms listed in the source header were not found in STEP"),
    ("IMPORT_STATUS", "DUPLICATE_IN_SOURCE",
     "Duplicate entry detected in the source data"),
    ("IMPORT_STATUS", "DUPLICATE_RESOLVED",
     "A previously identified duplicate has been resolved"),

    ("TERM_ANALYSIS", "CONSOLIDATION_CANDIDATE",
     "Term is a candidate for merging with a related term"),
    ("TERM_ANALYSIS", "MULTI_SENSE_ENTRY",
     "Term has multiple distinct semantic senses"),
    ("TERM_ANALYSIS", "CROSS_REGISTRY",
     "Term appears in or relates to multiple word registries"),
    ("TERM_ANALYSIS", "CROSS_PART_ROOT",
     "Root form spans both Old and New Testament corpora"),
    ("TERM_ANALYSIS", "PERIPHERAL_TERM",
     "Term is peripheral to the primary semantic field of this registry"),

    ("NOTE", "NOTE",
     "General annotation on this entry"),
    ("NOTE", "NOTE_ON_ROOT_FAMILY",
     "Annotation pertaining to root family relationships"),
    ("NOTE", "ANOMALY_NOTE",
     "An anomalous pattern has been noted for this entry"),
]

# Map existing TEXT flag values to flag_codes (identity for clean non-slash values)
TEXT_TO_CODE = {
    "STRONGS_RECONCILED":           "STRONGS_RECONCILED",
    "THIN_DATA":                    "THIN_DATA",
    "SMALL_VERSE_SAMPLE":           "SMALL_VERSE_SAMPLE",
    "NO_WORD_ANALYSIS":             "NO_WORD_ANALYSIS",
    "OCCURRENCE_COUNT_MISMATCH":    "OCCURRENCE_COUNT_MISMATCH",
    "NO_VERSES":                    "NO_VERSES",
    "CONSOLIDATION_CANDIDATE":      "CONSOLIDATION_CANDIDATE",
    "FORMAT_ERROR_IN_SOURCE":       "FORMAT_ERROR_IN_SOURCE",
    "TERMS_IN_HEADER_NOT_IN_STEP":  "TERMS_IN_HEADER_NOT_IN_STEP",
    "ANOMALY_NOTE":                 "ANOMALY_NOTE",
    "PARSE_ERROR":                  "PARSE_ERROR",
    "NOTE":                         "NOTE",
    "ARAMAIC_EQUIVALENT":           "ARAMAIC_EQUIVALENT",
    "PERIPHERAL_TERM":              "PERIPHERAL_TERM",
    "NOTE_ON_ROOT_FAMILY":          "NOTE_ON_ROOT_FAMILY",
    "MULTI_SENSE_ENTRY":            "MULTI_SENSE_ENTRY",
    "FORMAT_ISSUE_RESOLVED":        "FORMAT_ISSUE_RESOLVED",
    "DUPLICATE_RESOLVED":           "DUPLICATE_RESOLVED",
    "DUPLICATE_IN_SOURCE":          "DUPLICATE_IN_SOURCE",
    "CROSS_PART_ROOT":              "CROSS_PART_ROOT",
}

# Slash-combined → quality code list + optional phase2 flag code
# SOMATIC_EXPRESSION is a phase2 flag; its quality-pair goes to wa_term_phase2_flags
SLASH_MAP = {
    "THIN_DATA / UNCERTAIN_MEANING":        {"codes": ["THIN_DATA", "UNCERTAIN_MEANING"], "phase2": None},
    "PERIPHERAL_TERM / THIN_DATA":          {"codes": ["PERIPHERAL_TERM", "THIN_DATA"],   "phase2": None},
    "PERIPHERAL_TERM / SOMATIC_EXPRESSION": {"codes": ["PERIPHERAL_TERM"],                "phase2": "SOMATIC_EXPRESSION"},
    "MULTI_SENSE_ENTRY / CROSS_REGISTRY":   {"codes": ["MULTI_SENSE_ENTRY", "CROSS_REGISTRY"], "phase2": None},
}

# ─── Migration ────────────────────────────────────────────────────────────────
conn.execute("BEGIN")
try:
    # ── 1. Create phase2_flag_types (consolidated lookup) ─────────────────────
    conn.execute("""
        CREATE TABLE phase2_flag_types (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            flag_code   TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """)
    # Copy all 12 rows from wa_phase2_flag_types preserving their ids
    conn.execute("INSERT INTO phase2_flag_types SELECT id, flag_code, description FROM wa_phase2_flag_types")
    # Add THEOLOGICAL_ANCHOR from mti_phase2_flags (preserves its description)
    ta = dict(conn.execute("SELECT flag_code, description FROM mti_phase2_flags WHERE id=1").fetchone())
    conn.execute("INSERT INTO phase2_flag_types (flag_code, description) VALUES (?,?)",
                 (ta["flag_code"], ta["description"]))
    # Add SOMATIC_EXPRESSION (was misclassified as a quality flag)
    conn.execute("INSERT INTO phase2_flag_types (flag_code, description) VALUES (?,?)",
                 ("SOMATIC_EXPRESSION", "Term expresses inner state through somatic or body-language patterns"))

    theol_id   = conn.execute("SELECT id FROM phase2_flag_types WHERE flag_code='THEOLOGICAL_ANCHOR'").fetchone()[0]
    somatic_id = conn.execute("SELECT id FROM phase2_flag_types WHERE flag_code='SOMATIC_EXPRESSION'").fetchone()[0]
    total_p2   = conn.execute("SELECT COUNT(*) FROM phase2_flag_types").fetchone()[0]
    print(f"\n[1] phase2_flag_types created ({total_p2} rows)  "
          f"THEOLOGICAL_ANCHOR→id={theol_id}  SOMATIC_EXPRESSION→id={somatic_id}")

    # ── 2. Recreate wa_term_phase2_flags → FK: phase2_flag_types ──────────────
    conn.execute("ALTER TABLE wa_term_phase2_flags RENAME TO _wa_tpf_old")
    conn.execute("""
        CREATE TABLE wa_term_phase2_flags (
            term_inv_id INTEGER NOT NULL REFERENCES wa_term_inventory(id),
            flag_id     INTEGER NOT NULL REFERENCES phase2_flag_types(id),
            PRIMARY KEY (term_inv_id, flag_id)
        )
    """)
    conn.execute("INSERT INTO wa_term_phase2_flags SELECT term_inv_id, flag_id FROM _wa_tpf_old")
    n_tpf = conn.execute("SELECT COUNT(*) FROM wa_term_phase2_flags").fetchone()[0]
    conn.execute("DROP TABLE _wa_tpf_old")
    print(f"[2] wa_term_phase2_flags recreated ({n_tpf} rows) → FK: phase2_flag_types")

    # ── 3. Recreate mti_term_flags → FK: phase2_flag_types; remap flag_id ─────
    #    Old: flag_id=1 referenced mti_phase2_flags.id=1 (THEOLOGICAL_ANCHOR)
    #    New: flag_id must reference phase2_flag_types.id=theol_id
    conn.execute("ALTER TABLE mti_term_flags RENAME TO _mti_tf_old")
    conn.execute("""
        CREATE TABLE mti_term_flags (
            mti_term_id INTEGER NOT NULL REFERENCES mti_terms(id),
            flag_id     INTEGER NOT NULL REFERENCES phase2_flag_types(id),
            PRIMARY KEY (mti_term_id, flag_id)
        )
    """)
    conn.execute(
        "INSERT INTO mti_term_flags SELECT mti_term_id, ? FROM _mti_tf_old WHERE flag_id=1",
        (theol_id,))
    n_mtf = conn.execute("SELECT COUNT(*) FROM mti_term_flags").fetchone()[0]
    conn.execute("DROP TABLE _mti_tf_old")
    print(f"[3] mti_term_flags recreated ({n_mtf} rows) flag_id 1→{theol_id}")

    # ── 4. Drop old separate lookup tables ────────────────────────────────────
    conn.execute("DROP TABLE wa_phase2_flag_types")
    conn.execute("DROP TABLE mti_phase2_flags")
    print("[4] wa_phase2_flag_types and mti_phase2_flags dropped")

    # ── 5. Create wa_quality_flag_types ───────────────────────────────────────
    conn.execute("""
        CREATE TABLE wa_quality_flag_types (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            flag_group  TEXT NOT NULL,
            flag_code   TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO wa_quality_flag_types (flag_group, flag_code, description) VALUES (?,?,?)",
        QUALITY_FLAGS)
    print(f"[5] wa_quality_flag_types created ({len(QUALITY_FLAGS)} rows)")

    # ── 6. Build flag_code → id map ───────────────────────────────────────────
    code_to_id = {r[0]: r[1] for r in conn.execute(
        "SELECT flag_code, id FROM wa_quality_flag_types").fetchall()}

    # ── 7. Load all existing quality flag rows (with term_inv_id via join) ────
    dq_rows = [dict(r) for r in conn.execute("""
        SELECT dq.id, dq.file_id, dq.term_id, dq.flag, dq.description, dq.last_changed,
               ti.id AS term_inv_id
        FROM wa_data_quality_flags dq
        LEFT JOIN wa_term_inventory ti ON ti.term_id = dq.term_id
        ORDER BY dq.id
    """).fetchall()]

    new_dq_rows  = []  # (file_id, term_id, flag_id, description, last_changed)
    phase2_to_add = []  # (term_inv_id, flag_id) for SOMATIC_EXPRESSION splits

    for row in dq_rows:
        flag_text = row["flag"]
        if "/" in flag_text:
            mapping = SLASH_MAP.get(flag_text)
            if not mapping:
                raise ValueError(f"Unknown slash-combined flag: {flag_text!r}")
            for code in mapping["codes"]:
                new_dq_rows.append((row["file_id"], row["term_id"], code_to_id[code],
                                    row["description"], row["last_changed"]))
            if mapping["phase2"] and row["term_inv_id"]:
                phase2_to_add.append((row["term_inv_id"], somatic_id))
        else:
            code = TEXT_TO_CODE.get(flag_text)
            if not code:
                raise ValueError(f"Unmapped quality flag text: {flag_text!r}")
            new_dq_rows.append((row["file_id"], row["term_id"], code_to_id[code],
                                row["description"], row["last_changed"]))

    # ── 8. Rebuild wa_data_quality_flags with new schema ──────────────────────
    conn.execute("DROP TABLE wa_data_quality_flags")
    conn.execute("""
        CREATE TABLE wa_data_quality_flags (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id      INTEGER NOT NULL REFERENCES wa_file_index(id),
            term_id      TEXT,
            flag_id      INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
            description  TEXT,
            last_changed TEXT
        )
    """)
    conn.execute("CREATE INDEX idx_wdqf_file ON wa_data_quality_flags (file_id)")
    conn.execute("CREATE INDEX idx_wdqf_flag ON wa_data_quality_flags (flag_id)")
    conn.executemany(
        "INSERT INTO wa_data_quality_flags (file_id, term_id, flag_id, description, last_changed) VALUES (?,?,?,?,?)",
        new_dq_rows)
    print(f"[6] wa_data_quality_flags rebuilt: {len(new_dq_rows)} rows (was {len(dq_rows)})")

    # ── 9. Add SOMATIC_EXPRESSION phase2 flags from split rows ────────────────
    if phase2_to_add:
        for term_inv_id, fid in phase2_to_add:
            conn.execute(
                "INSERT OR IGNORE INTO wa_term_phase2_flags (term_inv_id, flag_id) VALUES (?,?)",
                (term_inv_id, fid))
        print(f"[7] Added {len(phase2_to_add)} SOMATIC_EXPRESSION entry(s) to wa_term_phase2_flags")

    conn.execute("COMMIT")
    print("\n✓ Migration complete")

except Exception as e:
    conn.execute("ROLLBACK")
    print(f"\n✗ ROLLED BACK: {e}")
    raise
finally:
    conn.execute("PRAGMA foreign_keys=ON")

# ─── Post-migration summary ───────────────────────────────────────────────────
print("\n=== Post-migration row counts ===")
for tbl in ("phase2_flag_types", "wa_term_phase2_flags", "mti_term_flags",
            "wa_quality_flag_types", "wa_data_quality_flags"):
    n = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
    print(f"  {tbl:35s}  {n}")

print("\n=== phase2_flag_types ===")
for r in conn.execute("SELECT id, flag_code FROM phase2_flag_types ORDER BY id").fetchall():
    print(f"  {r[0]:3d}  {r[1]}")

print("\n=== wa_quality_flag_types ===")
for r in conn.execute("SELECT id, flag_group, flag_code FROM wa_quality_flag_types ORDER BY id").fetchall():
    print(f"  {r[0]:3d}  {r[1]:20s}  {r[2]}")

conn.close()
