# WA-DimensionReview-Instruction-v1_3-2026-04-07

**Framework B — Soul Word Analysis Programme**
**Dimension Review Instruction — Claude AI and Claude Code**
**Version 1.3 | April 2026 | Status: Active governing instruction**

| **Document** | **Value** |
|---|---|
| Filename | WA-DimensionReview-Instruction-v1.3-2026-04-07.md |
| Supersedes | WA-DimensionReview-Instruction-v1.2-2026-04-06.md |
| Change note | v1.3 — Three corrections arising from C02 session practice: (1) Section 4.6 added: Mandatory coverage verification — CA must confirm every group in the cluster extract has a Phase B entry before Phase C proceeds for any registry; any group without a Phase B entry is a compliance gap that must be remedied before the session advances; (2) Section 5.4 and Section 9.3: pre-existing pointer scope expanded — the existing pointers extract must include both `wa_session_b_findings` and `wa_session_research_flags` for the cluster, and CA must verify uniqueness of both `finding_id` (Session B) and `flag_label` (Session D) against this extract before constructing any patch; DR-9 updated accordingly; (3) Section 5.4 template: `session_b_instruction` field value corrected to reference the current governing instruction version (was hardcoded to v1.1). |
| Companion documents | WA-VerseContext-Instruction-v2.4-20260403 │ WA-SessionB-Analysis-Instruction-v5.6 │ WA-Reference-v5.5 │ WA-Registry-Management-Guide-v5.6 │ patch_specification-v1.6 │ WA-SessionD-Orientation-v2.1 |
| Inputs | wa-dimension-report-{date}.md │ wa-registry-overview-{date}.json │ database_schema_{date}.json │ Dimension Review cluster extract — wa-dim-extract-{cluster}-{date}.json (Claude Code → Claude AI) │ Pre-existing pointers extract — wa-dim-existing-pointers-{cluster}-{date}.json (Claude Code → Claude AI) │ wa-vcb-{batch_id}-term-observations files (where group description correction is required) |
| Outputs | Cluster review assessment — wa-dim-cluster-review-{cluster}-v{n}-{date}.md (Claude AI) │ Dimension refinement log — wa-dim-refinement-log-{cluster}-v{n}-{date}.md (Claude AI, progressive) │ Dimension patch — wa-dim-patch-{cluster}-v{n}-{date}.json (Claude AI → Claude Code) │ Group description correction patch — wa-dim-grpdesc-patch-{cluster}-v{n}-{date}.json (Claude AI → Claude Code, when triggered) │ Session log — wa-dim-session-log-{scope}-v{n}-{date}.md (Claude AI, at breakpoints) |
| Claude AI role | Cluster assignment review, group quality assessment, dimension discernment, progressive refinement, Session B/D pointer capture, patch production |
| Claude Code role | Cluster extract construction, existing pointers extract construction, patch application to `wa_dimension_index`, `verse_context_group`, `wa_session_b_findings`, `wa_session_research_flags`, manual_override locking, dimension confidence field updates, VC batch re-run triggering where required, post-application integrity checks, dimension report regeneration |
| Interaction model | Claude Code constructs cluster extract + existing pointers extract → Claude AI reviews cluster (Phase A, B, C) → Claude AI produces patch(es) → researcher reviews → Claude Code applies → loop until cluster anchored → advance to next cluster |

---

## 0. Purpose and Scope

This document governs the Dimension Review stage — the analytical phase between Verse Context completion and Session B DataPrep. It covers cluster assignment validation, contextual meaning group quality assessment, progressive dimension refinement, and the capture of emergent Session B and D insights.

**What the Dimension Review does:**
- Validates that cluster assignments are analytically coherent
- Assesses and where necessary corrects contextual meaning group descriptions
- Reads groups within each cluster to discern what dimensions actually emerge from the data
- Progressively refines dimension assignments from automated hypothesis toward researcher-confirmed anchors
- Locks confirmed dimensions using the `manual_override` flag
- Captures emerging Session B and D observations as structured pointers in the database
- Prepares the ground for Session B — which should arise naturally from the data when the review is done well

**What the Dimension Review does NOT do:**
- Impose pre-formed dimension categories on the data — categories must emerge from the groups
- Perform the deep word analysis that is Session B's function
- Draw cross-cluster synthesis conclusions — that is Session D
- Delete or restructure verse-level data without a patch — all corrections go through the patch process
- Rush toward Session B — the quality of this stage directly determines the quality of Session B output

**The foundational principle of this stage:**

> Dimensions must flow from the data. The automated dimension labels in `wa_dimension_index` are starting hypotheses — keyword matches, not analytical conclusions. Every dimension label must be tested against the actual group content before it can be treated as reliable. A dimension becomes an anchor only when the verse evidence, read through the groups, genuinely warrants it.

**Stage sequence:**
```
Verse Context Complete (all 181 registries)
     │
     ▼
Claude Code: construct cluster extract + existing pointers extract (Sections 9.1, 9.3)
     │
     ▼
Dimension Review (this document) — per cluster
  ├── Phase A: Cluster assignment review (Claude AI → researcher decision → Claude Code patch if needed)
  ├── Phase B: Group quality review (Claude AI → researcher confirms or triggers correction)
  │     ├── Group description correction protocol (Section 4.5) if triggered
  │     └── Coverage verification (Section 4.6) — mandatory before Phase C begins
  └── Phase C: Dimension discernment and progressive refinement (iterative)
        ├── Claude AI: propose dimensions, capture B/D pointers
        ├── Researcher: confirm, refine, or reject
        ├── Claude Code: apply dimension patch
        └── Loop until researcher confirms dimension as anchor → manual_override = 1
     │
     ▼
Cluster complete → advance to next cluster
     │
     ▼
Session B DataPrep gate (all clusters complete)
```

| This document is self-standing. It does not rely on session memory. Claude AI requires this document, the cluster extract, and the existing pointers extract for the session. Claude Code requires this document and the patch specification. |
|---|

