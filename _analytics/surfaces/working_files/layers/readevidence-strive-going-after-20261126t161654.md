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

2026-11-26T16:16:54Z

## batch

- observations: 40
- left_after_this: 38
- evidence_in_scope: 158
- observations_in_scope: 158

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 24166
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jude 7 'desire' (sarx, G4561, flesh) is what the cities went after, flesh that is other, rendered unnatural desire.
  basis: stated
  grounds: pursued unnatural desire
  traces: [24111]
  verses: ["Jude 7"]
- observation: 24167
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 15:9, Deu 28:45, 2Sa 22:38, Psa 18:37 and Lam 3:66 destroying or consuming (H3423H, H8045, H3615H) is the end the pursuit aims at or reaches: the pursuer does not turn back until the pursued are consumed.
  basis: stated
  grounds: did not turn back until they were consumed
  traces: [24107, 24108, 24109]
  verses: ["2Sa 22:38", "Deu 28:45", "Exo 15:9", "Lam 3:66", "Psa 18:37"]
- observation: 24168
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 11:4 'destroyed' (H0006) falls on the pursuers: the Egyptians who pursued Israel were destroyed by the Lord at the Red Sea.
  basis: stated
  grounds: the Lord has destroyed them
  traces: [24107]
  verses: ["Deu 11:4"]
- observation: 24169
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 19:6, 2Sa 20:10, 2Ki 9:27 and Psa 109:16 death (H4194, H4191) is what the pursuit brings or aims at: the manslayer struck fatally, Amasa and Ahaziah dead, the needy pursued to be put to death.
  basis: stated
  grounds: to put them to death
  traces: [24107, 24108]
  verses: ["2Ki 9:27", "2Sa 20:10", "Deu 19:6", "Psa 109:16"]
- observation: 24170
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 28:22 'perish' (H0006) is the end set for the pursuit of the diseases: they pursue until the people perish.
  basis: stated
  grounds: They shall pursue you until you perish
  traces: [24109]
  verses: ["Deu 28:22"]
- observation: 24171
  step: 2.1
  item: pairing
  kind: pairing
  text: In Job 13:25 'dry' (H3002) qualifies the chaff Job asks whether God will pursue, a thing too light to be worth the chase.
  basis: stated
  grounds: pursue dry chaff
  traces: [24109]
  verses: ["Job 13:25"]
- observation: 24172
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 10:19 'stay' (H5975G) is negated: the men are not to stand still but to pursue the enemy.
  basis: stated
  grounds: do not stay there yourselves
  traces: [24107]
  verses: ["Jos 10:19"]
- observation: 24173
  step: 2.1
  item: pairing
  kind: pairing
  text: In Judg 1:6, Judg 8:12, Judg 20:45, 2Sa 20:6, 2Sa 24:13, 1Ki 20:20 and 2Ki 9:27 fleeing or escaping (H5127, H4422, H5337) is what the pursued do, the other half of the chase, and in 1Ki 20:20 Ben-hadad escapes.
  basis: stated
  grounds: Adoni-bezek fled, but they pursued him
  traces: [24107]
  verses: ["1Ki 20:20", "2Ki 9:27", "2Sa 20:6", "2Sa 24:13", "Judg 1:6", "Judg 20:45", "Judg 8:12"]
- observation: 24174
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 6:11 and 2Ti 2:22 'flee' (pheugo, G5343) is commanded together with pursue: the man of God flees these things, or youthful passions, and pursues righteousness.
  basis: stated
  grounds: flee these things. Pursue righteousness
  traces: [24110]
  verses: ["1Ti 6:11", "2Ti 2:22"]
- observation: 24175
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 34:14 and 1Pe 3:11 'evil' (H7451B, G2556G) is what one turns away from before seeking peace and pursuing it.
  basis: stated
  grounds: Turn away from evil and do good
  traces: [24110]
  verses: ["1Pe 3:11", "Psa 34:14"]
- observation: 24176
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 26:18 'evil' (H7451I) is denied by David: he asks what evil is on his hands that Saul pursues him.
  basis: stated
  grounds: What evil is on my hands
  traces: [24107]
  verses: ["1Sa 26:18"]
- observation: 24177
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 30:10 'exhausted' (H6296) describes the two hundred who stayed behind at the brook Besor, while David pursued with four hundred.
  basis: stated
  grounds: too exhausted to cross the brook Besor
  traces: [24107]
  verses: ["1Sa 30:10"]
- observation: 24178
  step: 2.1
  item: pairing
  kind: pairing
  text: In Gen 35:5 'terror' (H2847) from God falls on the surrounding cities, and the verse gives it as the reason no pursuit of Jacob's sons was made.
  basis: stated
  grounds: a terror from God fell upon the cities
  traces: [24107]
  verses: ["Gen 35:5"]
