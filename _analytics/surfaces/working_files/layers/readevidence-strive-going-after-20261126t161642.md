# ReadEvidence -- strive / going after -- step 2.1

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

## Limits

- grounds and every reason: characters at least: 10
- observation text: characters at least: 40
- consecutive verse words a text may copy, at most: 7

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

2026-11-26T16:16:42Z

## batch

- observations: 40
- left_after_this: 78
- evidence_in_scope: 158
- observations_in_scope: 158

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 24126
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Gen 31:23, Exo 14:23, Jos 2:7, Jos 8:16, Jos 8:17, Judg 7:23, 1Sa 24:14, 2Sa 2:19, 2Sa 20:7 and the other verses where it stands, achar (H0310A, after, behind) follows the verb of pursuit and points to the one chased; it gives direction, not a grade.
  basis: read
  grounds: pursued after them on the way
  traces: [24107, 24109]
  verses: ["1Sa 23:25", "1Sa 24:14", "1Sa 26:18", "1Sa 30:8", "2Sa 20:13", "2Sa 20:7", "2Sa 2:19", "Deu 11:4", "Exo 14:23", "Gen 31:23", "Jer 29:18", "Jos 2:5", "Jos 2:7", "Jos 8:16", "Jos 8:17", "Judg 20:45", "Judg 4:16", "Judg 7:23"]
- observation: 24127
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Gen 35:5, 2Sa 2:28 and Rom 9:30 the negator reaches the pursuit itself: the cities did not pursue, Joab's men pursued Israel no more, and the nations did not pursue righteousness.
  basis: read
  grounds: pursued Israel no more
  traces: [24107, 24110]
  verses: ["2Sa 2:28", "Gen 35:5", "Rom 9:30"]
- observation: 24128
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Hos 2:7 and Rom 9:31 the negator reaches the outcome of the pursuit: the lovers are not overtaken or found, and Israel did not reach the law it pursued; in Hos 2:7 first, better, now and then belong to her turning back.
  basis: read
  grounds: She shall pursue her lovers but not overtake them
  traces: [24110, 24111]
  verses: ["Hos 2:7", "Rom 9:31"]
- observation: 24129
  step: 2.1
  item: qualifier
  kind: pairing
  text: In 2Sa 2:19, 2Sa 22:38, Psa 18:37, Lam 3:43 and Amo 1:11 the qualifier tells how the pursuit was carried on: not turning aside or back, without pity, and in Amo 1:11 with anger kept perpetually and forever, whose punishment is not revoked.
  basis: read
  grounds: did not turn back until they were consumed
  traces: [24107, 24108]
  verses: ["2Sa 22:38", "2Sa 2:19", "Amo 1:11", "Lam 3:43", "Psa 18:37"]
- observation: 24130
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Psa 109:16 and Eze 35:6 a negated clause gives the reason for the pursuit or its punishment: he did not remember to show kindness, and you did not hate bloodshed; Eze 35:6 opens with an oath and 'therefore'.
  basis: read
  grounds: he did not remember to show kindness
  traces: [24108, 24109]
  verses: ["Eze 35:6", "Psa 109:16"]
- observation: 24131
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Psa 109:16, Job 13:25, Jude 7 and Rev 12:13 the qualifier falls on what is pursued: the poor and needy, dry chaff, desire that is unnatural, and the woman who bore the male child.
  basis: read
  grounds: pursued the poor and needy
  traces: [24108, 24109, 24111]
  verses: ["Job 13:25", "Jude 7", "Psa 109:16", "Rev 12:13"]
- observation: 24132
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Psa 34:14, 1Pe 3:11, 2Ti 2:22 and Hos 8:3 evil and good, youthful and pure set the pursuit against what is turned from or fled: turning from evil and doing good, fleeing youthful passions with those of a pure heart, and the good Israel spurned.
  basis: read
  grounds: Turn away from evil and do good
  traces: [24107, 24110]
  verses: ["1Pe 3:11", "2Ti 2:22", "Hos 8:3", "Psa 34:14"]