---

## 0.1 Pipeline Position

**Before this stage begins:**
- All 181 active registries have `verse_context_status = Complete`
- `wa_dimension_index` is populated with 3,401 contextual meaning groups
- Automated keyword classification has assigned dimension labels to 1,856 groups (55%); 1,545 (45%) are UNCLASSIFIED
- No `CLAUDE_AI` or `manual_override` dimension assessments exist
- `wa_session_b_dimensions` is effectively empty — populated during Session B, not here
- `wa_session_b_findings` and `wa_session_research_flags` may hold pre-existing entries from Verse Context session B flags

**What is already in `wa_dimension_index` per group:**

| Field | Content at stage entry |
|---|---|
| `group_code` | Unique code linking to `verse_context_group` |
| `context_description` | Phrase formed during Verse Context classification |
| `dimension` | Automated keyword label, or NULL |
| `dimension_confidence` | `KEYWORD_STRONG`, `KEYWORD_WEAK`, or NULL (UNCLASSIFIED) |
| `anchor_count`, `related_count`, `total_verse_count` | Verse footprint |
| `owning_registry_word`, `cluster_assignment` | Provenance |
| `manual_override` | 0 — no anchors set yet |
| `notes` | NULL — not yet populated by Claude AI |

**What this stage adds or updates:**

| Field / Table | What changes |
|---|---|
| `wa_dimension_index.dimension` | Confirmed, corrected, or newly assigned |
| `wa_dimension_index.dimension_confidence` | Updated to `CLAUDE_AI` after review |
| `wa_dimension_index.manual_override` | Set to `1` when researcher confirms anchor |
| `wa_dimension_index.notes` | Analytical reasoning recorded |
| `wa_dimension_index.last_modified` | Timestamp of change |
| `verse_context_group.context_description` | Corrected where Phase B finds inadequacy (via group description correction patch) |
| `verse_context_group.notes` | Correction rationale recorded |
| `wa_session_b_findings` | Emergent Session B observations inserted |
| `wa_session_research_flags` | Emergent Session D pointers inserted |

---

## 1. Foundational Principles

### 1.1 Data-First

No dimension category is assumed to be correct before the group content has been read. The automated labels are a starting map — useful as orientation, not as conclusion.

### 1.2 Progressive Refinement

Dimensions move through a confidence progression:

| Stage | `dimension_confidence` | `manual_override` | Meaning |
|---|---|---|---|
| Automated keyword match (broad) | `KEYWORD_WEAK` | 0 | Starting hypothesis — requires review |
| Automated keyword match (specific) | `KEYWORD_STRONG` | 0 | More reliable — still requires review |
| Claude AI assessed | `CLAUDE_AI` | 0 | Claude AI has read the group; dimension reflects content |
| Researcher confirmed anchor | `CLAUDE_AI` | 1 | Researcher confirmed — locked against automated change |

A dimension reaches anchor status only when the researcher is confident it reflects what the data genuinely shows.

### 1.3 Dimensions Emerge — They Are Not Imposed

The 12-category vocabulary currently in the data is an artefact of automated classification. It is a reasonable starting vocabulary, not an authoritative system. If, during Phase C, the vocabulary is found to be too broad, too narrow, or insufficient to capture what a group actually shows, this is a finding — not a problem. Claude AI must surface these tensions as observations for researcher decision. Claude AI must not resolve category-level questions unilaterally.

> **The structure of the inner being emerges from what Scripture shows through the data. The categories follow the evidence.**

### 1.4 Group Quality Is the Prerequisite

A dimension assignment is only as reliable as the group it is assigned to. If a `context_description` is vague, over-broad, or does not name an inner-being engagement, the dimension is unreliable regardless of how it was assigned. Phase B must be complete for **every group in the cluster extract** before Phase C proceeds for any registry.

### 1.5 Session B Will Arise from the Data

When the Dimension Review is done well — clusters validated, groups quality-checked, dimensions grounded in group content — Session B analysis will have a clear foundation. The analytical frame will be visible in the refined dimension landscape. Rushing this stage is counterproductive. Session B depth is directly proportional to Dimension Review quality.

### 1.6 All Changes Go Through the Patch Process

No corrections to group descriptions, dimension assignments, or any database field are made by direct database manipulation. Every change is encoded in a patch file, reviewed by the researcher, and applied by Claude Code. This applies to corrections arising from Phase B quality review, including re-runs of Verse Context batches where verse-level decisions are affected.

---

## 2. The `wa_dimension_index` — What Claude AI Reads

Each row represents one contextual meaning group. Claude AI works from the cluster extract (Section 9.1) as the primary session input.

### 2.1 Key Fields for Dimension Review

| Field | Purpose in this stage |
|---|---|
| `id` | Primary key — used in patch `match` fields |
| `group_code` | Human-readable identifier — referenced in session log and refinement log |
| `verse_context_group_id` | FK to `verse_context_group` — used in group description correction patches |
| `owning_registry_word` | Which registry this group belongs to |
| `cluster_assignment` | Which cluster |
| `context_description` | **Primary analytical input** — what does this group say about the inner being? |
| `dimension` | Current assigned dimension — the hypothesis to test |
| `dimension_confidence` | Reliability of current assignment |
| `anchor_count` / `total_verse_count` | Size of verse evidence base |
| `manual_override` | 1 = locked; 0 = open for refinement |
| `notes` | Analytical reasoning — written here during Phase C |
| `last_modified` | Tracks change timestamp |

### 2.2 What Claude AI Does NOT Have During the Dimension Review

Claude AI does not have the full verse texts unless they are explicitly provided via extract or upload. The `context_description` is the primary input — the summary of the verse evidence formed during Verse Context classification. Where a description is insufficient to assess the dimension, Claude AI flags this rather than guessing.

---

## 3. Phase A — Cluster Assignment Review

### 3.1 Purpose

