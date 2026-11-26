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

2026-11-26T16:12:15Z

## batch

- rows: 11
- rows_left_after_this: 51

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

- reference: Deu 28:22
  text: The Lord will strike you with wasting disease and with fever, inflammation and fiery heat, and with drought and with blight and with mildew. They shall pursue you until you perish.
  words: [" 0 lord H3068G HNpt | entity (divine); party divine", " 0 you H9031 HSp2ms", " 1 strike H5221 HVhi3ms | word of another collection; collections cruel", " 2 wasting disease H7829 HNcfsa", " 2 in/on/with H9003 HRd", " 3 fever H6920 HNcfsa", " 3 and H9002 HC | connective", " 3 in/on/with H9003 HRd", " 4 inflammation H1816 HNcfsa", " 4 and H9002 HC | connective", " 4 in/on/with H9003 HRd", " 5 fiery heat H2746 HNcmsa", " 5 and H9002 HC | connective", " 5 in/on/with H9003 HRd", " 6 drought H2719 HNcfsa", " 6 and H9002 HC | connective", " 6 in/on/with H9003 HRd", " 7 blight H7711B HNcmsa", " 7 and H9002 HC | connective", " 7 in/on/with H9003 HRd", " 8 mildew H3420 HNcmsa", " 8 and H9002 HC | connective", " 8 in/on/with H9003 HRd", "*9 pursue H7291 HVqq3cp | member of this collection", " 10 until H5704 HR", " 10 you H9031 HSp2ms", " 11 you H9041 HSp2ms", " 12 perish H0006 HVqcc | word of another collection; collections die"]
- reference: Deu 28:45
  text: “ All these curses shall come upon you and pursue you and overtake you till you are destroyed, because you did not obey the voice of the Lord your God, to keep his commandments and his statutes that he commanded you.
  words: [" 0 all H3605 HNcmsc", " 0 you H9031 HSp2ms", " 1 these H0428 HTm", " 1 [the] H9009 HTd", " 2 curses H7045 HNcfpa", " 2 [the] H9009 HTd", " 3 come H0935G HVqq3cp", " 4 upon H5921A HRd", "*5 pursue H7291 HVqq3cp | member of this collection", " 6 overtake H5381 HVhq3cp", " 6 you H9031 HSp2ms", " 7 till H5704 HR", " 7 you H9031 HSp2ms", " 8 destroyed H8045 HVNcc | word of another collection; collections destruction", " 9 because H3588A HTc | connective", " 9 you H9041 HSp2ms", " 10 not H3808 HTn | negator; qualifier negator; negator", " 11 obey H8085H HVqp2ms | word of another collection; collections convince", " 12 voice H6963A HNcmsc", " 12 in/on/with H9003 HR", " 13 lord H3068G HNpt | entity (divine); party divine", " 14 god H0430G HNcmpc | entity (divine); party divine", " 15 keep H8104G HVqcc | word of another collection; collections remove", " 15 to/for H9005 HR", " 15 your H9021 HSp2ms", " 16 commandments H4687 HNcfpc", " 17 statutes H2708 HNcfpc", " 17 and H9002 HC | connective", " 17 his H9023 HSp3ms", " 18 that H0834A HTr | connective", " 18 his H9023 HSp3ms", " 19 commanded H6680 HVpp3ms | word of another collection; collections command", " 20 you H9031 HSp2ms"]
- reference: 2Sa 2:28
  text: So Joab blew the trumpet, and all the men stopped and pursued Israel no more, nor did they fight anymore.
  words: [" 0 joab H3097G HNpm | entity (human); party human", " 1 blew H8628 HVqw3ms", " 2 trumpet H7782 HNcmsa", " 2 in/on/with H9003 HRd", " 3 all H3605 HNcmsc", " 4 men H5971K HNcmsa", " 4 [the] H9009 HTd", " 5 stopped H5975G HVqw3mp | word of another collection; collections self-control", "*6 pursued H7291 HVqi3mp | member of this collection", "*6 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 7 israel H3478 HNpl", " 7 israel H5750 HAcmsa | qualifier candidate; qualifier morph: adjective", " 8 no H3808 HTn | negator; qualifier negator; negator", " 9 nor H9002 HC | connective", " 10 fight H3898A HVNcc | word of another collection; collections combat", " 10 to/for H9005 HR", " 10 fight H5750 HAcmsa | word of another collection; qualifier morph: adjective; collections combat", " 11 anymore H3254G HVqp3cp", " 11 anymore H3808 HTn | negator; qualifier negator; negator", " 11 and H9002 HC | connective"]
