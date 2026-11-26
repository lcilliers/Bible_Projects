# ReadStructure -- strive / going after -- step 2.1

## What to do

Step 2.1, the structure of one subgroup (stage 1, B3): what stands with the subgroup's words in each verse, read from the stored structure. One item at a time: double-meaning (a surface with more than one code), qualifier (negators and the word each reaches, adjectives, adverbs, prepositional qualifiers), entity (who is named or referred to), direction (from whom to whom, by the grammar), pairing (one row for each partner collection: its words in the verses shared with the subgroup). Nothing here says what anything does for the inner being; that begins at step 3.1.

Read:
- Take one row at a time (`rows`): what it asks, its occurrences (`as`: member, the subgroup's word; partner, the other word), and its verses.
- Read each verse (`verses`) from its stored structure, one line for each word: * marks an occurrence of the subgroup; then the position, surface, Strong's code and morph, and what the pairing makes of the word (its type, the qualifier it carries, a negator, a party, the collections of a word of another collection). Nothing is evaluated that is not stored.
- Where each word stands: its side and distance from the subgroup's word, from the positions. Adjacency is not scope: a negator or qualifier is read for the word it reaches by the grammar.
- A pairing row shows the WordNet control for its partner collection: a pairing WordNet gives and the verses do not show is one to look for; a pairing only the verses show has no control.
- Differences in meaning are read from the base data (the Strong's code, the morph, the construction), not from the English alone. The subgroup's 1.1 senses (`senses`) are what the findings build on.

Write:
- Fill `answer.rows`: for each row, disposition observed with its `findings`, or none with its `reason` (where the row allows none: nothing of the item stands with the subgroup in its verses).
- One finding for each distinct thing the structure shows; the same finding in several verses is ONE finding naming all its occurrences; a verse that shows something different is its own finding. Together the findings name every occurrence of the row (occurrence ids or verse references), each in one finding.
- kind: as the template gives it (pairing; relation for direction; face for double-meaning). obs_text: concise; names the verses it holds in, as the package writes the references (for example Act 18:4); states what the structure shows (which word, where it stands, what it reaches or gives by the grammar); never a verse restated, never what it does for the inner being.
- basis: stated (the verse says it) or read (read from the structure), with `grounds`: words copied exactly from the verses it is tied to (the record checks them).
- Each subgroup's surface has its own finding; none joins two subgroups. A data error is named in grounds, not fixed.
- `older`: answer each older observation shown under the row, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` ["this"] or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` and `reason`), defer (with `collection`, `nature`, `finding`). One listed under another row is answered there.
- Where a reading, sense, enrichment or finding holds every occurrence of the row's subject, `occurrences` may be "all": the recorder names them.
- Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing written; correct the answer until it finds none, then -Action RecordStructure -File <the answer file>. The record refuses the whole file on any fault and lists every fault.

## Refused when (by rule)

- DA-02: belongs to collection; the nodes do not carry the collections
- IB-07: is not marked evidence: an inner-being observation traces to evidence; an observation does not trace itself
- LR-01: is not closed (every row answered
- LR-02: the text names none of them; names its grounds in the words of the verse; are not words of the lexicon entries; are not words of the verses; the data holds no occurrence for this aspect; names the occurrences it is about; names no occurrence (fill occurrences; are already in another sense; are in no sense; no occurrence to adopt for
- LR-03: cannot be recorded as none; none needs its reason
- PC-01: is not a step of the layered reading; is not a live subgroup of; no live collection; has no live subgroup; -Item must be one of; cannot read ;  are required;  is required
- PC-02: answer (its `command` must be; is a list of {observation, action, reason; the answer holds no ; (fill.senses): at least one; this is not the answer of a read
- PC-03: not a ledger row of; is not a 2.1 row of subgroup; occurrences that are not occurrences of; is not an older live observation on the occurrences of this row; is not an open old observation of this subgroup; adopt names a live observation; a deferral names a live collection; has no matching live verse_lexical row; both must be different live observations;  is not an occurrence of ; is not a live observation; is not a live node; does not exist;  is not a ; merge names a live observation to keep; defer names a live collection
- PC-04: kind must be one of; basis must be one of; role must be one of; route must be one of; tag must be one of; stage must be one of; nature must be one of; disposition must be observed; is not a node role; cannot be modified (allowed:; not in live cfg_enum ib_observation; , the item takes ; action is one of; names its marker, nature one of
- PC-05: only an open or an unvalidated row is recorded;  row is answered by its own command; the evidence validation of ; has no open row; is open; other items are; its group is retired or missing; carry names a LATER step of; the loop is for one subgroup at a time; partner collection 
- PC-06:  took more than 
- PC-07: cfg_setting layer.reading is missing; cfg_setting layer.scan; layer.reading step ; (apply iba/app/migration/archive/; the code is ahead of the config; have no nature in cfg_setting layer.reading; the read names rule(s) not active; is empty: run install_nature; are not ib_observation.tag values;  is missing
- RG-06: carries its route; this item takes no route
- RW-01: needs its reason, in words; say in words what was checked; say what it states that the existing record does not; state the finding the collection is to close; say in words which words it relies on; say in words why the word supports no finding; is the last word node of observation; already holds that occurrence: drop the node instead; its occurrence is on no live node of; carry gives its reason in words
- RW-03: is already live as observation; the same text as; a merge is for the same description
- RW-04: restates the verse; the observation text is missing or under; is a bare negation with no actual content; is not the ESV's wording
- RW-09: adopt needs its reason in words
- RW-12: morph_code is empty but; ) has no 
- RW-13: are still open in the ledger; have no answer in fill.older; its fate is not recorded; is not in the change log of observation; the change log does not show it
- RW-14: the statement used more than
- VA-03: name the carrying observations; the mapping is stated in words; occurrence(s) are on no node of; not carried needs its reason
- VA-04: only an observation that is neither is deleted here; repair those traces first
- VA-05: is an inner-being finding (its nodes carry an inner-being role); a deferred observation is marked now

## Limits

- grounds and every reason: characters at least: 10
- observation text: characters at least: 40
- consecutive verse words a text may copy, at most: 7

## The rules

- RG-14 morph-read: Morph is read, not carried: where occurrences of a word show different stems or voices, record whether the subject does, undergoes or causes the act.
- RG-16 homonym-and-data-error: A word that is only a homonym or a name, with no meaningful context, is recorded as such (tag no-human-context) and left. Data errors found while reading are flagged (tag data-error), not fixed in the reading.
- RG-21 grain: A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- RO11 one-row-per-code: One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- RW-03 no-duplicates-multi-node: One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- RW-04 concise-verse-specific: Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- RW-08 slants-own-rows: Where the evidence points to more than one reading, each is its own observation with its own evidence.
- RW-09 reread-builds-on-prior: A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- RW-11 missing-is-named: Missing data in the base extract is named as a gap, never substituted from memory or outside knowledge.
- RW-13 older-observations-answered-at-record: Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- RS-04 existing-checked-accept-modify-delete: When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- LR-02 nodes-are-built-from-the-data: The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
- LR-03 none-needs-a-permitted-reason: An aspect is recorded as none only where its item allows it (cfg_setting layer.reading none_allowed) and with its reason in words. A group definition and a group's Strong's enrichment are always observed.
- DA-02 a-node-per-occurrence-with-its-surfaces-collection: A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope (B:130), is not written and is listed.
- VA-03 consumption-is-verified-before-deletion: An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- VA-04 neither-evidence-nor-inner-being-is-deleted: An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.
- IB-07 inner-being-observations-trace-to-evidence: Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or on a live inner-being observation that itself traces to evidence (the trace chain of stage 4: a 3.2 behaviour traces the 3.1 elements it gathers, a 3.3 match the 3.1 and 3.2 observations it comes from; at most three links), unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed.
- LR-01 a-step-opens-on-gates-and-derives-its-ledger: A step of the layered reading opens only when the grouping is finished (every surface placed in a subgroup or isolated with its reason, every subgroup holding a surface) and the previous step is closed; with -Subgroup the needs and gates are judged for that subgroup alone (#2538). Step S1 is read after the grouping; step 1.1 needs step S1 closed: every word of the subgroup (surface and lettered Strong's code) answered and validated. Opening derives one ledger row for each aspect the data demands (cfg_setting layer.reading); an aspect the data no longer demands is retired, a new one is added, and a second open changes nothing.
- PC-01 the-command-names-a-live-unit: A read or record command names a live collection, a live subgroup of it where the read is by subgroup, and a step or item the layered reading knows. A command that names one that does not exist is refused and writes nothing.
- PC-02 the-answer-is-the-packet-form: An answer is the output form its read wrote: the `command` of that read; every entry an object, or a list, where the form has one; each field in its place with its type (a key unique in the answer, a text, a reason in words); each item answered once; and at least one entry where the form asks for entries. A file in another shape is refused whole and nothing is written.
- PC-03 names-are-those-the-packet-offers: Every ledger row, occurrence, observation, sense, node, verse and collection an answer names is one the packet offered for this unit, or a key the answer itself defines, and is live in the database. A name outside them is refused.
- PC-04 values-from-the-allowed-lists: Every coded value of an answer (kind, basis, item, part, role, route, mode, polarity, flag type, disposition, verdict, action, nature, stage, status) is one of the values the configuration allows for it (cfg_enum, cfg_setting layer.reading, reading.observation_items, validate.reading), as the packet lists them. Any other value is refused.
- PC-05 the-unit-is-at-its-step: A read or record runs only where the ledger has its unit at that step: the row open, or answered and not yet validated, and the steps before it closed (S1 before 1.1; the 2.1 rows before the sweep; the sweep before the evidence validation; its gate before 3.1; every subgroup through 3.1 before 3.2). Out of order it is refused, and the message names what comes first.
- PC-06 within-the-configured-limits: A read writes its packet within the time and size the configuration sets (cfg_setting layer.read_types: limits, package_max_chars, read_max_seconds). A read that would exceed them is refused, nothing is written, and the limit is named.
- PC-07 the-config-the-code-needs-is-present: The code of the reading runs only where the configuration it reads is in place (the settings, steps, items, natures, enums and rules it names). Where the code is ahead of the configuration, the command is refused and names what is missing.
- RG-06 parties-and-route: Record the parties: who bears the act, who causes it, who is acted on (source, target, impact, purpose), and the route (cfg_enum observation_route), whose meaning is cfg_behaviour_rule 72 (route-verses-hib-other-beings-data-only): A another being in its own right, B another being with the human inner being, C no bearing, data only; a verse may take A and B. A non-human being is never itself a HIB; a collective stays one HIB; an implied party is named as referential, never asserted.
- RW-01 changed-only-by-reading: No observation is changed except by a reading, and every change is recorded with its reason. An observation no longer supported by the verse is soft-deleted, with the reason.
- RW-12 marker-and-node-columns-at-creation: An observation is created with its marker (ib_observation.nature, from the item answered, cfg_setting layer.reading items.<item>.nature; a finding file never sets it) and every word node with the columns of layer.reading node_required. A column the data cannot give (layer.reading node_gap_columns: an empty morph in the source row, a surface with no placement in the collection index) is left empty and its reason is kept on the node (disposition_note); any other missing column refuses the whole file and nothing is written. A trace to a deleted observation is refused (IB-07).
- RW-14 every-lookup-is-pinpointed: A lookup of related data in the build or the validation is by an indexed column and takes a chunk of ids (cfg_setting layer.scan chunk); none runs once for each item of a list, and a statement that uses more work than layer.scan max_vm_ops is stopped and named, nothing written (lib/scanguard.py). The tests refuse a statement of the build whose query plan scans a table (layer.scan scan_ok lists the temporary tables a statement may scan).
- VA-05 the-marker-follows-content-not-stage: Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being, based on evidence, a building block of the stage 5 claims. The marker (ib_observation.nature) follows the content and purpose of the observation, never its stage (RS-04): an observation of any stage may be inner being when it traces to evidence. One that states both is split. The marker is set when the observation is created, by the item that is answered (cfg_setting layer.reading items.<item>.nature); a finding file never sets it; the validation changes it only where the content shows the item's nature does not hold.

## item

pairing

## made

2026-11-26T16:13:20Z

## batch

- rows: 4
- rows_left_after_this: 42

## senses

- sense: 24107
  text: Chasing to overtake: running after a person, band or army to overtake, capture or strike them, in Gen 14:15, Exo 14:9, Jos 10:19, Judg 4:16, Judg 20:45, Num 14:45, 1Sa 30:8, 2Sa 2:19, 2Ki 25:5 and the many other battle and flight narratives.
  verses: ["Gen.35.5", "Exod.14.4", "Josh.8.16", "Josh.10.19", "2Sam.17.1", "2Sam.20.6", "2Sam.20.7", "2Sam.20.13", "Gen.14.15", "Gen.31.23", "Exod.14.8", "Exod.14.9", "Exod.14.23", "Deut.11.4", "Josh.8.24", "Josh.2.7", "Josh.8.17", "Josh.24.6", "Judg.7.23", "Judg.20.43", "Judg.8.12", "Judg.4.16", "Judg.7.25", "Judg.1.6", "1Sam.23.25", "1Sam.30.10", "1Sam.17.52", "1Sam.7.11", "2Sam.20.10", "2Sam.2.28", "2Sam.2.19", "2Sam.2.24", "2Sam.22.38", "1Kgs.20.20", "2Kgs.9.27", "2Kgs.25.5", "2Chr.14.13", "2Chr.13.19", "Ps.18.37", "Jer.39.5", "Jer.52.8", "Josh.2.5", "1Sam.26.18", "1Sam.30.8", "1Sam.24.14", "2Sam.24.13", "Hos.8.3", "Judg.20.45", "Num.14.45"]
- sense: 24108
  text: Hounding to destroy: pursuit aimed at a person's life, standing or the weak, driven in some verses by desire or anger, in Exo 15:9, Deu 19:6, 1Sa 25:29, Psa 7:5, Psa 71:11, Psa 109:16, Psa 143:3, Job 19:22, Amo 1:11, Lam 3:43 and Rev 12:13.
  verses: ["Deut.19.6", "Amos.1.11", "Ps.143.3", "Ps.109.16", "Lam.3.43", "Exod.15.9", "1Sam.25.29", "Job.19.28", "Job.19.22", "Ps.71.11", "Ps.7.5", "Rev.12.13"]
- sense: 24109
  text: Pursuit by God or by what is not a person: God pursuing with tempest, sword or flood (Psa 83:15, Jer 29:18, Lam 3:66, Nah 1:8, Job 13:25), and curses, diseases, blood and the sword as pursuers (Deu 28:22, Deu 28:45, Eze 35:6, Jer 48:2), with honor chased off in Job 30:15.
  verses: ["Jer.48.2", "Job.13.25", "Ps.83.15", "Jer.29.18", "Lam.3.66", "Nah.1.8", "Deut.28.22", "Deut.28.45", "Ezek.35.6", "Job.30.15"]
- sense: 24110
  text: Pursuit of a good: going after righteousness, peace, love and the virtues as an aim, in Rom 9:30, Rom 9:31, Rom 14:19, 1Cor 14:1, 1Ti 6:11, 2Ti 2:22, 1Pe 3:11, Psa 34:14 and Isa 51:1.
  verses: ["Rom.9.31", "Rom.14.19", "1Cor.14.1", "1Tim.6.11", "2Tim.2.22", "1Pet.3.11", "Rom.9.30", "Ps.34.14", "Isa.51.1"]
- sense: 24111
  text: Going after a forbidden desire: the cities of Jude 7 going after other flesh, and the wife of Hos 2:7 chasing her lovers without reaching them.
  verses: ["Jude.1.7", "Hos.2.7"]

## verses

- reference: Gen 35:5
  text: And as they journeyed, a terror from God fell upon the cities that were around them, so that they did not pursue the sons of Jacob.
  words: [" 0 journeyed H5265 HVqw3mp", " 1 terror H2847 HNcfsc | word of another collection; collections fear", " 1 terror H1961 HVqw3ms | word of another collection; collections fear", " 2 god H0430G HNcmpa | entity (divine); party divine", " 3 upon H5921A HR", " 4 cities H5892B HNcmpa", " 4 [the] H9009 HTd", " 5 that H0834A HTr | connective", " 6 around H5439G HNcfpc", " 7 not H3808 HTn | negator; qualifier negator; negator", "*8 pursue H7291 HVqp3cp | member of this collection", " 8 them H9038 HSp3bp", " 8 and H9002 HC", "*8 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 9 sons H1121A HNcmpc", " 10 jacob H3290 HNpm | entity (human); party human"]
- reference: Judg 1:6
  text: Adoni-bezek fled, but they pursued him and caught him and cut off his thumbs and his big toes.
  words: [" 0 adoni-bezek H0137 HNpm | entity (human); party human", " 1 fled H5127 HVqw3ms | word of another collection; collections escape", "*2 pursued H7291 HVqw3mp | member of this collection", "*2 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 3 caught H0270 HVqw3mp | word of another collection; collections snatch", " 3 him H9033 HSp3ms", " 4 cut off H7112 HVpw3mp", " 4 cut off H0853 HTo", " 4 him H9033 HSp3ms", " 5 thumbs H0931 HNcfpc", " 5 thumbs H0853 HTo", " 5 thumbs H3027G HNcbdc", " 6 his H9023 HSp3ms", " 7 big toes H7272 HNcfdc", " 7 and H9002 HC | connective", " 7 his H9023 HSp3ms"]
- reference: Judg 8:12
  text: And Zebah and Zalmunna fled, and he pursued them and captured the two kings of Midian, Zebah and Zalmunna, and he threw all the army into a panic.
  words: [" 0 zebah H2078 HNpm | entity (human); party human", " 1 zalmunna H6759 HNpm | entity (human); party human", " 1 and H9002 HC | connective", " 2 fled H5127 HVqw3mp | word of another collection; collections escape", "*3 pursued H7291 HVqw3ms | member of this collection", "*3 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 4 captured H3920 HVqw3ms", " 4 them H9038 HSp3mp", " 5 two H8147 HNcbdc", " 5 two H0853 HTo", " 6 kings H4428G HNcmpc", " 7 midian H4080H HNpl", " 8 zebah H2078 HNpm | entity (human); party human", " 8 zebah H0853 HTo", " 9 zalmunna H6759 HNpm | entity (human); party human", " 9 zalmunna H0853 HTo", " 9 and H9002 HC | connective", " 10 all H3605 HNcmsc", " 10 and H9002 HC | connective", " 11 army H4264 HNcfsa", " 11 [the] H9009 HTd", " 12 panic H2729 HVhp3ms | word of another collection; collections fear"]
- reference: Judg 20:45
  text: And they turned and fled toward the wilderness to the rock of Rimmon. Five thousand men of them were cut down in the highways. And they were pursued hard to Gidom, and 2,000 men of them were struck down.
  words: [" 0 turned H6437G HVqw3mp | word of another collection; collections turn", " 1 fled H5127 HVqw3mp | word of another collection; collections escape", " 2 wilderness H4057B HNcmsa", " 2 [the] H9009 HTd", " 3 to H0413 HR", " 4 rock H5553H HNcmsc", " 4 [to] H9011 HSd", " 5 rimmon H7417C HNpl", " 5 [the] H9009 HTd", " 6 five H2568 HNcbsc", " 7 thousand H0505G HNcbpa", " 8 men H0376G HNcmsa | entity (human); party human", " 9 cut down H5953B HVpw3mp", " 10 highways H4546 HNcfpa", " 10 in/on/with H9003 HRd", " 10 him H9033 HSp3ms", "*11 pursued H1692 HVhw3mp | member of this collection", " 12 hard H0310A HAcmpc | word of another collection; qualifier morph: adjective; collections hard", " 13 gidom H1440 HNpl", " 13 him H9033 HSp3ms", " 13 gidom H5704 HR", " 14 2,000 H0505G HNcbda", " 14 2,000 H4480A HRd", " 14 him H9033 HSp3ms", " 15 men H0376G HNcmsa | entity (human); party human", " 16 struck down H5221 HVhw3mp"]
- reference: 1Sa 26:18
  text: And he said, “ Why does my lord pursue after his servant? For what have I done? What evil is on my hands?
  words: [" 0 said H0559 HVqw3ms", " 1 why H4100 HPi", " 1 to/for H9005 HR", " 1 why H2088 HTm", " 2 lord H0113 HNcmsc", "*3 pursue H7291 HVqrmsa | member of this collection", " 3 my H9020 HSp1bs", " 4 after H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 5 servant H5650 HNcmsc | entity (human); party human", " 6 for H3588A HTc | connective", " 6 his H9023 HSp3ms", " 7 what H4100 HPi", " 8 done H6213A HVqp1cs", " 9 what H4100 HPi", " 9 and H9002 HC | connective", " 10 evil H7451I HNcfsa | word of another collection; collections evildoer", " 10 my H9020 HSp1bs", " 11 hands H3027G HNcbsc", " 11 in/on/with H9003 HR"]
- reference: 1Sa 30:10
  text: But David pursued, he and four hundred men. Two hundred stayed behind, who were too exhausted to cross the brook Besor.
  words: [" 0 david H1732 HNpm | entity (human); party human", "*1 pursued H7291 HVqw3ms | member of this collection", " 2 he H1931 HPp3ms", " 3 four H0702 HNcbsa", " 3 and H9002 HC | connective", " 4 hundred H3967 HNcfpa", " 5 men H0376G HNcmsa | entity (human); party human", " 6 two hundred H3967 HNcfda", " 7 stayed behind H5975G HVqw3mp", " 8 who H0834A HTr | connective", " 8 who H0376G HNcmsa | entity (human); party human", " 9 exhausted H6296 HVpp3cp | word of another collection; collections faint", " 10 cross H5674A HVqcc", " 10 from H9006 HR", " 11 brook H5158N HNcmsc", " 11 brook H0853 HTo", " 12 besor H1308 HNpl", " 12 [the] H9009 HTd"]
- reference: 2Sa 20:6
  text: And David said to Abishai, “ Now Sheba the son of Bichri will do us more harm than Absalom. Take your lord’s servants and pursue him, lest he get himself to fortified cities and escape from us.”
  words: [" 0 david H1732 HNpm | entity (human); party human", " 1 said H0559 HVqw3ms", " 2 to H0413 HR", " 3 abishai H0052 HNpm | entity (human); party human", " 4 now H6258 HD | qualifier candidate; qualifier morph: adverb", " 5 sheba H7652A HNpm | entity (human); party human", " 5 to/for H9005 HRd", " 5 us H9035 HSp1bp", " 6 son H1121A HNcmsc", " 7 bichri H1075 HNpm | entity (human); party human", " 8 more harm H7489A HVqi3ms", " 9 than H4480A HR", " 10 absalom H0053 HNpm | entity (human); party human", " 11 take H3947G HVqv2ms | word of another collection; collections snatch", " 11 take H0859A HPp2ms | word of another collection; collections snatch", " 12 lord’s H0113 HNcmpc", " 13 servants H5650 HNcmpc | entity (human); party human", " 13 servants H0853 HTo", "*14 pursue H7291 HVqv2ms | member of this collection", " 14 your H9021 HSp2ms", "*14 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 15 lest H6435 HTc | connective", " 15 him H9033 HSp3ms", " 16 get H4672 HVqp3ms", " 17 fortified H1219 HAafpa | word of another collection; qualifier morph: adjective; collections guard", " 18 cities H5892B HNcmpa", " 18 to/for H9005 HRd", " 18 him H9033 HSp3ms", " 19 escape H5337 HVhq3ms | word of another collection; collections escape", " 20 us H5869J HNcfsc", " 20 our H9025 HSp1bp"]
- reference: 2Sa 24:13
  text: So Gad came to David and told him, and said to him, “Shall three years of famine come to you in your land? Or will you flee three months before your foes while they pursue you? Or shall there be three days ’ pestilence in your land? Now consider, and decide what answer I shall return to him who sent me.”
  words: [" 0 gad H1410H HNpm | entity (human); party human", " 1 came H0935G HVqw3ms", " 2 to H0413 HR", " 3 david H1732 HNpm | entity (human); party human", " 4 told H5046 HVhw3ms", " 5 said H0559 HVqw3ms", " 5 to/for H9005 HRd", " 5 him H9033 HSp3ms", " 6 years H8141 HNcmpa", " 6 to/for H9005 HRd", " 6 you H9031 HSp2ms", " 6 years H7651 HNcbsa", " 7 famine H7458 HNcmsa", " 8 come H0935G HVqi3fs", " 8 [¿] H9008 HTi", " 8 to/for H9005 HRd", " 8 him H9033 HSp3ms", " 9 land H0776G HNcfsc", " 9 in/on/with H9003 HR", " 10 flee H5127 HVqcc | word of another collection; collections escape", " 11 three H7969 HNcbsa", " 11 your H9021 HSp2ms", " 11 three H0518H HTc | connective", " 12 months H2320G HNcmpa", " 13 before H6440G HNcmpc", " 13 to/for H9005 HR", " 13 you H9041 HSp2ms", " 14 foes H6862C HNcmpc", " 15 they H1931 HPp3ms", "*16 pursue H7291 HVqrmsc | member of this collection", " 16 your H9021 HSp2ms", " 16 and H9002 HC", " 17 be H1961 HVqcc", " 18 three H7969 HNcbsc", " 18 you H9031 HSp2ms", " 18 three H0518H HTc | connective", " 18 and H9002 HC | connective", " 19 days H3117G HNcmpa", " 20 pestilence H1698 HNcmsa", " 21 land H0776G HNcfsc", " 21 in/on/with H9003 HR", " 22 now H6258 HD | qualifier candidate; qualifier morph: adverb", " 23 consider H3045 HVqv2ms | word of another collection; collections wise", " 23 your H9021 HSp2ms", " 24 decide H7200J HVqv2ms | word of another collection; collections choose", " 25 answer H1697H HNcmsa | word of another collection; collections profess", " 25 me H9030 HSp1bs", " 26 return H7725G HVhi1cs | word of another collection; collections return", " 26 return H4100 HPi | word of another collection; collections return", " 27 sent H7971G HVqrmsc"]
- reference: 1Ki 20:20
  text: And each struck down his man. The Syrians fled, and Israel pursued them, but Ben-hadad king of Syria escaped on a horse with horsemen.
  words: [" 0 each H0376I HNcmsa", " 1 struck down H5221 HVhw3mp", " 2 man H0376G HNcmsc | entity (human); party human", " 3 syrians H0758I HNpl", " 4 fled H5127 HVqw3mp | word of another collection; collections escape", " 4 his H9023 HSp3ms", " 5 israel H3478 HNpl", " 5 them H9038 HSp3mp", "*6 pursued H7291 HVqw3ms | member of this collection", " 7 ben-hadad H1130G HNpm | entity (human); party human", " 8 king H4428G HNcmsc", " 9 syria H0758I HNpl", " 10 escaped H4422 HVNw3ms | word of another collection; collections escape", " 11 on H5921A HR", " 12 horse H5483M HNcmsa", " 13 horsemen H6571B HNcmpa", " 13 and H9002 HC | connective"]
- reference: 2Ki 9:27
  text: When Ahaziah the king of Judah saw this, he fled in the direction of Beth-haggan. And Jehu pursued him and said, “ Shoot him also.” And they shot him in the chariot at the ascent of Gur, which is by Ibleam. And he fled to Megiddo and died there.
  words: [" 0 ahaziah H0274H HNpm | entity (human); party human", " 0 and H9002 HC | connective", " 1 king H4428G HNcmsc", " 2 judah H3063G HNpl", " 3 saw H7200G HVqp3ms", " 4 fled H5127 HVqw3ms | word of another collection; collections escape", " 5 direction H1870J HNcbsc", " 6 beth-haggan H1004H HNpl", " 6 beth-haggan H1588H HNpl", " 7 jehu H3058H HNpm | entity (human); party human", " 7 him H9033 HSp3ms", "*8 pursued H7291 HVqw3ms | member of this collection", "*8 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 9 said H0559 HVqw3ms", " 10 shoot H5221 HVhv2mp", " 10 shoot H0853 HTo", " 10 him H9033 HSp3ms", " 11 also H1571 HD | qualifier candidate; qualifier morph: adverb", " 12 chariot H4818 HNcfsa", " 12 [the] H9009 HTd", " 12 him H9033 HSp3ms", " 12 chariot H0413 HR", " 13 ascent H4608 HNcmsc", " 13 in/on/with H9003 HR", " 14 gur H1483 HNpl", " 15 which H0834A HTr | connective", " 16 by H0854 HR", " 17 ibleam H2991 HNpl", " 18 fled H5127 HVqw3ms | word of another collection; collections escape", " 19 megiddo H4023 HNpl", " 20 died H4191 HVqw3ms | word of another collection; collections die", " 21 there H8033G HD | qualifier candidate; qualifier morph: adverb"]
- reference: Job 13:25
  text: Will you frighten a driven leaf and pursue dry chaff?
  words: [" 0 frighten H6206 HVqi2ms | word of another collection; collections fear", " 1 driven H5086 HVNrmsa | word of another collection; collections compel", " 2 leaf H5929 HNcmsa", " 2 [¿] H9008 HTi", "*3 pursue H7291 HVqi2ms | member of this collection", " 4 dry H3002 HAamsa | word of another collection; qualifier morph: adjective; collections dry", " 5 chaff H7179 HNcmsa", " 5 chaff H0853 HTo", " 5 and H9002 HC | connective"]
- reference: Job 30:15
  text: Terrors are turned upon me; my honor is pursued as by the wind, and my prosperity has passed away like a cloud.
  words: [" 0 terrors H1091 HNcfpa | word of another collection; collections fear", " 0 terrors H5921A HR | word of another collection; collections fear", " 0 me H9030 HSp1bs", " 1 turned H2015 HVHp3ms | word of another collection; collections turn", " 2 honor H5082 HNcfsc | word of another collection; collections honor", "*3 pursued H7291 HVqi3fs | member of this collection", " 4 wind H7307H HNcfsa", " 4 like/as H9004 HRd", " 5 prosperity H3444 HNcfsc | word of another collection; collections rich", " 5 my H9020 HSp1bs", " 6 passed away H5674A HVqp3fs", " 7 cloud H5645 HNcmsa", " 7 like/as H9004 HR", " 7 and H9002 HC | connective", " 7 my H9020 HSp1bs"]
- reference: Psa 34:14
  text: Turn away from evil and do good; seek peace and pursue it.
  words: [" 0 away H5493G HVqv2ms", " 1 from H9006 HR", " 2 evil H7451B HAamsa | word of another collection; qualifier qualifier subgroup: Bad (a quality of something); morph: adjective; collections evildoer", " 3 do H6213A HVqv2ms | word of another collection; collections serve", " 4 good H2896B HAamsa | qualifier candidate; qualifier qualifier subgroup: Good, better, right (a quality of something); morph: adjective", " 5 seek H1245 HVpv2ms | word of another collection; collections search", " 6 peace H7965G HNcmsa | word of another collection; collections quarrel", "*7 pursue H7291 HVqv2ms | member of this collection", " 8 it H9033 HSp3ms"]
- reference: Psa 83:15
  text: so may you pursue them with your tempest and terrify them with your hurricane!
  words: [" 0 so H3651C HD | qualifier candidate; qualifier morph: adverb", "*1 pursue H7291 HVqi2ms | member of this collection", " 2 with H9003 HR", " 3 tempest H5591A HNcmsc", " 3 them H9038 HSp3mp", " 4 terrify H0926 HVpi2ms | word of another collection; collections fear", " 4 your H9021 HSp2ms", " 5 them H9038 HSp3mp", " 6 hurricane H5492A HNcfsc", " 6 in/on/with H9003 HR", " 6 and H9002 HC | connective", " 6 your H9021 HSp2ms"]
- reference: Jer 29:18
  text: I will pursue them with sword, famine, and pestilence, and will make them a horror to all the kingdoms of the earth, to be a curse, a terror, a hissing, and a reproach among all the nations where I have driven them,
  words: ["*0 pursue H7291 HVqq1cs | member of this collection", " 1 them H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 2 sword H2719 HNcfsa", " 2 in/on/with H9003 HRd", " 2 them H9038 HSp3mp", " 3 famine H7458 HNcmsa", " 3 in/on/with H9003 HRd", " 4 pestilence H1698 HNcmsa", " 4 and H9002 HC | connective", " 4 in/on/with H9003 HRd", " 5 make H5414I HVqq1cs", " 6 horror H2189 HNcfsa | word of another collection; collections fear", " 6 to/for H9005 HR", " 6 them H9038 HSp3mp", " 7 all H3605 HNcmsc", " 7 to/for H9005 HR", " 8 kingdoms H4467 HNcfpc", " 9 earth H0776G HNcfsa", " 9 [the] H9009 HTd", " 10 to H9005 HR", " 11 curse H0423 HNcfsa", " 12 terror H8047H HNcfsa | word of another collection; collections fear", " 12 and H9002 HC | connective", " 12 to/for H9005 HR", " 13 hissing H8322 HNcfsa", " 13 and H9002 HC | connective", " 13 to/for H9005 HR", " 14 reproach H2781 HNcfsa | word of another collection; collections chide", " 14 and H9002 HC | connective", " 14 to/for H9005 HR", " 15 all H3605 HNcmsc", " 15 in/on/with H9003 HR", " 16 nations H1471A HNcmpa", " 16 [the] H9009 HTd", " 17 where H8033G HD | qualifier candidate; qualifier morph: adverb", " 17 them H9038 HSp3mp", " 18 driven H5080 HVhp1cs | word of another collection; collections compel", " 18 driven H0834A HTr | word of another collection; collections compel"]
- reference: 1Ti 6:11
  text: But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.
  words: [" 0 but G1161 CONJ | connective", " 1 you G4771 P-2NS", " 2 o G5599 INJ", " 3 man G0444 N-VSM | entity (human); party human", " 4 god G2316 N-GSM-T | entity (divine); party divine", " 5 flee G5343 V-PAM-2S | word of another collection; collections escape", " 6 these G3778 D-APN", "*7 pursue G1161 CONJ | member of this collection", "*7 pursue G1377 V-PAM-2S | member of this collection", " 8 righteousness G1343 N-ASF | word of another collection; collections righteous", " 9 godliness G2150 N-ASF | word of another collection; collections godly", " 10 faith G4102G N-ASF | word of another collection; collections believe", " 11 love G0026 N-ASF | word of another collection; collections love", " 12 steadfastness G5281 N-ASF | word of another collection; collections loyalty", " 13 gentleness G4239 N-ASF | word of another collection; collections compassion"]
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
  words: [" 0 so G1161 CONJ | connective", " 1 flee G5343 V-PAM-2S | word of another collection; collections escape", " 2 youthful G3512 A-APF | qualifier candidate; qualifier morph: adjective", " 3 passions G1939 N-APF | word of another collection; collections desire", " 4 and G1161 CONJ | connective", "*5 pursue G1377 V-PAM-2S | member of this collection", " 6 righteousness G1343 N-ASF | word of another collection; collections righteous", " 7 faith G4102G N-ASF | word of another collection; collections believe", " 8 love G0026 N-ASF | word of another collection; collections love", " 9 peace G1515 N-ASF | word of another collection; collections quarrel", " 10 with G3326 PREP", " 11 call on G1941 V-PMP-GPM | word of another collection; collections call", " 12 lord G2962G N-ASM-T | entity (divine); party divine", " 13 from G1537 PREP", " 14 pure G2513 A-GSF | word of another collection; qualifier morph: adjective; collections cleanse", " 15 heart G2588 N-GSF | word of another collection; collections heart"]
- reference: 1Pe 3:11
  text: let him turn away from evil and do good; let him seek peace and pursue it.
  words: [" 0 away from G1578 V-AAM-3S", " 0 away from G0575 PREP", " 1 evil G2556G A-GSN | word of another collection; qualifier qualifier subgroup: Bad (a quality of something); morph: adjective; collections evildoer", " 2 and G2532 CONJ | connective", " 3 do G4160G V-AAM-3S | word of another collection; collections serve", " 4 good G0018 A-ASN | qualifier candidate; qualifier qualifier subgroup: Good, better, right (a quality of something); morph: adjective", " 5 seek G2212 V-AAM-3S | word of another collection; collections search", " 6 peace G1515 N-ASF | word of another collection; collections quarrel", " 7 and G2532 CONJ | connective", "*8 pursue G1377 V-AAM-3S | member of this collection", " 9 it G0846 P-ASF"]

## rows

- ledger_id: 2380
  item: pairing
  subject: escape
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Judg 1:6", "Judg 8:12", "Judg 20:45", "2Sa 20:6", "2Sa 24:13", "1Ki 20:20", "2Ki 9:27", "1Ti 6:11", "2Ti 2:22"]
  occurrences: [{"occurrence": 1114294, "reference": "Judg 1:6", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1114295, "reference": "Judg 1:6", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1112827, "reference": "Judg 8:12", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1112828, "reference": "Judg 8:12", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1113438, "reference": "Judg 20:45", "surface": "pursued", "strong": "H1692", "as": "member"}, {"occurrence": 1140278, "reference": "2Sa 20:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1140280, "reference": "2Sa 20:6", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1136445, "reference": "2Sa 24:13", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1168621, "reference": "1Ki 20:20", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1176771, "reference": "2Ki 9:27", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1176772, "reference": "2Ki 9:27", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1499466, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1161", "as": "member"}, {"occurrence": 1499467, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1500395, "reference": "2Ti 2:22", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1114293, "reference": "Judg 1:6", "surface": "fled", "strong": "H5127", "as": "partner"}, {"occurrence": 1112826, "reference": "Judg 8:12", "surface": "fled", "strong": "H5127", "as": "partner"}, {"occurrence": 1113423, "reference": "Judg 20:45", "surface": "fled", "strong": "H5127", "as": "partner"}, {"occurrence": 1140288, "reference": "2Sa 20:6", "surface": "escape", "strong": "H5337", "as": "partner"}, {"occurrence": 1136435, "reference": "2Sa 24:13", "surface": "flee", "strong": "H5127", "as": "partner"}, {"occurrence": 1168617, "reference": "1Ki 20:20", "surface": "fled", "strong": "H5127", "as": "partner"}, {"occurrence": 1168625, "reference": "1Ki 20:20", "surface": "escaped", "strong": "H4422", "as": "partner"}, {"occurrence": 1176765, "reference": "2Ki 9:27", "surface": "fled", "strong": "H5127", "as": "partner"}, {"occurrence": 1176788, "reference": "2Ki 9:27", "surface": "fled", "strong": "H5127", "as": "partner"}, {"occurrence": 1499464, "reference": "1Ti 6:11", "surface": "flee", "strong": "G5343", "as": "partner"}, {"occurrence": 1500391, "reference": "2Ti 2:22", "surface": "flee", "strong": "G5343", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2381
  item: pairing
  subject: evildoer
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["1Sa 26:18", "Psa 34:14", "1Pe 3:11"]
  occurrences: [{"occurrence": 1121272, "reference": "1Sa 26:18", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1265368, "reference": "Psa 34:14", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1508465, "reference": "1Pe 3:11", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1121282, "reference": "1Sa 26:18", "surface": "evil", "strong": "H7451I", "as": "partner"}, {"occurrence": 1265363, "reference": "Psa 34:14", "surface": "evil", "strong": "H7451B", "as": "partner"}, {"occurrence": 1508458, "reference": "1Pe 3:11", "surface": "evil", "strong": "G2556G", "as": "partner"}]
  older: [{"observation": 18216, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "1Sa 26:16 | David to Abner: \"you deserve to die, because you have not kept watch over your lord, the Lord's anointed\". David had refused to strike Saul (26:9–11, uncited), took the spear and jar as proof, and asks Saul: \"Why does my lord pursue after his servant? For what have I done? What evil is on my hands?\" (26:18). Saul: \"Is this your voice, my son David?\" (26:17) | 10.10 *Loyalty and honour* (a guard's duty failed; restraint toward the anointed); the hands as the seat of guilt, for signpost #1893", "verses": ["1Sam.26.16", "1Sam.26.18"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2382
  item: pairing
  subject: faint
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["1Sa 30:10"]
  occurrences: [{"occurrence": 1133706, "reference": "1Sa 30:10", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1133716, "reference": "1Sa 30:10", "surface": "exhausted", "strong": "H6296", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2383
  item: pairing
  subject: fear
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Gen 35:5", "Judg 8:12", "Job 13:25", "Job 30:15", "Psa 83:15", "Jer 29:18"]
  occurrences: [{"occurrence": 992262, "reference": "Gen 35:5", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 992265, "reference": "Gen 35:5", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1112827, "reference": "Judg 8:12", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1112828, "reference": "Judg 8:12", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1236036, "reference": "Job 13:25", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1240364, "reference": "Job 30:15", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1267293, "reference": "Psa 83:15", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1332622, "reference": "Jer 29:18", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 992253, "reference": "Gen 35:5", "surface": "terror", "strong": "H2847", "as": "partner"}, {"occurrence": 992254, "reference": "Gen 35:5", "surface": "terror", "strong": "H1961", "as": "partner"}, {"occurrence": 1112844, "reference": "Judg 8:12", "surface": "panic", "strong": "H2729", "as": "partner"}, {"occurrence": 1236032, "reference": "Job 13:25", "surface": "frighten", "strong": "H6206", "as": "partner"}, {"occurrence": 1240359, "reference": "Job 30:15", "surface": "terrors", "strong": "H1091", "as": "partner"}, {"occurrence": 1240360, "reference": "Job 30:15", "surface": "terrors", "strong": "H5921A", "as": "partner"}, {"occurrence": 1267297, "reference": "Psa 83:15", "surface": "terrify", "strong": "H0926", "as": "partner"}, {"occurrence": 1332633, "reference": "Jer 29:18", "surface": "horror", "strong": "H2189", "as": "partner"}, {"occurrence": 1332643, "reference": "Jer 29:18", "surface": "terror", "strong": "H8047H", "as": "partner"}]
  older: [{"observation": 11796, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Made a horror to the kingdoms of the earth.", "verses": ["Jer.24.9", "Deut.28.25", "Jer.19.8", "Jer.18.16", "Jer.44.22", "2Chr.30.7", "Mic.6.16", "Jer.34.17", "Jer.15.4", "Jer.25.9", "Jer.25.18", "Jer.29.18", "Jer.42.18", "Jer.44.12", "Jer.49.13", "Jer.49.17", "Jer.50.23", "Jer.51.37", "Jer.51.41", "Jer.51.43", "Deut.28.37", "2Chr.29.8", "Ezek.23.46", "Jer.48.39", "Jer.2.15", "Jer.4.7", "Jer.25.11", "Jer.25.38", "Jer.46.19", "Jer.48.9", "Jer.50.3", "Jer.51.29", "Isa.5.9", "Isa.13.9", "Isa.24.12", "Hos.5.9", "Zech.7.14", "Ps.46.8"]}, {"observation": 11808, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "\"The terrors of God\", \"your terrors\".", "verses": ["Job.6.4", "Job.30.15", "Ps.88.7", "Ps.88.15", "Ps.88.16"]}, {"observation": 11812, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Dread laid on peoples and creatures, and what it led to.", "verses": ["Gen.9.2", "Gen.35.5", "Exod.23.27", "Josh.2.9", "Num.22.3", "Ps.9.20", "Isa.19.17", "Dan.5.19", "Exod.15.16"]}, {"observation": 12557, "stage": "prior-capture", "kind": "party", "nature": null, "text": "Fear is also done to others as an act, with the one who frightens as the subject: Ahithophel's plan to throw the king's company into a panic, Gideon throwing an army into panic, sorceries from which Babylon hopes to inspire terror, God's justice so that man may strike terror no more, creditors roused to make the debtor tremble, Job asking whether God will frighten a driven leaf, those sent to terrify the nations.", "verses": ["2Sam.17.2", "Judg.8.12", "Isa.47.12", "Ps.10.18", "Hab.2.7", "Job.13.25", "Zech.1.21", "Ezek.30.9"]}, {"observation": 12703, "stage": "prior-capture", "kind": "face", "nature": null, "text": "Face G. Dread laid on nations, peoples and creatures (8 / 8 hits and verses; surfaces terror · dread · fear · feared): Laid by God, on cities, peoples, beasts; once so that the nations may know they are men.", "verses": ["Gen.9.2", "Gen.35.5", "Josh.2.9", "Ps.9.20", "Dan.5.19"]}, {"observation": 19212, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "What it does in the human: Dismay: \"you hid your face; I was dismayed\" (Psa 30:7); \"When you hide your face, they are dismayed; when you take away their breath, they die\" (Psa 104:29); The spirit failing: \"My spirit fails! Hide not your face from me, lest I be like those who go down to the pit\" (Psa 143:7); Being cast away: \"why do you cast my soul away? Why do you hide your face\" (Psa 88:14); Feeling forgotten: \"Will you forget me forever? How long will you hide your face from me?\" (Psa 13:1). The seat follows at once: \"How long must I take counsel in my soul and have sorrow in my heart all the day?\" (13:2); The body pressed down: \"Why do you hide your face? … For our soul is bowed down to the dust; our belly clings to the ground\" (Psa 44:24–25); Melting: \"you have hidden your face from us, and have made us melt in the hand of our iniquities\" (Isa 64:7). The previous verse: \"We all fade like a leaf\" (64:6); Being counted an enemy: \"Why do you hide your face and count me as your enemy?\" (Job 13:24); \"Will you frighten a driven leaf?\" (13:25); A collective conclusion: \"Have not these evils come upon us because our God is not among us?\" (Deu 31:17); Complaint: \"My way is hidden from the Lord, and my right is disregarded by my God\" (Isa 40:27). The answer: \"He does not faint or grow weary … He gives power to the faint\" (40:28–29); Banishment and the fear that follows it: Cain, \"from your face I shall be hidden. I shall be a fugitive … whoever finds me will kill me\" (Gen 4:14), after \"My punishment is greater than I can bear\" (4:13). Being hidden from God's face is followed at once by fear of man.", "verses": ["Ps.30.7", "Ps.104.29", "Ps.143.7", "Ps.88.14", "Ps.13.1", "Ps.13.2", "Ps.44.24", "Ps.44.25", "Isa.64.7", "Isa.64.6", "Job.13.24", "Job.13.25", "Deut.31.17", "Isa.40.27", "Isa.40.28", "Isa.40.29", "Gen.4.14", "Gen.4.13"]}, {"observation": 21808, "stage": "prior-reread", "kind": "face", "nature": null, "text": "Face, Making others afraid, as an act: The subject is the one who frightens: a counsellor, a judge, sorceries, debtors, God's messengers, horns", "verses": ["2Sam.17.2", "Judg.8.12", "Isa.47.12", "Ps.10.18", "Zech.1.21"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 57342
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "going after",
 "rows": [
  {
   "ledger_id": 2380,
   "item": "pairing",
   "subject": "escape",
   "disposition": "observed | none",
   "findings": [
    {
     "kind": "pairing",
     "obs_text": "",
     "basis": "read | stated",
     "grounds": "",
     "occurrences": []
    }
   ],
   "reason": "",
   "older": []
  },
  {
   "ledger_id": 2381,
   "item": "pairing",
   "subject": "evildoer",
   "disposition": "observed | none",
   "findings": [
    {
     "kind": "pairing",
     "obs_text": "",
     "basis": "read | stated",
     "grounds": "",
     "occurrences": []
    }
   ],
   "reason": "",
   "older": [
    {
     "observation": 18216,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2382,
   "item": "pairing",
   "subject": "faint",
   "disposition": "observed | none",
   "findings": [
    {
     "kind": "pairing",
     "obs_text": "",
     "basis": "read | stated",
     "grounds": "",
     "occurrences": []
    }
   ],
   "reason": "",
   "older": []
  },
  {
   "ledger_id": 2383,
   "item": "pairing",
   "subject": "fear",
   "disposition": "observed | none",
   "findings": [
    {
     "kind": "pairing",
     "obs_text": "",
     "basis": "read | stated",
     "grounds": "",
     "occurrences": []
    }
   ],
   "reason": "",
   "older": [
    {
     "observation": 11796,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 11808,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 11812,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 12557,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 12703,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 19212,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 21808,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  }
 ]
}
```
