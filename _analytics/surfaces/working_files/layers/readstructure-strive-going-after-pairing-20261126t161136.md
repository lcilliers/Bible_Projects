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

2026-11-26T16:11:36Z

## batch

- rows: 6
- rows_left_after_this: 62

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

- reference: Deu 19:6
  text: lest the avenger of blood in hot anger pursue the manslayer and overtake him, because the way is long, and strike him fatally, though the man did not deserve to die, since he had not hated his neighbor in the past.
  words: [" 0 lest H6435 HTc | connective", " 1 avenger H1350H HVqrmsc", " 2 blood H1818 HNcmsa", " 2 [the] H9009 HTd", " 3 in H3588A HTc | connective", " 4 hot H2552 HVqi3ms", " 5 anger H3824 HNcmsc | word of another collection; collections anger", "*6 pursue H7291 HVqi3ms | member of this collection", "*6 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 7 manslayer H7523 HVqrmsa", " 7 [the] H9009 HTd", " 8 overtake H5381 HVhq3ms", " 8 his H9023 HSp3ms", " 9 him H5315I HNcfsa", " 9 him H9033 HSp3ms", " 10 because H3588A HTc | connective", " 10 him H9033 HSp3ms", " 11 way H1870L HNcbsa", " 11 [the] H9009 HTd", " 12 long H7235A HVqi3ms", " 13 strike him fatally H5221 HVhq3ms", " 14 not H0369 HNcmsc", " 14 and H9002 HC | connective", " 14 to/for H9005 HRd", " 14 him H9033 HSp3ms", " 15 deserve H4941G HNcmsc | word of another collection; collections govern", " 16 die H4194 HNcmsa | word of another collection; collections die", " 17 since H3588A HTc | connective", " 18 not H3808 HTn | negator; qualifier negator; negator", " 19 hated H8130 HVqrmsa | word of another collection; collections love", " 20 neighbor H8543 HNcmsa", " 20 from H9006 HR", " 20 neighbor H1931 HPp3ms", " 20 to/for H9005 HRd", " 20 him H9033 HSp3ms", " 21 past H8032 HNcmsa"]
- reference: Jos 8:16
  text: So all the people who were in the city were called together to pursue them, and as they pursued Joshua they were drawn away from the city.
  words: [" 0 all H3605 HNcmsc", " 1 people H5971A HNcmsa", " 1 [the] H9009 HTd", " 2 who H0834A HTr | connective", " 3 city H5857G HNpl", " 3 in/on/with H9003 HRd", " 4 called H2199 HVNw3mp | word of another collection; collections call", "*5 pursue H7291 HVqcc | member of this collection", " 5 to/for H9005 HR", "*5 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", "*6 pursued H7291 HVqw3mp | member of this collection", " 6 them H9038 HSp3mp", "*6 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 7 joshua H3091G HNpm | entity (human); party human", " 8 drawn away H5423 HVNw3mp", " 9 from H4480A HR", " 10 city H5892B HNcfsa", " 10 [the] H9009 HTd"]
- reference: Judg 7:23
  text: And the men of Israel were called out from Naphtali and from Asher and from all Manasseh, and they pursued after Midian.
  words: [" 0 men H0376G HNcmsc | entity (human); party human", " 1 israel H3478 HNpl", " 2 called out H6817 HVNw3ms | word of another collection; collections call", " 3 naphtali H5321G HNpm | entity (human); party human", " 3 from H9006 HR", " 4 from H4480A HR", " 4 and H9002 HC | connective", " 5 asher H0836 HNpm | entity (human); party human", " 6 from H4480A HR", " 6 and H9002 HC | connective", " 7 all H3605 HNcmsc", " 8 manasseh H4519G HNpm | entity (human); party human", "*9 pursued H7291 HVqw3mp | member of this collection", " 10 after H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 11 midian H4080H HNpl"]