- reference: 2Sa 17:1
  text: Moreover, Ahithophel said to Absalom, “ Let me choose twelve thousand men, and I will arise and pursue David tonight.
  words: [" 0 ahithophel H0302 HNpm | entity (human); party human", " 1 said H0559 HVqw3ms", " 2 to H0413 HR", " 3 absalom H0053 HNpm | entity (human); party human", " 4 let H4994 HTj", " 5 choose H0977 HVqc1cs | word of another collection; collections choose", " 6 twelve H8147 HNcbda", " 6 twelve H6240 HNcbsa", " 7 thousand H0505G HNcbsa", " 8 men H0376G HNcmsa | entity (human); party human", " 9 arise H6965B HVqc1cs", "*10 pursue H7291 HVqc1cs | member of this collection", "*10 pursue H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 11 david H1732 HNpm | entity (human); party human", " 12 tonight H3915 HNcmsa", " 12 [the] H9009 HTd"]
- reference: 2Sa 24:13
  text: So Gad came to David and told him, and said to him, “Shall three years of famine come to you in your land? Or will you flee three months before your foes while they pursue you? Or shall there be three days ’ pestilence in your land? Now consider, and decide what answer I shall return to him who sent me.”
  words: [" 0 gad H1410H HNpm | entity (human); party human", " 1 came H0935G HVqw3ms", " 2 to H0413 HR", " 3 david H1732 HNpm | entity (human); party human", " 4 told H5046 HVhw3ms", " 5 said H0559 HVqw3ms", " 5 to/for H9005 HRd", " 5 him H9033 HSp3ms", " 6 years H8141 HNcmpa", " 6 to/for H9005 HRd", " 6 you H9031 HSp2ms", " 6 years H7651 HNcbsa", " 7 famine H7458 HNcmsa", " 8 come H0935G HVqi3fs", " 8 [¿] H9008 HTi", " 8 to/for H9005 HRd", " 8 him H9033 HSp3ms", " 9 land H0776G HNcfsc", " 9 in/on/with H9003 HR", " 10 flee H5127 HVqcc | word of another collection; collections escape", " 11 three H7969 HNcbsa", " 11 your H9021 HSp2ms", " 11 three H0518H HTc | connective", " 12 months H2320G HNcmpa", " 13 before H6440G HNcmpc", " 13 to/for H9005 HR", " 13 you H9041 HSp2ms", " 14 foes H6862C HNcmpc", " 15 they H1931 HPp3ms", "*16 pursue H7291 HVqrmsc | member of this collection", " 16 your H9021 HSp2ms", " 16 and H9002 HC", " 17 be H1961 HVqcc", " 18 three H7969 HNcbsc", " 18 you H9031 HSp2ms", " 18 three H0518H HTc | connective", " 18 and H9002 HC | connective", " 19 days H3117G HNcmpa", " 20 pestilence H1698 HNcmsa", " 21 land H0776G HNcfsc", " 21 in/on/with H9003 HR", " 22 now H6258 HD | qualifier candidate; qualifier morph: adverb", " 23 consider H3045 HVqv2ms | word of another collection; collections wise", " 23 your H9021 HSp2ms", " 24 decide H7200J HVqv2ms | word of another collection; collections choose", " 25 answer H1697H HNcmsa | word of another collection; collections profess", " 25 me H9030 HSp1bs", " 26 return H7725G HVhi1cs | word of another collection; collections return", " 26 return H4100 HPi | word of another collection; collections return", " 27 sent H7971G HVqrmsc"]
