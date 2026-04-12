# WA-023-Compassion — Session B CC Directive v2
**Filename:** wa-023-compassion-sessionB-cc-directive-v2-2026-04-11.md  
**Date:** 2026-04-11  
**Produced by:** Claude AI  
**Instruction:** WA-SessionB-Instruction-v4.6 (2026-04-10)  
**Stage:** Stage 2 — Post-analytical directives  
**Supersedes:** wa-023-compassion-sessionB-cc-directive-v1-2026-04-11.md (Directives 1–3 resolved)

---

## Directive 1 — Insert GOD_AS_SUBJECT mti_term_flags

**Background:** god_as_subject = 0 for all active OWNER terms in Reg 23 (automation gap). Pass 2 analysis identifies the following terms where God is the primary actor or subject across the verse corpus.

For each term listed below, insert a record into `mti_term_flags` with:
- `mti_term_id` = the MTI id for that term (query from mti_terms where strongs_number = X and owning_registry_fk = 23)
- `flag_id` = 1 (GOD_AS_SUBJECT)
- `source` = "Session B Pass 2 — wa-023-compassion-sessionB-brief-v1-2026-04-11"

**Terms requiring GOD_AS_SUBJECT flag:**

| Strong's | Transliteration | Basis |
|---|---|---|
| H2587 | chan.nun | 11/13 verses have God as subject; almost exclusively divine epithet |
| H2617B | che.sed | ~87/169 verses; predominantly divine steadfast love |
| H5150 | ni.chum | 2/3 verses; divine compassionate warmth (Hos 11:8, Zec 1:13) |
| G3627 | oikteirō | 1/1 verses; Rom 9:15 — exclusively divine sovereignty |
| G4697 | splanchnizō | Christological — Jesus in all Gospel uses; flag with note that subject is Christ |
| G4184 | polusplanchnos | 1/1 verses; Jas 5:11 — exclusively divine |
| H2551 | chem.lah | 1/2 verses; Gen 19:16 — divine mercy toward Lot |
| H7358 | re.chem | 9/25 verses; God as sovereign over the womb (opening, closing, consecrating) |

**Note on G4697 splanchnizō:** All Gospel uses have Jesus (God incarnate) as subject. The flag is appropriate but should carry a note: "Subject is Jesus Christ in all Gospel instances; one parable exception (Matt 18:27 — master)."

---

## Directive 2 — Insert SOMATIC flags

For each term listed below, insert a record into `mti_term_flags` or `wa_term_phase2_flags` as appropriate:

**SOMATIC_INNER_LINK (flag indicating term has a documented bodily dimension linked to inner experience):**

| Strong's | Transliteration | Basis |
|---|---|---|
| H7356A | ra.cham | Womb as the etymological and metaphorical origin of compassion |
| H7358 | re.chem | Anatomical womb — entire vocabulary of compassion originates from this term |
| G4697 | splanchnizō | Bowels/entrails as the named inner location of the compassion movement |

**BODY_INNER_EXPRESSION (flag indicating bodily movement expresses inner characteristic):**

| Strong's | Transliteration | Basis |
|---|---|---|
| H2347 | chus | Eye-language in 18/24 verses — the eye as seat/instrument of pity's expression or withholding |

---

## Directive 3 — Update sb_classification on word_registry

Update `word_registry` for registry no = 23:
- `sb_classification` = "Soul-body interface"
- `sb_classification_reasoning` = "Compassion originates at a somatic level (womb, gut, heart) and is felt as an inner-being orientation before producing outward action. The RACHAM/SPLANCHN vocabulary names a physically-located inner movement; the CHESED vocabulary names a settled character quality at the soul level. The soul-body interface classification applies primarily to the somatic sub-pattern; the characterological sub-pattern may require separate classification. Confidence: Medium. See WA-SessionB-Brief v1 Section 5."

---

## Directive 4 — Note on patch_specification (no action required)

The Stage 1 patch (PATCH-20260411-001-SESSIONB-V1) had its `update_registry` operation skipped by the applicator due to a format issue. The operation was applied manually. This should be noted in the patch_specification document for review in the next instruction revision cycle. No database action required — the patch was applied correctly.

---

*CC directive produced under WA-SessionB-Instruction-v4.6 (2026-04-10). All database actions require Claude Code execution.*
