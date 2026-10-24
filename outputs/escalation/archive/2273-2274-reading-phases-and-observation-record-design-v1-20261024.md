# #2273 and #2274 Design (v1): Reading.ps1 on the phases (B1), and the observation record shape (B2)

**Date:** 2026-10-24 · **Escalations:** #2273 (B1), #2274 (B2), from #2268 · **Status:** design for the
researcher's decision. Nothing has been built or changed.

Researcher, chat 2026-10-24 14:26 (verbatim, on #2273 v2): *"Run session-close and commit; start the builds
(design for B2 and B1 first) in a fresh Developer Mode session."* Researcher, chat 2026-10-24 (verbatim):
*"Start #2268 build B1 (#2273, Reading.ps1 on the phases)."*

What the design must deliver is fixed in `outputs/escalation/2268-config-alignment-change-set-v1-20261024.md`
§9 (B1, B2) and the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md` §2 to §5.
B2 comes first in this file because B1's observe step writes the record B2 defines.

---

## 1. What is there now (checked against the live database and code, 2026-10-24)

**The reading process** (`iba/app/lib/reading.py`, `iba/app/ps/Reading.ps1`, escalation #2228) has seven steps
and three gates:

| Step | What it does now | State after |
|---|---|---|
| Open | scope resolved and collated, verses kept, the gap JSON written (only for gap types with phase `recording`) | `open` |
| Record | the gap JSON's records written: observations (`not_read`, `read_in_files_only`), responses on open items, faces on strand hits | `open` |
| Check (gate 1) | every gap item has a row or a reason; verses marked analysed | `recorded` |
| Synergy | the synergy JSON built from the tables: observations, claims, blocks, open items | `recorded` |
| Apply | claims, dispositions, tellings, blocks rewritten, open items settled | `recorded` |
| Check (gate 2) | every observation carried or disposed, every claim told or held, every open item settled | `synergised` |
| Publish (gate 3) | the touched chapters published and copied | `published` |

Four readings exist, all `published` (m64-choose, m64-willing, m64-plan, m64-dedicate, all on #2247, home M64).

**What differs from the plan's phases** (plan §2):

| # | Gap between the code and the plan | Where it shows |
|---|---|---|
| G1 | No objective. A reading has a label and a home cluster only (`reading` table has no objective column). The plan's 0.C is a scope with a clear objective, which defines the home of what is recorded (RO10). | `reading` schema; `open_()` |
| G2 | 0.GAP pre and D4 observe are one step. Record writes the pre-gaps and the verse readings together, under one gate. The plan has the pre-gaps processed into the tables before the next gate (RO12), and only then the verses read (RO1). | `record()` |
| G3 | The gap types in config carry a phase of `recording` or `synergy`, not the plan's phases (0.GAP pre, D4 observe, 0.GAP post). | `cfg_setting reading.gap_types` |
| G4 | Open fills only four of the ten `recording` gap types (`not_read`, `read_in_files_only`, `meaning_missing`, `open_item`). The other six get an empty section. It also still looks for `hit_unread`, which is no longer an enum value, so strand hits are never put in the file. | `open_()` lines 181 to 214 |
| G5 | D3 (the current claims on the scope) is not read before observing. Claims first appear in the synergy JSON, after the verses are read. | `synergy()` |
| G6 | No step `reading.observe`. The 39 reading-a-verse method rules (RO1, RO2, RO11, RG-01 to RG-25, RW-01 to RW-11) sit on `reading.record`. | `cfg_method_rule` |
| G7 | Narrating is inside Apply, not a phase of its own. | `apply()` |

**The observation record** (`ib_observation`, written by `recordingpass.record_strand_observations`):

| # | Gap between the table and the plan (§3, RW-01 to RW-11) |
|---|---|
| H1 | No columns for face, role, operation, route or home. `parties` exists (the October ledger part). The parts are listed in `cfg_setting reading.observation_parts`, and the enums `observation_role` (characteristic, qualifier, standalone) and `observation_route` (A, B, C) exist, but no code reads them. |
| H2 | A reading writes stage `strand-reading`, tag `key-statement` (`recordingpass.STRAND_STAGE`, `STRAND_TAG`). The stage `reading` is in the enum and has its status flow (`cfg_status_flow ib_observation.reading`), but nothing writes it. |
| H3 | Dispositions are kept as `status` (resolved, open, silent, withdrawn) with the reason or the item in `revisit_note`. The enum `observation_disposition` (told, claim, held, data, context, withdrawn) is not used by any code. |
| H4 | A soft delete sets `status='withdrawn'` and overwrites `revisit_note`. The earlier note is lost, and no change other than supersede is recorded with its reason (RW-01). |
| H5 | Nothing stops two rows for the same verse, word and M-code (RO11, RW-03). |

Live counts (`SELECT stage, status, count(*) FROM ib_observation GROUP BY 1,2`): verse-reading 10,595 (4,953
withdrawn), strand-reading 773, char-answers 748, char-reading 118, char-subgroup 19; stage `reading` 0.

---

## 2. B2: the observation record

### 2.1 New columns on `ib_observation`

| Column | Holds | Controlled by |
|---|---|---|
| `face` | how the word appears in this verse, the circumstance, and why it differs from its other occurrences (RG-09) | text |
| `role` | characteristic, qualifier or standalone (RG-03) | `cfg_enum observation_role` |
| `operation` | the inner-being operation the verse shows (RG-03) | text |
| `route` | A, B or C (RG-06) | `cfg_enum observation_route` |
| `home` | the scope objective the observation was recorded for (RO10); see decision D2 | see D2 |
| `disposition` | where the observation ended up (RW-10) | `cfg_enum observation_disposition` |
| `disposition_note` | the reason, or the claim or item that carries it | text |

`parties` stays as it is. The six parts are read from `cfg_setting reading.observation_parts`, never listed in code.
Each column gets its `cfg_column` row and is added to the `ib_observation` write grant for `reading.observe`.

### 2.2 Stage and tag

A reading writes `stage='reading'`. The tag is still required (`tag NOT NULL`); see decision D3.

### 2.3 Every change kept with its reason (RW-01, H4)

A new table **`ib_observation_change`**: one row per change to an observation (observation, column, old value,
new value, reason, run_id, by, at). The writer refuses a change to a `reading` observation without a reason. A
soft delete is a change of `disposition` to `withdrawn` (and `status` to `withdrawn`), with its reason, and nothing
is overwritten. Rows of the older stages are not touched by B2. Gathering them is W-3.

### 2.4 No duplicate rows (RO11, RW-03)

Before writing, the writer refuses an observation of stage `reading` when a live `reading` observation already
grounds the same verse, strong and cluster for the same home. Several verses or terms on one observation stay
as several `ib_node` rows. What counts as "the same" is decision D4.

### 2.5 What B2 leaves to other builds

- The collation reading every observation of a verse, not only `draft`: B4 (#2276).
- The faces of the ledgers gathered into `face`: B8 (#2280), W-3.
- The quality checks on the parts at the gates: B11 (#2283).

---

## 3. B1: Reading.ps1 on the phases

### 3.1 The steps and states

D1 and D2 (word level and characteristics) run on their own schedule in their own steps, built by B3 (#2275).
They are not steps of a reading.

| Phase (plan §2) | Step | Reads | Writes | Gate (checked from the tables) | State after |
|---|---|---|---|---|---|
| 0.C Scope | **Open** `-Objective "…"` (new, required) | base data for the scope | the reading with its objective, its verses; the collation | — | `open` |
| 0.GAP pre | **Open** writes the pre-gap JSON; **Gather** writes it into the tables | every table for the scope, once (RO5); all observations already recorded for each verse | rows, or a reason per gap item; new open items | **Check**: every pre-gap item has a row that exists or a reason (RO12) | `gathered` |
| D3 + D4 Observe | **Observe** builds the observe JSON; **Record** writes it | per verse: its passage, all its observations in focus (RO2), the current claims resting on the scope (D3) | observations with their parts (B2) | **Check**: every verse of the scope has an observation, or a reason, for each M-code in focus and each T-code found relevant; every observation holds its parts | `observed` (verses marked analysed) |
| D4 Claims with 0.GAP post | **Synergy**, then **Apply** (as now) | the scope's observations and claims | claims, dispositions, open items settled | **Check**: the post-claims gap types (observed_no_claim, claim_not_told, claim_without_observation, citation_without_record) clear, from the same read (RO7) | `synergised` |
| D4 Narrate | **Apply** (as now; see D5) | claims and blocks | blocks | inside the gate above | — |
| Publish | **Publish** (as now) | — | the published files | as now | `published` |
| any | **Account** (as now, per state) | the tables | — | — | — |

The changes to the code:

1. **`open_()`** takes `-Objective` and writes it to a new column `reading.objective`. The gap JSON holds only the
   gap types of phase `pre` (G3, G4). Each type's detection reads from a registry keyed by the gap type's name,
   so B6 (#2278) adds the checks for the six types that are empty today without changing `open_()`. B1 builds
   the four that exist today (`not_read` moves to the observe phase) and fixes `face_not_gathered` to read
   `reading_strand_hit` (the old `hit_unread`).
2. **`record()`** is split in two. **Gather** writes the pre-gap JSON (the current `record()` minus verse readings).
   **Record** writes the observe JSON through the B2 writer.
3. **New `observe()`** builds the observe JSON once the reading is `gathered`. Per verse: reference, passage
   (the verse with its neighbours, from `verse`), words with strong, cluster and role tags, every observation
   already recorded for the verse (any stage, any status but withdrawn), and the claims resting on the scope.
   Per M-code in focus, a slot to fill with an observation (the parts from `reading.observation_parts`), an
   existing observation id that already says it, or a reason.
4. **`check()`** runs the gate for the reading's state: `open` (pre-gaps), `gathered` (observe), `observed`
   (post-claims, as gate 2 now). Each gate's gap types come from `reading.gap_types` by phase.
5. **`synergy()`, `apply()`, `publish()`** keep their behaviour. `synergy()` and `apply()` require state
   `observed` instead of `recorded`.

### 3.2 Config rows (all through `apply_logged`, each registering itself, rule 62)

| Row | Change |
|---|---|
| `cfg_enum reading_state` | add `gathered`, `observed`; retire `recorded` after the migration below |
| `cfg_setting reading.gap_types` | each type's `phase` becomes `pre`, `observe` or `post` (plan §4) |
| `cfg_step` | add `reading.gather`, `reading.observe` (ordinals renumbered); `reading.record` and `reading.check` descriptions restated |
| `cfg_method_rule` | RO1, RO2, RO11, RG-01 to RG-25, RW-01 to RW-11 move from `reading.record` to `reading.observe` |
| `cfg_column` | `reading.objective`; the seven `ib_observation` columns; `ib_observation_change` columns |
| `cfg_table` | `ib_observation_change` |
| `cfg_write_grant` | `reading.gather`, `reading.observe`, `reading.record` on their tables |
| `cfg_status_flow ib_observation.reading` | restated against the disposition column (D6) |

### 3.3 The four published readings

They stay `published`. Their `recorded_at` stays as it is. Their objective is left null and shown as "before
#2273" in Account. No observation of theirs is changed (W-3 does the gathering).

### 3.4 Documents

BUILD.md entry; USER-GUIDE.md section on Reading.ps1; the `Reading.ps1` help text; the Excel tool sheet for
Reading.ps1 (the drift finding on #2270 is closed with it).

---

## 4. Test, on a copy (B:97)

On a copy made with `iba/app/lib/dbsnapshot.copy_db`:

1. Migration: columns, table and config rows in place; config validates clean; the four readings still `published`
   and their Account still renders.
2. A trial reading of three verses (RG-19), run through every step: each gate refuses while its gaps stand, and
   passes once they are filled.
3. The B2 writer refuses: a part outside its enum; a duplicate row; a change without a reason. A soft delete
   keeps the earlier note.
4. No test suite exists for `reading.py`, `strandreading.py` or `recordingpass.py` (none found in the repo,
   2026-10-24). The test is a script under `iba/app/migration/` run against the copy, kept with the build,
   as the #2268 config alignment test was.

The results are written to `outputs/escalation/2273-2274-test-results-v1-<date>.md` and recorded on both items.

---

## 5. Decisions for the researcher

Each is a new decision (B:44), not settled by the rulings. My recommendation is first.

| # | Question | Options | Decision |
|---|---|---|---|
| D1 | Do B1 and B2 build as one change set? | (a) one build and one test, since Record writes the B2 shape; (b) B2 first, then B1 | |
| D2 | What does `home` hold? | (a) the reading's id, so the objective is read through it; (b) the objective text copied onto each row; (c) the home cluster, as `cluster_code` does now | |
| D3 | Which tag does a `reading` observation carry? | (a) a new tag `reading-observation`; (b) the reader picks from the existing tags (`ib_observation.tag`) per row; (c) make the tag optional for stage `reading` | |
| D4 | When are two observations duplicates? | (a) same verse, strong, cluster and home; (b) same verse, strong and cluster, whatever the home (one row across scopes, with nodes added) | |
| D5 | Is Narrate its own step and gate? | (a) no: stays inside Apply, as now, checked at the post gate; (b) yes: a `narrate` step after the claims gate | |
| D6 | How do `status` and `disposition` relate for stage `reading`? | (a) `disposition` holds where it ended up, `status` keeps only draft or withdrawn; (b) both kept, with `status` derived from `disposition` | |

Once approved, B1 and B2 are built and tested on a copy in this session, and the results recorded on #2273
and #2274.
