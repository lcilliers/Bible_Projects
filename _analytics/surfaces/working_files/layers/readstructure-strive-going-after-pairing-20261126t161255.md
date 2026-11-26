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

2026-11-26T16:12:55Z

## batch

- rows: 5
- rows_left_after_this: 46

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

- reference: Exo 15:9
  text: The enemy said, ‘I will pursue, I will overtake, I will divide the spoil, my desire shall have its fill of them. I will draw my sword; my hand shall destroy them.’
  words: [" 0 enemy H0341 HVqrmsa", " 1 said H0559 HVqp3ms", "*2 pursue H7291 HVqi1cs | member of this collection", " 3 overtake H5381 HVhi1cs", " 4 divide H2505A HVpi1cs", " 5 spoil H7998 HNcmsa", " 6 desire H5315L HNcfsc | word of another collection; collections desire", " 6 them H9038 HSp3mp", " 7 of them H4390 HVqi3fs", " 8 i H9020 HSp1bs", " 9 draw H7324 HVhi1cs", " 10 sword H2719 HNcfsc", " 11 my H9020 HSp1bs", " 12 hand H3027H HNcbsc", " 12 them H9038 HSp3mp", " 13 destroy H3423H HVhi3fs | word of another collection; collections destruction", " 13 my H9020 HSp1bs"]
- reference: Deu 11:4
  text: and what he did to the army of Egypt, to their horses and to their chariots, how he made the water of the Red Sea flow over them as they pursued after you, and how the Lord has destroyed them to this day,
  words: [" 0 what H0834A HTr | connective", " 0 and H9002 HC | connective", " 1 did H6213A HVqp3ms", " 2 army H2428A HNcmsc", " 2 to/for H9005 HR", " 3 egypt H4714G HNpl", " 4 horses H5483M HNcmpc", " 4 to/for H9005 HR", " 5 chariots H7393G HNcmsc", " 5 to/for H9005 HR", " 5 and H9002 HC | connective", " 5 his H9023 HSp3ms", " 6 how H0834A HTr | connective", " 6 his H9023 HSp3ms", " 7 water H4325G HNcmpc", " 7 water H0853 HTo", " 8 red H5488G HNtmsa", " 9 sea H3220G HNcmsc", " 10 flow over H6687 HVhp3ms", " 11 them H6440L HNcmpc", " 11 them H5921A HR", "*12 pursued H7291 HVqcc | member of this collection", " 12 in/on/with H9003 HR", " 12 their H9028 HSp3mp", " 13 after H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 13 they H9048 HSp3mp", " 14 lord H3068G HNpt | entity (divine); party divine", " 14 them H9038 HSp3mp", " 15 destroyed H0006 HVpw3ms | word of another collection; collections destruction", " 15 you H9036 HSp2mp", " 16 this H2088 HTm", " 16 [the] H9009 HTd", " 17 day H3117L HNcmsa", " 17 [the] H9009 HTd", " 17 day H5704 HR"]
- reference: Deu 19:6
  text: lest the avenger of blood in hot anger pursue the manslayer and overtake him, because the way is long, and strike him fatally, though the man did not deserve to die, since he had not hated his neighbor in the past.
  words: [" 0 lest H6435 HTc | connective", " 1 avenger H1350H HVqrmsc", " 2 blood H1818 HNcmsa", " 2 [the] H9009 HTd", " 3 in H3588A HTc | connective", " 4 hot H2552 HVqi3ms", " 5 anger H3824 HNcmsc | word of another collection; collections anger", "*6 pursue H7291 HVqi3ms | member of this collection", "*6 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 7 manslayer H7523 HVqrmsa", " 7 [the] H9009 HTd", " 8 overtake H5381 HVhq3ms", " 8 his H9023 HSp3ms", " 9 him H5315I HNcfsa", " 9 him H9033 HSp3ms", " 10 because H3588A HTc | connective", " 10 him H9033 HSp3ms", " 11 way H1870L HNcbsa", " 11 [the] H9009 HTd", " 12 long H7235A HVqi3ms", " 13 strike him fatally H5221 HVhq3ms", " 14 not H0369 HNcmsc", " 14 and H9002 HC | connective", " 14 to/for H9005 HRd", " 14 him H9033 HSp3ms", " 15 deserve H4941G HNcmsc | word of another collection; collections govern", " 16 die H4194 HNcmsa | word of another collection; collections die", " 17 since H3588A HTc | connective", " 18 not H3808 HTn | negator; qualifier negator; negator", " 19 hated H8130 HVqrmsa | word of another collection; collections love", " 20 neighbor H8543 HNcmsa", " 20 from H9006 HR", " 20 neighbor H1931 HPp3ms", " 20 to/for H9005 HRd", " 20 him H9033 HSp3ms", " 21 past H8032 HNcmsa"]
