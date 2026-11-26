# ReadStructure -- strive / exertion toward an end -- step 2.1

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

2026-11-26T15:47:07Z

## batch

- rows: 11
- rows_left_after_this: 14

## senses

- sense: 23951
  text: Exertion toward a goal: effort spent to reach or to do something, in 1Th 2:17, Gal 2:17, Luk 13:24, 1Ti 4:10, Heb 12:14, 1Cor 14:12, Heb 4:11 and Ecc 2:22; the goal is named in each, a meeting, a standing before God, entry, peace and holiness, excelling, rest, or in Ecc 2:22 the labour itself.
  verses: ["1Thess.2.17", "Gal.2.17", "Luke.13.24", "1Tim.4.10", "Heb.12.14", "1Cor.14.12", "Heb.4.11", "Eccl.2.22"]
- sense: 23952
  text: Contention against an opponent: disputing with another or rousing oneself against another, in Isa 45:9 against one's maker, in Pro 28:4 by those who keep the law against the wicked, and in Isa 41:11 where Israel's opponents are named by their dispute with Israel.
  verses: ["Isa.45.9", "Prov.28.4", "Isa.41.11"]
- sense: 23953
  text: Physical fighting: a bodily fight between men in Exo 21:22 and warfare between peoples in Psa 60:1, both with the verb natsah.
  verses: ["Exod.21.22", "Ps.60.1"]
- sense: 23954
  text: Jacob's contending with God: the struggle with God, or with the angel, in which Jacob prevailed, told in Gen 32:28, Hos 12:3 and Hos 12:4 with sarah and sur.
  verses: ["Gen.32.28", "Hos.12.4", "Hos.12.3"]
- sense: 23955
  text: A reaching after wind: in Ecc 1:14, Ecc 1:17, Ecc 2:11, Ecc 2:17, Ecc 2:26, Ecc 4:4, Ecc 4:6, Ecc 4:16 and Ecc 6:9 two related nouns, reut and rayon, name a striving after wind, a reaching after what gives nothing to hold.
  verses: ["Eccl.2.17", "Eccl.2.11", "Eccl.4.4", "Eccl.4.6", "Eccl.6.9", "Eccl.2.26", "Eccl.1.14", "Eccl.4.16", "Eccl.1.17"]

## verses

- reference: Gen 32:28
  text: Then he said, “Your name shall no longer be called Jacob, but Israel, for you have striven with God and with men, and have prevailed.”
  words: [" 0 said H0559 HVqw3ms", " 1 name H8034 HNcmsc", " 2 no H3808 HTn | negator; qualifier negator; negator", " 3 longer H5750 HAcmsa | qualifier candidate; qualifier morph: adjective", " 4 called H0559 HVNi3ms | word of another collection; collections call", " 5 jacob H3290 HNpm | entity (human); party human", " 6 israel H3478 HNpm", " 6 your H9021 HSp2ms", " 6 israel H3588B HTc | connective", " 6 israel H0518B HTc | connective", "*7 striven H8280 HVqp2ms | member of this collection", " 7 for H3588A HTc", " 8 god H0430G HNcmpa | entity (divine); party divine", " 8 with H5973A HR", " 9 men H0582 HNcmpa | entity (human); party human", " 9 with H5973A HR", " 9 and H9002 HC | connective", " 10 prevailed H3201 HVqw2ms | word of another collection; collections prevail"]
- reference: Exo 21:22
  text: “When men strive together and hit a pregnant woman, so that her children come out, but there is no harm, the one who hit her shall surely be fined, as the woman’s husband shall impose on him, and he shall pay as the judges determine.
  words: [" 0 men H0582 HNcmpa | entity (human); party human", "*1 strive H5327A HVNi3mp | member of this collection", "*1 strive H3588A HTc | member of this collection", " 1 and H9002 HC", " 2 hit H5062 HVqq3cp", " 3 pregnant H2030A HAafsa | qualifier candidate; qualifier morph: adjective", " 4 woman H0802G HNcfsa | entity (human); party human", " 5 children H3206 HNcmpc", " 6 come out H3318M HVqq3cp", " 7 no H3808 HTn | negator; qualifier negator; negator", " 7 and H9002 HC | connective", " 7 her H9024 HSp3fs", " 8 harm H0611 HNcmsa | word of another collection; collections benefit", " 8 harm H1961 HVqi3ms | word of another collection; collections benefit", " 9 surely H6064 HVqaa | word of another collection; collections loyalty", " 10 fined H6064 HVNi3ms", " 11 woman’s H0802G HNcfsa | entity (human); party human", " 11 [the] H9009 HTd", " 12 husband H1167H HNcmsc", " 12 husband H5921A HRd", " 12 him H9033 HSp3ms", " 13 impose H7896G HVqi3ms", " 13 impose H0834A HTr | connective", " 13 like/as H9004 HR", " 14 pay H5414N HVqq3ms | word of another collection; collections reward", " 15 judges H6414 HNcmpa | word of another collection; collections condemn", " 15 in/on/with H9003 HR"]
