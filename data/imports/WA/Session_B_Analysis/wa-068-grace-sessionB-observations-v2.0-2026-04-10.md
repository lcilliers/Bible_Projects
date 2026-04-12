# WA-068 Grace — Session B Observations Log v2.0
**Registry:** 068 — grace | **Session:** 1 | **Stage:** 1 — Data Audit
**Date:** 2026-04-10 | **Instruction:** WA-SessionB-Instruction-v4.1-2026-04-10
**Input file:** wa-068-grace-complete-2026-04-10.json (export 2026-04-10T05:04:06Z, schema 3.8.0, script v1.1)
**Supersedes:** wa-068-grace-sessionB-observations-v1.0-2026-04-10.md (based on wrong export)

---

## SECTION 1 — Registry Block

| Field | Status | Finding |
|---|---|---|
| word / no / id | OK | grace / 68 / 68 |
| cluster_assignment | OK | C17 |
| verse_context_status | OK | Complete |
| session_b_status | NOTE | `Analysis Complete` — from prior session B v3.1 (2026-04-09). This is a pre-v4.0 run. session_b.dimensions is null despite this status — partial write from old session model. Will be written in Stage 2. |
| dim_review_status | GAP | null — Dimension Review sub-process required |
| dim_review_version | GAP | null |
| sb_classification | OK | `Spirit-soul interface` — present with reasoning |
| sb_classification_reasoning | OK | Present and substantive |
| unique_term_count | ERROR | stated=2, actual active OWNERs=5 |
| shared_term_count | ERROR | stated=11, actual active XREFs=3 |
| term_sharing_ratio | NOTE | 0.846 — stale, follows from wrong counts |
| strongs_list | ERROR | 5 delete-status entries present: H2603B, H2600, H2606, H2433, H2594 — must be removed |
| strongs_list counts | NOTE | Stated counts reflect full term corpus including deleted terms; active counts differ but this is a reporting characteristic of the strongs_list, not a per-entry error |
| dimensions | NOTE | `Relational/Social` — pre-review keyword label; will be updated by Dimension Review |
| description | OK | Substantive and adequate |

---

## SECTION 2 — Statistics Block

| Field | Stated | Actual | Status |
|---|---|---|---|
| term_count | 13 | 13 | OK |
| active_term_count | 13 | 8 | ERROR — correct=8 |
| owner_term_count | 5 | 5 | OK |
| xref_term_count | 8 | 3 | ERROR — correct=3 |
| verse_count | 412 | 412 | OK |
| active_verse_count | 194 | 194 | OK |
| verse_context_group_count | 17 | 17 | OK |
| verse_context_record_count | 375 | 318+57=375 | OK |
| anchor_verse_count | 26 | 26 | OK |
| dimension_index_count | 11 | 11 | OK |
| research_flag_count | 5 | 5 | OK |
| session_b_finding_count | 0 | 0 | OK |
| cross_registry_link_count | 0 | 0 | OK (Session D) |
| correlation_xref_pair_count | 5 | 5 | OK |
| correlation_cooccurrence_pair_count | 48 | 48 | OK |
| correlation_dimension_pair_count | 0 | 0 | OK (expected — dim_review not run) |
| correlation_root_family_count | 1 | 1 | OK |
| correlation_shared_anchor_count | 9 | 9 | OK |

---

## SECTION 3 — Terms

Active terms (8): G5483, G5485, G5487 (OWNER Greek), H2580, H8469 (OWNER Hebrew), H2587, H2603A, H8467 (XREF Hebrew)
Deleted terms (5): H2433, H2594, H2600, H2603B, H2606

| Strong | Status | Owner | god_as_subject | somatic_link | Root | Finding |
|---|---|---|---|---|---|---|
| G5483 charizō | extracted | OWNER | 1 | 0 | CHAR ✓ | OK |
| G5485 charis | extracted | OWNER | 1 | 0 | CHAR ✓ | OK |
| G5487 charitoō | extracted | OWNER | 1 | 0 | CHAR ✓ | OK |
| H2580 chen | extracted | OWNER | 1 | 1 | CHEN ✓ | OK |
| H8469 ta.cha.nun | extracted_thin | OWNER | 0 | 1 | CHEN ✓ | OK |
| H2587 chan.nun | extracted | XREF | 1 | 0 | NONE | **GAP: missing CHEN root_family record** |
| H2603A cha.nan | extracted | XREF | 1 | 1 | NONE | **GAP: missing CHEN root_family record** |
| H8467 te.chin.nah | extracted_thin | XREF | 0 | 1 | NONE | **GAP: missing CHEN root_family record** |
| H2433 chin | delete | XREF | — | — | — | In strongs_list — **ERROR** |
| H2594 cha.ni.nah | delete | XREF | — | — | — | In strongs_list — **ERROR** |
| H2600 chin.nam | delete | XREF | — | — | — | In strongs_list — **ERROR** |
| H2603B cha.nan | delete | XREF | — | — | — | In strongs_list — **ERROR** |
| H2606 cha.nan.el | delete | XREF | — | — | — | In strongs_list — **ERROR** |

