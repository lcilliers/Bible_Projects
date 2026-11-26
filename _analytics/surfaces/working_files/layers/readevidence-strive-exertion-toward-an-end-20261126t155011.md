# ReadEvidence -- strive / exertion toward an end -- step 2.1

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

2026-11-26T15:50:11Z

## batch

- observations: 40
- left_after_this: 11
- evidence_in_scope: 132
- observations_in_scope: 135

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 24013
  step: 2.1
  item: pairing
  kind: pairing
  text: In Pro 28:4 'wicked' (H7563) are the ones the law-keepers strive against, referred to again by 'them' after the verb.
  basis: stated
  grounds: those who keep the law strive against them
  traces: [23952]
  verses: ["Pro 28:4"]
- observation: 24014
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 1:17 'madness' (H1947) and 'folly' (H5531A) are objects of 'to know', set beside wisdom; the applying of the heart to know them is what the verse calls a striving after wind.
  basis: stated
  grounds: to know madness and folly
  traces: [23955]
  verses: ["Ecc 1:17"]
- observation: 24015
  step: 2.1
  item: pairing
  kind: pairing
  text: In Pro 28:4 'forsake' (H5800A, a participle) names those who leave the law and praise the wicked, set opposite those who keep it and strive.
  basis: stated
  grounds: Those who forsake the law
  traces: [23952]
  verses: ["Pro 28:4"]
- observation: 24016
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 4:16 'rejoice' (H8055) is negated: the generations after the king take no joy in him, and the verse then calls it a striving after wind.
  basis: stated
  grounds: will not rejoice in him
  traces: [23955]
  verses: ["Ecc 4:16"]
- observation: 24017
  step: 2.1
  item: pairing
  kind: pairing
  text: In Heb 12:14 'holiness' (hagiasmos, G0038) is the second object of 'strive for', after peace, and the clause after it makes it the condition of seeing the Lord.
  basis: stated
  grounds: and for the holiness without which
  traces: [23951]
  verses: ["Heb 12:14"]
- observation: 24018
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 4:16 'led' (three codes, H6440G, H0834A, H1961: those he was before) names the people the king led without end; their later lack of rejoicing is called a striving after wind.
  basis: read
  grounds: all of whom he led
  traces: [23955]
  verses: ["Ecc 4:16"]
- observation: 24019
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 1:17 'heart' (lev, H3820A) is the object of 'applied': the speaker applied his heart to know, and that knowing is then called a striving after wind.
  basis: stated
  grounds: I applied my heart to know wisdom
  traces: [23955]
  verses: ["Ecc 1:17"]
- observation: 24020
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:22 'heart' (lev, H3820A) stands in construct after striving, so the striving is of the heart, joined to the toil.
  basis: stated
  grounds: striving of heart
  traces: [23951]
  verses: ["Ecc 2:22"]
- observation: 24021
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Th 2:17 'heart' (kardia, G2588) stands in the contrast 'in person, not in heart', which comes just before endeavored.
  basis: stated
  grounds: in person not in heart
  traces: [23951]
  verses: ["1Th 2:17"]
- observation: 24022
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 41:11 'put to shame' (H0954) is the outcome for the incensed, in the clause parallel to the one where those who strive against Israel come to nothing.
  basis: stated
  grounds: shall be put to shame
  traces: [23952]
  verses: ["Isa 41:11"]
- observation: 24023
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 4:10 'hope' (G1679, a perfect: hope set and standing) gives the ground of the toil and striving, in the clause after 'because'.
  basis: stated
  grounds: because we have our hope set on the living God
  traces: [23951]
  verses: ["1Ti 4:10"]
- observation: 24024
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 4:4 'envy' (qinah, H7068, with H3588A and H1931 at the same place) of a man toward his neighbor is named as the source of all toil and skill in work, which the verse then calls a striving after wind.
  basis: stated
  grounds: envy of his neighbor
  traces: [23955]
  verses: ["Ecc 4:4"]
