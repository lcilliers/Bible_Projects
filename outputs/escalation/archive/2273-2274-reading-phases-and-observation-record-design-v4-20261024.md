# #2273 and #2274 Design (v4): Reading.ps1 on the phases (B1), and the observation record (B2)

**Date:** 2026-10-24 · **Escalations:** #2273 (B1), #2274 (B2), from #2268 · **Status:** design for the
researcher's decision. Nothing has been built or changed.

Researcher, chat 2026-10-24 (verbatim): *"we are still too far off target regarding the observations. I think you
need to look at a number of ledgers and then compare that with the catelogue and from that synergise what it is
that you need to tease out of the verse - then you can decide which element of either the observation or node
capture it."*

This version rests on `outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md` (the comparison and
synthesis: seven kinds of finding, §5; their placement, §6). It also uses
`outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md` (how the tables have been used, muddles M1 to
M5). What the builds must deliver is fixed in `outputs/escalation/2268-config-alignment-change-set-v1-20261024.md`
§9 and the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md` §2 to §5.

---

## 1. What a reading records

A reading of a verse records **findings**. Each is one of seven kinds (synthesis §5):

| Kind | What it is | Example |
|---|---|---|
| face | the sense a word carries here, by what differs from its other occurrences | fear: "the word describes the one or thing feared" |
| party | who bears, causes or receives the act, who else acts, where it comes from, toward or from God | "evil spirit acting towards the inner being" |
| statement | what the verse shows the inner being doing or undergoing, including what sets it off, what follows and where it sits | "Fear leads to hiding" |
| link | a link the verse states between words or characteristics | "heard → anger → act" |
| use | how the words are used: the speaker's purpose, one phrase to different ends, one word in two senses | "slow to anger" as name, plea, threat, complaint |
| term | the term's meaning in context, surface variants, related words | the other senses of *ʾaph* |
| silence | a word with no inner-being bearing here, with the reason | "boiling pot" (life-death face I) |

**Each finding is one `ib_observation`, written once.** Its nodes apply it to every verse and word it covers, in
this reading and in any later one. A finding about other findings (a factor across faces, a pairing) applies to
them through `ib_node.traced_observation_id`.

## 2. B2: the observation record

### 2.1 `ib_observation`: the finding

| Column | Holds | Status |
|---|---|---|
| `obs_text` | the finding, in the verses' words where it quotes | exists |
| `meaning`, `implication` | what it means, and what it implies | exist |
| `basis` | stated or read | exists |
| `tag` | its kind: face, party, statement, link, use, term or silence (D2) | exists; enum values added |
| `route` | A, B or C, on a party finding (D3) | new |
| `stage` | `reading` | exists; the value exists |
| `status` | draft or withdrawn (dispositions are on the nodes) | exists |

A reading writes no `strong`, `cluster_code`, `cluster_subgroup_id`, `question_code` or `window` on the
observation (muddle M3). These are on its nodes. It writes no `setting`, `chain` or `parties` (the strand reading's
columns, M2). A setting is a party (the speaker) or part of the meaning (D4); a chain is a link finding; parties
are party findings.

**A duplicate** is a second live observation with the same text. The writer refuses it and adds nodes to the
existing one instead.

### 2.2 `ib_node`: the finding applied

| Column | Holds | Status |
|---|---|---|
| `verse_reference` | the verse | exists |
| `strong`, `surface`, `morph_code` | the word occurrence (a term finding about the word in general has a strong and no verse) | exist |
| `cluster_code` | **the word's own classification**: its M-code, or the T-code found relevant, checked against `cluster_strong` (M1) | exists; meaning restated |
| `cluster_subgroup_code` | the word's subgroup, where it has one | exists |
| `traced_observation_id` | the finding this one is about, for a finding about findings | exists |
| `question_code` | the catalogue prompt that led to it, when one did (optional; RG-17) | exists |
| `role` | the word's role in this finding: characteristic, qualifier or standalone (`cfg_enum observation_role`) (D7) | new |
| `reading_id` | the reading that applied it: the home (RO10) | new |
| `disposition`, `disposition_note` | where this verse ends up for this finding, with the reason or the claim or item (`cfg_enum observation_disposition`) | new |

The seat (heart, spirit, soul, mind, a body part) needs no column: the finding is applied by a node to the seat
word, classified by its own cluster.

### 2.3 Every change kept with its reason (RW-01)

A new table `ib_observation_change` records every change to an observation or a node: the observation, the node,
the column, the old value, the new value, the reason, the run and who made it. A node's soft delete is a change of
its `disposition` to `withdrawn` (this verse no longer supports it). An observation's soft delete is a change of its
`status` to `withdrawn` (the finding is wrong everywhere). Nothing is overwritten.

### 2.4 What B2 does not touch

The existing rows of every stage are left as they are. Restating them on this model is W-3, with #2260 to #2267;
the usage file's M1 to M5 are its input. `recordingpass.record_one_observation` (the retired API pass) is not
changed. B4 (#2276) makes the collation read every observation of a verse. B8 (#2280) gathers the ledgers' faces
as face findings.

---

## 3. B1: Reading.ps1 on the phases

D1 and D2 (word level and characteristics) run in their own steps, built by B3 (#2275).

| Phase (plan §2) | Step | Reads | Writes | Gate (checked from the tables) | State after |
|---|---|---|---|---|---|
| 0.C Scope | **Open** `-Objective "…"` (new, required) | base data for the scope | the reading with its objective and verses; the collation | — | `open` |
| 0.GAP pre | **Open** writes the pre-gap JSON; **Gather** writes it into the tables | every table for the scope, once (RO5); every finding already applied to each verse | rows, or a reason, per gap item; new open items | **Check**: every pre-gap item has a row that exists or a reason (RO12) | `gathered` |
| D3 + D4 Observe | **Observe** builds the observe JSON; **Record** writes it | per verse: its passage; every finding applied to it, with its nodes (RO2); the current claims on the scope (D3) | findings and nodes (§2) | **Check** (D8) | `observed` (verses marked analysed) |
| D4 Claims with 0.GAP post | **Synergy**, then **Apply** | the scope's findings, through their nodes; the claims | claims; node dispositions; open items settled | **Check**: the post-claims gap types clear, from the same read (RO7) | `synergised` |
| D4 Narrate | **Apply** (D5) | claims and blocks | blocks | inside the gate above | — |
| Publish | **Publish** (as now) | — | the published files | as now | `published` |
| any | **Account** (as now) | the tables | — | — | — |

The changes to the code:

1. **`open_()`** takes `-Objective` into a new column `reading.objective`. The gap JSON holds the gap types of
   phase `pre`. Each type's detection reads from a registry keyed by the type's name, so B6 (#2278) adds the
   missing checks without changing `open_()`. B1 fixes `face_not_gathered` to read `reading_strand_hit` (the code
   still looks for `hit_unread`, which is no longer an enum value).
2. **`record()`** is split. **Gather** writes the pre-gap JSON. **Record** writes the observe JSON through the B2
   writer, which replaces `record_strand_observations` for readings.
3. **New `observe()`** builds the observe JSON once the reading is `gathered`. Per verse: reference, passage,
   words with strong, cluster and role tags; every finding already applied to the verse, with its kind and nodes;
   the claims on the scope. Per word in focus, a slot to fill with an existing finding (a new node on it), a new
   finding with its nodes, or a reason. The catalogue rows that ask of one verse (53, synthesis §3) are given as
   prompts under the kind they serve, not as questions to answer.
4. **`check()`** runs the gate for the reading's state: `open`, `gathered`, `observed`.
5. **`synergy()` and `apply()`** require state `observed`. A disposition is written on the reading's nodes, not on
   the observation's `status`. **`publish()`** is unchanged.

### 3.1 Config rows (all through `apply_logged`, each registering itself, rule 62)

| Row | Change |
|---|---|
| `cfg_enum reading_state` | add `gathered`, `observed`; retire `recorded` once nothing holds it |
| `cfg_enum ib_observation.tag` | add face, party, statement, link, use, term, silence (D2) |
| `cfg_setting reading.observation_parts` | restated as the seven kinds and the node's parts (§1, §2) |
| `cfg_setting reading.gap_types` | each type's `phase` becomes `pre`, `observe` or `post` (plan §4) |
| `cfg_step` | add `reading.gather`, `reading.observe`; ordinals renumbered; `reading.record` and `reading.check` restated |
| `cfg_method_rule` | RO1, RO2, RO11, RG-01 to RG-25, RW-01 to RW-11 move from `reading.record` to `reading.observe`; RW-02, RW-03 and RO11 restated on the model (one finding, many nodes) |
| `cfg_table`, `cfg_column` | `ib_observation_change`; `ib_observation.route`; the new `ib_node` columns; `reading.objective`; `ib_node.cluster_code` restated as the word's own classification |
| `cfg_write_grant` | `reading.gather`, `reading.observe`, `reading.record` on their tables |
| `cfg_status_flow ib_observation.reading` | restated: draft or withdrawn; dispositions on the nodes |

### 3.2 The four published readings

They stay `published`. Their objective is null and shown as "before #2273" in Account. No observation or node of
theirs is changed (W-3).

### 3.3 Documents

BUILD.md entry; USER-GUIDE.md section on Reading.ps1; the `Reading.ps1` help text; the Excel tool sheet for
Reading.ps1 (closing the drift finding on #2270).

---

## 4. Test, on a copy (B:97)

On a copy made with `iba/app/lib/dbsnapshot.copy_db`:

1. Migration: tables, columns and config rows in place; config validates clean; the four readings still
   `published`, and their Account renders.
2. A trial reading of three verses (RG-19) through every step. Each gate refuses while its gaps stand and passes
   once they are filled.
3. The B2 writer: a finding whose text is already live is refused as a new row and taken as new nodes; one party
   finding applied to two verses and three words gives one observation and five nodes; a node's cluster not among
   its word's clusters is refused; a role, disposition or route outside its enum is refused; a change with no reason
   is refused; a soft delete keeps the earlier values in `ib_observation_change`.

No test suite exists for `reading.py`, `strandreading.py` or `recordingpass.py`. The test is a script under
`iba/app/migration/` run against the copy, as the #2268 config alignment test was. The results go to
`outputs/escalation/2273-2274-test-results-v1-<date>.md` and are recorded on both items.

---

## 5. Decisions for the researcher

Each is a new decision (B:44). My recommendation is first.

| # | Question | Options | Decision |
|---|---|---|---|
| D1 | Do B1 and B2 build as one change set? | (a) one build and one test, since Record writes the B2 shape; (b) B2 first, then B1 | |
| D2 | Is the finding's kind its tag? | (a) yes: the seven kinds are the tag values for stage `reading`; (b) a new column for the kind, with the tag kept for the older stages' meanings | |
| D3 | Where does the route go? | (a) on the party finding (`ib_observation.route`): the route follows from the party described; (b) on the node | |
| D4 | Is there a setting column? | (a) no: the speaker is a party finding, and the rest of the setting is part of the finding's meaning; (b) a node column | |
| D5 | Is Narrate its own step and gate? | (a) no: it stays inside Apply, checked at the post gate; (b) yes: a `narrate` step after the claims gate | |
| D6 | Are the existing node clusters corrected now? | (a) no: W-3 restates the existing rows (3,179 verse-reading and 213 strand-reading nodes carry the reading's cluster, not the word's); (b) yes, in B2's migration | |
| D7 | Is a word's role per finding or per occurrence? | (a) per finding (`ib_node.role`): the same word can be the characteristic in one finding and a qualifier in another; (b) once per occurrence in the reading, the same for every finding | |
| D8 | What must the Observe gate find for each verse? | (a) every M-code word in focus, and every T-code word found relevant, has a face finding applied to it (the ledgers' "every hit has a face") and a role; the verse has at least one statement or silence finding; any other kind only where the verse shows it; otherwise a reason; (b) a node of this reading on every word in focus, of any kind | |

Once approved, B1 and B2 are built and tested on a copy in this session, and the results recorded on #2273 and
#2274.