- reference: Deu 28:22
  text: The Lord will strike you with wasting disease and with fever, inflammation and fiery heat, and with drought and with blight and with mildew. They shall pursue you until you perish.
  words: [" 0 lord H3068G HNpt | entity (divine); party divine", " 0 you H9031 HSp2ms", " 1 strike H5221 HVhi3ms | word of another collection; collections cruel", " 2 wasting disease H7829 HNcfsa", " 2 in/on/with H9003 HRd", " 3 fever H6920 HNcfsa", " 3 and H9002 HC | connective", " 3 in/on/with H9003 HRd", " 4 inflammation H1816 HNcfsa", " 4 and H9002 HC | connective", " 4 in/on/with H9003 HRd", " 5 fiery heat H2746 HNcmsa", " 5 and H9002 HC | connective", " 5 in/on/with H9003 HRd", " 6 drought H2719 HNcfsa", " 6 and H9002 HC | connective", " 6 in/on/with H9003 HRd", " 7 blight H7711B HNcmsa", " 7 and H9002 HC | connective", " 7 in/on/with H9003 HRd", " 8 mildew H3420 HNcmsa", " 8 and H9002 HC | connective", " 8 in/on/with H9003 HRd", "*9 pursue H7291 HVqq3cp | member of this collection", " 10 until H5704 HR", " 10 you H9031 HSp2ms", " 11 you H9041 HSp2ms", " 12 perish H0006 HVqcc | word of another collection; collections die"]
- reference: Deu 28:45
  text: “ All these curses shall come upon you and pursue you and overtake you till you are destroyed, because you did not obey the voice of the Lord your God, to keep his commandments and his statutes that he commanded you.
  words: [" 0 all H3605 HNcmsc", " 0 you H9031 HSp2ms", " 1 these H0428 HTm", " 1 [the] H9009 HTd", " 2 curses H7045 HNcfpa", " 2 [the] H9009 HTd", " 3 come H0935G HVqq3cp", " 4 upon H5921A HRd", "*5 pursue H7291 HVqq3cp | member of this collection", " 6 overtake H5381 HVhq3cp", " 6 you H9031 HSp2ms", " 7 till H5704 HR", " 7 you H9031 HSp2ms", " 8 destroyed H8045 HVNcc | word of another collection; collections destruction", " 9 because H3588A HTc | connective", " 9 you H9041 HSp2ms", " 10 not H3808 HTn | negator; qualifier negator; negator", " 11 obey H8085H HVqp2ms | word of another collection; collections convince", " 12 voice H6963A HNcmsc", " 12 in/on/with H9003 HR", " 13 lord H3068G HNpt | entity (divine); party divine", " 14 god H0430G HNcmpc | entity (divine); party divine", " 15 keep H8104G HVqcc | word of another collection; collections remove", " 15 to/for H9005 HR", " 15 your H9021 HSp2ms", " 16 commandments H4687 HNcfpc", " 17 statutes H2708 HNcfpc", " 17 and H9002 HC | connective", " 17 his H9023 HSp3ms", " 18 that H0834A HTr | connective", " 18 his H9023 HSp3ms", " 19 commanded H6680 HVpp3ms | word of another collection; collections command", " 20 you H9031 HSp2ms"]
