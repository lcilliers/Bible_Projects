# WA-DimensionReview-Instruction-v2.2-2026-04-11

**Framework B — Soul Word Analysis Programme**
**Dimension Review Instruction — Claude AI and Claude Code**
**Version 2.2 | April 2026 | Status: Active governing instruction**

| **Document** | **Value** |
|---|---|
| Filename | WA-DimensionReview-Instruction-v1.10-20260414.md |
| Supersedes | WA-DimensionReview-Instruction-v1.9-20260409.md |
| Change note | v1.10 (20260414): Global rules integration. (1) Governing Rules header added — mandatory load of wa-global-general-rules-v2-20260414.json before session start. (2) Section 0 write-on-discovery paragraph removed — replaced with reference to GR-OBS-001. (3) Sections 1.1 and 1.3 "no pre-formed categories" text removed — replaced with reference to GR-PROG-002. (4) Section 1.6 "all changes through patches" paragraph removed — replaced with reference to GR-PROC-003. (5) Section 6.2 file writing versioning rule corrected: version-increment occurs when resuming work in a new session, not on every file save (resolves conflict between DR instruction and programme memory). (6) Companion documents table: WA-SessionB-Analysis-Instruction-v5.7 corrected to WA-SessionB-Instruction-v4.8; all dates updated to compact format. (7) All filename examples updated to compact date format per GR-FILE-009, lowercase per GR-FILE-007. |
| Companion documents | WA-VerseContext-Instruction-v2.5-20260409 │ WA-SessionB-Instruction-v4.8-20260414 │ WA-Reference-v5.5-20260330 │ WA-Registry-Management-Guide-v5.8-20260412 │ patch_specification-v1.10-20260412 │ WA-SessionD-Orientation-v3.0-20260412 │ WA-dim-session-log-methodology-v2.1-20260408.md |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules-v2-20260414.json**.

Claude AI must confirm the global rules file has been loaded before beginning any work in this session. State aloud: *"Global rules wa-global-general-rules-v2-20260414.json loaded."*

Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.

---
| Inputs | wa-dimension-report-{date}.md │ wa-registry-overview-{date}.json │ database_schema_{date}.json │ Dimension Review cluster extract — wa-dim-{cluster}-extract-{date}.json (Claude Code → Claude AI) │ Root family cluster extract — wa-dim-{cluster}-rootfamily-{date}.json (Claude Code → Claude AI) │ Pre-existing pointers extract — wa-dim-{cluster}-existing-pointers-{date}.json (Claude Code → Claude AI) │ Anchor verse vertical pass extract — wa-dim-{cluster}-vpass-{group_code}-{date}.json (Claude Code → Claude AI, on demand) │ wa-vcb-{batch_id}-term-observations files (where group description correction is required) |
| Outputs | Observations log — wa-dim-{cluster}-observations-v{n}-{date}.md (Claude AI, written continuously during session) │ Dimension patch — wa-dim-{cluster}-patch-v{n}-{date}.json (Claude AI → Claude Code, produced in separate patch session from observations log) │ Group description correction patch — wa-dim-{cluster}-grpdesc-patch-v{n}-{date}.json (Claude AI → Claude Code, when triggered) │ Return instruction — wa-dim-{cluster}-{registry_no}-return-v{n}-{date}.md (Claude AI → researcher, when upstream re-run required) │ Session log — wa-dim-{cluster}-session-log-v{n}-{date}.md (Claude AI, at breakpoints) |
| Claude AI role | Cluster assignment review, group quality assessment, characteristic-perspective correction, dimension discernment, dominant subject identification, anchor verse verification, progressive refinement, Session B/D pointer capture, observations log maintenance, patch production (separate patch session), return instruction production |
| Claude Code role | Cluster extract construction, root family extract construction, existing pointers extract construction, anchor verse vertical pass extract construction (on demand), patch application to `wa_dimension_index`, `verse_context_group`, `wa_session_b_findings`, `wa_session_research_flags`, manual_override locking, dimension confidence field updates, dominant_subject field updates, VC batch re-run triggering where required, registry and cluster stamp updates, post-application integrity checks, dimension report regeneration |
| Interaction model | Claude Code constructs cluster extract + root family extract + existing pointers extract → Claude AI runs analytical session (Phases A–C), writing observations log continuously → Claude AI runs patch session reading observations log → researcher reviews patch → Claude Code applies → loop until cluster anchored → advance to next cluster |

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

**The write-on-discovery principle (per GR-OBS-001 — non-waivable):**

Every analytical decision is written to the observations log immediately on discovery. Nothing is accumulated in memory. The observations log is the complete and authoritative record of the analytical session.

**Stage sequence:**
```
Verse Context Complete (all 181 registries)
     │
     ▼
Claude Code: construct cluster extract + root family extract + existing pointers extract
     │
     ▼
Dimension Review — Analytical Session (this document) — per cluster
  ├── Phase A: Cluster assignment review
  ├── Phase B: Group quality review (including QA-TERMCENTRIC screening)
  │     ├── Phase B.5: Characteristic-perspective correction sub-process (when QA-TERMCENTRIC raised)
  │     ├── Anchor verse verification (Section 5.6) — on demand during Phase B or C
  │     └── Coverage verification (Section 4.6) — mandatory before Phase C begins
  └── Phase C: Dimension discernment and progressive refinement (iterative)
        ├── Claude AI: read group, assign dimension + dominant_subject
        ├── Researcher: confirm, refine, or reject
        └── Loop until cluster complete
     │
     ▼   [All decisions written to observations log throughout]
     │   [Observations log version incremented on every write — no filename reuse]
     │
  └── Phase C complete for a registry ──────────────────────────────────────┐
                                                                             │
Dimension Review — Per-Registry Patch (inline — no separate session) ◄──────┘
  ├── Claude AI reads completed registry entries from observations log
  ├── Claude AI constructs patch for this registry only
  ├── Claude AI delivers patch to researcher
  ├── Researcher reviews → Claude Code applies
  └── Claude AI continues to next registry
     │
     ▼   [Final registry patch includes cluster stamp]
     │
Researcher reviews final patch → Claude Code applies → confirms cluster stamp → advance to next cluster
     │
     ▼
Session B DataPrep gate (all clusters complete AND cluster stamps set)
```

| This document is self-standing. It does not rely on session memory. The analytical session requires this document, the cluster extract, the root family extract, and the existing pointers extract. Per-registry patch production is inline — no separate patch session is needed. Claude Code requires this document and the patch specification. |
|---|

---

## 0.2 Operation Modes

The Dimension Review operates in two modes. The mode is declared at startup (Section 6.4, Step 0) and determines scope, stamp rules, and inputs throughout.

### Cluster Mode (normal pipeline path)

**Invoked by:** Normal Dimension Review processing — one cluster at a time, after all registries in the cluster have `verse_context_status = Complete`.

**Scope:**
- Phase A: Full cluster
- Phase B: Full cluster
- Phase C: Full cluster — all registries
- Stamps: Registry-level stamps set for each registry as it completes Phase C. Cluster-level stamp set when all registries in the cluster are complete.

