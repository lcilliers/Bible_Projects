# #2273 and #2274 Design (v3): Reading.ps1 on the phases (B1), and the observation record on its nodes (B2)

**Date:** 2026-10-24 · **Escalations:** #2273 (B1), #2274 (B2), from #2268 · **Status:** design for the
researcher's decision. Nothing has been built or changed.

Researcher, chat 2026-10-24 (verbatim): *"you may need to relook at B1 plan design. I don't think you understand
how ib_observation and ib_nodes work together. the ib_observation carries the distinct description, the nodes
apply the description to its 'classification'. … you first need to inspect if these missing columns need to be
applied in the nodes. this should also answer your question for a duplicate ib_observation. The same text can be
applied to multiple verses, terms etc."*

Researcher, chat 2026-10-24 (verbatim): *"I do not agree that parties is a new table. the party role in the verse is
an observation. That means that there will be one observation for instance 'evil spirit acting towards the IB'
and many verses and many characteristics affected (terms)"*

The inspection that answers this is `outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md`. It finds
the two tables muddled in the code so far (M1 to M5) and in design v1 (M6). This version rebuilds B2 on the model
and keeps B1's phases. What the builds must deliver is fixed in `outputs/escalation/2268-config-alignment-change-set-v1-20261024.md`
§9 and the plan `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md` §2 to §5.

---

## 1. The model B2 builds to

| Table | Holds | Never holds |
|---|---|---|
| `ib_observation` | one distinct description: its text (`obs_text`), its meaning, its basis (stated or read), stage, tag, status, supersedes, run | anything that can differ between the verses, terms or scopes the description applies to |
| `ib_node` | one application of that description: the verse; the term (strong, surface, morph); the classification it applies under (cluster, subgroup, question); and, new, the parts that belong to this application | the description itself |

**A duplicate** is a second live observation with the same description. The same description applied to another
verse, term or scope is a new node on the existing observation.

## 2. B2: the observation record

### 2.1 On the node (new columns on `ib_node`)

| Column | Holds | Controlled by | Rule |
|---|---|---|---|
| `role` | characteristic, qualifier or standalone, for this word in this verse | `cfg_enum observation_role` | RG-03, RG-04 |
| `route` | A, B or C | `cfg_enum observation_route` | RG-06 |
| `reading_id` | the reading (scope with its objective) that applied the description here: the home | FK to `reading` | RO10, RM-02 |
| `disposition` | where this verse ends up for the description | `cfg_enum observation_disposition` | RW-10, R5 |
| `disposition_note` | the reason, or the claim or item that carries it | text | RW-10 |

`cluster_code` on a node written by a reading is the word's own classification (the M-code in focus, or the
T-code found relevant), checked against `cluster_strong`. It is no longer the reading's cluster: that is
`reading_id` (M1).

### 2.2 The parties

A party's role in a verse is itself a description: who acts, towards whom, and to what effect (RG-06), for
example "evil spirit acting towards the inner being". It is written as one observation, applied by its nodes to
every verse and every term (characteristic) it affects. Many verses and many terms give many nodes on the same
observation, never a second row (§1). An implied party is named as referential in the description (RG-06).

### 2.3 The face

The face (RG-09) is likewise a description: how the word appears here and why it differs from its other
occurrences. It is written as an observation, applied by its nodes to every occurrence that shows that face. A
second occurrence with the same face gets a node on the same observation.

### 2.4 Operation

See decision D3.

### 2.5 Writing an observation from a reading

1. The text is matched against the live observations. An identical live text is never written again. The
   reading names the existing observation id, and the writer adds nodes to it (a duplicate, §1).
2. A new observation is written with stage `reading` and its tag. It carries no strong, cluster, subgroup or
   question of its own (M3). Those are on its nodes.
3. Each node is written with its parts (§2.1). A node with an M-code word and no role is refused.
4. `obs_text`, `meaning` and `basis` stay on the observation. The strand reading's other ledger parts
   (`setting`, `implication`, `chain`, `parties`) are not written by a reading. Whether `setting` belongs on the
   node is decision D4.

### 2.6 Every change kept with its reason (RW-01)

A new table `ib_observation_change` records every change to an observation or one of its nodes: the
observation, the node (when the change is to a node), the column, the old value, the new value, the reason, the
run and who made it. A soft delete is a change of the node's `disposition` to `withdrawn` (one verse no longer
supports it), or of the observation's `status` to `withdrawn` (the description is wrong everywhere), each with
its reason. Nothing is overwritten.

### 2.7 What B2 does not touch