- reference: Jos 10:19
  text: but do not stay there yourselves. Pursue your enemies; attack their rear guard. Do not let them enter their cities, for the Lord your God has given them into your hand.”
  words: [" 0 not H0408 HTn | negator; qualifier negator; negator", " 0 not H0859D HPp2mp", " 0 and H9002 HC | connective", " 1 stay H5975G HVqj2mp | word of another collection; collections endure", "*2 pursue H7291 HVqv2mp | member of this collection", "*2 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 3 enemies H0341 HVqrmpc", " 4 rear guard H2179 HVpq2mp", " 4 your H9026 HSp2mp", " 5 not H0408 HTn | negator; qualifier negator; negator", " 5 not H0853 HTo", " 5 them H9038 HSp3mp", " 6 let H5414K HVqj2mp", " 7 enter H0935G HVqcc", " 7 to/for H9005 HR", " 7 them H9038 HSp3mp", " 8 cities H5892B HNcmpc", " 8 cities H0413 HR", " 9 lord H3068G HNpt | entity (divine); party divine", " 9 them H9038 HSp3mp", " 10 god H0430G HNcmpc | entity (divine); party divine", " 11 given H5414G HVqp3ms | word of another collection; collections share", " 11 their H9028 HSp3mp", " 11 given H3588A HTc | word of another collection; collections share", " 12 your H9026 HSp2mp", " 13 hand H3027H HNcbsc", " 13 in/on/with H9003 HR", " 13 your H9026 HSp2mp"]
- reference: 2Sa 20:10
  text: But Amasa did not observe the sword that was in Joab’s hand. So Joab struck him with it in the stomach and spilled his entrails to the ground without striking a second blow, and he died. Then Joab and Abishai his brother pursued Sheba the son of Bichri.
  words: [" 0 amasa H6021G HNpm | entity (human); party human", " 0 and H9002 HC | connective", " 1 not H3808 HTn | negator; qualifier negator; negator", " 2 observe H8104I HVNp3ms | word of another collection; collections watch", " 3 sword H2719 HNcfsa", " 3 in/on/with H9003 HRd", " 4 that H0834A HTr | connective", " 5 joab’s H3097G HNpm | entity (human); party human", " 6 hand H3027G HNcbsc", " 6 in/on/with H9003 HR", " 7 struck H5221 HVhw3ms", " 8 in H9003 HRd", " 9 stomach H2570 HNcmsa", " 9 [the] H9009 HTd", " 9 him H9033 HSp3ms", " 9 her H9034 HSp3fs", " 9 stomach H0413 HR", " 10 spilled H8210G HVqw3ms", " 11 entrails H4578 HNcmpc", " 12 ground H0776H HNcfsa", " 12 his H9023 HSp3ms", " 13 without H3808 HTn | negator; qualifier negator; negator", " 13 and H9002 HC | connective", " 13 [to] H9011 HSd", " 14 second H8138B HVqp3ms", " 15 died H4191 HVqw3ms | word of another collection; collections die", " 15 to/for H9005 HRd", " 15 him H9033 HSp3ms", " 16 joab H3097G HNpm | entity (human); party human", " 16 and H9002 HC | connective", " 17 abishai H0052 HNpm | entity (human); party human", " 17 and H9002 HC | connective", " 18 brother H0251G HNcmsc", "*19 pursued H7291 HVqp3ms | member of this collection", " 19 his H9023 HSp3ms", "*19 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 20 sheba H7652A HNpm | entity (human); party human", " 21 son H1121A HNcmsc", " 22 bichri H1075 HNpm | entity (human); party human"]
- reference: 2Sa 22:38
  text: I pursued my enemies and destroyed them, and did not turn back until they were consumed.
  words: ["*0 pursued H7291 HVqc1cs | member of this collection", " 1 enemies H0341 HVqrmpc", " 2 destroyed H8045 HVhw1cs | word of another collection; collections destruction", " 2 my H9020 HSp1bs", " 3 not H3808 HTn | negator; qualifier negator; negator", " 3 and H9002 HC | connective", " 3 them H9038 HSp3mp", " 4 turn back H7725G HVqi1cs | word of another collection; collections turn", " 5 until H5704 HR", " 6 consumed H3615H HVpcc | word of another collection; collections destruction", " 6 them H9038 HSp3mp"]
