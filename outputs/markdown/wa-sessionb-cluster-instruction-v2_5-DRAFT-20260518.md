# wa-sessionb-cluster-instruction-v2_5-DRAFT-20260518

> **DRAFT FOR APPROVAL** — Framework B Soul Word Analysis Programme — Session B Cluster Analysis
> Version: v2_5 (DRAFT) | Date: 20260518
> Status: **DRAFT — not the active instruction. v2_4 remains current until this draft is approved and re-filed at `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md`.**
> Governs (upon approval): Session B cluster work from session open through cluster closure
> Supersedes: wa-sessionb-cluster-instruction-v2_4-20260517 (will be archived to `Workflow/archive/` on approval)
> Governed by: wa-global-general-rules [current]
>
> **Change note v2_4 → v2_5 (2026-05-18):** Three structural corrections to the cluster pipeline and one post-closure compliance flow.
>
> **(1) Inner-being scope clarified** as the entire human inner life — no theological narrowing. §1.1 names the in-scope register families. §2.8 adds a no-spiritualisation contamination guard alongside the cross-cluster (§2.2) and inherited-structure (§2.3) guards. §4.5.1, §6.3.1, §8.4.1 codify forbidden grounds at the phases where the bias historically operated.
>
> **(2) BOUNDARY resolved before findings.** A new Phase 8.5 (§11.5) sits between Phase 8 (old-VCG dissolution) and Phase 9 (catalogue findings). Every BOUNDARY-pending decision resolves to one of three outcomes — SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP — before findings author. By the time Phase 9 runs, the corpus is structurally final. Phase 12 closure shrinks to two post-findings checks: every E-coded finding is evidence-grounded, and every prompt × scope cell has a row (nothing left out).
>
> **(3) Disposition vocabulary consolidated.** §18 replaces the previous standalone co-occurrence section with a canonical reference listing all disposition vocabularies in one place — term-level (Phase 3), verse-level (Phase 8.5 + audit-fix), and inherited-finding-level (Phase 10). Each phase section references §18 rather than redefining the vocabulary inline. Cross-cluster co-occurrence becomes a discipline reminder inside the ROUTE-TO-CLUSTER definition (§18.2): CC produces a simple "other-cluster terms at this verse_record_id" list as informational input to the routing decision; no structured AI assessment, no notes-prefix mechanism. Cross-cluster relationship findings remain captured by T6 catalogue prompts at Phase 9 (existing mechanism).
>
> **Post-closure clusters** that pre-date v2_5 are brought into alignment by a separate audit-and-fix flow (§17) — a deep audit script identifies compliance gaps against the current instruction; researcher approves a fix list; CC builds targeted fix directives. Cluster status stays `Analysis Completed` throughout.
>
> No schema changes. Uses existing tables for all operations.
>
> **Change note v2_3 → v2_4 (2026-05-17):** Phase 7 §10.7 staged write-out and §10.8 no-sampling pre-submission checklist codified. Previously the brief-level discipline learned from M01's context-pressure failures (and re-explained in M01–M04 briefs); now part of the master instruction. Trigger: M04 v1 Phase 7 had a 287-verse coverage gap in M04-A (43% of the sub-group unenumerated), 22 phantom/cross-cluster vc_ids, and a JSON that used `key_verses` samples instead of complete `verses` arrays — all symptoms of holding too much in working context before any disk write. The two new sub-sections make sub-group-by-sub-group writing + per-sub-group sum verification mandatory, with a pre-submission checklist of conditions CC validates.
>
> **Change note v2_2 → v2_3 (2026-05-17):** Phase 5 distribution hard gate added (§8.6). After AI delivers the Phase 5 sub-group mapping, CC runs `scripts/_validate_cluster_phase5_distribution_v1_20260517.py` to verify no substantive sub-group exceeds 40% of the cluster's substantive (non-BOUNDARY) verse corpus. If exceeded, Phase 5 is rejected and AI must re-submit with finer-grained splits. Phase 6 cannot proceed until validation passes. Trigger: M04 Phase 5 produced one sub-group (M04-A) absorbing 81% of substantive verses, forcing 10 VCG-level distinctions inside one sub-group at Phase 7 — work that should have happened at Phase 5. Benchmark across closed clusters: M01 35%, M02 47%, M03 33%. Threshold of 40% catches M02 retroactively (closed before gate; not re-opened) and M04 (gate added mid-pipeline; rework decision pending researcher).
>
> **Change note v2_1 → v2_2 (2026-05-16):** Phase 11 enhancements driven by M01 Phase 9 output. (1) VCG-level scope for `cluster_finding` rows — AI's Phase 9 output for M01 used 38 non-canonical scope markers like `[E-VCG-02]` and `[E-VCG-01/03/04/05]` when a finding applied to specific VCGs within a sub-group rather than the whole sub-group. Schema migration M48 adds a nullable `vcg_scope` column to `cluster_finding` and extends the UNIQUE constraint to include it. The loader stores VCG specificity as queryable structure rather than dissolving it into text (§14.4). (2) Phase 11 fold operation — for `wa_session_b_findings` rows marked `RESOLVED-BY-CATALOGUE` in Phase 10 (where the inherited finding's content is captured by one or more Phase 9 Tier findings), the loader appends the inherited observation's text to each named cluster_finding row's `finding_text` with audit prefix (§14.5). This implements the user's "ensure observation meaning is incorporated in the Tier findings" requirement. (3) New `validated_cluster_observation` status value for Session B findings that are M01-relevant but don't match any Tier question — a future-cluster placeholder; not exercised by M01. (4) Phase 12 closure §15 expanded with per-VCG anchor and prompt-coverage checks.
>
> **Change note v2_0 → v2_1 (2026-05-16):** Cluster-centric Phase 10 disposition catalogue. (Triggered by M01's Phase 10 output. Full text in v2_4 frontmatter — preserved on approval.)
>
> **Change note v1_13 → v2_0 (2026-05-15):** Major restructure of the cluster analytical flow. (Triggered by M01's three Phase 6 restarts. Full text in v2_4 frontmatter — preserved on approval.)
>
> Full history: see §24.

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

### 1.1 Scope clarification — what counts as "inner being" (added v2_5)

**The cluster pipeline analyses the entire human inner life.** Per the programme charter (`CLAUDE.md` §1: "the inner life of mankind") and the cluster overview's stated subject ("human inner being"), the scope is the full range of human interior states. There is **no implicit theological qualifier**.

In scope (non-exhaustive):

- **Vertical relational** — fear of God, love for God, joy in God, hope in God, anger at God.
- **Horizontal relational** — love for neighbour, anger at enemy, compassion for stranger, marital affection, parental delight.
- **Self-directed** — self-pity, self-control, self-loathing, self-confidence, inward grief.
- **Circumstantial / situational** — cheerful-heart-from-good-news, vexation-at-betrayal, gladness-of-harvest, weariness-of-old-age.
- **Moral-positive** — gentleness, patience, contentment, trust, humility.
- **Moral-negative** — envy, lust, pride, malice, deceit, predatory delight.
- **Illicit / corrupt** — seductress's pleasure, drunkard's mirth, predator's exultation, conqueror's gloating.
- **Material / sensory** — refined-luxury, pampered-ease, dainty-living, sensory enjoyment of food/wine/beauty.
- **Volitional / agentive** — "seems good to you" deference, willingness, reluctance, resolve.
- **Evaluative / appraisive** — "what is good", "what is fitting", "what is pleasing", "what is acceptable".

Out of scope:

- Pure historical narration with no human inner state evidenced.
- Genealogies, geographical descriptions, ritual procedure (where no inner state is named or implied).
- Divine attributes considered abstractly (when God's `chesed` is being analysed as inner-being-of-God, that is for the relevant cluster's scope; when `chesed` describes the act-toward-people without an interior reference, that is out of scope — case by case).

**The recurring mistake to eradicate:** treating "no clear God-directed framing" or "no obvious spiritual category" as grounds for SET-ASIDE / BOUNDARY. A pampered woman's refined ease under siege-curse (Deu 28:56), a parent's delight in a wise son (Pro 23:24), and a predator's gloating over the poor (Hab 3:14) are **all inner-being content**. They belong in substantive sub-groups, not in a parking lot.

See §2.8 (no-spiritualisation contamination guard) for how this applies during every phase.

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
- **Phase 8.5 (v2_5) — BOUNDARY disposition (per-verse decision)**

When a task is "look at this corpus and synthesise an analytical view", AI works in chat with free-form output. Applies to:

- Phase 3 — Constitution debate
- Phase 5 — Sub-group formation (the synthesis layer; per-row output may be derived)
- Phase 7 — VCG design within sub-groups
- Phase 9 — Catalogue prompts

The split is structural: AI's role is synthesis where synthesis is needed and atomic decisions where atomic decisions are needed. Mixing them in one phase produced the M01 failure.

### 2.8 No-spiritualisation contamination guard (added v2_5)

A third contamination guard, alongside §2.2 (cross-cluster) and §2.3 (inherited-structure):

**The bias to eradicate:** treating "inner being" as if it implicitly meant "God-directed inner being" or "theologically framed inner being." Across earlier cluster work (M01–M04), AI's synthesis steps consistently pushed pure-human inner-being content (parental delight, marital affection, refined luxury under judgment, predatory exultation, cheerful-heart-from-circumstance, illicit pleasure-seeking) toward BOUNDARY or set-aside on the implicit ground that they "lacked a clear spiritual link." That ground is **not a valid analytical reason**. The scope is the full human inner life (§1.1).

**Where the bias lives:**

- **NOT in Pass A meaning records (Phase 2).** Verse meanings authored by API-driven Pass A are neutral; they capture pure-human content faithfully. The foundational data is sound.
- **YES in Phase 1 classifier system prompts** if the example list given to AI is implicitly all-theological. Phase 1 prompt content must include pure-human examples (§4.2, §4.5.1).
- **YES in Phase 3 constitution debate** when BOUNDARY verdicts cite "no theological framing" rather than evidence-based reasons (§6.3.1).
- **YES in Phase 5 sub-group formation** when sub-groups are designed around the cluster's vertical/divine register and pure-human verses are pushed to BOUNDARY (§8.4.1).
- **YES in Phase 7 VCG design** when within-sub-group VCGs cluster around God-directed evidence and exclude pure-human evidence as "not VCG-worthy."
- **YES in Phase 8.5 BOUNDARY disposition** if SET-ASIDE is over-applied to pure-human content (§11.5.4 sanity-check guards against this).

**The corrective discipline:** at every synthesis step, the test for inclusion in a substantive sub-group / VCG / cluster_finding is **"is an inner-being state evidenced in this verse?"** — not "is the inner-being state of the right kind?" Vertical vs horizontal, divine vs human, illicit vs righteous, sensory vs spiritual: all are inner being. Sub-groups distinguish among them; none are excluded as a class.

---

## 3. Starting point — session open

Before any analytical work begins, the session opens in full compliance with the Session Startup Rule (`wa-global-rules-startup [current]`):

1. Obslog created with prefix `wa-obslog-{cluster_code}-{description}-v1-{YYYYMMDD}.md` and saved to `Sessions/Session_Clusters/{cluster_code}/`.
2. Obslog version incremented at every transition point — phases, sub-groups, terms.
3. If obslog writing is interrupted or discontinued, the session **must stop**. Recover the missing recordings first.

**Cluster status at session open:** `cluster.status` must be `Not started` or `Data - In Progress`. If `Analysis Completed`, no further pipeline phases fire — post-closure compliance work goes via the audit-and-fix flow (§17), which does not require a status change. If `Published`, any DB change requires explicit researcher direction.

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
   - System prompt: cluster characteristic statement + T1 framework + classification rubric (relevant / set_aside / borderline) + **the explicit in-scope examples block from §1.1** (added v2_5) + strict-JSON output spec.
   - Per-verse data: `vc_id_placeholder`, `verse_record_id`, `reference`, `strongs`, `transliteration`, `gloss`, `language`, `verse_text`, `context_before`, `context_after`, `translation`.
2. CC iterates batches against the Claude API. The system prompt is cached on the first call; subsequent calls read it at cache pricing.
3. CC parses each batch's JSON response, validates fields, captures the raw response.

**System-prompt rubric must include (added v2_5):**

> "Inner being covers the entire range of human interior states — vertical and horizontal, positive and negative, righteous and corrupt, sensory and volitional. A pampered woman's refined ease, a predator's exultation, a parent's delight, a seductress's pleasure, a soldier's gladness-of-victory, and a worshipper's joy in God are all inner-being content. Classify SET_ASIDE only when no inner-being state of any kind is evidenced in the verse; do not classify SET_ASIDE because the inner-being state appears non-theological."

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
- `_patch_meta.governing_instruction = "wa-sessionb-cluster-instruction-v2_5-20260518"` (on approval; until then, v2_4)
- Filename: `wa-cluster-{code}-patch-vcnew-utreview-api-v1-{date}.json`

Operation shape per op — see §A1 for the canonical field set.

### 4.5.1 Classifier-rubric forbidden grounds (added v2_5)

The Phase 1 classifier must not use any of the following as a reason for SET_ASIDE or BORDERLINE:

- "Not God-directed" / "no clear vertical framing"
- "Lacks theological depth" / "no spiritual category named"
- "Inner state too mundane" / "too circumstantial"
- "Inner state too negative" / "too corrupt to be inner being"
- "Inner state is bodily / sensory rather than spiritual"

The only valid reasons for SET_ASIDE:

- "No inner-being state evidenced — the verse describes external events / ritual procedure / geographic information / genealogy only."
- "The term in this verse refers to something other than an inner state (literal object, place, idiomatic phrase that does not invoke an interior state)."
- "Out-of-scope by design — the term/verse belongs to a different programme axis."

For BORDERLINE:

- "Inner-being state is implied but not directly stated; researcher decision needed."
- "Term has a metaphorical reading that may or may not invoke an inner state; researcher decision."

If AI returns a SET_ASIDE with a reason matching the forbidden list, CC rejects the row and re-runs the verse with an explicit reminder.

### 4.6 Post-check

- Every UT verse from the §1 count has a recorded determination.
- Every borderline has a one-line rationale in the review document.
- Every term in `terms_covered` either has ≥1 active anchor in `verse_context` post-apply, OR has no active relevant rows (all-set-aside / all-borderline state — legitimate per §6.5.5 of the VC standard).
- `mti_terms.vc_status` set to `vc_completed` for every term in `terms_covered`.
- **No SET_ASIDE rows carry a forbidden-grounds reason (§4.5.1).** CC sample-checks.

**DB writes:** the VCNEW patch.

**Cluster status:** unchanged (`Not started` or `Data - In Progress`).

---

## 5. Phase 2 — Pass A per-verse meaning record (CC, JSON template + API)

**Purpose:** every `is_relevant=1` `verse_context` row receives a one-line meaning written to `verse_context.analysis_note`. The meaning answers: **what does this verse say about the inner-being characteristic the term names, in this verse's specific context?** Sub-groups, VCGs, and inherited structure are not visible to AI during this phase.

**Owner:** CC. AI fills the `meaning` field in the JSON template.

### 5.1 Why this phase exists where it does

The verse-meaning is a function of `(verse, term)`, not `(verse, term, sub-group)`. It does not depend on whether sub-groups have been defined yet — and recording meanings before sub-groups form prevents the inherited-structure contamination that v1_13's Phase 6 Pass A could not reliably prevent. Phase 3 (constitution debate) then has access to the meaning corpus, not just the gloss list, when deciding which terms belong in the cluster.

**Pass A meanings are neutral by design (v2_5 note).** The §2.8 bias correction does NOT affect Pass A. The neutral-meaning rubric ("what does this verse say about the inner state the term names, in this verse's context") yields pure-human and God-directed meanings on equal footing. No re-running of Pass A is required when v2_5 amends the synthesis layer.

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

Structure (per §19 reports map):

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

### 6.3.1 Disallowed BOUNDARY reasons (added v2_5)

Per §1.1 and §2.8, BOUNDARY may **not** be assigned solely because:

- The term's meaning corpus is predominantly horizontal (human-to-human) rather than vertical (God-directed).
- The meanings describe sensory / material / circumstantial inner-being rather than overtly spiritual inner-being.
- The meanings include corrupt, illicit, or morally-negative inner-being content (predatory delight, lustful pleasure, etc.).
- The meanings describe an inner-being state the analyst would prefer not to be in scope.

A valid BOUNDARY verdict requires one of:

- **Cluster-membership undecided** — the term's meaning corpus is genuinely on the borderline between this cluster's characteristic and another's; transfer destination is unclear; researcher decision needed.
- **Homonymic / polysemic spread** — the term's meaning corpus covers two or more distinct registers and the term may need sense-split treatment before a cluster decision can be made.
- **Supportive / qualifying register** — the term's meanings describe a state that enhances or qualifies the cluster's characteristic without itself carrying it as a primary characteristic (e.g. an intensifier register that pairs with the cluster's primary inner-being content).

Every BOUNDARY verdict must name which of the three valid reasons applies. CC pre-checks at Phase 4 input parse; verdicts citing the disallowed grounds are returned for revision.

### 6.4 Output

- Constitution debate document: `Sessions/Session_Clusters/{code}/WA-{code}-constitution-debate-v1-{date}.md` — per-term verdict with rationale, decision summary table.
- Obslog entries per term.

### 6.5 Post-check

- Every term has a verdict (STAYS / TRANSFERS-TO-{cluster} / BOUNDARY).
- Every TRANSFERS verdict names a destination cluster with one-line justification.
- Every BOUNDARY verdict names the analytical question AND cites one of the three valid reasons (§6.3.1).
- No verdict is "validated against inherited VCGs" — verdicts are validated against meanings.
- No verdict cites a forbidden ground from §6.3.1.

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
- **§7.3.1 co-occurrence informational input has been generated** (added v2_5; informational only, see §7.3.1 and §18.2 ROUTE-TO-CLUSTER discipline).

### 7.3 Operation A — Term transfers (cross-cluster)

For each TRANSFERS verdict:

- `mti_terms.cluster_code` UPDATE from `'{source}'` → `'{destination}'`
- No verse_context, verse_context_group, or vcg_term updates required — these tables resolve cluster ownership through `mti_term_id → mti_terms.cluster_code` (no denormalised `cluster_code` columns).

### 7.3.1 Co-occurrence discipline (added v2_5)

A Phase 4 TRANSFERS verdict moves a whole term out of the cluster. Before approving the transfer the researcher should be aware of any other cluster's terms that co-occur with the transferring term in the same verses — this is informational input only; it does not gate the transfer.

**Mechanism:** CC produces a simple co-occurrence list — for each verse where the transferring term has a `verse_context` row, list other active terms (and their clusters) that also have a `verse_context` row at the same `wa_verse_records.id`. Output: `Sessions/Session_Clusters/{code}/WA-{code}-phase4-cooccurrence-list-v1-{date}.md`. No AI assessment, no structured prefix on notes, no veto power.

**How it is used:** the constitution-debate document (§6.4) and the Phase 4 directive's MOTIVATION reference the co-occurrence list when explaining the transfer rationale. If a high-co-occurrence verse pattern suggests the transferring term has secondary analytical value in the source cluster, the researcher may override the TRANSFERS verdict back to STAYS or to BOUNDARY for further analysis. **The capture of cross-cluster relationship findings is the responsibility of T6 catalogue prompts at Phase 9, not Phase 4** — both clusters' Phase 9 outputs can name the relationship via T6.6 (shared anchors), T6.4 (vocabulary/root sharing), or T6.1 (co-occurrence).

### 7.4 Operation B — BOUNDARY designation

For BOUNDARY terms, no Phase 4 DB write is required. The term remains in the cluster; its BOUNDARY sub-group assignment happens in Phase 5/6 when the sub-group structure is created. The Phase 3 obslog is the durable record.

### 7.5 Directive

Phase 4 produces one directive per source cluster (the cluster being analysed):

- Filename: `wa-global-dir-{seq}-{code}-term-transfer-v1-{date}.md`
- Pattern: cluster-process directive per `wa-directive-instruction [current]`
- Five-element form: MOTIVATION (cite constitution debate + §7.3.1 co-occurrence list), SCOPE (Operation A list of mti_id → new cluster_code), OUTCOME REQUIRED (counts per destination), COMPLETION CONFIRMATION (post-state queries showing source count, destination counts, BOUNDARY-set unchanged).

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

### 8.4.1 BOUNDARY is not a parking lot (added v2_5)

**The discipline:** BOUNDARY at Phase 5 carries only the verses of BOUNDARY-verdict terms (§6.3.1). It is **not** a holding pen for verses of STAYS-verdict terms whose meanings happen to lack God-directed framing.

If a STAYS-verdict term's corpus includes verses that describe pure-human inner-being (e.g. a parent's delight, a soldier's gladness, a worker's contentment, a seductress's pleasure), those verses go to a **substantive sub-group** — design a sub-group for them, name it appropriately (e.g. "horizontal joy", "circumstantial gladness", "corrupt delight"), and route them there.

**The forbidden pattern to eradicate:** designing the substantive sub-groups around the cluster's vertical/divine register, then routing the residual pure-human verses to BOUNDARY. This is the M04 v1 failure (81% biggest sub-group on vertical joy, residual to BOUNDARY) and the broader bias §2.8 addresses.

**Operational test (CC enforcement):** if BOUNDARY at Phase 5 holds more than 15% of the cluster's substantive verse corpus AND the BOUNDARY sub-group contains verses of terms that are NOT themselves BOUNDARY-verdict (i.e. residual verses of STAYS-verdict terms have been routed there), Phase 5 is rejected and re-submitted with explicit sub-group design for the residual content.

### 8.5 Post-check

- Every is_relevant verse is assigned to exactly one sub-group (or to BOUNDARY).
- Every sub-group has a `core_description` written from meanings.
- Multi-faceted terms are explicitly named (primary + secondary).
- BOUNDARY sub-group exists if Phase 3 produced any BOUNDARY verdicts.
- **BOUNDARY contains only verses of BOUNDARY-verdict terms (§8.4.1).** Residual verses of STAYS-verdict terms are routed to substantive sub-groups.

### 8.6 Distribution hard gate (added 2026-05-17 amendment, retained in v2_5)

**Purpose:** prevent under-decomposition at the sub-group level. A sub-group structure where one substantive sub-group absorbs the cluster's dominant register forces the granular analytical work to happen at the VCG level (Phase 7), producing 10+ VCGs in a single sub-group while the rest of the cluster sits thin. This was the M04 case (Joy/Rejoicing register at 81% of substantive corpus) and required Phase 5 rework.

**Rule:** no substantive sub-group may hold more than **40%** of the cluster's substantive (non-BOUNDARY) verses. If the threshold is exceeded, **Phase 5 is rejected and AI must re-submit** with finer-grained sub-group splits before Phase 6 can proceed.

**CC enforcement:** after AI delivers the Phase 5 mapping JSON, CC runs:

```bash
python scripts/_validate_cluster_phase5_distribution_v1_20260517.py --cluster {code}
```

Exit code 0 = PASS (proceed to Phase 6). Exit code 2 = FAIL (re-submit to AI).

The validator writes `WA-{code}-phase5-distribution-validation-v1-{date}.md` reporting:
- Per-sub-group verse counts and % of substantive corpus
- Biggest-to-next ratio (informational, threshold 3×)
- Benchmark across closed clusters (M01 35%, M02 47%, M03 33%)
- Verdict and required action

**Resubmission guidance for AI:** read the dominant sub-group's term meanings and identify the natural register-splits (vertical vs horizontal, divine vs human, communal vs individual, OT vs NT-distinctive, present vs eschatological, righteous vs corrupt, etc.). Each split producing ≥10 verses warrants its own sub-group.

**Researcher override:** the researcher may approve a Phase 5 mapping that fails the gate when corpus structure genuinely justifies it (e.g. cluster terms all belong to one register family with no meaningful inner splits). Override must be documented in the obslog with rationale. Default behaviour is reject.

**DB writes:** None in Phase 5.

**Cluster status:** unchanged.

---

## 9. Phase 6 — Verse-to-sub-group mechanical routing + per-sub-group report (CC)

*(Unchanged from v2_4. See v2_4 §9 — entire section preserved verbatim. Operations A/B/C/D apply the Phase 5 mapping; per-sub-group meanings report is generated for Phase 7.)*

### 9.1–9.8

Preserve v2_4 §9.1 through §9.8 unchanged. Section reference numbers stable.

---

## 10. Phase 7 — VCG design within sub-groups (AI, chat)

*(Unchanged from v2_4. v2_4 §10.7 staged write-out, §10.8 no-sampling checklist, §10.9 CC validation all retained verbatim.)*

### 10.1–10.9

Preserve v2_4 §10.1 through §10.9 unchanged. Section reference numbers stable.

---

## 11. Phase 8 — Dissolve old VCGs with researcher comparison report (CC)

*(Unchanged from v2_4. See v2_4 §11.)*

### 11.1–11.6

Preserve v2_4 §11.1 through §11.6 unchanged.

---

## 11.5 Phase 8.5 — BOUNDARY resolution pass (added v2_5)

**Purpose:** every BOUNDARY-pending decision (every term assigned to `{code}-BOUNDARY` in Phase 5, every `BOUNDARY_DECISION_PENDING` flag raised during Phases 3–8) is resolved to exactly one of three outcomes — SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP — **before Phase 9 catalogue findings author**. By the time findings run, the cluster's verse corpus is structurally final. **BOUNDARY-pending is not a valid pre-Phase-9 state.**

**Owner:** AI (per-verse disposition proposal) + researcher (approval) + CC (apply).

**Why this fires before Phase 9:** findings run against whichever verses are in which sub-groups. A BOUNDARY-pending verse skews the findings — it either appears as an undifferentiated BOUNDARY observation (low analytical value) or worse, gets parked invisibly. Resolving BOUNDARY before findings means Phase 9 sees the cluster the researcher actually intends.

For the canonical definition of each disposition (eligibility, DB effect, cross-cluster impact, findings impact), see **§18 — Disposition vocabulary**.

### 11.5.1 Inputs (CC produces)

1. **BOUNDARY content report**: `Sessions/Session_Clusters/{code}/WA-{code}-boundary-resolution-input-v1-{date}.md` — per BOUNDARY term, the full verse list with Pass A meanings, current `cluster_subgroup_id` (the `{code}-BOUNDARY` sub-group), current `group_id` if assigned.
2. **Co-occurrence list** (per §18.2): for every BOUNDARY verse, a simple list of other clusters' active terms occurring at the same `wa_verse_records.id`. Informational only — no AI assessment, no structured notes. Used to inform ROUTE-TO-CLUSTER decisions.
3. **Programme cluster catalogue**: every cluster's characteristic statement (so ROUTE-TO-CLUSTER targets are named correctly).
4. **Cluster's current sub-group + VCG structure**: so PROMOTE-TO-SUBGROUP targets can be named (existing sub-group or a newly-proposed one).
5. **The obslog** through Phase 8.

### 11.5.2 Process

1. CC builds the BOUNDARY content report and the co-occurrence list (§11.5.1).
2. AI reads each BOUNDARY term's verses and proposes a per-verse disposition with rationale, following the §18.2 verse-level vocabulary. Output: a JSON template (one row per BOUNDARY vc_id) plus a synthesis document grouping dispositions by term.
3. CC validates the disposition JSON: every BOUNDARY vc_id has exactly one disposition; ROUTE-TO-CLUSTER targets are valid cluster codes AND the target cluster has a term at the same `wa_verse_records.id` (§18.2 eligibility check); PROMOTE-TO-SUBGROUP targets are existing sub-group codes or clearly-labelled new ones.
4. **Researcher reviews** the synthesis document. Approves bulk, per-term, or per-verse; rejects return to AI.
5. CC builds the Phase 8.5 directive (§11.5.3) once approved.
6. CC applies the directive.

**Forbidden:** "PARK", "DEFER", or "RESEARCHER-DECISION-LATER" non-dispositions. Every BOUNDARY verse must receive one of the three. If AI cannot decide, the case surfaces to the researcher with a recommended disposition; the researcher's decision is then one of the three.

### 11.5.3 Directive

- Filename: `wa-cluster-{code}-dir-{seq}-boundary-resolution-v1-{date}.md`
- Operations (see §18.2 for the full DB-effect specification of each disposition):
  - **Op A — SET-ASIDE:** UPDATE `verse_context.is_relevant=0`, `set_aside_reason=?`.
  - **Op B — ROUTE-TO-CLUSTER:** UPDATE `verse_context.is_relevant=0` in the source cluster with `set_aside_reason='routed to {target_cluster} via {target_term}'`. The target cluster's existing `verse_context` row for the co-occurring term carries the verse for that cluster's analysis. No new INSERTs on the target cluster's vc table; no structured notes-prefix.
  - **Op C — PROMOTE-TO-SUBGROUP (existing target):** UPDATE `verse_context.cluster_subgroup_id`; INSERT `mti_term_subgroup` if the term doesn't yet link to the target sub-group.
  - **Op D — PROMOTE-TO-SUBGROUP (new sub-group):** INSERT `cluster_subgroup`; INSERT `mti_term_subgroup`; UPDATE `verse_context.cluster_subgroup_id`.
  - **Op E — VCG follow-on:** for promoted verses needing VCG assignment, either INSERT new VCGs (with anchor designation) or UPDATE `verse_context.group_id` to an existing VCG. Triggered when the §11.5.2 synthesis identifies a coherent VCG-worthy group of promoted verses. *(If the promotion target is an existing sub-group with an existing VCG that fits, this op is just an UPDATE; new VCGs are only created where the meaning corpus warrants.)*
  - **Op F — Clear BOUNDARY flags:** UPDATE every `wa_session_research_flags` row carrying `BOUNDARY_DECISION_PENDING` for this cluster's terms — set `resolved=1`, populate `resolved_note` with the disposition + directive id.
- Five-element form per `wa-directive-instruction [current]`.
- **Packaging:** one bundled directive carries all dispositions for the cluster (decided 2026-05-18). Failure-radius isolation (§2.5) does not apply — each disposition is a single-row UPDATE/INSERT and rollback is row-level. If bundled directives prove unwieldy in practice (large clusters, hook timeouts, slow apply, quality deterioration from oversized review surface), the researcher may direct a split. Initial testing on M04 will inform.

### 11.5.4 Post-check

```sql
SELECT COUNT(*) FROM wa_session_research_flags rf
JOIN mti_terms mt ON mt.id = rf.term_id
WHERE mt.cluster_code = '{code}'
  AND rf.flag_code = 'BOUNDARY_DECISION_PENDING'
  AND COALESCE(rf.resolved, 0) = 0;
```

Must return **0** before Phase 9 begins.

Additional post-checks:

- Every BOUNDARY vc_id (pre-Phase-8.5) has either been routed to a substantive sub-group, marked as routed to another cluster (`is_relevant=0` + `set_aside_reason` cites target), or set aside.
- The `{code}-BOUNDARY` sub-group either holds 0 active verses (`is_relevant=1`) OR holds only verses the researcher has explicitly approved to retain (rare; carries audit note).
- Disposition mix sanity-check: if >50% SET-ASIDE across a BOUNDARY term's verses, CC flags the term for researcher review (the §2.8 spiritualisation filter may be operating).

**DB writes:** the Phase 8.5 directive's Ops A–F.

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 12. Phase 9 — Catalogue prompts (AI, chat)

*(Unchanged from v2_4. See v2_4 §12.)*

### 12.1–12.8

Preserve v2_4 §12.1 through §12.8 unchanged.

---

## 13. Phase 10 — Inherited-finding reconciliation (AI then CC)

*(Unchanged from v2_4. See v2_4 §13.)*

### 13.1–13.6

Preserve v2_4 §13.1 through §13.6 unchanged.

---

## 14. Phase 11 — `cluster_finding` load (CC)

*(Unchanged from v2_4. See v2_4 §14.)*

### 14.1–14.6

Preserve v2_4 §14.1 through §14.6 unchanged.

---

## 15. Phase 12 — Cluster closure (CC)

**Purpose:** verify the cluster's database state, resolve any remaining gaps, transition `cluster.status` to `Analysis Completed`.

### 15.1 Inputs

- Post-Phase-11 DB state (cluster_findings loaded).
- Validation report from `scripts/_validate_cluster_completion_v1_*.py --cluster {code}`.

### 15.2 Pre-flight (CC) — two finding-quality checks only

By v2_5 design, all structural checks that could impact findings have run by Phase 8.5 (BOUNDARY resolution). Phase 12 closure therefore concentrates on **the two checks the researcher requires post-findings**: every finding is evidence-grounded, and nothing has been left out.

1. **Evidence-grounding (every E finding cites verses)** — every `cluster_finding` row with `finding_status IN ('finding','cluster_synthesis')` has at least one verse reference, VCG code, or anchor citation in `finding_text`. CC's check parses each row's text for the standard reference patterns (e.g. `Gen 22:12`, `M01-E-VCG-02`, `[A]` anchor markers) and counts. Rows failing the check are listed in the validation report; closure does not proceed until every E-coded row passes.
2. **Completeness (nothing left out)** — every prompt × scope cell from the Phase 9 catalogue has a corresponding `cluster_finding` row. CC's check joins `wa_obs_question_catalogue` × the cluster's sub-group set (plus CLUSTER scope) against `cluster_finding` and reports any missing cells. Genuinely-silent prompts must be recorded as `finding_status='silent'` rows, not absent rows.

The following structural pre-flight items carry forward unchanged (regression guards against pipeline misuse, all expected to pass by Phase 8.5):

3. C1 check (VC-coverage gaps) = 0 — every term has its verses fully classified.
4. C2 check (stale vc_status) = 0 — every term's `vc_status='vc_completed'`.
5. Every is_relevant verse has `group_id` (Phase 7) and `cluster_subgroup_id` (Phase 6 or Phase 8.5 promotion).
6. R4 anchor check passes for every term (≥1 active anchor).
7. H3=0, H4=0, H5=0, H6=0, H7=0 (Phase 6 and Phase 7 should have produced clean health).
8. `BOUNDARY_DECISION_PENDING` count = 0 (set by Phase 8.5 §11.5.4). If non-zero, Phase 8.5 has not completed and the pipeline is being run out of order.
9. The `{code}-BOUNDARY` sub-group holds 0 active verses, OR holds only verses explicitly retained by researcher decision at Phase 8.5.

### 15.3 BOUNDARY exit (already happened at Phase 8.5)

Per §16 and §11.5, BOUNDARY resolution is a Phase 8.5 activity. Phase 12 closure does not include BOUNDARY exit operations — by Phase 12, every BOUNDARY-pending decision was resolved BEFORE findings authored (the Q3 ordering rule). The `Flagged-for-decision` option used in v2_4 is removed in v2_5.

### 15.4 Closure directive

- Filename: `wa-cluster-{code}-dir-{seq}-closure-v1-{date}.md`
- Operations:
  - **Op A:** any final verification corrections (gap row updates, anchor fixes, vc_status sync). Targeted touch-ups only; not analytical work.
  - **Op B:** UPDATE `cluster.status='Analysis Completed', last_updated_date=?` WHERE `cluster_code='{code}' AND status='Analysis - In Progress'`.

### 15.5 Post-check

- `cluster.status = 'Analysis Completed'`.
- §15.2 checks 1 (evidence-grounding) and 2 (completeness) both clean.
- Validation script clean (C1=0, C2=0).
- All H-checks at expected baseline.
- `BOUNDARY_DECISION_PENDING` count = 0.
- All Session C downstream consumers can read the cluster.

The cluster is now ready for Session C cluster publication.

**Cluster status transition:** `Analysis - In Progress` → `Analysis Completed`.

---

## 16. BOUNDARY discipline (canonical reference)

BOUNDARY is **a temporary sub-group** used during Phases 3–8.5 for terms that:

- Are supportive / descriptive / qualifying — they enhance the cluster's verse evidence without themselves carrying a distinct inner-being characteristic.
- Are undecided — the constitution debate (Phase 3) flagged them for further evidence-based review.
- Are homonymic / polysemic — the term's meaning corpus spans multiple registers requiring sense-split treatment.

**BOUNDARY is not a parking lot for residual verses** of STAYS-verdict terms whose meanings lack God-directed framing. Per §1.1, §2.8, §6.3.1, and §8.4.1, such verses belong in substantive sub-groups.

### 16.1 Lifecycle in v2_5

| Phase | BOUNDARY state |
|---|---|
| 3 | Constitution debate may assign terms to BOUNDARY (Phase 3 verdict), citing one of the three valid reasons (§6.3.1) |
| 4 | Term-transfer directive does not move BOUNDARY terms; they remain in cluster |
| 5 | Sub-group formation creates the `{code}-BOUNDARY` sub-group with description. BOUNDARY contains only verses of BOUNDARY-verdict terms (§8.4.1) |
| 6 | Verse-to-sub-group routing places BOUNDARY-term verses in the BOUNDARY sub-group |
| 7 | BOUNDARY may have its own minimal VCG set (typically a single aggregating VCG) |
| 8 | Old VCG dissolution proceeds the same way for BOUNDARY-routed verses |
| **8.5 (v2_5)** | **Mandatory BOUNDARY resolution pass (§11.5). Every BOUNDARY-pending decision resolves to SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP per §18.2. Researcher-approved. Zero pending flags before Phase 9.** |
| 9 | BOUNDARY is empty (or carries only researcher-approved retentions). Phase 9 findings author against the post-resolution corpus, not a parked queue. |
| 10 | Inherited finding reconciliation runs against a finalised structure (no surprise BOUNDARY-term findings to fold in late) |
| 11 | `cluster_finding` load proceeds normally |
| 12 | Closure pre-flight verifies `BOUNDARY_DECISION_PENDING = 0` as a regression check (§15.2). The substantive Phase 12 work is evidence-grounding + completeness of findings. |

### 16.2 At cluster closure (Phase 12)

BOUNDARY does **not** persist as a holding pen, and is no longer a Phase 12 concern. Every BOUNDARY decision was already resolved at Phase 8.5 (§11.5) — before findings ran. The `Flagged-for-decision` exit from v2_4 is removed: parking a BOUNDARY decision with a flag is never a valid resolution.

---

## 17. Post-closure compliance audit and surgical fix (added v2_5)

**Purpose:** when the cluster instruction evolves (a new version is approved), clusters already closed under earlier versions may carry findings, verse routings, or published Session C sections that no longer reflect current methodology. §17 specifies the surgical-fix flow used to bring a closed cluster into compliance **without re-opening it**.

**Principle:** do not redo. Identify the specific items affected and update them in place. The cluster's sub-group structure, VCG design, and verse routing remain intact unless an audit finding requires a targeted change.

### 17.1 Audit trigger

The flow fires when the researcher directs an audit of a closed cluster against the current instruction version. Typical triggers:

- New instruction version published; researcher elects to bring closed clusters into alignment.
- A finding surfaced during a later cluster's analysis suggests a prior cluster has a compliance gap.
- An external evidence change (verse re-classification, term re-extraction) affects a closed cluster.

The flow does **not** fire automatically. It runs per cluster, per researcher direction.

### 17.2 Mechanism — three components

1. **Audit script** — `scripts/_audit_cluster_against_instruction_v{N}_{date}.py` (read-only). Reads the cluster's DB state, reads the current cluster instruction, and produces a compliance report listing items where the cluster does not conform. Output: `Sessions/Session_Clusters/{code}/WA-{code}-audit-against-v{N}-v1-{date}.md`.
2. **Researcher review and approval** — researcher reads the compliance report, decides which gaps warrant a fix, and approves the proposed fix list (a subset of the audit findings).
3. **Fix directive(s)** — CC builds one or more targeted directives (filename prefix `wa-cluster-{code}-dir-{seq}-audit-fix-{description}-v1-{date}.md`) and applies them. Each directive touches only the rows named in the approved fix list.

### 17.3 What the audit script checks

The audit is a comparison between the cluster's persisted state and the current instruction's discipline rules. The check list is updated alongside the instruction. At v2_5 the audit checks include (non-exhaustive):

- **BOUNDARY pending flags** — count of unresolved `BOUNDARY_DECISION_PENDING` flags against the cluster's terms. Closed clusters under v2_4 may have non-zero counts; v2_5 requires zero. Fix path: run §18.2 verse-level dispositions on the pending queue only (mirrors the Phase 8.5 mechanic).
- **Forbidden SET_ASIDE grounds (§4.5.1)** — verses set aside under reasons in the forbidden list (e.g. "no clear theological framing"). Fix path: RESCUE candidates returned for researcher review; approved verses are restored to `is_relevant=1` and routed per §18.2.
- **BOUNDARY parking-lot residue (§8.4.1)** — verses of STAYS-verdict terms parked in the `{code}-BOUNDARY` sub-group. Fix path: PROMOTE-TO-SUBGROUP on affected verses; new sub-group authored if no existing one fits.
- **Findings whose evidence cites only spiritualised content** — `cluster_finding` rows whose `finding_text` references only God-directed verses for a register that v2_5 §1.1 expects to include pure-human content. Surfaced for researcher review; finding revision is a researcher judgement.
- **Evidence-grounding regression** — `cluster_finding` rows with `finding_status IN ('finding','cluster_synthesis')` that carry no verse / VCG / anchor reference in `finding_text`. Mirrors the §15.2 check 1 — applied retroactively to clusters closed before v2_5 added that check.
- **Completeness regression** — prompt × scope cells from the Phase 9 catalogue with no `cluster_finding` row (genuinely-silent prompts must be recorded as `finding_status='silent'`, not absent). Mirrors §15.2 check 2.
- **Session C section dependencies** — for each finding flagged for revision, the audit report lists which Session C chapters cite that finding. Researcher decides whether re-publication of affected sections is in scope.

The full check list is maintained inside the audit script. Each check has a code (e.g. `AUDIT-V25-BOUNDARY-PENDING`, `AUDIT-V25-FORBIDDEN-SETASIDE`) so the compliance report uses stable references.

### 17.4 Compliance report structure

The audit script writes a single compliance report with these sections:

- §1 — Cluster identity (code, prior closure date, prior closure instruction version, current instruction version).
- §2 — Summary table: per audit-check code, count of affected items, severity (info / advisory / blocking).
- §3 — Per affected item: identifier (vc_id / finding_id / verse reference / etc.), the discipline rule violated (with §-ref to the current instruction), the proposed fix, the Session C sections that cite or depend on the item.
- §4 — Aggregated impact: list of cluster_findings flagged for revision and the Session C chapters affected.
- §5 — Proposed fix-directive bundle (a draft directive scope CC would write on approval).

The report is read-only. No DB writes happen at audit time.

### 17.5 Fix directives — discipline

Fix directives follow standard `wa-directive-instruction [current]` form. Specific to this flow:

- **Cluster status does not change.** Cluster stays `Analysis Completed`. Fix directives are explicitly tagged as audit-fix work in their MOTIVATION section.
- **Each fix directive is bounded.** A directive touches only the rows named in the approved fix list. Cross-section work (e.g. fixing 12 findings + 8 verse routings) may be one bundled directive or several, per the failure-radius isolation rule (§2.5).
- **Findings revision approach:** when a `cluster_finding` row's text needs updating, the default is **in-place UPDATE with audit prefix** — the row's `finding_text` is updated and the new text begins with `**[Audit-fixed under directive {id} on {date}; v{N} compliance]** {revised content}`. Researcher may direct **append-and-supersede** instead (soft-delete prior row + INSERT new versioned row); both paths are supported, choice recorded per fix directive.
- **Session C re-publication is not automatic.** The audit report lists affected Session C sections; researcher decides whether to re-publish. If re-publication is approved, the relevant Session C inputs are regenerated by their normal scripts.

### 17.6 What the audit-and-fix flow does NOT do

- Re-run Phase 2 Pass A meanings — they were neutral by design (§5.1) and remain valid.
- Re-run Phase 9 catalogue prompts wholesale — selective finding revision only.
- Transition `cluster.status`.
- Re-route verses whose disposition is sound under both prior and current methodology.
- Force Session C re-publication.

### 17.7 Output artefacts

| Artefact | Source | Location |
|---|---|---|
| Compliance report | Audit script | `Sessions/Session_Clusters/{code}/WA-{code}-audit-against-v{N}-v1-{date}.md` |
| Approved fix list | Researcher (annotated copy of compliance report) | `Sessions/Session_Clusters/{code}/WA-{code}-audit-fix-list-approved-v1-{date}.md` |
| Fix directive(s) | CC | `Sessions/Session_Clusters/{code}/wa-cluster-{code}-dir-{seq}-audit-fix-{description}-v1-{date}.md` |
| Applied report | CC | `Sessions/Session_Clusters/{code}/WA-{code}-audit-fix-{description}-applied-v1-{date}.md` |

The audit-and-fix flow does not produce its own obslog section — it adds entries to the cluster's existing obslog under a heading `audit-v{instruction-version}-{date}`.

---

## 18. Disposition vocabulary (canonical reference)

The cluster pipeline uses **three disposition vocabularies** at three different scopes. Earlier versions defined them inline at the phase that used them, which made it hard to compare and led to subtle drift. v2_5 consolidates them here. Phases reference this section rather than redefining their disposition options.

| Vocabulary | Scope | Used by phase | Defined in |
|---|---|---|---|
| Term-level | One disposition per cluster term | Phase 3 constitution debate | §18.1 |
| Verse-level | One disposition per BOUNDARY verse | Phase 8.5 (§11.5) and audit-fix (§17) | §18.2 |
| Inherited-finding-level | One disposition per inherited Session B finding | Phase 10 inherited reconciliation | §18.3 |

### 18.1 Term-level dispositions (Phase 3)

Set by AI during the constitution debate. One verdict per term:

| Disposition | Meaning | Cascade |
|---|---|---|
| **STAYS** | Term's meaning corpus aligns with this cluster's characteristic. | Term remains; sub-group placement decided at Phase 5. |
| **TRANSFERS** | Term's meaning corpus aligns with another cluster's characteristic. Destination cluster named with one-line justification. | Phase 4 rebinds `mti_terms.cluster_code` to destination. §7.3.1 co-occurrence list is informational input to the decision. |
| **BOUNDARY** | Term sits between clusters (cluster-membership undecided), or spans multiple registers (homonymic/polysemic), or qualifies the characteristic without itself carrying it (supportive register). One of three valid reasons must be cited per §6.3.1. | Term stays in cluster; verses route to `{code}-BOUNDARY` sub-group at Phase 5/6; **must be resolved at Phase 8.5 (§11.5)** per the verse-level vocabulary in §18.2. |

### 18.2 Verse-level dispositions (Phase 8.5 and audit-fix)

Set per verse during Phase 8.5 BOUNDARY resolution (§11.5) and during audit-fix (§17) when an audit surfaces a routing/set-aside that needs correction. One disposition per BOUNDARY vc_id; verses of the same term may receive different dispositions.

#### SET-ASIDE

- **Eligibility:** no inner-being state of any kind is evidenced in the verse, OR the term in this verse refers to something other than an inner state (literal place name, object, idiom that does not invoke interior life). Per §4.5.1, **"not God-directed" / "no theological framing" / "not spiritual" are NOT valid eligibility grounds.** Per §1.1, the test is "is an inner-being state evidenced?", not "is it spiritualised?"
- **DB effect:** UPDATE `verse_context` SET `is_relevant=0`, `set_aside_reason='{rationale citing valid §4.5.1 ground}'`.
- **Cross-cluster impact:** none. The verse simply does not belong in any cluster's analysis under the source-cluster's term.
- **Findings impact:** none directly. The verse no longer contributes to any sub-group / VCG / cluster_finding evidence under this term.

#### ROUTE-TO-CLUSTER

- **Eligibility:** the verse's primary inner-being content belongs to another cluster's characteristic, AND the target cluster has a term at the same `wa_verse_records.id` (because verse_context rows are keyed by (verse_record_id, mti_term_id); without a target term, the verse cannot be analysed by the target cluster). If no target-cluster term exists at the verse, the correct disposition is SET-ASIDE, not ROUTE-TO-CLUSTER.
- **DB effect (verse-level):** UPDATE `verse_context` (source cluster's row) SET `is_relevant=0`, `set_aside_reason='routed to {target_cluster} via {target_term}'`. The target cluster's existing `verse_context` row for the co-occurring term continues to carry the verse in that cluster's analysis. No new INSERT on the target side; no rebinding of `mti_terms.cluster_code` (the term stays in source cluster — only this verse's contribution under this term is removed).
- **DB effect (term-level, rare):** if every verse of a term in the source cluster is ROUTE-TO-CLUSTER to the same target, the whole term should arguably TRANSFER (Phase 3 / Phase 4). Phase 8.5 is not the place for whole-term transfers; if that pattern surfaces, surface to researcher for a re-opening of Phase 3 / Phase 4 verdict.
- **Co-occurrence discipline (the simpler form of the old §18):** CC produces a "co-occurring terms at this verse_record_id" list as informational input to the ROUTE-TO-CLUSTER decision (§11.5.1 input 2). The list answers: "if I route this verse out of M04, which target cluster's term is going to carry it?" The decision is a researcher-or-AI judgement, not a structured workflow. No `[XCO-...]` notes are written. **Cross-cluster RELATIONSHIP findings (the analytical observation "tov and chesed jointly express divine pleasantness") belong in T6 catalogue prompts at Phase 9 in BOTH clusters' findings, not in routing-time notes.**
- **Findings impact:** the verse is no longer counted in the source cluster's findings evidence base (it appears in the source's set-aside record, not in any E-coded finding). The target cluster's findings already include the verse via its own term. T6 prompts in either cluster may name the cross-cluster relationship if one exists.

#### PROMOTE-TO-SUBGROUP

- **Eligibility:** the verse carries genuine inner-being content for the source cluster's characteristic that was mis-parked in `{code}-BOUNDARY` at Phase 5. The PROMOTE target is either an existing substantive sub-group, OR a new sub-group whose `core_description` is authored at Phase 8.5.
- **DB effect (existing sub-group target):** UPDATE `verse_context.cluster_subgroup_id` to the promotion target. INSERT `mti_term_subgroup` if the term doesn't yet link to the target sub-group.
- **DB effect (new sub-group target):** INSERT `cluster_subgroup` (`subgroup_code`, `label`, `core_description`); INSERT `mti_term_subgroup`; UPDATE `verse_context.cluster_subgroup_id`. The §8.6 distribution gate is re-checked: if PROMOTE-TO-SUBGROUP creates a sub-group exceeding 40% of the substantive corpus, the Phase 5 design is structurally faulty and Phase 5 should be re-opened rather than absorbing it at Phase 8.5.
- **VCG follow-on:** if the promoted verses form a coherent VCG-worthy cohort, INSERT a new `verse_context_group` row and link via `vcg_term`. Otherwise UPDATE `verse_context.group_id` to an existing VCG within the target sub-group.
- **Cross-cluster impact:** none. The verse stays in the source cluster.
- **Findings impact:** Phase 9 catalogue findings will include the promoted verses naturally (Phase 8.5 fires BEFORE Phase 9 per Q3 ordering). New sub-groups will appear under T1.2.1 (sub-group structural description) when findings author.

#### What is forbidden

- "PARK", "DEFER", "RESEARCHER-DECISION-LATER", "WAIT", "PENDING" — none of these is a valid disposition. Every BOUNDARY verse must receive SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP before Phase 9 (or, at audit-fix time, before the fix directive closes).
- ROUTE-TO-CLUSTER without a target-cluster term at the verse — see eligibility above.

#### Disposition-mix sanity check (CC, automated)

If across a single BOUNDARY term's verses the disposition mix is >50% SET-ASIDE, CC flags the term for researcher review before the Phase 8.5 directive packages. The suspicion is the §2.8 spiritualisation filter is operating (treating pure-human content as set-aside-worthy). Mix is informational; researcher confirms or directs revisions.

### 18.3 Inherited-finding-level dispositions (Phase 10)

Set by AI during Phase 10 reconciliation. Vocabulary defined in §13.2 — unchanged from v2_4. Seven values: `RESOLVED-BY-CATALOGUE`, `FOLD-INTO-PROMPT`, `NEW-CLUSTER-FINDING`, `SUPERSEDED`, `ROUTE-TO-CLUSTER`, `CARRY-TO-SESSION-D`, `RESEARCHER-DECISION`.

**Vocabulary collision warning:** `ROUTE-TO-CLUSTER` appears in both §18.2 (verse-level) and §18.3 (inherited-finding-level). They are different operations on different objects:

- Verse-level ROUTE-TO-CLUSTER (§18.2): a single `verse_context` row is set is_relevant=0 in the source cluster because the verse's primary content belongs to another cluster.
- Inherited-finding-level ROUTE-TO-CLUSTER (§18.3 / §13.2): a `wa_session_b_findings` row's status is set to `routed_cluster` because the inherited finding's analytical content is the target cluster's responsibility.

Both keep the name because both ARE "this object belongs to another cluster" decisions. The DB effect is unrelated. The directive that applies each is different. The phase that authors each is different.

---

## 19. Reports — input/output map (consolidated)

The cluster reports produced by analytics scripts in `scripts/`. All read-only (with one documented exception — see §6.1), all re-runnable. Naming convention `wa-cluster-{code}-{kind}-v{N}-{date}.md`; version auto-bumps per script's `next_version` helper.

| Report | Script | Used in phase | Sections |
|---|---|---|---|
| UT verse review | `_run_{code}_ut_review_via_api_*.py` | 1 | Per-term counts, borderline list, applied-patch reference |
| Pass A meanings applied | `_apply_{code}_passa_meanings_*.py` | 2 | Per-batch counts, sample meanings, applied-patch reference |
| Constitution report | `_generate_cluster_constitution_report_v1_*.py` | 3 | §1 characteristic · §2 per-term meaning corpus · §3 cross-term signals · §4 cluster catalogue |
| **Co-occurrence list** *(new v2_5)* | `_build_cluster_cooccurrence_list_*.py` | 4 (transfers), 8.5 (BOUNDARY routing), audit-fix | Per source-cluster verse: list of other clusters' active terms at the same `wa_verse_records.id`. Informational input only — no AI assessment, no structured notes. |
| Per-sub-group verse + meaning | `_generate_subgroup_meanings_report_v1_*.py` | 7 | Per sub-group: verse list with (reference, term, meaning) |
| Grouped cluster (post-Phase-7) | `_generate_cluster_grouped_v1_*.py` | 9 | Cluster → sub-group → VCG → anchor + verses |
| Inherited findings for reconciliation | `_generate_cluster_inherited_findings_v1_*.py` | 10 | Per inherited finding: text + term + verse anchors |
| VCG dissolution comparison | `_generate_vcg_dissolution_comparison_v1_*.py` | 8 | Per inherited VCG: old text · new routing · disposition · side-by-side |
| **BOUNDARY resolution input** *(new v2_5)* | `_generate_boundary_resolution_input_*.py` | 8.5 | Per BOUNDARY term: verses + Pass A meanings + simple co-occurrence list + cluster catalogue + current sub-group/VCG structure |
| Findings | `_generate_cluster_findings_report_v1_*.py` | 11, 12 | Organised tier → component → prompt; one section per sub-group |
| Tiered prompts catalogue | `build_obs_catalogue_tiered_extract.py` | 9 | 189 prompts T0–T7 |
| Cluster science extract | _(researcher-prepared)_ | 9 | Per-cluster science extract at `Workflow/Sciences/`. Mandatory T7 input. |

**Report regen rule:** at the start of each phase that consumes a report, regenerate the report from the current DB state. Stale reports invite reasoning on outdated assumptions.

---

## 20. Patches and directives — content checklist

This instruction never authorises CC to write to the database directly. Every DB change is mediated by a patch (`wa-patch-instruction [current]`) or a directive (`wa-directive-instruction [current]`).

**Packaging is the default** (per §2.5). Status transitions (per §2.6) are operations within the relevant phase's directive — never their own directive.

**Routing for cluster work:**

| Operation | Method | Reason |
|---|---|---|
| UT-review inserts on `verse_context` | **Patch (VCNEW)** | Atomic per-row work; ID-resolved by CC's API runner; standard VC-family path |
| Pass A meaning UPDATE on `verse_context.analysis_note` | **Patch (VCREVISE)** | Per-row UPDATE; CC's Pass A apply script |
| Term transfers — `mti_terms.cluster_code` rebind | **Directive (Phase 4)** | §7.3.1 co-occurrence list is informational input only |
| Sub-group create + term link + verse routing + (status flip if not yet fired) | **Directive (Phase 6)** | Packaged: Ops A/B/C/D |
| VCG create + term link + verse-to-VCG routing + anchor designation | **Directive (Phase 7)** | Packaged: Ops A/B/C/D |
| Old VCG soft-delete | **Directive (Phase 8)** | Researcher-gated for early clusters; packaged |
| **BOUNDARY resolution (per-verse SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP + clear-flags)** *(new v2_5, fires BEFORE Phase 9)* | **Directive (Phase 8.5)** | Packaged: Ops A–F per §11.5.3. Verse-level disposition vocabulary in §18.2. |
| Inherited-finding reconciliation | **Directive (Phase 10)** | Per-finding disposition; packaged |
| `cluster_finding` load | **Directive (Phase 11)** | Two-step structural+full-text loader |
| Closure (verification corrections + status complete) | **Directive (Phase 12)** | Op A: targeted corrections only. Op B: status flip. Substantive checks at §15.2: evidence-grounding + completeness of findings. |
| **Post-closure audit fix (targeted finding/routing/section updates)** *(new v2_5)* | **Directive (audit-fix)** | §17; cluster status does not change |

**Filename:** `wa-cluster-{code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md` (or `wa-global-dir-...` for cross-cluster directives). Sequence numbers reset per cluster.

---

## 21. Pre/post controls — consolidated table

| Phase | Pre-check | Post-check |
|---|---|---|
| **1 UT review** | Cluster term set fixed; UT count enumerated | Every UT verse classified; provisional anchors enforced; `mti_terms.vc_status='vc_completed'` for processed terms; **no SET_ASIDE rows carry forbidden-grounds reasons (§4.5.1)** |
| **2 Pass A meanings** | Phase 1 complete; UT=0 | Every is_relevant active vc row has `analysis_note` populated; no group-label sentinels |
| **3 Constitution debate** | Phase 2 complete; constitution report regenerated; cluster status `Not started` or `Data - In Progress` | Every term has a verdict; **every BOUNDARY verdict cites one of the three valid reasons (§6.3.1)**; status transitioned to `Data - In Progress` |
| **4 Term transfers + BOUNDARY** | Phase 3 complete; **§7.3.1 co-occurrence list generated as informational input** | TRANSFERS applied; source cluster count = pre − transfers; status `Analysis - In Progress` if directive fired |
| **5 Sub-group formation** | Phase 4 complete; cluster term set stable | Every is_relevant verse has provisional sub-group; **BOUNDARY contains only verses of BOUNDARY-verdict terms (§8.4.1)**; §8.6 distribution gate passes |
| **6 Verse routing + per-sub-group report** | Phase 5 design + mapping JSON committed | `cluster_subgroup` rows created; `mti_term_subgroup` populated; verse_context.cluster_subgroup_id set; H4=0, H6=0 |
| **7 VCG design** | Phase 6 complete; per-sub-group verse+meaning report fresh | Every is_relevant verse routed to a new VCG; every VCG has an anchor; H3=0; R4 passes; §10.7/10.8/10.9 checks pass |
| **8 Old VCG dissolution** | Phase 7 directive applied; researcher reviewed comparison report | Inherited VCGs soft-deleted (except UNROUTED) |
| **8.5 BOUNDARY resolution** *(new v2_5, before Phase 9)* | Phase 8 complete; BOUNDARY content report + §11.5.1 co-occurrence list built | **`BOUNDARY_DECISION_PENDING` count = 0**; every BOUNDARY vc has SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP outcome per §18.2; `{code}-BOUNDARY` sub-group empty (or researcher-retained only) |
| **9 Catalogue prompts** | **Phase 8.5 complete; BOUNDARY = 0**; grouped report fresh; science extract loaded | 189 prompts × (sub-group + CLUSTER) answered; every E names a verse |
| **10 Inherited-finding reconciliation** | Phase 9 complete; CC's inherited-findings report produced | Every inherited finding has a disposition; researcher-decision items surfaced |
| **11 `cluster_finding` load** | Phase 10 complete; consolidated findings parts 1–4 final | `cluster_finding` rows match expected counts |
| **12 Closure** | Phase 11 complete; validation script clean | **§15.2 check 1 (evidence-grounding): every E finding cites verses**. **§15.2 check 2 (completeness): every prompt × scope cell has a row**. C1=0, C2=0; `cluster.status='Analysis Completed'` |

**A failed pre-check stops the phase.** A failed post-check stops the phase from being handed off.

---

## 22. Status discipline

Per the Session Startup Rule and `wa-claudecode-instruction [current]`, AI never tells CC the cluster is "complete" — completion is set by the researcher, on review of CC's confirmation outputs. AI's role is to deliver a directive whose Completion Confirmation queries demonstrate the outcome required.

CC's role is to execute the directive faithfully and return the confirmation. CC does not extend scope, interpret ambiguity, or apply analytical judgement (per `wa-directive-instruction [current]` §8.4).

---

## A1. Cluster-process tables — column reference (authoritative)

*(Unchanged from v2_4. See v2_4 §A1 — entire section preserved verbatim.)*

---

## 23. Why v2_0 — the M01 precedent

*(Unchanged from v2_4. See v2_4 §21.)*

---

## 24. Change history

**v2_5 (2026-05-18)** — Three structural corrections + one post-closure compliance flow.

- **Inner-being scope clarified** — entire human inner life, no theological narrowing. NEW §1.1; NEW §2.8 no-spiritualisation contamination guard; NEW §4.5.1 Phase 1 forbidden SET_ASIDE grounds; NEW §6.3.1 Phase 3 disallowed BOUNDARY reasons; NEW §8.4.1 BOUNDARY-is-not-a-parking-lot.
- **BOUNDARY resolved before findings** — new Phase 8.5 (§11.5) between Phase 8 and Phase 9. Every BOUNDARY decision resolves to SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP **before catalogue findings author**. §15 Phase 12 closure shrinks to two post-findings checks: evidence-grounding (every E finding cites verses) and completeness (every prompt × scope cell has a row). §15.3 removes the "flagged-for-decision" exit. §16 lifecycle updated.
- **Disposition vocabulary consolidated** — NEW §18 (replaces v2_5-draft's standalone co-occurrence section) lists all three disposition vocabularies in one place: term-level (Phase 3), verse-level (Phase 8.5 + audit-fix), inherited-finding-level (Phase 10). Each phase section references §18 instead of redefining inline. Cross-cluster co-occurrence reduces to an informational discipline inside §18.2 ROUTE-TO-CLUSTER: CC produces a "other-cluster terms at this verse_record_id" list; no structured AI assessment, no `[XCO-...]` notes. Cross-cluster RELATIONSHIP findings remain captured by T6 catalogue prompts at Phase 9 (existing mechanism).
- **Audit-and-fix for post-closure compliance** — NEW §17. Closed clusters are not re-opened on instruction upgrades; a read-only audit script identifies compliance gaps, researcher approves a fix list, CC applies targeted fix directives. Cluster status does not change.

No schema changes. Section renumbering from v2_4: §17→§19, §18→§20, §19→§21, §20→§22, §21→§23, §22→§24. (§18 itself is repurposed for the disposition canonical reference; the prior v2_4 §18 had no equivalent.)

**v2_4 (2026-05-17)** — Phase 7 §10.7 staged write-out and §10.8 no-sampling pre-submission checklist codified. Phase 5 distribution hard gate §8.6 retained from v2_3. Trigger: M04 v1 Phase 7 failure (287-verse coverage gap).

**v2_3 (2026-05-17)** — Phase 5 distribution hard gate (§8.6) added. Trigger: M04 Phase 5 v1 81% biggest sub-group.

**v2_2 (2026-05-16)** — Phase 11 VCG-level scope + fold operation; M01 Phase 9 driver.

**v2_1 (2026-05-16)** — Phase 10 cluster-centric disposition catalogue; M01 Phase 10 driver.

**v2_0 (2026-05-15)** — Major restructure. Pass A meanings (Phase 2) added; constitution debate moved to Phase 3 after meanings; sub-group formation Phase 5 after constitution; Pass C reconciliation removed; Phase 8 (CC) dissolves old VCGs with researcher comparison report; new Phase 10 reconciles inherited findings; JSON-template + API pattern for atomic per-row work.

**v1_13 (2026-05-14)** — §5.1.1 provisional-anchor convention (R4 satisfaction on VCNEW patches). M46 API-driven UT review precedent.

**v1_12 (2026-05-14)** — Phase 7 segmentation discipline.

**v1_11 (2026-05-14)** — Phase 7 directive segmentation ambiguity resolved.

**v1_10 (2026-05-14)** — M39-driven intra-day refinement.

**v1_9 (2026-05-14)** — Directive packaging discipline (§2.5) + status transition discipline (§2.6) established.

**v1_8 (2026-05-14)** — Streamlining audit cleanups.

**v1_7 (2026-05-13)** — §11.8 parser-safety rules; §10.4 `vcg_term` INSERT requirement.

**v1_6 (2026-05-13)** — Phase 2 patch type corrected to VCNEW; split-patch guidance.

**v1_5 (2026-05-13)** — Status-init ceremony retired; comprehensive-report-gen script handles transition inline.

**v1_4 (2026-05-12)** — Phase 1 status-init directive made explicit; Phase 8 science extract mandatory.

**v1_3 (2026-05-12)** — Major rework from M05/M06/M15/M26 lessons. Phase 6 VCG reconciliation rewritten as three-pass; BOUNDARY formalised; pre/post checks per phase.

**v1_2 and earlier** — see `Workflow/archive/`.

---

## Editorial notes for the draft (delete on approval)

This DRAFT is intentionally **not** the final published instruction file. On researcher approval:

1. The `(Unchanged from v2_4)` reference sections (§9, §10, §11, §12, §13, §14, §A1, §23) are expanded back to their full v2_4 text.
2. All [OPEN-Q-N] markers are now resolved. (Q1 Phase 8.5 directive packaging: **one bundled directive**, to be tested in practice — researcher may direct a split if quality deteriorates. Q2 and Q5 from the prior draft dropped earlier: Q2 with the §18 redesign, Q5 with the Q3 directive moving BOUNDARY before findings.)
3. The DRAFT frontmatter (status, file name) is updated for the canonical filename.
4. v2_4 is archived to `Workflow/archive/`.
5. The change-history block in §24 is finalised (date stays 20260518; "(DRAFT)" tag removed).
6. The companion changes-summary document is moved to `Workflow/archive/` alongside v2_4 for record.

**Sections deliberately abbreviated** (to be expanded verbatim on approval; the v2_4 text for these is unchanged):

- §9 Phase 6 (v2_4 §9, full text)
- §10 Phase 7 (v2_4 §10, full text — including §10.7, §10.8, §10.9)
- §11 Phase 8 (v2_4 §11, full text)
- §12 Phase 9 (v2_4 §12, full text)
- §13 Phase 10 (v2_4 §13, full text — unchanged)
- §14 Phase 11 (v2_4 §14, full text)
- §A1 Cluster-process tables (v2_4 §A1, full text)
- §23 Why v2_0 (v2_4 §21, full text)

These are unchanged by the v2_5 amendments and are abbreviated here to keep the DRAFT review readable. The full text remains valid and will be carried over on approval.

---

*End of v2_5 DRAFT. All researcher-decision items resolved. Awaiting line-level review then promotion to `Workflow/Instructions/`.*