meaning / meaning_numbered: All null or PROSE_ONLY. No numbered sense structure. Stage 2 Pass 1 will address.

---

## SECTION 4 — Verse Context Groups

17 groups. All have context_descriptions. All have ≥1 anchor. classification_counts match actual counts for all 17 groups. OK structurally.

57 unassigned records: set_aside_reason=NULL for all. Pre-VCB-031 known gap per VC Instruction v2.5 Section 2.2 — no action required.

6 VC groups without DI entries — all XREF-owned (see Section 5 and 10c).

---

## SECTION 5 — Dimension Index

11 entries. All descriptions match VC group descriptions. All have KEYWORD_WEAK confidence. All have dominant_subject=null.

6 VC groups without DI entries: 2325-001, 2325-002, 2330-001, 984-001, 985-001, 985-002.
All 6 are XREF-owned: groups 2325-* and 2330-001 belong to reg 23 (H2603B/H2587); groups 984-001, 985-* belong to reg 111 (H2603A/H8467). Reg 68 has no authority over these — no DI entries to be created here. Correct per DR Instruction Section 2.1.

Note: H2603B now has status=delete in this export (was extracted_thin in Apr 9 export). Groups 2325-001 and 2325-002 are owned by reg 23 via H2603B but that term is deleted here. These groups remain visible via mti_term_id sharing — structurally correct.

Dimension Review required: all 11 OWNER-term groups, KEYWORD_WEAK → CLAUDE_AI.

---

## SECTION 6 — Session B Block

session_b.dimensions: null — not yet written (prior session used old model).
session_b.findings: [] — empty.
NOTE: session_b_status = `Analysis Complete` from prior session. Will be superseded when Stage 2 writes new session_b.dimensions data.

---

## SECTION 7 — Session D Block

Zero pointer flags, zero runs. OK.

---

## SECTION 8 — Research Flags

5 flags, all PH2_CROSS_REF_ENRICHMENT, all session_target=D, all unresolved. These are carried forward to Session D — no action in Stage 2 beyond noting them. Flags:
- PH2-068-001 (HIGH): Grace-Forgiveness formal connection via G5483 charizō
- PH2-068-002 (HIGH): Grace-Chesed boundary question via H2580 chen
- PH2-068-003 (HIGH): Grace-Repentance sequence via H8469/H2587
- PH2-068-004 (MEDIUM): Grace-Identity formation via G5485 1Cor 15:10
- PH2-068-005 (MEDIUM): Grace-Lament connection via H8469 weeping-supplication complex

---

## SECTION 9 — Cross-Registry Links

Zero. Expected — populated in Session D.

---

## SECTION 10 — Consistency Checks

**10a Root family completeness:**
3 active terms missing CHEN root_family records: H2587, H2603A, H8467. All others correct.
Root gloss mismatch on CHAR family: correlations.root_families shows root_gloss=None for CHAR; term root_family records show root_gloss='grace'. Minor inconsistency — the correlations block derives root_gloss from a different source. Flag for CC.

**10b Root family correlation signal:**
CHAR root appears in correlations.root_families with registry_count=2 (regs 4 and 68). Correct.
CHEN root does not appear in correlations.root_families — this is because H2587, H2603A, H8467 are missing their CHEN records; once added, CHEN signal may fire if CHEN root spans multiple registries. Not an error in the current state — consequence of 10a gap.

**10c DI vs VC group consistency:**
11 DI entries match 11 OWNER-term VC groups. 6 XREF-owned groups have no DI entry — correct per programme architecture. Descriptions match exactly for all 11.

**10d Anchor verse consistency:**
anchor_verse_count=26 matches actual. All 17 groups have ≥1 anchor. OK.