The cluster is the frame within which groups will be compared. A mis-assigned registry distorts the pool and may obscure or generate spurious patterns. Cluster assignments must be validated before group-level review begins.

### 3.2 Review Criteria

For each cluster, Claude AI assesses:

1. **Internal coherence** — Do the words share genuine inner-being affinity? Would their groups plausibly illuminate each other?
2. **Boundary cases** — Are there words that are predominantly about external acts, divine attributes, or social structures rather than the inner being?
3. **Missing affinity** — Are there words with stronger affinity for a different cluster?
4. **Size** — Very small clusters (fewer than 4 active words) or very large clusters (more than 13 active words) warrant review

### 3.3 Output

Claude AI produces a cluster assessment (Section 7.1 format) for each cluster. The assessment states coherence pattern, flags boundary ambiguities, and makes a recommendation: Confirm as-is, or Propose reassignment(s).

Claude AI does not reassign registries unilaterally. All reassignment decisions require researcher confirmation.

### 3.4 Claude Code Action (Phase A)

If the researcher confirms a reassignment, Claude Code applies a patch updating `cluster_assignment` on `word_registry` and all corresponding rows in `wa_dimension_index`. Patch type: `CLUSTERING` per patch_specification-v1.6 Section 0.1.

### 3.5 Processing Order

Clusters are reviewed in sequence: C01 through C22. Excluded registries (marked †) are listed for completeness but not assessed.

---

## 4. Phase B — Group Quality Review

### 4.1 Purpose

Phase B is a quality gate. It assesses whether each group's `context_description` is sufficient to support reliable dimension assignment. It does not perform the dimension assignment — that is Phase C.

### 4.2 Quality Criteria

A group has adequate quality when its `context_description`:

1. **Names an inner-being engagement** — identifies what state, capacity, orientation, disposition, or quality is in view
2. **Is specific enough to be distinct** — can be differentiated from other groups for this term
3. **Is grounded in verse evidence** — reflects what the verses show, not a general theological claim
4. **Does not over-generalise** — is not so broad that many unrelated uses would fit

### 4.3 Quality Flags

| Flag | Meaning | Phase C treatment |
|---|---|---|
| `QA-CLEAR` | Adequate — names a specific inner-being engagement | Proceed to Phase C |
| `QA-VAGUE` | Too general or non-specific | Flag for researcher; Phase C deferred pending decision |
| `QA-BROAD` | May be conflating materially different uses | Flag for researcher; Phase C deferred pending decision |
| `QA-EXTERNALISED` | Names external act rather than inner-being engagement | Flag for researcher; Phase C deferred pending decision |
| `QA-REVIEW` | Something warrants researcher attention; Claude AI uncertain | Flag for researcher; Phase C deferred pending decision |

Only `QA-CLEAR` groups proceed to Phase C without researcher input. All other flags are presented with full context before Phase C proceeds for that group.

### 4.4 Scope of Phase B

Phase B reads `context_descriptions` as recorded. It does not re-read original verse texts unless a relevant Verse Context observations file is provided. If a description is found inadequate, the assessment names the problem; the remedy is determined per Section 4.5.

### 4.5 Group Description Correction Protocol

**When a group description is found to be inadequate during Phase B, a correction may be warranted.** This is an allowed and expected outcome of the Dimension Review. All corrections go through the patch process.

**Step 1 — Claude AI assessment.** Claude AI states: (a) what is inadequate about the current description; (b) what a better description would need to capture; (c) a proposed revised description if the problem can be resolved from the existing `context_description` and the analytical context of the cluster; (d) whether verse text review is needed to write a reliable replacement.

**Step 2 — Researcher decision.** The researcher confirms, amends, or rejects the proposed correction. The researcher may also direct that the original Verse Context observations file be consulted before a revision is written.

**Step 2a — CC directive for verification extract.** When verse-level review is needed before writing a replacement description, CA produces a directive to CC as a `.md` file (not a JSON — the `.md` format is readable by both CC and the researcher). CC constructs the group description verification extract per Section 9.2 and returns it. CA then reads the verse texts from whatever means the content arrives — the JSON file, a chat summary, or an upload. CA needs the verse text; the JSON file is CC's working output, not a required CA input format.

**Step 3 — Correction options:**

| Scenario | Action |
|---|---|
| Correction is clear and does not affect verse assignments | Correction is encoded in the cluster dimension patch (Section 7.3) — updates `verse_context_group.context_description`, syncs `wa_dimension_index.context_description`, and records rationale in `verse_context_group.notes`. No separate patch file. |
| Correction requires reviewing which verses belong in the group | CA produces the correction within the cluster dimension patch AND flags that verse-level review is needed; researcher decides whether to trigger a Verse Context batch re-run for the affected terms |
| Problem is severe enough that the group may be incorrectly constructed | Researcher may trigger a Verse Context batch re-run for the affected terms — Claude Code resets the relevant registry's `verse_context_status` to In Progress and constructs a targeted re-run batch |

**⚠ Standalone `DIMREVIEW-GRPDESC` patch files** (Section 7.4) are used only for corrections made **outside of a live cluster session** — for example, repairing corrupt group descriptions discovered in a VCB batch before the Dimension Review begins. When a correction arises during a live cluster session, it travels in the cluster dimension patch.

**Step 4 — After patch application.** Claude Code applies the group description correction patch. If `verse_context_group.context_description` changes, Claude Code also updates the corresponding `context_description` in `wa_dimension_index` to maintain consistency. Claude Code confirms the update before Phase C proceeds for the corrected group.

**Step 5 — Re-run trigger.** If a Verse Context batch re-run is triggered, the Verse Context stage governs that work (WA-VerseContext-Instruction-v2.4). The Dimension Review for the affected registry resumes after the re-run is complete and `verse_context_status` returns to Complete.

### 4.6 Mandatory Coverage Verification

**⚠ Before Phase C begins for any registry, Claude AI must verify that every group in the cluster extract has a Phase B entry in the refinement log.**

