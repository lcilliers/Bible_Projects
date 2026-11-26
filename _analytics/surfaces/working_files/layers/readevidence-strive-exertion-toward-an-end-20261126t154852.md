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

2026-11-26T15:48:52Z

## batch

- observations: 40
- left_after_this: 91
- evidence_in_scope: 132
- observations_in_scope: 135

## code_checks

- passes: true
- findings: {"unmarked": [], "no_node": [], "word_missing": [], "traced_dead": [], "duplicate_text": [], "b1_not_traced_by_a_sense": [], "sense_not_traced_by_2_1": [], "older_open": []}

## observations

- observation: 23933
  step: S1
  item: word-sense
  kind: term
  text: In 1Th 2:17 spoudazo (be eager, make every effort; aorist active, first plural) names the effort Paul and his companions made to see the Thessalonians again after being parted from them; the adverb 'the more eagerly' and the phrase 'with great desire' heighten it, and its goal is the infinitive 'to see you'.
  basis: stated
  grounds: we endeavored the more eagerly; to see you face to face
  traces: []
  verses: ["1Th 2:17"]
- observation: 23934
  step: S1
  item: word-sense
  kind: term
  text: In Gal 2:17 zeteo (seek, try to obtain; present active participle, plural) has the infinitive 'to be justified in Christ' as its goal, so the seeking is aimed at a standing before God rather than at finding a thing or person; the ESV renders the participle as the noun phrase 'our endeavor'.
  basis: read
  grounds: in our endeavor to be justified in Christ
  traces: []
  verses: ["Gal 2:17"]
- observation: 23935
  step: S1
  item: word-sense
  kind: term
  text: In Gen 32:28 sarah (contend, persevere; Qal perfect, second masculine singular) names Jacob's contending with God and with men, a struggle he came through, since the verse joins it to 'and have prevailed'; the verb is given as the reason for the new name Israel.
  basis: stated
  grounds: you have striven with God and with men; have prevailed; Israel
  traces: []
  verses: ["Gen 32:28"]
- observation: 23936
  step: S1
  item: word-sense
  kind: term
  text: In Isa 45:9 rib (contend, quarrel; Qal participle) names the one who disputes with his maker; the verse pictures it as clay questioning the potter about what he makes, so the striving here is a complaint raised against the one who formed him.
  basis: stated
  grounds: strives with him who formed him; Does the clay say
  traces: []
  verses: ["Isa 45:9"]
- observation: 23937
  step: S1
  item: word-sense
  kind: term
  text: In Luk 13:24 agonizomai (struggle, contend as in a contest; present imperative, second plural) is a command to struggle to get in, its goal the infinitive 'to enter through the narrow door', set against the many who will only seek to enter and fail.
  basis: stated
  grounds: Strive to enter through the narrow door; will seek to enter and will not be able
  traces: []
  verses: ["Luk 13:24"]
- observation: 23938
  step: S1
  item: word-sense
  kind: term
  text: In 1Ti 4:10 agonizomai (struggle, labour hard; present indicative, first plural) stands paired with 'toil' for the ongoing labour of Paul and his fellow workers 'to this end', and the verse gives its ground in their hope set on the living God.
  basis: stated
  grounds: we toil and strive; because we have our hope set on the living God
  traces: []
  verses: ["1Ti 4:10"]
- observation: 23939
  step: S1
  item: word-sense
  kind: face
  text: In Heb 12:14 dioko, whose usual sense is to chase or pursue a person, is a present imperative with the objects peace with everyone and holiness, rendered 'Strive for': the pursuit is of a state to be reached and held, not of a person, and the verse ties holiness to seeing the Lord.
  basis: read
  grounds: Strive for peace with everyone
  traces: []
  verses: ["Heb 12:14"]
- observation: 23940
  step: S1
  item: word-sense
  kind: term
  text: In 1Cor 14:12 zeteo (seek, aim at; present active imperative, second plural) takes the infinitive 'to excel' with the goal of building up the church, and the verse sets it after the readers' eagerness for manifestations of the Spirit, directing that eagerness to a goal.
  basis: stated
  grounds: strive to excel in building up the church; eager for manifestations of the Spirit
  traces: []
  verses: ["1Cor 14:12"]