- observation: 24179
  step: 2.1
  item: pairing
  kind: pairing
  text: In Judg 8:12, Psa 83:15 and Jer 29:18 panic, terror or horror (H2729, H0926, H2189, H8047H) goes with the pursuit: Gideon throws the army into a panic, God is asked to terrify with his hurricane, and the pursued are made a horror.
  basis: stated
  grounds: terrify them with your hurricane
  traces: [24107, 24109]
  verses: ["Jer 29:18", "Judg 8:12", "Psa 83:15"]
- observation: 24180
  step: 2.1
  item: pairing
  kind: pairing
  text: In Job 13:25 and Job 30:15 frightening and terrors (H6206, H1091 with H5921A) are on the side of the one pursued: a leaf frightened, terrors turned on Job.
  basis: stated
  grounds: Terrors are turned upon me
  traces: [24109]
  verses: ["Job 13:25", "Job 30:15"]
- observation: 24181
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 109:16 'remember' (H2142) is negated and gives the ground of the charge: kindness was not remembered, and the needy were pursued instead.
  basis: stated
  grounds: he did not remember to show kindness
  traces: [24108]
  verses: ["Psa 109:16"]
- observation: 24182
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 71:11 and Hos 8:3 forsaking or spurning (H5800A, H2186A) comes before the pursuit: the foes say God has forsaken him, and Israel has spurned the good, so the enemy pursues.
  basis: stated
  grounds: Israel has spurned the good
  traces: [24107, 24108]
  verses: ["Hos 8:3", "Psa 71:11"]
- observation: 24183
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 8:24 'finished' (H3615G) marks the end of the killing in the field where Ai's men were pursued, before Israel returned to the city.
  basis: stated
  grounds: When Israel had finished killing
  traces: [24107]
  verses: ["Jos 8:24"]
- observation: 24184
  step: 2.1
  item: pairing
  kind: pairing
  text: In Job 19:22 'satisfied' (H7646) is negated: the friends who pursue Job are not satisfied with his flesh.
  basis: stated
  grounds: Why are you not satisfied with my flesh
  traces: [24108]
  verses: ["Job 19:22"]
- observation: 24185
  step: 2.1
  item: pairing
  kind: pairing
  text: In Nah 1:8 'complete' (H3617) is the end God makes of his adversaries, beside pursuing his enemies into darkness.
  basis: stated
  grounds: he will make a complete end
  traces: [24109]
  verses: ["Nah 1:8"]
- observation: 24186
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 6:11 'godliness' (eusebeia, G2150) is the second of the goods named as objects of pursue.
  basis: stated
  grounds: Pursue righteousness, godliness, faith
  traces: [24110]
  verses: ["1Ti 6:11"]
- observation: 24187
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 19:6 'deserve' (mishpat, H4941G) is negated: the manslayer pursued by the avenger did not deserve to die.
  basis: stated
  grounds: the man did not deserve to die
  traces: [24108]
  verses: ["Deu 19:6"]
- observation: 24188
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 20:6 'fortified' (H1219) names the cities Sheba might reach, the reason David gives for pursuing him at once.
  basis: stated
  grounds: lest he get himself to fortified cities
  traces: [24107]
  verses: ["2Sa 20:6"]
- observation: 24189
  step: 2.1
  item: pairing
  kind: pairing
  text: In Judg 20:45 'hard' (achar, H0310A) is the word after the verb that the ESV renders as the closeness of the pursuit: they were followed hard to Gidom.
  basis: stated
  grounds: they were pursued hard to Gidom
  traces: [24107]
  verses: ["Judg 20:45"]
- observation: 24190
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 14:4 and Exo 14:8 'harden' (chazaq, H2388G) is the Lord's act on Pharaoh's heart, and the pursuit of Israel follows it.
  basis: stated
  grounds: the Lord hardened the heart of Pharaoh
  traces: [24107]
  verses: ["Exo 14:4", "Exo 14:8"]
- observation: 24191
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 23:25 'heard' (H8085G) comes before the pursuit: Saul heard where David was and pursued him into the wilderness of Maon.
  basis: stated
  grounds: when Saul heard that, he pursued
  traces: [24107]
  verses: ["1Sa 23:25"]
- observation: 24192
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 51:1 'listen' (H8085G) is the call to those who pursue righteousness, opening the verse.
  basis: stated
  grounds: Listen to me, you who pursue
  traces: [24110]
  verses: ["Isa 51:1"]
- observation: 24193
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 14:4 and Exo 14:8 'heart' (lev, H3820A) is Pharaoh's, the object of the Lord's hardening that comes before the pursuit.
  basis: stated
  grounds: harden Pharaoh's heart, and he will pursue
  traces: [24107]
  verses: ["Exo 14:4", "Exo 14:8"]
