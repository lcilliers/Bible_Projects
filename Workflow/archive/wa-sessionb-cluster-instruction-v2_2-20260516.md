# wa-sessionb-cluster-instruction-v2_2-20260516

> Framework B Soul Word Analysis Programme — Session B Cluster Analysis
> Version: v2_2 | Date: 20260516
> Status: **Active — authoritative instruction for Session B cluster analytics**
> Governs: Session B cluster work from session open through cluster closure
> Supersedes: wa-sessionb-cluster-instruction-v2_1-20260516 (archived to `Workflow/archive/`)
> Governed by: wa-global-general-rules [current]
>
> **Change note v2_1 → v2_2 (2026-05-16):** Phase 11 enhancements driven by M01 Phase 9 output. (1) VCG-level scope for `cluster_finding` rows — AI's Phase 9 output for M01 used 38 non-canonical scope markers like `[E-VCG-02]` and `[E-VCG-01/03/04/05]` when a finding applied to specific VCGs within a sub-group rather than the whole sub-group. Schema migration M48 adds a nullable `vcg_scope` column to `cluster_finding` and extends the UNIQUE constraint to include it. The loader stores VCG specificity as queryable structure rather than dissolving it into text (§14.4). (2) Phase 11 fold operation — for `wa_session_b_findings` rows marked `RESOLVED-BY-CATALOGUE` in Phase 10 (where the inherited finding's content is captured by one or more Phase 9 Tier findings), the loader appends the inherited observation's text to each named cluster_finding row's `finding_text` with audit prefix (§14.5). This implements the user's "ensure observation meaning is incorporated in the Tier findings" requirement. (3) New `validated_cluster_observation` status value for Session B findings that are M01-relevant but don't match any Tier question — a future-cluster placeholder; not exercised by M01. (4) Phase 12 closure §15 expanded with per-VCG anchor and prompt-coverage checks.
>
> **Change note v2_0 → v2_1 (2026-05-16):** Cluster-centric Phase 10 disposition catalogue. Triggered by M01's Phase 10 output: 20 of 24 inherited findings were placed in `CARRY-TO-SESSION-D`, but on review 16 actually belonged to **another cluster's Session B / Phase 9** (the source registry's eventual M-cluster), not Session D. v2_0's catalogue conflated "belongs to another cluster" with "truly cross-cluster phenomenon" because it carried the legacy "cross-registry" framing — a leftover from the pre-cluster pivot. v2_1 splits these into two dispositions (`ROUTE-TO-CLUSTER` and a reframed `CARRY-TO-SESSION-D`) and adds an explicit decision tree (§13.2.1). Session D strict criterion: programme-wide patterns spanning ≥3 clusters, or methodological observations no single cluster's T6 prompts can capture — i.e. "few and very specific." Bilateral cluster relationships are handled by the target cluster's T6 prompts inside Phase 9, not by Session D. Op A status mapping in §13.4 extended with `routed_cluster`.
>
> **Change note v1_13 → v2_0 (2026-05-15):** Major restructure of the cluster analytical flow. The trigger was M01's three Phase 6 restarts: AI repeatedly re-anchored on inherited VCG headings rather than reading verses fresh, even after explicit corrections. The structural fix replaces the prior "read-design-reconcile" three-pass model (which kept inherited VCGs visible throughout) with a hard separation between the per-verse meaning record (atomic, JSON-template, API-driven, persisted to `verse_context.analysis_note`) and the new-VCG design (clusters meanings, never sees old VCGs). Phase numbering expands from 10 to 12 phases with explicit CC-vs-AI ownership per phase. Pass C reconciliation removed entirely — old VCGs are dissolved by CC as a separate phase with a researcher comparison report, no AI involvement in the dissolution. The constitution debate (term-level inclusion/transfer/BOUNDARY decisions) moves AFTER the meaning record, so the constitution debate is grounded in verse evidence not gloss-list inference. A new Phase 10 reconciles inherited Session B findings, SD pointers, and research flags against the new catalogue findings before closure. JSON-template input replaces free-form obslog writing for atomic per-row work (UT review, Pass A meanings). Old phases 5/6/7/8/9/10 are renumbered and partially redesigned; old §2.3 inherited-structure guard remains relevant but is now structurally enforced by the new phase sequencing.
>
> Full history: see §22.

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
- Tier catalogue in `Workflow/Tiers/wa-obs-catalogue-tiered-v{N}-{date}.md` — the 189-prompt T0–T7 catalogue, input to Phase 9

---

## 2. Operating principle

The non-negotiable rule, established at session open and applied throughout all phases:

> **Read every verse. Do not sample. Read what they say. Let the structure and analysis emerge from what is found. No assumptions from memory. No jumping to conclusions. Write on discovery.**

These four disciplines are not repeated in every phase below — they apply throughout. Re-read them when any phase reading begins.

### 2.1 Write-on-discovery

Every observation is written at the moment it is made, from the text that produced it. If an observation has not been written before moving to the next verse, it is not written — do not reconstruct observations from memory after the reading is complete. If you find yourself summarising at the end of a reading block rather than recording as you go, stop and go back.

### 2.2 Cross-cluster contamination guard

When working cluster N, prior knowledge from clusters 1 through N-1 must not colour the reading of cluster N's verses. Each cluster's verses are the sole authority for that cluster's findings. A finding that appears in a prior cluster is not evidence that the same finding applies here — it must be re-evidenced from this cluster's verse text.

### 2.3 Inherited-structure contamination guard

When working with a cluster's existing structure — VCG rows inherited from contributor registries, anchor verse claims from earlier work, prior session findings — these are **candidate evidence**, not confirmed truth. The pattern that produced repeated failures in M15 and M01: AI read the existing VCG labels and shaped its analysis to fit them.

**v2_0 operationalises this guard structurally**, not as a discipline reminder:

- Pass A meaning record (Phase 2) runs against verses with **no group/VCG/sub-group information visible to AI**.
- Constitution debate (Phase 3) runs against a **redesigned report** that exposes per-term meaning corpora, not inherited groupings.
- Sub-group formation (Phase 5) clusters meanings; inherited sub-groups are not shown.
- VCG design (Phase 7) clusters within sub-group meaning corpora; inherited VCGs are not shown.
- Dissolution of old VCGs (Phase 8) is a CC mechanical operation; AI is not asked to compare old-vs-new.

The guard is no longer "AI must remember not to look at inherited structure" — it is "AI never sees inherited structure during analytical work." Where AI references inherited findings (Phase 10 reconciliation), the comparison is explicit and bounded, not an ambient temptation.

### 2.4 Fluency is not a quality signal

Output that reads smoothly and is well-structured can still be entirely ungrounded. The test for every Phase 9 response is not "does this sound right?" but "can I name the specific verse or group that evidences this?" If no verse can be named, the response is not evidenced — mark it S (silent) or G (gap) rather than producing plausible-sounding text.

### 2.5 Directive packaging discipline

Every directive bundles its phase's full set of operations when packaging is feasible. CC processes the bundled operations in succession under a single transaction.

**Default: package.** If the operations belong to the same phase and act on the same cluster, the default is one directive carrying all of them.

**Splitting requires a stated reason.** The only legitimate reason to split is **failure-radius isolation** — a problem in one sub-group's mapping should not roll back another sub-group's work. The directive's MOTIVATION must state the isolation reason when a split is chosen.

**Forbidden patterns** (anti-patterns observed in earlier runs):

- Standalone "ceremony" directives — a directive whose sole operation is a single-field write (e.g. a status-only directive).
- Sequential-step directives — one directive per atomic operation when the operations could be ordered within one directive.
- Phase-spanning directives — a single directive mixing operations from two different phases.

### 2.6 Status transition discipline

All `cluster.status` transitions are operations within the relevant phase's directive — never a standalone directive.

| Transition | Carrier | §ref |
|---|---|---|
| `Not started` → `Data - In Progress` | Inline by the constitution-report-gen script | §6.1 |
| `Data - In Progress` → `Analysis - In Progress` | Operation within Phase 4's term-transfer/BOUNDARY directive (or Phase 6 if Phase 4 has no DB writes) | §7.6 / §9.6 |
| `Analysis - In Progress` → `Analysis Completed` | Operation within Phase 12's closure directive | §15.4 |

CC processes each transition as part of the directive's operation succession; the status flip fires inside the directive's transactional commit. AI never authors a `dir-NNN-status-init`, `dir-NNN-status-bump`, or `dir-NNN-status-complete` directive.

### 2.7 Atomic per-row work uses JSON templates; synthesis uses chat

When a task is "for each row in this list, decide one thing", AI receives a JSON template (`vc_id`, fields, empty target field) and returns the same JSON with the target field filled. CC builds the input and applies the output. **No free-form prose for atomic decisions.** Applies to:

- Phase 1 — UT classification (per-verse relevant/set_aside/borderline)
- Phase 2 — Pass A meaning record (per-verse meaning)
- Phase 5 — verse-to-sub-group mapping (if AI's Phase 5 output is encoded per-row)
- Phase 10 — inherited-finding reconciliation (per-finding disposition)

When a task is "look at this corpus and synthesise an analytical view", AI works in chat with free-form output. Applies to:

- Phase 3 — Constitution debate
- Phase 5 — Sub-group formation (the synthesis layer; per-row output may be derived)
- Phase 7 — VCG design within sub-groups
- Phase 9 — Catalogue prompts

The split is structural: AI's role is synthesis where synthesis is needed and atomic decisions where atomic decisions are needed. Mixing them in one phase produced the M01 failure.

---

## 3. Starting point — session open

Before any analytical work begins, the session opens in full compliance with the Session Startup Rule (`wa-global-rules-startup [current]`):

1. Obslog created with prefix `wa-obslog-{cluster_code}-{description}-v1-{YYYYMMDD}.md` and saved to `Sessions/Session_Clusters/{cluster_code}/`.
2. Obslog version incremented at every transition point — phases, sub-groups, terms.
3. If obslog writing is interrupted or discontinued, the session **must stop**. Recover the missing recordings first.

**Cluster status at session open:** `cluster.status` must be `Not started` or `Data - In Progress`. If `Analysis Completed` or `Published`, a re-open requires explicit researcher direction.

---

## 4. Phase 1 — UT verse review (CC, JSON template + API)

**Purpose:** every verse with status UT (untouched — no `verse_context` row exists for the `(verse_record_id, mti_term_id)` pair) is classified atomically as `relevant`, `set_aside`, or `borderline`. Each determination becomes a `verse_context` row (relevant or set_aside) or a borderline log entry (held for researcher decision).

**Owner:** CC. AI's only role is reading the per-batch system prompt and returning the JSON.

### 4.1 Inputs

- The cluster's term universe — `mti_terms` rows where `cluster_code='{code}'` and `status IN ('extracted','extracted_thin')`.
- For each term, every `wa_verse_records` row whose corresponding `verse_context` row does not yet exist (this is the UT set).

CC produces the UT load via a single SQL query against `wa_verse_records` LEFT JOIN `verse_context`.

### 4.2 Process

1. CC generates one JSON batch per term (or per-N-verse chunk for high-volume terms). Each batch carries:
   - System prompt: cluster characteristic statement + T1 framework + classification rubric (relevant / set_aside / borderline) + strict-JSON output spec.
   - Per-verse data: `vc_id_placeholder`, `verse_record_id`, `reference`, `strongs`, `transliteration`, `gloss`, `language`, `verse_text`, `context_before`, `context_after`, `translation`.
2. CC iterates batches against the Claude API. The system prompt is cached on the first call; subsequent calls read it at cache pricing.
3. CC parses each batch's JSON response, validates fields, captures the raw response.

### 4.3 Output

- VCNEW patch — one `verse_context.insert` op per `relevant` or `set_aside` classification. Borderlines are held in the log only.
- Review document: `Sessions/Session_Clusters/{code}/WA-{code}-UT-verse-review-api-v1-{date}.md` — per-term counts (UT / relevant / set_aside / borderline), borderline list, applied-patch reference.
- Raw API responses archive: `Sessions/Session_Clusters/{code}/WA-{code}-UT-api-raw-responses-{date}.json`.

### 4.4 Provisional-anchor rule (R4 satisfaction at Phase 1)

The applier's R4 integrity check requires every term with any `is_relevant=1` row to have at least one `is_anchor=1` row. **CC's patch builder enforces this at build time:**

1. For each term in the patch, query `SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND is_anchor=1 AND COALESCE(delete_flagged,0)=0`.
2. If zero, promote the **first** `is_relevant=1` op for that term to `is_anchor=1` as a provisional anchor.
3. If the term has only `set_aside` ops in the patch (no relevant), R4 does not require an anchor; leave all `is_anchor=0`.
4. Phase 7 VCG design may move the anchor designation to a different verse. The Phase 1 provisional is a placeholder, not a claim.

### 4.5 Patch shape (canonical)

Patch envelope per `wa-patch-instruction [current]` §15:

- `_patch_meta.patch_type = "VCNEW"`
- `_patch_meta.terms_covered = [mti_term_id, ...]`
- `_patch_meta.input_versions = {"<mti_term_id>": <md_version>, ...}` (dict, not list)
- `_patch_meta.cluster_code = "{code}"`
- `_patch_meta.governing_instruction = "wa-sessionb-cluster-instruction-v2_0-20260515"`
- Filename: `wa-cluster-{code}-patch-vcnew-utreview-api-v1-{date}.json`

Operation shape per op — see §A1 for the canonical field set.

### 4.6 Post-check

- Every UT verse from the §1 count has a recorded determination.
- Every borderline has a one-line rationale in the review document.
- Every term in `terms_covered` either has ≥1 active anchor in `verse_context` post-apply, OR has no active relevant rows (all-set-aside / all-borderline state — legitimate per §6.5.5 of the VC standard).
- `mti_terms.vc_status` set to `vc_completed` for every term in `terms_covered`.

**DB writes:** the VCNEW patch.

**Cluster status:** unchanged (`Not started` or `Data - In Progress`).

---

## 5. Phase 2 — Pass A per-verse meaning record (CC, JSON template + API)

**Purpose:** every `is_relevant=1` `verse_context` row receives a one-line meaning written to `verse_context.analysis_note`. The meaning answers: **what does this verse say about the inner-being characteristic the term names, in this verse's specific context?** Sub-groups, VCGs, and inherited structure are not visible to AI during this phase.

**Owner:** CC. AI fills the `meaning` field in the JSON template.

### 5.1 Why this phase exists where it does

The verse-meaning is a function of `(verse, term)`, not `(verse, term, sub-group)`. It does not depend on whether sub-groups have been defined yet — and recording meanings before sub-groups form prevents the inherited-structure contamination that v1_13's Phase 6 Pass A could not reliably prevent. Phase 3 (constitution debate) then has access to the meaning corpus, not just the gloss list, when deciding which terms belong in the cluster.

### 5.2 Inputs

- All `verse_context` rows for the cluster's terms where `is_relevant=1` AND `delete_flagged=0` AND `analysis_note IS NULL`.
- For each row: the linked `wa_verse_records` data (reference, verse_text, context_before, context_after, translation).
- For each row's term: Strong's, transliteration, gloss, language.

### 5.3 Process

1. CC generates JSON batches of ~50 verses each in canonical Bible order across the whole cluster (not by term, not by sub-group — to suppress grouping signal in the batch boundaries). Each batch is labelled `"batch": "{N} of {total}"`.
2. CC sends each batch to the Claude API with a system prompt: cluster characteristic statement + meaning-record rubric (1–2 sentences, ~250 chars, plain English, verse-specific, no group framing) + strict-JSON output spec.
3. CC parses responses, validates that every `vc_id` is echoed back with a non-empty `meaning`, captures raw responses.

### 5.4 What is deliberately suppressed from input

- `group_id`, `group_code`, VCG `context_description` — no inherited grouping visible.
- `cluster_subgroup_id` — sub-groups don't exist yet, but even if they did they would not appear.
- `is_anchor` — anchor designations are not relevant to meaning record.
- Existing `analysis_note` — only NULL rows are sent; once filled, never re-sent.
- Term co-membership lists — to prevent term-grouping anchoring within the cluster.

### 5.5 Output

- UPDATE patch: one `verse_context.update` op per filled meaning. `match` on `id` (vc_id) + `delete_flagged=0`. `set` carries `{"analysis_note": "<meaning>"}`.
- Pass A document: `Sessions/Session_Clusters/{code}/WA-{code}-passa-meanings-applied-v1-{date}.md` — per-batch counts, sample meanings, applied-patch reference.
- Raw API responses archive: `Sessions/Session_Clusters/{code}/WA-{code}-passa-api-raw-responses-{date}.json`.

### 5.6 Hard gate before Phase 3

```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = '{code}'
AND vc.is_relevant = 1
AND COALESCE(vc.delete_flagged,0) = 0
AND vc.analysis_note IS NULL;
```

Must return **0** before Phase 3 begins. If non-zero, return to Phase 2 for the missing batch(es).

### 5.7 Post-check

- Every is_relevant=1 active vc row in the cluster has `analysis_note` populated.
- Meaning length distribution within expected range (50–400 chars typical).
- No meaning text contains group-label markers (`[A]`, `[CLUSTER]`, VCG codes) — sentinel check; if present, the meaning was contaminated and needs re-running for that verse.

**DB writes:** the UPDATE patch.

**Cluster status:** unchanged.

---

## 6. Phase 3 — Cluster constitution debate (AI, chat, redesigned report)

**Purpose:** decide for each term in the cluster: stays in cluster / transfers to another cluster / placed in BOUNDARY for researcher review. Decisions are grounded in the per-verse meaning corpus from Phase 2, not in gloss-list interpretation.

**Owner:** AI (synthesis). CC produces the input report and applies the resulting directive in Phase 4.

### 6.1 Status transition (handled inline by the constitution-report-gen script)

When the constitution report is generated for a cluster at `cluster.status = 'Not started'`, the script (`_generate_cluster_constitution_report_v1_*.py`) **automatically transitions** the status to `Data - In Progress` as part of the same invocation (idempotent — no transition fires if status is already past `Not started`). A row-level JSON backup precedes the UPDATE.

This is the same one documented exception to the read-only convention for `_generate_*` scripts as in v1_13 §4.1.

### 6.2 Inputs

The **constitution report**, generated by CC: `Sessions/Session_Clusters/{code}/wa-cluster-{code}-constitution-v1-{date}.md`.

Structure (per §17 reports map):

- §1 — Cluster characteristic statement (one paragraph, the target the debate must produce a verdict against)
- §2 — Per-term identity + meaning corpus: every term's Strong's, transliteration, gloss, language, verse counts (G / SA), then **every Pass A meaning for the term's `is_relevant` verses**, one line per verse
- §3 — Cross-term signals: terms whose meaning corpora overlap heavily; terms whose meanings drift toward other clusters' characteristics
- §4 — Programme cluster catalogue: short list of named clusters and their characteristic statements (so AI can name a transfer target)

The constitution report **does not** contain inherited VCG information, sub-group structure, or anchor designations. Per §2.3 these are suppressed from constitution-debate input by design.

### 6.3 Process

1. Read each term's meaning corpus against the cluster's characteristic statement (§1).
2. For each term, decide: **STAYS** (meaning corpus aligns with the cluster's characteristic) / **TRANSFERS** (meaning corpus aligns with another cluster's characteristic — name the target) / **BOUNDARY** (meaning corpus is supportive, qualifying, or undecided — held for researcher review).
3. Record the decision per term in the obslog with rationale rooted in specific meanings.
4. For TRANSFERS, name the destination cluster code and one-line justification.
5. For BOUNDARY, name the candidate sub-group code (`{code}-BOUNDARY`) and the analytical question to resolve.

### 6.4 Output

- Constitution debate document: `Sessions/Session_Clusters/{code}/WA-{code}-constitution-debate-v1-{date}.md` — per-term verdict with rationale, decision summary table.
- Obslog entries per term.

### 6.5 Post-check

- Every term has a verdict (STAYS / TRANSFERS-TO-{cluster} / BOUNDARY).
- Every TRANSFERS verdict names a destination cluster with one-line justification.
- Every BOUNDARY verdict names the analytical question.
- No verdict is "validated against inherited VCGs" — verdicts are validated against meanings.

**DB writes:** None in Phase 3.

**Cluster status:** transitioned `Not started` → `Data - In Progress` inline at constitution-report generation (if applicable).

---

## 7. Phase 4 — Apply term transfers + BOUNDARY directives (CC)

**Purpose:** execute the structural decisions from Phase 3 — move TRANSFERS terms out, designate BOUNDARY terms.

**Owner:** CC.

### 7.1 Inputs

- The Phase 3 constitution-debate document (decisions per term).
- The obslog (Phase 3 section).

### 7.2 Pre-check

- Every term has a Phase 3 verdict.
- For TRANSFERS: every destination cluster_code exists in `cluster`.

### 7.3 Operation A — Term transfers (cross-cluster)

For each TRANSFERS verdict:

- `mti_terms.cluster_code` UPDATE from `'{source}'` → `'{destination}'`
- No verse_context, verse_context_group, or vcg_term updates required — these tables resolve cluster ownership through `mti_term_id → mti_terms.cluster_code` (no denormalised `cluster_code` columns).

### 7.4 Operation B — BOUNDARY designation

For BOUNDARY terms, no Phase 4 DB write is required. The term remains in the cluster; its BOUNDARY sub-group assignment happens in Phase 5/6 when the sub-group structure is created. The Phase 3 obslog is the durable record.

### 7.5 Directive

Phase 4 produces one directive per source cluster (the cluster being analysed):

- Filename: `wa-global-dir-{seq}-{code}-term-transfer-v1-{date}.md`
- Pattern: cluster-process directive per `wa-directive-instruction [current]`
- Five-element form: MOTIVATION (cite constitution debate), SCOPE (Operation A list of mti_id → new cluster_code), OUTCOME REQUIRED (counts per destination), COMPLETION CONFIRMATION (post-state queries showing source count, destination counts, BOUNDARY-set unchanged).

**If no terms transfer** (all STAYS or BOUNDARY), Phase 4 is skipped — no directive authored.

### 7.6 Status transition

If Phase 4 produces a directive, `cluster.status` `Data - In Progress` → `Analysis - In Progress` is **Operation N** within that directive (per §2.6). If Phase 4 is skipped (no transfers), the status transition fires in Phase 6's verse-routing directive instead.

### 7.7 Post-check

- Every TRANSFERS verdict has been applied.
- Source cluster term count = pre-count − TRANSFERS count.
- Each destination cluster count = pre-count + arrivals.
- Cross-table integrity: verse_context and verse_context_group rows for transferred terms now resolve to the new cluster_code.

**DB writes:** Operation A's UPDATE statements + status flip (if applicable).

---

## 8. Phase 5 — Sub-group formation from clustering meanings (AI, chat)

**Purpose:** form the cluster's sub-group structure by clustering the Phase 2 meaning corpus. Sub-groups emerge from the evidence, not from gloss-list interpretation.

**Owner:** AI (synthesis). CC produces the constitution report (already used in Phase 3) + a meaning-only listing for the now-stable term set, and applies the resulting directive in Phase 6.

### 8.1 Inputs

- Updated constitution report (regenerated post-Phase-4 to reflect the now-stable cluster term set).
- The obslog (through Phase 4).

### 8.2 Process

1. Read every verse-meaning across the cluster's now-stable term set, term by term.
2. Identify provisional clusters of meaning — groups of verses (from any term) that evidence substantially similar inner-being content.
3. Name each provisional cluster with a sub-group label and a one-paragraph `core_description` written from the meanings, not from prior labels.
4. For each verse, record its provisional sub-group assignment.
5. Note multi-faceted terms — terms whose verses span more than one provisional sub-group. These get primary + secondary sub-group records.

### 8.3 Output

- Sub-group design document: `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-design-v1-{date}.md` — list of sub-groups with `subgroup_code`, `label`, `core_description`, plus a verse-to-sub-group mapping table.
- Mapping JSON: `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-mapping-v1-{date}.json` — `{vc_id: subgroup_code}` for every is_relevant verse. CC uses this for the Phase 6 mechanical apply.
- Obslog entries per provisional sub-group.

### 8.4 BOUNDARY sub-group

If Phase 3 designated any BOUNDARY terms, AI also designs a `{code}-BOUNDARY` sub-group with a one-paragraph description identifying the analytical question (e.g. "perplexity/bewilderment terms — pending programme-level cluster reassignment").

### 8.5 Post-check

- Every is_relevant verse is assigned to exactly one sub-group (or to BOUNDARY).
- Every sub-group has a `core_description` written from meanings.
- Multi-faceted terms are explicitly named (primary + secondary).
- BOUNDARY sub-group exists if Phase 3 produced any BOUNDARY verdicts.

**DB writes:** None in Phase 5.

**Cluster status:** unchanged.

---

## 9. Phase 6 — Verse-to-sub-group mechanical routing + per-sub-group report (CC)

**Purpose:** apply the Phase 5 sub-group structure to the database — create `cluster_subgroup` rows, populate `mti_term_subgroup` term-to-sub-group links, set `verse_context.cluster_subgroup_id` for every verse. Produce the per-sub-group verse-and-meaning report that AI uses in Phase 7.

**Owner:** CC. No AI interpretation — the verse-to-sub-group routing comes directly from Phase 5's mapping JSON.

### 9.1 Inputs

- Phase 5 sub-group design document (sub-group definitions).
- Phase 5 mapping JSON (`{vc_id: subgroup_code}`).

### 9.2 Operation A — Create `cluster_subgroup` rows

INSERT one row per Phase 5 sub-group. Fields per §A1: `cluster_code`, `subgroup_code`, `label`, `core_description`, `sort_order`, `status='active'`, `version='v1'`, `source=<directive id>`, `created_at`, `last_updated_date`.

### 9.3 Operation B — Populate `mti_term_subgroup`

For each term, derive its sub-group set from Phase 5's mapping (one term may appear in multiple sub-groups if its verses span them). INSERT one `mti_term_subgroup` row per (term, sub-group) pair. `placement_note` records `[primary]` or `[secondary]` plus the analytical reason from Phase 5.

### 9.4 Operation C — Set `verse_context.cluster_subgroup_id`

For each is_relevant vc row, UPDATE `cluster_subgroup_id` to the sub-group from Phase 5's mapping. WHERE includes `id=? AND delete_flagged=0` to prevent UNIQUE-constraint collisions on soft-deleted duplicate rows (the duplicate-row defence learned from M46).

### 9.5 Operation D — `cluster.status` transition (if not already set in Phase 4)

If Phase 4 was skipped (no transfers), this directive carries the `Data - In Progress` → `Analysis - In Progress` transition as Operation D. If Phase 4 already fired the transition, Operation D is omitted.

### 9.6 Directive

Phase 6 produces one directive bundling Operations A/B/C/D:

- Filename: `wa-cluster-{code}-dir-{seq}-subgroup-assign-v1-{date}.md`
- Five-element form: MOTIVATION (cite Phase 5 documents + mapping JSON), SCOPE (the four operations explicit), OUTCOME REQUIRED (sub-group row counts, term-subgroup link counts, verse-routing counts, status flip if applicable), COMPLETION CONFIRMATION (per-sub-group verse counts match Phase 5 mapping; cluster.status='Analysis - In Progress').

### 9.7 Phase 7 input report

After the directive applies, CC generates the **per-sub-group verse-and-meaning report**: `Sessions/Session_Clusters/{code}/wa-cluster-{code}-subgroup-meanings-v1-{date}.md`.

Layout per sub-group:

```
## Sub-group {code}-X — {label}

Description: {core_description}
Term count: N
Verse count: M

| vc_id | reference | term | meaning |
|---|---|---|---|
| 12345 | Gen 22:12 | H3373 ya.re | Abraham's fear of God shown through obedience... |
| ... |
```

Suppressed: any inherited VCG references, group_id values, anchor designations.

### 9.8 Post-check

- `cluster_subgroup` rows match Phase 5 sub-group count.
- Every is_relevant vc row has `cluster_subgroup_id` set (or is in BOUNDARY).
- H4 health check (verse routed to sub-group its term has no `mti_term_subgroup` link to) = 0.
- H6 health check (term in cluster with no `mti_term_subgroup` link) = 0.
- The per-sub-group verse-and-meaning report is generated and ready for Phase 7.

**DB writes:** the Phase 6 directive's four operations.

**Cluster status:** `Analysis - In Progress` (set by either Phase 4 or Phase 6 directive).

---

## 10. Phase 7 — VCG design within sub-groups (AI, chat)

**Purpose:** within each sub-group, cluster the verse-meanings into VCGs (verse-context groups). Each VCG names a distinct inner-being phenomenon within the sub-group's characteristic. Routes verses to the new VCGs.

**Owner:** AI (synthesis per sub-group). CC applies the resulting directive.

### 10.1 Inputs

- Phase 6 per-sub-group verse-and-meaning report (`wa-cluster-{code}-subgroup-meanings-v1-{date}.md`).
- The obslog (through Phase 6).

The report is the **only** input. Inherited VCGs are not visible. The cluster's sub-group structure and per-verse meanings are the analytical material.

### 10.2 Process per sub-group

1. Read the sub-group's full verse-meaning list.
2. Cluster meanings into provisional VCGs — groups of verses with substantively similar inner-being content within this sub-group's register.
3. Name each VCG with a `group_code` (suggested format: `{primary_term_mti_id}-{seq}` or `{subgroup_code}-VCG-{seq}` — CC will assign final ids) and a `context_description` written from the meanings.
4. Designate **one anchor verse per VCG** — the verse that most directly and definitionally evidences the phenomenon the VCG names.
5. Identify dual-membership verses — verses that legitimately belong to two VCGs (within the same sub-group, or — rarely — across sub-groups).

### 10.3 Output

- VCG design document per sub-group: `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup_code}-vcg-design-v1-{date}.md`. Lists provisional VCG codes, descriptions, member verses, anchors, dual-memberships.
- VCG creation JSON per sub-group: `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup_code}-vcg-creation-v1-{date}.json` — `{provisional_code: {description, verses: [vc_id, ...], anchor_vc_id, ...}}`. CC uses this for the Phase 7 apply.

### 10.4 No Pass C / no reconciliation

Phase 7 does not compare against inherited VCGs. Inherited VCGs are dissolved by CC in Phase 8 with a researcher comparison report; AI is not involved.

### 10.5 Apply

CC packages the VCG creation across all sub-groups into one directive:

- Filename: `wa-cluster-{code}-dir-{seq}-vcg-create-v1-{date}.md`
- Operations:
  - **Op A:** INSERT `verse_context_group` rows per VCG. `group_code` assigned by CC (sequence within cluster); `context_description` from Phase 7 output.
  - **Op B:** INSERT `vcg_term` links — one per (VCG, term) where the VCG covers any of the term's verses.
  - **Op C:** UPDATE `verse_context.group_id` for every is_relevant verse → its new VCG id. WHERE includes `delete_flagged=0`.
  - **Op D:** UPDATE `verse_context.is_anchor=1` for every Phase 7 anchor designation (and reset prior anchors to 0 within the cluster's terms, except those preserved by explicit Phase 7 designation).

### 10.6 Post-check

- Every is_relevant vc row has `group_id` set to a new (Phase 7) VCG.
- Every VCG has exactly one `is_anchor=1` row (the Phase 7 anchor).
- H3 health check (mti not in VCG term set) = 0.
- R4 anchor gate passes for every term (≥1 active anchor).
- Old (inherited) VCGs are still present in DB but no longer referenced by any is_relevant verse — Phase 8 dissolves them.

**DB writes:** the Phase 7 directive's four operations.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 11. Phase 8 — Dissolve old VCGs with researcher comparison report (CC)

**Purpose:** soft-delete the inherited (pre-cluster-pivot) `verse_context_group` rows and their `vcg_term` links, now that every is_relevant verse has been re-routed to a new (Phase 7) VCG. Produce a researcher comparison report **before deletion** so the researcher can compare old-vs-new structure and approve the dissolution.

**Owner:** CC. No AI involvement.

### 11.1 Inputs

- Post-Phase-7 DB state (every is_relevant vc row points at a new VCG).
- The cluster's full inherited-VCG set — `verse_context_group` rows linked to the cluster's terms via `vcg_term`, not created by the current session's Phase 7 directive.

### 11.2 Identify inherited VCGs

```sql
SELECT vcg.id, vcg.group_code, vcg.context_description
FROM verse_context_group vcg
JOIN vcg_term vt ON vt.vcg_id = vcg.id
JOIN mti_terms mt ON mt.id = vt.mti_term_id
WHERE mt.cluster_code = '{code}'
  AND COALESCE(vcg.delete_flagged, 0) = 0
  AND vcg.id NOT IN (<set of VCG ids created by the Phase 7 directive>)
GROUP BY vcg.id;
```

### 11.3 Comparison report

CC produces `Sessions/Session_Clusters/{code}/WA-{code}-vcg-dissolution-comparison-v1-{date}.md`. Per inherited VCG, in `group_code` order:

```
### Old VCG {code} (id {N})

- Old description: {context_description}
- Old member verses: {count} — [first 5 references + "... and N more"]
- Disposition: {KEEP-EQUIVALENT | SPLIT | MERGED | OBSOLETE | UNROUTED}
- New routing of old members:
  - {first new VCG code} ({M} verses): {new VCG description excerpt}
  - {second new VCG code} ({K} verses): {new VCG description excerpt}
  - ...
- Side-by-side: old description vs new description text
```

**Disposition tag rules:**

- `KEEP-EQUIVALENT` — all member verses landed in one new VCG with similar meaning
- `SPLIT` — verses spread across multiple new VCGs within the same sub-group
- `MERGED` — verses joined other old VCGs' verses in one or more new VCGs
- `OBSOLETE` — verses re-routed entirely; the old framing has no analogue in new VCGs
- `UNROUTED` — some verses still have `group_id=NULL` (P-status); Phase 8 dissolution must wait until they're routed

Summary header: total inherited VCGs, dissolution counts per disposition, unrouted verse count.

### 11.4 Researcher gate

The comparison report is **researcher-eyes-required for the first cohort of clusters** (initial calibration of the new methodology). Once the researcher is satisfied that the dissolution dispositions are reliable, this can become a sampling check on later clusters.

Researcher reviews, approves dissolution in bulk or per-VCG, returns approval. CC executes the soft-delete directive only after approval.

### 11.5 Dissolution directive

- Filename: `wa-cluster-{code}-dir-{seq}-vcg-dissolve-v1-{date}.md`
- Operations:
  - **Op A:** UPDATE `verse_context_group SET delete_flagged=1, notes=<audit text>` WHERE `id IN (<inherited VCG ids>)` AND `delete_flagged=0`.
  - **Op B:** UPDATE `vcg_term SET delete_flagged=1` WHERE `vcg_id IN (<inherited VCG ids>)` AND `delete_flagged=0`.

**Soft-delete only.** Descriptions remain queryable for future inspection.

### 11.6 Post-check

- Every inherited VCG with `UNROUTED` disposition still has `delete_flagged=0` (preserved until its verses route).
- Every other inherited VCG has `delete_flagged=1`.
- Active VCG count for the cluster = Phase 7 VCG count (no inherited VCGs in the active set).
- H5 health check (orphan VCG with no active vc references) for the cluster's terms = 0.

**DB writes:** the dissolution directive's two operations.

**Cluster status:** unchanged.

---

## 12. Phase 9 — Catalogue prompts (AI, chat)

**Purpose:** answer every prompt in the T0–T7 catalogue (189 prompts, v2.1) at sub-group scope and at cluster scope. Every answer must be grounded in specific verse evidence or marked silent / gap. Output is the consolidated findings document that Phase 11 loads to `cluster_finding`.

This phase is largely unchanged from v1_13's Phase 8 (renumbered).

### 12.1 Inputs

- Post-Phase-7 grouped report — regenerated to reflect the new VCG structure.
- Per-cluster science extract: `Workflow/Sciences/wa-{code_lower}-{name}-scienceextract-v{V}-{date}.md` — **mandatory** input for T7 prompts. See §17 for the report map.
- Cluster instruction (this document).
- The obslog through Phase 8.

### 12.2 Pre-check

- All Phases 1–8 complete and committed.
- Grouped report regenerated.
- Science extract is present and current.

### 12.3 Process per sub-group + per cluster

For each prompt × scope cell:

1. Read the prompt.
2. Find the verses in scope (sub-group or cluster) that evidence the prompt.
3. Author the response:
   - **E** — evidenced finding; name the verses or VCGs.
   - **S** — silent; describe the silence pattern.
   - **G** — gap; describe what data is missing.
4. Write to the consolidated findings document.

### 12.4 Authoring discipline (parser-safe form)

Headers and scope markers must follow these rules so the Phase 11 loader can parse them:

1. **One scope marker per line.** Each `**[scope]**` marker starts at the beginning of a line.
2. **Every prompt must carry at least one explicit scope marker.** Forbidden: writing a brief cluster-wide statement under the prompt header without any `**[...]**` marker.
3. **One block per (prompt × scope).** Each (prompt, scope) cell appears at most once.
4. **Block separator.** A horizontal rule `---` on its own line marks the end of one prompt's findings.

Marker catalogue (recognised by the loader):

| Marker | Meaning |
|---|---|
| `**[A]**` or `**[A — Label]**` | finding for sub-group A (similarly B, C, …) |
| `**[A, B, C]**` (comma-separated) | finding shared across listed sub-groups; loader expands to one row per letter |
| `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` | cluster-level synthesis |
| `**[BOUNDARY — H1234 translit]**` | per-term structural characterisation for a BOUNDARY term |

Inline outcome codes (inside the scope marker's body):

- Body starts `E — text` or has no leading code → `finding` (or `cluster_synthesis` if scope is CLUSTER)
- Body starts `S — text` → `silent`
- Body starts `G — text` → `gap`

### 12.5 Output

Consolidated findings, structured into parts by tier:

- `Sessions/Session_Clusters/{code}/WA-{code}-consolidated-findings-v1-{date}-part1.md` (T0–T1)
- `…-part2-T2.md`, `…-part3-T3-T4.md`, `…-part4-T5-T7.md`

### 12.6 Cross-sub-group review pass

After all sub-group passes are complete, read across the full set of findings before producing the directive. Look for:

- Cluster-level patterns — findings that appear in the same form across all or most sub-groups → record once as `[CLUSTER]`.
- Structural relationships between sub-groups — causal sequences, constitutive relationships, asymmetries.
- Absences significant in totality — a prompt silent across all sub-groups is a cluster-level finding.
- Internal contradictions — resolve by returning to verse evidence before the directive is produced.

Findings surfaced are added to the consolidated findings document at their relevant prompt location.

### 12.7 Self-contained requirement

The document (parts 1–4) must be readable without reference to any other file:

- Every prompt answered with full text per scope — not structural labels or cross-references.
- Every E response includes specific verse reference(s) in the body.
- A Session C reader should be able to write the cluster publication using only these four parts.

### 12.8 Post-check

- 189 prompts × (sub-group set + CLUSTER) cells answered.
- Every E names at least one specific verse or VCG.
- BOUNDARY has structural characterisation notes (not full pass).

**DB writes:** None in Phase 9.

**Cluster status:** unchanged.

---

## 13. Phase 10 — Inherited-finding reconciliation (AI then CC)

**Purpose:** every inherited Session B finding, SD pointer, and research flag for the cluster's terms gets an explicit disposition relative to the new catalogue findings. Nothing is left orphaned.

This is new in v2_0. In v1_13 these legacy artefacts were left "untouched" by the cluster pipeline (per the explicit Phase 9 instruction `wa_session_b_findings` row count must be unchanged), with no path for their eventual resolution.

### 13.1 Inputs (CC produces)

- `Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-for-reconciliation-v1-{date}.md` — CC extracts every:
  - `wa_session_b_findings` row where `term_id` ∈ cluster's mti_ids, `status` IN (open, unresolved-equivalents)
  - `wa_session_research_flags` row for those terms (codes `PH2_*`, `SB_FINDING`, `SB_DIMENSION`, `SD_POINTER`)
  - `session_d_*` pointers / observations referencing the cluster's terms
- Layout: one section per inherited finding with its full text + term + cited verse anchors.

### 13.2 Process (AI, chat)

For each inherited finding, AI assigns one disposition:

| Disposition | Meaning |
|---|---|
| `RESOLVED-BY-CATALOGUE` | The finding is already captured in one of the new cluster_finding rows (T0–T7) — name the cluster_finding T-code(s) + scope(s). |
| `FOLD-INTO-PROMPT` | The finding adds new evidence to an existing cluster_finding — name target T-code + scope; provide a 1–2 sentence fold note. |
| `NEW-CLUSTER-FINDING` | The finding is real new evidence that doesn't fit any existing prompt in *this cluster* — name a target T-code; provide canonical finding text. |
| `SUPERSEDED` | The finding was authored under the pre-cluster-pivot lens and is no longer relevant — name the replacing cluster_finding (or note "no replacement — characteristic moved" / "data error already corrected"). |
| `ROUTE-TO-CLUSTER` | The finding's content belongs to **another cluster's Session B / Phase 9**. Name target cluster code (e.g. `M02-Anger`) if the cluster exists; otherwise name the source registry and note "cluster not yet built." Status stays operationally open; the finding will be picked up when the target cluster runs its Phase 10. |
| `CARRY-TO-SESSION-D` | **Strict criterion** (v2_1): a genuine cross-cluster phenomenon spanning **≥3 clusters** or a **programme-wide methodological** observation that no single cluster's T6 prompts can fully capture. Should be **few and very specific**. |
| `RESEARCHER-DECISION` | AI cannot decide; surface for researcher review. |

### 13.2.1 Decision tree (cluster-centric)

For each inherited finding, work the tree top to bottom and stop at the first hit:

1. Is the finding's content already in a Phase 9 cluster_finding for THIS cluster? → `RESOLVED-BY-CATALOGUE`
2. Does it add evidence to an existing Phase 9 finding in THIS cluster? → `FOLD-INTO-PROMPT`
3. Is it new evidence relevant to THIS cluster but missed in Phase 9? → `NEW-CLUSTER-FINDING`
4. Was it authored under a pre-cluster lens and is now obsolete (data error fixed, characteristic moved, etc.)? → `SUPERSEDED`
5. Does it concern **ANOTHER cluster's** characteristic / inner-being content (whether that cluster exists yet or not)? → `ROUTE-TO-CLUSTER`
6. Does it concern a pattern spanning **≥3 clusters** or a **programme-wide methodological** observation no single cluster's T6 can capture? → `CARRY-TO-SESSION-D`
7. Unable to decide between two of the above? → `RESEARCHER-DECISION`

**Important — bilateral cluster relationships go to T6 inside Phase 9, NOT to Session D.**

T6 (Structural Relationships with Other Characteristics, 24 prompts) inside Phase 9 already captures bilateral cluster relationships: T6.1 co-occurrence, T6.2 sequential, T6.3 causal/constitutive, T6.4 vocabulary/root sharing, T6.5 distinctions, T6.6 shared anchors, T6.7 dimensional sharing. If an inherited finding raises a bilateral relationship between THIS cluster and one other, it belongs in this cluster's T6 findings — use `NEW-CLUSTER-FINDING` (target T6.x) or `FOLD-INTO-PROMPT` (existing T6.x). If the bilateral relationship's home is the OTHER cluster's T6, use `ROUTE-TO-CLUSTER`. Either way, **not Session D**.

Session D is reserved for **≥3 clusters or programme-wide methodological** items. Examples: divine pathos attribution patterns across many clusters; the spirit/soul/heart boundary as it operates across all cluster spirit-level findings; commanded-inner-state grammar spanning explicit cluster names.

### 13.3 Output

- Reconciliation document: `Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-reconciliation-v1-{date}.md` — one section per inherited finding with assigned disposition and rationale.
- Reconciliation JSON: same content, machine-readable, for CC to apply.

### 13.4 Apply (CC)

- Filename: `wa-cluster-{code}-dir-{seq}-inherited-findings-reconcile-v1-{date}.md`
- Operations:
  - **Op A:** UPDATE `wa_session_b_findings.status` per disposition (mapping below); append `resolution_note` citing the cluster_finding, target cluster, or rationale.
  - **Op B:** UPDATE `wa_session_research_flags` (`resolved=1`, populate `resolved_note` with target cluster or Session D scope; researcher-decision items remain `resolved=0`).
  - **Op C:** UPDATE relevant `cluster_finding` rows for `FOLD-INTO-PROMPT` dispositions — append the inherited finding's evidence to `finding_text`.
  - **Op D:** INSERT new `cluster_finding` rows for `NEW-CLUSTER-FINDING` dispositions.

#### Op A status mapping (v2_1)

| Disposition | `wa_session_b_findings.status` |
|---|---|
| `RESOLVED-BY-CATALOGUE` | `resolved_qa` |
| `FOLD-INTO-PROMPT` | `folded` |
| `NEW-CLUSTER-FINDING` | `promoted` |
| `SUPERSEDED` | `superseded` |
| `ROUTE-TO-CLUSTER` | `routed_cluster` (resolution_note records target cluster code or `cluster not yet built — {registry-word}`) |
| `CARRY-TO-SESSION-D` | `routed_sd` (resolution_note records the cross-cluster scope) |
| `RESEARCHER-DECISION` | `open` (resolution_note flags researcher_decision + reason) |

Note: status column is free-text TEXT, no enum; `routed_cluster` was introduced in v2_1; v2_2 adds `validated_cluster_observation` for use when a finding is cluster-relevant but doesn't match any Tier question (see §14.5 fold path — these rows remain in `wa_session_b_findings` as standalone cluster observations rather than folding into a Tier finding).

### 13.5 Researcher gate

`RESEARCHER-DECISION` items surface for human review before the directive commits. The directive's MOTIVATION lists each researcher-decision item.

### 13.6 Post-check

- Every inherited finding has a status in the v2_1 mapping (`resolved_qa` / `folded` / `promoted` / `superseded` / `routed_cluster` / `routed_sd`) OR is a researcher-decision item awaiting review (status `open` with `researcher_decision` note).
- New `cluster_finding` rows from Op D have valid prompt FKs.
- `wa_session_b_findings` row count for the cluster's terms is unchanged (no DELETE; only UPDATE on `status` and `resolution_note`).
- Every `routed_cluster` row's `resolution_note` names a target cluster (existing code or future-registry placeholder).
- Every `routed_sd` row's `resolution_note` describes the ≥3-cluster / methodological scope.

**DB writes:** the reconciliation directive's four operations.

**Cluster status:** unchanged.

---

## 14. Phase 11 — `cluster_finding` load (CC)

**Purpose:** load the Phase 9 consolidated findings into `cluster_finding`, one row per (prompt × scope) cell with status, text, source file, and version.

This phase is functionally equivalent to v1_13's Phase 9 with the addition that Phase 10's inherited-finding reconciliation may have already inserted rows. The loader handles both.

### 14.1 Inputs

- The four parts of the consolidated findings document.
- The obslog through Phase 10.

### 14.2 Process

CC's structural-and-full-text loader (`scripts/_apply_{code}_findings_record_*.py`):

1. Build T-code → obs_id map from `wa_obs_question_catalogue`.
2. Parse each part for `**T#.#.#**` headers and scope markers.
3. Resolve each scope marker per §14.4 (scope-marker resolution).
4. Group (prompt, scope, vcg_scope) cells per UNIQUE constraint `(obs_id, cluster_code, cluster_subgroup_id, vcg_scope, version)`.
5. Resolve `finding_status` per group: `gap` > `silent` > `finding`; `cluster_synthesis` when scope=CLUSTER and outcome=E.
6. INSERT one `cluster_finding` row per group.
7. After INSERT pass, execute fold operation per §14.5 for any RESOLVED-BY-CATALOGUE rows in `wa_session_b_findings` (the Phase 10 reconciliation may have flagged inherited findings for fold-in).

### 14.3 Directive

- Filename: `wa-cluster-{code}-dir-{seq}-findings-record-v1-{date}.md`
- Operations:
  - Op A: bulk INSERT of cluster_finding rows.
  - Op B: append fold-in text + audit prefix to cluster_finding.finding_text for each RESOLVED-BY-CATALOGUE inherited finding (§14.5).
  - Op C: UPDATE `wa_session_b_findings.resolution_note` to add cluster_finding ids that received the fold.

### 14.4 Scope-marker resolution (v2_2)

The Phase 9 instruction §12.4 marker catalogue covers `[A]–[G]`, comma-grouped `[A, B, C]`, `[CLUSTER]`, and `[BOUNDARY ...]`. In practice AI may write more precise markers when a finding applies to specific VCGs or a cross-cluster axis rather than the whole sub-group. v2_2 handles these:

| Marker form (as written by AI) | Loader produces |
|---|---|
| `[A]` | 1 row: `cluster_subgroup_id=A.id`, `vcg_scope=NULL` |
| `[A, B, C]` | 3 rows: one per letter, all `vcg_scope=NULL` |
| `[CLUSTER]` | 1 row: `cluster_subgroup_id=NULL`, `vcg_scope=NULL` |
| `[BOUNDARY — H1234 translit]` | 1 row: `cluster_subgroup_id=BOUNDARY.id`, `vcg_scope='term:H1234'` |
| `[E-VCG-02]` | 1 row: `cluster_subgroup_id=E.id`, `vcg_scope='M01-E-VCG-02'` |
| `[E-VCG-02/03/04/05]` | 1 row: `cluster_subgroup_id=E.id`, `vcg_scope='M01-E-VCG-02;M01-E-VCG-03;M01-E-VCG-04;M01-E-VCG-05'` (semicolon-joined list) |
| `[B, C, D, E-VCG-01/03/04/05, F]` | 5 rows: B, C, D (each `vcg_scope=NULL`), E (multi-VCG `vcg_scope`), F (`vcg_scope=NULL`) |
| `[A/Wisdom]`, `[A/Love]` (cross-cluster axis) | Merge into the prompt's `[CLUSTER]` row body with "**M01 ↔ {axis} pair:**" prefix; no separate cluster_finding row (§14.4.1) |

#### 14.4.1 Cross-cluster axis markers — merge to CLUSTER

When AI uses `[A/X]` form where X names another cluster, this is a relationship-finding for T6.6 type prompts. Loader behaviour: do not create a separate row. Instead, append the marker's body to the prompt's `[CLUSTER]` row's `finding_text` with prefix `**M01 ↔ {axis} pair:**`. If no `[CLUSTER]` row exists for that prompt, create one (`finding_status='cluster_synthesis'`) carrying the axis content as the primary body.

### 14.5 Fold operation — RESOLVED-BY-CATALOGUE inherited findings

For each `wa_session_b_findings` row with `status='resolved_qa'` whose `resolution_note` names one or more Tier-question targets (e.g. `T3.8.1 [A]`), the Phase 11 loader:

1. Parses the target list from `resolution_note`.
2. For each target (T-code + optional scope), locates the matching `cluster_finding` row(s).
3. Appends a fold-in paragraph to `cluster_finding.finding_text` prefixed with:
   ```
   **[Folded from wa_session_b_findings.id={N}; finding_id={F}, registry={W}]**
   {original finding text}
   ```
4. Updates `wa_session_b_findings.resolution_note` to record the cluster_finding ids that received the fold (`... → folded into cluster_finding.id IN ({ids})`).

This implements the design principle: every inherited finding's analytical content reaches the Tier-keyed corpus where applicable, and the audit chain stays intact.

### 14.6 Post-check

- `cluster_finding` row counts match expected (per directive COMPLETION CONFIRMATION).
- Every T-code in the source documents resolved to a valid obs_id.
- Every `vcg_scope` value names an existing active VCG in `verse_context_group.group_code` (or is a semicolon-joined list thereof) when the loader runs in strict mode.
- Every RESOLVED-BY-CATALOGUE inherited finding has its fold-in text present in at least one named cluster_finding row.
- Every fold-target cluster_finding row's `finding_text` carries the `**[Folded from ...]**` marker.

**DB writes:** the findings-load directive.

**Cluster status:** unchanged.

---

## 15. Phase 12 — Cluster closure (CC)

**Purpose:** verify the cluster's database state, resolve any remaining gaps, transition `cluster.status` to `Analysis Completed`.

### 15.1 Inputs

- Post-Phase-11 DB state.
- Validation report from `scripts/_validate_cluster_completion_v1_*.py --cluster {code}`.

### 15.2 Pre-flight (CC)

1. C1 check (VC-coverage gaps) = 0 — every term has its verses fully classified.
2. C2 check (stale vc_status) = 0 — every term's `vc_status='vc_completed'`.
3. Every is_relevant verse has `group_id` (Phase 7) and `cluster_subgroup_id` (Phase 6).
4. R4 anchor check passes for every term (≥1 active anchor).
5. H3=0, H4=0, H5=0, H6=0, H7=0 (Phase 6 and Phase 7 should have produced clean health).
6. BOUNDARY terms (if any) have explicit dispositions per §16 (set-aside / promoted / reassigned / flagged).

### 15.3 BOUNDARY exit (mandatory)

Per §16, BOUNDARY is temporary. Before closure, every BOUNDARY term must exit via one of:

- **Set-aside** — verses marked `set_aside_reason`; term detached from BOUNDARY.
- **Promotion** — term moved to a characteristic-bearing sub-group; verses reassigned to a VCG.
- **Cluster reassignment** — term moved out of the cluster (rare at this stage).
- **Flagged-for-decision** — explicit pending-decision record with proposed disposition.

The closure directive includes BOUNDARY exit actions.

### 15.4 Closure directive

- Filename: `wa-cluster-{code}-dir-{seq}-closure-v1-{date}.md`
- Operations:
  - **Op A:** any BOUNDARY exit actions (UPDATE `mti_term_subgroup` placements, `verse_context` set-asides, etc.).
  - **Op B:** any final verification corrections (gap row updates, anchor fixes, vc_status sync).
  - **Op C:** UPDATE `cluster.status='Analysis Completed', last_updated_date=?` WHERE `cluster_code='{code}' AND status='Analysis - In Progress'`.

### 15.5 Post-check

- `cluster.status = 'Analysis Completed'`.
- Validation script clean (C1=0, C2=0).
- All H-checks at expected baseline (H1 reflects design-set-asides; others = 0).
- BOUNDARY empty or fully flagged.
- All Session C downstream consumers can read the cluster.

The cluster is now ready for Session C cluster publication.

**Cluster status transition:** `Analysis - In Progress` → `Analysis Completed`.

---

## 16. BOUNDARY discipline (canonical reference)

BOUNDARY is **a temporary sub-group** used during Phases 3–11 for terms that:

- Are supportive / descriptive / qualifying — they enhance the cluster's verse evidence without themselves carrying a distinct inner-being characteristic.
- Are undecided — the constitution debate (Phase 3) flagged them for further evidence-based review.

### 16.1 Lifecycle in v2_0

| Phase | BOUNDARY state |
|---|---|
| 3 | Constitution debate may assign terms to BOUNDARY (Phase 3 verdict) |
| 4 | Term-transfer directive does not move BOUNDARY terms; they remain in cluster |
| 5 | Sub-group formation creates the `{code}-BOUNDARY` sub-group with description |
| 6 | Verse-to-sub-group routing places BOUNDARY-term verses in the BOUNDARY sub-group |
| 7 | BOUNDARY may have its own minimal VCG set (typically a single aggregating VCG) |
| 8 | Old VCG dissolution proceeds the same way for BOUNDARY-routed verses |
| 9 | BOUNDARY terms receive structural characterisation notes (not the full 189-prompt pass) |
| 10 | Inherited finding reconciliation includes BOUNDARY-term findings |
| 11 | BOUNDARY characterisations recorded as `cluster_finding` rows under T1.2.1 |
| 12 | **BOUNDARY exit gate (mandatory):** every BOUNDARY term resolved per §15.3 |

### 16.2 At cluster closure (Phase 12)

BOUNDARY does **not** persist as a holding pen. Every BOUNDARY term must exit; the closure directive includes the exit actions.

---

## 17. Reports — input/output map (consolidated)

The cluster reports produced by analytics scripts in `scripts/`. All read-only (with one documented exception — see §6.1), all re-runnable. Naming convention `wa-cluster-{code}-{kind}-v{N}-{date}.md`; version auto-bumps per script's `next_version` helper.

| Report | Script | Used in phase | Sections |
|---|---|---|---|
| UT verse review | `_run_{code}_ut_review_via_api_*.py` | 1 | Per-term counts, borderline list, applied-patch reference |
| Pass A meanings applied | `_apply_{code}_passa_meanings_*.py` | 2 | Per-batch counts, sample meanings, applied-patch reference |
| **Constitution report** | **`_generate_cluster_constitution_report_v1_*.py`** | **3** | §1 cluster characteristic statement · §2 per-term identity + meaning corpus · §3 cross-term signals · §4 programme cluster catalogue |
| Per-sub-group verse + meaning | `_generate_subgroup_meanings_report_v1_*.py` | 7 | Per sub-group: verse list with (reference, term, meaning) |
| Grouped cluster (post-Phase-7) | `_generate_cluster_grouped_v1_*.py` | 9 | Cluster → sub-group → VCG → anchor + verses |
| Inherited findings for reconciliation | `_generate_cluster_inherited_findings_v1_*.py` | 10 | Per inherited finding: text + term + verse anchors |
| **VCG dissolution comparison** | **`_generate_vcg_dissolution_comparison_v1_*.py`** | **8** | Per inherited VCG: old text · new routing · disposition · side-by-side |
| Findings | `_generate_cluster_findings_report_v1_*.py` | 11, 12 | Organised tier → component → prompt; one section per sub-group |
| Tiered prompts catalogue | `build_obs_catalogue_tiered_extract.py` | 9 | 189 prompts T0–T7 |
| Cluster science extract | _(researcher-prepared)_ | 9 | Per-cluster science extract at `Workflow/Sciences/`. Mandatory T7 input. |

**Report regen rule:** at the start of each phase that consumes a report, regenerate the report from the current DB state. Stale reports invite reasoning on outdated assumptions.

**Reports that disappear in v2_0:** the v1_13 "comprehensive report" used for Phase 1 comprehension is no longer needed — Phase 1 is CC's UT review, not AI comprehension. The constitution report (Phase 3) absorbs the comprehension role with a different shape (meaning corpora, not verse text).

---

## 18. Patches and directives — content checklist

This instruction never authorises CC to write to the database directly. Every DB change is mediated by a patch (`wa-patch-instruction [current]`) or a directive (`wa-directive-instruction [current]`).

**Packaging is the default** (per §2.5). Status transitions (per §2.6) are operations within the relevant phase's directive — never their own directive.

**Routing for cluster work:**

| Operation | Method | Reason |
|---|---|---|
| UT-review inserts on `verse_context` | **Patch (VCNEW)** | Atomic per-row work; ID-resolved by CC's API runner; standard VC-family path |
| Pass A meaning UPDATE on `verse_context.analysis_note` | **Patch (VCREVISE)** | Per-row UPDATE; CC's Pass A apply script |
| Term transfers — `mti_terms.cluster_code` rebind | **Directive (Phase 4)** | Cross-cluster; status flip may be Operation N if Phase 4 fires; per `wa-directive-instruction [current]` §11.6 |
| Sub-group create + term link + verse routing + (status flip if not yet fired) | **Directive (Phase 6)** | Packaged: Ops A/B/C/D |
| VCG create + term link + verse-to-VCG routing + anchor designation | **Directive (Phase 7)** | Packaged: Ops A/B/C/D |
| Old VCG soft-delete | **Directive (Phase 8)** | Researcher-gated for early clusters; packaged |
| `cluster_finding` load | **Directive (Phase 11)** | Two-step structural+full-text loader |
| Inherited-finding reconciliation | **Directive (Phase 10)** | Per-finding disposition; packaged |
| Closure (BOUNDARY exit + verification corrections + status complete) | **Directive (Phase 12)** | Packaged including status flip |

**Filename:** `wa-cluster-{code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md` (or `wa-global-dir-...` for cross-cluster directives). Sequence numbers reset per cluster.

---

## 19. Pre/post controls — consolidated table

| Phase | Pre-check | Post-check |
|---|---|---|
| **1 UT review** | Cluster term set fixed; UT count enumerated | Every UT verse classified; provisional anchors enforced; `mti_terms.vc_status='vc_completed'` for processed terms |
| **2 Pass A meanings** | Phase 1 complete; UT=0 (no NULL vc rows for is_relevant) | Every is_relevant active vc row has `analysis_note` populated; no group-label sentinels in meanings |
| **3 Constitution debate** | Phase 2 complete; constitution report regenerated; cluster status `Not started` or `Data - In Progress` | Every term has a verdict (STAYS/TRANSFERS/BOUNDARY); status transitioned to `Data - In Progress` (inline if it was `Not started`) |
| **4 Term transfers + BOUNDARY** | Phase 3 complete; constitution-debate document committed | TRANSFERS applied; source cluster count = pre − transfers; status `Analysis - In Progress` if directive fired |
| **5 Sub-group formation** | Phase 4 complete; cluster term set stable; constitution report regenerated | Every is_relevant verse has provisional sub-group; sub-group `core_description` written from meanings; mapping JSON produced |
| **6 Verse routing + per-sub-group report** | Phase 5 design + mapping JSON committed | `cluster_subgroup` rows created; `mti_term_subgroup` populated; verse_context.cluster_subgroup_id set; H4=0, H6=0; status `Analysis - In Progress` |
| **7 VCG design** | Phase 6 complete; per-sub-group verse+meaning report fresh | Every is_relevant verse routed to a new VCG; every VCG has an anchor; H3=0; R4 passes |
| **8 Old VCG dissolution** | Phase 7 directive applied; researcher reviewed comparison report | Inherited VCGs soft-deleted (except UNROUTED); active VCG count = Phase 7 count |
| **9 Catalogue prompts** | Phase 8 complete; grouped report fresh; science extract loaded | 189 prompts × (sub-group + CLUSTER) answered; every E names a verse |
| **10 Inherited-finding reconciliation** | Phase 9 complete; CC's inherited-findings report produced | Every inherited finding has a disposition; researcher-decision items surfaced |
| **11 `cluster_finding` load** | Phase 10 complete; consolidated findings parts 1–4 final | `cluster_finding` rows match expected counts |
| **12 Closure** | Phase 11 complete; validation script clean | C1=0, C2=0; BOUNDARY empty or flagged; `cluster.status='Analysis Completed'` |

**A failed pre-check stops the phase.** A failed post-check stops the phase from being handed off.

---

## 20. Status discipline

Per the Session Startup Rule and `wa-claudecode-instruction [current]`, AI never tells CC the cluster is "complete" — completion is set by the researcher, on review of CC's confirmation outputs. AI's role is to deliver a directive whose Completion Confirmation queries demonstrate the outcome required.

CC's role is to execute the directive faithfully and return the confirmation. CC does not extend scope, interpret ambiguity, or apply analytical judgement (per `wa-directive-instruction [current]` §8.4).

---

## A1. Cluster-process tables — column reference (authoritative)

The six tables touched by cluster-process directives. **Author directives by consulting this list, not by analogy from another table.** Column names differ across these tables in non-obvious ways.

### `cluster`

`cluster_code` (PK) · `description` · `gloss` (not null) · `source` · `bucket` · `status` · `version` · `last_updated_date` · `short_name`

### `cluster_subgroup` (Phase 6 — Operation A creates these)

`id` (PK) · `cluster_code` (not null) · **`subgroup_code`** (not null — e.g. `M01-A`, `M01-BOUNDARY`) · `label` (not null) · **`core_description`** · `sort_order` · `status` · `version` · `source` · `notes` · `delete_flagged` · `created_at` · `last_updated_date`

> BOUNDARY is identified by `subgroup_code` naming convention. There is no `is_boundary` column.

### `mti_term_subgroup` (Phase 6 — Operation B populates the term↔sub-group join)

`id` (PK) · `mti_term_id` (not null) · `cluster_subgroup_id` (not null) · `placement_note` · `delete_flagged` (not null) · `created_at` (not null) · `last_updated_date` (not null)

> There is no `mti_terms.cluster_subgroup_id` column. Term placement lives in this join table (m:n — a term may have multiple rows for multi-faceted sub-group membership).

### `verse_context_group` (Phase 7 creates new ones; Phase 8 soft-deletes old)

`id` (PK) · **`group_code`** (not null) · **`context_description`** (not null) · `notes` · `delete_flagged` · `vertical_pass_flag`

> No `cluster_code` column — VCG ownership resolves through `vcg_term → mti_terms.cluster_code`.

### `vcg_term` (Phase 7 — Op B; Phase 8 — Op B soft-deletes)

`id` (PK) · `vcg_id` (not null) · `mti_term_id` (not null) · `placement_note` · `delete_flagged` (not null) · `created_at` (not null) · `last_updated_date` (not null)

### `verse_context` (Phase 1/2/6/7 write)

`id` (PK) · `verse_record_id` (not null) · `mti_term_id` (not null) · `group_id` · `cluster_subgroup_id` · `is_anchor` · `is_relevant` · `is_related` · `notes` · `delete_flagged` · `vertical_pass_flag` · `set_aside_reason` · **`analysis_note`** (per-verse meaning record — Phase 2)

> No `cluster_code` column — verse ownership resolves through `mti_term_id → mti_terms.cluster_code`.

> UNIQUE constraint: `(verse_record_id, mti_term_id, group_id, cluster_subgroup_id)` — applies regardless of `delete_flagged`. UPDATEs must include `delete_flagged=0` in WHERE to avoid colliding on soft-deleted duplicate rows.

### `mti_terms` (Phase 4 rebinds `cluster_code`)

`id` (PK) · `strongs_number` · `transliteration` · `gloss` · `language` · `owning_registry` · `owning_registry_fk` · `owning_word` · `owning_part` · `word_data_reference` · `word_data_ref_fk` · `status` · `exclusion_reason` · `extraction_date` · `strongs_reconciled` · `anchor_note` · `last_changed` · `delete_flagged` · `vc_status` · `vc_instruction_version` · `vc_status_updated_at` · `vc_status_note` · `md_version` · **`cluster_code`**

> No `cluster_subgroup_id` column on `mti_terms`. Sub-group placement is via `mti_term_subgroup`.

### `cluster_finding` (Phase 11 INSERTs)

`id` (PK) · `obs_id` (not null — FK to `wa_obs_question_catalogue.obs_id`) · `cluster_code` (not null) · `cluster_subgroup_id` · `finding_status` (not null — `finding`/`silent`/`gap`/`cluster_synthesis`) · `finding_text` · `source_file` · `version` · `notes` · `delete_flagged` · `created_at` · `last_updated_date`

> UNIQUE constraint: `(obs_id, cluster_code, cluster_subgroup_id, version)`.

### `wa_session_b_findings` (Phase 10 UPDATEs `status` + `resolution_note`)

`id` (PK) · `finding_id` · `registry_id` · `file_id` · `finding_type` · `finding` · `anchor_verses` · `raised_date` · `session_b_instruction` · `pass_ref` · `study_segment` · `delete_flag` · `obsolete_reason` · `obsolete_date` · `superseded_by_id` · `related_finding_id` · `resolution_note` · `thin_evidence` · **`status`** · `term_id` · `synthesis_outcome` · `tiers_engaged` · `structural_relationship` · `session_c_chapter` · `sd_pointer_ref`

> Phase 10 never DELETEs or INSERTs rows on this table — only UPDATEs `status` and appends to `resolution_note`. Row counts must remain unchanged per cluster's term set.

---

## 21. Why v2_0 — the M01 precedent

This instruction is the structural answer to a specific failure pattern: in M15's first attempts and M01's three Phase 6 restarts on 2026-05-15, AI re-anchored on inherited VCG headings during the "read every verse and write its meaning" step. Each correction — "read fresh, don't validate the old groups" — produced the same behaviour on the next attempt. AI's own closing entry on the M01 abandoned session (line 2058 of the abandoned obslog): *"the verse readings continued to be structured by pre-existing VCG group headings rather than proceeding from the text itself"*.

The diagnosis was structural, not behavioural: as long as inherited VCGs are present in AI's input during meaning-recording, AI will use them to frame its reading. The fix is to remove them from the input — and from the input of every analytical phase before VCG design.

v2_0 implements that fix:

1. Pass A meanings recorded against bare verses (no group framing visible). JSON template; per-row output; written to DB.
2. Constitution debate runs against meaning corpora, not glosses. Inherited groupings are absent from the constitution report.
3. Sub-group formation clusters meanings; inherited sub-groups are absent.
4. VCG design within sub-groups clusters meaning sub-corpora; inherited VCGs are absent.
5. Old VCG dissolution is CC-mechanical, with a researcher comparison report. AI is not asked to reconcile.

The cost is one new phase (Phase 2 — Pass A) and one new CC report (constitution). The benefit is the structural impossibility of the M01 failure mode.

---

## 22. Change history

**v2_0 (2026-05-15)** — Major restructure (this version). See §21 for the trigger and design rationale. Phases 1–10 redesigned/renumbered. Pass C reconciliation removed; Phase 8 (CC) dissolves old VCGs with a researcher comparison report. New Phase 10 reconciles inherited findings against the new catalogue. JSON-template + API pattern adopted for atomic per-row work (Phases 1, 2, 5-routing, 10). Constitution debate moves to Phase 3 after meanings; sub-group formation moves to Phase 5 (after constitution). v1_13's Pass A/B/C three-pass model is superseded.

**v1_13 (2026-05-14)** — §5.1.1 provisional-anchor convention (R4 satisfaction on VCNEW patches). M46 API-driven UT review precedent.

**v1_12 (2026-05-14)** — Phase 7 segmentation discipline (segment-tag in filename, obslog segment-close summaries). M39 mapping precedent.

**v1_11 (2026-05-14)** — Phase 7 directive segmentation ambiguity resolved.

**v1_10 (2026-05-14)** — M39-driven intra-day refinement.

**v1_9 (2026-05-14)** — Directive packaging discipline (§2.5) + status transition discipline (§2.6) established. Phase 7 segmentation pre-assessment.

**v1_8 (2026-05-14)** — Streamlining audit cleanups (frontmatter dedup, §5 renumber, T1.2.1 reference softened, OQ-NNN defined).

**v1_7 (2026-05-13)** — §11.8 parser-safety rules for Phase 8 markers; §10.4 `vcg_term` INSERT requirement (post-M47 m:n schema).

**v1_6 (2026-05-13)** — §5 Phase 2 patch type corrected to VCNEW; §5.4 split-patch guidance.

**v1_5 (2026-05-13)** — Status-init ceremony retired; comprehensive-report-gen script handles transition inline.

**v1_4 (2026-05-12)** — Phase 1 status-init directive made explicit; Phase 8 science extract mandatory.

**v1_3 (2026-05-12)** — Major rework from M05/M06/M15/M26 lessons. Phase 6 VCG reconciliation rewritten as three-pass (read → meanings → design → reconcile); BOUNDARY formalised; pre/post checks per phase.

**v1_2 and earlier** — see `Workflow/archive/`.
