# WA-DimensionReview-Instruction-v1.7-2026-04-09

**Framework B — Soul Word Analysis Programme**
**Dimension Review Instruction — Claude AI and Claude Code**
**Version 1.7 | April 2026 | Status: Active governing instruction**

| **Document** | **Value** |
|---|---|
| Filename | WA-DimensionReview-Instruction-v1.7-2026-04-09.md |
| Supersedes | WA-DimensionReview-Instruction-v1.6-2026-04-08.md |
| Change note | v1.7 — Six substantive additions arising from review against WA-VerseContext-Instruction-v2.5, the 2026-04-08 session transcript, and the root family full extract. (1) Root family extract added as a standard filtered session input (Section 9.4); Claude Code query specification and JSON structure defined. (2) Anchor verse vertical pass extract added as an on-demand sub-process input (Section 9.5); strict naming convention and trigger conditions specified to prevent uncontrolled extract proliferation. (3) Phase B quality flag `QA-TERMCENTRIC` added (Section 4.3) — names the specific inadequacy where a group description names what the term does rather than the inner-being characteristic served; triggers the characteristic-perspective correction sub-process (Section 4.7). (4) Characteristic-perspective correction sub-process added (Section 4.7) — fix-or-stop principle governs all term-centric corrections; sub-processes defined for in-session rewrite, VCB re-run, and upstream return instruction. (5) Return instruction format specified (Section 4.8) — formal `.md` directive when correction cannot be completed within the Dimension Review. (6) Cluster-level and registry-level Dimension Review version stamps added (Section 10) — two new fields on `word_registry` (`dim_review_status`, `dim_review_version`) and a new table `wa_dim_review_cluster_log`; Session B gates on the cluster-level stamp. Schema additions required: see Section 10.3. Companion document reference updated to v2.5. Startup protocol (Section 6.4) extended with VCB completeness check. Phase C extended with property-term dimension assignment guidance (Section 5.1). Session B gate condition updated (Section 10.4). No other sections changed. |
| Companion documents | WA-VerseContext-Instruction-v2.5-20260409 │ WA-SessionB-Analysis-Instruction-v5.7 │ WA-Reference-v5.5 │ WA-Registry-Management-Guide-v5.7 │ patch_specification-v1.6 │ WA-SessionD-Orientation-v2.1 │ WA-dim-session-log-methodology-v2.1-2026-04-08.md |
| Inputs | wa-dimension-report-{date}.md │ wa-registry-overview-{date}.json │ database_schema_{date}.json │ Dimension Review cluster extract — wa-dim-extract-{cluster}-{date}.json (Claude Code → Claude AI) │ Root family cluster extract — wa-dim-rootfamily-{cluster}-{date}.json (Claude Code → Claude AI) │ Pre-existing pointers extract — wa-dim-existing-pointers-{cluster}-{date}.json (Claude Code → Claude AI) │ Anchor verse vertical pass extract — wa-dim-vpass-{cluster}-{group_code}-{date}.json (Claude Code → Claude AI, on demand) │ wa-vcb-{batch_id}-term-observations files (where group description correction is required) |
| Outputs | Cluster review assessment — wa-dim-cluster-review-{cluster}-v{n}-{date}.md (Claude AI) │ Dimension refinement log — wa-dim-refinement-log-{cluster}-v{n}-{date}.md (Claude AI, progressive) │ Dimension patch — wa-dim-patch-{cluster}-v{n}-{date}.json (Claude AI → Claude Code) │ Group description correction patch — wa-dim-grpdesc-patch-{cluster}-v{n}-{date}.json (Claude AI → Claude Code, when triggered) │ Return instruction — wa-dim-return-{cluster}-{registry}-v{n}-{date}.md (Claude AI → researcher, when upstream re-run required) │ Session log — wa-dim-session-log-{scope}-v{n}-{date}.md (Claude AI, at breakpoints) |
| Claude AI role | Cluster assignment review, group quality assessment, characteristic-perspective correction, dimension discernment, dominant subject identification, anchor verse verification, progressive refinement, Session B/D pointer capture, patch production, return instruction production |
| Claude Code role | Cluster extract construction, root family extract construction, existing pointers extract construction, anchor verse vertical pass extract construction (on demand), patch application to `wa_dimension_index`, `verse_context_group`, `wa_session_b_findings`, `wa_session_research_flags`, manual_override locking, dimension confidence field updates, dominant_subject field updates, VC batch re-run triggering where required, registry and cluster stamp updates, post-application integrity checks, dimension report regeneration |
| Interaction model | Claude Code constructs cluster extract + root family extract + existing pointers extract → Claude AI reviews cluster (Phase A, B, B.5, C) → Claude AI produces patch(es) → researcher reviews → Claude Code applies → loop until cluster anchored → advance to next cluster |

---

## 0. Purpose and Scope

This document governs the Dimension Review stage — the analytical phase between Verse Context completion and Session B DataPrep. It covers cluster assignment validation, contextual meaning group quality assessment, characteristic-perspective correction, progressive dimension refinement, dominant subject identification, anchor verse verification, and the capture of emergent Session B and D insights.

**What the Dimension Review does:**
- Validates that cluster assignments are analytically coherent
- Assesses and where necessary corrects contextual meaning group descriptions — including full characteristic-perspective realignment of groups produced under the pre-v2.5 term-centric model
- Verifies that anchor verse data is complete and supports the group and dimension description
- Reads groups within each cluster to discern what dimensions actually emerge from the data
- Assigns the dominant subject (the `dominant_subject` field) for each group
- Progressively refines dimension assignments from automated hypothesis toward researcher-confirmed anchors
- Locks confirmed dimensions using the `manual_override` flag
- Captures emerging Session B and D observations as structured pointers in the database
- Stamps each registry and cluster with the Dimension Review version on completion
- Prepares the ground for Session B — which should arise naturally from the data when the review is done well

**What the Dimension Review does NOT do:**
- Impose pre-formed dimension categories on the data — categories must emerge from the groups
- Use theological context, circumstance, or relational setting as a dimension criterion
- Perform the deep word analysis that is Session B's function
- Draw cross-cluster synthesis conclusions — that is Session D
- Delete or restructure verse-level data without a patch — all corrections go through the patch process
- Rush toward Session B — the quality of this stage directly determines the quality of Session B output

**The foundational principle of this stage:**

> The dimension always follows the verse. Read the group. Name what you see. Then check whether an existing dimension already captures it. If yes — assign it. If no — propose a new name. Never fit a group into a dimension that does not genuinely describe it.

**The fix-or-stop principle:**

> The Dimension Review does not flag and pass. When a quality problem is identified, the Dimension Review follows whatever sub-process is necessary to fix it. If a fix cannot be completed within the Dimension Review session, the session stops and issues a formal return instruction to the appropriate upstream process. A group with an unresolved quality problem does not advance to Phase C.

**Stage sequence:**
```
Verse Context Complete (all 181 registries)
     │
     ▼
Claude Code: construct cluster extract + root family extract + existing pointers extract
     │
     ▼
Dimension Review (this document) — per cluster
  ├── Phase A: Cluster assignment review
  ├── Phase B: Group quality review (including QA-TERMCENTRIC screening)
  │     ├── Phase B.5: Characteristic-perspective correction sub-process (when QA-TERMCENTRIC raised)
  │     ├── Anchor verse verification (Section 5.6) — on demand during Phase B or C
  │     └── Coverage verification (Section 4.6) — mandatory before Phase C begins
  └── Phase C: Dimension discernment and progressive refinement (iterative)
        ├── Claude AI: read group, assign dimension + dominant_subject
        ├── Researcher: confirm, refine, or reject
        ├── Claude Code: apply dimension patch
        └── Loop until researcher confirms dimension as anchor → manual_override = 1
     │
     ▼
Cluster complete → Claude Code sets cluster stamp → advance to next cluster
     │
     ▼
Session B DataPrep gate (all clusters complete AND cluster stamps set)
```

