# WA-SessionB-Analysis-Instruction-v5_4-20260330

**Framework B — Soul Word Analysis Programme**

**Session B Analysis Instruction**

Version 5.4 | March 2026 | Status: Active governing instruction

| **Document** | **Value** |
|---|---|
| Filename | WA-SessionB-Analysis-Instruction-v5.6-20260330.md |
| Supersedes | WA-SessionB-Analysis-Instruction-v5.5-20260330.md |
| Change note | v5.6 — Section 4.4: mid-pool interruption detection added to status validation table — mixed pool states are a system failure requiring immediate stop and researcher notification. Section 12.4: failure patch rule added — if ANALYSIS patch is rejected, produce REPAIR failure patch before retrying. |
| Companion documents | WA-SessionB-DataPrep-Instruction-v5.4 │ WA-SessionB-Extraction-Instruction-v5.5 │ WA-VerseContext-Instruction-v1.2 │ WA-Reference-v5.4 |
| Inputs | Pool analysis dataset — wa-pool-{pool_id}-analysis-{date}.json |
| Outputs | Session B narrative — wa-{nnn}-{word}-analysis-{date}.md (one per word) │ Session B closing patch — PATCH-{date}-{nnn}-SESSIONB-V1.json (one per word) |
| Claude AI role | Analytical engine — reads pool dataset, performs all analysis, produces narrative documents and closing patches |
| Claude Code role | Pool analysis dataset construction, patch application, re-export |

---

## 0. Purpose and Scope

This document governs the Session B word analysis session — the session in which Claude AI reads the pool analysis dataset and produces a structured narrative analysis document for each word in the pool. It covers everything from startup through to final output.

This document does not govern:
- Data preparation and term classification — see WA-SessionB-DataPrep-Instruction-v5.3
- Pool analysis dataset construction — see WA-SessionB-ClaudeCode-Instructions-v2 Section 14.8
- Session B JSON extraction — see WA-SessionB-Extraction-Instruction-v5.3
- Registry management and programme state — see WA-Registry-Management-Guide-v5.4
- Session D capture and synthesis — see WA-SessionD-Orientation-v2.1
- Controlled vocabulary, schema, naming conventions — see WA-Reference-v5.3

| This document is self-standing. It does not rely on session memory. Everything Claude AI needs to perform a Session B Analysis is in this document and the pool analysis dataset. |
|---|

---

## 0.1 Pipeline Orientation

**Before this session begins:**
- Verse Context (Stage 1) has completed for all words in this pool. Every active OWNER term has contextual meaning groups and anchor verses designated in the database.
- Session B DataPrep has completed for all words in this pool. Every term has a deliberate mti_status — none are NULL.
- Claude Code has assembled the pool analysis dataset, which contains all the data needed for this session.

**What this session produces:**
- One standalone narrative document per word in the pool
- One Session B closing patch per word

**What happens next:**
- Claude Code applies the closing patches, sets session_b_status = Analysis Complete per word, re-exports each word's JSON
- Session B Extraction (WA-SessionB-Extraction-Instruction-v5.3) runs to produce the structured JSON outputs and Session D pointers

---

## 1. What Session B Is

Session B is the verse-grounded word analysis phase of the Framework B Soul Word Analysis Programme. It reads the pool analysis dataset — which contains anchor verses for each word's terms, grouped by contextual meaning — and produces a structured analysis of what the biblical text says about each word as a characteristic of the inner human being.

**Session B analyses a pool of words simultaneously.** Words sharing terms (via XREF relationships) are analysed together so that shared terms' inner-being content is visible within the session. Each word still produces its own standalone narrative document — the simultaneous reading serves the analysis, not the output format.

Session B is NOT:
- A dictionary exercise — the goal is not to define words but to read what the biblical text says about inner-being realities through those words
- A synthesis exercise — cross-pool patterns and whole-programme conclusions belong to Session D
- A theological commentary — Session B does not interpret passages for homiletical or doctrinal purposes
- A classification exercise — the concentric circle model defines scope, not category buckets

The governing method throughout Session B is: data first, interpretation second. Observations are anchored in specific anchor verses. No structural claim is made that cannot be traced to the verse corpus.

---

## 2. Working Definition of Inner Being

The inner being is the non-physical dimension of the human person — the seat of consciousness, emotion, will, moral disposition, relational capacity, and spiritual life. For this programme, the inner being is examined through three primary domains:

- **Spirit** (ruach / pneuma) — the dimension capable of direct relationship with God; the seat of spiritual life, worship, and divine communication
- **Soul** (nephesh / psyche) — the seat of desires, emotions, appetites, and relational life; the animating centre of personal existence
- **Body** (basar / soma) — the physical dimension, included because Scripture consistently portrays the body as both the instrument and expression of inner realities

These three domains are a working organisational frame, not a rigid classification system. Many characteristics operate across domains or at their boundaries. The frame organises the landscape; it does not dictate the findings.

| **⚠ Do not force findings into spirit/soul/body buckets. If a characteristic operates across domains, say so. The data drives the description.** |
|---|

---

## 3. The Scope Model — Concentric Circles

The concentric circle model defines scope. It answers: which relationships and entities are in scope when examining how the inner being of the human person functions?

| **Ring** | **Scope** |
|---|---|
| Ring 1 (innermost) | The human being's own inner life — spirit, soul, and body as described above. Primary object of study. |
| Ring 2 | The human being in relationship with God — divine-human encounter, God's action on the inner being, the human person's response toward God. |
| Ring 3 | The human being in relationship with other humans — interpersonal emotion, moral conduct, relational characteristics of the inner life. |
| Ring 4 (outermost) | The human being in relationship with the unseen world and living creatures. Included where these relationships illuminate inner-being characteristics. |

The scope model is used in Session B at two points:
- **Inclusion decision** — does this word have sufficient connection to the inner being to warrant full analysis?
- **Scope note** — which rings are active for this word? A descriptive observation, not a classification.

| **⚠ The circles define scope only — what is in scope and why. They do not describe how characteristics interact with each other or with God. That is Session D work.** |
|---|

---

## 4. Session Startup

### 4.1 Required Inputs

| **Input** | **Purpose** |
|---|---|
| This document (WA-SessionB-Analysis-Instruction-v5.2) | Governs all analytical behaviour for this session |
| Pool analysis dataset — wa-pool-{pool_id}-analysis-{date}.json | All words in the pool with their anchor verses, XREF term profiles, and cross-word map |

| No other documents are required. No session log. No prior chat memory. Everything needed is in these two inputs. |
|---|

### 4.2 Pool Session Model

**Primary approach — simultaneous analysis:**
Read all words in the pool together. All anchor verses across all words are loaded. Shared terms (XREFs) appear in the cross-word map. Produce one narrative per word, informed by the simultaneous reading.

**Fallback — word-by-word with XREF profiles:**
If the pool is too large for simultaneous reading (volume of anchor verses across all words exceeds what can be held in session), analyse words sequentially. For each word, the pool dataset's XREF term profiles remain available — shared terms' contextual groups and anchor references are present in the dataset even in sequential mode. Never produce a word analysis without XREF profile awareness.

**Determining the approach:** Read the pool dataset startup summary. Apply the following threshold:

**Current working threshold: approximately 9 words per pool.** If the pool contains more than approximately 9 words, default to word-by-word fallback unless the session context clearly allows simultaneous reading of the full anchor verse set. If the pool contains 9 or fewer words, use simultaneous analysis.

This threshold is subject to empirical revision as pool analyses proceed — it reflects current AI session capacity and will be updated as experience accumulates. State in the startup summary which approach is being used and the reason.

### 4.3 Startup Sequence

- Read this instruction document in full.
- Load and parse the pool analysis dataset.
- Read the meta block: pool_id, word list, cluster assignments, verse_context completion status per word.
- Confirm all words in the pool have `verse_context_status = Complete` and `session_b_status = Pre-Analysis Complete`.
- Read the cross-word map: identify shared terms across words in the pool.
- State the startup summary (Section 4.5).
- Determine session approach: simultaneous or word-by-word fallback.

### 4.4 Status Validation

| **Status combination** | **Required action** |
|---|---|
| verse_context_status = Complete AND session_b_status = Pre-Analysis Complete for ALL words | Proceed. This is the expected state. |
| verse_context_status = In Progress for any word | Stop. Pool is not ready. Verse Context has not completed for this word. Report to researcher. |
| session_b_status = NULL or Verse Context Reset for any word | Stop. DataPrep has not been run for this word. Report to researcher. |
| session_b_status = Analysis Complete or Session B Complete for any word | Note this word has been previously analysed. Confirm with researcher whether to re-analyse or skip. Do not duplicate analysis. |
| **Mixed states — some words at Pre-Analysis Complete, some at Analysis Complete** | **SYSTEM FAILURE — mid-pool interruption detected.** Stop immediately. Do not produce any analysis outputs. Produce a REPAIR mid-pool recovery patch for each word at Analysis Complete, resetting it to Pre-Analysis Complete. Report to researcher: which words are at which status, and that the pool must be re-run in full from Pre-Analysis Complete after the recovery patches are applied. See WA-SessionB-ClaudeCode-Instructions-v3.2 Section 15.4 for the recovery patch template. |