- reference: 1Sa 30:8
  text: And David inquired of the Lord, “Shall I pursue after this band? Shall I overtake them?” He answered him, “ Pursue, for you shall surely overtake and shall surely rescue.”
  words: [" 0 david H1732 HNpm | entity (human); party human", " 1 inquired H7592 HVqw3ms | word of another collection; collections ask", " 1 inquired H0559 HVqcc | word of another collection; collections ask", " 2 lord H3068G HNpt | entity (divine); party divine", " 2 in/on/with H9003 HR", "*3 pursue H7291 HVqi1cs | member of this collection", " 3 to/for H9005 HR", " 4 after H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 5 this H2088 HTm", " 5 [the] H9009 HTd", " 6 band H1416 HNcmsa", " 6 [the] H9009 HTd", " 7 overtake H5381 HVhi1cs", " 7 [¿] H9008 HTi", " 8 answered H0559 HVqw3ms | word of another collection; collections profess", " 8 him H9033 HSp3ms", "*9 pursue H7291 HVqv2ms | member of this collection", " 9 to/for H9005 HRd", " 9 him H9033 HSp3ms", " 10 for H3588A HTc | connective", " 11 surely H5381 HVhaa | word of another collection; collections loyalty", " 12 overtake H5381 HVhi2ms", " 13 surely H5337 HVhaa | word of another collection; collections loyalty", " 14 rescue H5337 HVhi2ms"]
- reference: Psa 143:3
  text: For the enemy has pursued my soul; he has crushed my life to the ground; he has made me sit in darkness like those long dead.
  words: [" 0 for H3588A HTc | connective", " 1 enemy H0341 HVqrmsa", "*2 pursued H7291 HVqp3ms | member of this collection", " 3 soul H5315G HNcfsc", " 4 crushed H1792 HVpp3ms | word of another collection; collections abase", " 4 my H9020 HSp1bs", " 5 life H2416C HNcfsc", " 6 ground H0776H HNcfsa", " 6 to/for H9005 HRd", " 7 sit H3427 HVhp3ms", " 7 my H9020 HSp1bs", " 8 darkness H4285 HNcmpa", " 8 in/on/with H9003 HR", " 8 me H9030 HSp1bs", " 9 long H5769J HNcmsa", " 10 dead H4191 HVqrmpc | word of another collection; collections live", " 10 like/as H9004 HR"]
- reference: Lam 3:43
  text: “You have wrapped yourself with anger and pursued us, killing without pity;
  words: [" 0 wrapped H5526B HVqp2ms", " 1 anger H0639G HNcmsa | word of another collection; collections anger", " 1 in/on/with H9003 HRd", "*2 pursued H7291 HVqw2ms | member of this collection", " 3 killing H2026 HVqp2ms | word of another collection; collections kill", " 3 us H9035 HSp1bp", " 4 without H3808 HTn | negator; qualifier negator; negator", " 5 pity H2550 HVqp2ms | word of another collection; collections compassion"]
- reference: Lam 3:66
  text: You will pursue them in anger and destroy them from under your heavens, O Lord.”
  words: ["*0 pursue H7291 HVqi2ms | member of this collection", " 1 anger H0639G HNcmsa | word of another collection; collections anger", " 1 in/on/with H9003 HR", " 2 destroy H8045 HVhu2ms | word of another collection; collections destruction", " 3 from H9006 HR", " 3 them H9038 HSp3mp", " 4 under H8478G HNcmsc", " 5 heavens H8064 HNcmpc", " 6 lord H3068G HNpt | entity (divine); party divine"]
- reference: Eze 35:6
  text: therefore, as I live, declares the Lord God, I will prepare you for blood, and blood shall pursue you; because you did not hate bloodshed, therefore blood shall pursue you.
  words: [" 0 therefore H3651C HD | qualifier candidate; qualifier morph: adverb", " 0 to/for H9005 HR", " 1 i H0589 HPp1bs", " 2 live H2416A HAamsa | word of another collection; qualifier morph: adjective; collections live", " 3 declares H5002 HNcmsc | word of another collection; collections preach", " 4 lord H0136 HNpt", " 5 god H3069 HNpt | entity (divine); party divine", " 6 prepare H6213H HVqi1cs | word of another collection; collections build", " 7 blood H1818 HNcmsa", " 7 to/for H9005 HR", " 7 for H3588A HTc | connective", " 8 blood H1818 HNcmsa", " 8 and H9002 HC | connective", " 8 you H9031 HSp2ms", "*9 pursue H7291 HVqi3ms | member of this collection", " 10 because H0518I HTc | connective", " 10 you H9031 HSp2ms", " 11 not H3808 HTn | negator; qualifier negator; negator", " 12 hate H8130 HVqp2ms | word of another collection; collections love", " 13 bloodshed H1818 HNcmsa", " 14 blood H1818 HNcmsa", " 14 and H9002 HC | connective", "*15 pursue H7291 HVqi3ms | member of this collection", " 16 you H9031 HSp2ms"]