| This document is self-standing. It does not rely on session memory. Claude AI requires this document, the cluster extract, the root family extract, and the existing pointers extract for the session. Claude Code requires this document and the patch specification. |
|---|

---

## 0.1 Pipeline Position

**Before this stage begins:**
- All 181 active registries have `verse_context_status = Complete`
- `wa_dimension_index` is populated with 3,401 contextual meaning groups
- Automated keyword classification has assigned dimension labels to 1,856 groups (55%); 1,545 (45%) are UNCLASSIFIED
- No `CLAUDE_AI` or `manual_override` dimension assessments exist
- `dominant_subject` field is NULL for all existing rows — populated during this stage
- `wa_session_b_dimensions` is effectively empty — populated during Session B, not here
- `wa_session_b_findings` and `wa_session_research_flags` may hold pre-existing entries from Verse Context session B flags
- `word_registry.dim_review_status` is NULL for all registries — populated during this stage
- `word_registry.dim_review_version` is NULL for all registries — populated during this stage
- `wa_dim_review_cluster_log` is empty — populated during this stage

**What this stage adds or updates:**

| Field / Table | What changes |
|---|---|
| `wa_dimension_index.dimension` | Confirmed, corrected, or newly assigned |
| `wa_dimension_index.dimension_confidence` | Updated to `CLAUDE_AI` after review |
| `wa_dimension_index.manual_override` | Set to `1` when researcher confirms anchor |
| `wa_dimension_index.dominant_subject` | Assigned: GOD / HUMAN / OTHER_HUMAN / UNSEEN / NONE |
| `wa_dimension_index.notes` | Analytical reasoning recorded |
| `wa_dimension_index.last_modified` | Timestamp of change |
| `verse_context_group.context_description` | Corrected where Phase B finds inadequacy |
| `verse_context_group.notes` | Correction rationale recorded |
| `wa_session_b_findings` | Emergent Session B observations inserted |
| `wa_session_research_flags` | Emergent Session D pointers inserted |
| `word_registry.dim_review_status` | Set to `Complete` when registry passes Dimension Review |
| `word_registry.dim_review_version` | Set to governing instruction version when registry passes |
| `wa_dim_review_cluster_log` | Cluster completion record inserted when full cluster confirmed |

---

## 1. Foundational Principles

### 1.1 Data-First

No dimension category is assumed to be correct before the group content has been read. The automated labels are a starting map — useful as orientation, not as conclusion. The confirmed dimension vocabulary (Section 5.7) is a working starting point derived from data, not an authoritative final system.

### 1.2 Progressive Refinement

Dimensions move through a confidence progression:

| Stage | `dimension_confidence` | `manual_override` | Meaning |
|---|---|---|---|
| Automated keyword match (broad) | `KEYWORD_WEAK` | 0 | Starting hypothesis — requires review |
| Automated keyword match (specific) | `KEYWORD_STRONG` | 0 | More reliable — still requires review |
| Claude AI assessed | `CLAUDE_AI` | 0 | Claude AI has read the group; dimension reflects content |
| Researcher confirmed anchor | `CLAUDE_AI` | 1 | Researcher confirmed — locked against automated change |

A dimension reaches anchor status only when the researcher is confident it reflects what the data genuinely shows.

### 1.3 The Dimension Vocabulary Is Iterative

The vocabulary in Section 5.7 was derived from data and represents the current best understanding. It will be revised as more data is reviewed. When a group does not fit any existing dimension, that is a finding, not a failure.

*Current vocabulary: 11 dimensions (updated v1.6 — dimension 11 Divine-Human Correspondence added from C18 data).*

### 1.4 Group Quality Is the Prerequisite

A dimension assignment is only as reliable as the group it is assigned to. Phase B must be complete — and all quality problems resolved — for every group in the cluster extract before Phase C proceeds for any registry. The fix-or-stop principle applies without exception.

### 1.5 Session B Will Arise from the Data

When the Dimension Review is done well — clusters validated, groups quality-checked, dimensions grounded in group content — Session B analysis will have a clear foundation. Rushing this stage is counterproductive. Session B depth is directly proportional to Dimension Review quality.

### 1.6 All Changes Go Through the Patch Process

No corrections to group descriptions, dimension assignments, or any database field are made by direct database manipulation. Every change is encoded in a patch file, reviewed by the researcher, and applied by Claude Code.

### 1.7 The Scope Signal — Dominant Subject

Every group receives a `dominant_subject` value identifying the primary bearer of the characteristic as observed in the verse evidence.

| Value | What it names |
|---|---|
| `GOD` | The subject of this group is God in any form — Father, Son, Spirit |
| `HUMAN` | The subject is the individual human person being studied |
| `OTHER_HUMAN` | The subject is another human person in relationship with the first |
| `UNSEEN` | The subject is an entity from the unseen world |
| `NONE` | No dominant subject identifiable, or the group is purely circumstantial |

### 1.8 The Two-Type Distinction — Characteristic Terms and Property Terms

Groups in the Dimension Review derive from two structurally different types of terms:

| Type | Definition | Examples | Behaviour |
|---|---|---|---|
| **Characteristic terms** | Name an inner-being state directly. The term itself is the characteristic. | soul (ne.phesh), faith (pistis), stubbornness (she.ri.rut), counsel (mo.e.tsah) | Removing the term removes the characteristic. The verse is about that characteristic. |
| **Property terms** | Describe how inner-being characteristics operate — mechanism, condition, expression, or channel. | hear (sha.ma), ear (o.zen), hearing (akoē), obey (hupakouō), give ear (a.zan) | Can serve different characteristics across the verse corpus. Can serve the same characteristic in opposite ways. |

This distinction governs how group descriptions are assessed in Phase B and how dimensions are assigned in Phase C. It does not affect the dimension vocabulary — dimensions name the characteristic, regardless of which type of term gives rise to the group.

**The spectrum observation:** The distinction may not be binary. Some terms sit between the poles — relational characteristic terms (e.g. attentiveness, receptivity) name an inner disposition always directed toward an object; act terms name the enactment or expression of that disposition. The characteristic-perspective model applies across the spectrum.

---

## 2. The `wa_dimension_index` — What Claude AI Reads

### 2.1 Key Fields for Dimension Review

| Field | Purpose in this stage |
|---|---|
| `id` | Primary key — used in patch `match` fields |
| `group_code` | Human-readable identifier |
| `verse_context_group_id` | FK to `verse_context_group` |
| `owning_registry_word` | Which registry this group belongs to |
| `cluster_assignment` | Which cluster |
| `context_description` | **Primary analytical input** |
| `dimension` | Current assigned dimension — the hypothesis to test |
| `dimension_confidence` | Reliability of current assignment |
| `dominant_subject` | Who bears the characteristic |
| `anchor_count` / `total_verse_count` | Size of verse evidence base |
| `manual_override` | 1 = locked; 0 = open for refinement |
| `notes` | Analytical reasoning |
| `last_modified` | Tracks change timestamp |

### 2.2 What Claude AI Does NOT Have During the Dimension Review

Claude AI does not have the full verse texts unless explicitly provided via extract or the anchor verse vertical pass extract (Section 9.5). The `context_description` is the primary input. Where a description is insufficient, Claude AI requests the appropriate extract rather than guessing.

---

## 3. Phase A — Cluster Assignment Review

### 3.1 Purpose

Validate that cluster assignments are analytically coherent before group-level review begins.

### 3.2 Review Criteria

For each cluster, Claude AI assesses:

1. **Internal coherence** — Do the words share genuine inner-being affinity?
2. **Boundary cases** — Are there words predominantly about external acts, divine attributes, or social structures?
3. **Missing affinity** — Are there words with stronger affinity for a different cluster?
4. **Size** — Very small clusters (fewer than 4 active words) or very large clusters (more than 13 active words) warrant review