**10e Correlation xref signal vs term inventory:**
CRITICAL: All 4 xref_sharing entries for pray/mercy/compassion/guilt include delete-status terms in shared_strongs. Current stated shared_term_count per partner: pray=10, mercy=10, compassion=10, guilt=9. Active-only count: 5, 5, 5, 5.
- H2600, H2606, H2433, H2594, H2603B are all delete-status but included in these signals.
- Per Session B Instruction Section 10e: these terms should not be generating xref signals after deletion. This is a corruption of the correlation signal — the shared_term_counts are inflated and the shared_strongs lists are inaccurate.
- CC directive required: recompute xref_sharing after excluding delete-status terms from the signal.

**10f Statistics correlation counts vs correlations block:**
All five fields match exactly. OK.

**10g Session B classification consistency:**
sb_classification present. sb_classification_reasoning present. session_b.dimensions null — partial write gap from old session model. Noted.

---

## AUDIT SUMMARY

### Confirmed OK
verse_context_status, cluster_assignment, verse/anchor counts, correlation count fields (statistics vs actual), all 17 group classification_counts, all 11 DI descriptions, all 5 research flags, sb_classification + reasoning, cross_registry_links (expected zero)

### Gaps requiring field-level patch

| # | Field | Current | Correct | Action |
|---|---|---|---|---|
| 1 | strongs_list | 13 entries incl. 5 delete | Remove H2433, H2594, H2600, H2603B, H2606 | UPDATE registry |
| 2 | statistics.active_term_count | 13 | 8 | UPDATE |
| 3 | statistics.xref_term_count | 8 | 3 | UPDATE |
| 4 | unique_term_count | 2 | 5 | UPDATE |
| 5 | shared_term_count | 11 | 3 | UPDATE |
| 6 | root_family H2587 | none | CHEN / favor | INSERT |
| 7 | root_family H2603A | none | CHEN / favor | INSERT |
| 8 | root_family H8467 | none | CHEN / favor | INSERT |

### Consistency failures requiring CC directive

| # | Check | Issue | Action |
|---|---|---|---|
| 9 | 10e | xref_sharing includes 5 delete-status terms across 4 partner registries — shared_term_counts inflated | CC directive: recompute xref_sharing excluding delete-status terms; update correlation_xref_pair_count if any partner drops to 0 |
| 10 | 10a/10b | correlations.root_families CHAR root_gloss=None vs term records root_gloss='grace' | CC directive: update root_gloss in correlation record to 'grace' |

### Dimension Review required
Yes — all 11 OWNER-term groups: KEYWORD_WEAK → CLAUDE_AI, dominant_subject null.

### Root family gaps
H2587, H2603A, H8467 — CHEN root code missing.

### Session D flags carried forward
5 PH2_CROSS_REF_ENRICHMENT flags — no Stage 2 action needed, noted for Session D.

---

## ADDENDUM — Analytical Review of H2600 and H2594 deletion decisions

**Date:** 2026-04-10 | Added following researcher challenge of deletion assumptions

### H2600 (chin.nam — for nothing / gratuitously) — 31 verses

**What the term actually does:**
chin.nam is an adverb derived from the chen/chanan root (same CHEN root family as H2580 and H8469). Its semantic range covers: *freely, for nothing, gratuitously, without cause, without merit, undeservedly*.

Reading across the 31 verses, it operates in two analytically distinct registers:

**Register 1 — structural mechanism of grace:** Isa 52:3 is the key verse: *"You were sold for nothing, and you shall be redeemed without money."* The without-cost, without-payment quality of God's redemptive act is precisely what grace names. Mal 1:10 ("fire on my altar in vain") and Eze 14:23 ("I have not done without cause") both show God as subject. David's statement in 2Sa 24:24 / 1Ch 21:24 — refusing to offer to God what costs him nothing — reveals the inner-being logic of gift: a gift without cost to the giver has no weight. This is the structural mirror of grace.

**Register 2 — causeless hostility:** Psa 35:7, 69:4, 109:3, 119:161 — persecution and hatred without cause. Job 1:9 — Satan's question "Does Job fear God for no reason?" — which presupposes that all devotion is transactional. This directly engages the inner-being question: what does it mean to love or fear God *without* cause, without calculation?

**Deletion assessment:** The deletion was recorded with no exclusion_reason. The term was filed under Reg 73 (guilt) because gratuitous suffering is part of its range. But chin.nam names the **structural logic of uncaused giving and receiving** — which is precisely what the grace registry studies. The inner-being content is substantial across 31 verses. The deletion appears to have been a processing decision rather than an analytical one.

**Reinstatement assessment:** Warranted. The term belongs in the grace analytical picture as an XREF from its OWNER (Reg 73). Its 31 verses need Verse Context classification from the grace perspective.