- observation: 24133
  step: 2.1
  item: qualifier
  kind: pairing
  text: In the other verses of the row, among them Gen 31:23, Deu 19:6, Jos 10:19, 1Sa 25:29, 2Sa 20:6, 2Ki 9:27, Jer 48:2 and 1Cor 14:1, the negators, adverbs and adjectives reach other words of the verse, a length of days, a place, a time, a second clause, and not the pursuit.
  basis: read
  grounds: for seven days and followed close after him
  traces: [24107, 24108, 24109, 24110]
  verses: ["1Cor 14:1", "1Sa 17:52", "1Sa 25:29", "2Ch 14:13", "2Ki 9:27", "2Sa 20:10", "2Sa 20:6", "2Sa 24:13", "Deu 19:6", "Deu 28:45", "Exo 14:4", "Gen 31:23", "Jer 29:18", "Jer 48:2", "Job 19:22", "Jos 10:19", "Jos 2:5", "Jos 8:17", "Jude 7", "Judg 20:43", "Judg 4:16", "Psa 83:15"]
- observation: 24134
  step: 2.1
  item: entity
  kind: pairing
  text: In the battle and flight narratives (Gen 14:15, Jos 8:16, Judg 4:16, Judg 7:25, 1Sa 23:25, 2Sa 2:19, 2Sa 20:10, 2Ki 9:27, Jer 39:5 and the rest) both pursuer and pursued are named persons, peoples or bands: Pharaoh, Barak, David, Saul, Abner, Joab, Sheba, Jehu, Zedekiah, the men of Israel; in Rev 12:13 the one pursued is the woman.
  basis: stated
  grounds: And Asahel pursued Abner
  traces: [24107, 24108, 24110]
  verses: ["1Ki 20:20", "1Sa 17:52", "1Sa 23:25", "1Sa 25:29", "1Sa 26:18", "1Sa 30:10", "1Sa 30:8", "1Sa 7:11", "1Ti 6:11", "2Ch 13:19", "2Ch 14:13", "2Ki 9:27", "2Sa 17:1", "2Sa 20:10", "2Sa 20:13", "2Sa 20:6", "2Sa 20:7", "2Sa 24:13", "2Sa 2:19", "2Sa 2:24", "2Sa 2:28", "Exo 14:23", "Exo 14:4", "Exo 14:8", "Exo 14:9", "Gen 14:15", "Gen 35:5", "Jer 39:5", "Jer 52:8", "Jos 2:5", "Jos 2:7", "Jos 8:16", "Judg 1:6", "Judg 20:43", "Judg 20:45", "Judg 4:16", "Judg 7:23", "Judg 7:25", "Judg 8:12", "Rev 12:13"]
- observation: 24135
  step: 2.1
  item: entity
  kind: pairing
  text: God is named in many of the verses: as the one who pursues (Lam 3:66, Eze 35:6), who hardens Pharaoh's heart or sends terror (Exo 14:4, Gen 35:5), who is asked or gives the enemy over (1Sa 30:8, Jos 10:19), in whose likeness the friends pursue (Job 19:22), and as the Lord sought or called on (Isa 51:1, 2Ti 2:22).
  basis: stated
  grounds: you who seek the Lord
  traces: [24107, 24108, 24109, 24110]
  verses: ["1Sa 25:29", "1Sa 30:8", "1Ti 6:11", "2Ch 14:13", "2Ti 2:22", "Amo 1:11", "Deu 11:4", "Deu 28:22", "Deu 28:45", "Exo 14:4", "Exo 14:8", "Eze 35:6", "Gen 35:5", "Isa 51:1", "Job 19:22", "Jos 10:19", "Lam 3:66", "Psa 71:11"]
- observation: 24136
  step: 2.1
  item: direction
  kind: relation
  text: In Lam 3:66, Eze 35:6, Deu 28:22 and Deu 28:45 the pursuit runs from God, or from what he sends (diseases, curses, blood), toward a people or an enemy, to destroy or overtake them.
  basis: read
  grounds: You will pursue them in anger
  traces: [24109]
  verses: ["Deu 28:22", "Deu 28:45", "Eze 35:6", "Lam 3:66"]