### 3.3 Output

Cluster assessment (Section 7.1 format). Recommendation: Confirm as-is, or Propose reassignment(s).

### 3.4 Claude Code Action (Phase A)

If reassignment confirmed: patch updating `cluster_assignment` on `word_registry` and all corresponding rows in `wa_dimension_index`. Patch type: `CLUSTERING`.

### 3.5 Processing Order

Clusters reviewed in sequence: C01 through C22.

---

## 4. Phase B — Group Quality Review

### 4.1 Purpose

Phase B is a quality gate and correction stage. It assesses whether each group's `context_description` is sufficient to support reliable dimension assignment — and where it is not, initiates the appropriate correction sub-process. Phase B does not pass quality problems forward. It fixes them or stops.

### 4.2 Quality Criteria

A group has adequate quality when its `context_description`:

1. **Names an inner-being characteristic** — identifies what state, capacity, orientation, disposition, or quality is in view, from the perspective of the characteristic rather than the term's behaviour
2. **States the term's role accurately** — for property terms, names the term's role relative to the characteristic (channel, mechanism, expression, obstacle, seat, counterpart)
3. **Is specific enough to be distinct** — can be differentiated from other groups for this term
4. **Is grounded in verse evidence** — reflects what the verses show, not a general theological claim
5. **Does not over-generalise** — is not so broad that many unrelated uses would fit

### 4.3 Quality Flags

| Flag | Meaning | Phase B.5 / Phase C treatment |
|---|---|---|
| `QA-CLEAR` | Adequate — names a specific inner-being characteristic with the term's role stated accurately | Proceed to Phase C |
| `QA-TERMCENTRIC` | Description names what the term does rather than the inner-being characteristic served; produced under pre-v2.5 term-centric model | Enter Phase B.5 — characteristic-perspective correction sub-process before Phase C |
| `QA-VAGUE` | Too general or non-specific — the characteristic is named but without sufficient precision | Flag for researcher; attempt in-session correction via verification extract; Phase C deferred pending resolution |
| `QA-BROAD` | May be conflating materially different uses — possible grouping error | Flag for researcher; Phase C deferred; may trigger VCB re-run |
| `QA-EXTERNALISED` | Names external act rather than inner-being engagement | Flag for researcher; Phase C deferred; correction required |
| `QA-REVIEW` | Something warrants researcher attention; Claude AI uncertain | Flag for researcher; Phase C deferred pending decision |

**Identifying `QA-TERMCENTRIC`:** A description is term-centric when:
- It names what the term does in the verse ("refusing to hear God", "hearing as inner receptive faculty") rather than what the verse is about ("heart-stubbornness expressed through refusal of God's word", "faith received — akoē as channel")
- It could apply to many different verses where the term appears with no differentiation by characteristic
- The inner-being characteristic being served is absent from the description or only parenthetical
- For property terms especially: the description does not name the term's role relative to the characteristic

Only `QA-CLEAR` groups proceed to Phase C without entering a correction sub-process. All other flags must be resolved before Phase C begins for that group.

### 4.4 Scope of Phase B

Phase B reads `context_descriptions` as recorded. It does not re-read original verse texts unless a verification extract or vertical pass extract is provided. If a description is found inadequate, the correction route is determined per Sections 4.5 or 4.7.

### 4.5 Group Description Correction Protocol (non-termcentric)

For groups flagged `QA-VAGUE`, `QA-BROAD`, `QA-EXTERNALISED`, or `QA-REVIEW`:

**Step 1 — Claude AI assessment.** State: (a) what is inadequate; (b) what a better description would need to capture; (c) a proposed revision if resolvable from existing context; (d) whether verse text review is needed.

**Step 2 — Researcher decision.** Confirm, amend, or reject. May direct verse-level review.

**Step 2a — CC directive for verification extract.** When verse-level review is needed: CA produces a `.md` directive to CC (Section 9.2). CC constructs and returns the group description verification extract.

**Step 3 — Correction options:**

| Scenario | Action |
|---|---|
| Correction clear, no verse assignment impact | Encoded in cluster dimension patch |
| Correction requires reviewing which verses belong | Encoded in patch AND researcher decides whether to trigger VCB re-run |
| Group may be incorrectly constructed | Researcher may trigger VCB re-run |

**Step 4 — After patch application.** Claude Code syncs `wa_dimension_index.context_description` with `verse_context_group.context_description`. Confirms before Phase C proceeds.

**Step 5 — Re-run trigger.** If VCB re-run triggered: governed by WA-VerseContext-Instruction-v2.5. Dimension Review for affected registry resumes after re-run completes.

### 4.6 Mandatory Coverage Verification

**⚠ Before Phase C begins for any registry, Claude AI must verify that every group in the cluster extract has a Phase B entry in the refinement log.**

1. Count total groups in extract (`extract_meta.row_count` or by counting `groups` array)
2. Count unique group codes recorded in Phase B entries
3. If counts match: coverage confirmed — proceed to Phase C
4. If counts do not match: perform Phase B on missing groups before proceeding

**This check must be confirmed in the refinement log before the first Phase C entry is written.**

### 4.7 Characteristic-Perspective Correction Sub-Process (Phase B.5)

**Triggered by:** `QA-TERMCENTRIC` flag on any group.

**Purpose:** Realign the group description from term-centric to characteristic-perspective, following the model established in WA-VerseContext-Instruction-v2.5 Section 6.2 Step 3. The fix-or-stop principle applies throughout.

**Step 1 — Claude AI determines whether the characteristic is discernible.**

Read the existing `context_description` and the anchor verses available in the cluster extract. Ask: what inner-being characteristic does this verse cluster primarily engage? What is the term's role relative to that characteristic?

- If the characteristic is discernible from the existing data → proceed to Step 2 (in-session rewrite)
- If the characteristic is not discernible from the description alone → request the anchor verse vertical pass extract (Section 9.5) and proceed to Step 2 after reading it
- If the anchor verses are themselves insufficient to determine the characteristic (verse evidence is ambiguous or the grouping appears wrong) → proceed to Step 3 (assess grouping soundness)

**Step 2 — In-session rewrite.**

Produce a revised `context_description` following the characteristic-perspective format:

> *[Characteristic] — [term] as [role]*

The revised description must:
- Name the inner-being characteristic the verse cluster primarily engages
- State the term's role accurately: seat, channel, mechanism, expression, obstacle, or counterpart
- Be grounded in what the verses show
- Be sufficient to distinguish this group from other groups for the same term

**Examples of compliant rewrites:**

| Old (term-centric) | New (characteristic-perspective) |
|---|---|
| *Hearing as the inner receptive faculty (faith, understanding, response)* | *Faith received — akoē as the channel through which faith arrives* |
| *Refusing to hear God* | *Heart-stubbornness expressed through refusal of God's word — sha.ma absent* |
| *Obeying God's voice: the inner act of covenantal obedience* | *Covenantal will — sha.ma as the act by which the will's orientation toward God is expressed* |
| *Ear as faculty for receiving divine address* | *Spiritual receptivity and its refusal — o.zen as the inner faculty through which divine word is received* |

The revised description is encoded in the cluster dimension patch (travels as a group description correction within `DIMREVIEW` patch — see Section 7.3).

**Step 3 — Assess grouping soundness.**

When the characteristic cannot be determined from the description and the anchor verse vertical pass extract reveals that the grouping itself may be wrong (verses about different characteristics grouped together, or a single characteristic appearing in opposite orientations that warrant distinct groups):