- reference: 2Ki 9:27
  text: When Ahaziah the king of Judah saw this, he fled in the direction of Beth-haggan. And Jehu pursued him and said, “ Shoot him also.” And they shot him in the chariot at the ascent of Gur, which is by Ibleam. And he fled to Megiddo and died there.
  words: [" 0 ahaziah H0274H HNpm | entity (human); party human", " 0 and H9002 HC | connective", " 1 king H4428G HNcmsc", " 2 judah H3063G HNpl", " 3 saw H7200G HVqp3ms", " 4 fled H5127 HVqw3ms | word of another collection; collections escape", " 5 direction H1870J HNcbsc", " 6 beth-haggan H1004H HNpl", " 6 beth-haggan H1588H HNpl", " 7 jehu H3058H HNpm | entity (human); party human", " 7 him H9033 HSp3ms", "*8 pursued H7291 HVqw3ms | member of this collection", "*8 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 9 said H0559 HVqw3ms", " 10 shoot H5221 HVhv2mp", " 10 shoot H0853 HTo", " 10 him H9033 HSp3ms", " 11 also H1571 HD | qualifier candidate; qualifier morph: adverb", " 12 chariot H4818 HNcfsa", " 12 [the] H9009 HTd", " 12 him H9033 HSp3ms", " 12 chariot H0413 HR", " 13 ascent H4608 HNcmsc", " 13 in/on/with H9003 HR", " 14 gur H1483 HNpl", " 15 which H0834A HTr | connective", " 16 by H0854 HR", " 17 ibleam H2991 HNpl", " 18 fled H5127 HVqw3ms | word of another collection; collections escape", " 19 megiddo H4023 HNpl", " 20 died H4191 HVqw3ms | word of another collection; collections die", " 21 there H8033G HD | qualifier candidate; qualifier morph: adverb"]
- reference: Job 13:25
  text: Will you frighten a driven leaf and pursue dry chaff?
  words: [" 0 frighten H6206 HVqi2ms | word of another collection; collections fear", " 1 driven H5086 HVNrmsa | word of another collection; collections compel", " 2 leaf H5929 HNcmsa", " 2 [¿] H9008 HTi", "*3 pursue H7291 HVqi2ms | member of this collection", " 4 dry H3002 HAamsa | word of another collection; qualifier morph: adjective; collections dry", " 5 chaff H7179 HNcmsa", " 5 chaff H0853 HTo", " 5 and H9002 HC | connective"]
- reference: Psa 18:37
  text: I pursued my enemies and overtook them, and did not turn back till they were consumed.
  words: ["*0 pursued H7291 HVqi1cs | member of this collection", " 1 enemies H0341 HVqrmpc", " 2 overtook H5381 HVhu1cs", " 2 my H9020 HSp1bs", " 3 not H3808 HTn | negator; qualifier negator; negator", " 3 and H9002 HC | connective", " 3 them H9038 HSp3mp", " 4 turn back H7725G HVqi1cs | word of another collection; collections turn", " 5 till H5704 HR", " 6 consumed H3615H HVpcc | word of another collection; collections destruction", " 6 them H9038 HSp3mp"]
- reference: Psa 109:16
  text: For he did not remember to show kindness, but pursued the poor and needy and the brokenhearted, to put them to death.
  words: [" 0 for H3282 HC | connective", " 0 for H0834A HTr | connective", " 1 not H3808 HTn | negator; qualifier negator; negator", " 2 remember H2142 HVqp3ms | word of another collection; collections forget", " 3 show H6213A HVqcc", " 4 kindness H2617A HNcmsa | word of another collection; collections compassion", "*5 pursued H7291 HVqw3ms | member of this collection", " 6 poor H6041 HAamsa | word of another collection; qualifier morph: adjective; collections rich", " 7 needy H0034 HAamsa | word of another collection; qualifier morph: adjective; collections rich", " 7 and H9002 HC | connective", " 7 needy H0376I HNcmsa | word of another collection; collections rich", " 8 brokenhearted H3512A HVNrmsc | word of another collection; collections pain", " 8 brokenhearted H3824 HNcmsa | word of another collection; collections pain", " 9 death H4191 HVpcc | word of another collection; collections die", " 9 to/for H9005 HR"]