**Verification procedure:**

1. Count the total number of groups in the cluster extract (`extract_meta.row_count` or by counting the `groups` array)
2. Count the number of unique group codes recorded in Phase B entries across the refinement log
3. If the two counts match: coverage is confirmed — proceed to Phase C
4. If the counts do not match: identify the missing groups by code, perform Phase B assessment for each, and record them in the refinement log before proceeding

**No group may be skipped.** A group without a Phase B entry is a compliance gap. Claude AI must perform Phase B on all missing groups in the same session, or explicitly defer them to a named follow-up session with researcher agreement. Deferral without researcher agreement is not permitted.

**This check must be performed and confirmed in the refinement log before the first Phase C entry is written.**

---

## 5. Phase C — Dimension Discernment and Progressive Refinement

### 5.1 The Core Question

For each `QA-CLEAR` group, the dimension assessment asks:

> What aspect of the inner being does this group engage? What is the nature of the inner-being involvement that the `context_description` names?

This is a discernment exercise, not a classification exercise. The goal is not to assign a label from a fixed list but to characterise what is actually present.

### 5.2 Working with the Existing Dimension Vocabulary

The current 12-category vocabulary is a working starting point. When assessing a group:

1. Read the `context_description`
2. Ask: what aspect of the inner being does this engage?
3. Check whether the existing automated label (if any) reflects the description
4. If yes — confirm it, upgrade confidence to `CLAUDE_AI`
5. If no — propose the more accurate label, with reasoning
6. If the vocabulary does not capture what the description shows — name the distinction and flag it

### 5.3 When the Vocabulary May Be Insufficient

When a group does not fit cleanly into any existing category, Claude AI must:
- Not force the group into an ill-fitting category
- Name what the group appears to show, in plain language
- Flag this as a vocabulary question for the researcher
- Record the observation in the refinement log

Vocabulary decisions — whether to add, split, merge, or rename dimensions — are researcher decisions, not Claude AI decisions.

### 5.4 Session B and D Pointer Capture

**Analytical observations that arise during Phase C and are relevant to Session B analysis or cross-registry synthesis must be captured in the patch.** This is not optional. Insights that surface during the dimension review will not survive to Session B unless they are encoded in the database.

**Two capture mechanisms are used:**

**Naming conventions for finding_id and flag_label:**

| Type | Convention | Example |
|---|---|---|
| Session B finding | `DIM-{registry_no}-{3-digit-sequence}` | `DIM-112-001` |
| Session D pointer | `DIM-{registry_no}-SD{3-digit-sequence}` | `DIM-112-SD001` |

**These must be unique programme-wide.** Before inserting, Claude AI must check the pre-existing pointers extract (Section 9.3) to confirm no collision with existing entries — both `finding_id` values in `session_b_findings` and `flag_label` values in `session_d_pointers`. If the extract shows existing entries for the cluster's registries, the numbering sequence must continue from the highest existing number, not restart from 001.

