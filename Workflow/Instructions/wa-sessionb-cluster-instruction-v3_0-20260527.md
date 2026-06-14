# Session B Cluster Instruction — v3_0

> **SUPERSEDED (2026-06-14)** by the v3_2 cluster-rollup model — `wa-cluster-rollup-design.md` / `wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md`. Retained for reference (v3_0 design phase); see `outputs/markdown/project-reconstruction/04-open-loops-and-incomplete-methodology-20260614.md` §4. Archiving pending the cleanup register.

**Status:** Active
**Date:** 2026-05-27
**Supersedes:** [`wa-sessionb-cluster-instruction-v2_9-20260526.md`](wa-sessionb-cluster-instruction-v2_9-20260526.md)
**Effective:** Immediately for all clusters whose work begins after this date. Closed clusters (pre-v3_0) follow §12 catch-up routine when their publication is scheduled.

This document specifies the cluster-analysis pipeline that produces the inner-being study's cluster outputs — characteristics, sub-groups, VCGs, catalogue findings, and publication prose — from a starting set of cluster terms.

It replaces v2_9 in full. v2_9 (and earlier) remain readable for provenance, but new cluster work uses v3_0 from the date above.

---

## §0. Change note — v2_9 → v3_0

v2_9 ran 12 numbered phases plus optional sub-phases (8.5, 8.7), plus a separate Session C publication routine (~8 AI sessions). v3_0 collapses that into **six phases (A–F)** with a single Phase C structural apply and a separate Phase E that produces publication prose from the findings database (re-runnable, backfillable).

Two governing principles, articulated by the researcher 2026-05-27 and codified in §2, sit above every phase: verse meaning rules all analytics; every observation must be recorded in the database.

Key reductions vs v2_9 (full quantification in [`wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md`](wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md)):

- **CC mechanical ops: −50%** (8 → 4 per cluster). Single Phase C structural apply replaces three v2_9 applies (P4, P6, P7-apply); single Phase F replaces P11+P12.
- **AI verse-corpus reads: −50%** (~18 → ~9 per cluster). Session C's seven chapter sessions are replaced by Phase E reading the findings table.
- **Session C AI sessions: −88% to −100%** (8 → 0–1). Session C becomes CC assembly from `prose_section`.
- **AI session count for Phase B itself is unchanged** (3 sessions for B.1+B.2+B.3, same as v2_9 P3+P5+P7). The Phase B saving is structural, not session-count.

Cross-checked against v2_9 for completeness — no v2_9 discipline is dropped silently; anything not carried forward is documented in §21.

---

## §1. Document scope

This instruction governs the **Session B Cluster pipeline** — Phase A through Phase F — for a single cluster, from "cluster has its term set assembled" through "cluster has approved publication prose in the database and is ready for assembly."

It does not govern:

- **Cluster splitting** (the optional pre-Phase-A move of dividing an oversized cluster into siblings — see [`wa-cluster-split-procedure`](wa-cluster-split-procedure.md) if applicable).
- **Programme-wide governance** — see [`wa-global-general-rules`](wa-global-general-rules.md) [current] (GR-REF-002, GR-FILE-003, etc.) and [`wa-global-flags`](wa-global-flags.md) [current].
- **DB schema, controlled vocabulary, patch operations** — see [`wa-reference`](wa-reference.md) [current], [`wa-patch-instruction`](wa-patch-instruction.md) [current].
- **Final publication assembly to PDF/DOCX** — see [`wa-sessionc-cluster-overview`](wa-sessionc-cluster-overview.md) [current] §7 step 7+ (kept for the assembler interface; Session C as an AI session is retired by §11 here).

Operational cross-references use `[current]` per GR-REF-002 — resolve to the highest-numbered version at read time.

---

## §2. Governing principles (codified 2026-05-27)

**GP-1. The verse meaning and context is the data and rules all analytics.**

Every analytical structure in the cluster — characteristic identity, sub-group design, VCG composition, catalogue findings, publication prose — defers to what the verses actually say (their Pass A meaning + their verse context). When an analytical structure conflicts with the verse evidence, the structure is wrong, not the evidence. Cluster identity is descriptive of evidence, not prescriptive over it.

**GP-2. All observations, however uncomfortable or disjointed, must be recorded in the database.**

Bias-screening is forbidden. An observation that cuts against the cluster's hoped-for shape is not less analytically valuable for that — it is often more so. Observations go into `cluster_observation` (with `status`, `target_phase`, and `resolution_note`) so they survive across phases and are processed rather than lost.

These two principles sit above every phase. Phase outputs that violate either are rejected at the CC stage gate.

---

## §3. Operating disciplines (carried from v2_9 §2)

**OD-1. Write-on-discovery.** Every analytical decision is written at the moment of discovery — verdict to obslog, mapping to JSON, finding to its scope-marked block. No accumulating in working memory, no "I'll write it up at the end." This is the overload protection mechanism for any phase with >100 evidence items in working set.

**OD-2. Contamination guard.** Inherited VCG codes, sub-group structures, and characteristic labels from prior cluster work are **not inputs** to the current phase's analytical decisions. They are suppressed from the input pack (see §6.1.2). The cluster's verse evidence + Pass A meaning corpus is the analytical material; inherited structure is consumed only by CC at Phase C for soft-delete.

**OD-3. Fluency-not-signal.** AI authoring fluency is not evidence of analytical correctness. A confidently-phrased verdict that fails the CC stage gate is wrong; a hesitant verdict that passes is right. Reviewers read for evidence-grounding, not for prose quality.

**OD-4. Atomic-vs-synthesis split.** An atomic decision (one term's verdict, one verse's sub-group assignment) is a discrete claim about discrete evidence. A synthesis statement (cluster-wide pattern, divine-pattern observation) is an integration across multiple atomic decisions. Never present synthesis as evidence for atomic decisions; never reduce synthesis to "the average of the atoms" without naming which atoms diverge.

---

## §4. Session open

Before any Phase begins, the session open performs:

1. **Read this document** ([current] — resolve from `Workflow/Instructions/`).
2. **Read [`wa-global-general-rules`](wa-global-general-rules.md) [current]** + active rows in `wa-global-flags` [current].
3. **Identify the cluster code and current cluster status** (`SELECT cluster_code, status FROM cluster WHERE cluster_code='{code}'`).
4. **Identify the phase to run** by matching cluster status to §16 pre-controls table.
5. **Read the cluster's `cluster_observation` rows with `status='open'`** — these may be inputs to the phase about to run.
6. **Read this phase's brief** (CC-produced; phase-specific). The brief declares Required-inputs explicitly per [feedback_ai_package_self_declaration].

Status discipline rules in §20.

---

## §5. Phase A — Read + meaning

**Owner:** CC (programmatic, via API). No AI chat session.

**Purpose:** for every cluster verse, classify whether it is inner-being-relevant (UT review) and, where it is, record its Pass A meaning and a set of inner-being keywords.

**Single CC operation, two passes wrapped together.**

### §5.1 A.1 — UT verse review

For each verse-record in the cluster's term set, classify:

- `IB` — verse evidences cluster-relevant inner-being content
- `CONTEXTUAL` — verse is in the term set but the term in this verse refers to outer-being / circumstantial / non-IB content
- `OUT` — verse is mis-routed (term sense in this verse does not belong to the cluster at all)

CC runs the UT classifier (`scripts/_run_ut_classifier_v{V}_*.py --cluster {code}`) which calls the Anthropic API per verse. Output: `verse_context.is_relevant ∈ {1, 0}` and `verse_context.ut_class ∈ {IB, CONTEXTUAL, OUT}`.

UT review uses Pass A heuristics-only at this stage — full meaning derivation happens at A.2 for IB verses.

### §5.2 A.2 — Pass A meaning + keywords

For each verse classified `IB` at A.1, CC runs the Pass A classifier (`scripts/_run_pass_a_v{V}_*.py --cluster {code}`) which calls the API once per verse and writes:

- `verse_context.meaning_pass_a` — one-line meaning summary (~30–80 words)
- `verse_context.keywords` — JSON list of 3–7 inner-being keywords (since schema 3.25.0 — per [feedback_phase2_passa_emits_keywords])

Once A.2 completes, CC builds the cluster's keyword analytics report — `wa-cluster-{code}-keyword-analytics-v1-{date}.md` — frequency tables, top tokens, top co-occurrence pairs, per-term keyword density, per-sub-group top keywords (when sub-groups exist; for fresh clusters this section is omitted).

### §5.3 Output

- `verse_context` rows updated (is_relevant, ut_class, meaning_pass_a, keywords).
- `wa-cluster-{code}-keyword-analytics-v1-{date}.md`.
- `wa-cluster-{code}-pass-a-summary-v1-{date}.md` — per-term verse counts, IB / CONTEXTUAL / OUT breakdown, sample meanings.

### §5.4 Pre-check

- `cluster.status` ∈ {`Not started`, `Data - In Progress`}.
- Cluster has terms assigned (`wa_term_inventory` rows where `cluster_code=?`).

### §5.5 Post-check

- Every verse in the cluster's term set has `ut_class` set.
- Every `is_relevant=1` verse has `meaning_pass_a` non-null and `keywords` populated.
- Keyword analytics report written.

### §5.6 Status transition

`Not started` or `Data - In Progress` → `Data - In Progress` (no change if already there; the formal transition happens at end of Phase B).

---

## §6. Phase B — Meaning grouping

**Owner:** AI (three sessions, B.1 → B.2 → B.3) with CC stage gates between them.

**Purpose:** decide which terms belong in the cluster, design the sub-groups that represent its characteristics, and design VCGs within each sub-group. All three sub-stages run from the same cluster's verse evidence; the analytical context builds progressively. **No verse-corpus re-read between stages** — input scaffolding is shared.

Detail design rationale: [`wa-v3_0-phase-b-control-design-v1-20260527.md`](wa-v3_0-phase-b-control-design-v1-20260527.md).

