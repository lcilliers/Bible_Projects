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

2026-11-26T16:13:45Z

## batch

- rows: 10
- rows_left_after_this: 32

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

- reference: Exo 14:4
  text: And I will harden Pharaoh’s heart, and he will pursue them, and I will get glory over Pharaoh and all his host, and the Egyptians shall know that I am the Lord.” And they did so.
  words: [" 0 harden H2388G HVpq1cs | word of another collection; collections harden", " 1 pharaoh’s H6547J HNtmsa | entity (human); party human", " 2 heart H3820A HNcmsc | word of another collection; collections heart", " 2 heart H0853 HTo | word of another collection; collections heart", "*3 pursue H7291 HVqq3ms | member of this collection", "*3 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 4 get glory H3513G HVNc1cs", " 4 them H9038 HSp3mp", " 5 pharaoh H6547J HNtmsa | entity (human); party human", " 5 in/on/with H9003 HR", " 6 all H3605 HNcmsc", " 6 and H9002 HC | connective", " 6 in/on/with H9003 HR", " 7 host H2428A HNcmsc", " 8 egyptians H4713 HNpl", " 9 know H3045 HVqq3cp | word of another collection; collections know", " 9 his H9023 HSp3ms", " 10 i H0589 HPp1bs", " 11 lord H3068G HNpt | entity (divine); party divine", " 11 lord H3588A HTc | connective", " 12 did H6213A HVqw3mp", " 13 so H3651C HD | qualifier candidate; qualifier morph: adverb"]
- reference: Exo 14:8
  text: And the Lord hardened the heart of Pharaoh king of Egypt, and he pursued the people of Israel while the people of Israel were going out defiantly.
  words: [" 0 lord H3068G HNpt | entity (divine); party divine", " 1 hardened H2388G HVpw3ms | word of another collection; collections harden", " 2 heart H3820A HNcmsc | word of another collection; collections heart", " 2 heart H0853 HTo | word of another collection; collections heart", " 3 pharaoh H6547J HNtmsa | entity (human); party human", " 4 king H4428G HNcmsc", " 5 egypt H4714G HNpl", "*6 pursued H7291 HVqw3ms | member of this collection", "*6 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 7 people H1121G HNcmpc", " 8 israel H3478 HNpl", " 9 people H1121G HNcmpc", " 9 and H9002 HC | connective", " 10 israel H3478 HNpl", " 11 going out H3318G HVqrmpa", " 12 defiantly H7311A HVqrfsa", " 12 defiantly H3027G HNcbsa", " 12 in/on/with H9003 HR"]
- reference: Deu 19:6
  text: lest the avenger of blood in hot anger pursue the manslayer and overtake him, because the way is long, and strike him fatally, though the man did not deserve to die, since he had not hated his neighbor in the past.
  words: [" 0 lest H6435 HTc | connective", " 1 avenger H1350H HVqrmsc", " 2 blood H1818 HNcmsa", " 2 [the] H9009 HTd", " 3 in H3588A HTc | connective", " 4 hot H2552 HVqi3ms", " 5 anger H3824 HNcmsc | word of another collection; collections anger", "*6 pursue H7291 HVqi3ms | member of this collection", "*6 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 7 manslayer H7523 HVqrmsa", " 7 [the] H9009 HTd", " 8 overtake H5381 HVhq3ms", " 8 his H9023 HSp3ms", " 9 him H5315I HNcfsa", " 9 him H9033 HSp3ms", " 10 because H3588A HTc | connective", " 10 him H9033 HSp3ms", " 11 way H1870L HNcbsa", " 11 [the] H9009 HTd", " 12 long H7235A HVqi3ms", " 13 strike him fatally H5221 HVhq3ms", " 14 not H0369 HNcmsc", " 14 and H9002 HC | connective", " 14 to/for H9005 HRd", " 14 him H9033 HSp3ms", " 15 deserve H4941G HNcmsc | word of another collection; collections govern", " 16 die H4194 HNcmsa | word of another collection; collections die", " 17 since H3588A HTc | connective", " 18 not H3808 HTn | negator; qualifier negator; negator", " 19 hated H8130 HVqrmsa | word of another collection; collections love", " 20 neighbor H8543 HNcmsa", " 20 from H9006 HR", " 20 neighbor H1931 HPp3ms", " 20 to/for H9005 HRd", " 20 him H9033 HSp3ms", " 21 past H8032 HNcmsa"]
