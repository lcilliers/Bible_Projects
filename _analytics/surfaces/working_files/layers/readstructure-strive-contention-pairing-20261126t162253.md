# ReadStructure -- strive / contention -- step 2.1

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

2026-11-26T16:22:53Z

## batch

- rows: 15
- rows_left_after_this: 17

## senses

- sense: 24277
  text: Discord among people: strife as a state between persons or in a place, in Gen 13:7, Gen 13:8, Deu 1:12, Psa 55:9, Pro 17:1, Pro 23:29, Hab 1:3, and in the vice lists of Rom 1:29, Gal 5:20 and 1Cor 3:3.
  verses: ["Rom.1.29", "1Cor.3.3", "Gal.5.20", "Gen.13.7", "Deut.1.12", "Ps.55.9", "Prov.17.1", "Hab.1.3", "Gen.13.8", "Prov.23.29"]
- sense: 24278
  text: Strife stirred up by a person: strife roused, spread or kindled by one named by his trait or act, the hot-tempered, the greedy, the quarrelsome, hatred, insolence, pressed anger, in Pro 10:12, Pro 13:10, Pro 15:18, Pro 16:28, Pro 17:14, Pro 22:10, Pro 26:21, Pro 29:22, Pro 30:33.
  verses: ["Prov.15.18", "Prov.29.22", "Prov.28.25", "Prov.16.28", "Prov.17.14", "Prov.22.10", "Prov.10.12", "Prov.17.19", "Prov.13.10", "Prov.30.33", "Prov.26.21", "Prov.20.3"]
- sense: 24279
  text: Strife raised against someone: hostile strife stirred up against the speaker, Zion, the king or the faithful, from which God shelters or delivers them, in Psa 56:6, Psa 59:3, Isa 54:15, 2Sa 22:44, Psa 18:43, Psa 31:20, and Jer 15:10, where the prophet is the man all contend with.
  verses: ["Ps.56.6", "Ps.59.3", "Isa.54.15", "2Sam.22.44", "Ps.18.43", "Ps.31.20", "Jer.15.10"]
- sense: 24280
  text: Strife in the body: in Job 33:19 the man rebuked by pain on his bed has a continual strife in his bones.
  verses: ["Job.33.19"]

## verses

- reference: 2Sa 22:44
  text: “You delivered me from strife with my people; you kept me as the head of the nations; people whom I had not known served me.
  words: [" 0 delivered H6403 HVpw2ms | word of another collection; collections save", "*1 strife H7379 HNcmpc | member of this collection", " 1 from H9006 HR", " 1 me H9030 HSp1bs", " 2 people H5971A HNcmsc", " 3 kept H8104H HVqi2ms | word of another collection; collections remove", " 3 my H9020 HSp1bs", " 4 head H7218H HNcmsc", " 4 to/for H9005 HR", " 4 me H9030 HSp1bs", " 5 nations H1471A HNcmpa", " 6 people H5971A HNcmsa", " 7 not H3808 HTn | negator; qualifier negator; negator", " 8 known H3045 HVqp1cs | word of another collection; collections know", " 9 served H5647H HVqi3mp | word of another collection; collections serve", " 10 me H9030 HSp1bs"]
- reference: Job 33:19
  text: “Man is also rebuked with pain on his bed and with continual strife in his bones,
  words: [" 0 rebuked H3198 HVHq3ms | word of another collection; collections chide", " 1 pain H4341 HNcmsa | word of another collection; collections pain", " 1 in/on/with H9003 HR", " 2 on H5921A HR", " 3 bed H4904 HNcmsc", " 4 continual H0386 HAamsa | word of another collection; qualifier morph: adjective; collections continual", "*5 strife H7230 HNcmsc | member of this collection; qualifier qualifier subgroup: Abundance, many, great (a quantity)", " 5 and H9002 HC", " 5 his H9023 HSp3ms", " 6 his H9023 HSp3ms", " 7 bones H6106G HNcmpc"]
