# WA Session Log — Session B Grace Analysis + Session D Architecture Design
## Framework B Soul Word Analysis Programme
### Date: 2026-04-09 | Status: Complete — ready for continuation

---

## Session Overview

This session covered two major workstreams:

1. **Session B analysis for grace (Registry 068)** — complete from instruction identification through patch production and Session C v2 document update
2. **Session D architecture design** — evaluation of the correlation extract and determination of what Session B must contribute to enable Session D synergy work

---

## Part 1 — Session B for Grace (Registry 068)

### 1.1 Instruction Identification

The session began with a request to perform Session B analysis on grace using "Session B instructions v3 in project files." Claude initially read the wrong instruction — `WA-SessionB-Analysis-Instruction-v5.7` (the pool-based analysis instruction from the project files). The researcher corrected this: the correct governing instruction is `Session-B-Instruction-v3.md`, uploaded by the researcher.

**Key finding from this confusion:** The project files contain the old pool-based instruction suite (v5.x series). The new instruction is v3, a fundamentally different design that the researcher uploaded directly. This discrepancy needs to be resolved in the project file set.

### 1.2 Instruction v3 — What to Attach

On reading Session B Instruction v3, the "What to Attach" section listed five separate Session C documents plus a completion note. The researcher clarified that all five sections and the completion note are produced as a single combined file.

**Action taken:** Updated Session B Instruction v3 to v3.1, amending the "What to Attach" section accordingly. File saved as `Session-B-Instruction-v3_1-2026-04-09.md`.

**Change note:** v3.1 — "What to Attach" updated: the five Session C reader-facing documents and the Session C completion note are produced and attached as a single combined file (`wa-[registry]-[word]-word-study.md`).

### 1.3 Input Files Used

- `wa-068-grace-complete-2026-04-09.json` — Registry 068 complete export (scope: complete, not pool format)
- `wa-068-grace-word-study.md` — Session C v1 combined document (Sections 1–5 + completion note)
- `Session-B-Instruction-v3_1-2026-04-09.md` — governing instruction

**Data anomaly identified during startup:** The JSON export is a registry complete export (`_export.scope = "complete"`), not the pool analysis dataset format specified by the old v5.x instruction. This was the correct format for Session B v3.

**Status fields at session start:**
- `verse_context_status`: Complete
- `session_b_status`: Verse Context Reset (DataPrep not yet run — noted as anomaly, proceeded because v3 does not require DataPrep as a gate)

### 1.4 Session B Five Passes — Findings

**Pass 1 — Meaning and Semantic Range**

- G5485 *charis*: semantic unity confirmed. The four apparent registers (disposition, gift, gratitude, commission) are contextual inflections of a single core concept — relational orientation moving from a greater toward a lesser that produces a concrete benefit. One genuine tension: "thanks" is the only sense where the recipient speaks rather than the giver acts, making it the full grace circuit compressed.
- G5483 *charizō*: the darker usage (Acts 25:11 — handing over a prisoner as political favour) is analytically significant. The structure of grace-giving is morally neutral in form; its character depends entirely on the giver's inner disposition. This has implications for spirit-soul-body classification.
- H2603B anomaly: gloss "be loathsome" inconsistent with grace registry. All verse assignments resolved to H2603A at span level. Identified as phantom entry — zero genuine corpus occurrences.
- Factual correction to Session C Section 4: G5485 occurrence count stated as "241 times in the NT alone" — conflates Mounce total NT count with programme's active verse set (88). Corrected in Session C v2.

**Pass 2 — Divine Dimension**

- `god_as_subject` = 0 on all nine active terms: confirmed data gap, not a genuine finding. God is the named agent in the majority of key anchor verses across G5485, G5483, G5487, H2580, H2587, H2603A.
- H8469 and H8467 (supplication terms): `god_as_subject` correctly retained at 0 — God is the addressee, not the agent.
- **Decision:** Patch `god_as_subject = 1` for G5485, G5483, G5487, H2580, H2587, H2603A.
- **Divine-human relationship pattern:** Three sub-patterns identified:
  1. Grace as sovereign gift — God gives, recipient receives and stands
  2. Grace as enabling force — God gives the capacity to respond (Zec 12:10: even supplication is given as grace)
  3. Grace as circuit — divine giving becomes ground of human giving (Eph 4:32)