**Gate:** Cluster Mode completion is the DataPrep gate — `wa_dim_review_cluster_log` must contain a record for the cluster before Session B DataPrep may open for any registry in that cluster.

### Registry Mode (Session B Stage 1 sub-process)

**Invoked by:** Session B Stage 1 Step C, when the audit finds `dim_review_status = null` or `dominant_subject = null` for any group in the target registry — i.e. the Dimension Review has not been run for this registry before Session B begins.

**Scope:**
- Phase A: Full cluster — analytical coherence requires reading the full cluster context even when only one registry is the target. Do not skip Phase A.
- Phase B: Full cluster — QA-TERMCENTRIC screening requires full cluster context. Do not skip Phase B. Record Phase B findings for all registries in the cluster in the observations log — these findings are available for the full cluster session when it runs.
- Phase C: Scoped to the target registry only — dimension assignment, dominant subject, and all Phase C steps apply only to the groups belonging to the target registry.
- Stamps: Registry-level stamp is set for the target registry. Cluster-level stamp is NOT set — the cluster has not been fully reviewed.

**Gate:** Registry Mode completion does not satisfy the DataPrep gate for the cluster. It satisfies only the Stage 2 gate for the target registry (all groups at CLAUDE_AI confidence with dominant_subject assigned, and dim_review_status = Complete on the registry record). The full cluster session must still be run to set the cluster-level stamp.

**Why Phase B must span the full cluster in Registry Mode:**
Phase B.5 (characteristic-perspective correction) requires understanding what inner-being characteristic a group serves — a judgement that requires the context of what other groups in the cluster describe. A group from the target registry that looks term-centric in isolation may be interpretable when adjacent groups in the same cluster are seen. Conversely, a group that looks clear in isolation may reveal a QA-TERMCENTRIC problem when the cluster's other groups provide the contrast needed to see it. Phase B quality assessment is not reliable when scoped to a single registry.

**Two-gate system:**

| Gate | What satisfies it | What it opens |
|---|---|---|
| Stage 2 gate (Registry Mode) | dim_review_status = Complete on registry + all groups CLAUDE_AI + all dominant_subject assigned | Session B Stage 2 may begin for this registry |
| DataPrep gate (Cluster Mode) | wa_dim_review_cluster_log record for cluster | Session B DataPrep for any registry in the cluster |

These gates are independent. A registry may proceed to Stage 2 under the Registry Mode gate even when the cluster's DataPrep gate is not yet satisfied.

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

Per GR-PROG-002: no dimension category is assumed correct before the group content has been read. The automated labels are a starting hypothesis — useful as orientation, not as conclusion. The confirmed dimension vocabulary (Section 5.7) is a working starting point derived from data, not an authoritative final system.

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

Per GR-PROG-002: the vocabulary in Section 5.7 was derived from data and represents the current best understanding. It will be revised as more data is reviewed. When a group does not fit any existing dimension, that is a finding, not a failure.

*Current vocabulary: 11 dimensions (updated v1.6 — dimension 11 Divine-Human Correspondence added from C18 data).*

### 1.4 Group Quality Is the Prerequisite

A dimension assignment is only as reliable as the group it is assigned to. Phase B must be complete — and all quality problems resolved — for every group in the cluster extract before Phase C proceeds for any registry. The fix-or-stop principle applies without exception.

### 1.5 Session B Will Arise from the Data

When the Dimension Review is done well — clusters validated, groups quality-checked, dimensions grounded in group content — Session B analysis will have a clear foundation. Rushing this stage is counterproductive. Session B depth is directly proportional to Dimension Review quality.

### 1.6 All Changes Go Through the Patch Process

Per GR-PROC-003 (non-waivable). No corrections to group descriptions, dimension assignments, or any database field are made by direct manipulation. Every change is encoded in a patch file, reviewed by the researcher, and applied by Claude Code.

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

**Before assessing coherence, identify excluded registries:** Any registry in the cluster with `session_b_status = "Analysis Complete"` is excluded from Phase B and Phase C (Section 6.4 Step 6). These registries are still visible in the Phase A cluster picture — their presence is noted and they inform the coherence assessment — but they are explicitly marked as excluded from further processing. Their group counts are not included in the active group total.

For each cluster, Claude AI assesses the active (non-excluded) registries:

1. **Internal coherence** — Do the words share genuine inner-being affinity?
2. **Boundary cases** — Are there words predominantly about external acts, divine attributes, or social structures?
3. **Missing affinity** — Are there words with stronger affinity for a different cluster?
4. **Size** — Very small clusters (fewer than 4 active words) or very large clusters (more than 13 active words) warrant review

### 3.3 Output

Write Phase A findings to observations log immediately. Format per Section 7.2.

---

## 4. Phase B — Group Quality Review

### 4.1 Purpose

Assess the quality of every group's `context_description` before dimension assignment begins. Every group belonging to an **active registry** (i.e. `session_b_status ≠ "Analysis Complete"`) receives a QA flag. Groups belonging to excluded registries (`session_b_status = "Analysis Complete"`) are skipped entirely — no QA flag is assigned, no entry is written to the observations log for those groups, and they do not appear in coverage verification counts.

### 4.2 QA Flag Vocabulary

| Flag | Meaning |
|---|---|
| `QA-CLEAR` | Description is sufficient for dimension assignment — characteristic-perspective model applied |
| `QA-TERMCENTRIC` | Description names what the term does rather than the inner-being characteristic served — triggers Phase B.5 |
| `QA-VAGUE` | Description is too brief or general to support dimension assignment |
| `QA-BROAD` | Description conflates two or more distinct inner-being characteristics in a single group |
| `QA-EXTERNALISED` | Description focuses on external circumstances rather than the inner-being characteristic |
| `QA-REVIEW` | Requires closer examination — potential data issue, conflicting evidence, or ambiguous construction |

### 4.3 QA-TERMCENTRIC — Definition

A group description is term-centric when it names what the term does rather than what inner-being characteristic the term serves in that verse context.

**Indicators:**
- Description begins with the term name followed by "as [action verb]ing"
- Description restates the term's lexical meaning without naming the inner-being state engaged
- No inner-being characteristic is named anywhere in the description

**Test:** Could this description apply equally to a verse where the inner-being content is entirely different? If yes — it is term-centric.

A term-centric description does not mean the group or its verse assignments are wrong — it means the description needs realignment. Phase B.5 corrects it.

### 4.4 Scope of Phase B

Phase B reads `context_descriptions` as recorded. It does not re-read original verse texts unless a verification extract or vertical pass extract is provided. If a description is found inadequate, the correction route is determined per Sections 4.5 or 4.7.

Write every QA flag assignment to the observations log immediately on assessment. Do not accumulate flags for later writing.

### 4.5 Group Description Correction Protocol (non-termcentric)

For groups flagged `QA-VAGUE`, `QA-BROAD`, `QA-EXTERNALISED`, or `QA-REVIEW`:

**Step 1 — Claude AI assessment.** State: (a) what is inadequate; (b) what a better description would need to capture; (c) a proposed revision if resolvable from existing context; (d) whether verse text review is needed. Write to observations log.