- reference: Psa 60:1
  text: To the choirmaster: according to Shushan Eduth. A Miktam of David; for instruction; when he strove with Aram-naharaim and with Aram-zobah, and when Joab on his return struck down twelve thousand of Edom in the Valley of Salt. O God, you have rejected us, broken our defenses; you have been angry; oh, restore us.
  words: [" 0 choirmaster H5329 HVprmsa", " 0 to/for H9005 HRd", " 1 according H5921A HR", " 2 shushan eduth H7799 HNtmsc", " 3 miktam H4387 HNtmsa", " 3 miktam H5715 HNcfsa", " 4 david H1732 HNpm | entity (human); party human", " 4 to/for H9005 HR", " 5 for H9005 HR", " 6 instruction H3925G HVpcc | word of another collection; collections teach", "*7 strove H5327A HVhcc | member of this collection", " 7 in/on/with H9003 HR", " 8 aram-naharaim H0763G HNpl", " 8 he H9043 HSp3ms", " 8 aram-naharaim H0853 HTo", " 9 aram-zobah H0760 HNpl", " 9 aram-zobah H0853 HTo", " 9 and H9002 HC | connective", " 10 joab H3097G HNpm | entity (human); party human", " 11 return H7725G HVqw3ms | word of another collection; collections return", " 12 struck down H5221 HVhw3ms", " 13 twelve H8147 HNcbda", " 13 twelve H6240 HNcbsa", " 14 thousand H0505G HNcbsa", " 15 edom H0123G HNpm", " 15 edom H0853 HTo", " 16 valley H1516G HNpl", " 16 in/on/with H9003 HR", " 17 salt H4417G HNpl", " 18 god H0430G HNcmpa | entity (divine); party divine", " 19 rejected H2186A HVqp2ms | word of another collection; collections reject", " 20 broken our defenses H6555 HVqp2ms", " 20 us H9035 HSp1bp", " 21 angry H0599 HVqp2ms | word of another collection; collections anger", " 21 us H9035 HSp1bp", " 22 restore H7725H HVpi2ms | word of another collection; collections refresh", " 23 to/for H9005 HR", " 23 us H9035 HSp1bp"]
- reference: Ecc 1:14
  text: I have seen everything that is done under the sun, and behold, all is vanity and a striving after wind.
  words: [" 0 seen H7200G HVqp1cs", " 1 everything H3605 HNcmsc", " 1 everything H0853 HTo", " 2 done H6213A HVNp3cp", " 2 which/that H9007 HTr", " 2 done H4639G HNcmpa", " 2 [the] H9009 HTd", " 3 under H8478G HNcmsc", " 4 sun H8121 HNcbsa", " 4 [the] H9009 HTd", " 5 behold H2009 HTj", " 5 and H9002 HC | connective", " 6 all H3605 HNcmsa", " 6 [the] H9009 HTd", " 7 vanity H1892 HNcmsa | word of another collection; collections pride", "*8 striving H7469 HNcfsc | member of this collection", " 8 and H9002 HC", " 9 wind H7307H HNcfsa"]