- **Eschatological dimension:** Present in Rom 5:2, Acts 20:32, Zec 12:10. Full expression of grace is future; present standing is forward-oriented hope.

**Pass 3 — Verse Annotation**

All 13 available anchor verses annotated. Key contributions:
- Eph 2:8: the grammar of grace — subject, means, ruled-out alternative in one sentence. Faith is the channel, not the cause.
- 2Cor 12:9: grace as relational address, not impersonal provision. The refusal of relief that names what is being given.
- Luk 1:28: *kecharitōmenē* is perfect passive — completeness and persistence of the grace-state grammatically encoded.
- Eph 4:32: *eusplanchnoi* (tenderhearted) — a somatic term locating compassion in the deep interior. Grace as humanly extended is an inner-organ experience before it is a willed act.
- Zec 12:10: identified as the formal link in the corpus between grace, supplication, mourning, and repentance. Dual anchor verse (both H2580 and H8469). Grace enables repentance — the capacity to turn is itself given.
- Two supplementary verses flagged for future consideration: Psa 45:2 (grace poured on lips — somatic specificity) and Joel 2:13 (channun invoked as basis for repentance call).

**Pass 4 — Somatic Evidence and Spirit-Soul-Body Classification**

Full somatic scan across all owner terms revealed substantially richer somatic evidence than anchor verse selection showed. Primary somatic clusters:
- Eyes/gaze: the "find favour in the eyes of" formula (H2580) — 28 somatic verses. Grace is constitutively a matter of the gaze of the greater party.
- Prostration/face: Ruth (Rut 2:10), Esther (Est 8:3), Daniel (Dan 9:3), Joab (2Sa 14:22), the captain (2Ki 1:13) — consistent bodily enactment of the inner posture of grace-seeking.
- Weeping-supplication complex: Jer 3:21, 31:9; Zec 12:10; Est 8:3; Dan 9:3 — weeping accompanies supplication consistently.
- Heart: organ of both the plea and its reception (1Ki 8:47, Psa 119:58, Joel 2:13, 2Cor 8:16, Rom 6:17).
- Raised hands: Psa 28:2, 1Ki 8:38, 54 — directional reaching toward the source of grace.

**Provisional classification: Spirit-soul interface.** Reasoning: Grace originates at the spirit level (received as gift from above, not self-generated). Expressed at the soul level (desire for it, fear of being without it, transformed disposition). Enacted through the body (prostration, tears, raised hands, gracious speech). Confidence: high. Consistent across 194 active verses and all nine owner terms.

**`somatic_link` patches recommended:** H2580, H2603A, H8469, H8467 → set to 1.

**Pass 5 — Language Annotation and Terms Review Audit**

Five language annotations produced for Session C Section 4:
1. **Correction:** G5485 occurrence count — 88 active vs 241 total NT. Section 4 conflated these.
2. **Addition:** G5486 *charisma* (gift) — not in Session C but in G5483 related words list. Distinguishes *charis* (disposition and general expression) from *charisma* (specific gift endowment). Analytically significant given Rom 12:6, 1Cor 12.
3. **Deepening:** LSJ entry for G5485 — classical Greek background (Homer, 8th century BC) shows dual sense of inner disposition and external effect predates NT. NT adds unilateral divine initiative.
4. **Addition:** H2580 *chen* — "find favour in the eyes/sight of" as the dominant syntactic form, making grace constitutively tied to the act of being seen. Not in Session C.
5. **Deepening:** H8469 *tachanum* — eschatological reversal in Zec 12:10 (capacity for supplication is itself given as grace) not stated explicitly in Section 4. Needs strengthening.

### 1.5 Session B Analytical Brief

Produced: `wa-068-grace-session-b-brief-2026-04-09.md`

Sections: Registry summary / Meaning findings / Divine dimension summary / Somatic signature / Spirit-soul-body classification / Session C corrections and additions / Cross-word signals for Session D / Open questions / Database write-back recommendations.

**Cross-word signals for Session D identified:**
1. Grace ↔ Chesed: chen and chesed travel together in OT formulas. Does chen name the disposition of which chesed is the sustained expression?
2. Grace ↔ Forgiveness: charizō formally carries both senses. Forgiveness is a named expression of grace received.
3. Grace ↔ Repentance: Zec 12:10 and Joel 2:13 establish grace-precedes-repentance sequence.
4. Grace ↔ Hope: Rom 5:2 pairs standing in grace with rejoicing in hope.
5. Grace ↔ Identity formation: 1Cor 15:10 — "by the grace of God I am what I am."
6. Grace ↔ Lament: weeping-supplication complex connects grace-seeking posture to lament tradition.