- reference: Psa 18:43
  text: You delivered me from strife with the people; you made me the head of the nations; people whom I had not known served me.
  words: [" 0 delivered H6403 HVpi2ms | word of another collection; collections save", " 1 from H9006 HR", " 1 me H9030 HSp1bs", "*2 strife H7379 HNcmpc | member of this collection", " 3 people H5971A HNcmsa", " 4 made H7760A HVqi2ms", " 5 head H7218H HNcmsc", " 5 to/for H9005 HR", " 5 me H9030 HSp1bs", " 6 nations H1471A HNcmpa", " 7 people H5971A HNcmsa", " 8 not H3808 HTn | negator; qualifier negator; negator", " 9 known H3045 HVqp1cs | word of another collection; collections know", " 10 served H5647H HVqi3mp | word of another collection; collections serve", " 11 me H9030 HSp1bs"]
- reference: Psa 31:20
  text: In the cover of your presence you hide them from the plots of men; you store them in your shelter from the strife of tongues.
  words: [" 0 in H9003 HR", " 1 cover H5643A HNcmsc", " 1 them H9038 HSp3mp", " 2 presence H6440H HNcmpc | word of another collection; collections offer", " 3 hide H5641 HVhi2ms | word of another collection; collections conceal", " 4 from H9006 HR", " 5 plots H7407 HNcmpc | word of another collection; collections plot", " 5 your H9021 HSp2ms", " 6 men H0376G HNcmsa | entity (human); party human", " 7 store H6845 HVqi2ms", " 8 shelter H5521 HNcfsa", " 8 in/on/with H9003 HR", " 8 them H9038 HSp3mp", " 9 from H9006 HR", "*10 strife H7379 HNcmsc | member of this collection", " 11 tongues H3956G HNcfpa"]
- reference: Pro 10:12
  text: Hatred stirs up strife, but love covers all offenses.
  words: [" 0 hatred H8135 HNcfsa | word of another collection; collections love", " 1 stirs up H5782 HVpi3fs", "*2 strife H4090 HNcmpa | member of this collection", " 3 love H0160 HNcfsa | word of another collection; collections love", " 4 covers H3680 HVpi3fs | word of another collection; collections conceal", " 5 all H5921A HR", " 5 and H9002 HC | connective", " 5 all H3605 HNcmsc", " 6 offenses H6588 HNcmpa | word of another collection; collections crime"]
- reference: Pro 13:10
  text: By insolence comes nothing but strife, but with those who take advice is wisdom.
  words: [" 0 by H9003 HR", " 1 insolence H2087 HNcmsa | word of another collection; collections pride", " 2 comes H5414G HVqi3ms", " 3 nothing but H7535 HD | qualifier candidate; qualifier morph: adverb", "*4 strife H4683 HNcfsa | member of this collection", " 5 with H0854 HR", " 6 take advice H3289 HVNrmpa | word of another collection; collections snatch", " 6 and H9002 HC | connective", " 7 wisdom H2451 HNcfsa | word of another collection; collections wise"]
- reference: Pro 17:1
  text: Better is a dry morsel with quiet than a house full of feasting with strife.
  words: [" 0 better H2896A HAamsa | qualifier candidate; qualifier qualifier subgroup: Good, better, well (a quality of something); morph: adjective", " 1 dry H2720A HAafsa | word of another collection; qualifier morph: adjective; collections dry", " 2 morsel H6595A HNcfsa", " 3 quiet H7962 HNcfsa | word of another collection; collections mute", " 3 and H9002 HC | connective", " 4 than H9006 HR", " 5 house H1004B HNcmsa", " 5 in/on/with H9003 HR", " 5 her H9034 HSp3fs", " 6 full H4392 HAamsa | qualifier candidate; qualifier morph: adjective", " 7 feasting H2077 HNcmpc", "*8 strife H7379 HNcmsa | member of this collection"]