**Step 2 — Researcher decision.** Confirm, amend, or reject. May direct verse-level review.

**Step 2a — CC directive for verification extract.** When verse-level review is needed: CA produces a `.md` directive to CC (Section 9.2). CC constructs and returns the group description verification extract.

**Step 3 — Correction options:**

| Scenario | Action |
|---|---|
| Correction clear, no verse assignment impact | Record in observations log; encoded in patch during patch session |
| Correction requires reviewing which verses belong | Record in observations log; researcher decides whether to trigger VCB re-run |
| Group may be incorrectly constructed | Researcher may trigger VCB re-run |

**Step 4 — After patch application.** Claude Code syncs `wa_dimension_index.context_description` with `verse_context_group.context_description`. Confirms before Phase C proceeds.

**Step 5 — Re-run trigger.** If VCB re-run triggered: governed by WA-VerseContext-Instruction-v2.5. Dimension Review for affected registry resumes after re-run completes.

### 4.6 Mandatory Coverage Verification

**⚠ Before Phase C begins for any registry, Claude AI must verify that every group belonging to an active registry has a Phase B entry in the observations log.**

1. Identify all excluded registries (`session_b_status = "Analysis Complete"`) and sum their group counts
2. Subtract excluded group counts from `extract_meta.row_count` to obtain the **active group count**
3. Count unique group codes recorded in Phase B entries in the observations log
4. If counts match: coverage confirmed — write confirmation to observations log (stating both the active count and the excluded count) and proceed to Phase C
5. If counts do not match: perform Phase B on missing active groups before proceeding

**Coverage verification entry format (updated):**
```
[COVERAGE-VERIFY] {cluster}
Groups in extract (total): {n}
Excluded registries (Analysis Complete): {list of reg_no/word} — {n} groups excluded
Active groups requiring Phase B: {n}
Groups with Phase B entry in observations log: {n}
Result: CONFIRMED / GAP FOUND — {list missing group codes if gap found}
```

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

Write the revised description to the observations log immediately — both the old and new text, with rationale.

**Examples of compliant rewrites:**

| Old (term-centric) | New (characteristic-perspective) |
|---|---|
| *Hearing as the inner receptive faculty (faith, understanding, response)* | *Faith received — akoē as the channel through which faith arrives* |
| *Refusing to hear God* | *Heart-stubbornness expressed through refusal of God's word — sha.ma absent* |
| *Obeying God's voice: the inner act of covenantal obedience* | *Covenantal will — sha.ma as the act by which the will's orientation toward God is expressed* |
| *Ear as faculty for receiving divine address* | *Spiritual receptivity and its refusal — o.zen as the inner faculty through which divine word is received* |

**Step 3 — Assess grouping soundness.**

When the characteristic cannot be determined from the description and the anchor verse vertical pass extract reveals that the grouping itself may be wrong:

- **Grouping is sound but description is wrong:** proceed to Step 2 with the richer data now available from the vertical pass extract.
- **Grouping is wrong — verses need re-reading and re-grouping:** trigger a VCB re-run for this term under WA-VerseContext-Instruction-v2.5. Issue a return instruction (Section 4.8). The Dimension Review for this registry pauses.
- **Source data is defective:** issue a return instruction (Section 4.8) directing return to Session A / STEP extraction. The Dimension Review for this registry pauses.

**Step 4 — Patch encoding.**

All in-session rewrites are recorded in the observations log with full old and new text. The patch session reads these entries and encodes them as group description corrections. The correction updates:
- `verse_context_group.context_description`
- `wa_dimension_index.context_description` (synced by Claude Code)
- `verse_context_group.notes` (correction rationale)

The group proceeds to Phase C after the rewrite is confirmed.

**Step 5 — Root family check.**

After rewriting a term-centric description, consult the root family extract (Section 9.4). Check whether sibling terms in the same root family have groups describing the same or related characteristics. Note any observations in the observations log. This may be a Session D pointer candidate.

### 4.8 Return Instruction Format

A return instruction is issued when a quality problem identified in Phase B or Phase B.5 cannot be resolved within the Dimension Review session and requires upstream reprocessing.

**File:** `wa-dim-{cluster}-{registry_no}-return-v{n}-{date}.md`

**Content:**