- reference: Jos 8:24
  text: When Israel had finished killing all the inhabitants of Ai in the open wilderness where they pursued them, and all of them to the very last had fallen by the edge of the sword, all Israel returned to Ai and struck it down with the edge of the sword.
  words: [" 0 israel H3478 HNpl", " 1 finished H3615G HVpcc | word of another collection; collections fulfill", " 1 like/as H9004 HR", " 1 finished H1961 HVqw3ms | word of another collection; collections fulfill", " 2 killing H2026 HVqcc | word of another collection; collections kill", " 2 to/for H9005 HR", " 3 inhabitants H3427 HVqrmpc", " 4 ai H5857G HNpl", " 4 [the] H9009 HTd", " 5 open H7704G HNcmsa | word of another collection; collections open", " 5 in/on/with H9003 HRd", " 6 wilderness H4057B HNcmsa", " 6 in/on/with H9003 HRd", " 7 where H0834A HTr | connective", "*8 pursued H7291 HVqp3cp | member of this collection", " 9 all H3605 HNcmsc", " 9 all H0853 HTo", " 10 fallen H5307J HVqw3mp", " 10 them H9038 HSp3mp", " 10 in/on/with H9003 HRd", " 10 him H9033 HSp3ms", " 10 fallen H8552 HVqcc", " 11 edge H6310H HNcmsc", " 11 to/for H9005 HR", " 11 edge H3605 HNcmsc", " 11 their H9028 HSp3mp", " 12 sword H2719 HNcfsa", " 13 all H3605 HNcmsc", " 14 israel H3478 HNpl", " 15 returned H7725G HVqw3mp | word of another collection; collections return", " 15 returned H5704 HR | word of another collection; collections return", " 15 they H9048 HSp3mp", " 16 ai H5857G HNpl", " 16 [the] H9009 HTd", " 17 struck H5221 HVhw3mp", " 18 edge H6310H HNcmsc", " 18 to/for H9005 HR", " 18 edge H0853 HTo", " 18 her H9034 HSp3fs", " 19 sword H2719 HNcfsa"]
- reference: Judg 20:45
  text: And they turned and fled toward the wilderness to the rock of Rimmon. Five thousand men of them were cut down in the highways. And they were pursued hard to Gidom, and 2,000 men of them were struck down.
  words: [" 0 turned H6437G HVqw3mp | word of another collection; collections turn", " 1 fled H5127 HVqw3mp | word of another collection; collections escape", " 2 wilderness H4057B HNcmsa", " 2 [the] H9009 HTd", " 3 to H0413 HR", " 4 rock H5553H HNcmsc", " 4 [to] H9011 HSd", " 5 rimmon H7417C HNpl", " 5 [the] H9009 HTd", " 6 five H2568 HNcbsc", " 7 thousand H0505G HNcbpa", " 8 men H0376G HNcmsa | entity (human); party human", " 9 cut down H5953B HVpw3mp", " 10 highways H4546 HNcfpa", " 10 in/on/with H9003 HRd", " 10 him H9033 HSp3ms", "*11 pursued H1692 HVhw3mp | member of this collection", " 12 hard H0310A HAcmpc | word of another collection; qualifier morph: adjective; collections hard", " 13 gidom H1440 HNpl", " 13 him H9033 HSp3ms", " 13 gidom H5704 HR", " 14 2,000 H0505G HNcbda", " 14 2,000 H4480A HRd", " 14 him H9033 HSp3ms", " 15 men H0376G HNcmsa | entity (human); party human", " 16 struck down H5221 HVhw3mp"]
