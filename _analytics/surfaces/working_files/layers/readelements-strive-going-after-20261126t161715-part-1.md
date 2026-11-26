# ReadElements -- strive / going after -- step 3.1

## What to do

Step 3.1, the elements of one subgroup (stage 4, C1; the end of the loop for the subgroup): what the evidence of the subgroup shows of the elements of a behaviour of the inner being. The input is the evidence observations of the subgroup by marker (`to_take_up`, the senses first, then the 2.1 findings and the older evidence), not the verses; the verses are kept for an occasional read-back. A finding is a building block, never a claim about the behaviour as a whole (that is stage 5).

Read:
- Read the observations to take up, in order: the senses (1.1) and their enrichments (1.2) first, then the 2.1 findings (pairings, qualifiers, entities, direction, double meanings), then the older evidence. The inner-being workings work more with the senses than with the surfaces, so findings rest on the senses first.
- For each item a finding may use (`uses`): what is done and its mode (operation, with its chain), whether a refusal or a pursuit (polarity), what it is directed at (object), the outward act (enactment), the other party with the route (party), the circumstance, and what a qualifier or a variation of the word gives the working (role, the dimension). Never the meaning of the word (stage 1).
- Read the older inner-being observations (`older_inner_being`) with them: each is considered first, accepted with a trace to evidence, restated where it says more than the evidence, consumed where a finding says the same, merged, or deleted where it cannot be made true.
- Go back to a verse (`verses`) only where the evidence does not settle the question, and say why.

