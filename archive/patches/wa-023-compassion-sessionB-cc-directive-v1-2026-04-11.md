# WA-023-Compassion — Session B CC Directive
**Filename:** wa-023-compassion-sessionB-cc-directive-v1-2026-04-11.md  
**Date:** 2026-04-11  
**Produced by:** Claude AI  
**Instruction:** WA-SessionB-Instruction-v4.6 (2026-04-10)  
**Stage:** Stage 1 — Remediation  
**Previous output ref:** wa-023-compassion-sessionB-observations-v3-2026-04-11.md

---

## Directive 1 — Root Family Correlation Signal Gaps

**Issue identified:** Consistency check 10b found four root codes present on active terms in Registry 23 (compassion) that span multiple registries but are absent from `correlations.root_families` in the export.

| Root code | Active terms in Reg 23 | Cross-registry evidence |
|---|---|---|
| SPLANCHN | G4697 splanchnizō (OWNER, Reg 23) | G4698 splanchnon is XREF in Reg 23, owned by Reg 111 (mercy) — same root spans two registries |
| OIKTEIRŌ | G3627 oikteirō (OWNER, Reg 23) | G3628 oiktirmos is XREF in Reg 23, owned by Reg 111 (mercy) — same root spans two registries |
| NICHUM | H5150 ni.chum (OWNER, Reg 23) | H5162G/H na.cham (XREF in Reg 23, owned by Reg 192 comfort) share this root |
| CHIN | H2587 chan.nun, H2594 cha.ni.nah (OWNER, Reg 23) | H2603A cha.nan (XREF in Reg 23, owned by Reg 68 grace) and H2580 chen (XREF in Reg 23, owned by Reg 68 grace) share this root |

**Action required:**

For each of the four root codes (SPLANCHN, OIKTEIRŌ, NICHUM, CHIN):

1. Query `wa_term_root_family` to confirm which registries carry this root code across the programme.
2. If registry_count ≥ 2: insert or update a `wa_root_family_correlation` record (or equivalent correlation table entry) so that the root family appears in the `correlations.root_families` signal for Registry 23's export.
3. If registry_count = 1 (single-registry root after investigation): record as single-registry — no correlation entry needed. Report back.

**Confirm:** After investigation, report the registry count and action taken for each root code.

---

## Directive 2 — Suffering Registry (Reg 214) — Boundary Note

**For information only — no action required at this stage.**

Registry 214 (suffering, C05) has been created and brought to Phase 1 Complete. Terms G3804 pathēma, G3663 homoiopathēs, G4777 sunkakopatheō, G4834 sumpatheō, G4841 sumpaschō, G3356 metriopatheō, G3805 pathētos, G4835 sumpathēs, G2553 kakopatheō, G3806 pathos appear in Reg 214's strongs_list.

Note: G4834, G4841, G3356, G3805, G4835 are currently OWNER-active in Reg 23 (compassion). Their OWNER/XREF classification in Reg 214 will be determined when Session A runs for Reg 214. No action on Reg 23 terms required now.

---

## Directive 3 — Programme-Wide Escalation: H0854 Extraction Anomaly

**Background:** H0854 *et* (Hebrew preposition "with", 932 occurrences) has been incorrectly extracted into at least 7 consecutive registries. In each case it has been reclassified to delete. The extraction anomaly suggests a systematic issue in the STEP extraction pipeline.

**Action requested:** Identify which registries have H0854 *et* in their strongs_list or terms array, confirm its status in each, and report the full count of affected registries. If a pipeline fix is feasible, propose the mechanism.

**Priority:** Low — does not block any current session. Record for programme-level review.

---

*CC directive produced under WA-SessionB-Instruction-v4.6 (2026-04-10). All actions require Claude Code execution. No database fields are changed by Claude AI assertion.*