**For Session B observations** (insights about how a specific registry's word operates in the inner being, patterns within the cluster that will inform Session B analysis):

Insert into `wa_session_b_findings`:

```json
{
  "op_id": "OP-{nnn}",
  "operation": "insert",
  "table": "wa_session_b_findings",
  "record": {
    "finding_id": "DIM-{registry_no}-{3-digit-sequence}",
    "registry_id": {registry_no},
    "file_id": null,
    "finding_type": "DIMENSION_REVIEW",
    "finding": "{Observation — what the dimension pattern shows about this word's inner-being role}",
    "anchor_verses": "{verse references if relevant, or null}",
    "raised_date": "{ISO date}",
    "session_b_instruction": "WA-DimensionReview-Instruction-v{current_version}-{current_date}"
  },
  "description": "Session B pointer — {registry_word}: {brief summary}"
}
```

**For Session D pointers** (cross-cluster patterns, vocabulary tensions, cross-registry relationships, synthesis questions that belong to the whole-programme level):

Insert into `wa_session_research_flags`:

```json
{
  "op_id": "OP-{nnn}",
  "operation": "insert",
  "table": "wa_session_research_flags",
  "record": {
    "registry_id": {registry_no},
    "file_id": null,
    "flag_code": "SD_POINTER",
    "flag_label": "DIM-{registry_no}-SD{3-digit-sequence}",
    "strongs_reference": null,
    "cross_registry_id": {linked_registry_no_or_null},
    "priority": "MEDIUM",
    "session_target": "D",
    "description": "{Cross-cluster or whole-programme observation — what synthesis question this raises}",
    "session_raised": "WA-DimensionReview-Instruction-v{current_version}",
    "raised_date": "{ISO date}",
    "resolved": 0
  },
  "description": "Session D pointer — {brief summary}"
}
```

**Guidance on what to capture:**
- A cluster showing consistent convergence on a dimension that does not align with its assumed semantic domain — worth capturing
- A word whose groups span an unexpectedly wide dimension range — flag for Session B
- Two words in different clusters whose groups appear to name the same inner-being phenomenon — flag for Session D
- A dimension pattern that the existing vocabulary cannot adequately name — flag for vocabulary decision and Session D
- An observation about how inner-being characteristics relate to each other within a cluster — Session B pointer

**Guidance on what NOT to capture:** Do not insert routine observations about individual groups that are adequately addressed by the dimension assignment itself. Pointers are for insights that go beyond the dimension label and would be lost without explicit capture.

### 5.5 Cross-Group Patterns Within a Cluster

When reviewing groups across a cluster, Claude AI looks for:

- **Convergence** — multiple groups from different registries naming the same inner-being engagement. Strong evidence for a genuine dimension.
- **Divergence** — groups clustered together but engaging materially different aspects of the inner being. May indicate a cluster spanning more than one dimension, or a boundary question.
- **Unexpected distribution** — groups under a dimension that does not match their cluster's apparent affinity. May be correctly assigned (the inner being is not neatly compartmentalised) or may indicate a keyword-match error.

Claude AI records these as observations in the refinement log, and as Session B/D pointers in the patch where they meet the capture criteria above.

### 5.6 The Refinement Cycle

Phase C is iterative:

1. Claude AI reads all `QA-CLEAR` groups; proposes dimension assignments for unclassified; confirms or corrects existing labels
2. Researcher reviews
3. Confirmed assignments patched with `dimension_confidence = CLAUDE_AI`
4. Researcher identifies which are stable enough to anchor → patched with `manual_override = 1`
5. Unanchored dimensions remain open for further refinement in a subsequent session

There is no requirement to anchor all dimensions in a single session. Progressive refinement over multiple sessions is the expected pattern.

---

## 6. Session Discipline

### 6.1 Unit of Work

The cluster is the unit of work. A session covers one cluster (or a portion of a large cluster), moving through Phases A, B, and C in sequence before advancing. A session does not need to complete a cluster, but must leave it in a clearly documented state.

### 6.2 File Writing Discipline

- After every registry reviewed in Phase B or C: write to the refinement log before proceeding
- On every write: state the current version and increment it
- Dual-write: working directory and `/mnt/user-data/outputs/` after every increment

### 6.3 Session Logs

Produce a session log at natural breakpoints. Session logs must record:
- Which cluster(s) and phases were covered
- Findings from Phase A (cluster coherence)
- Quality flags from Phase B and their resolution (including any group description correction patches triggered)
- Coverage verification result (Section 4.6) — counts and any gaps found and remedied
- Dimension proposals from Phase C and researcher responses
- Session B/D pointers captured
- Any vocabulary questions raised
- Current refinement log version
- Next steps

### 6.4 Startup Protocol

At the start of every new session continuing an existing Dimension Review:
1. State which cluster and phase is being continued
2. Confirm the refinement log version being loaded
3. State patch status — what was applied, what is pending
4. Confirm any unresolved flags or vocabulary questions from the prior session
5. Confirm the existing pointers extract has been loaded and the highest existing sequence numbers for Session B and Session D pointers noted

---

## 7. Output Formats

### 7.1 Cluster Review Assessment

```
## Cluster Review — {C##} | {summary of cluster words}
Date: {date} | Session: {session reference}

### Active registries in this cluster
{list with registry numbers}

### Excluded registries (noted only)
{list with †}

### Coherence assessment
{What inner-being affinity holds this cluster together — grounded in the words present}

### Boundary observations
{Any misplaced words or ambiguous scope — with reasoning}

### Recommendation
[ ] Confirm as-is
[ ] Propose reassignment: {word} (Reg {no}) → {target cluster} | Reason: {brief reason}

### Researcher decision
{Completed by researcher}
```

### 7.2 Dimension Refinement Log

Progressive document. Appended after every registry.

```
## Refinement Entry — Registry {nnn} | {word} | {cluster}
Date: {date} | Refinement log version: v{n}

### Phase B — Group quality
| Group code | Context description | QA flag | Notes |
|---|---|---|---|

### Coverage verification (required once per cluster — confirm before first Phase C entry)
Groups in extract: {n} | Groups with Phase B entry: {n} | Coverage: CONFIRMED / GAP FOUND
{If gap found: list missing group codes and note that Phase B was performed}

### Phase C — Dimension assessment
| Group code | Context description | Automated label | Claude AI proposal | Confidence | Notes |
|---|---|---|---|---|---|

### Session B/D pointers captured
{List of finding_id / flag_label values inserted in patch, with one-line summary}

### Vocabulary observations
{Any patterns, tensions, or category questions}

### Pending researcher decisions
{Flags, vocabulary questions, proposed reassignments awaiting input}
```

### 7.3 Dimension Patch

JSON patch for Claude Code. One patch per cluster session (or per registry for targeted corrections). Follows `patch_specification-v1.6`. Patch type: `DIMREVIEW` (see Section 8.5).

**⚠ patch_id token rule:** The `patch_id` must contain the string `DIMREVIEW` for CC's `apply_session_patch.py` exemption check to recognise that `session_b_status: null` is valid. Using a different token (e.g. `-DIM-`) will cause the patch to be rejected. See Section 8.5.

**Patch meta:**
```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-V{n}",
    "cluster": "{C##}",
    "produced_date": "{ISO date}",
    "produced_by": "WA-DimensionReview-Instruction-v1.3-2026-04-07",
    "session_b_status": null,
    "description": "Dimension review patch — {cluster}: {brief summary of changes}"
  }
}
```

**Dimension update operation (per group):**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "update",
  "table": "wa_dimension_index",
  "match": { "id": {dimension_index_id} },
  "set": {
    "dimension": "{confirmed dimension value}",
    "dimension_confidence": "CLAUDE_AI",
    "manual_override": 0,
    "notes": "{reasoning if label was changed or if notable}",
    "last_modified": "{ISO datetime}"
  },
  "description": "{group_code} — {registry_word}: {brief description of change}"
}
```

For researcher-anchored dimensions, `manual_override` is set to `1` in the same operation.

**Session B findings insert:** see Section 5.4 format.

**Session D pointer insert:** see Section 5.4 format.

**Patch summary:**
```json
{
  "_patch_summary": {
    "total_operations": 0,
    "dimension_updates": 0,
    "dimensions_anchored": 0,
    "session_b_findings_inserted": 0,
    "session_d_pointers_inserted": 0,
    "group_description_corrections": 0,
    "wa_dimension_index_syncs": 0
  }
}
```

**Note on group description corrections within a live session:** When Phase B produces a description correction, it is encoded directly in this cluster patch as two additional operations: (1) `update` on `verse_context_group` with the corrected `context_description` and correction rationale in `notes`; (2) `update` on `wa_dimension_index` to sync the `context_description`. These are not separate patch files. The `_patch_summary` fields `group_description_corrections` and `wa_dimension_index_syncs` count these operations.

### 7.4 Group Description Correction Patch (out-of-session use only)

**⚠ This patch type is for corrections made outside of a live cluster session only.** Within a live session, corrections travel in the cluster dimension patch (Section 7.3). This standalone patch type is used when corrupt or inadequate group descriptions are discovered and repaired before a Dimension Review session begins — for example, repairing VCB batch patch errors.

Patch type: `DIMREVIEW-GRPDESC`. patch_id must contain `DIMREVIEW-GRPDESC`.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-DIMREVIEW-GRPDESC-{scope}-V{n}",
    "registry_id": {registry_no},
    "word": "{word}",
    "produced_date": "{ISO date}",
    "produced_by": "WA-DimensionReview-Instruction-v1.3-2026-04-07",
    "session_b_status": null,
    "description": "Group description correction — {word}: {brief description of correction}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "update",
      "table": "verse_context_group",
      "match": { "id": {verse_context_group_id} },
      "set": {
        "context_description": "{revised description}",
        "notes": "Revised during Dimension Review Phase B: {reason for change}"
      },
      "description": "Group {group_code}: revised description — {reason}"
    },
    {
      "op_id": "OP-002",
      "operation": "update",
      "table": "wa_dimension_index",
      "match": { "id": {dimension_index_id} },
      "set": {
        "context_description": "{same revised description}",
        "notes": "Description updated to match verse_context_group correction",
        "last_modified": "{ISO datetime}"
      },
      "description": "wa_dimension_index sync — group {group_code}"
    }
  ]
}
```

