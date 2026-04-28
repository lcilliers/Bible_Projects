# CC Directives — Export Verification and Patch Applicator Update
## wa-global-cc-directives-v2-20260415.md
**Date:** 2026-04-15
**Governed by:** wa-global-general-rules-v2.2-20260415.json (GR-DIR-001 through GR-DIR-005, GR-PROC-003, GR-PROC-004)
**Previous directives:** wa-global-flag-remediation-directives-v1-20260415.md (DIR-001 through DIR-006 — all complete)
**Requires researcher approval before any directive is applied**

---

## DIR-20260415-007 — Data queries for Session B v5.0 first run pre-flight

**Motivation:** Three data points are needed before Session B v5.0 can begin on registry 023 (compassion). All three are read-only queries — no database changes. They resolve specific findings from the export cross-reference analysis (wa-global-sessionb-export-crossref-v1-20260415.md).

**Scope:** Read-only queries against bible_research.db. No writes.

**Query 1 — F-009: Unclassified verses from VCREPAIR errors**

PATCH-20260412-023-VCREPAIR-V1 recorded 23 errors. Determine whether any verse records for registry 023 OWNER terms currently have no corresponding verse_context record (i.e. are unclassified).

Return: count of wa_verse_records rows where delete_flagged=0, the associated mti_term has owning_registry_fk = 023, term_owner_type = 'OWNER', mti_terms.status IN ('extracted','extracted_thin'), AND no verse_context row exists for that verse_record_id + mti_term_id combination.

If count = 0: VCREPAIR errors were resolved. Session B v5.0 may proceed without Verse Context sub-process.
If count > 0: Session B v5.0 must trigger Verse Context sub-process before Stage 2.

**Query 2 — F-003: Open session_target=B flag description**

Return the full row from wa_session_research_flags where registry_id = 23 AND session_target = 'B' AND resolved = 0. Include all fields: id, flag_label, flag_code, category (via wa_quality_flag_types lookup), priority, strongs_reference, cross_registry_id, description, session_raised, raised_date.

**Query 3 — F-002: GOD_AS_SUBJECT terms in mti_term_flags**

Return all rows from mti_term_flags where flag_id = (SELECT id FROM phase2_flag_types WHERE flag_code = 'GOD_AS_SUBJECT') AND the associated mti_term has owning_registry_fk = 23. Include: mti_term_id, strongs_number (from mti_terms), transliteration, gloss, and the corresponding wa_term_inventory.id and wa_term_inventory.god_as_subject value.

**Completion confirmation — CC must return:**
1. Query 1 result: count of unclassified verses. If > 0, list the strongs_numbers affected.
2. Query 2 result: full row of the open B-flag.
3. Query 3 result: table of the 4 GOD_AS_SUBJECT terms with their wa_term_inventory.id and current god_as_subject field value.

---

## DIR-20260415-008 — Update apply_session_patch.py for Session B v5.0 write support

**Motivation:** Session B v5.0 writes analytical findings to `wa_session_b_findings` using all 18 fields (9 original + 9 lifecycle fields added via DIR-20260415-004) and writes entity links to `wa_finding_entity_links` (new table from DIR-20260415-005). The current `apply_session_patch.py` was written before these schema changes and cannot process operations against these fields or this table. Without this update, Stage 2 pass-close patches cannot be applied and Session B v5.0 cannot complete.

**Scope:** `scripts/apply_session_patch.py` — add support for new operations. No schema changes required — the tables and fields already exist.

**Required additions:**

**1. Support for all 18 fields on wa_session_b_findings inserts and updates**

Current applicator supports insert and update on `wa_session_b_findings` for the original 9 fields only. Extend to support all 18 fields:

New fields to add to insert/update support:
- `pass_ref` TEXT
- `study_segment` TEXT
- `delete_flag` INTEGER default 0
- `obsolete_reason` TEXT
- `obsolete_date` TEXT
- `superseded_by_id` INTEGER
- `related_finding_id` INTEGER
- `resolution_note` TEXT
- `thin_evidence` INTEGER default 0

**2. Support for finding supersession operation**

A new operation type is needed for the supersession pattern (Pass 5 language accuracy corrections): write a new finding, then set `delete_flag = 1`, `superseded_by_id`, `obsolete_reason`, and `obsolete_date` on the original finding. This must be atomic — both writes in a single transaction.

Operation type name: `supersede_finding`

Required fields:
- `original_finding_id` INTEGER — the id of the finding being superseded
- `obsolete_reason` TEXT — why it is being superseded
- `obsolete_date` TEXT — date of supersession
- `new_finding` OBJECT — the full new finding record (all 18 fields)

**3. Support for wa_finding_entity_links inserts**

New operation type: `insert_finding_entity_link`

Required fields per operation:
- `finding_id` INTEGER — FK to wa_session_b_findings.id. Must resolve before insert.
- `entity_type` TEXT — controlled: term / verse / group / dimension / registry / root_family / cross_registry
- `entity_id` INTEGER
- `entity_strongs` TEXT — nullable
- `raised_date` TEXT

Validation: `finding_id` must exist in `wa_session_b_findings` before insert. If the finding was inserted in the same patch (same transaction), use last_insert_rowid() resolution pattern — same approach as group_id resolution in VERSECONTEXT patches per patch spec Section 3.1.

**4. Extend null-exempt patch types**

The applicator currently rejects `session_b_status: null` for non-exempt patch types. Extend the null-exempt list to include a new patch type `SESSIONB_FINDINGS` — patches that write only to `wa_session_b_findings` and `wa_finding_entity_links` do not advance registry status and must carry `session_b_status: null`.

**Completion confirmation — CC must return:**
1. Confirm `apply_session_patch.py` now accepts all 18 fields on `wa_session_b_findings` insert and update operations — demonstrate with a test insert for registry 023 using a dummy finding with all 18 fields populated, then confirm the row exists and delete it.
2. Confirm `supersede_finding` operation type is supported — demonstrate with a test supersession on the dummy finding from step 1.
3. Confirm `insert_finding_entity_link` operation type is supported — demonstrate with a test entity link insert for the dummy finding, then confirm and delete.
4. Confirm `SESSIONB_FINDINGS` patch type is accepted with `session_b_status: null`.
5. State the updated version of `apply_session_patch.py`.

---

## Directive sequence

DIR-20260415-007 (queries) and DIR-20260415-008 (applicator update) are independent and may run in parallel.

DIR-20260415-007 results must be returned to Claude AI before Session B v5.0 first run begins.
DIR-20260415-008 must be confirmed complete before any Stage 2 pass-close patch is submitted.

---

*All directives require researcher approval before Claude Code begins. Confirmation outputs must be returned to Claude AI and the researcher before Session B v5.0 proceeds.*