- observation: 24137
  step: 2.1
  item: direction
  kind: relation
  text: In Isa 51:1, 1Ti 6:11 and 2Ti 2:22 the pursuit runs from a person toward a good, righteousness and the virtues, with the Lord named as the one sought or called on, and in 1Ti 6:11 and 2Ti 2:22 away from what is fled.
  basis: read
  grounds: flee youthful passions and pursue righteousness
  traces: [24110]
  verses: ["1Ti 6:11", "2Ti 2:22", "Isa 51:1"]
- observation: 24138
  step: 2.1
  item: direction
  kind: relation
  text: In 1Sa 25:29, Psa 71:11 and Job 19:22 the pursuit runs from enemies or friends toward a person's life, and God is named on the side of the one pursued or as the likeness of the pursuers.
  basis: read
  grounds: Why do you, like God, pursue me
  traces: [24108]
  verses: ["1Sa 25:29", "Job 19:22", "Psa 71:11"]
- observation: 24139
  step: 2.1
  item: direction
  kind: relation
  text: In the battle and flight narratives (Gen 14:15, Exo 14:9, Jos 8:16, Judg 4:16, 1Sa 23:25, 2Sa 2:19, 2Ki 9:27, Jer 39:5 and the rest) and in Amo 1:11 and Rev 12:13 the pursuit runs from one person or force toward another who flees, ahead of the pursuer.
  basis: read
  grounds: And Asahel pursued Abner
  traces: [24107, 24108]
  verses: ["1Ki 20:20", "1Sa 17:52", "1Sa 23:25", "1Sa 26:18", "1Sa 30:10", "1Sa 30:8", "1Sa 7:11", "2Ch 13:19", "2Ch 14:13", "2Ki 9:27", "2Sa 17:1", "2Sa 20:10", "2Sa 20:13", "2Sa 20:6", "2Sa 20:7", "2Sa 24:13", "2Sa 2:19", "2Sa 2:24", "2Sa 2:28", "Amo 1:11", "Deu 11:4", "Exo 14:23", "Exo 14:4", "Exo 14:8", "Exo 14:9", "Gen 14:15", "Gen 35:5", "Jer 39:5", "Jer 52:8", "Jos 10:19", "Jos 2:5", "Jos 2:7", "Jos 8:16", "Judg 1:6", "Judg 20:43", "Judg 20:45", "Judg 4:16", "Judg 7:23", "Judg 7:25", "Judg 8:12", "Rev 12:13"]
- observation: 24140
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 143:3 'crushed' (H1792) follows the pursuit of the speaker's soul: the enemy who pursued has crushed his life to the ground.
  basis: stated
  grounds: he has crushed my life to the ground
  traces: [24108]
  verses: ["Psa 143:3"]
- observation: 24141
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 19:6 'anger' (lev, H3824, the heart that is hot) is the state in which the avenger of blood pursues the manslayer, the reason the law gives for the cities of refuge.
  basis: stated
  grounds: the avenger of blood in hot anger
  traces: [24108]
  verses: ["Deu 19:6"]
- observation: 24142
  step: 2.1
  item: pairing
  kind: pairing
  text: In Lam 3:43 and Lam 3:66 'anger' (af, H0639G) is God's: he wrapped himself in anger and pursued Zion, and is asked to pursue the enemies in anger.
  basis: stated
  grounds: You will pursue them in anger
  traces: [24108, 24109]
  verses: ["Lam 3:43", "Lam 3:66"]
- observation: 24143
  step: 2.1
  item: pairing
  kind: pairing
  text: In Amo 1:11 'anger' (H0639G) and 'wrath' (H5678) are Edom's toward his brother, torn and kept forever, beside the pursuit with the sword.
  basis: stated
  grounds: his anger tore perpetually
  traces: [24108]
  verses: ["Amo 1:11"]
