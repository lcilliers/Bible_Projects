# wa-sessionb-cluster-instruction-v2_8-20260519

> Framework B Soul Word Analysis Programme — Session B Cluster Analysis
> Version: v2_8 | Date: 20260519
> Status: **Active — authoritative instruction for Session B cluster analytics**
> Governs: Session B cluster work from session open through cluster closure
> Supersedes: wa-sessionb-cluster-instruction-v2_7-20260519 (archived to `Workflow/archive/`)
> Governed by: wa-global-general-rules [current]
>
> **Change note v2_7 → v2_8 (2026-05-19):** Phase 5 (sub-group formation) now explicitly states the **characteristic-as-objective** principle (NEW §8.0). Sub-groups are designed to represent characteristics (inner-being faculties/states); one sub-group per characteristic is the default; multiple sub-groups per characteristic is the documented volume-split exception triggered by §8.6 (40% distribution gate). Codifies the researcher direction post-M07 Phase 4 and the M04 retrofit precedent — where the retrofit at Phase 8.7 had to integrate sub-groups that had been clustered by raw meaning similarity without the characteristic frame. The upstream fix avoids the M04-style integration debate (4 iterations across 7 characteristics spanning 17 sub-group links). §8.2 process steps re-ordered to start from characteristic identification; §8.6 distribution gate reframed as the volume-split trigger rather than under-decomposition signal; §11B Phase 8.7 reduces from retrofit work to confirmation step. No schema changes.
>
> **Change note v2_6 → v2_7 (2026-05-19):** Phase 3 TRANSFERS verdicts now require an explicit **verse-level relationship test** (NEW §6.3.2). Codifies the researcher direction surfaced during M07 Phase 3 (v1→v2 revision): a term STAYS in the source cluster if any verse in its meaning corpus evidences a relationship with or impact on the source cluster's characteristic, even when the term's primary register lies elsewhere; the cross-register relationship is flagged in the rationale for Phase 5/7. TRANSFERS verdicts are confirmed only when no verse evidences any source-cluster relationship (accidental placement). Corpus-primary-register reasoning alone is no longer sufficient — it produced 8 false-positive transfers on M07 v1 that were corrected to STAYS on v1→v2 review. No schema changes.
>
> **Change note v2_5 → v2_6 (2026-05-19):** Characteristic-driven Phase 9. Three structural changes, codifying the M04 retrofit pattern (2026-05-18 to 2026-05-19, 1,512 cluster_finding rows landed).
>
> **(1) NEW Phase 8.7 — Characteristic mapping (§11B)** sits between Phase 8.5 (BOUNDARY resolution) and Phase 9 (catalogue findings). Sub-groups are now treated as **capacity organisers**; the **characteristic** (one or more sub-groups grouped under a single inner-being faculty/state) is the **evaluating unit** at Phase 9. AI proposes a characteristic map (iterative debate where needed — M04 took 4 versions); researcher approves; CC loads to three schema tables. Per researcher direction 2026-05-18: *"sub groups is purely a capacity organiser, the evaluating unit is the characteristic or group of sub groups."*
>
> **(2) Phase 9 (§12) restructured at characteristic scope.** Findings are authored per-characteristic (189 prompts × N characteristics, one batch per characteristic) and then in a final 8th cluster-synthesis session (189 prompts × CLUSTER + free-form prose appendix). Sub-group-scope findings are no longer authored as primary output — the prior `[A]/[B]/[C]` markers remain in the §12.4 catalogue for backward compatibility with pre-v2_6 closed clusters only. Multi-characteristic bundles permitted (one input file covering N characteristics with distinctly separated per-characteristic data blocks) but each batch is a self-contained 189-prompt pass against that characteristic's evidence only — no cross-batch evidence pooling. Per-batch DB load is now mandatory (each completed characteristic's findings are INSERTed to `cluster_finding` immediately via the parametric loader); Phase 11 (§14) reduces to validation + the inherited-findings fold operation.
>
> **(3) Schema additions M49 (3.22.0 → 3.23.0) and M50 (3.23.0 → 3.24.0):** new tables `characteristic`, `characteristic_subgroup` (M:N — one characteristic can span multiple sub-groups), `cluster_observation` (carry-forward observations with open → confirmed/refined lifecycle); `cluster_finding.characteristic_id` column with extended UNIQUE constraint allowing CHAR-scope and CLUSTER-scope rows to coexist per prompt. The §12.4 marker catalogue gains `**[CHAR-N]**` (characteristic-scope) and re-purposes `**[CLUSTER]**` for the cluster-synthesis 8th session only.
>
> **Closed clusters** (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46) need analogous characteristic mapping when revisited under the §17 audit-fix flow or for Session C revision — see §11B.6 backfill triggers. **M04 is the canonical worked precedent** (7 characteristics, 17 sub-group links, 4 carry-forward observations).
>
> **Operational artefacts (M04 retrofit, retained as templates):**
>
> - `scripts/_build_m04_characteristic_phase9_package_20260518.py` — single-characteristic builder
> - `scripts/_build_m04_characteristic_phase9_bundle_20260519.py` — multi-characteristic bundle builder
> - `scripts/_build_m04_phase9_cluster_synthesis_20260519.py` — 8th-session synthesis builder (per-prompt matrix; AI receives 7 characteristics' findings stacked per prompt)
> - `scripts/_apply_phase9_characteristic_findings_20260518.py` — per-batch loader, `[CHAR-N]` parser, 189-row gate
> - `scripts/_apply_phase9_cluster_synthesis_20260519.py` — cluster-synthesis loader, `[CLUSTER]` parser; splits prose appendix to standalone file
> - `scripts/_merge_phase9_segments_20260519.py` — parametric segment merger when AI splits a batch by tier-pair (T0+T1, T2+T3, T4+T5, T6+T7)
>
> **Change note v2_4 → v2_5 (2026-05-18):** Three structural corrections to the cluster pipeline and one post-closure compliance flow.
>
> **(1) Inner-being scope clarified** as the entire human inner life — no theological narrowing. §1.1 names the in-scope register families. §2.8 adds a no-spiritualisation contamination guard alongside the cross-cluster (§2.2) and inherited-structure (§2.3) guards. §4.5.1, §6.3.1, §8.4.1 codify forbidden grounds at the phases where the bias historically operated.
>
> **(2) BOUNDARY resolved before findings.** A new Phase 8.5 (§11A) sits between Phase 8 (old-VCG dissolution) and Phase 9 (catalogue findings). Every BOUNDARY-pending decision resolves to one of three outcomes — SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP — before findings author. By the time Phase 9 runs, the corpus is structurally final. Phase 12 closure shrinks to two post-findings checks: every E-coded finding is evidence-grounded, and every prompt × scope cell has a row (nothing left out).
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
- **YES in Phase 8.5 BOUNDARY disposition** if SET-ASIDE is over-applied to pure-human content (§11A.4 sanity-check guards against this).

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

### 6.3.2 Verse-level relationship test for TRANSFERS (added v2_7)

A **TRANSFERS-TO-{cluster}** verdict requires more than "the term's meaning corpus aligns primarily with another cluster's characteristic." Corpus-primary-register reasoning is too aggressive: it loses analytically-significant cross-cluster relationships when a term's primary register is elsewhere but its verses still evidence genuine relationships with the source cluster.

**The test, verse by verse:**

1. Read every verse in the term's meaning corpus.
2. For each verse, ask: *does this verse evidence any relationship with or impact on the source cluster's characteristic?* "Relationship" is broad and includes any of: direct evidence, structural opposite, instrument-of-the-characteristic, response-to-the-characteristic, protective-against, produced-by, in-tension-with.
3. The Pass A meaning is the input; read it for any source-cluster-relational content.

**The verdict rule:**

- If **any** verse evidences a relationship with the source cluster → **STAYS**, with a **cross-register flag** in the rationale that names the term's primary register destination and the source-cluster relationship across the corpus. The term stays in the source cluster; the flag travels with it.
- If **no** verse evidences any source-cluster relationship → **TRANSFERS-TO-{cluster}**, accidental placement.

**The cross-register flag** is consumed at Phase 5 (sub-group formation) and Phase 7 (VCG design): those phases can place the term in a sub-group or VCG that names the cross-register relationship; the flag also informs Phase 9 T6 (Structural Relationships with Other Characteristics) findings.

**Worked example (M07 v1 → v2 revision, 2026-05-19):**

- `G1848 exoutheneō` (to reject, 11 verses) — v1 verdict: TRANSFERS-TO-M06 (corpus primary register is contempt). v2 verdict: STAYS with cross-register flag to M06. Reason: every one of the 11 verses evidences contempt as the **active mechanism producing shame in the recipient** (Luk 18:9; Luk 23:11; Act 4:11; etc.). The contempt-shame dynamic is itself M07-relational content; the term sits in M07 with a flag noting the M06 primary register.
- `H2617B che.sed` (162 verses) — v1 verdict: TRANSFERS-TO-M05. v2 verdict: TRANSFERS-TO-M05 confirmed. Reason: across all 162 verses, every Pass A meaning names loyal love / steadfast love / covenant faithfulness; **no verse** evidences any M07 (shame) relational content. Accidental placement.

M07 v1 produced 10 TRANSFERS verdicts; v2 review revised 8 to STAYS with cross-register flags and confirmed 2 as accidental-placement transfers.

**CC pre-checks at Phase 4 input parse:** every TRANSFERS verdict's rationale must establish that no verse in the corpus evidences source-cluster relational content. Verdicts that justify transfer on corpus-primary-register grounds alone, without the verse-level test, are returned for revision.

### 6.4 Output

- Constitution debate document: `Sessions/Session_Clusters/{code}/WA-{code}-constitution-debate-v1-{date}.md` — per-term verdict with rationale, decision summary table.
- Obslog entries per term.

### 6.5 Post-check

- Every term has a verdict (STAYS / TRANSFERS-TO-{cluster} / BOUNDARY).
- Every STAYS verdict carrying a cross-register flag (per §6.3.2) names the term's other-register destination and the source-cluster relationship that justified retention.
- Every TRANSFERS verdict names a destination cluster with one-line justification AND passes the §6.3.2 verse-level relationship test (no verse evidences source-cluster relational content).
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

**Purpose:** form the cluster's sub-group structure such that sub-groups **represent characteristics** (inner-being faculties/states), grounded in the Phase 2 meaning corpus. Sub-groups emerge from the evidence, not from gloss-list interpretation.

**Owner:** AI (synthesis). CC produces the constitution report (already used in Phase 3) + a meaning-only listing for the now-stable term set, and applies the resulting directive in Phase 6.

### 8.0 Sub-groups represent characteristics (added v2_8)

The Phase 5 design objective is **structural**, not just analytical:

1. **A sub-group represents a characteristic** — a single inner-being faculty/state the cluster expresses. The default is **1 sub-group : 1 characteristic**.
2. **Volume-split is the documented exception.** When a single characteristic's verse corpus exceeds the §8.6 distribution gate (40% of substantive verses), the characteristic is split into multiple sub-groups by a documented split-axis (vertical vs horizontal, OT vs NT-distinctive, present vs eschatological, communal vs solitary, etc.). The characteristic identity is preserved across the splits; Phase 8.7 (§11B) will bind them back via `characteristic_subgroup` rows.
3. **A sub-group serving two characteristics (SPLIT_SUBGROUP) is rare and must be flagged.** It arises when the same lexical sub-group contains different VCG registers serving different characteristics (M04-E precedent: `sa.s.von` → Joy, `agalliao` → Suffering-Joy, in different VCGs of the same sub-group). At Phase 5 the AI flags this; at Phase 7 (VCG design) the registers are separated; at Phase 8.7 the SPLIT_SUBGROUP observation is recorded.
4. **Cross-register flags from Phase 3 (v2_7 §6.3.2) inform characteristic identification at Phase 5.** A term carrying a cross-register flag (e.g. `G1848 exoutheneō` flagged with M06-contempt while STAYS in M07-shame) suggests the cluster has a characteristic-shaped relationship the flag names; Phase 5 may design a sub-group around the relational dynamic (e.g. a contempt-producing-shame sub-group).

**Why this discipline (rationale from M04 retrofit, 2026-05-18):** the M04 retrofit at Phase 8.7 (§11B) had to integrate sub-groups that had been clustered by raw meaning similarity without the characteristic frame. The result was a 4-version characteristic-mapping debate spanning 7 characteristics across 17 sub-group links. Some characteristics (Joy, Delight) had to be reconstructed from 4–5 sub-groups each. M07 starts fresh under this v2_8 discipline — design sub-groups to represent characteristics from the start, and Phase 8.7 reduces to a confirmation step.

### 8.1 Inputs

- Updated constitution report (regenerated post-Phase-4 to reflect the now-stable cluster term set).
- Phase 3 verdict document, especially the cross-register flags (v2_7 §6.3.2) — these identify cluster-relational dimensions Phase 5 must accommodate.
- The obslog (through Phase 4).

### 8.2 Process

1. **Identify the characteristics the cluster expresses.** Read across the cluster's meaning corpus and name the distinct inner-being faculties/states present. A characteristic is a single answer to the question *"what specific inner-being faculty or state does this body of verses evidence?"* Aim for an analytically clean list — typically 3 to 8 characteristics per cluster.
2. **Map each characteristic to its evidence.** Note which terms' verses primarily evidence each characteristic.
3. **Design sub-groups to carry the characteristics.** Default: one sub-group per characteristic. Volume-split: if a characteristic's evidence corpus would exceed the §8.6 distribution gate, split it into multiple sub-groups by a named split-axis (recorded in each sub-group's `core_description`).
4. Name each sub-group with a `subgroup_code` and a one-paragraph `core_description` written from the meanings, naming the characteristic it represents (and the split-axis when applicable).
5. For each verse, record its sub-group assignment.
6. Note multi-faceted terms — terms whose verses span more than one sub-group. These get primary + secondary sub-group records.
7. Flag any SPLIT_SUBGROUP cases — sub-groups that on closer inspection contain VCG-level registers serving different characteristics (rare; flagged for Phase 7).

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