- reference: Job 13:25
  text: Will you frighten a driven leaf and pursue dry chaff?
  words: [" 0 frighten H6206 HVqi2ms | word of another collection; collections fear", " 1 driven H5086 HVNrmsa | word of another collection; collections compel", " 2 leaf H5929 HNcmsa", " 2 [¿] H9008 HTi", "*3 pursue H7291 HVqi2ms | member of this collection", " 4 dry H3002 HAamsa | word of another collection; qualifier morph: adjective; collections dry", " 5 chaff H7179 HNcmsa", " 5 chaff H0853 HTo", " 5 and H9002 HC | connective"]
- reference: Psa 109:16
  text: For he did not remember to show kindness, but pursued the poor and needy and the brokenhearted, to put them to death.
  words: [" 0 for H3282 HC | connective", " 0 for H0834A HTr | connective", " 1 not H3808 HTn | negator; qualifier negator; negator", " 2 remember H2142 HVqp3ms | word of another collection; collections forget", " 3 show H6213A HVqcc", " 4 kindness H2617A HNcmsa | word of another collection; collections compassion", "*5 pursued H7291 HVqw3ms | member of this collection", " 6 poor H6041 HAamsa | word of another collection; qualifier morph: adjective; collections rich", " 7 needy H0034 HAamsa | word of another collection; qualifier morph: adjective; collections rich", " 7 and H9002 HC | connective", " 7 needy H0376I HNcmsa | word of another collection; collections rich", " 8 brokenhearted H3512A HVNrmsc | word of another collection; collections pain", " 8 brokenhearted H3824 HNcmsa | word of another collection; collections pain", " 9 death H4191 HVpcc | word of another collection; collections die", " 9 to/for H9005 HR"]
- reference: Jer 29:18
  text: I will pursue them with sword, famine, and pestilence, and will make them a horror to all the kingdoms of the earth, to be a curse, a terror, a hissing, and a reproach among all the nations where I have driven them,
  words: ["*0 pursue H7291 HVqq1cs | member of this collection", " 1 them H0310A HAcmpc | qualifier candidate; qualifier morph: adjective", " 2 sword H2719 HNcfsa", " 2 in/on/with H9003 HRd", " 2 them H9038 HSp3mp", " 3 famine H7458 HNcmsa", " 3 in/on/with H9003 HRd", " 4 pestilence H1698 HNcmsa", " 4 and H9002 HC | connective", " 4 in/on/with H9003 HRd", " 5 make H5414I HVqq1cs", " 6 horror H2189 HNcfsa | word of another collection; collections fear", " 6 to/for H9005 HR", " 6 them H9038 HSp3mp", " 7 all H3605 HNcmsc", " 7 to/for H9005 HR", " 8 kingdoms H4467 HNcfpc", " 9 earth H0776G HNcfsa", " 9 [the] H9009 HTd", " 10 to H9005 HR", " 11 curse H0423 HNcfsa", " 12 terror H8047H HNcfsa | word of another collection; collections fear", " 12 and H9002 HC | connective", " 12 to/for H9005 HR", " 13 hissing H8322 HNcfsa", " 13 and H9002 HC | connective", " 13 to/for H9005 HR", " 14 reproach H2781 HNcfsa | word of another collection; collections chide", " 14 and H9002 HC | connective", " 14 to/for H9005 HR", " 15 all H3605 HNcmsc", " 15 in/on/with H9003 HR", " 16 nations H1471A HNcmpa", " 16 [the] H9009 HTd", " 17 where H8033G HD | qualifier candidate; qualifier morph: adverb", " 17 them H9038 HSp3mp", " 18 driven H5080 HVhp1cs | word of another collection; collections compel", " 18 driven H0834A HTr | word of another collection; collections compel"]