- observation: 24144
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 30:8 'inquired' (H7592 with H0559) comes before the pursuit: David asks the Lord whether to pursue, and the answer commands it.
  basis: stated
  grounds: Shall I pursue after this band
  traces: [24107]
  verses: ["1Sa 30:8"]
- observation: 24145
  step: 2.1
  item: pairing
  kind: pairing
  text: In Rom 9:30 'faith' (pistis, G4102G) names the righteousness the nations reached without pursuing it, a righteousness by faith.
  basis: stated
  grounds: a righteousness that is by faith
  traces: [24110]
  verses: ["Rom 9:30"]
- observation: 24146
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 6:11 and 2Ti 2:22 'faith' (G4102G) is one of the goods named as objects of the command to pursue, beside righteousness and love.
  basis: stated
  grounds: pursue righteousness, faith, love, and peace
  traces: [24110]
  verses: ["1Ti 6:11", "2Ti 2:22"]
- observation: 24147
  step: 2.1
  item: pairing
  kind: pairing
  text: In Eze 35:6 'prepare' (H6213H) is God's act that comes before the pursuit: he prepares Edom for blood, and then blood pursues.
  basis: stated
  grounds: I will prepare you for blood
  traces: [24109]
  verses: ["Eze 35:6"]
- observation: 24148
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 8:16 and Judg 7:23 'called' (H2199, H6817) is the summoning of the people, which comes before and sets off the pursuit.
  basis: stated
  grounds: were called together to pursue them
  traces: [24107]
  verses: ["Jos 8:16", "Judg 7:23"]
- observation: 24149
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Ti 2:22 'call on' (G1941) names the company in which the pursuit is made: people who call on the Lord with a heart that is pure.
  basis: stated
  grounds: those who call on the Lord
  traces: [24110]
  verses: ["2Ti 2:22"]
- observation: 24150
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jer 29:18 'reproach' (H2781) is among what the people become among the nations after God pursues them with sword, famine and pestilence.
  basis: stated
  grounds: a hissing, and a reproach
  traces: [24109]
  verses: ["Jer 29:18"]
- observation: 24151
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 17:1 'choose' (H0977) is Ahithophel's selecting of twelve thousand men, the first step of the pursuit he proposes against David.
  basis: stated
  grounds: Let me choose twelve thousand men
  traces: [24107]
  verses: ["2Sa 17:1"]
- observation: 24152
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 24:13 'decide' (H7200J) is put to David among three judgments, one of them fleeing while foes pursue.
  basis: stated
  grounds: Now consider, and decide what answer
  traces: [24107]
  verses: ["2Sa 24:13"]
- observation: 24153
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Ti 2:22 'pure' (G2513) qualifies the heart of those with whom the pursuit is to be made.
  basis: stated
  grounds: from a pure heart
  traces: [24110]
  verses: ["2Ti 2:22"]
- observation: 24154
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 2:28 'fight' (H3898A with H5750) is stopped together with the pursuit at the trumpet: they pursued no more and fought no more.
  basis: stated
  grounds: nor did they fight anymore
  traces: [24107]
  verses: ["2Sa 2:28"]
- observation: 24155
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 28:45 'commanded' (H6680) belongs to the commandments not kept, the reason the curses pursue and overtake.
  basis: stated
  grounds: that he commanded you
  traces: [24109]
  verses: ["Deu 28:45"]
- observation: 24156
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 109:16, Lam 3:43 and Amo 1:11 kindness or pity (H2617A, H2550, H7356B) is withheld from the one pursued: no kindness remembered, killing without pity, pity cast off.
  basis: stated
  grounds: killing without pity
  traces: [24108]
  verses: ["Amo 1:11", "Lam 3:43", "Psa 109:16"]
- observation: 24157
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 6:11 'gentleness' (G4239) is the last of the goods the man of God is told to pursue.
  basis: stated
  grounds: steadfastness, gentleness
  traces: [24110]
  verses: ["1Ti 6:11"]