**Note:** Claude Code must verify that `verse_context_group.id` and `wa_dimension_index.verse_context_group_id` match before applying. The `wa_dimension_index.context_description` is a denormalised copy — it must be kept in sync with the source `verse_context_group.context_description` at all times.

---

## 8. Claude Code Protocol and Boundaries

### 8.1 Claude Code Responsibilities

Claude Code is responsible for all database operations in the Dimension Review pipeline:

| Task | Claude Code action |
|---|---|
| Construct cluster extract | Query `wa_dimension_index` joined to `word_registry` for the requested cluster (Section 9.1) |
| Construct existing pointers extract | Query `wa_session_b_findings` and `wa_session_research_flags` for the cluster's registries (Section 9.3) |
| Apply dimension patch | Update `wa_dimension_index` per operations; log patch_id; report summary |
| Apply group description correction patch | Update `verse_context_group.context_description` AND sync `wa_dimension_index.context_description`; verify FK consistency before applying |
| Apply cluster reassignment patch | Update `word_registry.cluster_assignment` AND `wa_dimension_index.cluster_assignment` for all affected groups |
| Apply Session B findings inserts | Insert into `wa_session_b_findings` |
| Apply Session D pointer inserts | Insert into `wa_session_research_flags` |
| Post-application integrity check | Verify `manual_override = 1` rows were not incorrectly modified; verify `wa_dimension_index.context_description` matches `verse_context_group.context_description`; report any discrepancies |
| Trigger VC re-run | Reset `verse_context_status = 'In Progress'` for affected registry; construct targeted re-run batch per WA-VerseContext-Instruction-v2.4 |
| Regenerate dimension report | Re-run dimension report query after each patch application cycle |

### 8.2 Claude Code Boundaries — What Claude Code Does NOT Do

Claude Code does not make analytical decisions. Specifically:

- Does not determine what dimension a group should carry
- Does not assess group quality
- Does not decide whether a group description correction is warranted
- Does not set `manual_override = 1` except on explicit researcher instruction carried in the patch
- Does not trigger a VC re-run without researcher decision carried in the patch or session transcript
- Does not modify `wa_session_b_dimensions` during this stage — that table is populated during Session B

### 8.3 Patch Validation — Claude Code

Before applying any Dimension Review patch, Claude Code validates:

1. `patch_id` has not been previously applied
2. All `wa_dimension_index.id` values in update operations exist in the table
3. No operation targets a row with `manual_override = 1` unless `manual_override` is explicitly set in the operation (protecting locked anchors)
4. All `verse_context_group.id` values in group description correction operations exist
5. All `wa_session_b_findings.finding_id` values are unique programme-wide (not previously inserted in any registry, not only the current cluster)
6. All `wa_session_research_flags.flag_label` values are unique programme-wide
7. `session_b_status` in `_patch_meta` is `null` — Dimension Review patches do not advance `word_registry.session_b_status`

If validation fails, the entire patch is rejected. No partial application.

### 8.4 Post-Application Reporting

After every patch application, Claude Code reports:
- Count of `wa_dimension_index` rows updated
- Count of rows now at `manual_override = 1` (anchored)
- Count of `wa_session_b_findings` rows inserted
- Count of `wa_session_research_flags` rows inserted
- Count of `verse_context_group` descriptions updated (if group description correction patch)
- Any integrity check findings
- Confirmation that `wa_dimension_index.context_description` is in sync with `verse_context_group.context_description` for all corrected groups

### 8.5 New Patch Types

The following patch types are introduced by this instruction and should be added to the cross-reference table in `patch_specification-v1.6 Section 0.1`:

| Patch type | Governing instruction | Valid `session_b_status` | Content |
|---|---|---|---|
| `DIMREVIEW` | WA-DimensionReview-Instruction-v1.3 | `null` | `wa_dimension_index` updates; `wa_session_b_findings` inserts; `wa_session_research_flags` inserts; `verse_context_group` description corrections (when arising within a live session) |
| `DIMREVIEW-GRPDESC` | WA-DimensionReview-Instruction-v1.3 | `null` | `verse_context_group` description updates; `wa_dimension_index` context_description sync — **out-of-session use only** |