- observation: 23941
  step: S1
  item: word-sense
  kind: term
  text: In Heb 4:11 spoudazo (be eager, make every effort; aorist subjunctive, first plural, a call to the hearers with the writer) has the goal 'to enter that rest', and the purpose clause sets it against falling by the same disobedience.
  basis: stated
  grounds: Let us therefore strive to enter that rest; so that no one may fall
  traces: []
  verses: ["Heb 4:11"]
- observation: 23942
  step: S1
  item: word-sense
  kind: term
  text: In Pro 28:4 garah (stir up strife; Hithpael imperfect, third masculine plural) is reflexive: those who keep the law rouse themselves against the wicked, set opposite those who forsake the law and praise them.
  basis: stated
  grounds: those who keep the law strive against them
  traces: []
  verses: ["Pro 28:4"]
- observation: 23943
  step: S1
  item: word-sense
  kind: term
  text: In Exo 21:22 natsah (struggle; Niphal imperfect, third masculine plural) is a physical fight between men, the Niphal with 'together' making it mutual, in a case of law where the fight causes harm to a pregnant woman.
  basis: stated
  grounds: When men strive together and hit a pregnant woman
  traces: []
  verses: ["Exo 21:22"]
- observation: 23944
  step: S1
  item: word-sense
  kind: face
  text: In Isa 41:11 rib is a noun in construct (strife, dispute) which the ESV renders as the verb phrase 'those who strive against you': the word names Israel's opponents by their quarrel with Israel, set beside those incensed against them, who will come to nothing.
  basis: read
  grounds: those who strive against you shall be as nothing
  traces: []
  verses: ["Isa 41:11"]
- observation: 23945
  step: S1
  item: word-sense
  kind: term
  text: In Ecc 1:14, 2:11, 2:17, 2:26, 4:4, 4:6 and 6:9 reut (longing, striving; a feminine noun in construct) is in each the phrase 'a striving after wind', set beside 'vanity' in six of them and beside 'toil' in 4:6: a reaching after what cannot be grasped, said of what is done under the sun.
  basis: stated
  grounds: a striving after wind; all is vanity; two hands full of toil
  traces: []
  verses: ["Ecc 1:14", "Ecc 2:11", "Ecc 2:17", "Ecc 2:26", "Ecc 4:4", "Ecc 4:6", "Ecc 6:9"]
- observation: 23946
  step: S1
  item: word-sense
  kind: term
  text: In Ecc 1:17 and Ecc 4:16 rayon (longing, striving; a masculine noun in construct) is in the phrase 'a striving after wind', said in 1:17 of applying the heart to know wisdom, madness and folly, and in 4:16 of a king's following that later ones will not rejoice in.
  basis: stated
  grounds: a striving after wind; I applied my heart to know wisdom; will not rejoice in him
  traces: []
  verses: ["Ecc 1:17", "Ecc 4:16"]
- observation: 23947
  step: S1
  item: word-sense
  kind: term
  text: In Ecc 2:22 rayon is joined to 'heart' and paired with 'toil' ('the toil and striving of heart'): here it is the effort a man's heart spends in his labour beneath the sun, in a question asking what he has from it.
  basis: stated
  grounds: all the toil and striving of heart; What has a man
  traces: []
  verses: ["Ecc 2:22"]
- observation: 23948
  step: S1
  item: word-sense
  kind: term
  text: In Psa 60:1, in the superscription, natsah (struggle; Hiphil infinitive construct) names David's warfare against Aram-naharaim and Aram-zobah, set beside Joab's striking down of Edom: a fight between peoples, giving the occasion of the psalm.
  basis: stated
  grounds: when he strove with Aram-naharaim and with Aram-zobah
  traces: []
  verses: ["Psa 60:1"]
- observation: 23949
  step: S1
  item: word-sense
  kind: face
  text: In Hos 12:4 sur, whose head sense in the lexicon is to rule or act as prince, is a Qal narrative verb rendered 'strove' and used of Jacob contending with the angel and prevailing, the same event Hos 12:3 tells with sarah; here it is a struggle with a heavenly being, not a ruling.
  basis: read
  grounds: He strove with the angel and prevailed
  traces: []
  verses: ["Hos 12:4"]
- observation: 23950
  step: S1
  item: word-sense
  kind: term
  text: In Hos 12:3 sarah (contend; Qal perfect, third masculine singular) names Jacob's contending with God in his manhood, set after his taking his brother by the heel in the womb; it recalls the struggle Gen 32:28 gives as the reason for the name Israel.
  basis: stated
  grounds: in his manhood he strove with God; took his brother by the heel
  traces: []
  verses: ["Hos 12:3"]
