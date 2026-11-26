# ReadEvidence -- boast / boastful -- step 2.1

## What to do

The evidence validation (B5) of one subgroup, after its sweep, the gate before 3.1: the code checks of its observations (shown in `code_checks`), and the reading of every evidence observation of the subgroup (its own of S1 to 2.1, and the older ones on its occurrences kept as evidence) for whether it is true, founded and coherent with the others. Inner being is not judged here; the two validations are never run together.

Read:
- Read the code checks first: a failing check names observations to repair (unmarked, no node, a word node missing a column without its reason, a trace to a deleted observation, two of one text, a B1 observation no sense traces, a sense the 2.1 observations on its occurrences do not trace, an older observation left open).
- Take one observation at a time (`observations`, in the order of the steps): its text, basis and grounds against its verses (`verses`) and the observations it traces. Is it true of those verses? Does it say more than they show? Does it contradict another observation of the subgroup?

Write:
- Fill `answer.observations`, one entry for each observation of the package: verdict true, with `why` (what in the verses and the data bears it out); or verdict repair, with `why` (what is wrong) and `actions`: the actions of the validation that repair it (cfg_setting validate.reading actions, each with its parameters, for example {"action": "restate", "oid": id, "new_text": ..., "checked": ..., "reason": ...}, or delete_neither, complete_node, add_trace).
- A repair is checked as it is written; an observation that cannot be made true is deleted with its reason.
- Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing written; correct the answer until it finds none, then -Action RecordEvidence -File <the answer file>, and ReadEvidence again until every evidence observation is read; the gate passes when all are read and the code checks pass.

## Refused when (by rule)