### 8.6 Distribution hard gate (added 2026-05-17, reframed in v2_8 as the volume-split trigger)

**Purpose under v2_8:** enforce the §8.0 volume-split provision. A sub-group that exceeds 40% of the cluster's substantive verse corpus signals that **its characteristic has too much verse volume to be handled as a single sub-group** — the characteristic must be split into multiple sub-groups by a named split-axis (per §8.0 rule 2). The same characteristic identity persists across the splits; Phase 8.7 binds them back via `characteristic_subgroup`.

(Prior framing — "under-decomposition" — was descriptive of M04 v1's failure mode but inverted the analytical frame. The right frame is: the cluster has a characteristic with substantial verse volume; that volume requires structural split into multiple sub-groups.)

**Rule:** no substantive sub-group may hold more than **40%** of the cluster's substantive (non-BOUNDARY) verses. If the threshold is exceeded, **Phase 5 is rejected and AI must re-submit** with the over-volume characteristic split across multiple sub-groups before Phase 6 can proceed.

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

### 10.7 Staged write-out (mandatory — AI workflow)

For each sub-group, processed sequentially in sub-group code order (M{NN}-A, M{NN}-B, ..., M{NN}-BOUNDARY):

1. **Read** every verse-meaning in the sub-group's section of the meanings report. Every row. No skipping.
2. **Design** VCGs and member assignments for that sub-group.
3. **Write the per-sub-group design document to disk immediately:**
   `Sessions/Session_Clusters/{code}/WA-{code}-{subgroup_code}-vcg-design-v1-{date}.md`
4. **Append obslog entries** for the sub-group's VCG decisions to the cluster obslog.
5. **Verify per-sub-group sum.** Sum the member vc_ids across the sub-group's VCGs. The total **must equal** the sub-group's verse count from the input meanings report. Record a verification line at the end of the sub-group document:

   ```
   **Verification**: VCG member sums = N1 + N2 + ... + Nk = TOTAL, matches M{NN}-{X} input count of TOTAL ✓
   ```

   If the sum does not match: identify which verses are missing or duplicated. Fix before moving on. Do not advance to the next sub-group until verification passes.

6. Move to the next sub-group; repeat steps 1–5.

After every sub-group is processed, write three additional artefacts:

7. **Unified VCG creation JSON** across all sub-groups: `Sessions/Session_Clusters/{code}/WA-{code}-vcg-creation-v1-{date}.json`. Top-level keys are sub-group codes; each contains a `vcgs` array. Every VCG has `provisional_code`, `description`, `verses` (complete array — not a sample, not `key_verses`), `anchor_vc_id` (must be a member of `verses`).
8. **Cross-routing flags document** (if any verses surfaced as needing routing review): `Sessions/Session_Clusters/{code}/WA-{code}-phase7-cross-routing-flags-v1-{date}.md`.
9. **Pre-submission checklist** verification (§10.8).

**Rationale:** AI working on a cluster with ≥500 verses is under context pressure. Holding 10+ sub-groups of design work in memory before any output produces sampling, omissions, and phantom vc_ids. Sequencing the work sub-group-by-sub-group, with mandatory disk write + sum verification after each, clears working context between sub-groups and produces durable artefacts even if a later sub-group needs re-attempting.

### 10.8 No-sampling pre-submission checklist

Before declaring Phase 7 complete, AI must verify each condition. CC will mechanically check every item on receipt; failures send Phase 7 back for resubmission.

- [ ] One design document per substantive sub-group + one for BOUNDARY (N files total = sub-group count). No combined documents.
- [ ] Each design document carries a sum-verification line per §10.7 step 5.
- [ ] Unified JSON file written with field name `verses` (not `key_verses`, not `members`, not "representative" anything). Complete arrays.
- [ ] Every `anchor_vc_id` is present in its VCG's `verses` array.
- [ ] Union of all `verses` across all VCGs in a sub-group equals the sub-group's input count from the meanings report.
- [ ] Total `verses` across the whole cluster equals the cluster's total is_relevant verse count.
- [ ] No vc_id appears in two different VCGs unless explicitly flagged as dual-membership in the design document.
- [ ] Every vc_id used in the output appears in the meanings report (i.e. is a M{NN} is_relevant vc, not invented, not from another cluster). CC validates by joining against the DB.
- [ ] BOUNDARY sub-group's aggregating VCG contains every is_relevant vc of every BOUNDARY term.

**Reading-discipline rule (absolute):** the meaning of every is_relevant vc in the input report must be read. No sampling. No "representative members." No "the rest follow the same pattern." The §10.7 staged write-out enforces this in practice; the §10.8 checklist verifies it on submission.

### 10.9 CC validation of Phase 7 output (before apply)

CC parses the unified JSON and verifies:

1. Every vc_id in the JSON exists in `verse_context` with `is_relevant=1`, `delete_flagged=0`, and `cluster_code` matching the cluster.
2. No vc_id appears in two VCGs (unless the design document explicitly flags dual-membership; CC records secondary VCGs in `verse_context.notes`).
3. Sum of `verses` per sub-group equals the DB's count of is_relevant vc rows routed to that sub-group at Phase 6.
4. Every `anchor_vc_id` is in its VCG's `verses`.
5. BOUNDARY-VCG-01 contains every BOUNDARY term's is_relevant vc rows.

If any check fails, Phase 7 is rejected and resubmitted to AI. CC builds a delta report naming the gap (missing vc_ids, phantom vc_ids, sum mismatches, anchor-not-in-members) and hands it back to AI as the resubmission input.

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

### 11.4.1 Dissolution directive

*(In v2_4 this sub-section was numbered §11.5. Renumbered to §11.4.1 in v2_5 because §11.5 is now occupied by Phase 8.5 — see §11A.)*

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

## 11A. Phase 8.5 — BOUNDARY resolution pass (added v2_5)

**Purpose:** every BOUNDARY-pending decision (every term assigned to `{code}-BOUNDARY` in Phase 5, every `BOUNDARY_DECISION_PENDING` flag raised during Phases 3–8) is resolved to exactly one of three outcomes — SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP — **before Phase 9 catalogue findings author**. By the time findings run, the cluster's verse corpus is structurally final. **BOUNDARY-pending is not a valid pre-Phase-9 state.**

**Owner:** AI (per-verse disposition proposal) + researcher (approval) + CC (apply).

**Why this fires before Phase 9:** findings run against whichever verses are in which sub-groups. A BOUNDARY-pending verse skews the findings — it either appears as an undifferentiated BOUNDARY observation (low analytical value) or worse, gets parked invisibly. Resolving BOUNDARY before findings means Phase 9 sees the cluster the researcher actually intends.

For the canonical definition of each disposition (eligibility, DB effect, cross-cluster impact, findings impact), see **§18 — Disposition vocabulary**.

### 11A.1 Inputs (CC produces)

1. **BOUNDARY content report**: `Sessions/Session_Clusters/{code}/WA-{code}-boundary-resolution-input-v1-{date}.md` — per BOUNDARY term, the full verse list with Pass A meanings, current `cluster_subgroup_id` (the `{code}-BOUNDARY` sub-group), current `group_id` if assigned.
2. **Co-occurrence list** (per §18.2): for every BOUNDARY verse, a simple list of other clusters' active terms occurring at the same `wa_verse_records.id`. Informational only — no AI assessment, no structured notes. Used to inform ROUTE-TO-CLUSTER decisions.
3. **Programme cluster catalogue**: every cluster's characteristic statement (so ROUTE-TO-CLUSTER targets are named correctly).
4. **Cluster's current sub-group + VCG structure**: so PROMOTE-TO-SUBGROUP targets can be named (existing sub-group or a newly-proposed one).
5. **The obslog** through Phase 8.

### 11A.2 Process

1. CC builds the BOUNDARY content report and the co-occurrence list (§11A.1).
2. AI reads each BOUNDARY term's verses and proposes a per-verse disposition with rationale, following the §18.2 verse-level vocabulary. Output: a JSON template (one row per BOUNDARY vc_id) plus a synthesis document grouping dispositions by term.
3. CC validates the disposition JSON: every BOUNDARY vc_id has exactly one disposition; ROUTE-TO-CLUSTER targets are valid cluster codes AND the target cluster has a term at the same `wa_verse_records.id` (§18.2 eligibility check); PROMOTE-TO-SUBGROUP targets are existing sub-group codes or clearly-labelled new ones.
4. **Researcher reviews** the synthesis document. Approves bulk, per-term, or per-verse; rejects return to AI.
5. CC builds the Phase 8.5 directive (§11A.3) once approved.
6. CC applies the directive.

**Forbidden:** "PARK", "DEFER", or "RESEARCHER-DECISION-LATER" non-dispositions. Every BOUNDARY verse must receive one of the three. If AI cannot decide, the case surfaces to the researcher with a recommended disposition; the researcher's decision is then one of the three.

### 11A.3 Directive

- Filename: `wa-cluster-{code}-dir-{seq}-boundary-resolution-v1-{date}.md`
- Operations (see §18.2 for the full DB-effect specification of each disposition):
  - **Op A — SET-ASIDE:** UPDATE `verse_context.is_relevant=0`, `set_aside_reason=?`.
  - **Op B — ROUTE-TO-CLUSTER:** UPDATE `verse_context.is_relevant=0` in the source cluster with `set_aside_reason='routed to {target_cluster} via {target_term}'`. The target cluster's existing `verse_context` row for the co-occurring term carries the verse for that cluster's analysis. No new INSERTs on the target cluster's vc table; no structured notes-prefix.
  - **Op C — PROMOTE-TO-SUBGROUP (existing target):** UPDATE `verse_context.cluster_subgroup_id`; INSERT `mti_term_subgroup` if the term doesn't yet link to the target sub-group.
  - **Op D — PROMOTE-TO-SUBGROUP (new sub-group):** INSERT `cluster_subgroup`; INSERT `mti_term_subgroup`; UPDATE `verse_context.cluster_subgroup_id`.
  - **Op E — VCG follow-on:** for promoted verses needing VCG assignment, either INSERT new VCGs (with anchor designation) or UPDATE `verse_context.group_id` to an existing VCG. Triggered when the §11A.2 synthesis identifies a coherent VCG-worthy group of promoted verses. *(If the promotion target is an existing sub-group with an existing VCG that fits, this op is just an UPDATE; new VCGs are only created where the meaning corpus warrants.)*
  - **Op F — Clear BOUNDARY flags:** UPDATE every `wa_session_research_flags` row carrying `BOUNDARY_DECISION_PENDING` for this cluster's terms — set `resolved=1`, populate `resolved_note` with the disposition + directive id.
- Five-element form per `wa-directive-instruction [current]`.
- **Packaging:** one bundled directive carries all dispositions for the cluster (decided 2026-05-18). Failure-radius isolation (§2.5) does not apply — each disposition is a single-row UPDATE/INSERT and rollback is row-level. If bundled directives prove unwieldy in practice (large clusters, hook timeouts, slow apply, quality deterioration from oversized review surface), the researcher may direct a split. Initial testing on M04 will inform.

### 11A.4 Post-check

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

## 11B. Phase 8.7 — Characteristic mapping (added v2_6; reduced to confirmation under v2_8 §8.0)

**Purpose under v2_8:** confirm and formally load the characteristic ↔ sub-group mapping that Phase 5 designed (§8.0). Under v2_6's introduction this phase did retrofit work — integrating sub-groups that had been clustered without the characteristic frame; under v2_8 Phase 5 bakes the frame in from the start, so Phase 8.7 reduces to: verify the mapping holds against the final (post-Phase-8.5) verse corpus, record any SPLIT_SUBGROUP observations flagged at Phase 5/7, and load `characteristic`, `characteristic_subgroup`, `cluster_observation` rows.

The remainder of §11B retains the M06-era language for backward compatibility with closed clusters (which need characteristic-mapping backfill per §11B.6).

**Purpose (legacy framing — applies to pre-v2_8 closed clusters):** identify the **characteristics** (inner-being faculties / states) the cluster's sub-groups jointly represent. A characteristic is the **evaluating unit** at Phase 9; a sub-group is a **capacity organiser** (a unit sized for analytical handling). One characteristic may span multiple sub-groups; in rare cases (e.g. M04-E in M04) a single sub-group may serve two characteristics in different VCG registers (the SPLIT_SUBGROUP pattern).

**Owner:** AI (proposal, iterative debate) + researcher (approval) + CC (load).

**Why this fires here:** Phase 5 (sub-group formation) and Phase 7 (VCG design) decompose the cluster for analytical handling — sized at ≤40% of substantive verses per sub-group (§8.6) and at coherent VCG units within each. But "what inner-being faculty does this sub-group express?" is a separate question from "is this sub-group analytically sized?" The characteristic map answers the first question after the second is settled. Without it, Phase 9 ends up applying the 189-prompt catalogue to capacity-units rather than evaluation-units, fragmenting findings that belong together (M04-L's cognitive-evaluative face and M04-O's circumstantial face are two faces of one Gladness characteristic; Phase 9 must see them as one).

> **Researcher direction 2026-05-18:** *"sub groups is purely a capacity organiser, the evaluating unit is the characteristic or group of sub groups."*

### 11B.1 Inputs (CC produces)

1. **Sub-group + VCG structural report** (post-Phase-8.5): every sub-group's `core_description`, member terms, member counts, VCGs with `context_description`. Same content as the Phase 8.5 grouped report but tightened to characteristic-mapping needs.
2. **Cluster constitution document** (output of Phase 3) — the cluster's overall characteristic statement, used to bound the map.
3. **Mapping brief** (`WA-{code}-characteristic-mapping-brief-v{N}-{date}.md`) — AI-facing brief specifying the task, decisions required, and discipline (one characteristic per faculty/state; M:N sub-group binding allowed; partial sub-groups must be flagged with VCG-level register notes).
4. **Mapping structural input** (`WA-{code}-characteristic-mapping-input-v{N}-{date}.md`) — the report bundled with the brief's required-inputs declaration.

### 11B.2 Process

1. **CC produces** the mapping brief + structural input (§11B.1, items 3–4) from the post-Phase-8.5 DB state.
2. **AI proposes** an initial characteristic map: name, definition (one-sentence inner-being statement), constituent sub-groups, qualifier-note per sub-group ("how this sub-group serves the characteristic"), and partial-register notes for SPLIT_SUBGROUP cases.
3. **Researcher reviews.** Common outcomes: accept; request refinement (e.g. "split this characteristic into two"; "this sub-group's evaluative face belongs with M04-O, not M04-G"); ask for analytical justification. **M04 took four iterations** before the researcher approved v4 — this is a normal range; the map is the foundation Phase 9 builds on, so iteration cost is recovered downstream.
4. **AI revises** until researcher signs off. The final approved map is the canonical `WA-{code}-characteristic-map-v{N}-{date}.md`.
5. **AI also produces** any carry-forward observations surfaced during the mapping debate — analytical hints that Phase 9 should attend to but cannot resolve at mapping time. Each observation has: title, description, target_phase (typically `phase_9_findings`), observation_type (INTER_RELATIONSHIP / INTEGRATION_NOTE / SPLIT_SUBGROUP / boundary or scope note), and may be linked to a specific characteristic or to the cluster.
6. **CC loads** the approved map + observations to three schema tables (§11B.3).

**Forbidden:** introducing new sub-groups, new VCGs, or new term placements at Phase 8.7. The map is an interpretation layer over the structurally-final corpus — not a re-shaping mechanism. If a mapping debate surfaces a Phase 5/7/8 structural problem, return to that phase rather than working around it at Phase 8.7.

### 11B.3 Schema (M49 + M50)

Three tables (M49, schema 3.22.0 → 3.23.0):

| Table | Columns (key) | Purpose |
|---|---|---|
| `characteristic` | `id`, `cluster_code`, `char_seq` (1-N), `short_name`, `definition` | One row per characteristic. `char_seq` is the canonical ordering within the cluster (typically by intensity, vocabulary breadth, or analytical centrality). |
| `characteristic_subgroup` | `characteristic_id`, `cluster_subgroup_id`, `qualifier_note`, `is_partial` (bool), `partial_register_note` | M:N join. `is_partial=1` flags SPLIT_SUBGROUP cases where the sub-group serves this characteristic in only some VCGs; `partial_register_note` names which register(s). |
| `cluster_observation` | `id`, `cluster_code`, `characteristic_id` (nullable), `cluster_subgroup_id` (nullable), `source_phase`, `observation_type`, `target_phase`, `title`, `description`, `status` (`open` / `confirmed` / `refined`), `resolution_note`, dates | Carry-forward analytical hints. Status advances `open` → `confirmed` / `refined` when the target phase's findings address it. |

One column added (M50, schema 3.23.0 → 3.24.0):

| Table | Column | Purpose |
|---|---|---|
| `cluster_finding` | `characteristic_id` (nullable FK to `characteristic.id`) | Characteristic-scope rows carry the FK; cluster-synthesis rows leave it NULL. UNIQUE constraint extended to `(obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope, version)` so CHAR-scope and CLUSTER-scope rows coexist per prompt. |

### 11B.4 Load

CC writes a per-cluster load script: `scripts/_apply_m{NN}_characteristic_observation_schema_and_{code}_load_{date}.py` (template: `_apply_m49_characteristic_observation_schema_and_m04_load_20260518.py`).

For the first cluster to use this phase, the script also applies the M49 + M50 migrations (one-time, idempotent — checks current schema_version before running). For subsequent clusters, the load script omits the migration steps and writes only the per-cluster rows.

### 11B.5 Post-check

- `SELECT COUNT(*) FROM characteristic WHERE cluster_code='{code}'` matches the approved-map count.
- Every sub-group with `is_relevant` verses is bound to at least one characteristic via `characteristic_subgroup`. The `{code}-BOUNDARY` sub-group (if it has any retained verses post §11A) is bound to a "Boundary" characteristic or explicitly noted as un-bound with researcher approval.
- Partial sub-groups (`is_partial=1`) carry a `partial_register_note` naming the VCG(s) that serve this characteristic.
- All carry-forward observations seeded with `status='open'` and `target_phase='phase_9_findings'` (or a different phase if the observation is intentionally deferred further).

### 11B.6 Backfill for closed clusters

Closed clusters (`status='Analysis Completed'` or similar) that pre-date v2_6 lack characteristic + characteristic_subgroup + cluster_observation rows. They are not re-opened on instruction upgrade; the backfill is triggered by:

1. **§17 audit-fix flow** — when an audit identifies a v2_6 compliance gap and the fix list includes characteristic mapping.
2. **Session C revision** — when a publication-ready cluster is revisited and needs the characteristic structure for the Session C narrative.
3. **Cross-cluster work** — when a project crosses M04 and a closed cluster and the synthesis requires comparable characteristic structures.

Backfill follows §11B.2 with one omission: no schema migration (M49 + M50 already applied). The load script writes the cluster's rows only. The mapping AI session uses the same brief + structural input templates as the M04 precedent.

Closed-cluster backfill **does not** re-run Phase 9 — the pre-v2_6 `cluster_finding` rows remain valid as sub-group-scope findings; the new characteristic structure provides the additional interpretation layer for Session C and cross-cluster work.

**DB writes:** the load script's INSERTs (characteristic, characteristic_subgroup, cluster_observation; one-time M49 + M50 if first cluster).

**Cluster status:** unchanged (`Analysis - In Progress`).

---

## 12. Phase 9 — Catalogue prompts (AI, chat)

**Purpose:** answer every prompt in the T0–T7 catalogue (189 prompts, v2.1) at **characteristic scope** for each of the cluster's N characteristics (one per-characteristic batch), then at **cluster scope** in a final 8th cluster-synthesis session. Every answer must be grounded in specific verse evidence or marked silent / gap. Findings are written to `cluster_finding` per batch as they complete (no longer accumulated for a Phase 11 bulk load — see §14 for the v2_6 role of Phase 11).

Under v2_6, Phase 9 fires against:

- A **structurally-final corpus** (BOUNDARY decisions resolved at Phase 8.5, §11A); and
- An **approved characteristic map** with carry-forward observations seeded (Phase 8.7, §11B).

Findings therefore describe the cluster the researcher intends, organised by the inner-being faculty/state each characteristic names, rather than by capacity-units (sub-groups).

### 12.1 Inputs (per batch)

Each AI session — whether single-characteristic, multi-characteristic bundle, or the 8th cluster-synthesis — is built by CC and includes:

1. **Brief** (`WA-{code}-phase9-char{N}-{short}-brief-v{V}-{date}.md` for single-char, `WA-{code}-phase9-bundle-char{seqs}-brief-…` for bundles, `WA-{code}-phase9-cluster-synthesis-brief-…` for the 8th session). Primary task instructions, including the required-inputs declaration (per [feedback_ai_package_self_declaration]).
2. **Structural input** — sibling file to the brief. Single-char: characteristic definition + sub-groups + VCGs + verses (with Pass A meanings) + 189-prompt catalogue. Bundle: per-characteristic data blocks distinctly separated (§2.A, §3.A, §2.B, §3.B, …) + shared catalogue. Synthesis: per-prompt matrix (one section per prompt showing the 7 characteristics' findings stacked verbatim from `cluster_finding`) + confirmed observations.
3. **Governing instruction** — this document (`wa-sessionb-cluster-instruction-v2_6-20260519.md`), §12 disciplines.
4. **Per-cluster science extract** — `Workflow/Sciences/wa-{code_lower}-{name}-scienceextract-v{V}-{date}.md` — **mandatory** input for every AI-facing Phase 9 package (single-char, bundle, and synthesis). Programme-curated scientific lens for T7.3 (human science framework) prompts. *Memorialised after Phase 9 v1 was built without it; the assumption "AI's general knowledge will suffice" was incorrect — every cluster has a curated science extract that must be loaded so framing stays consistent across clusters and reviewers.*
5. **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{date}.md` Ch.1 'Defining Inner Being'. Background.
6. **Global rules** — `wa-global-general-rules` [current]. Programme discipline.

The catalogue is reproduced inside the structural input (§4 of the per-char and bundle inputs); no separate catalogue file required.

### 12.2 Pre-check (before any Phase 9 batch fires)

- All Phases 1–8.5 complete and committed.
- `BOUNDARY_DECISION_PENDING` count = 0 (per §11A.4).
- Phase 8.7 characteristic map approved by researcher; rows present in `characteristic`, `characteristic_subgroup`; carry-forward observations seeded in `cluster_observation` with `status='open'` (per §11B.5).
- Schema at 3.24.0 or later (M49 + M50 applied).
- Science extract is present and current.

### 12.3 Two-stage process

**Stage A — per-characteristic batches.** For each characteristic (in `char_seq` order or any order the researcher prefers), one AI session runs the full 189-prompt catalogue against that characteristic's evidence only. Output: 189 cluster_finding rows with `characteristic_id={N}`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`.

**Stage B — cluster synthesis (8th session, after all N characteristic batches close).** One AI session runs the 189-prompt catalogue against all N characteristics' findings stacked (per-prompt matrix). Output: 189 cluster_finding rows with `characteristic_id=NULL`, `finding_status='cluster_synthesis'`; plus a free-form prose appendix capturing emergent themes that the 189-prompt structure cannot fully capture (saved as a standalone `-appendix-` file, not in DB).

### 12.4 Authoring discipline (parser-safe form)

Headers and scope markers must follow these rules so the per-batch loader can parse them:

1. **One scope marker per line.** Each `**[scope]**` marker starts at the beginning of a line.
2. **Every prompt must carry exactly one scope marker** (the marker matching the batch's scope). Mixing CHAR-N and CLUSTER markers within one batch is forbidden.
3. **One block per (prompt × scope).** Each (prompt, scope) cell appears at most once.
4. **Block separator.** A horizontal rule `---` on its own line marks the end of one prompt's findings.
5. **Outcome code inline.** The marker body starts with the outcome code: `E — `, `S — `, or `G — `.

Marker catalogue (v2_6, recognised by the loaders):

| Marker (as written by AI) | Used in | Loader produces |
|---|---|---|
| `**[CHAR-N]**` | per-characteristic batch (Stage A) | 1 row: `characteristic_id=N`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`, `finding_status` per outcome code (E→`finding`, S→`silent`, G→`gap`) |
| `**[CLUSTER]**` | cluster-synthesis 8th session (Stage B) only | 1 row: `characteristic_id=NULL`, `cluster_subgroup_id=NULL`, `vcg_scope=NULL`, `finding_status='cluster_synthesis'`; outcome E/S/G captured in `notes` |
| `**[A]**`, `**[A, B, C]**`, `**[E-VCG-02]**`, etc. | **pre-v2_6 only** — retained in the v2_2 loader for backward compatibility with closed clusters | sub-group-scoped row, `characteristic_id=NULL` (see §14.4) |
| `**[BOUNDARY — H1234 translit]**` | should not appear; Phase 8.5 eliminates BOUNDARY before findings | retained for pre-v2_5 closed clusters (see §14.4) |

The `[CHAR-N]` marker is **the only valid marker for new Phase 9 work** under v2_6. The other forms remain parseable so the loaders can ingest pre-v2_6 closed-cluster artefacts without modification.

Inline outcome codes — body must begin with one of:

- `E — text` → outcome `E`; loader sets `finding_status='finding'` (CHAR scope) or stores `outcome=E` in notes (CLUSTER scope, `finding_status='cluster_synthesis'`)
- `S — text` → outcome `S`; `finding_status='silent'` (CHAR scope) or `outcome=S` in notes (CLUSTER scope)
- `G — text` → outcome `G`; `finding_status='gap'` (CHAR scope) or `outcome=G` in notes (CLUSTER scope)

### 12.5 Per-characteristic batch flow (Stage A)

1. **CC builds the package** with `_build_{code}_characteristic_phase9_package_*.py` (single-char) or `_build_{code}_characteristic_phase9_bundle_*.py` (multi-char).
2. **AI runs the batch.** For each of the 189 prompts:
   - Read all the characteristic's verses (no sampling).
   - Author one finding. E findings must name the specific verses / VCGs / sub-groups within the characteristic that evidence the answer. S findings describe the analytical significance of the absence; G findings describe what data would be needed.
   - Mark the block with `**[CHAR-N]** {E|S|G} — …`.
3. **AI's self-check at end of batch.** Confirm 189 prompts answered; every E names evidence; carry-forward observations (open status) addressed; new analytical patterns surfaced.
4. **AI hands off** the findings file (or segments, see §12.7).
5. **CC merges segments** (if needed) and **applies via** `_apply_phase9_characteristic_findings_*.py --char-seq N`. The loader:
   - Parses 189 `[CHAR-N]` blocks (hard 189 gate; rejects partial)
   - Verifies all q_codes map to `obs_id`
   - UNIQUE-constraint preflight on `(obs_id, cluster_code, characteristic_id, NULL, NULL, version)`
   - INSERTs 189 rows
   - Post-verify confirms row count + outcome tally
6. **CC updates** `cluster_observation.status` for any observation the batch's self-check confirmed or refined (`open` → `confirmed` / `refined`; populate `resolution_note` with the analytical validation from the batch).
7. **Move to next characteristic.** Per researcher direction: *"each characteristic need to be completed and self checked per the current instructions before moving to the next."*

### 12.6 Cluster synthesis flow (Stage B — 8th session)

1. **CC builds the synthesis package** with `_build_{code}_phase9_cluster_synthesis_*.py`. The structural input is a per-prompt matrix: for each of the 189 prompts, the N characteristics' findings are stacked verbatim from `cluster_finding` (via DB query, not by reading the findings files).
2. **AI runs the synthesis batch.** For each prompt, read the N stacked characteristic findings, then author **one** cluster-scope finding examining what surfaces when the characteristics are compared (patterns, divergences, shared anchors). Mark with `**[CLUSTER]** {E|S|G} — …`. **Do not restate** per-char findings; the cluster-scope row is the integration across them.
3. **AI also writes** a free-form prose appendix (suggested 2,000–4,000 words) capturing emergent themes that the 189-prompt structure does not fully capture. Suggested themes (M04 precedent): Joy/Gladness boundary, SPLIT_SUBGROUP register-pairs, OT-NT vocabulary arcs, Spirit-constituted vs cultivated, christological convergence, communal vs solitary, eschatological orientation, inversions and corruptions.
4. **CC applies via** `_apply_phase9_cluster_synthesis_*.py`. The loader:
   - Detects the `## Appendix` heading and splits body vs appendix
   - Parses 189 `[CLUSTER]` blocks from body (hard 189 gate)
   - Writes appendix to a sibling `-appendix-` file (not in DB)
   - INSERTs 189 cluster-synthesis rows with `characteristic_id=NULL`, `finding_status='cluster_synthesis'`, outcome E/S/G in `notes`

### 12.7 Segmentation (when a batch is too large for one AI response)

When a per-characteristic batch (or the synthesis batch) exceeds a single AI response, segment by tier-pair using the canonical convention: **seg1 T0+T1 (36 prompts) · seg2 T2+T3 (64) · seg3 T4+T5 (45) · seg4 T6+T7 (44)**. Filename: `WA-{code}-phase9-char{N}-{short}-findings-seg{N}-T{x}T{y}-v{V}-{date}.md`.

CC merges the segments via `_merge_phase9_segments_*.py` (parametric) which:

- Strips per-segment headers
- Validates total prompt count
- Writes a canonical merged file
- Supports `--allow-partial` to merge incomplete sets (loader still rejects unless 189)

The synthesis batch's seg4 typically also carries the prose appendix; the merge handles that (the loader's appendix split kicks in downstream).

### 12.8 Carry-forward observations (lifecycle)

Each per-characteristic batch's brief carries the observations linked to that characteristic (and any cluster-wide observations whose description references the characteristic) — split between **OPEN** (action this batch) and **CONFIRMED (context only)** (validated by an earlier batch; included as analytical context the current batch may still need — the M04 SPLIT_SUBGROUP confirmed in Char 2's run was carried forward as context to Char 7's run).

At the end of each batch's self-check, the AI flags whether each OPEN observation surfaced as expected. CC updates `cluster_observation.status` to `confirmed` (analytical validation) or `refined` (validated with substantive correction); `resolution_note` captures the analytical content from the self-check; `resolved_date` populated.

By the time the synthesis session runs, all open observations should be confirmed or refined; the synthesis input's §2 surfaces them as direct inputs.

### 12.9 Self-check requirements (every batch)

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

**Self-tally is not authoritative.** AI's E/S/G counts have proven unreliable across M04's batches (consistent miscounting of buckets even when the total of 189 is correct). The loader's parse counts are the ground truth — CC reports the parser's numbers, not the self-tally, when summarising a batch.

### 12.10 DB writes (changed under v2_6)

Phase 9 now writes to `cluster_finding` **per batch** as findings arrive, via the parametric loaders (§12.5 for CHAR-scope, §12.6 for CLUSTER-scope). This replaces v2_5's pattern of accumulating findings as files for a bulk Phase 11 load. Rationale: per-batch loading lets CC run coverage checks between batches, confirm observations inline, and detect parser issues immediately rather than at the end of the cluster's Phase 9. Phase 11 (§14) is now reserved for the inherited-findings fold operation only.

### 12.11 Post-check (cluster-level, after both stages complete)

- `SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='{code}' AND COALESCE(delete_flagged,0)=0` returns **N×189 + 189** rows (N per-char batches + 1 synthesis = total).
- Every characteristic in `characteristic` for the cluster has exactly 189 `cluster_finding` rows.
- `SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='{code}' AND characteristic_id IS NULL AND finding_status='cluster_synthesis'` returns 189.
- Every E (CHAR-scope) finding's body names at least one specific verse or VCG.
- All `cluster_observation` rows are `confirmed` or `refined` (or explicitly deferred to later phases — `target_phase` updated to reflect the deferral).
- Synthesis appendix file written (1 standalone `-appendix-` file per cluster).
- No `[A]`, `[BOUNDARY ...]`, or `[E-VCG-XX]` markers in the new Phase 9 output (only valid for pre-v2_6 closed clusters).

**DB writes:** the per-batch INSERTs from §12.5 and §12.6 loaders.

**Cluster status:** unchanged (`Analysis - In Progress`).

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

For each inherited finding, AI assigns one disposition. See §18.3 for the canonical inherited-finding disposition vocabulary (consolidated in v2_5). The seven values:

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

## 14. Phase 11 — Inherited-finding fold + validation (CC)

**Purpose under v2_6:** apply the inherited-findings fold operation (§14.5) for any `RESOLVED-BY-CATALOGUE` rows that Phase 10's reconciliation flagged, then run cluster-level validation against the per-batch loads completed during Phase 9.

**Changed under v2_6.** Phase 11 no longer performs the primary `cluster_finding` INSERTs — those are done per batch during Phase 9 (§12.5 for per-characteristic, §12.6 for cluster-synthesis). Phase 11 reduces to two things:

1. The fold operation for inherited findings (§14.5) — unchanged from v2_2.
2. Cluster-level validation that the Phase 9 per-batch loads landed cleanly (row counts, evidence-grounding spot checks, observation-status sweep).

The v2_2 scope-marker resolution table (§14.4) is retained verbatim because it still applies to **pre-v2_6 closed-cluster ingestion** (when an audit fix needs to load legacy `[A]`/`[E-VCG-02]`/`[CLUSTER]` rows into a closed cluster's `cluster_finding`). For new Phase 9 work the loaders in §12.5 / §12.6 produce CHAR-scope and CLUSTER-scope rows directly per the v2_6 marker catalogue (§12.4).

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
| `[BOUNDARY — H1234 translit]` | 1 row: `cluster_subgroup_id=BOUNDARY.id`, `vcg_scope='term:H1234'` — *should not appear under v2_5 (Phase 8.5 eliminates BOUNDARY content before findings author); retained in the loader for backward compatibility with pre-v2_5 closed clusters* |
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
8. `BOUNDARY_DECISION_PENDING` count = 0 (set by Phase 8.5 §11A.4). If non-zero, Phase 8.5 has not completed and the pipeline is being run out of order.
9. The `{code}-BOUNDARY` sub-group holds 0 active verses, OR holds only verses explicitly retained by researcher decision at Phase 8.5.

### 15.3 BOUNDARY exit (already happened at Phase 8.5)

Per §16 and §11A, BOUNDARY resolution is a Phase 8.5 activity. Phase 12 closure does not include BOUNDARY exit operations — by Phase 12, every BOUNDARY-pending decision was resolved BEFORE findings authored (the Q3 ordering rule). The `Flagged-for-decision` option used in v2_4 is removed in v2_5.

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
| **8.5 (v2_5)** | **Mandatory BOUNDARY resolution pass (§11A). Every BOUNDARY-pending decision resolves to SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP per §18.2. Researcher-approved. Zero pending flags before Phase 9.** |
| 9 | BOUNDARY is empty (or carries only researcher-approved retentions). Phase 9 findings author against the post-resolution corpus, not a parked queue. |
| 10 | Inherited finding reconciliation runs against a finalised structure (no surprise BOUNDARY-term findings to fold in late) |
| 11 | `cluster_finding` load proceeds normally |
| 12 | Closure pre-flight verifies `BOUNDARY_DECISION_PENDING = 0` as a regression check (§15.2). The substantive Phase 12 work is evidence-grounding + completeness of findings. |

### 16.2 At cluster closure (Phase 12)

BOUNDARY does **not** persist as a holding pen, and is no longer a Phase 12 concern. Every BOUNDARY decision was already resolved at Phase 8.5 (§11A) — before findings ran. The `Flagged-for-decision` exit from v2_4 is removed: parking a BOUNDARY decision with a flag is never a valid resolution.

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

### 17.3.1 Audit verdict — surgical vs phase-restart

The audit's findings are aggregated into a verdict at one of two levels. **The verdict drives the response, not the fix.**

- **Surgical** — the non-compliance is localised: a few biased set-asides, a few BOUNDARY verses parked under disallowed reasons, a finding whose evidence base shifted. Surgical fix directives (§17.5) apply. The cluster stays `Analysis Completed` throughout.
- **Phase-restart** — the non-compliance is systemic and cannot be repaired in place. Pre-v2_5 closures often fall here: (a) Phase 1 SET_ASIDE classifications were made under forbidden grounds at scale; (b) Phase 3 BOUNDARY verdicts were issued for disallowed reasons across multiple terms (§6.3.1); (c) Phase 5 sub-groups don't cover register families that v2_5 §1.1 brings into scope. Surgical fixes cannot rebuild missing sub-groups or re-classify dozens of verses without effectively redoing the affected phase — the honest move is to restart from the earliest affected phase under v2_5 discipline.

The audit script writes the verdict in §1 of the compliance report (surgical / phase-restart / mixed). For a mixed verdict, the audit names which items are surgical and which need restart. The researcher decides which path to take — the verdict is a recommendation, not a binding instruction.

### 17.3.2 Phase-restart paths

When the audit recommends a phase restart, the cluster transitions via standard `cluster.status` values rather than a new state. The transition is part of a restart directive's MOTIVATION + Op N.

| Restart from | Status transition | Why |
|---|---|---|
| Phase 1 (UT classifier) | `Analysis Completed` → `Data - In Progress` | Re-classifying SET_ASIDE rows that cited forbidden grounds (§4.5.1). Pipeline re-enters at Phase 1; downstream phases run again. |
| Phase 3 (Constitution debate) | `Analysis Completed` → `Data - In Progress` | BOUNDARY verdicts re-issued under §6.3.1. Sub-group structure rebuilds from Phase 5. |
| Phase 5 (Sub-group formation) | `Analysis Completed` → `Analysis - In Progress` | Cluster's terms are stable; sub-group structure is re-designed to include register families v2_5 §1.1 brings into scope. |
| Phase 7 (VCG design) | `Analysis Completed` → `Analysis - In Progress` | Sub-groups stable; VCGs re-designed. |
| Phase 8.5 only | `Analysis Completed` → `Analysis - In Progress` | The most common path for pre-v2_5 closures: BOUNDARY queue resolves under §11A, then Phase 9 augmentation only for new sub-groups; existing findings stay unless the augmentation forces revisions. |

A phase-restart directive carries:

- **Op A — Backup** of every row that the restart will touch (per §17.5 audit-trail principle).
- **Op B — Status transition** per the table above.
- **Op C+ — Per-phase ops** to roll back the affected work (e.g., soft-delete sub-groups created from biased BOUNDARY verdicts; clear `cluster_subgroup_id` on affected `verse_context` rows) so the restart phase begins from a clean state.

The cluster's `version` field bumps on re-close (e.g. `v1` → `v2`).

**Restarts are not retroactive Phase 8.5 only.** When the audit verdict is "Phase 3 BOUNDARY verdicts were biased at scale", a Phase 8.5-only run cannot recover — the constitution debate itself produced verdicts that need re-doing. The honest path is the Phase 3 restart even though it costs more.

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
| Verse-level | One disposition per BOUNDARY verse | Phase 8.5 (§11A) and audit-fix (§17) | §18.2 |
| Inherited-finding-level | One disposition per inherited Session B finding | Phase 10 inherited reconciliation | §18.3 |

### 18.1 Term-level dispositions (Phase 3)

Set by AI during the constitution debate. One verdict per term:

| Disposition | Meaning | Cascade |
|---|---|---|
| **STAYS** | Term's meaning corpus aligns with this cluster's characteristic. | Term remains; sub-group placement decided at Phase 5. |
| **TRANSFERS** | Term's meaning corpus aligns with another cluster's characteristic. Destination cluster named with one-line justification. | Phase 4 rebinds `mti_terms.cluster_code` to destination. §7.3.1 co-occurrence list is informational input to the decision. |
| **BOUNDARY** | Term sits between clusters (cluster-membership undecided), or spans multiple registers (homonymic/polysemic), or qualifies the characteristic without itself carrying it (supportive register). One of three valid reasons must be cited per §6.3.1. | Term stays in cluster; verses route to `{code}-BOUNDARY` sub-group at Phase 5/6; **must be resolved at Phase 8.5 (§11A)** per the verse-level vocabulary in §18.2. |

### 18.2 Verse-level dispositions (Phase 8.5 and audit-fix)

Set per verse during Phase 8.5 BOUNDARY resolution (§11A) and during audit-fix (§17) when an audit surfaces a routing/set-aside that needs correction. One disposition per BOUNDARY vc_id; verses of the same term may receive different dispositions.

#### SET-ASIDE

- **Eligibility:** no inner-being state of any kind is evidenced in the verse, OR the term in this verse refers to something other than an inner state (literal place name, object, idiom that does not invoke interior life). Per §4.5.1, **"not God-directed" / "no theological framing" / "not spiritual" are NOT valid eligibility grounds.** Per §1.1, the test is "is an inner-being state evidenced?", not "is it spiritualised?"
- **DB effect:** UPDATE `verse_context` SET `is_relevant=0`, `set_aside_reason='{rationale citing valid §4.5.1 ground}'`.
- **Cross-cluster impact:** none. The verse simply does not belong in any cluster's analysis under the source-cluster's term.
- **Findings impact:** none directly. The verse no longer contributes to any sub-group / VCG / cluster_finding evidence under this term.

#### ROUTE-TO-CLUSTER

- **Eligibility:** the verse's primary inner-being content belongs to another cluster's characteristic, AND the target cluster has a term at the same `wa_verse_records.id` (because verse_context rows are keyed by (verse_record_id, mti_term_id); without a target term, the verse cannot be analysed by the target cluster). If no target-cluster term exists at the verse, the correct disposition is SET-ASIDE, not ROUTE-TO-CLUSTER.
- **DB effect (verse-level):** UPDATE `verse_context` (source cluster's row) SET `is_relevant=0`, `set_aside_reason='routed to {target_cluster} via {target_term}'`. The target cluster's existing `verse_context` row for the co-occurring term continues to carry the verse in that cluster's analysis. No new INSERT on the target side; no rebinding of `mti_terms.cluster_code` (the term stays in source cluster — only this verse's contribution under this term is removed).
- **DB effect (term-level, rare):** if every verse of a term in the source cluster is ROUTE-TO-CLUSTER to the same target, the whole term should arguably TRANSFER (Phase 3 / Phase 4). Phase 8.5 is not the place for whole-term transfers; if that pattern surfaces, surface to researcher for a re-opening of Phase 3 / Phase 4 verdict.
- **Co-occurrence discipline (the simpler form of the old §18):** CC produces a "co-occurring terms at this verse_record_id" list as informational input to the ROUTE-TO-CLUSTER decision (§11A.1 input 2). The list answers: "if I route this verse out of M04, which target cluster's term is going to carry it?" The decision is a researcher-or-AI judgement, not a structured workflow. No `[XCO-...]` notes are written. **Cross-cluster RELATIONSHIP findings (the analytical observation "tov and chesed jointly express divine pleasantness") belong in T6 catalogue prompts at Phase 9 in BOTH clusters' findings, not in routing-time notes.**
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
| **BOUNDARY resolution (per-verse SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP + clear-flags)** *(new v2_5, fires BEFORE Phase 9)* | **Directive (Phase 8.5)** | Packaged: Ops A–F per §11A.3. Verse-level disposition vocabulary in §18.2. |
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
| **8.5 BOUNDARY resolution** *(new v2_5, before Phase 9)* | Phase 8 complete; BOUNDARY content report + §11A.1 co-occurrence list built | **`BOUNDARY_DECISION_PENDING` count = 0**; every BOUNDARY vc has SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP outcome per §18.2; `{code}-BOUNDARY` sub-group empty (or researcher-retained only) |
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

The six tables touched by cluster-process directives. **Author directives by consulting this list, not by analogy from another table.** Column names differ across these tables in non-obvious ways.

### `cluster`

`cluster_code` (PK) · `description` · `gloss` (not null) · `source` · `bucket` · `status` · `version` · `last_updated_date` · `short_name`

### `cluster_subgroup` (Phase 6 — Operation A creates these; Phase 8.5 may INSERT new sub-groups under PROMOTE-TO-SUBGROUP)

`id` (PK) · `cluster_code` (not null) · **`subgroup_code`** (not null — e.g. `M01-A`, `M01-BOUNDARY`) · `label` (not null) · **`core_description`** · `sort_order` · `status` · `version` · `source` · `notes` · `delete_flagged` · `created_at` · `last_updated_date`

> BOUNDARY is identified by `subgroup_code` naming convention. There is no `is_boundary` column.

### `mti_term_subgroup` (Phase 6 — Operation B populates the term↔sub-group join; Phase 8.5 may INSERT new links under PROMOTE-TO-SUBGROUP)

`id` (PK) · `mti_term_id` (not null) · `cluster_subgroup_id` (not null) · `placement_note` · `delete_flagged` (not null) · `created_at` (not null) · `last_updated_date` (not null)

> There is no `mti_terms.cluster_subgroup_id` column. Term placement lives in this join table (m:n — a term may have multiple rows for multi-faceted sub-group membership).

### `verse_context_group` (Phase 7 creates new ones; Phase 8 soft-deletes old; Phase 8.5 may INSERT VCG follow-ons)

`id` (PK) · **`group_code`** (not null) · **`context_description`** (not null) · `notes` · `delete_flagged` · `vertical_pass_flag`

> No `cluster_code` column — VCG ownership resolves through `vcg_term → mti_terms.cluster_code`.

### `vcg_term` (Phase 7 — Op B; Phase 8 — Op B soft-deletes; Phase 8.5 may INSERT under VCG follow-on)

`id` (PK) · `vcg_id` (not null) · `mti_term_id` (not null) · `placement_note` · `delete_flagged` (not null) · `created_at` (not null) · `last_updated_date` (not null)

### `verse_context` (Phase 1/2/6/7 write; Phase 8.5 UPDATEs per §18.2 verse-level dispositions)

`id` (PK) · `verse_record_id` (not null) · `mti_term_id` (not null) · `group_id` · `cluster_subgroup_id` · `is_anchor` · `is_relevant` · `is_related` · `notes` · `delete_flagged` · `vertical_pass_flag` · `set_aside_reason` · **`analysis_note`** (per-verse meaning record — Phase 2)

> No `cluster_code` column — verse ownership resolves through `mti_term_id → mti_terms.cluster_code`.

> UNIQUE constraint: `(verse_record_id, mti_term_id, group_id, cluster_subgroup_id)` — applies regardless of `delete_flagged`. UPDATEs must include `delete_flagged=0` in WHERE to avoid colliding on soft-deleted duplicate rows.

### `mti_terms` (Phase 4 rebinds `cluster_code`)

`id` (PK) · `strongs_number` · `transliteration` · `gloss` · `language` · `owning_registry` · `owning_registry_fk` · `owning_word` · `owning_part` · `word_data_reference` · `word_data_ref_fk` · `status` · `exclusion_reason` · `extraction_date` · `strongs_reconciled` · `anchor_note` · `last_changed` · `delete_flagged` · `vc_status` · `vc_instruction_version` · `vc_status_updated_at` · `vc_status_note` · `md_version` · **`cluster_code`**

> No `cluster_subgroup_id` column on `mti_terms`. Sub-group placement is via `mti_term_subgroup`.

### `cluster_finding` (Phase 11 INSERTs; audit-fix may UPDATE/INSERT/soft-delete per §17)

`id` (PK) · `obs_id` (not null — FK to `wa_obs_question_catalogue.obs_id`) · `cluster_code` (not null) · `cluster_subgroup_id` · `finding_status` (not null — `finding`/`silent`/`gap`/`cluster_synthesis`) · `finding_text` · `source_file` · `version` · `notes` · `delete_flagged` · `created_at` · `last_updated_date`

> UNIQUE constraint: `(obs_id, cluster_code, cluster_subgroup_id, version)`.

### `wa_session_b_findings` (Phase 10 UPDATEs `status` + `resolution_note`)

`id` (PK) · `finding_id` · `registry_id` · `file_id` · `finding_type` · `finding` · `anchor_verses` · `raised_date` · `session_b_instruction` · `pass_ref` · `study_segment` · `delete_flag` · `obsolete_reason` · `obsolete_date` · `superseded_by_id` · `related_finding_id` · `resolution_note` · `thin_evidence` · **`status`** · `term_id` · `synthesis_outcome` · `tiers_engaged` · `structural_relationship` · `session_c_chapter` · `sd_pointer_ref`

> Phase 10 never DELETEs or INSERTs rows on this table — only UPDATEs `status` and appends to `resolution_note`. Row counts must remain unchanged per cluster's term set.

---

## 23. Why v2_0 — the M01 precedent

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

## 24. Change history

**v2_8 (2026-05-19)** — Phase 5 sub-groups represent characteristics. NEW §8.0 codifies the design objective: sub-groups carry characteristics 1:1 by default; volume-split into multiple sub-groups per characteristic is the documented exception driven by the §8.6 distribution gate; SPLIT_SUBGROUP (one sub-group serving two characteristics in different VCG registers) is the rare exception flagged at Phase 5 and resolved at Phase 7/8.7. §8.2 process reordered to start from characteristic identification rather than meaning-clustering. §8.6 distribution gate reframed as the volume-split trigger (the same 40% threshold; the analytical frame inverted from "under-decomposition" to "characteristic volume requires structural split"). §11B (Phase 8.7) reduced from retrofit work to confirmation step for new clusters; retains M04-style retrofit language for closed-cluster backfill. Triggered by researcher direction post-M07 Phase 4: codify the M04 retrofit logic upstream so future clusters skip the 4-version characteristic-mapping debate. No schema changes.

**v2_7 (2026-05-19)** — Phase 3 verse-level relationship test for TRANSFERS verdicts. Triggered by M07 Phase 3 (v1→v2 revision) where corpus-primary-register reasoning produced 8 false-positive transfers that the researcher's verse-by-verse review reversed to STAYS with cross-register flags. NEW §6.3.2 codifies the test: a term STAYS in the source cluster if any verse in its corpus evidences a relationship with the source cluster's characteristic (cross-register flagged); TRANSFERS confirmed only when no verse does. §6.5 post-check updated to require the verse-level test pass on every TRANSFERS verdict. M07 worked example included in §6.3.2: `G1848 exoutheneō` was the canonical v1→v2 reversal (contempt-shame relational pair); `H2617B che.sed` (162 verses, zero shame relational content) was the canonical TRANSFER-confirmed case. No schema changes; no section renumbering.

**v2_6 (2026-05-19)** — Characteristic-driven Phase 9. Codifies the M04 retrofit pattern (2026-05-18 to 2026-05-19, 1,512 cluster_finding rows landed across 7 characteristics + cluster synthesis).

- **NEW Phase 8.7 — Characteristic mapping (§11B).** Sits between Phase 8.5 and Phase 9. Sub-groups treated as capacity organisers; characteristic (one or more sub-groups under a single inner-being faculty/state) is the evaluating unit. AI proposes a map (iterative debate where needed — M04 took 4 versions); researcher approves; CC loads to `characteristic`, `characteristic_subgroup`, `cluster_observation` tables. Per researcher direction 2026-05-18: *"sub groups is purely a capacity organiser, the evaluating unit is the characteristic or group of sub groups."*
- **REVISED §12 — Phase 9 at characteristic scope.** Per-characteristic batches (189 prompts × N characteristics, `[CHAR-N]` marker) + a final 8th cluster-synthesis session (189 prompts × CLUSTER, `[CLUSTER]` marker, plus free-form prose appendix). Sub-group-scope findings no longer authored as primary output (the v2_2 `[A]/[B]/[C]` / `[E-VCG-XX]` markers retained in §14.4 for backward-compatibility ingestion of pre-v2_6 closed clusters). Multi-characteristic bundles permitted with strict per-batch isolation; per-batch DB load mandatory; Phase 11 reduces to inherited-findings fold + cluster-level validation. Self-tally flagged as unreliable; parser is ground truth (M04 evidence: 3-in-a-row miscounts where total 189 was correct but E/S/G buckets drifted).
- **Schema additions M49 + M50.** M49 (3.22.0 → 3.23.0) adds `characteristic`, `characteristic_subgroup` (M:N), `cluster_observation`. M50 (3.23.0 → 3.24.0) adds `cluster_finding.characteristic_id` with extended UNIQUE constraint so CHAR-scope + CLUSTER-scope rows coexist per prompt.
- **Science extract — mandatory required input.** Already noted in v2_5 §12.1, but elevated under v2_6 to mandatory in every AI-facing Phase 9 package (single-char, bundle, synthesis). Memorialised in [feedback_phase9_science_extract_required] after CC's earlier "no science doc exists" assessment proved wrong; one is curated per cluster at `Workflow/Sciences/wa-m{NN}-{short}-scienceextract-v*.md`.
- **Operational artefacts (M04 precedent, retained as templates):** `_build_m04_characteristic_phase9_package_*.py` (single-char builder), `_build_m04_characteristic_phase9_bundle_*.py` (bundle builder), `_build_m04_phase9_cluster_synthesis_*.py` (synthesis builder, per-prompt matrix from DB), `_apply_phase9_characteristic_findings_*.py` (per-batch loader), `_apply_phase9_cluster_synthesis_*.py` (synthesis loader with appendix split), `_merge_phase9_segments_*.py` (parametric segment merger).
- **Closed-cluster backfill (§11B.6).** M01, M02, M03, M05, M06, M15, M20, M26, M39, M46 need characteristic mapping when revisited; triggered by §17 audit-fix flow or Session C revision. Backfill omits M49 + M50 migration steps (already applied). Closed-cluster backfill does NOT re-run Phase 9; pre-v2_6 sub-group-scope findings remain valid.

No section renumbering. §11B inserted between §11A and §12 (same pattern as §11A's insertion at v2_5). §12 rewritten in place. §14 narrowed in scope. §24 prepended.

**v2_5 (2026-05-18)** — Three structural corrections + one post-closure compliance flow.

- **Inner-being scope clarified** — entire human inner life, no theological narrowing. NEW §1.1; NEW §2.8 no-spiritualisation contamination guard; NEW §4.5.1 Phase 1 forbidden SET_ASIDE grounds; NEW §6.3.1 Phase 3 disallowed BOUNDARY reasons; NEW §8.4.1 BOUNDARY-is-not-a-parking-lot.
- **BOUNDARY resolved before findings** — new Phase 8.5 (§11A) between Phase 8 and Phase 9. Every BOUNDARY decision resolves to SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP **before catalogue findings author**. §15 Phase 12 closure shrinks to two post-findings checks: evidence-grounding (every E finding cites verses) and completeness (every prompt × scope cell has a row). §15.3 removes the "flagged-for-decision" exit. §16 lifecycle updated.
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