- observation: 23951
  step: 1.1
  item: group-definition
  kind: group
  text: Exertion toward a goal: effort spent to reach or to do something, in 1Th 2:17, Gal 2:17, Luk 13:24, 1Ti 4:10, Heb 12:14, 1Cor 14:12, Heb 4:11 and Ecc 2:22; the goal is named in each, a meeting, a standing before God, entry, peace and holiness, excelling, rest, or in Ecc 2:22 the labour itself.
  basis: read
  grounds: make every effort
  traces: [23933, 23934, 23937, 23938, 23939, 23940, 23941, 23947]
  verses: ["1Cor 14:12", "1Th 2:17", "1Ti 4:10", "Ecc 2:22", "Gal 2:17", "Heb 12:14", "Heb 4:11", "Luk 13:24"]
- observation: 23952
  step: 1.1
  item: group-definition
  kind: group
  text: Contention against an opponent: disputing with another or rousing oneself against another, in Isa 45:9 against one's maker, in Pro 28:4 by those who keep the law against the wicked, and in Isa 41:11 where Israel's opponents are named by their dispute with Israel.
  basis: read
  grounds: strife, controversy, dispute
  traces: [23936, 23942, 23944]
  verses: ["Isa 41:11", "Isa 45:9", "Pro 28:4"]
- observation: 23953
  step: 1.1
  item: group-definition
  kind: group
  text: Physical fighting: a bodily fight between men in Exo 21:22 and warfare between peoples in Psa 60:1, both with the verb natsah.
  basis: read
  grounds: to struggle
  traces: [23943, 23948]
  verses: ["Exo 21:22", "Psa 60:1"]
- observation: 23954
  step: 1.1
  item: group-definition
  kind: group
  text: Jacob's contending with God: the struggle with God, or with the angel, in which Jacob prevailed, told in Gen 32:28, Hos 12:3 and Hos 12:4 with sarah and sur.
  basis: read
  grounds: contend, have power, contend with, persist
  traces: [23935, 23949, 23950]
  verses: ["Gen 32:28", "Hos 12:3", "Hos 12:4"]
- observation: 23955
  step: 1.1
  item: group-definition
  kind: group
  text: A reaching after wind: in Ecc 1:14, Ecc 1:17, Ecc 2:11, Ecc 2:17, Ecc 2:26, Ecc 4:4, Ecc 4:6, Ecc 4:16 and Ecc 6:9 two related nouns, reut and rayon, name a striving after wind, a reaching after what gives nothing to hold.
  basis: read
  grounds: longing, striving
  traces: [23945, 23946]
  verses: ["Ecc 1:14", "Ecc 1:17", "Ecc 2:11", "Ecc 2:17", "Ecc 2:26", "Ecc 4:16", "Ecc 4:4", "Ecc 4:6", "Ecc 6:9"]
- observation: 23956
  step: 1.2
  item: strong-enrichment
  kind: enrichment
  text: Each code of this sense names effort toward a goal from its own side: spoudazo (G4704) eagerness and haste, agonizomai (G0075) struggle as in a contest, zeteo (G2212) seeking to obtain, dioko (G1377) pursuit pressed to a goal, and rayon (H7475) longing. The surface strive carries all four Greek codes, so Luk 13:24, Heb 12:14, 1Cor 14:12 and Heb 4:11 differ by code. The lexicon bears out the sense.
  basis: read
  grounds: to endeavor earnestly, strive, make every effort
  traces: [23951]
  verses: ["1Cor 14:12", "1Th 2:17", "1Ti 4:10", "Ecc 2:22", "Gal 2:17", "Heb 12:14", "Heb 4:11", "Luk 13:24"]
- observation: 23957
  step: 1.2
  item: strong-enrichment
  kind: enrichment
  text: rib as verb (H7378) and noun (H7379) covers contending in words or at law and quarrel; garah (H1624) in its Hithpael is to rouse oneself against another and engage in strife. The lexicon bears out a contention against another in Isa 45:9, Isa 41:11 and Pro 28:4; the surface strive carries both the noun H7379 and the verb H1624.
  basis: read
  grounds: strife, controversy, dispute
  traces: [23952]
  verses: ["Isa 41:11", "Isa 45:9", "Pro 28:4"]
