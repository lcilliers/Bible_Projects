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

2026-11-26T16:17:05Z

## batch

- observations: 38
- left_after_this: 0
- evidence_in_scope: 158
- observations_in_scope: 158

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 24206
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 6:11 'steadfastness' (hupomone, G5281) is one of the goods named as objects of pursue.
  basis: stated
  grounds: faith, love, steadfastness, gentleness
  traces: [24110]
  verses: ["1Ti 6:11"]
- observation: 24207
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 7:5 'glory' (kavod, H3519) is laid in the dust by the enemy who is invited to pursue and overtake the speaker's soul.
  basis: stated
  grounds: lay my glory in the dust
  traces: [24108]
  verses: ["Psa 7:5"]
- observation: 24208
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jer 48:2 'silence' (H1826H) is what Madmen will be brought to, beside the sword that will pursue it.
  basis: stated
  grounds: shall be brought to silence
  traces: [24109]
  verses: ["Jer 48:2"]
- observation: 24209
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 2:5, Jos 2:7, Jos 8:17 and Jos 8:24 the gate shut or the city left open (H5462, H6605A) and the open field (H7704G) set the place of the pursuit: the gate shut behind the pursuers, Ai left open, the men killed in the open.
  basis: stated
  grounds: They left the city open and pursued Israel
  traces: [24107]
  verses: ["Jos 2:5", "Jos 2:7", "Jos 8:17", "Jos 8:24"]
- observation: 24210
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 17:52 'wounded' (H2491A) names the Philistines who fell on the way as the men of Israel pursued them.
  basis: stated
  grounds: the wounded Philistines fell on the way
  traces: [24107]
  verses: ["1Sa 17:52"]
- observation: 24211
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 109:16 'brokenhearted' (H3512A with levav, H3824) names the third group pursued to death, beside the poor and needy.
  basis: stated
  grounds: the poor and needy and the brokenhearted
  traces: [24108]
  verses: ["Psa 109:16"]
- observation: 24212
  step: 2.1
  item: pairing
  kind: pairing
  text: In Eze 35:6 'declares' (H5002) marks the sentence that blood shall pursue Edom as the Lord's own word.
  basis: stated
  grounds: declares the Lord God
  traces: [24109]
  verses: ["Eze 35:6"]
- observation: 24213
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Cor 14:1 'prophesy' (G4395) is named as the gift to be desired most, after the command to pursue love.
  basis: stated
  grounds: especially that you may prophesy
  traces: [24110]
  verses: ["1Cor 14:1"]
- observation: 24214
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 30:8 'answered' (H0559) introduces the Lord's reply to David's question whether to pursue.
  basis: stated
  grounds: He answered him, Pursue
  traces: [24107]
  verses: ["1Sa 30:8"]
- observation: 24215
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 24:13 'answer' (H1697H) is what Gad must bring back after David chooses among the judgments, one of them a pursuit by foes.
  basis: stated
  grounds: decide what answer I shall return
  traces: [24107]
  verses: ["2Sa 24:13"]
- observation: 24216
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 34:14, Rom 14:19, 2Ti 2:22 and 1Pe 3:11 'peace' (H7965G, G1515) is an object of the pursuit, in Psa 34:14 and 1Pe 3:11 first sought and then pursued.
  basis: stated
  grounds: seek peace and pursue it
  traces: [24110]
  verses: ["1Pe 3:11", "2Ti 2:22", "Psa 34:14", "Rom 14:19"]
- observation: 24217
  step: 2.1
  item: pairing
  kind: pairing
  text: In Amo 1:11 'cast off' (H7843) has pity as its object: Edom pursued his brother and cast off pity.
  basis: stated
  grounds: cast off all pity
  traces: [24108]
  verses: ["Amo 1:11"]
- observation: 24218
  step: 2.1
  item: pairing
  kind: pairing
  text: In Deu 28:45 'keep' (H8104G) belongs to the commandments not kept, the reason the curses pursue.
  basis: stated
  grounds: to keep his commandments and his statutes
  traces: [24109]
  verses: ["Deu 28:45"]
- observation: 24219
  step: 2.1
  item: pairing
  kind: pairing
  text: In Amo 1:11 'kept' (H8104G) has wrath as its object: Edom kept his wrath forever, beside the pursuit of his brother.
  basis: stated
  grounds: he kept his wrath forever
  traces: [24108]
  verses: ["Amo 1:11"]
- observation: 24220
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jer 48:2 'renown' (H8416) of Moab is no more, at the opening of the oracle in which the sword will pursue Madmen.
  basis: stated
  grounds: the renown of Moab is no more
  traces: [24109]
  verses: ["Jer 48:2"]