- reference: Amo 1:11
  text: Thus says the Lord: “For three transgressions of Edom, and for four, I will not revoke the punishment, because he pursued his brother with the sword and cast off all pity, and his anger tore perpetually, and he kept his wrath forever.
  words: [" 0 says H0559 HVqp3ms", " 0 thus H3541 HD | qualifier candidate; qualifier morph: adverb", " 1 lord H3068G HNpt | entity (divine); party divine", " 2 three H7969 HNcbsa", " 3 transgressions H6588 HNcmpc | word of another collection; collections sin", " 4 edom H0123G HNpm", " 5 four H0702 HNcbsa", " 5 four H5921A HR", " 5 and H9002 HC | connective", " 6 not revoke H7725O HVhi1cs", " 6 not revoke H3808 HTn | negator; qualifier negator; negator", " 7 punishment H5921A HR | word of another collection; collections reward", "*8 pursued H7291 HVqcc | member of this collection", " 8 him H9033 HSp3ms", "*8 pursued H5921A HR | member of this collection", " 9 brother H0251G HNcmsc", " 10 sword H2719 HNcfsa", " 10 in/on/with H9003 HRd", " 10 he H9043 HSp3ms", " 11 cast off H7843 HVpq3ms | word of another collection; collections reject", " 11 his H9023 HSp3ms", " 12 pity H7356B HNcmpc | word of another collection; collections compassion", " 13 anger H0639G HNcmsc | word of another collection; collections anger", " 14 tore H2963 HVqw3ms", " 14 his H9023 HSp3ms", " 15 perpetually H5703 HNcmsa | qualifier candidate; qualifier qualifier subgroup: Forever, ever, always (a quality of time)", " 15 to/for H9005 HR", " 16 kept H8104G HVqp3ms | word of another collection; collections remove", " 16 his H9023 HSp3ms", " 17 wrath H5678 HNcfsc | word of another collection; collections anger", " 17 and H9002 HC | connective", " 17 his H9023 HSp3ms", " 18 forever H5331 HNcmsa | qualifier candidate; qualifier qualifier subgroup: Forever, ever, always (a quality of time)", " 18 her H9034 HSp3fs"]
- reference: Rom 9:30
  text: What shall we say, then? That Gentiles who did not pursue righteousness have attained it, that is, a righteousness that is by faith;
  words: [" 0 what G5101 I-ASN", " 1 say G4483 V-FAI-1P", " 2 then G3767 CONJ | connective", " 3 that G3754G CONJ | connective", " 4 gentiles G1484 N-NPN", " 5 who G3588 T-NPN", " 6 not G3361 PRT-N | negator; qualifier negator; negator", "*7 pursue G1377 V-PAP-NPN | member of this collection", " 8 righteousness G1343 N-ASF | word of another collection; collections righteous", " 9 attained G2638 V-2AAI-3S", " 10 is G1161 CONJ | connective", " 11 righteousness G1343 N-ASF | word of another collection; collections righteous", " 12 that G3588 T-ASF", " 13 by G1537 PREP", " 14 faith G4102G N-GSF | word of another collection; collections believe"]