```
# WA-DIM-RETURN — Cluster {C##} Registry {nnn} ({word})
Date: {date} | Instruction version: WA-DimensionReview-Instruction-v2.2-2026-04-11

## Reason for return
{State precisely what was found and why it cannot be resolved within the Dimension Review}

## Registry affected
Registry {nnn} — {word} | Cluster {C##}
Groups affected: {list of group_codes}
Terms affected: {list of strongs_number / transliteration}

## Return destination
{One of:}
- VCB re-run: Re-run Verse Context for the listed terms under WA-VerseContext-Instruction-v2.5.
  Specific instruction: {what the re-run must achieve}
- Session A / STEP extraction: Re-extract the listed terms from STEP.
  Specific instruction: {what is wrong with the source data and what the re-extraction must correct}

## Resume condition
The Dimension Review for Registry {nnn} resumes when:
{State the specific condition}

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

**Excluded registries do not enter Phase C.** Any registry with `session_b_status = "Analysis Complete"` is fully excluded. Claude AI must not process, assign dimensions to, or write Phase C entries for groups belonging to these registries. If a group from an excluded registry appears in the cluster extract, it is silently skipped.

For each `QA-CLEAR` group (and each group that has passed Phase B.5 correction) belonging to an **active registry**, Phase C asks two questions:

> 1. **What kind of inner-being characteristic does this group describe?** — assign a dimension from the vocabulary (Section 5.7), or name a new one.
> 2. **Who is the primary bearer of this characteristic in this group's verse evidence?** — assign a `dominant_subject` value (Section 1.7).

**Property-term dimension assignment:** Where a group derives from a property term, the dimension is assigned to the *inner-being characteristic the group serves* — not to the property term's function.

**Characteristic term dimension assignment:** Where a group derives from a characteristic term, the dimension is assigned to the characteristic directly.

Write every Phase C assignment to the observations log immediately on assignment. Do not accumulate.

### 5.2 The Three Assignment Rules

**Rule 1 — The verse leads.** Read the `context_description`. Name what you actually see. Then check whether an existing dimension captures it.

**Rule 2 — If it could fit more than one dimension, assign the dominant one.** One label per group. Record the reasoning in the observations log.

**Rule 3 — If it fits no existing dimension, do not force it.** Name what the group shows in plain language. Record in observations log. Present to researcher. Do not assign a dimension that does not genuinely describe it.

### 5.3 Working Through a Group — Step by Step

1. Read the `context_description` (confirmed characteristic-perspective from Phase B/B.5)
2. Identify: is this a characteristic term or a property term group? (Section 1.8)
3. **Read each anchor verse text against the description.** For every anchor verse in the group:
   - Read the full verse text as supplied in the cluster extract
   - Verify that the description captures all inner-being aspects the verse shows
   - Note any inner-being aspects present in the verse but absent from the description
   - Note any aspects claimed in the description that are not grounded in this anchor verse (may be drawn from other verses in the group — note this explicitly)
   - If the anchor verse reveals a problem that cannot be resolved from the verse text alone, request a vertical pass extract (Section 5.6)
   - Write AV verification findings to observations log immediately (format: Section 7.2)
4. Ask: what inner-being characteristic does this group primarily describe?
5. Ask: who is the primary bearer — GOD, HUMAN, OTHER_HUMAN, UNSEEN, or NONE?
6. Check dimension vocabulary (Section 5.7) — does an existing dimension fit clearly?
7. Check whether any observation warrants a Session B or D pointer (Section 5.4)
8. Write all findings to observations log before moving to the next group

### 5.4 Session B and D Pointer Capture

Analytical observations arising during Phase C that are relevant to Session B or cross-registry synthesis must be captured in the observations log immediately on discovery, with full content. The patch session reads these entries and encodes them as insert operations.

**Naming conventions:**

| Type | Convention | Example |
|---|---|---|
| Session B finding | `DIM-{registry_no}-{3-digit-sequence}` | `DIM-112-001` |
| Session D pointer | `DIM-{registry_no}-SD{3-digit-sequence}` | `DIM-112-SD001` |

**Root family pointers:** Cross-registry root families identified via the root family extract (Section 9.4) are strong candidates for Session D pointers. Capture in observations log with full description.

**Uniqueness:** Check pre-existing pointers extract (Section 9.3) before inserting. Numbering must continue from the highest existing sequence.

For insert formats, see Section 7.3.

### 5.5 Cross-Group Patterns Within a Cluster

When reviewing groups across a cluster, look for:

- **Convergence** — multiple groups from different registries naming the same characteristic
- **Divergence** — groups clustered together but engaging materially different inner-being aspects
- **Subject patterns** — a dimension appearing consistently in GOD vs HUMAN groups
- **Vocabulary gaps** — recurring characteristics that no existing dimension captures
- **Root family resonance** — groups from terms in the same root family showing related or contrasting dimension assignments

Record all pattern observations in the observations log as they are identified.

### 5.6 Anchor Verse Vertical Pass Extract

**Purpose:** Obtain full term-link context for an anchor verse when the in-session anchor verse reading (Section 5.3 Step 3) reveals a problem that cannot be resolved from the verse text alone.

The mandatory anchor verse reading in Step 3 is performed for every group using the verse text in the cluster extract. When that reading is sufficient to verify the description and confirm the dimension — which will be the case for most groups — no further action is required. A vertical pass extract is requested only when the anchor verse reading reveals a specific problem requiring fuller context.

**Request a vertical pass extract when the anchor verse reading shows:**

- The group description has been rewritten in Phase B.5 and the new description names a characteristic that should be corroborated by the verse's full term-link context
- The anchor verse is in a key theological passage and the full term-link context would confirm or challenge the dimension assignment
- The anchor verse was previously flagged as analytically complex
- A `QA-BROAD` flag was raised
- The anchor verse text alone is insufficient to determine whether the description's claims are grounded (e.g. the verse is truncated, or the inner-being content depends on the wider passage)

**Findings from the vertical pass check are recorded in the observations log immediately.** Corrections are encoded in the patch via the patch session.

**One extract per group.** Do not request separate extracts for each anchor verse.

**Do not over-request.** Request only when the conditions above are met. Most groups will not require a vertical pass extract — the in-session anchor verse reading is sufficient.

### 5.7 The Dimension Vocabulary

*Derived from data. Working vocabulary as of v1.9. Will be revised as additional data is reviewed.*

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

`dominant_subject` for this dimension: Assign `NONE` where the subject is genuinely dual. Assign `GOD` or `HUMAN` where one pole dominates but the correspondence is analytically significant.

**⚠ When no existing dimension fits:** Name what the group shows in plain language. Record in observations log. Present to researcher. Do not assign a dimension that does not genuinely describe it.

---

## 6. Session Discipline

### 6.1 Unit of Work

**The phase is the minimum unit of work.** A single session covers at most one phase for one registry (or the full cluster for Phase A). Claude AI must never attempt to complete multiple phases or multiple registries across all phases in a single session.

**Mandatory incremental discipline:**

Large clusters cannot be processed reliably in a single session. The C17 cluster (284 groups, 10 registries) is a confirmed example: attempting to hold all group analysis in working memory without intermediate disk writes risks truncation, analytical drift, and undetectable omissions. This discipline is not optional — it is a data integrity requirement.

The rules are:
- **Phase A** for the full cluster is one session.
- **Phase B** for the full cluster is one session (may be split by registry for very large clusters — see below).
- **Phase C** for a single registry is one session. Phase C is never combined with Phase A or Phase B in the same session.
- Within a single large registry (more than approximately 20 groups), Phase B and Phase C may each need to be split into sub-sessions by term family or group range. The split point must be recorded explicitly in the observations log.
- The observations log is written to disk and the researcher downloads it at the end of every session before the next session begins.

**Mode-dependent scope (unchanged from v2.0):**

**Cluster Mode:** The cluster is the analytical scope. Phase A covers the full cluster. Phase B covers the full cluster. Phase C covers registries one at a time.

**Registry Mode:** Phase C is scoped to the target registry only. Phase A and Phase B still span the full cluster for analytical coherence (Section 0.2).

### 6.2 The Observations Log — Primary Analytical Artefact

The observations log is the continuous write-to-disk record of all analytical decisions during the analytical session. It replaces the refinement log as the in-session artefact. The patch is generated in a separate session from the observations log.

**The write-on-discovery principle is absolute:** every item below is written to the observations log at the moment it is determined — not accumulated in memory and transcribed at the end:

- Phase A findings and cluster coherence assessment
- Every Phase B QA flag and its resolution
- Every Phase B.5 description rewrite (old text, new text, rationale)
- Every Phase C dimension assignment (group code, dimension, dominant subject, notes)
- Every Session B finding (with full content as it will appear in the database)
- Every Session D pointer (with full content as it will appear in the database)
- Every field update decision (e.g. dominant_subject, dimension corrections)
- Coverage verification result
- Any anchor verse verification findings
- Any instruction amendment notes
- Any return instruction triggers
- Registry-level and cluster-level stamp decisions

**File writing discipline — no filename reuse:**
- Write to disk after every individual observation or group of closely related observations — do not wait until a phase or registry is complete.
- Dual-write: working directory (`/home/claude/`) and `/mnt/user-data/outputs/`.
- **The observations log filename is never reused.** Every write increments the version by 0.1: `v1.0`, `v1.1`, `v1.2`, … The previous version remains on disk. The current version is always the highest-numbered file. This applies within a session as well as across sessions.
- When resuming across sessions: confirm the highest existing version number from the uploaded file, then continue from the next increment (e.g. if the uploaded file is `v1.3`, the next write produces `v1.4`).
- **At the end of every session, present the current observations log file for researcher download before stopping.** The researcher must download the log before the next session begins. This is non-negotiable — the observations log is the sole persistent record carried across session boundaries. Analytical work not written to a downloaded log is at risk of being lost.
- **At the start of every session (except the very first), the researcher uploads the existing observations log.** Claude AI reads it in full before beginning any new analytical work. Claude AI does not re-derive or re-run any analysis already recorded in the log — it only appends to a new version file.

**The observations log is the source for per-registry patch production.** After each registry's Phase C is confirmed complete, the patch is constructed from the observations log entries for that registry. No analytical decision should need to be re-derived during patch construction.

### 6.3 Session Logs

Produce a session log at the end of every session (i.e. after every phase or sub-phase). Session logs must record:
- Which cluster(s), registries, and phase(s) were covered in this session
- Phase A findings summary (if Phase A was run)
- Phase B quality flag summary and resolutions (if Phase B was run)
- Coverage verification result (if applicable)
- Phase C dimension proposals and researcher responses summary (if Phase C was run)
- Session B/D pointers captured
- Current observations log filename and version
- Dimension Review version stamp status (registry-level and cluster-level)
- Whether patch session has been run
- **Explicit stop point:** the last group code or phase step completed in this session
- **Resume instruction:** exactly what the next session must begin with — which registry, which phase, which group code, and which observations log version to load

Session logs are summaries — the observations log is the complete record.

### 6.4 Startup Protocol — Analytical Session

Before beginning any phase of the analytical session, confirm in sequence:

0. **Mode declaration:** State which mode this session operates in: Cluster Mode or Registry Mode (Section 0.2). If Registry Mode, state the target registry number and word. This determines Phase C scope and stamp rules for the entire session.
1. **Instruction read:** State that this instruction has been read in full.
2. **Cluster extract confirmed loaded:** State the extract filename and row count.
3. **Root family extract confirmed loaded:** State the extract filename and root count.
4. **Existing pointers extract confirmed loaded:** State the extract filename and pointer count.
5. **Observations log initialised or loaded:**
   - If this is the first session for this cluster: create the observations log file on disk with header, filename, date, governing instruction version, mode declaration, and input file references.
   - If this is a continuation session: the researcher has uploaded the existing observations log. State the filename and version. Read it in full. Confirm the stop point recorded in the previous session log. Do not re-run or re-record any analysis already present in the log.
6. **Registry status check — two filters applied at startup:**

   **Filter 1 — Analysis Complete exclusion:** Scan every registry in `cluster_registries` for `session_b_status = "Analysis Complete"`. Any registry carrying this status has completed the full word analysis programme and **must be excluded from all Phase B and Phase C processing in this session**. These registries are skipped entirely — their groups are not flagged, not reviewed, and not patched. Record each excluded registry in the observations log under a `[EXCLUDED]` entry. The exclusion also applies to coverage verification: excluded registry groups are subtracted from the total group count before the coverage check is run (Section 4.6).

   **Filter 2 — VCB completeness check:** For the remaining (non-excluded) registries, confirm that `verse_context_status = Complete`. In Registry Mode, this check is still performed for the full cluster — Phase B requires cluster context regardless of mode. If non-excluded registries lack VCB completion, note this; it does not block Phase B or Phase C for the target registry but must be flagged.

   **Important:** Analysis Complete exclusion takes absolute precedence over VCB status. A registry with `session_b_status = "Analysis Complete"` is excluded regardless of its `verse_context_status`.
7. **Schema check noted:** Note that Claude Code must verify schema additions (Section 10.3) before applying stamps.
8. **Phase and scope declaration:** State exactly which phase and which registry (or cluster scope) this session will cover. State the expected stopping point. Confirm that no work beyond this scope will be attempted in this session.

### 6.5 Per-Registry Patch Protocol

The patch is produced inline, immediately after each registry's Phase C is confirmed complete. There is no separate patch session. Patch construction is mechanical — no analytical work is performed.

**Trigger:** Phase C for a registry is complete (all groups assigned, STAMP entry written to observations log, observations log version incremented and written to disk).

**Steps:**

1. **Increment observations log version.** Before constructing the patch, write the current registry's STAMP entry and SESSION-END marker to the observations log. Produce a new observations log version file (increment by 0.1). This ensures the patch reads from a stable, complete snapshot.

2. **Patch ID assigned.** Format: `PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-REG{nnn}-V{n}` where `{nnn}` is the registry number (zero-padded to 3 digits). Example: `PATCH-20260411-DIMREVIEW-C17-REG023-V1`.

3. **Scope of patch.** The patch covers only the completed registry:
   - All `wa_dimension_index` dimension updates for groups belonging to this registry
   - Any Phase B.5 `verse_context_group` and `wa_dimension_index` context_description corrections for this registry
   - Any `wa_session_b_findings` inserts arising from this registry's Phase C
   - Any `wa_session_research_flags` inserts arising from this registry's Phase C
   - The registry stamp (`word_registry` update: `dim_review_status = Complete`, `dim_review_version`)
   - **If this is the final registry in the cluster:** also include the cluster stamp (`wa_dim_review_cluster_log` insert)

4. **Three-check verification before writing:**
   - All group codes in the patch are present in the cluster extract for this registry
   - No group for this registry is missing from the patch
   - No duplicate group codes in patch operations

5. **Deliver patch.** Present patch file to researcher for review. Claude Code applies. Confirm application before proceeding to the next registry.

6. **Continue.** Once the patch is applied and confirmed, proceed to the next registry.

---

### 6.6 Session Boundary Protocol

This section governs how sessions start, stop, and hand off to each other. It exists because the Dimension Review for large clusters cannot be completed in a single session and the observations log must function as a reliable persistent record across multiple sessions.

**At the end of every session, Claude AI must:**

1. Finish writing all analytical work from the current session to the observations log on disk.
2. Write a session boundary marker to the observations log:
```
[SESSION-END] {date} | Phase: {phase} | Registry: {reg_no} ({word}) | Last group completed: {group_code or "N/A"}
Next session begins: Phase {X} | Registry {reg_no} ({word}) | Starting from: {group_code or "beginning of phase"}
Observations log version: {filename}
```
3. Present the observations log file for researcher download via the `present_files` tool.
4. Stop. Do not begin the next phase or next registry.

**At the start of every continuation session, Claude AI must:**

1. Confirm the researcher has uploaded the observations log from the previous session.
2. Read the observations log in full from the beginning.
3. Locate the `[SESSION-END]` marker at the end of the log.
4. State the resume point out loud before beginning any work: *"Resuming from: [phase, registry, group code]. The previous session ended at [last group code]. I will begin with [first group code or step in this session]."*
5. Append new work to the existing log — never overwrite or replace it.

**Hard limits — Claude AI must never:**

- Attempt to complete an entire cluster (all phases, all registries) in a single session.
- Attempt to complete more than one phase for a single registry in a single session.
- Reconstruct analytical decisions from memory rather than reading from the uploaded observations log.
- Skip the patch production step after a registry's Phase C is complete — the patch must be produced, delivered, and confirmed applied before the next registry begins.
- Skip the download step at the end of a session, even if the session was short.

**Recommended session sizes:**

| Work | Expected session |
|---|---|
| Phase A — full cluster | 1 session |
| Phase B — up to ~30 groups | 1 session |
| Phase B — 30+ groups | Split by registry; 1 session per 2–3 registries |
| Phase C — up to ~15 groups | 1 session, followed immediately by per-registry patch |
| Phase C — 15+ groups | Split by term family; 1 session per ~15 groups; patch after each registry completes |
| Patch construction | Inline after each registry's Phase C — not a separate session |

These are guidelines, not hard limits. The researcher and Claude AI may agree to different splits. What is non-negotiable is that the observations log is written and downloaded before any session ends.

---

## 7. Output Formats

### 7.1 Cluster Review Assessment (Phase A — written to observations log)

```
## Phase A — Cluster Review: {C##} | {summary of cluster words}
Date: {date}

