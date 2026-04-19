# WA Dimension Review Instruction

**Framework B — Soul Word Analysis Programme**
**Version 3_3 | 20260418 | Status: Active governing instruction**

| | |
|-|-|
| **Filename** | wa-dimensionreview-instruction-v3_3-20260418.md |
| **Supersedes** | wa-dimensionreview-instruction-v3_2-20260417.md |
| **Governing rules** | wa-global-general-rules [current] — must be loaded and confirmed before beginning any session per GR-LOAD-001. Rules are referenced by ID throughout; the global file is authoritative in any conflict. |
| **Companion documents** | wa-versecontext-instruction [current] · wa-sessionb-analysis-readiness [current] · wa-sessionb-analysis-output [current] · wa-reference [current] · wa-registry-management-guide [current] · wa-patch-instruction [current] · wa-sessiond-orientation [current] |
| **Inputs** | Cluster extract: `wa-dim-{cluster}-extract-{YYYYMMDD}.json` (Claude Code → Claude AI) · Root family extract: `wa-dim-{cluster}-rootfamily-{YYYYMMDD}.json` (Claude Code → Claude AI) · Existing pointers extract: `wa-dim-{cluster}-existing-pointers-{YYYYMMDD}.json` (Claude Code → Claude AI) · Anchor verse vertical pass extract: `wa-dim-{cluster}-vpass-{group_code}-{YYYYMMDD}.json` (Claude Code → Claude AI, on demand) · Group description verification extract: `wa-dim-{cluster}-grpverify-{group_code}-{YYYYMMDD}.json` (Claude Code → Claude AI, on demand) · Observations log from previous session (researcher upload, on continuation) |
| **Outputs** | **Claude AI:** Observations log: `wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md` · Per-registry dimension patch: `wa-dim-{cluster}-reg{nnn}-patch-v{n}-{YYYYMMDD}.json` · Group description correction patch: `wa-dim-{cluster}-grpdesc-patch-v{n}-{YYYYMMDD}.json` (when triggered out-of-session) · Return instruction: `wa-dim-{cluster}-{registry_no}-return-v{n}-{YYYYMMDD}.md` (when upstream re-run required) · Session log: `wa-dim-{cluster}-session-log-v{n}-{YYYYMMDD}.md` · CC directives: `wa-dim-{cluster}-cc-directive-{type}-{YYYYMMDD}.md` · **Claude Code:** Patch application confirmation · Integrity check report · Dimension report regeneration |

## Change note

**v3_3 (2026-04-18):** GR-REF-002 sweep. (1) Header row version updated to `v3_3` with underscored convention per GR-FILE-003. (2) Governing rules reference migrated from `wa-global-general-rules-v1-2026-04-13.json` (very stale — 5 major versions behind current v2_11) to `[current]`. (3) Companion documents row replaced with current corpus: wa-versecontext-instruction, wa-sessionb-analysis-readiness, wa-sessionb-analysis-output, wa-reference, wa-registry-management-guide, wa-patch-instruction, wa-sessiond-orientation — all as `[current]`. Retired references (WA-SessionB-Instruction-v4.8, patch_specification-v1.10) removed; replaced by their successors in the consolidated corpus. (4) Body references to WA-VerseContext-Instruction-v3.1 in §5.3, §6.6, §6.7 return instruction template, §11 CC directive metadata example, patch_index table — migrated to `[current]`. (5) §11/§16 patch index rows referencing `WA-DimensionReview-Instruction-v3.1` updated to `[current]`. (6) Footer superseded-by line refreshed. Historical v3.2, v3.1, v3.0 change notes retained below for provenance.

**v3.2 (2026-04-17):** Single correction applied to resolve FLAG-002 in the global flags register (originally raised 2026-04-14, D-01A confirmed). The instruction was stating a per-save version-increment discipline for the observations log (increment by 0.1 on every write), which contradicts GR-OBS-004 (version-increment at named batch boundaries, not per save). Three locations amended: Section 8.2 (File writing discipline bullet list), Section 8.6 (Per-registry patch protocol — trigger description and step 1), and Section 15 (Naming Conventions — Observations log versioning line). Edits align the instruction with GR-OBS-004 by reference rather than by repeating rule content inline, per the document-purpose principle stated in the global rules file (instructions reference global rules by ID; they do not duplicate them). No other content reviewed or changed in this version — a full audit of this instruction against v2_8 of the global rules is tracked under FLAG-010 and will be done in a separate cycle.

**v3.1 (2026-04-14):** Six corrections following global rules coverage check against wa-global-general-rules-v1-2026-04-13.json. (1) Header: governing rules filename corrected from `wa-global-general-rules-v2-20260414.json` to `wa-global-general-rules-v1-2026-04-13.json`; supersedes updated from merged source reference to `v3_0-20260414`. (2) Section 8.3: session log requirements extended to include GR-OBS-003 — unresolved session actions must be confirmed resolved or explicitly summarised. (3) Section 10.3: note added that existing pointer content is historical per GR-DATA-007 — read for numbering continuity only. (4) Section 10 (new note after Section 10.1): GR-DATA-001 status filter requirement applied to all CC directives and extract queries. (5) Section 5.3: GR-PROG-003 citation added — cluster reassignment proposals raised only when placement materially disrupts analytical work. (6) Section 12.1: GR-DIR-001 citation added — CC directives are plain-language, specifying motivation, operations, and expected outcomes.

**v3.0 (2026-04-14):** Complete structural rewrite for clarity and consistency. All analytical content retained from the merged source document (combining v2.2-20260411, v1.10-20260414, and intervening revisions). Structural problems corrected: duplicate statements consolidated, logical sequence restored, Claude AI and Claude Code responsibilities separated cleanly, stale cross-references removed. Operation modes promoted to Section 1. Phases reorganised into numbered sections matching pipeline sequence. Session discipline, output formats, CC protocol, data extracts, stamps, and decision rules each occupy a dedicated section. Naming conventions consolidated into a single reference section.

---

## 1. Purpose, Scope, and Pipeline Position

The Dimension Review is the analytical stage between Verse Context completion and Session B. It validates cluster assignments, assesses and corrects contextual meaning group quality, assigns dimensions and dominant subjects to every active group, locks confirmed assignments, and captures emergent Session B and Session D observations. When it is done well, Session B will arise naturally from the data.

**What the Dimension Review does:**
- Validates that cluster assignments are analytically coherent
- Assesses every group's `context_description` for quality — and where necessary corrects it, including full characteristic-perspective realignment of groups produced under the pre-v2.5 term-centric model
- Verifies that anchor verse data is complete and supports the group description
- Reads groups within each cluster to discern what dimensions actually emerge from the data
- Assigns the `dominant_subject` field for every active group
- Progressively refines dimension assignments from automated hypothesis toward researcher-confirmed anchors
- Locks confirmed dimensions using the `manual_override` flag
- Captures emerging Session B and Session D observations as structured pointers in the database
- Stamps each registry and cluster with the governing instruction version on completion
- Prepares the ground for Session B

**What the Dimension Review does not do:**
- Impose pre-formed dimension categories on the data — dimensions must emerge from the groups (per GR-PROG-002)
- Use theological context, circumstance, or relational setting as a dimension criterion
- Perform the deep word analysis that is Session B's function
- Draw cross-cluster synthesis conclusions — that is Session D
- Delete or restructure verse-level data without a patch — all corrections go through the patch process (per GR-PROC-003)
- Rush toward Session B — the quality of this stage directly determines the quality of Session B output

**Pipeline:**