### H2594 (cha.ni.nah — favour) — 1 verse, delete_flagged=1

**The single verse:** Jer 16:13 — *"I will show you no favor."*

This is God explicitly withholding favour as an act of covenant judgment. The exclusion argument was "adequately covered by chen/chanan." But this verse does something chen and chanan do not do in their corpus — it names the **withdrawal** of grace as a divine act. The negative pole of the disposition. It engages the question: what does it mean for the inner being when grace is withdrawn? And behind that: what is the inner-being structure of a God who can both give and withhold favour?

**Additional finding:** The single verse record (vid=167213, Jer 16:13) has delete_flagged=1 — the verse itself has been removed from the active set, not just the term. Reinstatement requires both the mti status change and the verse record restoration.

**Additional finding:** H2594's mti record has a data conflict: owning_registry (text field) = '212' but owning_registry_fk (integer FK) = 23. Registry 23 is gracious/compassion; Registry 212 is pray. This conflict must be resolved by CC before reinstatement can proceed correctly.

**Reinstatement assessment:** Warranted despite single occurrence. The verse is analytically significant — it is not incidental usage but a direct divine speech act about the withdrawal of favour. The verse record must be restored alongside the mti status.

### Pipeline consequences if researcher confirms reinstatement

| Item | H2594 | H2600 |
|---|---|---|
| mti.status change | delete → extracted_thin | delete → extracted |
| Verse record restoration | vid=167213 delete_flagged=1 → 0 | Not needed — 31 verses present |
| verse_context_status reg 68 | Complete → In Progress | Complete → In Progress |
| Verse Context classification | OWNER reg 23 must classify H2594 | OWNER reg 73 must classify H2600 |
| Root family | CHEN record needed | CHEN record needed |
| owning_registry_fk conflict | Must be resolved first | N/A |
| strongs_list | Re-add with correct count | Re-add with count=31 |
| statistics updates | active_term_count +1, xref_term_count +1 | active_term_count +1, xref_term_count +1 |
| god_as_subject | Jer 16:13 = God as subject → set to 1 | Eze 14:23, Mal 1:10 = God as subject → set to 1 |

**Critical dependency:** Both terms are XREFs — Verse Context is delivered by their OWNER registries (23 and 73). Reg 68 cannot complete VC for these terms independently. If the OWNER registries have not yet classified these terms, reg 68's verse_context_status remains In Progress until they do.

**This materially changes the action plan.** Reinstatement is not a field patch — it triggers upstream dependencies in two other registries.

---

## INSTRUCTION AMENDMENT NOTE — Session B Audit: strongs_list handling

**Date:** 2026-04-10
**Triggered by:** Session B audit of Reg 068 grace — strongs_list incorrectly flagged delete-status terms as errors
**Target instruction:** WA-SessionB-Instruction-v4.1 — Section 1 (Registry block audit, strongs_list field)
**Amendment type:** Clarification + new mandatory audit step

### What the current instruction says
Section 1 directs: check strongs_list — "Flag any deleted term still listed."

### What is actually correct
CC is instructed to include deleted term records in the complete Session B export so that Claude AI can examine them during validation. The presence of delete-status terms in the strongs_list is therefore expected and correct — it reflects the full term inventory including deleted terms, which is by design.

### Required amendment — two points

**Point 1 — Consistency check (existing check, corrected framing):**
When auditing the strongs_list, do not flag delete-status terms as errors. Instead, verify consistency: confirm that every term in the strongs_list has a corresponding entry in the terms array, and that the mti.status recorded there matches the expected active or delete state. The presence of delete-status terms in the strongs_list is not a gap — it is the intended state for a Session B export.

**Point 2 — New mandatory audit step — deletion justification review:**
For every term in the strongs_list with mti.status=delete, Claude AI must read the term's actual semantic content and verse corpus and make an independent analytical judgement on whether the deletion is justified. This is not a checkbox. The questions to answer for each deleted term are:

1. Does this term name an inner-being characteristic, mechanism, or structural property relevant to the registry being studied — even if it does so indirectly?
2. Does the exclusion_reason field contain a documented analytical rationale? If the exclusion_reason is null, the deletion must be treated as unreviewed and examined with greater scrutiny.
3. Could the inner-being content this term carries be relevant to Session D cross-registry synthesis, even if it does not fit the registry's primary analytical face?
4. Is the deletion based on semantic irrelevance, or on adequacy-of-coverage by other terms? Adequacy-of-coverage is a weaker justification and should be challenged when the term names something structurally distinct.

