# Cluster-reading pipeline — full trace, dispatch to write

> Every stage, every config read (with live current value), every method rule (verbatim), every
> LLM instruction (verbatim), every input/output JSON shape, every validation/recording step,
> every status transition. Built by reading all 3,137 lines of the 9 files that make up this
> pipeline end to end — `run.py`, `handlers/lexical.py` (`meaning`), `handlers/cluster.py`
> (`subgroup`/`reading`/`answer`), `versereadinggenerate.py`, `subgroupgenerate.py`,
> `charreadinggenerate.py`, `charanswergenerate.py`, `recordingpass.py`, `clusterstatus.py` — not
> summarized from memory or from prior session notes.

## Contents

- [0. Dispatch layer (`run.py`)](#0-dispatch)
- [1. Stage 1 — verse-reading (`lexical.meaning`)](#stage-1)
- [2. Stage 2 — char-subgroup (`cluster.subgroup`)](#stage-2)
- [3. Stage 3 — char-reading (`cluster.reading`)](#stage-3)
- [4. Stage 4 — char-answers (`cluster.answer`)](#stage-4)
- [5. The single writer (`recordingpass.py`)](#recordingpass)
- [6. The status machine (`clusterstatus.py`)](#clusterstatus)
- [7. Findings surfaced while tracing](#findings)

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
  deliberately including the mechanically-unwired T2/T6/T10–T15 tags per
  `role-list-includes-unwired-tags`).
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