- reference: 1Sa 23:25
  text: And Saul and his men went to seek him. And David was told, so he went down to the rock and lived in the wilderness of Maon. And when Saul heard that, he pursued after David in the wilderness of Maon.
  words: [" 0 saul H7586G HNpm | entity (human); party human", " 1 men H0582 HNcmpc | entity (human); party human", " 1 and H9002 HC | connective", " 2 went H1980G HVqw3ms", " 3 seek H1245 HVpcc | word of another collection; collections search", " 3 to/for H9005 HR", " 3 his H9023 HSp3ms", " 4 david H1732 HNpm | entity (human); party human", " 4 to/for H9005 HR", " 5 told H5046 HVhw3mp", " 6 went down H3381 HVqw3ms", " 7 rock H5553H HNcmsa", " 7 [the] H9009 HTd", " 8 lived H3427 HVqw3ms | word of another collection; collections live", " 9 wilderness H4057B HNcmsc", " 9 in/on/with H9003 HR", " 10 maon H4584G HNpl", " 11 saul H7586G HNpm | entity (human); party human", " 12 heard H8085G HVqw3ms | word of another collection; collections hear", "*13 pursued H7291 HVqw3ms | member of this collection", " 14 after H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 15 david H1732 HNpm | entity (human); party human", " 16 wilderness H4057B HNcmsc", " 17 maon H4584G HNpl"]
- reference: 2Sa 20:6
  text: And David said to Abishai, “ Now Sheba the son of Bichri will do us more harm than Absalom. Take your lord’s servants and pursue him, lest he get himself to fortified cities and escape from us.”
  words: [" 0 david H1732 HNpm | entity (human); party human", " 1 said H0559 HVqw3ms", " 2 to H0413 HR", " 3 abishai H0052 HNpm | entity (human); party human", " 4 now H6258 HD | qualifier candidate; qualifier morph: adverb", " 5 sheba H7652A HNpm | entity (human); party human", " 5 to/for H9005 HRd", " 5 us H9035 HSp1bp", " 6 son H1121A HNcmsc", " 7 bichri H1075 HNpm | entity (human); party human", " 8 more harm H7489A HVqi3ms", " 9 than H4480A HR", " 10 absalom H0053 HNpm | entity (human); party human", " 11 take H3947G HVqv2ms | word of another collection; collections snatch", " 11 take H0859A HPp2ms | word of another collection; collections snatch", " 12 lord’s H0113 HNcmpc", " 13 servants H5650 HNcmpc | entity (human); party human", " 13 servants H0853 HTo", "*14 pursue H7291 HVqv2ms | member of this collection", " 14 your H9021 HSp2ms", "*14 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 15 lest H6435 HTc | connective", " 15 him H9033 HSp3ms", " 16 get H4672 HVqp3ms", " 17 fortified H1219 HAafpa | word of another collection; qualifier morph: adjective; collections guard", " 18 cities H5892B HNcmpa", " 18 to/for H9005 HRd", " 18 him H9033 HSp3ms", " 19 escape H5337 HVhq3ms | word of another collection; collections escape", " 20 us H5869J HNcfsc", " 20 our H9025 HSp1bp"]
- reference: Job 19:22
  text: Why do you, like God, pursue me? Why are you not satisfied with my flesh?
  words: [" 0 why H4100 HPi", " 0 to/for H9005 HR", " 1 god H0410G HNcmsa | entity (divine); party divine", " 1 me H9030 HSp1bs", " 1 like H3644G HR", "*2 pursue H7291 HVqi2mp | member of this collection", " 3 not H3808 HTn | negator; qualifier negator; negator", " 3 my H9020 HSp1bs", " 4 satisfied H7646 HVqi2mp | word of another collection; collections fulfill", " 5 flesh H1320 HNcmsc", " 5 and H9002 HC | connective", " 5 from H9006 HR"]
- reference: Psa 71:11
  text: and say, “ God has forsaken him; pursue and seize him, for there is none to deliver him.”
  words: [" 0 say H0559 HVqcc", " 0 to/for H9005 HR", " 1 god H0430G HNcmpa | entity (divine); party divine", " 2 forsaken H5800A HVqp3ms | word of another collection; collections forsake", "*3 pursue H7291 HVqv2mp | member of this collection", " 3 him H9033 HSp3ms", " 4 seize H8610 HVqv2mp | word of another collection; collections snatch", " 5 for H3588A HTc | connective", " 5 him H9033 HSp3ms", " 6 none H0369 HNcmsc", " 7 deliver H5337 HVhrmsa | word of another collection; collections save"]