- reference: Jer 39:5
  text: But the army of the Chaldeans pursued them and overtook Zedekiah in the plains of Jericho. And when they had taken him, they brought him up to Nebuchadnezzar king of Babylon, at Riblah, in the land of Hamath; and he passed sentence on him.
  words: [" 0 army H2428A HNcmsc", " 1 chaldeans H3778 HNpl", "*2 pursued H7291 HVqw3mp | member of this collection", "*2 pursued H0310A HAcmpc | member of this collection; qualifier morph: adjective", " 3 overtook H5381 HVhw3mp", " 3 them H9038 HSp3mp", " 4 zedekiah H6667H HNpm | entity (human); party human", " 4 zedekiah H0853 HTo", " 5 plains H6160L HNcfpc", " 5 in/on/with H9003 HR", " 6 jericho H3405G HNpl", " 7 taken H3947G HVqw3mp | word of another collection; collections snatch", " 8 up H5927H HVhw3mp", " 8 up H0853 HTo", " 8 him H9033 HSp3ms", " 9 to H0413 HR", " 10 nebuchadnezzar H5019 HNpm | entity (human); party human", " 10 him H9033 HSp3ms", " 11 king H4428G HNcmsc", " 12 babylon H0894 HNpl", " 13 riblah H7247H HNpl", " 14 land H0776G HNcfsc", " 14 in/on/with H9003 HR", " 14 [to] H9011 HSd", " 15 hamath H2574G HNpl", " 16 passed H1696I HVpw3ms", " 17 sentence H4941G HNcmpa | word of another collection; collections condemn", " 17 sentence H0854 HRd | word of another collection; collections condemn", " 17 him H9033 HSp3ms"]
- reference: Lam 3:43
  text: “You have wrapped yourself with anger and pursued us, killing without pity;
  words: [" 0 wrapped H5526B HVqp2ms", " 1 anger H0639G HNcmsa | word of another collection; collections anger", " 1 in/on/with H9003 HRd", "*2 pursued H7291 HVqw2ms | member of this collection", " 3 killing H2026 HVqp2ms | word of another collection; collections kill", " 3 us H9035 HSp1bp", " 4 without H3808 HTn | negator; qualifier negator; negator", " 5 pity H2550 HVqp2ms | word of another collection; collections compassion"]
- reference: Amo 1:11
  text: Thus says the Lord: “For three transgressions of Edom, and for four, I will not revoke the punishment, because he pursued his brother with the sword and cast off all pity, and his anger tore perpetually, and he kept his wrath forever.
  words: [" 0 says H0559 HVqp3ms", " 0 thus H3541 HD | qualifier candidate; qualifier morph: adverb", " 1 lord H3068G HNpt | entity (divine); party divine", " 2 three H7969 HNcbsa", " 3 transgressions H6588 HNcmpc | word of another collection; collections sin", " 4 edom H0123G HNpm", " 5 four H0702 HNcbsa", " 5 four H5921A HR", " 5 and H9002 HC | connective", " 6 not revoke H7725O HVhi1cs", " 6 not revoke H3808 HTn | negator; qualifier negator; negator", " 7 punishment H5921A HR | word of another collection; collections reward", "*8 pursued H7291 HVqcc | member of this collection", " 8 him H9033 HSp3ms", "*8 pursued H5921A HR | member of this collection", " 9 brother H0251G HNcmsc", " 10 sword H2719 HNcfsa", " 10 in/on/with H9003 HRd", " 10 he H9043 HSp3ms", " 11 cast off H7843 HVpq3ms | word of another collection; collections reject", " 11 his H9023 HSp3ms", " 12 pity H7356B HNcmpc | word of another collection; collections compassion", " 13 anger H0639G HNcmsc | word of another collection; collections anger", " 14 tore H2963 HVqw3ms", " 14 his H9023 HSp3ms", " 15 perpetually H5703 HNcmsa | qualifier candidate; qualifier qualifier subgroup: Forever, ever, always (a quality of time)", " 15 to/for H9005 HR", " 16 kept H8104G HVqp3ms | word of another collection; collections remove", " 16 his H9023 HSp3ms", " 17 wrath H5678 HNcfsc | word of another collection; collections anger", " 17 and H9002 HC | connective", " 17 his H9023 HSp3ms", " 18 forever H5331 HNcmsa | qualifier candidate; qualifier qualifier subgroup: Forever, ever, always (a quality of time)", " 18 her H9034 HSp3fs"]
