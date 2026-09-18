# Session Log — 2026-09-18

**Scope:** A Developer Mode session that completed the analytics-processing build side of #1706's
cluster-reading pipeline — **4 of 5 stages now built, registered, and validated live end-to-end on
the `M67` pilot cluster: `verse-reading` → `char-subgroup` → `char-reading` → `char-answers`**.
Also fixed six real infrastructure gaps found along the way (a missing status transition, two
`recordingpass.py` write-path bugs, a stale documentation gate, an unregistered tag, and a missing
catalogue `window` taxonomy — the last built out fully, 11 windows across all 99 active questions),
then worked through every on-hold/in-progress escalation tied to this series and prepared the
resolved ones for approval. **Stage 5 (`char-synergy`) remains open and undesigned** — the
researcher's own explicit next question, not resolved here.

---

## What got built, in order

1. **Stage 2 (`char-subgroup`) completed for `M67`.** The prior session's own reset (`#1723`,
   progressive-relational redesign) had wiped `M67`'s Stage 2 data; re-ran it live: 4 subgroups,
   9/9 strongs placed, `$0.2183`.
2. **A stale "gate" retired.** Three documents were still citing `#1704`/`#1705` (both closed since
   2026-09-15/16) as an open blocker on Stage 3 — the researcher caught this recurring and asked
   for it fixed for good. Corrected all three docs plus `BUILD.md` #286; confirmed live that the
   actual resolution (`M0.6.5`, question-driven catalogue expansion, not a forced mechanical walk)
   had already been built and was working.
3. **Stage 3 (`char-reading`) built** (`lib/charreadinggenerate.py`, `handlers/cluster.py:reading`,
   `CharReading.ps1`, `register_cluster_reading_step_v1_20260918.py`). Found and root-fixed a real
   gap on the way: the `allocated`→`ready_for_reading` subgroup-status transition was designed
   (`#1690` §3a) but never built. Ran live on all 4 of `M67`'s subgroups: 26 observations, `$0.3518`
   (one transient JSON-formatting glitch on the first-ever call, escalation `#1726`, confirmed not
   truncation, clean on retry, closed self-correctable). `BUILD.md` #287.
4. **Stage 4 (`char-answers`) built** (`lib/charanswergenerate.py`, `handlers/cluster.py:answer`,
   `CharAnswer.ps1`, `register_cluster_answer_step_v1_20260918.py`), a 52-question characteristic-
   grain catalogue battery per subgroup (queried live from the catalogue, excluding `D7.7.1` and
   4 science-extract-dependent questions). Found and root-fixed two real bugs in `recordingpass.py`
   itself (shared by all 4 live stages): genuine occurrence-less negative findings were being
   silently discarded (lost 10 of 52 answers on the first run, fixed, clean re-run); `ib_node.strong`
   was never carrying the per-occurrence value, only the observation's own outer `strong` (invisible
   for Stages 1–3, load-bearing for Stage 4's new subgroup-wide shape). Also found and fixed a third,
   independent gap: `needs_adjacent_verse_context` had been named in every stage's own prompt since
   Stage 1 but was never actually registered in `cfg_enum`. Ran live on all 4 subgroups: 259
   observations, all 52/52 battery questions answered every time, `$1.48` total. `BUILD.md` #288.