- reference: Psa 109:16
  text: For he did not remember to show kindness, but pursued the poor and needy and the brokenhearted, to put them to death.
  words: [" 0 for H3282 HC | connective", " 0 for H0834A HTr | connective", " 1 not H3808 HTn | negator; qualifier negator; negator", " 2 remember H2142 HVqp3ms | word of another collection; collections forget", " 3 show H6213A HVqcc", " 4 kindness H2617A HNcmsa | word of another collection; collections compassion", "*5 pursued H7291 HVqw3ms | member of this collection", " 6 poor H6041 HAamsa | word of another collection; qualifier morph: adjective; collections rich", " 7 needy H0034 HAamsa | word of another collection; qualifier morph: adjective; collections rich", " 7 and H9002 HC | connective", " 7 needy H0376I HNcmsa | word of another collection; collections rich", " 8 brokenhearted H3512A HVNrmsc | word of another collection; collections pain", " 8 brokenhearted H3824 HNcmsa | word of another collection; collections pain", " 9 death H4191 HVpcc | word of another collection; collections die", " 9 to/for H9005 HR"]
- reference: Isa 51:1
  text: “ Listen to me, you who pursue righteousness, you who seek the Lord: look to the rock from which you were hewn, and to the quarry from which you were dug.
  words: [" 0 listen H8085G HVqv2mp | word of another collection; collections hear", " 1 to H0413 HR", "*2 pursue H7291 HVqrmpc | member of this collection", " 2 me H9030 HSp1bs", " 3 righteousness H6664G HNcmsa | word of another collection; collections righteous", " 4 seek H1245 HVprmpc | word of another collection; collections search", " 5 lord H3068G HNpt | entity (divine); party divine", " 6 look H5027 HVhv2mp", " 7 to H0413 HR", " 8 rock H6697H HNcmsa", " 9 hewn H2672 HVPp2mp", " 10 to H0413 HR", " 11 quarry H4718B HNcfsc", " 11 and H9002 HC | connective", " 11 quarry H0953A HNcmsa", " 12 dug H5365 HVPp2mp"]
- reference: Hos 8:3
  text: Israel has spurned the good; the enemy shall pursue him.
  words: [" 0 israel H3478 HNpl", " 1 spurned H2186A HVqp3ms | word of another collection; collections forsake", " 2 good H2896B HAamsa | qualifier candidate; qualifier qualifier subgroup: Good, better, right (a quality of something); morph: adjective", " 3 enemy H0341 HVqrmsa", "*4 pursue H7291 HVqi3ms | member of this collection", " 5 him H9033 HSp3ms"]
- reference: Nah 1:8
  text: But with an overflowing flood he will make a complete end of the adversaries, and will pursue his enemies into darkness.
  words: [" 0 overflowing H5674A HVqrmsa", " 1 flood H7858 HNcmsa", " 1 and H9002 HC | connective", " 1 in/on/with H9003 HR", " 2 make H6213H HVqi3ms", " 3 complete H3617 HNcfsa | word of another collection; collections fulfill", " 4 adversaries H4725 HNcmsc", "*5 pursue H7291 HVpi3ms | member of this collection", " 5 his H9023 HSp3ms", " 6 enemies H0341 HVqrmpc", " 6 and H9002 HC | connective", " 6 her H9024 HSp3fs", " 7 darkness H2822 HNcmsa"]