- observation: 24221
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 8:24 'returned' (H7725G with H5704) closes the pursuit: when the killing in the open was finished, all Israel returned to Ai.
  basis: stated
  grounds: all Israel returned to Ai
  traces: [24107]
  verses: ["Jos 8:24"]
- observation: 24222
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 24:13 'return' (H7725G with H4100) is the answer Gad must take back after David chooses among the judgments.
  basis: stated
  grounds: what answer I shall return
  traces: [24107]
  verses: ["2Sa 24:13"]
- observation: 24223
  step: 2.1
  item: pairing
  kind: pairing
  text: In Hos 2:7 'return' (H7725G) follows the failed pursuit: the wife resolves to go back to her first husband.
  basis: stated
  grounds: I will go and return to my first husband
  traces: [24111]
  verses: ["Hos 2:7"]
- observation: 24224
  step: 2.1
  item: pairing
  kind: pairing
  text: In Amo 1:11 and Jude 7 'punishment' (H5921A, G1349) follows the pursuit: for Edom it will not be revoked, and for the cities it is eternal fire.
  basis: stated
  grounds: by undergoing a punishment of eternal fire
  traces: [24108, 24111]
  verses: ["Amo 1:11", "Jude 7"]
- observation: 24225
  step: 2.1
  item: pairing
  kind: pairing
  text: In Job 30:15 'prosperity' (H3444) has passed away like a cloud, beside Job's honor pursued as by the wind.
  basis: stated
  grounds: my prosperity has passed away like a cloud
  traces: [24109]
  verses: ["Job 30:15"]
- observation: 24226
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 109:16 'poor' and 'needy' (H6041, H0034 with H0376I) name those pursued to be put to death.
  basis: stated
  grounds: pursued the poor and needy
  traces: [24108]
  verses: ["Psa 109:16"]
- observation: 24227
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 51:1, Rom 9:30, Rom 9:31, 1Ti 6:11 and 2Ti 2:22 'righteousness' (H6664G, G1343) is the object of the pursuit; in Rom 9:30 it is reached without pursuit and in Rom 9:31 the law of it pursued and not reached.
  basis: stated
  grounds: you who pursue righteousness
  traces: [24110]
  verses: ["1Ti 6:11", "2Ti 2:22", "Isa 51:1", "Rom 9:30", "Rom 9:31"]
- observation: 24228
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jude 7 'sexual immorality' (G1608) is what the cities indulged in, together with going after unnatural desire.
  basis: stated
  grounds: indulged in sexual immorality
  traces: [24111]
  verses: ["Jude 7"]
- observation: 24229
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 71:11 'deliver' (H5337) is negated in the foes' words: there is none to deliver him, so they urge pursuit.
  basis: stated
  grounds: there is none to deliver him
  traces: [24108]
  verses: ["Psa 71:11"]
- observation: 24230
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 23:25, 1Sa 25:29 and Hos 2:7 seeking (baqash, H1245) goes with the pursuit of a person: Saul seeks David, men seek David's life, the wife seeks her lovers and does not find them.
  basis: stated
  grounds: she shall seek them but shall not find them
  traces: [24107, 24108, 24111]
  verses: ["1Sa 23:25", "1Sa 25:29", "Hos 2:7"]
- observation: 24231
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 34:14, 1Pe 3:11 and Isa 51:1 seeking (H1245, G2212) is paired with pursuing a good: peace sought and pursued, and those who pursue righteousness called those who seek the Lord.
  basis: stated
  grounds: you who seek the Lord
  traces: [24110]
  verses: ["1Pe 3:11", "Isa 51:1", "Psa 34:14"]
- observation: 24232
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 2:28 'stopped' (H5975G) ends the pursuit at Joab's trumpet.
  basis: stated
  grounds: all the men stopped and pursued Israel no more
  traces: [24107]
  verses: ["2Sa 2:28"]
- observation: 24233
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 34:14 and 1Pe 3:11 doing good (H6213A, G4160G) stands between turning from evil and seeking and pursuing peace.
  basis: stated
  grounds: turn away from evil and do good
  traces: [24110]
  verses: ["1Pe 3:11", "Psa 34:14"]
- observation: 24234
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jude 7 'serve' (G4295) has the cities as subject: they serve as an example by their punishment.
  basis: stated
  grounds: serve as an example
  traces: [24111]
  verses: ["Jude 7"]
- observation: 24235
  step: 2.1
  item: pairing
  kind: pairing
  text: In Jos 10:19 'given' (H5414G with H3588A) gives the ground of the command to pursue: the Lord has given the enemies into their hand.
  basis: stated
  grounds: has given them into your hand
  traces: [24107]
  verses: ["Jos 10:19"]