### Excluded registries (Analysis Complete — no further processing)
{list with registry numbers, words, and group counts — or "None" if none excluded}

### Active registries
{list with registry numbers and group counts — excluded registries not included in active count}

### Coherence assessment
{What inner-being affinity holds this cluster together — assessed from active registries}

### Boundary observations
{Any misplaced words or ambiguous scope}

### Cross-registry root families
{Summary of cross-registry root families identified — counts and key observations}

### Recommendation
[ ] Confirm as-is
[ ] Propose reassignment: {word} (Reg {no}) → {target cluster} | Reason: {brief reason}
```

### 7.2 Observations Log — Format and Structure

The observations log is a sequential record. Entries are written in the order they are made. There is no pre-defined section structure — entries follow the analytical sequence.

**File header:**
```
# WA Dimension Review Observations Log — {C##}
Filename: wa-dim-{cluster}-observations-v{n}-{date}.md
Governing instruction: WA-DimensionReview-Instruction-v2.2-2026-04-11
Cluster extract: wa-dim-{cluster}-extract-{date}.json ({n} groups)
Root family extract: wa-dim-{cluster}-rootfamily-{date}.json ({n} roots)
Existing pointers extract: wa-dim-{cluster}-existing-pointers-{date}.json ({n} pointers)
Session date: {date}
```

**Excluded registry entry format (one entry per excluded registry — written during startup):**
```
[EXCLUDED] Reg {n} ({word}) | session_b_status = Analysis Complete
All {n} groups in this registry are excluded from Phase B, Phase C, and patch operations.
Analysis is complete for this word. No further Dimension Review processing applies.
```

**Phase A entry format:**
```
[PHASE-A] {cluster} | {date}
{Cluster coherence assessment — see Section 7.1 template}
RECOMMENDATION: CONFIRM / PROPOSE REASSIGNMENT: {details}
```

**Phase B entry format (one entry per group):**
```
[PHASE-B] {group_code} | {strongs} {transliteration} | Reg {n} ({word})
QA-FLAG: {flag}
{If QA-CLEAR: brief note why}
{If any other flag: what is inadequate and proposed correction}
```

**Phase B.5 entry format (one entry per rewrite):**
```
[PHASE-B5] {group_code} | REWRITE
OLD: {existing context_description}
NEW: {revised characteristic-perspective description}
RATIONALE: {why the old description was term-centric and what characteristic the new description names}
PATCH-TARGET: verse_context_group.id = {id} | wa_dimension_index.id = {id}
```

**Phase C entry format (one entry per group):**
```
[PHASE-C] {group_code} | {strongs} {transliteration} | Reg {n} ({word})
DIMENSION: {dimension name}
DOMINANT-SUBJECT: {GOD|HUMAN|OTHER_HUMAN|UNSEEN|NONE}
NOTES: {reasoning — especially if automated label is being changed, or if near-miss with another dimension}
PATCH-TARGET: wa_dimension_index.id = {id}
```

**AV verification entry format (one entry per group, written as part of Phase C Step 3):**
```
[AV-VERIFY] {group_code} | {strongs} {transliteration}
AV: {verse_ref} — {verse_text}
DESC covers: {what aspects of the verse the description captures}
VERSE also shows: {inner-being aspects present in the verse but not in the description — or "nothing additional"}
VERDICT: FULL ALIGNMENT / DESC PARTIALLY EXCEEDS AV / DESCRIPTION GAP / ANCHOR VERSE MISMATCH
{If any issue: state what the gap or mismatch is and what action is required}
FLAG: {NONE / MINOR / MODERATE / SIGNIFICANT} — {brief statement of issue if not NONE}
ACTION: {correction required, or "None"}
```

Verdict definitions:
- **FULL ALIGNMENT** — description captures all inner-being aspects the verse shows; no action needed
- **DESC PARTIALLY EXCEEDS AV** — description includes claims drawn from other verses in the group, not this anchor verse alone; note explicitly but no correction needed if claims are valid for the wider group
- **DESCRIPTION GAP** — the verse shows inner-being content not captured in the description; assess whether the description needs correction
- **ANCHOR VERSE MISMATCH** — the anchor verse does not ground the description at all; the wrong verse has been designated as anchor; correction required

**Session B finding entry format:**
```
[SESSION-B] {flag_label e.g. DIM-187-001}
REGISTRY: {n} ({word})
DESCRIPTION: {full text as it will appear in wa_session_b_findings.description}
PATCH-TARGET: wa_session_b_findings insert
```

**Session D pointer entry format:**
```
[SESSION-D] {flag_label e.g. DIM-187-SD002}
REGISTRY: {n} ({word})
SESSION-TARGET: D
DESCRIPTION: {full text as it will appear in wa_session_research_flags.description}
PATCH-TARGET: wa_session_research_flags insert
```

**Coverage verification entry:**
```
[COVERAGE-VERIFY] {cluster}
Groups in extract: {n}
Groups with Phase B entry in observations log: {n}
Result: CONFIRMED / GAP FOUND — {list missing group codes if gap found}
```

**Stamp decision entry:**
```
[STAMP] Registry {n} ({word})
dim_review_status: Complete
dim_review_version: WA-DimensionReview-Instruction-v2.2-2026-04-11
PATCH-TARGET: word_registry.no = {n}
```

**Instruction amendment note entry:**
```
[INSTRUCTION-NOTE] {date}
OBSERVATION: {what was observed that suggests an instruction amendment}
PROPOSED CHANGE: {what should change in the instruction}
ACTION: Flag for instruction update after session
```

### 7.3 Dimension Patch

JSON patch for Claude Code. Produced inline after each registry's Phase C is confirmed complete. Patch type: `DIMREVIEW`. The `patch_id` must contain the string `DIMREVIEW`.

**Patch ID format:** `PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-REG{nnn}-V{n}`
- `{cluster}` — cluster code, uppercase (e.g. `C17`)
- `{nnn}` — registry number, zero-padded to 3 digits (e.g. `023`)
- `{n}` — patch version starting at 1; increment if the patch is revised and reissued

**Patch meta:**
```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-REG{nnn}-V{n}",
    "cluster": "{C##}",
    "registry_no": {nnn},
    "registry_word": "{word}",
    "produced_date": "{ISO date}",
    "produced_by": "WA-DimensionReview-Instruction-v2.2-2026-04-11",
    "observations_log": "wa-dim-{cluster}-observations-v{n}-{date}.md",
    "session_b_status": null,
    "description": "Dimension review patch — {cluster} Reg {nnn} ({word}): {brief summary}"
  }
}
```

**`session_b_status: null` — formal note:** The Dimension Review does not advance the `session_b_status` workflow. The correct value is always `null`. The applicator must NOT reject DIMREVIEW patches for having `null` in this field — this is a registered exception in patch_specification-v1.7 Section 8.6 and Appendix A.6.

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

**Group description correction operation (characteristic-perspective rewrite):**
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

**Registry version stamp operation:**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "update",
  "table": "word_registry",
  "match": { "no": {registry_no} },
  "set": {
    "dim_review_status": "Complete",
    "dim_review_version": "WA-DimensionReview-Instruction-v2.2-2026-04-11"
  },
  "description": "Registry {nnn} ({word}): Dimension Review complete under v2.2"
}
```

