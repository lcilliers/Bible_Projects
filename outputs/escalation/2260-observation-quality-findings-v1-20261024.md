# #2260 Observations written since the recast, checked against the observation rules (v1)

**Date:** 2026-10-24 · **Escalation:** #2260 · **Status:** findings only. Nothing has been changed. The next step waits for your direction.

Researcher, chat 2026-10-24 (verbatim): *"before I answer you, because you are running ahead.  it seems to me that the work we have done since yesterday's recasting of the process have not properly updated the ib_observations per the rules for the observations, and your gap analysis is not doing any quality checks."*

**Both are confirmed.**

## 1. What was written since 2026-10-22

Query (read-only, iba.db): `ib_observation` with `created_at >= '2026-10-22'`, grouped by stage, tag and question code.

| Stage | Tag | Question code | Rows | Ids | No Strong's |
|---|---|---|---|---|---|
| `strand-reading` | `key-statement` | none | 773 | 11762 to 12534 | 505 |

By run:

| Source | Rows | Ids |
|---|---|---|
| #2172 catch-up imports of the October strand ledgers (fear 140, anger 313, life-death 159, origin of thought 24) | 636 | 11762 to 12451 |
| `RUN-20261022_135240_954-STRANDREAD` | 26 | 12453 to 12478 |
| The #2247 M64 readings through `Reading.ps1` (seven `-READING` runs) | 111 | 12479 to 12534, plus older rows those runs re-marked |

Every row is written by one function, `iba/app/lib/recordingpass.py:571-601`, `record_strand_observations`. That function fixes:
- stage `strand-reading` and tag `key-statement` for every row;
- `strong` only when the observation's words are a single code, and null otherwise;
- no question code, no window and no word role.

This is the October strand-ledger shape (#2172). The reading process (#2228) reuses it, although the strand steps are retired (#2228 D-a).

## 2. Against the observation rules

| Rule | What it requires | What the rows show |
|---|---|---|
| `cfg_behaviour_rule` 73, role per occurrence | each M-coded word given its role against the verse's main act | **No role is recorded.** 505 of the 773 rows have no Strong's, so the word cannot even be named. |
| `cfg_method_rule` 108 and 119, concise and verse-specific | the finding tied to this verse and this occurrence | **Multi-verse summaries.** Verses per observation: readings 6.5 on average (maximum 42); catch-up 3.8 (maximum 39). Stage 1 (`verse-reading`), before 2026-10-22: 1.05 (9,871 rows). |
| `cfg_method_rule` 112 and 121, span-grounded | answerable only from this occurrence's verse, span and morph | Not met. For example, observation 12479 sets "the sons of God; Lot; David; Elijah and the prophets of Baal" in one row. |
| `wa_obs_question_catalogue`, `cfg_step` `lexical.meaning` and `lexical.relational` | the word-level (M0.1, M0.5) then relational (M0.6.5, M0.7, M0.8.1) answers per occurrence; method rule 125 refuses the relational half without the word level | None of the 773 rows answers a catalogue question. M64 is still at `cluster.status` `t_cluster_assignment_completed`: Stage 1 has not run for it. |
| `cfg_setting ib_observation.tag_guidance` | every tag defined there | `key-statement` is in `cfg_enum ib_observation.tag`, but **it has no guidance entry.** |
| `cfg_enum ib_observation.stage` | a live stage | `strand-reading` is still in the enum, but its steps are retired. |

**The structure passes and the fitness does not.** Each value is a valid enum value, which is why the checks pass, but the rows are not the observations the rules describe (B:24).

## 3. The gap analysis

`iba/app/lib/versecollate.py:166-170`: a verse is "not read" only when it has **no observation of any kind** and no strand face. Any row on the verse counts as read, whatever its stage, tag, Strong's or question coverage. The same test feeds `Reading.ps1`'s gap JSON (`iba/app/lib/reading.py:50`, `:184-189`). Nothing checks, for the words of the scope:
- whether the occurrence has its Stage 1 word-level and relational answers;
- whether the observation names the word, or is a single-verse finding;
- whether a role is recorded.

So the counts in `outputs/escalation/2161-m72-reading-plan-v2-20261024.md` §2 ("with an observation") are **presence counts, not quality counts.** The same holds for the verses gate 1 marked `analysed` in the M64 readings.

## 4. What it reaches

- **#2247 (completed), M64 Will & Resolve.** 111 observations of this shape. Claims C-331 to C-393 rest on them, and they are told in 10.7 and 13.1 and published.
- **The #2172 catch-up.** 662 rows from the October ledgers, imported in this shape.
- **#2161 and #2259.** Both plans rest on the presence counts. Both stay paused.

Not checked yet: whether the observations from before 2026-10-22 in the `char-*` stages meet the same rules.
