# #2304 Design (v3): the reading cycle on one JSON: 0.C scope, 0.GAP pre, observe

Date: 2026-10-26. Escalation #2304. Developer Mode session 79681341. **v3 adds the cluster documents to D3** (the
readings already written in the cluster files are adopted first); v2 carried the answers on D1 to D5. Earlier versions
are in `outputs/escalation/archive/`. **Nothing is built** (B:105). Facts were queried today on live `iba/app/db/iba.db`, read-only. What is marked
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

**One JSON file per scope run, saved to the cluster** (D2): in the home cluster's subfolder of `_analytics/Clusters`
(`cfg_setting report.cluster_folder_naming_convention`, e.g. `_analytics/Clusters/M18 - desire-longing/`), named
`<label>-v{n}-<YYYYMMDD>.json`, prior versions in its `archive/`. Each step reads the file the step before it wrote
and adds its own section. No step rebuilds what an earlier step put in the file. The cluster reading index reads
`_analytics/Clusters` (`reading_index.roots`), so it must leave these files out (#2279, B7).

What changes against today:

| | today (#2273 design v6) | this design |
|---|---|---|
| files | `-collation.json`, `-gaps.json`, `-observe.json` under `outputs/reading`, each built on its own | one JSON per scope run in the cluster's folder, added to step by step |
| scope | any selectors; `-Home` a cluster | one subgroup, or a segment of one (section 2); the subgroup is the home |
| what 0.GAP pre does | lists gap items and writes a record or reason per item into the tables | reads `verse_lexical`, the existing observations and the open items into the JSON; writes no table (section 3) |
| open items | a pre-gap section, answered at Gather | read at 0.GAP pre; each answered at Record, never silently passed (section 4) |
| cluster documents | the lines naming the verse, shown in the collation | read at 0.GAP pre; what they already say is adopted before anything new is written (sections 3, 4) |
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
units when it comes into focus. No segment is stored anywhere yet. **D1 (ruled): a segment is a subset of the
subgroup.** It is given by the subgroup's surfaces it keeps (`-Surface`) or the verses of the subgroup it keeps
(`-Verse`, intersected with the subgroup), and is recorded in the JSON (`scope.segment`). Which of the two the
segments use in practice is left to the prototype (the researcher: "likely to be a subset of a sub group").

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
| `documents` | the cluster reading index (`reading_ref`, `reading_file`, `reading_section`), as `versecollate` reads it today | every line of a cluster file that names the verse: file, section heading, line number, line kind, the line's text; and the observations already imported from that file (`ib_observation.revisit_note` naming it) |
| `open_items` | the open items register (`escalation_thread_item`, through `escalation.match_open_items`, as today) | the open items that match the verse: item, thread, its target, `read_for`, `why`, `comes_back_when` |
| `meaning_missing` | the lexicon, as today | codes with no meaning senses (and no Mounce for Greek) |

**Placing an existing node on its occurrence.** No node has `verse_lexical_id` yet (16,901 nodes, 0 with it). The
gathering places each node with `versescope.node_occurrences`: on its occurrence where its code and surface occur
once in the verse; on none where they occur twice or more (606 nodes over 139 verses live). Nothing is written back.

**For each home occurrence** the gathering adds `existing`: the observations already placed on it, so Observe can see
what is there. Facts for `M18_thirst` today: 28 live observations have nodes in its 42 verses, and none of them falls
on the 44 home occurrences; they sit on other words in those verses.

**The cluster documents** (D3, the researcher: observations "already formulated in the existing documents, must be
adopted and have precedence"). The gathering reads, per verse, every line of the cluster files that names it, through
the reading index, which reads only those lines and never a whole file. Facts for `M18_thirst` today: all 42 of its
verses are named in the files, in 175 lines of 32 files (63 bullets, 54 table rows, 43 headings, 15 paragraphs),
mostly the M18 group E worksheets and readings of 2026-10-09. Four of those 32 files already had observations
imported into `ib_observation` (189 in all; the October catch-up, #2266). A line already imported is shown with the
observation it became, so it is used, not imported twice. The index has to be current before the gathering reads it
(`Reading-Index.ps1`), so a file changed since it was indexed is listed, as the collation lists it today.

**The open items the scope run clears** (D3, ruled). Besides the per-verse matches, the gathering lists once, in
`gathered.open_items`, every open item of the register related to the scope: an item whose target verses lie in the
scope (whole: this run can close it) or reach past it (in part: it can be read in part, #2250), and an item naming
the home subgroup's cluster or one of its codes. Each carries its target, what to read for and why it is open.

**D3 (ruled, c):** every existing observation is shown; none counts as observed until the reading applies it with a
node of its own. **D4 (ruled, a):** today's pre-gate records (a row or a reason per gap item, RO12) are dropped;
creating and updating observations, and answering the open items, are done in one place, Record (section 4).

## 4. c) D3 + D4 observe: the missing observations written

**Input.** The file with `scope` and `gathered`. Observe writes section `observe`: the slots to fill. Record reads
the filled section and writes the tables.

**The slots.** One per home occurrence (`home: true`), and one per qualifier bound to it (design v6 section 2: every
T2 word, a tagged word working adverbially (RG-24), a word in `reading.non_characteristic_strongs` (RG-23)). The
other subgroups' occurrences are shown, to be read in the verse, and get no slot of their own (rule 120: they are
another subgroup's home).

**One slot per open item** in `gathered.open_items`. **No open item related to the scope is passed over in silence**
(the researcher, D4 and D5): each is answered with a response in the register's own vocabulary (`closed`,
`touched` with "read in part" where the item reaches past the scope, `forward`, `withdrawn`, `superseded`), with what
the reading found.

Each slot is filled with one of:
- `{"adopt": {"file": ..., "line": n, "finding": {...}}}`: a reading already written in a cluster document, taken into
  the table as a finding in the B2 shape, citing its file and line (section 4, adoption);
- `{"use": <observation id>}`: an existing finding applies here; Record adds a node of this reading to it;
- `{"finding": {...}}`: a new finding, in the B2 shape (kind as tag, `obs_text`, `meaning`, `implication`, `basis`,
  `route`), with the occurrences it covers;
- `{"open_item": {...}}`: in the `Open-Item.ps1 -Action Add` shape;
- `{"reason": "..."}`: why nothing is recorded (for example a silence).

**Adoption first: the documents have precedence.** Where a slot's verse has document lines, the reading takes
what they already say before writing anything new:
- a document line that states a reading of the word or verse is adopted (`adopt`), or, where it was imported
  already, its observation is used (`use`);
- a new `finding` is written only for what the documents do not say;
- a document line that is passed over gets a `reason` (for example a heading or a reference list that names the verse
  and says nothing about it, or a reading the verse does not bear out, with why).

So no document line naming a verse in the scope passes unanswered either, and an observation already done is
recorded, not redone. How an adopted reading is put into the B2 shape is decision **D7** (section 6).

**What "missing" means.** A home occurrence, or a qualifier bound to one, that has no node of this reading; and an
open item related to the scope with no response from this reading. Observe lists the slots; the reading fills them;
the Observe gate (Check) passes only when every slot, open items included, is filled and written.

**What Record writes**, through the B2 writer (`lib/observationrecord`), in one transaction:
- `ib_observation`: a new or adopted finding, once (a duplicate text gets nodes on the existing one, as today); an
  adopted finding carries its source, `<file>:<line>`, in `meaning_source`;
- `ib_node`: one per occurrence the finding covers, with `verse_lexical_id`, `verse_reference`, `strong`, `surface`,
  `cluster_code`, `cluster_subgroup_code`, `role`, `reading_id`;
- `ib_observation_change`: every change with its reason (RW-01);
- the open items: each slot's response through the register (`escalation_thread_item_response`, as Gather writes it
  today), and the item's state where the response settles it; a new open item through `openitem.add`.

Writing `verse_lexical_id` on new nodes is the part of U6 (#2296) that this cycle needs. The backfill of old nodes is
not needed for it, and stays with U6.

## 5. Prototype and test, on a copy (B:97)

Scope: `M18_thirst` (42 verses, 44 home occurrences; small, and with existing observations). On a backup-API copy:
1. Open: the scope section against plain SQL on the subgroup's pairs; the refusals (no subgroup, two subgroups, a
   qualifier group, an unmapped cluster).
2. Gather: every verse has text, passage and lexical rows; every live node on the verses is either placed on its
   occurrence or listed as unplaced; nothing written to any table.
3. Gather: every open item related to the scope listed once, against a plain query of the register; every
   document line naming a verse of the scope listed with its text, against a plain query of the reading index, and
   the lines already imported shown with their observation.
4. Observe: one slot per home occurrence, per bound qualifier and per related open item; nothing else.
5. Record, with a small filled section (one `adopt`, one `use`, one `finding`, one new open item, one `reason`, and a
   response on each related open item): the rows and their `verse_lexical_id`; the responses in the register; a duplicate text
   turned into nodes; a half-filled file, or one with an open item left unanswered, refused whole, with nothing
   written.
6. Check: the gate passes only when every slot is written.

The JSON file of each step goes to the researcher with the test results, as asked ("let me have a look").

## 6. Decisions: the researcher's answers (chat 2026-10-26, verbatim)

> D1 likely to be a subset of a sub group. D2 - one Json file per scope run in Json format saved to the cluster. D3 :
> c: all are shown. I forgot that that D3 also need to read the open items register the open items that will be
> cleared by the scope run. D4 and D5 must include the updating of open items related to the scope. Open items
> related to the scope must not be silently ignored. D4 - this can be dropped as recommended to consolidate the
> observations creation/update in D5.

| # | point | ruled |
|---|---|---|
| D1 | How a segment is given | a subset of the subgroup (section 2); by surfaces or by verses, to be seen in the prototype |
| D2 | The file | one JSON file per scope run, saved to the cluster's folder (section 1) |
| D3 | Existing observations | c: all shown, none counts until applied; the gathering also reads the open items the run will clear (section 3) |
| D4 | Today's pre-gate records | dropped; observations and open items are created and updated in Record (section 4) |
| D5 | New nodes carry `verse_lexical_id`; open items updated | yes, with every related open item answered (section 4) |
| D6 | Rewriting the #2273 design | not answered: kept as recommended, after the prototype is confirmed |

The researcher, on D3 (chat 2026-10-26, verbatim):

> another item I missed in D3 is the cluster documents (files). Observations are already formulated in the existing
> documents, must be adopted and have precedence, I want to see if it can be avoided to redo observations already
> done, but just never recorded.

Recorded in sections 3 and 4: the documents are read at 0.GAP pre and adopted first at Record. One point is left:

| # | point | options | my recommendation *(inferential)* |
|---|---|---|---|
| D7 | How an adopted reading is put into the B2 shape | a) word for word: the line's text as `obs_text`, with a kind; b) restated in the B2 shape (kind, `obs_text`, `meaning`, `implication`, `basis`) keeping the document's substance and words, citing the line | b: a worksheet line is often a fragment (a table row, a bullet), and the B2 shape is what the claims step reads; the citation keeps the line traceable. The prototype on `M18_thirst` shows how much of the 175 lines this applies to |

**Related open items** (cross-checked, B:65): #2262 (gap analysis counts any observation as read) is met by D3;
#2260 and #2261 (observations outside the rules, in the strand-ledger shape) are what D3 c keeps out of the count;
#2276 (B4, the collation reads every observation) is met by the gathering's `observations`; #2278 (B6, gap types and
their checks) is changed by D4; #2279 (B7, reading output folder and index exclusion) is changed by D2; #2280 (B8,
ledger faces gathered) is met in part by the adoption from the cluster documents; #2266 (the October catch-up import)
is the source of the observations already imported; #2296 (U6) gives the `verse_lexical_id` slice (D5). All are on hold under the parked
#2268.

## 7. What would change in the code (after the decisions; nothing yet)

`iba/app/lib/reading.py`: `open_` (one subgroup, the segment, the file in the cluster's folder), `gather` (read-only,
the section, the related open items), `observe` (reads the file), `record` (reads the section, writes
`verse_lexical_id` and the open item responses), `check` (the gates). Config: the step descriptions, RO12 and the
pre-gap settings (D4), the output folder (D2) and the reading index's exclusion of it. USER-GUIDE.md section 8 and the PS worksheet. No schema
change: `ib_node.verse_lexical_id` exists (#2292).
