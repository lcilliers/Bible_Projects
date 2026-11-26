# ReadEnrichment -- boast / boastful -- step 1.2

## What to do

Step 1.2, the enrichment of one subgroup (stage 1, B2): for each sense of step 1.1, what the Strong's codes of its occurrences say. The lexicon is the point of this read. Nothing here says what a sense does for the inner being; that begins at step 3.1.

Read:
- Take one sense at a time (`senses`: its text from step 1.1, its codes, words and occurrences).
- Read the lexicon of each of its codes (`codes`: sense_head, meaning_range, lsj, mounce, related), the three meaning sources read together, none picked and the others dropped.
- Validate the sense against its codes: do the lexicon entries bear out the meaning the sense names? Where they do not, say so in the enrichment; the sense is not changed here.
- Where one surface carries several codes in the sense, read what each code adds.

Write:
- Fill `answer.enrichments`: one entry for each sense, named by `sense` (the id of its 1.1 observation); every sense has exactly one. The enrichment takes the sense's occurrences.
- kind: enrichment. obs_text: a short definition from the lexicon entries; names the codes that link the sense to its usage and what different codes of one surface add; names verses the sense holds in, as the package writes the references (for example Psa 77:6); concise; never the lexicon copied whole, never a verse restated, never what the sense does for the inner being.
- basis: read, with `grounds`: words copied exactly from the lexicon of a code of the sense (sense_head, meaning_range, lsj or mounce; the record checks them); or stated, where a verse says it.
- Where the lexicon does not bear out the sense, the enrichment says so with its grounds; a missing lexicon entry is named, never filled from memory (RW-11).
- `older`: answer each older observation shown, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` ["this"] for this answer's enrichments or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` 2.1 and `reason`), defer (with `collection`, `nature`, `finding`).
- Where a reading, sense, enrichment or finding holds every occurrence of the row's subject, `occurrences` may be "all": the recorder names them.
- Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing written; correct the answer until it finds none, then -Action RecordEnrichment -File <the answer file>. The record refuses the whole file on any fault and lists every fault.

## Refused when (by rule)