- reference: Pro 17:19
  text: Whoever loves transgression loves strife; he who makes his door high seeks destruction.
  words: [" 0 loves H0157G HVqrmsa | word of another collection; collections love", " 1 transgression H6588 HNcmsa | word of another collection; collections crime", " 2 loves H0157G HVqrmsa | word of another collection; collections love", "*3 strife H4683 HNcfsa | member of this collection", " 4 door H6607 HNcmsc", " 5 high H1361 HVhrmsa", " 6 seeks H1245 HVprmsa | word of another collection; collections search", " 6 his H9023 HSp3ms", " 7 destruction H7667 HNcmsa | word of another collection; collections destruction"]
- reference: Pro 20:3
  text: It is an honor for a man to keep aloof from strife, but every fool will be quarreling.
  words: [" 0 honor H3519 HNcmsa | word of another collection; collections honor", " 1 man H0376G HNcmsa | entity (human); party human", " 1 to/for H9005 HRd", " 2 keep aloof H7674 HNcfsa", " 3 from H9006 HR", "*4 strife H7379 HNcmsa | member of this collection", " 5 every H3605 HNcmsa", " 5 and H9002 HC | connective", " 6 fool H0191 HAamsa | word of another collection; qualifier morph: adjective; collections folly", " 7 quarreling H1566 HVti3ms | word of another collection; collections quarrel"]
- reference: Pro 22:10
  text: Drive out a scoffer, and strife will go out, and quarreling and abuse will cease.
  words: [" 0 out H1644G HVpv2ms", " 1 scoffer H3887 HAamsa | word of another collection; qualifier morph: adjective; collections scoff", "*2 strife H4066 HNcmsa | member of this collection", " 3 go out H3318G HVqu3ms", " 4 quarreling H1779 HNcmsa | word of another collection; collections quarrel", " 5 abuse H7036 HNcmsa | word of another collection; collections oppress", " 5 and H9002 HC | connective", " 6 cease H7673A HVqu3ms | word of another collection; collections mute"]
- reference: Pro 23:29
  text: Who has woe? Who has sorrow? Who has strife? Who has complaining? Who has wounds without cause? Who has redness of eyes?
  words: [" 0 who H4310 HPi", " 0 to/for H9005 HR", " 1 woe H0188 HTj | word of another collection; collections tribulation", " 2 who H4310 HPi", " 2 to/for H9005 HR", " 3 sorrow H0017 HTj | word of another collection; collections tribulation", " 4 who H4310 HPi", " 4 to/for H9005 HR", "*5 strife H4079 HNcmpa | member of this collection", " 6 who H4310 HPi", " 6 to/for H9005 HR", " 7 complaining H7879 HNcmsa | word of another collection; collections mutter", " 8 who H4310 HPi", " 8 to/for H9005 HR", " 9 wounds H6482 HNcmpa | word of another collection; collections pain", " 10 without cause H2600 HD | qualifier candidate; qualifier morph: adverb", " 11 who H4310 HPi", " 11 to/for H9005 HR", " 12 redness H2448 HNcfsa", " 13 eyes H5869A HNcfda"]
- reference: Pro 28:25
  text: A greedy man stirs up strife, but the one who trusts in the Lord will be enriched.
  words: [" 0 greedy H7342I HAamsc | word of another collection; qualifier morph: adjective; collections greed", " 1 man H5315J HNcfsa", " 2 stirs up H1624 HVpi3ms", "*3 strife H4066 HNcmsa | member of this collection", " 4 trusts H0982 HVqrmsa | word of another collection; collections trust", " 5 lord H3068G HNpt | entity (divine); party divine", " 5 lord H5921A HR", " 6 enriched H1878 HVPi3ms | word of another collection; collections rich"]