- reference: Ecc 2:11
  text: Then I considered all that my hands had done and the toil I had expended in doing it, and behold, all was vanity and a striving after wind, and there was nothing to be gained under the sun.
  words: [" 0 considered H6437G HVqq1cs | word of another collection; collections thought", " 1 all H3605 HNcmsc", " 1 in/on/with H9003 HR", " 1 all H0589 HPp1bs", " 2 hands H3027G HNcbdc", " 2 my H9020 HSp1bs", " 2 which/that H9007 HTr", " 3 done H4639G HNcmpc", " 3 done H6213A HVqp3cp", " 4 toil H5999 HNcbsa | word of another collection; collections labor", " 4 in/on/with H9003 HRd", " 4 and H9002 HC | connective", " 4 my H9020 HSp1bs", " 5 expended H5998 HVqp1cs", " 5 which/that H9007 HTr", " 6 it H6213A HVqcc", " 6 to/for H9005 HR", " 7 behold H2009 HTj", " 7 and H9002 HC | connective", " 8 all H3605 HNcmsa", " 8 [the] H9009 HTd", " 9 vanity H1892 HNcmsa | word of another collection; collections pride", "*10 striving H7469 HNcfsc | member of this collection", " 10 and H9002 HC", " 11 wind H7307H HNcfsa", " 12 nothing H0369 HNcmsc", " 12 and H9002 HC | connective", " 13 gained H3504 HNcmsa | word of another collection; collections benefit", " 14 under H8478G HNcmsc", " 15 sun H8121 HNcbsa", " 15 [the] H9009 HTd"]
- reference: Ecc 2:17
  text: So I hated life, because what is done under the sun was grievous to me, for all is vanity and a striving after wind.
  words: [" 0 hated H8130 HVqq1cs | word of another collection; collections love", " 1 life H2416E HNcmpa", " 1 [the] H9009 HTd", " 1 life H0853 HTo", " 2 what H4639G HNcmsa", " 2 [the] H9009 HTd", " 2 what H5921A HRd", " 2 me H9030 HSp1bs", " 3 done H6213A HVNp3ms", " 3 which/that H9007 HTr", " 4 under H8478G HNcmsc", " 5 sun H8121 HNcbsa", " 5 [the] H9009 HTd", " 6 grievous H7451A HAamsa | word of another collection; qualifier qualifier subgroup: Bad (a quality of something); morph: adjective; collections lament", " 7 for H3588A HTc | connective", " 8 all H3605 HNcmsa", " 8 [the] H9009 HTd", " 8 all H3588A HTc | connective", " 9 vanity H1892 HNcmsa | word of another collection; collections pride", "*10 striving H7469 HNcfsc | member of this collection", " 10 and H9002 HC", " 11 wind H7307H HNcfsa"]
- reference: Ecc 2:22
  text: What has a man from all the toil and striving of heart with which he toils beneath the sun?
  words: [" 0 what H4100 HPi", " 0 what H3588A HTc | connective", " 1 has H1933B HVqrmsa", " 2 man H0120G HNcmsa | entity (human); party human", " 2 to/for H9005 HRd", " 3 all H3605 HNcmsc", " 4 toil H5999 HNcbsc | word of another collection; collections labor", " 4 in/on/with H9003 HR", "*5 striving H7475 HNcmsc | member of this collection", " 5 in/on/with H9003 HR", " 5 and H9002 HC", " 5 his H9023 HSp3ms", " 6 heart H3820A HNcmsc | word of another collection; collections heart", " 7 which H1931 HPp3ms", " 7 which/that H9007 HTr", " 7 his H9023 HSp3ms", " 8 toils H6001B HAamsa | qualifier candidate; qualifier morph: adjective", " 9 beneath H8478G HNcmsc", " 10 sun H8121 HNcbsa", " 10 [the] H9009 HTd"]