If the review finds that a deleted term carries analytically significant inner-being content that is not fully covered by the active terms — the term must be flagged for researcher review with a full analytical statement, not simply accepted as deleted.

### What this session found applying this discipline
- H2433 (chin — beauty): deletion confirmed — aesthetic register only, no inner-being dispositional content, verse delete_flagged
- H2603B (cha.nan — to be loathsome): deletion confirmed — homograph with no corpus, all verses resolve to H2603A
- H2606 (cha.nan.el — Tower of Hananel): deletion confirmed — proper noun, geographical reference only
- H2600 (chin.nam — for nothing/gratuitously): **deletion challenged** — names the structural mechanism of uncaused giving; analytically significant for grace; exclusion_reason null; reinstatement warranted
- H2594 (cha.ni.nah — favour): **deletion challenged** — single verse names divine withdrawal of favour; names the negative pole of the grace disposition; analytically significant; reinstatement warranted

### Action required on instruction
WA-SessionB-Instruction-v4.1 Section 1 strongs_list audit to be updated with:
- Correction of the "flag deleted terms" rule to "verify consistency, presence expected"
- Addition of the deletion justification review as a mandatory step with the four questions above

This amendment applies from the next Session B operation onward.

---

## ADDENDUM — CC Directive v2 Execution Report and VC Consequence Decision

**Date:** 2026-04-10

### CC execution confirmed

All operations from Directive v2 applied without integrity violations:
- Section A: owning_registry text corrected on H2433 (mti 2333), H2594 (mti 2334), H2606 (mti 2331) — all now '23'
- Section B: H2594 reinstated — status=extracted_thin, Jer 16:13 (vr 167213) restored, GOD_AS_SUBJECT flag inserted
- Section C: H2600 reinstated — status=extracted, all 31 verses restored, GOD_AS_SUBJECT flag inserted, exclusion_reason recorded
- Active verses for Reg 68: 194 → 226 (+32: 1 from H2594, 31 from H2600)

### Verse Context consequence — decision

Neither OWNER registry has verse_context records for the reinstated terms:
- H2594 (mti 2334): Reg 23 has 0 active vc records — no classification to inherit
- H2600 (mti 138): Reg 73 has 0 active vc records — no classification to inherit

Per VC Instruction v2.5 Section 0.2 and Section 13.2, a registry is Complete only when all its XREF terms have an OWNER that has been classified. This condition is no longer met for Reg 68.

**Instruction to CC:** Set verse_context_status for Reg 068 = 'In Progress'.

**Important qualification for Session B Stage 2:** This status change reflects a dependency on upstream work in Regs 23 and 73 — it is not a quality failure in Reg 68's own classification. All five OWNER terms for Reg 68 have complete and sound VC classification. Session B Stage 2 may proceed against the existing OWNER term corpus. H2594 and H2600 will be incorporated into the analytical picture when Regs 23 and 73 complete VC for those terms. This will be noted in the Stage 2 analytical brief as an open dependency.

---

## ADDENDUM — Directive v3 Execution Confirmed | Gap 1 Closed

**Date:** 2026-04-10

CC confirms:
- verse_context_status for Reg 068: In Progress ✓
- Fresh export produced: wa-068-grace-complete-2026-04-10.json
- 226 active verses (up from 194) ✓
- H2594 + H2600 reinstated ✓
- owning_registry text corrected on H2433, H2594, H2606 ✓
- verse_context_status = In Progress ✓
- GOD_AS_SUBJECT flags on mti 2334 and 138 ✓
- Correlations layer included ✓

**Gap 1 (strongs_list — deletion justification review): CLOSED**

Next: Load fresh export and proceed to Gap 2.

---

## ADDENDUM — Gaps 2–5 retracted | Instruction correction

**Date:** 2026-04-10

Gaps 2–5 from the original audit (active_term_count, xref_term_count, unique_term_count, shared_term_count) are retracted. CC confirmed these were not errors.

**active_term_count = 13:** Correct. Counts wa_term_inventory.delete_flagged = 0 across all 13 inventory records. The mti_terms.status = delete on five terms is a programme-wide deletion flag whose cascade to the inventory table is a deferred operation in the Session B process. The extract script counts inventory-level activity, not MTI-level status. These are two distinct things.

**xref_term_count = 8:** Correct. Same logic — 8 XREF terms with delete_flagged = 0 in the inventory.

**unique_term_count / shared_term_count:** These fields do not exist in the statistics block of the extract. They are registry-level fields. The audit should not have treated them as statistics block fields.

