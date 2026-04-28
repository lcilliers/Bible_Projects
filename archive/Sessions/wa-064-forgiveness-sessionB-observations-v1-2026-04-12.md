# Session B Observations Log
## Registry 064 — forgiveness
**Instruction:** WA-SessionB-Instruction-v4.7-2026-04-12
**Session:** Session 1
**Date:** 2026-04-12
**Input:** wa-064-forgiveness-complete-2026-04-12.json
**Word study input:** wa-064-forgiveness-word-study-v1-2026-04-12.md

---

## STAGE 1 — DATA AUDIT

### Section 1 — Registry block audit

| Field | Status | Notes |
|---|---|---|
| `word` | OK | "forgiveness" |
| `no` | OK | 64 |
| `id` | OK | Present |
| `cluster_assignment` | OK | C17 |
| `verse_context_status` | OK | Complete — Stage 1 can proceed |
| `session_b_status` | NOTE | "Verse Context Reset" — will be advanced to Analysis Complete at Stage 4 |
| `dim_review_status` | GAP | null — Dimension Review sub-process will be required |
| `dim_review_version` | GAP | null — Dimension Review not yet run |
| `sb_classification` | GAP | null — not yet assigned; to be addressed in Stage 2 Pass 4 |
| `sb_classification_reasoning` | GAP | null — not yet assigned |
| `strongs_list` | Reviewed below | 7 terms total; see deletion review |
| `dimensions` | NOTE | "Relational/Social" — pre-review label; Dimension Review required |
| `sharing_ratio` | NOTE | null — registry has 0 XREF terms and no sharing |

**Strongs_list entries vs. terms array:**
All 7 terms present in terms array. No delete-status terms found — all 7 are active (`term_owner_type = OWNER`, `delete_flagged = 0`). Deletion justification review: not applicable — no deleted terms.

**Registry block summary:** Two structural gaps — `dim_review_status` and `dim_review_version` both null, confirming Dimension Review is required. `sb_classification` and `sb_classification_reasoning` null — expected at this stage. No field errors.

---

### Section 2 — Statistics block audit

| Field | Reported | Actual | Status |
|---|---|---|---|
| `term_count` | 7 | 7 terms in array | OK |
| `active_term_count` | 7 | 7 with delete_flagged=0 | OK |
| `owner_term_count` | 7 | 7 OWNER, delete_flagged=0 | OK |
| `xref_term_count` | 0 | 0 XREF | OK |
| `verse_count` | 190 | Counted across all terms | OK |
| `active_verse_count` | 190 | All delete_flagged=0 | OK |
| `verse_context_group_count` | 14 | 14 groups in verse_context.groups | OK |
| `verse_context_record_count` | 190 | Contexts across all groups: requires count | VERIFY |
| `anchor_verse_count` | 14 | 14 anchors confirmed in Session C read | OK |
| `dimension_index_count` | 14 | 14 rows in dimension_index | OK |
| `research_flag_count` | 1 | 1 flag: DIMREVIEW_SESSION_D | OK |
| `session_b_finding_count` | 1 | 1 finding: DIM-64-001 | OK |
| `cross_registry_link_count` | 0 | 0 — expected (Session D populates) | OK |
| `correlation_xref_pair_count` | 0 | 0 — no XREF terms | OK |
| `correlation_cooccurrence_pair_count` | 34 | 34 entries in cooccurrence array | OK |
| `correlation_dimension_pair_count` | 19 | 19 entries in dimension_overlap array | OK — but note: dim_review_status is null; dimension overlap signals require CLAUDE_AI confidence, which has not been assigned. These 19 entries appear to have been generated from an earlier Dimension Review or from KEYWORD_WEAK confidence data. Must be treated as provisional until Dimension Review sub-process completes and confirms. |
| `correlation_root_family_count` | 0 | 0 entries in root_families | INVESTIGATE — see Section 10b |
| `correlation_shared_anchor_count` | 6 | 6 entries in shared_anchor_verses | OK — note: 2 entries share Lev 4:20 with mercy (duplicated entry for reg=111); see consistency check |

**Statistics block summary:** One item for investigation: `correlation_root_family_count = 0` despite 7 terms with root_family records present. This is unexpected and will be examined in Section 10b.

---

### Section 3 — Terms audit

**G0859 | afesis | Greek | OWNER**
- mti.status: extracted
- god_as_subject: 0 — GAP (verse evidence in groups 879-001 and 880-001 places God as actor; Eph 1:7 shows divine forgiveness; `mti_term_flags` GOD_AS_SUBJECT flag likely absent — directive to Claude Code required in Pass 2)
- somatic_link: 0 — NOTE (no somatic link claimed; somatic scan required in Pass 4)
- meaning/meaning_numbered: prose-only (quality flags note NO_WORD_ANALYSIS and PROSE_ONLY_MEANING) — no structured senses available from STEP; accepted as-is
- quality_flags: NO_WORD_ANALYSIS, PROSE_ONLY_MEANING
- phase2_flags: none
- root_family: root_code=AFE, root_gloss="forgiveness" — present

**G0863G | afiēmi | Greek | OWNER** (to release: leave)
- mti.status: extracted
- god_as_subject: 0 — NOTE (this sub-gloss is the leave/abandon sense; God is not predominantly the subject here — acceptable)
- somatic_link: 0
- meaning: prose-only; single sense covering all sub-glosses — structural gap (three sub-glosses G0863G/H/I share the same parsed_meaning_id; sense differentiation between leave, forgive, permit is not in the meaning_parsed senses; this is a STEP data limitation, not a field error)
- quality_flags: none listed in full audit
- phase2_flags: none
- root_family: root_code=AFE, root_gloss="forgiveness" — present

**G0863H | afiēmi | Greek | OWNER** (to release: forgive)
- mti.status: extracted
- god_as_subject: 0 — GAP (this is the primary forgiveness verb; God is consistently the acting subject in many of its uses; `mti_term_flags` GOD_AS_SUBJECT directive required in Pass 2)
- somatic_link: 0
- meaning: same prose block as G0863G — STEP limitation
- quality_flags: none listed
- phase2_flags: none
- root_family: root_code=AFE, root_gloss="forgiveness" — present

**G0863I | afiēmi | Greek | OWNER** (to release: permit)
- mti.status: extracted
- god_as_subject: 0 — acceptable (permit sense; Jesus permits, but this is not specifically a divine-attribute use)
- somatic_link: 0
- quality_flags: none
- phase2_flags: none
- root_family: root_code=AFE, root_gloss="forgiveness" — present

**H5545 | sa.lach | Hebrew | OWNER**
- mti.status: extracted
- god_as_subject: 0 — GAP (H5545 is the OT verb for divine forgiveness; in the OT corpus it is overwhelmingly God as subject; this is the most significant god_as_subject gap in this registry; directive required)
- somatic_link: 0
- meaning_parsed: 3 senses (Qal: to forgive; Niphal: to be forgiven) — structured senses present
- quality_flags: none noted
- phase2_flags: none
- root_family: root_code not explicitly stated in data; related_words show H5546/H5547/H5548; root_family array shows root_gloss="forgiving" — NOTE: root_gloss here is "forgiving" (from H5546 adjective form), while for the Greek family it is "forgiveness". This is not an error per se but a labelling inconsistency across the two language families. The Hebrew root family root_code needs to be verified (see Section 10a).

**H5546 | sal.lach | Hebrew | OWNER** (forgiving — adjective)
- mti.status: extracted
- god_as_subject: 0 — GAP (Psa 86:5 uses this term exclusively of God; "you are forgiving" — this is by definition a divine attribute term; directive required)
- somatic_link: 0
- occurrence_count: 1 — single occurrence (Psa 86:5)
- meaning: "ready to forgive, forgiving" — adequate
- root_family: root_gloss="forgiving"

**H5547 | se.li.chah | Hebrew | OWNER** (forgiveness — noun)
- mti.status: extracted
- god_as_subject: 0 — GAP (all 3 occurrences — Psa 86:5, Psa 130:4, Dan 9:9 — use this as a divine possession/attribute; "with you there is forgiveness"; directive required)
- somatic_link: 0
- occurrence_count: 3
- meaning: "forgiveness" — single sense, adequate
- root_family: root_gloss="forgiving"

**Terms audit summary:**
- god_as_subject gap: Terms G0859, G0863H, H5545, H5546, H5547 — all should have GOD_AS_SUBJECT flag. This is the programme-wide automation gap. Directive to Claude Code required.
- No deleted terms — deletion review not applicable.
- Root family present on all 7 terms but root_code for Hebrew family needs verification in Section 10a.
- No unexpected quality or phase2 flags. STEP sense-structure limitation for G0863G/H/I is a known data constraint, not a gap to patch.

---

### Section 4 — Verse context groups audit

All 14 groups have context_descriptions. Checked anchor designation across all 14 groups: each has exactly 1 anchor verse (confirmed in Session C read). Group codes: no duplicates detected (5376-001/002/003, 5377-001/002, 5378-001/002, 5379-001/002/003, 5380-001, 879-001/002, 880-001). Classification counts: contexts arrays present in all 14 groups.

One structural observation: group 5380-001 (mti_term_id=5380) — the mti_term_id 5380 does not correspond to any Strong's number in the 7 active terms. The mti_term_ids used by groups are: 5376, 5377, 5378, 5379, 5380, 879, 880. Cross-checking against terms array: the terms use strongs_numbers G0859, G0863G/H/I, H5545, H5546, H5547. The mti_term_ids (5376–5380, 879, 880) appear to be `mti_terms.id` values (database primary keys), not Strong's numbers. This is expected programme structure. The group assignments are correct — the mti_term_id field on groups links to mti_terms.id.

**Set-aside verses:** Statistics report 38 set-aside verses. These appear in the `verse_context.unassigned` array (not in any group). All 38 have `set_aside_reason = null`. Distribution: 34 from mti_term_id 5376 (G0863G — leave/abandon sense), 4 from mti_term_id 5378 (G0863I — permit sense). The leave/abandon sense of *aphiēmi* produces many verses not classifiable as forgiveness-relevant. The null set_aside_reason is a data quality note — reasons were not recorded for these set-aside decisions. Not a blocking gap for Stage 2 but noted. The statistics count of 190 total verse_context_records = 152 in-group + 38 set-aside: **CONFIRMED CONSISTENT**.

**Verse context groups audit: OK.** All 14 groups properly formed with 1 anchor each.

---

### Section 5 — Dimension index audit

All 14 groups have dimension index entries. Confidence levels:

All 14 groups: dimension_confidence = CLAUDE_AI, dominant_subject populated. No KEYWORD_WEAK entries. No null dominant_subject entries.

| Group | Dimension | Confidence | Dominant Subject |
|---|---|---|---|
| 5376-001 | Volition | CLAUDE_AI | HUMAN |
| 5376-002 | Relational Disposition | CLAUDE_AI | HUMAN |
| 5376-003 | Relational Disposition | CLAUDE_AI | HUMAN |
| 5377-001 | Relational Disposition | CLAUDE_AI | GOD |
| 5377-002 | Relational Disposition | CLAUDE_AI | HUMAN |
| 5378-001 | Relational Disposition | CLAUDE_AI | NONE |
| 5378-002 | Moral Character | CLAUDE_AI | HUMAN |
| 5379-001 | Relational Disposition | CLAUDE_AI | GOD |
| 5379-002 | Dependence / Creatureliness | CLAUDE_AI | HUMAN |
| 5379-003 | Relational Disposition | CLAUDE_AI | GOD |
| 5380-001 | Relational Disposition | CLAUDE_AI | GOD |
| 879-001 | Relational Disposition | CLAUDE_AI | GOD |
| 879-002 | Emotion — Negative | CLAUDE_AI | HUMAN |
| 880-001 | Relational Disposition | CLAUDE_AI | GOD |