- observation: 24236
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Ch 14:13 'broken' (H7665) names the Ethiopians as broken before the Lord and his army as Asa pursued them.
  basis: stated
  grounds: they were broken before the Lord
  traces: [24107]
  verses: ["2Ch 14:13"]
- observation: 24237
  step: 2.1
  item: pairing
  kind: pairing
  text: In Amo 1:11 'transgressions' (H6588) frame the charge against Edom, of which the pursuit of his brother is the one named.
  basis: stated
  grounds: For three transgressions of Edom
  traces: [24108]
  verses: ["Amo 1:11"]
- observation: 24238
  step: 2.1
  item: pairing
  kind: pairing
  text: In Gen 31:23, Judg 1:6, 2Sa 20:6, 2Ch 13:19, Psa 71:11 and Jer 39:5 taking or seizing (H3947G, H0270, H3920, H8610) is what the pursuit is for or ends in: kinsmen taken along, Adoni-bezek caught, cities taken, the one forsaken to be seized, Zedekiah taken.
  basis: stated
  grounds: pursue and seize him
  traces: [24107, 24108]
  verses: ["2Ch 13:19", "2Sa 20:6", "Gen 31:23", "Jer 39:5", "Judg 1:6", "Psa 71:11"]
- observation: 24239
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 2:19, 2Sa 22:38 and Psa 18:37 turning (H5186, H7725G) is negated: the pursuer does not turn aside or back until the pursued is reached or consumed.
  basis: stated
  grounds: did not turn back till they were consumed
  traces: [24107]
  verses: ["2Sa 22:38", "2Sa 2:19", "Psa 18:37"]
- observation: 24240
  step: 2.1
  item: pairing
  kind: pairing
  text: In Judg 20:45 'turned' (H6437G) is the flight of the pursued toward the wilderness, and in Job 30:15 'turned' (H2015) the terrors turned on Job.
  basis: stated
  grounds: And they turned and fled toward the wilderness
  traces: [24107, 24109]
  verses: ["Job 30:15", "Judg 20:45"]
- observation: 24241
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 20:10 'observe' (H8104I) is negated: Amasa did not watch the sword in Joab's hand, before Joab and Abishai pursued Sheba.
  basis: stated
  grounds: Amasa did not observe the sword
  traces: [24107]
  verses: ["2Sa 20:10"]
- observation: 24242
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Sa 17:52 'shout' (H7321) goes with the rising of Israel and Judah before they pursued the Philistines.
  basis: stated
  grounds: rose with a shout and pursued the Philistines
  traces: [24107]
  verses: ["1Sa 17:52"]
- observation: 24243
  step: 2.1
  item: pairing
  kind: pairing
  text: In 2Sa 24:13 'consider' (H3045) is Gad's call to David to weigh the three judgments, one of them a pursuit by foes.
  basis: stated
  grounds: Now consider, and decide
  traces: [24107]
  verses: ["2Sa 24:13"]

## verses

- reference: Eze 35:6
  text: therefore, as I live, declares the Lord God, I will prepare you for blood, and blood shall pursue you; because you did not hate bloodshed, therefore blood shall pursue you.
- reference: Amo 1:11
  text: Thus says the Lord: “For three transgressions of Edom, and for four, I will not revoke the punishment, because he pursued his brother with the sword and cast off all pity, and his anger tore perpetually, and he kept his wrath forever.
- reference: 2Sa 24:13
  text: So Gad came to David and told him, and said to him, “Shall three years of famine come to you in your land? Or will you flee three months before your foes while they pursue you? Or shall there be three days ’ pestilence in your land? Now consider, and decide what answer I shall return to him who sent me.”
- reference: Jer 48:2
  text: the renown of Moab is no more. In Heshbon they planned disaster against her: ‘ Come, let us cut her off from being a nation!’ You also, O Madmen, shall be brought to silence; the sword shall pursue you.
- reference: 2Ch 14:13
  text: Asa and the people who were with him pursued them as far as Gerar, and the Ethiopians fell until none remained alive, for they were broken before the Lord and his army. The men of Judah carried away very much spoil.
- reference: 2Sa 20:6
  text: And David said to Abishai, “ Now Sheba the son of Bichri will do us more harm than Absalom. Take your lord’s servants and pursue him, lest he get himself to fortified cities and escape from us.”
- reference: Psa 109:16
  text: For he did not remember to show kindness, but pursued the poor and needy and the brokenhearted, to put them to death.
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
- reference: 1Sa 30:8
  text: And David inquired of the Lord, “Shall I pursue after this band? Shall I overtake them?” He answered him, “ Pursue, for you shall surely overtake and shall surely rescue.”
- reference: Psa 71:11
  text: and say, “ God has forsaken him; pursue and seize him, for there is none to deliver him.”