- reference: Ecc 2:26
  text: For to the one who pleases him God has given wisdom and knowledge and joy, but to the sinner he has given the business of gathering and collecting, only to give to one who pleases God. This also is vanity and a striving after wind.
  words: [" 0 for H3588A HTc | connective", " 1 one H0120G HNcmsa | entity (human); party human", " 1 to/for H9005 HR", " 2 pleases H2896A HAamsa | word of another collection; qualifier qualifier subgroup: Good, better, well (a quality of something); morph: adjective; collections delight", " 2 which/that H9007 HTr", " 3 him H6440G HNcmpc", " 3 to/for H9005 HR", " 4 given H5414G HVqp3ms | word of another collection; collections share", " 4 his H9023 HSp3ms", " 5 wisdom H2451 HNcfsa | word of another collection; collections wise", " 6 knowledge H1847 HNcfsa | word of another collection; collections know", " 6 and H9002 HC | connective", " 7 joy H8057 HNcfsa | word of another collection; collections delight", " 7 and H9002 HC | connective", " 8 sinner H2398 HVqrmsa | word of another collection; collections sin", " 8 and H9002 HC | connective", " 8 to/for H9005 HRd", " 9 given H5414G HVqp3ms | word of another collection; collections share", " 10 business H6045 HNcmsa", " 11 gathering H0622 HVqcc", " 11 to/for H9005 HR", " 12 collecting H3664 HVqcc", " 12 and H9002 HC | connective", " 12 to/for H9005 HR", " 13 give H5414G HVqcc | word of another collection; collections share", " 13 to/for H9005 HR", " 14 pleases H2896A HAamsa | word of another collection; qualifier qualifier subgroup: Good, better, well (a quality of something); morph: adjective; collections delight", " 14 to/for H9005 HR", " 14 pleases H6440G HNcmpc | word of another collection; collections delight", " 15 god H0430G HNcmpa | entity (divine); party divine", " 15 [the] H9009 HTd", " 15 to/for H9005 HR", " 16 this H2088 HTm", " 17 also H1571 HD | qualifier candidate; qualifier morph: adverb", " 18 vanity H1892 HNcmsa | word of another collection; collections pride", "*19 striving H7469 HNcfsc | member of this collection", " 19 and H9002 HC", " 20 wind H7307H HNcfsa"]
- reference: Ecc 4:4
  text: Then I saw that all toil and all skill in work come from a man’s envy of his neighbor. This also is vanity and a striving after wind.
  words: [" 0 i H0589 HPp1bs", " 1 saw that H7200G HVqq1cs", " 2 all H3605 HNcmsc", " 2 all H0853 HTo", " 3 toil H5999 HNcbsa | word of another collection; collections labor", " 4 all H3605 HNcmsc", " 4 all H0853 HTo", " 4 and H9002 HC | connective", " 5 skill H3788 HNcmsc | word of another collection; collections skill", " 6 work H4639G HNcmsa | word of another collection; collections labor", " 6 [the] H9009 HTd", " 7 man’s H0376I HNcmsa", " 8 envy H7068 HNcfsc | word of another collection; collections jealous", " 8 envy H3588A HTc | word of another collection; collections jealous", " 8 envy H1931 HPp3fs | word of another collection; collections jealous", " 9 neighbor H7453 HNcmsc | entity (human); party human", " 9 from H9006 HR", " 10 this H2088 HTm", " 11 also H1571 HD | qualifier candidate; qualifier morph: adverb", " 11 his H9023 HSp3ms", " 12 vanity H1892 HNcmsa | word of another collection; collections pride", "*13 striving H7469 HNcfsc | member of this collection", " 13 and H9002 HC", " 14 wind H7307H HNcfsa"]
- reference: Ecc 4:6
  text: Better is a handful of quietness than two hands full of toil and a striving after wind.
  words: [" 0 better H2896A HAamsa | qualifier candidate; qualifier qualifier subgroup: Good, better, well (a quality of something); morph: adjective", " 1 handful H3709G HNcfsc", " 1 handful H4393 HNcmsc", " 2 quietness H5183A HNcfsa | word of another collection; collections mute", " 3 two hands H2651 HNcmda", " 4 full H4393 HNcmsc", " 4 from H9006 HR", " 5 toil H5999 HNcbsa | word of another collection; collections labor", "*6 striving H7469 HNcfsc | member of this collection", " 6 and H9002 HC", " 7 wind H7307H HNcfsa"]