- **Grouping is sound but description is wrong:** proceed to Step 2 with the richer data now available from the vertical pass extract.
- **Grouping is wrong — verses need re-reading and re-grouping:** trigger a VCB re-run for this term under WA-VerseContext-Instruction-v2.5. The re-run will re-classify the term's verses under the characteristic-perspective model, producing corrected groups and descriptions. Issue a return instruction (Section 4.8). The Dimension Review for this registry pauses.
- **Source data is defective** (missing term links, incorrect Strong's assignment, term incorrectly deleted — pattern identified via vertical pass extract): issue a return instruction (Section 4.8) directing return to Session A / STEP extraction. The Dimension Review for this registry pauses.

**Step 4 — Patch encoding.**

All in-session rewrites travel in the cluster dimension patch as group description corrections (Section 7.3). The correction updates:
- `verse_context_group.context_description`
- `wa_dimension_index.context_description` (synced by Claude Code)
- `verse_context_group.notes` (correction rationale)

The group proceeds to Phase C after the rewrite is confirmed.

**Step 5 — Root family check.**

After rewriting a term-centric description, consult the root family extract (Section 9.4). Check whether sibling terms in the same root family have groups describing the same or related characteristics. If yes: note in the refinement log. This may be a Session D pointer candidate (same root, same characteristic across registries) or may inform the rewrite's precision.

### 4.8 Return Instruction Format

A return instruction is issued when a quality problem identified in Phase B or Phase B.5 cannot be resolved within the Dimension Review session and requires upstream reprocessing.

**File:** `wa-dim-return-{cluster}-{registry_no}-v{n}-{date}.md`

**Content:**

```
# WA-DIM-RETURN — Cluster {C##} Registry {nnn} ({word})
Date: {date} | Instruction version: WA-DimensionReview-v1.7-2026-04-09

## Reason for return

{State precisely what was found and why it cannot be resolved within the Dimension Review}

## Registry affected

Registry {nnn} — {word} | Cluster {C##}
Groups affected: {list of group_codes}
Terms affected: {list of strongs_number / transliteration}

## Return destination

{One of:}
- VCB re-run: Re-run Verse Context for the listed terms under WA-VerseContext-Instruction-v2.5.
  Specific instruction: {what the re-run must achieve — e.g. re-classify under characteristic-perspective model; re-group verses that are incorrectly combined}
- Session A / STEP extraction: Re-extract the listed terms from STEP.
  Specific instruction: {what is wrong with the source data and what the re-extraction must correct}

## Resume condition

The Dimension Review for Registry {nnn} resumes when:
{State the specific condition — e.g. VCB re-run complete and verse_context_status = Complete for Registry {nnn}; or re-extraction complete and mti_terms record corrected}

## Programme state at return

Dimension Review for Cluster {C##}: paused at Registry {nnn}
Registries in cluster reviewed before pause: {list}
Registries in cluster not yet reviewed: {list}
Patch status: {any patches produced and applied before the pause}
```

The return instruction is delivered to the researcher. The researcher directs Claude Code to execute the upstream process. The Dimension Review resumes when the resume condition is met.

---

## 5. Phase C — Dimension Discernment and Progressive Refinement

### 5.1 The Core Question

For each `QA-CLEAR` group (and each group that has passed Phase B.5 correction), Phase C asks two questions:

> 1. **What kind of inner-being characteristic does this group describe?** — assign a dimension from the vocabulary (Section 5.7), or name a new one.
> 2. **Who is the primary bearer of this characteristic in this group's verse evidence?** — assign a `dominant_subject` value (Section 1.7).

**Property-term dimension assignment:** Where a group derives from a property term, the dimension is assigned to the *inner-being characteristic the group serves* — not to the property term's function. A group describing *"faith received — akoē as channel"* carries the dimension of the characteristic (Cognition or Volition — faith as inner act of reception), not a dimension of hearing. This is the correct application of the characteristic-perspective model at the dimension assignment stage.

**Characteristic term dimension assignment:** Where a group derives from a characteristic term, the dimension is assigned to the characteristic directly. *"Stubbornness of heart — the inner condition of wilful self-determination"* carries Volition or Moral Character, depending on whether the emphasis is on the act of will or the stable disposition.

### 5.2 The Three Assignment Rules

**Rule 1 — The verse leads.** Read the `context_description`. Name what you actually see. Then check whether an existing dimension captures it.

**Rule 2 — If it could fit more than one dimension, assign the dominant one.** One label per group. Record the reasoning in `notes`.

**Rule 3 — If it fits no existing dimension, do not force it.** Name what the group shows in plain language. Flag as a candidate new dimension. Present to researcher. Do not assign an ill-fitting label.

### 5.3 Working Through a Group — Step by Step

1. Read the `context_description` (confirmed characteristic-perspective from Phase B/B.5)
2. Identify: is this a characteristic term or a property term group? (Section 1.8)
3. Ask: what inner-being characteristic does this group primarily describe?
4. Ask: who is the primary bearer — GOD, HUMAN, OTHER_HUMAN, UNSEEN, or NONE?
5. Check dimension vocabulary (Section 5.7) — does an existing dimension fit clearly?
6. Check whether any observation warrants a Session B or D pointer (Section 5.4)

### 5.4 Session B and D Pointer Capture

Analytical observations arising during Phase C that are relevant to Session B or cross-registry synthesis must be captured in the patch.

**Naming conventions:**

| Type | Convention | Example |
|---|---|---|
| Session B finding | `DIM-{registry_no}-{3-digit-sequence}` | `DIM-112-001` |
| Session D pointer | `DIM-{registry_no}-SD{3-digit-sequence}` | `DIM-112-SD001` |

**Root family pointers:** Cross-registry root families identified via the root family extract (Section 9.4) are strong candidates for Session D pointers. When the same root generates inner-being vocabulary in two or more registries with related or contrasting dimensions, capture this as a Session D pointer. Label: `DIM-{registry_no}-SD{sequence}` on the registry whose group triggered the observation.

**Uniqueness:** Check pre-existing pointers extract (Section 9.3) before inserting. Numbering must continue from the highest existing sequence, not restart from 001.

For insert formats, see Section 7.3.

### 5.5 Cross-Group Patterns Within a Cluster

When reviewing groups across a cluster, look for:

- **Convergence** — multiple groups from different registries naming the same characteristic
- **Divergence** — groups clustered together but engaging materially different inner-being aspects
- **Subject patterns** — a dimension appearing consistently in GOD vs HUMAN groups
- **Vocabulary gaps** — recurring characteristics that no existing dimension captures
- **Root family resonance** — groups from terms in the same root family showing related or contrasting dimension assignments

### 5.6 Anchor Verse Verification Sub-Process

**Purpose:** Verify that the verse evidence supporting each group is complete and coherent with the group description and dimension assignment. This is a completeness check — not Session B analysis.

**When to trigger:** Claude AI requests an anchor verse vertical pass extract (Section 9.5) when, during Phase B or Phase C:

- The group description has been rewritten in Phase B.5 and the new description names a characteristic that should be corroborated by the verse's full term-link context
- A group's anchor verse is in a key theological passage (multiple terms likely present) and the vertical pass data would confirm or challenge the dimension assignment
- A group's anchor verse was previously flagged in the session transcript or observations files as analytically complex
- A `QA-BROAD` flag was raised — the vertical pass data may reveal that the verse engages different characteristics through different terms, informing whether the grouping is correct

**What Claude AI checks from the vertical pass extract:**

1. **Correct placement:** Is this verse correctly assigned to this group under the characteristic-perspective model? Do the active term links in the verse support the characteristic described?
2. **Completeness:** Are there active term links in the same verse belonging to the current cluster that have no verse_context classification? If yes, this is a data gap — flag it.
3. **Unclassified terms:** Are there active term links with no group assignment (verse_context = [] or group = None)? Identify whether this represents a classification gap or an expected set-aside.
4. **Deleted terms:** Are there deleted term links (vr_deleted = 1 or mti_status = delete) that appear to have been incorrectly deleted? Apply the lev-pattern test: does the term have a status_note indicating it should be active? If yes, flag for REPAIR.
5. **Cross-registry coherence:** Does the verse's full term-link picture support the dimension assigned to this group? Do other registries' classifications of the same verse confirm or complicate the dimension?

**Findings from the vertical pass check are recorded in the refinement log.** Corrections are encoded in the cluster dimension patch. Detected data gaps (unclassified active terms, incorrectly deleted terms) are encoded as return instructions or REPAIR patches as appropriate.

**One extract per group.** A single vertical pass extract covers all anchor verses for one group. Do not request separate extracts for each anchor verse. See Section 9.5 for the naming convention.

**Do not over-request.** The vertical pass extract is an on-demand tool. It is not required for every group. Request it only when the trigger conditions above are met.

### 5.7 The Dimension Vocabulary

*Derived from data. Working vocabulary as of v1.7. Will be revised as additional data is reviewed.*

**01 — Emotion — Positive**
*Inner states of pleasure, joy, delight, or satisfaction*

**02 — Emotion — Negative**
*Inner states of pain, distress, grief, fear, anger, shame, or anxiety*

**03 — Cognition**
*Inner acts of knowing, perceiving, remembering, understanding, and discerning*

**04 — Volition**
*Inner acts of willing, purposing, choosing, desiring, and deciding*

Note: Volition is the *act* of willing. Stable orientation of the will toward God or others → consider Relational Disposition (06).

**05 — Moral Character**
*Stable inner qualities of moral nature — goodness, justice, integrity, purity, faithfulness*

**06 — Relational Disposition**
*Inner orientation toward another — love, compassion, favour, attachment, contempt, hatred*

**07 — Vitality / Existence**
*The animating life of the inner person — its constitution, continuation, fragility, and end*

**08 — Transformation**
*Inner change — renewal, healing, purification, formation, or degradation*

**09 — Agency / Power**
*The exercise of inner capacity — sovereignty, authority, strength, restraint, self-giving*

**10 — Dependence / Creatureliness**
*The inner posture of reliance — humility, dependence, trust, security*

**11 — Divine-Human Correspondence**
*Inner-being characteristics that operate across the boundary between God and the human person*

Assign when the same quality, act, or state appears in both divine and human subjects within the same group, or where God's inner-being characteristic is the direct ground, mirror, or counterpart of the human characteristic.

`dominant_subject` for this dimension: Assign `NONE` where the subject is genuinely dual. Assign `GOD` or `HUMAN` where one pole dominates but the correspondence is analytically significant. Record the God-human tension explicitly in notes.

**⚠ When no existing dimension fits:** Name what the group shows in plain language. Record in refinement log. Present to researcher. Do not assign a dimension that does not genuinely describe it.

---

## 6. Session Discipline

### 6.1 Unit of Work

The cluster is the unit of work. A session covers one cluster (or a portion of a large cluster). A session does not need to complete a cluster but must leave it in a clearly documented state.

### 6.2 File Writing Discipline

- After every registry reviewed in Phase B or C: write to the refinement log before proceeding
- On every write: state the current version and increment it
- Dual-write: working directory and `/mnt/user-data/outputs/`

### 6.3 Session Logs

Produce a session log at natural breakpoints. Session logs must record:
- Which cluster(s) and phases were covered
- Phase A findings
- Phase B quality flags and resolutions, including Phase B.5 corrections
- Any return instructions issued
- Coverage verification result
- Anchor verse verification findings (when triggered)
- Dimension proposals from Phase C and researcher responses
- Vocabulary gaps and Session B/D pointers
- Current refinement log version
- Dimension Review version stamp status (registry-level and cluster-level)
- Next steps

### 6.4 Startup Protocol

At the start of every new session continuing an existing Dimension Review:

1. State which cluster and phase is being continued
2. Confirm the refinement log version being loaded
3. State patch status — what was applied, what is pending
4. Confirm any unresolved flags, return instructions, or vocabulary questions from the prior session
5. Confirm the existing pointers extract has been loaded and highest existing sequence numbers noted
6. **VCB completeness check:** Confirm that all registries assigned to this cluster have `verse_context_status = Complete`. If any registry is at `In Progress` (including after a REPAIR), halt and note the dependency. Do not begin Phase A until all registries in the cluster have a complete VCB on their full active term set.
7. **Root family extract confirmed loaded:** State the extract filename and row count.

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
{What inner-being affinity holds this cluster together}

### Boundary observations
{Any misplaced words or ambiguous scope}

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

### Phase B.5 — Characteristic-perspective corrections (when triggered)
| Group code | Old description | New description | Correction route | Patch reference |
|---|---|---|---|---|

### Anchor verse verification (when triggered)
| Group code | Anchor verse | Vertical pass extract | Findings | Action |
|---|---|---|---|---|

### Return instructions issued (when triggered)
| Group code | Term | Return destination | Resume condition |
|---|---|---|---|

### Coverage verification (required once per cluster — confirm before first Phase C entry)
Groups in extract: {n} | Groups with Phase B entry: {n} | Coverage: CONFIRMED / GAP FOUND

### Phase C — Dimension assessment
| Group code | Context description | Dimension | Dominant subject | Confidence | Notes |
|---|---|---|---|---|---|

### Root family observations
{Patterns identified via root family extract — intra-registry and cross-registry}

### Vocabulary observations
{Groups fitting no existing dimension}

### Session B/D pointers captured
{List of finding_id / flag_label values, with one-line summary}

### Dimension Review version stamp
Registry {nnn}: dim_review_status = {Complete / Paused — return instruction issued}

### Pending researcher decisions
{Flags, vocabulary questions, proposed reassignments awaiting input}
```

### 7.3 Dimension Patch

JSON patch for Claude Code. One patch per cluster session. Patch type: `DIMREVIEW`. The `patch_id` must contain the string `DIMREVIEW`.

**Patch meta:**
```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-V{n}",
    "cluster": "{C##}",
    "produced_date": "{ISO date}",
    "produced_by": "WA-DimensionReview-Instruction-v1.7-2026-04-09",
    "session_b_status": null,
    "description": "Dimension review patch — {cluster}: {brief summary}"
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
    "dominant_subject": "{GOD|HUMAN|OTHER_HUMAN|UNSEEN|NONE}",
    "manual_override": 0,
    "notes": "{reasoning}",
    "last_modified": "{ISO datetime}"
  },
  "description": "{group_code} — {registry_word}: {brief description}"
}
```

**Group description correction operation (characteristic-perspective rewrite, within-session):**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "update",
  "table": "verse_context_group",
  "match": { "id": {verse_context_group_id} },
  "set": {
    "context_description": "{revised characteristic-perspective description}",
    "notes": "Revised during Dimension Review Phase B.5: term-centric description realigned to characteristic-perspective model. Old: {old description}"
  },
  "description": "Group {group_code}: characteristic-perspective rewrite"
}
```