**Open questions for researcher:**
1. H2603B data error — resolve before any write-back on that term.
2. Confirm god_as_subject patch for H8469 and H8467 (retained at 0 — addressee not agent).
3. Confirm meaning_numbered field scope — whether Session B should populate this for G5485.
4. Charisma G5486 — confirm whether registered elsewhere in the programme.

### 1.6 H2603B Investigation

Researcher uploaded STEP data for H2603B. Analysis showed:
- `vocab_count: 1` vs H2603A `vocab_count: 81`
- All 72 verses fetched under H2603B resolved at span level to H2603A (`span_code_found = H2603A` in all 72 cases)
- Zero genuine H2603B span hits

**Decision:** H2603B is a phantom entry — a theoretical lexicographical distinction with no recoverable textual presence in the STEP-tagged corpus. Should not be added as a registry word. Status → `delete`.

**Rationale:** No verse evidence; the theoretical semantic content ("to be loathsome") is not an inner-being characteristic in the programme's sense; data error in the grace registry now explained.

### 1.7 Session B Patch

**V1 produced and rejected by Claude Code:** OP-001 through OP-010 targeted `mti_terms` but `god_as_subject` and `somatic_link` exist on `wa_term_inventory`, not `mti_terms`.

**V2 produced:** `PATCH-20260409-068-SESSIONB-V2.json` — all 10 field updates retargeted to `wa_term_inventory` with `term_inv_id` as primary match key and `strongs_number` as verification field.

**Patch contents (18 operations):**
- OP-001–006: `god_as_subject → 1` on `wa_term_inventory` for G5485, G5483, G5487, H2580, H2587, H2603A
- OP-007–010: `somatic_link → 1` on `wa_term_inventory` for H2580, H2603A, H8469, H8467
- OP-011: H2603B → `delete` on `mti_terms` (phantom entry, zero corpus span hits)
- OP-012: `sb_classification = Spirit-soul interface`, `session_b_status = Analysis Complete` on `word_registry`
- OP-013–017: Five research flags (PH2-068-001 to 005) with flag_code `PH2_CROSS_REF_ENRICHMENT` — Grace-Forgiveness, Grace-Chesed, Grace-Repentance, Grace-Identity, Grace-Lament
- OP-018: Registry note referencing Session B brief

**Flag code issue noted:** The five grace flags were raised with `PH2_CROSS_REF_ENRICHMENT`. The old Extraction instruction required `SD_POINTER` for cross-registry observations to surface in SD pointer queries. This is a gap in Session B v3 — the instruction needs to specify the correct flag code for Session D observations. When the merged Session B instruction is written, this must be explicit.

### 1.8 Session C v2

Produced: `wa-068-grace-word-study-v2-2026-04-09.md`