### §6.0 Phase B overview

| Sub-stage | Question | Output | CC stage gate |
|---|---|---|---|
| B.1 | Which terms stay, which transfer, which BOUNDARY? | Constitution-debate file with per-term verdict | §6.3.1 forbidden-grounds check + §6.3.2 verse-level relationship test |
| B.2 | What sub-groups (= characteristics) does the cluster's evidence form? | Sub-group design file + verse-to-sub-group mapping JSON | §8.4.1 BOUNDARY-not-a-parking-lot + §8.6 distribution gate (40% ceiling) |
| B.3 | Within each sub-group, what VCGs are present? | Per-sub-group VCG design files + unified VCG creation JSON | §10.8 no-sampling checklist + §10.9 DB-join validation |

Three AI sessions, three researcher review gates, one structural apply (at Phase C). The shared input scaffolding (constitution report, Pass A meaning corpus, keyword analytics, programme cluster catalogue) loads once and is referenced across the stages.

### §6.1 B.1 — Constitution debate

#### §6.1.1 Inputs

The **constitution report**, generated by CC: `Sessions/Session_Clusters/{code}/wa-cluster-{code}-constitution-v1-{date}.md`. Structure (per §17 reports map):

- §1 — Cluster characteristic statement (one paragraph; the target the debate must produce a verdict against)
- §2 — Per-term identity + meaning corpus: every term's Strong's, transliteration, gloss, language, verse counts (G / SA), then **every Pass A meaning for the term's `is_relevant` verses**, one line per verse
- §3 — Cross-term signals: terms whose meaning corpora overlap heavily; terms whose meanings drift toward other clusters' characteristics
- §4 — Programme cluster catalogue: short list of named clusters and their characteristic statements (for naming transfer targets)

#### §6.1.2 Inherited structure not visible (canonical statement)

The constitution report **does not contain inherited VCG information, sub-group structure, or anchor designations.** This is the contamination guard per OD-2. Verdicts are formed from meanings, not from inherited groupings.

This canonical suppression also applies to B.2 input (the sub-group design) and B.3 input (the per-sub-group meaning reports). Inherited structure surfaces only at Phase C, and only to CC for soft-delete.

#### §6.1.3 Process

For each term, AI decides:

- **STAYS** — meaning corpus aligns with the cluster's characteristic.
- **TRANSFERS-TO-{cluster}** — meaning corpus aligns with another cluster's characteristic; accidental placement here.
- **BOUNDARY** — meaning corpus is supportive, qualifying, or undecided; held for researcher review.

Every verdict carries rationale rooted in specific Pass A meanings (cite verse IDs / Pass A excerpts).

#### §6.1.4 Disallowed BOUNDARY reasons (carried from v2_9 §6.3.1)

BOUNDARY may **not** be assigned solely because:

- The term's meaning corpus is predominantly horizontal (human-to-human) rather than vertical (God-directed).
- The meanings describe sensory / material / circumstantial inner-being rather than overtly spiritual inner-being.
- The meanings include corrupt, illicit, or morally-negative inner-being content.
- The meanings describe an inner-being state the analyst would prefer not to be in scope.

A valid BOUNDARY verdict requires one of:

- **Cluster-membership undecided** — borderline between this cluster's characteristic and another's; researcher decision needed.
- **Homonymic / polysemic spread** — corpus covers two or more distinct registers; term may need sense-split treatment.
- **Supportive / qualifying register** — meanings describe an enhancing/qualifying state without itself carrying a primary characteristic.

CC pre-checks at the B.1 stage gate; verdicts citing forbidden grounds are returned for revision.

#### §6.1.5 Verse-level relationship test for TRANSFERS (carried from v2_9 §6.3.2)

A **TRANSFERS-TO-{cluster}** verdict requires more than "the term's meaning corpus aligns primarily with another cluster." Corpus-primary-register reasoning is too aggressive.

**The test, verse by verse:** Read every verse in the term's meaning corpus. For each, ask *does this verse evidence any relationship with or impact on the source cluster's characteristic?* "Relationship" is broad: direct evidence, structural opposite, instrument-of-the-characteristic, response-to-the-characteristic, protective-against, produced-by, in-tension-with.

**The verdict rule:**

- If **any** verse evidences a source-cluster relationship → **STAYS** with a **cross-register flag** in the rationale naming the term's primary register destination and the source-cluster relationship.
- If **no** verse evidences source-cluster relationship → **TRANSFERS-TO-{cluster}**.

Cross-register flags carry forward to B.2 (sub-group design may name the relational dynamic) and B.3 (VCGs may be designed around the cross-register relationship) and Phase D (T6 Structural Relationships findings).

#### §6.1.6 Output

- `Sessions/Session_Clusters/{code}/WA-{code}-constitution-debate-v1-{date}.md` — per-term verdict with rationale; decision summary table at end.
- Obslog entries per term.

#### §6.1.7 B.1 → B.2 stage gate (CC)

CC parses the constitution-debate file and verifies:

- Every term has a verdict (STAYS / TRANSFERS-TO-{cluster} / BOUNDARY).
- Every STAYS-with-flag names the other-register destination and the source-cluster relationship.
- Every TRANSFERS rationale establishes that no verse in the corpus evidences source-cluster relational content.
- Every BOUNDARY verdict cites one of the three §6.1.4 valid reasons.
- No verdict cites a forbidden ground.

Validator: `scripts/_validate_cluster_phase_b1_v1_{date}.py --cluster {code}`. Exit 0 = PASS. Exit 2 = FAIL with delta report naming the affected verdicts.

**Researcher review** follows CC pre-check pass. The constitution-debate file is the artefact.

**DB writes at B.1:** None.

### §6.2 B.2 — Sub-group design

#### §6.2.1 Inputs

- Post-constitution meaning corpus (STAYS terms only; TRANSFERS-OUT terms excluded; BOUNDARY terms collected separately).
- Keyword analytics report (`wa-cluster-{code}-keyword-analytics-v1-{date}.md`) — the structural scaffolding for axis discovery.

#### §6.2.2 Sub-groups represent characteristics (canonical)

A **sub-group represents a characteristic** — a single inner-being faculty/state the cluster expresses. **Default: 1 sub-group : 1 characteristic.** Sub-groups are designed for characteristic representation from the start (per [feedback_phase5_subgroups_represent_characteristics]).

The **volume-split exception** (§6.2.7): when a single characteristic's verse corpus would exceed the 40% distribution ceiling, the characteristic is split into multiple sub-groups by a documented split-axis (vertical vs horizontal, OT vs NT-distinctive, present vs eschatological, communal vs solitary, righteous vs corrupt, etc.). The characteristic identity is preserved across the splits; Phase C.5 binds them back via `characteristic_subgroup` rows. **The same characteristic identity bridges multiple sub-groups; this is not a second AI step.**

A **SPLIT_SUBGROUP** (sub-group serving two characteristics) is rare and must be flagged at B.2. M04-E precedent: `sa.s.von` → Joy, `agalliao` → Suffering-Joy, in different VCGs of the same sub-group. B.2 flags the case; B.3 separates the registers into different VCGs; Phase C.5 records the SPLIT_SUBGROUP observation.

Cross-register flags from B.1 inform B.2 — a term with a cross-register flag may motivate a sub-group named around the relational dynamic (e.g. a contempt-producing-shame sub-group in M07).

#### §6.2.3 Process

1. **Identify the characteristics the cluster expresses.** Read keyword analytics + sampled meanings to identify the distinct inner-being faculties/states present. Aim for an analytically clean list — typically 3 to 8 characteristics per cluster.
2. **Map each characteristic to its evidence.** Note which terms' verses primarily evidence each characteristic.
3. **Design sub-groups to carry the characteristics.** 1:1 default; volume-split if §6.2.7 forces it.
4. **Name each sub-group** with a `subgroup_code` (`{code}-A`, `{code}-B`, …) and a one-paragraph `core_description` written from the meanings — naming the characteristic it represents (and the split-axis when applicable).
5. **For each verse, record its sub-group assignment.**
6. **Multi-faceted terms** — terms whose verses span more than one sub-group — get primary + secondary records.
7. **Flag SPLIT_SUBGROUP cases** if any sub-group serves two characteristics.

#### §6.2.4 Output

- `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-design-v1-{date}.md` — list of sub-groups with code, label, core_description, evidence basis.
- `Sessions/Session_Clusters/{code}/WA-{code}-subgroup-mapping-v1-{date}.json` — `{vc_id: subgroup_code}` for every `is_relevant=1` verse.
- Obslog entries per provisional sub-group.

#### §6.2.5 BOUNDARY sub-group

If B.1 designated any BOUNDARY terms, AI also designs a `{code}-BOUNDARY` sub-group with a one-paragraph description identifying the analytical question (e.g. "perplexity/bewilderment terms — pending programme-level cluster reassignment").

#### §6.2.6 BOUNDARY is not a parking lot (carried from v2_9 §8.4.1)

BOUNDARY at B.2 carries only the verses of BOUNDARY-verdict terms (§6.1.3). It is **not** a holding pen for verses of STAYS-verdict terms whose meanings happen to lack God-directed framing.

If a STAYS-verdict term's corpus includes verses describing pure-human inner-being (parent's delight, soldier's gladness, worker's contentment, seductress's pleasure), those verses go to a **substantive sub-group** — designed and named appropriately (e.g. "horizontal joy", "circumstantial gladness", "corrupt delight").

**The forbidden pattern to eradicate:** designing substantive sub-groups around the cluster's vertical/divine register, then routing the residual pure-human verses to BOUNDARY. This is the M04 v1 failure and the broader bias GP-2 addresses.

**Operational test:** if BOUNDARY at B.2 holds >15% of the cluster's substantive verse corpus AND contains verses of STAYS-verdict terms, B.2 is rejected and resubmitted with explicit sub-group design for the residual content.