### 4.5 Startup Summary

```
Session B v5.2 startup complete.
Pool: {pool_id}
Words in pool: {n} — {list: registry_no — word}

Per-word status:
  {nnn} — {word}: verse_context_status={status} | session_b_status={status}
  [repeat]

Shared terms (cross-word map):
  {n} terms shared across words in this pool
  Highest sharing: {term} shared by {n} words

Total anchor verses: {n} across all words
Session approach: SIMULTANEOUS / WORD-BY-WORD FALLBACK

Ready to proceed.
```

---

## 5. Reading Protocol — Anchor Verses

Session B analysis is grounded in the anchor verses provided in the pool dataset. Verse Context has already filtered the full corpus — anchor verses are the canonical evidence for each term's inner-being engagement.

### 5.1 What anchor verses represent

Each anchor verse is the most clear and economical demonstration of a term's inner-being function within a specific contextual meaning group. Verse Context designated these carefully. The anchor verse, together with the group's `context_description`, is the primary analytical input for that term in that meaning context.

### 5.2 Reading rules

- Read every anchor verse provided for every active OWNER term across all words in the pool.
- Read each anchor verse in relation to its `context_description` — the description names what inner-being engagement to look for.
- Note the specific word form (`target_word`) occurring in the verse.
- Note how many related verses are in each group (the `related_count`) — this indicates the weight of evidence behind the anchor.
- A group with one anchor and many related verses carries more evidential weight than a group with one anchor and no related verses.

### 5.3 What to observe while reading

- What the verse says about the inner being directly — what it feels, does, experiences, or is characterised by
- Who or what is the subject — the human person, God, an external agent
- Whether the characteristic is presented as positive, negative, or neutral
- Whether the body is involved as instrument or expression
- Whether the verse connects this inner-being characteristic to another — especially to characteristics of words in the same pool

### 5.4 Reading discipline

Observations must be anchored in specific verses. Not acceptable as analytical foundations:
- General impressions without verse citation
- Theological conclusions beyond what the verses directly address
- Claims from XREF profiles that cannot be verified from anchor verse text in this pool (see Section 5.5)

| **⚠ Session B analysis is grounded in the anchor verses provided. You are not reading the full corpus — Verse Context has done that work. Work with what is provided. If an anchor verse is insufficient for a claim, note the limitation rather than supplementing from external knowledge.** |
|---|

### 5.5 XREF term profiles — how to use them

The pool dataset includes XREF term profiles for any term shared between words in this pool. A XREF profile contains:
- The term's Strong's number, transliteration, gloss, and mti_status
- The OWNER registry: which word owns this term
- The OWNER's verse_context_groups for this term: group_code, context_description, anchor verse references (not full text)

**How to use XREF profiles in analysis:**
- XREF profiles show how the OWNER registry classifies the shared term — what contextual meaning groups exist and what they describe
- Use them to understand the shared term's inner-being range as established by the OWNER analysis
- When describing how this word uses a shared term, you may reference the OWNER's contextual groups by their descriptions
- Do not quote anchor verse text from the OWNER registry's groups — that text is not in this dataset. Reference the group descriptions only.
- If the OWNER registry is also in this pool (simultaneous analysis), its full anchor verses are available and you may read them directly.

**XREF profiles and cross-word observations:**
When a term appears in two or more words in this pool, you can see directly how different words engage with the same term. Differences in contextual group usage between words are significant observations to include in the narrative as Session B findings — not deferred to Session D.

---

## 6. Evidential Status Framework

Every active OWNER term in the registry must be assigned an evidential status as part of the analysis. XREF terms do not require evidential status assignment — their status is inherited from the OWNER registry.

