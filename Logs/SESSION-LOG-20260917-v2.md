# Session Log — 2026-09-17 (v2, second Developer Mode session of the day)

**Scope:** A second, later Developer Mode session (following the morning's, closed and logged as
`SESSION-LOG-20260917.md`) authorized to build `#1706`'s full 5-stage cluster-reading pipeline.
Built and executed Stage 1 (`lexical.meaning`/`verse-reading`) live against real API calls on
`M67`, then went through an extensive, researcher-driven review-and-correct cycle against the
actual output — surfacing a major core-design correction (verse-reading must be progressive and
relational across the M-code words in a verse, not isolated to one cluster's own member strongs),
which was fully designed, built, and used to reset and redo `M67`'s verse-reading from scratch.
Built Stage 2 (`cluster.subgroup`/`char-subgroup`). Closed out with three researcher-caught data-
quality gaps (`question_code`, `tag`, `obs_text` all had zero write-time validation) — each
root-fixed with a validator plus a backed-up cleanup of the existing bad rows, not just patched.
Session closed here at the researcher's request, to hand off cleanly into a fresh Developer Mode
session for the next phase.

---

## Escalations touched, by id, outcome

- **`#1706`** (Full lexical stack rebuild — consolidated build proposal) — parent thread,
  `v29`→`v32`. Carries the role-driven-walk resolution record from earlier the same day. Still
  `in-progress`, `next_action=review`, assigned Researcher.
- **`#1718`** (auto-raised: 1 code in scope with no `cluster_strong` allocation) — root-caused and
  fixed, `completed`/self-correctable.
- **`#1719`** (Layer 1 role staleness after post-build `cluster_strong` edit) — carried a pointed
  researcher challenge about a prior `-ShortDescription` misuse; the real fix (a hard-refuse guard
  in `Escalation.ps1`'s `-Action Raise` branch) was built and verified this session, not just
  documented. `re-assigned`, `ready_for_approval`, assigned Researcher.
- **`#1720`** (48 of 95 clusters missing `cluster.gloss`) — carried forward, `re-assigned`,
  `ready_for_approval`, assigned Researcher.
- **`#1721`** (auto-raised: `M67` status mismatch for subgroup allocation) — `completed`/
  self-correctable.
- **`#1722`** (auto-raised: `UNIQUE constraint failed` on `cluster_subgroup`) — root cause was the
  table's plain `UNIQUE` constraints deviating from the established partial-unique-index
  soft-delete convention; fixed via table recreation. `completed`/self-correctable.
- **`#1723`** (Verse-reading must be progressive, relational, not isolated) — the main thread this
  session, `v1`→`v16`. Captured, in order: the core progressive/relational redesign (front-loading,
  `M0.6.5` relational question, `M0.5.11` alternative-meaning question, window redefinition, the
  tag/window conflation finding, the parked-qualifier-role finding, the discovery-mode requirement
  for Stage 5, the `2Cor.8.16`/location test case); the full rebuild and `M67` reset/redo under the
  new mechanism; the `question_code`/`tag`/`obs_text` validation gaps found and root-fixed one by
  one, each via direct researcher inspection of live data, not assumed. Still `in-progress`,
  `next_action=ready_for_approval`, assigned Researcher — genuinely awaiting review, not closed.
- **`#1724`** (auto-raised: `lexical.meaning` crashed, `no such column: n.verse_id`) — root-caused
  (`_prior_relational_context` queried a column `ib_node` doesn't have) and fixed. `completed`/
  self-correctable.
- **`#1725`** (auto-raised: model reply JSON truncated) — root-caused (front-loading increased
  expected output volume past the token ceiling) and fixed via a dedicated smaller batch size plus
  a raised ceiling. `completed`/self-correctable.

Backlog confirmed clean at close: 24 open escalations, none `next_action_assigned_to='Claude'`
(`outputs/escalation/escalation-list-v103-20260917.md`).

## Files and deliverables

**New library/handler code:** `iba/app/lib/subgroupgenerate.py` (Stage 2 assembly); extensive
rewrites to `iba/app/lib/versereadinggenerate.py` (front-loading, prior-relational-context,
`TAG_GUIDANCE`) and `iba/app/lib/recordingpass.py` (`record_subgroups`, `_effective_cluster_code`,
`_window_for`, `_validate_question_code`/`InvalidQuestionCode`, `_validate_tag`/`InvalidTag`,
`_validate_obs_text`/`InvalidObservationText`); `iba/app/handlers/cluster.py` (new `subgroup()`
handler); `iba/app/handlers/lexical.py` (staleness gate, dedicated batch-size setting);
`iba/app/lib/clusterstatus.py` (`require_ready_for_subgroup_allocation`,
`advance_after_subgroup_allocation`).

**New PS entry points:** `iba/app/ps/VerseReading.ps1` (Stage 1), `iba/app/ps/ClusterSubgroup.ps1`
(Stage 2). **Fixed:** `iba/app/ps/Escalation.ps1` (hard-refuse guard on `-ShortDescription` misuse
with `-Action Raise`).

**Migrations run live (all idempotent, dry-run verified before commit), all under
`iba/app/migration/`:** `register_cluster_subgroup_step_v1_20260917.py`,
`fix_cluster_subgroup_unique_constraints_v1_20260917.py`,
`reclassify_g0627_to_t3_v1_20260917.py`, `progressive_relational_verse_reading_v1_20260917.py`,
`fix_lexical_meaning_batch_scaling_v1_20260917.py`, `reset_m67_for_progressive_reading_v1_20260917.py`,
`clean_invalid_question_code_observations_v1_20260917.py`,
`retire_old_layer2_lexical_enrich_v1_20260917.py`, `drop_cluster_gloss_v1_20260917.py`,
`extend_tag_vocabulary_v1_20260917.py`, `retag_answered_no_flag_v1_20260917.py`.

**New docs (`iba/docs/`):** `1706-progressive-relational-verse-reading-v1-20260917.md` — the living
design-capture doc for the whole `#1723` thread, built up across the session, §1–§9.

**New/updated outputs (`outputs/`):** `outputs/markdown/1706-stage1-prompt-visibility-v1-20260917.md`
(real prompt+payload example for researcher review); `outputs/csv/observation.csv`,
`outputs/csv/verse-reading-observations.csv` (researcher's own manual DB pulls, later found to be
stale snapshots and explained as such, not re-exported).

**Updated in place:** `iba/app/BUILD.md` (entries #274–#284), `iba/app/USER-GUIDE.md` (§12b-iv,
§12b-v).

**Database (live, real state change, not just a file diff):** `wa_obs_question_catalogue` +
`window` column, `M0.5.11`/`M0.6.5` questions added; `ib_observation.tag` `cfg_enum` — retired
`instance-meaning`/`cross-cluster-significance`, added `tightly-related`/`no-direct-connection`
mid-session then a further 8 (`qualifier-for-term`, `no-impact`, `not-related-to-meaningful-word`,
`sole-mcode-in-verse`, `cluster-pole-negative`, `cluster-pole-positive`, `attested-pre-nt`,
`nt-coinage`) at close; `ib_observation.window` `cfg_enum` replaced with
`[meaning, action-impact, relational]`; `cluster_subgroup`/`cluster_subgroup_strong` UNIQUE
constraints replaced with partial unique indexes; `G0627` reclassified `T2`→`T3`; `M67`'s
`stage='verse-reading'`/`stage='char-subgroup'` data hard-deleted and redone from scratch (backed
up first); 76 invalid-`question_code` rows deleted; 43 rows retagged off `answered-no-flag`/`none`;
1 content-less `obs_text` row deleted. `M67`'s live verse-reading count at close: **304 valid
observations**.

**Real spend, honestly logged** (`_analytics/lexical-extracts/lexical-llm-usage.csv`): tracked
across the `M67` reset/redo batches and the debug cycles that preceded it (JSON-truncation and
`n.verse_id` crashes both cost real, small API calls before being fixed).

## Decisions — researcher's own vs. Claude self-correctable

**Researcher's own decisions this session** (design work, never self-correctable, per standing
rule): the entire progressive-relational verse-reading redesign — front-loading every M-code
strong's word-level battery on first touch, propagating `M0.6.5` relational findings forward
without duplication, discovery-mode reading for Stage 5 (not built, recorded), the alternative-
meaning gap (`M0.5.11`), the qualifier-role-lost finding (tied to the still-parked `#1598`), the
window redefinition (angle, not pipeline-stage), the tag/window conflation correction; the explicit
authorization to reset and redo `M67`'s verse-reading under the new mechanism; the entire tag-
vocabulary correction sequence (`tag` is a categorisation/filtering value, not just a peculiarity
flag — corrected an earlier, too-narrow framing from the same thread) culminating in confirming
`no-impact`, `not-related-to-meaningful-word`, `qualifier-for-term`, the cluster-pole pair, and the
attestation pair; the meta-instruction to close-read `obs_text` rather than skim for peculiarity,
which is what actually surfaced the broadened scope of `qualifier-for-term` and the pole/attestation
findings.

**Claude self-correctable fixes, closed directly, not escalated:** the `_prior_relational_context`
`n.verse_id` bug (`#1724`); the JSON-truncation/batch-scaling fix (`#1725`); the `cluster_subgroup`
UNIQUE-constraint gap (`#1722`); the `M67` status-mismatch crash (`#1721`); the missing-
`cluster_strong`-allocation gap (`#1718`); and, closed this session but investigated and fixed
properly rather than routed around, the recurring `Escalation.ps1 -ShortDescription` misuse
(`#1719` — a real code fix, a hard-refuse guard, after being told directly this had been patched
around rather than fixed multiple times before).

**Three researcher-caught data-quality gaps, each root-fixed with a validator, not just patched:**
1. `question_code` — bare component codes (`M0.1`/`M0.5`) accepted with no validation; 76 existing
   rows silently un-bindable and permanently mis-flagged as "covered." Fixed:
   `_validate_question_code`/`InvalidQuestionCode`.
2. `tag` — `answered-no-flag` (77% of the corpus) and the unregistered literal `none` (15 rows)
   masking real, filterable findings. Fixed: `_validate_tag`/`InvalidTag` plus the 8-tag vocabulary
   extension and a rewritten prompt.
3. `obs_text` — one row was the literal string `"none"`, tracing to an observation that already
   held the real answer. Fixed: `_validate_obs_text`/`InvalidObservationText`.

All three: write-time validation added first (rejects going forward), then a backed-up, targeted
cleanup of the existing bad rows (never a blind rewrite) — the researcher explicitly checked, at
close, that this was root-cause work and not just item-by-item patching; verified live against the
actual code before answering.

## Open items carried into the next session

1. **`#1723`'s own review** — the whole progressive-relational redesign, the rebuilt/reset `M67`
   verse-reading, and the tag-vocabulary work are all `ready_for_approval` — genuinely awaiting the
   researcher's own review, not decided or closed here.
2. **`#1719`/`#1720`** — Layer 1 staleness and the `cluster.gloss` gap, both `ready_for_approval`,
   not yet actioned.
3. **Stage 2 (`char-subgroup`) execution** — built (`subgroupgenerate.py`, `handlers/cluster.py:
   subgroup()`, `ClusterSubgroup.ps1`) but not yet run live against `M67` post-reset — `M67`'s
   status needs re-checking against the `ready_for_subgroup_allocation` gate before that can
   happen.
4. **Stages 3–5** (`char-reading`/`char-answers`/`char-synergy`) — zero execution code. Stage 5 is
   not even fully designed yet (`#1695`/`#1698` still open); the discovery-mode requirement
   recorded this session against it is a real, concrete requirement, not yet built.
5. **Qualifier T-code reclassification** (`#1598`, parked) — the tag-level `qualifier-for-term`
   partially surfaces this without needing the full T-code project; the T-code project itself is
   still untouched.
6. **Test case flagged for Stage 4**: `2Cor.8.16` — how "location"/faculty handling is dealt with
   (`heart`/`G2588` currently has no `T14` Body-Parts tag despite a locative function in that
   verse). Not built, recorded for when Stage 4 is designed.
7. **The role-driven-walk "expand the questions" instruction's actual implementation status** vs.
   the 12-dimension catalogue realignment done earlier the same day — genuinely unclear from the
   written record, flagged for the researcher rather than guessed at.

## Git state — confirmed, not asserted

_To be filled in immediately after the commit+push below completes, per the established
"(cont.)" pattern — not asserted before it actually happens._