**Cluster stamp operation:**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "insert",
  "table": "wa_dim_review_cluster_log",
  "record": {
    "cluster": "{C##}",
    "completed_date": "{ISO date}",
    "instruction_version": "WA-DimensionReview-Instruction-v2.2-2026-04-11",
    "registry_count": {n},
    "group_count": {n},
    "anchored_count": {n},
    "notes": "{any cluster-level observations}"
  },
  "description": "Cluster {C##} Dimension Review complete — stamp set"
}
```

**Session B finding insert and Session D pointer insert:** see Section 5.4 for naming conventions. Full content read from observations log. Table targets: `wa_session_b_findings` and `wa_session_research_flags` respectively.

### 7.4 Group Description Correction Patch (out-of-session use only)

Patch type: `DIMREVIEW-GRPDESC`. Used only for corrections made outside a live cluster session. Unchanged from v1.7.

---

## 8. Claude Code Protocol and Boundaries

### 8.1 Claude Code Responsibilities

| Task | Claude Code action |
|---|---|
| Construct cluster extract | Query per Section 9.1 |
| Construct root family extract | Query per Section 9.4 |
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
| `DIMREVIEW` | WA-DimensionReview-Instruction-v2.2 | `null` | `wa_dimension_index` updates; `verse_context_group` corrections; `wa_session_b_findings` inserts; `wa_session_research_flags` inserts; `word_registry` stamp update (one registry per patch); `wa_dim_review_cluster_log` insert (final registry patch only) |
| `DIMREVIEW-GRPDESC` | WA-DimensionReview-Instruction-v2.2 | `null` | Out-of-session group description corrections only |

---

## 9. Data Extracts — Required Inputs for Claude AI

### 9.1 Cluster Extract — Primary Session Input

**Extract name:** `wa-dim-{cluster}-extract-{date}.json`

All `wa_dimension_index` rows for the requested cluster, joined to `word_registry`, `verse_context_group`, `mti_terms`. All anchor and related verse arrays mandatory. See v1.7 Section 9.1 for full field mapping and JSON structure.

**`produced_by`:** `"Claude Code — WA-DimensionReview-Instruction-v2.2-2026-04-11"`

### 9.2 Group Description Verification Extract

**Extract name:** `wa-dim-{cluster}-grpverify-{group_code}-{date}.json`

Constructed on demand when Phase B requires verse-level review before a description correction can be written.

### 9.3 Pre-existing Session B/D Pointer Extract

**Extract name:** `wa-dim-{cluster}-existing-pointers-{date}.json`

Includes all existing entries for cluster registries — both Dimension Review and Verse Context batch flags.

### 9.4 Root Family Cluster Extract — Standard Session Input

**Extract name:** `wa-dim-{cluster}-rootfamily-{date}.json`

Required session input. Claude Code constructs at the same time as the cluster extract. Full JSON structure, query specification, and `cross_registry` / `in_current_cluster` flag definitions unchanged from v1.7 Section 9.4.

### 9.5 Anchor Verse Vertical Pass Extract — On-Demand Sub-Process Input

**Extract name:** `wa-dim-{cluster}-vpass-{group_code}-{date}.json`

| Component | Rule |
|---|---|
| `wa-dim` | Fixed prefix |
| `{cluster}` | Cluster being reviewed — e.g. `c02` |
| `vpass` | Fixed segment identifying extract type |
| `{group_code}` | Group code — e.g. `758-001` |
| `{date}` | Date of extract construction |

**⚠ Naming discipline is mandatory.** One extract per group. Do not use verse references, registry names, or other identifiers — the group_code is the only permissible identifier after `vpass`.

**CC directive file:** `wa-dim-{cluster}-cc-directive-vpass-{group_code}-{date}.md`

Trigger conditions, content structure, and CC directive format unchanged from v1.7 Section 9.5.

---

## 10. Dimension Review Version Stamps

### 10.1 Purpose

The version stamp system records, at both registry and cluster level, which version of the Dimension Review instruction was used to review and confirm the data. Session B gates on the cluster-level stamp.

### 10.2 Registry-Level Stamp

When all groups for a registry have passed Phase B (including Phase B.5 where triggered) and Phase C dimension assignments are confirmed:

| Field | Table | Value |
|---|---|---|
| `dim_review_status` | `word_registry` | `Complete` |
| `dim_review_version` | `word_registry` | `WA-DimensionReview-Instruction-v2.2-2026-04-11` |

The registry stamp is included in the per-registry patch for that registry (Section 6.5 step 3) and applied by Claude Code when the patch is applied.

**In Registry Mode:** The registry-level stamp is set for the target registry only. It satisfies the Stage 2 gate for that registry (Session B Stage 2 may begin). It does NOT set the cluster-level stamp and does NOT open the DataPrep gate for other registries in the cluster.

### 10.3 Cluster-Level Stamp

When all registries in a cluster have `dim_review_status = Complete`, Claude Code inserts a record into `wa_dim_review_cluster_log`. This is the DataPrep gate.

**In Registry Mode:** The cluster-level stamp is NOT set. The full cluster Dimension Review session must be run to set it. Session B DataPrep for other registries in the cluster cannot open based on a Registry Mode completion alone.

**Schema additions** — apply once, before the first cluster stamp (DDL unchanged from v1.7 Section 10.3).

### 10.4 Session B Gate System

Two independent gates govern when Session B processing may advance. These gates are not in conflict — they operate at different scopes.

| Gate | Condition | What it opens |
|---|---|---|
| **Stage 2 gate** | Registry has `dim_review_status = Complete` AND all dimension_index groups at `CLAUDE_AI` confidence AND all `dominant_subject` assigned | Session B Stage 2 (analytical passes) may begin for this registry. May be satisfied by Registry Mode completion. |
| **DataPrep gate** | `wa_dim_review_cluster_log` contains a record for the cluster AND all registries in the cluster have `dim_review_status = Complete` AND all registries have `verse_context_status = Complete` | Session B DataPrep for any registry in the cluster. Requires full Cluster Mode completion — Registry Mode alone does not satisfy this gate. |

Gate check query unchanged from v1.7 Section 10.4 for the DataPrep gate. Stage 2 gate check:
```sql
SELECT no, word, dim_review_status, verse_context_status
FROM word_registry
WHERE no = {registry_no}
  AND dim_review_status = 'Complete'
  AND verse_context_status = 'Complete';