- reference: 1Ti 6:11
  text: But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.
  words: [" 0 but G1161 CONJ | connective", " 1 you G4771 P-2NS", " 2 o G5599 INJ", " 3 man G0444 N-VSM | entity (human); party human", " 4 god G2316 N-GSM-T | entity (divine); party divine", " 5 flee G5343 V-PAM-2S | word of another collection; collections escape", " 6 these G3778 D-APN", "*7 pursue G1161 CONJ | member of this collection", "*7 pursue G1377 V-PAM-2S | member of this collection", " 8 righteousness G1343 N-ASF | word of another collection; collections righteous", " 9 godliness G2150 N-ASF | word of another collection; collections godly", " 10 faith G4102G N-ASF | word of another collection; collections believe", " 11 love G0026 N-ASF | word of another collection; collections love", " 12 steadfastness G5281 N-ASF | word of another collection; collections loyalty", " 13 gentleness G4239 N-ASF | word of another collection; collections compassion"]
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
  words: [" 0 so G1161 CONJ | connective", " 1 flee G5343 V-PAM-2S | word of another collection; collections escape", " 2 youthful G3512 A-APF | qualifier candidate; qualifier morph: adjective", " 3 passions G1939 N-APF | word of another collection; collections desire", " 4 and G1161 CONJ | connective", "*5 pursue G1377 V-PAM-2S | member of this collection", " 6 righteousness G1343 N-ASF | word of another collection; collections righteous", " 7 faith G4102G N-ASF | word of another collection; collections believe", " 8 love G0026 N-ASF | word of another collection; collections love", " 9 peace G1515 N-ASF | word of another collection; collections quarrel", " 10 with G3326 PREP", " 11 call on G1941 V-PMP-GPM | word of another collection; collections call", " 12 lord G2962G N-ASM-T | entity (divine); party divine", " 13 from G1537 PREP", " 14 pure G2513 A-GSF | word of another collection; qualifier morph: adjective; collections cleanse", " 15 heart G2588 N-GSF | word of another collection; collections heart"]

## rows

