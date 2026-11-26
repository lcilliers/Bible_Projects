# #2538: ReadElements (step 3.1) — the instruction block and a real package (v1, 2026-11-26)

Written by Claude, session 760131f7, for the researcher's review before 3.1 is read live for "reasoning".
- **The package:** [`2538-readelements-sample-package-v1-20261126.json`](2538-readelements-sample-package-v1-20261126.json), exactly as ReadElements writes it, made on a copy of live with `elements_2538_v1_20261126.py` applied. Nothing was written to the live database.
- **Size and time:** 102,159 characters (about 25,539 tokens) and 0.41 s.
- **What it holds:** 123 evidence observations to take up (the 7 senses and 7 enrichments first, then the 109 2.1 findings); 15 word readings it may rest on besides; 17 older inner-being observations; 16 earlier readings; 41 occurrences in 36 verses.
- **Parts, in characters:** instruction 11,407, uses 1,279, meaning_by_code 7,781, to_take_up 43,179, may_rest_on_besides 6,099, older_inner_being 11,038, earlier_readings 6,585, occurrences 4,596, verses 6,537, answer 1,952.
- **One package for the subgroup.** A 3.1 row is recorded whole: every observation taken up must be rested on by a finding or declared not used, and a second record withdraws the first. So the subgroup cannot be split across packages.

## 1. What the build found and settled

- **The lexicon.** In the form the old LayerPull used, the meaning of each code was the whole lexicon: 301,474 of 388,907 characters for "reasoning". Step 3.1 reads evidence, and the full lexicon is read at 1.2, whose enrichments 3.1 takes up. The package now gives each code's sense head and meaning range, cut to 500 characters (7,781 in all).
- **Two evidence gates that disagreed.** 3.1 has its own older evidence gate (`collectionvalidate`). It counted dead traces on inner-being observations in the evidence layer, so it refused "reasoning" over the 16 old-group findings the sweep kept as inner being, which B5 had passed. Inner-being traces belong to the inner-being layer, which `trace_gaps` already checks (VA-06). The evidence layer of `collectionvalidate` now skips inner-being observations, as B5 does. The validation tests give the same results with and without this change.
- **The old group's findings.** RW-13 answers only older observations of other stages, so the 16 kept findings of the replaced group (build stage layer-3) would have floated past 3.1. They are listed as `earlier_readings` and must each be answered in the record's `existing` (accept, modify, delete, merge or leave): the record refuses an answer that leaves any out.
- **Older observations already answered.** All 17 older inner-being observations on "reasoning" were answered at earlier steps. They are shown for the reading (IB-05) and marked `answered_before`; the record asks again only for one not yet answered on an occurrence a finding names (RW-13).

## 2. The instruction block

**What this read is.** Step 3.1, the elements of one subgroup (stage 4, C1; the end of the loop for the subgroup): what the evidence of the subgroup shows of the elements of a behaviour of the inner being. The input is the evidence observations of the subgroup by marker (`to_take_up`, the senses first, then the 2.1 findings and the older evidence), not the verses; the verses are kept for an occasional read-back. A finding is a building block, never a claim about the behaviour as a whole (that is stage 5).

**How to read.**
1. Read the observations to take up, in order: the senses (1.1) and their enrichments (1.2) first, then the 2.1 findings (pairings, qualifiers, entities, direction, double meanings), then the older evidence. The inner-being workings work more with the senses than with the surfaces, so findings rest on the senses first.
2. For each item a finding may use (`uses`): what is done and its mode (operation, with its chain), whether a refusal or a pursuit (polarity), what it is directed at (object), the outward act (enactment), the other party with the route (party), the circumstance, and what a qualifier or a variation of the word gives the working (role, the dimension). Never the meaning of the word (stage 1).
3. Read the older inner-being observations (`older_inner_being`) with them: each is considered first, accepted with a trace to evidence, restated where it says more than the evidence, consumed where a finding says the same, merged, or deleted where it cannot be made true.
4. Go back to a verse (`verses`) only where the evidence does not settle the question, and say why.