- observation: 24158
  step: 2.1
  item: pairing
  kind: pairing
  text: In Job 13:25 'driven' (H5086) describes the leaf, and in Jer 29:18 'driven' (H5080 with H0834A) names the nations where God has scattered the people he pursues.
  basis: stated
  grounds: where I have driven them
  traces: [24109]
  verses: ["Jer 29:18", "Job 13:25"]
- observation: 24159
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jer 39:5 'sentence' (H4941G with H0854) is passed on Zedekiah after he was pursued and overtaken.
  basis: stated
  grounds: he passed sentence on him
  traces: [24107]
  verses: ["Jer 39:5"]
- observation: 24160
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jude 7 'eternal' (G0166) qualifies the fire of the punishment that follows going after unnatural desire.
  basis: stated
  grounds: a punishment of eternal fire
  traces: [24111]
  verses: ["Jude 7"]
- observation: 24161
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 28:45 'obey' (H8085H) is negated: not obeying the voice of the Lord is the reason the curses pursue.
  basis: stated
  grounds: you did not obey the voice
  traces: [24109]
  verses: ["Deu 28:45"]
- observation: 24162
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 28:22 'strike' (H5221) is the Lord's striking with disease, the things that then pursue until they perish.
  basis: stated
  grounds: The Lord will strike you
  traces: [24109]
  verses: ["Deu 28:22"]
- observation: 24163
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 15:9 'desire' (nephesh, H5315L) is the enemy's, which is to have its fill of them: it stands in the same boast as I will pursue and overtake.
  basis: stated
  grounds: my desire shall have its fill of them
  traces: [24108]
  verses: ["Exo 15:9"]
- observation: 24164
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Cor 14:1 'earnestly desire' (zeloo, G2206) is the second command after 'Pursue love', with the spiritual gifts as its object.
  basis: stated
  grounds: earnestly desire the spiritual gifts
  traces: [24110]
  verses: ["1Cor 14:1"]
- observation: 24165
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Ti 2:22 'passions' (G1939) are the youthful ones to be fled, set against what is to be pursued.
  basis: stated
  grounds: flee youthful passions
  traces: [24110]
  verses: ["2Ti 2:22"]

## verses

- reference: Deu 19:6
  text: lest the avenger of blood in hot anger pursue the manslayer and overtake him, because the way is long, and strike him fatally, though the man did not deserve to die, since he had not hated his neighbor in the past.
- reference: Eze 35:6
  text: therefore, as I live, declares the Lord God, I will prepare you for blood, and blood shall pursue you; because you did not hate bloodshed, therefore blood shall pursue you.
- reference: Lam 3:43
  text: “You have wrapped yourself with anger and pursued us, killing without pity;
- reference: Lam 3:66
  text: You will pursue them in anger and destroy them from under your heavens, O Lord.”
- reference: Amo 1:11
  text: Thus says the Lord: “For three transgressions of Edom, and for four, I will not revoke the punishment, because he pursued his brother with the sword and cast off all pity, and his anger tore perpetually, and he kept his wrath forever.
- reference: 2Sa 24:13
  text: So Gad came to David and told him, and said to him, “Shall three years of famine come to you in your land? Or will you flee three months before your foes while they pursue you? Or shall there be three days ’ pestilence in your land? Now consider, and decide what answer I shall return to him who sent me.”
- reference: Jer 48:2
  text: the renown of Moab is no more. In Heshbon they planned disaster against her: ‘ Come, let us cut her off from being a nation!’ You also, O Madmen, shall be brought to silence; the sword shall pursue you.
- reference: Exo 15:9
  text: The enemy said, ‘I will pursue, I will overtake, I will divide the spoil, my desire shall have its fill of them. I will draw my sword; my hand shall destroy them.’
- reference: Job 13:25
  text: Will you frighten a driven leaf and pursue dry chaff?
- reference: Exo 14:4
  text: And I will harden Pharaoh’s heart, and he will pursue them, and I will get glory over Pharaoh and all his host, and the Egyptians shall know that I am the Lord.” And they did so.