```
Verse Context complete (verse_context_status = Complete for all registries in cluster)
     │
     ▼
Claude Code: construct cluster extract + root family extract + existing pointers extract
     │
     ▼
Dimension Review — Analytical Session (this document) — per cluster
  ├── Phase A: Cluster assignment review
  ├── Phase B: Group quality review
  │     ├── Phase B.5: Characteristic-perspective correction sub-process (when QA-TERMCENTRIC raised)
  │     └── Coverage verification — mandatory before Phase C begins
  └── Phase C: Dimension discernment and dominant subject assignment
        ├── Claude AI: read group → assign dimension + dominant_subject
        ├── Researcher: confirm, refine, or reject
        └── Per-registry patch produced inline after Phase C complete for each registry
     │
     ▼
Researcher reviews patch → Claude Code applies → Claude AI continues to next registry
     │
     ▼
Final registry patch includes cluster stamp → Session B gate opens for cluster
```

**Roles:**

| System | Responsibility |
|-|-|
| **Claude AI** | Cluster assignment review · group quality assessment · characteristic-perspective correction · dimension discernment · dominant subject identification · anchor verse verification · Session B/D pointer capture · observations log (written continuously) · per-registry patch construction (inline after each registry Phase C) · return instruction production · CC directive production |
| **Claude Code** | Cluster extract construction · root family extract construction · existing pointers extract construction · anchor verse vertical pass extract construction (on demand) · patch application · context_description sync · session B/D pointer persistence · registry and cluster stamp updates · post-application integrity checks · dimension report regeneration |

Claude Code does not make analytical decisions. All classification, dimension assignment, and quality assessment decisions belong to Claude AI.

**Three governing principles:**

> **The dimension always follows the verse.** Read the group. Name what you see. Then check whether an existing dimension already captures it. If yes — assign it. If no — propose a new name. Never fit a group into a dimension that does not genuinely describe it.

> **Fix or stop.** The Dimension Review does not flag and pass. When a quality problem is identified, it follows whatever sub-process is necessary to fix it. If a fix cannot be completed within the session, a formal return instruction is issued to the appropriate upstream process. A group with an unresolved quality problem does not advance to Phase C.

> **Write on discovery (per GR-OBS-001 — non-waivable).** Every analytical decision is written to the observations log immediately on discovery. Nothing is accumulated in memory for later transcription.

---

## 2. Operation Modes

The Dimension Review operates in two modes. The mode is declared at startup (Section 7.4, Step 0) and governs scope, stamp rules, and patch operations throughout the session.

### 2.1 Cluster Mode — normal pipeline path

**Invoked by:** Normal Dimension Review processing — one cluster at a time, after all active registries in the cluster have `verse_context_status = Complete`.

**Scope:**
- Phase A: full cluster
- Phase B: full cluster
- Phase C: all active registries in the cluster, one at a time