Followed immediately by the `wa_dimension_index` context_description sync operation.

**Registry version stamp operation (after all groups for a registry are confirmed):**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "update",
  "table": "word_registry",
  "match": { "no": {registry_no} },
  "set": {
    "dim_review_status": "Complete",
    "dim_review_version": "WA-DimensionReview-Instruction-v1.7-2026-04-09"
  },
  "description": "Registry {nnn} ({word}): Dimension Review complete under v1.7"
}
```

**Cluster stamp operation (after all registries in cluster are confirmed — one insert into `wa_dim_review_cluster_log`):**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "insert",
  "table": "wa_dim_review_cluster_log",
  "record": {
    "cluster": "{C##}",
    "completed_date": "{ISO date}",
    "instruction_version": "WA-DimensionReview-Instruction-v1.7-2026-04-09",
    "registry_count": {n},
    "group_count": {n},
    "anchored_count": {n},
    "notes": "{any cluster-level observations}"
  },
  "description": "Cluster {C##} Dimension Review complete — stamp set"
}
```

**Session B findings insert and Session D pointer insert:** see Section 5.4 formats (unchanged from v1.6).

### 7.4 Group Description Correction Patch (out-of-session use only)

Patch type: `DIMREVIEW-GRPDESC`. Used only for corrections made outside a live cluster session. See v1.6 Section 7.4 for format. Unchanged.