**Instruction amended:** WA-SessionB-Instruction-v4.3 corrects Section 2 (statistics verification logic for active_term_count and xref_term_count) and Section 1 (unique_term_count / shared_term_count correctly identified as registry-level fields not in the statistics block).

---

## ADDENDUM — Gaps 6–8 closed | Root family CC report notes

**Date:** 2026-04-10

**Gaps 6–8 confirmed closed:** CHEN root_family records inserted for H2587 (ti=5589), H2603A (ti=5586), H8467 (ti=5588). root_family_count will be 8 on next export (was 5).

**CC notable finding — pre-backfill record:**
CC identified an older CHEN record (id=258) for H2600 at term_inv_id=285 with lang=None, gloss=None. This belongs to H2600's entry in a different registry's inventory — not Reg 068's (Reg 068 has H2600 at ti=5587). The old record is a pre-backfill artefact with incomplete data. It is not in Reg 068's scope and does not affect this session. Flagged for future programme-wide audit: incomplete root_family records with lang=None, gloss=None from pre-backfill processing should be corrected.

**Deferred from Directive v4 — now actionable:**
H2594 (ti=5592) and H2600 (ti=5587) in Reg 068 both require CHEN root_family records. Reinstatement is confirmed stable. To be addressed in next directive (Gap 9 or dedicated root directive).

---

## ADDENDUM — Instruction amendment v4.3 | Statistics audit logic corrected

**Date:** 2026-04-10
**Instruction updated:** WA-SessionB-Instruction-v4.3-2026-04-10

Two corrections made to Session B audit instruction following researcher challenge of gaps 2–5:

**Correction 1 — active_term_count and xref_term_count (Section 2 statistics block):**
Previous instruction directed Claude AI to verify these counts against mti_terms.status. This is wrong. The extract script counts wa_term_inventory.delete_flagged = 0 — inventory-level activity. A term can have mti_terms.status = delete while remaining active in the inventory because the cascade has not been applied. Claude AI must not subtract mti-deleted terms from these counts. Instruction rewritten with explicit note on the deferred cascade.

**Correction 2 — unique_term_count / shared_term_count (Section 1 registry block):**
Previous instruction directed Claude AI to verify these as statistics block fields. They do not exist in the statistics block — they are registry-level fields. Instruction corrected: note their values only, do not audit them as statistics fields.

---

## ADDENDUM — Directive v5 issued | Root family records for reinstated terms

**Date:** 2026-04-10
**Directive:** wa-068-grace-sessionB-cc-directive-v5-2026-04-10.md

**Purpose:** Insert CHEN root_family records for H2594 and H2600 — both reinstated in Directive v2 and confirmed stable. Deferred from Directive v4 at that time pending reinstatement stability.

**Operations specified:**
- H2594 (cha.ni.nah): INSERT at term_inv_id=5592, root_code=CHEN, root_language=Hebrew, root_gloss=favor
- H2600 (chin.nam): INSERT at term_inv_id=5587, root_code=CHEN, root_language=Hebrew, root_gloss=favor

**Note included in directive:** Pre-existing CHEN record (id=258, ti=285) belongs to H2600 in a different registry's inventory. Reg 068's H2600 entry is ti=5587. CC must insert at ti=5587 only.

**Expected state after application:** All seven active Hebrew CHEN-root terms in Reg 068 carry CHEN records: H2580, H8469 (existing); H2587, H2603A, H8467 (Directive v4); H2594, H2600 (Directive v5). root_family_count expected = 10.

**Fresh export requested** after Directive v5 is confirmed — to capture all changes from Directives v2 through v5.

**Status:** Directive issued — awaiting CC confirmation.

---

## ADDENDUM — Gap 9 retracted | xref_sharing corruption finding was wrong

**Date:** 2026-04-10

Gap 9 (xref_sharing includes MTI-deleted terms — shared_term_counts inflated) is retracted.

**Reason:** The same logic error that produced gaps 2–5 applied here. The xref_sharing signal is built from inventory-active terms (wa_term_inventory.delete_flagged=0), not from mti_terms.status. All 13 inventory records have delete_flagged=0 including H2433, H2603B, and H2606 whose mti cascade has not been applied. The shared_term_counts of 10/10/10/9 correctly reflect the inventory-active state.

**Post-reinstatement note:** H2594 and H2600 are now inventory-active (reinstated). The xref_sharing signal may need recomputing after the fresh export from Directive v5 to confirm the reinstated terms appear correctly in shared_strongs where applicable. This is a verification check on the fresh export, not a correction.

