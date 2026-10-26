# #2304 Design (v1): the reading cycle on one JSON: 0.C scope, 0.GAP pre, observe

Date: 2026-10-26. Escalation #2304. Developer Mode session 79681341. **Nothing is built**: this is the design for the
researcher to decide (B:105). Facts were queried today on live `iba/app/db/iba.db`, read-only. What is marked
*(inferential)* is my judgement.

## 0. The instruction (verbatim)

> both files in 2268 B1 and B2 is used as reference, but need to be rewritten. 0.C get scope. scope is either a
> subgroup, or a segment of a subgroup. either case collect the related verse references using surface.subgroup. 0.C
> output is a json with all the verse references in scope. This json feed into 0.GAP pre. 0.GAP pre read the
> verse-lexical and and existing ib_observations for the verses into the JSON. This JSON is the input into D3 + D4.
> Observe identifies any missing observations and write the missing observations into the tables. So the next cycle
> to prototype and confirm is a) the JSON output of 0.C, b) that the gathering of 0.GAP pre is developed and update
> the JSON c) that the observed reading use the prior JSON as input and complete the writing of observations table.

The reference files are `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`
(#2273 B1 phases, #2274 B2 observation record). This design replaces their phases 0.C, 0.GAP pre and D3 + D4 observe.
Their observation record (B2, section 3: the finding in `ib_observation`, applied by `ib_node`, every change in
`ib_observation_change`) stays as the shape the observe step writes.

## 1. The cycle in one picture

```
Reading.ps1 -Step Open    (0.C)       scope request  ->  <label>.json  { scope }                     state open
Reading.ps1 -Step Gather  (0.GAP pre) <label>.json   ->  <label>.json  { scope, gathered }           state gathered
Reading.ps1 -Step Observe (D3 + D4)   <label>.json   ->  <label>.json  { scope, gathered, observe }  (slots to fill)
Reading.ps1 -Step Record              the filled observe section  ->  ib_observation, ib_node         state observed
```

**One JSON file per reading** (`reading.output_dir/<label>/<label>.json`). Each step reads the file the step before
it wrote and adds its own section. No step rebuilds what an earlier step put in the file. *(inferential: this is
what "this JSON feed into" and "update the JSON" ask for; today Open, Gather and Observe each write a separate file,
and Observe rebuilds from the tables.)*

What changes against today:

| | today (#2273 design v6) | this design |
|---|---|---|
| files | `-collation.json`, `-gaps.json`, `-observe.json`, each built on its own | one `<label>.json`, added to step by step |
| scope | any selectors; `-Home` a cluster | one subgroup, or a segment of one (section 2); the subgroup is the home |
| what 0.GAP pre does | lists gap items and writes a record or reason per item into the tables | reads `verse_lexical` and the existing observations into the JSON; writes no table (section 3) |
| observe input | rebuilt from the tables | the gathered JSON (section 4) |
| a node's word | code and surface in the verse | the occurrence itself, `ib_node.verse_lexical_id` (rule 121) |

## 2. a) 0.C: the scope JSON

**Input.** `Reading.ps1 -Step Open -Label <name> -Escalation <id> -Objective "<words>" -Subgroup <code>
[-Segment <...>]`.
- Exactly one subgroup. It is the home (rule 120). A qualifier group is refused (as `Verse-Scope.ps1` refuses it
  now), and so is a `not_this_sense` or anomaly group *(inferential: neither is a characteristic to read)*.
- The home cluster is the subgroup's cluster; `-Home` is no longer given.
- The reading gate of #2294 stays: a cluster with unallocated or stale pairs is refused.

**How the verses are found.** `lib/versescope.resolve`, as built in U5 (#2295): the subgroup's (code, surface) pairs
in `surface_subgroup`, joined to the `verse_lexical` rows that carry them, with current settlements applied. Exact to
the occurrence.

**A segment of a subgroup.** RO13 (`segment-large-subgroup`, #2298 Q3 a) says a large subgroup is cut into logical
units when it comes into focus. No segment is stored anywhere yet. How a segment is given is decision **D1**
(section 6).

**Output: section `scope`.** It is the resolver's version 2 answer, kept whole. Each verse carries its reference and
its occurrences (illustration; the ids are not real):

```json
{"label": "m18-thirst", "reading_id": 12, "escalation": 2304, "objective": "...",
 "scope": {
   "version": 2, "home": ["M18_thirst"], "segment": null,
   "request": {"subgroup": ["M18_thirst"], "home": ["M18_thirst"]},
   "counts": {"verses": 42, "in_scope": 44, "home": 44, "other_subgroups": 54},
   "verses": [
     {"verse_id": 123, "reference": "Psa 42:2", "osis": "Psa.42.2", "routes": ["..."],
      "occurrences": [
        {"id": 556677, "position": 3, "strong": "H6770", "surface": "thirsts", "cluster": "M18",
         "subgroup": "M18_thirst", "kind": "group", "two_sense": false, "in_scope": true, "home": true},
        {"id": 556680, "position": 7, "strong": "H5315G", "surface": "soul", "cluster": "M47",
         "subgroup": "M47_...", "kind": "group", "two_sense": false, "in_scope": false, "home": false}],
      "context": [{"id": 556678, "strong": "H0430G", "surface": "God", "clusters": ["T4"], "in_scope": false}]}]}}
```

A real example from today, made by `Verse-Scope.ps1 -Subgroup M18_thirst`:
`outputs/verse-scope/m18-thirst-0c-sample-20261026.json` (42 verses, 44 occurrences in the home, 54 other subgroups
in those verses). The verses are also kept in `reading_verse`, as today.

## 3. b) 0.GAP pre: the gathering

**Input.** The scope section. **Output.** Section `gathered`, keyed by verse id, added to the same file. Read-only:
0.GAP pre writes no table *(this follows the instruction: it "read[s] ... into the JSON")*.

Per verse:

| field | from | what |
|---|---|---|
| `text` | `verse.text` | the ESV text |
| `passage` | the verses around it, as `observe()` builds the passage today | the context for the reading (RO1) |
| `lexical` | `verse_lexical`, one row per occurrence, by occurrence id | `morph_code`, `role`, `is_negator`, `party_kind`, `narrative_morph`, `gloss_consistent_in_verse`, and the code's gloss (`strong`) |
| `observations` | `ib_node` on the verse, joined to `ib_observation` | every live observation on the verse (status not withdrawn): id, stage, tag, `obs_text`, `meaning`, `basis`; and its nodes, each placed on its occurrence |
| `unplaced_nodes` | the same | nodes that match several occurrences (rule 121: to the cluster's anomaly group) |
| `open_items` | `escalation.match_open_items`, as today | the open thread items that match the verse |
| `meaning_missing` | the lexicon, as today | codes with no meaning senses (and no Mounce for Greek) |

**Placing an existing node on its occurrence.** No node has `verse_lexical_id` yet (16,901 nodes, 0 with it). The
gathering places each node with `versescope.node_occurrences`: on its occurrence where its code and surface occur
once in the verse; on none where they occur twice or more (606 nodes over 139 verses live). Nothing is written back.

**For each home occurrence** the gathering adds `existing`: the observations already placed on it, so Observe can see
what is there. Facts for `M18_thirst` today: 28 live observations have nodes in its 42 verses, but only 4 nodes fall
on the 44 home occurrences; the rest sit on other words in those verses.

Which existing observations count as "already observed" is decision **D3** (section 6). Whether today's pre-gate
records (a row or a reason per gap item, RO12) stay is decision **D4**.

## 4. c) D3 + D4 observe: the missing observations written

**Input.** The file with `scope` and `gathered`. Observe writes section `observe`: the slots to fill. Record reads
the filled section and writes the tables.

**The slots.** One per home occurrence (`home: true`), and one per qualifier bound to it (design v6 section 2: every
T2 word, a tagged word working adverbially (RG-24), a word in `reading.non_characteristic_strongs` (RG-23)). The
other subgroups' occurrences are shown, to be read in the verse, and get no slot of their own (rule 120: they are
another subgroup's home).

Each slot is filled with one of:
- `{"use": <observation id>}`: an existing finding applies here; Record adds a node of this reading to it;
- `{"finding": {...}}`: a new finding, in the B2 shape (kind as tag, `obs_text`, `meaning`, `implication`, `basis`,
  `route`), with the occurrences it covers;
- `{"open_item": {...}}`: in the `Open-Item.ps1 -Action Add` shape;
- `{"reason": "..."}`: why nothing is recorded (for example a silence).

**What "missing" means.** A home occurrence, or a qualifier bound to one, that has no node of this reading. Observe
lists the slots; the reading fills them; the Observe gate (Check) passes when every slot is filled and written.

**What Record writes**, through the B2 writer (`lib/observationrecord`), in one transaction:
- `ib_observation`: a new finding, once (a duplicate text gets nodes on the existing one, as today);
- `ib_node`: one per occurrence the finding covers, with `verse_lexical_id`, `verse_reference`, `strong`, `surface`,
  `cluster_code`, `cluster_subgroup_code`, `role`, `reading_id`;
- `ib_observation_change`: every change with its reason (RW-01).

Writing `verse_lexical_id` on new nodes is the part of U6 (#2296) that this cycle needs. The backfill of old nodes is
not needed for it, and stays with U6.

## 5. Prototype and test, on a copy (B:97)

Scope: `M18_thirst` (42 verses, 44 home occurrences; small, and with existing observations). On a backup-API copy:
1. Open: the scope section against plain SQL on the subgroup's pairs; the refusals (no subgroup, two subgroups, a
   qualifier group, an unmapped cluster).
2. Gather: every verse has text, passage and lexical rows; every live node on the verses is either placed on its
   occurrence or listed as unplaced; nothing written to any table.
3. Observe: one slot per home occurrence and per bound qualifier; nothing else.
4. Record, with a small filled section (one `use`, one `finding`, one `open_item`, one `reason`): the rows and their
   `verse_lexical_id`; a duplicate text turned into nodes; a half-filled file refused whole, with nothing written.
5. Check: the gate passes only when every slot is written.

The JSON file of each step goes to the researcher with the test results, as asked ("let me have a look").

## 6. Decisions for the researcher

| # | point | options | my recommendation *(inferential)* |
|---|---|---|---|
| D1 | How a segment of a subgroup is given | a) a subset of the subgroup's surfaces (`-Surface "thirst,thirsty"`); b) a list of verses within the subgroup (`-Verse`, intersected with it); c) both | c: the subgroups are surface groups, so a logical unit of one is most likely a set of its surfaces (a); b serves a trial of a few verses (RG-19) |
| D2 | One JSON file, added to step by step | a) one file, each step adds its section and refuses if it is already there; b) one file per step, each carrying the earlier sections | a, as instructed |
| D3 | Which existing observations count as already observed | a) any live observation with a node on the occurrence; b) only findings of the reading stage (the eight kinds); c) every one is shown, and none counts until the reading applies it with a node of its own (`use`) | c: it answers #2262 (any observation counted as read) and #2260 (observations outside the rules), and an existing finding is still reused, not rewritten |
| D4 | Today's pre-gate records (a row or a reason per gap item, RO12) | a) dropped: 0.GAP pre only gathers, and open items and missing meanings are met in the observe slots; b) kept as a Gather check before Observe | a: it keeps 0.GAP pre to what the instruction gives it |
| D5 | New nodes carry `verse_lexical_id` | yes, or no | yes: without it the record is not per occurrence (rule 121) |
| D6 | The reference files | rewrite #2273 design v6 section 4 (the 0.C, 0.GAP pre and observe rows) now, or after the prototype is confirmed | after: the prototype may still change them |

**Related open items** (cross-checked, B:65): #2262 (gap analysis counts any observation as read) is met by D3;
#2260 and #2261 (observations outside the rules, in the strand-ledger shape) are what D3 c keeps out of the count;
#2276 (B4, the collation reads every observation) is met by the gathering's `observations`; #2278 (B6, gap types and
their checks) is changed by D4; #2296 (U6) gives the `verse_lexical_id` slice (D5). All are on hold under the parked
#2268.

## 7. What would change in the code (after the decisions; nothing yet)

`iba/app/lib/reading.py`: `open_` (one subgroup, the segment, the file), `gather` (read-only, the section),
`observe` (reads the file), `record` (reads the section, writes `verse_lexical_id`), `check` (the gates). Config: the
step descriptions, RO12 and the pre-gap settings if D4 a. USER-GUIDE.md section 8 and the PS worksheet. No schema
change: `ib_node.verse_lexical_id` exists (#2292).