- observation: 23958
  step: 1.2
  item: strong-enrichment
  kind: enrichment
  text: natsah (H5327A) is given only as to struggle, in the Niphal of Exo 21:22 and the Hiphil of Psa 60:1; the lexicon gives no more than struggle, so the bodily and armed nature of the fight comes from the verses. H3588A (ki, that, when) is the conjunction the surface carries in Exo 21:22 and adds no meaning to the sense.
  basis: read
  grounds: to struggle
  traces: [23953]
  verses: ["Exo 21:22", "Psa 60:1"]
- observation: 23959
  step: 1.2
  item: strong-enrichment
  kind: enrichment
  text: sarah (H8280) is to contend, persist and persevere, and its related words include Israel (H3478), the name Gen 32:28 explains. sur (H7786) has rule and reign as its head sense, but its range includes contend and prevail over, which Hos 12:4 uses. The lexicon bears out the sense for both codes, with sur lying nearer to ruling.
  basis: read
  grounds: contend, have power, contend with, persist
  traces: [23954]
  verses: ["Gen 32:28", "Hos 12:3", "Hos 12:4"]
- observation: 23960
  step: 1.2
  item: strong-enrichment
  kind: enrichment
  text: reut (H7469) and rayon (H7475) are given the same range, longing and striving, and their related words include words for thought (H7454, H7476) and for pasturing (H7462B). The lexicon bears out the sense of a reaching after in Ecc 1:14 and Ecc 1:17, and adds nothing on the wind it is joined with.
  basis: read
  grounds: longing, striving
  traces: [23955]
  verses: ["Ecc 1:14", "Ecc 1:17", "Ecc 2:11", "Ecc 2:17", "Ecc 2:26", "Ecc 4:16", "Ecc 4:4", "Ecc 4:6", "Ecc 6:9"]
- observation: 23961
  step: 2.1
  item: double-meaning
  kind: face
  text: In Exo 21:22 the surface strive stands on two codes at one position: natsah (H5327A, struggle, Niphal) and ki (H3588A, the conjunction 'when'), so the one English word holds both the opening conjunction and the verb of a fight between men.
  basis: read
  grounds: When men strive together
  traces: [23953]
  verses: ["Exo 21:22"]
- observation: 23962
  step: 2.1
  item: double-meaning
  kind: face
  text: In Pro 28:4 (garah, H1624, a Hithpael verb) and Isa 41:11 (rib, H7379, a noun in construct) the surface strive stands on two Hebrew codes of contention, each followed by the party opposed, 'them' and 'you'.
  basis: read
  grounds: strive against
  traces: [23952]
  verses: ["Isa 41:11", "Pro 28:4"]
- observation: 23963
  step: 2.1
  item: double-meaning
  kind: face
  text: In Luk 13:24, 1Ti 4:10, 1Cor 14:12, Heb 4:11 and Heb 12:14 the surface strive stands on four Greek codes, agonizomai (G0075), zeteo (G2212), spoudazo (G4704) and dioko (G1377), each with a goal as an infinitive or an object: one English word covers struggle, seeking, eagerness and pursuit.
  basis: read
  grounds: strive to enter
  traces: [23951]
  verses: ["1Cor 14:12", "1Ti 4:10", "Heb 12:14", "Heb 4:11", "Luk 13:24"]
- observation: 23964
  step: 2.1
  item: double-meaning
  kind: face
  text: In Ecc 1:14, 2:11, 2:17, 2:26, 4:4, 4:6 and 6:9 (reut, H7469) and in Ecc 1:17 and 4:16 (rayon, H7475) the surface striving stands in the same construct phrase with 'wind', so the two codes give one face in that phrase.
  basis: read
  grounds: a striving after wind
  traces: [23955]
  verses: ["Ecc 1:14", "Ecc 1:17", "Ecc 2:11", "Ecc 2:17", "Ecc 2:26", "Ecc 4:16", "Ecc 4:4", "Ecc 4:6", "Ecc 6:9"]
- observation: 23965
  step: 2.1
  item: double-meaning
  kind: face
  text: In Ecc 2:22 striving stands on rayon (H7475) in construct with 'heart' and joined to 'toil', with no 'wind': the code that gives the phrase with wind in Ecc 1:17 and 4:16 here names the effort of the heart in labour.
  basis: read
  grounds: striving of heart
  traces: [23951]
  verses: ["Ecc 2:22"]