---

## 8. Claude Code Protocol and Boundaries

### 8.1 Claude Code Responsibilities

| Task | Claude Code action |
|---|---|
| Construct cluster extract | Query per Section 9.1 |
| Construct root family extract | Query per Section 9.4 — filtered to cluster's registries |
| Construct existing pointers extract | Query per Section 9.3 |
| Construct anchor verse vertical pass extract | Query per Section 9.5 — on demand, per group |
| Apply dimension patch | Update `wa_dimension_index`; sync `context_description`; apply group description corrections; insert session B/D pointers; set registry and cluster stamps |
| Apply cluster reassignment patch | Update `word_registry.cluster_assignment` and `wa_dimension_index.cluster_assignment` |
| Apply schema additions | Create `word_registry.dim_review_status`, `word_registry.dim_review_version`, `wa_dim_review_cluster_log` per Section 10.3 |
| Post-application integrity check | Verify manual_override rows not incorrectly modified; verify context_description sync; verify stamp fields set correctly; report discrepancies |
| Trigger VC re-run | Reset `verse_context_status = 'In Progress'` for affected registry on researcher instruction |
| Regenerate dimension report | After each patch application cycle |

### 8.2 Claude Code Boundaries

Claude Code does not make analytical decisions. It does not:
- Determine dimensions or dominant subjects
- Assess group quality
- Decide whether a description is term-centric
- Write or approve revised descriptions
- Set `manual_override = 1` except on explicit researcher instruction in the patch
- Trigger VCB re-runs without researcher decision

### 8.3 Patch Validation — Claude Code

Before applying any Dimension Review patch:

1. `patch_id` not previously applied
2. All `wa_dimension_index.id` values exist
3. No operation targets `manual_override = 1` row without explicit override in operation
4. All `verse_context_group.id` values exist (for description corrections)
5. All `finding_id` values unique programme-wide
6. All `flag_label` values unique programme-wide
7. `session_b_status` in `_patch_meta` is `null`
8. All `dominant_subject` values are valid vocabulary
9. `dim_review_version` value is a recognised instruction version string
10. `wa_dim_review_cluster_log` insert: cluster code is a valid cluster assignment value in `word_registry`

### 8.4 Post-Application Reporting

After every patch application, Claude Code reports:
- Count of `wa_dimension_index` rows updated
- Count of rows now at `manual_override = 1`
- Count of `dominant_subject` values newly assigned
- Count of group descriptions corrected (Phase B.5 rewrites)
- Count of `wa_session_b_findings` rows inserted
- Count of `wa_session_research_flags` rows inserted
- Count of `word_registry` rows stamped (`dim_review_status = Complete`)
- Whether cluster stamp was set (insert into `wa_dim_review_cluster_log`)
- Integrity check findings

### 8.5 Patch Types

| Patch type | Governing instruction | Valid `session_b_status` | Content |
|---|---|---|---|
| `DIMREVIEW` | WA-DimensionReview-Instruction-v1.7 | `null` | `wa_dimension_index` updates; `verse_context_group` corrections; `wa_session_b_findings` inserts; `wa_session_research_flags` inserts; `word_registry` stamp updates; `wa_dim_review_cluster_log` inserts |
| `DIMREVIEW-GRPDESC` | WA-DimensionReview-Instruction-v1.7 | `null` | Out-of-session group description corrections only |

---

## 9. Data Extracts — Required Inputs for Claude AI

### 9.1 Cluster Extract — Primary Session Input

*(Unchanged from v1.6 except `produced_by` version string)*

**Extract name:** `wa-dim-extract-{cluster}-{date}.json`

All `wa_dimension_index` rows for the requested cluster, joined to `word_registry`, `verse_context_group`, `mti_terms`. All anchor and related verse arrays mandatory. See v1.6 Section 9.1 for full field mapping and JSON structure.

**`produced_by`:** `"Claude Code — WA-DimensionReview-Instruction-v1.7-2026-04-09"`

### 9.2 Group Description Verification Extract

*(Unchanged from v1.6)*

Constructed on demand when Phase B requires verse-level review before a description correction can be written.

**Extract name:** `wa-dim-grpverify-{group_code}-{date}.json`

### 9.3 Pre-existing Session B/D Pointer Extract

*(Unchanged from v1.6)*

**Extract name:** `wa-dim-existing-pointers-{cluster}-{date}.json`

Includes all existing entries for cluster registries — both Dimension Review and Verse Context batch flags.

### 9.4 Root Family Cluster Extract — Standard Session Input

**Extract name:** `wa-dim-rootfamily-{cluster}-{date}.json`

Claude Code constructs this extract at the same time as the cluster extract. It is a required session input, not optional.

**Scope:** All root families where at least one term belongs to a registry assigned to the current cluster. For each root family in scope: all terms in the family (including those in other clusters/registries), all groups for each term, and anchor verses for each group.

**Purpose:** Provides the root-family axis of analytical relationship for Phase C cross-group pattern detection (Section 5.5), Phase B.5 root family check (Section 4.7 Step 5), and Session D pointer identification. Enables identification of intra-registry root families (multiple terms in same registry sharing a root) and cross-registry root families (same root generating terms in different registries).

**JSON structure:**

```json
{
  "extract_meta": {
    "extract_type": "dimension_review_rootfamily",
    "cluster": "C##",
    "produced_date": "YYYY-MM-DD",
    "produced_by": "Claude Code — WA-DimensionReview-Instruction-v1.7-2026-04-09",
    "governing_instruction": "WA-DimensionReview-Instruction-v1.7-2026-04-09",
    "root_count": 0,
    "group_count": 0,
    "cross_registry_root_count": 0
  },
  "roots": [
    {
      "root_code": "...",
      "root_language": "Hebrew|Greek|null",
      "root_gloss": "...",
      "in_cluster_registries": [32, 153],
      "cross_registry": true,
      "term_count": 0,
      "group_count": 0,
      "terms": [
        {
          "strongs_number": "...",
          "transliteration": "...",
          "gloss": "...",
          "language": "...",
          "reg_no": 0,
          "reg_word": "...",
          "cluster_assignment": "C##",
          "in_current_cluster": true
        }
      ],
      "groups": [
        {
          "group_code": "...",
          "context_description": "...",
          "strongs_number": "...",
          "transliteration": "...",
          "gloss": "...",
          "registry_no": 0,
          "registry_word": "...",
          "cluster_assignment": "C##",
          "dimension": "...",
          "dimension_confidence": "...",
          "dominant_subject": null,
          "manual_override": 0,
          "anchor_verses": [
            {
              "verse_record_id": 0,
              "book": "...",
              "chapter": 0,
              "verse": 0,
              "reference": "...",
              "verse_text": "..."
            }
          ]
        }
      ]
    }
  ]
}
```

**Claude Code query specification:**