**No directive required for this gap.**

---

## ADDENDUM — Gap 10: CHAR root_gloss null — investigation required

**Date:** 2026-04-10

**Finding:** correlations.root_families shows CHAR root_gloss = null, registry_count = 2, spanning Reg 4 (anger) and Reg 68 (grace). Term root_family records in Reg 68 carry root_gloss = 'grace' on G5483, G5485, G5487.

**Assessment:** The null is the extract script's correct response to a conflict between two registries sharing the CHAR root code with different gloss values. This is not a simple correction. Greek etymology does not support anger and grace sharing a root — the grace cluster derives from χαρ- (joy/favour), unrelated to anger vocabulary. The CHAR root code assignment on Reg 4 may be an error.

**Action:** Investigation directive issued to CC (Directive v6) — querying Reg 4 for CHAR root records before any correction is made. No database changes until investigation is reported.

**Instruction update:** WA-SessionB-Instruction-v4.4 updates check 10a (root_gloss null in correlations is not automatically an error when registry_count > 1 — investigate cause first) and check 10e (xref signal built on inventory-level delete_flagged, not mti_terms.status — corrects same error as v4.3).

**Status:** Directive v6 issued — awaiting CC investigation report.

---

## ADDENDUM — Gap 10 revised: CHAR root query issued | Programme note for Reg 4

**Date:** 2026-04-10

**Directive v6 revised:** Now a query request only — CC to return Reg 4 CHAR root_family records. No database changes pending assessment of results.

**Programme note — to be carried to Reg 4 (anger) Session B:**

> During Reg 068 (grace) Session B Stage 1, the CHAR root code was found spanning both Reg 068 and Reg 4 (anger) in the correlations.root_families signal. Reg 068's CHAR records carry root_gloss = 'grace'. The correlations block shows root_gloss = null — indicating the extract script found a gloss conflict across the two registries. Greek etymology does not support anger and grace sharing a root (grace cluster derives from χαρ- meaning joy/favour; anger vocabulary derives from unrelated roots). When Reg 4 reaches Session B Stage 1, the CHAR root_family records on Reg 4's terms must be examined and the assignment verified. If the CHAR code was incorrectly applied to Reg 4 terms, it should be corrected on those terms and the correlations block for both registries recomputed. Cross-reference: wa-068-grace-sessionB-observations-v2.0-2026-04-10.md Gap 10.

**Status:** CC query (Directive v6) issued — awaiting result before any further action on gap 10.

---

## ADDENDUM — Gap 10 closed | CHAR root code collision confirmed | Programme note updated

**Date:** 2026-04-10

### CC query result — Reg 4 CHAR records

Three terms in Reg 4 (anger) carry CHAR: H2734 cha.rah (to be incensed), H2740 cha.ron (burning anger), H8474 ta.cha.rah (to contend). All three have root_gloss = None and root_language = None — pre-backfill records, never enriched. All are from Hebrew חרה (charah — to burn, be angry).

### Diagnosis confirmed: root code collision

CHAR has been applied to two entirely unrelated etymological families:
- Reg 68 (grace): Greek χάρις (charis) — χαρ- root meaning joy/favour. Records fully enriched: root_gloss='grace', root_language='Greek'.
- Reg 4 (anger): Hebrew חרה (charah) — to burn/be angry. Records not enriched: root_gloss=None, root_language=None.

The correlations.root_families entry (root_gloss=null, registry_count=2) is the extract script's correct response to this collision — honest null, not an error.

### Reg 68 action: none required

Reg 68's CHAR records are fully correct. No changes needed on the Reg 68 side.

### Resolution path

1. Reg 4 Session B Stage 1 must assign a new distinct root code to H2734, H2740, H8474 — separating the Hebrew anger root from the Greek grace root. Proposed code: CHARAH (or CHAR-H), root_gloss='burn/anger', root_language='Hebrew'.
2. Once Reg 4's records are corrected, correlations.root_families for CHAR will recompute to registry_count=1 (Reg 68 only) with root_gloss='grace'.
3. No action required in Reg 68 Session B.

**Gap 10: CLOSED from Reg 68's perspective. Resolution deferred to Reg 4 Session B.**

### Updated programme note for Reg 4 (anger) Session B