**Stamps:** Registry-level stamp set for each registry as it completes Phase C. Cluster-level stamp set when all registries in the cluster are complete (included in the final registry's patch).

**Gate:** Cluster Mode completion is the DataPrep gate — `wa_dim_review_cluster_log` must contain a record for the cluster before Session B DataPrep may open for any registry in that cluster.

### 2.2 Registry Mode — Session B Stage 1 sub-process

**Invoked by:** Session B Stage 1, when the audit finds `dim_review_status = null` or `dominant_subject = null` for any group in the target registry — i.e. the Dimension Review has not been run for this registry before Session B begins.

**Scope:**
- Phase A: full cluster — analytical coherence requires reading the full cluster context even when only one registry is the target
- Phase B: full cluster — QA-TERMCENTRIC screening requires full cluster context; Phase B findings for all registries are recorded in the observations log for use when the full cluster session runs
- Phase C: scoped to the target registry only

**Why Phase B must span the full cluster in Registry Mode:** Phase B.5 requires understanding what inner-being characteristic a group serves — a judgement that requires the context of adjacent groups in the cluster. A group that looks term-centric in isolation may be interpretable when adjacent groups are seen; conversely, a group that looks clear in isolation may reveal a QA-TERMCENTRIC problem only when the cluster's other groups provide the contrast. Phase B quality assessment is not reliable when scoped to a single registry.

**Stamps:** Registry-level stamp set for the target registry. Cluster-level stamp is NOT set — the cluster has not been fully reviewed.

**Gate:** Registry Mode completion satisfies the Stage 2 gate for the target registry only. The full cluster session must still be run to set the cluster-level DataPrep stamp.

### 2.3 Two-gate system

| Gate | What satisfies it | What it opens |
|-|-|-|
| **Stage 2 gate** | `dim_review_status = Complete` on registry + all groups at `CLAUDE_AI` confidence + all `dominant_subject` assigned | Session B Stage 2 may begin for this registry. May be satisfied by Registry Mode completion. |
| **DataPrep gate** | `wa_dim_review_cluster_log` record for cluster + all registries in cluster at `dim_review_status = Complete` + all at `verse_context_status = Complete` | Session B DataPrep for any registry in the cluster. Requires full Cluster Mode completion — Registry Mode alone does not satisfy this gate. |

These gates are independent. A registry may proceed to Stage 2 under the Stage 2 gate even when the cluster's DataPrep gate is not yet satisfied.

---

## 3. Foundational Principles

### 3.1 Data-first

Per GR-PROG-002: no dimension category is assumed correct before the group content has been read. The automated labels are a starting hypothesis — useful as orientation, not as conclusion. The confirmed dimension vocabulary (Section 6.7) is a working starting point derived from data, not an authoritative final system.

### 3.2 Progressive refinement

Dimensions move through a confidence progression:

| Stage | `dimension_confidence` | `manual_override` | Meaning |
|-|-|-|-|
| Automated keyword match (broad) | `KEYWORD_WEAK` | 0 | Starting hypothesis — requires review |
| Automated keyword match (specific) | `KEYWORD_STRONG` | 0 | More reliable — still requires review |
| Claude AI assessed | `CLAUDE_AI` | 0 | Claude AI has read the group; dimension reflects content |
| Researcher confirmed anchor | `CLAUDE_AI` | 1 | Researcher confirmed — locked against automated change |

A dimension reaches anchor status only when the researcher is confident it reflects what the data genuinely shows.

### 3.3 The dimension vocabulary is iterative

Per GR-PROG-002: the vocabulary in Section 6.7 was derived from data and represents the current best understanding. It will be revised as more data is reviewed. When a group does not fit any existing dimension, that is a finding, not a failure.

*Current vocabulary: 11 dimensions. Dimension 11 (Divine-Human Correspondence) added from C18 data at v1.6.*

### 3.4 Group quality is the prerequisite

A dimension assignment is only as reliable as the group it is assigned to. Phase B must be complete — and all quality problems resolved — for every active group in the cluster extract before Phase C proceeds for any registry. The fix-or-stop principle applies without exception.

### 3.5 Session B will arise from the data

When the Dimension Review is done well — clusters validated, groups quality-checked, dimensions grounded in group content — Session B analysis will have a clear foundation. Rushing this stage is counterproductive. Session B depth is directly proportional to Dimension Review quality.

### 3.6 All changes go through the patch process

Per GR-PROC-003 (non-waivable): no corrections to group descriptions, dimension assignments, or any database field are made by direct manipulation. Every change is encoded in a patch file, reviewed by the researcher, and applied by Claude Code.

### 3.7 Dominant subject

Every active group receives a `dominant_subject` value identifying the primary bearer of the characteristic as observed in the verse evidence. NULL is not valid after Dimension Review.

| Value | What it names |
|-|-|
| `GOD` | The subject of this group is God in any form — Father, Son, Spirit |
| `HUMAN` | The subject is the individual human person being studied |
| `OTHER_HUMAN` | The subject is another human person in relationship with the first |
| `UNSEEN` | The subject is an entity from the unseen world |
| `NONE` | No dominant subject identifiable, or the group is purely circumstantial |

### 3.8 Characteristic terms and property terms

Groups in the Dimension Review derive from two structurally different types of terms:

| Type | Definition | Behaviour |
|-|-|-|
| **Characteristic terms** | Name an inner-being state directly. The term itself is the characteristic. | Removing the term removes the characteristic. The verse is about that characteristic. |
| **Property terms** | Describe how inner-being characteristics operate — mechanism, condition, expression, or channel. | Can serve different characteristics across the verse corpus. Can serve the same characteristic in opposite ways. |

This distinction governs how group descriptions are assessed in Phase B and how dimensions are assigned in Phase C. It does not change the dimension vocabulary — dimensions name the characteristic, regardless of which type of term gives rise to the group.

---

## 4. The `wa_dimension_index` — What Claude AI Reads

### 4.1 Key fields for Dimension Review

| Field | Purpose in this stage |
|-|-|
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

### 4.2 What Claude AI does not have during the Dimension Review

Claude AI does not have full verse texts unless explicitly provided via extract or via the anchor verse vertical pass extract (Section 10.5). The `context_description` is the primary analytical input. Where a description is insufficient, Claude AI requests the appropriate extract rather than guessing.

---

## 5. Phase A — Cluster Assignment Review

### 5.1 Purpose

Validate that cluster assignments are analytically coherent before group-level review begins.

### 5.2 Excluded registries

Before assessing coherence, identify excluded registries: any registry in the cluster with `session_b_status = "Analysis Complete"` is excluded from Phase B and Phase C. These registries remain visible in the Phase A cluster picture — their presence is noted and informs the coherence assessment — but they are explicitly marked as excluded from further processing. Their group counts are not included in the active group total.

### 5.3 Review criteria

For each cluster, assess the active (non-excluded) registries against:

1. **Internal coherence** — do the words share genuine inner-being affinity?
2. **Boundary cases** — are there words predominantly about external acts, divine attributes, or social structures?
3. **Missing affinity** — are there words with stronger affinity for a different cluster?
4. **Size** — clusters with fewer than 4 or more than 13 active words warrant review

Per GR-PROG-003: cluster assignment is a processing unit, not a semantic classification. Propose reassignment only when placement materially disrupts analytical work — not on the basis of semantic affinity alone. Semantic relationships across clusters are captured by correlation signals and Session D synthesis.

### 5.4 Output

Write Phase A findings to the observations log immediately on assessment. Format per Section 8.2.

---

## 6. Phase B — Group Quality Review

### 6.1 Purpose

Assess the quality of every active group's `context_description` before dimension assignment begins. Every group belonging to an active registry (i.e. `session_b_status ≠ "Analysis Complete"`) receives a QA flag. Groups belonging to excluded registries are skipped entirely — no QA flag, no observations log entry, and not counted in coverage verification.

### 6.2 QA flag vocabulary

| Flag | Meaning |
|-|-|
| `QA-CLEAR` | Description is sufficient for dimension assignment — characteristic-perspective model applied |
| `QA-TERMCENTRIC` | Description names what the term does rather than the inner-being characteristic served — triggers Phase B.5 |
| `QA-VAGUE` | Description is too brief or general to support dimension assignment |
| `QA-BROAD` | Description conflates two or more distinct inner-being characteristics in a single group |
| `QA-EXTERNALISED` | Description focuses on external circumstances rather than the inner-being characteristic |
| `QA-REVIEW` | Requires closer examination — potential data issue, conflicting evidence, or ambiguous construction |

Write every QA flag assignment to the observations log immediately on assessment. Do not accumulate flags for later writing.

### 6.3 QA-TERMCENTRIC — definition

A group description is term-centric when it names what the term does rather than what inner-being characteristic the term serves in that verse context.

**Indicators:**
- Description begins with the term name followed by "as [action verb]ing"
- Description restates the term's lexical meaning without naming the inner-being state engaged
- No inner-being characteristic is named anywhere in the description

**Test:** Could this description apply equally to a verse where the inner-being content is entirely different? If yes — it is term-centric.

A term-centric description does not mean the group or its verse assignments are wrong — it means the description needs realignment. Phase B.5 corrects it.

### 6.4 Group description correction protocol — non-TERMCENTRIC flags

For groups flagged `QA-VAGUE`, `QA-BROAD`, `QA-EXTERNALISED`, or `QA-REVIEW`:

**Step 1 — Claude AI assessment.** State: (a) what is inadequate; (b) what a better description would need to capture; (c) a proposed revision if resolvable from existing context; (d) whether verse text review is needed. Write to observations log.

**Step 2 — Researcher decision.** Confirm, amend, or reject. May direct verse-level review.

**Step 2a — CC directive for verification extract.** When verse-level review is needed: Claude AI produces a `.md` CC directive (Section 10.2). Claude Code constructs and returns the group description verification extract.

**Step 3 — Correction options:**

| Scenario | Action |
|-|-|
| Correction clear, no verse assignment impact | Record in observations log; encoded in per-registry patch |
| Correction requires reviewing which verses belong | Record in observations log; researcher decides whether to trigger VCB re-run |
| Group may be incorrectly constructed | Researcher may trigger VCB re-run |

**Step 4 — After patch application.** Claude Code syncs `wa_dimension_index.context_description` with `verse_context_group.context_description`. Confirms before Phase C proceeds.

**Step 5 — Re-run trigger.** If VCB re-run triggered: governed by wa-versecontext-instruction [current]. Dimension Review for affected registry resumes after re-run completes.

### 6.5 Coverage verification — mandatory before Phase C begins

Before Phase C begins for any registry, Claude AI must verify that every active group has a Phase B entry in the observations log.

1. Identify all excluded registries (`session_b_status = "Analysis Complete"`) and sum their group counts
2. Subtract excluded group counts from `extract_meta.row_count` to obtain the active group count
3. Count unique group codes recorded in Phase B entries in the observations log
4. If counts match: coverage confirmed — write confirmation to observations log and proceed to Phase C
5. If counts do not match: complete Phase B for missing active groups before proceeding

Coverage verification entry format:
```
[COVERAGE-VERIFY] {cluster}
Groups in extract (total): {n}
Excluded registries (Analysis Complete): {list of reg_no/word} — {n} groups excluded
Active groups requiring Phase B: {n}
Groups with Phase B entry in observations log: {n}
Result: CONFIRMED / GAP FOUND — {list missing group codes if gap found}
```

### 6.6 Phase B.5 — Characteristic-perspective correction sub-process

**Triggered by:** `QA-TERMCENTRIC` flag on any group.

**Purpose:** Realign the group description from term-centric to characteristic-perspective, following the model established in wa-versecontext-instruction [current] Section 4. The fix-or-stop principle applies throughout.

**Step 1 — Determine whether the characteristic is discernible.**

Read the existing `context_description` and the anchor verses available in the cluster extract. Ask: what inner-being characteristic does this verse cluster primarily engage? What is the term's role relative to that characteristic?

- Characteristic discernible from existing data → proceed to Step 2 (in-session rewrite)
- Characteristic not discernible from description alone → request anchor verse vertical pass extract (Section 10.5) and proceed to Step 2 after reading it
- Anchor verses themselves are insufficient (verse evidence is ambiguous or the grouping appears wrong) → proceed to Step 3

**Step 2 — In-session rewrite.**

Produce a revised `context_description` following the characteristic-perspective format:

> *[Characteristic] — [term] as [role]*

The revised description must:
- Name the inner-being characteristic the verse cluster primarily engages
- State the term's role accurately: seat, channel, mechanism, expression, obstacle, or counterpart
- Be grounded in what the verses show
- Be sufficient to distinguish this group from other groups for the same term

Write both the old and new text to the observations log, with rationale, immediately on completion.

**Examples of compliant rewrites:**

| Old (term-centric) | New (characteristic-perspective) |
|-|-|
| *Hearing as the inner receptive faculty (faith, understanding, response)* | *Faith received — akoē as the channel through which faith arrives* |
| *Refusing to hear God* | *Heart-stubbornness expressed through refusal of God's word — sha.ma absent* |
| *Obeying God's voice: the inner act of covenantal obedience* | *Covenantal will — sha.ma as the act by which the will's orientation toward God is expressed* |
| *Ear as faculty for receiving divine address* | *Spiritual receptivity and its refusal — o.zen as the inner faculty through which divine word is received* |

**Step 3 — Assess grouping soundness.**

When the characteristic cannot be determined and the anchor verse vertical pass extract reveals that the grouping itself may be wrong:

- **Grouping is sound but description is wrong:** proceed to Step 2 with the richer data from the vertical pass extract.
- **Grouping is wrong — verses need re-reading and re-grouping:** trigger a VCB re-run under wa-versecontext-instruction [current]. Issue a return instruction (Section 6.7). The Dimension Review for this registry pauses.
- **Source data is defective:** issue a return instruction (Section 6.7) directing return to Session A / STEP extraction. The Dimension Review for this registry pauses.

**Step 4 — Patch encoding.**

All in-session rewrites are recorded in the observations log with full old and new text. The per-registry patch reads these entries and encodes them as group description corrections, updating:
- `verse_context_group.context_description`
- `wa_dimension_index.context_description` (synced by Claude Code)
- `verse_context_group.notes` (correction rationale)

The group proceeds to Phase C after the rewrite is confirmed.

**Step 5 — Root family check.**

After rewriting a term-centric description, consult the root family extract (Section 10.4). Check whether sibling terms in the same root family have groups describing the same or related characteristics. Note any observations in the observations log. This may be a Session D pointer candidate.

### 6.7 Return instruction

A return instruction is issued when a quality problem identified in Phase B or Phase B.5 cannot be resolved within the Dimension Review session and requires upstream reprocessing. The Dimension Review for the affected registry pauses until the upstream process completes and the resume condition is met.

**File:** `wa-dim-{cluster}-{registry_no}-return-v{n}-{YYYYMMDD}.md`

**Content:**

```
# WA-DIM-RETURN — Cluster {C##} Registry {nnn} ({word})
Date: {YYYYMMDD} | Instruction version: wa-dimensionreview-instruction [current]

## Reason for return
{State precisely what was found and why it cannot be resolved within the Dimension Review}

## Registry affected
Registry {nnn} — {word} | Cluster {C##}
Groups affected: {list of group_codes}
Terms affected: {list of strongs_number / transliteration}

## Return destination
{One of:}
- VCB re-run: Re-run Verse Context for the listed terms under wa-versecontext-instruction [current].
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

---

## 7. Phase C — Dimension Discernment and Dominant Subject Assignment

### 7.1 Scope and exclusions

**Excluded registries do not enter Phase C.** Any registry with `session_b_status = "Analysis Complete"` is fully excluded. Claude AI must not process, assign dimensions to, or write Phase C entries for groups belonging to these registries.

In Registry Mode, Phase C is scoped to the target registry only.

### 7.2 The core questions

For each `QA-CLEAR` group (and each group that has passed Phase B.5 correction) belonging to an active registry, Phase C asks two questions:

> 1. **What kind of inner-being characteristic does this group describe?** — assign a dimension from the vocabulary (Section 7.7), or name a new one.
> 2. **Who is the primary bearer of this characteristic in this group's verse evidence?** — assign a `dominant_subject` value (Section 3.7).

**Property-term dimension assignment:** the dimension is assigned to the inner-being characteristic the group serves — not to the property term's function.

**Characteristic-term dimension assignment:** the dimension is assigned to the characteristic directly.

Write every Phase C assignment to the observations log immediately on assignment. Do not accumulate.

### 7.3 The three assignment rules

**Rule 1 — The verse leads.** Read the `context_description`. Name what you actually see. Then check whether an existing dimension captures it.

**Rule 2 — If it could fit more than one dimension, assign the dominant one.** One label per group. Record the reasoning in the observations log.

**Rule 3 — If it fits no existing dimension, do not force it.** Name what the group shows in plain language. Record in observations log. Present to researcher. Do not assign a dimension that does not genuinely describe it.

### 7.4 Working through a group — step by step

1. Read the `context_description` (confirmed characteristic-perspective from Phase B / B.5)
2. Identify: is this a characteristic term or a property term group? (Section 3.8)
3. **Read each anchor verse text against the description.** For every anchor verse supplied in the cluster extract:
   - Verify that the description captures all inner-being aspects the verse shows
   - Note any inner-being aspects present in the verse but absent from the description
   - Note any aspects claimed in the description that are not grounded in this anchor verse
   - If the anchor verse reveals a problem that cannot be resolved from the verse text alone, request a vertical pass extract (Section 10.5)
   - Write AV verification findings to observations log immediately (format: Section 8.2)
4. Ask: what inner-being characteristic does this group primarily describe?
5. Ask: who is the primary bearer — GOD, HUMAN, OTHER_HUMAN, UNSEEN, or NONE?
6. Check the dimension vocabulary (Section 7.7) — does an existing dimension fit clearly?
7. If yes: assign it. If no: name what the group shows; record and present to researcher
8. Check whether any observation warrants a Session B or Session D pointer (Section 7.5)
9. Write all findings to the observations log before moving to the next group

### 7.5 Session B and Session D pointer capture

Analytical observations arising during Phase C that are relevant to Session B or cross-registry synthesis must be captured in the observations log immediately on discovery, with full content. The per-registry patch encodes them as insert operations.

**Naming conventions:**

| Type | Convention | Example |
|-|-|-|
| Session B finding | `DIM-{registry_no}-{3-digit-sequence}` | `DIM-112-001` |
| Session D pointer | `DIM-{registry_no}-SD{3-digit-sequence}` | `DIM-112-SD001` |

**Root family pointers:** cross-registry root families identified via the root family extract are strong candidates for Session D pointers. Capture in observations log with full description.

**Uniqueness:** check the pre-existing pointers extract (Section 10.3) before inserting. Numbering must continue from the highest existing sequence.

For insert formats, see Section 9.3.

### 7.6 Cross-group patterns within a cluster

When reviewing groups across a cluster, look for:

- **Convergence** — multiple groups from different registries naming the same characteristic
- **Divergence** — groups clustered together but engaging materially different inner-being aspects
- **Subject patterns** — a dimension appearing consistently in GOD vs HUMAN groups
- **Vocabulary gaps** — recurring characteristics that no existing dimension captures
- **Root family resonance** — groups from terms in the same root family showing related or contrasting dimension assignments

Record all pattern observations in the observations log as they are identified.

### 7.7 The dimension vocabulary

*Derived from data. Working vocabulary as of v3.1. Will be revised as additional data is reviewed.*

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

`dominant_subject` for this dimension: assign `NONE` where the subject is genuinely dual. Assign `GOD` or `HUMAN` where one pole dominates but the correspondence is analytically significant.

**⚠ When no existing dimension fits:** name what the group shows in plain language. Record in observations log. Present to researcher. Do not assign a dimension that does not genuinely describe it.

---

## 8. Session Discipline

### 8.1 Unit of work

**The phase is the minimum unit of work.** A single session covers at most one phase for one registry (or the full cluster for Phase A). Claude AI must never attempt to complete multiple phases or multiple registries across all phases in a single session.

**Mandatory incremental discipline:**

Large clusters cannot be processed reliably in a single session. The C17 cluster (284 groups, 10 registries) is a confirmed example: attempting to hold all group analysis in working memory without intermediate disk writes risks truncation, analytical drift, and undetectable omissions. This discipline is a data integrity requirement, not a preference.

**Phase and session rules:**
- Phase A for the full cluster: one session
- Phase B for the full cluster: one session (may be split by registry for very large clusters)
- Phase C for a single registry: one session; immediately followed by per-registry patch production
- Phase C is never combined with Phase A or Phase B in the same session
- Within a single large registry (more than approximately 20 groups), Phase B and Phase C may each need to be split into sub-sessions by term family or group range; the split point must be recorded in the observations log

**Recommended session sizes:**

| Work | Expected session |
|-|-|
| Phase A — full cluster | 1 session |
| Phase B — up to ~30 groups | 1 session |
| Phase B — 30+ groups | Split by registry; 1 session per 2–3 registries |
| Phase C — up to ~15 groups | 1 session, followed immediately by per-registry patch |
| Phase C — 15+ groups | Split by term family; 1 session per ~15 groups; patch after each registry completes |

These are guidelines. The researcher and Claude AI may agree to different splits. What is non-negotiable: the observations log is written and downloaded before any session ends.

### 8.2 The observations log — primary analytical artefact

The observations log is the continuous write-to-disk record of all analytical decisions. It is the sole persistent record carried across session boundaries. The per-registry patch is constructed from it. No analytical decision should need to be re-derived during patch construction.

**The write-on-discovery principle is absolute.** Every item below is written to the observations log at the moment it is determined — not accumulated in memory:

- Phase A findings and cluster coherence assessment
- Every Phase B QA flag and its resolution
- Every Phase B.5 description rewrite (old text, new text, rationale)
- Every Phase C dimension assignment (group code, dimension, dominant subject, notes)
- Every AV verification finding
- Every Session B finding (with full content as it will appear in the database)
- Every Session D pointer (with full content as it will appear in the database)
- Coverage verification result
- Any return instruction triggers
- Registry-level and cluster-level stamp decisions
- Any instruction amendment notes

**File writing discipline:**
- Write to disk continuously per GR-OBS-001 — every observation or closely related group of observations goes to the log at the moment of discovery
- Dual-write per GR-FILE-008 — working directory (`/home/claude/`) and `/mnt/user-data/outputs/`
- Version-increment the observations log per GR-OBS-004 — at named batch boundaries (start of a new session on the same cluster, completion of a phase, or another logical point recorded in the log), not on every file save within a session. Previous versions remain on disk for audit.
- When resuming across sessions on the same cluster, read the most recent version of the log and continue from there

**At the end of every session:** present the current observations log file for researcher download via the `present_files` tool before stopping. The researcher must download the log before the next session begins. Analytical work not written to a downloaded log is at risk of being lost.

**At the start of every continuation session:** the researcher uploads the existing observations log. Claude AI reads it in full before beginning any new work. Claude AI does not re-derive or re-run any analysis already recorded in the log — it only appends to a new version file.

### 8.3 Session logs

Produce a session log at the end of every session (i.e. after every phase or sub-phase). Each session log records:

- Which cluster(s), registries, and phase(s) were covered in this session
- Phase A findings summary (if Phase A was run)
- Phase B quality flag summary and resolutions (if Phase B was run)
- Coverage verification result (if applicable)
- Phase C dimension proposals and researcher responses summary (if Phase C was run)
- Session B/D pointers captured
- Current observations log filename and version
- Dimension Review version stamp status (registry-level and cluster-level)
- Whether per-registry patch has been produced and confirmed applied
- **Unresolved session actions** — per GR-OBS-003: data-quality findings, methodology notes, sequencing decisions, verification records, or any other session action that has not been resolved must be explicitly listed. If all session actions are resolved, state this explicitly. A session log that is silent on unresolved actions does not satisfy this requirement.
- **Explicit stop point:** the last group code or phase step completed in this session
- **Resume instruction:** exactly what the next session must begin with — which registry, which phase, which group code, and which observations log version to load

Session logs are summaries — the observations log is the complete analytical record.

### 8.4 Startup protocol — analytical session

Before beginning any phase, confirm in sequence:

0. **Mode declaration.** State which mode: Cluster Mode or Registry Mode (Section 2). If Registry Mode, state the target registry number and word. This determines Phase C scope and stamp rules for the entire session.
1. **Instruction read.** State that this instruction has been read in full.
2. **Global rules confirmed.** State the GR-LOAD-001 confirmation for the current global rules file.
3. **Cluster extract confirmed loaded.** State the extract filename and row count.
4. **Root family extract confirmed loaded.** State the extract filename and root count.
5. **Existing pointers extract confirmed loaded.** State the extract filename and pointer count.
6. **Observations log initialised or loaded.**
   - First session for this cluster: create the observations log file on disk with header, filename, date, governing instruction version, mode declaration, and input file references.
   - Continuation session: the researcher has uploaded the existing observations log. State the filename and version. Read it in full. Confirm the stop point from the previous session log. Do not re-run or re-record any analysis already present in the log.
7. **Registry status check — two filters applied at startup:**

   *Filter 1 — Analysis Complete exclusion:* scan every registry in `cluster_registries` for `session_b_status = "Analysis Complete"`. Any registry carrying this status is excluded from all Phase B and Phase C processing. Record each excluded registry in the observations log under an `[EXCLUDED]` entry. Exclusion applies to coverage verification: excluded registry groups are subtracted from the total group count before the coverage check is run (Section 6.5).

   *Filter 2 — VCB completeness check:* for remaining (non-excluded) registries, confirm `verse_context_status = Complete`. In Registry Mode, this check still spans the full cluster — Phase B requires cluster context regardless of mode. If non-excluded registries lack VCB completion, note this; it does not block Phase B or Phase C for the target registry but must be flagged.

   Analysis Complete exclusion takes absolute precedence over VCB status.

8. **Schema check noted.** Note that Claude Code must verify schema additions (Section 11.3) before applying stamps.
9. **Phase and scope declaration.** State exactly which phase and which registry (or cluster scope) this session will cover. State the expected stopping point. Confirm that no work beyond this scope will be attempted in this session.

### 8.5 Session boundary protocol

**At the end of every session, Claude AI must:**

1. Finish writing all analytical work from the current session to the observations log on disk.
2. Write a session boundary marker to the observations log:
```
[SESSION-END] {YYYYMMDD} | Phase: {phase} | Registry: {reg_no} ({word}) | Last group completed: {group_code or "N/A"}
Next session begins: Phase {X} | Registry {reg_no} ({word}) | Starting from: {group_code or "beginning of phase"}
Observations log version: {filename}
```
3. Present the observations log file for researcher download via the `present_files` tool.
4. Stop. Do not begin the next phase or next registry.

**At the start of every continuation session, Claude AI must:**

1. Confirm the researcher has uploaded the observations log from the previous session.
2. Read the observations log in full from the beginning.
3. Locate the `[SESSION-END]` marker at the end of the log.
4. State the resume point: *"Resuming from: [phase, registry, group code]. The previous session ended at [last group code]. I will begin with [first group code or step in this session]."*
5. Append new work to the existing log — never overwrite or replace it.

**Hard limits — Claude AI must never:**
- Attempt to complete an entire cluster in a single session
- Attempt to complete more than one phase for a single registry in a single session
- Reconstruct analytical decisions from memory rather than reading from the uploaded observations log
- Skip per-registry patch production after Phase C for a registry is complete
- Skip the download step at the end of a session

### 8.6 Per-registry patch protocol

The patch is produced inline, immediately after each registry's Phase C is confirmed complete. Patch construction is mechanical — no analytical work is performed.

**Trigger:** Phase C for a registry is complete (all groups assigned, STAMP entry written to observations log, observations log finalised and written to disk per GR-OBS-004).

**Steps:**

1. **Finalise observations log.** Write the current registry's STAMP entry and SESSION-END marker to the observations log. Version-increment per GR-OBS-004 — registry completion is a named boundary. This ensures the patch reads from a stable, complete snapshot.

2. **Assign patch ID.** Format: `PATCH-{YYYYMMDD}-DIMREVIEW-{CLUSTER}-REG{NNN}-V{n}` — e.g. `PATCH-20260414-DIMREVIEW-C17-REG023-V1`.

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

## 9. Output Formats

### 9.1 Observations log — header and entry formats

**File header:**
```
# WA Dimension Review Observations Log — {C##}
Filename: wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md
Governing instruction: wa-dimensionreview-instruction [current]
Mode: {Cluster Mode / Registry Mode — target registry {nnn} ({word})}
Cluster extract: wa-dim-{cluster}-extract-{YYYYMMDD}.json ({n} groups)
Root family extract: wa-dim-{cluster}-rootfamily-{YYYYMMDD}.json ({n} roots)
Existing pointers extract: wa-dim-{cluster}-existing-pointers-{YYYYMMDD}.json ({n} pointers)
Session date: {YYYYMMDD}
```

**Excluded registry entry:**
```
[EXCLUDED] Reg {n} ({word}) | session_b_status = Analysis Complete
All {n} groups in this registry are excluded from Phase B, Phase C, and patch operations.
```

**Phase A entry:**
```
[PHASE-A] {cluster} | {YYYYMMDD}
{Cluster coherence assessment — see Section 5.3}
### Excluded registries (Analysis Complete)
{list with registry numbers, words, and group counts — or "None"}
### Active registries
{list with registry numbers and group counts}
### Coherence assessment
{What inner-being affinity holds this cluster together}
### Boundary observations
{Any misplaced words or ambiguous scope}
### Cross-registry root families
{Summary from root family extract}
### Recommendation
[ ] Confirm as-is
[ ] Propose reassignment: {word} (Reg {no}) → {target cluster} | Reason: {brief reason}
```

**Phase B entry (one per group):**
```
[PHASE-B] {group_code} | {strongs} {transliteration} | Reg {n} ({word})
QA-FLAG: {flag}
{If QA-CLEAR: brief note why}
{If any other flag: what is inadequate and proposed correction}
```

**Phase B.5 entry (one per rewrite):**
```
[PHASE-B5] {group_code} | REWRITE
OLD: {existing context_description}
NEW: {revised characteristic-perspective description}
RATIONALE: {why the old description was term-centric and what characteristic the new description names}
PATCH-TARGET: verse_context_group.id = {id} | wa_dimension_index.id = {id}
```

**Phase C entry (one per group):**
```
[PHASE-C] {group_code} | {strongs} {transliteration} | Reg {n} ({word})
DIMENSION: {dimension name}
DOMINANT-SUBJECT: {GOD|HUMAN|OTHER_HUMAN|UNSEEN|NONE}
NOTES: {reasoning — especially if automated label is being changed or near-miss with another dimension}
PATCH-TARGET: wa_dimension_index.id = {id}
```

**AV verification entry (written as part of Phase C Step 3, one per group):**
```
[AV-VERIFY] {group_code} | {strongs} {transliteration}
AV: {verse_ref} — {verse_text}
DESC covers: {what aspects of the verse the description captures}
VERSE also shows: {inner-being aspects present in the verse but not in the description — or "nothing additional"}
VERDICT: FULL ALIGNMENT / DESC PARTIALLY EXCEEDS AV / DESCRIPTION GAP / ANCHOR VERSE MISMATCH
FLAG: {NONE / MINOR / MODERATE / SIGNIFICANT} — {brief statement of issue if not NONE}
ACTION: {correction required, or "None"}
```

Verdict definitions:
- **FULL ALIGNMENT** — description captures all inner-being aspects the verse shows; no action needed
- **DESC PARTIALLY EXCEEDS AV** — description includes claims drawn from other verses in the group, not this anchor verse alone; note explicitly but no correction needed if claims are valid for the wider group
- **DESCRIPTION GAP** — the verse shows inner-being content not captured in the description; assess whether the description needs correction
- **ANCHOR VERSE MISMATCH** — the anchor verse does not ground the description at all; the wrong verse has been designated as anchor; correction required

**Session B finding entry:**
```
[SESSION-B] {flag_label e.g. DIM-187-001}
REGISTRY: {n} ({word})
DESCRIPTION: {full text as it will appear in wa_session_b_findings.description}
PATCH-TARGET: wa_session_b_findings insert
```

**Session D pointer entry:**
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
Groups in extract (total): {n}
Excluded registries (Analysis Complete): {list} — {n} groups excluded
Active groups requiring Phase B: {n}
Groups with Phase B entry in observations log: {n}
Result: CONFIRMED / GAP FOUND — {list missing group codes if gap found}
```

**Stamp decision entry:**
```
[STAMP] Registry {n} ({word})
dim_review_status: Complete
dim_review_version: WA-DimensionReview-Instruction-v3.1-20260414
PATCH-TARGET: word_registry.no = {n}
```

**Instruction amendment note entry:**
```
[INSTRUCTION-NOTE] {YYYYMMDD}
OBSERVATION: {what was observed that suggests an instruction amendment}
PROPOSED CHANGE: {what should change in the instruction}
ACTION: Flag for instruction update after session
```

### 9.2 Per-registry dimension patch

JSON patch for Claude Code. Produced inline after each registry's Phase C is confirmed complete. Constructed by reading the observations log — no re-derivation of analytical decisions.

**Patch meta:**
```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-DIMREVIEW-{CLUSTER}-REG{NNN}-V{n}",
    "patch_type": "DIMREVIEW",
    "cluster": "{C##}",
    "registry_no": {nnn},
    "registry_word": "{word}",
    "produced_date": "{YYYYMMDD}",
    "produced_by": "WA-DimensionReview-Instruction-v3.1-20260414",
    "observations_log": "wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md",
    "session_b_status": null,
    "description": "Dimension review patch — {cluster} Reg {nnn} ({word}): {brief summary}"
  }
}
```

**`session_b_status: null` — formal note:** The Dimension Review does not advance the `session_b_status` workflow. The correct value is always `null`. The patch applicator must not reject DIMREVIEW patches for having `null` in this field — this is a registered exception per wa-patch-instruction [current].

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

**Group description correction operation (Phase B.5 rewrite):**
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

Followed immediately by the `wa_dimension_index` context_description sync operation:
```json
{
  "op_id": "OP-{nnn}",
  "operation": "update",
  "table": "wa_dimension_index",
  "match": { "verse_context_group_id": {verse_context_group_id} },
  "set": {
    "context_description": "{same revised description}"
  },
  "description": "Sync wa_dimension_index.context_description for group {group_code}"
}
```

**Registry version stamp operation:**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "update",
  "table": "word_registry",
  "match": { "no": {registry_no} },
  "set": {
    "dim_review_status": "Complete",
    "dim_review_version": "WA-DimensionReview-Instruction-v3.1-20260414"
  },
  "description": "Registry {nnn} ({word}): Dimension Review complete under v3.1"
}
```

**Cluster stamp operation (final registry patch only):**
```json
{
  "op_id": "OP-{nnn}",
  "operation": "insert",
  "table": "wa_dim_review_cluster_log",
  "record": {
    "cluster": "{C##}",
    "completed_date": "{YYYYMMDD}",
    "instruction_version": "WA-DimensionReview-Instruction-v3.1-20260414",
    "registry_count": {n},
    "group_count": {n},
    "anchored_count": {n},
    "notes": "{any cluster-level observations}"
  },
  "description": "Cluster {C##} Dimension Review complete — stamp set"
}
```

**Session B finding insert and Session D pointer insert:** full content read from observations log. Table targets: `wa_session_b_findings` and `wa_session_research_flags` respectively. For field mapping, see Section 7.5.

### 9.3 Group description correction patch — out-of-session use only

Patch type: `DIMREVIEW-GRPDESC`. Used only for corrections made outside a live cluster session.

**File:** `wa-dim-{cluster}-grpdesc-patch-v{n}-{YYYYMMDD}.json`

**Patch ID format:** `PATCH-{YYYYMMDD}-DIMREVIEW-GRPDESC-{scope}-V{n}`

---

## 10. Data Extracts — Required Inputs for Claude AI

### 10.1 Cluster extract — primary session input

**File:** `wa-dim-{cluster}-extract-{YYYYMMDD}.json`

All `wa_dimension_index` rows for the requested cluster, joined to `word_registry`, `verse_context_group`, `mti_terms`. All anchor and related verse arrays mandatory. Produced by Claude Code per the CC instruction and database schema.

**`produced_by`:** `"Claude Code — WA-DimensionReview-Instruction-v3.1-20260414"`

**Status filter requirement (GR-DATA-001):** All CC directives and extract queries that join or filter against `mti_terms` must include `AND mt.status IN ('extracted', 'extracted_thin')`. Omitting this filter causes delete-status terms to appear as false positives. This applies to all extract construction queries without exception.

### 10.2 Group description verification extract — on demand

**File:** `wa-dim-{cluster}-grpverify-{group_code}-{YYYYMMDD}.json`

**CC directive file:** `wa-dim-{cluster}-cc-directive-grpverify-{group_code}-{YYYYMMDD}.md`

Constructed on demand when Phase B requires verse-level review before a description correction can be written. Claude AI produces the CC directive; Claude Code constructs and returns the extract.

### 10.3 Pre-existing Session B/D pointer extract — standard session input

**File:** `wa-dim-{cluster}-existing-pointers-{YYYYMMDD}.json`

Includes all existing entries for cluster registries — both Dimension Review and Verse Context batch flags. Required to ensure new pointer numbering continues from the highest existing sequence.

Per GR-DATA-007: the content of existing pointer records is a historical record from the session in which each flag was raised. It is not a current-state assertion about the programme. Read this extract for numbering continuity only — do not treat flag descriptions as verified current facts without checking against live data.

### 10.4 Root family cluster extract — standard session input

**File:** `wa-dim-{cluster}-rootfamily-{YYYYMMDD}.json`

Required session input. Constructed by Claude Code at the same time as the cluster extract. Identifies cross-registry root families relevant to the cluster. Used during Phase B.5 Step 5 and Phase C Session D pointer identification.

### 10.5 Anchor verse vertical pass extract — on-demand sub-process input

**File:** `wa-dim-{cluster}-vpass-{group_code}-{YYYYMMDD}.json`

**CC directive file:** `wa-dim-{cluster}-cc-directive-vpass-{group_code}-{YYYYMMDD}.md`

**Purpose:** obtain full term-link context for an anchor verse when the in-session anchor verse reading (Section 7.4 Step 3) reveals a problem that cannot be resolved from the verse text alone.

**Request a vertical pass extract when the anchor verse reading shows:**
- The group description has been rewritten in Phase B.5 and the new description names a characteristic that should be corroborated by the verse's full term-link context
- The anchor verse is in a key theological passage and the full term-link context would confirm or challenge the dimension assignment
- The anchor verse was previously flagged as analytically complex
- A `QA-BROAD` flag was raised
- The anchor verse text alone is insufficient to determine whether the description's claims are grounded

**Do not over-request.** Request only when the conditions above are met. Most groups will not require a vertical pass extract — the in-session anchor verse reading is sufficient.

**One extract per group.** Do not request separate extracts for each anchor verse.

**Naming discipline is mandatory:** the group_code is the only permissible identifier after `vpass`. Do not use verse references, registry names, or other identifiers.

---

## 11. Dimension Review Version Stamps

### 11.1 Purpose

The version stamp system records, at both registry and cluster level, which version of the Dimension Review instruction was used to review and confirm the data. Session B gates on the cluster-level stamp.

### 11.2 Registry-level stamp

When all groups for a registry have passed Phase B (including Phase B.5 where triggered) and Phase C dimension assignments are confirmed:

| Field | Table | Value |
|-|-|-|
| `dim_review_status` | `word_registry` | `Complete` |
| `dim_review_version` | `word_registry` | `WA-DimensionReview-Instruction-v3.1-20260414` |

The registry stamp is included in the per-registry patch and applied by Claude Code when the patch is applied.

**In Registry Mode:** the registry-level stamp is set for the target registry only. It satisfies the Stage 2 gate for that registry. It does NOT set the cluster-level stamp and does NOT open the DataPrep gate for other registries in the cluster.

### 11.3 Cluster-level stamp and schema requirements

When all registries in a cluster have `dim_review_status = Complete`, Claude Code inserts a record into `wa_dim_review_cluster_log`. This is the DataPrep gate.

**In Registry Mode:** the cluster-level stamp is NOT set. The full cluster Dimension Review session must be run to set it.

**Schema additions** — apply once, before the first cluster stamp:
- `word_registry.dim_review_status` (TEXT)
- `word_registry.dim_review_version` (TEXT)
- `wa_dim_review_cluster_log` table

Claude Code verifies these fields exist before applying any stamp operation.

### 11.4 Session B gate system

| Gate | Condition | What it opens |
|-|-|-|
| **Stage 2 gate** | `dim_review_status = Complete` on registry AND all dimension_index groups at `CLAUDE_AI` confidence AND all `dominant_subject` assigned | Session B Stage 2 (analytical passes) may begin for this registry |
| **DataPrep gate** | `wa_dim_review_cluster_log` record for cluster AND all registries at `dim_review_status = Complete` AND all at `verse_context_status = Complete` | Session B DataPrep for any registry in the cluster |

**Stage 2 gate query:**
```sql
SELECT no, word, dim_review_status, verse_context_status
FROM word_registry
WHERE no = {registry_no}
  AND dim_review_status = 'Complete'
  AND verse_context_status = 'Complete';
