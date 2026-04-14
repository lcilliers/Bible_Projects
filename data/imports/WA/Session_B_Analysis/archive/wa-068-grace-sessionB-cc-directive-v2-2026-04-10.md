# CC Directive — Registry 068 Grace — Term Reinstatement: H2594 and H2600
**File:** wa-068-grace-sessionB-cc-directive-v2-2026-04-10.md
**Date:** 2026-04-10
**Supersedes:** wa-068-grace-sessionB-cc-directive-v1-2026-04-10.md
**Change note:** v2 — Two corrections from v1: (1) god_as_subject operations repointed from wa_term_inventory (redundant field) to mti_term_flags (flag_code=GOD_AS_SUBJECT, flag_id=1) per CLAUDE.md Section 17.6. (2) owning_registry text field correction extended to H2433 and H2606, which carry the same FK mismatch as H2594 — all three affected by the same batch processing error.
**From:** Claude AI — Session B Stage 1
**Registry:** 068 — grace
**Source export:** wa-068-grace-complete-2026-04-10.json
**Analytical basis:** wa-068-grace-sessionB-observations-v2.0-2026-04-10.md

---

## What this directive covers

Two terms in Reg 068 (H2594 and H2600) have been confirmed by the researcher for reinstatement from delete to active status following Session B analytical review. A data integrity issue affecting three terms (H2433, H2594, H2606) with a corrupted owning_registry text field is also addressed.

---

## SECTION A — owning_registry text field correction

**Issue:** Three terms share the same FK mismatch: owning_registry text field = '212' but owning_registry_fk integer = 23. All three were processed together in one batch operation where the text field was incorrectly set. The FK (23) is the reliable value — it points correctly to Reg 23 (gracious/compassion), which is the correct owner for all three terms etymologically.

**Affected terms:**

| Strong | Transliteration | mti_id | Current text | Correct text | FK (authoritative) |
|---|---|---|---|---|---|
| H2433 | chin | 2333 | '212' | '23' | 23 |
| H2594 | cha.ni.nah | 2334 | '212' | '23' | 23 |
| H2606 | cha.nan.el | 2331 | '212' | '23' | 23 |

**Operations:**

1. `mti_terms` id=2333 (H2433): set owning_registry = '23'
2. `mti_terms` id=2334 (H2594): set owning_registry = '23'
3. `mti_terms` id=2331 (H2606): set owning_registry = '23'

H2433 and H2606 remain correctly deleted — this correction is data integrity only, no status change. H2594 is also corrected here; its reinstatement follows in Section B.

---

## SECTION B — Term reinstatement: H2594 (cha.ni.nah — favour)

**mti_id:** 2334
**Current status:** delete
**Verse corpus:** 1 verse — Jer 16:13 (wa_verse_records id=167213, currently delete_flagged=1)

**Why reinstated:**
The single verse — *"I will show you no favor"* — is a direct divine speech act naming the withdrawal of grace as an act of covenant judgment. This is the negative pole of the grace disposition: what it means for God to withhold favour. This is not duplicated anywhere in the active term corpus. It is analytically significant for Session B (the full dispositional range of grace) and Session D (cross-registry synthesis on divine favour and its conditions). The original exclusion was based on adequacy-of-coverage, which is insufficient when the term names something structurally distinct from what the active terms cover.

**Operations** (Section A operation 2 must be applied first):

1. `mti_terms` id=2334: set status = 'extracted_thin' (single verse corpus — correct status for ≤5 verses)
2. `wa_verse_records` id=167213: set delete_flagged = 0 (restore the sole verse)
3. `mti_term_flags`: insert row — mti_term_id=2334, flag_id=1, flag_code='GOD_AS_SUBJECT'
   Rationale: Jer 16:13 — God is the subject speaking in first person ("I will show you no favor")

**Verse Context consequence:**
H2594 is XREF — OWNER is Reg 23 (gracious/compassion). Check whether Reg 23 has active verse_context records for mti_term_id=2334. Report:
- If yes: Reg 68 inherits the classification via shared mti_term_id. verse_context_status for Reg 68 is unaffected.
- If no: verse_context_status for Reg 68 must be set to In Progress. Reg 68 is blocked pending Reg 23 classifying this term.

---

## SECTION C — Term reinstatement: H2600 (chin.nam — for nothing / gratuitously)

**mti_id:** 138
**Current status:** delete — no exclusion_reason was documented
**Verse corpus:** 31 verses, all currently delete_flagged=1

**Why reinstated:**
chin.nam names the structural logic of uncaused, unmerited giving — the without-cost, without-payment, without-merit quality that is the defining mechanism of grace. Key verses:
- Isa 52:3: *"You were sold for nothing, and you shall be redeemed without money"* — the without-payment logic of divine redemption stated directly
- Job 1:9: *"Does Job fear God for no reason?"* — Satan's assumption that all devotion is transactional, which grace overturns
- 2Sa 24:24 / 1Ch 21:24: David refusing to offer to God what costs him nothing — a gift without cost to the giver has no weight
- Eze 14:23, Mal 1:10: God as subject

The term is owned by Reg 73 (guilt), where it appears in the register of undeserved suffering. That is a different analytical face of the same term. Reinstatement in Reg 68 as XREF does not conflict with Reg 73's ownership — both registries analyse it from their respective perspectives. The original deletion was undocumented and was a processing decision rather than an analytical one.

**Operations:**

1. `mti_terms` id=138: set status = 'extracted' (31-verse corpus)
2. `wa_verse_records`: set delete_flagged = 0 for all 31 records:
   ids: 167138, 167135, 167134, 167148, 167131, 167132, 167133, 167130, 167129,
        167142, 167143, 167145, 167144, 167158, 167157, 167159, 167155, 167156,
        167149, 167150, 167154, 167151, 167152, 167153, 167139, 167140, 167141,
        167146, 167137, 167136, 167147
3. `mti_term_flags`: insert row — mti_term_id=138, flag_id=1, flag_code='GOD_AS_SUBJECT'
   Rationale: Eze 14:23 — "I have not done without cause all that I have done"; Mal 1:10 — God as subject of the without-cause offering context
4. `mti_terms` id=138: set exclusion_reason = 'REINSTATED 2026-04-10: Original deletion undocumented. Session B analytical review (Reg 068) found term names the structural mechanism of uncaused grace — the without-cost, without-merit quality that grace presupposes. Verse corpus restored. XREF from Reg 73 (guilt) where term appears in the undeserved-suffering register.'

**Verse Context consequence:**
H2600 is XREF — OWNER is Reg 73 (guilt). Check whether Reg 73 has active verse_context records for mti_term_id=138. Report:
- If yes: Reg 68 inherits the classification. verse_context_status for Reg 68 is unaffected.
- If no: verse_context_status for Reg 68 must be set to In Progress. Reg 68 is blocked pending Reg 73 classifying this term.

---

## Execution order

1. Section A — owning_registry text corrections (all three terms: H2433, H2594, H2606)
2. Section B — H2594 reinstatement (depends on Section A op 2 being applied first)
3. Section C — H2600 reinstatement (independent of Sections A and B)

---

## Reporting required

After applying all operations, report:
1. Confirmation that each operation succeeded, by section
2. Any integrity violations or unexpected states encountered
3. Verse Context status for H2594: does Reg 23 have active vc records for mti_term_id=2334?
4. Verse Context status for H2600: does Reg 73 have active vc records for mti_term_id=138?
5. Whether verse_context_status for Reg 068 remains Complete or must be set to In Progress

Do not produce a fresh export yet. Claude AI will review the Verse Context consequence report before determining next steps.
