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

2026-11-26T15:49:44Z

## batch

- observations: 40
- left_after_this: 51
- evidence_in_scope: 132
- observations_in_scope: 135

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 23973
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Gen 32:28 the negator 'no' with 'longer' (H3808, H5750) reaches 'be called Jacob', the old name, not the verb striven.
  basis: read
  grounds: no longer be called Jacob
  traces: [23954]
  verses: ["Gen 32:28"]
- observation: 23974
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Exo 21:22 'pregnant' (H2030A) qualifies the woman struck and 'no' (H3808) negates 'harm'; neither reaches strive.
  basis: read
  grounds: there is no harm
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 23975
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Hos 12:4 the adverb 'there' (H8033G) reaches 'spoke', placing God's speaking at Bethel; it does not reach strove.
  basis: read
  grounds: there God spoke with us
  traces: [23954]
  verses: ["Hos 12:4"]
- observation: 23976
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Luk 13:24 'narrow' (G4728) qualifies the door that is the goal of the striving; 'many' (G4183) names those who seek, and 'not' (G3756) negates 'be able' in their clause, not the command to strive.
  basis: read
  grounds: the narrow door
  traces: [23951]
  verses: ["Luk 13:24"]
- observation: 23977
  step: 2.1
  item: qualifier
  kind: pairing
  text: In 1Cor 14:12 'so' (G3779) opens the sentence and applies what went before to the readers; it reaches the whole sentence and not strive alone.
  basis: read
  grounds: So with yourselves
  traces: [23951]
  verses: ["1Cor 14:12"]
- observation: 23978
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Gal 2:17 'sinners' (G0268) is what those who endeavor are found to be, and 'not' (G3361) closes the verse as a denial of the question about Christ; neither reaches the endeavor.
  basis: read
  grounds: Certainly not
  traces: [23951]
  verses: ["Gal 2:17"]
- observation: 23979
  step: 2.1
  item: qualifier
  kind: pairing
  text: In 1Ti 4:10 'all' (G3956), 'especially' (G3122) and 'believe' (G4103) qualify the people of whom God is Savior, in the clause about him; none reaches strive.
  basis: read
  grounds: especially of those who believe
  traces: [23951]
  verses: ["1Ti 4:10"]
- observation: 23980
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Heb 12:14 'everyone' (G3956) gives the range of the peace that is pursued, and 'no one' (G3762) is the subject of 'will see', in the clause about holiness.
  basis: read
  grounds: peace with everyone
  traces: [23951]
  verses: ["Heb 12:14"]
- observation: 23981
  step: 2.1
  item: entity
  kind: pairing
  text: In Gen 32:28 and Hos 12:3 the striving is with God (elohim, H0430G), and in Gen 32:28 also with men (H0582); the one who strove is Jacob (H3290), named in Gen 32:28 and referred to by 'he' in Hos 12:3.
  basis: stated
  grounds: you have striven with God
  traces: [23954]
  verses: ["Gen 32:28", "Hos 12:3"]
- observation: 23982
  step: 2.1
  item: entity
  kind: pairing
  text: In Exo 21:22 those who strive are 'men' (H0582), not named, and a third party, a pregnant woman (H0802G), is struck by them; her husband is named after, as the one who sets the fine.
  basis: stated
  grounds: When men strive together and hit a pregnant woman
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 23983
  step: 2.1
  item: entity
  kind: pairing
  text: In Psa 60:1 the one who strove is David (H1732), named in the superscription with Joab (H3097G) and the peoples fought; God (H0430G) is addressed in the body of the verse, not named as a party of the fighting.
  basis: read
  grounds: A Miktam of David
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 23984
  step: 2.1
  item: entity
  kind: pairing
  text: In Ecc 2:22 and 2:26 the one who labours is 'a man' (adam, H0120G), in 2:26 set under God (H0430G), who gives to the one who pleases him; in Ecc 4:4 the neighbor (H7453) is the one envied.
  basis: stated
  grounds: What has a man from all the toil
  traces: [23951, 23955]
  verses: ["Ecc 2:22", "Ecc 2:26", "Ecc 4:4"]
- observation: 23985
  step: 2.1
  item: entity
  kind: pairing
  text: In Isa 41:11 those who strive are 'those' (H0582, men in construct with the noun of strife), the opponents of the one addressed as 'you'.
  basis: stated
  grounds: those who strive against you
  traces: [23952]
  verses: ["Isa 41:11"]
- observation: 23986
  step: 2.1
  item: entity
  kind: pairing
  text: In Gal 2:17 Christ (G5547) is named twice, as the one in whom justification is sought and as the subject of the question whether he serves sin.
  basis: stated
  grounds: is Christ then a servant of sin
  traces: [23951]
  verses: ["Gal 2:17"]
- observation: 23987
  step: 2.1
  item: entity
  kind: pairing
  text: In 1Th 2:17 the readers are addressed as 'brothers' (G0080), the ones from whom the writers were torn away and whom they made the effort to see.
  basis: stated
  grounds: torn away from you, brothers
  traces: [23951]
  verses: ["1Th 2:17"]
