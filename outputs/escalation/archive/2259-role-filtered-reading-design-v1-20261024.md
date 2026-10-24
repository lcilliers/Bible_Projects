# #2259 Reading: filter the deeper reading on the role of the words (design v1)

**Date:** 2026-10-24 · **Escalation:** #2259, raised from #2161 (M72 Authority & Dominion) · **Status:** design for your decision. Nothing has been built and no config has been changed.

Researcher, chat 2026-10-24 (verbatim): *"A large percentage of the verses have terms that is not directly inner being focussed, but inner being supportive or not inner being related. (e.g.  the word king may be used as a designation, but the verse say nothing about underlying behaviour).  The study should not be contaminated with the terms that have little or no bearing on the inner being.  I would suggest that this decision can only be made after the verse has gone through ib_observation , but the deeper reading of the verses in the next phase must defnitely be filtered on the role of the words."*

## 1. What exists now

- **The rule.** `cfg_behaviour_rule` 73, *read-verse-by-role-of-each-mcode-word*: every M-coded word in a verse is given a role per occurrence, against the verse's main inner-being operation. The roles are characteristic, qualifier / process-element, or standalone. A qualifier gets no account of its own from that verse.
- **No record of the role.** `ib_observation` has no role field. `verse_lexical.role` holds the cluster tags, not a reading role. The role given while reading is lost once the observation is written.
- **No filter at gate 2.** `iba/app/lib/reading.py` (lines 441 to 448) passes gate 2 only when every observation on the scope is carried by a claim, held on an item, or silent. Nothing narrows that on role. A designation-only "king" observation would have to be dealt with like any other.

So the rule says what to do, but the process cannot record the role or act on it.

## 2. The sequence you set

1. **Gate 1 (recording).** Every verse in the item is read and goes through `ib_observation` as it does now. While reading it, each M-coded word in scope is given its role.
2. **Gate 2 (synergy, the deeper reading).** Only the words with an inner-being bearing go on into claims and the narrative. The rest stop at the observation, with their role on record.

## 3. Decisions

### D1. The roles

| Your word | Meaning | Rule 73 | What gate 2 does |
|---|---|---|---|
| **inner-being focus** | the word names or carries the inner-being act of the verse | characteristic | full synergy: claim, telling, narrative |
| **inner-being supportive** | the word qualifies the act: who acts, the setting, the ground, the outcome | qualifier / process-element | carried only as a qualifier of the act it serves, inside that act's observation and claim; no claim of its own |
| **not inner-being related** | the word is a designation or setting and says nothing about the inner being (your "king" example) | (none) | no claim and no telling; it stops at gate 1 |

Rule 73's third role, **standalone**, has no place in your three words. Where it belongs is your call: (a) inner-being focus; (b) its own fourth role; (c) retired in favour of the three.

### D2. Where the role is recorded

| Option | What it is | For | Against |
|---|---|---|---|
| **A. One row per word occurrence** | A new table, `observation_word_role`: observation, verse, Strong's, role. The roles are a `cfg_enum`. Gate 1 refuses an observation that leaves a scope word without a role. | Matches rule 73's per-occurrence role. One observation can hold a focus word and a designation word. The filter and the reports can be mechanical. | New table, new gate 1 check. |
| B. One role per observation | A column on `ib_observation` | Smaller | An observation with words in two roles cannot be recorded truly |
| C. No new record | The reader sets the observation to `silent` with a reason | No build | The role is not in the tables, so nothing checks the filter and no one can review it later |

**Claude recommends A.**

### D3. The filter at gate 2

With A:
- **Not related.** An observation whose scope words are all *not inner-being related* is set `silent` by the tool, with the reason "role: not inner-being related", and is listed in the reading's Account. The verse is not lost. If the same verse holds another act, that act has its own observation and goes on.
- **Supportive.** The word is carried in the claim of the act it qualifies. It is not a claim of its own. Synergy lists it under that act.
- **Focus.** As now.
- The synergy JSON shows the role counts per item, so you can check the filter without reading every row (B:24).

### D4. The rule

A new `cfg_behaviour_rule`, `study_method.deeper-reading-filtered-on-word-role`, delivered at the first use of `Reading.ps1` (`cfg_rule_scope`). Proposed wording:

> At gate 1 every M-coded word in scope is given its role (inner-being focus, inner-being supportive, not inner-being related), after the verse is read and its observation recorded. Gate 2 carries only inner-being focus words into claims and the narrative; a supportive word is carried only as a qualifier of the act it serves; a not-related word stops at the observation. The role is decided per occurrence, never per word or cluster.

Rule 73 then points to it for the roles, so the roles have one home (B:3).

## 4. What it means for #2161

The M72 item set in `outputs/escalation/2161-m72-reading-plan-v2-20261024.md` stands. The role is recorded at gate 1, so the M72 readings wait for this build. If they started first, every role given in them would be lost, and their verses would have to be read again.

## 5. Your decisions

| | Your choice | Comment |
|---|---|---|
| D1 the three roles, and where standalone goes (a, b or c) | | |
| D2 where the role is recorded (A, B or C) | | |
| D3 the filter at gate 2 | | |
| D4 the rule and its wording | | |
