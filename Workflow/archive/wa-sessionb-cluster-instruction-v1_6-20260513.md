# wa-sessionb-cluster-instruction-v1_6-20260513

> Framework B Soul Word Analysis Programme — Session B Cluster Analysis
> Version: v1_6 | Date: 20260513
> Status: **Active — authoritative instruction for Session B cluster analytics**
> **Change note v1_5 → v1_6 (2026-05-13):** §5 Phase 2 (UT verse review) patch type **corrected** from `VCREVISE` to `VCNEW`. Per `wa-patch-instruction [current]` §15.6 rules 5 and 6: VCNEW is inserts-only, VCREVISE is updates-only. UT verses by definition have NO existing `verse_context` row — Phase 2 creates them, which is `insert`, which is VCNEW. The prior v1_5 wording said VCREVISE with "upsert" operations, which is not a supported operation type and produced applicator errors. §5 now specifies the correct patch type, canonical operation shape with field names and JSON structure, and the corrected filename pattern (`patch-vcnew-utreview` not `patch-vcrevise-utreview`). §16 routing table updated. Added §5.4 — split-patch guidance for the rare case where Phase 2 also revises existing VC rows (use legacy `VERSECONTEXT` combined, or two separate patches).
> **Change note v1_4 → v1_5 (2026-05-13):** §4 Phase 1 status-transition simplified. The cluster status transition `Not started` → `Data - In Progress` is now handled **inline** by the comprehensive-report-gen script (`_generate_cluster_comprehensive_v1_*.py`) — no separate directive required. The earlier dir-001 status-init directive ceremony was overhead for a single-row metadata update. The script is idempotent: if status is anything other than `Not started`, no write occurs. A row-level JSON backup is taken when the transition fires. **Knock-on changes:** §7 Phase 4 directive sequence numbers shift down (subgroup-assign was dir-002 → now dir-001; term-rebind was dir-003 → now dir-002) for clusters following the v1_5 flow; clusters initialised under v1_4 retain their existing dir numbering. §17 pre/post controls updated.
> **Change note v1_3 → v1_4 (2026-05-13):** Two refinements. (1) §4 Phase 1 — cluster status transition `Not started` → `Data - In Progress` is now an **explicit required step at session open**, authored as a small status-init directive (dir-001) before any analytical work. Previously hand-wavy ("CC sets via §11 directive if needed"). (2) §11 Phase 8 — the cluster-specific science extract document (`Workflow/Sciences/wa-{cluster_code_lower}-{name}-scienceextract-v{V}-{date}.md`) is now a **mandatory input** for the catalogue pass. The T7 tier prompts cannot be answered substantively without the scientific framing context this document provides. Added to §11 inputs, §14 reports map, and §17 pre/post controls table.
> **Change note v1_2 → v1_3 (2026-05-13):** Major rework based on M05, M06, M15, M26 completed runs. Substantive changes: (1) Phase 6 (VCG reconciliation) **fully rewritten** to enforce read-verses-first → write-meaning → design-fresh-VCGs → reconcile-against-existing sequence — the M15 lesson that existing VCG labels bias the reading if not deliberately set aside. (2) BOUNDARY formalised as a **temporary sub-group** with mandatory exit before cluster closure (Phase 10 step). (3) **Pre-check / Post-check** added to every phase as explicit gates AI must pass. (4) Data sources **consolidated** — phases reference specific sections of the comprehensive and grouped reports rather than introducing new files. (5) New §15 BOUNDARY discipline (single canonical reference). (6) New §17 Pre/post controls table (consolidated view). (7) Vague language tightened; repetition of operating principles pruned (rules in §2 not repeated in every phase).
> Governs: Session B cluster work from session open through Phase 10 closure
> Replaces (on finalisation): wa-sessionb-analysis-readiness, wa-sessionb-analysis-output, wa-dimensionreview-instruction, wa-versecontext-instruction, wa-registry-management-guide
> Governed by: wa-global-general-rules [current]

---

## 1. Document scope

This instruction is the authoritative source for the Session B cluster analysis flow — the analytical phase that takes a cluster dataset (terms + verses + prior groupings) and produces a fully-classified cluster with sub-groups, verse-context groups, anchor verses, and a full catalogue-prompt findings record in the database.

**Remains in force, referenced by this instruction:**

- `wa-directive-instruction [current]` — every cluster-process change to the database goes via a directive
- `wa-patch-instruction [current]` — verse-status patches and any non-cluster-process DB writes
- `wa-claudecode-instruction [current]` — CC's operational responsibilities
- `wa-database-schema [current]` — table reference
- `wa-sessiona-prose-instruction [current]` — Session A prose source
- `wa-sessionc-cluster-overview [current]` — downstream consumer (cluster publication)
- `wa-sessiond-orientation [current]` — cross-cluster synthesis consumer
- Tier catalogue in `Workflow/Tiers/wa-obs-catalogue-tiered-v{N}-{date}.md` — the 189-prompt T0–T7 catalogue, input to Phase 8

---

## 2. Operating principle

The non-negotiable rule, established at session open and applied throughout all phases:

> **Read every verse. Do not sample. Read what they say. Let the structure and analysis emerge from what is found. No assumptions from memory. No jumping to conclusions. Write on discovery.**

These four disciplines are not repeated in every phase below — they apply throughout. Re-read them when any phase reading begins.

### 2.1 Write-on-discovery

Every observation is written at the moment it is made, from the text that produced it. If an observation has not been written before moving to the next verse, it is not written — do not reconstruct observations from memory after the reading is complete. If you find yourself summarising at the end of a reading block rather than recording as you go, stop and go back.

### 2.2 Cross-cluster contamination guard