- reference: 1Ti 6:11
  text: But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.
  words: [" 0 but G1161 CONJ | connective", " 1 you G4771 P-2NS", " 2 o G5599 INJ", " 3 man G0444 N-VSM | entity (human); party human", " 4 god G2316 N-GSM-T | entity (divine); party divine", " 5 flee G5343 V-PAM-2S | word of another collection; collections escape", " 6 these G3778 D-APN", "*7 pursue G1161 CONJ | member of this collection", "*7 pursue G1377 V-PAM-2S | member of this collection", " 8 righteousness G1343 N-ASF | word of another collection; collections righteous", " 9 godliness G2150 N-ASF | word of another collection; collections godly", " 10 faith G4102G N-ASF | word of another collection; collections believe", " 11 love G0026 N-ASF | word of another collection; collections love", " 12 steadfastness G5281 N-ASF | word of another collection; collections loyalty", " 13 gentleness G4239 N-ASF | word of another collection; collections compassion"]
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
  words: [" 0 so G1161 CONJ | connective", " 1 flee G5343 V-PAM-2S | word of another collection; collections escape", " 2 youthful G3512 A-APF | qualifier candidate; qualifier morph: adjective", " 3 passions G1939 N-APF | word of another collection; collections desire", " 4 and G1161 CONJ | connective", "*5 pursue G1377 V-PAM-2S | member of this collection", " 6 righteousness G1343 N-ASF | word of another collection; collections righteous", " 7 faith G4102G N-ASF | word of another collection; collections believe", " 8 love G0026 N-ASF | word of another collection; collections love", " 9 peace G1515 N-ASF | word of another collection; collections quarrel", " 10 with G3326 PREP", " 11 call on G1941 V-PMP-GPM | word of another collection; collections call", " 12 lord G2962G N-ASM-T | entity (divine); party divine", " 13 from G1537 PREP", " 14 pure G2513 A-GSF | word of another collection; qualifier morph: adjective; collections cleanse", " 15 heart G2588 N-GSF | word of another collection; collections heart"]

## rows