#### §6.2.7 Distribution hard gate (carried from v2_9 §8.6)

**Rule:** no substantive sub-group may hold more than **40%** of the cluster's substantive (non-BOUNDARY) verses.

If exceeded, the over-volume characteristic has too much verse volume to be handled as one sub-group; it must be split across multiple sub-groups by a named split-axis. The same characteristic identity persists across the splits; Phase C.5 binds them back via `characteristic_subgroup`.

**CC enforcement at B.2 → B.3 stage gate:** `scripts/_validate_cluster_phase_b2_v1_{date}.py --cluster {code}` runs the distribution check + §6.2.6 BOUNDARY-not-a-parking-lot check + every-verse-assigned check.

Exit 0 = PASS. Exit 2 = FAIL with delta report naming the dominant sub-group and listing candidate split-axes drawn from its term meanings.

**Researcher override** is documented in obslog with rationale (rare; default is reject).

**Researcher review** follows CC pre-check pass.

**DB writes at B.2:** None.

### §6.3 B.3 — VCG design within sub-groups

#### §6.3.1 Inputs

- Per-sub-group verse-and-meaning report (CC builds from B.2 mapping + DB): one file per sub-group, containing just that sub-group's verses with Pass A meanings.
- The obslog (through B.2).

The per-sub-group report is the only input. Inherited VCGs are not visible (OD-2).

#### §6.3.2 Process per sub-group

1. Read the sub-group's full verse-meaning list.
2. Cluster meanings into provisional VCGs — verses with substantively similar inner-being content within this sub-group's register.
3. Name each VCG with a provisional `group_code` (suggested: `{subgroup_code}-VCG-{seq}`) and a `context_description` from the meanings.
4. Designate **one anchor verse per VCG** — the verse that most directly and definitionally evidences the phenomenon the VCG names.
5. Identify dual-membership verses — verses that legitimately belong to two VCGs (within the same sub-group, or — rarely — across sub-groups). Flag in design document.

#### §6.3.3 Staged write-out (mandatory — overload control)

For each sub-group, processed sequentially in sub-group code order (M{NN}-A, M{NN}-B, …, M{NN}-BOUNDARY):

1. **Read** every verse-meaning in the sub-group's section of its report. Every row. No skipping.
2. **Design** VCGs and member assignments for that sub-group.
3. **Write the per-sub-group design document to disk immediately:**
   `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup_code}-vcg-design-v1-{date}.md`
4. **Append obslog entries** for the sub-group's VCG decisions.
5. **Verify per-sub-group sum.** Sum the member vc_ids across the sub-group's VCGs. The total **must equal** the sub-group's verse count from the input report. Record:

   ```
   **Verification**: VCG member sums = N1 + N2 + ... + Nk = TOTAL, matches {subgroup_code} input count of TOTAL ✓
   ```

   If the sum does not match, identify which verses are missing or duplicated. Fix before moving on. **Do not advance to the next sub-group until verification passes.**

6. Move to the next sub-group; repeat steps 1–5.

This is the heart of the overload protection — working memory clears between sub-groups; durable artefacts produced even if a later sub-group needs re-attempting.

#### §6.3.4 Output

After every sub-group is processed:

7. **Unified VCG creation JSON** across all sub-groups: `Sessions/Session_Clusters/{code}/WA-{code}-vcg-creation-v1-{date}.json`. Top-level keys are sub-group codes; each contains a `vcgs` array. Every VCG has `provisional_code`, `description`, `verses` (complete array), `anchor_vc_id` (must be a member of `verses`).
8. **Cross-routing flags document** (if any verses surfaced as needing routing review): `Sessions/Session_Clusters/{code}/WA-{code}-phase-b3-cross-routing-flags-v1-{date}.md`.
9. **Pre-submission checklist verification** (§6.3.5).

#### §6.3.5 No-sampling pre-submission checklist (carried from v2_9 §10.8)

Before declaring B.3 complete, AI must verify each condition:

- [ ] One design document per substantive sub-group + one for BOUNDARY (N files total = sub-group count). No combined documents.
- [ ] Each design document carries a sum-verification line per §6.3.3 step 5.
- [ ] Unified JSON file written with field name `verses` (not `key_verses`, not `members`, not "representative" anything). Complete arrays.
- [ ] Every `anchor_vc_id` is present in its VCG's `verses` array.
- [ ] Union of all `verses` across all VCGs in a sub-group equals the sub-group's input count.
- [ ] Total `verses` across the whole cluster equals the cluster's total is_relevant verse count.
- [ ] No vc_id appears in two different VCGs unless explicitly flagged as dual-membership.
- [ ] Every vc_id used in the output appears in the meanings report (i.e. is a cluster IB vc, not invented).
- [ ] BOUNDARY sub-group's aggregating VCG contains every is_relevant vc of every BOUNDARY term.

**Reading-discipline rule (absolute):** the meaning of every is_relevant vc in the input report must be read. No sampling. No "representative members." No "the rest follow the same pattern." The §6.3.3 staged write-out enforces this; the §6.3.5 checklist verifies it on submission.

#### §6.3.6 B.3 → C stage gate (CC)

CC parses the unified JSON and runs `scripts/_validate_cluster_phase_b3_v1_{date}.py --cluster {code}`:

1. Every vc_id in the JSON exists in `verse_context` with `is_relevant=1`, `delete_flagged=0`, `cluster_code` matching.
2. No vc_id appears in two VCGs (unless design document explicitly flags dual-membership; CC records secondary VCGs in `verse_context.notes`).
3. Sum of `verses` per sub-group equals the DB's count of is_relevant vc rows routed to that sub-group at B.2.
4. Every `anchor_vc_id` is in its VCG's `verses`.
5. BOUNDARY-VCG-01 contains every BOUNDARY term's is_relevant vc rows.

If any check fails, B.3 is rejected and resubmitted to AI. CC builds a per-sub-group delta report naming the gap (missing vc_ids, phantom vc_ids, sum mismatches, anchor-not-in-members).

**Researcher review** follows CC pre-check pass.

**DB writes at B.3:** None. All writes deferred to Phase C single apply.

### §6.4 Phase B post-checks (cluster-level)

- B.1 / B.2 / B.3 stage gates all PASS.
- All `cluster_observation` rows raised during Phase B carry `target_phase` populated and `status` either `confirmed`, `refined`, or `open` with a forward-targeted `target_phase` (e.g. Phase D for SPLIT_SUBGROUP).
- All files written under `Sessions/Session_Clusters/{code}/`.

### §6.5 Status transition

`Data - In Progress` → unchanged. Status transitions to `Analysis - In Progress` at the start of Phase D (first analytical write).

---

## §7. Phase C — Structural cleanup (single CC apply)

**Owner:** CC. No AI session. One consolidated directive.

**Purpose:** apply every structural decision from Phase B to the DB in a single transaction-bounded operation. Soft-delete inherited VCGs, designate BOUNDARY, route verses to new sub-groups, create new VCGs, anchor verses, load characteristic rows.

### §7.1 Inputs

- B.1 constitution-debate file (`WA-{code}-constitution-debate-v1-{date}.md`)
- B.2 sub-group design file + mapping JSON (`WA-{code}-subgroup-design-…`, `WA-{code}-subgroup-mapping-…`)
- B.3 unified VCG creation JSON (`WA-{code}-vcg-creation-v1-{date}.json`)
- Inherited VCG state from `verse_context_group` (cluster-tied or term-tied)

### §7.2 Operations (single directive `wa-cluster-{code}-dir-{seq}-phase-c-apply-v1-{date}.md`)

| Op | Action | Target tables |
|---|---|---|
| **C.1** | Apply term transfers + BOUNDARY designation | `wa_term_inventory.cluster_code` (TRANSFERS); `wa_term_inventory.boundary_flag=1` (BOUNDARY); `wa_term_inventory.cross_register_target` (STAYS-with-flag) |
| **C.2** | Sub-group create + verse routing | INSERT `cluster_subgroup` rows; UPDATE `verse_context.cluster_subgroup_id` |
| **C.3** | Inherited-VCG soft-delete (silent; per [feedback_phase8_silent_softdelete]) | UPDATE `verse_context_group.delete_flagged=1` for inherited VCGs tied to this cluster's terms; UPDATE `verse_context.group_id=NULL` for affected vc rows; UPDATE `vcg_term.delete_flagged=1` |
| **C.4** | VCG create + verse routing + anchor | INSERT new `verse_context_group` rows (with `group_code` assigned by CC sequence); INSERT `vcg_term` links; UPDATE `verse_context.group_id`; UPDATE `verse_context.is_anchor` |
| **C.5** | Characteristic load (silent, 1:1 default) | INSERT `characteristic` rows (one per substantive sub-group; short_name = sub-group label, definition = core_description, char_seq = sort_order); INSERT `characteristic_subgroup` rows (1:1 by default; multiple rows per characteristic if §6.2.7 volume-split was applied; `is_partial=0` for 1:1, `is_partial=1` for split sub-groups) |

### §7.3 BOUNDARY resolution (conditional sub-op of C.2)

If B.1 produced BOUNDARY verdicts AND the researcher has approved a disposition for each BOUNDARY term, the directive includes per-BOUNDARY-term disposition rows:

- **set_aside** — the term is dropped from cluster scope; `wa_term_inventory.cluster_code=NULL`, `boundary_flag=0`, set_aside reason recorded
- **route-to-cluster-{code}** — the term moves to a different cluster
- **move-to-substantive-sub-group** — the term joins a substantive sub-group of the same cluster (re-designation from BOUNDARY)

Per [feedback_boundary_resolution_required], **BOUNDARY-pending is not valid cluster closure**. C.4 cannot be applied while any BOUNDARY term has no disposition.

If no BOUNDARY verdicts were issued at B.1, C.3 is a no-op for BOUNDARY.

### §7.4 Pre-check (before applying)