- observation: 24194
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Ti 2:22 'heart' (kardia, G2588) is the pure heart of those in whose company righteousness is pursued.
  basis: stated
  grounds: call on the Lord from a pure heart
  traces: [24110]
  verses: ["2Ti 2:22"]
- observation: 24195
  step: 2.1
  item: pairing
  kind: pairing
  text: In Job 30:15 'honor' (H5082) is the subject of the pursuit: it is chased away as by the wind, beside prosperity passed like a cloud.
  basis: stated
  grounds: my honor is pursued as by the wind
  traces: [24109]
  verses: ["Job 30:15"]
- observation: 24196
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 8:24, Judg 7:25 and Lam 3:43 killing (harag, H2026) goes with the pursuit: the men of Ai killed where they were pursued, Oreb and Zeeb killed before the pursuit of Midian, and Zion pursued and killed without pity.
  basis: stated
  grounds: pursued us, killing without pity
  traces: [24107, 24108]
  verses: ["Jos 8:24", "Judg 7:25", "Lam 3:43"]
- observation: 24197
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 14:4 'know' (H3045) gives the purpose of the pursuit God brings about: the Egyptians shall know that he is the Lord.
  basis: stated
  grounds: the Egyptians shall know that I am the Lord
  traces: [24107]
  verses: ["Exo 14:4"]
- observation: 24198
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 2:5 'know' (H3045) is negated in Rahab's word that she does not know where the men went, before she tells the king's men to pursue.
  basis: stated
  grounds: I do not know where the men went
  traces: [24107]
  verses: ["Jos 2:5"]
- observation: 24199
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 25:29 'living' and 'lives' (H2416A, H5315H) set the life of the one pursued, bound in the bundle of the living with the Lord, against those who rise to pursue it.
  basis: stated
  grounds: bound in the bundle of the living
  traces: [24108]
  verses: ["1Sa 25:29"]
- observation: 24200
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 24:14 and Psa 143:3 'dead' (H4191) is a likeness: David names himself a dead dog that Saul pursues, and the pursued speaker is made to sit like those long dead.
  basis: stated
  grounds: After a dead dog! After a flea
  traces: [24107, 24108]
  verses: ["1Sa 24:14", "Psa 143:3"]
- observation: 24201
  step: 2.1
  item: pairing
  kind: pairing
  text: In Num 14:45, 1Sa 23:25, 2Ch 14:13 and Eze 35:6 the words of living (H3427, H4241 with H0369, H2416A) give the place of those pursued, the end of the pursued, and God's oath 'as I live'.
  basis: stated
  grounds: as I live, declares the Lord God
  traces: [24107, 24109]
  verses: ["1Sa 23:25", "2Ch 14:13", "Eze 35:6", "Num 14:45"]
- observation: 24202
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 19:6 and Eze 35:6 'hated' (H8130) gives the legal ground: the manslayer had not hated his neighbor, and Edom did not hate bloodshed, so blood pursues.
  basis: stated
  grounds: since he had not hated his neighbor
  traces: [24108, 24109]
  verses: ["Deu 19:6", "Eze 35:6"]
- observation: 24203
  step: 2.1
  item: pairing
  kind: pairing
  text: In Hos 2:7 'lovers' (H0157G) are the object of the wife's pursuit, which does not reach them.
  basis: stated
  grounds: She shall pursue her lovers
  traces: [24111]
  verses: ["Hos 2:7"]
- observation: 24204
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Cor 14:1, 1Ti 6:11 and 2Ti 2:22 'love' (agape, G0026) is an object of the command to pursue, first in 1Cor 14:1.
  basis: stated
  grounds: Pursue love, and earnestly desire
  traces: [24110]
  verses: ["1Cor 14:1", "1Ti 6:11", "2Ti 2:22"]
- observation: 24205
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 30:8 'surely' (H5381, H5337, infinitive absolutes) doubles the verbs of the Lord's answer: the pursuit he commands will surely overtake and surely rescue.
  basis: stated
  grounds: you shall surely overtake and shall surely rescue
  traces: [24107]
  verses: ["1Sa 30:8"]

## verses

- reference: Deu 19:6
  text: lest the avenger of blood in hot anger pursue the manslayer and overtake him, because the way is long, and strike him fatally, though the man did not deserve to die, since he had not hated his neighbor in the past.
- reference: Eze 35:6
  text: therefore, as I live, declares the Lord God, I will prepare you for blood, and blood shall pursue you; because you did not hate bloodshed, therefore blood shall pursue you.
- reference: Lam 3:43
  text: “You have wrapped yourself with anger and pursued us, killing without pity;
- reference: Lam 3:66
  text: You will pursue them in anger and destroy them from under your heavens, O Lord.”
- reference: 2Sa 24:13
  text: So Gad came to David and told him, and said to him, “Shall three years of famine come to you in your land? Or will you flee three months before your foes while they pursue you? Or shall there be three days ’ pestilence in your land? Now consider, and decide what answer I shall return to him who sent me.”
