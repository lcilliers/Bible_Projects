# Audit Word — First Test Session Results
**Word:** Soul (registry 182) | **Date:** 2026-03-23 | **Run ID:** RUN-20260323_202200-AUDIT_WORD

---

## Coding Changes Completed This Session

| File | Change |
|---|---|
| `engine/audit_word.py` | Complete rewrite (Pre-A1 through A10) |
| `engine/constants.py` | `EXPECTED_SCHEMA_VERSION = "3.3.0"`, `AUDITED_SENTINEL = "AUDITED"` |
| `engine/migrate.py` | M12 added: `delete_flagged` columns + `wa_verse_term_links` + version bump |
| `engine/engine.py` | `--interactive`, `--extract-file` args; updated `run_audit_word` call |

---

## Migration Result

```
Current schema: 3.2.0  Target: 3.3.0
Applied: M01…M12 (all idempotent) ✓
Schema version now: 3.3.0
```

---

## Dry-Run Gap Report (soul, registry 182)

| Category | Count | Note |
|---|---|---|
| NEW_TERM | 0 | |
| STALE_TERM | 0 | |
| MISSING_MTI | 16 | Terms in DB with no mti_terms row |
| DB_ONLY_TERM | 3 | H4578, H5397, G5590 — 0 verses each |
| MISSING_ROOT | 0 | |
| MISSING_RELATED | 0 | |
| ORPHAN_RELATED | 0 | |
| MISSING_VERSE | 9 | New verse groups per sub-code |
| ORPHAN_VERSE | 0 | |
| STALE_VERSE | 748 | ALL existing verses — context_before/context_after were NULL in DB; populated from JSON |
| MISSING_VTL | 0 | |
| STALE_VTL | 63 | |
| **Total** | **839** | |

---

## Full Run Results (AUTO-APPROVE)

Applied categories: MISSING_MTI, DB_ONLY_TERM, MISSING_VERSE, STALE_VERSE, STALE_VTL

### A6 Verify
```
file_id=36  terms_active=24 (+3 delete_flagged)  verses_active=757  vtl=766
verses_inserted=9   verses_updated=748   verses_flagged=0
```

### A7 Meaning Handler
- 27 legacy meaning records migrated (`meaning` field → `wa_meaning_parsed`)
- 27 terms parsed

### A8 Quality Flags
- Full reset: DELETE all existing quality flags for file_id=36
- 60 quality flags written. Phase 2 flags NOT touched.

### A9 Audit Result: REVIEW
| Check | Result | Detail |
|---|---|---|
| WR-01 to WR-04, 06-07, 09-18, 20 | PASS (17) | |
| WR-05 | REVIEW | ID gaps in wa_term_inventory: (491,493), (493,1530) |
| WR-08 | REVIEW | Low verse/occurrence ratio: H4578/H5397/G5590 (0 active verses after delete_flag) |
| WR-19 | REVIEW | Parse warnings without NOTE flag for 17 terms |

Researcher notes on REVIEW items:
- WR-05: ID gaps are expected — terms registered with explicit IDs across sessions
- WR-08: H4578/H5397/G5590 have 0 verses because they were flagged DB_ONLY (not in include_codes)
- WR-19: Parse warnings — terms whose medium_def had low-confidence parsing. Will be addressed in researcher review phase.

### A10 Registry Update
```
last_automation_run : AUDITED
automation_run_id   : RUN-20260323_202200-AUDIT_WORD
phase1_status       : Complete
term_count          : 24
verse_count         : 757
approved_by         : PROVISIONAL
mti_terms count     : 28     ← was 12; 16 MISSING_MTI rows inserted
delete_flagged terms: 3
vtl rows            : 766
quality flags       : 60
```

---

## Issues Found and Resolved During Session

1. **MISSING_MTI handler absent** — `_apply_changes` had no code for `MISSING_MTI` gap category. Added INSERT INTO mti_terms for each gap item, plus entry in `_interactive_gate` prompts.
2. **748 STALE_VERSE** — Expected: `context_before`/`context_after` were NULL in all existing verse records (populated pre-M05). JSON provides these fields. The update populates them correctly.

---

## Post-Run State Summary

Soul (registry 182) is now **AUDITED** and marked **PROVISIONAL**:
- All 24 active terms present, 3 DB_ONLY terms flagged for archiving
- All 757 span-confirmed verses have correct context, target_word, span data
- 766 VTL rows linking verses to terms
- 60 quality flags re-derived from STEP data
- 27 meanings successfully migrated to parsed meaning tables
- 28 mti_terms rows for this registry (was 12)
- Researcher sign-off needed to change PROVISIONAL → APPROVED

---

## Next Steps

- Researcher review of WR-19 parse warnings (low-confidence meanings)
- Researcher review of DB_ONLY terms (H4578/H5397/G5590) — archive when ready
- Run audit_word for next word in queue
