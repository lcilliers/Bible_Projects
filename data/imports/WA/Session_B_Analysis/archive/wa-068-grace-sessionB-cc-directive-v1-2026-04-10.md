# CC Directive — Registry 068 Grace — Term Reinstatement: H2594 and H2600
**File:** wa-068-grace-sessionB-cc-directive-v1-2026-04-10.md
**Date:** 2026-04-10
**From:** Claude AI — Session B Stage 1
**Registry:** 068 — grace
**Source export:** wa-068-grace-complete-2026-04-10.json
**Analytical basis:** wa-068-grace-sessionB-observations-v2.0-2026-04-10.md

---

## What this directive covers

Two terms in Reg 068 currently carry mti.status = delete. Session B analytical review found both deletions analytically unjustified. The researcher has confirmed reinstatement of both. This directive specifies all database operations required to reinstate them.

---

## Term 1 — H2594 (cha.ni.nah — favour)

**mti_id:** 2334
**Current status:** delete
**Verse corpus:** 1 verse — Jer 16:13 (wa_verse_records id=167213, currently delete_flagged=1)

**Why reinstated:**
The single verse — *"I will show you no favor"* — is a direct divine speech act naming the withdrawal of grace as an act of covenant judgment. This is the negative pole of the grace disposition: what it means for God to withhold favour. This is not duplicated anywhere in the active term corpus. It is analytically significant for Session B (the full dispositional range of grace) and Session D (cross-registry synthesis on divine favour and its conditions). The original exclusion was based on adequacy-of-coverage, which is insufficient when the term names something structurally distinct.

**Prior data issue to resolve first:**
The mti record has a conflict: owning_registry text field = '212' but owning_registry_fk integer = 23. Registry 23 (gracious/compassion) is the analytically correct owner. Registry 212 (pray) is incorrect. This must be corrected before the term is reinstated.

**Operations required:**

1. `mti_terms` id=2334: set owning_registry text = '23' (to match owning_registry_fk=23)
2. `mti_terms` id=2334: set status = 'extracted_thin' (single verse corpus — correct status)
3. `wa_verse_records` id=167213: set delete_flagged = 0 (restore the sole verse)
4. `wa_term_inventory` (or term record): set god_as_subject = 1 (Jer 16:13 — God is speaking in first person)

**Verse Context consequence:**
H2594 is XREF — Reg 23 (gracious/compassion) is the OWNER. Check whether Reg 23 has active verse_context records for mti_term_id=2334. Report:
- If yes: Reg 68 inherits the classification via shared mti_term_id. verse_context_status for Reg 68 is unaffected.
- If no: verse_context_status for Reg 68 must be set to In Progress. Reg 68 is blocked pending Reg 23 classifying this term.

---

## Term 2 — H2600 (chin.nam — for nothing / gratuitously)

**mti_id:** 138
**Current status:** delete — no exclusion_reason documented
**Verse corpus:** 31 verses, all currently delete_flagged=1

**Why reinstated:**
chin.nam names the structural logic of uncaused, unmerited giving — the without-cost, without-payment, without-merit quality that is the defining mechanism of grace. Key verses from the corpus:
- Isa 52:3: *"You were sold for nothing, and you shall be redeemed without money"* — the without-payment logic of divine redemption
- Job 1:9: *"Does Job fear God for no reason?"* — Satan's assumption that all devotion is transactional, which grace directly overturns
- 2Sa 24:24 / 1Ch 21:24: David refusing to offer to God what costs him nothing — the inner logic that a gift without cost has no weight
- Eze 14:23, Mal 1:10: God as subject

The term is owned by Reg 73 (guilt), where it appears in the register of undeserved suffering (hatred without cause, persecution without grounds). That is a different analytical face of the same term. Reinstatement in Reg 68 as XREF does not conflict with Reg 73's ownership — both registries can hold it as XREF from their respective perspectives. The original deletion was undocumented and appears to have been a processing decision rather than an analytical one.

**Operations required:**

1. `mti_terms` id=138: set status = 'extracted' (31-verse corpus — correct status)
2. `wa_verse_records`: set delete_flagged = 0 for all 31 records:
   ids: 167138, 167135, 167134, 167148, 167131, 167132, 167133, 167130, 167129,
        167142, 167143, 167145, 167144, 167158, 167157, 167159, 167155, 167156,
        167149, 167150, 167154, 167151, 167152, 167153, 167139, 167140, 167141,
        167146, 167137, 167136, 167147
3. `wa_term_inventory` (or term record): set god_as_subject = 1 (Eze 14:23, Mal 1:10 — God is subject)
4. `mti_terms` id=138: set exclusion_reason = 'REINSTATED 2026-04-10: Original deletion undocumented. Session B analytical review (Reg 068) found term names the structural mechanism of uncaused grace. Verse corpus restored. XREF from Reg 73 (guilt) where term appears in the undeserved-suffering register.'

**Verse Context consequence:**
H2600 is XREF — Reg 73 (guilt) is the OWNER. Check whether Reg 73 has active verse_context records for mti_term_id=138. Report:
- If yes: Reg 68 inherits the classification. verse_context_status for Reg 68 is unaffected.
- If no: verse_context_status for Reg 68 must be set to In Progress. Reg 68 is blocked pending Reg 73 classifying this term.

---

## Reporting required

After applying all operations, report:
1. Confirmation that each operation succeeded
2. Any integrity violations or unexpected states encountered
3. Verse Context status for H2594 (does Reg 23 have vc records for mti_term_id=2334?)
4. Verse Context status for H2600 (does Reg 73 have vc records for mti_term_id=138?)
5. Whether verse_context_status for Reg 068 remains Complete or must be set to In Progress

Do not produce a fresh export yet. Claude AI will review the Verse Context consequence report before determining next steps.