- ledger_id: 2358
  item: pairing
  subject: abase
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 143:3"]
  occurrences: [{"occurrence": 1254167, "reference": "Psa 143:3", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1254169, "reference": "Psa 143:3", "surface": "crushed", "strong": "H1792", "as": "partner"}]
  older: [{"observation": 15919, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Broken spirit and heart as acceptable: \"The sacrifices of God are a broken spirit; a broken and contrite heart … you will not despise\" (Psa 51:17); \"humble and contrite in spirit\" (Isa 66:2).; Revisit 2026-09-28: \"crushed / contrite\" is one vocabulary. Its meaning is set by who crushes and to whom the crushed spirit is turned: enemy, words, sorrow, the Lord, or offered to God. See Batch F §5, including the Psa 143:3–7 chain.", "verses": ["Ps.51.17", "Isa.66.2", "Ps.143.3", "Ps.143.4", "Ps.143.7"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2359
  item: pairing
  subject: anger
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Deu 19:6", "Lam 3:43", "Lam 3:66", "Amo 1:11"]
  occurrences: [{"occurrence": 1066140, "reference": "Deu 19:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1066141, "reference": "Deu 19:6", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1346065, "reference": "Lam 3:43", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1346070, "reference": "Lam 3:66", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1389447, "reference": "Amo 1:11", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1389449, "reference": "Amo 1:11", "surface": "pursued", "strong": "H5921A", "as": "member"}, {"occurrence": 1066139, "reference": "Deu 19:6", "surface": "anger", "strong": "H3824", "as": "partner"}, {"occurrence": 1346063, "reference": "Lam 3:43", "surface": "anger", "strong": "H0639G", "as": "partner"}, {"occurrence": 1346071, "reference": "Lam 3:66", "surface": "anger", "strong": "H0639G", "as": "partner"}, {"occurrence": 1389457, "reference": "Amo 1:11", "surface": "anger", "strong": "H0639G", "as": "partner"}, {"occurrence": 1389464, "reference": "Amo 1:11", "surface": "wrath", "strong": "H5678", "as": "partner"}]
  older: [{"observation": 11923, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Anger has a course in time:", "verses": ["Gen.27.44", "Gen.27.45", "Amos.1.11", "Prov.19.19", "Eph.4.26"]}, {"observation": 11971, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Zion's lament from inside", "verses": ["Lam.1.12", "Lam.3.1", "Lam.3.43", "Lam.5.22"]}, {"observation": 12034, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Zion's lament: confession, and the anger felt from inside.", "verses": ["Lam.3.43", "Lam.1.12", "Lam.2.21", "Lam.2.22"]}, {"observation": 12037, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "The anger called down on those who seek one's life.", "verses": ["Ps.56.7", "Ps.69.24", "Jer.18.23", "Lam.3.66"]}, {"observation": 12050, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Against a brother: turned and forgotten, or kept forever.", "verses": ["Gen.27.45", "Amos.1.11", "Ezek.35.11", "1Sam.17.28", "1Sam.20.30"]}, {"observation": 12183, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "Anger kept forever, cursed.", "verses": ["Gen.49.6", "Gen.49.7", "Amos.1.11", "Isa.14.6", "Prov.22.8"]}, {"observation": 13320, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "The heat family outside the anger tag (ḥāmam, OT-15): \"the avenger of blood in hot anger\" (Deu 19:6).", "verses": ["Deut.19.6"]}, {"observation": 14724, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "What it does: \"Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow, which was brought upon me, which the Lord inflicted on the day of his fierce anger\" (Lam 1:12); \"The Lord has become like an enemy\" (2:5). \"He has bent his bow like an enemy … and he has killed all who were delightful in our eyes\" (2:4). \"The Lord has made Zion forget festival and Sabbath\" (2:6); \"you have killed them in the day of your anger, slaughtering without pity\" (2:21); \"on the day of the anger of the Lord no one escaped or survived\" (2:22); \"I am the man who has seen affliction under the rod of his wrath\" (3:1); \"You have wrapped yourself with anger and pursued us, killing without pity; you have wrapped yourself with a cloud so that no prayer can pass through\" (3:43–44); \"The Lord gave full vent to his wrath\" (4:11).", "verses": ["Lam.1.12", "Lam.2.5", "Lam.2.4", "Lam.2.6", "Lam.2.21", "Lam.2.22", "Lam.3.1", "Lam.3.43", "Lam.3.44", "Lam.4.11"]}, {"observation": 16453, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Redeemer = avenger [lexical]: \"the avenger [*gōʾēl*] of blood in hot anger [*his heart is hot*] pursue the manslayer [*strike his nephesh*]\" (Deu 19:6; Jos 20:3, 9). The kinsman-redeemer pursues a *nephesh* for a *nephesh*.", "verses": ["Deut.19.6", "Josh.20.3", "Josh.20.9"]}, {"observation": 17295, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "10.10 *Relating to others* | v15 | 1Sa 19:1–7 in *Loyalty and honour*; Deu 19:6 in *Anger between people*; new *Friends, company and care* (Job 6:15–18; Ecc 4:9–11; Job 31:19–20; Job 17:8–9 against 31:29–30; Pro 10:12; Song 2:7)", "verses": ["Deut.19.6"]}, {"observation": 18139, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Heat that kills (Deu 19:4–6). *\"lest the avenger of blood in hot anger pursue the manslayer … though the man did not deserve to die, since he had not hated his neighbor in the past\"*. The Hebrew says \"while his heart is hot\". The law builds cities of refuge because the heat of a grieving relative will not tell the innocent from the guilty. The law allows for the inner state and sets a distance between it and the act (\"because the way is long\").", "verses": ["Deut.19.4", "Deut.19.6"]}, {"observation": 21407, "stage": "engagement", "kind": "use", "nature": null, "text": "Anger is here the anger, wrath or fury of God against persons or nations (kindled, poured out, turned away, executed, provoked); it is God's own act upon them, and bears on their inner response, which other words of the verse name, if at all.", "verses": ["1Chr.13.10", "1Kgs.14.9", "1Kgs.15.30", "1Kgs.16.2", "1Kgs.16.7", "1Kgs.21.22", "2Chr.28.25", "2Chr.29.10", "2Chr.30.8", "2Chr.33.6", "2Chr.34.25", "2Kgs.13.3", "2Kgs.21.15", "2Kgs.21.6", "2Kgs.22.17", "2Kgs.23.19", "2Kgs.23.26", "2Kgs.24.20", "2Sam.24.1", "2Sam.6.7", "Dan.9.16", "Deut.11.17", "Deut.13.17", "Deut.29.20", "Deut.29.23", "Deut.29.24", "Deut.29.27", "Deut.29.28", "Deut.31.17", "Deut.31.29", "Deut.32.16", "Deut.32.21", "Deut.32.22", "Deut.6.15", "Deut.7.4", "Deut.9.19", "Exod.32.12", "Exod.34.6", "Exod.4.14", "Ezek.13.13", "Ezek.20.21", "Ezek.20.8", "Ezek.22.20", "Ezek.25.14", "Ezek.35.11", "Ezek.38.18", "Ezek.43.8", "Ezek.5.13", "Ezek.5.15", "Ezek.7.3", "Ezek.7.8", "Hab.3.12", "Hab.3.8", "Hos.11.9", "Hos.13.11", "Hos.14.4", "Hos.8.5", "Isa.10.25", "Isa.10.4", "Isa.10.5", "Isa.12.1", "Isa.13.13", "Isa.13.3", "Isa.13.9", "Isa.30.27", "Isa.30.30", "Isa.42.25", "Isa.48.9", "Isa.5.25", "Isa.54.8", "Isa.63.3", "Isa.63.6", "Isa.66.15", "Isa.9.12", "Isa.9.17", "Isa.9.21", "Jer.10.24", "Jer.11.17", "Jer.12.13", "Jer.15.14", "Jer.17.4", "Jer.18.23", "Jer.2.35", "Jer.21.5", "Jer.23.20", "Jer.25.37", "Jer.25.38", "Jer.25.6", "Jer.25.7", "Jer.3.12", "Jer.30.24", "Jer.32.29", "Jer.32.30", "Jer.32.31", "Jer.32.37", "Jer.33.5", "Jer.36.7", "Jer.4.26", "Jer.4.8", "Jer.42.18", "Jer.44.3", "Jer.44.6", "Jer.49.37", "Jer.51.45", "Jer.52.3", "Jer.7.18", "Jer.7.20", "Jer.8.19", "Job.20.23", "Job.21.17", "Job.35.15", "Job.4.9", "Job.40.11", "Job.42.7", "Job.9.13", "Job.9.5", "Joel.2.13", "Jonah.3.9", "Jonah.4.2", "Josh.23.16", "Josh.7.1", "Josh.7.26", "Judg.10.7", "Judg.2.14", "Judg.2.20", "Judg.3.8", "Judg.6.39", "Lam.1.12", "Lam.2.1", "Lam.2.21", "Lam.2.22", "Lam.2.3", "Lam.3.43", "Lam.3.66", "Lam.4.11", "Mic.5.15", "Mic.7.18", "Nah.1.3", "Nah.1.6", "Neh.4.5", "Neh.9.17", "Num.11.1", "Num.11.10", "Num.11.33", "Num.12.9", "Num.14.18", "Num.22.22", "Num.25.3", "Num.25.4", "Num.32.10", "Num.32.13", "Num.32.14", "Prov.24.18", "Ps.102.10", "Ps.103.8", "Ps.106.40", "Ps.145.8", "Ps.27.9", "Ps.30.5", "Ps.38.1", "Ps.6.1", "Ps.69.24", "Ps.7.6", "Ps.74.1", "Ps.77.9", "Ps.78.21", "Ps.78.31", "Ps.78.38", "Ps.78.49", "Ps.78.50", "Ps.78.58", "Ps.79.6", "Ps.85.3", "Ps.85.5", "Ps.86.15", "Ps.90.11", "Ps.90.7", "Rev.14.10", "Zech.10.3", "Zech.7.12", "Zeph.2.2", "Zeph.2.3", "Zeph.3.8"]}, {"observation": 21408, "stage": "engagement", "kind": "face", "nature": null, "text": "Anger is here the anger, wrath, rage or fury of a person or people: a state of the heart aroused against another, a thing or God, named by the word itself.", "verses": ["1Sam.11.6", "1Sam.17.28", "1Sam.20.30", "1Sam.20.34", "1Tim.2.8", "2Chr.21.16", "2Chr.25.10", "2Cor.12.20", "2Sam.11.20", "2Sam.12.5", "Amos.1.11", "Col.3.8", "Dan.11.20", "Deut.19.6", "Eccl.10.4", "Eccl.5.17", "Eccl.7.9", "Eph.4.26", "Eph.4.31", "Eph.6.4", "Esth.1.12", "Esth.2.1", "Exod.11.8", "Exod.32.19", "Exod.32.22", "Gal.5.20", "Gen.27.45", "Gen.30.2", "Gen.39.19", "Gen.44.18", "Gen.49.6", "Gen.49.7", "Heb.11.27", "Hos.7.6", "Isa.14.6", "Isa.7.4", "Jas.1.19", "Jas.1.20", "Job.18.4", "Job.32.2", "Job.32.3", "Job.32.5", "Job.36.13", "Judg.14.19", "Judg.8.3", "Judg.9.30", "Mark.3.5", "Matt.18.34", "Num.22.27", "Num.24.10", "Prov.14.29", "Prov.15.1", "Prov.15.18", "Prov.16.32", "Prov.19.11", "Prov.20.2", "Prov.21.14", "Prov.22.24", "Prov.27.4", "Prov.29.22", "Prov.30.33", "Ps.124.3", "Ps.37.8", "Ps.55.3"]}, {"observation": 21434, "stage": "engagement", "kind": "use", "nature": null, "text": "Wrath is here the anger, wrath or fury of God against persons or nations (kindled, poured out, turned away, executed, provoked); it is God's own act upon them, and bears on their inner response, which other words of the verse name, if at all.", "verses": ["1Chr.27.24", "1Sam.28.18", "1Thess.1.10", "1Thess.2.16", "1Thess.5.9", "2Chr.12.12", "2Chr.12.7", "2Chr.19.10", "2Chr.19.2", "2Chr.24.18", "2Chr.28.11", "2Chr.28.13", "2Chr.29.8", "2Chr.32.25", "2Chr.32.26", "2Chr.34.21", "2Chr.34.25", "2Chr.36.16", "2Kgs.22.13", "2Kgs.22.17", "2Kgs.23.26", "2Kgs.3.27", "Amos.1.11", "Col.3.6", "Dan.9.16", "Deut.29.23", "Deut.29.28", "Deut.9.22", "Deut.9.7", "Deut.9.8", "Eph.2.3", "Eph.5.6", "Exod.22.24", "Exod.32.10", "Exod.32.11", "Ezek.13.13", "Ezek.13.15", "Ezek.14.19", "Ezek.16.38", "Ezek.16.42", "Ezek.20.13", "Ezek.20.21", "Ezek.20.33", "Ezek.20.34", "Ezek.20.8", "Ezek.21.31", "Ezek.22.20", "Ezek.22.21", "Ezek.22.22", "Ezek.22.31", "Ezek.24.8", "Ezek.25.14", "Ezek.30.15", "Ezek.36.18", "Ezek.36.6", "Ezek.38.18", "Ezek.38.19", "Ezek.7.12", "Ezek.7.14", "Ezek.7.19", "Ezek.7.8", "Ezek.8.18", "Ezek.9.8", "Ezra.10.14", "Ezra.7.23", "Ezra.8.22", "Hab.3.2", "Hab.3.8", "Heb.3.11", "Heb.4.3", "Hos.11.9", "Hos.13.11", "Hos.5.10", "Isa.10.6", "Isa.13.13", "Isa.13.9", "Isa.27.4", "Isa.51.17", "Isa.51.20", "Isa.51.22", "Isa.59.18", "Isa.60.10", "Isa.63.3", "Isa.63.5", "Isa.63.6", "Isa.9.19", "Jer.10.10", "Jer.10.25", "Jer.18.20", "Jer.21.12", "Jer.21.5", "Jer.23.19", "Jer.25.15", "Jer.30.23", "Jer.32.31", "Jer.32.37", "Jer.33.5", "Jer.36.7", "Jer.4.4", "Jer.42.18", "Jer.44.6", "Jer.50.13", "Jer.50.25", "Jer.7.20", "Jer.7.29", "Job.14.13", "Job.16.9", "Job.19.11", "Job.19.29", "Job.20.28", "Job.21.20", "Job.21.30", "John.3.36", "Josh.22.20", "Josh.9.20", "Lam.2.2", "Lam.3.1", "Lam.4.11", "Lev.10.6", "Luke.21.23", "Luke.3.7", "Matt.3.7", "Mic.5.15", "Nah.1.6", "Neh.13.18", "Num.1.53", "Num.16.46", "Num.18.5", "Num.25.11", "Prov.11.23", "Prov.11.4", "Ps.106.23", "Ps.110.5", "Ps.2.12", "Ps.2.5", "Ps.21.9", "Ps.38.1", "Ps.56.7", "Ps.59.13", "Ps.6.1", "Ps.78.38", "Ps.78.49", "Ps.78.62", "Ps.85.3", "Ps.88.16", "Ps.88.7", "Ps.89.46", "Ps.90.11", "Ps.90.7", "Ps.90.9", "Ps.95.11", "Rev.11.18", "Rev.14.10", "Rev.14.19", "Rev.15.1", "Rev.15.7", "Rev.16.1", "Rev.16.19", "Rev.19.15", "Rev.6.16", "Rev.6.17", "Rom.1.18", "Rom.12.19", "Rom.13.4", "Rom.13.5", "Rom.2.5", "Rom.2.8", "Rom.4.15", "Rom.5.9", "Rom.9.22", "Zech.8.2", "Zeph.1.15", "Zeph.1.18"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2360
  item: pairing
  subject: ask
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["1Sa 30:8"]
  occurrences: [{"occurrence": 1127766, "reference": "1Sa 30:8", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1127777, "reference": "1Sa 30:8", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1127762, "reference": "1Sa 30:8", "surface": "inquired", "strong": "H7592", "as": "partner"}, {"occurrence": 1127763, "reference": "1Sa 30:8", "surface": "inquired", "strong": "H0559", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2361
  item: pairing
  subject: believe
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Rom 9:30", "1Ti 6:11", "2Ti 2:22"]
  occurrences: [{"occurrence": 1478924, "reference": "Rom 9:30", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1499466, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1161", "as": "member"}, {"occurrence": 1499467, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1500395, "reference": "2Ti 2:22", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1478931, "reference": "Rom 9:30", "surface": "faith", "strong": "G4102G", "as": "partner"}, {"occurrence": 1499470, "reference": "1Ti 6:11", "surface": "faith", "strong": "G4102G", "as": "partner"}, {"occurrence": 1500397, "reference": "2Ti 2:22", "surface": "faith", "strong": "G4102G", "as": "partner"}]
  older: [{"observation": 15465, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Where it comes from, in three verbs: Given: \"the fruit of the Spirit is … gentleness\" (Gal 5:22–23). In the same passage: \"Let us not become conceited\" (5:26); Pursued: \"Pursue righteousness, godliness, faith, love, steadfastness, gentleness\" (1Ti 6:11). It is pursued in flight from \"the love of money\" (6:10); Put on: Col 3:12 (group III).", "verses": ["Gal.5.22", "Gal.5.23", "Gal.5.26", "1Tim.6.11", "1Tim.6.10"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2362
  item: pairing
  subject: build
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Eze 35:6"]
  occurrences: [{"occurrence": 1348324, "reference": "Eze 35:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1348332, "reference": "Eze 35:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1348317, "reference": "Eze 35:6", "surface": "prepare", "strong": "H6213H", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2363
  item: pairing
  subject: call
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Jos 8:16", "Judg 7:23", "2Ti 2:22"]
  occurrences: [{"occurrence": 1090121, "reference": "Jos 8:16", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1090123, "reference": "Jos 8:16", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1090124, "reference": "Jos 8:16", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1090126, "reference": "Jos 8:16", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1108076, "reference": "Judg 7:23", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1500395, "reference": "2Ti 2:22", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1090120, "reference": "Jos 8:16", "surface": "called", "strong": "H2199", "as": "partner"}, {"occurrence": 1108066, "reference": "Judg 7:23", "surface": "called out", "strong": "H6817", "as": "partner"}, {"occurrence": 1500401, "reference": "2Ti 2:22", "surface": "call on", "strong": "G1941", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 58284
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "going after",
 "rows": [
  {
   "ledger_id": 2358,
   "item": "pairing",
   "subject": "abase",
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
     "observation": 15919,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2359,
   "item": "pairing",
   "subject": "anger",
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
     "observation": 11923,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 11971,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 12034,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 12037,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 12050,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 12183,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 13320,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 14724,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 16453,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 17295,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 18139,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 21407,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 21408,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 21434,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2360,
   "item": "pairing",
   "subject": "ask",
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
   "ledger_id": 2361,
   "item": "pairing",
   "subject": "believe",
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
     "observation": 15465,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2362,
   "item": "pairing",
   "subject": "build",
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
   "ledger_id": 2363,
   "item": "pairing",
   "subject": "call",
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