```

---

## 12. Claude Code Protocol and Boundaries

### 12.1 Claude Code responsibilities

Per GR-DIR-001: all directives to Claude Code are written in plain language, not as JSON patches. Each directive specifies motivation, exact operations, and expected outcomes. Claude Code executes; Claude AI determines what should be done.

| Task | Claude Code action |
|-|-|
| Construct cluster extract | Query per Section 10.1 |
| Construct root family extract | Query per Section 10.4 |
| Construct existing pointers extract | Query per Section 10.3 |
| Construct anchor verse vertical pass extract | Query per Section 10.5 — on demand, per group |
| Construct group verification extract | Query per Section 10.2 — on demand |
| Apply dimension patch | Update `wa_dimension_index`; sync `context_description`; apply group description corrections; insert session B/D pointers; set registry and cluster stamps |
| Apply cluster reassignment patch | Update `word_registry.cluster_assignment` and `wa_dimension_index.cluster_assignment` |
| Apply schema additions | Create `dim_review_status`, `dim_review_version`, `wa_dim_review_cluster_log` per Section 11.3 |
| Post-application integrity check | Verify manual_override rows not incorrectly modified; verify context_description sync; verify stamp fields set correctly; report discrepancies |
| Trigger VC re-run | Reset `verse_context_status = 'In Progress'` for affected registry on researcher instruction |
| Regenerate dimension report | After each patch application cycle |

### 12.2 Claude Code boundaries

Claude Code does not make analytical decisions. It does not:
- Determine dimensions or dominant subjects
- Assess group quality or flag QA issues
- Decide whether a description is term-centric
- Write or approve revised descriptions
- Set `manual_override = 1` except on explicit researcher instruction in the patch
- Trigger VCB re-runs without researcher decision

### 12.3 Patch validation before application

Before applying any Dimension Review patch:

1. `patch_id` not previously applied
2. All `wa_dimension_index.id` values exist
3. No operation targets a `manual_override = 1` row without explicit override in the operation
4. All `verse_context_group.id` values exist (for description corrections)
5. All `finding_id` values unique programme-wide
6. All `flag_label` values unique programme-wide
7. `session_b_status` in `_patch_meta` is `null`
8. All `dominant_subject` values are valid vocabulary
9. `dim_review_version` value is a recognised instruction version string
10. `wa_dim_review_cluster_log` insert: cluster code is a valid cluster assignment value in `word_registry`

### 12.4 Post-application reporting

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

### 12.5 Patch types

| Patch type | Governing instruction | Valid `session_b_status` | Content |
|-|-|-|-|
| `DIMREVIEW` | wa-dimensionreview-instruction [current] | `null` | `wa_dimension_index` updates; `verse_context_group` corrections; `wa_session_b_findings` inserts; `wa_session_research_flags` inserts; `word_registry` stamp update (one registry per patch); `wa_dim_review_cluster_log` insert (final registry patch only) |
| `DIMREVIEW-GRPDESC` | wa-dimensionreview-instruction [current] | `null` | Out-of-session group description corrections only |

---

## 13. Decision Rules and Boundaries

### 13.1 Claude AI never acts unilaterally on

- Cluster reassignments
- Vocabulary additions, splits, or renamings
- Setting `manual_override = 1`
- Triggering a Verse Context batch re-run
- Marking a group as `delete_flagged`
- Writing revised `context_descriptions` to the patch without researcher confirmation
- Setting cluster stamps — set by Claude Code after all registries in the cluster are confirmed

### 13.2 Claude AI may propose independently

- Dimension assignments for any group (written to observations log)
- `dominant_subject` assignments (written to observations log)
- Corrections to existing labels that do not match group content (written to observations log)
- Quality flags including `QA-TERMCENTRIC`
- Characteristic-perspective rewrites under Phase B.5 (proposed — confirmed before patch encoding)
- Anchor verse vertical pass extract requests (produces CC directive independently)
- Candidate new dimension names where no existing dimension fits (written to observations log)
- Session B/D pointer content (written to observations log with full text)
- Return instructions (issued independently when conditions in Section 6.7 are met; researcher is informed)
- Instruction amendment notes (written to observations log under `[INSTRUCTION-NOTE]` tag)

---

## 14. Integrity Rules

| Rule | Requirement |
|-|-|
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
| DR-11 | `dominant_subject` must be assigned for every active group in Phase C — NULL is not valid post-review |
| DR-12 | `dominant_subject` values restricted to: GOD, HUMAN, OTHER_HUMAN, UNSEEN, NONE |
| DR-13 | The dimension vocabulary may only be extended by researcher decision |
| DR-14 | A `QA-TERMCENTRIC` group must not advance to Phase C until Phase B.5 correction is complete or a return instruction is issued |
| DR-15 | The anchor verse vertical pass extract must follow the naming convention `wa-dim-{cluster}-vpass-{group_code}-{YYYYMMDD}.json` — no other naming is permitted |
| DR-16 | Session B may not open for a cluster until `wa_dim_review_cluster_log` contains a record for that cluster and all registries show `dim_review_status = Complete` |
| DR-17 | Schema additions (Section 11.3) must be applied before the first stamp operation — Claude Code verifies before applying any stamp |
| DR-18 | A registry that has received a return instruction retains `dim_review_status = NULL` until the upstream process completes and the Dimension Review resumes and confirms the registry |
| DR-19 | Every analytical decision must be written to the observations log on discovery — no accumulation in memory for later transcription |
| DR-20 | Per-registry patch construction reads from the observations log only — no re-derivation of analytical decisions is permitted; patch scope is limited to the completed registry and must not include entries from registries not yet confirmed complete |

---

## 15. Naming Conventions

All filenames are fully lowercase. No uppercase characters anywhere (per GR-FILE-007).

**File naming pattern:** `wa-dim-{cluster}-{description}-{version}-{YYYYMMDD}.{ext}`

The cluster reference immediately follows the prefix, allowing all files from the same cluster to sort together.

| File type | Pattern | Example |
|-|-|-|
| Cluster extract | `wa-dim-{cluster}-extract-{YYYYMMDD}.json` | `wa-dim-c01-extract-20260414.json` |
| Root family extract | `wa-dim-{cluster}-rootfamily-{YYYYMMDD}.json` | `wa-dim-c01-rootfamily-20260414.json` |
| Existing pointers extract | `wa-dim-{cluster}-existing-pointers-{YYYYMMDD}.json` | `wa-dim-c01-existing-pointers-20260414.json` |
| Group verification extract | `wa-dim-{cluster}-grpverify-{group_code}-{YYYYMMDD}.json` | `wa-dim-c02-grpverify-3012-001-20260414.json` |
| Vertical pass extract | `wa-dim-{cluster}-vpass-{group_code}-{YYYYMMDD}.json` | `wa-dim-c02-vpass-758-001-20260414.json` |
| CC directive — group verification | `wa-dim-{cluster}-cc-directive-grpverify-{group_code}-{YYYYMMDD}.md` | `wa-dim-c02-cc-directive-grpverify-3012-001-20260414.md` |
| CC directive — vertical pass | `wa-dim-{cluster}-cc-directive-vpass-{group_code}-{YYYYMMDD}.md` | `wa-dim-c02-cc-directive-vpass-758-001-20260414.md` |
| Observations log | `wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md` | `wa-dim-c10-observations-v1.0-20260414.md` |
| Per-registry dimension patch | `wa-dim-{cluster}-reg{nnn}-patch-v{n}-{YYYYMMDD}.json` | `wa-dim-c01-reg023-patch-v1-20260414.json` |
| Group description correction patch | `wa-dim-{cluster}-grpdesc-patch-v{n}-{YYYYMMDD}.json` | `wa-dim-c17-grpdesc-patch-v2-20260414.json` |
| Return instruction | `wa-dim-{cluster}-{registry_no}-return-v{n}-{YYYYMMDD}.md` | `wa-dim-c02-213-return-v1-20260414.md` |
| Session log | `wa-dim-{cluster}-session-log-v{n}-{YYYYMMDD}.md` | `wa-dim-c01-session-log-v1-20260414.md` |

**Patch ID patterns:**
- Per-registry dimension patch: `PATCH-{YYYYMMDD}-DIMREVIEW-{CLUSTER}-REG{NNN}-V{n}` — e.g. `PATCH-20260414-DIMREVIEW-C01-REG023-V1`
- Out-of-session group description correction: `PATCH-{YYYYMMDD}-DIMREVIEW-GRPDESC-{scope}-V{n}`

**Observations log versioning:** per GR-OBS-004 (version-increment at named batch boundaries, not per file save within a session). Previous versions remain on disk for audit.

---

*wa-dimensionreview-instruction-v3_3-20260418 | Supersedes wa-dimensionreview-instruction-v3_2-20260417.md | v3_3: GR-REF-002 sweep — governing rules pointer and companion documents migrated to `[current]`; body references to retired-document names updated*

*Historical: WA-DimensionReview-Instruction-v3.2-20260417 | Supersedes wa-dimensionreview-instruction-v3_1-20260414.md | v3.2: single correction to resolve FLAG-002 — observations log versioning aligned to GR-OBS-004 by reference*
