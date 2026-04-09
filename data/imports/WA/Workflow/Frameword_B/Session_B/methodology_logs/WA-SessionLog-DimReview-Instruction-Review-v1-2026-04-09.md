# WA-SessionLog-DimReview-Instruction-Review-v1-2026-04-09

**Framework B — Soul Word Analysis Programme**
**Session Log — Dimension Review Instruction Review**
**Version 1.0 | 2026-04-09 | Status: Complete**

| **Field** | **Value** |
|---|---|
| Filename | WA-SessionLog-DimReview-Instruction-Review-v1-2026-04-09.md |
| Session date | 2026-04-09 |
| Previous output | None — opening review session |
| Session type | Analytical review — no patch produced |
| Governing instruction reviewed | WA-DimensionReview-Instruction-v1.6-2026-04-08 |
| Inputs reviewed | WA-VerseContext-Instruction-v2.5-20260409.md; WA-DimensionReview-Instruction-v1.6-2026-04-08.md; WA-SessionTranscript-2026-04-08-v1-20260409.docx; wa-root-family-full-extract-20260409.json |

---

## 1. Session Purpose

The researcher requested a review of the DimensionReview Instruction v1.6 in light of three new inputs:

1. **VerseContext v2.5** — the updated governing instruction for Verse Context work, superseding v2.4
2. **Session transcript 2026-04-08** — recording three bodies of work: VCB-031 (Registry 213 listen), the vertical pass experiment, and the H3820A lev REPAIR
3. **Root family full extract** — a new data structure produced by Claude Code linking groups to their Hebrew/Greek roots, registry assignments, and anchor verses

The review was conducted as analytical work only. No instruction update was drafted in this session. The session closes with documented gaps and two open questions for researcher decision before the instruction is updated.

---

## 2. Inputs Read

### 2.1 WA-VerseContext-Instruction-v2.5-20260409.md

Read in full. Two substantive additions relative to v2.4 were identified as relevant to this review:

**Addition 1 — `set_aside_reason` controlled vocabulary (Section 2.2 and 3.2):**
Five values added to the `verse_context` table: `no_inner_being`, `physical_only`, `spatial_only`, `wrong_face`, `other`. The `wrong_face` value is the vertical-pass-enabling value — it records that a verse contains inner-being content carried by a *different* term, enabling future cross-registry rediscovery without re-reading the corpus. Applies from VCB-032 onward.

**Addition 2 — Characteristic-perspective grouping model (Section 6.2 Step 3):**
The grouping rule was revised from term-centric to characteristic-perspective. The old rule asked what the term does in the verse; the new rule asks what inner-being characteristic the verse cluster is primarily about. A distinction between characteristic terms (naming an inner-being state directly) and property terms (describing how characteristics operate — mechanism, condition, expression, channel) is now explicit. Group descriptions must name the characteristic being served, with the term's role stated accurately relative to it. Applies from VCB-032 onward.

The companion document reference in the DimensionReview v1.6 header lists v2.4 as the governing companion. This is now outdated.

### 2.2 WA-DimensionReview-Instruction-v1.6-2026-04-08.md

Read in full. Key sections examined in relation to the new inputs:
- Section 2.1 (key fields — `context_description` as primary analytical input)
- Section 4.2–4.3 (Phase B quality criteria and quality flags)
- Section 4.6 (mandatory coverage verification)
- Section 5.1–5.3 (Phase C dimension discernment)
- Section 5.5 (cross-group patterns)
- Section 5.7 (dimension vocabulary)
- Section 6.4 (startup protocol)
- Section 9.1 (cluster extract specification)
- Section 9.3 (existing pointers extract specification)

### 2.3 WA-SessionTranscript-2026-04-08-v1-20260409.docx

Read via XML extraction. Three distinct bodies of work recorded in the transcript:

**Section 1 — VCB-031: Registry 213 (listen), 748 verses, 36 OWNER terms.**
Full classification documented term by term. 477 relevant, 271 set aside, 49 groups, patch applied. Registry 213: verse_context_status = Complete.