- DA-02: belongs to collection; the nodes do not carry the collections
- IB-07: is not marked evidence: an inner-being observation traces to evidence; an observation does not trace itself
- LR-01: is not closed (every row answered
- PC-01: is not a step of the layered reading; is not a live subgroup of; no live collection; has no live subgroup; cannot read ;  are required;  is required
- PC-02: answer (its `command` must be; is a list of {observation, action, reason; the answer holds no ; answered twice; a true observation takes no action; unknown parameter(s); a sheet is an object; missing parameter(s); this is not the answer of a read
- PC-03: is not an older live observation on the occurrences of this row; is not an open old observation of this subgroup; not an evidence observation of; a deferral names a live collection; has no matching live verse_lexical row; both must be different live observations;  is not an occurrence of ; is not a live observation; is not a live node; does not exist;  is not a ; merge names a live observation to keep; defer names a live collection
- PC-04: basis must be one of; role must be one of; route must be one of; tag must be one of; stage must be one of; nature must be one of; verdict is true or repair; cannot be modified (allowed:; not in live cfg_enum ib_observation; action is one of; names its marker, nature one of; is not an action of the validation
- PC-05: the evidence validation of ; has no open row; its group is retired or missing; has no evidence-validation row; carry names a LATER step of; the loop is for one subgroup at a time; partner collection 
- PC-06:  s, more than 
- PC-07: cfg_setting layer.reading is missing; cfg_setting layer.scan; layer.reading step ; (apply iba/app/migration/archive/; the code is ahead of the config; have no nature in cfg_setting layer.reading; the read names rule(s) not active; is empty: run install_nature; are not ib_observation.tag values;  is missing
- RW-01: needs its reason, in words; say in words what was checked; say what it states that the existing record does not; state the finding the collection is to close; say in words which words it relies on; say in words why the word supports no finding; is the last word node of observation; already holds that occurrence: drop the node instead; its occurrence is on no live node of; carry gives its reason in words
- RW-03: is already live as observation; the same text as; a merge is for the same description
- RW-04: is a bare negation with no actual content
- RW-13: are still open in the ledger; have no answer in fill.older; its fate is not recorded; is not in the change log of observation; the change log does not show it
- RW-14: the statement used more than
- VA-02: why says, in words,; a repair names the actions
- VA-03: name the carrying observations; the mapping is stated in words; occurrence(s) are on no node of; not carried needs its reason
- VA-04: only an observation that is neither is deleted here; repair those traces first
- VA-05: a deferred observation is marked now

## The rules

- VA-01 a-sheet-is-one-checked-transaction: A sheet of validation actions is checked whole (every action named, its parameters complete) and written in one transaction: any action the tables refuse refuses the whole sheet and nothing is kept. -Check runs every action and rolls back. Every change is kept in ib_observation_change with its reason (RW-01); nothing is physically deleted.
- VA-02 repair-first-and-every-finding-acted-on: A finding of the validation is repaired first: a wording that is untrue or stronger than its verse is restated and the restatement checked against the base data; a node missing a column is completed, or the reason the data cannot give it is recorded; a duplicate is consolidated; a node is deleted only when another live node carries its occurrence or it supports no finding of its observation. A finding is left open only when a named collection's validation will touch the observation: the deferral to that collection and the finding are recorded, and the check accepts it as deferred. A finding with no named owner is closed in the validation.
- VA-03 consumption-is-verified-before-deletion: An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- VA-04 neither-evidence-nor-inner-being-is-deleted: An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.
- VA-05 the-marker-follows-content-not-stage: Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being, based on evidence, a building block of the stage 5 claims. The marker (ib_observation.nature) follows the content and purpose of the observation, never its stage (RS-04): an observation of any stage may be inner being when it traces to evidence. One that states both is split. The marker is set when the observation is created, by the item that is answered (cfg_setting layer.reading items.<item>.nature); a finding file never sets it; the validation changes it only where the content shows the item's nature does not hold.
- VA-06 evidence-validation-gates-inner-being-validation: The validation runs in two layers, never concurrently: evidence first, then inner being. The inner-being layer is judged only when the evidence layer passes (every in-scope observation marked, none without a live node, no word node missing a required column without its reason, no live trace to a deleted observation, no two of one meaning). A later evidence change reopens only the inner-being rows it touches. In the build this gate is: step 3.1 does not open before the evidence layer passes, and step 3.3 does not close before both layers pass (cfg_setting layer.reading open_gate and closing_gate).
- RW-01 changed-only-by-reading: No observation is changed except by a reading, and every change is recorded with its reason. An observation no longer supported by the verse is soft-deleted, with the reason.
- RW-03 no-duplicates-multi-node: One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- RW-04 concise-verse-specific: Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- RW-06 resolved-fresh-on-evidence: Verse references are resolved fresh at write time, never taken from the text written. Relations are recorded only on evidence.
- RW-11 missing-is-named: Missing data in the base extract is named as a gap, never substituted from memory or outside knowledge.
- DA-02 a-node-per-occurrence-with-its-surfaces-collection: A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope (B:130), is not written and is listed.
- IB-07 inner-being-observations-trace-to-evidence: Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or on a live inner-being observation that itself traces to evidence (the trace chain of stage 4: a 3.2 behaviour traces the 3.1 elements it gathers, a 3.3 match the 3.1 and 3.2 observations it comes from; at most three links), unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed.
- LR-01 a-step-opens-on-gates-and-derives-its-ledger: A step of the layered reading opens only when the grouping is finished (every surface placed in a subgroup or isolated with its reason, every subgroup holding a surface) and the previous step is closed; with -Subgroup the needs and gates are judged for that subgroup alone (#2538). Step S1 is read after the grouping; step 1.1 needs step S1 closed: every word of the subgroup (surface and lettered Strong's code) answered and validated. Opening derives one ledger row for each aspect the data demands (cfg_setting layer.reading); an aspect the data no longer demands is retired, a new one is added, and a second open changes nothing.
- PC-01 the-command-names-a-live-unit: A read or record command names a live collection, a live subgroup of it where the read is by subgroup, and a step or item the layered reading knows. A command that names one that does not exist is refused and writes nothing.
- PC-02 the-answer-is-the-packet-form: An answer is the output form its read wrote: the `command` of that read; every entry an object, or a list, where the form has one; each field in its place with its type (a key unique in the answer, a text, a reason in words); each item answered once; and at least one entry where the form asks for entries. A file in another shape is refused whole and nothing is written.
- PC-03 names-are-those-the-packet-offers: Every ledger row, occurrence, observation, sense, node, verse and collection an answer names is one the packet offered for this unit, or a key the answer itself defines, and is live in the database. A name outside them is refused.
- PC-04 values-from-the-allowed-lists: Every coded value of an answer (kind, basis, item, part, role, route, mode, polarity, flag type, disposition, verdict, action, nature, stage, status) is one of the values the configuration allows for it (cfg_enum, cfg_setting layer.reading, reading.observation_items, validate.reading), as the packet lists them. Any other value is refused.
- PC-05 the-unit-is-at-its-step: A read or record runs only where the ledger has its unit at that step: the row open, or answered and not yet validated, and the steps before it closed (S1 before 1.1; the 2.1 rows before the sweep; the sweep before the evidence validation; its gate before 3.1; every subgroup through 3.1 before 3.2). Out of order it is refused, and the message names what comes first.
- PC-06 within-the-configured-limits: A read writes its packet within the time and size the configuration sets (cfg_setting layer.read_types: limits, package_max_chars, read_max_seconds). A read that would exceed them is refused, nothing is written, and the limit is named.
- PC-07 the-config-the-code-needs-is-present: The code of the reading runs only where the configuration it reads is in place (the settings, steps, items, natures, enums and rules it names). Where the code is ahead of the configuration, the command is refused and names what is missing.
- RW-13 older-observations-answered-at-record: Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- RW-14 every-lookup-is-pinpointed: A lookup of related data in the build or the validation is by an indexed column and takes a chunk of ids (cfg_setting layer.scan chunk); none runs once for each item of a list, and a statement that uses more work than layer.scan max_vm_ops is stopped and named, nothing written (lib/scanguard.py). The tests refuse a statement of the build whose query plan scans a table (layer.scan scan_ok lists the temporary tables a statement may scan).

## item

evidence-validation

## made

2026-11-26T15:09:02Z

## batch

- observations: 32
- left_after_this: 0
- evidence_in_scope: 32
- observations_in_scope: 34

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 23873; step: S1; item: word-sense; kind: term; text: In Rom 1:30 the noun (accusative plural) names a kind of person, the braggart, in the list of those God gave up to a debased mind, standing between haughty and inventors of evil; the ESV renders the noun as the adjective boastful.; basis: read; grounds: haughty, boastful, inventors of evil; traces: []; verses: ["Rom 1:30"]
- observation: 23874; step: S1; item: word-sense; kind: face; text: In 2Cor 11:17 the noun of boasting (genitive singular) qualifies the confidence Paul speaks with: it is a confidence of boasting, which he says he speaks as a fool and not as the Lord would. The ESV turns the genitive noun into the adjective boastful.; basis: read; grounds: with this boastful confidence; traces: []; verses: ["2Cor 11:17"]
- observation: 23875; step: S1; item: word-sense; kind: face; text: In Psa 5:5 and Psa 75:4 the participle (masculine plural) is a noun for a kind of person, rendered the boastful, under a code whose lexicon gives acting madly or foolishly: they shall not stand before the Lord's eyes, beside all evildoers (Psa 5:5), and they are told not to boast, beside the wicked told not to lift the horn (Psa 75:4).; basis: read; grounds: The boastful shall not stand; traces: []; verses: ["Psa 5:5", "Psa 75:4"]
- observation: 23876; step: S1; item: word-sense; kind: face; text: In Isa 10:12 the noun is height or haughtiness (construct, with eyes): the king of Assyria's eyes are lifted high, which the ESV renders as the boastful look in his eyes, set beside the speech of his arrogant heart; the Lord will punish both.; basis: read; grounds: the boastful look in his eyes; traces: []; verses: ["Isa 10:12"]
- observation: 23877; step: 1.1; item: group-definition; kind: group; text: The boastful as a kind of person: a noun or a participle used as a noun names those given to boasting, listed among the ungodly or set beside evildoers and the wicked (Rom 1:30, Psa 5:5, Psa 75:4).; basis: read; grounds: boaster, braggart; traces: [23873, 23875]; verses: ["Psa 5:5", "Psa 75:4", "Rom 1:30"]
- observation: 23878; step: 1.1; item: group-definition; kind: group; text: Boasting as the quality of an act or a look: the noun gives its character to something else, the confidence Paul speaks with (2Cor 11:17) and the height of the king of Assyria's eyes (Isa 10:12).; basis: read; grounds: haughtiness, height, elevation; traces: [23874, 23876]; verses: ["2Cor 11:17", "Isa 10:12"]
- observation: 23879; step: 1.2; item: strong-enrichment; kind: enrichment; text: The boastful as a kind of person is borne out by G0213 at Rom 1:30, boaster, braggart, whose older senses in LSJ are a wanderer and a charlatan or quack, one who claims more than he has. H1984C at Psa 5:5 and Psa 75:4 does not give boasting: its lexicon is acting madly, and the boastful rests there on the ESV's rendering, the related H1984H and H1984I being the codes of boasting.; basis: read; grounds: boaster, braggart; traces: [23877]; verses: ["Psa 5:5", "Psa 75:4", "Rom 1:30"]
- observation: 23880; step: 1.2; item: strong-enrichment; kind: enrichment; text: Boasting as a quality is borne out by G2746 at 2Cor 11:17, boasting, glorying in, which gives its character to the confidence named, and by H7312 at Isa 10:12, haughtiness, height, elevation, the height of the eyes; the Hebrew gives the look its height, the Greek gives the speech its boasting.; basis: read; grounds: haughtiness, height, elevation; traces: [23878]; verses: ["2Cor 11:17", "Isa 10:12"]
- observation: 23881; step: 2.1; item: double-meaning; kind: face; text: The surface boastful names persons in Rom 1:30 (G0213, a noun in a list of vices) and in Psa 5:5 and Psa 75:4 (H1984C, a participle used as a noun): the face of the word as a kind of person, standing first in Psa 5:5 and after say to in Psa 75:4.; basis: read; grounds: I say to the boastful; traces: [23877]; verses: ["Psa 5:5", "Psa 75:4", "Rom 1:30"]
- observation: 23882; step: 2.1; item: double-meaning; kind: face; text: In 2Cor 11:17 the surface boastful carries G2746, a genitive noun that stands right before confidence and gives it its character: the face of the word as a quality of speech.; basis: read; grounds: this boastful confidence; traces: [23878]; verses: ["2Cor 11:17"]
- observation: 23883; step: 2.1; item: double-meaning; kind: face; text: In Isa 10:12 the surface boastful carries H7312, height, in construct with look and his eyes: the face of the word as the height of a look, set after the speech of the arrogant heart.; basis: read; grounds: the boastful look in his eyes; traces: [23878]; verses: ["Isa 10:12"]
- observation: 23884; step: 2.1; item: qualifier; kind: pairing; text: In Psa 5:5 the negator not stands right after boastful and reaches stand, the verb of which the boastful are the subject; before, with your eyes, gives the place where they shall not stand.; basis: read; grounds: shall not stand before your eyes; traces: [23877]; verses: ["Psa 5:5"]
- observation: 23885; step: 2.1; item: qualifier; kind: pairing; text: In Psa 75:4 the boastful are the ones addressed after say to; the first not reaches the verb boast that follows, the second reaches lift up, said to the wicked: both negators fall on the acts, not on the word boastful.; basis: read; grounds: Do not lift up your horn; traces: [23877]; verses: ["Psa 75:4"]
- observation: 23886; step: 2.1; item: qualifier; kind: pairing; text: In Rom 1:30 boastful stands in a list of descriptors of the same persons, with slanderers, haters of God and haughty before it and inventors of evil and disobedient after it; the words qualify the persons side by side and none governs boastful.; basis: read; grounds: insolent, haughty, boastful, inventors of evil; traces: [23877]; verses: ["Rom 1:30"]
- observation: 23887; step: 2.1; item: qualifier; kind: pairing; text: In 2Cor 11:17 the negator not stands three words after boastful and reaches as the Lord would: it denies the manner of the saying, not the boasting confidence, which is then set as a fool's.; basis: read; grounds: I say not as the Lord would; traces: [23878]; verses: ["2Cor 11:17"]
- observation: 23888; step: 2.1; item: entity; kind: pairing; text: In 2Cor 11:17 the Lord is named five words after boastful, as the one whose way of speaking Paul's boasting confidence is not: the Lord stands as the measure the boast does not meet, set against the fool.; basis: read; grounds: not as the Lord would; traces: [23878]; verses: ["2Cor 11:17"]
- observation: 23889; step: 2.1; item: direction; kind: relation; text: In 2Cor 11:17 the direction runs from Paul, the speaker, to his hearers, and the Lord is named only as the standard of a way of saying: the boasting confidence goes out from Paul and is measured against how the Lord would speak, not addressed to him.; basis: read; grounds: What I am saying with this boastful confidence; traces: [23878]; verses: ["2Cor 11:17"]
- observation: 23890; step: 2.1; item: pairing; kind: pairing; text: In 2Cor 11:17 confidence (believe) stands right after boastful, which qualifies it as a genitive: the confidence is a confidence of boasting, the thing Paul speaks with.; basis: read; grounds: this boastful confidence; traces: [23878]; verses: ["2Cor 11:17"]
- observation: 23891; step: 2.1; item: pairing; kind: pairing; text: In Isa 10:12 punish (condemn) stands six words before boastful, with the Lord as subject: the boastful look of the king's eyes is one of the two objects the Lord will punish.; basis: read; grounds: he will punish the speech; traces: [23878]; verses: ["Isa 10:12"]
- observation: 23892; step: 2.1; item: pairing; kind: pairing; text: In Psa 5:5 and Psa 75:4 evildoers or the wicked (evildoer) stand in the parallel line with the boastful: the Lord hates all evildoers after the boastful shall not stand (Psa 5:5), and the wicked are told not to lift the horn after the boastful are told not to boast (Psa 75:4).; basis: read; grounds: you hate all evildoers; traces: [23877]; verses: ["Psa 5:5", "Psa 75:4"]
- observation: 23893; step: 2.1; item: pairing; kind: pairing; text: In Rom 1:30 evil (evildoer) stands two words after boastful, in inventors of evil, the next item of the same list of persons.; basis: read; grounds: boastful, inventors of evil; traces: [23877]; verses: ["Rom 1:30"]
- observation: 23894; step: 2.1; item: pairing; kind: pairing; text: In 2Cor 11:17 fool (folly) closes the verse, eight words after boastful: the boasting confidence is spoken as a fool, set against as the Lord would.; basis: read; grounds: but as a fool; traces: [23878]; verses: ["2Cor 11:17"]
- observation: 23895; step: 2.1; item: pairing; kind: pairing; text: In Isa 10:12 finished (fulfill) stands twelve words before boastful, in the time clause: when the Lord has finished his work on Zion, then comes the punishment of the boastful look; a word of time, not of the boast.; basis: read; grounds: When the Lord has finished all his work; traces: [23878]; verses: ["Isa 10:12"]
- observation: 23896; step: 2.1; item: pairing; kind: pairing; text: In Isa 10:12 heart (heart) stands three words before boastful, in the parallel object: the speech of the arrogant heart and the boastful look of the eyes are the two things of the king the Lord will punish, heart and eyes side by side.; basis: read; grounds: the speech of the arrogant heart; traces: [23878]; verses: ["Isa 10:12"]
- observation: 23897; step: 2.1; item: pairing; kind: pairing; text: In Isa 10:12 work (labor) stands ten words before boastful and is the Lord's work on Zion and Jerusalem, finished before the punishment; the work is the Lord's, not the king's.; basis: read; grounds: all his work on Mount Zion; traces: [23878]; verses: ["Isa 10:12"]
- observation: 23898; step: 2.1; item: pairing; kind: pairing; text: In Psa 5:5 hate (love) stands six words after the boastful, with the Lord as subject and all evildoers as object, in the line parallel to the boastful not standing before him.; basis: read; grounds: you hate all evildoers; traces: [23877]; verses: ["Psa 5:5"]
- observation: 23899; step: 2.1; item: pairing; kind: pairing; text: In Isa 10:12 arrogant (pride) stands four words before boastful, on the heart, in the parallel object: an arrogant heart and a boastful look are named together. The WordNet control pairs boastful with proud (similar), and the verse bears it out.; basis: read; grounds: the arrogant heart of the king; traces: [23878]; verses: ["Isa 10:12"]
- observation: 23900; step: 2.1; item: pairing; kind: pairing; text: In Rom 1:30 haughty (pride) stands right before boastful in the same list of persons, the two words side by side, as the WordNet pairing of boastful with proud has it.; basis: read; grounds: insolent, haughty, boastful; traces: [23877]; verses: ["Rom 1:30"]
- observation: 23901; step: 2.1; item: pairing; kind: pairing; text: In Rom 1:30 disobedient (rebel) stands three words after boastful, the last item of the list, with to parents: disobedience to parents is named among the same persons as the braggart.; basis: read; grounds: disobedient to parents; traces: [23877]; verses: ["Rom 1:30"]
- observation: 23902; step: 2.1; item: pairing; kind: pairing; text: In Rom 1:30 slanderers (scoff) opens the verse, four words before boastful, the first of the list in which the braggart stands.; basis: read; grounds: slanderers, haters of God; traces: [23877]; verses: ["Rom 1:30"]
- observation: 15116; step: older (prior-capture); item: null; kind: statement; text: It speaks of its own hand: The king of Assyria: "the speech of the arrogant heart of the king of Assyria and the boastful look in his eyes. For he says: 'By the strength of my hand I have done it, and by my wisdom, for I have understanding'" (Isa 10:12–13); In the same passage he is the Lord's rod (10:5, 15). I read: pride credits itself with what it was used for.; basis: read; grounds: null; traces: []; verses: ["Isa 10:12", "Isa 10:13"]
- observation: 15159; step: older (prior-capture); item: null; kind: statement; text: After not acknowledging God. "since they did not see fit to acknowledge God, God gave them up to a debased mind ... insolent, haughty, boastful" (Rom 1:28–30).; basis: stated; grounds: null; traces: []; verses: ["Rom 1:28", "Rom 1:30"]

## verses

- reference: Psa 5:5; text: The boastful shall not stand before your eyes; you hate all evildoers.
- reference: Rom 1:30; text: slanderers, haters of God, insolent, haughty, boastful, inventors of evil, disobedient to parents,
- reference: 2Cor 11:17; text: What I am saying with this boastful confidence, I say not as the Lord would but as a fool.
- reference: Psa 75:4; text: I say to the boastful, ‘Do not boast,’ and to the wicked, ‘Do not lift up your horn;
- reference: Isa 10:12; text: When the Lord has finished all his work on Mount Zion and on Jerusalem, he will punish the speech of the arrogant heart of the king of Assyria and the boastful look in his eyes.
- reference: Isa 10:13; text: For he says: “ By the strength of my hand I have done it, and by my wisdom, for I have understanding; I remove the boundaries of peoples, and plunder their treasures; like a bull I bring down those who sit on thrones.
- reference: Rom 1:28; text: And since they did not see fit to acknowledge God, God gave them up to a debased mind to do what ought not to be done.

## measured

- package_chars: 33222
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "boast",
 "subgroup": "boastful",
 "observations": [
  {
   "observation": 23873,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23874,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23875,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23876,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23877,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23878,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23879,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23880,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23881,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23882,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23883,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23884,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23885,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23886,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23887,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23888,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23889,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23890,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23891,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23892,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23893,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23894,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23895,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23896,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23897,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23898,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23899,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23900,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23901,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23902,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 15116,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 15159,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ]
}
```