```sql
-- Step 1: Identify all root_codes where at least one term belongs to the current cluster
SELECT DISTINCT rf.root_code
FROM wa_term_root_family rf
JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE wr.cluster_assignment = '{C##}'
  AND rf.delete_flagged = 0
  AND ti.delete_flagged = 0;

-- Step 2: For each root_code identified, retrieve all terms in the root family
-- (including terms from other registries/clusters)
SELECT rf.root_code, rf.root_language, rf.root_gloss,
       mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
       wr.no as reg_no, wr.word as reg_word, wr.cluster_assignment
FROM wa_term_root_family rf
JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
JOIN mti_terms mt ON mt.id = ti.mti_term_id
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
WHERE rf.root_code IN ({root_codes_from_step_1})
  AND rf.delete_flagged = 0
  AND ti.delete_flagged = 0
  AND mt.status IN ('extracted', 'extracted_thin')
ORDER BY rf.root_code, wr.no;

-- Step 3: For each term, retrieve its groups and anchor verses from wa_dimension_index
SELECT wdi.group_code, wdi.context_description, wdi.dimension,
       wdi.dimension_confidence, wdi.dominant_subject, wdi.manual_override,
       wdi.owning_registry_no, wdi.owning_registry_word, wdi.cluster_assignment,
       mt.strongs_number, mt.transliteration, mt.gloss
FROM wa_dimension_index wdi
JOIN mti_terms mt ON mt.id = wdi.mti_term_id
WHERE mt.strongs_number IN ({strongs_from_step_2})
  AND wdi.delete_flagged = 0;

-- Anchor verses are retrieved per group via verse_context and wa_verse_records
-- (same join as cluster extract Section 9.1)
```

**`cross_registry` flag:** Set `true` for any root family where `in_cluster_registries` contains registries from more than one cluster. These are the highest-priority root families for Session D pointer capture.

**`in_current_cluster` flag:** Set `true` for terms whose registry is assigned to the current cluster. Terms from other clusters are included for context but flagged accordingly.

### 9.5 Anchor Verse Vertical Pass Extract — On-Demand Sub-Process Input

**Extract name:** `wa-dim-vpass-{cluster}-{group_code}-{date}.json`

| Component | Rule |
|---|---|
| `wa-dim-vpass` | Fixed prefix — always present, always lowercase |
| `{cluster}` | Cluster being reviewed — e.g. `c02` |
| `{group_code}` | Group code of the group whose anchor verses are being verified — e.g. `758-001` |
| `{date}` | Date of extract construction — `YYYYMMDD` |

**⚠ Naming discipline is mandatory.** One extract per group (both anchor verses for a group are in the same file). Extracts accumulate under `wa-dim-vpass-{cluster}-` prefix and sort together. Do not use verse references, registry names, or other identifiers in the filename — the group_code is the only permissible identifier after the cluster. A file named `wa-dim-vpass-c02-jer7-24-20260409.json` is a naming violation.

**Trigger conditions** (Section 5.6). Requested only when one of the specified conditions is met. Not for every group.

**Content:** For each anchor verse of the group: full verse text, all term links (active and deleted), for each active term link: verse_context classification, all groups for that term, root and siblings. This matches the structure demonstrated in `wa-verticalpass-jer7-24-2026-04-09.json`.

**JSON structure:**

```json
{
  "extract_meta": {
    "extract_type": "dim_review_vpass",
    "cluster": "C##",
    "group_code": "...",
    "context_description": "...",
    "registry_no": 0,
    "registry_word": "...",
    "produced_date": "YYYY-MM-DD",
    "produced_by": "Claude Code — WA-DimensionReview-Instruction-v1.7-2026-04-09",
    "anchor_verse_count": 0
  },
  "anchor_verses": [
    {
      "verse_record_id": 0,
      "reference": "...",
      "verse_text": "...",
      "total_term_links": 0,
      "active_term_links": 0,
      "registries_touched": 0,
      "clusters_touched": 0,
      "roots_involved": 0,
      "term_links": [
        {
          "verse_record_id": 0,
          "vr_deleted": 0,
          "target_word": "...",
          "span_strong_match": 1,
          "strongs_number": "...",
          "transliteration": "...",
          "gloss": "...",
          "language": "...",
          "mti_id": 0,
          "mti_status": "...",
          "term_owner_type": "...",
          "registry_no": 0,
          "registry_word": "...",
          "cluster": "...",
          "verse_context": [
            {
              "vc_id": 0,
              "group_id": 0,
              "is_anchor": 0,
              "is_relevant": 1,
              "is_related": 0,
              "set_aside_reason": null,
              "vc_notes": null,
              "vc_deleted": 0,
              "group_code": "...",
              "context_description": "...",
              "dimension": "...",
              "dimension_confidence": "...",
              "dominant_subject": null,
              "manual_override": 0
            }
          ],
          "all_groups_for_term": [
            {
              "group_code": "...",
              "context_description": "...",
              "dimension": "...",
              "dimension_confidence": "...",
              "dominant_subject": null,
              "verse_count": 0
            }
          ],
          "root": {
            "root_code": "...",
            "root_language": "...",
            "root_gloss": "...",
            "siblings": [
              {
                "strongs_number": "...",
                "transliteration": "...",
                "gloss": "...",
                "reg_no": 0,
                "reg_word": "..."
              }
            ]
          }
        }
      ]
    }
  ]
}
```

**Claude Code CC directive format:** CA produces a `.md` directive when requesting this extract:

**Directive file:** `wa-dim-cc-directive-vpass-{cluster}-{group_code}-{date}.md`

```
# WA-DIM CC Directive — Anchor Verse Vertical Pass Extract
Date: {date}
Cluster: {C##}
Group: {group_code}
Registry: {nnn} ({word})

## Request
Construct anchor verse vertical pass extract for group {group_code}.
Anchor verses: {list verse_record_ids from cluster extract}

## Output file
wa-dim-vpass-{cluster}-{group_code}-{date}.json

## Reason for request
{One of the trigger conditions from Section 5.6 — state which condition applies}
```

---

## 10. Dimension Review Version Stamps

### 10.1 Purpose

The version stamp system records, at both registry and cluster level, which version of the Dimension Review instruction was used to review and confirm the data. Session B gates on the cluster-level stamp. The stamps ensure that Session B always operates on data that has been quality-assured under a known, versioned instruction.

### 10.2 Registry-Level Stamp

When all groups for a registry have passed Phase B (including Phase B.5 where triggered) and Phase C dimension assignments are confirmed, the registry receives a version stamp in the cluster dimension patch:

| Field | Table | Value |
|---|---|---|
| `dim_review_status` | `word_registry` | `Complete` |
| `dim_review_version` | `word_registry` | `WA-DimensionReview-Instruction-v1.7-2026-04-09` |

If a registry cannot complete Dimension Review (return instruction issued), the stamp is not set. The field remains NULL and the return instruction documents the reason.

### 10.3 Cluster-Level Stamp

When all registries in a cluster have `dim_review_status = Complete`, Claude Code inserts a record into `wa_dim_review_cluster_log`. This is the Session B gate.

**Schema addition required** — Claude Code must apply the following DDL before the first cluster stamp is set:

```sql
-- Field additions to word_registry
ALTER TABLE word_registry ADD COLUMN dim_review_status TEXT DEFAULT NULL;
ALTER TABLE word_registry ADD COLUMN dim_review_version TEXT DEFAULT NULL;

-- New cluster log table
CREATE TABLE wa_dim_review_cluster_log (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  cluster             TEXT    NOT NULL UNIQUE,
  completed_date      TEXT    NOT NULL,
  instruction_version TEXT    NOT NULL,
  registry_count      INTEGER NOT NULL DEFAULT 0,
  group_count         INTEGER NOT NULL DEFAULT 0,
  anchored_count      INTEGER NOT NULL DEFAULT 0,
  notes               TEXT,
  last_modified       TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now'))
);
```

**⚠ Schema additions are applied once, before the first DIMREVIEW patch that includes a stamp operation.** Claude Code confirms the columns/table exist before applying any stamp operation. If not yet applied, Claude Code applies the DDL, confirms success, then proceeds with the patch.

### 10.4 Session B Gate

Session B DataPrep for a cluster may begin only when:

1. `wa_dim_review_cluster_log` contains a record for the cluster (`cluster = '{C##}'`)
2. All registries in the cluster have `word_registry.dim_review_status = Complete`
3. All registries in the cluster have `word_registry.verse_context_status = Complete`

**Claude Code gate check query:**