Notable: the session identified before classification began that several terms were likely homographs or AVF candidates (H0240, H4928, H4997, G0463, G1873, G1874, G1251, G1522). 57 deferred flags were raised and resolved in the flags register. Final distribution: 22 confirmed set aside, 33 confirmed include, 1 partial (DF-050 Isaiah 41–48 cluster).

Schema additions applied to the database before the patch:
- `verse_context_group.vertical_pass_flag` INTEGER DEFAULT 0
- `verse_context.vertical_pass_flag` INTEGER DEFAULT 0
- `verse_context.set_aside_reason` TEXT DEFAULT NULL

Set-aside reason distribution in VCB-031: `no_inner_being` 240, `divine_subject` 16, `wrong_face` 14, `avf_homograph` 1.

**Section 2 — Vertical Pass Experiment and Methodological Discovery.**

The researcher identified during flag review that the grouping work had been term-centric throughout VCB-031 — group descriptions named what the term does, not what the verse is about. The exchange is recorded as follows in the transcript:

> RESEARCHER: The groups in these flags highlight to me that many groups are going to be wrong. Verses are not properly read. It looks like the grouping focuses purely on the main term, but the verse often is primarily about another term; the main term is functioning as a qualifier, enhancer, or input.

> CLAUDE AI: You are identifying a classification error that runs through the grouping work: the group descriptions are being written as if the target term is the main subject of the verse, when in many cases the term is functioning as a qualifier, modifier, or channel — and the verse is primarily about something else.

This exchange produced the two-type distinction: *characteristic terms* (naming an inner-being state directly; removing the term removes the characteristic) vs *property terms* (describing how characteristics operate — mechanism, condition, expression, channel; can serve different characteristics in opposite ways across the corpus). The spectrum observation was also noted: the distinction may not be binary — there may be a spectrum from pure characteristic terms through relational characteristic terms, property/act terms, to purely functional terms.

The revised grouping model under the characteristic-perspective approach: groups are now clusters of verses in which the target term contributes to, expresses, resists, or channels the same inner-being characteristic, with the group description naming that characteristic and the term's role stated accurately relative to it. The session transcript documents the VCB-031 groups being rebuilt under this revised model before the patch was produced.

Three-verse vertical pass experiment: Jer 7:24, Rom 10:17, Isa 55:3. Each verse was pulled from the database and read across all registry faces simultaneously. Findings:

- *Jer 7:24*: Four term links (mo.e.tsah, she.ri.rut, o.zen, sha.ma) across three registries (32 counsel, 153 stubbornness, 213 listen). Characteristic map: she.ri.rut = root characteristic (stubbornness of the heart); mo.e.tsah = substitute inner orientation (autonomous counsel replacing divine guidance); sha.ma = property term naming the covenantal act absent; o.zen = property term naming the inner faculty closed. Critical absence: H3820A lev not in active term links — the word "hearts" (libbam) present in the verse but mti=581 incorrectly at status=delete. This triggered the repair investigation.

- *Rom 10:17*: Four term links (christos, pistis, ek, akoē) across four registries. Characteristic map: pistis = the destination (faith); akoē = property term (channel through which faith arrives); ek = directional connector; christos = source. Cross-registry confirmation: faith registry 59 classifies the same verse independently. VCB-031 group 7498-001 (faith received — akoē as channel) confirmed as correctly constructed.

- *Isa 55:3*: Eight term links across six registries (appetite, compassion, covenant × 2, despair, love, soul, listen). Most complex: six characteristics active simultaneously, no single registry face complete. Soul (ne.phesh) overarching subject; ear (o.zen) entry point; covenant, faithfulness, steadfast love the framework; soul-life (cha.yah) the promised outcome. Note: H0539 a.man in despair registry 44 unexpected — flagged for Session B. H2617B che.sed in compassion registry 23 set aside with null set_aside_reason (pre-VCB-031 record).