**⚠ Critical — exemption check matching:** CC's `apply_session_patch.py` determines whether `session_b_status: null` is a valid (exempt) state by checking whether the patch_id string contains the registered patch type token. This means:
- A `DIMREVIEW` patch **must** have `DIMREVIEW` in its `patch_id` — e.g. `PATCH-20260406-DIMREVIEW-C01-V1`
- A `DIMREVIEW-GRPDESC` patch **must** have `DIMREVIEW-GRPDESC` in its `patch_id` — e.g. `PATCH-20260406-DIMREVIEW-GRPDESC-112-V1`
- A patch_id containing only `-DIM-` (without `REVIEW`) will **not** match the exemption check and will be rejected

CA must use the correct token pattern. CC must register both token patterns in the exemption list.

---

## 9. Data Extracts — Required Inputs for Claude AI

### 9.1 Cluster Extract — Primary Session Input

Claude Code constructs this extract before each Dimension Review cluster session. It is the complete analytical input for Claude AI — no other database access is needed for normal Phases A, B, and C.

**Extract name:** `wa-dim-extract-{cluster}-{date}.json`

**Query scope:** All `wa_dimension_index` rows for the requested cluster, joined to `word_registry` for registry-level context, and to `verse_context_group` for group-level identity.

**JSON structure:**

```json
{
  "extract_meta": {
    "extract_type": "dimension_review_cluster",
    "cluster": "C##",
    "produced_date": "YYYY-MM-DD",
    "produced_by": "Claude Code — WA-DimensionReview-Instruction-v1.3",
    "governing_instruction": "WA-DimensionReview-Instruction-v1.3-2026-04-07",
    "row_count": 0
  },
  "cluster_registries": [ ... ],
  "groups": [ ... ]
}
```

**Field mapping:**

| JSON field | Source table | Source column |
|---|---|---|
| `group.id` | `wa_dimension_index` | `id` |
| `group.verse_context_group_id` | `wa_dimension_index` | `verse_context_group_id` |
| `group.group_code` | `wa_dimension_index` | `group_code` |
| `group.owning_registry_no` | `wa_dimension_index` | `owning_registry_no` |
| `group.owning_registry_word` | `wa_dimension_index` | `owning_registry_word` |
| `group.cluster_assignment` | `wa_dimension_index` | `cluster_assignment` |
| `group.mti_term_id` | `wa_dimension_index` | `mti_term_id` |
| `group.strongs_number` | `mti_terms` | `strongs_number` |
| `group.transliteration` | `mti_terms` | `transliteration` |
| `group.gloss` | `mti_terms` | `gloss` |
| `group.language` | `mti_terms` | `language` |
| `group.context_description` | `wa_dimension_index` | `context_description` |
| `group.dimension` | `wa_dimension_index` | `dimension` |
| `group.dimension_confidence` | `wa_dimension_index` | `dimension_confidence` |
| `group.manual_override` | `wa_dimension_index` | `manual_override` |
| `group.anchor_count` | `wa_dimension_index` | `anchor_count` |
| `group.related_count` | `wa_dimension_index` | `related_count` |
| `group.total_verse_count` | `wa_dimension_index` | `total_verse_count` |
| `group.delete_flagged` | `wa_dimension_index` | `delete_flagged` |
| `group.notes` | `wa_dimension_index` | `notes` |
| `group.last_modified` | `wa_dimension_index` | `last_modified` |

### 9.2 Group Description Verification Extract

Constructed on demand when Phase B identifies a group requiring verse-level review before a description correction can be written.

**Extract name:** `wa-dim-grpverify-{group_code}-{date}.json`

**CC directive format:** `.md` file delivered by CA to CC (see Section 4.5).

**Field mapping:**

| JSON field | Source table | Source column |
|---|---|---|
| `group.id` | `wa_dimension_index` | `id` |
| `group.group_code` | `wa_dimension_index` | `group_code` |
| `group.strongs_number` | `mti_terms` | `strongs_number` |
| `group.transliteration` | `mti_terms` | `transliteration` |
| `group.current_description` | `verse_context_group` | `context_description` |
| `group.notes` | `verse_context_group` | `notes` |
| `anchor_verses.verse_record_id` | `verse_context` | `verse_record_id` (where `is_anchor = 1`, `group_id = group.id`, `delete_flagged = 0`) |
| `anchor_verses.book` | `wa_verse_records` / `books` | `books.name` (via `wa_verse_records.book_id`) |
| `anchor_verses.chapter` | `wa_verse_records` | `chapter` |
| `anchor_verses.verse` | `wa_verse_records` | `verse` |
| `anchor_verses.verse_text` | `wa_verse_records` | `verse_text` |
| `related_verses.*` | Same as anchor_verses | where `is_related = 1`, `is_anchor = 0` |

---

### 9.3 Pre-existing Session B/D Pointer Extract

**Required session input.** Claude Code constructs this extract at the same time as the cluster extract, before the session begins. Claude AI uses it to verify uniqueness of all `finding_id` and `flag_label` values before constructing any pointer inserts in the patch.

**Extract name:** `wa-dim-existing-pointers-{cluster}-{date}.json`

**⚠ This extract must include all existing entries for the cluster's registries, not only entries previously created by Dimension Review sessions.** Verse Context batch flags (PH2 flags and similar) may already occupy sequence numbers. Failure to check the full existing set risks duplicate key violations at patch application.

```json
{
  "extract_meta": {
    "extract_type": "existing_pointers",
    "cluster": "C##",
    "produced_date": "YYYY-MM-DD"
  },
  "session_b_findings": [
    {
      "finding_id": "",
      "registry_id": 0,
      "finding_type": "",
      "finding": "",
      "raised_date": "",
      "session_b_instruction": ""
    }
  ],
  "session_d_pointers": [
    {
      "flag_label": "",
      "registry_id": 0,
      "flag_code": "",
      "description": "",
      "session_target": "",
      "raised_date": ""
    }
  ]
}
```

**Source tables:**

| JSON array | Source table | Filter |
|---|---|---|
| `session_b_findings` | `wa_session_b_findings` | `registry_id IN (SELECT id FROM word_registry WHERE cluster_assignment = '{C##}')` |
| `session_d_pointers` | `wa_session_research_flags` | Same registry filter; `session_target = 'D'` |