The existing rows (10,595 verse-reading, 773 strand-reading, 885 char-stage) are left as they are. Restating
them on the model is W-3, with #2260 to #2267. M1, M2, M4 and M5 in the inspection are its input.
`recordingpass.record_one_observation` (the retired API pass) is not changed. The collation reading every
observation of a verse is B4 (#2276). The faces of the ledgers are gathered by B8 (#2280).

---

## 3. B1: Reading.ps1 on the phases

The phases are unchanged from v1 except where B2 changes what Observe writes.

D1 and D2 (word level and characteristics) run in their own steps, built by B3 (#2275). They are not steps of a
reading.

| Phase (plan §2) | Step | Reads | Writes | Gate (checked from the tables) | State after |
|---|---|---|---|---|---|
| 0.C Scope | **Open** `-Objective "…"` (new, required) | base data for the scope | the reading with its objective, its verses; the collation | — | `open` |
| 0.GAP pre | **Open** writes the pre-gap JSON; **Gather** writes it into the tables | every table for the scope, once (RO5); all observations already applied to each verse | rows, or a reason, per gap item; new open items | **Check**: every pre-gap item has a row that exists or a reason (RO12) | `gathered` |
| D3 + D4 Observe | **Observe** builds the observe JSON; **Record** writes it | per verse: its passage, every observation applied to it with its nodes (RO2), the current claims on the scope (D3) | observations and nodes (§2.5) | **Check**: every verse has, for each M-code word in focus and each T-code found relevant, a node of this reading or a reason; every node holds its role and route; every verse has a party observation applied to it, or a reason | `observed` (verses marked analysed) |
| D4 Claims with 0.GAP post | **Synergy**, then **Apply** | the scope's observations, through their nodes, and the claims | claims, node dispositions, open items settled | **Check**: the post-claims gap types clear, from the same read (RO7) | `synergised` |
| D4 Narrate | **Apply** (decision D5) | claims and blocks | blocks | inside the gate above | — |
| Publish | **Publish** (as now) | — | the published files | as now | `published` |
| any | **Account** (as now, per state) | the tables | — | — | — |

The changes to the code:

1. **`open_()`** takes `-Objective` into a new column `reading.objective`. The gap JSON holds only the gap
   types of phase `pre`. Each type's detection reads from a registry keyed by the gap type's name, so B6 (#2278)
   adds the checks for the types that are empty today without changing `open_()`. B1 fixes `face_not_gathered`
   to read `reading_strand_hit` (the code still looks for `hit_unread`, no longer an enum value).
2. **`record()`** is split. **Gather** writes the pre-gap JSON. **Record** writes the observe JSON through the
   B2 writer (§2.5), replacing `record_strand_observations` for readings.
3. **New `observe()`** builds the observe JSON once the reading is `gathered`. Per verse: reference, passage,
   words with strong, cluster and role tags, every observation applied to the verse with its nodes (any stage,
   any status but withdrawn), and the claims on the scope. Per word in focus, a slot to fill with an
   existing observation id (a new node on it), a new observation with its node, or a reason.
4. **`check()`** runs the gate for the reading's state: `open`, `gathered`, `observed`.
5. **`synergy()` and `apply()`** require state `observed`. A disposition is written on the reading's nodes
   (§2.1), not on the observation's `status`. **`publish()`** is unchanged.
6. **`scope_observations()`** keeps finding a scope's observations through their nodes, which fits the model.

### 3.1 Config rows (all through `apply_logged`, each registering itself, rule 62)

| Row | Change |
|---|---|
| `cfg_enum reading_state` | add `gathered`, `observed`; retire `recorded` once nothing holds it |
| `cfg_enum ib_observation.tag` | add `face` and `party` (and the tag decided in D2) |
| `cfg_setting reading.gap_types` | each type's `phase` becomes `pre`, `observe` or `post` (plan §4) |
| `cfg_setting reading.observation_parts` | restated: role, route, home and disposition on the node; face and parties as observations (D3 settles operation) |
| `cfg_step` | add `reading.gather`, `reading.observe`; ordinals renumbered; `reading.record` and `reading.check` restated |
| `cfg_method_rule` | RO1, RO2, RO11, RG-01 to RG-25, RW-01 to RW-11 move from `reading.record` to `reading.observe`; RW-02, RW-03 and RO11 restated on the model (§1) |
| `cfg_table`, `cfg_column` | `ib_observation_change`; the new `ib_node` columns; `reading.objective`; `ib_node.cluster_code` restated as the word's classification |
| `cfg_write_grant` | `reading.gather`, `reading.observe`, `reading.record` on their tables |
| `cfg_status_flow ib_observation.reading` | restated: the observation is draft or withdrawn; dispositions are on the nodes |

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
2. A trial reading of three verses (RG-19) through every step. Each gate refuses while its gaps stand, and passes
   once they are filled.
3. The B2 writer: a description already live is refused as a new row and taken as a node; a node with no role
   is refused; a role or route outside its enum is refused; a node's cluster not among the word's clusters is
   refused; a change with no reason is refused; a soft delete keeps the earlier values in `ib_observation_change`.

No test suite exists for `reading.py`, `strandreading.py` or `recordingpass.py`. The test is a script under
`iba/app/migration/` run against the copy, as the #2268 config alignment test was. The results go to
`outputs/escalation/2273-2274-test-results-v1-<date>.md` and are recorded on both items.

---

## 5. Decisions for the researcher

Each is a new decision (B:44). My recommendation is first.

| # | Question | Options | Decision |
|---|---|---|---|
| D1 | Do B1 and B2 build as one change set? | (a) one build and one test, since Record writes the B2 shape; (b) B2 first, then B1 | |
| D2 | Which tag does a reading's observation carry, other than a face or a party? | (a) the reader picks from `ib_observation.tag` per description, with `face` and `party` added; (b) a single new tag `reading-observation` | |
| D3 | Is the operation a controlled value or a description? | (a) a description: an observation applied to the verses and terms it covers, like the face and the parties; (b) a controlled value on the node (a new enum, which needs its list) | |
| D4 | Does `setting` (the circumstance of the verse) stay? | (a) no column: the circumstance belongs in the face (RG-09); (b) a node column | |
| D5 | Is Narrate its own step and gate? | (a) no: it stays inside Apply, as now, checked at the post gate; (b) yes: a `narrate` step after the claims gate | |
| D6 | Are the existing node clusters corrected now? | (a) no: W-3 restates the existing rows (3,179 verse-reading and 213 strand-reading nodes carry the reading's cluster, not the word's); (b) yes, in B2's migration | |

Once approved, B1 and B2 are built and tested on a copy in this session, and the results recorded on #2273 and #2274.