Programme-level findings from the vertical pass:
1. Many-to-many confirmed in live data
2. Characteristic vs property distinction holds in real verse evidence
3. Vertical pass model produces richer analytical output than any single registry face
4. Group descriptions validated by cross-registry confirmation
5. Vertical pass functions as a data quality probe (surfaced the lev deletion)
6. Three items flagged for Session B follow-up: H0539 a.man (reg 44), G1537 ek (reg 140), H2617B che.sed null reason

**Section 3 — REPAIR: H3820A lev (mti=581).**

Discovery: H3820A lev incorrectly set to status=delete during bulk cleanup. Status note on mti=581 explicitly read: *"THE primary Hebrew heart term — Must be extracted as the registry's anchor term"* — directly contradicting the delete status. Result: Registry 183 (heart) completed VCB without its canonical Hebrew anchor term.

REPAIR patch PATCH-20260408-REPAIR-LEV-H3820A-V1.json applied. Operations: mti=581 status → extracted; Registry 183 verse_context_status → In Progress. Applicator also applied beyond patch specification: delete_flagged=0, term_owner_type=OWNER on mti=581; 331 verse records restored to active. Session transcript notes this as a programme-level learning: future REPAIR patches involving term restoration should specify all three fields explicitly (status, delete_flagged, term_owner_type).

VCB-032 scoped: targeted session for H3820A lev (331 verses).

### 2.4 wa-root-family-full-extract-20260409.json

Partially read (structure, metadata, sampled entries). Produced by Claude Code on 2026-04-09.

Structure:
- 945 roots
- 3,077 groups
- All 3,077 groups have anchor verses populated
- Each root carries: `root_code`, `root_language`, `root_gloss`, `term_count`, `registry_count`, `group_count`, a `terms` array (strongs, transliteration, gloss, language, reg_no, reg_word), and a `groups` array
- Each group carries: `group_code`, `context_description`, `strongs_number`, `transliteration`, `gloss`, `registry_no`, `registry_word`, `dimension`, `dimension_confidence`, `dominant_subject`, `anchor_verses`

Key structural observations:
- 59 roots span more than one registry (cross-registry roots)
- Largest cross-registry examples by registry count: ATSAV (anguish/distress/grief/sorrow — 4 registries, 8 terms, 8 groups); LUPE (same four registries, 6 terms, 9 groups); AVAH (sorrow/desire/iniquity — 3 registries, 4 terms, 9 groups)
- Within-registry root families: e.g., ADIN root (delight — registry 42) with 6 terms and 5 groups; all terms in the same registry, analytically related by etymology
- The extract effectively provides a third axis of relationship (root-family axis) alongside the cluster axis (already in the dimension extract) and the registry axis

---

## 3. Gaps Identified

### Gap 1 — Characteristic-perspective model not reflected in Phase B quality criteria
**Location:** Sections 4.2, 4.3 of DimensionReview v1.6
**Urgency:** High — directly affects quality assessment of pre-v2.5 groups