- observation: 23988
  step: 2.1
  item: entity
  kind: pairing
  text: In 1Ti 4:10 the living God (G2316) is the one on whom the hope of those who strive is set, and the Savior of all people (G0444); the strivers are 'we'.
  basis: stated
  grounds: the living God, who is the Savior of all people
  traces: [23951]
  verses: ["1Ti 4:10"]
- observation: 23989
  step: 2.1
  item: entity
  kind: pairing
  text: In Heb 12:14 the Lord (G2962G) is the one who will not be seen without holiness; the strivers are the readers addressed by the imperative.
  basis: stated
  grounds: no one will see the Lord
  traces: [23951]
  verses: ["Heb 12:14"]
- observation: 23990
  step: 2.1
  item: direction
  kind: relation
  text: In Gen 32:28 and Hos 12:3 the striving goes from Jacob toward God, with the preposition 'with' (H5973A, H0854); in Gen 32:28 it also goes toward men, and the verse closes on his prevailing.
  basis: stated
  grounds: you have striven with God
  traces: [23954]
  verses: ["Gen 32:28", "Hos 12:3"]
- observation: 23991
  step: 2.1
  item: direction
  kind: relation
  text: In Exo 21:22 the striving runs both ways between the men (Niphal, 'together'), and its harm passes to a third party, the woman they strike.
  basis: stated
  grounds: When men strive together and hit a pregnant woman
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 23992
  step: 2.1
  item: direction
  kind: relation
  text: In Psa 60:1 the striving goes from David against two peoples, Aram-naharaim and Aram-zobah, while the body of the verse turns to God in address.
  basis: stated
  grounds: when he strove with Aram-naharaim and with Aram-zobah
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 23993
  step: 2.1
  item: direction
  kind: relation
  text: In Isa 41:11 the striving comes from opponents against the one addressed, 'against you'.
  basis: stated
  grounds: those who strive against you
  traces: [23952]
  verses: ["Isa 41:11"]
- observation: 23994
  step: 2.1
  item: direction
  kind: relation
  text: In 1Th 2:17 the effort goes from the writers toward persons, the brothers they want to see face to face.
  basis: stated
  grounds: to see you face to face
  traces: [23951]
  verses: ["1Th 2:17"]
- observation: 23995
  step: 2.1
  item: direction
  kind: relation
  text: In Gal 2:17, 1Ti 4:10 and Heb 12:14 the effort goes toward an end and against no party: justification in Christ, 'this end' with hope set on God, and peace with everyone with the holiness without which the Lord is not seen.
  basis: read
  grounds: in our endeavor to be justified in Christ
  traces: [23951]
  verses: ["1Ti 4:10", "Gal 2:17", "Heb 12:14"]
- observation: 23996
  step: 2.1
  item: direction
  kind: relation
  text: In Ecc 2:22, 2:26 and 4:4 the striving is directed at no party: it is a man's own labour in 2:22, the business God gives to the sinner in 2:26, and work that comes from a man's envy of his neighbor in 4:4.
  basis: read
  grounds: What has a man from all the toil
  traces: [23951, 23955]
  verses: ["Ecc 2:22", "Ecc 2:26", "Ecc 4:4"]
- observation: 23997
  step: 2.1
  item: pairing
  kind: pairing
  text: In Psa 60:1 'angry' (anaph, H0599) is said of God toward his people in the prayer of the verse, while 'strove' stands in the superscription for David's wars; the two words lie in different parts of the verse.
  basis: read
  grounds: you have been angry
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 23998
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 41:11 'incensed' (H2734) and 'those who strive against you' are two parallel names for the same opponents, each clause with its own outcome, shame and perishing.
  basis: read
  grounds: all who are incensed against you
  traces: [23952]
  verses: ["Isa 41:11"]
- observation: 23999
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 6:9 'wandering' (H1980I, an infinitive) of the appetite stands on the lesser side of the comparison, and the same clause then calls it a striving after wind.
  basis: read
  grounds: the wandering of the appetite
  traces: [23955]
  verses: ["Ecc 6:9"]
- observation: 24000
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Ti 4:10 'believe' (G4103) names those of whom God is especially Savior, in the clause that gives the ground of the toil and striving.
  basis: read
  grounds: especially of those who believe
  traces: [23951]
  verses: ["1Ti 4:10"]
- observation: 24001
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 21:22 'harm' (two codes, H0611 and H1961) is negated: the case set out is a fight that brings the birth but no further harm, which decides the penalty.
  basis: read
  grounds: but there is no harm
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 24002
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:11 'gained' (yitron, H3504) follows the striving after wind and is negated: the toil under the sun is said to leave no gain.
  basis: stated
  grounds: nothing to be gained under the sun
  traces: [23955]
  verses: ["Ecc 2:11"]
- observation: 24003
  step: 2.1
  item: pairing
  kind: pairing
  text: In Gen 32:28 'called' (H0559, Niphal) gives the renaming of Jacob, and the clause with 'striven' is joined to it by 'for' as its reason.
  basis: stated
  grounds: Your name shall no longer be called Jacob
  traces: [23954]
  verses: ["Gen 32:28"]