| **Evidential Status** | **When to assign** |
|---|---|
| confirmed | Term is clearly vocabulary for the inner being in this registry. Anchor verse evidence is direct and unambiguous. |
| plausible | Term is relevant to the inner being but evidence is indirect or depends on interpretive steps. Include with a brief note. |
| uncertain | Term's connection to the inner being is genuinely unclear from the anchor verses. Retain — do not exclude — but document the uncertainty explicitly. |
| instrumental | Term describes something that acts on the inner being from outside rather than being an inner-being characteristic itself. Retain with note. |
| relational_only | Term operates only in relational or social contexts with no direct inner-being referent. Retain with note. |

**The retention default:** All terms with any plausible connection are retained. A false exclusion is more costly than retaining a peripheral term. Evidential status documents confidence; it does not trigger exclusion.

**Retention notes:** Every term with status other than `confirmed` requires a brief retention note naming the question or uncertainty without resolving it.

---

## 7. Ten-Step Analysis Protocol

Every word analysis in the pool follows this sequence. Steps may be combined in output presentation but must all be completed for each word.

| **Step** | **Content** |
|---|---|
| 1. Registry overview | Word label, registry number, active OWNER term count, XREF term count, anchor verse count, language distribution, pool context (which other words are in this pool, what shared terms exist). Note any significant data quality issues. |
| 2. Term inventory review | Survey all active OWNER terms. Identify primary terms (high anchor verse count, clear semantic connection) and peripheral terms. Note XREF terms and their OWNER registries. Note any terms requiring evidential status below confirmed. Apply quality flag handling (see below). |
| 3. Scope assessment | Apply the concentric circle scope model. Which rings are active? Is the word clearly within inner-being scope or is its connection indirect? State the scope assessment explicitly. |
| 4. Root and etymology | For Hebrew terms: note the root family and any etymology illuminating the inner-being meaning. For Greek terms: note LXX connections to Hebrew vocabulary where relevant. Etymology is context, not argument. Apply root data absence rule (see below). |
| 5. Anchor verse reading | Read all anchor verses provided for all OWNER terms. Note contextual meaning groups and their descriptions. Follow the reading protocol in Section 5. Note intra-pool cross-word observations as potential Session B findings. |
| 6. XREF profile review | Read XREF term profiles for shared terms. Note how the OWNER registry classifies shared terms. Identify where this word's use of shared terms aligns with or diverges from the OWNER's contextual groups. |
| 7. Semantic range | Describe the semantic range of the primary OWNER terms based on anchor verse evidence. What does the word describe? What situations, states, or actions does it cover? |
| 8. Inner-being characterisation | What does this word tell us about the inner being of the human person? This is the core analytical question. Answer it from the anchor verse evidence. |
| 9. Dimensional profile | Which dimensions are present: relational environment, spirit-soul-body, inner operations, being/character? Note which are active with supporting observations. Do not force coverage of all dimensions. |
| 10. Evidential status assignment | Assign evidential status to every active OWNER term. Record retention notes for all non-confirmed terms. |

**Step 2 — Quality flag handling:** The pool dataset includes quality_flags and phase2_flags arrays on each OWNER term. Handle these as follows:

| Flag type | Action |
|---|---|
| PH2_VOLUME_LIMITATION, THIN_DATA, SMALL_VERSE_SAMPLE | Add a caution note in the analysis: evidence is thin for this term; analytical weight should reflect the limited corpus. Note in evidential status. |
| HIGH_FREQUENCY_ANCHOR | Note that the term's anchor verse coverage may be incomplete due to high occurrence count. Analytical claims should be qualified accordingly. |
| PH2_CROSS_REGISTRY_REQUIRED, PH2_BOUNDARY_QUESTION | Record as a Session D pointer — these require cross-pool visibility to resolve. Do not attempt to resolve within this session. |
| PH2_DATA_ERROR, SPAN_RESOLUTION_CONFLICT | Note the data quality issue in the registry overview. Analytical claims relying on affected verses should be qualified. |
| CONCRETE_PHYSICAL, SPAN_FILTER_APPLIED | Informational only — note in term inventory review if relevant to scope assessment. No analytical qualification required. |
| All other flag types | Review flag description; use judgement — if analytically significant, note it; if administrative, no action needed. |

**Step 4 — Root data absence rule:** Root_family data is not currently included in the pool analysis dataset structure. If root data is absent for a term, note this explicitly in the Step 4 section of the narrative and proceed without it. Do not draw on prior knowledge of root families external to the dataset. Where root etymology is analytically significant and root data is missing, record this as a Session D enrichment item: "Root data unavailable for {term} — etymology warrants further investigation."

---

## 8. Dimensional Framework

