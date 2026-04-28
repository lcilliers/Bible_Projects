# WA — CC Directive: Verse Context Sub-Process
**Registry 062 — fellowship**
Filename: wa-062-fellowship-dir-001-vc-subproc-v1-20260416.md
Date: 2026-04-16
Issued by: Claude AI — wa-sessionb-analysis-readiness-v1_2-20260416.md Step 1.5 Trigger 3
Requires researcher approval before execution.
Previous output: wa-062-preanalysis-v1-20260416.json (apply that patch first — see sequencing note)

---

## DIRECTIVE ID

**DIR-20260416-001**

---

## MOTIVATION

During Session B Stage 1 Analysis Readiness for Registry 062 (fellowship), Step 1.2 Section B Cross-check B2 identified four active OWNER terms that have active verse records in `wa_verse_records` but no `verse_context_group` records. These terms were not classified during the original Verse Context run. Per the Analysis Readiness instruction (Step 1.5 Trigger 3), a targeted Verse Context sub-process is required for all four before a fresh export can be produced and Stage 2 can begin. The sub-process must complete and its patch be applied before a fresh export is pulled.

**Terms requiring Verse Context classification:**

| strongs_number | transliteration | mti_term_id | occurrence_count | active verse_records |
|---|---|---|---|---|
| H2271 | chab.bar | 7572 | 1 | 1 |
| H2279 | cho.ve.ret | 7570 | 4 | 3 |
| H4225 | mach.be.ret | 7567 | 8 | 7 |
| H4226 | me.chab.be.rah | 7571 | 2 | 2 |

---

## SEQUENCING NOTE

Apply **wa-062-preanalysis-v1-20260416.json** (patch_id: `PATCH-20260416-062-PREANALYSIS-V1`) before executing this directive. Confirm OP-001 and OP-002 from that patch are applied (H2269 delete_flagged=1; G2842 phase2_flag soft-deleted) before proceeding to Step 1 below.

---

## SCOPE

Tables affected: `verse_context_group`, `verse_context`
Registry: 062 (fellowship)
Terms in scope: H2271 (mti_term_id=7572), H2279 (mti_term_id=7570), H4225 (mti_term_id=7567), H4226 (mti_term_id=7571)
No other tables are modified by this directive.
`word_registry.verse_context_status` is NOT changed by this directive — registry 062 is already `Complete`; this sub-process fills a gap within that state.

---

## STEPS

**Step 1 — Pre-construction verification.**

Confirm for each of the four terms:
- `mti_terms.status IN ('extracted', 'extracted_thin')` (per GR-DATA-001)
- `wa_term_inventory.delete_flagged = 0` and `term_owner_type = 'OWNER'`
- At least one `wa_verse_records` row with `delete_flagged = 0`
- Zero existing `verse_context_group` rows for this `mti_term_id`
- Zero existing `verse_context` rows for this `mti_term_id`

Also confirm that wa-062-preanalysis-v1-20260416.json has been applied: `wa_term_inventory.delete_flagged = 1` for term_inv_id=7733 (H2269).

Report results before proceeding. Halt and report to researcher if any check fails.

**Step 2 — Construct targeted Verse Context batch JSON.**

Construct a batch JSON for these four terms following wa-versecontext-instruction-v2_7-20260414.md Section 5.3 format. This is a targeted sub-process batch — not a programme-wide accumulation. Use the next available VCB batch ID from the programme sequence, or `VCB-062-SUB-001` if no sequence log is accessible. `existing_groups` array for each term is empty. Include all active verse records per term with full verse_text and span_strong_match (NULL values included as-is). Deliver batch JSON to Claude AI.

**Step 3 — Claude AI classification.**

Claude AI classifies all verses for the four terms under wa-versecontext-instruction-v2_7-20260414.md and produces a VERSECONTEXT patch file and observations file.

**Step 4 — Apply VERSECONTEXT patch and verify.**

Apply the VERSECONTEXT patch produced by Claude AI per the applicator rules in wa-patch-specification-v1_12-20260416.md Section 8. After application, verify consistency rules R1–R4 per Section 8.5.

**Step 5 — Produce fresh export.**

Re-export the complete word data for registry 062. Record the new version number and export date. Deliver to Claude AI for Step 1.6.

---

## OUTCOME REQUIRED

After execution of this directive, the following must be true in the database:

1. At least one `verse_context_group` row exists for each of the four `mti_term_id` values (7572, 7570, 7567, 7571), with `delete_flagged = 0`.
2. At least one `verse_context` row with `is_anchor = 1` exists for each group created, with `delete_flagged = 0`.
3. All `verse_context` rows for these terms satisfy consistency rules R1–R4 (wa-patch-specification-v1_12-20260416.md Section 8.5): zero violations.
4. `word_registry.verse_context_status` for registry 062 remains `'Complete'` — unchanged.
5. A fresh complete word export for registry 062 has been produced with a new version number.

---

## COMPLETION CONFIRMATION

CC must return the following confirmation block to Claude AI before Step 1.6 begins:

```
DIR-20260416-001 EXECUTION CONFIRMED

Pre-construction verification:
  wa-062-preanalysis-v1-20260416.json applied (patch_id PATCH-20260416-062-PREANALYSIS-V1): [YES/NO]
  H2271 mti_status: [value] | verse_records: [n] | existing groups before: 0
  H2279 mti_status: [value] | verse_records: [n] | existing groups before: 0
  H4225 mti_status: [value] | verse_records: [n] | existing groups before: 0
  H4226 mti_status: [value] | verse_records: [n] | existing groups before: 0

Batch JSON produced: [filename] | terms: 4 | verse_records: [n]

VERSECONTEXT patch applied: [filename]
Post-application group verification:
  H2271 (mti_id=7572): [n] group(s), [n] anchor verse(s)
  H2279 (mti_id=7570): [n] group(s), [n] anchor verse(s)
  H4225 (mti_id=7567): [n] group(s), [n] anchor verse(s)
  H4226 (mti_id=7571): [n] group(s), [n] anchor verse(s)

Consistency rules R1–R4: [PASS / FAIL — detail if FAIL]
word_registry.verse_context_status (reg 062): [value — must be 'Complete']

Fresh export produced: [filename] | version: [n] | export_date: [YYYYMMDD]
```

---

## GOVERNING RULES AND INSTRUCTIONS

- wa-global-general-rules-v2_4-20260416.json — GR-DIR-001 through GR-DIR-008, GR-DATA-001, GR-OBS-005, GR-PROC-003, GR-PROC-004
- wa-sessionb-cc-instructions-v3_4-20260416.md
- wa-versecontext-instruction-v2_7-20260414.md (CC roles: Sections 5, 8, 13, 14)
- wa-patch-specification-v1_12-20260416.md (Section 8 — Verse Context patch operations)

---

*wa-062-fellowship-dir-001-vc-subproc-v1-20260416.md*
*DIR-20260416-001 | Issued by Claude AI | Status: PENDING researcher approval*