> During Reg 068 (grace) Session B Stage 1, a root code collision was confirmed: the CHAR code has been assigned to both the Greek χάρις (charis/grace) family in Reg 068 and the Hebrew חרה (charah/anger) family in Reg 4. These are etymologically unrelated. Reg 4's three CHAR records (H2734 cha.rah, H2740 cha.ron, H8474 ta.cha.rah) have root_gloss=None and root_language=None — pre-backfill, never enriched. When Reg 4 reaches Session B Stage 1, these records must be reassigned to a new distinct root code (proposed: CHARAH, root_gloss='burn/anger', root_language='Hebrew') to resolve the collision. Once corrected, the correlations.root_families CHAR entry for both registries must be recomputed. Cross-reference: wa-068-grace-sessionB-observations-v2.0-2026-04-10.md Gap 10.

---

## ADDENDUM — Cross-registry directive issued for Reg 4 CHAR root correction

**Date:** 2026-04-10

Researcher elected to fix Reg 4 now rather than deferring to Reg 4's Session B.

Directive issued: wa-reg004-anger-cc-directive-v1-2026-04-10.md

Operations specified:
1. Identify distinct wa_term_root_family record ids for the 3 Reg 4 CHAR records (deduplicated query)
2. Update all three: root_code CHAR → CHARAH, root_gloss → 'burn/anger', root_language → 'Hebrew', note added
3. Recompute correlations.root_families for both Reg 4 and Reg 68
4. Export updates for both registries

Expected outcome: CHAR in Reg 68 correlations will show registry_count=1, root_gloss='grace'. CHARAH in Reg 4 will show registry_count=1, root_gloss='burn/anger'. Collision resolved.

**Status:** Directive issued — awaiting CC confirmation.

---

## ADDENDUM — Reg 4 CHAR correction confirmed | Gap 10 fully resolved

**Date:** 2026-04-10

### CC execution confirmed

- Step 1: wa_term_root_family record ids confirmed — rf.id=33 (H2740), rf.id=34 (H2734), rf.id=35 (H8474)
- Step 2: All three updated — root_code=CHARAH, root_gloss='burn/anger', root_language='Hebrew', note set. Zero CHAR records remain in Reg 4.
- Step 3: Correlations recomputed for both registries.

### Key outcome

Both CHAR (Reg 68) and CHARAH (Reg 4) now have registry_count=1. Neither appears in correlations.root_families — the signal requires registry_count ≥ 2. The false cross-registry link is eliminated.

### Statistics consequence for Reg 068

correlation_root_family_count: 1 → 0. This is correct — CHAR is now single-registry and falls below the ≥2 threshold for the signal. The statistics block in the Reg 068 export must reflect this change.

### Next action

Upload fresh Reg 068 export to verify correlation_root_family_count = 0 and confirm all gap 10 changes are correctly reflected before closing.

**Status:** Awaiting fresh Reg 068 export upload.

---

## ADDENDUM — Fresh export verified | All gaps resolved | Stage 1 complete

**Date:** 2026-04-10 | **Export timestamp:** 2026-04-10T11:32:31Z

### Spot-check results — all directives v2 through v6 + Reg 4 directive

| Check | Expected | Actual | Status |
|---|---|---|---|
| verse_context_status | In Progress | In Progress | ✓ |
| active_verse_count | 226 | 226 | ✓ |
| H2594 status | extracted_thin | extracted_thin | ✓ |
| H2594 active_verses | 1 | 1 | ✓ |
| H2594 GOD_AS_SUBJECT flag | present | present | ✓ |
| H2600 status | extracted | extracted | ✓ |
| H2600 active_verses | 31 | 31 | ✓ |
| H2600 GOD_AS_SUBJECT flag | present | present | ✓ |
| root_family_count | 10 | 10 | ✓ |
| CHEN records: H2580, H8469, H2587, H2594, H2600, H2603A, H8467 | all present | all present | ✓ |
| CHAR records: G5483, G5485, G5487 | all present | all present | ✓ |
| owning_registry H2433 | '23' | '23' | ✓ |
| owning_registry H2594 | '23' | '23' | ✓ |
| owning_registry H2606 | '23' | '23' | ✓ |
| correlation_root_family_count | 0 | 0 | ✓ |
| correlations.root_families | empty (CHAR single-registry) | 0 entries | ✓ |

**All gaps resolved. Stage 1 remediation complete.**

### Open dependency carried forward to Stage 2
H2594 and H2600 are reinstated but their OWNER registries (Reg 23 and Reg 73) have no verse_context records for these terms. Reg 068 verse_context_status = In Progress as a result. Stage 2 proceeds against the five OWNER terms only. The two reinstated XREFs will be incorporated when Regs 23 and 73 complete VC classification for those terms.