| **Dimension** | **What it covers** |
|---|---|
| Relational environment | How this characteristic manifests in relationships — with God, other humans, the created world. Corresponds to outer scope rings. |
| Spirit-soul-body | Which domain(s) of the inner being are primarily engaged — spiritual, psychic/soulish, or somatic/bodily. |
| Inner operations | The functional dynamics — how it is triggered, develops, what it produces, what it responds to. |
| Being / character | Whether this characteristic is presented as a formed disposition, moral quality, or aspect of identity — something the person is, not merely experiences. |

| The dimensional profile is descriptive: this characteristic is active in these dimensions. It does not mean: this characteristic belongs exclusively to this dimension. Multiple dimensions may be simultaneously active. |
|---|

---

## 9. Science Framework

Session B does not engage scientific literature. This rule is absolute:

| **⚠ No references to neuroscience, psychology, cognitive science, or any other scientific field in Session B output. Science engagement is deferred to Session D. If a scientific parallel surfaces during analysis, note it briefly as a Session D observation and do not develop it.** |
|---|

This rule protects the data-first methodology. Scientific frameworks risk fitting biblical data to modern categories rather than allowing categories to emerge from the corpus.

---

## 10. Cross-Word Observations and Session D Boundary

### 10.1 Intra-pool observations — Session B findings

When analysing a pool simultaneously, cross-word observations for words in the same pool are **Session B findings**, not Session D pointers. These belong in the narrative.

This includes:
- How two words in the pool use the same term differently or similarly
- Where anchor verses for different words in the pool address the same inner-being situation
- How words in the pool relate to each other conceptually — one being the precondition for another, one being the resolution of another, etc.
- Where the XREF profile shows a term shared between pool words with divergent contextual group usage

These observations are made in the narrative's inner-being characterisation section (Step 8) and documented in the pool findings block of the compliance statement.

### 10.2 Cross-pool observations — Session D pointers

Observations that require comparing this pool's findings with words in a different pool belong in Session D pointers, not the narrative. These are structural observations only — no interpretation.

What qualifies as a Session D pointer:
- A term present in this pool and in one or more other pools — structural observation, not analysis
- A pattern visible in this pool's findings that may extend to other pools — flagged as a hypothesis, not a conclusion
- Conceptual dynamics that require whole-programme visibility to assess — e.g. how this pool's characteristics interact with characteristics from unrelated pools

| **⚠ The boundary is the pool. What you can see within the pool's simultaneous data belongs in the narrative. What requires looking beyond the pool belongs in Session D pointers.** |
|---|

### 10.3 Verse overlaps with other pools

Where an anchor verse in this pool is known to appear in a registry outside this pool, record it as a Session D pointer. Do not analyse the overlap — record the structural fact.

---

## 11. Output — Per-Word Narrative Document

### 11.1 One narrative per word — standalone

Each word in the pool produces one narrative document. The analysis may have been derived from simultaneous reading of multiple words, but each document stands alone. A reader of a single word's narrative should not need to read another word's narrative to understand it.

This means:
- Intra-pool cross-word observations are written into each word's narrative where they are relevant to that word's characterisation
- Each narrative references the pool context in Section 1 but stands independently as an analysis of that word
- Do not produce combined pool narratives or documents that span multiple words

### 11.2 File naming

```
wa-{nnn}-{word}-analysis-{YYYYMMDD}.md
Example: wa-069-gratitude-analysis-20260329.md
```

One file per word. Produce all word narratives before producing any closing patches.

### 11.3 Required sections

| **Section** | **Content** |
|---|---|
| 1. Registry overview | Meta: registry number, word, pool context, OWNER term count, XREF term count, anchor verse count, language distribution, data quality notes |
| 2. Scope assessment | Concentric circle scope rings active, inclusion rationale |
| 3. Term inventory | All active OWNER terms with evidential status and retention notes. XREF terms listed with OWNER registry noted. |
| 4. Root and etymology | Root family, etymological notes, LXX connections where relevant |
| 5. Semantic range | What the primary OWNER terms cover, how they function in the biblical text, based on anchor verse evidence |
| 6. Inner-being characterisation | Core finding: what this word tells us about the inner being. Include intra-pool cross-word observations where relevant. |
| 7. Dimensional profile | Which dimensions are active and why, based on anchor verse evidence |
| 8. Key verse observations | The most significant anchor verses for this analysis with brief annotations explaining what each contributes |
| 9. Evidential status summary | Consolidated table: all OWNER terms with evidential status and retention notes |
| 10. Session D pointers | Cross-pool and whole-programme observations only — structural facts, no interpretation |
| 11. Compliance statement | See Section 11.4 |