- reference: Lam 3:66
  text: You will pursue them in anger and destroy them from under your heavens, O Lord.”
  words: ["*0 pursue H7291 HVqi2ms | member of this collection", " 1 anger H0639G HNcmsa | word of another collection; collections anger", " 1 in/on/with H9003 HR", " 2 destroy H8045 HVhu2ms | word of another collection; collections destruction", " 3 from H9006 HR", " 3 them H9038 HSp3mp", " 4 under H8478G HNcmsc", " 5 heavens H8064 HNcmpc", " 6 lord H3068G HNpt | entity (divine); party divine"]
- reference: 1Cor 14:1
  text: Pursue love, and earnestly desire the spiritual gifts, especially that you may prophesy.
  words: ["*0 pursue G1377 V-PAM-2P | member of this collection", " 1 love G0026 N-ASF | word of another collection; collections love", " 2 and G1161 CONJ | connective", " 3 earnestly desire G2206 V-PAM-2P | word of another collection; collections desire", " 4 spiritual gifts G4152 A-APN | qualifier candidate; qualifier morph: adjective", " 5 especially G3123H ADV | qualifier candidate; qualifier morph: adverb", " 6 that G2443 CONJ | connective", " 7 prophesy G4395 V-PAS-2P | word of another collection; collections preach"]
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
  words: [" 0 so G1161 CONJ | connective", " 1 flee G5343 V-PAM-2S | word of another collection; collections escape", " 2 youthful G3512 A-APF | qualifier candidate; qualifier morph: adjective", " 3 passions G1939 N-APF | word of another collection; collections desire", " 4 and G1161 CONJ | connective", "*5 pursue G1377 V-PAM-2S | member of this collection", " 6 righteousness G1343 N-ASF | word of another collection; collections righteous", " 7 faith G4102G N-ASF | word of another collection; collections believe", " 8 love G0026 N-ASF | word of another collection; collections love", " 9 peace G1515 N-ASF | word of another collection; collections quarrel", " 10 with G3326 PREP", " 11 call on G1941 V-PMP-GPM | word of another collection; collections call", " 12 lord G2962G N-ASM-T | entity (divine); party divine", " 13 from G1537 PREP", " 14 pure G2513 A-GSF | word of another collection; qualifier morph: adjective; collections cleanse", " 15 heart G2588 N-GSF | word of another collection; collections heart"]
- reference: Jude 7
  text: just as Sodom and Gomorrah and the surrounding cities, which likewise indulged in sexual immorality and pursued unnatural desire, serve as an example by undergoing a punishment of eternal fire.
  words: [" 0 as G5613 PRT | connective", " 1 sodom G4670 N-NPN-L", " 2 and G2532 CONJ | connective", " 3 gomorrah G1116 N-NSF-L", " 4 and G2532 CONJ | connective", " 5 surrounding G4012 PREP", " 5 surrounding G0846 P-APF", " 6 cities G4172 N-NPF", " 7 which G3778 P-APF", " 8 likewise G3664 A-ASM | qualifier candidate; qualifier morph: adjective", " 8 likewise G5158 N-ASM", " 9 sexual immorality G1608 V-AAP-NPF | word of another collection; collections righteous", " 10 and G2532 CONJ | connective", "*11 pursued G0565 V-2AAP-NPF | member of this collection", "*11 pursued G3694 PREP | member of this collection", " 12 unnatural G2087 A-GSF | qualifier candidate; qualifier morph: adjective", " 13 desire G4561 N-GSF | word of another collection; collections desire", " 14 serve G4295 V-PNI-3P | word of another collection; collections serve", " 15 example G1164 N-ASN", " 16 undergoing G5254 V-PAP-NPF", " 17 punishment G1349 N-ASF | word of another collection; collections reward", " 18 eternal G0166 A-GSN | word of another collection; qualifier morph: adjective; collections continual", " 19 fire G4442 N-GSN"]

## rows