- observation: 24025
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 1:17 'know' (yada, H3045) is used three times: twice for setting the heart to know wisdom, madness and folly, and once for perceiving that this too is a striving after wind.
  basis: stated
  grounds: I perceived that this also is
  traces: [23955]
  verses: ["Ecc 1:17"]
- observation: 24026
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:26 'knowledge' (H1847) is one of the gifts God gives to the one who pleases him, set against the sinner's business that is called a striving after wind.
  basis: stated
  grounds: God has given wisdom and knowledge and joy
  traces: [23955]
  verses: ["Ecc 2:26"]
- observation: 24027
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:11, 2:22, 4:4 and 4:6 'toil' (amal, H5999), and in 4:4 also 'work' (H4639G), stand with striving in one verse: joined to it by 'and' in 2:22 and 4:6, and in 2:11 and 4:4 as what the verse then calls a striving after wind.
  basis: read
  grounds: toil and a striving after wind
  traces: [23951, 23955]
  verses: ["Ecc 2:11", "Ecc 2:22", "Ecc 4:4", "Ecc 4:6"]
- observation: 24028
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 45:9 'work' (H6467) is the potter's work in the clay's mouth, a complaint that it has no handles, which pictures the one who strives with his maker.
  basis: read
  grounds: Your work has no handles
  traces: [23952]
  verses: ["Isa 45:9"]
- observation: 24029
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 4:10 'toil' (kopiao, G2872) is paired with strive by 'and', both verbs of the same subject and with the same end.
  basis: stated
  grounds: we toil and strive
  traces: [23951]
  verses: ["1Ti 4:10"]
- observation: 24030
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:17 'grievous' (H7451A) says how what is done under the sun weighed on the speaker; it gives the reason he hated life, before the verse calls it all a striving after wind.
  basis: stated
  grounds: was grievous to me
  traces: [23955]
  verses: ["Ecc 2:17"]
- observation: 24031
  step: 2.1
  item: pairing
  kind: pairing
  text: In Hos 12:4 'wept' (H1058) follows strove and prevailed: after the struggle Jacob wept and sought favor.
  basis: stated
  grounds: he wept and sought his favor
  traces: [23954]
  verses: ["Hos 12:4"]
- observation: 24032
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 4:10 'living' (G2198, a participle) describes God, the one on whom the hope behind the striving is set.
  basis: stated
  grounds: our hope set on the living God
  traces: [23951]
  verses: ["1Ti 4:10"]
- observation: 24033
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:17 'hated' (H8130) has life as its object and opens the verse; the reason follows, and the verse ends by calling it all a striving after wind.
  basis: stated
  grounds: So I hated life
  traces: [23955]
  verses: ["Ecc 2:17"]
- observation: 24034
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 21:22 'surely' (H6064, an infinitive absolute) doubles the verb 'fined', making the penalty after the fight certain.
  basis: read
  grounds: shall surely be fined
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 24035
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 4:16 'surely' (ki, H3588A) opens the closing clause with emphasis, the clause that calls it a striving after wind.
  basis: read
  grounds: Surely this also is vanity
  traces: [23955]
  verses: ["Ecc 4:16"]
- observation: 24036
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 4:6 'quietness' (H5183A) is on the side judged better, a single handful of it set against two hands full of toil and striving after wind.
  basis: stated
  grounds: a handful of quietness
  traces: [23955]
  verses: ["Ecc 4:6"]
- observation: 24037
  step: 2.1
  item: pairing
  kind: pairing
  text: In Heb 4:11 'rest' (katapausis, G2663) is the goal of strive, the rest the hearers are urged to enter.
  basis: stated
  grounds: strive to enter that rest
  traces: [23951]
  verses: ["Heb 4:11"]
- observation: 24038
  step: 2.1
  item: pairing
  kind: pairing
  text: In Gen 32:28 and Hos 12:4 'prevailed' (H3201) follows the striving in both tellings and is joined to it by 'and', so the struggle is told with its outcome.
  basis: stated
  grounds: and have prevailed
  traces: [23954]
  verses: ["Gen 32:28", "Hos 12:4"]