**Analytical observation — group 879-002 (Emotion — Negative):** This group describes "the absolute limit of forgiveness — the unforgivable sin against the Holy Spirit, and the conditions under which forgiveness is withheld or inaccessible." The dimension assignment of Emotion — Negative is analytically questionable. The group describes a theological limit — a category of sin beyond forgiveness — not an emotion. The anchor verse (Mar 3:29) presents a doctrinal statement, not an emotional state. This is the Session C flag from the completion note (Question 4). Will carry into Stage 2 Pass 1 and Pass 3 for review. No immediate patch — Dimension Review sub-process confirmed complete (CLAUDE_AI confidence); but this specific assignment may warrant revision in Stage 1 remediation.

**Dimension Review sub-process status:** All 14 groups show CLAUDE_AI confidence. `dim_review_status` is null at the registry level but groups are already at CLAUDE_AI confidence. This suggests Dimension Review was conducted without the registry-level status being updated. The Dimension Review sub-process is therefore NOT required to be re-run — the work was done. What IS required is a field-level patch to set `dim_review_status = Complete` and `dim_review_version` on the registry record. **This resolves the gap identified in Section 1 — the Dimension Review sub-process can be skipped; only the registry status field needs patching.**

**Exception: group 879-002 dimension assignment.** This will be reviewed in Stage 2 Pass 1 and a dimension correction patch produced if warranted.

---

### Section 6 — Session B block

- `session_b.dimensions`: null — not yet assigned (expected at this stage; Stage 2 will write this)
- `session_b.findings`: 1 finding present — DIM-64-001 (Luk 7:47 inner-being causal chain: forgiveness → love). This is an analytical pre-finding from Dimension Review; incorporated into Session C word study v1 and will drive Pass 2 and Pass 3 investigation.

---

### Section 7 — Session D block

- `session_d.sd_pointer_flags`: count = 0 (none yet — Stage 2 will produce these)
- `session_d.runs`: count = 0

---

### Section 8 — Research flags

One flag present: `DIMREVIEW_SESSION_D` | session_target = D | resolved = 0 | priority: note in session_research_flags. This flag is carried forward to Session D — no action required in Stage 2.

---

### Section 9 — Cross-registry links

`cross_registry_link_count = 0` — expected; populated during Session D. No action required.

---

### Section 10 — Consistency checks

**10a — Root family completeness:**
- Root AFE (Greek): G0859, G0863G, G0863H, G0863I — all 4 Greek terms carry AFE root code. Complete.
- Root SALACH (Hebrew): H5545, H5546, H5547 — all 3 Hebrew terms carry SALACH root code. Complete.
- Root glosses: AFE root_gloss = "forgiveness" on all 4 Greek terms. SALACH root_gloss = "forgiving" on all 3 Hebrew terms. The Hebrew family root_gloss uses the adjective form ("forgiving" from H5546) rather than the noun ("forgiveness"). This is a minor labelling inconsistency but not an analytical error — "forgiving" accurately describes the SALACH root family's character. No patch required.
- Correlations.root_families = 0: Investigated. Both AFE and SALACH roots appear to be single-registry (only appearing in registry 64). The zero in the correlation signal is consistent with single-registry root codes, not an error. **OK — expected behaviour per instruction 10b.**

**10b — Root family correlation signal:** Both root codes appear to be registry 64-only. Zero correlation root_family signals confirmed as expected. No action.

**10c — Dimension index vs verse context group consistency:** All 14 group codes match. All 14 context_descriptions match exactly between DI and VC. **OK.**

**10d — Anchor verse consistency:** All 14 groups have exactly 1 anchor. `anchor_verse_count` statistics = 14, actual = 14. **OK.**

**10e — Correlation xref signal vs term inventory:** `xref_sharing` = 0 entries. No XREF terms exist. No inconsistency possible. **OK.**

**10f — Statistics vs correlations block:** All 5 correlation count fields match exactly. **OK.**

**10g — Session B classification consistency:** `sb_classification = null`, `sb_classification_reasoning = null`, `session_b.dimensions = null`. All null consistently — no partial write gap. Expected at this stage. **OK.**

**Verse context record count:** Statistics say 190; confirmed as 152 in-group contexts + 38 set-aside (unassigned) = 190. **OK.**

---

## AUDIT SUMMARY — Registry 064 (forgiveness) | 2026-04-12

### Fields confirmed OK
- word, no, id, cluster_assignment, verse_context_status (Complete)
- All 7 terms: present, active, OWNER, correct term_owner_type
- All statistics fields (including correlation counts and verse context record count)
- All 14 verse context groups: context_descriptions, anchors, group codes
- All 14 dimension index entries: CLAUDE_AI confidence, dominant_subject populated, descriptions match VC
- Consistency checks 10a–10g: all passed

### Gaps requiring field-level patch
1. `dim_review_status` | null | `Complete` | update_registry
2. `dim_review_version` | null | `WA-DimensionReview-Instruction-v1.9-2026-04-09` | update_registry

### Gaps requiring Claude Code directives (not field-level patches)
1. `mti_term_flags` GOD_AS_SUBJECT flag missing for terms: G0859, G0863H, H5545, H5546, H5547
   — These are `mti_term_flags` insert operations, governed by WA-Reference Section 13.3
   — Directive to Claude Code required (produced at end of Pass 2 in Stage 2)

### Analytical items for Stage 2 review (not field-level patches)
1. Group 879-002 dimension assignment (Emotion — Negative) — analytically questionable; review in Pass 1 and Pass 3; dimension correction patch may follow
2. 38 set-aside verses from G0863G (leave/abandon): null set_aside_reason — informational; no patch required
3. DIM-64-001 finding (Luk 7:47 causal chain) — carry into Stage 2 analytical work

### Verse Context sub-process required?
[x] No — verse_context_status = Complete; all groups properly formed

### Dimension Review sub-process required?
[x] No — all 14 groups already at CLAUDE_AI confidence; only registry status field update needed (included in field-level patch above)

### Statistics corrections required?
[x] No — all fields verified correct

### strongs_list — deletion justification review
[x] All deletions confirmed — no deleted terms exist; review not applicable

### Root family gaps
[x] No — all 7 terms have root_family records; both AFE and SALACH roots complete

### Open items requiring researcher decision
1. **Group 879-002 dimension (Emotion — Negative):** The description and anchor verse (Mar 3:29 — the unforgivable sin) describe a theological limit, not an emotional state. Possible correct dimensions: Theological/Divine-Human (the divine refusal to forgive), or Volition (the irreversible inner decision that constitutes this sin). This will be reviewed analytically in Stage 2 before any patch is raised. Claude AI will present a recommendation with full reasoning before patching.


---

## STAGE 1 — REMEDIATION CONFIRMED

**Patch PATCH-20260412-064-SESSIONB-V1 applied and confirmed by Claude Code — 2026-04-12**
- dim_review_status = Complete ✓
- dim_review_version = WA-DimensionReview-Instruction-v1.9-2026-04-09 ✓

Fresh extract not required before Stage 2 — the only patched fields are registry-level status fields that do not affect the analytical data (terms, verses, groups, dimension index). Stage 2 proceeds against the existing export `wa-064-forgiveness-complete-2026-04-12.json`.

**Stage 1: COMPLETE.**

---

## STAGE 2 — ANALYTICAL PASSES

Beginning Pass 1 — Meaning and Semantic Range.


---

## PASS 1 — MEANING AND SEMANTIC RANGE

### Primary semantic picture

The vocabulary of forgiveness operates on two distinct but structurally related act-types across the corpus:

**Act-type 1 — Release of debt/guilt (the core forgiveness sense):** This covers groups 5377-001, 5377-002, 5379-001, 5379-002, 5379-003, 879-001, 879-002, 880-001. The act is the cancellation of a legitimate claim — a genuine account is held, and the holder releases it. Whether God releasing sin's penalty (5377-001, 5379-001, 5379-003, 879-001) or a person releasing a debt owed by another (5377-002), the structure is: claim held → claim released. The claim is real; the release is deliberate and complete. **This is the governing sense of the word.**

**Act-type 2 — Release as leaving/permitting (the structural family sense):** Groups 5376-001/002/003, 5378-001/002. These groups use the same verb (*aphiēmi*) in its leaving, abandoning, and permitting registers. The act-structure is identical — releasing something held — but the object released is not a debt but a person, a place, a commitment, a gate. This sense is structurally upstream of the forgiveness sense; the word-family covers all acts of release, of which debt-forgiveness is the theologically most concentrated form.

**Implication for Pass 1:** The forgiveness registry includes the structural family (leave/permit) as essential context for understanding what the forgiveness sense actually does. The word is not merely borrowed metaphor — releasing sin is the same word-act as releasing a prisoner, leaving a home, or granting access. This is not incidental. It means forgiveness is, at its root, an *act of release* — something held, something let go.

---

### Group-by-group semantic findings

**Group 5376-001 (leave for discipleship — Volition, dom_subj HUMAN):**
The deliberate leaving of home, family, possessions as an inner-reordering act. The act is voluntary and costly. The anchor (Mar 10:29) places Jesus as the affirmer of what the leavers have done — the divine validation of the human releasing act. Semantic contribution: *leaving-as-costly-choice* — voluntary forfeiture of what is legitimately held. This is the volitional pole of the word family: the person decides to release and acts on it.

**Group 5376-002 (abandonment of what is owed — Relational Disposition, dom_subj HUMAN):**
The same act in its failure mode: leaving a spouse (1 Cor 7:11-13), abandoning first love (Rev 2:4 — anchor), neglecting the weightier matters of law (Mat 23:23), the disciples fleeing at arrest (Mar 14:50). Semantic contribution: *leaving-as-relational-failure* — the morally wrong release. The anchor (Rev 2:4) is the sharpest: "you have abandoned the love you had at first." This verse reveals the word's darker capacity — it can name betrayal as readily as forgiveness. The same act that constitutes forgiveness (releasing a claim) can constitute abandonment (releasing a loyalty). This semantic duality is significant: forgiveness is the right use of the releasing-act; abandonment is the wrong use.

**Group 5376-003 (relational priority — Relational Disposition, dom_subj HUMAN):**
The relational logic of the leave/stay act: leaving one gift to seek reconciliation (Mat 5:24 — anchor); the shepherd leaving the ninety-nine (Mat 18:12); the Father's not leaving the Son alone (Joh 8:29). The anchor (Mat 5:24) is theologically rich: leave your gift *before the altar* — i.e., suspend worship to restore relationship. The horizontal must be resolved before the vertical offering is valid. The priority is not that altar-worship is unimportant; it is that broken relationship poisons the offering. **Session C flag: Section 2 confirmed — forgiveness is not secondary to worship but its precondition.**