### 11.4 Compliance statement

Required text — include in Section 11 of every narrative:

```
This analysis was produced under WA-SessionB-Analysis-Instruction-v5.2-20260329.

Pool: {pool_id}
Words analysed simultaneously / word-by-word fallback: {state which}
Anchor verse reading: complete for all active OWNER terms.
Evidential status assigned to all OWNER terms.

Intra-pool cross-word observations incorporated: {n}
  {brief list of key observations included in narrative}

Session D pointers recorded: {n} (cross-pool / whole-programme observations only)

The Session B closing patch has been produced and submitted to Claude Code.
This document stands alone as a complete analysis of {word} ({registry_nnn}).
```

### 11.5 Output quality standards

- Every claim is backed by an anchor verse citation
- No synthesis propositions — observations connecting this word to registries outside this pool belong in Section 10 (Session D pointers), not in the body analysis
- No scientific references
- Evidential status assigned to every active OWNER term
- Retention note provided for every non-confirmed term
- The analysis describes what the biblical text says, not what the analyst thinks the text means in a broader framework

---

## 12. Session B Closing Patch

When all narrative documents for the pool are complete, produce one closing patch per word before ending the session.

### 12.1 What the closing patch contains

This patch is a lightweight status-advance patch — it is NOT the full Session B data extraction patch. The full analytical data (evidential status on `wa_term_inventory`, dimensional profile, key findings, SD pointer flags, word_registry.dimensions, word_registry.description) is written by the Extraction session's analysis completion patch (SESSIONB type).

This patch does only two things:
- A `registry_note` recording the analysis document filename
- An `update_registry` operation setting `session_b_status = Analysis Complete` as the final operation

**No term-level writes in this patch.** `mti_terms.status_note` is NOT written here. All term-level analytical results belong in the Extraction patch. The Analysis session's sole DB output is the status advance and the filename note.

**Researcher checkpoint rule:** If a situation arises during an Analysis session that appears to require a bulk field update on mti_terms or any other table, and no standard patch operation covers it — stop. Do not construct a patch. Surface a field-level proposal to the researcher describing: the table, the fields to be updated, the proposed values, the derivation rule, and the operation count. Wait for explicit researcher approval before constructing any patch operation not covered by this instruction.

### 12.2 Patch file naming

To avoid conflict with the Extraction session's analysis completion patch (which uses SESSIONB type), this patch is named with an `-ANALYSIS-` infix:

```
PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1.json
Example: PATCH-20260330-069-ANALYSIS-V1.json
```

One patch per word.

### 12.3 Patch format

Patch format follows patch_specification_v1.4. Key requirements:
- `patch_id` format: `PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1`
- `patch_type` in `_patch_meta`: `"SESSIONB"`
- `session_b_status` in `_patch_meta`: `"Analysis Complete"`
- Closing `_patch_summary` block required
- `update_registry` setting `session_b_status = Analysis Complete` must be the final operation

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1",
    "registry_id": 0,
    "word": "{word}",
    "pool_id": "{pool_id}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-Analysis-Instruction-v5.4",
    "patch_type": "SESSIONB",
    "session_b_status": "Analysis Complete",
    "description": "Session B analysis complete — status advance — registry {nnn} — {word}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "registry_note",
      "description": "Analysis document: wa-{nnn}-{word}-analysis-{date}.md — pool: {pool_id}"
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": 0,
      "set": { "session_b_status": "Analysis Complete" },
      "description": "Session B analysis complete — pool {pool_id}"
    }
  ],
  "_patch_summary": {
    "total_operations": 2,
    "registry_notes": 1,
    "update_registry": 1
  }
}
```

### 12.4 Handoff to Claude Code

```
PATCH SUBMISSION TO CLAUDE CODE

Pool: {pool_id}
Patches: {n} files — one per word (ANALYSIS type)

For each patch:
  File: PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1.json
  Registry: {nnn} — {word}
  Action required:
    1. Apply patch — registry_note and update_registry only
    2. Confirm session_b_status = Analysis Complete on word_registry
    3. Re-export JSON as wa-{nnn}-{word}-extract-{date}.json
    4. Confirm re-export complete

When all {n} words in pool are at Analysis Complete:
  Report to researcher — pool ready for Session B Extraction