- observation: 24039
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 1:14, 2:11, 2:17, 2:26, 4:4, 4:16 and 6:9 'vanity' (hevel, H1892) is joined to striving by 'and' as the first of the two names given to the case; in 4:16 'this' (H2088) stands at the same place.
  basis: stated
  grounds: vanity and a striving after wind
  traces: [23955]
  verses: ["Ecc 1:14", "Ecc 2:11", "Ecc 2:17", "Ecc 2:26", "Ecc 4:16", "Ecc 4:4", "Ecc 6:9"]
- observation: 24040
  step: 2.1
  item: pairing
  kind: pairing
  text: In Heb 12:14 'peace' (eirene, G1515) is the first object of strive for, its range given by 'with everyone'.
  basis: stated
  grounds: Strive for peace with everyone
  traces: [23951]
  verses: ["Heb 12:14"]
- observation: 24041
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 60:1 'restore' (H7725H) is the plea that closes the prayer of the verse, apart from the superscription where 'strove' stands.
  basis: read
  grounds: oh, restore us
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 24042
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 60:1 'rejected' (H2186A) is said of God toward his people in the prayer of the verse, apart from the superscription where 'strove' names David's wars.
  basis: read
  grounds: O God, you have rejected us
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 24043
  step: 2.1
  item: pairing
  kind: pairing
  text: In Pro 28:4 'keep' (shamar, H8104G, a participle) names the subject of strive: those who keep the law, set opposite those who forsake it.
  basis: stated
  grounds: those who keep the law strive
  traces: [23952]
  verses: ["Pro 28:4"]
- observation: 24044
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 60:1 'return' (H7725G) is Joab's coming back from the wars, in the clause of the superscription that follows David's striving.
  basis: stated
  grounds: Joab on his return struck down
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 24045
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 21:22 'pay' (H5414N) is what the one who struck the woman must do after the fight, the amount set by the husband and the judges.
  basis: stated
  grounds: he shall pay as the judges determine
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 24046
  step: 2.1
  item: pairing
  kind: pairing
  text: In Gal 2:17 'justified' (dikaioo, G1344, an aorist passive infinitive) is the goal of the endeavor, a standing received in Christ.
  basis: stated
  grounds: to be justified in Christ
  traces: [23951]
  verses: ["Gal 2:17"]
- observation: 24047
  step: 2.1
  item: pairing
  kind: pairing
  text: In Luk 13:24 'seek' (zeteo, G2212, future) is what the many will do to enter, set against the command to strive, and followed by their not being able.
  basis: stated
  grounds: will seek to enter and will not be able
  traces: [23951]
  verses: ["Luk 13:24"]
- observation: 24048
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:26 'given' and 'give' (natan, H5414G) are used three times: God gives wisdom, knowledge and joy to the one who pleases him, gives the sinner the business of gathering, and that gathering is given on to the one who pleases God.
  basis: stated
  grounds: he has given the business of gathering
  traces: [23955]
  verses: ["Ecc 2:26"]
- observation: 24049
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:26 'sinner' (H2398, a participle) is the one given the business of gathering, the part of the verse called a striving after wind.
  basis: stated
  grounds: to the sinner he has given
  traces: [23955]
  verses: ["Ecc 2:26"]
- observation: 24050
  step: 2.1
  item: pairing
  kind: pairing
  text: In Gal 2:17 'sinners' (G0268) is what those who endeavor are found to be, and 'sin' (G0266) stands in the question whether Christ is its servant.
  basis: stated
  grounds: is Christ then a servant of sin
  traces: [23951]
  verses: ["Gal 2:17"]
- observation: 24051
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 4:4 'skill' (H3788) in work is named with toil as coming from envy, and both are then called a striving after wind.
  basis: stated
  grounds: all skill in work
  traces: [23955]
  verses: ["Ecc 4:4"]
- observation: 24052
  step: 2.1
  item: pairing
  kind: pairing
  text: In Luk 13:24 'able' (ischyo, G2480) is negated: the many who seek will lack the strength to enter, set against the command to strive.
  basis: stated
  grounds: will not be able
  traces: [23951]
  verses: ["Luk 13:24"]

## verses

- reference: Ecc 2:17
  text: So I hated life, because what is done under the sun was grievous to me, for all is vanity and a striving after wind.
