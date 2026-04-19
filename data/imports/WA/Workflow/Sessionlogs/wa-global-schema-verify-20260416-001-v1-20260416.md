# WA — Schema Verification Report: DIR-20260416-001
**Filename:** wa-global-schema-verify-20260416-001-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Directive verified:** wa-global-dir-20260416-001-schema-catalogue-v1-20260416.md
**Schema version confirmed:** v3.9.0 (exported 2026-04-16)
**Previous output refs:**
- wa-global-dir-20260416-001-schema-catalogue-v1-20260416.md (directive)
- wa-global-schema-sessionb-changes-v1_1-20260416.md (design authority)

---

## Verification Result: PASS

All five schema changes specified in DIR-20260416-001 have been applied correctly. Schema version has advanced to v3.9.0. No data loss detected.

---

## SC-01 — `wa_session_b_findings`: 2 columns added

**Expected:** `status TEXT DEFAULT 'pending'`, `term_id INTEGER FK → mti_terms(id) ON DELETE SET NULL`

**Result: PASS**

| Column | Type | notnull | Default | FK | Match |
|---|---|---|---|---|---|
| `status` | TEXT | False | `'pending'` | — | ✓ |
| `term_id` | INTEGER | False | NULL | `mti_terms(id) ON DELETE SET NULL` | ✓ |

Row count: 171 — unchanged. All existing rows have `status = 'pending'` and `term_id = NULL` by default.

**One minor note:** The directive specified `status` as nullable (DEFAULT 'pending', no NOT NULL). The schema confirms this — `notnull=False`. This is consistent with the design intention; existing rows carry the default without constraint enforcement. No remediation needed.

---

## SC-02 — `wa_term_phase2_flags`: 2 columns added

**Expected:** `delete_flagged INTEGER DEFAULT 0`, `obsolete_reason TEXT NULL`

**Result: PASS**

| Column | Type | notnull | Default | Match |
|---|---|---|---|---|
| `delete_flagged` | INTEGER | False | 0 | ✓ |
| `obsolete_reason` | TEXT | False | NULL | ✓ |

Row count: 1,580 — unchanged.

---

## SC-03 — `wa_obs_question_catalogue`: table created

**Expected:** 12 columns; `obs_id` PK AUTOINCREMENT; `question_code` UNIQUE; `scope` DEFAULT 'universal'; `status` DEFAULT 'active'; `deleted` DEFAULT 0.

**Result: PASS**

| Column | Type | notnull | Default | Match |
|---|---|---|---|---|
| `obs_id` | INTEGER | False | NULL | ✓ PK AUTOINCREMENT |
| `question_code` | TEXT | True | NULL | ✓ UNIQUE (index confirmed) |
| `section` | TEXT | True | NULL | ✓ |
| `source_word` | TEXT | False | NULL | ✓ |
| `source_registry_no` | INTEGER | False | NULL | ✓ FK → word_registry(id) |
| `question_text` | TEXT | True | NULL | ✓ |
| `pattern_type` | TEXT | False | NULL | ✓ |
| `scope` | TEXT | True | `'universal'` | ✓ |
| `status` | TEXT | True | `'active'` | ✓ |
| `deleted` | INTEGER | True | 0 | ✓ |
| `date_added` | TEXT | True | NULL | ✓ |
| `catalogue_version` | TEXT | True | NULL | ✓ |

Unique index on `question_code` confirmed: `sqlite_autoindex_wa_obs_question_catalogue_1`.
Row count: 0 — correct; population is a separate step.

---

## SC-04 — `wa_finding_catalogue_links`: table created

**Expected:** 11 columns; `id` PK AUTOINCREMENT; FKs to `wa_session_b_findings(id)` and `wa_obs_question_catalogue(obs_id)`; UNIQUE `(finding_id, question_id)`; `status` DEFAULT 'suggested'; `delete_flagged` DEFAULT 0.

**Result: PASS**

| Column | Type | notnull | Default | Match |
|---|---|---|---|---|
| `id` | INTEGER | False | NULL | ✓ PK AUTOINCREMENT |
| `finding_id` | INTEGER | True | NULL | ✓ FK → wa_session_b_findings(id) |
| `question_id` | INTEGER | True | NULL | ✓ FK → wa_obs_question_catalogue(obs_id) |
| `coverage` | TEXT | False | NULL | ✓ |
| `status` | TEXT | True | `'suggested'` | ✓ |
| `pattern_type` | TEXT | False | NULL | ✓ |
| `mapped_date` | TEXT | False | NULL | ✓ |
| `validated_date` | TEXT | False | NULL | ✓ |
| `validated_by` | TEXT | False | NULL | ✓ |
| `session_b_note` | TEXT | False | NULL | ✓ |
| `delete_flagged` | INTEGER | True | 0 | ✓ |

Unique index on `(finding_id, question_id)` confirmed: `sqlite_autoindex_wa_finding_catalogue_links_1`.
Row count: 0 — correct.

---

## SC-05 — `wa_finding_entity_links`: 1 column added

**Expected:** `delete_flagged INTEGER NOT NULL DEFAULT 0`

**Result: PASS**

| Column | Type | notnull | Default | Match |
|---|---|---|---|---|
| `delete_flagged` | INTEGER | True | 0 | ✓ |

Row count: 0 — unchanged.

**Note:** The directive specified `NOT NULL DEFAULT 0`. The schema confirms `notnull=True` and `default=0` — this is consistent and correct.

---

## Row Count Summary

| Table | Expected rows | Actual rows | Match |
|---|---|---|---|
| `wa_session_b_findings` | 171 | 171 | ✓ |
| `wa_term_phase2_flags` | 1,580 | 1,580 | ✓ |
| `wa_finding_entity_links` | 0 | 0 | ✓ |
| `wa_obs_question_catalogue` | 0 | 0 | ✓ |
| `wa_finding_catalogue_links` | 0 | 0 | ✓ |

No data loss. No unexpected rows.

---

## Schema Version

Confirmed: **v3.9.0** (exported 2026-04-16). Advanced from v3.8.0 as specified.

---

## One Observation for the Record

The `wa_obs_question_catalogue` table as created does not include the `scope` field described in the design document's note distinguishing `scope` (analytical scope at creation: universal/word_specific) from `status` (operational state: active/word_specific/non_word). Checking the SQL confirms `scope` **is present** with `NOT NULL DEFAULT 'universal'`. This is correct — both fields exist and are distinct as intended.

---

## Verdict

**DIR-20260416-001 executed correctly and completely.** All five schema changes are present, correctly structured, and consistent with the design authority `wa-global-schema-sessionb-changes-v1_1-20260416.md`. Schema is at v3.9.0.

**T-SC is complete. Instruction drafting (T-02 onward) may proceed.**

---

*End of wa-global-schema-verify-20260416-001-v1-20260416.md*
*Directive verified: wa-global-dir-20260416-001-schema-catalogue-v1-20260416.md*
*Schema version at verification: v3.9.0*