- ledger_id: 2384
  item: pairing
  subject: forget
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 109:16"]
  occurrences: [{"occurrence": 1254311, "reference": "Psa 109:16", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1254308, "reference": "Psa 109:16", "surface": "remember", "strong": "H2142", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2385
  item: pairing
  subject: forsake
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 71:11", "Hos 8:3"]
  occurrences: [{"occurrence": 1255503, "reference": "Psa 71:11", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1387729, "reference": "Hos 8:3", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1255502, "reference": "Psa 71:11", "surface": "forsaken", "strong": "H5800A", "as": "partner"}, {"occurrence": 1387726, "reference": "Hos 8:3", "surface": "spurned", "strong": "H2186A", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2386
  item: pairing
  subject: fulfill
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Jos 8:24", "Job 19:22", "Nah 1:8"]
  occurrences: [{"occurrence": 1096929, "reference": "Jos 8:24", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1239904, "reference": "Job 19:22", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1396159, "reference": "Nah 1:8", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1096916, "reference": "Jos 8:24", "surface": "finished", "strong": "H3615G", "as": "partner"}, {"occurrence": 1096918, "reference": "Jos 8:24", "surface": "finished", "strong": "H1961", "as": "partner"}, {"occurrence": 1239907, "reference": "Job 19:22", "surface": "satisfied", "strong": "H7646", "as": "partner"}, {"occurrence": 1396157, "reference": "Nah 1:8", "surface": "complete", "strong": "H3617", "as": "partner"}]
  older: [{"observation": 16478, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Flesh devoured: \"Why are you not satisfied with my flesh?\" (Job 19:22); \"each devours the flesh of his own arm\" (Isa 9:20); \"I will make your oppressors eat their own flesh\" (Isa 49:26).", "verses": ["Job.19.22", "Isa.9.20", "Isa.49.26"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2387
  item: pairing
  subject: godly
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["1Ti 6:11"]
  occurrences: [{"occurrence": 1499466, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1161", "as": "member"}, {"occurrence": 1499467, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1499469, "reference": "1Ti 6:11", "surface": "godliness", "strong": "G2150", "as": "partner"}]
  older: [{"observation": 20187, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Toward riches: *\"those who desire to be rich fall into temptation, into a snare, into many senseless and harmful desires that plunge people into ruin\"* (1Ti 6:9). Beside it: *\"godliness with contentment is great gain\"* (6:6), and *\"flee these things. Pursue righteousness\"* (6:11).", "verses": ["1Tim.6.9", "1Tim.6.6", "1Tim.6.11"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2388
  item: pairing
  subject: govern
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Deu 19:6"]
  occurrences: [{"occurrence": 1066140, "reference": "Deu 19:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1066141, "reference": "Deu 19:6", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1066158, "reference": "Deu 19:6", "surface": "deserve", "strong": "H4941G", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2389
  item: pairing
  subject: guard
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["2Sa 20:6"]
  occurrences: [{"occurrence": 1140278, "reference": "2Sa 20:6", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1140280, "reference": "2Sa 20:6", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1140284, "reference": "2Sa 20:6", "surface": "fortified", "strong": "H1219", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2390
  item: pairing
  subject: hard
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Judg 20:45"]
  occurrences: [{"occurrence": 1113438, "reference": "Judg 20:45", "surface": "pursued", "strong": "H1692", "as": "member"}, {"occurrence": 1113439, "reference": "Judg 20:45", "surface": "hard", "strong": "H0310A", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2391
  item: pairing
  subject: harden
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Exo 14:4", "Exo 14:8"]
  occurrences: [{"occurrence": 1007225, "reference": "Exo 14:4", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1007226, "reference": "Exo 14:4", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1017218, "reference": "Exo 14:8", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1017219, "reference": "Exo 14:8", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1007221, "reference": "Exo 14:4", "surface": "harden", "strong": "H2388G", "as": "partner"}, {"occurrence": 1017212, "reference": "Exo 14:8", "surface": "hardened", "strong": "H2388G", "as": "partner"}]
  older: [{"observation": 13752, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "God hardens a human seat (19 verses): Pharaoh (Exo 4:21; 7:3; 9:12; 10:1, 20, 27; 11:10; 14:4, 8) and the Egyptians (14:17); Sihon, \"the Lord your God hardened his spirit and made his heart obstinate\" (Deu 2:30); the Canaanites (Jos 11:20); \"Make the heart of this people dull [heavy]\" (Isa 6:10); \"why do you ... harden our heart?\" (Isa 63:17); Joh 12:40; Rom 9:18; \"I gave them over to their stubborn hearts\" (Psa 81:12).", "verses": ["Exod.4.21", "Exod.7.3", "Exod.9.12", "Exod.10.1", "Exod.10.20", "Exod.10.27", "Exod.11.10", "Exod.14.4", "Exod.14.8", "Exod.14.17", "Deut.2.30", "Josh.11.20", "Isa.6.10", "Isa.63.17", "John.12.40", "Rom.9.18", "Ps.81.12"]}, {"observation": 13764, "stage": "prior-capture", "kind": "term", "nature": null, "text": "The same root, used of God, means glory: kaved, \"to be heavy\", is the word for Pharaoh's hardened heart (Exo 8:15, 32; 9:34; 10:1), and in the same narrative God says \"I will harden [chazaq] Pharaoh's heart ... and I will get glory [kaved] over Pharaoh\" (Exo 14:4, 17); the root that makes the human heart heavy makes God glorious (also Lev 10:3; Isa 26:15; Hag 1:8; Eze 28:22; 39:13).", "verses": ["Exod.8.15", "Exod.8.32", "Exod.9.34", "Exod.10.1", "Exod.14.4", "Exod.14.17"]}, {"observation": 16069, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Hardening | \"I will harden [*strengthen*] his heart\" (Exo 4:21); \"Pharaoh's heart was hardened\" (Exo 7:13, 22; 8:19; 9:12, 35; 10:20, 27; 11:10; 14:4, 8, 17); \"to harden their hearts … that they should come against Israel\" (Jos 11:20); \"you shall not harden your heart or shut your hand against your poor brother\" (Deu 15:7); Zedekiah \"hardened his heart against turning to the Lord\" (2Ch 36:13)", "verses": ["Exod.4.21", "Exod.7.13", "Exod.7.22", "Exod.8.19", "Exod.9.12", "Exod.9.35", "Exod.10.20", "Exod.10.27", "Exod.11.10", "Exod.14.4", "Exod.14.8", "Exod.14.17", "Josh.11.20", "Deut.15.7", "2Chr.36.13"]}, {"observation": 16731, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Hardened: \"the Lord hardened the heart of Pharaoh king of Egypt\" (Exo 14:8; 4:21); \"the Lord your God hardened his spirit and made his heart obstinate, that he might give him into your hand\" (Deu 2:30) [H1] (Sihon)", "verses": ["Exod.14.8", "Exod.4.21", "Deut.2.30"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2392
  item: pairing
  subject: hear
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["1Sa 23:25", "Isa 51:1"]
  occurrences: [{"occurrence": 1130463, "reference": "1Sa 23:25", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1306545, "reference": "Isa 51:1", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1130462, "reference": "1Sa 23:25", "surface": "heard", "strong": "H8085G", "as": "partner"}, {"occurrence": 1306543, "reference": "Isa 51:1", "surface": "listen", "strong": "H8085G", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2393
  item: pairing
  subject: heart
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Exo 14:4", "Exo 14:8", "2Ti 2:22"]
  occurrences: [{"occurrence": 1007225, "reference": "Exo 14:4", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1007226, "reference": "Exo 14:4", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1017218, "reference": "Exo 14:8", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1017219, "reference": "Exo 14:8", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1500395, "reference": "2Ti 2:22", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1007223, "reference": "Exo 14:4", "surface": "heart", "strong": "H3820A", "as": "partner"}, {"occurrence": 1007224, "reference": "Exo 14:4", "surface": "heart", "strong": "H0853", "as": "partner"}, {"occurrence": 1017213, "reference": "Exo 14:8", "surface": "heart", "strong": "H3820A", "as": "partner"}, {"occurrence": 1017214, "reference": "Exo 14:8", "surface": "heart", "strong": "H0853", "as": "partner"}, {"occurrence": 1500405, "reference": "2Ti 2:22", "surface": "heart", "strong": "G2588", "as": "partner"}]
  older: [{"observation": 15880, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Revisit 2026-09-28: Pharaoh's hardening is also expressed by *ḥāzaq* \"make strong\" (Exo 4:21; 7:13; 14:4, 8), which is filed in M23 Strength & Courage. The same verb gives \"be strong, let your heart take courage\" (Psa 27:14).; In context (Exo 14:4–8), the hardening gives firmness to a change of heart Pharaoh had already made (\"What is this we have done?\", 14:5).; See Batch G §3.3. The data therefore hold hardening under grief (heavy), rebellion (Batch C §9.3) and strength, according to the root.", "verses": ["Exod.4.21", "Exod.7.13", "Exod.14.4", "Exod.14.8", "Ps.27.14"]}]
  older_answered_under_another_row: [{"observation": 13752, "answered_under": 2391}, {"observation": 13764, "answered_under": 2391}, {"observation": 16069, "answered_under": 2391}, {"observation": 16731, "answered_under": 2391}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 57632
- seconds: 0.04

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "going after",
 "rows": [
  {
   "ledger_id": 2384,
   "item": "pairing",
   "subject": "forget",
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
   "ledger_id": 2385,
   "item": "pairing",
   "subject": "forsake",
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
   "ledger_id": 2386,
   "item": "pairing",
   "subject": "fulfill",
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
     "observation": 16478,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2387,
   "item": "pairing",
   "subject": "godly",
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
     "observation": 20187,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2388,
   "item": "pairing",
   "subject": "govern",
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
   "ledger_id": 2389,
   "item": "pairing",
   "subject": "guard",
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
   "ledger_id": 2390,
   "item": "pairing",
   "subject": "hard",
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
   "ledger_id": 2391,
   "item": "pairing",
   "subject": "harden",
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
     "observation": 13752,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 13764,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 16069,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 16731,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2392,
   "item": "pairing",
   "subject": "hear",
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
   "ledger_id": 2393,
   "item": "pairing",
   "subject": "heart",
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
     "observation": 15880,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  }
 ]
}
```