**Group 5377-001 (God's act of releasing guilt — Relational Disposition, dom_subj GOD):**
The core NT forgiveness group. God (via Jesus) releases persons from the penalty of sin. This group contains 26 verses — the largest group in the registry. The dominant pattern: Jesus pronounces forgiveness directly (Luk 5:20, 7:47-48, 7:49, Mar 2:5; Mat 9:2), followed by challenge from onlookers ("Who can forgive sins but God alone?" Mar 2:7). This pattern is a Christological claim embedded in the forgiveness corpus: Jesus' authority to forgive sins is presented as evidence of divine identity. Session C Section 1 confirmed — God is the primary actor for this group. **GOD_AS_SUBJECT directive required (G0863H).**

Key semantic observation: the Greek term here is G0863H (*aphiēmi* — to release: forgive). The passive constructions are significant: "your sins are forgiven" — the person receives the release; they do not perform it. The person is acted upon by God.

**Session D flag SD-001:** Luk 7:47 (in this group) establishes a causal inner-being sequence: forgiveness received → love produced (already in DIM-64-001). But the sequence in Luk 5:20 (paralytic healed and forgiven simultaneously) raises a different question: is there a connection between physical healing and inner release that the data warrants examining? The paralytic's access to Jesus is through the faith of others (Mar 2:5: "when he saw *their* faith"). Does corporate faith mediate individual forgiveness in a way that connects to the listening/prayer/intercession cluster? This implicates registry 213 (listen) and the intercession dimension.

**Group 5377-002 (human act of forgiving — Relational Disposition, dom_subj HUMAN):**
The horizontal dimension: the human person forgiving another. The group contains the Lord's Prayer (Mat 6:12, Luk 11:4), the command to forgive seventy times seven (Mat 18:21), the parable of the unmerciful servant (Mat 18:27-32-35), and the condition placed on prayer (Mar 11:25). The anchor (Mat 18:35) adds the critical qualifier: "from your heart" — forgiveness must be an inner act, not merely verbal. 

Semantic finding: the word in this group is identical to group 5377-001 (same Strong's G0863H), but the subject shifts from God to human. The horizontal forgiveness is explicitly modelled on and conditioned by the vertical. Mat 6:14-15 makes this structural dependence explicit: the Father's forgiveness of us is conditioned on our forgiveness of others. This is not a simple cause-effect — it is a *relational congruence requirement*: you cannot occupy the position of one who has been forgiven while simultaneously occupying the position of one who refuses to forgive.

**Session D flag SD-002:** Mat 18:27 — the master "out of pity" forgives the servant's debt. The word translated "pity" (*splagchnizomai*) names a visceral compassion — a movement of the inner organs. This is the somatic entry point for forgiveness in this group: forgiveness, at its human origin in this verse, arises from a body-involving compassion response. This directly connects to the compassion registry (023) and the mercy registry (111). The question for Session D: does compassion *precede* forgiveness as its inner-being condition, or is it merely one pathway to forgiveness?

**Group 5378-001 (permitting/granting access — Relational Disposition, dom_subj NONE):**
The permit sense of *aphiēmi*. Jesus permits children to come (Mar 10:14 — anchor), permits baptism to fulfil righteousness (Mat 3:15), permits a person to give away their cloak (Mat 5:40). The inner-being posture is *receptivity and non-obstruction* — the holding-open of a door. The dominant subject is NONE (it varies: sometimes Jesus, sometimes a person following an instruction). The forgiveness connection is structural: the same act-form (releasing, allowing) names both forgiveness and hospitality. **This group's contribution to the forgiveness word study is the establishing of a shared act-structure between forgiving and welcoming.**

**Group 5378-002 (withholding permission — Moral Character, dom_subj HUMAN):**
The negative pole: refusing to permit, obstructing, closing the door. Mat 23:13 (anchor — Pharisees shutting the kingdom in people's faces). Also: Jesus not permitting demons to speak (Mar 1:34); Korban tradition preventing care for parents (Mar 7:12); Mat 27:50 (Jesus "yielded up his spirit" — *aphiēmi* in its releasing of life sense); Rom 1:27 ("gave up natural relations"). The anchor and the Korban verse reveal: the Pharisees' shutting of the kingdom is the exact inverse of Jesus' opening of it to children (5378-001). Same act, opposite moral valence.

Dim assignment review — **879-002:** The group description for 879-002 says "the absolute limit of forgiveness — the unforgivable sin against the Holy Spirit, and the conditions under which forgiveness is withheld or inaccessible." The three verses in this group are: Mar 3:29 (anchor — "never has forgiveness, guilty of eternal sin"), Heb 9:22 ("without shedding of blood there is no forgiveness"), Heb 10:18 ("where there is forgiveness, no more offering for sin"). These three verses together describe: the outer theological boundary of forgiveness, the covenantal-blood requirement for forgiveness to be possible, and the finality of forgiveness once obtained. **None of these is an emotional state. The dimension "Emotion — Negative" is incorrect.** The group describes *theological and covenantal conditions* governing forgiveness access. The correct dimension is **Theological/Divine-Human** — these verses define what God does or does not do under specific covenantal and moral conditions. Or alternatively, considered as a unit describing the inner-being consequence of a specific sin-state: **Moral Character** (the state of one who has crossed the limit). Claude AI assessment: **Theological/Divine-Human** is the most accurate dimension — the subject matter is the divine determination of forgiveness boundaries, not an emotion in the person. **Patch required: group 879-002 dimension = Theological/Divine-Human.** Will be included in a Stage 1 remediation patch.

**Group 5379-001 (atonement-mediated forgiveness — Relational Disposition, dom_subj GOD):**
The Levitical corpus: sacrifice → priestly atonement → forgiveness granted (passive: "they shall be forgiven"). 13 verses, all from Lev/Num. The consistent pattern: forgiveness is not automatic — it requires mediation. The Hebrew verb is H5545 (*sālach*, Qal/Niphal). **GOD_AS_SUBJECT directive required (H5545).** The passive construction throughout ("shall be forgiven") establishes forgiveness as a *conferred* state — the worshipper receives it but does not self-generate it. This group confirms the programme description: *sālach* in the OT operates exclusively as a divine act mediated through the cultic system. No human is the subject of *sālach* in this corpus.

Semantic observation: the verb in the Lev 4-6 passage operates in a cultic grammar where the formula is invariant: "the priest shall make atonement… and he/they shall be forgiven." The forgiveness is covenantally guaranteed by the correct execution of the ritual — it is not conditional on interior feeling but on exterior covenantal act. This is theologically important: OT forgiveness in the *sālach* corpus is objective and covenantally administered. The inner-being dimension is present (the worshipper's standing before God is changed) but the mechanism is outward.

**Session D flag SD-003:** The Levitical pattern (sacrifice → atonement → forgiveness) and the NT pattern (Christ's blood → repentance/faith → forgiveness) run in parallel. The programme already has a guilt registry (073) and a sin registry (147). The question for Session D: does the atonement-mediated structure of OT forgiveness carry forward as the structural template for NT forgiveness, and if so, what does this suggest about the inner-being conditions that forgiveness addresses (guilt as inner state, atonement as the mechanism that satisfies it)? This implicates guilt (073), sin (147), and repentance (135) simultaneously.

**Group 5379-002 (intercession for forgiveness — Dependence/Creatureliness, dom_subj HUMAN):**
The petitionary dimension: Daniel praying for national forgiveness (Dan 9:19 — anchor), Moses interceding (Num 14:19-20), Amos crying out (Amos 7:2), Naaman asking for pre-emptive pardon (2Ki 5:18). This group also includes God refusing to forgive (Deu 29:20, 2Ki 24:4, Lam 3:42), and Jeremiah 5:7 ("How can I pardon you?"). The forgiveness is sought, not assumed. The Dependence/Creatureliness dimension is well-assigned: the posture is that of the creature appealing to the Creator, acknowledging that forgiveness is not owed.

Semantic note: the contrast between God granting forgiveness (Num 14:20: "I have pardoned, according to your word") and God withholding it (Deu 29:20, 2Ki 24:4, Lam 3:42) establishes that forgiveness is genuinely conditional — God can and does refuse. This is important: the registry contains the full picture, including refusal. The God who forgives freely is also the God who does not forgive where there is no repentance or where the covenant has been wilfully and finally broken.

**Group 5379-003 (new covenant forgiveness — Relational Disposition, dom_subj GOD):**
The programmatic new covenant promises: Jeremiah 31:34 (anchor — "I will forgive their iniquity and remember their sin no more"), the Solomon and Chronicles prayer-forgiveness patterns (1Ki 8:30-50, 2Ch 6-7), Psa 103:3, Jer 33:8, Jer 50:20. The anchor verse is the most concentrated: forgiveness that includes the *cessation of divine memory* — not a suppression but a genuine covenantal resolution. The Solomon/Chronicles pattern is interesting: Solomon's prayer lists the conditions under which God will forgive (prayer, repentance, return), and God's response in 2Ch 7:14 confirms the pattern. These are not guilt-release formulae but covenant-relationship maintenance acts.

**Session D flag SD-004:** Jeremiah 31:34 is a shared anchor verse with guilt (073) and love (103). Its appearance in three registries reflects its theological density: the new covenant is described in terms of knowledge of God (cognitive/volitional), forgiveness of iniquity (relational), and remembrance-ceasing (cognitive/relational boundary). Does forgiveness in the new covenant context involve a *cognitive* dimension — the removal of the basis for the guilt-state — that connects it to the knowledge and thought registries? Session D needs to examine this verse's inner-being grammar across three registries simultaneously.

**Group 5380-001 (forgiveness as divine attribute — Relational Disposition, dom_subj GOD):**
One verse, one anchor: Psa 86:5. *Sallāch* (H5546) — "you are forgiving." The unique OT occurrence of forgiveness as a divine disposition-word. Single-verse group; the anchor is the entire verse. **GOD_AS_SUBJECT directive required (H5546).** The verse places forgiveness alongside "good" and "abounding in steadfast love" — forgiveness belongs to the essential character of God, not to a special act or a specific covenantal mechanism. It is a description of what God *is*, not just what God *does*.

**Group 879-001 (forgiveness as spiritual transaction — Relational Disposition, dom_subj GOD):**
The NT noun *aphesis* in its fullest theological expression: forgiveness of sins as the gift of redemption through Christ's blood. Eph 1:7 (anchor), Col 1:14, Acts 2:38, 5:31, 10:43, 13:38, 26:18, Luk 1:77, 3:3, 24:47, 4:18, Mar 1:4, Mat 26:28. The consistent formula: "forgiveness of sins" as the content of the gospel proclamation. Acts 2:38 clusters repentance + baptism + forgiveness of sins + gift of the Holy Spirit in a single sequence. Acts 26:18 maps the full conversion sequence: turn from darkness to light, from Satan to God → receive forgiveness of sins + place among the sanctified. The Lucan pattern (Luk 1:77, 3:3, 24:47, 4:18) presents forgiveness as the content of messianic liberation: "proclaim liberty to the captives" (4:18) uses *aphesis* — the same word as forgiveness, here translated "liberty." The connection between forgiveness and liberation from captivity is not metaphorical in Luke — they are the same word. **GOD_AS_SUBJECT directive required (G0859 — *aphesis*).**

**Session D flag SD-005:** Acts 26:18 presents a sequence: blindness → sight → turn from darkness/Satan to God → forgiveness → sanctification. This is an inner-being sequence that implicates spiritual blindness (207), calling (019), forgiveness (064), and sanctification. Does the programme have sufficient registry coverage of the conversion inner-being sequence as a structured progression? The question for Session D: is the movement from spiritual blindness to forgiveness to sanctification a recognisable inner-being grammar that operates consistently across the corpus, and does its structure illuminate how forgiveness functions as a *gateway* state in the inner-being landscape rather than a terminal one?

**Group 879-002 (limit of forgiveness — dimension correction required):**
Three verses: Mar 3:29 (anchor — unforgivable sin), Heb 9:22 (no forgiveness without blood), Heb 10:18 (forgiveness complete → no more offering). As analysed above, the dimension should be Theological/Divine-Human. See patch required.

**Group 880-001 (forgiveness as divine possession — Relational Disposition, dom_subj GOD):**
*Selichah* (H5547) in Psa 130:4, Dan 9:9, Neh 9:17. Psa 130:4 (anchor): "with you there is forgiveness, that you may be feared." Dan 9:9: "to the Lord our God belong mercy and forgiveness." Neh 9:17: God described as "a God ready to forgive" (*eloah selichot*). The noun names forgiveness as something God *possesses* — it is *with* him, it *belongs* to him. The fear-connection in Psa 130:4 is theologically paradoxical: forgiveness produces fear rather than presumption. **GOD_AS_SUBJECT directive required (H5547).** The fear-dimension implies that receiving forgiveness is not a transaction that leaves the recipient unchanged — it produces a new orientation (reverential fear) that is itself an inner-being state.

**Session D flag SD-006:** Psa 130:4 — forgiveness produces *fear* (yir'ah — reverential awe). Fear/reverence is a distinct inner-being state with its own registry or related registries (reverence is registry 138, which is a pure XREF registry). The question for Session D: does the forgiveness corpus show that receiving forgiveness characteristically produces a specific downstream inner orientation (love in Luk 7:47, fear in Psa 130:4)? Are these the same downstream state named differently, or two distinct responses to forgiveness? This also implicates the grace registry (068) where DIM-68 established grace → supplication. The pattern across three registries — grace → supplication, forgiveness → love (Luk 7:47), forgiveness → fear (Psa 130:4) — may constitute a recognisable inner-being generator pattern for Session D.

---

### Pass 1 — Session C check

Checking Section 1 (Characteristic Summary) and Section 2 (Impact Description) against Pass 1 findings:

- Section 1: "the deliberate choice to cancel the account of injury" — **confirmed**
- Section 1: "the Hebrew and Greek vocabulary covers sending away, releasing, covering over" — **partial correction needed**: the Hebrew vocabulary here is specifically the *sālach* family (pardon/forgive); it does not prominently cover "covering over" in this registry (that would be *kāphar* or *kāsâh*, which are not in this registry's terms). Section 4 should remove "covering over" as a vocabulary description. The Greek vocabulary does involve a send-away/release act, confirmed.
- Section 1: "Forgiveness in Scripture is consistently modelled on what God does" — **confirmed and deepened**: the *sālach* verb is used exclusively of God in the OT corpus of this registry.
- Section 2: "What feeds and strengthens forgiveness is the prior experience of being forgiven" — **confirmed** by Mat 18:27 (the master's pity preceding his forgiveness) and the structural logic of Mat 6:14-15.
- Section 2: "what forgiveness produces in the person who practises it is a form of inner freedom" — **confirmed** in principle; the Luk 7:47 chain (forgiveness received → love produced) and Psa 130:4 (forgiveness → fear) add specific named inner states to what was described only as "inner freedom."
- Section 2: Statement about somatic evidence (weeping at Luk 7:47) — the word study's Section 1 mentions no somatic detail; somatic pass (Pass 4) will address.

**Correction flag for Session C Section 4:** Remove "covering over" from vocabulary description. The *sālach* family does not primarily carry that sense.

**Deepening flag for Session C Section 2:** The inner states produced by forgiveness are not only "inner freedom" but specifically named: love (Luk 7:47) and reverential fear (Psa 130:4). These should be named explicitly in Section 2's account of what forgiveness produces.

---

### Pass 1 — dimension correction patch required

Group 879-002 dimension should be **Theological/Divine-Human** (not Emotion — Negative). The three verses (Mar 3:29, Heb 9:22, Heb 10:18) describe covenantal and theological conditions governing forgiveness — the outer limit, the blood requirement, and the finality once achieved. These are theological propositions about divine action, not emotional states. A patch will be prepared for researcher review.

---

### Pass 1 complete. SD pointers raised: SD-001 through SD-006.


---

## PASS 2 — DIVINE DIMENSION

### Dominant pattern of divine involvement

The divine dimension in the forgiveness registry is extraordinarily concentrated. Across the 14 groups, God is the dominant subject in 6 groups (5377-001, 5379-001, 5379-003, 5380-001, 879-001, 880-001) — more than any other subject pattern. In two further groups (5379-002, 880-001), God's response (to grant or withhold) is the central event even though humans are the initiating subjects. The overall pattern:

**God is the originator, model, and ultimate source of forgiveness.** The human capacity to forgive (5377-002) is presented as derivative — conditioned on having received forgiveness, commanded as a pattern that reflects the divine act. There is no evidence in this corpus of a forgiveness capacity that is self-generated in the human person. Every forgiveness in the corpus is either: God forgiving a human, or a human forgiving another human in explicit response to having been forgiven by God.

### Dominant pattern: God gives, sustains, and defines

- OT: God forgives through covenantal mediation — sacrifice, priest, atonement, then conferred pardon (*sālach* always God as subject; passive "shall be forgiven" for the human)
- OT: God holds forgiveness as his essential disposition (*sallāch* — the readying to pardon)
- OT: God's forgiveness is genuinely conditional — he grants it in response to repentance/intercession, refuses it when the covenant is finally broken (Deu 29:20, 2Ki 24:4, Lam 3:42)
- NT: God forgives through Christ's authority (Jesus claiming divine prerogative directly — "who can forgive sins but God alone?" answered by Jesus forgiving); through Christ's blood (*aphesis* in Eph 1:7, Mat 26:28)
- NT: The human act of forgiving is explicitly conditioned on God's forgiveness of the human (Mat 6:14-15, Mat 18:35, Mar 11:25)

### Eschatological dimension

Present but not dominant. Jeremiah 31:34 (group 5379-003) is the programmatic eschatological statement — new covenant forgiveness that includes the cessation of divine memory of sin. Acts 26:18 points toward sanctification as the trajectory of forgiveness. Luk 4:18 uses *aphesis* for the messianic liberation proclaimed in Jubilee terms — the "year of the Lord's favour" frame makes forgiveness eschatological in the sense of final restoration. Heb 10:18 ("where there is forgiveness of these, there is no longer any offering for sin") is eschatological in the Hebrews sense: the final, complete forgiveness that terminates the sacrificial system.

**Eschatological signature:** Forgiveness is not eschatologically concentrated — it is a present-tense reality in both testaments — but it has an eschatological *fulfilment* dimension where the promise is finally, fully, and irreversibly enacted.

### Divine-human relationship type

**Derivative and responsive.** The human characteristic is derivative (received from God; the inner capacity depends on having been the recipient of divine forgiveness) and responsive (exercised toward others in response to the divine act). This places forgiveness at the Spirit-primary to Spirit-soul-interface range of the classification — the characteristic in its fully functioning form cannot be explained by natural human capacity alone. The grace registry (068) follows the same pattern.

### GOD_AS_SUBJECT flag assessment — Pass 2 findings

| Term | Assessment | Directive needed? |
|---|---|---|
| G0859 (*aphesis*) | Yes — divine subject in groups 879-001, 880-001; "forgiveness of sins" as God's gift | Yes |
| G0863G (to release: leave) | No — leave/abandon sense; human subjects throughout | No |
| G0863H (to release: forgive) | Yes — God/Jesus primary subject in 5377-001; human in 5377-002 | Yes — for the God-as-subject verses; the term has dual subject use |
| G0863I (to release: permit) | Mixed — Jesus permits in 5378-001; no consistent divine subject | No |
| H5545 (*sālach*) | Yes — OT forgiveness verb; exclusively divine subject in this corpus | Yes |
| H5546 (*sallāch*) | Yes — divine disposition term (Psa 86:5 — "you are forgiving") | Yes |
| H5547 (*selichah*) | Yes — all 3 occurrences present forgiveness as divine possession | Yes |

**Directive required for 5 terms: G0859, G0863H, H5545, H5546, H5547.**

Note on G0863H: this term has dual subject use (God/Jesus in 5377-001; humans in 5377-002). The GOD_AS_SUBJECT flag appropriately reflects the pattern-level observation that this term *primarily* or *significantly* involves God as subject. It should be set.

### Session D flags from Pass 2

**SD-007:** The pattern where Jesus claims authority to forgive sins (Luk 5:20-24; Mar 2:5-10; Mat 9:2-6) generates a Christological argument: Jesus' forgiveness is God's forgiveness. The scribes are right that "only God can forgive sins" — Jesus' point is that he is that God. This pattern is not merely theological background; it is an inner-being statement about the source of forgiveness. The question for Session D: does the Christological claim embedded in the forgiveness corpus relate to the authority registry (197) or the dominion registry (199) — both in C20? The connection between forgiveness-authority and authority in general is worth examining.

**SD-008:** Mat 6:14-15 establishes a reciprocal structure: human forgiveness of others ↔ Father's forgiveness of the human. The structural congruence is not a quid pro quo (performance-based reward) but a relational coherence requirement — the person who has received forgiveness and refuses to extend it has, in some sense, not understood what they received. This is structurally parallel to the James 2 argument about faith and works. The question for Session D: is there a pattern across registries where a received inner-being gift (grace, forgiveness) is structured so that its retention requires its exercise? Does this pattern appear elsewhere in the corpus?

### Pass 2 complete. New SD pointers: SD-007, SD-008.
Total running SD count: SD-001 through SD-008.


---

## PASS 3 — VERSE ANNOTATIONS (Anchor Verse Evidence)

All 14 anchor verses read with full application of Section 2.0a cross-registry questions after each.

---

**REFERENCE:** Mar 10:29
**STRONG'S:** G0863G (to release: leave)
**CONTEXT GROUP:** 5376-001
**ANCHOR:** yes
**ANNOTATION:** Jesus validates the disciples' costly act of leaving — home, family, land — for the sake of the gospel. The word *aphiēmi* here is the deliberate release of what is legitimately held. Jesus' response frames the leaving as a spiritually significant act whose reward exceeds what is given up. The verse does not concern forgiveness directly, but it establishes the inner grammar of the releasing-act: it is chosen, costly, and relationally reorienting. The act of leaving is here driven by a higher loyalty — the same inner-act structure that underlies forgiveness proper. **The verse shows that the releasing-act is not passive or reluctant; it is wilfully prioritised.**
**SESSION C FLAG:** deepen — Section 1's description of forgiveness as "deliberate choice" is confirmed and enriched by this structural observation about the *aphiēmi* family.

*Cross-registry questions (2.0a):* The "for my sake and for the gospel" frame raises the calling registry (019). The inner act of leaving home and family as a discipleship response — what does this suggest about the relationship between calling, inner reordering, and forgiveness as a releasing-act? Flag: **SD-009** — The *aphiēmi* leaving-act in group 5376-001 (leaving for discipleship) may encode an inner-being reordering that connects volitionally to calling (019) and to the concept of inner prioritisation. Does the programme's treatment of calling address the inner cost of the leaving-act as a dimension of that vocation? Implicates registry 019 (calling).

---

**REFERENCE:** Rev 2:4
**STRONG'S:** G0863G (to release: leave)
**CONTEXT GROUP:** 5376-002
**ANCHOR:** yes
**ANNOTATION:** The risen Christ's accusation against the Ephesian church: "you have abandoned the love you had at first." The word *aphiēmi* — the same word used for forgiveness — here names a spiritual defection: the releasing of something that should have been kept. The verse reveals that the act-structure of forgiveness can be turned against itself: the same will that can release a debt (rightly) can release a loyalty (wrongly). What was abandoned is "first love" — not primary in time only, but primary in quality. **The verse defines the anti-pattern: where forgiveness is the right use of releasing, this is its wrong use.** The church's failure is not that it committed a dramatic sin but that it slowly released what it should have held.
**SESSION C FLAG:** deepen — Section 2's account of what opposes forgiveness (hardening of inner account-keeping) should be complemented by this: the same releasing faculty that enables forgiveness can, directed wrongly, constitute abandonment. The inner capacity for forgiveness is morally double-edged.

*Cross-registry questions (2.0a):* "First love" directly implicates registry 103 (love). The abandonment of love while maintaining orthodox conduct (the Ephesians are otherwise commended) suggests a dissociation between external religious performance and inner relational orientation. Flag: **SD-010** — Does the Ephesian pattern (orthodox conduct + abandoned love) represent an inner-being failure mode where relational disposition (love, forgiveness) is atrophied while moral conduct continues? Implicates love (103), possibly fellowship (062).

---

**REFERENCE:** Mat 5:24
**STRONG'S:** G0863G (to release: leave)
**CONTEXT GROUP:** 5376-003
**ANCHOR:** yes
**ANNOTATION:** Leave your gift at the altar; be reconciled first; then offer. The word *aphiēmi* names the deliberate suspension of a religious act in order to restore a human relationship. The sequence is striking: the gift is already at the altar — worship is already begun — when reconciliation takes priority. The inner priority being named is not that relationships matter more than God, but that broken relationships create an obstacle to vertical offering that must be resolved before the offering can be genuine. **Forgiveness as a precondition of worship: this verse places the horizontal before the vertical not in importance but in sequence.** The releasing-act here is temporarily releasing a gift in order to permanently restore a relationship.
**SESSION C FLAG:** confirmed — Section 2 states forgiveness precedes worship. This verse confirms it precisely.

*Cross-registry questions (2.0a):* The gift before the altar implicates worship vocabulary and the broader inner-being grammar of offering. What is the inner-being posture of the worshipper who knows there is unresolved conflict between himself and his brother? Is the forgiveness registry the precondition entry point for several other registry states (worship, prayer, love)? Flag already raised — see SD-001 context; this deepens the question about whether forgiveness functions as a gateway state.

---

**REFERENCE:** Luk 7:47
**STRONG'S:** G0863H (to release: forgive)
**CONTEXT GROUP:** 5377-001
**ANCHOR:** yes
**ANNOTATION:** The most analytically significant verse in the registry. Jesus draws the explicit inner-being causal chain: the woman's many sins are forgiven, and *therefore* she loved much. The inverse — the one forgiven little loves little — completes the logic. The causal direction is crucial: this is not "she loved much and therefore was forgiven" (which would make forgiveness a reward for love); it is "she was forgiven much and therefore loved much" (forgiveness as the generative cause of love). **The verse establishes that forgiveness received is not a neutral transaction — it transforms the inner person, specifically by producing the orientation of love.** This is the most direct inner-being causal statement in the entire forgiveness corpus. It is already captured in DIM-64-001 and was central to the Session C word study.
**SESSION C FLAG:** confirmed and deepened — the annotation in Session C v1 is accurate. Deepen by naming the causal direction explicitly: forgiveness → love is asymmetric; the verse will not bear the reverse reading.

*Cross-registry questions (2.0a):* Love (103) and forgiveness (064) are causally connected here. But the verse also implicates guilt: the woman's many sins presuppose guilt (073) as the prior state that forgiveness addresses. The inner-being sequence in this verse is: guilt (prior state) → forgiveness received (release of guilt) → love produced (downstream orientation). Three registries in causal sequence. Flag: **SD-011** — Does the full corpus support a three-registry causal chain: guilt → forgiveness → love? This is a Session D priority question because it maps an inner-being progression rather than a static state description.

---

**REFERENCE:** Mat 18:35
**STRONG'S:** G0863H (to release: forgive)
**CONTEXT GROUP:** 5377-002
**ANCHOR:** yes
**ANNOTATION:** "If you do not forgive your brother from your heart." The qualifier "from your heart" is the entire weight of this verse's analytical contribution — it names the inner location where forgiveness must originate to be genuine. The parable preceding this verse has shown the servant who verbally accepted his master's forgiveness while inwardly retaining his claim against the fellow-servant. Jesus' conclusion identifies the failure precisely: the forgiveness did not reach the heart. **Forgiveness is not complete as a verbal or legal declaration; it must have an inner locus. A forgiveness that exists only in words or conduct but has not reached the inner person is not forgiveness in the register Scripture requires.** This verse is the most direct statement in the NT of forgiveness as an inner-being act.
**SESSION C FLAG:** confirmed and deepened — Section 1 describes forgiveness as involving an inner act of release. This verse specifies the locus: heart. Session C Section 4 should note that the heart terminology here parallels other heart-locus inner-being acts in Scripture.

*Cross-registry questions (2.0a):* Heart (Hebrew *lēb/lēbāb*; Greek *kardia*) is the inner-being locus invoked. The programme likely has a heart-related registry or the heart appears across many registries. What does "from your heart" add to the forgiveness picture that "from your will" would not? Does the heart language distinguish forgiveness from mere decision-making and locate it in the affective-volitional centre? Flag: **SD-012** — The "from your heart" qualifier may implicate the programme's treatment of heart as an inner-being faculty. Does the forgiveness corpus consistently locate the act in the heart, and if so, does this connect structurally to other heart-locus acts in adjacent registries?

---

**REFERENCE:** Mar 10:14
**STRONG'S:** G0863I (to release: permit)
**CONTEXT GROUP:** 5378-001
**ANCHOR:** yes
**ANNOTATION:** Jesus' indignation at those who hinder the children: "Let the children come to me; do not hinder them." The word *aphiēmi* is the granting of access — the opening of the way. Jesus' emotional response (indignation) marks this as a morally weighted act: hindering access to him is treated as a serious failure. The verse names a *posture of welcome* — an inner orientation that does not obstruct but opens. **The forgiveness connection is structural: to forgive is to open the way for a person from whom the way had been closed; to permit access is to extend the same opening posture to those who are marginal or overlooked.** The word carries the same act-structure across both uses.
**SESSION C FLAG:** confirmed — used in Session C to illustrate the permitting/opening sense of the word family.

*Cross-registry questions (2.0a):* Jesus' indignation (*ēganaktēsen*) — a strong emotional response to an injustice — is worth noting. The emotional faculty is activated *by* the blocking of access, and it drives the corrective command. Does anger at injustice function as a precondition for or accompaniment to the act of opening/restoring in other registry contexts? The absence question: what is conspicuously absent in the disciples who hindered the children? It is the posture of welcome — the same inner orientation that forgiveness requires. Flag: **SD-013** — Is there a connection between the inner posture of welcome/receptivity (permit sense) and the inner posture of forgiveness (release sense)? Do they share an inner-being disposition that the programme should examine across registries of hospitality, acceptance, or compassion?

---

**REFERENCE:** Mat 23:13
**STRONG'S:** G0863I (to release: permit)
**CONTEXT GROUP:** 5378-002
**ANCHOR:** yes
**ANNOTATION:** The Pharisees shut the kingdom in people's faces — the exact opposite act to Jesus opening the way. The word *aphiēmi* (negated: *ouk aphiēte*) names the deliberate obstruction of access. The verse identifies this as a moral failure so grave it receives a "woe" — covenantal curse language. **The obstructing of access and the withholding of forgiveness are structurally the same inner-being posture: both close what should be open.** The religious leaders who refuse forgiveness and the leaders who shut the kingdom's door are, in this word-family, performing the same act. This verse supplies the darkest end of the permitting spectrum: not just failing to open, but actively closing.
**SESSION C FLAG:** confirmed — used in Session C to illustrate the negative permitting sense. The structural connection between obstruction and unforgiveness should be named more explicitly in Section 1.

*Cross-registry questions (2.0a):* The "woe" language implicates judgment vocabulary. The pride registry, the Pharisee-pattern as an inner-being failure mode, self-justification. The absence question: what is absent in the Pharisees? Not knowledge (they know the law) and not religious practice (they tithe meticulously — Mat 23:23). What is absent is an inner orientation of mercy and welcome. Does the programme have sufficient coverage of the inner-being failure modes associated with religious formalism? Flag consolidated under SD-010 (inner-being dissociation between religious performance and inner orientation).

---

**REFERENCE:** Lev 4:20
**STRONG'S:** H5545 (*sālach*)
**CONTEXT GROUP:** 5379-001
**ANCHOR:** yes
**ANNOTATION:** The standard Levitical formula: sacrifice performed, priest makes atonement, "and they shall be forgiven." The passive construction is theologically definitive — the worshipper does not forgive themselves or achieve forgiveness; they receive it as the outcome of a covenantally prescribed act. The formula is invariant: the specifics of the offering may change (bull, goat, bird, flour), but the outcome-statement is always the same. **This invariance names forgiveness as a covenantally guaranteed outcome of the correct mediatory act — it is objective in the sense that it does not depend on the worshipper's internal emotional state at the time of offering, but on the correct execution of the covenant rite.** What changes in the worshipper is their standing before God — an inner reality — but the mechanism is outward.
**SESSION C FLAG:** confirmed — Section 3 annotation is accurate. Deepen: the invariance of the formula is itself analytically significant — it reveals that OT forgiveness is covenantal-objective, not subjectively mediated.

*Cross-registry questions (2.0a):* The atonement mechanism (priest, sacrifice, blood) is upstream of forgiveness in this text. The guilt-offering (*asham*) and sin-offering (*hattā't*) both produce forgiveness as their outcome. Does the programme have sufficient coverage of the inner-being dimension of OT ritual — specifically, what happens in the person between the act of offering and the receipt of "you shall be forgiven"? Is there a repentance or guilt state that precedes the offering? The text is silent on this, which may itself be the observation: the covenantal mechanism does not specify the inner-being prerequisite beyond the act. Flag: **SD-014** — Does the contrast between OT covenantal-objective forgiveness (Levitical formula: correct ritual → forgiveness) and NT experiential forgiveness (repentance + faith → forgiveness) reflect two distinct inner-being grammars of receiving forgiveness, or is one the fulfilment of the other? This is a Session D synthesis question implicating repentance (135), guilt (073), faith (059), and the programme's understanding of covenant.

---

**REFERENCE:** Dan 9:19
**STRONG'S:** H5545 (*sālach*)
**CONTEXT GROUP:** 5379-002
**ANCHOR:** yes
**ANNOTATION:** Daniel's urgent intercession: "O Lord, hear; O Lord, forgive; O Lord, pay attention and act; delay not." The four imperatives addressed to God express an escalating urgency — not desperation born of doubt about God's character, but of awareness of the people's need. The appeal is explicitly not to Israel's merit ("we have sinned") but to God's own name and character ("your city, your people, called by your name"). **The verse shows that seeking forgiveness is an act of inner confidence in God's character, not a transaction between equals.** The one who prays this prayer knows two things simultaneously: that the request is justified by the offender's need, and that only the offended party has the power to grant it. The posture is Dependence/Creatureliness precisely because the one praying cannot self-grant what they are seeking.
**SESSION C FLAG:** confirmed and deepened — the confidence-within-dependence posture is a more precise description than the Session C annotation provided.

*Cross-registry questions (2.0a):* The corporate nature of this intercession (Daniel prays for the whole nation, not just himself) raises questions about communal inner-being states. What does it mean for a community to receive forgiveness? Does forgiveness have a collective inner-being dimension that the programme has captured? Flag: **SD-015** — Does the intercession for communal forgiveness in the OT corpus (Dan 9, Num 14, Amos 7, Solomon's prayer in 1Ki 8) name an inner-being posture distinct from individual forgiveness-seeking? Is there a programme registry or cluster that would benefit from attention to the corporate dimension of inner-being states?

---

**REFERENCE:** Jer 31:34
**STRONG'S:** H5545 (*sālach*)
**CONTEXT GROUP:** 5379-003
**ANCHOR:** yes
**ANNOTATION:** The new covenant promise: God will forgive iniquity and *remember sin no more*. The two clauses are not synonymous — forgiveness is the release of the penalty; the cessation of memory is the removal of the basis for future charges. Together they describe a complete covenantal resolution: not only is the debt released, but the record is expunged. **This verse sets the standard for what genuine forgiveness means in both testaments: it is not mere forbearance (tolerating a debt while retaining a record) but actual cancellation (releasing the claim and erasing the account).** The human analogue to this is the verse-world's most challenging requirement: not only to release the claim but to release the memory of the claim as a live grievance.
**SESSION C FLAG:** confirmed — the Session C annotation on this verse is accurate and strong. The human analogue question (releasing memory) is worth deepening in Section 2.

*Cross-registry questions (2.0a):* Shared anchor with guilt (073), thought (160), love (103). The "remember no more" clause implicates the cognitive dimension of forgiveness — specifically, whether forgiveness requires the suppression or transformation of memory, and what that means for the inner-being state of guilt. Flag SD-004 already raised. Deepen: the juxtaposition of "no longer shall each one teach his neighbour to know the Lord, for they shall all know me" — the forgiveness is located in a new-covenant context where direct knowledge of God replaces mediated instruction. Forgiveness and knowing God are the twin promises of Jer 31:31-34. Does the knowledge registry (if it exists) share this anchor?

---

**REFERENCE:** Psa 86:5
**STRONG'S:** H5546 (*sallāch*)
**CONTEXT GROUP:** 5380-001
**ANCHOR:** yes
**ANNOTATION:** The only OT occurrence of forgiveness as a divine disposition-word. "You, O Lord, are good and forgiving, abounding in steadfast love to all who call upon you." The three adjectives are placed in apposition: goodness, forgivingness, and *hesed* (steadfast love). Forgiveness here is not an occasional act but a defining character quality — as fundamental to what God *is* as his goodness or his covenant loyalty. **This verse resolves the question of where forgiveness ultimately comes from: it belongs to the character of God before it becomes a possibility for human experience.** The person who calls upon God encounters the disposition of forgiveness in God's essential nature. This is why the human capacity to forgive is derivative — it begins in encountering someone who is, by nature, forgiving.
**SESSION C FLAG:** confirmed — this verse is the primary anchor for the claim that forgiveness is "received before it can be given." The annotation in Session C v1 is sound. Deepen: the adjective form (*sallāch*) naming a stable disposition rather than an episodic act is analytically significant and unique in the OT.

*Cross-registry questions (2.0a):* The pairing of forgiveness with *hesed* (steadfast love/mercy) in this verse is the clearest single verse in the corpus for the forgiveness-mercy connection. The question for Session D is not just whether the two registries are connected but how their relationship is structured: is *hesed* the broader disposition of which forgiveness is a specific application? Or are they parallel expressions of the same divine character? Flag: **SD-016** — Psa 86:5 places forgiveness alongside goodness and steadfast love as co-equal divine attributes. Does the programme's treatment of mercy (111) and kindness (099) situate them in the same attribute cluster, and does this suggest a systematic relationship between forgiveness and the broader hesed-family? This is a Session D priority for the C17 cluster synthesis.

---

**REFERENCE:** Eph 1:7
**STRONG'S:** G0859 (*aphesis*)
**CONTEXT GROUP:** 879-001
**ANCHOR:** yes
**ANNOTATION:** "In him we have redemption through his blood, the forgiveness of our trespasses, according to the riches of his grace." The verse links four terms in a single statement: redemption (buyback), blood (the price paid), forgiveness (the release of the debt), and grace (the character of God that makes it available). **Forgiveness here is not freestanding — it is embedded in a matrix of divine acts. The blood is the mechanism; the forgiveness is the outcome; the grace is the disposition from which the whole proceeds.** The word *aphesis* is used rather than *aphiēmi* — the noun form, naming the state of forgiveness as a possession: "we have redemption… the forgiveness." Forgiveness is something held by the believer in Christ, not something sought moment by moment.
**SESSION C FLAG:** confirmed — Session C Section 3 annotation is accurate. The grace connection confirmed as a formal vocabulary connection (grace/aphesis in the same verse). This is the most direct single-verse evidence for the forgiveness-grace structural connection noted in Section 5.

*Cross-registry questions (2.0a):* Grace (068) appears in this verse as the source of forgiveness ("according to the riches of his grace"). This is the same relationship noted in the grace word study: grace is the upstream disposition that generates specific divine acts. The connection between grace and forgiveness in this verse is causal and directional: grace → forgiveness. Flag: **SD-017** — Eph 1:7 locates forgiveness "according to the riches of his grace" — grace as the upstream source. Does the grace corpus (068) consistently present grace as the source-disposition from which forgiveness and other covenantal acts flow? If so, grace and forgiveness occupy different positions in an inner-being hierarchy (disposition vs. specific act), and Session D should map this relationship precisely.

---

**REFERENCE:** Mar 3:29
**STRONG'S:** G0859 (*aphesis*)
**CONTEXT GROUP:** 879-002
**ANCHOR:** yes
**ANNOTATION:** "Whoever blasphemes against the Holy Spirit never has forgiveness, but is guilty of an eternal sin." The noun *aphesis* names forgiveness as something that can be permanently absent — a state of non-forgiveness that is final. This verse names the outer boundary of the forgiveness corpus: the point at which forgiveness is structurally inaccessible. The verse does not explain the mechanism of this permanent withholding, nor does it define the blasphemy in precise terms. Its function is to establish that forgiveness, while characteristic of God's disposition, is not automatically extended regardless of the inner state of the person. **The existence of a limit to forgiveness reveals that forgiveness is not a mechanical process but a relational act that requires something from the receiving side — and where that reception is finally and completely closed, the forgiveness cannot reach.** This is consistent with the Luk 7:47 logic: the person who is forgiven little loves little — the relational capacity to receive forgiveness is itself a variable.
**SESSION C FLAG:** confirmed with deepening — the Session C annotation is sound. The dimension correction (Theological/Divine-Human replacing Emotion — Negative) is confirmed by this reading. There is no emotional state described in this verse — only a theological determination about forgiveness accessibility.

*Cross-registry questions (2.0a):* The "eternal sin" language implicates sin (147) and possibly the deadness/spiritual-death registry (210). The permanent inaccessibility of forgiveness for one inner-being state raises the question of what the inner-being grammar of the unforgivable sin is — is it a volitional state (final refusal), a cognitive state (final darkening of understanding), or a spiritual state (severance from the Spirit)? This is a question the forgiveness corpus cannot answer from within its own data. Flag SD-006 (deadness/forgiveness connection) extended: **SD-018** — The unforgivable sin in Mar 3:29 names a state in which forgiveness is permanently inaccessible. Does the programme have vocabulary for describing the inner-being state of the person in this condition? Does spiritual blindness (207), deadness (210), or hardness of heart (which would implicate rebellion registry 128) best describe the inner-being precondition of the unforgivable sin? Session D question spanning registries 147, 207, 210, 128.

---

**REFERENCE:** Psa 130:4
**STRONG'S:** H5547 (*selichah*)
**CONTEXT GROUP:** 880-001
**ANCHOR:** yes
**ANNOTATION:** "But with you there is forgiveness, that you may be feared." Forgiveness is described as something God *has* — a possession located *with* him, not a general availability in the universe. The "that you may be feared" clause names the inner-being consequence of encountering forgiveness: not presumption or casualness, but reverential fear. The paradox is deliberate — one might expect that the availability of forgiveness would reduce fear, but the verse says the opposite. **Forgiveness, when genuinely encountered, produces the reverential awe that recognises the magnitude of what is being offered.** The one who truly grasps that there is forgiveness "with God" does not take it for granted — they are awed by it. This deepens the Luk 7:47 picture: forgiveness produces love *and* fear — not terror of condemnation but the fear that belongs to standing before the one who holds your debt and chooses to release it.
**SESSION C FLAG:** deepening required — Session C Section 3 annotation captures this but does not name the two downstream inner states (love and fear) together. Section 2 should note both as named consequences of forgiveness received.

*Cross-registry questions (2.0a):* Fear/reverence (registry 138 — pure XREF registry) is the downstream inner state here. But the fear that forgiveness produces is not the fear of punishment — it is reverential awe. Does the programme distinguish these two fear-registers? Does the reverence registry (138) operate in the same semantic space as the fear produced by encountering divine forgiveness? Flag SD-006 already raised — this verse confirms and deepens it.

---

### Pass 3 complete. New SD pointers raised: SD-009 through SD-018.
Total running SD count: SD-001 through SD-018.

**Supplementary verse flag (non-anchor):**
During review of group 5377-001 verses: Luk 23:34 ("Father, forgive them, for they know not what they do") — a non-anchor verse of exceptional significance. Jesus forgiving his executioners from the cross is the most extreme application of the human forgiveness command (5377-002 pattern) in divine form. This verse represents the pattern of forgiveness extended without waiting for repentance — grace preceding penitence. Session C Section 3 does not include this verse (it is not an anchor); however, its inner-being significance warrants mention in Session B analytical brief as a supplementary observation.


---

## PASS 4 — SOMATIC EVIDENCE AND SPIRIT-SOUL-BODY CLASSIFICATION

### 4a — Somatic scan

Scanning all verse records for each owner term for body-part reference, physical posture, physiological reaction, or somatic expression.

**G0859 (aphesis — forgiveness, NT noun):**
No body-part language in the direct verses. Eph 1:7 uses "blood" (*haima*) — this is not a somatic reference to the human person but to Christ's sacrificial blood as mechanism. Luk 4:18 uses "the poor" / "captives" / "blind" / "oppressed" — these are social/physical conditions that *aphesis* (liberty/forgiveness) addresses, but they describe the state being released from, not the somatic expression of forgiveness. **No direct somatic expression identified for G0859.**

**G0863G (aphiēmi — to release: leave):**
Mar 10:29 — no somatic language.
Several verses describe physical departure (leaving boats, leaving houses, leaving nets) — these are *physical acts* but the somatic significance is the *action* of leaving, not a bodily manifestation of an inner state. The physical act of leaving represents and externalises the inner reordering. This is **instrument** category: the body performs the release; it is not the origin or expression of the inner state.

**G0863H (aphiēmi — to release: forgive):**
Luk 7:47-48: The anchor for this term is accompanied by the immediately preceding context (not captured in the verse itself but in the pericope) where the woman weeps at Jesus' feet, wets his feet with tears, wipes them with her hair, and anoints them. This is the most somatically rich passage in the entire forgiveness corpus. The somatic acts (weeping, prostration, touching feet, anointing with oil) are the *expression* of the inner state preceding forgiveness — or, more precisely, the visible evidence that the forgiveness has already been received and is producing love as its downstream state. **The somatic expression is: weeping (tears), prostration, touch.** Classification for this somatic context: **expression** — the body manifests what has been received inwardly.
Mat 18:27 — the master "out of pity" (*splagchnizomai*): the compassion that precedes forgiveness is described with a somatic word (bowel-movement metaphor for deep visceral response). The compassion that generates the forgiving act is itself somatically located. **This is the most significant somatic entry point for forgiveness as a received inner state — the compassion that precedes granting forgiveness is visceral in its origin.**
Mat 18:35 — "from your heart" (*ek tēs kardias*): the heart as the required locus of forgiveness. The heart is a primary inner-being organ in Scripture — not merely the emotional seat but the whole-person centre of will, understanding, and feeling. This is a **somatic location** for the forgiveness act, even though it is not a visible bodily expression.

**G0863I (aphiēmi — to release: permit):**
Mar 10:14 — Jesus "indignant" (*ēganaktēsen*): emotional/physiological response, but the somatic language is about Jesus' inner state, not the act of permitting. No direct somatic involvement in the permitting act itself.
Mat 27:50 — "yielded up his spirit" (*aphēken to pneuma*): This is the releasing of the *pneuma* (spirit) at death — the body releasing the spirit. This is a somatic event of the highest significance (the moment of death) but it is in the permit/release group, not the forgiveness group. It is noted for cross-registry observation (spirit-body interface at death) but does not contribute to the somatic picture of forgiveness.

**H5545 (sālach — to forgive, Hebrew):**
Levitical corpus (group 5379-001): the physical acts of the sacrificial system — bringing animals, laying hands on them, slaughtering, burning fat, sprinkling blood — are all present in the surrounding context of the Lev 4-6 passages. These physical acts are the ritual mechanism of forgiveness in the OT cultic system. **The body performs the ritual; the forgiveness is the spiritual outcome.** Classification: **instrument** — the body (of the worshipper through the offering) performs the act that produces forgiveness.
Psa 25:11 — "pardon my guilt, for it is great" — no somatic language.
Amos 7:2 — "please forgive! How can Jacob stand?" — prostration/standing language implied but not somatic.

**H5546 (sallāch — forgiving):**
Psa 86:5 — single verse, no somatic language.

**H5547 (selichah — forgiveness):**
Psa 130:4 — no somatic language. Dan 9:9, Neh 9:17 — no somatic language.

---

### 4b — Somatic pattern summary

**Primary somatic evidence: the Luk 7:47 context (pericope surrounding the anchor).**
The woman's somatic acts — weeping, prostration at Jesus' feet, wiping with hair, anointing — are the most concentrated somatic expression in the corpus. These acts belong to the context of forgiveness received, not forgiveness extended. The body is expressing what has been received: the inner state of love produced by the forgiveness.

**Secondary somatic evidence: Mat 18:27 (*splagchnizomai*).**
The visceral compassion that precedes the forgiving act in the parable. This somatic signal points to forgiveness as arising from a body-involving compassion response — not pure cognition or will, but a movement that originates in the physical-emotional interior.

**Tertiary somatic evidence: Mat 18:35 ("from the heart").**
The heart as the required inner location of genuine forgiveness.

**Pattern summary:**
- The body is not prominently involved in the *act* of forgiving as such (no consistent somatic expression accompanies the direct forgiveness pronouncements in the corpus — Jesus says "your sins are forgiven" without described somatic accompaniment)
- The body *is* involved in:
  - The reception of forgiveness (weeping, prostration — expression of the inner transformation)
  - The compassion that precedes extending forgiveness (*splagchnizomai* — visceral origin)
  - The ritual mechanism of OT forgiveness (sacrificial acts — instrument)
- The somatic signature is primarily **expression** (body manifesting what has been received) with secondary **instrument** (body performing the ritual mechanism)
- The heart is named as the required inner locus — this is a somatic location but not a visible physical expression

**Somatic concentration: diffuse.** The forgiveness act itself is not consistently somatically expressed; the responses *to* receiving forgiveness are the primary somatic sites.

---

### 4c — Spirit-soul-body provisional classification

**Classification: Spirit-soul interface**

**Reasoning:**
Forgiveness in this corpus operates at a level that cannot be explained by natural human capacity alone. The human capacity to forgive is consistently presented as derivative of having received divine forgiveness — it requires an encounter with the divine at its foundation. This places it above the ordinary soul-level range of human characteristics. The consistent pattern in both testaments: forgiveness originates in God's character (*sallāch* — his disposition; *selichah* — his possession), flows down through divine acts (OT: cultic atonement; NT: Christ's blood and authority), and produces a transformed inner state in the recipient (love, reverential fear). The human act of forgiving (5377-002) is emphatically not self-generated — it is conditioned, commanded, and empowered by the experience of having been forgiven divinely.

However, forgiveness is not purely spirit-primary in the sense of being inaccessible to ordinary human experience. The corpus contains verses where human forgiveness is simply commanded as a practical relational act (Luk 17:3-4 — "if he repents, forgive him"). The command implies capacity — a person can comply with this instruction without necessarily having had a deep encounter with God's forgiving character. There is a soul-level dimension to forgiveness as an act of the will and the relational disposition.

The resolution: **spirit-soul interface**. At its fullest expression and deepest root, forgiveness is a spirit-level characteristic — originated in God, received from God, capable of transforming the inner person (love, fear) in ways that exceed natural capacity. At its practical exercise, it also operates at the soul level — as a decision of the relational will, within human reach when commanded. The two levels are not contradictory; they name the depth at which forgiveness can operate, with the spirit-level being the source and the soul-level being the exercise ground.

**Confidence: Medium.** The spirit-soul interface is a provisional assignment pending Session D synthesis. The deep-source argument is strong; the soul-level practical dimension is also present. No strong body-primary dimension.

**Somatic flag status:** Somatic evidence present (Luk 7:47 context, Mat 18:27) but not sufficient to affect the spirit-soul classification.

### Pass 4 complete. No new SD pointers beyond those already raised.


---

## PASS 5 — LANGUAGE AUDIT (Section 4 of word study)

### 5a — Accuracy audit against lexical data

**G0859 (aphesis):**
- Session C says "appears 62 times in the NT" — confirmed (occurrence_count = 62).
- Session C notes "legal and financial word" — confirmed by LSJ: remission of debt, cancellation, discharge from bond; formal releasing of prisoners.
- Session C notes Luk 4:18 as using *aphesis* translated "liberty" — confirmed (verse present in corpus; target_word = "liberty").
- Quality flags on this term: NO_WORD_ANALYSIS (meaning field is null for G0859; STEP returned no word analysis block), PROSE_ONLY_MEANING. This is a known STEP data limitation — the term has lexical data from Mounce and LSJ but no structured sense numbering from STEP. Session C Section 4 correctly describes this limitation implicitly by working from Mounce and LSJ. **Correction needed:** Session C describes the sense range accurately but does not note that the structured sense data is unavailable — this should be mentioned honestly in Section 4 as a data coverage note.

**G0863G/H/I (aphiēmi sub-glosses):**
- Session C describes occurrence count as 236 for the leave-sense — confirmed (G0863G occurrence_count = 236).
- Session C notes the forgiveness sense has 64 occurrences — confirmed (G0863H = 64).
- Session C notes the permit sense has 32 occurrences — confirmed (G0863I = 32).
- Session C total "332 NT occurrences of the same underlying verb" — **correction needed**: 236 + 64 + 32 = 332. This is the sum of the three sub-gloss occurrence counts, but these counts represent classified sub-uses within STEP's tagging — they do not necessarily add up to a non-overlapping total occurrence count of the lexeme. The actual occurrence count of the Greek lexeme *aphiēmi* in the NT is 143 according to most lexicons (Mounce notes it is "the most common of several Greek words meaning to forgive"). The STEP sub-gloss counts (236/64/32) represent the total STEP instances across the programme, not the NT occurrence count of the lexeme. Session C's statement "together these three sub-glosses represent 332 NT occurrences" is misleading. **Correction: Remove the claim about 332 NT occurrences; use Mounce's occurrence data for the lexeme, and note that the three sub-glosses reflect the programme's own classification of uses.**
- LSJ data for G0863G: confirms the classical range — send away, discharge, give up, divorce, remit, forgive. The Luk 4:18 use ("proclaim liberty") is within the LSJ classical sense of "release" (*aphesis*) as used for the freeing of prisoners. This is confirmed and was already incorporated in Session C.
- Causative stem: not present for any of the three sub-glosses — confirmed (causative_form_present = 0 for all). Session C does not claim causativity; correct.

**H5545 (sālach):**
- Session C states "occurring 49 times in the Old Testament" — confirmed (occurrence_count = 49).
- Session C notes "Qal: to forgive; Niphal: to be forgiven" — confirmed in meaning_parsed senses.
- Session C notes "no causative or intensive stem" — confirmed (causative_form_present = 0).
- Session C correctly observes that *sālach* is used almost exclusively of God as the acting subject. **Deepening needed:** The exclusivity is stronger than "almost" — within the verses in this corpus, there is *no* occurrence of *sālach* with a human subject. The claim should be stated more precisely: in all 49 occurrences recorded in this programme's corpus, *sālach* is used only of God. (Caveat: programme corpus may not represent every OT occurrence — the 49 is the programme's extracted count, not the exhaustive count. However, standard lexical scholarship confirms that *sālach* is exclusively divine in the OT.)

**H5546 (sallāch):**
- 1 occurrence — Psa 86:5 — confirmed.
- Session C notes it is "the only place in the entire Hebrew Bible where forgiveness is named as a stable character quality." Confirmed.
- The adjective form — confirmed: sense = "ready to forgive, forgiving."

**H5547 (selichah):**
- Session C states "occurring three times (Psalm 86:5, Psalm 130:4, Daniel 9:9)" — confirmed (occurrence_count = 3). Dan 9:9 is in the corpus; Neh 9:17 also present (880-001 group has 3 verses: Dan 9:9, Neh 9:17, Psa 130:4). **Correction needed:** Session C lists the occurrences as Psa 86:5, Psa 130:4, Dan 9:9 — but Neh 9:17 is the third verse in the 880-001 group, and Psa 86:5 uses H5546 (the adjective), not H5547 (the noun). The three occurrences of H5547 (*selichah*) are: Psa 130:4, Dan 9:9, Neh 9:17. Psa 86:5 should be attributed to H5546 (*sallāch*). **This is a factual error in Session C Section 4 that requires correction.**

### 5b — Completeness audit

- All 7 owner terms covered in Section 4. ✓
- Root family discussion: Session C discusses the AFE root (Greek) and SALACH root (Hebrew) but does not explicitly name the root codes — this is acceptable (reader-facing document; root codes are internal).
- Synthesis observation: Session C provides one and it is sound. It could be deepened with the specific noting of the spirit-soul interface character of the vocabulary family.
- Related words: Session C notes the primary related words (G0859 ↔ G0863G/H/I; H5545 ↔ H5546/H5547). H5548 (Salecah — a place name) appears in related_words for the Hebrew terms — correctly excluded from the word study discussion (place name, no inner-being relevance). ✓

### 5c — Language annotations

**LA-001:** G0859 occurrence count — confirm 62 in NT. No correction needed.
**LA-002:** G0863G/H/I occurrence counts — 236/64/32 confirmed as STEP sub-gloss counts. Remove the sum claim (332 "NT occurrences") — replace with lexeme-level statement. The combined corpus coverage across the three sub-glosses represents the programme's working verse set for this term family, not the total NT occurrence count of *aphiēmi* as a lexeme.
**LA-003:** H5547 (*selichah*) occurrences — correct the list: Psa 130:4, Dan 9:9, Neh 9:17 (not Psa 86:5). Psa 86:5 uses H5546 (*sallāch*, adjective).
**LA-004:** H5545 (*sālach*) — strengthen "almost exclusively" to "in this programme's corpus, exclusively of God as subject." Note scholarly consensus that *sālach* is divine-only in the OT.
**LA-005:** G0859 — add honest data coverage note: structured sense data from STEP was unavailable for this term (STEP did not return a word analysis block); Mounce and LSJ are the primary lexical sources used.

### Pass 5 complete. No new SD pointers.


---

## PASS 6 — CORRELATION AUDIT AND CONNECTION VERIFICATION

Reviewing all correlation signals against SD pointers already raised in Passes 1–5.

### All correlation signals

**XREF sharing:** 0 — no shared terms with other registries. Expected. No pointers needed.

**Verse cooccurrence (top 15 by shared verse count):**

| Registry | Word | Cluster | Shared verses | SD pointer coverage |
|---|---|---|---|---|
| 073 | guilt | C13 | 54 | SD-003, SD-004, SD-011, SD-014 — well covered |
| 187 | strength | C20 | 19 | Not yet flagged — see below |
| 111 | mercy | C17 | 16 | SD-002, SD-016 — covered |
| 135 | repentance | C13 | 12 | SD-003, SD-008, SD-014 — covered |
| 197 | authority | C20 | 10 | SD-007 — covered |
| 103 | love | C17 | 10 | SD-006, SD-010, SD-011, SD-016 — well covered |
| 059 | faith | C15 | 9 | SD-014 — partial; see below |
| 043 | desire | C04 | 8 | Not flagged — investigate |
| 184 | spirit | C01 | 7 | SD-005 (sanctification sequence) — partial |
| 213 | listen | C02 | 6 | SD-001 — covered (corporate faith/prayer context) |
| 128 | rebellion | C09 | 6 | SD-018 — covered |
| 057 | evil | C11 | 6 | Not flagged |
| 019 | calling | C19 | 6 | SD-009 — covered |
| 210 | deadness | C21 | 5 | SD-006, SD-018 — covered |
| 173 | will | C14 | 5 | Not flagged |

**Gaps to address:**

**Strength (187) — 19 shared verses, no SD pointer raised:**
19 shared verses is a substantial signal. Strength and forgiveness co-occurring 19 times requires investigation. Reading the group descriptions: strength appears as a C20 word (power cluster). The co-occurrence may reflect passages where God's forgiving act is described in terms of his power/strength (e.g., "according to the greatness of your steadfast love" — Num 14:19; "exalted him at his right hand as Leader and Savior" — Acts 5:31). The forgiveness that comes from divine strength is a theological statement about the cost of forgiveness: it requires divine power to forgive genuinely and at such scale. **SD-019:** 19 shared verses between forgiveness (064) and strength (187) suggest the forgiveness corpus frequently invokes divine power alongside divine forgiveness. Does the programme's treatment of strength/might/power (C20 cluster) address the relationship between divine omnipotence and the capacity to forgive at scale? Is forgiveness structurally dependent on strength in a way the C20 cluster analysis should examine?

**Faith (059) — 9 shared verses, only partial coverage:**
Faith and forgiveness share 9 verses. The pattern is clear from the corpus: repentance and faith are consistently the human conditions through which forgiveness is received (Acts 2:38, Acts 10:43, Acts 26:18, Luk 5:20 "when he saw their faith"). **SD-020:** The forgiveness corpus consistently pairs faith as the human instrument through which divine forgiveness is received. Is this causal (faith produces the conditions for forgiveness) or merely sequential (faith is the posture in which forgiveness is recognised)? Session D question implicating faith (059) and repentance (135) as the access-conditions to forgiveness.

**Desire (043) — 8 shared verses, not flagged:**
8 shared verses with desire (C04) is unexpected. Examining the pattern: the leave/abandon groups (5376) include verses about leaving behind earthly attachments for discipleship — which implies a reordering of desire. The forgiveness-as-releasing-act may connect to desire because both releasing a debt and releasing an attachment require the willingness to forgo something the inner person wants to retain. **SD-021:** Does the forgiveness corpus' structural leaving-act (releasing what is legitimately held) connect to the desire registry (043) through the shared inner-being grammar of relinquishment? When forgiveness requires forgoing the satisfaction of the retained claim, is there a desire-level reordering taking place? Session D question.

**Will (173) — 5 shared verses, not flagged:**
Will (C14) and forgiveness sharing 5 verses is consistent with the volitional character of the releasing-act (Volition dimension on group 5376-001). Forgiveness as a willful decision is present throughout the corpus. No new pointer needed — the connection is absorbed within the broader volitional dimension of forgiveness already addressed.

**Evil (057) — 6 shared verses:**
Evil and forgiveness co-occurring 6 times reflects the natural pairing: forgiveness addresses evil done by or to a person. The connection is structural (evil is what forgiveness responds to) rather than a deep inner-being relationship. **SD-022:** Does the evil registry (057) address the inner-being grammar of being the one who has committed evil and received forgiveness, versus being the one against whom evil was committed who must forgive? The forgiveness corpus treats both sides; does the evil corpus address the inner experience of the perpetrator who is forgiven?

**Dimension overlap review:**

5 registries share 5 dimensions with forgiveness: covenant (034), kindness (099), peace (117), strength (187), authority (197). The C17 cluster (covenant, kindness, peace, mercy, love, fellowship, grace, compassion) is the inner cluster for forgiveness — all these share Relational Disposition as the dominant dimension.

The C20 overlaps (strength, authority, might, dominion, power) are cross-cluster: 5 shared dimensions each. This is higher than expected for a relational-disposition word crossing into a power cluster. **The dimension overlap between forgiveness and the C20 power/authority cluster is analytically significant.** It confirms SD-007 (Christological authority claim) and SD-019 (divine strength and forgiveness scale). Flag confirmed.

**Deadness (210) — 5 shared dimensions.** The overlap is unexpected at first glance but consistent with the theologically negative groups in the forgiveness corpus (879-002, the unforgivable sin; the judgment language of 5379-002 where God refuses forgiveness). Deadness and the absence of forgiveness may co-occur in the same eschatological/judgment passages.

**Shared anchor verses:**

| Verse | Partner registry | Partner cluster |
|---|---|---|
| Jer 31:34 | guilt (073) | C13 |
| Jer 31:34 | thought (160) | C02 |
| Jer 31:34 | love (103) | C17 |
| Lev 4:20 | mercy (111) | C17 |
| Lev 4:20 | mercy (111) | C17 (duplicate entry) |
| Mar 3:29 | sin (147) | C11 |

The Lev 4:20 duplicate entry for mercy (111) is a data anomaly — the same anchor verse appears twice for the same partner registry. This is likely an extract artefact (two dimension index rows for the shared anchor rather than one). Note for Claude Code: not a blocking issue.

**Section 5 review against signals:**

Current Session C Section 5 connections vs. Pass 6 signals:

| Connection | In Section 5? | Signal confirmed? | Status |
|---|---|---|---|
| Guilt (073) | Yes | Cooccurrence (54) + shared anchor (Jer 31:34) | ✓ confirmed; priority HIGH correct |
| Mercy (111) | Yes | Cooccurrence (16) + shared anchor (Lev 4:20) | ✓ confirmed; priority HIGH correct |
| Grace (068) | Yes | Dimension overlap (3) | ✓ confirmed; priority HIGH correct |
| Repentance (135) | Yes | Cooccurrence (12) | ✓ confirmed; priority HIGH correct |
| Love (103) | Yes | Cooccurrence (10) + shared anchor (Jer 31:34) | ✓ confirmed; priority HIGH correct |
| Covenant (034) | Yes | Dimension overlap (5) | ✓ confirmed; priority Medium correct |
| Sin (147) | Yes | Shared anchor (Mar 3:29) | ✓ confirmed; priority Medium correct |
| Kindness (099) | Yes | Dimension overlap (5) | ✓ confirmed |
| Peace (117) | Yes | Dimension overlap (5) | ✓ confirmed |
| Compassion (023) | Yes | Dimension overlap (4) | ✓ confirmed |
| Deadness (210) | Yes | Dimension overlap (5) | ✓ confirmed |
| Strength (187) | **No** | Cooccurrence (19) | **ADD — HIGH priority signal** |
| Faith (059) | **No** | Cooccurrence (9) | **ADD — HIGH priority** |
| Desire (043) | **No** | Cooccurrence (8) | **ADD — Medium** |
| Authority (197) | **No** | Cooccurrence (10) + dimension overlap (5) | **ADD — Medium** |
| Evil (057) | **No** | Cooccurrence (6) | **ADD — Lower** |

**Section 5 additions required:** Strength, faith, desire, authority, evil — five connections confirmed by signals but absent from Session C Section 5.

### Pass 6 complete. New SD pointers: SD-019 through SD-022.
Total SD count: SD-001 through SD-022. **22 SD pointers raised across all passes.**


---

## SECTION 2.2 — SD POINTER COMPILATION

**SD pointer count: 22. Writing to observations log as authoritative record.**

| Flag label | Strongs | Partner reg | Priority | Summary |
|---|---|---|---|---|
| DIM-064-SD001 | G0863H | 213 | MEDIUM | Corporate faith mediates individual forgiveness (Mar 2:5/Luk 5:20); connects to listen/prayer/intercession cluster |
| DIM-064-SD002 | G0863H | 023 | HIGH | Mat 18:27 *splagchnizomai* — visceral compassion precedes forgiving act; compassion as inner-being precondition of forgiveness |
| DIM-064-SD003 | H5545 | 073,135 | HIGH | Atonement-mediated OT forgiveness vs. NT faith-mediated forgiveness; implications for inner-being prerequisites of receiving forgiveness |
| DIM-064-SD004 | H5545 | 073,103,160 | HIGH | Jer 31:34 shared anchor with guilt/love/thought — new covenant forgiveness as cognitive-relational joint act; remember no more |
| DIM-064-SD005 | G0859 | 019,207 | MEDIUM | Acts 26:18 conversion sequence: blindness→sight→forgiveness→sanctification — forgiveness as gateway inner-being state |
| DIM-064-SD006 | H5547 | 138 | HIGH | Psa 130:4 — forgiveness produces reverential fear; two downstream states from forgiveness (love Luk 7:47; fear Psa 130:4); connects to reverence registry |
| DIM-064-SD007 | G0863H | 197,199 | MEDIUM | Christological authority claim embedded in forgiveness pronouncements (Mar 2:7); authority-forgiveness structural connection |
| DIM-064-SD008 | G0863H | null | MEDIUM | Mat 6:14-15 reciprocal structure — received inner-being gift requires exercise for retention; pattern question for cross-registry |
| DIM-064-SD009 | G0863G | 019 | MEDIUM | Leaving-act in discipleship (Mar 10:29) encodes inner-being reordering connecting to calling; inner cost of vocation |
| DIM-064-SD010 | G0863G | 103,062 | MEDIUM | Rev 2:4 Ephesian pattern — orthodox conduct + abandoned love; inner-being dissociation between religious performance and relational disposition |
| DIM-064-SD011 | G0863H | 073,103 | HIGH | Three-registry causal chain: guilt→forgiveness→love (Luk 7:47); reproducibility across corpus; forgiveness as transitional state |
| DIM-064-SD012 | G0863H | null | LOWER | "From your heart" (Mat 18:35) — heart as forgiveness locus; cross-registry heart-as-faculty question |
| DIM-064-SD013 | G0863I | 023 | LOWER | Posture of welcome/receptivity (permit sense) and posture of forgiveness (release sense) — shared inner-being disposition question |
| DIM-064-SD014 | H5545 | 073,135,059 | HIGH | OT covenantal-objective vs NT experiential inner-being grammar of receiving forgiveness; two grammars or one fulfilled? |
| DIM-064-SD015 | H5545 | null | LOWER | Corporate dimension of forgiveness in OT intercession (Dan 9, Num 14, Amos 7) — communal inner-being states |
| DIM-064-SD016 | H5546 | 111,099 | HIGH | Psa 86:5 — forgiveness alongside goodness and *hesed*; systematic relationship between forgiveness and *hesed*-family in C17 |
| DIM-064-SD017 | G0859 | 068 | HIGH | Eph 1:7 — forgiveness "according to the riches of his grace"; grace as source-disposition upstream of forgiveness; inner-being hierarchy |
| DIM-064-SD018 | G0859 | 147,207,210,128 | MEDIUM | Mar 3:29 unforgivable sin — inner-being state of one for whom forgiveness is permanently inaccessible; deadness/blindness/rebellion connections |
| DIM-064-SD019 | G0859 | 187 | MEDIUM | 19 shared verses forgiveness-strength; divine power invoked alongside forgiveness at scale; C20 cluster question |
| DIM-064-SD020 | G0859 | 059,135 | HIGH | Faith as access condition to forgiveness consistently paired in NT; causal vs sequential question |
| DIM-064-SD021 | G0863G | 043 | MEDIUM | Leave/relinquishment act implicates desire reordering; inner grammar of forgoing the retained claim |
| DIM-064-SD022 | G0859 | 057 | LOWER | Evil as the object of forgiveness; perpetrator-experience dimension question |


---

## SECTION 2.2 — SD POINTER PERSISTENCE CONFIRMED

**Patch PATCH-20260412-064-SDPOINTERS-V1 applied manually by Claude Code — 2026-04-12**
**Patch PATCH-20260412-064-DIMCORRECT-V1 applied manually by Claude Code — 2026-04-12**
**GOD_AS_SUBJECT directive applied manually by Claude Code — 2026-04-12**

Note: `insert_research_flag` and `update_dimension_index` operation types not supported by applicator — both applied manually. Applicator gap noted for programme-wide tracking.

**SD pointer persistence confirmed: 22 SD_POINTER records in database. Observations log count: 22. Match: YES.**

**Group 879-002 dimension confirmed: Theological/Divine-Human | CLAUDE_AI | GOD.**

---

## SECTION 3.5 — PRE-STAGE 3b VALIDATION GATE

Observations log SD pointer count: 22.
Database SD_POINTER count: 22.
**Match confirmed. Proceeding to Stage 3.**


---

## SESSION CLOSE — Registry 064 (forgiveness)
**Date:** 2026-04-12

Stage 1: COMPLETE
Stage 2: COMPLETE — 22 SD pointers raised
Section 2.2: COMPLETE — 22 SD_POINTER records confirmed in database
Stage 3: COMPLETE — word study v2 produced (internal with completion note)
Stage 3b: COMPLETE — publication version v3 produced; completion note v2 produced as standalone
Stage 4: COMPLETE — closing patch produced; session_b_status = Analysis Complete

All mandatory outputs confirmed:
  [x] Observations log: wa-064-forgiveness-sessionB-observations-v1-2026-04-12.md
  [x] Analytical brief: wa-064-forgiveness-sessionB-brief-v1-2026-04-12.md
  [x] SD pointer patch: PATCH-20260412-064-SDPOINTERS-V1.json (applied)
  [x] Word study (internal): wa-064-forgiveness-word-study-v2-2026-04-12.md
  [x] Word study (publication): wa-064-forgiveness-word-study-v3-2026-04-12.md
  [x] Session C completion note: wa-064-forgiveness-sessionC-note-v2-2026-04-12.md
  [x] Closing patch: PATCH-20260412-064-ANALYSIS-V1.json (pending Claude Code confirmation)

Pending: closing patch confirmation from Claude Code.