- reference: Isa 41:11
  text: Behold, all who are incensed against you shall be put to shame and confounded; those who strive against you shall be as nothing and shall perish.
- reference: Ecc 2:11
  text: Then I considered all that my hands had done and the toil I had expended in doing it, and behold, all was vanity and a striving after wind, and there was nothing to be gained under the sun.
- reference: Ecc 2:22
  text: What has a man from all the toil and striving of heart with which he toils beneath the sun?
- reference: Ecc 4:4
  text: Then I saw that all toil and all skill in work come from a man’s envy of his neighbor. This also is vanity and a striving after wind.
- reference: Ecc 4:6
  text: Better is a handful of quietness than two hands full of toil and a striving after wind.
- reference: Gal 2:17
  text: But if, in our endeavor to be justified in Christ, we too were found to be sinners, is Christ then a servant of sin? Certainly not!
- reference: Ecc 6:9
  text: Better is the sight of the eyes than the wandering of the appetite: this also is vanity and a striving after wind.
- reference: Isa 45:9
  text: “ Woe to him who strives with him who formed him, a pot among earthen pots! Does the clay say to him who forms it, ‘ What are you making?’ or ‘Your work has no handles ’?
- reference: Luk 13:24
  text: “ Strive to enter through the narrow door. For many, I tell you, will seek to enter and will not be able.
- reference: Hos 12:4
  text: He strove with the angel and prevailed; he wept and sought his favor. He met God at Bethel, and there God spoke with us —
- reference: Pro 28:4
  text: Those who forsake the law praise the wicked, but those who keep the law strive against them.
- reference: Psa 60:1
  text: To the choirmaster: according to Shushan Eduth. A Miktam of David; for instruction; when he strove with Aram-naharaim and with Aram-zobah, and when Joab on his return struck down twelve thousand of Edom in the Valley of Salt. O God, you have rejected us, broken our defenses; you have been angry; oh, restore us.
- reference: Gen 32:28
  text: Then he said, “Your name shall no longer be called Jacob, but Israel, for you have striven with God and with men, and have prevailed.”
- reference: Exo 21:22
  text: “When men strive together and hit a pregnant woman, so that her children come out, but there is no harm, the one who hit her shall surely be fined, as the woman’s husband shall impose on him, and he shall pay as the judges determine.
- reference: 1Th 2:17
  text: But since we were torn away from you, brothers, for a short time, in person not in heart, we endeavored the more eagerly and with great desire to see you face to face,
- reference: Ecc 2:26
  text: For to the one who pleases him God has given wisdom and knowledge and joy, but to the sinner he has given the business of gathering and collecting, only to give to one who pleases God. This also is vanity and a striving after wind.
- reference: Ecc 4:16
  text: There was no end of all the people, all of whom he led. Yet those who come later will not rejoice in him. Surely this also is vanity and a striving after wind.
- reference: Ecc 1:17
  text: And I applied my heart to know wisdom and to know madness and folly. I perceived that this also is but a striving after wind.
- reference: Ecc 1:14
  text: I have seen everything that is done under the sun, and behold, all is vanity and a striving after wind.
- reference: Heb 4:11
  text: Let us therefore strive to enter that rest, so that no one may fall by the same sort of disobedience.
- reference: 1Ti 4:10
  text: For to this end we toil and strive, because we have our hope set on the living God, who is the Savior of all people, especially of those who believe.
- reference: Heb 12:14
  text: Strive for peace with everyone, and for the holiness without which no one will see the Lord.

## measured

- package_chars: 37388
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "strive",
 "subgroup": "exertion toward an end",
 "observations": [
  {
   "observation": 24013,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24014,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24015,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24016,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24017,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24018,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24019,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24020,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24021,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24022,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24023,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24024,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24025,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24026,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24027,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24028,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24029,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24030,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24031,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24032,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24033,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24034,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24035,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24036,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24037,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24038,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24039,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24040,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24041,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24042,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24043,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24044,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24045,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24046,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24047,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24048,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24049,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24050,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24051,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24052,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ]
}
```