```

**If any ANALYSIS patch is rejected by the applicator:** Produce a REPAIR failure patch immediately for that word (patch naming: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1`; patch_type: REPAIR; session_b_status: current unchanged value; one registry_note recording the failure). Submit the failure patch. Report to researcher: which patch was rejected, the rejection reason, and the failure patch_id. Do not proceed with any remaining pool patches or Extraction until the researcher has reviewed. See WA-SessionB-ClaudeCode-Instructions-v3.2 Section 16 for the failure patch template.

| This session ends when all narrative documents are complete AND all ANALYSIS patches are submitted to Claude Code. Do not end the session with narratives only. Do not produce JSON extraction in this session — that is the Extraction session's responsibility (WA-SessionB-Extraction-Instruction-v5.4). The Extraction session produces the full analytical data patch (SESSIONB type) with evidential status, dimensions, findings, SD pointer flags, and word_registry field updates. |
|---|

---

## 13. Researcher Compliance Rules

| **⚠ Do not make assumptions or guesses. When uncertain, stop, present the evidence, state the uncertainty, offer options, and ask the researcher. Do not proceed on a best guess.** |
|---|

### 13.1 When to stop and ask

- A term's scope is ambiguous and the anchor verses do not resolve it
- A term sits at the boundary between two registries
- The registry status is inconsistent with the requested work
- A data anomaly is present with no clear explanation
- A scope decision would materially affect the analysis
- An anchor verse is insufficient as sole evidence for a claim

### 13.2 Source transparency

When a definition or interpretation has multiple possible sources, state the source explicitly:
- **Gloss-based** — from the STEP gloss or Strong's entry
- **Anchor-verse-based** — observation derived from reading the anchor verse(s)
- **Context-description-based** — inferred from the Verse Context group description
- **XREF-profile-based** — derived from the OWNER registry's contextual classification
- **Researcher instruction** — direction received in this session

### 13.3 Assumption labelling

Where Claude AI has proceeded on an assumption that could not be confirmed, label it explicitly: *Assumption: [statement] — confirm with researcher.*

### 13.4 Session D boundary

| **⚠ The most common compliance failure is crossing from observation into synthesis. Session B describes what each word means within the context of its pool. Session D asks what the full programme's data reveals when all pools are considered together. Do not cross that boundary.** |
|---|

---

## Annexure A — Session B Narrative Document Template

File naming: `wa-{nnn}-{word}-analysis-{YYYYMMDD}.md`

---

**Document header block:**

| **Field** | **Value** |
|---|---|
| Registry number | {nnn} |
| Word | {word} |
| Analysis date | {YYYYMMDD} |
| Pool | {pool_id} |
| Session approach | {simultaneous / word-by-word fallback} |
| Active OWNER terms | {n} |
| XREF terms | {n} |
| Anchor verses (total) | {n} |
| Instruction version | WA-SessionB-Analysis-Instruction-v5.2 |
| Pool dataset | wa-pool-{pool_id}-analysis-{date}.json |
| session_b_status at analysis | Pre-Analysis Complete |

---

**Section 1: Registry Overview**

{Word label, registry number, pool membership and shared terms summary, term count, anchor verse count, language distribution. Data quality notes from DataPrep if any.}

**Section 2: Scope Assessment**

{Concentric circle rings active. Inclusion rationale. Whether word is clearly within scope or connection to inner being is indirect.}

**Section 3: Term Inventory**

{All active OWNER terms — strongs_number, transliteration, gloss, evidential status, retention note (for non-confirmed).}
{XREF terms — strongs_number, gloss, OWNER registry, mti_status.}

**Section 4: Root and Etymology**

{Root families for Hebrew terms. LXX connections for Greek terms. Etymology as context, not argument.}

**Section 5: Semantic Range**

{What the primary OWNER terms cover based on anchor verse evidence. What situations, states, or actions the word describes.}

**Section 6: Inner-Being Characterisation**