- observation: 24004
  step: 2.1
  item: pairing
  kind: pairing
  text: In Pro 28:4 'praise' (H1984B) of the wicked by those who forsake the law is set opposite the striving against the wicked by those who keep it.
  basis: stated
  grounds: Those who forsake the law praise the wicked
  traces: [23952]
  verses: ["Pro 28:4"]
- observation: 24005
  step: 2.1
  item: pairing
  kind: pairing
  text: In Exo 21:22 'judges' (H6414) set the payment due after the fight between the men; the word stands at the close of the case, not with strive.
  basis: stated
  grounds: he shall pay as the judges determine
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 24006
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 41:11 'confounded' (H3637) is the outcome for the incensed, in the clause parallel to the one where those who strive against Israel come to nothing.
  basis: stated
  grounds: put to shame and confounded
  traces: [23952]
  verses: ["Isa 41:11"]
- observation: 24007
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 2:26 'pleases' (H2896A, H6440G) and 'joy' (H8057) belong to the one God favours, who receives wisdom, knowledge and joy, set against the sinner's business of gathering, which is called a striving after wind.
  basis: stated
  grounds: wisdom and knowledge and joy
  traces: [23955]
  verses: ["Ecc 2:26"]
- observation: 24008
  step: 2.1
  item: pairing
  kind: pairing
  text: In Hos 12:4 'favor' (H2603A, Hithpael) follows the striving: after prevailing, Jacob wept and sought favor.
  basis: stated
  grounds: he wept and sought his favor
  traces: [23954]
  verses: ["Hos 12:4"]
- observation: 24009
  step: 2.1
  item: pairing
  kind: pairing
  text: In Ecc 6:9 'appetite' (nephesh, H5315L) is the one whose wandering is set below the sight of the eyes and called a striving after wind.
  basis: stated
  grounds: the wandering of the appetite: this also is vanity
  traces: [23955]
  verses: ["Ecc 6:9"]
- observation: 24010
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Cor 14:12 'eager' (zelotes, G2207) names the readers' eagerness for manifestations of the Spirit, and the imperative 'strive' that follows turns it to building up the church.
  basis: read
  grounds: since you are eager for manifestations of the Spirit
  traces: [23951]
  verses: ["1Cor 14:12"]
- observation: 24011
  step: 2.1
  item: pairing
  kind: pairing
  text: In 1Th 2:17 'desire' (epithymia, G1939) qualified by 'great' goes with endeavored in a prepositional phrase, naming what went with the effort to see the readers.
  basis: read
  grounds: with great desire to see you
  traces: [23951]
  verses: ["1Th 2:17"]
- observation: 24012
  step: 2.1
  item: pairing
  kind: pairing
  text: In Isa 41:11 'perish' (H0006) is the end of those who strive against Israel, after 'shall be as nothing'.
  basis: stated
  grounds: shall be as nothing and shall perish
  traces: [23952]
  verses: ["Isa 41:11"]

## verses

- reference: Isa 41:11
  text: Behold, all who are incensed against you shall be put to shame and confounded; those who strive against you shall be as nothing and shall perish.
- reference: Ecc 2:11
  text: Then I considered all that my hands had done and the toil I had expended in doing it, and behold, all was vanity and a striving after wind, and there was nothing to be gained under the sun.
- reference: Ecc 2:22
  text: What has a man from all the toil and striving of heart with which he toils beneath the sun?
- reference: Ecc 4:4
  text: Then I saw that all toil and all skill in work come from a man’s envy of his neighbor. This also is vanity and a striving after wind.
- reference: Gal 2:17
  text: But if, in our endeavor to be justified in Christ, we too were found to be sinners, is Christ then a servant of sin? Certainly not!
- reference: Ecc 6:9
  text: Better is the sight of the eyes than the wandering of the appetite: this also is vanity and a striving after wind.
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
- reference: 1Cor 14:12
  text: So with yourselves, since you are eager for manifestations of the Spirit, strive to excel in building up the church.
- reference: 1Ti 4:10
  text: For to this end we toil and strive, because we have our hope set on the living God, who is the Savior of all people, especially of those who believe.
- reference: Hos 12:3
  text: In the womb he took his brother by the heel, and in his manhood he strove with God.
- reference: Heb 12:14
  text: Strive for peace with everyone, and for the holiness without which no one will see the Lord.

## measured

- package_chars: 37013
- seconds: 0.01

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "strive",
 "subgroup": "exertion toward an end",
 "observations": [
  {
   "observation": 23973,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23974,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23975,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23976,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23977,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23978,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23979,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23980,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23981,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23982,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23983,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23984,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23985,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23986,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23987,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23988,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23989,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23990,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23991,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23992,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23993,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23994,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23995,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23996,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23997,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23998,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23999,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24000,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24001,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24002,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24003,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24004,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24005,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24006,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24007,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24008,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24009,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24010,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24011,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 24012,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ]
}
```