**What to write.**
1. Fill `answer.findings`: each one observation, with a `key` unique in the answer, `kind` (of the item's kinds), `text`, `basis` (stated or read), `parts` with `item` (one of `uses`) and what the item needs (with `grounds`), and `nodes`: a `traced` node on each observation it rests on (from `to_take_up` or `may_rest_on_besides`) and an `occurrence` node, with its `role` chosen from the verse (characteristic, qualifier, object, relational target, enactment or standalone), on the occurrences those observations cover.
2. An occurrence outside the observations a finding rests on is allowed only with a `read_back` entry on the finding: {verse: the osis id, why}.
3. `not_used`: {observation id: reason} for every observation to take up that no finding rests on. Every one is rested on or declared, never both.
4. `older`: answer, once, each older inner-being observation (`older_inner_being`) that has a node on an occurrence your findings name (RW-13; the record lists any it misses, and refuses an answer to one on no named occurrence: those are shown, not demanded, IB-05): keep (with nature inner_being: it stands, traced to evidence), restate, merge, consume (carriers ["this"] or ids, mapping), delete_neither, or defer (collection, nature, finding).
5. `existing`: answer every earlier reading (`earlier_readings`: inner being of an earlier grouping on these occurrences) with accept, modify, delete, merge or leave, and its reason.
6. The text says what the evidence shows of the element; it names its verses; it never restates a verse and never states the behaviour as a whole.
7. Then: Collection-Build.ps1 -Action RecordElements -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.

**The rules this read keeps** (text read live from `cfg_method_rule`):

- **IB-02 stage-4-starts-from-the-observations:** Stage 4 starts from the observations, not the verses (researcher, #2526 Q7, 2026-11-21): the subgroups and the stage 3 observations on them are the input, the behaviours are discovered from analysing them, and the base data is read back into only occasionally. Every finding of step 3.1 or 3.2 rests on named observations (a traced node on each, with an occurrence node as well) and its occurrence nodes lie within the occurrences those observations cover; an occurrence outside them is allowed only where the finding records a read-back (the verse and why). Each node has a role from reading.node_roles other than lexical, chosen by the reading. A 3.3 finding carries nodes on the occurrences of both sides in the shared verses.
- **IB-03 findings-follow-the-observation-rules:** A finding of a stage 4 row is checked by the rules of observationrecord.check and check_item_parts (kind, text, basis, route, parts.item and what the item needs, node roles, collection of each node) and by RG, RW and RS, which are not restated here: one observation for each finding, never a duplicate, with a node on each word it applies to (RO11, RW-03); founded in the observations and never a restatement of the verse (B:131); parts.item is one of the items the row's item uses (cfg_setting layer.reading). An observation whose nodes all bear on an act is refused: those words are nodes of the observation of the act. A finding is a building block of a behaviour and never a claim (stage 5).
- **IB-04 nothing-is-lost-on-the-way-to-stage-5:** Nothing the step reads is lost on the way to stage 5. Step 3.1: every stage 3 observation of the subgroup is rested on by a finding or declared in not_used with its reason in words. Step 3.2: every 3.1 observation of the collection is gathered into a behaviour (a traced node on it from a flag finding of type discovery) or declared in not_gathered with its reason, and the row has at least one behaviour unless it is recorded as none with its reason. A behaviour names and gathers; it makes no claim about what the behaviour is.
- **IB-05 earlier-observations-are-shown-not-demanded:** An earlier inner-being observation with a node on the occurrences of a 3.1 row (any stage but lexical, layer-1, layer-2 and layer-3) is shown in the pull for information and may be actioned in `existing`: accepted, modified, deleted, merged or left, each with its reason, through observationrecord (RW-01, RW-09); nothing is demanded of it, and it counts for nothing in the check. A row answered again withdraws its earlier observations with the reason. Every older live observation with a node on an occurrence of the row is answered in fill.older at the record of the row (RW-13); this rule's `existing` actions of stage 4 are unchanged.
- **IB-07 inner-being-observations-trace-to-evidence:** Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed.
- **RG-03 role-per-occurrence:** Find the main inner-being operation, and give every word that bears on it its role in this finding (cfg_setting reading.node_roles): characteristic, qualifier and what it gives the characteristic, object or content, relational target, or enactment. A word read in the verse that holds nothing for the inner being is standalone. The role comes from this verse, never from the cluster tag. Where a standalone word proves to qualify a characteristic, it is a qualifier of it.
- **RG-04 qualifier-binding:** A qualifier gets no separate account of itself, but what it gives the characteristic it binds to is evaluated for its value and recorded as a qualification finding, applied by its nodes to the qualifier (role qualifier) and the characteristic (role characteristic). What it gives can vary widely: grade, nature, impact, size, relation, a measure, strengthening, ground, cause, object, setting or bait are examples, not a list (#2273 D9). A qualifier whose usage varies across contexts may earn its own reading later.
- **RG-06 parties-and-route:** Record the parties: who bears the act, who causes it, who is acted on (source, target, impact, purpose), and the route (cfg_enum observation_route). A non-human being is never itself a HIB; a collective stays one HIB; an implied party is named as referential, never asserted.
- **RG-10 never-not-x:** Never close a verse or item on 'not X'. A role label is never a verdict; the close records what the verse is. Silence about the inner being is a finding, recorded as data with its reason.
- **RG-11 hidden-behind-act:** A phenomenon hidden behind a stated or refrained act may be named, with the verb, clause or stated silence that grounds it, and whether it is stated or read.
- **RG-13 source-vs-enablement:** Keep the source of an interior state apart from the source of an enablement to act.
- **RG-24 adverbial-qualifier:** A tagged word that works adverbially in an occurrence (a noun with a preposition qualifying the predicate, as 'in the counsel of the wicked') is a qualifier there, not the verse's characteristic. The role is per occurrence: the same word may be the characteristic elsewhere.
- **RG-25 simile-tenor:** In a simile, the predicates of the vehicle (the tree that yields, does not wither) are read for what they say of the one compared (the tenor), not as the vehicle's own acts.
- **RO11 one-row-per-code:** One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- **RW-03 no-duplicates-multi-node:** One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- **RW-04 concise-verse-specific:** Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- **RW-12 marker-and-node-columns-at-creation:** An observation is created with its marker (ib_observation.nature, from the item answered, cfg_setting layer.reading items.<item>.nature; a finding file never sets it) and every word node with the columns of layer.reading node_required. A column the data cannot give (layer.reading node_gap_columns: an empty morph in the source row, a surface with no placement in the collection index) is left empty and its reason is kept on the node (disposition_note); any other missing column refuses the whole file and nothing is written. A trace to a deleted observation is refused (IB-07).
- **VA-05 the-marker-follows-content-not-stage:** Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being, based on evidence, a building block of the stage 5 claims. The marker (ib_observation.nature) follows the content and purpose of the observation, never its stage (RS-04): an observation of any stage may be inner being when it traces to evidence. One that states both is split. The marker is set when the observation is created, by the item that is answered (cfg_setting layer.reading items.<item>.nature); a finding file never sets it; the validation changes it only where the content shows the item's nature does not hold.

**The items a finding may use:**

- **role** (qualification, statement; basis stated, read): its role: the qualifier and what it gives the characteristic
- **polarity** (statement; basis stated, read): whether the act is a refusal or a pursuit
- **object** (statement; basis stated, read): what the act is directed at or against
- **enactment** (statement; basis stated, read): the outward act the inner act produces, where the verse states one
- **party** (party; basis stated, read): the other party and the sequence, with the route
- **circumstance** (statement; basis stated): how it appears here: the circumstance of the verse
- **operation** (statement; basis stated, read): the operation as an action description (who or what does what), its mode, the primary one
- **chain** (link; basis stated, read): the chain of operations the verse links in sequence
- **flag** (statement; basis stated, read): a typed flag: data-quality, or discovery for the claims process

## 3. The data, as the package carries it

**The first observation to take up (a sense):**

```json
{
 "observation": 22861,
 "stage": "layer-1",
 "kind": "group",
 "item": "group-definition",
 "text": "Reasoning as argument put to other people: Paul reasons with Jews and others in the synagogue, the market and the hall of Tyrannus and before Felix, and the Lord invites the people to argue the case out together. The word is spoken argument with a hearer and a matter, aimed at persuading or setting right; the Greek verb is of discourse and the Hebrew verb of arguing a case. Verses: Act 17:2, Act 1",
 "basis": "read",
 "verses": [
  "Acts.17.2",
  "Acts.17.17",
  "Acts.18.4",
  "Acts.18.19",
  "Acts.24.25",
  "Acts.19.8",
  "Acts.19.9",
  "Isa.1.18"
 ]
}
```

**One earlier reading:**

```json
{
 "observation": 22473,
 "stage": "layer-3",
 "kind": "statement",
 "text": "Reasoning is a done act of speech in seven Acts verses: Paul reasons in the synagogue, in the marketplace, in the hall of Tyrannus and before Felix (Act 17:2, 17:17, 18:4, 18:19, 19:8, 19:9, 24:25). The verb stands in the aorist or imperfect and is spoken to hearers, with persuading beside it in several; it is an exchange of grounds in speech and not a silent act."
}
```

**The answer to fill (its first parts):**

```json
{
 "command": "ReadElements",
 "collection": "thought",
 "subgroup": "reasoning",
 "ledger_id": 1294,
 "findings": [
  {
   "key": "f1",
   "kind": "",
   "text": "",
   "basis": "read | stated",
   "parts": {
    "item": "role | polarity | object | enactment | party | circumstance | operation | chain | flag",
    "grounds": ""
   },
   "nodes": [
    {
     "occurrence": "<occurrence id>",
     "role": "<a node role>"
    },
    {
     "traced": "<id of an observation it rests on>"
    }
   ],
   "read_back": []
  }
 ],
 "not_used": {},
 "older": [],
 "existing": [
  {
   "observation": 22473,
   "action": "accept | modify | delete | merge | leave",
   "reason": ""
  },
  {
   "observation": 22474,
   "action": "accept | modify | delete | merge | leave",
   "reason": ""
  }
 ]
}
```

## 4. Tested

- **`iba/app/tools/temp_2538_elements_test_run.py`, on a copy of live: 19 of 21 pass.** It covers:
  - the package takes up exactly the observations the recorder demands, senses first, within its limits;
  - LayerNext names ReadElements;
  - refused whole, with nothing written: a wrong command, another row, an earlier reading left out, a trace to an observation the row may not rest on, an occurrence outside what a finding rests on with no read-back, an observation taken up neither rested on nor declared, a finding of an item the step does not use;
  - a minimal answer, written as scaffolding on the copy, recorded: the 3.1 row validates, the finding is marked inner being, the loop of "reasoning" is complete, and LayerNext moves to the next subgroup.
  - The two blocked cases need an older inner-being observation not yet answered, and "reasoning" has none.
- **The other suites:** the loop-order test passes 8 of 8 on a copy of live. The validation tests give the same results with and without the `collectionvalidate` change.

The 3.1 reading itself, about 123 observations to build on, is the live run after your review.
