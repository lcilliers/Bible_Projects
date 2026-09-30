# Cluster-reading pipeline — full trace, dispatch to write

> Every stage, every config read (with live current value), every method rule (verbatim), every
> LLM instruction (verbatim), every input/output JSON shape, every validation/recording step,
> every status transition. Built by reading all 3,137 lines of the 9 files that make up this
> pipeline end to end — `run.py`, `handlers/lexical.py` (`meaning`), `handlers/cluster.py`
> (`subgroup`/`reading`/`answer`), `versereadinggenerate.py`, `subgroupgenerate.py`,
> `charreadinggenerate.py`, `charanswergenerate.py`, `recordingpass.py`, `clusterstatus.py` — not
> summarized from memory or from prior session notes.
>
> **Living document (escalation #1804, researcher instruction, verbatim): "this report stays
> assigned to you until the work in 1806 to fix the gaps are completed. This report must be
> continuiously updated for every new aspect of the verse-lexical work so I can use it as a 100%
> true reflection of the verse-lexical process... I do not make any decisions on this report - its
> yours to keep up to date."** Last updated 2026-09-21 — see Finding 4 (corrected), Findings 5–11
> (new), Finding 6's science-family correction (prose-grounded, escalation #1805), and Finding 11
> (full pipeline wiring audit — placement/payload/instructions/write-back, all 103 questions, plus
> the concrete code-level cause of Finding 6's M83 gap) for what changed since v2.

## Contents

- [0. Dispatch layer (`run.py`)](#0-dispatch)
- [1. Stage 1 — verse-reading (`lexical.meaning`)](#stage-1)
- [2. Stage 2 — char-subgroup (`cluster.subgroup`)](#stage-2)
- [3. Stage 3 — char-reading (`cluster.reading`)](#stage-3)
- [4. Stage 4 — char-answers (`cluster.answer`)](#stage-4)
- [5. The single writer (`recordingpass.py`)](#recordingpass)
- [6. The status machine (`clusterstatus.py`)](#clusterstatus)
- [7. Findings surfaced while tracing](#findings)
  - Finding 4 (corrected 2026-09-21) — precise Stage 1 mechanism + the authoritative,
    DB-validated catalogue coverage audit (escalation #1806)
  - Finding 5 (new, 2026-09-21) — `verse_lexical.role`/`is_negator`/`party_kind` were
    base-family-contaminated corpus-wide; fixed, rebuilt, verified; `governance.base_data_spine`
    extended

---

<a id="0-dispatch"></a>
## 0. Dispatch layer (`run.py`)

Every stage below is invoked as `python -m iba.app.run <work_package> --step <id> --run-id <id>
--param Key=Value`, landing in `run_step()`.

**Gates, in order, before any handler code runs** (`run_step`, lines 111–160):
1. `cfg.work_package_inactive(package)` — refuses if the work package is retired/unknown.
2. `cfg.step_inactive(package, step_id)` — refuses if the step is retired/unknown.
3. `cfg.step_kind(package, step_id) is None` — refuses if the step has no `operations`/`utility`
   classification in `cfg_step.kind`.
4. A fourth gate (`cfg_escalation.module_blocking` — refuse if an unresolved escalation exists for
   this step/module) is **present in the code but commented out**, disabled 2026-08-26 per direct
   researcher instruction (escalation #859: the gate was blocking routine dispatch often enough
   that routing around it, not resolving the module, had become normal — "there is now such an
   accumulation of errors and bugs that this control is null"). Not re-enabled without a redesign.

All four live steps below (`lexical.meaning`/`cluster.subgroup`/`cluster.reading`/`cluster.answer`)
are registered `kind='operations'`, not inactive — confirmed live, gates 1–3 pass.

**Then**: `Ctx` is built (`db`, `cfg`, `step`, `run_id`, `word`, `word_id`, `params`, `step_id`),
the handler function named in `cfg_step.handler` is resolved and called with that `Ctx`.

**On an uncaught exception**: the transaction is rolled back FIRST (a fix for a real bug found
2026-08-06 — an in-process crash used to leave the crashed handler's own partial writes committed),
then a `self_correctable` escalation is raised recording the traceback, `run.state` is set
`'failed'`, and the exception is re-raised — the crash is never silently swallowed.

**On a returned `Outcome`**: the `condition` is resolved to a `path` via `cfg_on_fail[step_id,
condition]` (`'ok'` needs no rule). A `decision_required` escalation is always reassigned to
`report-stop` regardless of its originally-configured path (escalation #798/#799 SS5) — so it
always returns a terminal exit code, never "paused resumably". Exit codes: `ok`/`report-continue`/
`self-heal` → 0, `pause-continue` → 2, `report-stop` → 3, an uncaught exception at the CLI boundary
→ 1.

---

<a id="stage-1"></a>
## 1. Stage 1 — verse-reading (`lexical.meaning`)

**Registration** (`cfg_step`): work package `verse-lexical`, handler
`iba.app.handlers.lexical:meaning`, scope `cluster`, kind `operations`.
**Write grant** (`cfg_write_grant`): `ib_observation`, `ib_node`, `run_batch`.

### 1.1 Handler walk (`handlers/lexical.py:meaning`, called per `-ClusterCode`)

1. Checks the 3 write grants above (`_may`).
2. Requires `-ClusterCode`; `-Preview` defaults to `true` (a missing/blank param is treated as
   preview — never a live call by default).
3. `lexicalscope.resolve_strongs(conn, cluster_code=...)` — the cluster's member strongs.
4. `lexicalscope.resolve_verse_ids_for_strongs(...)` — every verse those strongs occur in.
5. **Freshness gate** (`lexical.stale_role_strongs_for_cluster`, escalation #1719): refuses the
   whole run if any member strong's live `verse_lexical.role` data doesn't currently list this
   cluster, despite `cluster_strong` saying it should — i.e. Layer 1 hasn't been rebuilt since a
   membership change. Hard stop, not a partial run.
6. Verse ids are chunked into batches of `lexical.meaning_max_verses_per_batch` (**live value:
   10**) — a dedicated, smaller override than the shared `passage.max_verses` other steps use,
   because front-loading (§1.3 below) multiplies expected output per batch.
7. **Per batch**: assemble the package (§1.2), check `batchcontrol.content_key` /
   `already_committed` (resume/skip — a batch a prior run already committed for this exact verse-id
   set is skipped, never re-paid for), check the batch's estimated cost against
   `lexical.llm_max_cost_per_batch` (**live value: $1.00**) — over cap fails the WHOLE run
   (`cost-cap-exceeded`), not just that batch.
8. If `-Preview`, no API call, no write — returns the batch list + total estimated cost for the
   *not-yet-committed* batches only.
9. If live: `batchcontrol.start_batch` (writes `status='running'`, commits immediately — the crash
   safeguard) → `versereadinggenerate.call_api` → `log_usage` (CSV, `lexical.llm_usage_log_path`) →
   `versereadinggenerate.parse_response` → `recordingpass.record_batch(..., stage='verse-reading',
   similarity_threshold=cluster.recording_similarity_threshold)` → `conn.commit()` →
   `batchcontrol.commit_batch`. Any exception in this window calls `batchcontrol.fail_batch` before
   re-raising.
10. After every batch: `clusterstatus.advance_if_verse_reading_complete` — the ordinal-2 →
    ordinal-3 (`ready_for_subgroup_allocation`) transition (§6).

### 1.2 Payload assembly (`versereadinggenerate.assemble_batch_package`)

**Config read, with live values:**
| key | live value |
|---|---|
| `lexical.llm_chars_per_token` | 4 |
| `lexical.llm_max_output_tokens` | 40000 |
| `lexical.llm_rate_input_per_million` | 3.0 |
| `lexical.llm_rate_output_per_million` | 15.0 |
| `lexical.llm_model` | `"claude-sonnet-5"` |

**DB reads, per batch of verses:**
- `verse` (id/osisId/text, `deleted=0`) for the batch's verse ids.
- `verse_lexical` (strong/surface/morph_code/role, `deleted=0`, ordered by position) — **every**
  live row for these verses, not just the cluster's own member strongs, so `roles_in_verse` can
  carry every role-bearing word's full `cluster_codes` array (M-codes and role-T-codes together,
  deliberately including the mechanically-unwired tags per `role-list-includes-unwired-tags`).
  **Corrected 2026-09-21** (researcher caught an error in this line's own T-code list): the
  mechanically-WIRED subset is exactly `T4`/`T5`/`T7`/`T8`/`T9` (Adversarial/Negator/Party-Divine/
  Party-Human/Party-Angelic) — the 5 codes `lexical.py`'s `load_code_classes()` hardcodes into a
  dict to compute the real `is_negator`/`party_kind` DB columns (`iba/app/lib/lexical.py:219-220`),
  confirmed matching the live `cfg_method_rule.role-list-includes-unwired-tags` text verbatim.
  **`T3` (Operations) is NOT wired** despite being heavily referenced in `D7.7.1`'s own prompt
  *text* ("where an action or movement word is classified as an Operation... role-T3") — that's
  the LLM interpreting the raw role array itself, not Python computing a derived column from it;
  checked live, no code path branches on `role-T3` anywhere. So the correct unwired set is
  `T2`/`T3`/`T6`/`T10`–`T15` (9 codes) — this line previously omitted `T3` from that list, wrongly
  implying it was wired.
- **Front-loading** (`_strongs_needing_battery`): of the M-code strongs present in these verses
  that are NOT this cluster's own members, which ones have **no** live `stage='verse-reading'
  M0.1%/M0.5%` observation anywhere yet — only those get added to the battery this pass, so a
  LATER cluster's pass over the same verse finds them already covered.
- `_meaning_sources(strong)` for the resulting battery-strong set — `strong_meaning_tree` +
  `strong_lexicon.lsj`/`.mounce`, each included only if it has content for that exact strong.
- `_prior_relational_context` — every existing `stage='verse-reading' question_code='M0.6.5'`
  observation for verses in this batch (any cluster's pass), so a later pass builds on it instead
  of duplicating.
- `wa_obs_question_catalogue` — question text for `M0.1%`, `M0.5%`, `D7.7.1`, `M0.6.5` (queried
  live, not hardcoded).
- `cfg_enum WHERE name='ib_observation.tag' AND inactive=0` — the valid tag list.
- **`cfg_method_rule WHERE step='lexical.meaning' AND active=1`** — 8 live rules, verbatim:
  1. `read-3-sources-complementary` — read all 3 meaning sources as complementary evidence, never
     picking one and dropping the others.
  2. `role-list-includes-unwired-tags` — the role list includes every live role-cluster tag, not
     only the mechanically-wired subset.
  3. `per-cluster-scope-not-subgroup` — this stage runs per-cluster, anchored to the cluster as
     home; subgroups don't exist yet.
  4. `answers-M0.1-M0.5-D7.7` — this stage's catalogue linkage (M0.1/M0.5/D7.7.1/M0.6.5).
  5. `needs-adjacent-verse-context-applies-here` — the cross-cutting flag applies here too.
  6. `cost-bounded-small-batches` — never a full-cluster push in one call.
  7. `cluster-status-2to3-transition-verse-reading-complete` — the status-advance rule.
  8. `strongs-reassigned-detection` — membership-change flagging rule.

### 1.3 The LLM instruction, verbatim (`_instructions`)

> You are producing verse-reading observations for cluster {cluster_code}, the pre-subgroup Layer 2
> pass (`lexical.meaning`). You are given, per verse: the verse's own base text, `roles_in_verse` —
> every role-bearing word in that verse, each carrying `cluster_codes` (the full set of M-code and
> role-T-code tags) and `is_home_cluster` (true if this word belongs to cluster {cluster_code}) —
> and `prior_relational_context_by_verse` — any M0.6.5 relational findings ALREADY recorded for
> these verses by an earlier cluster's own pass. You are also given `meaning_sources_by_strong` for
> {home_strongs} (this cluster's own member strongs). [+ a front-load note naming any additional
> strongs, if present]. Read all present meaning sources as complementary evidence, never picking
> one and ignoring the others.
>
> Method rules governing this task: [the 8 rules above]
>
> TWO KINDS OF QUESTION, answered differently: M0.1/M0.5 (word-level battery) answer for EVERY
> strong listed in `meaning_sources_by_strong`. M0.6.5 (relational) and D7.7.1 answer ONLY for this
> cluster's own home strong(s). For M0.6.5: if prior context exists for this verse, your answer MUST
> build on it — state what THIS characteristic's own vantage point adds, never repeat what a prior
> pass already said. If no prior context, you start the relational chain.
>
> Answer these catalogue questions: [live M0.1/M0.5/D7.7.1/M0.6.5 question text]
>
> Valid `tag` values: [live list]. `tag` is a categorisation value, not just a peculiarity flag —
> prefer a specific tag whenever the finding matches it [8 `TAG_GUIDANCE` definitions given
> verbatim: `qualifier-for-term`, `no-impact`, `not-related-to-meaningful-word`,
> `sole-mcode-in-verse`, `cluster-pole-negative`, `cluster-pole-positive`, `attested-pre-nt`,
> `nt-coinage`]. Use `answered-no-flag` ONLY for a genuinely plain answer matching none of the
> above. NEVER use the literal string `none` — it is not registered and will be rejected.
>
> STRICT BOUNDARIES: verse values must be one of exactly those given; `strong` for M0.1/M0.5 must be
> a key of `meaning_sources_by_strong`, for M0.6.5/D7.7.1 one of the home strongs; D7.7.1 only
> applies when an operation-tagged word co-occurs with a party-tagged word; `question_code` MUST be
> the exact leaf code, never a bare component code (`M0.1`/`M0.5` rejected); one observation per
> sub-question; `could-not-resolve`/`needs_adjacent_verse_context` require stating the reason in
> `obs_text`; no fields beyond the shape, no prose outside the JSON.
>
> Respond with ONLY a JSON object: `{"observations": [{"strong", "question_code" or null, "tag",
> "obs_text", "meaning_source", "occurrences": [{"verse", "surface", "morph_code"}]}]}`

### 1.4 Input/output JSON shapes

**Input `content`:** `{"cluster_code", "verses": [{"verse", "text", "roles_in_verse": [{"strong",
"surface", "morph_code", "cluster_codes", "is_home_cluster"}]}], "meaning_sources_by_strong":
{strong: {"strong_meaning_tree"?, "strong_lexicon.lsj"?, "strong_lexicon.mounce"?}},
"prior_relational_context_by_verse": {verse: [{"from_cluster", "about_strong", "finding"}]}}`

**Expected output:** `{"observations": [{"strong", "question_code", "tag", "obs_text",
"meaning_source", "occurrences": [{"verse", "surface", "morph_code"}]}]}` — validated by
`parse_response`, which only checks the top-level `observations` key exists and the text is valid
JSON (possibly fenced in ` ```json `). No schema validation beyond that at this layer — field-level
correctness is `recordingpass.py`'s job (§5).

### 1.5 API call mechanics (`call_api`, shared by all 4 stages via `lexicalenrichgenerate.call_api`)

POST to `lexical.llm_api_url` (`https://api.anthropic.com/v1/messages`), `anthropic-version`
`2023-06-01`, model = `lexical.llm_model` (`claude-sonnet-5`), `max_tokens` =
`lexical.llm_max_output_tokens`, **`thinking` explicitly `{"type": "disabled"}`** (a fix for a real
bug found 2026-09-17: the API defaults to extended thinking even unrequested, and with a bounded
`max_output_tokens` the entire budget was sometimes consumed by thinking, leaving zero tokens for
the actual answer — a real-money empty response). 600s timeout. If the response hits `max_tokens`
with no text content, raises `ApiCallFailed` naming the setting to raise.

---

<a id="stage-2"></a>
## 2. Stage 2 — char-subgroup (`cluster.subgroup`)

**Registration:** work package `cluster-reading`, handler `iba.app.handlers.cluster:subgroup`,
scope `cluster`, kind `operations`. **Write grant:** `cluster_subgroup`, `cluster_subgroup_strong`,
`ib_observation`, `ib_node`, `run_batch`.

### 2.1 Handler walk (`handlers/cluster.py:subgroup`)

1. Checks 5 write grants.
2. Requires `-ClusterCode`; `-Preview` defaults true.
3. `clusterstatus.require_ready_for_subgroup_allocation` — **hard precondition**: refuses
   (`not-ready`) unless `cluster.status == 'ready_for_subgroup_allocation'`.
4. `lexicalscope.resolve_strongs` — the cluster's member strongs (the WHOLE set, one call, never
   batched — a holistic judgement over the cluster's entire membership at once, unlike Stage 1's
   per-verse chunking).
5. `batchcontrol.already_committed` — resume/skip against this exact member-strong set.
6. Assemble the package (§2.2); check estimated cost against **`cluster.subgroup_llm_max_cost`
   — NOT SET in `cfg_setting` (see §7 finding 1), so the hardcoded Python fallback of $2.00 is
   what's actually enforced, silently.**
7. If preview: report only. If live: `start_batch` → `subgroupgenerate.call_api` → `log_usage` →
   `parse_response` → `recordingpass.record_subgroups` (writes `cluster_subgroup`/
   `cluster_subgroup_strong`, §5) → `recordingpass.record_batch(..., stage='char-subgroup')` (any
   substantive analytical claim, separate from the placement decision) → commit → `commit_batch`.
8. `clusterstatus.advance_after_subgroup_allocation` (cluster: `ready_for_subgroup_allocation` →
   `ready_for_reading`) then `advance_subgroups_after_allocation` (every non-FLAG subgroup:
   `allocated` → `ready_for_reading`).

### 2.2 Payload assembly (`subgroupgenerate.assemble_cluster_package`)

**Config:** same `lexical.llm_chars_per_token`/rate settings as Stage 1, plus
**`cluster.subgroup_llm_max_output_tokens` — also NOT SET in `cfg_setting`, falls back to the
hardcoded 8000.**

**Per member strong** (`_strong_profile`): `strong.stepGloss`/`stepTransliteration`; up to 8
distinct `surface` forms from `verse_lexical`; **every** `stage='verse-reading' ib_observation` row
for that strong (question_code/tag/obs_text) — the real analytical grounding, not a cold dictionary
read; `_meaning_sources`.

**`cfg_method_rule WHERE step='cluster.subgroup'`** — 9 live rules, verbatim:
1. `full-cluster-read-before-assignment` — every strong's gloss/surface read FIRST, before any
   assignment.
2. `meaning-based-not-surface-similar` — grouped on actual shared meaning, not superficial wording.
3. `max-10-subgroups-flag-excluded` — real subgroups top out at 10; FLAG doesn't count against it.
4. `label-true-to-essence-not-wordlist` — label names what the subgroup IS, not a gloss list.
5. `singleton-subgroup-valid` — a one-member subgroup is a valid outcome, not a mis-grouping sign.
6. `flag-conditions-and-reason-required` — FLAG for no inner-being implication / wrong cluster /
   other anomaly, reason always recorded.
7. `placement-note-captures-any-observation` — not FLAG-only, available for any placement.
8. `anchor-verse-llm-selected` — the LLM itself picks each subgroup's representative verse.
9. `one-strong-one-subgroup` — every strong placed exactly once.

### 2.3 The LLM instruction, verbatim (`_instructions`)

> You are forming meaning-based subgroups (families) of the strongs belonging to cluster
> {cluster_code}, the char-subgroup stage (process b) of the cluster-reading pipeline. You are
> given, per strong: its dictionary gloss/transliteration, a sample of its distinct surface forms as
> they actually occur in the corpus, its already-captured verse-reading observations (real
> analytical grounding from a prior stage — read these as primary evidence of what the word actually
> means in context, not just the dictionary gloss), and its meaning_sources.
>
> Method rules governing this task: [the 9 rules above]
>
> TWO DIFFERENT OUTPUTS — do not confuse them: `placement_note` is ONLY a short rationale for the
> placement decision itself — why this strong belongs in this subgroup, or why it's FLAGged. It is a
> comment ABOUT a placement, never the analytical claim itself. `observations` is where any
> substantive analytical finding goes.
>
> STRICT BOUNDARIES: every one of {N} strongs must be placed into exactly one subgroup, no
> exceptions — [full list given]. A strong that doesn't fit goes under `subgroup_code "FLAG"`,
> reason stated in its `placement_note` (required for FLAG). Every non-FLAG subgroup needs a stable
> `subgroup_code`, a `label` true to its essence, a one-sentence `core_description`, and an
> `anchor_verse_reference` drawn from one of its own member strongs' occurrences. FLAG needs none of
> those. Valid `tag` values: [live list]. Each observation's `strong` must be a cluster member. No
> fields beyond the shape, no prose outside the JSON.
>
> Respond with ONLY a JSON object: `{"subgroups": [{"subgroup_code", "label", "core_description",
> "anchor_verse_reference", "members": [{"strong", "placement_note"}]}], "observations": [{"strong",
> "tag", "obs_text", "question_code": null, "meaning_source", "occurrences": [...]}]}`

### 2.4 Input/output shapes

**Input:** `{"cluster_code", "strongs": {strong: {"gloss", "transliteration", "surface_forms",
"verse_reading_observations": [{"question_code","tag","obs_text"}], "meaning_sources"}}}`

**Output:** `{"subgroups": [...], "observations": [...]}` — `parse_response` requires BOTH keys
present (unlike Stage 1's single `observations` key).

**Writer (`recordingpass.record_subgroups`)** — see §5.2 for the full validation/write logic
(refuses if the cluster already has live subgroups; validates every subgroup has a code, every
non-FLAG subgroup has a label, every FLAG member has a placement_note, every member strong is
placed exactly once, no cluster member is missing, no non-member strong appears).

---

<a id="stage-3"></a>
## 3. Stage 3 — char-reading (`cluster.reading`)

**Registration:** work package `cluster-reading`, handler `iba.app.handlers.cluster:reading`, scope
`subgroup`, kind `operations`. **Write grant:** `ib_observation`, `ib_node`, `run_batch`.

### 3.1 Handler walk (`handlers/cluster.py:reading`)

1. Checks 3 write grants. Requires `-ClusterCode` AND `-SubgroupCode`.
2. `clusterstatus.require_subgroup_ready_for_reading` — hard precondition:
   `cluster_subgroup.status == 'ready_for_reading'`.
3. Member strongs from `cluster_subgroup_strong` for this subgroup's id.
4. `charreadinggenerate.assemble_subgroup_packages` — normally **1** package (whole subgroup, one
   call); if exactly one member strong's corpus-wide occurrence count exceeds **60**
   (`_MAX_OCCURRENCES_PER_STRONG`), that strong is split by **surface form** into multiple packages
   (never splitting one surface's own occurrences across passes; escalation #1761, researcher's own
   rule). If **more than one** member strong is over cap simultaneously, raises
   `MultipleOverCapStrongs` — not designed, refuses rather than guessing a packing order.
5. Cost check per package against `lexical.llm_max_cost_per_batch` ($1.00, live).
6. Per package (resume/skip via `batchcontrol` keyed on `selector_key = cluster|subgroup` +
   `batch_key`): `start_batch` → `call_api` → `log_usage` → `parse_response` →
   `recordingpass.record_batch(..., stage='char-reading', subgroup_id=..., subgroup_code=...)` →
   commit → `commit_batch`.
7. After ALL packages: `charreadinggenerate.compute_strong_checks` — **code-computed** completeness
   (never LLM-self-reported): diffs each member strong's full occurrence list against what
   `ib_node` actually traced at this stage; reports any `missing_verses`.
8. `clusterstatus.advance_subgroup_after_reading` (`ready_for_reading` → `ready_for_answer`).

### 3.2 Payload assembly (`charreadinggenerate.assemble_subgroup_packages`/`_strong_reading_profile`)

**Config:** `lexical.llm_max_output_tokens` (40000, shared with Stage 1's fallback default — no
dedicated setting for this stage), same rate settings.

**Per member strong:** gloss/transliteration; **every** occurrence corpus-wide (verse text,
surface, morph_code — NOT deduplicated by verse, no sampling — `scan-every-occurrence-no-sampling`
rule); all meaning sources; its own Stage 1 (`verse-reading`) observations; its Stage 2
(`char-subgroup`) placement observations; any of its own PRIOR `char-reading` observations (empty
on a first run, populated on a re-read).

**`cfg_method_rule WHERE step='cluster.reading'`** — 14 live rules, verbatim (key ones; full list
in the file):
`per-subgroup-never-whole-cluster`; `read-3-sources-complementary-reading`;
`scan-every-occurrence-no-sampling`; `grouping-never-excuses-skipping`;
`every-instance-states-what-it-is`; `not-a-single-distilled-meaning` — "the aim is not a single
distilled meaning — show what a verse's or strong's meaning could be or is likely to be, including
alternative candidate readings"; `difference-is-its-own-observation`;
`cross-strong-comparison-is-this-stages-own-task`; `morph-actively-read-not-merely-carried`;
`per-strong-traceability-verified-by-code`; `homonym-no-context-earmarked-and-left`;
`data-errors-flagged-separately`; `reread-includes-existing-rows`;
`role-driven-walk-not-forced` — the mechanical role-walk is NOT a structural gate here (superseded
2026-09-17).

### 3.3 The LLM instruction, verbatim (`_instructions`)

> You are producing char-reading observations (process c) for subgroup {code!r} of cluster
> {cluster_code} — "{label}" ({core_description}). This subgroup's own member strongs are {N}. You
> are given, per strong: gloss/transliteration, EVERY occurrence corpus-wide (verse text, surface,
> morph_code — not deduplicated, no sampling), all present meaning sources (read as complementary
> evidence), its own Stage 1 observations already captured (real grounding — do not re-derive or
> duplicate these, build on them), its Stage 2 placement observations, and any of its own prior
> char-reading observations (if this is a re-read). [+ a PARTIAL COVERAGE note if this package is a
> surface-split batch, naming exactly which surface forms this pass covers and which it doesn't]
>
> Method rules governing this task: [the 14 rules above]
>
> YOUR ACTUAL JOB, distinct from Stage 1's per-verse reading: synergise the similar and different
> contextual meaning of THIS SUBGROUP'S OWN member strongs against EACH OTHER — where do they
> genuinely share meaning, and where do they diverge? Stage 1 already covers per-occurrence
> surface/gloss divergence for each strong on its own; your value is the cross-strong comparison
> within this one subgroup, and any strong-level pattern only visible from its FULL occurrence list.
>
> Valid `tag` values: [live list]. Prefer `tightly-related`/`no-direct-connection` for cross-strong
> comparison; `verse-grouping` where several of a strong's OWN occurrences share one genuinely alike
> reading; `difference-inference` for a specific inference (morph-driven included); `surface-gloss-
> divergence` only for a NEW pattern not already covered by Stage 1; `no-human-context` for a
> homonym with no meaningful context (earmark, stop); `data-error` for a data-quality issue noticed
> while reading; `could-not-resolve`/`needs_adjacent_verse_context` per existing definitions.
>
> STRICT BOUNDARIES: every `strong` must be a subgroup member; every `verse` in `occurrences` must
> be one actually given for that strong; do NOT answer catalogue questions here (`question_code`
> should be null for essentially all of these); no fields beyond the shape, no prose outside JSON.
>
> Respond with ONLY a JSON object: `{"observations": [{"strong", "question_code": null, "tag",
> "obs_text", "meaning_source", "occurrences": [{"verse", "surface", "morph_code"}]}]}`

### 3.4 Input/output shapes

**Input:** `{"cluster_code", "subgroup_code", "label", "core_description",
"anchor_verse_reference", "strongs": {strong: {"gloss", "transliteration", "occurrences":
[{"verse","verse_text","surface","morph_code"}], "meaning_sources",
"verse_reading_observations","char_subgroup_observations","prior_char_reading_observations"}}}`

**Output:** same shape as Stage 1's — `{"observations": [...]}`.

---

<a id="stage-4"></a>
## 4. Stage 4 — char-answers (`cluster.answer`)

**Registration:** work package `cluster-reading`, handler `iba.app.handlers.cluster:answer`, scope
`subgroup`, kind `operations`. **Write grant:** `ib_observation`, `ib_node`, `run_batch`.

### 4.1 Handler walk (`handlers/cluster.py:answer`)

1. Checks 3 write grants. Requires `-ClusterCode` AND `-SubgroupCode`.
2. `clusterstatus.require_subgroup_ready_for_answer` — hard precondition:
   `cluster_subgroup.status == 'ready_for_answer'`.
3. Member strongs from `cluster_subgroup_strong`.
4. `batchcontrol.already_committed` — resume/skip (whole-subgroup, single call, no over-cap split
   logic at this stage).
5. Assemble the package (§4.2); cost check against `lexical.llm_max_cost_per_batch` ($1.00).
6. If live: `start_batch` → `call_api` → `log_usage` → `parse_response` →
   `recordingpass.record_batch(..., stage='char-answers', subgroup_id=..., subgroup_code=...)` →
   commit → `commit_batch`.
7. `charanswergenerate.compute_question_checks` — **code-computed** per-question completeness:
   a question counts answered for this subgroup if some `char-answers` observation for it has ≥1
   `ib_node` row citing one of the subgroup's own member strongs.
8. `clusterstatus.advance_subgroup_after_answer` (`ready_for_answer` → `answer_complete`), then
   `recompute_cluster_status_rollup` (cluster → `ready_for_observations` once EVERY live,
   non-FLAG subgroup has reached `answer_complete`).

### 4.2 Payload assembly (`charanswergenerate.assemble_subgroup_package`/`battery_questions`)

**Battery scope** (`battery_questions`, queried live from `wa_obs_question_catalogue`): every
active question whose `scope` is `Characteristic (HIB behaviour)` / `Characteristic relational` /
`The HIB` / `Other non-human beings`, **excluding**:
- `D7.7.1` — already answered by Stage 1, despite carrying a matching scope label (a known,
  documented scope-vs-answering-stage mismatch, not silently resolved).
- Any question whose text mentions "science extract" (currently `D9.1.1`/`D9.2.1`/`D11.2.1`/
  `D12.1.1`) — the science-extract file isn't wired in yet; answering without it would invent an
  unsupported claim.

Confirmed live: **52 questions** currently make this cut (matches `package["question_count"]` seen
in this session's earlier data pull).

**Per member strong** (`_strong_answer_profile`): gloss/transliteration; every occurrence
corpus-wide; meaning sources; observations from **all 3 prior stages**
(`verse_reading_observations`/`char_subgroup_observations`/`char_reading_observations`) plus any
prior `char-answers` observations of its own (re-read case).

**`cfg_method_rule WHERE step='cluster.answer'`** — 7 live rules, verbatim:
1. `per-subgroup-answer-never-whole-cluster`.
2. `multiple-slants-not-one-distilled-answer` — where evidence genuinely differs, a SEPARATE
   observation per distinct slant, all under the same `question_code`.
3. `scope-level-governs-evidence-trail` — a strong-grounded slant sets `strong`; a subgroup-wide
   slant leaves `strong` null but every occurrence carries its own.
4. `adjacent-context-flagged-not-fetched-answer`.
5. `cross-family-flagging-out-of-scope-this-build` — deliberately not requested (its own tag value
   unchosen).
6. `battery-scope-excludes-verse-reading-and-science-extract`.
7. `per-question-completeness-verified-by-code`.

### 4.3 The LLM instruction, verbatim (`_instructions`)

> You are answering the characteristic-grain catalogue battery (process d, char-answers) for
> subgroup {code!r} of cluster {cluster_code} — "{label}" ({core_description}). This subgroup's own
> member strongs are {N}. You are given, per strong: gloss, EVERY occurrence corpus-wide, all
> meaning sources, and its own observations already captured at every prior stage (verse-reading,
> char-subgroup, char-reading — real analytical grounding, read this as your primary evidence, do
> not re-derive it from scratch) plus any of its own prior char-answer observations (if this is a
> re-read).
>
> Method rules governing this task: [the 7 rules above]
>
> CORE RULE — MULTIPLE SLANTS, NOT ONE DISTILLED ANSWER: where the subgroup's own strongs or
> evidence genuinely point to different answers to the same question, produce a SEPARATE observation
> for EACH distinct slant, all under the SAME question_code — never flatten into one 'the
> characteristic means X' answer. A single slant is correct only when the evidence actually is
> uniform across every member strong, not a default.
>
> EVIDENCE TRAIL, per scope: for a slant grounded in ONE specific member strong, set `strong` to
> that strong's code and cite its own occurrences. For a slant grounded in the SUBGROUP AS A WHOLE,
> leave `strong` null on the observation itself, but EVERY element of `occurrences` MUST carry its
> own `strong` field — an occurrence without its own strong cannot be resolved and will be silently
> dropped.
>
> Answer these catalogue questions (one or more observations per question_code, per the
> multiple-slants rule above): [52 live questions, each shown with its `scope`]
>
> Valid `tag` values: [live list]. Use `needs_adjacent_verse_context` where insufficient. Use
> `could-not-resolve` where genuinely unresolvable. **`answered-no-flag` is for a plain, substantive
> answer with nothing else to categorise — escalation #1770: it is NOT expected to dominate; check
> every OTHER tag below first and only fall back to `answered-no-flag` once none of them genuinely
> apply.** [then every `TAG_GUIDANCE` definition, same 8 as Stage 1, given verbatim]
>
> STRICT BOUNDARIES: `question_code` MUST be an exact leaf code from the list above. Do NOT attempt
> cross-family/cross-cluster comparison — that belongs to a later synergy stage. Every `strong`
> value (observation or occurrence) must be a subgroup member. Every `verse` in `occurrences` must
> be one actually given for that strong. No fields beyond the shape, no prose outside JSON.
>
> Respond with ONLY a JSON object: `{"observations": [{"strong": "..." or null, "question_code",
> "tag", "obs_text", "meaning_source", "occurrences": [{"strong", "verse", "surface",
> "morph_code"}]}]}`

**Note the bold sentence above** — the explicit "NOT expected to dominate" instruction with
`TAG_GUIDANCE` definitions is the escalation-#1770 fix (BUILD.md #299). See §7 finding 3 for why
this matters to reading the existing data correctly.

### 4.4 Input/output shapes

**Input:** `{"cluster_code", "subgroup_code", "label", "core_description",
"anchor_verse_reference", "strongs": {strong: {"gloss","transliteration","occurrences",
"meaning_sources","verse_reading_observations","char_subgroup_observations",
"char_reading_observations","prior_char_answer_observations"}}}`

**Output:** `{"observations": [{"strong": "..." or null, "question_code", "tag", "obs_text",
"meaning_source", "occurrences": [{"strong","verse","surface","morph_code"}]}]}` — the only stage
whose `occurrences` carry their own `strong` (needed for the subgroup-wide-slant case).

---

<a id="recordingpass"></a>
## 5. The single writer (`recordingpass.py`)

**Every** stage's parsed model output reaches the database only through this module — no other code
writes `ib_observation`/`ib_node` (checklist rule 0.1), and verse references are always resolved
fresh against live `iba.db` data, never trusted from the model's own text (rule 0.5).

### 5.1 `record_one_observation` — per observation, in order

1. `_validate_stage(conn, stage)` — the caller-supplied stage literal checked live against
   `cfg_enum ib_observation.stage`; raises `ValueError` (a programming-bug assertion, not a
   data-quality skip) if it's ever wrong.
2. `_validate_question_code` — if set, must match a live, active `wa_obs_question_catalogue` row.
   Invalid → the WHOLE observation is skipped (`skipped-invalid-question-code`), never written under
   a phantom code (escalation #1719).
3. `_validate_tag` — must match a live, active `cfg_enum ib_observation.tag` value. Invalid →
   skipped (`skipped-invalid-tag`).
4. `_validate_obs_text` — refuses a bare negation with no content (`^\s*(none|n/?a|null|nothing|-)
   \s*\.?\s*$`) — "none — because X" passes (has substance), the bare string "none" alone doesn't.
   Invalid → skipped (`skipped-invalid-obs-text`).
5. **`meaning_source` is NOT validated at all** — see §7 finding 2.
6. `_effective_cluster_code` — a word-level (M0.1/M0.5) observation is re-filed under the strong's
   own live M-code cluster membership (`cluster_strong`), not the pass's own cluster_code — so a
   later cluster's pass finds it covered regardless of which pass originally produced it. M0.6.5/
   D7.7.1 stay keyed to the pass's own cluster (they're that cluster's vantage point).
7. Every claimed `occurrence` is resolved fresh (`resolve_occurrence`) against live
   `verse_lexical`/`verse` by strong + verse osisId, disambiguated by surface/morph if the strong
   occurs more than once in that verse. Unresolvable → collected as `unresolved`, not written as a
   phantom node.
8. If the model gave occurrences and NONE resolved → the whole observation is skipped
   (`skipped-no-resolvable-occurrences`). If it gave zero occurrences by design (a genuine
   subgroup-wide negative finding, e.g. "no evidence of X across this subgroup") → proceeds with 0
   nodes, a distinction added 2026-09-18 after the first real Stage 4 run silently discarded 10
   substantive negative answers under the old, cruder check.
9. **Same/broaden/new decision** — `_existing_candidates` (same `cluster_code`/`stage`/`strong`/
   `question_code`) compared via `difflib.SequenceMatcher` on normalized text against the new
   `obs_text`:
   - Exact `obs_text` match AND the new occurrence refs are already a subset of the candidate's
     existing node refs → **no-op**, true duplicate.
   - Best-matching candidate's similarity ≥ `cluster.recording_similarity_threshold` (**live value:
     0.85**) → **`aligned-superficial-edit`**: the existing row's `obs_text` is updated in place,
     `status` reset to `'draft'` (escalation #1782), new occurrence nodes appended under the SAME
     `observation_id` (seq continuing from that observation's own current max, not restarting at 0
     — a real bug found and fixed 2026-09-18).
   - A candidate exists but below threshold → **`new-expands-existing`**: a genuinely new row,
     linked back via `ib_node.traced_observation_id`.
   - No candidate at all → **`new-observation`**.
10. `_insert_observation` — validates the literal `"draft"` status against the live enum
    (`_assert_valid_ib_status`, defensive), derives `window` from the question's own catalogue row
    (`_window_for`, itself now cross-checked against the live `ib_observation.window` enum).
11. Every resolved occurrence not already an existing node ref gets its own `ib_node` row
    (`seq` incrementing), carrying `traced_observation_id` (set only for `new-expands-existing`) and
    the caller's own `subgroup_code`.

### 5.2 `record_subgroups` (Stage 2's own writer, `cluster_subgroup`/`cluster_subgroup_strong`)

**Refuses outright** if the cluster already has ANY live `cluster_subgroup` row — re-grouping/
re-allocation reconciliation is explicitly not designed yet (#1690 §5 item 1), never guessed at
silently. Then validates, before writing anything: every subgroup has a `subgroup_code`; every
non-FLAG subgroup has a `label`; every FLAG member has a `placement_note`; no strong is placed
twice; every cluster member strong IS placed somewhere; no non-member strong is placed anywhere.
Any violation raises `SubgroupWriteError` — the whole write fails, never a partial cluster (these
are the model violating its own output contract, a different kind of failure than a per-item data
gap).

---

<a id="clusterstatus"></a>
## 6. The status machine (`clusterstatus.py`)

**`cluster.status` ordinals:** `strong_assignment_in_progress`(1) → `t_cluster_assignment_completed`
(2) → `ready_for_subgroup_allocation`(3) → `ready_for_reading`(4) → `ready_for_observations`(5) →
`ready_for_synthesis`(6) → `completed`(7); `strongs_reassigned`(8) is an out-of-band flag state, not
part of the forward sequence.

**`cluster_subgroup.status` ordinals:** `allocated`(1) → `ready_for_reading`(2) →
`ready_for_answer`(3) → `answer_complete`(4) → `completed`(5); `re_read_needed`(6) out-of-band.

Both ordinal maps are cross-checked live against `cfg_enum` (`_assert_enum_parity`) on every call
that uses them — added 2026-09-18 after these two enum groups were found registered but never
looked up anywhere; confirmed no actual drift at the time, and this assertion now catches any
future edit to one side without the other.

**Every transition is single-step and unconditional once its precondition holds** — no transition
in this module does a partial/fuzzy advance:
- `advance_if_verse_reading_complete` — ordinal 2→3, gated on EVERY member strong having ≥1 live
  `stage='verse-reading' ib_observation` row.
- `advance_after_subgroup_allocation` — ordinal 3→4, unconditional on Stage 2 completing.
- `advance_subgroups_after_allocation` — every `allocated` subgroup → `ready_for_reading`,
  unconditional.
- `advance_subgroup_after_reading` — `ready_for_reading`→`ready_for_answer`, unconditional per
  subgroup.
- `advance_subgroup_after_answer` — `ready_for_answer`→`answer_complete`, unconditional per
  subgroup.
- `recompute_cluster_status_rollup` — cluster `ready_for_reading`→`ready_for_observations`, gated
  on EVERY live non-FLAG subgroup having reached `answer_complete` (FLAG subgroups carry `status
  IS NULL` and are permanently excluded from this gate).
- `flag_if_reassigned` — fires only once a cluster has progressed past ordinal 2; sets
  `strongs_reassigned` and raises a real `decision_required` escalation — per the researcher's own
  instruction (#1697 v5), **no automatic resubmission**, manual control only.

---

<a id="findings"></a>
## 7. Findings surfaced while tracing (not assumed, checked live against real data)

### Finding 1 — two Stage 2 cost/token caps are silently running on hardcoded fallbacks, not config

`cluster.subgroup_llm_max_cost` and `cluster.subgroup_llm_max_output_tokens` are read via
`ctx.cfg.setting(key, default)` in both `subgroupgenerate.py` and `handlers/cluster.py`'s
`subgroup()` — but **neither key exists in `cfg_setting`**, confirmed live. The Python-literal
defaults ($2.00, 8000 tokens) are what's actually enforced, invisibly — a `configmaint.propose`
change to either would currently do nothing, because there's no row to change. Every OTHER
cost/token cap in this pipeline (Stage 1/3/4's `lexical.llm_max_cost_per_batch`/
`lexical.llm_max_output_tokens`) IS a real, live `cfg_setting` row. Not fixed here — flagging for a
decision (register the two missing settings at their current fallback values, or a different
number).

### Finding 2 — `ib_observation.meaning_source` has zero write-time validation, confirmed measured

Already known (escalation #1771) and reconfirmed this session with real numbers (escalation
#1796): 37+ distinct free-form strings are live against the 3-value canonical enum
(`strong_meaning_tree`/`strong_lexicon.lsj`/`strong_lexicon.mounce`) — e.g. `"strong_meaning_tree;
lsj; mounce"`, `"role list"`, `"cluster_codes"`. `recordingpass.py` deliberately does not validate
this field (a validator was written, then removed again after confirming it would discard nearly
every future observation that sets it). Genuinely open, tied to #1771's still-undecided redesign
of the field's shape (letting the model name more than one source explicitly).

### Finding 3 — the char-answers tag-uniformity data is real, but entirely PRE-DATES the fix meant to address it

Checked precisely, not assumed: **all 748 live `char-answers` observations were created between
2026-09-18T03:48Z and 2026-09-18T13:25Z** — a single day, a single session. The fix that added the
`TAG_GUIDANCE` definitions and the explicit "`answered-no-flag`... NOT expected to dominate" line to
`charanswergenerate.py`'s own prompt (§4.3, bold sentence) was built the SAME session, as the
direct, same-day response to seeing this exact 84%-`answered-no-flag` pattern in this exact data
(BUILD.md #299, escalation #1770). **No `char-answers` batch has been run since that fix landed** —
confirmed via `run_batch`/`ib_observation.created_at`, and via this session's own cluster-coverage
count (still exactly 3 clusters / 12 subgroups through char-answers, unchanged since 2026-09-18).

This means: the near-uniform tagging and the low genuine-negative rate measured in the last two
turns of this conversation are accurate facts about the OLD, pre-fix prompt's output — they are
**not** evidence about what the CURRENT code (with the tag guidance and the explicit
anti-domination instruction) actually produces, because it has never been exercised. The honest
open question is not "did the pipeline fail" (it did, for that specific defect, before the fix) but
"does it still fail now" — which is untested, not unknown-and-assumed-fine. The only way to answer
it is to actually re-run one subgroup through `cluster.answer` with the current code and measure the
same statistics fresh.

### Finding 4 — 27 of 99 active catalogue questions are structurally unreachable by ANY stage, not just "not yet answered" (CORRECTED 2026-09-21)

**This is the gap the report above missed on its first pass** — it documented what each stage's
query does mechanically, but never reconciled the UNION of all 4 stages' coverage against the
full catalogue.

**Superseded by an authoritative, DB-validated audit (escalation #1806):**
[`outputs/catalogue-coverage-audit-20260921-v2.md`](catalogue-coverage-audit-20260921-v2.md) +
paired `.csv` — every one of the 103 catalogue rows (not just the 99 active ones), classified by
mechanism and cross-checked live (`SELECT COUNT(*) FROM ib_observation WHERE question_code=?` per
row, zero surprises found). This section is now a summary of that audit, not the primary source —
read the audit for the full per-row disclosure.

**Correction to the original text below:** Stage 1's mechanism was described here as "a HARDCODED
literal list" — true of `D7.7.1`/`M0.6.5` (exact-match, pinned) but NOT of `M0.1%`/`M0.5%`, which
are `LIKE`-prefix matches that auto-update when a new `M0.1.x`/`M0.5.x` question is added to the
catalogue. Re-verified directly against `versereadinggenerate.py` line ~210-212 this session, not
re-asserted from the original pass.

| scope | total | mechanism (validated) |
|---|---:|---|
| Characteristic (HIB behaviour) | 24 | 19 char-answers (dynamic) + 4 excluded (science-extract, #1805) + 1 pinned (`D7.7.1`, Stage 1) |
| Characteristic relational | 17 | char-answers (dynamic) — full coverage |
| Other non-human beings | 12 | char-answers (dynamic) — full coverage |
| The HIB | 4 | char-answers (dynamic) — full coverage |
| **The verse** | 5 | 1 pinned (`M0.6.5`, Stage 1); the other 4 (`M0.6.1`–`M0.6.4`) share this scope but no stage ever asks them |
| **Verse-context** | 10 | 0 covered — no stage's query anywhere selects `scope='Verse-context'` |
| **Word/term (lexical)** | 27 | 14 dynamic-prefix (`M0.1%`/`M0.5%`, Stage 1); the other 13 share the scope label but no stage asks them (6 of the 13 are additionally worded "In this verse...", a scope-vs-wording mismatch — see the audit's own wording-vs-grain section) |
| Science | 4 | RETIRED (`deleted=1`) — superseded by the `D9`/`D11`/`D12` science-extract questions above |

**Root cause, precisely (unchanged, now stated exactly):** Stage 4 (`char-answers`) selects its
battery by `scope IN (...)` — dynamic, auto-covers a new question under one of its 4 scopes. Stage
1 (`verse-reading`) selects by `question_code LIKE 'M0.1%' OR LIKE 'M0.5%'` (dynamic, by prefix) OR
`question_code IN ('D7.7.1','M0.6.5')` (pinned, exact) — **never by scope**. Any question whose
`scope` is `'The verse'`/`'Verse-context'`/`'Word/term (lexical)'` but whose code doesn't match one
of those four conditions is invisible to every stage's SQL, permanently, regardless of how many
clusters get processed. Stages 2/3 (`char-subgroup`/`char-reading`) answer no catalogue question at
all by design (`question_code` written `NULL`, per each stage's own explicit LLM instruction).

**Not decided here, genuinely open:** whether this is (a) a 5th stage never built, (b) these 27
questions are mis-scoped in the catalogue (should some of them actually carry one of the 4
char-answers scopes instead?), or (c) deliberately out of scope for the current build phase. The
mechanism as built has no opinion on any of the three — it simply never queries these scopes.

### Finding 5 — `verse_lexical.role`/`is_negator`/`party_kind` were base-family-contaminated corpus-wide; fixed, rebuilt, verified (2026-09-21, escalations #1806/#1807/#1810/#1812)

Discovered investigating a researcher-reported `verse_lexical` correctness concern (verse_id 7478,
strong H7725O), corrected through iteration when the researcher caught two real mistakes in the
investigation itself (see escalation #1810's own history for the honest account, including a
verification-script bug and a silently-failed rebuild).

**Root cause:** `iba/app/lib/lexical.py`'s `load_role_codes`/`_role_for` (role) and
`load_code_classes`/`_code_classes_for` (`is_negator`/`party_kind`) both keyed their
`cluster_strong` lookup on `_base(strong)` — the suffix-stripped code — unioning live cluster
allocations across every sub-lettered sibling sharing a base number, not the exact occurring
strong. Example: H7725O's own live `cluster_strong` allocation is M11 only; its stored `role` was
`["M11","M81","T3"]`, the extra two borrowed from unrelated siblings H7725N/H7725G-M. Confirmed to
explain 100% of every mismatch found (1,694 in a 3-cluster scoped report, 69,563 of 544,667 live
rows project-wide for `role`; 9,100 for `is_negator`/`party_kind`). A third, related but distinct
defect in the same field: 4 strongs (`H0113`, `H4317M`, `H4317Q`, `G3413`) carry two live,
deliberately-kept-dual party classifications (e.g. Michael's H4317* codes, human+angelic per
escalation #1606's own instruction) — the old code picked between them via unordered Python set
iteration, non-deterministic across process runs; fixed to resolve to `None` on a genuine conflict.

**Governance consequence:** `governance.base_data_spine` (§73) extended from
`verse-span-strong-must-sync` to `verse-span-strong-cluster-must-sync` (escalation #1812,
`GOVERNANCE.md` §78/§79) — a strong with zero live `cluster_strong` allocation is now classified a
spine FATAL, not a soft lexical-build precondition. Escalation #1807 (9 such strongs, e.g.
`G2279`/`G4537`/`H6446` — none fit any inner-being cluster on inspection) is the live instance,
still awaiting the researcher's decision on whether they get a cluster or a formal out-of-scope
marker; the 28 verses containing them are the only part of the live corpus still wrong.

**Propagation into THIS pipeline, traced directly (not assumed):** `role` is read by
`versereadinggenerate.py`/`subgroupgenerate.py`/`charanswergenerate.py` (§1.2/§2.2/§4.2 above) —
every live `verse_lexical` row's `role` for every verse in a batch, not just the cluster's own
member strongs. 1,013 Stage 1 `verse-reading` observations (`M0.6.5`/`D7.7.1` only — the two
question types whose own instructions read OTHER words' role tags) were built from a contaminated
role tag; 380 downstream Stage 2/3/4 observations for the 17 affected strongs inherited that text
verbatim (Stages 2-4 each independently query `ib_observation WHERE strong=? AND
stage='verse-reading'`, unfiltered by question). Full detail:
`outputs/observations-based-on-incorrect-role-20260920.md` + CSV. `is_negator`/`party_kind` are
NOT read by any of Stages 1-4 (checked directly, zero references) — no `ib_observation`
re-examination question for those two fields, unlike `role`.

**Corpus-wide rebuild:** three full passes via `lexical.build` (the active step — `lexical.run`,
which earlier code comments in this pipeline called "the real front door," is `cfg_step.inactive=1`,
retired), each independently verified against live recomputation, not assumed clean. Final state: 0
mismatches anywhere in the live corpus for `role` or `is_negator`/`party_kind`, outside the 28
verses still gated on escalation #1807.

**Still open, not decided here:** whether any of the 7,046 observations this pipeline has ever
produced (across every cluster, every stage) need regenerating given what they were actually built
from — tracked on escalation #1810, not executed (LLM-cost-bearing, none of this session's fixes
touched `ib_observation` at all).

### Finding 6 — a validated catalogue coverage audit, and a real, isolated population-coverage gap in M83 (2026-09-21, escalation #1806)

**Catalogue coverage audit.** `outputs/catalogue-coverage-audit-20260921-v2.md` + CSV supersede
Finding 4's own hand-rolled scope table above as the primary source — all 103 catalogue rows
(not just the 99 active ones), each cross-checked live against `ib_observation`, zero surprises.
Confirms Finding 4's numbers and sharpens the mechanism: Stage 1 is prefix-dynamic for
`M0.1%`/`M0.5%`, pinned-exact only for `D7.7.1`/`M0.6.5` — not a flat hardcoded list as Finding 4
originally said.

**Population anchors vs. observation density.** `outputs/population-vs-observations-density-20260921-v3.md`
+ 3 CSVs (cluster/strong/subgroup grain) — verse/span/strong counts per cluster, per owned strong,
per `cluster_subgroup`, cross-referenced against actual `ib_observation` counts at each grain.
Surfaced a real, previously-undocumented gap: M83's `A_general_seeking` subgroup (strongs `G2212`,
`H1245`) is still `cluster_subgroup.status='ready_for_reading'` while M83's other 3 subgroups are
`answer_complete` — confirmed against the status column directly, not inferred from zero counts.
That one subgroup holds **328 of M83's 496 total verses (66%)** — meaning M83's current
char-reading (55)/char-answers (216) observation counts reflect analysis of only its smaller,
already-complete subgroups; its single largest population segment hasn't reached those stages at
all. M49 and M67 have no equivalent split. Not a data-quality defect — a legitimate, checkable
"how much of this cluster has actually been analysed" fact this pipeline's own state didn't
surface anywhere else.

**Science-question family, corrected (2026-09-21, researcher correction).** This trace's own §Finding 4
table and the #1814 wording review both treated `D9.1.1`/`D9.2.1`/`D11.2.1`/`D12.1.1` (the
science-extract family, still 0/4 answered live, excluded by `charanswergenerate.py`'s own filter) as
a minor structural footnote — without checking `bible_research.db` `prose_section` id 6, "Science and
the Bible," first. Researcher caught this directly. That prose section is a core, deliberate programme
methodology, not incidental: *"Scripture is the primary lens; science is the second lens... the
programme identifies three kinds of convergence — phenomenological, mechanistic, structural — and
three kinds of divergence — register, reductive, genuine."* `D9.1.1`=mechanistic, `D9.2.1`=structural
(generational transmission), `D11.2.1`=innate-endowment vs. `D11.1`'s created-design/fallen-condition
finding, `D12.1.1`=social-expression pattern — each a named check the prose itself calls for, not an
arbitrary add-on. Consequence: #1805 (the open build escalation for this mechanism) is a not-yet-built
piece of a load-bearing programme methodology, not a minor coverage gap — priority raised there
directly (v3). Separately confirmed: the 4 `T7.3.x` catalogue rows this family superseded were already
`deleted=1` before this session, per their own `review_note` — escalation #1712 (2026-09-17), not this
trace's or this review's doing. Full grounding: `outputs/catalogue-question-wording-review-20260921-v5.md`
new "science-question family, corrected" section.

### What was NOT found — checked, not assumed

- `record_one_observation`'s validation chain (stage/question_code/tag/obs_text/status) is real,
  live, and enforced at every write site, not decorative.
- The same/broaden/new duplicate-handling logic is real and does what its own docstring claims —
  traced line by line, not just read the comment.
- Every stage's LLM prompt genuinely embeds live catalogue/enum/rule content at call time (no
  hardcoded second copies that could drift) — confirmed by reading the actual SQL, not the
  docstrings' claims about it.
- Status transitions are gated correctly and don't advance early — every transition function
  checks its own precondition before writing.

### Finding 7 — catalogue question wording reviewed, all 103 rows (2026-09-21, escalation #1814, spawned from #1806)

Researcher observation, verbatim: the questions actually feeding Stage 1 (and every other stage)
are "poorly worded, open for interpretation and confusion... likely the reason why so many
questions have simply failed." Directly relevant here because §1.2 above already documents that
`versereadinggenerate.py` shows the LLM **only** `question_code`+`question_text` — no `scope`
field — so a question's wording is that stage's *entire* signal for what it's evaluating and at
what grain. Full review: `outputs/catalogue-question-wording-review-20260921-v4.md` + CSV (v4, superseding v2
after the researcher caught that my first pass accepted "across the evidence" as a real grain
statement without checking it names anything — 10 rows moved from wrongly-COMPLIANT to REVISE on
recheck) — 51 of 103 rows compliant against an explicit, stated convention (subject + grain stated
in the text itself, no embedded jargon, no embedded process instructions), 48 flagged for revision,
4 retired. Two of the flagged rows (`M0.6.5`, `D7.7.1`) are ones this trace's own §1.3/§4.3 quote
verbatim as live LLM instructions — their revised wording (jargon and embedded process-instructions
removed) is not yet applied to the catalogue; if/when it is, this document's own quoted instruction
text in §1.3 will need updating to match.

**v4 update (2026-09-21):** re-examined against Findings 8/9 (escalation #1815) and Finding 10
(#1817), per researcher instruction to evaluate that impact on this review. The 18 rows originally
lumped under one `definitional-category` label split three ways once cross-checked against the
coverage audit's own mechanism classification: **13** (`M0.1.1`-`M0.1.3`, `M0.5.1`-`M0.5.10`) are
`DYNAMIC-STAGE1`, front-loaded for every M-code strong in a verse regardless of cluster membership —
exposed to both the `_effective_cluster_code()` misattribution bug (population now fully enumerable
via #1817, fix not yet applied) and, more fundamentally, Finding 9's conclusion that asking these
questions of a front-loaded non-member strong has no valid referent at all under the now-settled
"characteristic = the M-code cluster as a whole" definition — a confirmed *mechanism* error, not a
wording defect in these 13 questions. **5** (`M0.2.1`/`2.2`, `M0.3.1`-`3.3`) are `DYNAMIC-STAGE4`,
not front-loaded, not exposed to either problem — the original review had wrongly conflated them
with the 13. `M0.6.5`/`D7.7.1` (already REVISE, unrelated wording issues) are `PINNED-STAGE1`,
confirmed also not exposed. No verdicts or wording changed as a result — this is a mechanism/design
finding staying on #1815, not a wording-review correction. Escalation #1814 updated to v5.

### Finding 8 — "the characteristic" doesn't have one stable referent in `M0.1`/`M0.5` observations (2026-09-21, escalation #1815)

Researcher question, verbatim: *"before I review, it is clear in your mind what characteristic
refers to. in the context of the questions, what will you be looking at?"* Checking the working
definition (the M-code cluster as a whole, per `cluster_strong`) against live data rather than just
asserting it surfaced a real gap: §1.2's own front-loading mechanism ("the FIRST cluster-pass to
touch a verse answers `M0.1`/`M0.5` for EVERY M-code strong present in that verse, not just its own
home strong(s)") means a cluster's own reading pass writes `M0.1`/`M0.5` observations for words that
are not members of that cluster at all — confirmed live, M49's own answers include `H6440G`
("face"), `H6310G` ("mouth"), `H7218A` ("head"), `H5945B` ("Most High"), `H7342G` ("Broad Wall"),
one of which (`H6186A`) says outright in its own text: *"is not a member of M49; front-loaded here
because it co-occurs in Jer.50.14."* In these rows "the characteristic" refers to whatever that
OTHER word's own meaning is, not the cluster named by `cluster_code`. Quantified across the 3
analysed clusters: 149 of 3404 total `M0.1`/`M0.5` observations (4.4%) are for non-member,
front-loaded strongs (M49 65/1148, M67 4/242, M83 80/2014) — a real, bounded minority, not the
majority, but not negligible. Bears directly on escalation #1814's wording review, since every
revision there assumed "the characteristic" has one stable referent.

**Root cause, found in code (2026-09-21, same escalation):** `recordingpass.py`'s
`_effective_cluster_code()` (lines 108-124) already exists specifically to solve this — redirect a
front-loaded observation to the strong's OWN owning cluster, per its own docstring ("they are
inherently that cluster's own vantage point... not a [pass's]"). The bug: its query is restricted to
`cluster_code LIKE 'M%'` — M-code clusters only. Every mislabeled strong checked (`H6440G`, `H6310G`,
`H7218A`, `H5945B`, `H7342G`, `H6186A`) has ONLY a T-code allocation (T14/T7/T2/T3), no M-code home
at all — the query finds nothing, falls through to the reading pass's own code, and that fallback
is the entire bug. Not simply "widen the query to match T-codes too": T-codes are themselves defined
as "referent-identity classification, orthogonal to the thematic M-code axis," not characteristics
in the `M0.1.1` sense — a word whose only home is `T14` (Body-Parts) has no characteristic to name
at all. Two concrete fix options, not decided here: (a) exclude M-code-less strongs from front-
loading entirely, or (b) keep front-loading them but record `cluster_code` as `NULL`/a dedicated
non-characteristic marker rather than any real cluster. Also open: whether to correct the 149
already-recorded observations once the code is fixed. Tracked on #1815.

### Finding 9 — the foundational definition of "characteristic" exists, but doesn't specify the current pipeline's operational grain (2026-09-21, escalations #1815/#1816)

Researcher challenge, verbatim: *"You have in the whole preparation of the pipeline build, nor in
the generation of 7000 observations ever ask what is a characteristic, and what I am measuring or
working with. how it is possible?"* Investigated rather than answered from impression. The
programme prose (`prose_section` id 5, "Defining Inner Being" — reachable only after a governance
fix: escalation #1809's `bible_research.db` exclusion conflicted with `governance.
prose_canonical_authority`, resolved by escalation #1816 adding an explicit prose-table exemption)
gives a real, rigorous definition: *"Inner-being characteristics are the non-physical, internal
states, capacities, and expressions that constitute a person's invisible life."* That's a precise
word-INCLUSION filter — given an English word, does it qualify as inner-being content — and it's
what the original ~214-word registry was screened against.

**What it does not specify:** the operational GRAIN "the characteristic" refers to under the
current M-code cluster architecture — the original single word, the whole cluster (a composite of
several Hebrew/Greek strongs), or the specific strong being read at a given moment (the actual
per-row grain Finding 8's `M0.1`/`M0.5` observations are recorded at). That is a different question
from "what counts as inner-being vocabulary," and the prose doesn't settle it. This gap — a real
foundational definition, and a cluster-based architecture built later without re-deriving what "the
characteristic" means at that architecture's own grain — may be the actual root Findings 6-8 are all
symptoms of. **Resolved 2026-09-21, same escalation:** the legacy `characteristic` table lead was a
dead end — researcher confirmed it and related `bible_research.db` tables are "fragments of things
that has gone wrong," not a resource. With that ruled out, committed to an explicit operational
definition rather than leaving the gap open: **"the characteristic" = the M-code cluster as a
whole** (identity = the cluster's own name; evidence base = the union of every verse where any
owned strong occurs; vocabulary = the set of owned strongs as one concept's lexical instantiations;
subgroups = facets within it; a single strong's occurrence = an instance of it, never the
characteristic itself). Under this definition, **Finding 8 stops being an ambiguity and becomes a
confirmed error**: `M0.1.1` asking "what is the characteristic called" about a front-loaded,
non-member strong has no valid referent — that word doesn't instantiate the cluster's concept at
all. The front-loading *mechanism* (answer once per batch, don't re-ask later) is a reasonable
efficiency device; the *question wording*, applied to a non-member strong, asks about something
that isn't there — which is exactly why several of the 149 non-member observations self-correct
mid-answer ("H6186A... is not a member of M49"). Not decided here: what those front-loaded
non-member strongs should be asked instead — a real design question, tracked on #1815.

### Finding 10 — the base-data spine is now fully sound corpus-wide, zero exceptions (2026-09-21, escalations #1807/#1817)

Closes a thread running since escalation #1613/#1812: the 9 strongs `lexical.readiness` Leg 3 found
with zero `cluster_strong` allocation (root of escalations #1807/#1810's 28-verse exclusion) are now
classified — `G2375`/`H6446` fit `T12` (Objects-Artifacts, matching live "weapon"/garment
precedent), `G4537` fits `T3` (Operations, an unambiguous action verb), the other 6 have no fit
anywhere and are `T2` per researcher instruction. `iba/app/migration/assign_1807_unmapped_
strongs_v1_20260921.py` applied, `lexical.readiness` re-run clean (0 FATAL across all 3 legs, was
9). This also unblocked the 28 verses Finding 5's corpus-wide `role`/`is_negator`/`party_kind`
rebuild couldn't reach — rebuilt (17 chapters, 500 verses, 55 corrections, 0 failures). Final,
unconditional, whole-corpus verification: 0 `role` mismatches, 0 `is_negator`/`party_kind`
mismatches, anywhere. Finding 5's fix is now 100% complete, not 99.9%.

### Finding 11 — full pipeline wiring audit: placement, payload sizing, instruction clarity, write-back (2026-09-21, escalation #1806)

Researcher instruction, verbatim: *"work through the catalogue once again, and make sure that each
questions is presented to llm at the right point with the correct input data and that llm is not
overloaded with unnecessary data; that llm know exactly what need to be done with each question
and that the output from llm is correctly presented to CC to update the tables with all the
relevant columns that need to completed."* Full deliverable: `outputs/pipeline-wiring-audit-
20260921-v2.md` + CSV, all 103 rows × 4 dimensions, built by reading all 4 stage-generator modules
(`versereadinggenerate.py`, `subgroupgenerate.py`, `charreadinggenerate.py`,
`charanswergenerate.py`) and `recordingpass.py` directly, live code, this session — joining the
already-live placement audit (Finding 6/#1806 coverage audit) and instruction-wording audit
(#1814) with two genuinely new dimensions.

**New finding — Stage 4 (char-answers) has no payload ceiling.** Unlike Stage 3, which caps any
single member strong at 60 corpus-wide occurrences and splits by surface form when exceeded
(`_MAX_OCCURRENCES_PER_STRONG`/`_partition_occurrences_by_surface`), Stage 4 sends all ~52
characteristic-grain catalogue questions plus every corpus-wide occurrence for every subgroup
member strong (uncapped) plus the full 3-stage observation history, in ONE call, with no splitting
mechanism at all. Not observed broken yet — the largest live Stage-4 payload so far
(`M83/D_consultative_inquiry`, 164 occurrences, 1 strong) succeeded at $0.69/call, 6 of 52
questions left unanswered (code-computed and reported, not silently swallowed) — but there is no
ceiling and no advance signal if a much larger subgroup ever reaches this stage. Flagged, not
fixed — tracked on #1806/#1805.

**New finding — the concrete, code-level reason Finding 6's M83 population gap exists.** M83's
`A_general_seeking` subgroup (328 of 496 verses, 66%) has never actually been attempted at Stage 3:
zero rows exist for it in the `run` table. Its 2 member strongs, `G2212` (116 corpus occurrences)
and `H1245` (225 occurrences), **both individually exceed Stage 3's 60-occurrence cap at once** —
exactly the case `charreadinggenerate.py`'s own `MultipleOverCapStrongs` exception exists for, and
its docstring states plainly this is "not yet designed": the existing split logic only handles ONE
over-cap strong per subgroup, riding every other member strong's full profile along unpartitioned.
Compare `M49/D_yadah_praise_confess` (run ids 3109→3117→3132): exactly ONE over-cap strong
(`H3034`, 114 occurrences) — the existing mechanism handled it correctly, 2 split passes, succeeded.
M83's case needs that mechanism extended to 2+ simultaneously-over-cap strongs — a real, specific,
not-yet-designed build item, not a scheduling coincidence.

**Confirmed clean, checked not assumed:** Stage 3's own instructions leave a soft door open for
`question_code` to be non-null in narrow cases ("unless an observation genuinely IS a direct
answer to an already-live catalogue question") — live check: 0 of 118 `char-reading` observations
have ever used it. No duplicate-answering risk between Stage 3 and Stage 4 in practice.
`cluster_subgroup_id`/`cluster_subgroup_code` write-back confirmed correctly populated for Stage
3/4 and correctly NULL for Stage 1/2; `window` confirmed correctly derived from the catalogue and
validated against its live `cfg_enum`.

**CORRECTED 2026-09-21 (escalation #1821) — the completeness-check praise below this line was
wrong.** This entry originally cited `compute_question_checks`'s "N of 52 unanswered" run-outcome
figures as proof completeness is "code-computed... not silently swallowed." Researcher's follow-up
challenge (on Finding 12) prompted a direct re-check, live: those figures are themselves unreliable.
`compute_question_checks` only counts a question "answered" if its observation has at least one
`ib_node` citation row — but `recordingpass.py` deliberately and correctly permits a whole-subgroup
answer with ZERO citations (its own docstring names this: a legitimate negative/synthesis finding
not tied to one verse). Checked both subgroups whose latest run reported a nonzero unanswered
count: `M49/A_thanksgiving_act` (reported 1/52 unanswered, `D10.1.2`) is a genuine gap, confirmed 0
observations anywhere. `M83/D_consultative_inquiry` (reported 6/52 unanswered) is mostly a FALSE
POSITIVE: only `D7.2.3` is genuinely missing for this subgroup's own strongs (it DOES exist for
M83's other subgroups, `B_intensified_seeking`/`C_hostile_pursuit` — this subgroup's own evidence
may just not support it, not necessarily a miss); the other 5 (`M0.2.2`, `X0.1.2`, `X0.5.1`,
`X0.5.2`, `X0.5.3`) have real, substantive, citation-free observations written in the SAME run that
reported them unanswered. Both subgroups are marked `cluster_subgroup.status='answer_complete'`
regardless of the real gap or the false ones — the status label does not reflect either. Not fixed
here — the checker function itself needs the same zero-citation exception `record_one_observation`
already has; tracked on #1821.

**2026-09-21 addendum — the 48 approved wording revisions applied live, plus 2 new column-
alignment gaps found (escalation #1818, spawned from the closed #1814).** Per full-column sweep of
`wa_obs_question_catalogue` (all 103 rows, not sampled): the 48 approved revisions are now live
(`iba/app/migration/apply_catalogue_wording_v1_20260921.py`), and the `M0.5.11`/`M0.6.5` tier=NULL
gap is fixed (both were silently excluded from `cataloguereport.py`'s own tiered listing until
now). Two further gaps found, not fixed — genuine decisions, not mechanical: `section` is stale
for 92 of 103 rows (old pre-realignment T0–T7 labels, never migrated to the live D1–D12/M0/X0/F0
scheme `dimension` already carries correctly); `prompt_seq` is NULL for the 9 newest questions
(D1/D2/D7.7/D9/D11.2/D12.1), which sort first out of sequence in that same report. **Corrected same
day (escalation #1818 v3), researcher pushback that this was Claude's own job, not a question
back:** `prompt_seq` fixed (each affected row was the sole/first member of a brand-new component —
unambiguous once actually checked). `section` determined genuinely redundant (nothing live reads
it; `dimension` already does its job) and marked superseded in `cfg_column`, not repaired — same
verdict this table already recorded for 3 other retired columns. Also found and fixed in the same
pass: 4 rows with `status`/`deleted` disagreement (the retired `T7.3.x` family). `cfg_enum`
registered for `status`/`tier`/`scope` (none existed before). Full record: `BUILD.md` #306. `window`,
`dimension`, `component_code`/`component_title`, `scope` all confirmed clean.

**Write-back audit, corrected count.** 14 rows (not 13) carry the #1815 `cluster_code`
misattribution exposure — `M0.5.11` was missed in the original 18-row `definitional-category`
sweep (its `issue_type` was never tagged that way) but is `DYNAMIC-STAGE1`/word-level like the
other 13; corrected in `catalogue_review_data.py`, wording review regenerated to
`outputs/catalogue-question-wording-review-20260921-v6.md`.

**Placement summary (68 correct / 27 structurally-unreachable / 4 blocked-known-#1805 / 4
retired), payload summary (52 Stage-4 rows carry the new no-cap risk, 16 Stage-1 rows confirmed
right-sized, 35 never reach any stage), write-back summary (54 correct, 14 the known #1815 bug, 35
N/A)** — full detail per question in the CSV, not repeated here.

### Finding 12 — verse-context relational reading is thin: rich data loaded, barely questioned (2026-09-21, escalation #1819)

Researcher challenge, verbatim: *"I honestly do not understand this section. I still do not know
how and at what stage which questions are reading the verse-context with full view of all the
related words and there standing in relation to each to each other. I still feels as if only a
small subset of T codes are considered, T3 is ignored, and that the verse-context reading is
watered down."* Checked precisely, not defended — the concern is accurate.

**Only Stage 1 (`verse-reading`) ever assembles the full cross-word picture of a verse.**
`roles_in_verse` carries every role-bearing word's complete tag array (every T-code/M-code,
T2–T15, nothing filtered). No other stage (2/3/4) ever re-sees this — they only ever see a single
strong's own occurrences and prior findings, never "everything tagged in this verse, together."

**Of Stage 1's own ~16 questions, only 2 are genuinely relational, both narrow:** `D7.7.1`
(operation-word (`T3`) relation to party-words (`T7`/`T8`/`T9`) only) and `M0.6.5` (this
characteristic's relation to *other M-code characteristics* only). The other 14 (`M0.1.1`–`3`,
`M0.5.1`–`11`) are single-word lexical/definitional questions, answered per strong, in total
isolation from every other tagged word in the same verse — despite that data sitting in the same
LLM call.

**Catalogue-wide T-code coverage, checked by direct query against every live `question_text`:**
`T4`/`T5`/`T7`/`T8`/`T9` (Adversarial/Negator/Divine/Human/Angelic party) are the only T-codes with
real code-computed columns (`is_negator`/`party_kind`, `lexical.py:219-220`) and substantive
question coverage (the `D7.1`–`D7.6` family, 8 questions) — but those are answered at **Stage 4**,
per-strong/per-subgroup, not as part of Stage 1's full-verse cross-word reading. `T3` (Operations)
is referenced by exactly **one** question anywhere (`D7.7.1`), narrowly, with no general
operation-meaning question and no computed column — whatever the LLM happens to notice there,
unverified. `T6` (Connective) and `T10`–`T15` (Places/Corporate/Objects/Natural-World/Body-Parts/
Calendar) are referenced by **zero** questions anywhere — confirmed, not inferred.

**Net assessment:** the pipeline loads a genuinely rich per-verse relational dataset at Stage 1,
but the catalogue barely questions it — 2 of 16 Stage-1 questions are relational at all, 7 of 14
T-codes get no question coverage whatsoever, `T3` gets one narrow, unverified toehold. Distinct
from Finding 4/#1806 (the `Verse-context` SCOPE tag never being selected by any stage — a wiring
gap) and Finding 8/#1815 (the characteristic-definition/front-loading misattribution bug) — this is
a design gap in what the catalogue asks of data it already has, not a wiring or definition bug.

**RESOLVED 2026-09-21, same escalation.** Researcher instruction, verbatim: *"The objective of the
lexical llm read is to have a rich / comprehensive understanding of the context of the verse in
relation to all the M-code strongs in the verse. That is the objective you need to achieve. Go
through all the questions relating to it, enrich those questions, and add questions that will
acheive this objective."* `M0.6.5` enriched with explicit relation-type vocabulary (cause/enable/
intensify/block/respond-to/tension, same-party-vs-different-party) — was an open, unguided
narrative, now systematic. New `M0.6.6` added — a whole-network synthesis question, closing the
exact gap `M0.6.5`'s own deliberate single-vantage design (#1723) leaves open. Both wired all the
way through, not left as catalogue-only content that would itself become another
`STRUCTURALLY-UNREACHABLE` row (`versereadinggenerate.py`: added to the Stage 1 selection query,
given its own progressive prior-context stream `prior_network_context_by_verse` kept separate from
`M0.6.5`'s own chain, prompt instructions and module docstring updated, companion `cfg_method_rule`
text corrected). Verified end-to-end against real M49 data, no API call: payload, prompt, and
question-offering all confirmed working. `T3`/`T6`/`T10`–`T15`'s near-zero coverage is not
addressed by this fix — `M0.6.5`/`M0.6.6` are M-code-to-M-code questions, per the researcher's own
stated scope ("all the M-code strongs"); the T-code coverage gap remains open if it needs its own
treatment. Full record: `BUILD.md` #308.

### Finding 13 — Stage 1 is 71% of cost / 80% of time; root cause is a missing skip-check for the calling cluster's own strongs, not bloated payloads (2026-09-21, escalation #1820)

Researcher question, verbatim: *"during the first three cluster pipeline processes I noticed that
the majority of time and cost for the process is consumed by the lexical stage. am I neurotic to
think that we have not properly thought through the loading of data into llm... instead of
carefully selecting the right data for the right question."* Checked with real numbers from the
`run` table, not a feeling-check.

**Confirmed: Stage 1 (verse-reading) dominates** — 70.8% of cost ($25.32 of $35.74) and 79.9% of
wall-clock time across M49/M67/M83's completed runs.

**Root cause is NOT bloated per-call payloads.** Average cost per LLM call is comparable across all
4 stages — Stage 1 $0.325/call, Stage 2 $0.455, Stage 3 $0.206, Stage 4 $0.361 — Stage 1 is
actually the *cheapest* per call. It costs more in total because it needs 78 calls against Stage
4's 14, a structural granularity difference: Stage 1 must touch every verse in small batches;
Stage 4 aggregates a whole subgroup (often hundreds of verses) into one call. Cross-cluster
verse-reprocessing checked and ruled out for these 3 clusters (0–1 shared verses per pair).

**The real, actionable finding:** the front-loaded word-level battery (`M0.1`/`M0.5`, 14
questions — facts *about a word*, not a verse, e.g. "what is the characteristic called") already
has a skip-check (`_strongs_needing_battery`) for *other clusters'* strongs riding along in a
verse, but **not** for the calling cluster's own home strongs — `versereadinggenerate.py:203-204`
includes `cluster_member_strongs` in the battery unconditionally, every verse-batch, with no check
for whether that strong already has settled answers. Checked live: `H3034` (114 occurrences, M49)
has **432 distinct stored `M0.1`/`M0.5` observation rows**, not 14 (one settled answer each) and
not anywhere near 114×14 either — `recordingpass.py`'s similarity dedup does real consolidation
work, but only on what gets *written*, not on whether the LLM gets *called*. Every verse-batch
touching `H3034` pays for a fresh word-level answer-generation, discovers afterward it's a
near-duplicate, and merges/discards it. The filtering happens after paying for the redundant
generation, not before.

**RESOLVED 2026-09-21, same escalation.** Researcher pushback, verbatim: *"the problem with this
whjole process is that the output value of this read is near insiginifcant, we could just as well
complete ignore it so little value comes out of it — it is frustratingly difficult to get you to
connect what is the real value expected out of this process."* Demonstrated the problem concretely
before fixing it, not just re-argued the cost case: sampled 8 real `M0.1.1` answers for `H3034`
across different verses — every one restates the same root-meaning/essential-nature claim in
slightly different words, near-zero new information past the first answer. Fixed
(`versereadinggenerate.py`): the existing skip-check now applies to the calling cluster's own home
strongs too, not just front-loaded non-members. `meaning_sources_by_strong` stays populated for
every home strong regardless (`M0.6.5`/`M0.6.6`/`D7.7.1` need it unconditionally); new prompt
language tells the LLM explicitly which home strongs already have a settled battery and must not
be re-answered. A real bug in the first pass of this fix (a leftover reference to the renamed
`needs_battery` variable, `NameError` on the first live test) was caught and fixed before shipping.
Verified live, twice: a batch touching an already-fully-answered strong correctly shows the skip
instruction; a fresh mixed-strong batch still assembles correctly. Full record: `BUILD.md` #309.

### Finding 14 — "the primary term" in `M0.5.2`/`M0.5.3` has no operational definition (2026-09-21, escalation #1822)

Researcher question, verbatim: *"what is regarded as the primary term in M0.5.2 and M0.5.3."*
Checked precisely — there is no operational definition anywhere. Confirmed two ways: (1) code
search across every live stage-generator module for "primary" — zero hits; the governing
instruction just says "answer for EVERY strong listed in `meaning_sources_by_strong` — not just
this cluster's own member strongs," with no designation of which one (if any) is primary. (2)
Empirically — checked M49's 5 owned strongs directly: every one, including `G2170` (occurs in a
single verse), has its own separate `M0.5.2`/`M0.5.3` answer (`G2168`: 16/15, `G2169`: 9/8,
`G2170`: 3/3, `H3034`: 26/25, `H8426`: 17/17) — no selection is happening; each strong's own
answer is framed as if it alone were "the primary term."

`M0.5.1` genuinely does name two primary terms ("the primary Hebrew and Greek terms" — one per
testament, cluster-level). `M0.5.2`/`M0.5.3` inherit that singular phrasing but are answered under
the current per-strong front-loading mechanism (#1723, 2026-09-17) with no concept of one term
being more "primary" than another — the wording predates that redesign and was never updated to
match it. Same underlying pattern as Finding 13 (a question worded as scoped to one thing,
mechanically repeated across every strong), a distinct instance: this one is a wording/scope
mismatch in the catalogue text itself, not a missing skip-check. Also worth noting: the #1814
wording review marked both rows `COMPLIANT` under the `definitional-category` bucket without
catching this ambiguity.

**RESOLVED 2026-09-21, same escalation.** Researcher instruction, verbatim: *"fix the redundant
terminology."* "The primary term" replaced with "this term" in `M0.5.2`/`M0.5.3` — matches the
actual per-strong mechanism exactly, no false "primary" designation implied. Also fixed `M0.4.1`/
`M0.6.1`, which carry the identical latent issue despite being currently `STRUCTURALLY-UNREACHABLE`
— consistency, so the same confusion doesn't resurface if #1806's verse-context redesign ever wires
them in. Full record: `BUILD.md` #309.

### Finding 15 — 8 Stage-4 questions cite a per-verse "gate" question by code that is itself structurally unreachable (2026-09-21, escalation #1823)

Researcher question, verbatim: *"what happens when the mechanism (in the CSV) is marked as
structurally-unreachable? what does it mean."* Answering it surfaced a more serious problem in the
27-row `STRUCTURALLY-UNREACHABLE` set — one I introduced/preserved myself without catching it.

**8 live questions, all answered at Stage 4, cite a per-verse "gate" question by code that is
itself never asked by any stage, ever (zero observations):** `D7.1.2`/`D7.1.3` cite `D7.1.1`;
`D7.2.2`/`D7.2.3` cite `D7.2.1`; `D7.3.3` cites `D7.3.1`/`D7.3.2`; `D7.4.2b` cites `D7.4.2a`;
`D7.4.3b` cites `D7.4.3a`; `D7.5.2` cites `D7.5.1`. Each gate question (e.g. `D7.1.1`: "In this
verse, does the characteristic operate from God toward the human person...") is meant to establish
*which* verses satisfy a condition the aggregate follow-up then filters on ("across the verses
where X was found, per `D7.1.1`") — but that gate is never recorded anywhere, so the citation
points at nothing live. The Stage 4 LLM presumably re-derives the gate finding fresh from its own
full occurrence data when answering the aggregate question, rather than building on a real
per-verse finding as the wording implies — the "per `CODE`" framing is currently a fiction, not a
working cross-reference.

**Not a problem I found independently — I put several of these exact citations into the live
catalogue myself**, in the #1814 wording revision (v4/v5, applied live via
`apply_catalogue_wording_v1_20260921.py`), following that review's own stated convention ("cite
sibling questions by code, not bare pronoun") without checking whether the cited sibling was
itself reachable. Not resolved here — tracked on #1823.

**Also flagged in the same turn:** `outputs/pipeline-wiring-audit-20260921-v2.csv`/`.md`'s own
`question_text` column is now stale — it predates both the #1814 wording application and escalation
#1818's column-governance fixes. Not regenerated here (a review action, not urgent) — the live DB
is authoritative in the meantime.

**2026-09-21 addendum — fixed and regenerated fresh (escalation #1823, researcher instruction:
"bring the CSV up to date. and ensure that the catalogue questions text does not include stale
terminology that is no longer relevant").** Checking every `(per CODE)` citation catalogue-wide,
not just the D7 family Finding 15 first spotted, found the same broken pattern in `D10`/`D3`/`D5`/
`D6` too — **15 questions total** cited a dead gate code. Fixed
(`iba/app/migration/fix_dead_gate_citations_v1_20260921.py`): each dead citation dropped, the
gate's own filter condition inlined in plain language instead. `catalogue_review_data.py`
reconciled for the same 15 rows (its own `revised_text` had gone stale relative to the live fix).
All 3 dependent reports regenerated fresh from the live DB, in order: `catalogue-coverage-audit-
20260921-v3` → `catalogue-question-wording-review-20260921-v7` → `pipeline-wiring-audit-20260921-
v3`. Verified: 0 dead-citation traces remain anywhere; mechanism/placement counts unchanged
(text-only fix, no wiring change). Full record: `BUILD.md` #307.

### Finding 16 — the same/broaden/new dedup mechanism has essentially never fired: 0 of 378 pairs merge, root cause is a wording-similarity threshold that can't recognize paraphrased LLM output (2026-09-21, escalation #1824)

Researcher challenge, verbatim: *"I thought the rule is that the same observation should never be
repeated, if another verse or instance in the same verse refers to the same observation then it
creates another node, not another observation. also a word observation can never just be a repeat
of the lexical meaning, it need to state what is the meaning in the context. I doubt if these rules
have ever been applied."* Checked precisely, with real similarity-score computation — both rules
are real, pre-existing, documented design principles, and both are being systematically violated.

**Rule 1 confirmed real** — escalation #1692's `ib_node` finalization doc (2026-09-12), researcher's
own words: *"if ib_node refers to the same observation... then a row is created, for each item
referencing the same observation."* `recordingpass.py` implements this via a `difflib.
SequenceMatcher` text-similarity check (threshold 0.85): above it, align into the SAME observation
with a new node; below, a genuinely new observation. Computed the actual similarity scores for all
28 `M0.1.1` observations recorded for `H3034` — **378 pairwise comparisons, maximum similarity ever
seen 0.51, mean 0.19, zero pairs reached 0.85.** Not a near-miss — a systemic failure to trigger.
Root cause: independently-generated LLM paraphrases of the same claim vary in wording/structure
every time; character-level text similarity between paraphrases is intrinsically low (0.1–0.5) even
when the semantic content is identical. The 0.85 threshold is calibrated for near-verbatim repeats
(typos, trivial edits), not paraphrase-level semantic equivalence — it essentially never fires
against real LLM output.

**Rule 2 also confirmed real** — `WA-verse-reading-technique-v4-2026-08-05.md`, the foundational
method doc: *"Verse reading is not pattern recognition, it is about the meaning in context of each
element."* Rereading Finding 13's own 8-sample `H3034`/`M0.1.1` set against this standard: 6 of 8
restate the word's generic root meaning/essential nature with no real verse-specific content; only
2 (`2Chr.7.3`'s corporate context, `Ps.76.10`'s "arising from human wrath" angle) derive anything
from that specific verse.

**Not retroactively fixed by Finding 13's skip-check.** That fix stops NEW redundant LLM calls
going forward (a strong's word-level battery is now answered at most once, ever) — it does not
clean the duplicate rows already written (28 for `H3034`/`M0.1.1` alone; Finding 13 already found
~30 observations per question per high-frequency strong corpus-wide, suggesting this scale is
systemic, not isolated), and it does not fix the underlying similarity-threshold bug itself, which
would still affect any OTHER stage relying on the same merge logic to consolidate genuinely-
restated content (`M0.6.5`/`M0.6.6`'s progressive relational chain, Stage 3/4's own same/broaden/
new usage) — not checked here, scope not yet established.

**RESOLVED 2026-09-21, same escalation, v3 correction.** Researcher redirected the fix, verbatim:
*"similarity is not matching sentences. Similarly to matching keys... match a) surface b) meaning
extraction keywords c) morph."* Built and verified (`BUILD.md` #312): new `ib_observation.
meaning_keywords` column + `recordingpass.py`'s `_keyword_match_candidate()` — matches on keyword
overlap AND matching (surface, morph_code) together, forcing the align path ahead of prose
similarity. Scoped to the new `M0.7` family only, not retrofitted onto `M0.1`/`M0.5` (already
solved differently). Verified 3 ways, including full integration against real DB schema (rolled
back after): two completely differently-worded observations with matching surface/morph/keywords
correctly consolidated instead of duplicating — exactly the case the original 0-of-378 finding
proved impossible under the old mechanism. Not retroactive — `M67`'s existing 845 `M0.7`
observations predate this fix; future runs benefit.

**2026-09-21 addendum — CSV staleness check, researcher-prompted.** Researcher: *"so is the csv up
to date with with latest planned handling of the questions."* It wasn't — 6 rows stale (5 with
pre-#1822/#1819-fix text, `M0.6.6` missing entirely, and the coverage-audit script's own hardcoded
`PINNED-STAGE1` classifier hadn't been told about `M0.6.6` either, so a first regeneration attempt
wrongly showed it as unreachable — caught and fixed before the deliverable shipped). All 3 reports
regenerated fresh: `catalogue-coverage-audit-20260921-v5` → `catalogue-question-wording-review-
20260921-v8` (`catalogue_review_data.py` reconciled: `M0.6.5`'s stale REVISE entry replaced —
its originally-flagged process-instruction is no longer in the live text, superseded by the #1819
enrichment — and a new `M0.6.6` entry added) → `pipeline-wiring-audit-20260921-v4`. Current
never-answered count unchanged by this session's fixes: 27 `STRUCTURALLY-UNREACHABLE` + 4
`EXCLUDED-SCIENCE-EXTRACT` — the dead-citation fix (#1823) repaired question TEXT, not placement.
Confirmed directly: beyond `M0.6.6`, no other gap-filling questions have been proposed for this
27+4 set — #1806's original ask remains open.

### Finding 17 — full gap-closure design delivered for all 31 unanswerable questions + the known incomplete-data blocker (2026-09-21, escalation #1806, closes the original ask)

Researcher instruction, verbatim: *"you need now to focus on all the questions that is either not
answerable, or have incomplete data for answering, and have every question supported in a design
suggestion on how we going to close the gap."* Full design: `outputs/gap-closure-design-
20260921.md`. Every one of the 31 unanswerable questions (27 `STRUCTURALLY-UNREACHABLE` + 4
`EXCLUDED-SCIENCE-EXTRACT`) sorted into 5 categories by what actually closes it:

- **A (16)** — genuinely per-verse questions (10 already `Verse-context`-scoped, 6 mis-tagged
  `Word/term (lexical)` despite identical "in this verse" wording). Fix: re-scope the 6, then one
  code change extending Stage 1's selection to dynamically include `scope='Verse-context'` — same
  treatment `D7.7.1` already gets. Named tradeoff: up to 16 more questions per Stage 1 call, on
  top of Finding 13's own cost finding.
- **B (4)** — already aggregate-worded despite the wrong scope tag; re-scope only, no code change,
  3 of 4 match a direct sibling's already-live scope.
- **C (2)** — new Stage-1 question, same mechanism `M0.6.5`/`M0.6.6` already use.
- **D (5, `X0.4.1`–`3` + `M0.6.3`/`M0.6.4`)** — genuinely need the `char-synergy` stage named in
  the original `#1682` spec and every stage module's own docstring but never built (confirmed
  live: 0 `cfg_step` rows for it). Re-scoping alone would make Stage 4 attempt these with the
  wrong data (no cross-cluster vocabulary access, no cross-subgroup visibility) — the exact
  failure mode this session has spent most of its time diagnosing elsewhere, not something to
  repeat here on purpose. Flagged as real, separate future build work.
- **E (4)** — already designed on escalation #1805 v5, not re-derived.

Plus the one known **incomplete-data** blocker (distinct from placement): `M83/A_general_seeking`
(Finding 11) — both member strongs simultaneously exceed Stage 3's occurrence cap, needs the
existing single-strong split logic extended to 2+ strongs at once. Nothing in this design has been
applied — Categories A/B/C are low-risk and buildable once confirmed; D needs its own scoping pass
as a genuine 5th stage; E and the `M83` blocker each have their own already-tracked open decision.

**2026-09-21, extended correction cycle and Category A actually built (escalation #1806 v14-v20,
`BUILD.md` #310).** Researcher pushback, correctly: Category A's original placement (Stage 1,
characteristic-scoped) was wrong twice over — Stage 1 must never be characteristic-aware ("verse-
reading does not know, and does not answer to a char"), and the answer must be per-occurrence, not
settled-once, since a strong can behave differently verse to verse. Applied, not just re-designed
again: a new `concise-and-verse-specific-obs-text` method rule (root-causing Finding 16/#1824's
0-of-378-merge failure — generic padded prose, not a broken algorithm) applied first, since the
new questions' correctness depends on it; then 16 new word-level, characteristic-agnostic
verse-reading questions (`M0.7.1`-`16`, one per Category A char-question, `D10.4.1`'s own worked
example now `M0.7.4`), wired into Stage 1's actual selection/prompt code, verified end-to-end
against real M49 data. Honestly incomplete: this is the SUPPLY side only — the original char-
questions (`D10.1.1` etc.) are not yet wired to CONSUME these observations, which needs Stage 3
to start answering real `question_code`s for the first time (currently 0 of 118 live rows do) —
a materially bigger, separate change, flagged not rushed.

**2026-09-21, first live test — 4 real failures, all fixed, then confirmed clean** (`BUILD.md`
entry #311, escalations #1825-#1828). Testing the supply side above against real `M67` data failed 4
times before succeeding, each auto-raising its own escalation, each a genuine bug not a fluke:
`M0.7`'s roughly-doubled per-strong question count reopened a truncation failure mode `#1723`
had already fixed once — the first fix attempt (halve the verse-count cap) was directionally
right but the wrong lever (checked live: `M67`'s own 5-verse chunks range 6-21 distinct M-code
strongs, a fixed verse count can't reliably bound that). Real fix: batch by strong-density
directly (`_chunk_verses_by_strong_density`, new, `iba/app/handlers/lexical.py`). A second,
unrelated bug (raw control characters in `obs_text` breaking strict JSON parsing) fixed with
Python's own `strict=False` leniency, across all 5 modules sharing the same parse pattern.
**Confirmed live, 5th attempt:** `M67` completed clean, 18/18 batches, $3.12 spent, 0 failures,
**845 real `M0.7` observations across 42 strongs** — the substantiation layer is live, not just
designed. All 4 escalations closed with this live result as their resolution.