- ledger_id: 2375
  item: pairing
  subject: desire
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Exo 15:9", "1Cor 14:1", "2Ti 2:22", "Jude 7"]
  occurrences: [{"occurrence": 1005416, "reference": "Exo 15:9", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1483275, "reference": "1Cor 14:1", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1500395, "reference": "2Ti 2:22", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1512349, "reference": "Jude 7", "surface": "pursued", "strong": "G0565", "as": "member"}, {"occurrence": 1512350, "reference": "Jude 7", "surface": "pursued", "strong": "G3694", "as": "member"}, {"occurrence": 1005420, "reference": "Exo 15:9", "surface": "desire", "strong": "H5315L", "as": "partner"}, {"occurrence": 1483278, "reference": "1Cor 14:1", "surface": "earnestly desire", "strong": "G2206", "as": "partner"}, {"occurrence": 1500393, "reference": "2Ti 2:22", "surface": "passions", "strong": "G1939", "as": "partner"}, {"occurrence": 1512352, "reference": "Jude 7", "surface": "desire", "strong": "G4561", "as": "partner"}]
  older: [{"observation": 14051, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "The enemy's own appetite. In the song, the enemy boasts, \"my desire [nephesh] shall have its fill of them\" (Exo 15:9), and is answered by the wind of God (15:10). The enemy's appetite and God's fury meet over the same people. Already read in F v4 §8.4 (\"the enemy's soul and the pursued soul\").", "verses": ["Exod.15.9", "Exod.15.10"]}, {"observation": 14501, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "How it co-exists: The enemy's own appetite. In the song, the enemy boasts, \"my desire [nephesh] shall have its fill of them\" (Exo 15:9), and is answered by the wind of God (15:10). The enemy's appetite and God's fury meet over the same people. Already read in F v4 §8.4 (\"the enemy's soul and the pursued soul\"); The same anger threatens the one it protects, if roles reverse. Exo 22:24 is said to Israel about their own widows: \"I will kill you with the sword, and your wives shall become widows\". God's anger is for the weak, whoever the oppressor is.", "verses": ["Exod.15.9", "Exod.15.10"]}, {"observation": 14877, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Exo 15:7 (DL): Context seat: Exo 15:9 \"desire\" nephesh; Whose · check: the enemy's · appetite-sense; Already read in: F v4 §8.4; §: §3.", "verses": ["Exod.15.9"]}, {"observation": 15093, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Shown in an act: \"I will sing to the Lord, for he has triumphed gloriously; the horse and his rider he has thrown into the sea\" (Exo 15:1, 21); \"In the greatness of your majesty you overthrow your adversaries\" (15:7); The enemy's own rising is quoted in the same song: \"I will pursue, I will overtake, I will divide the spoil, my desire shall have its fill of them\" (15:9).", "verses": ["Exod.15.1", "Exod.15.21", "Exod.15.7", "Exod.15.9"]}, {"observation": 16842, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "6.3 Flesh and justification: \"by works of the law no human being [*flesh*] will be justified\" (Rom 3:20; Gal 2:16); \"God has done what the law, weakened by the flesh, could not do … in the likeness of sinful flesh … he condemned sin in the flesh\" (Rom 8:3); \"manifested in the flesh, vindicated by the Spirit\" (1Ti 3:16) [U]; \"you were justified in the name of the Lord Jesus Christ and by the Spirit of our God\" (1Co 6:11) [D1]; \"unnatural desire [*other flesh*] … undergoing a punishment of eternal fire\" (Jude 7); [Claude reading] Within this cluster *flesh* means three things: all humanity, which cannot be justified; the place where sin is condemned; and Christ's own flesh, which is vindicated by the Spirit. This extends Batch G §7 (flesh valued by circumstance).", "verses": ["Rom.3.20", "Gal.2.16", "Rom.8.3", "1Tim.3.16", "1Cor.6.11", "Jude.1.7"]}, {"observation": 16946, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "The enemy's appetite: \"The enemy said, 'I will pursue, I will overtake … my desire [*nephesh*] shall have its fill of them'\" (Exo 15:9) .", "verses": ["Exod.15.9"]}, {"observation": 17075, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "3.4 Flesh and passion: \"the works of the flesh are evident: sexual immorality, impurity, sensuality\" (Gal 5:19); \"abstain from the passions of the flesh, which wage war against your soul\" (1Pe 2:11); \"indulged in sexual immorality and pursued unnatural desire [*other flesh*]\" (Jude 7); \"do not get drunk with wine, for that is debauchery, but be filled with the Spirit\" (Eph 5:18) [D3] — filled with wine vs filled with the Spirit; [lexical] Flesh = genitals in Eze 16:26 (\"lustful [*great of flesh*] neighbors\") and Eze 23:20.; Ezekiel: \"defiled her with their whoring lust … she turned from them in disgust [*her nephesh*]\" (Eze 23:17–18). The soul turns away in revulsion from what it lusted after.", "verses": ["Gal.5.19", "1Pet.2.11", "Jude.1.7", "Eph.5.18", "Ezek.16.26", "Ezek.23.17", "Ezek.23.18"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2376
  item: pairing
  subject: destruction
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Exo 15:9", "Deu 11:4", "Deu 28:45", "2Sa 22:38", "Psa 18:37", "Lam 3:66"]
  occurrences: [{"occurrence": 1005416, "reference": "Exo 15:9", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1072080, "reference": "Deu 11:4", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1086236, "reference": "Deu 28:45", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1149814, "reference": "2Sa 22:38", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1271714, "reference": "Psa 18:37", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1346070, "reference": "Lam 3:66", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1005429, "reference": "Exo 15:9", "surface": "destroy", "strong": "H3423H", "as": "partner"}, {"occurrence": 1072087, "reference": "Deu 11:4", "surface": "destroyed", "strong": "H0006", "as": "partner"}, {"occurrence": 1086241, "reference": "Deu 28:45", "surface": "destroyed", "strong": "H8045", "as": "partner"}, {"occurrence": 1149816, "reference": "2Sa 22:38", "surface": "destroyed", "strong": "H8045", "as": "partner"}, {"occurrence": 1149823, "reference": "2Sa 22:38", "surface": "consumed", "strong": "H3615H", "as": "partner"}, {"occurrence": 1271723, "reference": "Psa 18:37", "surface": "consumed", "strong": "H3615H", "as": "partner"}, {"occurrence": 1346073, "reference": "Lam 3:66", "surface": "destroy", "strong": "H8045", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2377
  item: pairing
  subject: die
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Deu 19:6", "Deu 28:22", "2Sa 20:10", "2Ki 9:27", "Psa 109:16"]
  occurrences: [{"occurrence": 1066140, "reference": "Deu 19:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1066141, "reference": "Deu 19:6", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1072275, "reference": "Deu 28:22", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1146428, "reference": "2Sa 20:10", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1146430, "reference": "2Sa 20:10", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1176771, "reference": "2Ki 9:27", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1176772, "reference": "2Ki 9:27", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1254311, "reference": "Psa 109:16", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1066159, "reference": "Deu 19:6", "surface": "die", "strong": "H4194", "as": "partner"}, {"occurrence": 1072279, "reference": "Deu 28:22", "surface": "perish", "strong": "H0006", "as": "partner"}, {"occurrence": 1146420, "reference": "2Sa 20:10", "surface": "died", "strong": "H4191", "as": "partner"}, {"occurrence": 1176790, "reference": "2Ki 9:27", "surface": "died", "strong": "H4191", "as": "partner"}, {"occurrence": 1254318, "reference": "Psa 109:16", "surface": "death", "strong": "H4191", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2378
  item: pairing
  subject: dry
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Job 13:25"]
  occurrences: [{"occurrence": 1236036, "reference": "Job 13:25", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1236037, "reference": "Job 13:25", "surface": "dry", "strong": "H3002", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2379
  item: pairing
  subject: endure
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Jos 10:19"]
  occurrences: [{"occurrence": 1095124, "reference": "Jos 10:19", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1095125, "reference": "Jos 10:19", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1095123, "reference": "Jos 10:19", "surface": "stay", "strong": "H5975G", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 54631
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "going after",
 "rows": [
  {
   "ledger_id": 2375,
   "item": "pairing",
   "subject": "desire",
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
     "observation": 14051,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 14501,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 14877,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 15093,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 16842,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 16946,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 17075,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2376,
   "item": "pairing",
   "subject": "destruction",
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
   "ledger_id": 2377,
   "item": "pairing",
   "subject": "die",
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
   "ledger_id": 2378,
   "item": "pairing",
   "subject": "dry",
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
   "ledger_id": 2379,
   "item": "pairing",
   "subject": "endure",
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
  }
 ]
}
```