- reference: 1Ti 6:11
  text: But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.
  words: [" 0 but G1161 CONJ | connective", " 1 you G4771 P-2NS", " 2 o G5599 INJ", " 3 man G0444 N-VSM | entity (human); party human", " 4 god G2316 N-GSM-T | entity (divine); party divine", " 5 flee G5343 V-PAM-2S | word of another collection; collections escape", " 6 these G3778 D-APN", "*7 pursue G1161 CONJ | member of this collection", "*7 pursue G1377 V-PAM-2S | member of this collection", " 8 righteousness G1343 N-ASF | word of another collection; collections righteous", " 9 godliness G2150 N-ASF | word of another collection; collections godly", " 10 faith G4102G N-ASF | word of another collection; collections believe", " 11 love G0026 N-ASF | word of another collection; collections love", " 12 steadfastness G5281 N-ASF | word of another collection; collections loyalty", " 13 gentleness G4239 N-ASF | word of another collection; collections compassion"]
- reference: 2Ti 2:22
  text: So flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart.
  words: [" 0 so G1161 CONJ | connective", " 1 flee G5343 V-PAM-2S | word of another collection; collections escape", " 2 youthful G3512 A-APF | qualifier candidate; qualifier morph: adjective", " 3 passions G1939 N-APF | word of another collection; collections desire", " 4 and G1161 CONJ | connective", "*5 pursue G1377 V-PAM-2S | member of this collection", " 6 righteousness G1343 N-ASF | word of another collection; collections righteous", " 7 faith G4102G N-ASF | word of another collection; collections believe", " 8 love G0026 N-ASF | word of another collection; collections love", " 9 peace G1515 N-ASF | word of another collection; collections quarrel", " 10 with G3326 PREP", " 11 call on G1941 V-PMP-GPM | word of another collection; collections call", " 12 lord G2962G N-ASM-T | entity (divine); party divine", " 13 from G1537 PREP", " 14 pure G2513 A-GSF | word of another collection; qualifier morph: adjective; collections cleanse", " 15 heart G2588 N-GSF | word of another collection; collections heart"]
- reference: Jude 7
  text: just as Sodom and Gomorrah and the surrounding cities, which likewise indulged in sexual immorality and pursued unnatural desire, serve as an example by undergoing a punishment of eternal fire.
  words: [" 0 as G5613 PRT | connective", " 1 sodom G4670 N-NPN-L", " 2 and G2532 CONJ | connective", " 3 gomorrah G1116 N-NSF-L", " 4 and G2532 CONJ | connective", " 5 surrounding G4012 PREP", " 5 surrounding G0846 P-APF", " 6 cities G4172 N-NPF", " 7 which G3778 P-APF", " 8 likewise G3664 A-ASM | qualifier candidate; qualifier morph: adjective", " 8 likewise G5158 N-ASM", " 9 sexual immorality G1608 V-AAP-NPF | word of another collection; collections righteous", " 10 and G2532 CONJ | connective", "*11 pursued G0565 V-2AAP-NPF | member of this collection", "*11 pursued G3694 PREP | member of this collection", " 12 unnatural G2087 A-GSF | qualifier candidate; qualifier morph: adjective", " 13 desire G4561 N-GSF | word of another collection; collections desire", " 14 serve G4295 V-PNI-3P | word of another collection; collections serve", " 15 example G1164 N-ASN", " 16 undergoing G5254 V-PAP-NPF", " 17 punishment G1349 N-ASF | word of another collection; collections reward", " 18 eternal G0166 A-GSN | word of another collection; qualifier morph: adjective; collections continual", " 19 fire G4442 N-GSN"]

## rows

