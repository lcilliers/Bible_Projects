"""Update WA-SessionB-ClaudeCode-Instructions.md with all post-v5 changes."""
import os

PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "data", "imports", "WA", "Workflow", "Frameword_B", "Session_B",
    "WA-SessionB-ClaudeCode-Instructions.md"
)

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ── FIX 1: Header — update date and version references ──
content = content.replace(
    "> Extracted from all six v5 governing documents — 2026-03-27.",
    "> Extracted from all six v5 governing documents — 2026-03-27.\n> Updated 2026-03-29 for schema v3.7.0, housekeeping, and new columns."
)

# ── FIX 2: Section 2.4 A2 — add first-time population bypass ──
content = content.replace(
    "| A2 | DB snapshot + structural completeness check |",
    "| A2 | DB snapshot + structural completeness check (bypasses STOP if Step 1 JSON available for first-time population) |"
)

# ── FIX 3: Section 2.6 — update stale numbers ──
content = content.replace(
    "- **Run audit_word for remaining registries** — ~179 words still need Session B processing; each requires a current JSON export before DataPrep can begin",
    "- **Run audit_word for remaining registries** — 144 words at Ready for Analysis; all have been extracted and audited with current JSON exports"
)
content = content.replace(
    "- **Investigate zero-term registries** — 13 registries show no terms (Task 5 of Implementation Instruction); these may be data linkage issues requiring wa_file_index fixes or Phase 1 re-runs",
    "- **Zero-term registries** — resolved. All 6 non-excluded zero-term registries have been extracted and audited (consciousness, meekness, resolve, sensuality, energy, resentment)"
)

# ── FIX 4: Section 5.1 — correct scope logic ──
content = content.replace(
    "- **Scope**: `full` (pre-analysis) or `final` (Analysis Complete / Session B Complete)",
    "- **Scope**: `full` (pre-analysis) or `final` (v5.2 extraction complete — requires both session_b_status at Analysis Complete AND wa_session_b_dimensions row present)"
)

# ── FIX 5: Section 12 — replace stale impact summary with completed status ──
old_section_12 = """## 12. Engine and Script Impact Summary

The following engine components require updates to support v5:

| Component | Required Change |
|-----------|----------------|
| constants.py | Schema version update (3.6.0 -> next version after Tasks 1-8) |
| migrate.py | New migrations for Tasks 1, 3, 8 (ALTER TABLE, CREATE TABLE) |
| apply_session_patch.py | Support SESSIONB, SESSIOND, CLUSTERING patch types |
| audit.py | New audit checks for new tables and fields |
| flag_engine.py | Recognise new flag codes (SB_FINDING, SB_DIMENSION, etc.) |
| report.py | Include cluster_assignment, sb_classification in reports |
| word_export.py | Export new fields (evidential_status, retention_note, sb_classification, carry_forward) |

---"""

new_section_12 = """## 12. Engine and Script Status (v3.7.0)

All v5 implementation tasks complete. Schema at v3.7.0 (migration M16).

| Component | Status |
|-----------|--------|
| constants.py | Schema version 3.7.0 |
| migrate.py | Migrations M01-M16 complete |
| apply_session_patch.py | Supports SESSIONB, SESSIOND, CLUSTERING, update_evidential_status, SD pointers auto-report |
| audit_word.py | A2 first-time population bypass, scope-aware A11 export |
| flag_engine.py | All flag codes recognised |
| word_export.py | Exports evidential_status, retention_note, sb_classification, carry_forward, term_owner_type |

### Additional Scripts

| Script | Purpose |
|--------|---------|
| _batch_extract.py | Subprocess-isolated batch STEP extraction + audit_word |
| _produce_final_extract.py | Final registry extract (wa-{nnn}-{word}-final-{date}.json) from database |
| _generate_programme_report.py | Comprehensive programme status report |

---"""

content = content.replace(old_section_12, new_section_12)

# ── ADD: Section 13 — New columns and housekeeping ──
# Append before the final line
final_line = content.rstrip().split("\n")[-1]
content = content.rstrip()

section_13 = """

## 13. Schema Additions (post-v5 housekeeping, 2026-03-28)

### 13.1 word_registry — new columns

| Column | Type | Purpose |
|--------|------|---------|
| unique_term_count | INTEGER | Count of terms unique to this registry. Engine-derived. |
| shared_term_count | INTEGER | Count of terms shared with other registries. Engine-derived. |
| term_sharing_ratio | REAL | 0.0 (all unique) to 1.0 (all shared). Engine-derived. |

### 13.2 wa_term_inventory — new columns

| Column | Type | Purpose |
|--------|------|---------|
| term_owner_type | TEXT | OWNER (canonical home for this Strong's) or XREF (cross-reference copy). |

**XREF handling:** XREF term records remain active for cross-registry linkage queries. Their verse records are delete_flagged — excluded from all standard queries and exports.

### 13.3 wa_verse_records — new columns

| Column | Type | Purpose |
|--------|------|---------|
| mti_term_id | INTEGER | Direct FK to mti_terms.id — one-hop path from verse to master term. |

### 13.4 wa_quality_flag_types — new flag

| Flag Code | Description |
|-----------|-------------|
| CONCRETE_PHYSICAL | Term denotes a concrete physical object (sand, hand, stork). Flagged, not excluded. Verse analysis may reveal inner-being usage in context. |

### 13.5 Housekeeping rules

- Particle terms (ki, asher, al, im, etc.) are delete_flagged across all registries
- mti_status=delete is synced to wa_term_inventory.delete_flagged
- Verse records under delete_flagged terms are also delete_flagged
- XREF verse records are delete_flagged (OWNER verses only in active set)
- CONCRETE_PHYSICAL is a queryable filter, not an exclusion — terms remain active

### 13.6 Programme state queries — additions

**Term sharing (not-shared words):**
```sql
SELECT no, word, cluster_assignment, unique_term_count, phase1_term_count, phase1_verse_count
FROM word_registry
WHERE term_sharing_ratio = 0.0 AND phase1_status != 'Excluded' AND phase1_term_count > 0
ORDER BY no;
```

**Ownership distribution:**
```sql
SELECT term_owner_type, COUNT(*) as terms
FROM wa_term_inventory WHERE delete_flagged = 0
GROUP BY term_owner_type;
```

---

*WA-SessionB-ClaudeCode-Instructions  |  Updated 20260329  |  Schema v3.7.0*
"""

content += section_13

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("ClaudeCode Instructions updated — 5 fixes + Section 13 added.")