- reference: Rom 1:29
  text: They were filled with all manner of unrighteousness, evil, covetousness, malice. They are full of envy, murder, strife, deceit, maliciousness. They are gossips,
  words: [" 0 filled G4137 V-RPP-APM | word of another collection; collections fill", " 1 all G3956 A-DSF | qualifier candidate; qualifier morph: adjective", " 2 unrighteousness G0093 N-DSF | word of another collection; collections evildoer", " 2 unrighteousness G4202 N-DSF | word of another collection; collections evildoer", " 3 evil G4189 N-DSF | word of another collection; collections evildoer", " 4 covetousness G4124 N-DSF | word of another collection; collections greed", " 5 malice G2549 N-DSF | word of another collection; collections evildoer", " 6 full G3324 A-APM | qualifier candidate; qualifier morph: adjective", " 7 envy G5355 N-GSM | word of another collection; collections jealous", " 8 murder G5408 N-GSM | word of another collection; collections kill", "*9 strife G2054 N-GSF | member of this collection", " 10 deceit G1388 N-GSM | word of another collection; collections deceive", " 11 maliciousness G2550 N-GSF | word of another collection; collections evildoer", " 12 gossips G5588 N-APM"]
- reference: 1Cor 3:3
  text: for you are still of the flesh. For while there is jealousy and strife among you, are you not of the flesh and behaving only in a human way?
  words: [" 0 for G1063 CONJ | connective", " 1 are G1510 V-PAI-2P", " 2 still G2089 ADV | word of another collection; qualifier morph: adverb; collections mute", " 3 flesh G4559 A-NPM | qualifier candidate; qualifier morph: adjective", " 4 for G1063 CONJ | connective", " 5 while G3699 CONJ | connective", " 6 jealousy G2205 N-NSM | word of another collection; collections jealous", " 7 and G2532 CONJ | connective", "*8 strife G2054 N-NSF | member of this collection", " 9 among G1722 PREP", " 10 you G5213 P-2DP", " 11 you G1510 V-PAI-2P", " 12 not G3780 PRT-N | negator; qualifier negator; negator", " 13 flesh G4559 A-NPM | qualifier candidate; qualifier morph: adjective", " 14 and G2532 CONJ | connective", " 15 behaving G4043 V-PAI-2P", " 16 in G2596 PREP", " 17 human way G0444 N-ASM | entity (human); party human"]
- reference: Gal 5:20
  text: idolatry, sorcery, enmity, strife, jealousy, fits of anger, rivalries, dissensions, divisions,
  words: [" 0 idolatry G1495 N-NSF", " 1 sorcery G5331 N-NSF", " 2 enmity G2189 N-NPF | word of another collection; collections love", "*3 strife G2054 N-NSF | member of this collection", " 4 jealousy G2205 N-NSM | word of another collection; collections jealous", " 5 anger G2372 N-NPM | word of another collection; collections anger", " 6 rivalries G2052 N-NPF", " 7 dissensions G1370 N-NPF | word of another collection; collections quarrel", " 8 divisions G0139 N-NPF"]

## rows