- reference: Hos 2:7
  text: She shall pursue her lovers but not overtake them, and she shall seek them but shall not find them. Then she shall say, ‘I will go and return to my first husband, for it was better for me then than now.’
- reference: Jude 7
  text: just as Sodom and Gomorrah and the surrounding cities, which likewise indulged in sexual immorality and pursued unnatural desire, serve as an example by undergoing a punishment of eternal fire.
- reference: 2Sa 20:10
  text: But Amasa did not observe the sword that was in Joab’s hand. So Joab struck him with it in the stomach and spilled his entrails to the ground without striking a second blow, and he died. Then Joab and Abishai his brother pursued Sheba the son of Bichri.
- reference: 1Sa 23:25
  text: And Saul and his men went to seek him. And David was told, so he went down to the rock and lived in the wilderness of Maon. And when Saul heard that, he pursued after David in the wilderness of Maon.
- reference: Isa 51:1
  text: “ Listen to me, you who pursue righteousness, you who seek the Lord: look to the rock from which you were hewn, and to the quarry from which you were dug.
- reference: Job 30:15
  text: Terrors are turned upon me; my honor is pursued as by the wind, and my prosperity has passed away like a cloud.
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
- reference: Psa 7:5
  text: let the enemy pursue my soul and overtake it, and let him trample my life to the ground and lay my glory in the dust. Selah
- reference: Jos 2:5
  text: And when the gate was about to be closed at dark, the men went out. I do not know where the men went. Pursue them quickly, for you will overtake them.”
- reference: 1Ti 6:11
  text: But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.
- reference: Jos 8:24
  text: When Israel had finished killing all the inhabitants of Ai in the open wilderness where they pursued them, and all of them to the very last had fallen by the edge of the sword, all Israel returned to Ai and struck it down with the edge of the sword.
- reference: 2Sa 2:28
  text: So Joab blew the trumpet, and all the men stopped and pursued Israel no more, nor did they fight anymore.
- reference: 1Sa 17:52
  text: And the men of Israel and Judah rose with a shout and pursued the Philistines as far as Gath and the gates of Ekron, so that the wounded Philistines fell on the way from Shaaraim as far as Gath and Ekron.
- reference: Rom 9:30
  text: What shall we say, then? That Gentiles who did not pursue righteousness have attained it, that is, a righteousness that is by faith;
- reference: Rom 9:31
  text: but that Israel who pursued a law that would lead to righteousness did not succeed in reaching that law.
- reference: Jer 39:5
  text: But the army of the Chaldeans pursued them and overtook Zedekiah in the plains of Jericho. And when they had taken him, they brought him up to Nebuchadnezzar king of Babylon, at Riblah, in the land of Hamath; and he passed sentence on him.
- reference: 2Sa 2:19
  text: And Asahel pursued Abner, and as he went, he turned neither to the right hand nor to the left from following Abner.
- reference: Deu 28:45
  text: “ All these curses shall come upon you and pursue you and overtake you till you are destroyed, because you did not obey the voice of the Lord your God, to keep his commandments and his statutes that he commanded you.
- reference: Judg 20:45
  text: And they turned and fled toward the wilderness to the rock of Rimmon. Five thousand men of them were cut down in the highways. And they were pursued hard to Gidom, and 2,000 men of them were struck down.
- reference: 2Sa 22:38
  text: I pursued my enemies and destroyed them, and did not turn back until they were consumed.
- reference: Psa 18:37
  text: I pursued my enemies and overtook them, and did not turn back till they were consumed.
- reference: Rom 14:19
  text: So then let us pursue what makes for peace and for mutual upbuilding.
- reference: Jos 2:7
  text: So the men pursued after them on the way to the Jordan as far as the fords. And the gate was shut as soon as the pursuers had gone out.
- reference: Jos 8:17
  text: Not a man was left in Ai or Bethel who did not go out after Israel. They left the city open and pursued Israel.
- reference: Gen 31:23
  text: he took his kinsmen with him and pursued him for seven days and followed close after him into the hill country of Gilead.
- reference: Judg 1:6
  text: Adoni-bezek fled, but they pursued him and caught him and cut off his thumbs and his big toes.
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

- package_chars: 40992
- seconds: 0.04

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "strive",
 "subgroup": "going after",
 "observations": [
  {
   "observation": 24206,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24207,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24208,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24209,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24210,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24211,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24212,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24213,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24214,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24215,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24216,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24217,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24218,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24219,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24220,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24221,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24222,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24223,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24224,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24225,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24226,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24227,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24228,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24229,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24230,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24231,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24232,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24233,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24234,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24235,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24236,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24237,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24238,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24239,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24240,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24241,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24242,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24243,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ],
 "repairs": []
}
```