```

### 10.5 Monitoring Query

Unchanged from v1.7 Section 10.5.

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

- Dimension assignments for any group (written to observations log)
- `dominant_subject` assignments (written to observations log)
- Corrections to existing labels that do not match group content (written to observations log)
- Quality flags including `QA-TERMCENTRIC`
- Characteristic-perspective rewrites under Phase B.5 (proposed — confirmed before patch)
- Anchor verse vertical pass extract requests (produces CC directive independently)
- Candidate new dimension names where no existing dimension fits (written to observations log)
- Session B/D pointer content (written to observations log with full text)
- Return instructions (issued independently when the conditions in Section 4.8 are met; researcher is informed)
- Instruction amendment notes (written to observations log under `[INSTRUCTION-NOTE]` tag)

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
| DR-15 | The anchor verse vertical pass extract must follow the naming convention `wa-dim-{cluster}-vpass-{group_code}-{date}.json` — no other naming is permitted |
| DR-16 | Session B may not open for a cluster until `wa_dim_review_cluster_log` contains a record for that cluster and all registries show `dim_review_status = Complete` |
| DR-17 | Schema additions (Section 10.3) must be applied before the first stamp operation — Claude Code verifies before applying any stamp |
| DR-18 | A registry that has received a return instruction retains `dim_review_status = NULL` until the upstream process completes and the Dimension Review resumes and confirms the registry |
| DR-19 | Every analytical decision must be written to the observations log on discovery — no accumulation in memory for later transcription |
| DR-20 | Per-registry patch construction reads from the observations log only — no re-derivation of analytical decisions is permitted during patch construction; patch scope is limited to the completed registry and must not include entries from registries not yet confirmed complete |

---

## 13. Naming Conventions

**File naming pattern:** `[Prefix]-[reference]-[short description]-[Version]-[date]`

The reference (cluster, registry, batch, group code, etc.) immediately follows the prefix. This allows all files from the same programme reference to sort together.

| File type | Pattern | Example |
|---|---|---|
| Cluster extract | `wa-dim-{cluster}-extract-{date}.json` | `wa-dim-c01-extract-2026-04-09.json` |
| Root family cluster extract | `wa-dim-{cluster}-rootfamily-{date}.json` | `wa-dim-c01-rootfamily-2026-04-09.json` |
| Existing pointers extract | `wa-dim-{cluster}-existing-pointers-{date}.json` | `wa-dim-c01-existing-pointers-2026-04-09.json` |
| Group verification extract | `wa-dim-{cluster}-grpverify-{group_code}-{date}.json` | `wa-dim-c02-grpverify-3012-001-2026-04-09.json` |
| Anchor verse vertical pass extract | `wa-dim-{cluster}-vpass-{group_code}-{date}.json` | `wa-dim-c02-vpass-758-001-2026-04-09.json` |
| CC directive — group verification | `wa-dim-{cluster}-cc-directive-grpverify-{group_code}-{date}.md` | `wa-dim-c02-cc-directive-grpverify-3012-001-2026-04-09.md` |
| CC directive — vertical pass | `wa-dim-{cluster}-cc-directive-vpass-{group_code}-{date}.md` | `wa-dim-c02-cc-directive-vpass-758-001-2026-04-09.md` |
| Observations log | `wa-dim-{cluster}-observations-v{n}-{date}.md` | `wa-dim-c10-observations-v1.0-2026-04-09.md` — version increments by 0.1 on every write; filename never reused |
| Per-registry dimension patch | `wa-dim-{cluster}-reg{nnn}-patch-v{n}-{date}.json` | `wa-dim-c01-reg023-patch-v1-2026-04-09.json` |
| Group description correction patch (out-of-session) | `wa-dim-{cluster}-grpdesc-patch-v{n}-{date}.json` | `wa-dim-vcb029-grpdesc-patch-v2-2026-04-09.json` |
| Return instruction | `wa-dim-{cluster}-{registry_no}-return-v{n}-{date}.md` | `wa-dim-c02-213-return-v1-2026-04-09.md` |
| Session log | `wa-dim-{cluster}-session-log-v{n}-{date}.md` | `wa-dim-c01-session-log-v1-2026-04-09.md` |

**Note on patch_id patterns:**
- Per-registry dimension patch: `PATCH-{YYYYMMDD}-DIMREVIEW-{cluster}-REG{nnn}-V{n}` — e.g. `PATCH-20260411-DIMREVIEW-C01-REG023-V1`
- Out-of-session group description correction: `PATCH-{YYYYMMDD}-DIMREVIEW-GRPDESC-{scope}-V{n}`

All filenames lowercase. Cluster codes lowercase in filenames (c01, c02) even where referred to as C01, C02 in prose.

---

*WA-DimensionReview-Instruction-v1.9-2026-04-09 | Supersedes v1.8-2026-04-09 | v1.9: Mandatory anchor verse reading added to Phase C step-by-step (Section 5.3 Step 3) — re-reading each anchor verse against the group description is now required for every group; Section 5.6 reframed from on-demand sub-process to vertical pass extract trigger conditions; AV verification observations log entry format added (Section 7.2); all version strings updated to v1.9*

*WA-DimensionReview-Instruction-v2.0-2026-04-10 | Supersedes v1.9-2026-04-09 | v2.0: Registry Mode formalised (Section 0.2) — two modes defined: Cluster Mode (normal path) and Registry Mode (Session B Stage 1 sub-process); Section 6.1 updated — unit of work is mode-dependent; Section 6.4 startup protocol updated — mode declaration added as Step 0, VCB completeness nuance added for Registry Mode; Section 7.3 patch template — session_b_status: null exception formally noted, Registry Mode patch_id pattern documented; Section 8.5 updated; Sections 10.2–10.4 updated — two-gate system documented; all version strings updated to v2.0*

*WA-DimensionReview-Instruction-v2.1-2026-04-10 | Supersedes v2.0-2026-04-10 | v2.1: (1) Incremental session discipline mandated — phase is minimum unit of work, observations log downloaded at end of every session, new Section 6.6 Session Boundary Protocol; (2) Analysis Complete exclusion rule — registries with session_b_status = "Analysis Complete" excluded from Phase B, Phase C, coverage verification, and patch operations; [EXCLUDED] log entry format added; exclusion identified at startup Step 6; all version strings updated to v2.1*

*WA-DimensionReview-Instruction-v2.2-2026-04-11 | Supersedes v2.1-2026-04-10 | v2.2: (1) Per-registry patch production — patch produced inline after each registry Phase C, no separate patch session; Section 6.5 replaced; Section 6.6 hard limit removed; patch ID format REG{nnn}; cluster stamp in final registry patch; DR-20 updated; Section 8.5 updated; Section 13 updated; (2) Observations log no-overwrite versioning — filename increments by 0.1 on every write, previous versions retained on disk; all version strings updated to v2.2*