5. **Researcher's own direct review of the `char-answers` data surfaced 4 more real issues.**
   Investigated each before touching anything:
   - `ib_observation.cluster_subgroup_id` / `ib_node.cluster_subgroup_code` — real, already-
     registered `cfg_column` entries `recordingpass.py` had never populated for any stage. Fixed
     (both take the caller's own already-known subgroup as an explicit parameter now); backfilled
     285 `ib_observation` / 594 `ib_node` rows written before the fix, all resolved cleanly.
   - `cluster.status` — genuinely stale (`M67` stuck at `ready_for_reading` despite all subgroups
     reaching `answer_complete`). Built the `ready_for_reading`→`ready_for_observations` rollup
     (deliberately scoped to only this one transition — the next depends on undesigned Stage 5),
     ran it once for `M67`.
   - `window` — checked and confirmed NOT a code bug (correctly deriving from the catalogue exactly
     as designed); the real gap was that the catalogue itself only had `window` populated for ~4 of
     ~150 questions. Flagged for the researcher's own call rather than guessed at.
   `BUILD.md` #289.
6. **Window taxonomy designed and applied, per researcher's clarification of the column's actual
   purpose** ("show from which angle we are observing the data... helps compare answers of the same
   nature"). Read all 99 active catalogue questions in full, grouped by real analytical angle (not
   mechanically 1:1 per component — the existing `meaning` window already spanned 2 components on
   this same principle). Extended the 3 existing windows and designed 8 new ones (`literary`,
   `cognitive`, `affective`, `operational`, `constitutional`, `origin`, `scientific`, `faculty`).
   Applied live: 83 catalogue rows assigned a window (0 active questions now NULL), 8 new `cfg_enum`
   values registered, all 259 existing observations backfilled (259/259 resolved). `BUILD.md` #290.
7. **Escalation reconciliation.** Per researcher instruction ("prepare on-hold/in-progress
   escalations related to this series for approval"), triaged all 20 open escalations, found and
   fixed a real proactive bug along the way (`#1717`, `narrativegenerate.py`'s own copy of the
   already-fixed extended-thinking vulnerability — fixed before its first-ever live run), and moved
   6 items to `ready_for_approval` with real, substantiated resolutions (not rubber-stamped):
   `#1706` (master build thread, consolidated final status), `#1682` (parent design thread, realized
   in code), `#1712` (catalogue adequacy, its one open item resolved by practice), `#1703` (adjacent-
   context flag rate, now measured on real data: 3.1%/4.2%), `#1717` (the bug fix above), plus `#1526`
   and `#1607` verified still accurate from prior sessions. Left `#1695`/`#1698` (Stage 5 design)
   honestly open — their trigger condition is now met, but no design content exists yet, and marking
   them approved would have been dishonest. Researcher approved the prepared items same session.

## Escalations touched, by id, outcome

- **`#1706`** (parent build thread) — `v33`→`v39`, `ready_for_approval`, approved.
- **`#1682`** (original process design) — `v20`, `ready_for_approval`, approved.
- **`#1712`** (catalogue adequacy) — `v7`, `ready_for_approval`, approved.
- **`#1703`** (adjacent-context flag rate) — `v5`, `ready_for_approval`, approved.
- **`#1717`** (narrativegenerate.py bug) — raised → `v2`, `ready_for_approval`, approved; real fix
  applied same turn.
- **`#1726`** (auto-raised: char-reading first call, JSON not valid) — `completed`/self-correctable,
  confirmed transient (retry succeeded, not truncation).
- **`#1695`** (Stage 5 design) — `v3`, status update only, correctly left `in-progress`/`review`.
- **`#1698`** (Stage 5 cross-cluster gap) — `v3`, status update only, correctly left
  `in-progress`/`review`.
- **`#1526`, `#1607`** — verified unchanged, already `ready_for_approval` from prior sessions.
- Confirmed **unrelated to this series**, left untouched: `#737`, `#770`, `#784`, `#1022`, `#1385`,
  `#1386`, `#1387`, `#1533`, `#1544`, `#1658`, `#1699`.

## Files and deliverables

**New library/handler code:** `iba/app/lib/charreadinggenerate.py`, `iba/app/lib/
charanswergenerate.py`; `iba/app/handlers/cluster.py` (new `reading()`/`answer()` handlers, `subgroup()`
now also advances subgroup status); `iba/app/lib/clusterstatus.py`
(`advance_subgroups_after_allocation`, `require_subgroup_ready_for_reading`/`_answer`,
`advance_subgroup_after_reading`/`_answer`, `recompute_cluster_status_rollup`); `iba/app/lib/
recordingpass.py` (2 real fixes: occurrence-less findings no longer discarded, per-occurrence
`strong` now carried through; `subgroup_id`/`subgroup_code` params added); `iba/app/lib/
narrativegenerate.py` (proactive extended-thinking fix).

**New PS entry points:** `iba/app/ps/CharReading.ps1`, `iba/app/ps/CharAnswer.ps1`.

**New migrations, all idempotent, dry-run verified, committed live:** `register_cluster_reading_
step_v1_20260918.py`, `register_cluster_answer_step_v1_20260918.py`, `register_needs_adjacent_
verse_context_tag_v1_20260918.py`, `backfill_subgroup_columns_char_reading_answers_v1_20260918.py`,
`design_and_backfill_char_windows_v1_20260918.py`.

**Updated in place:** `iba/app/BUILD.md` (entries #286–#290), `iba/app/USER-GUIDE.md` (§12b-vi,
§12b-vii), `iba/docs/1706-full-pipeline-build-checklist-v1-20260917.md`, `iba/docs/1706-role-
driven-walk-consolidated-status-v1-20260917.md`.

**Database (live, real state change):** `M67`'s Stage 2/3/4 data (subgroups re-run, 26 char-reading
+ 259 char-answers observations, all with correct `cluster_subgroup_id`/`cluster_subgroup_code`);
`cluster.status` (`M67` → `ready_for_observations`); `cluster_subgroup.status` (all 4 subgroups →
`answer_complete`); `wa_obs_question_catalogue.window` (83 rows newly assigned, 0 active questions
NULL); `cfg_enum` (`ib_observation.tag` +1, `ib_observation.window` +8); `cfg_step`/`cfg_write_
grant`/`cfg_method_rule` (2 new steps, 4 write grants, 19 method rules).

**Real spend, honestly logged** (`_analytics/lexical-extracts/lexical-llm-usage.csv`), all on `M67`:
Stage 2 `$0.2183`; Stage 3 `$0.4510` across 5 calls (1 wasted on the transient JSON glitch, 4 clean
— net productive spend `$0.3518`); Stage 4 `$1.4799` across 5 calls (1 partial pre-fix run
superseded by a clean re-run). **Session total: `$2.1492`.**

## Decisions — researcher's own vs. Claude self-correctable

**Researcher's own decisions this session:** the "gate is no longer relevant, update it" instruction
that triggered the stale-documentation correction; the window column's actual purpose and design
method ("derive the windows... from the component_title, but name them to align the objective");
the instruction to work through all on-hold/in-progress escalations related to this series and
prepare them for approval; approval of the prepared items; the decision to exit Developer Mode for
further testing.

**Claude self-correctable fixes, closed directly, not escalated:** the missing `allocated`→
`ready_for_reading` subgroup-status transition; the two `recordingpass.py` write-path bugs
(occurrence-less findings, per-occurrence `strong`); the unregistered `needs_adjacent_verse_context`
tag; the missing `cluster_subgroup_id`/`cluster_subgroup_code` population; the `cluster.status`
rollup; the `narrativegenerate.py` proactive bug fix (`#1717`); the transient JSON-formatting
failure (`#1726`, confirmed transient, no code change).

**Design work presented, not silently decided:** the 11-window taxonomy (component-title groupings)
was Claude's own analytical work per the researcher's stated method, but is presented for review as
content, not asserted as beyond question — the researcher can rename/regroup any of it.

## Open items carried into the next session

1. **Stage 5 (`char-synergy`) design** — `#1695`/`#1698`, genuinely not started. Trigger condition
   ("after complete build+test up to synergy") is now met. Researcher has not yet said whether to
   start this now or hold it.
2. **Further testing of Stages 1–4 beyond `M67`** — per this session's own closing discussion, this
   belongs in a fresh, standard-permission (App Mode) session, not a continuation of this one.
3. **Science-extract file wiring for `D9`/`D11`/`D12`** — excluded from Stage 4's battery this
   build, wiring still not decided (`checklist`'s own long-standing note, unchanged this session).
4. **`#729`** (cross-cluster co-occurrence mechanism) — still unowned, untouched this session.

## Git state — confirmed, not asserted

26 files staged and committed (`database/bible_research.db` and `backups/` excluded per standing
rule — neither present this session), pushed to `origin/main`:

```
$ git add -A
$ git commit -m "session 20260918: ..."
[main fc6d597d] session 20260918: cluster-reading pipeline Stages 3-4 built and validated on M67
(char-reading/char-answers), six infra gaps root-fixed (subgroup-status transition, two
recordingpass.py write-path bugs, unregistered tag, subgroup columns never populated, stale
cluster.status rollup), 11-window analytical-angle taxonomy designed and applied catalogue-wide,
escalation series reconciled and prepared for approval (Stage 5 synergy left open), session log
 26 files changed, 4538 insertions(+), 64 deletions(-)

$ git push origin main
To https://github.com/lcilliers/Bible_Projects.git
   e9734e51..fc6d597d  main -> main

$ git status
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean

$ git log -1 --format="%H %ci %s"
fc6d597d4fe09ff3de5e0a726fe51dd1593f2e86 2026-09-18 05:57:01 +0100 session 20260918: ...
```

**Note on scope:** this commit includes the researcher's own manual DB export
(`outputs/csv/verse-reading-observations v2 20260918.csv`) and SQLite scratch-query files
(`scripts/SQLite/IBA_DB/*.sqlite3-query`) — staged per the standing rule to commit the full
outstanding working tree at close, not filtered to "written by Claude this session only." Both
read before staging, confirmed benign (plain data export, plain SQL scratch queries).