The DimensionReview v1.6 Phase B quality criteria test whether a `context_description` "names an inner-being engagement" (Section 4.2, criterion 1) and "is specific enough to be distinct" (criterion 2). Under the old term-centric model, a description like *"Hearing as the inner receptive faculty (faith, understanding, response)"* would pass Phase B — it names an inner-being engagement (hearing), it is specific (one term's function). Under the characteristic-perspective model introduced in v2.5, the same description would be analytically inadequate: it names what the term does, not what the verse is about. The characteristic (faith, understanding) is named only parenthetically, and the term's role relative to that characteristic (channel, mechanism) is absent.

Phase B as currently written has no category for this type of inadequacy. The existing flags (`QA-VAGUE`, `QA-BROAD`, `QA-EXTERNALISED`, `QA-REVIEW`) do not map cleanly to the term-centric problem. `QA-EXTERNALISED` comes closest but technically means the description names an external act rather than an inner-being engagement — which is not exactly the problem with term-centric descriptions (those do name an inner-being engagement; they just name it from the wrong perspective).

The corpus of groups produced before VCB-032 was classified under the old model. The DimensionReview instruction does not currently distinguish between groups formed under the old and new models, and has no handling rule for the systematic rework that pre-v2.5 term-centric descriptions may require.

*This gap requires researcher decision before the instruction is updated. See Section 5, Question 2.*

### Gap 2 — Root family extract not integrated as a session input
**Location:** Sections 9.1, 9.3, 5.5 of DimensionReview v1.6
**Urgency:** Medium-High — new data is available; adds analytical depth available for Phase C and pointer capture

The DimensionReview cluster extract (Section 9.1) groups by cluster assignment. The root family extract groups by etymological/morphological root. These are different analytical axes:

- **Cluster axis**: semantic affinity of the English registry word
- **Root axis**: linguistic origin of the Hebrew/Greek term

The root axis surfaces two things the cluster extract does not:

1. *Intra-registry root families*: multiple terms in the same registry sharing a root. The ADIN root (delight) has 6 terms all in registry 42 — their groups are analytically related by more than cluster assignment. Phase C cross-group pattern detection (Section 5.5) would be richer if root-family relationships were visible.

2. *Cross-registry root families*: 59 roots span more than one registry. Examples: ATSAV and LUPE both span the anguish/distress/grief/sorrow cluster; AVAH spans sorrow/desire/iniquity. These are strong candidates for Session D pointers (same root generating inner-being vocabulary distributed across multiple registries). The existing Section 5.4 guidance on what to capture for Session D does not reference root-family evidence.

The extract provides 3,077 groups all with anchor verses populated — it is immediately usable as an analytical input. However, loading 945 roots and 3,077 groups for every cluster session would be excessive. A filtered version (roots whose terms appear in the cluster's registries) would be tractable. Whether this should be a standard input or an on-demand reference requires a researcher decision.

*This gap requires researcher decision before the instruction is updated. See Section 5, Question 1.*

### Gap 3 — Companion document reference to v2.4 outdated
**Location:** Header table of DimensionReview v1.6
**Urgency:** Low — maintenance fix, no analytical consequence in current sessions

The companion documents field lists `WA-VerseContext-Instruction-v2.4-20260403`. The governing Verse Context instruction is now v2.5. The reference should be updated. This is a mechanical change but matters for the document's self-standing integrity — any future reader would load v2.4 rather than v2.5.

### Gap 4 — Property-term dimension assignment logic not explicit in Phase C
**Location:** Sections 5.1–5.3, 5.7 of DimensionReview v1.6
**Urgency:** Medium — will resolve correctly in practice under "read the group, name what you see" but benefits from explicit guidance

The 11 current dimensions (Section 5.7) were derived from data predominantly composed of characteristic terms. Under the characteristic-perspective model, property-term groups carry the dimension of the *characteristic served through the term*, not the term's own function. For example: group 7498-001 (akoē/hearing — *"faith received — akoē as channel through which faith arrives"*) carries a dimension related to Volition or Cognition (faith-reception), not a dimension related to the sensory act of hearing. The term is a property term; the dimension is assigned to the characteristic it serves.

The instruction's Phase C already contains the right orientation: "read the group; name what you see" (Section 5.1). In practice, applying this rule to a well-formed characteristic-perspective group description will produce the correct result. However, the instruction does not currently make this explicit — a reviewer encountering a property-term group for the first time might attempt to assign a dimension to what the term does rather than to the characteristic served.

### Gap 5 — `wrong_face` set-aside data not surfaceable during Phase C
**Location:** Section 2.2 of DimensionReview v1.6
**Urgency:** Low — future vertical pass and cross-registry concern; not immediately blocking

VerseContext v2.5 introduces the `wrong_face` set-aside value, which preserves in the database the information that a verse contains inner-being content carried by a different term. During Phase C dimension assignment, Claude AI reads `context_description` and `anchor_verses` for each group. It does not have access to `wrong_face` set-aside records for the same term in other registries. Those records carry analytically significant cross-registry information.

For the current Dimension Review (clusters C10–C22 remaining), this gap does not block work. The `wrong_face` value will accumulate from VCB-032 onward; its analytical significance grows as the corpus builds. The mechanism to surface it (the rediscovery query in VerseContext v2.5 Section 3.6) is in place at the data layer but is not referenced from the DimensionReview instruction.

### Gap 6 — Startup protocol has no check for VCB completeness on full term set
**Location:** Section 6.4 of DimensionReview v1.6
**Urgency:** Medium — specific risk for Registry 183 (heart); may affect any registry repaired after VCB completion

The startup protocol (Section 6.4) requires confirmation of patch status, refinement log version, and existing pointer sequences. It does not include a check that each registry in the cluster has `verse_context_status = Complete` on its *full* term set — i.e., that no REPAIR has been applied since VCB completion that placed a registry back into In Progress.

Registry 183 (heart) is the immediate case: it shows `verse_context_status = Complete` from the original VCB run, but that completion is on an incomplete term set (H3820A lev was absent). Following REPAIR, Registry 183 is at In Progress pending VCB-032. If Registry 183's cluster were to enter Dimension Review before VCB-032 is applied, the cluster extract would be built on an incomplete group set for Registry 183.

The fix is a simple startup check: before proceeding with Phase A for any cluster, confirm that all registries assigned to that cluster have `verse_context_status = Complete`. If any are In Progress, halt and note the dependency.

---

## 4. Analytical Reflections

**On the root family extract as a structural input.** The significance of this extract is not merely that it provides additional data. It represents a third axis of analytical relationship that was not available when the DimensionReview instruction was designed. The cluster axis (semantic grouping by English registry word) and the root axis (etymological grouping by Hebrew/Greek term) are complementary but not redundant. A cluster groups words that the programme has determined to share inner-being affinity. A root family groups terms that share linguistic origin regardless of the programme's analytical judgements. Cross-registry root families (59 roots) are particularly valuable as independent evidence for inner-being relationships — they do not depend on the cluster assignment logic and therefore provide a check on it.

**On the characteristic-perspective model and the existing group corpus.** The methodology correction introduced in v2.5 has retrospective implications. The 3,077 groups in `wa_dimension_index` were not all produced under the same model. Groups from registries processed before VCB-031 (the large majority) were formed under the term-centric model. The Dimension Review Phase B quality gate was the intended point at which inadequate group descriptions would be caught and corrected. If Phase B's quality criteria are not updated to flag term-centric descriptions specifically, the correction may not be applied systematically. The DimensionReview Group Description Correction Protocol (Section 4.5) provides the mechanism for remediation — but it will only be triggered if Phase B correctly identifies the problem.

**On the vertical pass and the Dimension Review.** The vertical pass experiment confirms that the inner-being meaning of a verse is often distributed across multiple registries. The Dimension Review works registry by registry within a cluster. Phase C cross-group pattern detection (Section 5.5) encourages looking across groups within a cluster, but not across clusters or across registries in different clusters. The root family extract partially addresses this by providing a cross-cluster, cross-registry view. The full vertical pass architecture — reading a verse from multiple faces simultaneously — is beyond the Dimension Review's scope, but the root family data brings the cross-registry axis one step closer.

---

## 5. Open Questions for Researcher Decision

Two decisions are required before the DimensionReview instruction is updated. Both are presented with full context and Claude AI assessment.

### Question 1 — Root family extract: standard input or on-demand reference?

**Context.** The root family extract (945 roots, 3,077 groups, all with anchor verses) is available. It provides a cross-registry, root-based axis of analytical relationship not currently available in any other session input. 59 roots span more than one registry — these are the most analytically significant for Session D pointer capture.

**Option A — Standard session input (filtered by cluster).** Claude Code produces a root-family extract filtered to roots whose terms appear in the current cluster's registries, alongside the cluster extract and existing pointers extract. This would typically be a small file (most clusters have 4–10 registries; the root-family data for those registries is a small subset of the full 3,077 groups). Claude AI reads it at Phase C to inform cross-group pattern detection and Session D pointer capture.

**Option B — On-demand reference.** The full extract is available and can be consulted when a cross-registry pattern is suspected. Claude AI does not load it by default but may request a filtered query when a specific root-family relationship becomes analytically relevant.

**Claude AI assessment.** Option A is analytically stronger. The value of the root-family data is in *surfacing* patterns that would not be visible without it — patterns that are not suspected in advance. Option B requires knowing in advance that a root-family relationship exists, which reduces its value as a discovery tool. A filtered-by-cluster extract would be small and tractable. The cost is an additional Claude Code output per cluster session; the gain is richer Phase C analysis and more reliable Session D pointer capture.

### Question 2 — Pre-v2.5 term-centric group descriptions: new Phase B flag or existing flags?

**Context.** Groups produced before VCB-032 were formed under the term-centric model. Their `context_descriptions` name what the term does, not the characteristic served. Phase B as currently written may not reliably flag these as inadequate — they describe an inner-being engagement (even if from the wrong perspective) and are specific enough to be distinct. The existing `QA-EXTERNALISED` flag comes closest but is technically defined as naming an external act, not an inner-being engagement.

**Option A — New flag `QA-TERMCENTRIC`.** Add a specific flag category for descriptions that name what the term does rather than the characteristic served. This makes the systematic problem explicit and ensures it is handled consistently. Phase B reviewers have a clear criterion to apply.

**Option B — Apply existing flags.** Use `QA-VAGUE` (the description is not specific enough in terms of naming the characteristic) or `QA-REVIEW` (something warrants researcher attention) for term-centric descriptions. No new flag category is added.

**Claude AI assessment.** Option A is analytically cleaner and more consistent with the instruction's design principle of making quality problems explicit. The term-centric problem is a specific, identifiable inadequacy with a specific remediation (rewrite the description to name the characteristic and the term's role). Giving it a named flag ensures it is not resolved by vague correction decisions. Given that the majority of the existing corpus may be affected, a consistent handling rule is more important than saving a flag category.

---

## 6. Next Steps

| # | Action | Dependency | Owner |
|---|---|---|---|
| 1 | Researcher decision on Question 1 (root family extract: standard or on-demand) | This session log | Researcher |
| 2 | Researcher decision on Question 2 (term-centric flag: new category or existing) | This session log | Researcher |
| 3 | Update DimensionReview instruction to v1.7 incorporating decisions and all six gaps | Decisions 1 and 2 | Claude AI |
| 4 | VCB-032: classify H3820A lev (331 verses) — Registry 183 → Complete | REPAIR already applied | Next session |
| 5 | C10 Dimension Review: confirm Registry 183 cluster assignment; check VCB completeness before proceeding | VCB-032 must be complete | After VCB-032 |

---

## 7. Programme State at Session Close

| Item | State |
|---|---|
| Dimension Review | Clusters C01–C09 complete. C10 next. |
| DimensionReview instruction | v1.6 — review complete; v1.7 update pending researcher decisions |
| VerseContext instruction | v2.5 — governing from VCB-032 onward |
| Registry 213 (listen) | verse_context_status = Complete. VCB-031 applied. |
| Registry 183 (heart) | verse_context_status = In Progress. VCB-032 scoped. REPAIR applied. |
| Root family extract | wa-root-family-full-extract-20260409.json — available; integration into DimensionReview pending decision |
| Open questions | 2 (see Section 5) |

---

*WA-SessionLog-DimReview-Instruction-Review-v1-2026-04-09.md | Session date: 2026-04-09 | No previous output in this chain | Documents gaps between WA-DimensionReview-Instruction-v1.6 and WA-VerseContext-Instruction-v2.5; records findings from session transcript 2026-04-08 and root family extract structure*