When working cluster N, prior knowledge from clusters 1 through N-1 must not colour the reading of cluster N's verses. Each cluster's verses are the sole authority for that cluster's findings. A finding that appears in a prior cluster is not evidence that the same finding applies here — it must be re-evidenced from this cluster's verse text. This applies with particular force to prompts where a strong finding emerged in earlier work (e.g. M06's spirit-level silence).

### 2.3 Inherited-structure contamination guard

When working with a cluster's existing structure — sub-group placements inherited from prior phases, verse_context_group rows inherited from contributor registries, anchor verse claims from earlier work — these are **candidate evidence**, not confirmed truth. The pattern that produced the failure in M15's first attempts: AI read the existing VCG labels and shaped its analysis to fit them. The corrective: read the verses first; write what each verse means in its own terms; design groupings from those meanings; only THEN compare to the existing structure and decide what to keep / refine / replace.

This guard is operationalised in Phase 6 (§9).

### 2.4 Fluency is not a quality signal

Output that reads smoothly and is well-structured can still be entirely ungrounded. The test for every Phase 8 response is not "does this sound right?" but "can I name the specific verse or group that evidences this?" If no verse can be named, the response is not evidenced — mark it S (silent) or G (gap) rather than producing plausible-sounding text.

---

## 3. Starting point — session open

Before any analytical work begins, the session opens in full compliance with the Session Startup Rule (`wa-global-rules-startup [current]`):

1. Obslog created with prefix `wa-obslog-{cluster_code}-{description}-v1-{YYYYMMDD}.md` and saved to `Sessions/Session_Clusters/{cluster_code}/`.
2. Obslog version incremented at every transition point — phases, sub-groups, terms.
3. If obslog writing is interrupted or discontinued, the session **must stop**. Recover the missing recordings first.

**Cluster status at session open:** `cluster.status` must be `Not started` or `Data - In Progress`. If `Analysis Completed` or `Published`, a re-open requires explicit researcher direction.

---

## 4. Phase 1 — Comprehension of the dataset

**Purpose:** establish a reading-level understanding of the cluster — what terms, how many verses, what prior structure exists, what evidence has already been recorded.

**Inputs (see §14 for the report-section map):**

- `wa-cluster-{code}-comprehensive-v{N}-{date}.md` — full per-term identity, every verse with status, all prior groups, findings, SD pointers
- `wa-cluster-{code}-detail-v{N}-{date}.md` — compact per-term overview

**Pre-check:**

- The comprehensive report is regenerated from current DB state and reflects today's data.
- Obslog created and writeable.
- The cluster's current status is `Not started` or `Data - In Progress`. Other states require explicit researcher direction (per §3).

### 4.1 Status transition (handled by the report-gen script, no directive required)

When the comprehensive report is generated for a cluster currently at `cluster.status = 'Not started'`, the script (`_generate_cluster_comprehensive_v1_*.py`) **automatically transitions** the status to `Data - In Progress` as part of the same invocation. A row-level JSON backup is taken before the UPDATE.

- The transition is logged to stdout: `status: 'Not started' → 'Data - In Progress' (backup: ...)`.
- Idempotent — if status is anything other than `Not started` (e.g. re-entry mid-session at `Data - In Progress`), no write occurs and stdout reports `status: 'Data - In Progress'  (no transition)`.
- No directive ceremony. AI records the transition in the obslog using the stdout output as the source.

This is the **one documented exception** to the read-only convention for `_generate_*` scripts. The exception is narrow: a single field on a single row, gated by current status, with a backup file.

### 4.2 Process

1. Read §1 (cluster summary) for the description, gloss list, and per-term stats.
2. Read §2 (verses by sub-group, if any prior structure exists) to see the inherited state.
3. Read §3 (per-term comprehensive detail) to register the term universe — gloss, transliteration, root family, related words, verse count per term.
4. Scan §4 (appendix items) — registry-level findings and SD pointers attached to cluster terms.

**Output:**

- Comprehensive report at `Sessions/Session_Clusters/{code}/wa-cluster-{code}-comprehensive-v{N}-{date}.md`.
- `cluster.status = 'Data - In Progress'` (the script handled the transition automatically if needed).
- High-level overview note in the obslog (Phase 1 section): term count, verse count, prior-group count, prior-finding count, prior-SD-pointer count, observations on data shape. Record the status transition (if it fired) using the script's stdout output.

**Post-check:**

- `cluster.status = 'Data - In Progress'`.
- The overview note in the obslog answers all five counts above.
- If the script transitioned status, the obslog records the transition (timestamp + backup path).
- No analytical claims have been made yet — Phase 1 is descriptive only.

**DB writes:** At most one — the inline status transition by the report-gen script, only if status was `Not started`. AI does not author any directive in Phase 1.

**Cluster status at end of Phase 1:** `Data - In Progress`.

---

## 5. Phase 2 — UT verse review

**Purpose:** every verse with status UT (untouched — no `verse_context` row exists for the (verse_record_id, mti_term_id) pair) must be read individually, term-spans noted, classified.

**Inputs (see §14):**

- `wa-cluster-{code}-comprehensive-v{N}-{date}.md` — UT verses are identifiable in §3 (per-term verse status column)

**Pre-check:**

- Phase 1 complete (overview note in obslog).
- UT verse count from §1 of the comprehensive report is recorded in the obslog.

**Process per UT verse:**

1. Read the verse text in full. Note the term-spans recorded at this verse location.
2. Determine the term's actual relevance:
   - **Confirmed relevant** — the verse evidences the term's characteristic.
   - **Borderline** — needs researcher decision; flagged for attention.
   - **Set aside** — the verse uses the term in a sense unrelated to the cluster's characteristic; populate `set_aside_reason`.
3. Record the determination in the obslog with the verse reference, term, and one-line reason.

**Output:**

- Obslog entries per verse (Phase 2 section).
- UT review document: `Sessions/Session_Clusters/{code}/WA-{code}-UT-verse-review-v1-{date}.md` — table form, one row per (verse, term), with proposed status + reason.

**Post-check (before patch authoring):**

- Every UT verse has a recorded determination (count matches pre-check count).
- Every Borderline entry has been raised in the obslog with a proposed resolution.
- Set-asides have a populated `set_aside_reason`.

### 5.1 DB writes — VCNEW patch (corrected v1_6)

Phase 2 uses the standard VC patch path per `wa-patch-instruction [current]` §3, §15.

**Patch type is `VCNEW`, not `VCREVISE`.** Per `wa-patch-instruction` §15.6 rules 5–6: `VCNEW` requires every operation to be `insert`; `VCREVISE` requires every operation to be `update`. UT verses by definition have **no existing `verse_context` row** — Phase 2 creates them, which is `insert`, which is VCNEW. (If Phase 2 also revises pre-existing VC rows — rare — see §5.4.)

**ID resolution.** AI runs an ID-resolver query (or asks CC for a one-shot lookup) mapping each (book, chapter, verse_num, mti_term_id) to its `verse_record_id` before drafting the patch.

**Patch envelope:**

- `_patch_meta.patch_type = "VCNEW"`.
- `_patch_meta.terms_covered = [mti_term_id, ...]` — every Strong's `mti_term_id` whose verses appear in operations.
- `_patch_meta.input_versions = {"<mti_term_id>": <md_version>, ...}` — **a JSON object (dict), not a list**. Keys are stringified mti_term_ids; values are the integer `md_version` from `mti_terms`. Per `wa-patch-instruction` §15.6.4-bis the applicator validates this gate with `.items()` — a list will fail with `'list' object has no attribute 'items'`.
- Filename: `wa-cluster-{code}-patch-vcnew-utreview-v1-{date}.json`.

**Operation shape (canonical — every op uses these exact field names):**

```json
{
  "op_id": "OP-001",
  "table": "verse_context",
  "operation": "insert",
  "record": {
    "verse_record_id": 169917,
    "mti_term_id": 5571,
    "group_id": null,
    "is_anchor": 0,
    "is_relevant": 0,
    "is_related": 0,
    "set_aside_reason": "na.dad rendered 'thrown away' — describes physical discarding/fate of worthless men. No inner-being state named or engaged by the term in this verse."
  }
}
```

Required field names: `op_id`, `table`, `operation`, `record`. Inside `record`: `verse_record_id`, `mti_term_id`, `group_id` (null at Phase 2; Phase 7 assigns), `is_anchor`, `is_relevant`, `is_related`, and the relevance-specific fields below. **Do not use** `op_seq`, `vr_id`, `mti_id`, `action`, `fields`, `reference` — these are not recognised by the applicator and the patch will be rejected with `Unsupported operation:`.

**Per-classification rules:**

| Phase 2 outcome | `is_relevant` | `set_aside_reason` | `group_id` |
|---|---:|---|---|
| **Set aside** | 0 | populated (one-line reason) | `null` |
| **Confirmed relevant** | 1 | omit (or null) | `null` (Phase 7 will assign) |
| **Borderline** | _(do not write — held in obslog only for researcher decision)_ | — | — |

**Validation and apply:**

```bash
# Dry-run first
python scripts/apply_session_patch.py --dry-run "Sessions/Session_Clusters/{code}/wa-cluster-{code}-patch-vcnew-utreview-v1-{date}.json"

# Live
python scripts/apply_session_patch.py "Sessions/Session_Clusters/{code}/wa-cluster-{code}-patch-vcnew-utreview-v1-{date}.json"
```

The applicator validates the envelope (patch_type, terms_covered, input_versions), enforces the input-versions gate (A-03), and routes each operation through the standard verse_context insert path. On success it bumps each touched term's `md_version` and stamps `vc_status` accordingly.

### 5.4 Split-patch guidance (rare case: Phase 2 touches existing VC rows)

If Phase 2 review surfaces verses that already have a `verse_context` row (not strictly UT — e.g. a previously classified row that this review revises), the work splits across two patch types:

- **VCNEW** — for genuine UT verses (no existing row). Operation = `insert`.
- **VCREVISE** — for verses with an existing row that the review revises. Operation = `update`.

Two acceptable patterns:

1. **Two separate patches** — one VCNEW, one VCREVISE. VCNEW applies first (per `wa-patch-instruction` §15 order). Both share the same session/batch reference in `_patch_meta`.
2. **Single legacy `VERSECONTEXT` combined patch** — `patch_type = "VERSECONTEXT"` permits both `insert` and `update` operations in one patch (per `wa-patch-instruction` §15.6 rule 7 / §15.7). Acceptable when the volume is small; not the default.

For pure UT review (the common Phase 2 case — every verse is UT), only the VCNEW patch is produced.

**Cluster status:** unchanged (`Data - In Progress`).

---

## 6. Phase 3 — Characteristic debate from the gloss list

**Purpose:** subdivide the cluster's terms into provisional sub-groups based on distinct characteristics.

### 6.1 The T1 framework definition (apply throughout this phase)

> **A distinct inner-being characteristic has:**
>
> 1. **Identifiable constitutional location** — heart, mind, will, conscience, soul, spirit, or body — where in the inner person it sits.
> 2. **A distinguishable set of inner faculties engaged** — perception, thought, memory, feeling, conscience, will, agency.
> 3. **A recognisable impact** — the characteristic produces a definable effect on the person, on relationships, or on action.
> 4. **A structural opposite** — the characteristic has a named or implicit opposite that defines its contour from the other side.
> 5. **A distinguishing causal direction or directional object** — the characteristic is directed toward, produced by, or operating against something nameable.

A grouping that does not satisfy these criteria is not a characteristic-bearing sub-group; it is either a **BOUNDARY** (supportive / descriptive / qualifying / undecided term — see §15) or a flag for cluster reassignment.

### 6.2 Recognised tension — the onion principle

The inner being is not made of separable bricks neatly assignable to sub-groups. It is made of compounds that morph and change character through the person's inner life. Each analytical layer peels without discarding the whole. Sub-groupings are peels — not divisions.

### 6.3 Inputs (see §14)

The cluster's comprehensive report is the sole input:

- `wa-cluster-{code}-comprehensive-v{N}-{date}.md`:
  - **§1 Cluster summary** — cluster description, full gloss list, per-term stats
  - **§3 Per-term comprehensive detail** — gloss, transliteration, root family, related words per term

Do not introduce additional report files for this phase.

### 6.4 Pre-check

- Phase 1 + Phase 2 complete.
- Comprehensive report has been regenerated post-Phase 2 (UT review reflected in DB).

### 6.5 Process

1. Read all glosses against the T1 characteristic definition.
2. Propose provisional sub-groups, each named by the dominant characteristic it carries.
3. Test each provisional sub-group against the five T1 criteria (§6.1) — explicitly, in the obslog.
4. Identify three categories of terms:
   - **Characteristic-bearing** — assigned to a sub-group (e.g., M06-A Hatred).
   - **Supportive / descriptive / qualifying / undecided** → BOUNDARY (temporary; see §15).
   - **Flagged** — terms requiring further investigation, possibly belonging to a different cluster → flagged sub-group, or proposed cluster reassignment.

### 6.6 Output

- Provisional sub-group list with T1-test rationale per sub-group → obslog (Phase 3 section).
- Characteristic-debate document: `Sessions/Session_Clusters/{code}/WA-{code}-characteristic-debate-v1-{date}.md` — full debate, candidate groupings, rationale.

### 6.7 Post-check

- Every term is assigned to a sub-group, BOUNDARY, or flagged for cluster reassignment — no term is left unclassified.
- Each proposed sub-group has its T1-test result recorded in the obslog.
- The phase's output is explicitly labelled **provisional** — Phase 4's control read will revise it.

**Provisional-by-definition guard:** Phase 3 output is a hypothesis, not a finding. Grouping from glosses alone is inherently incomplete. Do not begin Phase 5 with the assumption that the Phase 3 groupings are correct.

**DB writes:** None.

**Cluster status:** unchanged.

---

## 7. Phase 4 — Control read and the compound-morphing correction

**Purpose:** validate the provisional sub-groups via a bidirectional control read.

### 7.1 Inputs (see §14)

- The provisional sub-group list from Phase 3 (obslog + characteristic-debate document)
- `wa-cluster-{code}-comprehensive-v{N}-{date}.md` §3 (per-term comprehensive detail) — for each term's full meaning text, evidential status, and verse pattern

### 7.2 Pre-check

- Phase 3 complete with characteristic-debate document and obslog entries.
- The T1 criteria (§6.1) are explicitly available for re-application.

### 7.3 Process — bidirectional control

- **Direction 1 — grouping → term:** does each term's actual description fit the proposed group?
- **Direction 2 — term → grouping:** does the term's full description resist the proposed group? Does it suggest a different sub-group, a different cluster, or no cluster at all?

The control read may surface:

- Re-assignment to another sub-group within the cluster.
- Transfer into or out of BOUNDARY.
- Cluster reassignment (term moves to a different M-cluster, T2, or FLAG).
- Additional flags requiring researcher resolution.

**Note:** Phase 4 does not validate existing VCGs (verse_context_group rows from contributor registries). Those are reconciled in Phase 6. Phase 4 is about which **terms** belong in which **sub-groups**.

### 7.4 Open-question discipline

Every question that cannot be resolved by reading alone is recorded in the obslog as **OQ-NNN** with a proposed disposition. The Phase 4 directive is authored only after all OQ items are resolved (researcher confirmation of dispositions makes the scope definite). An unresolved OQ means the directive's scope is not yet known.

### 7.5 Output

- Confirmed sub-group list with any cluster reassignments → obslog (Phase 4 section).
- Issues raised for researcher input, with proposed dispositions.

### 7.6 Post-check

- Every OQ-NNN has a researcher-confirmed disposition.
- Every term that moved between sub-groups (or out of the cluster) has its rationale recorded.
- The post-Phase-4 sub-group list is final for this session's analytical pass.

### 7.7 DB writes — up to two directives

1. **Sub-group assignment directive** — creates `cluster_subgroup` rows, assigns each term's `mti_terms.cluster_subgroup_id`. Per `wa-directive-instruction [current]` §11.4.
   - Filename: `wa-cluster-{code}-dir-001-subgroup-assign-v1-{date}.md` (the first cluster-process directive — earlier dir-001 status-init from v1_4 is retired)
   - Required content (five-element form):
     - **MOTIVATION** — cite the characteristic-debate document and obslog.
     - **SCOPE** — every Strong's listed with its sub-group destination; every cluster_subgroup row to be created with code, label, description.
     - **OUTCOME REQUIRED** — count per sub-group, total terms post-update.
     - **COMPLETION CONFIRMATION** — `SELECT subgroup_code, COUNT(*) FROM mti_terms mt JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id WHERE mt.cluster_code='{code}' GROUP BY subgroup_code` matches expected counts.

2. **Cluster reassignment directive** (if applicable) — moves terms out of the cluster.
   - Filename: `wa-cluster-{code}-dir-002-term-rebind-v1-{date}.md` (or merged into the sub-group directive's Operation B).
   - Per directive §11.6.

**Cluster status transition:** `Data - In Progress` → `Analysis - In Progress` (set as part of directive's outcome).

---

## 8. Phase 5 — First reading pass and 250-word sub-group summaries

**Purpose:** produce a high-level analytical summary per sub-group as context for Phase 6.

### 8.1 Inputs (see §14)

- `wa-cluster-{code}-grouped-v{N}-{date}.md` — regenerated AFTER Phase 4's directive applied. Cluster → sub-group → group → anchor + verses, with per-term lexical context (v2 layout).
- The obslog with Phases 1–4 entries.

### 8.2 Pre-check

- Phase 4 directive applied (verified by COMPLETION CONFIRMATION query in the directive output).
- A fresh grouped report has been regenerated post-Phase-4. **Do not proceed with a stale report.** Per §14 report-regen rule.

### 8.3 Process per sub-group

1. Read every verse currently assigned to the sub-group (across all the sub-group's terms and groups).
2. Produce a 250-word summary describing what the sub-group's verses, taken together, evidence about the characteristic.
3. Record any observations that emerge during summary preparation — these may seed later finding entries.

### 8.4 Output

- One 250-word summary per sub-group → obslog (Phase 5 section).
- Summary document: `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-summaries-v1-{date}.md`.

### 8.5 Post-check

- One summary per sub-group (count matches confirmed sub-group count from Phase 4).
- Each summary names at least two specific verse anchors that exemplify the characteristic.
- BOUNDARY does not receive a 250-word summary — a single line acknowledging the BOUNDARY terms suffices.

**DB writes:** None.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 9. Phase 6 — VCG reconciliation: read first, design fresh, then reconcile

**Purpose:** every non-set-aside verse in the cluster belongs to a `verse_context_group` whose context description is grounded in the actual verse text — and the cluster's final VCG set reflects what the verses say, not what the inherited VCG labels suggested.

**This is the highest-failure-risk phase.** In M15's first attempts, the existing VCGs (inherited from contributor registries) biased the reading: AI shaped its observations to fit the labels rather than reading the verses on their own terms. The corrective is a strict sequencing of work — operationalised below.

### 9.1 Inputs (see §14)

- `wa-cluster-{code}-grouped-v{N}-{date}.md` — verses by sub-group; the existing VCG state.
- The obslog with the Phase 5 summaries.

### 9.2 Pre-check

- Phase 5 complete with one summary per sub-group.
- The grouped report is fresh (post-Phase-4 applied).
- The obslog Phase 6 section is opened.

### 9.3 Process — three-pass, ordered (do not skip or interleave)

**Pass A — Read every verse, write its meaning.** For each sub-group, in turn:

1. Read every non-set-aside verse in the sub-group, including its inherited VCG label and existing context_description **only as background**, not as the answer.
2. Write to the obslog, for each verse: `{verse_reference} | {term} | one-line plain-English meaning of what the verse says about the characteristic in this verse's context`.
3. Do not name or refer to existing VCGs during this pass. Write what the verse means in its own terms.

**Pass A output:** a complete per-verse meaning list in the obslog, one line per verse.

**Pass B — Design VCGs fresh from the meanings.** With Pass A complete:

1. Read the per-verse meaning list (the obslog entries from Pass A).
2. Group verses with substantively similar meaning into provisional VCGs.
3. Name each provisional VCG with a description that captures the shared inner-being phenomenon — written from the verse meanings, not from any existing VCG label.
4. Designate one anchor verse per provisional VCG — the verse that most directly and definitionally evidences the named phenomenon.
5. Identify dual-membership verses — verses that legitimately belong to two distinct VCGs.

**Pass B output:** a fresh VCG design — one section per provisional VCG: provisional code, context description, member verses (with brief per-verse note), anchor, dual-membership notes.

**Pass C — Reconcile against existing VCGs.** Only after Pass B is complete:

1. List the cluster's existing VCGs for this sub-group (from the grouped report).
2. For each existing VCG, decide:
   - **KEEP** — the existing VCG matches a Pass-B-designed VCG exactly; retain.
   - **REFINE** — the existing VCG matches a Pass-B-designed VCG broadly but description needs revision; retain ID, update context_description.
   - **SPLIT** — the existing VCG corresponds to two or more Pass-B-designed VCGs; mark the existing VCG for soft-delete, create new VCGs.
   - **MERGE** — multiple existing VCGs correspond to a single Pass-B-designed VCG; mark all but one for soft-delete, retain one with updated description.
   - **OBSOLETE** — no Pass-B-designed VCG corresponds to this existing VCG; soft-delete (the existing VCG's verses must end up reassigned to a Pass-B VCG or set aside).
3. For each Pass-B-designed VCG with no existing equivalent: **NEW** — create.

**Pass C output:** a reconciliation decision per existing VCG and per Pass-B VCG.

### 9.4 Conglomerate-group split test

If during Pass A or Pass B the verses assigned to an existing VCG contain genuinely distinct inner-being phenomena (different subjects, different directions, different faculty engagements, different consequences), Pass B will produce multiple VCGs from that source — apply SPLIT in Pass C.

The diagnostic for splitting: can the verses be answered uniformly by a single anchor, or do different subsets need different anchors? If different anchors are needed, split.

### 9.5 Output document per sub-group

`Sessions/Session_Clusters/{code}/WA-{code}-{subgroup}-group-verse-mapping-v1-{date}.md`. Structure:

1. **§A — Per-verse meaning list** (Pass A output): every non-set-aside verse with its plain-English meaning.
2. **§B — Pass-B VCG design** (Pass B output): one section per provisional VCG with description, member verses, anchor, dual-memberships.
3. **§C — Reconciliation decisions** (Pass C output): table of every existing VCG with decision (KEEP / REFINE / SPLIT / MERGE / OBSOLETE), and every Pass-B VCG with no existing equivalent (NEW).
4. **§D — Cross-VCG dual assignments** (verses that legitimately belong to two VCGs): table.
5. **§E — Flags-for-CC** (optional): any verses that cannot be classified within the proposed structure.

### 9.6 Post-check (before submitting any directive)

- Every non-set-aside verse in the sub-group has a Pass-A meaning entry.
- Every Pass-A meaning has been used to inform a Pass-B VCG assignment.
- Every Pass-B VCG has at least one anchor verse named.
- Every existing VCG has a Pass-C reconciliation decision.
- Verse counts add up: Pass-B VCG memberships + dual-assignments + set-asides = sub-group total.
- Obslog Phase 6 section contains: the Pass A meanings (per verse), the Pass B VCG design rationale, the Pass C reconciliation decisions.

**DB writes:** None in Phase 6. The mapping documents are the analytical artefact; database application happens in Phase 7.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 10. Phase 7 — Group-verse mapping application

**Purpose:** apply each sub-group's Phase 6 reconciliation decisions to the database.

### 10.1 Inputs

- One group-verse mapping document per sub-group (Phase 6 output).

### 10.2 Pre-check

- Every sub-group has a Phase 6 mapping document with all five sections (§A–§E).
- All §C reconciliation decisions are explicit (no "tbd" or "see Phase 8" entries).

### 10.3 Routing — one directive per sub-group (default)

Each sub-group gets its own cluster-process directive. Reasons:

1. Phase 6 produces one mapping document per sub-group; the directive boundary follows naturally.
2. Failure radius is contained — a problem in M05-C's mapping does not roll back M05-A and M05-B writes.
3. AI can apply incrementally: complete one sub-group end-to-end (mapping → directive → apply → confirmation) before starting the next.
4. The administrative cost of N directives is small.

**Combined directive (single per cluster) — permitted only with explicit researcher direction.**

### 10.4 Directive content

- Filename: `wa-cluster-{code}-dir-{seq}-{subgroup}-mapping-v1-{date}.md`
- Pattern: cluster-process directive per `wa-directive-instruction [current]` §11.4.
- Five-element form:
  - **MOTIVATION** — cite the Phase 6 mapping document and obslog session reference.
  - **SCOPE** — sub-group code, term set, operations:
    - `verse_context_group` UPDATE (REFINE: update context_description, retain ID).
    - `verse_context_group` INSERT (NEW + SPLIT children).
    - `verse_context_group` soft-delete (MERGE non-retained + OBSOLETE).
    - `verse_context` UPSERT — set `group_id`, `cluster_subgroup_id`, `is_anchor`, `is_relevant`; include dual-assignment second rows.
    - Explicit handling of set-asides: "set-asides not re-evaluated unless the mapping explicitly re-includes them".
  - **OUTCOME REQUIRED** — verse-count expectations per VCG post-apply; anchor count per VCG = 1; cross-VCG dual count; set-aside row count unchanged.
  - **COMPLETION CONFIRMATION** — verse-count query per VCG; anchor-count query; dual-assignment query; soft-deleted-VCG count check; set-aside count check; application report saved to `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup}-group-mapping-applied-v1-{date}.md`.

### 10.5 Pre-flight (CC executes before any write)

- Every verse reference in the mapping doc resolves to a `wa_verse_records` row for the named term.
- Every term's mti_term_id is in the cluster and assigned to the named sub-group.
- Every existing group_id targeted for REFINE / MERGE-retain / SPLIT / OBSOLETE matches its declared term context.
- Pass-B verse counts match Pass-A counts (sub-group total reconciled).

**Halt-on-error before any write** — if pre-flight fails, CC reports and waits.

### 10.6 Post-check (per applied directive)

- COMPLETION CONFIRMATION queries in the directive output match the expected values.
- The application report (`WA-{code}-{subgroup}-group-mapping-applied-v1-{date}.md`) is written by CC and reviewed.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 11. Phase 8 — Catalogue pass (per-prompt analytical work)

**Purpose:** apply every prompt in the 189-prompt T0–T7 catalogue to each sub-group, producing one finding per (prompt × sub-group), plus cluster-level synthesis findings where the prompt's evidence cuts across sub-groups.

### 11.1 Inputs (see §14)

- `wa-cluster-{code}-grouped-v{N}-{date}.md` — latest, reflecting Phase 7 writes.
- `Workflow/Tiers/wa-obs-catalogue-tiered-v{N}-{date}.md` — the full 189-prompt catalogue. Refresh via `python scripts/build_obs_catalogue_tiered_extract.py` if a newer catalogue version has been seeded.
- **`Workflow/Sciences/wa-{cluster_code_lower}-{name}-scienceextract-v{V}-{date}.md`** — the cluster's science extract. Mandatory input. Researcher-prepared (one per cluster, indexed by cluster code). Example for M20: `Workflow/Sciences/wa-m20-doubt-scienceextract-v1_0-20260513.md`. **Rationale:** the T7 tier prompts ask what physical and clinical sciences observe about the inner capacities corresponding to the cluster's characteristics. Without the science extract in context, T7 responses default to thin general-knowledge claims or to S (silent). The extract provides the scientific framing AI weaves into T7 responses while keeping the analytical record grounded.
- The obslog through Phase 7.

### 11.2 Pre-check

- Phase 7 directives applied for every sub-group (verified by each directive's COMPLETION CONFIRMATION).
- The grouped report is fresh (post-Phase-7).
- The tiered catalogue is the current `catalogue_version` (verified against `wa_obs_question_catalogue`).
- **The cluster's science extract exists at `Workflow/Sciences/wa-{cluster_code_lower}-...-scienceextract-v{V}-{date}.md` and has been loaded into AI's context.** If the extract is missing for the cluster, Phase 8 cannot begin — escalate to researcher for the extract to be prepared.

### 11.3 Governing principle (applied throughout all passes)

> The focus is on describing the intricacies of the characteristic(s), rather than answering a theoretical question. Keep it grounded.

### 11.4 Outcome codes

Every response carries one outcome code:

- **E (Evidenced)** — the verse evidence in this sub-group's VCGs directly addresses the prompt. Must name at least one specific verse or VCG.
- **S (Silent)** — the verse evidence does not address this prompt for this sub-group. A consistent pattern of silence across sub-groups is a cluster-level finding (record once at the cluster level, not N times at sub-group level).
- **G (Gap)** — the question should be answerable but the data needed is not yet available. G is not S: S means the verses are silent; G means data may exist but has not been retrieved.

### 11.5 Discipline

- Every E-coded response anchored to a named verse or VCG.
- No theoretical elaboration beyond what the text shows.
- Silence recorded as silence, not glossed over.
- Each sub-group must have a complete answer for each catalogue prompt before the next sub-group begins.
- All observations rooted in the cluster's data — not memory, not training, not extraneous knowledge, not prior cluster findings.
- The style of the answer must allow Session C to articulate the analysis with only the findings as input.

### 11.6 BOUNDARY treatment in Phase 8

BOUNDARY terms do **not** receive the full 189-prompt catalogue pass. Produce one structural characterisation note per BOUNDARY term: what role does this term play in the cluster economy? (Delivery mechanism? Quality marker? Behavioural expression? Undecided?) Record under T1.2.1. If the characterisation reveals a term should be promoted to a full sub-group, **flag for researcher decision** — do not promote unilaterally. See §15 for BOUNDARY discipline including the Phase 10 exit gate.

### 11.7 Sub-group completion gate

Before moving from one sub-group to the next, confirm:

- All 189 prompts have an E, S, or G marker for the completed sub-group.
- No prompt left blank.
- No E response left without a verse citation.
- Phase 8 self-check (§17) passed for this sub-group.

Do not continue elaborating within a completed sub-group — move on.

### 11.8 Output style (verbatim into the obslog)

```text
**T{tier}.{component}.{seq}** — {prompt text}

**[A — Hatred]** {finding text — verbatim, with verse anchors}

**[B — Contempt]** {finding text}

…

**[CLUSTER]** {cluster-level synthesis where applicable}
```

Markers (recognised by the Phase 9 loader script):

- `**[X]**` or `**[X — Label]**` → finding for that sub-group
- `**[A, B, C]**` → finding shared across listed sub-groups
- `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` → cluster-level synthesis
- `**S — [scope]**` → silent for that scope
- `**G — [scope]**` or `**G**` → gap

### 11.9 Output document

Consolidated findings, structured into parts by tier:

- `Sessions/Session_Clusters/{code}/WA-{code}-consolidated-findings-v1-{date}-part1.md` (T0–T1)
- `…-part2-T2.md`, `…-part3-T3-T4.md`, `…-part4-T5-T7.md`

### 11.10 Post-check (per sub-group, before moving on)

- 189 prompts answered with E/S/G.
- Every E names at least one specific verse or VCG.
- Consistent cross-sub-group silences will be aggregated as cluster-level findings in Phase 9.
- BOUNDARY has structural characterisation notes (not full pass).

**DB writes:** None in Phase 8.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 12. Phase 9 — Findings recording (validation + DB write)

**Purpose:** validate that every prompt has been applied to every sub-group with grounded evidence, then record findings in `cluster_finding`.

### 12.1 Inputs

- The four parts of the consolidated findings document (Phase 8 output).
- The obslog through Phase 8.
- Any prior session findings (`wa_session_research_flags` rows) attached to terms in this cluster — see §12.5 for handling.

### 12.2 Pre-check

- All four consolidated findings parts exist and are version-aligned to the same Phase 8 pass.
- Every sub-group's 189 prompts have responses.
- BOUNDARY characterisations are present.

### 12.3 Cross-sub-group review pass

After all sub-group passes are complete, read across the full set of findings before producing the directive. Look for:

- **Cluster-level patterns** — findings that appear in the same form across all or most sub-groups → record once as `[CLUSTER]` at the relevant prompt.
- **Structural relationships between sub-groups** — causal sequences, constitutive relationships, or structural asymmetries visible only across sub-groups.
- **Absences significant in totality** — a prompt silent across all sub-groups is a cluster-level finding.
- **Internal contradictions** — resolve by returning to the verse evidence before the directive is produced.

Findings surfaced are added to the consolidated findings document at their relevant prompt location.

### 12.4 Consolidated findings document — self-contained requirement

The document (parts 1–4) must be readable without reference to any other file:

- Every prompt answered with full text per sub-group — not structural labels or cross-references.
- Every E response includes the specific verse reference(s) in the body of the response text.
- A Session C reader should be able to write the cluster publication using only these four parts.

### 12.5 Legacy `wa_session_research_flags`

The registry-era Q&A findings system (`wa_session_research_flags` rows with `flag_code` in `PH2_*`, `SB_FINDING`, `SB_DIMENSION`, `SD_POINTER`, etc.) **remains in place**. It is not deprecated, not retired, not migrated.

**Why both exist:**

- `wa_session_research_flags` is **registry-scope**: each row anchored to a specific word's analytical session.
- `cluster_finding` is **cluster + sub-group + catalogue-prompt scope**.
- Neither subsumes the other.

**Hard rules during Session B cluster work:**

- ❌ Do not modify any `wa_session_research_flags` row.
- ❌ Do not insert new `wa_session_research_flags` rows.
- ❌ Do not retire / soft-delete registry findings.
- ✓ Do read them as context.
- ✓ Do cite them by id in cluster findings where they materially support a cluster claim (paraphrase, not copy).

### 12.6 Validation step (before the directive is produced)

- Every prompt × sub-group cell has E, S, or G with grounded evidence.
- All cross-sub-group review findings are reflected in the consolidated document.
- Open questions from prior sessions still relevant have been validated or noted.

**Do not rerun the entire analysis** to prepare the directive — the directive is built from the obslog + updated consolidated findings.

### 12.7 DB writes — one directive per cluster

- Filename: `wa-cluster-{code}-dir-{seq}-findings-record-v1-{date}.md`
- Pattern: cluster-process directive per `wa-directive-instruction [current]` §11.5.
- Required content:
  - **MOTIVATION** — cite the consolidated findings document, the obslog session, the catalogue version.
  - **SCOPE** — table `cluster_finding`; cluster_code; source files (the four parts); operation: UPSERT one row per (prompt × scope), parsing `**T#.#.#**` headers and scope markers.
  - **OUTCOME REQUIRED** — one row per source-document marker; `finding_status` per marker type (E→`finding`, S→`silent`, G→`gap`, CLUSTER→`cluster_synthesis`); `finding_text` set to verbatim prose; `source_file` set to part-N filename.
  - **COMPLETION CONFIRMATION** — row counts by status; 3-row sample; gap list; confirmation that `wa_session_b_findings` row count is unchanged for this cluster's terms.

**Two-step load is acceptable:**

1. Structural loader — creates one row per (189 prompts × N sub-groups + 189 cluster-level rows) with status defaults.
2. Full-text loader — parses the consolidated findings document and updates `finding_text` + `finding_status` for every authored marker.

### 12.8 Post-check

- `cluster_finding` row counts match expected (per directive COMPLETION CONFIRMATION).
- `wa_session_b_findings` row count for this cluster's terms is unchanged.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 13. Phase 10 — Verification, BOUNDARY exit, completion

**Purpose:** verify the database state matches the analysis, resolve gaps, exit BOUNDARY, close the cluster.

### 13.1 Inputs

- The post-Phase-9 `cluster_finding` rows.
- A verification report (CC produces; AI reviews).
- The Phase 6 mapping documents (for BOUNDARY review).

### 13.2 Pre-check

- Phase 9 directive applied (verified by COMPLETION CONFIRMATION).
- Cluster has BOUNDARY (if applicable) with its terms recorded.

### 13.3 Step 1 — CC verification

CC runs verification and produces `outputs/markdown/{code}_findings_verification_{date}.txt`:

- Anchor verse claims — every VCG's named anchor exists as a `verse_context` row with `is_anchor=1`.
- NT verse availability — every NT verse cited in the findings exists in `wa_verse_records` for the cited Strong's.
- VCG code references — every `group_code` cited in the findings exists with the expected `mti_term_id`.
- Coverage summary — counts per status per scope; expected vs actual.
- Validation pass per `_validate_cluster_completion_v1_*.py` — VC-coverage gaps (C1) and stale vc_status (C2).

CC raises flags for mismatches.

### 13.4 Step 2 — AI response

For each flag, AI authors `Sessions/Session_Clusters/{code}/WA-{code}-verification-response-v1-{date}.md`:

- What the verification confirmed.
- What the verification did not check.
- Each flag's analysis and required action (DB repair, analytical correction, or "no change — verification artefact").

### 13.5 Step 3 — Gap resolution

Gap rows (`finding_status='gap'`) reviewed:

- Gaps resolvable by DB query — CC runs queries; AI updates gap rows to `finding` status with resolved text.
- Gaps requiring external data — remain as `gap` with explanatory text marking the dependency.

### 13.6 Step 4 — BOUNDARY exit (mandatory before closure)

Per §15, BOUNDARY is a temporary sub-group. Before closure, every BOUNDARY term must exit via one of:

- **Set-aside** — the term's cluster-context verses are set aside (`verse_context.set_aside_reason` populated); the term is detached from BOUNDARY.
- **Promotion to a real sub-group** — the term is moved to a characteristic-bearing sub-group; its verses are reassigned to a VCG in that sub-group via a small reconciliation directive.
- **Cluster reassignment** — the term is moved out of the cluster (rare at this stage; requires researcher decision).
- **Flagged** — the term cannot be resolved by reading alone; flagged with explicit pending-decision note. **Flagged-for-decision is a legitimate exit state** for cases where the researcher will revisit, but it must be explicitly recorded — BOUNDARY does not silently persist as a holding pen.

**Post-BOUNDARY-exit check:** BOUNDARY contains zero terms, OR every remaining BOUNDARY term has an explicit flagged-for-decision record in the obslog with a proposed disposition.

### 13.7 Step 5 — Final corrections directive

- Filename: `wa-cluster-{code}-dir-{seq}-verification-corrections-v1-{date}.md`
- Pattern: per `wa-directive-instruction [current]` §11.5/§11.6.
- Required content:
  - **MOTIVATION** — cite verification report, AI's verification-response, BOUNDARY exit decisions.
  - **SCOPE** — list of (prompt × scope) cells to update, anchor flags to repair, BOUNDARY term moves, vc_status sync (per `_validate_cluster_completion_v1_*.py` C2 backfill).
  - **OUTCOME REQUIRED** — exact post-state per cell.
  - **COMPLETION CONFIRMATION** — final remaining-gap count, BOUNDARY exit state, cluster-level findings count, vc_status sync confirmation.

### 13.8 Step 6 — Validation re-run

After the corrections directive applies, re-run `_validate_cluster_completion_v1_*.py --cluster {code}`:

- C1 (VC-coverage gaps) must be 0, OR every gap term has a documented analytical exit.
- C2 (stale vc_status) must be 0.

### 13.9 Step 7 — Cluster closure

After CC confirms the corrections directive and the validation re-run is clean:

- AI authors a one-line directive (or includes the status update in the corrections directive's Outcome): `UPDATE cluster SET status='Analysis Completed', last_updated_date=? WHERE cluster_code=?`.
- Researcher confirms before the status flip.

**Cluster status transition:** `Analysis - In Progress` → `Analysis Completed`.

### 13.10 Post-check

- `cluster.status = 'Analysis Completed'`.
- Validation script reports clean.
- BOUNDARY is empty or fully flagged.
- All Session C downstream consumers can read the cluster (per `wa-sessionc-cluster-overview [current]`).

The cluster is now ready for Session C cluster publication.

---

## 14. Reports — input/output map (consolidated)

The cluster reports produced by analytics scripts in `scripts/`. All read-only, all re-runnable. Naming convention `wa-cluster-{code}-{kind}-v{N}-{date}.md`; version auto-bumps per script's `next_version` helper.

| Report | Script | Used in phases | Sections referenced |
|---|---|---|---|
| Cluster overview | `_generate_cluster_overview_v1_*.py` | (programme-wide) | (programme reference, not a cluster input) |
| Per-cluster detail | `_generate_cluster_term_report_v1_*.py` | 1 | Compact per-term sheet |
| Comprehensive cluster | `_generate_cluster_comprehensive_v1_*.py` | 1, 2, 3, 4 | §1 cluster summary (gloss list) · §2 verses by sub-group (inherited state) · §3 per-term comprehensive detail (gloss, root family, related words) · §4 appendix items |
| Grouped cluster (v2) | `_generate_cluster_grouped_v1_*.py` | 5, 6, 8 | Cluster → sub-group → VCG → anchor + verses; v2 adds sub-group stats and per-term lexical context |
| Findings | `_generate_cluster_findings_report_v1_*.py` | 9, 10 | One section per sub-group, organised tier → component → prompt |
| Tiered prompts catalogue | `build_obs_catalogue_tiered_extract.py` | 8 | 189 prompts T0–T7 |
| **Cluster science extract** | _(researcher-prepared, no generator script)_ | **8** | Per-cluster science extract at `Workflow/Sciences/wa-{cluster_code_lower}-{name}-scienceextract-v{V}-{date}.md`. Provides scientific framing (human / clinical sciences) for the T7 catalogue prompts. **Mandatory input** for Phase 8 — see §11.1 / §11.2. One per cluster. |

**Report regen rule:** at the start of each phase that consumes a report, regenerate the report from the current DB state. Reports are snapshots — stale reports invite reasoning on outdated assumptions. The cluster science extract is researcher-prepared rather than DB-derived; it does not need regeneration per phase, but if the researcher updates it mid-session (e.g. v1_1) the latest version is the one Phase 8 consumes.

---

## 15. BOUNDARY discipline (canonical reference)

BOUNDARY is **a temporary sub-group** used during Phases 3–9 for terms that:

- Are supportive / descriptive / qualifying — they enhance the cluster's verse evidence without themselves carrying a distinct inner-being characteristic.
- Are undecided — the analytical pass has not yet determined whether they belong to a characteristic-bearing sub-group, should be set aside, or should be moved out of the cluster.

### 15.1 Lifecycle

| Phase | BOUNDARY state |
|---|---|
| 3 | Terms enter BOUNDARY (provisional) |
| 4 | Control read may move terms in or out of BOUNDARY |
| 5 | BOUNDARY does not receive a 250-word summary (one line acknowledging its terms suffices) |
| 6 | BOUNDARY's verses receive a Pass-A meaning entry and Pass-C reconciliation; BOUNDARY may have its own VCGs (typically minimal — single VCG aggregating supportive material) |
| 7 | BOUNDARY's VCGs applied like any other sub-group |
| 8 | BOUNDARY terms receive structural characterisation notes (not the full 189-prompt pass) |
| 9 | BOUNDARY characterisations recorded as `cluster_finding` rows under T1.2.1 |
| 10 | **BOUNDARY exit gate (mandatory):** every BOUNDARY term resolved per §13.6 |

### 15.2 At cluster closure (Phase 10)

BOUNDARY does **not** persist as a holding pen. Every BOUNDARY term must exit via one of:

1. **Set-aside** — verses marked `set_aside_reason`; term detached from BOUNDARY.
2. **Promotion** — term moved to a characteristic-bearing sub-group; verses reassigned to a VCG in that sub-group.
3. **Cluster reassignment** — term moved out of the cluster.
4. **Flagged-for-decision** — explicit pending-decision record in obslog with proposed disposition (legitimate exit state for researcher follow-up; **not** an indefinite hold).

The Phase 10 corrections directive includes the BOUNDARY exit actions in its scope. The cluster cannot move to `Analysis Completed` while BOUNDARY contains unresolved terms.

---

## 16. Patches and directives — content checklist

This instruction never authorises CC to write to the database directly. Every DB change is mediated by a patch (`wa-patch-instruction [current]`) or a directive (`wa-directive-instruction [current]`).

**Routing for cluster work:**

| Operation | Method | Reason |
|---|---|---|
| Verse status update (UT → confirmed/set-aside) — first-time inserts on `verse_context` | **Patch (VCNEW)** | Standard VC-family path; AI runs an ID-resolver query before authoring (see §5). VCNEW is `insert`-only per `wa-patch-instruction` §15.6 rule 5. |
| Verse status update — revision of existing `verse_context` rows | Patch (VCREVISE) or legacy VERSECONTEXT | VCREVISE is `update`-only per `wa-patch-instruction` §15.6 rule 6. Rare in Phase 2; see §5.4. |
| `cluster_subgroup` create + `mti_terms.cluster_subgroup_id` assign | Directive (§11.4) | Cluster-process — schema relationships span tables |
| Cluster reassignment (term moves between clusters) | Directive (§11.6) | Requires cleanup of orphan sub-group references |
| VCG mapping apply (`verse_context_group` UPDATE/INSERT/soft-delete + `verse_context` UPSERT) | Directive (§11.4) | Source is structured markdown the parser must interpret |
| Cluster findings recording (`cluster_finding`) | Directive (§11.5) | Two-step structural+full-text load via parser |
| Schema enablement for cluster tables | Directive (§10) | DDL — applicator does not do DDL |
| Verse-context status corrections at scale (registry-style) | Patch (VERSECONTEXT family) | Field names and IDs known in advance |
| Word-registry / mti_terms metadata corrections | Patch | Standard data-write |

**Common directive requirements (per `wa-directive-instruction [current]` §3 + §11.3):**

1. **DIRECTIVE ID** in format `DIR-YYYYMMDD-NNN`
2. **MOTIVATION** — cite source document(s), obslog session reference, analytical pass that produced the artefact
3. **SCOPE** — cluster_code; sub-group code; tables touched; selection criteria; explicit set-aside handling
4. **OUTCOME REQUIRED** — exact row counts, status distribution, untouched-table check
5. **COMPLETION CONFIRMATION** — queries CC runs + expected results

**Filename:** `wa-cluster-{code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md`. Sequence numbers reset per cluster.

**Directive companion files per phase:**

| Phase | Directive suffix | Companion |
|---|---|---|
| 2 | _(patch — VCNEW; VCREVISE only if revising existing rows — see §5.4)_ | `WA-{code}-UT-verse-review-v1-{date}.md` |
| 4 | `subgroup-assign` (+ optional `term-rebind`) | `WA-{code}-characteristic-debate-v1-{date}.md` |
| 7 | `{subgroup}-mapping` | `WA-{code}-{subgroup}-group-verse-mapping-v1-{date}.md` (Phase 6 output) |
| 9 | `findings-record` | `WA-{code}-consolidated-findings-v1-{date}-part{N}.md` (×4) |
| 10 | `verification-corrections` | `WA-{code}-verification-response-v1-{date}.md` |

---

## 17. Pre/post controls — consolidated table

| Phase | Pre-check | Post-check |
|---|---|---|
| **1 Comprehension** | Comprehensive report regenerated; obslog created; cluster status is `Not started` or `Data - In Progress` | Status transition handled inline by the report-gen script (if status was `Not started`); `cluster.status='Data - In Progress'`; overview note answers all five count metrics; if transition fired, obslog records timestamp + backup path |
| **2 UT review** | UT count from §1 recorded | Every UT verse has a determination; set-asides have a reason; counts match |
| **3 Characteristic debate** | Phases 1+2 complete; comprehensive report fresh post-Phase-2 | Every term is in a sub-group, BOUNDARY, or flagged; each sub-group passed the five T1 tests; output explicitly labelled provisional |
| **4 Control read** | Phase 3 complete; T1 criteria available | Every OQ-NNN has researcher disposition; term movements have rationale; sub-group list final for this session |
| **5 Summaries** | Phase 4 directive applied; grouped report fresh post-Phase-4 | One summary per sub-group; each names ≥2 anchor verses; BOUNDARY acknowledged but not summarised |
| **6 VCG reconciliation** | Phase 5 complete; grouped report fresh | Every non-set-aside verse has Pass-A meaning entry; every Pass-B VCG has an anchor; every existing VCG has Pass-C decision; verse counts reconcile |
| **7 Mapping apply** | Every sub-group has Phase 6 mapping document with all five sections; all §C decisions explicit | COMPLETION CONFIRMATION queries match expected; application report written |
| **8 Catalogue pass** | Phase 7 directives applied; grouped report fresh post-Phase-7; catalogue is current version; **cluster science extract exists and is loaded in AI context** | Per sub-group: 189 prompts answered with E/S/G; every E names a verse; BOUNDARY has structural characterisation; T7 responses draw on the science extract where applicable |
| **9 Findings recording** | All four consolidated parts version-aligned; cross-sub-group review complete | `cluster_finding` row counts match expected; `wa_session_b_findings` unchanged |
| **10 Verification + closure** | Phase 9 applied; BOUNDARY terms identified | Validation re-run clean (C1=0, C2=0); BOUNDARY exited; `cluster.status='Analysis Completed'` |

**A failed pre-check stops the phase.** A failed post-check stops the phase from being handed off.

**Silence-as-finding rule** (applies across Phase 8/9): a consistent pattern of S across all or most sub-groups for a given prompt is a positive finding about the cluster's character — record once as a cluster-level finding, not N times at sub-group level.

---

## 18. Status discipline

Per the Session Startup Rule and `wa-claudecode-instruction [current]`, AI never tells CC the cluster is "complete" — completion is set by the researcher, on review of CC's confirmation outputs. AI's role is to deliver a directive whose Completion Confirmation queries demonstrate the outcome required.

CC's role is to execute the directive faithfully and return the confirmation. CC does not extend scope, interpret ambiguity, or apply analytical judgement (per `wa-directive-instruction [current]` §8.4).

---

## 19. Change history

**v1_6 (2026-05-13) — Active.** §5 Phase 2 patch type corrected from VCREVISE to VCNEW (UT verses are first-time inserts; VCREVISE is update-only per `wa-patch-instruction §15.6` rules 5–6). Added canonical operation JSON shape with exact field names (`op_id`, `table`, `operation: "insert"`, `record` with `verse_record_id`, `mti_term_id`, `group_id`, etc.) — the prior wording said "upsert" with `fields`, which is not a recognised operation. Added §5.4 split-patch guidance for the rare case where Phase 2 also revises existing rows. §16 patch-routing table updated. M20 first-run revealed the issue.

**v1_5 (2026-05-13) — Superseded by v1_6.** §4 Phase 1 status-transition simplified. Removed the dir-001 status-init directive ceremony introduced in v1_4. The comprehensive-report-gen script now handles the `Not started` → `Data - In Progress` transition inline, with a row-level JSON backup. Idempotent. §7 directive sequence renumbered for clusters following the v1_5 flow (subgroup-assign now dir-001; term-rebind now dir-002). Clusters initialised under v1_4 retain their existing dir numbering — no retrospective renaming.

**v1_4 (2026-05-13) — Superseded by v1_5.** Two refinements: (1) §4 Phase 1 — cluster status transition `Not started` → `Data - In Progress` is now an explicit required step at session open, authored as `dir-001-status-init` before any analytical work. Previously hand-wavy. (2) §11 Phase 8 — per-cluster science extract document (`Workflow/Sciences/wa-{cluster_code_lower}-{name}-scienceextract-v{V}-{date}.md`) is a mandatory input for the catalogue pass; T7 prompts cannot be answered substantively without the scientific framing context. Added to §11.1 inputs, §11.2 pre-check, §14 reports map, and §17 pre/post controls table.

**v1_3 (2026-05-13) — Superseded by v1_4.** Major rework based on M05/M06/M15/M26 completed runs. Phase 6 (VCG reconciliation) rewritten with explicit three-pass sequence (read verses → write meanings → design fresh → reconcile against existing). BOUNDARY formalised as temporary with mandatory Phase 10 exit (new §15). Pre-check / Post-check added to every phase. New §17 consolidated pre/post controls table. Data sources consolidated — phases reference sections of the comprehensive and grouped reports; no new files introduced. Operating principles moved entirely to §2 (no repetition in phase sections).

**v1_2 (2026-05-13) — Superseded by v1_3.** Removed `wa-cluster-overview` from Phase 1 inputs; T1 framework definition pulled out as visible callout in §6; Phase 3 inputs reframed to reference comprehensive-report sections; status changed from DRAFT to Active.

**v1_1 (2026-05-07) — Superseded.** Additions and clarifications derived from the M06 first-run. No existing content removed.

**v1_0 (2026-05-07) — DRAFT, superseded.** First issue. Three of five open items resolved on issue: Phase 7 default per-sub-group directive; Phase 2 VCREVISE patch; legacy `wa_session_research_flags` retained as appendix-tier.

---

*wa-sessionb-cluster-instruction-v1_6-20260513 | Active — authoritative instruction for Session B cluster analytics*
*Replaces (on finalisation): wa-sessionb-analysis-readiness, wa-sessionb-analysis-output, wa-dimensionreview-instruction, wa-versecontext-instruction, wa-registry-management-guide*
*Cross-references: wa-directive-instruction [current] §11 (cluster-process directives); wa-patch-instruction [current] §3, §15; wa-sessionc-cluster-overview [current] (downstream Session C cluster publication)*