- reference: 2Ch 14:13
  text: Asa and the people who were with him pursued them as far as Gerar, and the Ethiopians fell until none remained alive, for they were broken before the Lord and his army. The men of Judah carried away very much spoil.
- reference: Gen 14:15
  text: And he divided his forces against them by night, he and his servants, and defeated them and pursued them to Hobah, north of Damascus.
- reference: 1Sa 26:18
  text: And he said, “ Why does my lord pursue after his servant? For what have I done? What evil is on my hands?
- reference: 2Sa 20:6
  text: And David said to Abishai, “ Now Sheba the son of Bichri will do us more harm than Absalom. Take your lord’s servants and pursue him, lest he get himself to fortified cities and escape from us.”
- reference: Deu 11:4
  text: and what he did to the army of Egypt, to their horses and to their chariots, how he made the water of the Red Sea flow over them as they pursued after you, and how the Lord has destroyed them to this day,
- reference: Deu 28:22
  text: The Lord will strike you with wasting disease and with fever, inflammation and fiery heat, and with drought and with blight and with mildew. They shall pursue you until you perish.
- reference: Psa 143:3
  text: For the enemy has pursued my soul; he has crushed my life to the ground; he has made me sit in darkness like those long dead.
- reference: Psa 109:16
  text: For he did not remember to show kindness, but pursued the poor and needy and the brokenhearted, to put them to death.
- reference: Jos 8:16
  text: So all the people who were in the city were called together to pursue them, and as they pursued Joshua they were drawn away from the city.
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
- reference: 1Sa 30:8
  text: And David inquired of the Lord, “Shall I pursue after this band? Shall I overtake them?” He answered him, “ Pursue, for you shall surely overtake and shall surely rescue.”
- reference: 2Sa 17:1
  text: Moreover, Ahithophel said to Absalom, “ Let me choose twelve thousand men, and I will arise and pursue David tonight.
- reference: 2Ki 9:27
  text: When Ahaziah the king of Judah saw this, he fled in the direction of Beth-haggan. And Jehu pursued him and said, “ Shoot him also.” And they shot him in the chariot at the ascent of Gur, which is by Ibleam. And he fled to Megiddo and died there.
- reference: Psa 71:11
  text: and say, “ God has forsaken him; pursue and seize him, for there is none to deliver him.”
- reference: Hos 2:7
  text: She shall pursue her lovers but not overtake them, and she shall seek them but shall not find them. Then she shall say, ‘I will go and return to my first husband, for it was better for me then than now.’
- reference: Jer 29:18
  text: I will pursue them with sword, famine, and pestilence, and will make them a horror to all the kingdoms of the earth, to be a curse, a terror, a hissing, and a reproach among all the nations where I have driven them,
- reference: Judg 7:23
  text: And the men of Israel were called out from Naphtali and from Asher and from all Manasseh, and they pursued after Midian.
- reference: Judg 20:43
  text: Surrounding the Benjaminites, they pursued them and trod them down from Nohah as far as opposite Gibeah on the east.
- reference: Gen 35:5
  text: And as they journeyed, a terror from God fell upon the cities that were around them, so that they did not pursue the sons of Jacob.
- reference: Jude 7
  text: just as Sodom and Gomorrah and the surrounding cities, which likewise indulged in sexual immorality and pursued unnatural desire, serve as an example by undergoing a punishment of eternal fire.
- reference: 1Sa 24:14
  text: After whom has the king of Israel come out? After whom do you pursue? After a dead dog! After a flea!
- reference: 2Sa 20:10
  text: But Amasa did not observe the sword that was in Joab’s hand. So Joab struck him with it in the stomach and spilled his entrails to the ground without striking a second blow, and he died. Then Joab and Abishai his brother pursued Sheba the son of Bichri.
- reference: Job 19:22
  text: Why do you, like God, pursue me? Why are you not satisfied with my flesh?