Write:
- Fill `answer.findings`: each one observation, with a `key` unique in the answer, `kind` (of the item's kinds), `text`, `basis` (stated or read), `parts` with `item` (one of `uses`) and what the item needs (with `grounds`), and `nodes`: a `traced` node on each observation it rests on (from `to_take_up` or `may_rest_on_besides`) and an `occurrence` node, with its `role` chosen from the verse (characteristic, qualifier, object, relational target, enactment or standalone), on the occurrences those observations cover.
- An occurrence outside the observations a finding rests on is allowed only with a `read_back` entry on the finding: {verse: the osis id, why}.
- `not_used`: {observation id: reason} for every observation to take up that no finding rests on. Every one is rested on or declared, never both.
- `older`: answer, once, each older inner-being observation (`older_inner_being`) that has a node on an occurrence your findings name (RW-13; the record lists any it misses, and refuses an answer to one on no named occurrence: those are shown, not demanded, IB-05): keep (with nature inner_being: it stands, traced to evidence), restate, merge, consume (carriers ["this"] or ids, mapping), delete_neither, or defer (collection, nature, finding).
- `existing`: answer every earlier reading (`earlier_readings`: inner being of an earlier grouping on these occurrences) with accept, modify, delete, merge or leave, and its reason.
- The text says what the evidence shows of the element; it names its verses; it never restates a verse and never states the behaviour as a whole.
- In place of writing `nodes`, a finding may name `rests_on` (the observations it rests on) and `role` (the node role of the words they cover; `roles` {occurrence: role, or "" to leave one out} for the exceptions): the recorder writes a traced node on each and an occurrence node on each occurrence they cover (each observation's `covers` or `occurrences` lists them). Nodes written by hand are kept.
- Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing written; correct the answer until it finds none, then -Action RecordElements -File <the answer file>. The record refuses the whole file on any fault and lists every fault.

## Refused when (by rule)

- DA-02: is not a word of a collection; is in no collection: name the occurrence it supports; word node(s) carry no collection; names collection ; belongs to collection; has a node with no collection; the nodes do not carry the collections
- IB-02: are outside the observations the finding rests on; a finding rests on observations; rests on no observation (a traced node on each); which this row may not rest on; outside the observations it rests on; gives no reason in words
- IB-03: names its grounds in the words of the verse (parts.grounds; at least one node (what the finding applies to); only a term finding applies to a word with no verse
- IB-04: names an observation this row must take up; is neither rested on by a finding nor in; is both rested on by a finding and in; is part of this match and no finding traces it; without a reason in words; are neither rested on by a finding nor declared; declares an observation this row does not take up; of the match are not traced
- IB-06: its observations are missing or withdrawn; records are not readable; which this row does not use;  has stage ; has no node on an occurrence
- IB-07: is not marked evidence: an inner-being observation traces to evidence; an observation does not trace itself
- IB-08: the collection shows at least one behaviour; no behaviour: the collection row needs a flag finding
- LR-01: is not closed (every row answered
- LR-02: the data holds no occurrence for this aspect
- LR-03: cannot be recorded as none; none needs its reason; recorded as none without a permitted reason
- PC-01: is not a step of the layered reading; is not a live subgroup of; no live collection; has no live subgroup; cannot read ;  are required;  is required
- PC-02: answer (its `command` must be; a node is an object; a finding is an object; parts is an object with; is a list of {observation, action, reason; a unique key is required; is a short name unique in the row; text is required; a read_back entry is ;  is {observation id: reason}; `traced` is the id of an observation; a node names the occurrence id of the word; a node names the word (strong); an `existing` entry names a live observation and an action; the row is answered by findings; this is not the answer of a read
- PC-03: nothing written:
  ledger ; not a ledger row of; is not an occurrence this row may name; is neither a live observation nor a finding key; are not observations this row may rest on; is not an older live observation on the occurrences of this row; is not an open old observation of this subgroup; a deferral names a live collection; has no matching live verse_lexical row; both must be different live observations; is not a live occurrence of;  is not an occurrence of ; is not a live observation; is not a live node; does not exist;  is not a ; merge names a live observation to keep; defer names a live collection; which this row may not name
- PC-04: kind must be one of; basis must be one of; role must be one of; route must be one of; tag must be one of; stage must be one of; nature must be one of; parts.item is one of; are not among; is written as a finding of the kind; has the basis; gives parts.polarity; gives parts.mode; gives parts.flag_type; disposition must be observed; cannot be modified (allowed:; not in live cfg_enum ib_observation; action is one of; names its marker, nature one of
- PC-05: only an open or an unvalidated row is recorded; the evidence validation of ; has no row for; has no open row; its group is retired or missing; carry names a LATER step of; the loop is for one subgroup at a time; the data no longer demands this aspect; partner collection 
- PC-06:  s, more than ;  characters, more than 
- PC-07: cfg_setting layer.reading is missing; cfg_setting layer.scan; layer.reading step ; (apply iba/app/migration/archive/; the code is ahead of the config; have no nature in cfg_setting layer.reading; the read names rule(s) not active; is empty: run install_nature; are not ib_observation.tag values;  is missing
- RG-03: every node it holds bears on an act; has a node with no valid stage 4 role
- RG-04: a qualification finding applies to its qualifier
- RG-06: carries its route; is held only on a party or link finding
- RS-04: earlier reading(s) of the subg;  needs its reason (
- RW-01: needs its reason, in words; say in words what was checked; say what it states that the existing record does not; state the finding the collection is to close; say in words which words it relies on; say in words why the word supports no finding; is the last word node of observation; already holds that occurrence: drop the node instead; its occurrence is on no live node of; carry gives its reason in words
- RW-03: is already live as observation; the same text as; an existing finding takes nodes only; a merge is for the same description
- RW-04: restates the verse; is a bare negation with no actual content
- RW-13: are still open in the ledger; have no answer in fill.older; its fate is not recorded; is not in the change log of observation; the change log does not show it
- RW-14: the statement used more than
- VA-03: name the carrying observations; the mapping is stated in words; occurrence(s) are on no node of; not carried needs its reason
- VA-04: only an observation that is neither is deleted here; repair those traces first
- VA-05: a deferred observation is marked now

## Limits

- grounds and every reason: characters at least: 10
- observation text: characters at least: 40
- consecutive verse words a text may copy, at most: 7

## The rules

- IB-02 stage-4-starts-from-the-observations: Stage 4 starts from the observations, not the verses (researcher, #2526 Q7, 2026-11-21): the subgroups and the stage 3 observations on them are the input, the behaviours are discovered from analysing them, and the base data is read back into only occasionally. Every finding of step 3.1 or 3.2 rests on named observations (a traced node on each, with an occurrence node as well) and its occurrence nodes lie within the occurrences those observations cover; an occurrence outside them is allowed only where the finding records a read-back (the verse and why). Each node has a role from reading.node_roles other than lexical, chosen by the reading. A 3.3 finding carries nodes on the occurrences of both sides in the shared verses. In 3.1 a qualification finding may also hold, with the role qualifier, the occurrences of the partner words the subgroup's 2.1 qualifier observations name, where the reading judges the qualifier bears on the working; a qualifier that does not bear on it is declared in not_used with its reason, never forced into a finding.
- IB-03 findings-follow-the-observation-rules: A finding of a stage 4 row is checked by the rules of observationrecord.check and check_item_parts (kind, text, basis, route, parts.item and what the item needs, node roles, collection of each node) and by RG, RW and RS, which are not restated here: one observation for each finding, never a duplicate, with a node on each word it applies to (RO11, RW-03); founded in the observations and never a restatement of the verse (B:131); parts.item is one of the items the row's item uses (cfg_setting layer.reading). An observation whose nodes all bear on an act is refused: those words are nodes of the observation of the act. A finding is a building block of a behaviour and never a claim (stage 5).
- IB-04 nothing-is-lost-on-the-way-to-stage-5: Nothing the step reads is lost on the way to stage 5. Step 3.1: every stage 3 observation of the subgroup is rested on by a finding or declared in not_used with its reason in words. Step 3.2: every 3.1 observation of the collection is gathered into a behaviour (a traced node on it from a flag finding of type discovery) or declared in not_gathered with its reason, and the row has at least one behaviour unless it is recorded as none with its reason. A behaviour names and gathers; it makes no claim about what the behaviour is.
- IB-05 earlier-observations-are-shown-not-demanded: An earlier inner-being observation with a node on the occurrences of a 3.1 row (any stage but those of the build: lexical, layer-1, layer-2, layer-3.1 to layer-3.3, and layer-3 before 2026-11-26) is shown in the pull for information and may be actioned in `existing`: accepted, modified, deleted, merged or left, each with its reason, through observationrecord (RW-01, RW-09); nothing is demanded of it, and it counts for nothing in the check. A row answered again withdraws its earlier observations with the reason. Every older live observation with a node on an occurrence of the row is answered in fill.older at the record of the row (RW-13); this rule's `existing` actions of stage 4 are unchanged.
- IB-07 inner-being-observations-trace-to-evidence: Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or on a live inner-being observation that itself traces to evidence (the trace chain of stage 4: a 3.2 behaviour traces the 3.1 elements it gathers, a 3.3 match the 3.1 and 3.2 observations it comes from; at most three links), unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed.
- RG-03 role-per-occurrence: Find the main inner-being operation, and give every word that bears on it its role in this finding (cfg_setting reading.node_roles): characteristic, qualifier and what it gives the characteristic, object or content, relational target, or enactment. A word read in the verse that holds nothing for the inner being is standalone. The role comes from this verse, never from the cluster tag. Where a standalone word proves to qualify a characteristic, it is a qualifier of it.
- RG-04 qualifier-binding: A qualifier gets no separate account of itself, but what it gives the characteristic it binds to is evaluated for its value and recorded as a qualification finding, applied by its nodes to the qualifier (role qualifier) and the characteristic (role characteristic). What it gives can vary widely: grade, nature, impact, size, relation, a measure, strengthening, ground, cause, object, setting or bait are examples, not a list (#2273 D9). A qualifier whose usage varies across contexts may earn its own reading later.
- RG-06 parties-and-route: Record the parties: who bears the act, who causes it, who is acted on (source, target, impact, purpose), and the route (cfg_enum observation_route), whose meaning is cfg_behaviour_rule 72 (route-verses-hib-other-beings-data-only): A another being in its own right, B another being with the human inner being, C no bearing, data only; a verse may take A and B. A non-human being is never itself a HIB; a collective stays one HIB; an implied party is named as referential, never asserted.
- RG-10 never-not-x: Never close a verse or item on 'not X'. A role label is never a verdict; the close records what the verse is. Silence about the inner being is a finding, recorded as data with its reason.
- RG-11 hidden-behind-act: A phenomenon hidden behind a stated or refrained act may be named, with the verb, clause or stated silence that grounds it, and whether it is stated or read.
- RG-13 source-vs-enablement: Keep the source of an interior state apart from the source of an enablement to act.
- RG-24 adverbial-qualifier: A tagged word that works adverbially in an occurrence (a noun with a preposition qualifying the predicate, as 'in the counsel of the wicked') is a qualifier there, not the verse's characteristic. The role is per occurrence: the same word may be the characteristic elsewhere.
- RG-25 simile-tenor: In a simile, the predicates of the vehicle (the tree that yields, does not wither) are read for what they say of the one compared (the tenor), not as the vehicle's own acts.
- RO11 one-row-per-code: One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- RW-03 no-duplicates-multi-node: One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- RW-04 concise-verse-specific: Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- RW-12 marker-and-node-columns-at-creation: An observation is created with its marker (ib_observation.nature, from the item answered, cfg_setting layer.reading items.<item>.nature; a finding file never sets it) and every word node with the columns of layer.reading node_required. A column the data cannot give (layer.reading node_gap_columns: an empty morph in the source row, a surface with no placement in the collection index) is left empty and its reason is kept on the node (disposition_note); any other missing column refuses the whole file and nothing is written. A trace to a deleted observation is refused (IB-07).
- VA-05 the-marker-follows-content-not-stage: Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being, based on evidence, a building block of the stage 5 claims. The marker (ib_observation.nature) follows the content and purpose of the observation, never its stage (RS-04): an observation of any stage may be inner being when it traces to evidence. One that states both is split. The marker is set when the observation is created, by the item that is answered (cfg_setting layer.reading items.<item>.nature); a finding file never sets it; the validation changes it only where the content shows the item's nature does not hold.
- B:72 route-verses-hib-other-beings-data-only: The study's primary focus is the human inner being (HIB). Each verse read is routed by what it shows, and the route is recorded in its observation. (A) Other beings in their own right: a word used of God, angels, other spirits or nature (non-HIB) is routed to Ch 13 "Other beings" (13.1 Divine, 13.2 Angels, 13.3 Other spirits, 13.4 Nature), read for what the verses say that being is and does; for God, also how his character passed to the HIB through creation in his image, held open (#1984). (B) Another being interacting with the HIB is fully in HIB scope. A verse may take A and B, described from different angles. (C) A verse with no inner-being and no other-being bearing is still assessed and recorded as data, and does not enter the narrative.
- DA-02 a-node-per-occurrence-with-its-surfaces-collection: A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope (B:130), is not written and is listed.
- IB-06 stage-4-check-rederives-from-the-tables: LayerCheck validates a stage 4 row from the tables alone: the demanded occurrences and the observations the row may rest on are re-derived; at least one live observation of the stage of its step (layer-3.1, layer-3.2 or layer-3.3) with its stable_key on the row; each observation's parts still valid and its item one the row uses; each live node has a valid role, a collection and its subgroup; each observation has a traced node on an observation the row may rest on; in 3.1 and 3.2 each occurrence node lies in the occurrences of the observations it rests on or its verse is in the recorded read-back; the completeness of IB-04 (not_used, not_gathered, the behaviour of 3.2); no observation restates a run of the verse longer than reading.observation_items max_verse_words_copied. A row that fails is unvalidated and its step is not closed.
- IB-08 what-a-behaviour-is: A behaviour (step 3.2) is one working of the inner being: one core operation, who or what does what, shown by several element observations of 3.1. Elements that show the same operation belong to one behaviour, whatever their mode, polarity, object, party or circumstance, and in whatever subgroup they sit; those differences are written as relating findings (operation, chain, party, circumstance, role). Different operations linked in sequence are a chain between behaviours, not one behaviour. A group that holds two operations is split; two groups that hold one operation are joined. An element that shows no working of a human inner being (another being in its own right, route A of B:72; a word that is not an act of the mind) is declared not gathered with its reason. A behaviour is named by what is done, never by what it means for the inner being (stage 5).
- LR-01 a-step-opens-on-gates-and-derives-its-ledger: A step of the layered reading opens only when the grouping is finished (every surface placed in a subgroup or isolated with its reason, every subgroup holding a surface) and the previous step is closed; with -Subgroup the needs and gates are judged for that subgroup alone (#2538). Step S1 is read after the grouping; step 1.1 needs step S1 closed: every word of the subgroup (surface and lettered Strong's code) answered and validated. Opening derives one ledger row for each aspect the data demands (cfg_setting layer.reading); an aspect the data no longer demands is retired, a new one is added, and a second open changes nothing.
- LR-02 nodes-are-built-from-the-data: The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
- LR-03 none-needs-a-permitted-reason: An aspect is recorded as none only where its item allows it (cfg_setting layer.reading none_allowed) and with its reason in words. A group definition and a group's Strong's enrichment are always observed.
- PC-01 the-command-names-a-live-unit: A read or record command names a live collection, a live subgroup of it where the read is by subgroup, and a step or item the layered reading knows. A command that names one that does not exist is refused and writes nothing.
- PC-02 the-answer-is-the-packet-form: An answer is the output form its read wrote: the `command` of that read; every entry an object, or a list, where the form has one; each field in its place with its type (a key unique in the answer, a text, a reason in words); each item answered once; and at least one entry where the form asks for entries. A file in another shape is refused whole and nothing is written.
- PC-03 names-are-those-the-packet-offers: Every ledger row, occurrence, observation, sense, node, verse and collection an answer names is one the packet offered for this unit, or a key the answer itself defines, and is live in the database. A name outside them is refused.
- PC-04 values-from-the-allowed-lists: Every coded value of an answer (kind, basis, item, part, role, route, mode, polarity, flag type, disposition, verdict, action, nature, stage, status) is one of the values the configuration allows for it (cfg_enum, cfg_setting layer.reading, reading.observation_items, validate.reading), as the packet lists them. Any other value is refused.
- PC-05 the-unit-is-at-its-step: A read or record runs only where the ledger has its unit at that step: the row open, or answered and not yet validated, and the steps before it closed (S1 before 1.1; the 2.1 rows before the sweep; the sweep before the evidence validation; its gate before 3.1; every subgroup through 3.1 before 3.2). Out of order it is refused, and the message names what comes first.
- PC-06 within-the-configured-limits: A read writes its packet within the time and size the configuration sets (cfg_setting layer.read_types: limits, package_max_chars, read_max_seconds). A read that would exceed them is refused, nothing is written, and the limit is named.
- PC-07 the-config-the-code-needs-is-present: The code of the reading runs only where the configuration it reads is in place (the settings, steps, items, natures, enums and rules it names). Where the code is ahead of the configuration, the command is refused and names what is missing.
- RS-04 existing-checked-accept-modify-delete: When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- RW-01 changed-only-by-reading: No observation is changed except by a reading, and every change is recorded with its reason. An observation no longer supported by the verse is soft-deleted, with the reason.
- RW-13 older-observations-answered-at-record: Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- RW-14 every-lookup-is-pinpointed: A lookup of related data in the build or the validation is by an indexed column and takes a chunk of ids (cfg_setting layer.scan chunk); none runs once for each item of a list, and a statement that uses more work than layer.scan max_vm_ops is stopped and named, nothing written (lib/scanguard.py). The tests refuse a statement of the build whose query plan scans a table (layer.scan scan_ok lists the temporary tables a statement may scan).
- VA-03 consumption-is-verified-before-deletion: An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- VA-04 neither-evidence-nor-inner-being-is-deleted: An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.

## made

2026-11-26T16:17:15Z

## unit

- ledger_id: 2536
- to_take_up: 137
- may_rest_on_besides: 21
- older_inner_being: 0
- earlier_readings: 0
- occurrences: 114
- verses: 82

## asks

What do the stage 3 observations of this subgroup (its definition, its Strong's enrichment, its pairings, qualifiers, entities, direction, relations and double meanings, with the stage 1 senses) show of the elements of a behaviour of the inner being: what is done and its mode, whether a refusal or a pursuit, what it is directed at, the outward act, the other party with the route, the circumstance, the chain of operations, and the dimensions of the working (what a qualifier or a variation of the word gives it, from the lexical variation the stage 3 observations record)? Each finding is one observation that rests on named observations (a traced node on each) and carries nodes on the occurrences those observations cover, with the role each has; an occurrence outside them is allowed only with a read-back (the verse and why). Every stage 3 observation of the subgroup is rested on by a finding or declared not used, with the reason. A finding is a building block and never a claim about the behaviour as a whole (stage 5).

## uses

- item: role
  name: its role: the qualifier and what it gives the characteristic
  kinds: ["qualification", "statement"]
  bases: ["stated", "read"]
- item: polarity
  name: whether the act is a refusal or a pursuit
  kinds: ["statement"]
  bases: ["stated", "read"]
- item: object
  name: what the act is directed at or against
  kinds: ["statement"]
  bases: ["stated", "read"]
- item: enactment
  name: the outward act the inner act produces, where the verse states one
  kinds: ["statement"]
  bases: ["stated", "read"]
- item: party
  name: the other party and the sequence, with the route
  kinds: ["party"]
  bases: ["stated", "read"]
- item: circumstance
  name: how it appears here: the circumstance of the verse
  kinds: ["statement"]
  bases: ["stated"]
- item: operation
  name: the operation as an action description (who or what does what), its mode, the primary one
  kinds: ["statement"]
  bases: ["stated", "read"]
- item: chain
  name: the chain of operations the verse links in sequence
  kinds: ["link"]
  bases: ["stated", "read"]
- item: flag
  name: a typed flag: data-quality, or discovery for the claims process
  kinds: ["statement"]
  bases: ["stated", "read"]

## node_roles

- relevant: ["characteristic", "qualifier"]
- bears_on: ["object", "relational_target", "enactment"]
- recognised: ["standalone"]
- lexical: ["lexical"]

## allowed_values

- polarity: ["refusal", "pursuit"]
- mode: ["done", "foreseen", "commanded", "negated", "reported"]
- flag_type: ["data-quality", "discovery"]
- route: ["A", "B", "C"]
- basis: ["read", "stated"]

## definition_of_the_subgroup

null

## meaning_by_code

- G0565: {"sense_head": "to go away", "meaning_range": "to go away, withdraw; <b>to go away, depart,</b> <ref='Mat.8.18'>Mt. 8:18</ref>; <b>to go forth, pervade,</b> as a rumor, <ref='Mat.4.24'>Mt. 4:24</ref>; <b>to arrive at</b> a destination, <ref='Luk.23.33'>Lk. 23:33</ref>; <b>to pass away, disappear,</b> <ref='Rev.21.4'>Rev. 21:4;</ref> <greek>ἀπέρχομαι ὀπισω</greek>, <b>to follow,</b> <ref='Mrk.1.20'>Mk. 1:20</ref>"}
- G1161: {"sense_head": "then", "meaning_range": "but, and, then, rather; a conjunctive particle, marking the superaddition of a clause, whether in opposition or in continuation, to what has preceded, and it may be variously rendered <b>but, on the other hand, and, also, now,</b> etc.; <greek>καὶ δέ</greek>, when there is a special superaddition in continuation, <b>too, yea,</b> etc. It sometimes is found at the commencement of the apodosis of a sentence, <ref='Act.11.17.'>Acts 11:17.</ref> It serves also to mark the resumption of an interrupte"}
- G1377: {"sense_head": "to pursue", "meaning_range": "to pursue, persecute, to systematically oppress and harass a person or group, as an extended meaning of pursuing a person on foot in a chase; also from the image of the chase comes the meaning of striving and pressing on to a goal with intensity: to press on; <b>to put in rapid motion; to pursue; to follow, pursue the direction of,</b> <ref='Luk.17.23'>Lk. 17:23</ref>; <b>to follow eagerly, endeavor earnestly to acquire,</b> <ref='Rom.9.30, 31; 12.13'>Rom. 9:30, 31; 12:13</ref>; <b>to press forw"}
- G3694: {"sense_head": "after", "meaning_range": "behind, after, following; can function as an <i>improper preposition</i>, <b>behind, after, at one's back,</b> <ref='Mat.4.10'>Mt. 4:10</ref>; <ref='Luk.7.38'>Lk. 7:38</ref>; <ref='Rev.1.10'>Rev. 1:10;</ref> <greek>τὰ ὀπισω</greek>, <b>the things which are behind,</b> <ref='Php.3.13'>Phil. 3:13;</ref> <greek>ὀπισω</greek> and <greek>εἰς τὰ ὀπισω</greek>, <b>back, backwards,</b> <ref='Mat.24.18'>Mt. 24:18</ref>; <ref='Mrk.13.16'>Mk. 13:16</ref>; <ref='Luk.9.62'>Lk. 9:62</ref>, when an <i>improper"}
- H0310A: {"sense_head": "after", "meaning_range": "1) after the following part, behind (of place), hinder, afterwards (of time); 1a) as an adverb; 1a1) behind (of place); 1a2) afterwards (of time); 1b) as a preposition; 1b1) behind, after (of place); 1b2) after (of time); 1b3) besides; 1c) as a conjunction; 1c) after that; 1d) as a substantive; 1d1) hinder part; 1e) with other prepositions; 1e1) from behind; 1e2) from following after"}
- H1692: {"sense_head": "to cleave", "meaning_range": "1) to cling, stick, stay close, cleave, keep close, stick to, stick with, follow closely, join to, overtake, catch; 1a) (Qal); 1a1) to cling, cleave to; 1a2) to stay with; 1b) (Pual) to be joined together; 1c) (Hiphil); 1c1) to cause to cleave to; 1c2) to pursue closely; 1c3) to overtake; 1d) (Hophal) to be made to cleave; Aramaic equivalent: <i>de.vaq</i> (דְּבֵק \"to cleave\" H1693)"}
- H1980N: {"sense_head": "follow/behind/go[after", "meaning_range": "1) to go, walk, come; 1a) (Qal); 1a1) to go, walk, come, depart, proceed, move, go away; 1a2) to die, live, manner of life (fig.); 1b) (Piel); 1b1) to walk; 1b2) to walk (fig.); 1c) (Hithpael); 1c1) to traverse; 1c2) to walk about; 1d) (Niphal) to lead, bring, lead away, carry, cause to walk"}
- H3807: {"sense_head": "to crush", "meaning_range": "1) to beat, crush by beating, crush to pieces, crush fine; 1a) (Qal); 1a1) to beat or crush fine; 1a2) to beat, hammer; 1b) (Piel); 1b1) to beat or crush fine; 1b2) to beat, hammer; 1c) (Pual) to be beaten; 1d) (Hiphil) to beat in pieces, shatter; 1e) (Hophal) to be beaten, be crushed"}
- H5921A: {"sense_head": "upon", "meaning_range": "prep; 1) upon, on the ground of, according to, on account of, on behalf of, concerning, beside, in addition to, together with, beyond, above, over, by, on to, towards, to, against; 1a) upon, on the ground of, on the basis of, on account of, because of, therefore, on behalf of, for the sake of, for, with, in spite of, notwithstanding, concerning, in the matter of, as regards; 1b) above, beyond, over (of excess); 1c) above, over (of elevation or pre-eminence); 1d) upon, to, over to, unto, in addit"}
- H7291: {"sense_head": "to pursue", "meaning_range": "1) to be behind, follow after, pursue, persecute, run after; 1a) (Qal); 1a1) to pursue, put to flight, chase, dog, attend closely upon; 1a2) to persecute, harass (fig); 1a3) to follow after, aim to secure (fig); 1a4) to run after (a bribe) (fig); 1b) (Niphal); 1b1) to be pursued; 1b2) one pursued (participle); 1c) (Piel) to pursue ardently, aim eagerly to secure, pursue; 1d) (Pual) to be pursued, be chased away; 1e) (Hiphil) to pursue, chase"}

## to_take_up

- observation: 24107
  stage: layer-1
  kind: group
  item: group-definition
  text: Chasing to overtake: running after a person, band or army to overtake, capture or strike them, in Gen 14:15, Exo 14:9, Jos 10:19, Judg 4:16, Judg 20:45, Num 14:45, 1Sa 30:8, 2Sa 2:19, 2Ki 25:5 and the many other battle and flight narratives.
  basis: read
  verses: ["Gen.35.5", "Exod.14.4", "Josh.8.16", "Josh.10.19", "2Sam.17.1", "2Sam.20.6", "2Sam.20.7", "2Sam.20.13", "Gen.14.15", "Gen.31.23", "Exod.14.8", "Exod.14.9"]
  covers: [980685, 992262, 992265, 1002313, 1007225, 1007226, 1017218, 1017219, 1025306, 1025307, 1026620, 1049373, 1072080, 1090121, 1090123, 1090124, 1090126, 1095124, 1095125, 1096187, 1096929, 1099532, 1099870, 1100649, 1100651, 1108076, 1108735, 1112827, 1112828, 1113262, 1113263, 1113438, 1114265, 1114294, 1114295, 1121272, 1127766, 1127777, 1129782, 1130463, 1133706, 1133770, 1134485, 1136445, 1140278, 1140280, 1143028, 1143029, 1146428, 1146430, 1148875, 1148876, 1149386, 1149387, 1149715, 1149716, 1149814, 1150573, 1150575, 1150647, 1150649, 1168621, 1176771, 1176772, 1185497, 1185498, 1201457, 1218034, 1218035, 1271714, 1343502, 1343503, 1344701, 1344702, 1387729]
- observation: 24108
  stage: layer-1
  kind: group
  item: group-definition
  text: Hounding to destroy: pursuit aimed at a person's life, standing or the weak, driven in some verses by desire or anger, in Exo 15:9, Deu 19:6, 1Sa 25:29, Psa 7:5, Psa 71:11, Psa 109:16, Psa 143:3, Job 19:22, Amo 1:11, Lam 3:43 and Rev 12:13.
  basis: read
  verses: ["Deut.19.6", "Amos.1.11", "Ps.143.3", "Ps.109.16", "Lam.3.43", "Exod.15.9", "1Sam.25.29", "Job.19.28", "Job.19.22", "Ps.71.11", "Ps.7.5", "Rev.12.13"]
  covers: [1005416, 1066140, 1066141, 1131980, 1237988, 1239904, 1254167, 1254311, 1255503, 1265931, 1346065, 1389447, 1389449, 1519119]
- observation: 24109
  stage: layer-1
  kind: group
  item: group-definition
  text: Pursuit by God or by what is not a person: God pursuing with tempest, sword or flood (Psa 83:15, Jer 29:18, Lam 3:66, Nah 1:8, Job 13:25), and curses, diseases, blood and the sword as pursuers (Deu 28:22, Deu 28:45, Eze 35:6, Jer 48:2), with honor chased off in Job 30:15.
  basis: read
  verses: ["Jer.48.2", "Job.13.25", "Ps.83.15", "Jer.29.18", "Lam.3.66", "Nah.1.8", "Deut.28.22", "Deut.28.45", "Ezek.35.6", "Job.30.15"]
  covers: [1072275, 1086236, 1236036, 1240364, 1267293, 1318794, 1318795, 1332622, 1346070, 1348324, 1348332, 1396159]
- observation: 24110
  stage: layer-1
  kind: group
  item: group-definition
  text: Pursuit of a good: going after righteousness, peace, love and the virtues as an aim, in Rom 9:30, Rom 9:31, Rom 14:19, 1Cor 14:1, 1Ti 6:11, 2Ti 2:22, 1Pe 3:11, Psa 34:14 and Isa 51:1.
  basis: read
  verses: ["Rom.9.31", "Rom.14.19", "1Cor.14.1", "1Tim.6.11", "2Tim.2.22", "1Pet.3.11", "Rom.9.30", "Ps.34.14", "Isa.51.1"]
  covers: [1265368, 1306545, 1478924, 1479773, 1479969, 1483275, 1499466, 1499467, 1500395, 1508465]
- observation: 24111
  stage: layer-1
  kind: group
  item: group-definition
  text: Going after a forbidden desire: the cities of Jude 7 going after other flesh, and the wife of Hos 2:7 chasing her lovers without reaching them.
  basis: read
  verses: ["Jude.1.7", "Hos.2.7"]
  covers: [1385716, 1512349, 1512350]
- observation: 24112
  stage: layer-1
  kind: enrichment
  item: strong-enrichment
  text: radaph (H7291) is to be behind and follow after, to chase and put to flight; achar (H0310A, after) marks the one chased as ahead; dabaq (H1692) adds keeping close and overtaking in Judg 20:45, and katat (H3807, to crush) in Num 14:45 adds the beating down the ESV renders as pursuit. The lexicon bears out the chase.
  basis: read
  verses: ["Gen.14.15", "Gen.35.5", "Gen.31.23", "Exod.14.4", "Exod.14.8", "Exod.14.9", "Exod.14.23", "Num.14.45", "Deut.11.4", "Josh.8.16", "Josh.10.19", "Josh.2.5"]
  covers: [980685, 992262, 992265, 1002313, 1007225, 1007226, 1017218, 1017219, 1025306, 1025307, 1026620, 1049373, 1072080, 1090121, 1090123, 1090124, 1090126, 1095124, 1095125, 1096187, 1096929, 1099532, 1099870, 1100649, 1100651, 1108076, 1108735, 1112827, 1112828, 1113262, 1113263, 1113438, 1114265, 1114294, 1114295, 1121272, 1127766, 1127777, 1129782, 1130463, 1133706, 1133770, 1134485, 1136445, 1140278, 1140280, 1143028, 1143029, 1146428, 1146430, 1148875, 1148876, 1149386, 1149387, 1149715, 1149716, 1149814, 1150573, 1150575, 1150647, 1150649, 1168621, 1176771, 1176772, 1185497, 1185498, 1201457, 1218034, 1218035, 1271714, 1343502, 1343503, 1344701, 1344702, 1387729]
- observation: 24113
  stage: layer-1
  kind: enrichment
  item: strong-enrichment
  text: radaph (H7291) has the figurative sense to persecute and harass, and dioko (G1377) the sense to oppress a person or group systematically, the dragon's pursuit in Rev 12:13; al (H5921A, upon) in Amo 1:11 is a preposition and adds no meaning. The lexicon bears out a hostile pursuit.
  basis: read
  verses: ["Exod.15.9", "Deut.19.6", "1Sam.25.29", "Job.19.28", "Job.19.22", "Ps.143.3", "Ps.109.16", "Ps.71.11", "Ps.7.5", "Lam.3.43", "Amos.1.11", "Rev.12.13"]
  covers: [1005416, 1066140, 1066141, 1131980, 1237988, 1239904, 1254167, 1254311, 1255503, 1265931, 1346065, 1389447, 1389449, 1519119]
- observation: 24114
  stage: layer-1
  kind: enrichment
  item: strong-enrichment
  text: radaph (H7291) carries no sense of its own for a pursuer that is God, a curse or blood; the lexicon gives the chase, and the verses Psa 83:15, Deu 28:45 and Eze 35:6 supply the pursuer. halak (H1980N) with achar in Jer 48:2 is to go after, given here to the sword.
  basis: read
  verses: ["Deut.28.22", "Deut.28.45", "Job.13.25", "Job.30.15", "Ps.83.15", "Jer.48.2", "Jer.29.18", "Lam.3.66", "Ezek.35.6", "Nah.1.8"]
  covers: [1072275, 1086236, 1236036, 1240364, 1267293, 1318794, 1318795, 1332622, 1346070, 1348324, 1348332, 1396159]
- observation: 24115
  stage: layer-1
  kind: enrichment
  item: strong-enrichment
  text: dioko (G1377) from the image of the chase has the sense of pressing on to a goal and following eagerly to acquire it, which Rom 14:19 and 1Ti 6:11 use; radaph (H7291) has the figurative sense to follow after and aim to secure, used in Psa 34:14 and Isa 51:1. de (G1161) is a particle and adds no meaning.
  basis: read
  verses: ["Ps.34.14", "Isa.51.1", "Rom.9.30", "Rom.9.31", "Rom.14.19", "1Cor.14.1", "1Tim.6.11", "2Tim.2.22", "1Pet.3.11"]
  covers: [1265368, 1306545, 1478924, 1479773, 1479969, 1483275, 1499466, 1499467, 1500395, 1508465]
- observation: 24116
  stage: layer-1
  kind: enrichment
  item: strong-enrichment
  text: aperchomai (G0565) is to go away or depart, and opiso (G3694, after) in Jude 7 turns the going away into a going after; radaph (H7291) in Hos 2:7 is the chase itself. The lexicon has no sense of desire in these codes; the desire is in the objects the verses name.
  basis: read
  verses: ["Hos.2.7", "Jude.1.7"]
  covers: [1385716, 1512349, 1512350]
- observation: 24117
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Gen 35:5, Exo 14:4, Deu 19:6, Jos 8:16, Jos 10:19, 2Sa 17:1, 2Sa 20:6, 2Sa 20:7 and 2Sa 20:13 the surface pursue stands on two codes at one place, radaph (H7291) and achar (H0310A, after): the verb and the word that marks the one chased as ahead.
  basis: read
  verses: ["Gen.35.5", "Exod.14.4", "Deut.19.6", "Josh.8.16", "Josh.10.19", "2Sam.17.1", "2Sam.20.6", "2Sam.20.7", "2Sam.20.13"]
  covers: [992262, 992265, 1007225, 1007226, 1066140, 1066141, 1090121, 1090123, 1095124, 1095125, 1140278, 1140280, 1143028, 1143029, 1150573, 1150575, 1150647, 1150649]
- observation: 24118
  stage: layer-2
  kind: face
  item: double-meaning
  text: In the other Hebrew verses of the row, among them Exo 15:9, Deu 28:45, Psa 34:14, Lam 3:66, Hos 2:7 and Nah 1:8, the surface pursue stands on radaph (H7291) alone, whether the object is a person, a good or the one God pursues.
  basis: read
  verses: ["Exod.15.9", "Deut.28.22", "Deut.28.45", "Josh.2.5", "1Sam.24.14", "1Sam.25.29", "1Sam.26.18", "1Sam.30.8", "2Sam.24.13", "Job.13.25", "Job.19.22", "Job.19.28"]
  covers: [1005416, 1072275, 1086236, 1096187, 1121272, 1127766, 1127777, 1129782, 1131980, 1136445, 1236036, 1237988, 1239904, 1255503, 1265368, 1265931, 1267293, 1306545, 1332622, 1346070, 1348324, 1348332, 1385716, 1387729, 1396159]
- observation: 24119
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Jer 48:2 the surface pursue stands on halak (H1980N, go) with achar (H0310A, after), not on radaph: the sword goes after Madmen.
  basis: read
  verses: ["Jer.48.2"]
  covers: [1318794, 1318795]
- observation: 24120
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Rom 9:30, Rom 14:19, 1Cor 14:1, 1Ti 6:11, 2Ti 2:22 and 1Pe 3:11 the surface pursue stands on dioko (G1377), and in 1Ti 6:11 also on de (G1161, but), the particle at the same place.
  basis: read
  verses: ["Rom.9.30", "Rom.14.19", "1Cor.14.1", "1Tim.6.11", "2Tim.2.22", "1Pet.3.11"]
  covers: [1478924, 1479969, 1483275, 1499466, 1499467, 1500395, 1508465]
- observation: 24121
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Exo 14:8, Exo 14:9, Jos 8:16, Judg 4:16, 2Sa 2:19, 2Ki 9:27, Jer 39:5 and the other verses where both stand, the surface pursued holds radaph (H7291) and achar (H0310A, after) at one place, the verb with the word that sets the one chased ahead.
  basis: read
  verses: ["Exod.14.8", "Exod.14.9", "Josh.8.16", "Josh.24.6", "Judg.1.6", "Judg.4.16", "Judg.8.12", "2Sam.2.19", "2Sam.2.24", "2Sam.2.28", "2Sam.20.10", "2Kgs.9.27"]
  covers: [1017218, 1017219, 1025306, 1025307, 1090124, 1090126, 1100649, 1100651, 1112827, 1112828, 1113262, 1113263, 1114294, 1114295, 1146428, 1146430, 1148875, 1148876, 1149386, 1149387, 1149715, 1149716, 1176771, 1176772, 1185497, 1185498, 1218034, 1218035, 1343502, 1343503, 1344701, 1344702]
- observation: 24122
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Amo 1:11 the surface pursued holds radaph (H7291) with al (H5921A, upon), so the brother Edom pursued stands as the one the pursuit comes upon.
  basis: read
  verses: ["Amos.1.11"]
  covers: [1389447, 1389449]
- observation: 24123
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Gen 14:15, Exo 14:23, Jos 8:24, 1Sa 30:10, Psa 18:37, Psa 109:16, Job 30:15 and the other verses of radaph alone, the surface pursued stands on radaph (H7291) with no second code.
  basis: read
  verses: ["Gen.14.15", "Gen.31.23", "Exod.14.23", "Deut.11.4", "Josh.2.7", "Josh.8.17", "Josh.8.24", "Judg.7.23", "Judg.7.25", "Judg.20.43", "1Sam.7.11", "1Sam.17.52"]
  covers: [980685, 1002313, 1026620, 1072080, 1096929, 1099532, 1099870, 1108076, 1108735, 1114265, 1130463, 1133706, 1133770, 1134485, 1149814, 1168621, 1201457, 1240364, 1254167, 1254311, 1271714, 1346065]
- observation: 24124
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Num 14:45 the surface pursued stands on katat (H3807, crush) and in Judg 20:45 on dabaq (H1692, keep close): neither is radaph, and the English gives both as pursuit.
  basis: read
  verses: ["Num.14.45", "Judg.20.45"]
  covers: [1049373, 1113438]
- observation: 24125
  stage: layer-2
  kind: face
  item: double-meaning
  text: In Rom 9:31 and Rev 12:13 the surface pursued stands on dioko (G1377), and in Jude 7 on aperchomai (G0565, go away) with opiso (G3694, after), a going away after unnatural desire.
  basis: read
  verses: ["Rom.9.31", "Jude.1.7", "Rev.12.13"]
  covers: [1479773, 1512349, 1512350, 1519119]
- observation: 24126
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In Gen 31:23, Exo 14:23, Jos 2:7, Jos 8:16, Jos 8:17, Judg 7:23, 1Sa 24:14, 2Sa 2:19, 2Sa 20:7 and the other verses where it stands, achar (H0310A, after, behind) follows the verb of pursuit and points to the one chased; it gives direction, not a grade.
  basis: read
  verses: ["Gen.31.23", "Exod.14.23", "Deut.11.4", "Josh.2.5", "Josh.2.7", "Josh.8.16", "Josh.8.17", "Judg.4.16", "Judg.7.23", "Judg.20.45", "1Sam.23.25", "1Sam.24.14"]
  covers: [1002313, 1026620, 1072080, 1090121, 1090123, 1090124, 1090126, 1096187, 1099532, 1099870, 1108076, 1113262, 1113263, 1113438, 1121272, 1127766, 1127777, 1129782, 1130463, 1149386, 1149387, 1150573, 1150575, 1150647, 1150649, 1332622]
- observation: 24127
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In Gen 35:5, 2Sa 2:28 and Rom 9:30 the negator reaches the pursuit itself: the cities did not pursue, Joab's men pursued Israel no more, and the nations did not pursue righteousness.
  basis: read
  verses: ["Gen.35.5", "2Sam.2.28", "Rom.9.30"]
  covers: [992262, 992265, 1148875, 1148876, 1478924]
- observation: 24128
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In Hos 2:7 and Rom 9:31 the negator reaches the outcome of the pursuit: the lovers are not overtaken or found, and Israel did not reach the law it pursued; in Hos 2:7 first, better, now and then belong to her turning back.
  basis: read
  verses: ["Hos.2.7", "Rom.9.31"]
  covers: [1385716, 1479773]
- observation: 24129
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In 2Sa 2:19, 2Sa 22:38, Psa 18:37, Lam 3:43 and Amo 1:11 the qualifier tells how the pursuit was carried on: not turning aside or back, without pity, and in Amo 1:11 with anger kept perpetually and forever, whose punishment is not revoked.
  basis: read
  verses: ["2Sam.22.38", "Ps.18.37", "Lam.3.43", "Amos.1.11", "2Sam.2.19"]
  covers: [1149814, 1271714, 1346065, 1389447, 1389449]
- observation: 24130
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In Psa 109:16 and Eze 35:6 a negated clause gives the reason for the pursuit or its punishment: he did not remember to show kindness, and you did not hate bloodshed; Eze 35:6 opens with an oath and 'therefore'.
  basis: read
  verses: ["Ps.109.16", "Ezek.35.6"]
  covers: [1254311, 1348324, 1348332]
- observation: 24131
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In Psa 109:16, Job 13:25, Jude 7 and Rev 12:13 the qualifier falls on what is pursued: the poor and needy, dry chaff, desire that is unnatural, and the woman who bore the male child.
  basis: read
  verses: ["Job.13.25", "Jude.1.7", "Rev.12.13", "Ps.109.16"]
  covers: [1236036, 1512349, 1512350, 1519119]
- observation: 24132
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In Psa 34:14, 1Pe 3:11, 2Ti 2:22 and Hos 8:3 evil and good, youthful and pure set the pursuit against what is turned from or fled: turning from evil and doing good, fleeing youthful passions with those of a pure heart, and the good Israel spurned.
  basis: read
  verses: ["Ps.34.14", "Hos.8.3", "2Tim.2.22", "1Pet.3.11"]
  covers: [1265368, 1387729, 1500395, 1508465]
- observation: 24133
  stage: layer-2
  kind: pairing
  item: qualifier
  text: In the other verses of the row, among them Gen 31:23, Deu 19:6, Jos 10:19, 1Sa 25:29, 2Sa 20:6, 2Ki 9:27, Jer 48:2 and 1Cor 14:1, the negators, adverbs and adjectives reach other words of the verse, a length of days, a place, a time, a second clause, and not the pursuit.
  basis: read
  verses: ["Exod.14.4", "Deut.19.6", "Deut.28.45", "Josh.10.19", "Judg.20.43", "1Sam.17.52", "1Sam.25.29", "2Sam.20.6", "2Sam.20.10", "2Sam.24.13", "2Kgs.9.27", "2Chr.14.13"]
  covers: [1007225, 1007226, 1066140, 1066141, 1086236, 1095124, 1095125, 1108735, 1131980, 1133770, 1136445, 1140278, 1140280, 1146428, 1146430, 1176771, 1176772, 1201457, 1239904, 1267293, 1318794, 1318795, 1483275]
- observation: 24134
  stage: layer-2
  kind: pairing
  item: entity
  text: In the battle and flight narratives (Gen 14:15, Jos 8:16, Judg 4:16, Judg 7:25, 1Sa 23:25, 2Sa 2:19, 2Sa 20:10, 2Ki 9:27, Jer 39:5 and the rest) both pursuer and pursued are named persons, peoples or bands: Pharaoh, Barak, David, Saul, Abner, Joab, Sheba, Jehu, Zedekiah, the men of Israel; in Rev 12:13 the one pursued is the woman.
  basis: stated
  verses: ["Gen.14.15", "Gen.35.5", "Exod.14.4", "Exod.14.8", "Exod.14.9", "Exod.14.23", "Josh.2.5", "Josh.2.7", "Josh.8.16", "Judg.1.6", "Judg.4.16", "Judg.7.23"]
  covers: [980685, 992262, 992265, 1007225, 1007226, 1017218, 1017219, 1025306, 1025307, 1026620, 1090121, 1090123, 1090124, 1090126, 1096187, 1099532, 1108076, 1108735, 1112827, 1112828, 1113262, 1113263, 1113438, 1114265, 1114294, 1114295, 1121272, 1127766, 1127777, 1130463, 1131980, 1133706, 1133770, 1134485, 1136445, 1140278, 1140280, 1143028, 1143029, 1146428, 1146430, 1148875, 1148876, 1149386, 1149387, 1149715, 1149716, 1150573, 1150575, 1150647, 1150649, 1168621, 1176771, 1176772, 1201457, 1218034, 1218035, 1343502, 1343503, 1344701, 1344702, 1499466, 1499467, 1519119]
- observation: 24135
  stage: layer-2
  kind: pairing
  item: entity
  text: God is named in many of the verses: as the one who pursues (Lam 3:66, Eze 35:6), who hardens Pharaoh's heart or sends terror (Exo 14:4, Gen 35:5), who is asked or gives the enemy over (1Sa 30:8, Jos 10:19), in whose likeness the friends pursue (Job 19:22), and as the Lord sought or called on (Isa 51:1, 2Ti 2:22).
  basis: stated
  verses: ["Deut.11.4", "Deut.28.22", "Deut.28.45", "Josh.10.19", "Job.19.22", "Ps.71.11", "Isa.51.1", "Lam.3.66", "Ezek.35.6", "Amos.1.11", "2Tim.2.22", "Gen.35.5"]
  covers: [1072080, 1072275, 1086236, 1095124, 1095125, 1239904, 1255503, 1306545, 1346070, 1348324, 1348332, 1389447, 1389449, 1500395]
- observation: 24136
  stage: layer-2
  kind: relation
  item: direction
  text: In Lam 3:66, Eze 35:6, Deu 28:22 and Deu 28:45 the pursuit runs from God, or from what he sends (diseases, curses, blood), toward a people or an enemy, to destroy or overtake them.
  basis: read
  verses: ["Deut.28.22", "Deut.28.45", "Lam.3.66", "Ezek.35.6"]
  covers: [1072275, 1086236, 1346070, 1348324, 1348332]
- observation: 24137
  stage: layer-2
  kind: relation
  item: direction
  text: In Isa 51:1, 1Ti 6:11 and 2Ti 2:22 the pursuit runs from a person toward a good, righteousness and the virtues, with the Lord named as the one sought or called on, and in 1Ti 6:11 and 2Ti 2:22 away from what is fled.
  basis: read
  verses: ["Isa.51.1", "1Tim.6.11", "2Tim.2.22"]
  covers: [1306545, 1499466, 1499467, 1500395]
- observation: 24138
  stage: layer-2
  kind: relation
  item: direction
  text: In 1Sa 25:29, Psa 71:11 and Job 19:22 the pursuit runs from enemies or friends toward a person's life, and God is named on the side of the one pursued or as the likeness of the pursuers.
  basis: read
  verses: ["1Sam.25.29", "Job.19.22", "Ps.71.11"]
  covers: [1131980, 1239904, 1255503]
- observation: 24139
  stage: layer-2
  kind: relation
  item: direction
  text: In the battle and flight narratives (Gen 14:15, Exo 14:9, Jos 8:16, Judg 4:16, 1Sa 23:25, 2Sa 2:19, 2Ki 9:27, Jer 39:5 and the rest) and in Amo 1:11 and Rev 12:13 the pursuit runs from one person or force toward another who flees, ahead of the pursuer.
  basis: read
  verses: ["Gen.14.15", "Gen.35.5", "Exod.14.4", "Exod.14.8", "Exod.14.9", "Exod.14.23", "Deut.11.4", "Josh.2.5", "Josh.2.7", "Josh.8.16", "Josh.10.19", "Judg.1.6"]
  covers: [980685, 992262, 992265, 1007225, 1007226, 1017218, 1017219, 1025306, 1025307, 1026620, 1072080, 1090121, 1090123, 1090124, 1090126, 1095124, 1095125, 1096187, 1099532, 1108076, 1108735, 1112827, 1112828, 1113262, 1113263, 1113438, 1114265, 1114294, 1114295, 1121272, 1127766, 1127777, 1130463, 1133706, 1133770, 1134485, 1136445, 1140278, 1140280, 1143028, 1143029, 1146428, 1146430, 1148875, 1148876, 1149386, 1149387, 1149715, 1149716, 1150573, 1150575, 1150647, 1150649, 1168621, 1176771, 1176772, 1201457, 1218034, 1218035, 1343502, 1343503, 1344701, 1344702, 1389447, 1389449, 1519119]
- observation: 24140
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Psa 143:3 'crushed' (H1792) follows the pursuit of the speaker's soul: the enemy who pursued has crushed his life to the ground.
  basis: stated
  verses: ["Ps.143.3"]
  covers: [1254167]
- observation: 24141
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Deu 19:6 'anger' (lev, H3824, the heart that is hot) is the state in which the avenger of blood pursues the manslayer, the reason the law gives for the cities of refuge.
  basis: stated
  verses: ["Deut.19.6"]
  covers: [1066140, 1066141]
- observation: 24142
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Lam 3:43 and Lam 3:66 'anger' (af, H0639G) is God's: he wrapped himself in anger and pursued Zion, and is asked to pursue the enemies in anger.
  basis: stated
  verses: ["Lam.3.43", "Lam.3.66"]
  covers: [1346065, 1346070]
- observation: 24143
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Amo 1:11 'anger' (H0639G) and 'wrath' (H5678) are Edom's toward his brother, torn and kept forever, beside the pursuit with the sword.
  basis: stated
  verses: ["Amos.1.11"]
  covers: [1389447, 1389449]
- observation: 24144
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 1Sa 30:8 'inquired' (H7592 with H0559) comes before the pursuit: David asks the Lord whether to pursue, and the answer commands it.
  basis: stated
  verses: ["1Sam.30.8"]
  covers: [1127766, 1127777]
- observation: 24145
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Rom 9:30 'faith' (pistis, G4102G) names the righteousness the nations reached without pursuing it, a righteousness by faith.
  basis: stated
  verses: ["Rom.9.30"]
  covers: [1478924]
- observation: 24146
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 1Ti 6:11 and 2Ti 2:22 'faith' (G4102G) is one of the goods named as objects of the command to pursue, beside righteousness and love.
  basis: stated
  verses: ["1Tim.6.11", "2Tim.2.22"]
  covers: [1499466, 1499467, 1500395]
- observation: 24147
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Eze 35:6 'prepare' (H6213H) is God's act that comes before the pursuit: he prepares Edom for blood, and then blood pursues.
  basis: stated
  verses: ["Ezek.35.6"]
  covers: [1348324, 1348332]
- observation: 24148
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Jos 8:16 and Judg 7:23 'called' (H2199, H6817) is the summoning of the people, which comes before and sets off the pursuit.
  basis: stated
  verses: ["Josh.8.16", "Judg.7.23"]
  covers: [1090121, 1090123, 1090124, 1090126, 1108076]
- observation: 24149
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 2Ti 2:22 'call on' (G1941) names the company in which the pursuit is made: people who call on the Lord with a heart that is pure.
  basis: stated
  verses: ["2Tim.2.22"]
  covers: [1500395]
- observation: 24150
  stage: layer-2
  kind: pairing
  item: pairing
  text: In Jer 29:18 'reproach' (H2781) is among what the people become among the nations after God pursues them with sword, famine and pestilence.
  basis: stated
  verses: ["Jer.29.18"]
  covers: [1332622]
- observation: 24151
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 2Sa 17:1 'choose' (H0977) is Ahithophel's selecting of twelve thousand men, the first step of the pursuit he proposes against David.
  basis: stated
  verses: ["2Sam.17.1"]
  covers: [1143028, 1143029]
- observation: 24152
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 2Sa 24:13 'decide' (H7200J) is put to David among three judgments, one of them fleeing while foes pursue.
  basis: stated
  verses: ["2Sam.24.13"]
  covers: [1136445]
- observation: 24153
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 2Ti 2:22 'pure' (G2513) qualifies the heart of those with whom the pursuit is to be made.
  basis: stated
  verses: ["2Tim.2.22"]
  covers: [1500395]
- observation: 24154
  stage: layer-2
  kind: pairing
  item: pairing
  text: In 2Sa 2:28 'fight' (H3898A with H5750) is stopped together with the pursuit at the trumpet: they pursued no more and fought no more.
  basis: stated
  verses: ["2Sam.2.28"]
  covers: [1148875, 1148876]