**Claude AI uniqueness check procedure:**

1. On session startup, read the existing pointers extract
2. Note the highest existing sequence number for Session B findings (`DIM-{n}-{seq}`) per registry
3. Note the highest existing sequence number for Session D pointers (`DIM-{n}-SD{seq}`) per registry
4. When constructing new pointer inserts: start from the next available sequence number, not from 001
5. Verify no proposed `finding_id` or `flag_label` appears in the existing extract before including it in the patch

---

## 10. Decision Rules and Boundaries

### 10.1 Claude AI Never Acts Unilaterally On

- Cluster reassignments — always researcher decision
- Vocabulary additions, splits, or renamings — always researcher decision
- Setting `manual_override = 1` — always researcher instruction
- Triggering a Verse Context batch re-run — always researcher decision
- Marking a group as `delete_flagged` — always researcher decision
- Writing revised `context_descriptions` to the patch without researcher confirmation

### 10.2 Claude AI May Propose Independently

- `CLAUDE_AI` dimension assignments for unclassified groups
- Corrections to `KEYWORD_WEAK` or `KEYWORD_STRONG` labels that do not match the group content
- Quality flags (`QA-*`) for any group
- Revised group descriptions as proposals (not as final patch content until confirmed)
- Session B/D pointer content for researcher review before patching
- Vocabulary tension and cluster coherence observations and recommendations

### 10.3 Presenting Decisions to the Researcher

When presenting a decision for researcher input, Claude AI must supply:
1. The full `context_description`
2. The current automated dimension (if any)
3. Claude AI's proposed dimension or correction and the reasoning
4. Where relevant: how this group compares with other groups in the same cluster
5. The options available and what each means for the programme

Researcher decisions must never be presented as bare option lists.

---

## 11. Integrity Rules

| Rule | Requirement |
|---|---|
| DR-1 | No dimension may be anchored (`manual_override = 1`) without researcher confirmation in the session transcript |
| DR-2 | No cluster reassignment may be patched without researcher confirmation |
| DR-3 | Phase C must not begin for a group until its Phase B quality flag is resolved |
| DR-4 | KEYWORD_STRONG groups still require Phase C review — they are not auto-confirmed |
| DR-5 | Group description corrections must be researcher-confirmed before encoding in a patch |
| DR-6 | `wa_dimension_index.context_description` must be kept in sync with `verse_context_group.context_description` at all times — Claude Code verifies after every group description correction patch |
| DR-7 | Dimension Review patches carry `session_b_status: null` — they must not advance `word_registry.session_b_status` |
| DR-8 | No patch may update a row with `manual_override = 1` except on explicit researcher instruction within that patch |
| DR-9 | Session B/D pointer `finding_id` and `flag_label` values must be unique programme-wide — Claude AI verifies against the existing pointers extract before patch construction; Claude Code validates again before application |
| DR-10 | Every group in the cluster extract must have a Phase B entry in the refinement log before Phase C begins — compliance verified and recorded in the refinement log (Section 4.6) |

---

## 12. Naming Conventions

| File type | Pattern | Example |
|---|---|---|
| Cluster extract | `wa-dim-extract-{cluster}-{date}.json` | `wa-dim-extract-C01-2026-04-06.json` |
| Group verification extract | `wa-dim-grpverify-{group_code}-{date}.json` | `wa-dim-grpverify-3012-001-2026-04-06.json` |
| CC directive for group verification | `wa-dim-cc-directive-grpverify-{group_code}-{date}.md` | `wa-dim-cc-directive-grpverify-3012-001-2026-04-06.md` |
| Existing pointers extract | `wa-dim-existing-pointers-{cluster}-{date}.json` | `wa-dim-existing-pointers-C01-2026-04-06.json` |
| Dimension refinement log | `wa-dim-refinement-log-{cluster}-v{n}-{date}.md` | `wa-dim-refinement-log-C02-v1.0-2026-04-06.md` |
| Dimension patch (cluster) | `wa-dim-patch-{cluster}-v{n}-{date}.json` | `wa-dim-patch-C01-v1-2026-04-06.json` |
| Group description correction patch (out-of-session only) | `wa-dim-grpdesc-patch-{scope}-v{n}-{date}.json` | `wa-dim-grpdesc-patch-vcb029-all-v2-2026-04-06.json` |
| Session log | `wa-dim-session-log-{scope}-v{n}-{date}.md` | `wa-dim-session-log-C01-v1-2026-04-06.md` |

**Note on patch_id patterns:**
- Cluster dimension patch: `PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-V{n}` — e.g. `PATCH-20260406-DIMREVIEW-C01-V1`
- Out-of-session group description correction patch: `PATCH-{YYYYMMDD}-DIMREVIEW-GRPDESC-{scope}-V{n}` — e.g. `PATCH-20260406-DIMREVIEW-GRPDESC-211-V1`

The token in the patch_id must match the registered patch type exactly. See Section 8.5.

---

*WA-DimensionReview-Instruction-v1.3-2026-04-07 | Supersedes v1.2-2026-04-06 | v1.3: Section 4.6 added — mandatory coverage verification before Phase C; Section 5.4 — uniqueness check procedure expanded to include both Session B and Session D against the existing pointers extract, sequence numbering rule added; Section 5.4 template — `session_b_instruction` field corrected to reference current governing instruction version; Section 6.4 — startup protocol updated to include existing pointers extract confirmation; Section 6.3 — session log must record coverage verification result; Section 7.2 — refinement log format updated to include coverage verification block; DR-9 updated — uniqueness is now CA pre-check + CC validation; DR-10 added — Phase B coverage is mandatory and recorded; Section 8.1 — CC responsibilities updated to include existing pointers extract construction; Section 8.3 — validation rule 5 and 6 updated to programme-wide scope; Section 9.3 — extract scope note added; Section 12 — refinement log naming pattern updated to include cluster.*