- reference: 1Sa 23:25
  text: And Saul and his men went to seek him. And David was told, so he went down to the rock and lived in the wilderness of Maon. And when Saul heard that, he pursued after David in the wilderness of Maon.
- reference: Isa 51:1
  text: “ Listen to me, you who pursue righteousness, you who seek the Lord: look to the rock from which you were hewn, and to the quarry from which you were dug.
- reference: Exo 14:8
  text: And the Lord hardened the heart of Pharaoh king of Egypt, and he pursued the people of Israel while the people of Israel were going out defiantly.
- reference: 1Cor 14:1
  text: Pursue love, and earnestly desire the spiritual gifts, especially that you may prophesy.
- reference: Jos 10:19
  text: but do not stay there yourselves. Pursue your enemies; attack their rear guard. Do not let them enter their cities, for the Lord your God has given them into your hand.”
- reference: 1Pe 3:11
  text: let him turn away from evil and do good; let him seek peace and pursue it.
- reference: 1Sa 25:29
  text: If men rise up to pursue you and to seek your life, the life of my lord shall be bound in the bundle of the living in the care of the Lord your God. And the lives of your enemies he shall sling out as from the hollow of a sling.
- reference: Psa 34:14
  text: Turn away from evil and do good; seek peace and pursue it.
- reference: Jos 2:5
  text: And when the gate was about to be closed at dark, the men went out. I do not know where the men went. Pursue them quickly, for you will overtake them.”
- reference: Psa 83:15
  text: so may you pursue them with your tempest and terrify them with your hurricane!
- reference: 1Ti 6:11
  text: But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.
- reference: 1Sa 30:10
  text: But David pursued, he and four hundred men. Two hundred stayed behind, who were too exhausted to cross the brook Besor.
- reference: 2Sa 2:28
  text: So Joab blew the trumpet, and all the men stopped and pursued Israel no more, nor did they fight anymore.
- reference: 1Sa 17:52
  text: And the men of Israel and Judah rose with a shout and pursued the Philistines as far as Gath and the gates of Ekron, so that the wounded Philistines fell on the way from Shaaraim as far as Gath and Ekron.
- reference: Rom 9:30
  text: What shall we say, then? That Gentiles who did not pursue righteousness have attained it, that is, a righteousness that is by faith;
- reference: Judg 8:12
  text: And Zebah and Zalmunna fled, and he pursued them and captured the two kings of Midian, Zebah and Zalmunna, and he threw all the army into a panic.
- reference: Hos 8:3
  text: Israel has spurned the good; the enemy shall pursue him.
- reference: Rom 9:31
  text: but that Israel who pursued a law that would lead to righteousness did not succeed in reaching that law.
- reference: Jer 39:5
  text: But the army of the Chaldeans pursued them and overtook Zedekiah in the plains of Jericho. And when they had taken him, they brought him up to Nebuchadnezzar king of Babylon, at Riblah, in the land of Hamath; and he passed sentence on him.
- reference: 2Sa 2:19
  text: And Asahel pursued Abner, and as he went, he turned neither to the right hand nor to the left from following Abner.
- reference: Deu 28:45
  text: “ All these curses shall come upon you and pursue you and overtake you till you are destroyed, because you did not obey the voice of the Lord your God, to keep his commandments and his statutes that he commanded you.
- reference: Judg 4:16
  text: And Barak pursued the chariots and the army to Harosheth-hagoyim, and all the army of Sisera fell by the edge of the sword; not a man was left.
- reference: Judg 20:45
  text: And they turned and fled toward the wilderness to the rock of Rimmon. Five thousand men of them were cut down in the highways. And they were pursued hard to Gidom, and 2,000 men of them were struck down.
- reference: 1Sa 7:11
  text: And the men of Israel went out from Mizpah and pursued the Philistines and struck them, as far as below Beth-car.
- reference: 2Sa 2:24
  text: But Joab and Abishai pursued Abner. And as the sun was going down they came to the hill of Ammah, which lies before Giah on the way to the wilderness of Gibeon.