- reference: Ecc 4:16
  text: There was no end of all the people, all of whom he led. Yet those who come later will not rejoice in him. Surely this also is vanity and a striving after wind.
  words: [" 0 no H0369 HNcmsc", " 1 end H7093 HNcmsa", " 2 all H3605 HNcmsc", " 2 to/for H9005 HR", " 3 people H5971A HNcmsa", " 3 [the] H9009 HTd", " 4 all H3605 HNcmsa", " 4 to/for H9005 HR", " 5 led H6440G HNcmpc | word of another collection; collections govern", " 5 to/for H9005 HR", " 5 led H0834A HTr | word of another collection; collections govern", " 5 led H1961 HVqp3ms | word of another collection; collections govern", " 6 yet H1571 HD | qualifier candidate; qualifier morph: adverb", " 6 their H9028 HSp3mp", " 7 come later H0314 HAampa | qualifier candidate; qualifier morph: adjective", " 7 [the] H9009 HTd", " 8 not H3808 HTn | negator; qualifier negator; negator", " 9 rejoice H8055 HVqi3mp | word of another collection; collections gladden", " 10 surely H3588A HTc | word of another collection; collections loyalty", " 10 in/on/with H9003 HRd", " 10 him H9033 HSp3ms", " 11 also H1571 HD | qualifier candidate; qualifier morph: adverb", " 12 vanity H1892 HNcmsa | word of another collection; collections pride", " 12 vanity H2088 HTm | word of another collection; collections pride", "*13 striving H7475 HNcmsc | member of this collection", " 13 and H9002 HC", " 14 wind H7307H HNcfsa"]
- reference: Ecc 6:9
  text: Better is the sight of the eyes than the wandering of the appetite: this also is vanity and a striving after wind.
  words: [" 0 better H2896A HAamsa | qualifier candidate; qualifier qualifier subgroup: Good, better, well (a quality of something); morph: adjective", " 1 sight H4758 HNcmsc", " 2 eyes H5869A HNcfda", " 3 than H9006 HR", " 4 wandering H1980I HVqcc | word of another collection; collections astray", " 5 appetite H5315L HNcfsa | word of another collection; collections desire", " 6 this H2088 HTm", " 7 also H1571 HD | qualifier candidate; qualifier morph: adverb", " 8 vanity H1892 HNcmsa | word of another collection; collections pride", "*9 striving H7469 HNcfsc | member of this collection", " 9 and H9002 HC", " 10 wind H7307H HNcfsa"]
- reference: Isa 45:9
  text: “ Woe to him who strives with him who formed him, a pot among earthen pots! Does the clay say to him who forms it, ‘ What are you making?’ or ‘Your work has no handles ’?
  words: [" 0 woe H1945 HTj | word of another collection; collections tribulation", "*1 strives H7378 HVqrmsa | member of this collection", " 2 with H0854 HR", " 3 formed him H3335G HVqrmsc", " 4 pot H2789 HNcmsa", " 4 him H9033 HSp3ms", " 5 among earthen H0127G HNcfsa", " 6 pots H2789 HNcmpc", " 6 pots H0854 HR", " 7 clay H2563A HNcmsa", " 8 say H0559 HVqi3ms", " 8 [¿] H9008 HTi", " 9 forms H3335G HVqrmsc", " 9 to/for H9005 HR", " 10 what H4100 HPi", " 10 him H9033 HSp3ms", " 11 making H6213H HVqi2ms", " 12 work H6467 HNcmsc | word of another collection; collections labor", " 12 and H9002 HC | connective", " 13 to/for H9005 HRd", " 13 him H9033 HSp3ms", " 14 no H0369 HNcmsc", " 14 your H9021 HSp2ms", " 15 handles H3027G HNcbda"]
- reference: Hos 12:4
  text: He strove with the angel and prevailed; he wept and sought his favor. He met God at Bethel, and there God spoke with us —
  words: ["*0 strove H7786 HVqw3ms | member of this collection", " 1 angel H4397H HNcmsa", " 1 angel H0413 HR", " 2 prevailed H3201 HVqw3ms | word of another collection; collections prevail", " 3 wept H1058 HVqp3ms | word of another collection; collections laugh", " 4 favor H2603A HVtw3ms | word of another collection; collections delight", " 5 met H4672 HVqi3ms", " 6 bethel H1008G HNpl", " 6 to/for H9005 HR", " 6 him H9033 HSp3ms", " 7 spoke H1696G HVpi3ms", " 7 him H9033 HSp3ms", " 7 there H8033G HD | qualifier candidate; qualifier morph: adverb", " 7 and H9002 HC | connective", " 8 with H5973A HR", " 9 us H9035 HSp1bp"]