- DA-02: belongs to collection; the nodes do not carry the collections
- IB-07: is not marked evidence: an inner-being observation traces to evidence; an observation does not trace itself
- LR-01: is not closed (every row answered
- LR-02: the text names none of them; names its grounds in the words of the verse; are not words of the lexicon entries; are not words of the verses; the data holds no occurrence for this aspect; names the occurrences it is about; names no occurrence (fill occurrences; are already in another sense; are in no sense; has no enrichment (one enrichment; is already enriched by enrichment; no occurrence to adopt for
- LR-03: cannot be recorded as none; none needs its reason
- PC-01: is not a step of the layered reading; is not a live subgroup of; no live collection; has no live subgroup; cannot read ;  are required;  is required
- PC-02: answer (its `command` must be; is a list of {observation, action, reason; the answer holds no ; (fill.senses): at least one; this is not the answer of a read
- PC-03: nothing written:
  ledger ; not a ledger row of; occurrences that are not occurrences of; is not an older live observation on the occurrences of this row; is not an open old observation of this subgroup; is not a 1.1 sense of subgroup; adopt names a live observation; a deferral names a live collection; has no matching live verse_lexical row; both must be different live observations;  is not an occurrence of ; is not a live observation; is not a live node; does not exist;  is not a ; merge names a live observation to keep; defer names a live collection
- PC-04: kind must be one of; basis must be one of; role must be one of; route must be one of; tag must be one of; stage must be one of; nature must be one of; disposition must be observed; is not a node role; cannot be modified (allowed:; not in live cfg_enum ib_observation; , the item takes ; action is one of; names its marker, nature one of
- PC-05: only an open or an unvalidated row is recorded;  row is answered by its own command; the evidence validation of ; has no open row; its group is retired or missing; carry names a LATER step of; the loop is for one subgroup at a time; partner collection 
- PC-06:  s, more than ;  characters, more than 
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

- RG-08 the-original: For every word that names an inner or bodily act, look at the original: the root's range in all three meaning sources read together, never one picked and the others dropped; the ESV renderings across its verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is open, record each, and mark the choice 'I read'.
- RG-21 grain: A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- RO11 one-row-per-code: One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- RW-03 no-duplicates-multi-node: One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- RW-04 concise-verse-specific: Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- RW-09 reread-builds-on-prior: A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- RW-11 missing-is-named: Missing data in the base extract is named as a gap, never substituted from memory or outside knowledge.
- RW-13 older-observations-answered-at-record: Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- RS-04 existing-checked-accept-modify-delete: When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- LR-02 nodes-are-built-from-the-data: The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
- VA-03 consumption-is-verified-before-deletion: An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- VA-04 neither-evidence-nor-inner-being-is-deleted: An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.
- DA-02 a-node-per-occurrence-with-its-surfaces-collection: A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope (B:130), is not written and is listed.
- IB-07 inner-being-observations-trace-to-evidence: Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or on a live inner-being observation that itself traces to evidence (the trace chain of stage 4: a 3.2 behaviour traces the 3.1 elements it gathers, a 3.3 match the 3.1 and 3.2 observations it comes from; at most three links), unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed.
- LR-01 a-step-opens-on-gates-and-derives-its-ledger: A step of the layered reading opens only when the grouping is finished (every surface placed in a subgroup or isolated with its reason, every subgroup holding a surface) and the previous step is closed; with -Subgroup the needs and gates are judged for that subgroup alone (#2538). Step S1 is read after the grouping; step 1.1 needs step S1 closed: every word of the subgroup (surface and lettered Strong's code) answered and validated. Opening derives one ledger row for each aspect the data demands (cfg_setting layer.reading); an aspect the data no longer demands is retired, a new one is added, and a second open changes nothing.
- LR-03 none-needs-a-permitted-reason: An aspect is recorded as none only where its item allows it (cfg_setting layer.reading none_allowed) and with its reason in words. A group definition and a group's Strong's enrichment are always observed.
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

## made

2026-11-26T15:06:18Z

## unit

- ledger_id: 2170
- senses: 2
- occurrences: 5
- codes: 4
- older: 0

## prompts


## senses

- sense: 23877; text: The boastful as a kind of person: a noun or a participle used as a noun names those given to boasting, listed among the ungodly or set beside evildoers and the wicked (Rom 1:30, Psa 5:5, Psa 75:4).; codes: ["G0213", "H1984C"]; words: ["boastful|G0213", "boastful|H1984C"]; occurrences: ["Psa 5:5", "Rom 1:30", "Psa 75:4"]
- sense: 23878; text: Boasting as the quality of an act or a look: the noun gives its character to something else, the confidence Paul speaks with (2Cor 11:17) and the height of the king of Assyria's eyes (Isa 10:12).; codes: ["G2746", "H7312"]; words: ["boastful|G2746", "boastful|H7312"]; occurrences: ["2Cor 11:17", "Isa 10:12"]

## occurrences_in_no_sense


## codes

- G0213: {"surfaces": ["boastful"], "sense_head": "braggart", "meaning_range": "boaster, braggart; <b>prideful, arrogant, boasting,</b> <ref='Rom.1.30'>Rom. 1:30;</ref> <ref='2Ti.3.2'>2Tim. 3:2</ref>*", "lsj": "<b> ἀλαζ-ών</b> [ᾰλ], όνος, ὁ, ἡ, <br /> (ἄλη) properly <b>wanderer about country, vagrant</b>, [<a href=\"javascript:void(0)\" title=\" 7th-6th c.BC: Alcaeus Lyricus Comedy texts 31. \">Refs 7th c.BC+</a>]<br /><Level2><b>__II</b></Level2> <b>charlatan, quack</b>, especially of Sophists, [<a href=\"javascript:void(0)\" title=\" 5th c.BC: Cratinus Comicus 380, 5th-6th c.BC: Aristophanes Comicus “Nubes” 102, 5th-6th c.BC: Plato Philosophus “Charmides” 173c, +others \">Refs 5th c.BC+</a>]<br /><Level3><b>__II.2</b></Level3> <b>braggart, boaster</b>, [<a href=\"javascript:void(0)\" title=\" 5th-6th c.BC: Xenophon Historicus “Institutio Cyri (Cyropaedia)” 2.2.12, 4th c.BC: Aristoteles Philosophus “Ethica N", "mounce": "boaster, braggart", "related": ["G0212 ἀλαζονεία boasting"]}
- G2746: {"surfaces": ["boastful"], "sense_head": "pride", "meaning_range": "boasting, pride;; <b>boasting, pride, glorying in; this can refer to proper or improper boasting, depending on the object of the boast; </b> a later equivalent to <greek>καύχημαι</greek>, <ref='Rom.3.27'>Rom. 3:27;</ref> <ref='2Co.7.4, 14; 11.10'>2Cor. 7:4, 14; 11:10</ref>", "lsj": "<b> καύχ-ησις</b>, εως, ἡ, <br /> <b>boasting</b>, [<a href=\"javascript:void(0)\" title=\" 4th-3rd c.BC: Epicurus Philosophus “Fragmenta” 93, LXX.1Ch.29.13, +others, 1st c.BC: Philodemus Philosophus “περὶ κακιῶν ί” p.27 1st c.AD: Josephus Historicus, 1st c.AD: Philo Judaeus 1.534, NT.Rom.15.17. \">NT+4th c.BC+</a>]", "mounce": "boasting, pride;", "related": ["G2744 καυχάομαι to boast"]}
- H1984C: {"surfaces": ["boastful"], "sense_head": "to be foolish", "meaning_range": "1) (Poel) to make a fool of, make into a fool; 1f) (Hithpoel) to act madly, act like a madman", "lsj": "", "mounce": "", "related": ["H1947 הוֹלֵלָה madness", "H1948 הוֹלֵלוּת madness", "H1974 הִלּוּל praise", "H1984A הָלַל to shine", "H1984B הָלַל to boast: praise", "H1984H הָלַל to boast: boast", "H1984I הָלַל to boast: rave madly", "H1985 הִלֵּל Hillel", "H3094G יְהַלֶּלְאֵל Jehallelel", "H3094H יְהַלֶּלְאֵל Jehallelel", "H4110 מַהֲלָל praise", "H4111G מַהֲלַלְאֵל Mahalalel"]}
- H7312: {"surfaces": ["boastful"], "sense_head": "height", "meaning_range": "1) haughtiness, height, elevation; 1a) height, loftiness; 1b) haughtiness; Aramaic equivalent: <i>rum</i> (רוּם \"height\" H7314)", "lsj": "", "mounce": "", "related": ["H4791 מָרוֹם height", "H7216G רָאמוֹת Ramoth", "H7216H רָאמוֹת Ramoth", "H7311A רוּם to exalt", "H7311B רָמַם be rotten", "H7314 רוּם height", "H7315 רוֹם hight", "H7316G רוּמָה Dumah", "H7316H רוּמָה Rumah", "H7317 רוֹמָה haughtily", "H7318 רוֹמָם extolling", "H7320 רֹמַ֫מְתִּי עֶ֫זֶר Romamti-ezer"]}

## older


## measured

- package_chars: 23685
- seconds: 0.09

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadEnrichment",
 "collection": "boast",
 "subgroup": "boastful",
 "ledger_id": 2170,
 "enrichments": [
  {
   "sense": 23877,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 23878,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  }
 ],
 "older": []
}
```