```sql
-- Check all three conditions for a cluster before Session B
SELECT
  wr.no,
  wr.word,
  wr.verse_context_status,
  wr.dim_review_status,
  wr.dim_review_version,
  CASE WHEN dcl.cluster IS NOT NULL THEN 'SET' ELSE 'NOT SET' END as cluster_stamp
FROM word_registry wr
LEFT JOIN wa_dim_review_cluster_log dcl ON dcl.cluster = wr.cluster_assignment
WHERE wr.cluster_assignment = '{C##}'
  AND wr.session_b_status IS NOT NULL
ORDER BY wr.no;
-- Session B gate: all rows must show
--   verse_context_status = 'Complete'
--   dim_review_status = 'Complete'
--   cluster_stamp = 'SET'
```

If any row fails any condition, Session B does not open for that cluster.

### 10.5 Monitoring Query

```sql
-- Programme-wide Dimension Review progress
SELECT
  wr.cluster_assignment,
  COUNT(*) as registry_count,
  SUM(CASE WHEN wr.dim_review_status = 'Complete' THEN 1 ELSE 0 END) as dim_complete,
  SUM(CASE WHEN wr.verse_context_status = 'Complete' THEN 1 ELSE 0 END) as vcb_complete,
  CASE WHEN dcl.cluster IS NOT NULL THEN dcl.instruction_version ELSE 'NOT SET' END as cluster_stamp
FROM word_registry wr
LEFT JOIN wa_dim_review_cluster_log dcl ON dcl.cluster = wr.cluster_assignment
WHERE wr.session_b_status IS NOT NULL
GROUP BY wr.cluster_assignment
ORDER BY wr.cluster_assignment;
```

---

## 11. Decision Rules and Boundaries

### 11.1 Claude AI Never Acts Unilaterally On

- Cluster reassignments
- Vocabulary additions, splits, or renamings
- Setting `manual_override = 1`
- Triggering a Verse Context batch re-run
- Marking a group as `delete_flagged`
- Writing revised `context_descriptions` to the patch without researcher confirmation
- Setting cluster stamps — these are set by Claude Code after all registries in the cluster are confirmed

### 11.2 Claude AI May Propose Independently

- Dimension assignments for any group
- `dominant_subject` assignments
- Corrections to existing labels that do not match group content
- Quality flags including `QA-TERMCENTRIC`
- Characteristic-perspective rewrites under Phase B.5 (proposed — confirmed before patch)
- Anchor verse vertical pass extract requests (produces CC directive independently)
- Candidate new dimension names where no existing dimension fits
- Session B/D pointer content
- Return instructions (issued independently when the conditions in Section 4.8 are met; researcher is informed)

---

## 12. Integrity Rules

| Rule | Requirement |
|---|---|
| DR-1 | No dimension may be anchored (`manual_override = 1`) without researcher confirmation |
| DR-2 | No cluster reassignment may be patched without researcher confirmation |
| DR-3 | Phase C must not begin for a group until its Phase B quality flag is resolved |
| DR-4 | KEYWORD_STRONG groups still require Phase C review — not auto-confirmed |
| DR-5 | Group description corrections must be researcher-confirmed before encoding in a patch |
| DR-6 | `wa_dimension_index.context_description` must be kept in sync with `verse_context_group.context_description` at all times |
| DR-7 | Dimension Review patches carry `session_b_status: null` |
| DR-8 | No patch may update a row with `manual_override = 1` except on explicit researcher instruction |
| DR-9 | Session B/D pointer `finding_id` and `flag_label` values must be unique programme-wide |
| DR-10 | Every group in the cluster extract must have a Phase B entry before Phase C begins |
| DR-11 | `dominant_subject` must be assigned for every group in Phase C — NULL is not valid post-review |
| DR-12 | `dominant_subject` values restricted to: GOD, HUMAN, OTHER_HUMAN, UNSEEN, NONE |
| DR-13 | The dimension vocabulary may only be extended by researcher decision |
| DR-14 | A `QA-TERMCENTRIC` group must not advance to Phase C until Phase B.5 correction is complete or a return instruction is issued |
| DR-15 | The anchor verse vertical pass extract must follow the naming convention `wa-dim-vpass-{cluster}-{group_code}-{date}.json` exactly — no other naming is permitted |
| DR-16 | Session B may not open for a cluster until `wa_dim_review_cluster_log` contains a record for that cluster and all registries show `dim_review_status = Complete` |
| DR-17 | Schema additions (Section 10.3) must be applied before the first stamp operation — Claude Code verifies before applying any stamp |
| DR-18 | A registry that has received a return instruction retains `dim_review_status = NULL` until the upstream process completes and the Dimension Review resumes and confirms the registry |

---

## 13. Naming Conventions

| File type | Pattern | Example |
|---|---|---|
| Cluster extract | `wa-dim-extract-{cluster}-{date}.json` | `wa-dim-extract-c01-2026-04-09.json` |
| Root family cluster extract | `wa-dim-rootfamily-{cluster}-{date}.json` | `wa-dim-rootfamily-c01-2026-04-09.json` |
| Group verification extract | `wa-dim-grpverify-{group_code}-{date}.json` | `wa-dim-grpverify-3012-001-2026-04-09.json` |
| Anchor verse vertical pass extract | `wa-dim-vpass-{cluster}-{group_code}-{date}.json` | `wa-dim-vpass-c02-758-001-2026-04-09.json` |
| CC directive — group verification | `wa-dim-cc-directive-grpverify-{group_code}-{date}.md` | `wa-dim-cc-directive-grpverify-3012-001-2026-04-09.md` |
| CC directive — vertical pass | `wa-dim-cc-directive-vpass-{cluster}-{group_code}-{date}.md` | `wa-dim-cc-directive-vpass-c02-758-001-2026-04-09.md` |
| Existing pointers extract | `wa-dim-existing-pointers-{cluster}-{date}.json` | `wa-dim-existing-pointers-c01-2026-04-09.json` |
| Dimension refinement log | `wa-dim-refinement-log-{cluster}-v{n}-{date}.md` | `wa-dim-refinement-log-c02-v1.0-2026-04-09.md` |
| Dimension patch | `wa-dim-patch-{cluster}-v{n}-{date}.json` | `wa-dim-patch-c01-v1-2026-04-09.json` |
| Group description correction patch (out-of-session) | `wa-dim-grpdesc-patch-{scope}-v{n}-{date}.json` | `wa-dim-grpdesc-patch-vcb029-all-v2-2026-04-09.json` |
| Return instruction | `wa-dim-return-{cluster}-{registry_no}-v{n}-{date}.md` | `wa-dim-return-c02-213-v1-2026-04-09.md` |
| Session log | `wa-dim-session-log-{scope}-v{n}-{date}.md` | `wa-dim-session-log-c01-v1-2026-04-09.md` |

**Note on patch_id patterns:**
- Cluster dimension patch: `PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-V{n}` — e.g. `PATCH-20260409-DIMREVIEW-C01-V1`
- Out-of-session group description correction: `PATCH-{YYYYMMDD}-DIMREVIEW-GRPDESC-{scope}-V{n}`

All filenames lowercase. Cluster codes lowercase in filenames (c01, c02) even where referred to as C01, C02 in prose.

---

*WA-DimensionReview-Instruction-v1.7-2026-04-09 | Supersedes v1.6-2026-04-08 | v1.7: Root family extract added as standard session input (Section 9.4); anchor verse vertical pass extract added as on-demand sub-process (Section 9.5); QA-TERMCENTRIC flag and Phase B.5 characteristic-perspective correction sub-process added (Sections 4.3, 4.7); return instruction format specified (Section 4.8); fix-or-stop principle stated (Section 0); cluster and registry version stamps added (Section 10); two new schema fields and one new table specified (Section 10.3); Session B gate updated to require cluster stamp (Section 10.4); startup VCB completeness check added (Section 6.4); property-term dimension assignment guidance added (Section 5.1); companion document updated to v2.5; 5 new integrity rules DR-14 through DR-18*