**Changes from v1 to v2:**
- Section 1: Added closing paragraph — even the capacity to seek grace is itself given (Zec 12:10 finding).
- Section 2: Added somatic body-alignment paragraph (prostration, raised hands, fasting as body enacting the soul's posture). Added forward-directed hope as a dimension of standing in grace (Rom 5:2/Acts 20:32).
- Section 3: All 13 verse annotations replaced or substantially deepened. Notable: grammatical precision on *kecharitōmenē* as perfect passive; somatic register of *eusplanchnoi*; Zec 12:10 as formal grace-repentance link and dual anchor verse.
- Section 4: Five language annotation corrections applied. Occurrence count corrected; *charisma* G5486 added; LSJ classical background deepened; *chen* gaze formula added; *tachanum* eschatological reversal strengthened.
- Section 5: Two new connections added — Lament (formal and somatic) and Identity Formation (theological). Summary table updated to 10 connections.
- Section 6 (completion note): Updated to record all Session B outcomes, patches applied, H2603B deletion, sb_classification assignment, and questions carried forward to Session D.

### 1.9 Session D Readiness — Grace

**Current status:** `session_b_status = Analysis Complete` (pending patch application).

**What remains before grace is Session D-ready:** The Extraction session (v5.6) must run to produce:
- `wa-068-grace-json-[date].json` — Session B structured JSON
- Analysis completion patch (SESSIONB type) with evidential_status, dimensional profile, key findings
- `wa-068-grace-final-[date].json` — final registry extract
- `wa-068-grace-sdpointers-[date].json` — Session D pointers file
- Status advance to `Session B Complete`

**Open question raised (unresolved):** The Extraction instruction (v5.6) was written for the pool-based pipeline — it expects pool analysis datasets, pool narrative documents, pool context. The new v3 pipeline has none of these. Whether v5.6 can be adapted as-is or needs updating before the Extraction session runs for grace was not resolved in this session.

---

## Part 2 — Session B Instruction Consolidation Discussion

### 2.1 The Researcher's Instruction

The researcher stated: "My expectation is that you merge the actions for Session B into the v3 document following the completely new methodology of working with segments and then to set dimensions as the new consolidation mechanism to provision Session D."

### 2.2 Clarifying Questions Raised

Before drafting, two questions were asked:
1. What do you mean by "segments" as the new methodology?
2. When you say "dimensions as the consolidation mechanism to provision Session D", do you mean dimensions replace the SD pointer file, or dimensions become the organising structure within Session B?

The researcher indicated they would answer later and uploaded `wa-pooling-dimensions-comparison-2026-04-09.md` to provide context.

### 2.3 The Pooling-Dimensions Comparison Document — Key Content

The document established the following:

**The pool model** was designed to solve the XREF sharing problem — words sharing terms need to be analysed together. It defined 16 pool IDs (not stored in the database — defined in RMG Section 7a). The pool pipeline required DataPrep, pool assembly gate, and simultaneous analysis.

**Dimension Review** emerged as an intermediate stage between Verse Context and Session B that was not in the original v5.x design. It:
- Reviews all 3,469 contextual meaning groups across 22 clusters
- Assigns dimensions and dominant_subject to each group
- Corrects group descriptions
- Captures Session B findings and Session D pointers during review
- Has reviewed 820 of 3,469 groups (23.6%), with 3 clusters fully reviewed (C20–C22)

**Session B v3 (per-word model):**
- Input: complete word extract + Session C document
- No pool assembly gate
- No DataPrep prerequisite
- Five defined passes: Meaning, Divine Dimension, Verse Annotation, Somatic/Spirit-Soul-Body, Language Annotation
- Loses simultaneous XREF visibility (XREF data in extract but no OWNER-side verse context)

**The grace experiment** showed the per-word model is viable for independent words (not-shared, no critical XREF dependencies).

**Three grouping systems now coexist:**
- Clusters (C01–C22): for Dimension Review, stored in database
- Pools (16 IDs): for XREF-shared analysis, not stored in database, not yet triggered
- Dimensions (11 categories): per contextual meaning group in dimension_index

**Programme state at session date:**
- Phase 1: Complete — 182 registries
- Verse Context: Complete — 182 registries, 62,245 records
- Dimension Review: 8.8% — 16 registries, 3 clusters (C20–C22)
- DataPrep: Not started
- Pool Assembly: Not triggered
- Session B: 1 registry (grace, reg 068) at Analysis Complete via v3
- Session C: Not started formally
- Session D: Not started

### 2.4 Open Questions from the Comparison Document (Unresolved)

1. Does the pool model still apply for pool-connected words?
2. Is DataPrep still needed, or fold into Session B v3?
3. Should Dimension Review complete before Session B begins?
4. For pool-connected words (e.g. mercy + compassion), how is XREF context handled?
5. How do clusters, pools, and the per-word model coexist?

### 2.5 Researcher's Clarification on Session D Visualisation

The researcher stated: "At the moment, I cannot visualise how the output of Session C and B will be introduced to Session D to allow for synergy sessions that fits into the Claude AI limitations that remains a major stumbling block."

**Claude's assessment:** This is a design problem, not an instruction-writing problem. Writing a merged Session B instruction without resolving the Session D interface would embed assumptions. Suggested producing a Session D Input Design document using grace as a worked example.

---

## Part 3 — Session D Architecture Analysis

### 3.1 SD Pointer Dataset Evaluation

Researcher uploaded `wa-session-d-pointers-analysis-2026-04-09.json` (341 total records: 84 SD pointers + 167 session B findings + 90 other flags).

**Key findings from evaluation:**

**Coverage:**
- 63.7% of registries (116 of 182) have at least one pointer or finding
- Only 54 registries have formal SD_POINTER records
- C05 has no SD pointers at all; C21 has findings but no pointers
- All 12 high-priority pointers concentrated in C01, C03, C10, C11, C13, C14, C15, C19, C20

**Source distribution:**
- 84 SD_POINTER records come from old Session B Extraction (v5.1/v5.2) — March 2026 analysis
- 167 session_b_findings are predominantly (138) of type DIMENSION_REVIEW
- Dataset is shaped by Dimension Review, not completed Session B analysis

**Grace flags location:** The five grace research flags (PH2-068-001 to 005) are in `other_research_flags` under flag_code `PH2_CROSS_REF_ENRICHMENT` — correctly separate from the 84 SD_POINTER records but not surfacing in the SD pointer layer due to flag code mismatch.

**Structural architecture problem:** 41 of 84 SD pointers have no `cross_registry_id` — they are programme-level structural observations (e.g. "C01 has 21% Theological/Divine-Human density") sitting as flat text with no structured destination. These are analytically the most valuable but the least navigable.

**Conclusion:** The flags are too inconsistent to be the foundation for Session D. The researcher's conclusion: flags are not the right mechanism.

### 3.2 Identifying the Real Correlation Signals

The researcher asked: "I am trying to figure out what data exists to show that two things need to be correlated and investigated."

Analysis of the registry overview (`wa-registry-overview-20260406.json`) revealed three structural layers already in the database:

1. **Shared Strong's numbers** — objective, hard data. When two registries share the same Hebrew or Greek term, Scripture uses the same word in both semantic territories. 1,260 cross-cluster Strong's number connections identified. Top pairs: mind (C01) ↔ purpose (C02): 69 shared terms; hope (C04) ↔ trust (C15): 46 shared terms.

2. **Dimension co-occurrence** — 162 of 212 registries have dimension_profile data. Moral/Conscience + Spiritual/God-ward co-occur in 76 registries — the programme's dominant structural pairing.

3. **Dimension_profile as cross-registry grouping axis** — 52 registries active in Theological/Divine-Human; 110 in Spiritual/God-ward. Session D could receive one dimension at a time.

**Researcher's correction:** "You want to add descriptions embedded into prose files 213 of them, then scan through the prose — does not make sense." Claude acknowledged this correctly — the signals are structured data in the database. Claude Code queries them. Session D receives a structured dataset, not prose files.

### 3.3 The Correlation Extract

Researcher provided `wa-correlations-2026-04-09.json` — five structural signals mined from the database by Claude Code:

| Signal | Pairs Found | What It Detects |
|---|---|---|
| XREF term sharing | 452 pairs (≥3 shared Strong's) | Shared Hebrew/Greek vocabulary |
| Verse co-occurrence | 3,768 pairs (≥5 shared verses) | OWNER terms in same biblical verse |
| Dimension overlap | 154 pairs (≥2 shared dimensions) | Similar inner-being dimension profiles |
| Root family connections | 59 roots spanning 2+ registries | Etymological connections |
| Shared anchor verses | 1,230 instances | Same verse designated anchor by both |

**Composite scoring:** XREF ×2, co-occurrence ×0.5, dimension ×10, root ×15, anchor ×20. 141 pairs have 3+ signals converging.

**Claude's evaluation:**

*What works well:*
- Anchor verse signal is the most analytically precise — both words independently judged that verse to be their canonical demonstration. Convergence is not coincidental.
- Composite scoring with weights is sensible (root ×15, anchor ×20 correct).
- 141 multi-signal pairs is the right working set.
- Cross-cluster flag is the right filter — 151 of top 200 pairs are cross-cluster.

*Top cross-cluster pairs (score ≥150):*
- pride (C09) + strength (C20): 244
- heart (C01) + strength (C20): 206
- fear (C06) + strength (C20): 195
- purpose (C02) + heart (C01): 193
- courage (C08) + strength (C20): 184
- purpose (C02) + will (C14): 167
- delight (C03) + love (C17): 157
- awe (C03) + fear (C06): 146.5

*Verses shared as anchors by most registries:*
- Gen 6:5: 36 pairs, 34 cross-cluster
- Mic 6:8: 21 pairs, 18 cross-cluster (compassion, condemnation, goodness, humility)
- Gal 5:22: 15 pairs, 14 cross-cluster (faith, goodness, joy, love)
- Exo 34:6: 15 pairs, 14 cross-cluster (anger, compassion, faith)

*One gap flagged:* The verse co-occurrence signal does not distinguish whether terms appear as grammatical complements or merely in proximity. The anchor signal is cleaner. For Session D prioritisation, the anchor signal may need more weight, or co-occurrence should be filtered to verses where both terms are OWNER anchors.

*Cluster field missing from ranked_pairs:* Has to be reconstructed by joining back to signals layer. Minor fix needed in next extract version.

### 3.4 What Session B Must Add for Session D

Researcher's question: "What additional information must come out of Session B analysis that is not yet in the database to trigger Session D synergising work?"

**Key finding:** All five correlation signals exist without any Session B work. Session D can identify which word pairs to investigate right now. What Session B adds is what Session D reads when it investigates a pair — not what triggers the investigation.

**One exception — the only Session B output that directly affects signal quality:**

**`wa_term_inventory.evidential_status`** — currently NULL for all terms. Once populated, Claude Code can filter the XREF signal to use only `confirmed` and `plausible` terms. Currently every shared Strong's number is weighted equally, including instrumental and peripheral terms. This inflates some pair scores. The ranked pairs will shift after Session B runs. The correlation extract needs one regeneration pass after Session B completes across the programme.

**This is the one gate:** Do not run the programme-wide Session D synthesis until evidential_status is populated for at least the high-scoring pairs' terms.

**What Session B adds to make Session D better (not trigger conditions):**

| Output | Where Written | Session D Use |
|---|---|---|
| `evidential_status` | `wa_term_inventory` | Filters XREF signal — removes weak terms from pair scoring |
| `sb_classification` | `word_registry` | Sixth signal — pairs sharing same spirit/soul/body level |
| `wa_session_b_dimensions` | dedicated table | Dimension grouping axis for Session D packaging |
| `word_registry.description` (confirmed) | `word_registry` | What Claude AI reads to understand each word in a pair |
| `wa_session_b_findings` | dedicated table | Interpretive context for what the pair means |

**Practical Session D architecture that the correlation extract enables:**

Claude Code packages a Session D session as:
1. Filtered `ranked_pairs` — top N cross-cluster pairs with 3+ signals, cluster annotated
2. For each pair: the shared anchor verses (from `shared_anchor_verses` signal) with full verse text
3. For each pair: the shared Strong's numbers (from `xref_sharing`) with glosses
4. Registry descriptions for both words

Claude AI receives one pair or one thematically related group of pairs at a time. It reads the shared verses and answers: what is Scripture doing when these two words appear together?

This resolves the context limitation: Session D does not receive 212 words. It receives one pair at a time — typically 5–15 shared verses plus two word descriptions. Fully manageable.

**Practical sequence:**
- Session D can begin now on strongest cross-cluster pairs using current five signals
- Session B runs concurrently with Dimension Review completion
- As words complete Session B, `evidential_status` and `sb_classification` populate
- When enough words in a thematic group are complete, Claude Code regenerates the correlation extract for that group with filtered signal quality and the classification signal added
- Programme-wide Session D synthesis (Pass 3 per orientation document) waits until Session B is substantially complete

### 3.5 Researcher's Closing Assessment

"We are making progress. We are teasing out what Session B is responsible for to update or add to the database."

---

## Outputs Produced This Session

| File | Type | Description |
|---|---|---|
| `Session-B-Instruction-v3_1-2026-04-09.md` | MD | Updated instruction — "What to Attach" amended for single combined file |
| `wa-068-grace-session-b-brief-2026-04-09.md` | MD | Session B analytical brief — all five passes |
| `wa-068-grace-word-study-v2-2026-04-09.md` | MD | Session C v2 — all Session B annotations incorporated |
| `PATCH-20260409-068-SESSIONB-V1.json` | JSON | **Rejected** — wrong table (mti_terms instead of wa_term_inventory) |
| `PATCH-20260409-068-SESSIONB-V2.json` | JSON | **Corrected patch — ready for Claude Code** |

---

## Decisions Made

| Decision | Detail |
|---|---|
| H2603B | Delete — zero genuine corpus span hits, all 72 verses resolve to H2603A |
| god_as_subject | Patch to 1 for G5485, G5483, G5487, H2580, H2587, H2603A. Retain 0 for H8469, H8467 |
| somatic_link | Patch to 1 for H2580, H2603A, H8469, H8467 |
| sb_classification | Spirit-soul interface — high confidence |
| session_b_status | Analysis Complete (via OP-012 in patch) |
| Session B v3.1 | "What to Attach" updated for single combined Session C file |
| SD pointer flags | Grace flags raised as PH2_CROSS_REF_ENRICHMENT — needs correction to SD_POINTER in merged instruction |
| Session D triggers | Correlation signals (five) already exist without Session B. evidential_status is the one Session B output that directly affects signal quality and is a gate for programme-wide Session D synthesis |

---

## Open Items — Carry Forward to Next Session

### High Priority

1. **Merged Session B instruction** — the researcher's stated next step. Must consolidate DataPrep, Analysis (v3), and Extraction into one instruction. Key design questions still open:
   - Does DataPrep become a pass within Session B v3, or is it redundant given the complete extract?
   - What flag code should cross-registry Session D observations use? (Currently PH2_CROSS_REF_ENRICHMENT for grace — should be SD_POINTER for proper SD pointer extraction)
   - How does the merged instruction handle the Extraction outputs (evidential_status, dimensional profile, key findings, Session D pointers)?
   - Does the sdpointers file survive in the new architecture, or is it replaced by the structured correlation extract?

2. **"Segments" and "dimensions as consolidation mechanism"** — the researcher's design language was not fully defined before the session ended. This needs to be clarified at the start of the next session before the merged instruction is drafted.

3. **Grace Extraction** — the Extraction instruction (v5.6) was written for the pool-based pipeline and needs adaptation before it can be run for grace. Either adapt v5.6 or include extraction in the merged instruction.

4. **Cluster field on ranked_pairs** — correlation extract needs cluster annotation on ranked_pairs for Session D filtering. Minor Claude Code fix.

### Medium Priority

5. **Dimension overlap signal will strengthen** — currently only C20–C22 contribute. As Dimension Review progresses, regenerate the correlation extract. The dimension signal weight (×10) may need revisiting once more clusters complete.

6. **Co-occurrence signal quality** — consider filtering to verses where both terms are OWNER anchors rather than all co-occurring verse records. Would sharpen the signal.

7. **DataPrep status for grace** — grace reached Analysis Complete without DataPrep (no PREANALYSIS patch). This was flagged as anomalous but not blocked. When the merged instruction is written, the DataPrep question needs a definitive answer for existing registries.

8. **Programme-level flag inconsistency** — the session confirmed flags are too inconsistent to be the foundation for Session D. The flag layer should be treated as supplementary commentary only. No action needed, but the Session D design should not depend on flags.

### Lower Priority

9. **meaning_numbered field** — all nine active grace terms have meaning = null and meaning_numbered = null. Session B established sense structure for G5485 (four senses). Whether to populate meaning_numbered is a researcher decision.

10. **Charisma G5486** — not an owner term in grace registry. Analytical relationship to charis and charizō is significant. Confirm whether G5486 is registered elsewhere in the programme.

11. **Reference document update** — `WA-Reference-v5.5` Section 13.3 notes god_as_subject and somatic_link as "redundant fields — do not write in Session B pipeline." The grace patch wrote these fields. If they are superseded by the mti_term_flags mechanism as the Reference states, the patch approach for other registries needs to be confirmed against the current schema state.

---

## Programme State After This Session

| Stage | Status |
|---|---|
| Phase 1 | Complete — 182 registries |
| Verse Context | Complete — 182 registries |
| Dimension Review | C20–C22 complete; C01–C09 complete (per memory context); C10–C22 remaining |
| DataPrep | 0 registries at Pre-Analysis Complete |
| Session B | 1 registry (grace, reg 068) at Analysis Complete — pending patch application |
| Session C | 1 registry (grace, reg 068) at v2 |
| Session D | Not started — correlation extract ready for first pilot |

---

*WA-SessionLog-SessionB-SessionD-Design-2026-04-09 | Produced end of session 2026-04-09 | Covers full session from Session B grace analysis through Session D architecture design*