- reference: 1Ti 4:10
  text: For to this end we toil and strive, because we have our hope set on the living God, who is the Savior of all people, especially of those who believe.
  words: [" 0 for G1063 CONJ | connective", " 1 to G1519 PREP", " 2 this G3778 D-ASN", " 3 toil G2872 V-PAI-1P | word of another collection; collections labor", " 4 and G2532 CONJ | connective", "*5 strive G0075 V-PNI-1P | member of this collection", " 6 because G3754H CONJ | connective", " 7 hope G1679 V-RAI-1P | word of another collection; collections hope", " 8 on G1909 PREP", " 9 living G2198 V-PAP-DSM | word of another collection; collections live", " 10 god G2316 N-DSM-T | entity (divine); party divine", " 11 who G3739 R-NSM", " 12 is G1510 V-PAI-3S", " 13 savior G4990 N-NSM", " 14 all G3956 A-GPM | qualifier candidate; qualifier morph: adjective", " 15 people G0444 N-GPM | entity (human); party human", " 16 especially G3122 ADV | qualifier candidate; qualifier morph: adverb", " 17 believe G4103 A-GPM | word of another collection; qualifier morph: adjective; collections believe"]
- reference: Heb 4:11
  text: Let us therefore strive to enter that rest, so that no one may fall by the same sort of disobedience.
  words: [" 0 therefore G3767 CONJ | connective", "*1 strive G4704 V-AAS-1P | member of this collection", " 2 enter G1525 V-2AAN", " 2 enter G1519 PREP", " 3 that G1565 D-ASF", " 4 rest G2663 N-ASF | word of another collection; collections mute", " 5 no G3363 CONJ | connective", " 6 one G5100 X-NSM", " 7 fall G4098 V-2AAS-3S", " 8 by G1722 PREP", " 9 same G0846 P-DSN", " 10 sort G5262 N-DSN", " 11 disobedience G0543 N-GSF | word of another collection; collections submission"]
- reference: Heb 12:14
  text: Strive for peace with everyone, and for the holiness without which no one will see the Lord.
  words: ["*0 strive G1377 V-PAM-2P | member of this collection", " 1 peace G1515 N-ASF | word of another collection; collections quarrel", " 2 with G3326 PREP", " 3 everyone G3956 A-GPM | qualifier candidate; qualifier morph: adjective", " 4 and G2532 CONJ | connective", " 5 holiness G0038 N-ASM | word of another collection; collections godly", " 6 without G5565 PREP", " 7 which G3739 R-GSM", " 8 no one G3762 A-NSM | qualifier candidate; qualifier morph: adjective", " 9 see G3708G V-FDI-3S", " 10 lord G2962G N-ASM-T | entity (divine); party divine"]

## rows