- ledger_id: 2605
  item: pairing
  subject: fill
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Rom 1:29"]
  occurrences: [{"occurrence": 1474520, "reference": "Rom 1:29", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1474510, "reference": "Rom 1:29", "surface": "filled", "strong": "G4137", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2606
  item: pairing
  subject: folly
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 20:3"]
  occurrences: [{"occurrence": 1279293, "reference": "Pro 20:3", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1279296, "reference": "Pro 20:3", "surface": "fool", "strong": "H0191", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2607
  item: pairing
  subject: greed
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 28:25", "Rom 1:29"]
  occurrences: [{"occurrence": 1276486, "reference": "Pro 28:25", "surface": "strife", "strong": "H4066", "as": "member"}, {"occurrence": 1474520, "reference": "Rom 1:29", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1276483, "reference": "Pro 28:25", "surface": "greedy", "strong": "H7342I", "as": "partner"}, {"occurrence": 1474515, "reference": "Rom 1:29", "surface": "covetousness", "strong": "G4124", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2608
  item: pairing
  subject: honor
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 20:3"]
  occurrences: [{"occurrence": 1279293, "reference": "Pro 20:3", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1279288, "reference": "Pro 20:3", "surface": "honor", "strong": "H3519", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2609
  item: pairing
  subject: jealous
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Rom 1:29", "1Cor 3:3", "Gal 5:20"]
  occurrences: [{"occurrence": 1474520, "reference": "Rom 1:29", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1483152, "reference": "1Cor 3:3", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1489959, "reference": "Gal 5:20", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1474518, "reference": "Rom 1:29", "surface": "envy", "strong": "G5355", "as": "partner"}, {"occurrence": 1483150, "reference": "1Cor 3:3", "surface": "jealousy", "strong": "G2205", "as": "partner"}, {"occurrence": 1489960, "reference": "Gal 5:20", "surface": "jealousy", "strong": "G2205", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2610
  item: pairing
  subject: kill
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Rom 1:29"]
  occurrences: [{"occurrence": 1474520, "reference": "Rom 1:29", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1474519, "reference": "Rom 1:29", "surface": "murder", "strong": "G5408", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2611
  item: pairing
  subject: know
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["2Sa 22:44", "Psa 18:43"]
  occurrences: [{"occurrence": 1146714, "reference": "2Sa 22:44", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1256723, "reference": "Psa 18:43", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1146726, "reference": "2Sa 22:44", "surface": "known", "strong": "H3045", "as": "partner"}, {"occurrence": 1256732, "reference": "Psa 18:43", "surface": "known", "strong": "H3045", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2612
  item: pairing
  subject: love
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 10:12", "Pro 17:19", "Gal 5:20"]
  occurrences: [{"occurrence": 1282867, "reference": "Pro 10:12", "surface": "strife", "strong": "H4090", "as": "member"}, {"occurrence": 1277687, "reference": "Pro 17:19", "surface": "strife", "strong": "H4683", "as": "member"}, {"occurrence": 1489959, "reference": "Gal 5:20", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1282865, "reference": "Pro 10:12", "surface": "hatred", "strong": "H8135", "as": "partner"}, {"occurrence": 1282868, "reference": "Pro 10:12", "surface": "love", "strong": "H0160", "as": "partner"}, {"occurrence": 1277684, "reference": "Pro 17:19", "surface": "loves", "strong": "H0157G", "as": "partner"}, {"occurrence": 1277686, "reference": "Pro 17:19", "surface": "loves", "strong": "H0157G", "as": "partner"}, {"occurrence": 1489958, "reference": "Gal 5:20", "surface": "enmity", "strong": "G2189", "as": "partner"}]
  older: [{"observation": 18725, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "M51 Love & Devotion | 34 | 14 | rouse + love 7 (Song 2:7, 3:5, 8:4; Pro 10:12)", "verses": ["Song.2.7", "Song.3.5", "Song.8.4", "Prov.10.12"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2613
  item: pairing
  subject: mute
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 17:1", "Pro 22:10", "1Cor 3:3"]
  occurrences: [{"occurrence": 1279276, "reference": "Pro 17:1", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1279117, "reference": "Pro 22:10", "surface": "strife", "strong": "H4066", "as": "member"}, {"occurrence": 1483152, "reference": "1Cor 3:3", "surface": "strife", "strong": "G2054", "as": "member"}, {"occurrence": 1279268, "reference": "Pro 17:1", "surface": "quiet", "strong": "H7962", "as": "partner"}, {"occurrence": 1279122, "reference": "Pro 22:10", "surface": "cease", "strong": "H7673A", "as": "partner"}, {"occurrence": 1483146, "reference": "1Cor 3:3", "surface": "still", "strong": "G2089", "as": "partner"}]
  older: [{"observation": 21282, "stage": "engagement", "kind": "qualification", "nature": null, "text": "Quiet gives a peaceable nature: a calm and gentle disposition of a spirit, a life, a house, or a people, named by another word.", "verses": ["1Pet.3.4", "1Tim.2.2", "Prov.17.1", "Ps.35.20"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2614
  item: pairing
  subject: mutter
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 23:29"]
  occurrences: [{"occurrence": 1279162, "reference": "Pro 23:29", "surface": "strife", "strong": "H4079", "as": "member"}, {"occurrence": 1279165, "reference": "Pro 23:29", "surface": "complaining", "strong": "H7879", "as": "partner"}]
  older: [{"observation": 21561, "stage": "engagement", "kind": "statement", "nature": null, "text": "Complaining names the inner operation of voicing grievance, set among woe, sorrow and strife.", "verses": ["Prov.23.29"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2615
  item: pairing
  subject: offer
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 31:20"]
  occurrences: [{"occurrence": 1261407, "reference": "Psa 31:20", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1261396, "reference": "Psa 31:20", "surface": "presence", "strong": "H6440H", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2616
  item: pairing
  subject: oppress
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 22:10"]
  occurrences: [{"occurrence": 1279117, "reference": "Pro 22:10", "surface": "strife", "strong": "H4066", "as": "member"}, {"occurrence": 1279120, "reference": "Pro 22:10", "surface": "abuse", "strong": "H7036", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2617
  item: pairing
  subject: pain
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Job 33:19", "Pro 23:29"]
  occurrences: [{"occurrence": 1242771, "reference": "Job 33:19", "surface": "strife", "strong": "H7230", "as": "member"}, {"occurrence": 1279162, "reference": "Pro 23:29", "surface": "strife", "strong": "H4079", "as": "member"}, {"occurrence": 1242766, "reference": "Job 33:19", "surface": "pain", "strong": "H4341", "as": "partner"}, {"occurrence": 1279168, "reference": "Pro 23:29", "surface": "wounds", "strong": "H6482", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2618
  item: pairing
  subject: plot
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 31:20"]
  occurrences: [{"occurrence": 1261407, "reference": "Psa 31:20", "surface": "strife", "strong": "H7379", "as": "member"}, {"occurrence": 1261399, "reference": "Psa 31:20", "surface": "plots", "strong": "H7407", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2619
  item: pairing
  subject: pride
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Pro 13:10"]
  occurrences: [{"occurrence": 1279211, "reference": "Pro 13:10", "surface": "strife", "strong": "H4683", "as": "member"}, {"occurrence": 1279208, "reference": "Pro 13:10", "surface": "insolence", "strong": "H2087", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 53152
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "contention",
 "rows": [
  {
   "ledger_id": 2605,
   "item": "pairing",
   "subject": "fill",
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
   "ledger_id": 2606,
   "item": "pairing",
   "subject": "folly",
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
   "ledger_id": 2607,
   "item": "pairing",
   "subject": "greed",
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
   "ledger_id": 2608,
   "item": "pairing",
   "subject": "honor",
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
   "ledger_id": 2609,
   "item": "pairing",
   "subject": "jealous",
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
   "ledger_id": 2610,
   "item": "pairing",
   "subject": "kill",
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
   "ledger_id": 2611,
   "item": "pairing",
   "subject": "know",
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
   "ledger_id": 2612,
   "item": "pairing",
   "subject": "love",
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
     "observation": 18725,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2613,
   "item": "pairing",
   "subject": "mute",
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
     "observation": 21282,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2614,
   "item": "pairing",
   "subject": "mutter",
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
     "observation": 21561,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2615,
   "item": "pairing",
   "subject": "offer",
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
   "ledger_id": 2616,
   "item": "pairing",
   "subject": "oppress",
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
   "ledger_id": 2617,
   "item": "pairing",
   "subject": "pain",
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
   "ledger_id": 2618,
   "item": "pairing",
   "subject": "plot",
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
   "ledger_id": 2619,
   "item": "pairing",
   "subject": "pride",
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