- reference: Exo 15:9
  text: The enemy said, ‘I will pursue, I will overtake, I will divide the spoil, my desire shall have its fill of them. I will draw my sword; my hand shall destroy them.’
- reference: Job 13:25
  text: Will you frighten a driven leaf and pursue dry chaff?
- reference: Exo 14:4
  text: And I will harden Pharaoh’s heart, and he will pursue them, and I will get glory over Pharaoh and all his host, and the Egyptians shall know that I am the Lord.” And they did so.
- reference: 2Ch 14:13
  text: Asa and the people who were with him pursued them as far as Gerar, and the Ethiopians fell until none remained alive, for they were broken before the Lord and his army. The men of Judah carried away very much spoil.
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
- reference: Num 14:45
  text: Then the Amalekites and the Canaanites who lived in that hill country came down and defeated them and pursued them, even to Hormah.
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
- reference: 1Sa 30:8
  text: And David inquired of the Lord, “Shall I pursue after this band? Shall I overtake them?” He answered him, “ Pursue, for you shall surely overtake and shall surely rescue.”
- reference: 2Ki 9:27
  text: When Ahaziah the king of Judah saw this, he fled in the direction of Beth-haggan. And Jehu pursued him and said, “ Shoot him also.” And they shot him in the chariot at the ascent of Gur, which is by Ibleam. And he fled to Megiddo and died there.
- reference: Psa 71:11
  text: and say, “ God has forsaken him; pursue and seize him, for there is none to deliver him.”
- reference: Hos 2:7
  text: She shall pursue her lovers but not overtake them, and she shall seek them but shall not find them. Then she shall say, ‘I will go and return to my first husband, for it was better for me then than now.’
- reference: Jer 29:18
  text: I will pursue them with sword, famine, and pestilence, and will make them a horror to all the kingdoms of the earth, to be a curse, a terror, a hissing, and a reproach among all the nations where I have driven them,
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
- reference: Job 30:15
  text: Terrors are turned upon me; my honor is pursued as by the wind, and my prosperity has passed away like a cloud.
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
- reference: Jos 8:24
  text: When Israel had finished killing all the inhabitants of Ai in the open wilderness where they pursued them, and all of them to the very last had fallen by the edge of the sword, all Israel returned to Ai and struck it down with the edge of the sword.
- reference: 1Sa 30:10
  text: But David pursued, he and four hundred men. Two hundred stayed behind, who were too exhausted to cross the brook Besor.
- reference: Judg 8:12
  text: And Zebah and Zalmunna fled, and he pursued them and captured the two kings of Midian, Zebah and Zalmunna, and he threw all the army into a panic.
- reference: Hos 8:3
  text: Israel has spurned the good; the enemy shall pursue him.
- reference: Nah 1:8
  text: But with an overflowing flood he will make a complete end of the adversaries, and will pursue his enemies into darkness.
- reference: Deu 28:45
  text: “ All these curses shall come upon you and pursue you and overtake you till you are destroyed, because you did not obey the voice of the Lord your God, to keep his commandments and his statutes that he commanded you.
- reference: Judg 20:45
  text: And they turned and fled toward the wilderness to the rock of Rimmon. Five thousand men of them were cut down in the highways. And they were pursued hard to Gidom, and 2,000 men of them were struck down.
- reference: 2Sa 22:38
  text: I pursued my enemies and destroyed them, and did not turn back until they were consumed.
- reference: Psa 18:37
  text: I pursued my enemies and overtook them, and did not turn back till they were consumed.
- reference: 1Ki 20:20
  text: And each struck down his man. The Syrians fled, and Israel pursued them, but Ben-hadad king of Syria escaped on a horse with horsemen.
- reference: Judg 7:25
  text: And they captured the two princes of Midian, Oreb and Zeeb. They killed Oreb at the rock of Oreb, and Zeeb they killed at the winepress of Zeeb. Then they pursued Midian, and they brought the heads of Oreb and Zeeb to Gideon across the Jordan.
- reference: Judg 1:6
  text: Adoni-bezek fled, but they pursued him and caught him and cut off his thumbs and his big toes.

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

- package_chars: 44178
- seconds: 0.04

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "strive",
 "subgroup": "going after",
 "observations": [
  {
   "observation": 24166,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24167,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24168,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24169,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24170,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24171,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24172,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24173,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24174,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24175,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24176,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24177,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24178,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24179,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24180,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24181,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24182,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24183,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24184,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24185,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24186,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24187,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24188,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24189,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24190,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24191,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24192,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24193,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24194,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24195,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24196,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24197,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24198,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24199,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24200,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24201,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24202,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24203,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24204,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24205,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ],
 "repairs": []
}
```