- observation: 23966
  step: 2.1
  item: double-meaning
  kind: face
  text: In Psa 60:1 the surface strove stands on natsah (H5327A, a Hiphil infinitive) for David's warfare against Aram-naharaim and Aram-zobah, in the superscription.
  basis: read
  grounds: when he strove with Aram-naharaim
  traces: [23953]
  verses: ["Psa 60:1"]
- observation: 23967
  step: 2.1
  item: double-meaning
  kind: face
  text: In Hos 12:3 (sarah, H8280, with God) and Hos 12:4 (sur, H7786, with the angel) the surface strove stands on two different codes for the one struggle of Jacob, told in two lines that follow each other.
  basis: read
  grounds: strove with
  traces: [23954]
  verses: ["Hos 12:3", "Hos 12:4"]
- observation: 23968
  step: 2.1
  item: qualifier
  kind: pairing
  text: In 1Th 2:17 the comparative adverb 'more eagerly' (G4056) qualifies endeavored, and 'great' (G4183) qualifies 'desire', the noun of the phrase that goes with the verb; the negator 'not' (G3756) reaches 'in heart', set against 'in person', not the verb.
  basis: read
  grounds: the more eagerly and with great desire
  traces: [23951]
  verses: ["1Th 2:17"]
- observation: 23969
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Ecc 1:17, 2:26, 4:4, 4:16 and 6:9 the adverb 'also' (gam, H1571) stands in the clause that calls the case a striving after wind, adding it to the cases already called so; it reaches the clause, not the noun striving.
  basis: read
  grounds: this also is
  traces: [23955]
  verses: ["Ecc 1:17", "Ecc 2:26", "Ecc 4:16", "Ecc 4:4", "Ecc 6:9"]
- observation: 23970
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Ecc 4:16 'not' (H3808) negates 'rejoice', 'come later' (H0314) names those who will not rejoice, and 'yet' (H1571) sets this against the king's great following; none of them reaches striving.
  basis: read
  grounds: those who come later will not rejoice in him
  traces: []
  verses: ["Ecc 4:16"]
- observation: 23971
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Ecc 4:6 and 6:9 'better' (tov, H2896A) opens a comparison in which the striving after wind stands on the side judged the lesser: with two hands full of toil in 4:6, with the wandering of the appetite in 6:9.
  basis: read
  grounds: Better is a handful of quietness
  traces: [23955]
  verses: ["Ecc 4:6", "Ecc 6:9"]
- observation: 23972
  step: 2.1
  item: qualifier
  kind: pairing
  text: In Ecc 2:17, 2:22 and 2:26 the adjectives grievous (H7451A), toils (H6001B) and pleases (H2896A) qualify other words of their verses, what is done under the sun, the man who labours, and the one who pleases God; none reaches striving.
  basis: read
  grounds: was grievous to me
  traces: [23951, 23955]
  verses: ["Ecc 2:17", "Ecc 2:22", "Ecc 2:26"]

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
- reference: 1Cor 14:12
  text: So with yourselves, since you are eager for manifestations of the Spirit, strive to excel in building up the church.
- reference: Ecc 1:17
  text: And I applied my heart to know wisdom and to know madness and folly. I perceived that this also is but a striving after wind.
- reference: Ecc 1:14
  text: I have seen everything that is done under the sun, and behold, all is vanity and a striving after wind.
- reference: Heb 4:11
  text: Let us therefore strive to enter that rest, so that no one may fall by the same sort of disobedience.
- reference: 1Ti 4:10
  text: For to this end we toil and strive, because we have our hope set on the living God, who is the Savior of all people, especially of those who believe.
- reference: Hos 12:3
  text: In the womb he took his brother by the heel, and in his manhood he strove with God.
- reference: Heb 12:14
  text: Strive for peace with everyone, and for the holiness without which no one will see the Lord.

## measured

- package_chars: 43005
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEvidence",
 "collection": "strive",
 "subgroup": "exertion toward an end",
 "observations": [
  {
   "observation": 23933,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23934,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23935,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23936,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23937,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23938,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23939,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23940,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23941,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23942,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23943,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23944,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23945,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23946,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23947,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23948,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23949,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23950,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23951,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23952,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23953,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23954,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23955,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23956,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23957,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23958,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23959,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23960,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23961,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23962,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23963,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23964,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23965,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23966,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23967,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23968,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23969,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23970,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23971,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  },
  {
   "observation": 23972,
   "verdict": "true | repair",
   "why": "",
   "actions": []
  }
 ]
}
```