- ledger_id: 2364
  item: pairing
  subject: chide
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Jer 29:18"]
  occurrences: [{"occurrence": 1332622, "reference": "Jer 29:18", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1332649, "reference": "Jer 29:18", "surface": "reproach", "strong": "H2781", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2365
  item: pairing
  subject: choose
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["2Sa 17:1", "2Sa 24:13"]
  occurrences: [{"occurrence": 1143028, "reference": "2Sa 17:1", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1143029, "reference": "2Sa 17:1", "surface": "pursue", "strong": "H0310A", "as": "member"}, {"occurrence": 1136445, "reference": "2Sa 24:13", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1143022, "reference": "2Sa 17:1", "surface": "choose", "strong": "H0977", "as": "partner"}, {"occurrence": 1136460, "reference": "2Sa 24:13", "surface": "decide", "strong": "H7200J", "as": "partner"}]
  older: [{"observation": 12480, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "People select men for battle, leadership or a task, and the word marks fitness: \"Moses chose able men out of all Israel and made them heads over the people\" (Exo 18:25); \"700 chosen men who were left-handed; every one could sling a stone at a hair and not miss\" (Judg 20:16); \"300,000 choice men, fit for war, able to handle spear and shield\" (2Ch 25:5). The same word names the men \"chosen from the assembly, well-known men\" who rose up against Moses (Num 16:2).", "verses": ["Josh.8.3", "Exod.14.7", "Exod.17.9", "Exod.18.25", "Num.16.2", "Num.26.9", "Judg.20.15", "Judg.20.16", "Judg.20.34", "1Sam.13.2", "2Sam.6.1", "2Sam.10.9", "2Sam.17.1", "1Kgs.12.21", "1Chr.19.10", "2Chr.11.1", "2Chr.13.3", "2Chr.13.17", "2Chr.25.5"]}, {"observation": 19448, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "19 | 2Sa 17:1 | Men selected (for battle, leadership or a task) | B | H0977 \"choose\" HVqc1cs @5 | Moreover, Ahithophel said to Absalom, “ Let me choose twelve thousand men, and I will arise and pursue David tonight.", "verses": ["2Sam.17.1"]}, {"observation": 21515, "stage": "engagement", "kind": "face", "nature": null, "text": "Choose is here a person's own act of choosing or deciding: a purposeful act of the will that picks one thing, way, person or course over another (choose life, choose whom you will serve, decided in his heart, Mary has chosen the good portion).", "verses": ["1Chr.21.10", "1Chr.21.11", "1Kgs.18.23", "1Kgs.18.25", "1Sam.17.8", "2Sam.17.1", "2Sam.24.12", "Acts.15.22", "Acts.15.25", "Deut.1.13", "Deut.23.16", "Deut.30.19", "Exod.17.9", "Isa.56.4", "Isa.7.15", "Isa.7.16", "Job.15.5", "Job.34.33", "Job.34.4", "Job.7.15", "Josh.24.15", "Matt.20.14", "Matt.20.15", "Num.14.4", "Phil.1.22", "Prov.1.29", "Prov.3.31", "Ps.25.12"]}, {"observation": 21529, "stage": "engagement", "kind": "face", "nature": null, "text": "Decide is here a person's own act of choosing or deciding: a purposeful act of the will that picks one thing, way, person or course over another (choose life, choose whom you will serve, decided in his heart, Mary has chosen the good portion).", "verses": ["1Chr.21.12", "2Sam.24.13", "Job.22.28", "Rom.14.13"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2366
  item: pairing
  subject: cleanse
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["2Ti 2:22"]
  occurrences: [{"occurrence": 1500395, "reference": "2Ti 2:22", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1500404, "reference": "2Ti 2:22", "surface": "pure", "strong": "G2513", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2367
  item: pairing
  subject: combat
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["2Sa 2:28"]
  occurrences: [{"occurrence": 1148875, "reference": "2Sa 2:28", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1148876, "reference": "2Sa 2:28", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1148881, "reference": "2Sa 2:28", "surface": "fight", "strong": "H3898A", "as": "partner"}, {"occurrence": 1148883, "reference": "2Sa 2:28", "surface": "fight", "strong": "H5750", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2368
  item: pairing
  subject: command
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Deu 28:45"]
  occurrences: [{"occurrence": 1086236, "reference": "Deu 28:45", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1086259, "reference": "Deu 28:45", "surface": "commanded", "strong": "H6680", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2369
  item: pairing
  subject: compassion
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 109:16", "Lam 3:43", "Amo 1:11", "1Ti 6:11"]
  occurrences: [{"occurrence": 1254311, "reference": "Psa 109:16", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1346065, "reference": "Lam 3:43", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1389447, "reference": "Amo 1:11", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1389449, "reference": "Amo 1:11", "surface": "pursued", "strong": "H5921A", "as": "member"}, {"occurrence": 1499466, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1161", "as": "member"}, {"occurrence": 1499467, "reference": "1Ti 6:11", "surface": "pursue", "strong": "G1377", "as": "member"}, {"occurrence": 1254310, "reference": "Psa 109:16", "surface": "kindness", "strong": "H2617A", "as": "partner"}, {"occurrence": 1346069, "reference": "Lam 3:43", "surface": "pity", "strong": "H2550", "as": "partner"}, {"occurrence": 1389456, "reference": "Amo 1:11", "surface": "pity", "strong": "H7356B", "as": "partner"}, {"occurrence": 1499473, "reference": "1Ti 6:11", "surface": "gentleness", "strong": "G4239", "as": "partner"}]
  older: [{"observation": 17635, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "No delight in blessing: \"He loved to curse … He did not delight in blessing\" (Psa 109:17), from one who \"did not remember to show kindness\" (109:16). The cursing soaks in \"like oil into his bones\" (109:18). I read the figure as what a man delights in becoming his own substance. This also goes to 10.5.", "verses": ["Ps.109.17", "Ps.109.16", "Ps.109.18"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2370
  item: pairing
  subject: compel
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Job 13:25", "Jer 29:18"]
  occurrences: [{"occurrence": 1236036, "reference": "Job 13:25", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1332622, "reference": "Jer 29:18", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1236033, "reference": "Job 13:25", "surface": "driven", "strong": "H5086", "as": "partner"}, {"occurrence": 1332658, "reference": "Jer 29:18", "surface": "driven", "strong": "H5080", "as": "partner"}, {"occurrence": 1332659, "reference": "Jer 29:18", "surface": "driven", "strong": "H0834A", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2371
  item: pairing
  subject: condemn
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Jer 39:5"]
  occurrences: [{"occurrence": 1343502, "reference": "Jer 39:5", "surface": "pursued", "strong": "H7291", "as": "member"}, {"occurrence": 1343503, "reference": "Jer 39:5", "surface": "pursued", "strong": "H0310A", "as": "member"}, {"occurrence": 1343526, "reference": "Jer 39:5", "surface": "sentence", "strong": "H4941G", "as": "partner"}, {"occurrence": 1343527, "reference": "Jer 39:5", "surface": "sentence", "strong": "H0854", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2372
  item: pairing
  subject: continual
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Jude 7"]
  occurrences: [{"occurrence": 1512349, "reference": "Jude 7", "surface": "pursued", "strong": "G0565", "as": "member"}, {"occurrence": 1512350, "reference": "Jude 7", "surface": "pursued", "strong": "G3694", "as": "member"}, {"occurrence": 1512357, "reference": "Jude 7", "surface": "eternal", "strong": "G0166", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2373
  item: pairing
  subject: convince
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Deu 28:45"]
  occurrences: [{"occurrence": 1086236, "reference": "Deu 28:45", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1086245, "reference": "Deu 28:45", "surface": "obey", "strong": "H8085H", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2374
  item: pairing
  subject: cruel
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Deu 28:22"]
  occurrences: [{"occurrence": 1072275, "reference": "Deu 28:22", "surface": "pursue", "strong": "H7291", "as": "member"}, {"occurrence": 1072254, "reference": "Deu 28:22", "surface": "strike", "strong": "H5221", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 58012
- seconds: 0.03

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "going after",
 "rows": [
  {
   "ledger_id": 2364,
   "item": "pairing",
   "subject": "chide",
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
   "ledger_id": 2365,
   "item": "pairing",
   "subject": "choose",
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
     "observation": 12480,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 19448,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 21515,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    },
    {
     "observation": 21529,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2366,
   "item": "pairing",
   "subject": "cleanse",
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
   "ledger_id": 2367,
   "item": "pairing",
   "subject": "combat",
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
   "ledger_id": 2368,
   "item": "pairing",
   "subject": "command",
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
   "ledger_id": 2369,
   "item": "pairing",
   "subject": "compassion",
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
     "observation": 17635,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2370,
   "item": "pairing",
   "subject": "compel",
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
   "ledger_id": 2371,
   "item": "pairing",
   "subject": "condemn",
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
   "ledger_id": 2372,
   "item": "pairing",
   "subject": "continual",
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
   "ledger_id": 2373,
   "item": "pairing",
   "subject": "convince",
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
   "ledger_id": 2374,
   "item": "pairing",
   "subject": "cruel",
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