- reference: 2Sa 22:38
  text: I pursued my enemies and destroyed them, and did not turn back until they were consumed.
- reference: Psa 18:37
  text: I pursued my enemies and overtook them, and did not turn back till they were consumed.
- reference: Exo 14:9
  text: The Egyptians pursued them, all Pharaoh’s horses and chariots and his horsemen and his army, and overtook them encamped at the sea, by Pi-hahiroth, in front of Baal-zephon.
- reference: Jos 2:7
  text: So the men pursued after them on the way to the Jordan as far as the fords. And the gate was shut as soon as the pursuers had gone out.
- reference: 1Ki 20:20
  text: And each struck down his man. The Syrians fled, and Israel pursued them, but Ben-hadad king of Syria escaped on a horse with horsemen.
- reference: Jer 52:8
  text: But the army of the Chaldeans pursued the king and overtook Zedekiah in the plains of Jericho, and all his army was scattered from him.
- reference: Jos 8:17
  text: Not a man was left in Ai or Bethel who did not go out after Israel. They left the city open and pursued Israel.
- reference: Rev 12:13
  text: And when the dragon saw that he had been thrown down to the earth, he pursued the woman who had given birth to the male child.
- reference: Gen 31:23
  text: he took his kinsmen with him and pursued him for seven days and followed close after him into the hill country of Gilead.
- reference: 2Sa 20:7
  text: And there went out after him Joab’s men and the Cherethites and the Pelethites, and all the mighty men. They went out from Jerusalem to pursue Sheba the son of Bichri.
- reference: 2Sa 20:13
  text: When he was taken out of the highway, all the people went on after Joab to pursue Sheba the son of Bichri.
- reference: Judg 7:25
  text: And they captured the two princes of Midian, Oreb and Zeeb. They killed Oreb at the rock of Oreb, and Zeeb they killed at the winepress of Zeeb. Then they pursued Midian, and they brought the heads of Oreb and Zeeb to Gideon across the Jordan.
- reference: Judg 1:6
  text: Adoni-bezek fled, but they pursued him and caught him and cut off his thumbs and his big toes.
- reference: Exo 14:23
  text: The Egyptians pursued and went in after them into the midst of the sea, all Pharaoh’s horses, his chariots, and his horsemen.
- reference: 2Ch 13:19
  text: And Abijah pursued Jeroboam and took cities from him, Bethel with its villages and Jeshanah with its villages and Ephron with its villages.

## validation_actions

- add_trace: ["oid", "target", "reason", "moved"]
- add_word_node: ["oid", "occurrence", "strong", "role", "reason"]
- annotate: ["oid", "note"]
- close_deferral: ["oid", "collection_id", "reason"]
- complete_node: ["node_id", "role", "collection_id", "reason"]
- consume: ["old_id", "carriers", "mapping", "uncarried"]
- create_observation: ["spec", "nature", "reason", "serves", "traces"]
- defer: ["oid", "collection_id", "finding"]
- delete_neither: ["oid", "reason", "node_ids"]
- drop_node: ["node_id", "carried_by", "reason"]
- drop_unrelated_node: ["node_id", "reason"]
- mark_self_evidencing: ["oid", "reason"]
- move_node: ["node_id", "to_obs", "reason"]
- note_node: ["node_id", "note"]
- restate: ["oid", "new_text", "checked", "reason", "more"]
- set_nature: ["oid", "nature", "reason"]

## measured

- package_chars: 50678
- seconds: 0.04

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "strive",
 "subgroup": "going after",
 "observations": [
  {
   "observation": 24126,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24127,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24128,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24129,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24130,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24131,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24132,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24133,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24134,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24135,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24136,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24137,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24138,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24139,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24140,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24141,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24142,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24143,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24144,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24145,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24146,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24147,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24148,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24149,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24150,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24151,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24152,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24153,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24154,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24155,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24156,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24157,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24158,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24159,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24160,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24161,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24162,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24163,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24164,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24165,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ],
 "repairs": []
}
```
