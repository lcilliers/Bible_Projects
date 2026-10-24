# #2273 and #2274 Design (v5): Reading.ps1 on the phases (B1), and the observation record (B2)

**Date:** 2026-10-24 · **Escalations:** #2273 (B1), #2274 (B2), from #2268 · **Status:** design for the
researcher's approval. Nothing has been built or changed.

Researcher, chat 2026-10-24 (verbatim), on design v4: *"D1 - yes, the reading is directed toward the outcome, they
are not independent. D2 - agree a) ; D3 - route may be from one characteristic to another, without a party involved
therefore it could be a) or b)  D4 the setting is part of the route/party - it is a finding, not a classification
(node) ; D5 narrate is a separate step (b)  D6 - there is no need to reclassify, unless on a re-read is found to be
an error and need fixing. I don't think it matters, because if there are another term on the verse, it will be
picked up when the other term is read; D7 - a) ; D8 (b) this is likely the trigger for the most open items to be
created when a verse reading is taking place.   One thing I am missing the the reading of the qualifyers - it somehow
feel for me that qualifyers are ignored, but they can have a large impact on the characteristic (it shows grade,
nature, impact, size, relations)"*

This version carries those rulings (§6 lists where each lands) and adds the reading of qualifiers (§2). It rests on
`outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md` (the ledgers and the catalogue compared)
and `outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md` (how the tables have been used). What
the builds must deliver is fixed in `outputs/escalation/2268-config-alignment-change-set-v1-20261024.md` §9 and the
plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md` §2 to §5. B1 and B2 are built as one
change set (D1).

---

## 1. What a reading records

A reading of a verse records **findings**, of eight kinds. The kind is the observation's tag (D2).

| Kind | What it is | Example |
|---|---|---|
| face | the sense a word carries here, by what differs from its other occurrences | fear: "the word describes the one or thing feared" |
| qualification | what a qualifier gives the characteristic it binds to (§2) | "exceedingly" raises the mariners' fear (Jon 1:10) |
| party | who bears, causes or receives the act, who else acts, where it comes from, toward or from God; with its setting and route | "evil spirit acting towards the inner being" |
| statement | what the verse shows the inner being doing or undergoing, including what sets it off, what follows and where it sits | "Fear leads to hiding" |
| link | a link the verse states between words or characteristics; with its setting and route | "heard → anger → act" |
| use | how the words are used: the speaker's purpose, one phrase to different ends, one word in two senses | "slow to anger" as name, plea, threat, complaint |
| term | the term's meaning in context, surface variants, related words | the other senses of *ʾaph* |
| silence | a word with no inner-being bearing here, with the reason | "boiling pot" (life-death face I) |

**Each finding is one `ib_observation`, written once.** Its nodes apply it to every verse and word it covers, in
this reading and later ones. A finding about other findings (a factor across faces, a pairing) applies to them
through `ib_node.traced_observation_id`.

## 2. The reading of qualifiers

**Why they were being lost.** `cfg_method_rule` RG-04 says *"A qualifier gets no own account from the verse"*, and
the observation record had nowhere to put what the qualifier gives. So a qualifier was at most a note inside a
characteristic's statement.

**What changes.**
- A qualifier is read for what it gives the characteristic: its **grade, nature, impact, size or relation**
  (researcher, 2026-10-24). RG-04's list (a measure, strengthening, ground, cause, object, setting, bait) is merged
  into these (D9).
- Each is a **qualification finding**. What it gives is held on the finding (`ib_observation.qualifies`, a new
  `cfg_enum observation_qualifies`). The finding's nodes apply it to the qualifier word (role qualifier) and to the
  characteristic word it binds to (role characteristic), in every verse where the same qualification holds.
- RG-04 is restated: a qualifier gets no separate account of itself, but what it gives the characteristic is a
  finding of its own. RG-22 and RG-24 stay as they are: a T2 word is always read as the qualifier of what it binds
  to, and a tagged word working adverbially is a qualifier there.
- **The words in focus include the qualifiers.** The observe JSON lists, per M-code word, the content words of the
  verse that bind to it: every T2 word, any tagged word working adverbially (RG-24), and the words in
  `reading.non_characteristic_strongs` (RG-23). Each is a slot of its own, so a qualifier cannot pass unread (D8).

## 3. B2: the observation record

### 3.1 `ib_observation`: the finding

| Column | Holds | Status |
|---|---|---|
| `obs_text` | the finding, in the verses' words where it quotes, with its setting where the finding has one (D4) | exists |
| `meaning`, `implication` | what it means, and what it implies | exist |
| `basis` | stated or read | exists |
| `tag` | its kind (§1) | exists; enum values added |
| `route` | A, B or C, on a party or link finding (D3) | new |
| `qualifies` | grade, nature, impact, size or relation, on a qualification finding (§2) | new |
| `stage` | `reading` | exists |
| `status` | draft or withdrawn (dispositions are on the nodes) | exists |

A reading writes no `strong`, `cluster_code`, `cluster_subgroup_id`, `question_code` or `window` on the
observation (these are on the nodes), and no `setting`, `chain` or `parties` column (the setting is part of the
party or link finding, D4; a chain is a link finding; parties are party findings).

**A duplicate** is a second live observation with the same text. The writer refuses it and adds nodes to the
existing one instead.

### 3.2 `ib_node`: the finding applied

| Column | Holds | Status |
|---|---|---|
| `verse_reference` | the verse | exists |
| `strong`, `surface`, `morph_code` | the word occurrence (a term finding about the word in general has a strong and no verse) | exist |
| `cluster_code` | the word's own classification: its M-code, or the T-code found relevant | exists |
| `cluster_subgroup_code` | the word's subgroup, where it has one | exists |
| `traced_observation_id` | the finding this one is about, for a finding about findings | exists |
| `question_code` | the catalogue prompt that led to it, when one did (optional) | exists |
| `role` | the word's role in this finding: characteristic, qualifier or standalone (D7) | new |
| `reading_id` | the reading that applied it: the home (RO10) | new |
| `disposition`, `disposition_note` | where this verse ends up for this finding, with the reason or the claim or item | new |

Existing nodes are not reclassified (D6). A node found wrong on a re-read is corrected then, with its reason
(§3.3).

### 3.3 Every change kept with its reason (RW-01)

A new table `ib_observation_change` records every change to an observation or a node: the observation, the node,
the column, the old value, the new value, the reason, the run and who made it. A node's soft delete is a change of
its `disposition` to `withdrawn`. An observation's soft delete is a change of its `status` to `withdrawn`. Nothing
is overwritten.

### 3.4 What B2 does not touch

Existing rows of every stage stay as they are (D6). Restating them is W-3, with #2260 to #2267.
`recordingpass.record_one_observation` (the retired API pass) is not changed. B4 (#2276) makes the collation read
every observation of a verse. B8 (#2280) gathers the ledgers' faces as face findings.

---

## 4. B1: Reading.ps1 on the phases

D1 and D2 (word level and characteristics) run in their own steps, built by B3 (#2275).

| Phase (plan §2) | Step | Reads | Writes | Gate (checked from the tables) | State after |
|---|---|---|---|---|---|
| 0.C Scope | **Open** `-Objective "…"` (new, required) | base data for the scope | the reading with its objective and verses; the collation | — | `open` |
| 0.GAP pre | **Open** writes the pre-gap JSON; **Gather** writes it into the tables | every table for the scope, once (RO5); every finding already applied to each verse | rows, or a reason, per gap item; new open items | **Check**: every pre-gap item has a row that exists or a reason (RO12) | `gathered` |
| D3 + D4 Observe | **Observe** builds the observe JSON; **Record** writes it | per verse: its passage; every finding applied to it, with its nodes (RO2); the current claims on the scope (D3) | findings and nodes (§3); open items | **Check**: every word in focus, qualifiers included, has a node of this reading, of any kind, or an open item or a reason (D8) | `observed` (verses marked analysed) |
| D4 Claims with 0.GAP post | **Synergy**, then **Apply** | the scope's findings, through their nodes; the claims | claims; node dispositions; open items settled | **Check**: every node of this reading carried by a claim or disposed; every claim rests on a finding (RO7) | `synergised` |
| D4 Narrate | **Narrate** (new, D5) | the claims and the blocks | tellings; blocks rewritten | **Check**: every current claim told or held; every verse cited in a block has a finding behind it | `narrated` |
| Publish | **Publish** | — | the published files | as now | `published` |
| any | **Account** | the tables | — | — | — |

The changes to the code:

1. **`open_()`** takes `-Objective` into a new column `reading.objective`. The gap JSON holds the gap types of
   phase `pre`. Each type's detection reads from a registry keyed by the type's name, so B6 (#2278) adds the
   missing checks without changing `open_()`. B1 fixes `face_not_gathered` to read `reading_strand_hit` (the code
   still looks for `hit_unread`, which is no longer an enum value).
2. **`record()`** is split. **Gather** writes the pre-gap JSON. **Record** writes the observe JSON through the B2
   writer, which replaces `record_strand_observations` for readings.
3. **New `observe()`** builds the observe JSON once the reading is `gathered`. Per verse: reference, passage, words
   with strong, cluster and role tags; every finding already applied to the verse, with its kind and nodes; the
   claims on the scope. Per word in focus, qualifiers included (§2): a slot to fill with an existing finding (a new
   node on it), a new finding with its nodes, an open item, or a reason. The catalogue rows that ask of one verse
   are given as prompts under the kind they serve.
4. **`apply()`** writes claims, node dispositions and open items. Tellings and the block rewrite move to
   **`narrate()`** (new).
5. **`check()`** runs the gate for the reading's state: `open`, `gathered`, `observed`, `synergised`.
6. **`publish()`** requires state `narrated`.

### 4.1 Config rows (all through `apply_logged`, each registering itself, rule 62)

| Row | Change |
|---|---|
| `cfg_enum reading_state` | add `gathered`, `observed`, `narrated`; retire `recorded` once nothing holds it |
| `cfg_enum ib_observation.tag` | add face, qualification, party, statement, link, use, term, silence |
| `cfg_enum observation_qualifies` | new: grade, nature, impact, size, relation (D9) |
| `cfg_setting reading.observation_parts` | restated as the eight kinds and the node's parts (§1, §3) |
| `cfg_setting reading.gap_types` | each type's `phase` becomes `pre`, `observe`, `post` or `narrate`: claim_not_told and citation_without_record move to `narrate` |
| `cfg_step` | add `reading.gather`, `reading.observe`, `reading.narrate`; ordinals renumbered; `reading.record`, `reading.apply` and `reading.check` restated |
| `cfg_method_rule` | RO1, RO2, RO11, RG-01 to RG-25, RW-01 to RW-11 move from `reading.record` to `reading.observe`; RN-01 to RN-15 and RO9 move from `reading.apply` to `reading.narrate`; RG-04 restated (§2); RW-02, RW-03 and RO11 restated (one finding, many nodes) |
| `cfg_table`, `cfg_column` | `ib_observation_change`; `ib_observation.route`, `.qualifies`; the new `ib_node` columns; `reading.objective`, `reading.narrated_at` |
| `cfg_write_grant` | `reading.gather`, `reading.observe`, `reading.record`, `reading.narrate` on their tables |
| `cfg_status_flow ib_observation.reading` | restated: draft or withdrawn; dispositions on the nodes |

### 4.2 The four published readings

They stay `published`. Their objective is null and shown as "before #2273" in Account. No observation or node of
theirs is changed.

### 4.3 Documents

BUILD.md entry; USER-GUIDE.md section on Reading.ps1; the `Reading.ps1` help text; the Excel tool sheet for
Reading.ps1 (closing the drift finding on #2270).

---

## 5. Test, on a copy (B:97)

On a copy made with `iba/app/lib/dbsnapshot.copy_db`:

1. Migration: tables, columns and config rows in place; config validates clean; the four readings still
   `published`, and their Account renders.
2. A trial reading of three verses (RG-19), one with a qualifier (for example Jon 1:10, "exceedingly afraid"),
   through every step. Each gate refuses while its gaps stand and passes once they are filled. A qualifier left
   without a node, an open item or a reason stops the Observe gate.
3. The B2 writer: a finding whose text is already live is refused as a new row and taken as new nodes; one party
   finding applied to two verses and three words gives one observation and five nodes; a qualification finding
   without `qualifies` is refused; a role, disposition, route or `qualifies` value outside its enum is refused; a
   change with no reason is refused; a soft delete keeps the earlier values in `ib_observation_change`.

No test suite exists for `reading.py`, `strandreading.py` or `recordingpass.py`. The test is a script under
`iba/app/migration/` run against the copy. The results go to `outputs/escalation/2273-2274-test-results-v1-<date>.md`
and are recorded on both items.

---

## 6. The rulings, and what is left to confirm

| # | Ruling (2026-10-24) | Where it lands |
|---|---|---|
| D1 | one change set | B1 and B2 build and test together (§5) |
| D2 | the kind is the tag | §1, §3.1 |
| D3 | "route may be from one characteristic to another, without a party involved" | `route` on the party finding and on the link finding (§3.1): both are findings (D4) |
| D4 | the setting is part of the route or party, a finding | no setting column; the setting is written in the party or link finding (§3.1) |
| D5 | Narrate is its own step | `reading.narrate`, state `narrated` (§4) |
| D6 | no reclassification unless a re-read finds an error | existing nodes untouched (§3.2, §3.4) |
| D7 | role per finding | `ib_node.role` (§3.2) |
| D8 | a node on every word in focus, of any kind; the main source of open items | the Observe gate (§4); qualifiers are words in focus (§2) |

**To confirm:**

| # | Question | Options | Decision |
|---|---|---|---|
| D3 | I read "could be a) or b)" as: the route is held on the finding, on both party and link findings. Is that right? | (a) yes, on the finding; (b) on the node, so one finding can take a different route in different verses | |
| D9 | What can a qualifier give? | (a) your five: grade, nature, impact, size, relation, with RG-04's list read into them (measure and strengthening as grade; ground, cause and bait as relation; object and setting as relation or nature); (b) your five plus RG-04's seven, twelve values | |

Once confirmed, B1 and B2 are built and tested on a copy in this session, and the results recorded on #2273 and
#2274.