- ledger_id: 2282
  item: pairing
  subject: labor
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Ecc 2:11", "Ecc 2:22", "Ecc 4:4", "Ecc 4:6", "Isa 45:9", "1Ti 4:10"]
  occurrences: [{"occurrence": 1285032, "reference": "Ecc 2:11", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1285121, "reference": "Ecc 2:22", "surface": "striving", "strong": "H7475", "as": "member"}, {"occurrence": 1285196, "reference": "Ecc 4:4", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1285207, "reference": "Ecc 4:6", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1294373, "reference": "Isa 45:9", "surface": "strives", "strong": "H7378", "as": "member"}, {"occurrence": 1499524, "reference": "1Ti 4:10", "surface": "strive", "strong": "G0075", "as": "member"}, {"occurrence": 1285019, "reference": "Ecc 2:11", "surface": "toil", "strong": "H5999", "as": "partner"}, {"occurrence": 1285119, "reference": "Ecc 2:22", "surface": "toil", "strong": "H5999", "as": "partner"}, {"occurrence": 1285179, "reference": "Ecc 4:4", "surface": "toil", "strong": "H5999", "as": "partner"}, {"occurrence": 1285184, "reference": "Ecc 4:4", "surface": "work", "strong": "H4639G", "as": "partner"}, {"occurrence": 1285206, "reference": "Ecc 4:6", "surface": "toil", "strong": "H5999", "as": "partner"}, {"occurrence": 1294389, "reference": "Isa 45:9", "surface": "work", "strong": "H6467", "as": "partner"}, {"occurrence": 1499522, "reference": "1Ti 4:10", "surface": "toil", "strong": "G2872", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2283
  item: pairing
  subject: lament
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Ecc 2:17"]
  occurrences: [{"occurrence": 1284708, "reference": "Ecc 2:17", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1284702, "reference": "Ecc 2:17", "surface": "grievous", "strong": "H7451A", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2284
  item: pairing
  subject: laugh
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Hos 12:4"]
  occurrences: [{"occurrence": 1385251, "reference": "Hos 12:4", "surface": "strove", "strong": "H7786", "as": "member"}, {"occurrence": 1385255, "reference": "Hos 12:4", "surface": "wept", "strong": "H1058", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2285
  item: pairing
  subject: live
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["1Ti 4:10"]
  occurrences: [{"occurrence": 1499524, "reference": "1Ti 4:10", "surface": "strive", "strong": "G0075", "as": "member"}, {"occurrence": 1499528, "reference": "1Ti 4:10", "surface": "living", "strong": "G2198", "as": "partner"}]
  older: [{"observation": 12331, "stage": "strand-reading", "kind": "key-statement", "nature": null, "text": "The soul, the heart and the conscience turned toward the living God, or away.", "verses": ["Ps.42.2", "Ps.84.2", "Heb.3.12", "Heb.10.31", "Heb.9.14", "Deut.5.26", "1Tim.4.10"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2286
  item: pairing
  subject: love
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Ecc 2:17"]
  occurrences: [{"occurrence": 1284708, "reference": "Ecc 2:17", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1284689, "reference": "Ecc 2:17", "surface": "hated", "strong": "H8130", "as": "partner"}]
  older: [{"observation": 16883, "stage": "prior-capture", "kind": "statement", "nature": null, "text": "Revisit (Batch G §6, §5.4): A third, despairing use: \"I loathe my life … the bitterness of my soul\" (Job 10:1); \"So I hated life … I … gave my heart up to despair\" (Ecc 2:17–20); Jonah: \"take my life … angry enough to die\" (Jon 4:3, 9, context 4:1–11); Here the soul turns against its life from exhaustion, not for another's sake. The words overlap with Joh 12:25; the purpose differs.; On \"lose / save\": Mat 16:26 (\"what shall a man give in return for his soul?\") and Mic 6:7–8 (the firstborn refused as a price for \"the sin of my soul\") both refuse a price for the soul.", "verses": ["Job.10.1", "Eccl.2.17", "Eccl.2.18", "Eccl.2.20", "Jonah.4.3", "Jonah.4.9", "John.12.25", "Matt.16.26", "Mic.6.7"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2287
  item: pairing
  subject: loyalty
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Exo 21:22", "Ecc 4:16"]
  occurrences: [{"occurrence": 1015257, "reference": "Exo 21:22", "surface": "strive", "strong": "H5327A", "as": "member"}, {"occurrence": 1015258, "reference": "Exo 21:22", "surface": "strive", "strong": "H3588A", "as": "member"}, {"occurrence": 1287996, "reference": "Ecc 4:16", "surface": "striving", "strong": "H7475", "as": "member"}, {"occurrence": 1015270, "reference": "Exo 21:22", "surface": "surely", "strong": "H6064", "as": "partner"}, {"occurrence": 1287990, "reference": "Ecc 4:16", "surface": "surely", "strong": "H3588A", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2288
  item: pairing
  subject: mute
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Ecc 4:6", "Heb 4:11"]
  occurrences: [{"occurrence": 1285207, "reference": "Ecc 4:6", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1504215, "reference": "Heb 4:11", "surface": "strive", "strong": "G4704", "as": "member"}, {"occurrence": 1285202, "reference": "Ecc 4:6", "surface": "quietness", "strong": "H5183A", "as": "partner"}, {"occurrence": 1504219, "reference": "Heb 4:11", "surface": "rest", "strong": "G2663", "as": "partner"}]
  older: [{"observation": 21290, "stage": "engagement", "kind": "face", "nature": null, "text": "Quietness is itself the settled inner rest and trust: the result of righteousness, the ground of strength, and better than toil and striving.", "verses": ["Eccl.4.6", "Isa.30.15", "Isa.32.17"]}]
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2289
  item: pairing
  subject: prevail
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Gen 32:28", "Hos 12:4"]
  occurrences: [{"occurrence": 987217, "reference": "Gen 32:28", "surface": "striven", "strong": "H8280", "as": "member"}, {"occurrence": 1385251, "reference": "Hos 12:4", "surface": "strove", "strong": "H7786", "as": "member"}, {"occurrence": 987224, "reference": "Gen 32:28", "surface": "prevailed", "strong": "H3201", "as": "partner"}, {"occurrence": 1385254, "reference": "Hos 12:4", "surface": "prevailed", "strong": "H3201", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2290
  item: pairing
  subject: pride
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Ecc 1:14", "Ecc 2:11", "Ecc 2:17", "Ecc 2:26", "Ecc 4:4", "Ecc 4:16", "Ecc 6:9"]
  occurrences: [{"occurrence": 1288469, "reference": "Ecc 1:14", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1285032, "reference": "Ecc 2:11", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1284708, "reference": "Ecc 2:17", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1287677, "reference": "Ecc 2:26", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1285196, "reference": "Ecc 4:4", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1287996, "reference": "Ecc 4:16", "surface": "striving", "strong": "H7475", "as": "member"}, {"occurrence": 1285680, "reference": "Ecc 6:9", "surface": "striving", "strong": "H7469", "as": "member"}, {"occurrence": 1288468, "reference": "Ecc 1:14", "surface": "vanity", "strong": "H1892", "as": "partner"}, {"occurrence": 1285031, "reference": "Ecc 2:11", "surface": "vanity", "strong": "H1892", "as": "partner"}, {"occurrence": 1284707, "reference": "Ecc 2:17", "surface": "vanity", "strong": "H1892", "as": "partner"}, {"occurrence": 1287676, "reference": "Ecc 2:26", "surface": "vanity", "strong": "H1892", "as": "partner"}, {"occurrence": 1285195, "reference": "Ecc 4:4", "surface": "vanity", "strong": "H1892", "as": "partner"}, {"occurrence": 1287994, "reference": "Ecc 4:16", "surface": "vanity", "strong": "H1892", "as": "partner"}, {"occurrence": 1287995, "reference": "Ecc 4:16", "surface": "vanity", "strong": "H2088", "as": "partner"}, {"occurrence": 1285679, "reference": "Ecc 6:9", "surface": "vanity", "strong": "H1892", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2291
  item: pairing
  subject: quarrel
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Heb 12:14"]
  occurrences: [{"occurrence": 1505281, "reference": "Heb 12:14", "surface": "strive", "strong": "G1377", "as": "member"}, {"occurrence": 1505282, "reference": "Heb 12:14", "surface": "peace", "strong": "G1515", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)
- ledger_id: 2292
  item: pairing
  subject: refresh
  asks: Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.
  none_allowed: true
  verses: ["Psa 60:1"]
  occurrences: [{"occurrence": 1254571, "reference": "Psa 60:1", "surface": "strove", "strong": "H5327A", "as": "member"}, {"occurrence": 1254596, "reference": "Psa 60:1", "surface": "restore", "strong": "H7725H", "as": "partner"}]
  older: []
  wordnet_control: WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)

## measured

- package_chars: 57920
- seconds: 0.02

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadStructure",
 "collection": "strive",
 "subgroup": "exertion toward an end",
 "rows": [
  {
   "ledger_id": 2282,
   "item": "pairing",
   "subject": "labor",
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
   "ledger_id": 2283,
   "item": "pairing",
   "subject": "lament",
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
   "ledger_id": 2284,
   "item": "pairing",
   "subject": "laugh",
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
   "ledger_id": 2285,
   "item": "pairing",
   "subject": "live",
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
     "observation": 12331,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2286,
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
     "observation": 16883,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2287,
   "item": "pairing",
   "subject": "loyalty",
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
   "ledger_id": 2288,
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
     "observation": 21290,
     "action": "keep | restate | merge | consume | delete_neither | defer | carry",
     "reason": ""
    }
   ]
  },
  {
   "ledger_id": 2289,
   "item": "pairing",
   "subject": "prevail",
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
   "ledger_id": 2290,
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
  },
  {
   "ledger_id": 2291,
   "item": "pairing",
   "subject": "quarrel",
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
   "ledger_id": 2292,
   "item": "pairing",
   "subject": "refresh",
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