- Phase B stage gates all PASS (B.1, B.2, B.3 validators all exit 0).
- Researcher has approved all three Phase B artefacts.
- BOUNDARY terms (if any) have disposition recorded in the directive.
- Inherited VCG soft-delete preview (CC dry-runs the WHERE clause and reports the affected row counts; researcher confirms numbers are in expected range — typically full cluster's inherited VCG set).

### §7.5 Apply discipline

Phase C runs as a single transaction (`BEGIN IMMEDIATE`). All operations succeed or all roll back. CC writes the validation report `WA-{code}-phase-c-validation-v1-{date}.md` post-apply.

Idempotency: the apply script checks `wa_term_inventory.cluster_code` and `cluster_subgroup` presence before issuing each operation. A partial-apply rerun is detected and either resumed from the last completed op or aborted with a clear delta report.

### §7.6 Post-check

- All B.1 verdicts reflected in `wa_term_inventory`.
- All B.2 sub-groups present in `cluster_subgroup` with `cluster_code={code}`.
- All B.2 verse assignments reflected in `verse_context.cluster_subgroup_id`.
- All B.3 VCGs present in `verse_context_group` with cluster-tied group_codes.
- All B.3 verse assignments reflected in `verse_context.group_id`.
- All anchors reflected in `verse_context.is_anchor=1`.
- All inherited VCGs for this cluster's terms have `delete_flagged=1`.
- `characteristic` table has N rows for the cluster's N substantive sub-groups (or N rows for N characteristics where volume-splits collapse to fewer characteristics).
- `characteristic_subgroup` rows present (N rows for 1:1 default; more if volume-splits).
- `cluster_observation` carry-forward observations (SPLIT_SUBGROUP, cross-register-flag relational dynamics) seeded with `status='open'`, `target_phase='D'`.

### §7.7 Status transition

`Data - In Progress` → `Structurally Ready` (new status added to controlled vocabulary in v3_0). Phase D cannot start until status reaches this state.

---

## §8. Phase D — Analytics findings

**Owner:** AI (N+1 sessions: one per characteristic + one cluster-synthesis). CC validates + loads.

**Purpose:** answer every prompt in the T0–T7 catalogue (189 prompts, v2.1) at **characteristic scope** for each of the cluster's N characteristics, then at **cluster scope** in a final synthesis session. Findings are written to `cluster_finding` per batch.

Phase D inherits v2_9 §12 ("Phase 9") almost verbatim. The major v3_0 change is that **tier-prose authoring is removed from Phase D** and moved to Phase E (the separate, re-runnable, backfillable prose phase). Phase D produces findings only.

### §8.1 Inputs (per batch)

Each AI session — single-characteristic, multi-characteristic bundle, or cluster-synthesis — is built by CC and includes:

1. **Brief** — primary task instructions, including Required-inputs declaration per [feedback_ai_package_self_declaration]. Naming:
   - Single-char: `WA-{code}-phase-d-char{N}-{short}-brief-v{V}-{date}.md`
   - Bundle: `WA-{code}-phase-d-bundle-char{seqs}-brief-…`
   - Synthesis: `WA-{code}-phase-d-cluster-synthesis-brief-…`
2. **Structural input** — sibling file to the brief.
   - Single-char: characteristic definition + sub-groups + VCGs + verses (with Pass A meanings) + 189-prompt catalogue
   - Bundle: per-characteristic data blocks distinctly separated (§2.A, §3.A, §2.B, §3.B, …) + shared catalogue
   - Synthesis: per-prompt matrix (one section per prompt showing the N characteristics' findings stacked verbatim from `cluster_finding`) + confirmed observations
3. **Governing instruction** — this document, §8.
4. **Per-cluster science extract** — `Workflow/Sciences/wa-{code_lower}-{name}-scienceextract-v{V}-{date}.md` — **mandatory** input for every AI-facing Phase D package per [feedback_phase9_science_extract_required].
5. **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{date}.md` Ch.1 'Defining Inner Being'. Background.
6. **Global rules** — `wa-global-general-rules` [current].

### §8.2 Pre-check (before any Phase D batch fires)

- Phase B (B.1, B.2, B.3) complete and committed via Phase C.
- Cluster status = `Structurally Ready`.
- `BOUNDARY_DECISION_PENDING` count = 0 (BOUNDARY dispositions all applied at C.3).
- Phase C.5 characteristic rows present; `characteristic_subgroup` links present.
- Carry-forward observations seeded in `cluster_observation` with `status='open'`, `target_phase='D'`.
- Schema at 3.24.0 or later.
- Science extract present and current.

### §8.3 Two-stage process

**Stage A — per-characteristic batches.** For each characteristic (in `char_seq` order or any order the researcher prefers), one AI session runs the full 189-prompt catalogue against that characteristic's evidence only. Output: 189 cluster_finding rows with `characteristic_id={N}`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`.

**Stage B — cluster synthesis (after all N characteristic batches close).** One AI session runs the 189-prompt catalogue against all N characteristics' findings stacked (per-prompt matrix). Output: 189 cluster_finding rows with `characteristic_id=NULL`, `finding_status='cluster_synthesis'`.

**Note vs v2_9:** Stage B's free-form prose appendix (M04 precedent) is **removed from Phase D under v3_0** — that emergent-theme prose moves to Phase E as `sc_v2_synth_appendix`. Phase D produces structured findings only.

### §8.4 Authoring discipline (parser-safe form)

Headers and scope markers must follow these rules so the per-batch loader can parse them:

1. **One scope marker per line.** Each `**[scope]**` marker starts at the beginning of a line.
2. **Every prompt must carry exactly one scope marker** (matching the batch's scope). Mixing CHAR-N and CLUSTER markers within one batch is forbidden.
3. **One block per (prompt × scope).**
4. **Block separator.** A horizontal rule `---` on its own line marks the end of one prompt's findings.
5. **Outcome code inline.** The marker body starts with `E — `, `S — `, or `G — `.

| Marker | Used in | Loader produces |
|---|---|---|
| `**[CHAR-N]**` | per-characteristic batch (Stage A) | `cluster_finding`: `characteristic_id=N`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`, `finding_status` per outcome (E→`finding`, S→`silent`, G→`gap`) |
| `**[CLUSTER]**` | cluster-synthesis (Stage B) | `cluster_finding`: `characteristic_id=NULL`, `finding_status='cluster_synthesis'`; outcome E/S/G in `notes` |

Inline outcome codes:

- `E — text` → outcome E; `finding_status='finding'` (CHAR) or `outcome=E` (CLUSTER, `finding_status='cluster_synthesis'`)
- `S — text` → outcome S; `finding_status='silent'` (CHAR) or `outcome=S` (CLUSTER)
- `G — text` → outcome G; `finding_status='gap'` (CHAR) or `outcome=G` (CLUSTER)

### §8.5 Per-characteristic batch flow

1. **CC builds the package** with `_build_{code}_characteristic_phase_d_package_*.py` (single-char) or `_build_{code}_characteristic_phase_d_bundle_*.py` (multi-char).
2. **AI runs the batch tier-by-tier** (mandatory per [feedback_phase9_tier_by_tier_mandatory]):
   - One tier per AI response — write the tier's findings, then STOP and wait for resume.
   - For each of the tier's prompts: read all the characteristic's verses (no sampling), author one finding with E/S/G + evidence (verses, VCGs, sub-groups within the characteristic that evidence the answer).
   - Mark each block with `**[CHAR-N]** {E|S|G} — …`.
   - At end of tier: STOP. Self-checks happen at end of full batch, not mid-tier.
3. **AI's self-check at end of batch.** Confirm 189 prompts answered; every E names evidence; carry-forward observations addressed; new analytical patterns surfaced.
4. **AI hands off** the findings file (or segments — see §8.7).
5. **CC merges segments** (if needed) and **applies via** `_apply_phase_d_characteristic_findings_*.py --char-seq N`. The loader:
   - Parses 189 `[CHAR-N]` blocks (hard 189 gate; rejects partial)
   - Verifies all q_codes map to `obs_id`
   - UNIQUE-constraint preflight on `(obs_id, cluster_code, characteristic_id, NULL, NULL, version)`
   - INSERTs 189 rows
   - Post-verify confirms row count + outcome tally
6. **CC updates `cluster_observation.status`** for any observation the batch's self-check confirmed or refined (`open` → `confirmed` / `refined`; populate `resolution_note`).
7. **Move to next characteristic.** Per [feedback_phase9_tier_by_tier_mandatory] discipline: each characteristic completes and self-checks before moving to the next.

### §8.6 Cluster synthesis flow (Stage B)

1. **CC builds the synthesis package** with `_build_{code}_phase_d_cluster_synthesis_*.py`. Structural input is a per-prompt matrix: for each of the 189 prompts, the N characteristics' findings stacked verbatim from `cluster_finding` (via DB query).
2. **AI runs the synthesis batch tier-by-tier.** For each prompt, read the N stacked characteristic findings, then author **one** cluster-scope finding examining what surfaces when the characteristics are compared (patterns, divergences, shared anchors). Mark with `**[CLUSTER]** {E|S|G} — …`. **Do not restate** per-char findings; the cluster-scope row is the integration across them.
3. **CC applies via** `_apply_phase_d_cluster_synthesis_*.py`. The loader:
   - Parses 189 `[CLUSTER]` blocks (hard 189 gate)
   - INSERTs 189 cluster-synthesis rows with `characteristic_id=NULL`, `finding_status='cluster_synthesis'`, outcome E/S/G in `notes`

### §8.7 Segmentation (when a batch is too large for one AI response)

When a per-characteristic batch (or the synthesis batch) exceeds a single AI response, segment by tier-pair: **seg1 T0+T1 (36 prompts) · seg2 T2+T3 (64) · seg3 T4+T5 (45) · seg4 T6+T7 (44)**. Filename: `WA-{code}-phase-d-char{N}-{short}-findings-seg{N}-T{x}T{y}-v{V}-{date}.md`.

CC merges segments via `_merge_phase_d_segments_*.py`:

- Strips per-segment headers
- Validates total prompt count
- Writes a canonical merged file
- Supports `--allow-partial` (loader still rejects unless 189)

### §8.8 Carry-forward observations (lifecycle)

Each per-characteristic batch's brief carries the observations linked to that characteristic — split between **OPEN** (action this batch) and **CONFIRMED (context only)** (validated by an earlier batch; provided as analytical context).

At the end of each batch's self-check, AI flags whether each OPEN observation surfaced as expected. CC updates `cluster_observation.status` to `confirmed` (validated) or `refined` (validated with substantive correction); `resolution_note` captures the analytical content; `resolved_date` populated.

By the time the synthesis session runs, all open observations should be confirmed or refined; the synthesis input's §2 surfaces them as direct inputs.

Per [feedback_two_governing_principles] GP-2: **observations are recorded in the database, not screened.** An observation that cuts against the characteristic's hoped-for shape is logged.

### §8.9 Self-check requirements (every batch)

Each batch's findings file ends with a self-check block:

```markdown
## Self-check

- Prompts answered: 189 / 189 ✓
- E findings naming specific evidence: <count>
- S findings: <count>
- G findings: <count>
- Carry-forward observations addressed: <per-observation status note>
- Unexpected analytical patterns surfaced: <list>
```

**Self-tally is not authoritative.** AI's E/S/G counts have proven unreliable. The loader's parse counts are ground truth — CC reports parser numbers, not the self-tally.

### §8.10 DB writes

Phase D writes to `cluster_finding` **per batch** as findings arrive, via the parametric loaders. No accumulation for later bulk load.

### §8.11 Post-check (cluster-level, after both stages complete)

- `SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='{code}' AND COALESCE(delete_flagged,0)=0` returns **N×189 + 189** rows.
- Every characteristic has exactly 189 `cluster_finding` rows.
- `SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='{code}' AND characteristic_id IS NULL AND finding_status='cluster_synthesis'` returns 189.
- Every E (CHAR-scope) finding's body names at least one specific verse or VCG.
- All `cluster_observation` rows are `confirmed` / `refined` (or explicitly deferred with `target_phase` updated to a later phase per GP-2).

### §8.12 Status transition

`Structurally Ready` → `Analysis Complete` on Phase D batch completion (when all N+1 batches loaded and post-checks pass).

---

## §9. Phase E — Publication prose

**Owner:** AI (N+1 sessions: one per characteristic for tier prose + one cluster-synthesis). CC validates + loads.

**Purpose:** produce the cluster's publication-ready prose **from the findings in the database**, write it to `prose_section`, and make it available for the CC publication assembler (§11). Phase E is **separate from Phase D** so that prose can be backfilled for clusters whose findings exist but were authored under pre-v3_0 (no tier prose) AND re-run when findings are updated.

### §9.1 Why a separate phase

Per researcher direction 2026-05-27:

> *"Phase D prose. This must be produced from the findings in the database. The prose may have to be a separate Phase to allow for CC to return the the findings to generate the prose. Should be required, with the ability to backfill the missing prose, and rerun the prose if findings were updated."*

Phase D produces analytical findings; those are the **source data** for the prose. Reading the findings from `cluster_finding` (small, structured rows) instead of re-reading the verse corpus (large, prose) is the single biggest cost saving in v3_0 vs v2_9 Session C — see [cycle comparison §3](wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md).

Separating prose from findings also means:

- Prose can be **backfilled** for any cluster whose findings already exist.
- Prose can be **re-run** when findings are updated (e.g. post-audit corrections).
- Prose authoring failures don't invalidate the findings; they only invalidate the prose.
- The publication pipeline (§11) is fed from the prose store, decoupled from the analytics pipeline.

### §9.2 Inputs (per batch)

Each Phase E AI session — per-characteristic tier prose or cluster-synthesis prose — is built by CC and includes:

1. **Brief** — primary task instructions per [feedback_ai_package_self_declaration].
2. **Structural input** — the characteristic's (or cluster's) findings as **flat rows from `cluster_finding`**, grouped by tier. NOT a re-read of verses.
   - Per-char: 189 findings + characteristic definition + sub-groups + VCGs (for citation context)
   - Synthesis: 189 cluster-synthesis findings + the 8 per-char characteristic definitions
3. **Governing instruction** — this document, §9.
4. **Tier-prose section type specifications** — `prose_section_type` rows for `sc_v2_tier_T0..T7` (per-char) and `sc_v2_synth_opening`, `sc_v2_synth_divine_pattern`, `sc_v2_synth_appendix` (synthesis). These specify `expected_length_min` / `expected_length_max` per tier.
5. **Per-cluster science extract** — mandatory.
6. **Programme prose** — mandatory.
7. **Global rules** — mandatory.
8. **Style and method discipline** — [`wa-sessionc-cluster-style-method-v1_1-20260512.md`](wa-sessionc-cluster-style-method-v1_1-20260512.md) — **mandatory**. Defines voice (essayistic, evidential, reverent-not-devotional, confident-not-hedging), audience (intelligent reader with no project-internal vocabulary), citation discipline (every analytical claim grounded by a quoted verse; verbatim quotation; no project-internal codes), forbidden vocabulary (no "cluster", "sub-group", "VCG", "tier", "T0..T7", "finding", "constitutional location" in published prose — use thematic names), the silence principle (name only meaningful silences), and the closing reverse-audit + self-review (see §9.7).

### §9.3 Per-characteristic tier prose flow

For each characteristic, one AI session produces 8 tier prose blocks (T0..T7). The AI reads the characteristic's 189 findings — **not the verses** — and authors a publication-ready prose summary per tier.

**Authoring discipline:**

1. For each tier T{N} (T0 first, T7 last):
   - Read the tier's findings (typically 21–33 per tier).
   - Author a publication-ready prose summary. Length per `expected_length_min/max` (T0: 800–1200; T1: 800–1400; T2: 600–1000; T3: 600–1000; T4: 600–1200; T5: 600–1200; T6: 400–800; T7: 400–700 — programme defaults; cluster-specific overrides via `prose_section_type` metadata).
   - Format: prose paragraphs. No bullet points. No headers within the tier block.
   - Use the cluster's verse-citation conventions inherited from the findings (sub-group / VCG / verse cites where the findings used them).
   - Open the block with `**[TIER_PROSE_T{N}]**` marker on its own line.
2. After each tier completes, **write the tier block to disk immediately** as a sibling section of the running prose file.
3. After all 8 tiers complete, AI closes with a self-check block (similar to §8.9 — word counts per tier, citation density check).

**File:** `Sessions/Session_Clusters/{code}/WA-{code}-phase-e-char{N}-{short}-tier-prose-v{V}-{date}.md` — one file per characteristic, containing all 8 tier blocks.

### §9.4 Cluster synthesis prose flow

One AI session produces the three cluster-scope prose sections:

- `sc_v2_synth_opening` — Ch1 cluster-wide opening (300–500 words). Derived from cluster-synthesis T0+T1 findings.
- `sc_v2_synth_divine_pattern` — Ch3 cluster-wide divine-pattern spine (1500–2500 words). Derived from cluster-synthesis T0 findings + per-char T0 tier prose.
- `sc_v2_synth_appendix` — free-form emergent-themes appendix (2000–4000 words). Derived from cluster-synthesis findings + per-char tier prose; captures themes the 189-prompt structure does not fully name (Joy/Gladness boundary, OT-NT vocabulary arcs, SPLIT_SUBGROUP register-pairs, etc. — M04 precedent).

**File:** `Sessions/Session_Clusters/{code}/WA-{code}-phase-e-cluster-synthesis-prose-v{V}-{date}.md` — one file containing all three blocks, each opened with its marker (`**[CLUSTER_OPENING]**`, `**[CLUSTER_DIVINE_PATTERN]**`, `**[CLUSTER_APPENDIX]**`).

### §9.5 CC ingest into `prose_section`

CC parses each Phase E file and writes to `prose_section`. Per [v3 publication pipeline §2.4](wa-v3-publication-pipeline-design-v1-20260527.md), the loader is `scripts/_ingest_phase_e_prose_v1_{date}.py`.

For each tier block:

```
INSERT INTO prose_section (
    section_type_id,         -- sc_v2_tier_T{N}.id
    cluster_code,            -- {code}
    characteristic_id,       -- {char.id}
    cluster_subgroup_id,     -- NULL (tier prose is char-scope)
    heading,                 -- '{char.short_name} — Tier T{N}' or parsed from text
    body,                    -- the prose
    word_count,              -- computed
    status,                  -- 'draft'
    version,                 -- max(existing_version)+1
    supersedes_id,           -- previous version's id, if exists
    author,                  -- 'claude_ai'
    metadata_json,           -- {"generator": "phase_e_tier_prose", "source_file": "...", ...}
    source_file,             -- relative path
    delete_flagged           -- 0
);
```

For cluster-synthesis blocks: same shape, but `characteristic_id=NULL` and `section_type_id` matches `sc_v2_synth_*`.

### §9.6 Idempotency and re-run

The ingester uses **body-hash comparison** for idempotency:

1. Compute `sha256(body)` for the incoming block.
2. Look up the current latest active version (`superseded_by_id IS NULL`) for `(cluster_code, characteristic_id, section_type_id)`.
3. If the existing latest's body hash matches the incoming hash, **no new row is inserted** — the rerun is a no-op.
4. If the hashes differ, a new row is inserted with `version = existing.version + 1`, `supersedes_id = existing.id`; the existing row is updated with `superseded_by_id = new.id`.

This means **Phase E can be re-run safely**. If findings have been updated and the AI re-authors prose, only changed prose creates new rows; unchanged prose stays at its existing version.

### §9.7 Reverse audit + self-review on completion (mandatory)

Per [style/method §10–§11](wa-sessionc-cluster-style-method-v1_1-20260512.md), every Phase E AI session must run two completion checks **before** the file is handed off for CC ingestion. These are non-optional.

**A. Reverse audit** (style/method §10):

1. **Findings coverage.** Walk every finding in the structural-input batch that fell within the tier's scope. For each finding, confirm one of:
   - The finding's claim is reflected in the tier prose (paraphrased, not necessarily verbatim), OR
   - The finding is a *routine silent* finding whose omission is justified by the silence principle (style/method §6), OR
   - The finding was redundant with one already covered.
   - If none of the three, the finding was missed — add prose that incorporates it.
2. **Anchor verse coverage.** Walk the tier's anchor verses (per the structural input). Confirm each is quoted *verbatim* at least once. Add a sentence using any missing anchor.
3. **Lens coverage.** Confirm the tier prose engages the tier's thematic lens (Divine Image / Faculty in Operation / Constitutional Location / Faculties / Relational Interfaces / Transformation / Inter-characteristic / View from outside Scripture — see style/method §5 for the name-only-not-the-code rule).

**B. Self-review pass** (style/method §11):

Read the tier prose end-to-end as a reader would. Correct:

- **Repetition** — same point in two places; pick the better and remove the duplicate.
- **Overreach** — claims beyond what the cited verses carry; soften or remove rather than propping up.
- **Padding** — sentences that add words but no content (throat-clearing, signposting, restating the heading).
- **Tonal drift** — devotional phrasing; first-person plural; hedging; any forbidden vocabulary from style/method §3 that slipped through.
- **Structural drift** — list-of-findings rather than essayistic prose; missing topic sentences; sentences depending on codes the reader cannot see.

**Order of operations:** write → reverse audit → self-review → return. The returned tier prose is the post-self-review version.

**CC validation hook:** the ingester (`_ingest_phase_e_prose_v1_*.py`) runs forbidden-vocabulary detection (a regex pass for "cluster", "sub-group", "VCG", "T0..T7", "finding-id", VCG codes) and rejects the block if any forbidden token is present. The author must address findings before re-submit.

### §9.8 Backfill discipline

For clusters whose findings exist but lack Phase E prose (pre-v3_0 closed clusters: M01, M02, M05, M06, M15, M20, M26, M39, M46; plus M03 partially):

1. **Backfill is a once-off Phase E run** when the cluster is scheduled for publication.
2. Same inputs as a normal Phase E run — the findings drive the prose; the verses are not re-read.
3. Same ingest path. The first run creates `version=1` rows; subsequent re-runs follow §9.6 idempotency.
4. The cluster's `cluster_observation` rows are scanned for `target_phase='E'` or `target_phase='publication'` items before backfill; any open observations are surfaced as inputs.

See §12 catch-up routine for the operational workflow.

### §9.9 Phase E required-or-not

Per researcher direction:

> *"Should be required, with the ability to backfill the missing prose, and rerun the prose if findings were updated."*

**For new cluster work** (Phase A → F under v3_0): Phase E is **required** for cluster closure. A cluster cannot transition to `Publication Ready` without Phase E prose loaded for every characteristic + cluster-synthesis.

**For pre-v3_0 closed clusters**: Phase E is **deferred and required only when publication is scheduled** — backfilled per §9.7 + §12.

### §9.10 Pre-check

- Phase D complete: every characteristic has 189 findings; cluster-synthesis has 189 findings.
- `prose_section_type` rows for `sc_v2_tier_T0..T7` + `sc_v2_synth_*` registered (one-time programme-level setup — done 2026-05-27).
- `cluster_observation` rows targeting Phase E (if any) surfaced as inputs.

### §9.11 Post-check

- For every characteristic: 8 `prose_section` rows (T0..T7) with `cluster_code={code}`, `characteristic_id={char.id}`, `delete_flagged=0`, current latest version (`superseded_by_id IS NULL`).
- 3 cluster-synthesis `prose_section` rows (opening, divine_pattern, appendix) with `cluster_code={code}`, `characteristic_id=NULL`.
- Total: 8N + 3 active prose rows per cluster.
- `prose_section_fts` indexed (trigger fires automatically on INSERT).
- All Phase E AI files written under `Sessions/Session_Clusters/{code}/`.

### §9.12 Status transition

`Analysis Complete` → `Publication Ready` on Phase E ingest of the full prose set. (For backfill on pre-v3_0 closed clusters, the status may already be `Analysis Complete`; the transition then fires on backfill completion.)

---

## §10. Phase F — Validation + closure

**Owner:** CC mechanical. No AI session in the normal case.

**Purpose:** validate the cluster's completeness across A–E and flip status to closed. Replaces v2_9's Phase 10 (inherited reconciliation), Phase 11 (validation), Phase 12 (closure) in a single consolidated phase.

### §10.1 F.1 — Inherited-finding reconciliation (conditional)

If the cluster had pre-existing Session B findings, SD pointers, or research flags from before its Phase A entry (rare for fresh clusters; common for clusters being re-analysed), CC produces a disposition report and either:

- Auto-folds them into Phase D output by mapping inherited findings to the closest Phase D finding (CC heuristic + researcher review)
- Routes them to `cluster_observation` with `status='deferred'`, `target_phase='audit'` for post-closure handling

This step is a no-op for clusters with no inherited artefacts (most fresh v3_0 clusters).

### §10.2 F.2 — Validation (11-check)

CC runs `scripts/_validate_cluster_closure_v1_{date}.py --cluster {code}` which performs:

1. **Phase A complete:** every term's verses have `ut_class` set; every is_relevant=1 has `meaning_pass_a` and `keywords`.
2. **Phase B applied:** every term has cluster verdict (STAYS / TRANSFERS / BOUNDARY); every is_relevant verse has `cluster_subgroup_id` and `group_id`; every VCG has anchor.
3. **Phase C applied:** `characteristic` rows present; `characteristic_subgroup` links present; inherited VCGs `delete_flagged=1`.
4. **Phase D complete:** N×189 + 189 `cluster_finding` rows; every characteristic has exactly 189 findings; cluster-synthesis has 189; every E names evidence.
5. **Phase E complete:** 8N + 3 active prose rows; every characteristic has all 8 tier prose blocks; cluster-synthesis has all 3 prose blocks; prose FTS indexed.
6. **Observations resolved:** every `cluster_observation` row is `confirmed` / `refined` / `deferred` (with `target_phase` set to a future programme-level phase like `audit` or `publication`). No `open` observations targeting completed phases.
7. **Distribution healthy:** no substantive sub-group exceeds 40% of substantive verses (§6.2.7 still holds).
8. **BOUNDARY clean:** no `BOUNDARY_DECISION_PENDING` flags active.
9. **Citation traceability:** `finding_citation` rows present (extractor runs automatically; see §10.3).
10. **FTS in sync:** `prose_section_fts` rebuilt or trigger-synced.
11. **Status discipline:** cluster.status = `Publication Ready` (set by §9.12) or `Analysis Complete` (if Phase E deferred for backfill); no anomaly.

Validation report: `WA-{code}-phase-f-validation-v1-{date}.md`. PASS / REVIEW / STOP outcome per check.

### §10.3 F.3 — Citation extraction (automatic)

CC runs the two-stage citation extractor:

- Stage 1: extract verse references from cluster_finding body text (regex + structured parse).
- Stage 2: derive VCG citations from the verse refs (verse_id → vcg via verse_context.group_id).

Result: `finding_citation` rows for every cluster_finding row that cites a verse or VCG.

Script: `scripts/_extract_finding_citations_v1_{date}.py --cluster {code}`. Already runs as part of programme-wide post-Phase-D pipeline (see [citation backfill](Workflow/Clusters/wa-finding-citation-backfill-20260527.md)).

### §10.4 F.4 — Status flip

If F.2 validation PASSES: `cluster.status` → `Closed` (terminal status for v3_0 clusters).

If F.2 has REVIEW or STOP outcomes: cluster remains at current status; researcher review required. CC writes a corrective-actions plan.

### §10.5 Post-check

- `cluster.status='Closed'` (or cluster remains at prior state with corrective-actions plan filed).
- All validation checks PASS.
- Finding citations extracted.
- Cluster is ready for publication pipeline (§11).

---

## §11. Publication pipeline — Session C reduced to CC assembly

**Owner:** CC mechanical + optional researcher polish. No AI session in the normal case.

**Purpose:** assemble the cluster's publication artefact from `prose_section` (loaded at Phase E or backfilled) into combined Markdown / PDF / DOCX. Replaces v2_x Session C's ~7-chapter AI authoring routine.

Detail in [v3 publication pipeline design](wa-v3-publication-pipeline-design-v1-20260527.md).

### §11.1 Inputs

- `prose_section` rows for the cluster (8N + 3 active rows post-Phase E).
- The tier-to-chapter mapping (programme-canonical; see §11.2).
- Cluster metadata for title/subtitle/author.

### §11.2 Tier → chapter mapping (programme-canonical)

| Source prose section | Consumed by chapter |
|---|---|
| `sc_v2_synth_opening` (cluster) | Ch1 |
| `sc_v2_tier_T0` (per char) | Ch1 (cluster intro), Ch3 (per-char divine pattern) |
| `sc_v2_synth_divine_pattern` (cluster) | Ch3 (cluster spine) |
| `sc_v2_tier_T1` (per char) | Ch1, Ch5 |
| `sc_v2_tier_T2` (per char) | Ch4 |
| `sc_v2_tier_T3` (per char) | Ch4 |
| `sc_v2_tier_T4` (per char) | Ch5 |
| `sc_v2_tier_T5` (per char) | Ch5 |
| `sc_v2_tier_T6` (per char) | Ch6 |
| `sc_v2_tier_T7` (per char) | Ch7 |
| `sc_v2_synth_appendix` (cluster) | Appendix |

### §11.3 Assembly flow

```
1. CC: scripts/_assemble_cluster_publication_from_db_v1_{date}.py --cluster {code}
   - Resolves latest active version per section (WHERE superseded_by_id IS NULL)
   - Joins per-tier prose into chapter-shaped Markdown per §11.2
   - Writes combined master document (chapter-form): wa-cluster-{code}-publication-v1-{date}.md
2. (Optional) researcher reviews assembled chapter-form markdown; edits in place or via ingest
3. (Optional, if researcher edits) CC: scripts/_ingest_chapter_prose_v1_{date}.py
   - Inserts revised prose as new version; old version becomes superseded
4. CC: regenerate chapter-form output via #1
5. **Integrated-essay form** (single flowing study; M09 precedent):
   - One AI run synthesises the chapter-form into a single integrated essay for a non-technical reader
   - Structure: title + subtitle → "What this study is" → "The divine pattern" (cluster-wide T0 spine) → one section per characteristic (using the thematic name, woven across T1–T7) → optional appendix
   - Style/method §1–§12 govern this run (essayistic prose, no project vocabulary, verbatim citation, silence principle, reverse audit + self-review)
   - Output: wa-cluster-{code}-essay-v1-{date}.md
6. CC: PDF/DOCX render via scripts/combine_cluster_published_to_docx.py
   - Renders the integrated essay (step 5) as the publication artefact: wa-cluster-{code}-essay-v1-{date}.docx
   - Note: the chapter-form (step 1) is intermediate scaffolding for review; the essay-form (step 5) is the publication target. Both are persisted; only the essay-form is the final user-facing artefact.
```

### §11.4 Backwards compatibility — Session C as historical mode

Pre-v3_0 clusters with chapter-draft Markdown files (M01, M03, M09, M15) had their chapter drafts backfilled into `prose_section` as `sc_v2_ch{N}` rows (2026-05-27, see [backfill log](Workflow/Clusters/wa-finding-citation-backfill-20260527.md) and [backfill script](scripts/_backfill_published_clusters_to_prose_section_20260527.py)).

The assembler handles both:

- **v3_0 clusters**: read tier-prose rows (`sc_v2_tier_*`) + synthesis-prose rows (`sc_v2_synth_*`), assemble per §11.2 mapping.
- **Pre-v3_0 clusters with backfilled chapter prose**: read `sc_v2_ch{N}` rows directly (no per-tier assembly needed — the chapter prose is already cluster-scope, hand-authored under old Session C).

The decision branch is automatic in the assembler script.

### §11.5 Idempotency

The assembler is read-only on `prose_section` (no writes). Re-runs produce the same output (modulo timestamp in the file header) as long as the underlying rows are unchanged. After researcher edits + ingest, a re-run picks up the new latest version automatically.

---

## §12. Catch-up routine for pre-v3_0 closed clusters

For the 9 pre-v3_0 closed clusters with characteristics loaded by [characteristic backfill](scripts/_apply_generic_characteristic_backfill_20260527.py) (M01, M02, M05, M06, M15, M20, M26, M39, M46) **plus M03**:

### §12.1 Status mapping

| State | What it means | Action needed |
|---|---|---|
| Findings present, no Phase E prose, no chapter drafts | Pre-v2_6 closed cluster; characteristics retrofitted today; needs prose authoring | Run Phase E backfill |
| Findings present, chapter drafts in `prose_section` (M01, M03, M09, M15) | Pre-v3_0 closed; chapter drafts authored under legacy Session C and ingested | No Phase E backfill needed; assembler reads `sc_v2_ch{N}` directly |
| Findings present, partial prose | Mixed state | Inspect per-cluster; backfill missing tier prose |

### §12.2 Backfill workflow per cluster

```
1. CC: build Phase E input pack (the cluster's 189×N findings + characteristic definitions)
   scripts/_build_{code}_phase_e_input_v1_{date}.py --cluster {code}
2. AI: run per-characteristic tier-prose batches (8 tier prose per characteristic) tier-by-tier
3. CC: ingest each finished tier-prose file via _ingest_phase_e_prose_v1_*.py
4. AI: run cluster-synthesis prose batch
5. CC: ingest synthesis file
6. CC: re-run §10.2 F.2 validation; if PASS, status → 'Closed'
   (For clusters already 'Closed' under v2_x, status → 'Publication Ready')
7. CC: scripts/_assemble_cluster_publication_from_db_v1_{date}.py --cluster {code}
   → assembled markdown
8. (Optional) researcher review + revisions via ingest
9. CC: combine_cluster_published_to_docx.py
   → PDF + DOCX
```

### §12.3 Catch-up cost (estimate)

For an N=7 cluster, Phase E backfill = 7 per-char tier-prose AI sessions + 1 cluster-synthesis prose AI session = 8 AI sessions per cluster. The findings table is the input — verses are not re-read.

For 10 catch-up clusters (M01..M46): 80 AI sessions total. Manageable. Spread across days/weeks as bandwidth allows.

---

## §13. Revised publishing routine (for already-published clusters wanting revisions)

For clusters whose publication is already complete and the researcher wants prose revisions:

```
1. Researcher edits chapter or tier-prose markdown file
2. CC: _ingest_phase_e_prose_v1_*.py (or _ingest_chapter_prose_v1_*.py for sc_v2_ch{N} cases)
   - New version inserted; old version superseded
   - Supersession chain preserved in prose_section
3. CC: _assemble_cluster_publication_from_db_v1_*.py --cluster {code}
   - Picks up latest active version automatically
4. CC: regenerate PDF/DOCX
```

Idempotency per §9.6: if the input body matches the current latest version's body (hash), no new row is inserted.

---

## §14. BOUNDARY discipline (canonical reference, carried from v2_9 §16)

BOUNDARY at B.1 is a verdict applied to a term whose meaning corpus does not yet support a STAYS or TRANSFERS decision. It is a **provisional state**, not a closure state.

**Valid BOUNDARY reasons** (per §6.1.4):

- Cluster-membership undecided (borderline)
- Homonymic / polysemic spread requiring sense-split
- Supportive / qualifying register

**Disposition options at Phase C.3 (per [feedback_boundary_resolution_required])** — exactly one per BOUNDARY term:

- **set_aside** — drop from cluster scope; `set_aside_reason` recorded; the verses still contribute to the term's semantic record per [feedback_setaside_verses_inform_word_meaning].
- **route-to-cluster-{code}** — re-route the term to another cluster; the term's verses follow.
- **move-to-substantive-sub-group** — promote to a substantive sub-group of the same cluster; the term joins as a normal STAYS member.

**BOUNDARY-pending is not valid cluster closure.** The Phase C.3 apply cannot run while any BOUNDARY term has no disposition. Phase F.2 validation check 8 confirms zero BOUNDARY_DECISION_PENDING flags.

---

## §15. Disposition vocabulary (canonical reference, carried from v2_9 §18)

| Term | Used in | Meaning |
|---|---|---|
| STAYS | B.1 verdict | Term's meaning corpus aligns with cluster characteristic; term remains |
| STAYS-with-flag | B.1 verdict | STAYS, with cross-register flag naming other-cluster relational dynamic |
| TRANSFERS-TO-{cluster} | B.1 verdict | Accidental placement; term moves to named cluster |
| BOUNDARY | B.1 verdict | Provisional; awaits Phase C disposition |
| set_aside | C.3 disposition | Term dropped from cluster scope |
| route-to-cluster-{code} | C.3 disposition | Term moves to named cluster |
| move-to-substantive-sub-group | C.3 disposition | Term promotes from BOUNDARY to a substantive sub-group |
| open | cluster_observation.status | Awaits handling by target_phase |
| confirmed | cluster_observation.status | Analytically validated by a later phase |
| refined | cluster_observation.status | Validated with substantive correction |
| deferred | cluster_observation.status | Held for post-closure handling (audit, publication revision, etc.) |
| 1:1 default | C.5 | One sub-group → one characteristic |
| volume-split | C.5 | One characteristic split across multiple sub-groups (§6.2.7 trigger) |
| SPLIT_SUBGROUP | C.5 | One sub-group serving two characteristics (rare) |

---

## §16. Pre/post controls — consolidated table

| Phase | Status pre | CC scripts | AI session | DB writes | Status post |
|---|---|---|---|---|---|
| **A.1** | `Not started` or `Data - In Progress` | UT classifier API | — | `verse_context.ut_class`, `is_relevant` | `Data - In Progress` |
| **A.2** | `Data - In Progress` | Pass A classifier API + keyword analytics build | — | `verse_context.meaning_pass_a`, `keywords` | `Data - In Progress` |
| **B.1** | `Data - In Progress` | constitution report gen + B.1 validator | constitution debate | — | `Data - In Progress` |
| **B.2** | `Data - In Progress` | sub-group meanings report + B.2 distribution validator | sub-group design | — | `Data - In Progress` |
| **B.3** | `Data - In Progress` | per-sub-group reports + B.3 unified-JSON validator | VCG design | — | `Data - In Progress` |
| **C** | `Data - In Progress` (B.3 gate PASS) | Phase C apply (all 5 ops in one transaction) | — | term transfers, sub-groups, VCGs, characteristics, inherited soft-deletes | `Structurally Ready` |
| **D** (per char) | `Structurally Ready` or `Analysis - In Progress` | per-char package builder + per-char loader | per-char findings | `cluster_finding` 189 rows | `Analysis - In Progress` |
| **D** (synthesis) | `Analysis - In Progress` | synthesis package builder + synthesis loader | cluster synthesis | `cluster_finding` 189 rows | `Analysis Complete` |
| **E** (per char) | `Analysis Complete` | per-char Phase E builder + tier-prose ingester | per-char tier prose | `prose_section` 8 rows | unchanged |
| **E** (synthesis) | `Analysis Complete` | synthesis Phase E builder + synthesis-prose ingester | cluster synthesis prose | `prose_section` 3 rows | `Publication Ready` |
| **F** | `Publication Ready` | validator + citation extractor + status flip | — *(conditional inherited-fold AI)* | `cluster_finding.characteristic_id` fold (conditional), `finding_citation` rows | `Closed` |
| **Pub** | `Closed` | assembler + PDF/DOCX renderer | — *(optional polish AI)* | none | unchanged |

---

## §17. Reports — input/output map (consolidated)

| Report | Owner | Builder | Consumer | When generated |
|---|---|---|---|---|
| `WA-{code}-keyword-analytics-v{V}-{date}.md` | CC | `scripts/_build_cluster_keyword_analytics_*.py` | B.2 input | end of Phase A |
| `WA-{code}-pass-a-summary-v{V}-{date}.md` | CC | `scripts/_build_pass_a_summary_*.py` | researcher review | end of Phase A |
| `wa-cluster-{code}-constitution-v{V}-{date}.md` | CC | `scripts/_generate_cluster_constitution_report_v1_*.py` | B.1 input | start of Phase B.1 |
| `WA-{code}-constitution-debate-v{V}-{date}.md` | AI | B.1 session | B.1 → B.2 gate + Phase C.1 | end of B.1 |
| `WA-{code}-subgroup-design-v{V}-{date}.md` + `-mapping-v{V}-{date}.json` | AI | B.2 session | B.2 → B.3 gate + Phase C.2 | end of B.2 |
| `WA-{code}-subgroup-meanings-v{V}-{date}.md` (per sub-group) | CC | `scripts/_build_subgroup_meanings_reports_*.py` | B.3 input | start of B.3 |
| `WA-{code}-{subgroup_code}-vcg-design-v{V}-{date}.md` (per sub-group) | AI | B.3 session | B.3 → C gate + Phase C.4 | end of each sub-group within B.3 |
| `WA-{code}-vcg-creation-v{V}-{date}.json` | AI | B.3 session | Phase C.4 | end of B.3 |
| `WA-{code}-phase-c-validation-v{V}-{date}.md` | CC | Phase C apply | researcher | post Phase C |
| `WA-{code}-phase-d-char{N}-{short}-findings-v{V}-{date}.md` | AI | Phase D char batch | Phase D char loader | per char batch |
| `WA-{code}-phase-d-cluster-synthesis-findings-v{V}-{date}.md` | AI | Phase D synthesis | Phase D synthesis loader | post all char batches |
| `WA-{code}-phase-e-char{N}-{short}-tier-prose-v{V}-{date}.md` | AI | Phase E char batch | Phase E ingester | per char batch (after Phase D char) |
| `WA-{code}-phase-e-cluster-synthesis-prose-v{V}-{date}.md` | AI | Phase E synthesis | Phase E ingester | post all char Phase E |
| `WA-{code}-phase-f-validation-v{V}-{date}.md` | CC | Phase F validator | researcher | pre status flip |

---

## §18. Patches and directives — content checklist

Every directive issued by AI for CC application must include the five required elements per [`wa-directive-instruction`](wa-directive-instruction.md) [current]:

1. **Required-inputs declaration** (§2 of directive) — brief, structural inputs, instruction docs, global rules, pre-decisions, out-of-scope.
2. **Out-of-scope statement** (§3).
3. **Pre-decisions** (§4) — any researcher-approved decisions the directive is acting on.
4. **Operations** (§5) — discrete SQL or script invocations with parameters.
5. **Post-checks** (§6) — verifiable outcomes the directive must achieve.

Phase C is the heaviest directive in v3_0 — one directive with 5 operations consolidated. AI does not issue Phase C; CC builds it from Phase B artefacts.

Phase D / Phase E directives are simpler — typically one directive per batch loader invocation (189 cluster_finding inserts or 8 prose_section inserts).

---

## §19. Post-closure compliance audit and surgical fix (carried from v2_9 §17)

After Phase F closure, the cluster is locked for normal pipeline operations. However, post-closure issues may emerge:

- A characteristic-mapping flaw discovered during publication review
- A BOUNDARY disposition that should have been different
- A finding error caught by cross-cluster correlation

The audit-and-fix flow:

1. **Audit** — researcher or CC identifies the issue; produces a corrective-actions plan.
2. **Surgical fix** — minimal-scope DB patch + obslog entry + re-validation.
3. **Re-validation** — Phase F validator re-run; if PASS, status remains `Closed`; if any check fails, cluster reverts to prior status pending fix.

Audit-driven fixes do **not** trigger Phase D / E re-run. They are surgical. A full rerun is reserved for substantive analytical re-design (rare).

For pre-v3_0 closed clusters with post-closure findings additions (e.g. M07 Terms Added), the audit-fix is the path. See [project_v25_audit_tool](../../C:/Users/lerouxc/.claude/projects/g--My-Drive-Bible-study-projects/memory/project_v25_audit_tool.md).

---

## §20. Status discipline

Cluster status under v3_0:

```
Not started
    ↓ (Phase A start)
Data - In Progress
    ↓ (Phase C apply)
Structurally Ready
    ↓ (Phase D first batch start)
Analysis - In Progress
    ↓ (Phase D synthesis complete)
Analysis Complete
    ↓ (Phase E full ingest)
Publication Ready
    ↓ (Phase F validation PASS)
Closed
```

For pre-v3_0 clusters at `Analysis Complete` (the v2_x terminal status), the transition path is `Analysis Complete` → `Publication Ready` via Phase E backfill → `Closed` via Phase F re-validation.

Status flips fire on phase exits (per [feedback_cluster_status_advance]) — the **first analytical write** for `Analysis - In Progress`; **all required writes complete** for the terminal statuses.

No cluster ever returns to an earlier status under v3_0 except via surgical fix (§19) with explicit reset.

---

## §21. Why v3_0 — the changes from v2_9

### §21.1 The two governing principles (codified)

GP-1 (verse meaning rules) and GP-2 (all observations recorded) were operational disciplines articulated in v2_5 / v2_8 but not formalised. v3_0 §2 codifies them at the top of the document; every phase reads them as gates.

### §21.2 Six phases instead of twelve

v2_9 ran Phase 1–12 + 8.5 + 8.7 = 14 named phases (with most sub-phases being silent CC or conditional). v3_0 collapses:

- v2_9 Phase 1+2 → v3_0 Phase A (single API-driven pass)
- v2_9 Phase 3+5+7 → v3_0 Phase B (B.1+B.2+B.3 staged, three AI sessions, three CC stage gates, single Phase C apply at end)
- v2_9 Phase 4+6+8+8.5+8.7 → v3_0 Phase C (single CC apply)
- v2_9 Phase 9 → v3_0 Phase D (findings only — prose moved to E)
- v2_9 Session C → v3_0 Phase E (findings-driven) + §11 CC assembly
- v2_9 Phase 10+11+12 → v3_0 Phase F (single CC validation + closure)

Phase B's **internal three-stage structure** preserves every v2_9 control (B.1 carries §6.3.1 + §6.3.2 disciplines; B.2 carries §8.4.1 + §8.6; B.3 carries §10.7 + §10.8 + §10.9). The v3_0 contribution is structural cleanliness, not control elimination.

### §21.3 Phase E as a separate, re-runnable, backfillable phase

The biggest publication-pipeline shift. v2_9 Session C re-read the verse corpus seven times per cluster (once per chapter). v3_0 Phase E reads the findings table (small, structured) once per characteristic per tier and writes to `prose_section`. Backfill is the same code path. Re-run after findings updates is the same code path. Assembly is CC-mechanical from the prose store.

Quantified saving: ~7 verse-corpus re-reads per cluster eliminated. Across the programme's remaining ~30 clusters × 7 characteristics, this is roughly 40M–200M tokens of avoided re-read.

### §21.4 CC cycle reduction

CC mechanical ops drop from 8 → 4 per cluster. Phase C consolidates four v2_9 CC ops; Phase F consolidates two v2_9 CC ops. The remaining CC ops (Phase A, per-Phase-D loader, per-Phase-E ingester, Phase F validator + assembler) are unchanged in nature but with cleaner boundaries.

### §21.5 What's not changing

- AI session count for the grouping work (Phase 3+5+7 = B.1+B.2+B.3 = 3 sessions). The cycle comparison v1 needs corrigendum on this point.
- The Phase D 189-prompt catalogue structure.
- The cluster_observation lifecycle (open → confirmed/refined/deferred).
- The BOUNDARY discipline.
- The science-extract requirement for Phase D batches.
- The tier-by-tier mandatory write-out discipline.

---

## §22. Change history

| Version | Date | Notes |
|---|---|---|
| v3_0 | 2026-05-27 | Initial v3_0. Supersedes v2_9. Six-phase structure; separate Phase E; CC assembly publication pipeline. Two governing principles codified. |
| v2_9 | 2026-05-26 | Phase 8 scaled down to silent CC soft-delete. |
| v2_8 | 2026-05-21 | Sub-groups represent characteristics; tier-by-tier mandatory for Phase 9. |
| v2_7 | 2026-05-20 | Verse-level relationship test for TRANSFERS. |
| v2_6 | 2026-05-19 | Characteristic mapping at Phase 8.7. |
| v2_5 | 2026-05-17 | Phase 8.5 BOUNDARY resolution; §17 audit-fix flow; BOUNDARY-not-a-parking-lot discipline. |
| v2_4 | earlier | Closed; M01 era. |
| (earlier) | various | See archived versions in `Workflow/archive/`. |

---

*v3_0 — 2026-05-27. Authoritative cluster-pipeline instruction. Cross-checked against v2_9 for completeness. Phase B internal structure derived from [phase-b control design](wa-v3_0-phase-b-control-design-v1-20260527.md). Cycle quantification derived from [v2_9-vs-v3_0 cycle comparison](wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md), corrected per §21.5.*