{Core finding: what this word tells us about the inner being. Ground every claim in anchor verse evidence. Include intra-pool cross-word observations where they illuminate this word's characterisation.}

**Section 7: Dimensional Profile**

{Dimensions active — relational environment, spirit-soul-body, inner operations, being/character. Supporting observations per active dimension. State explicitly if a dimension is not evidenced.}

**Section 8: Key Verse Observations**

{Most significant anchor verses — reference, verse text, brief annotation explaining what this verse contributes to the analysis. Group by contextual meaning group or by term.}

**Section 9: Evidential Status Summary**

| Term | Transliteration | Language | Evidential Status | Retention Note |
|---|---|---|---|---|
| {H/Gnnnn} | {text} | {Hebrew/Greek} | {status} | {note or null} |

**Section 10: Session D Pointers**

{Cross-pool and whole-programme observations only. Structural facts — no interpretation.}
{Format: pointer_id, observation, registries implicated, why it cannot be resolved within this pool.}

**Section 11: Compliance Statement**

```
This analysis was produced under WA-SessionB-Analysis-Instruction-v5.2-20260329.

Pool: {pool_id}
Words analysed simultaneously / word-by-word fallback: {state which}
Anchor verse reading: complete for all active OWNER terms.
Evidential status assigned to all OWNER terms.

Intra-pool cross-word observations incorporated: {n}
  {brief list}

Session D pointers recorded: {n}

The Session B closing patch has been produced and submitted to Claude Code.
This document stands alone as a complete analysis of {word} (registry {nnn}).
```

---

## Annexure B — Pool Analysis Dataset Structure

File naming: `wa-pool-{pool_id}-analysis-{date}.json`

This dataset is constructed by Claude Code per WA-SessionB-ClaudeCode-Instructions-v2 Section 14.8. Its structure is specified here for Claude AI's reference when reading the dataset.

```json
{
  "meta": {
    "pool_id": "{pool_id}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "Claude Code — WA-SessionB-ClaudeCode-Instructions-v2",
    "governing_instruction": "WA-SessionB-Analysis-Instruction-v5.2-20260329.md",
    "word_count": 0,
    "total_anchor_verses": 0
  },
  "words": [
    {
      "registry_id": 0,
      "word": "{word}",
      "cluster_assignment": "{cluster_id}",
      "session_b_status": "Pre-Analysis Complete",
      "verse_context_status": "Complete",
      "phase1_term_count": 0,
      "phase1_verse_count": 0,
      "owner_terms": [
        {
          "mti_term_id": 0,
          "strongs_number": "{H/Gnnnn}",
          "transliteration": "{text}",
          "gloss": "{text}",
          "language": "{Hebrew or Greek}",
          "mti_status": "{extracted or extracted_thin}",
          "quality_flags": [],
          "phase2_flags": [],
          "total_verses": 0,
          "contextual_groups": [
            {
              "group_id": 0,
              "group_code": "{mti_term_id}-{serial}",
              "context_description": "{brief phrase}",
              "anchor_count": 0,
              "related_count": 0,
              "set_aside_count": 0,
              "anchor_verses": [
                {
                  "verse_record_id": 0,
                  "reference": "{Book Ch:V}",
                  "verse_text": "{full ESV text}",
                  "target_word": "{word form in this verse}",
                  "span_strong_match": 1
                }
              ]
            }
          ]
        }
      ],
      "xref_terms": [
        {
          "strongs_number": "{H/Gnnnn}",
          "transliteration": "{text}",
          "gloss": "{text}",
          "mti_status": "{status}",
          "owner_registry_id": 0,
          "owner_word": "{word}",
          "owner_contextual_groups": [
            {
              "group_code": "{mti_term_id}-{serial}",
              "context_description": "{brief phrase}",
              "anchor_verse_references": ["{Book Ch:V}", "{Book Ch:V}"],
              "related_count": 0
            }
          ]
        }
      ]
    }
  ],
  "cross_word_map": [
    {
      "strongs_number": "{H/Gnnnn}",
      "transliteration": "{text}",
      "gloss": "{text}",
      "appears_in": [
        {
          "registry_id": 0,
          "word": "{word}",
          "term_owner_type": "{OWNER or XREF}",
          "group_count": 0
        }
      ]
    }
  ]
}
```

**Notes on reading the dataset:**
- `owner_terms` contains all active OWNER terms with full anchor verse text — these are the primary reading material
- `xref_terms` contains profiles for shared terms — group descriptions and anchor references only, no full verse text
- `cross_word_map` is the inter-word picture — every term shared across words in the pool
- Where a term appears as OWNER in one word and XREF in another within the same pool, the OWNER word's full anchor verses are in `owner_terms` for that word's entry — read them directly if analysing simultaneously

---

*WA-SessionB-Analysis-Instruction-v5.6 | 20260330 | Supersedes v5.5-20260330 | Section 4.4: mid-pool interruption detection; Section 12.4: failure patch rule on patch rejection*
