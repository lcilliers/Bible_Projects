# ReadWords -- boast / boast about -- step S1

## What to do

Step S1, the words of one subgroup (stage 1, the lexical analysis): each word -- a surface with its lettered Strong's code -- read in the verse of each of its occurrences, for what it is and how it is used there. Nothing here says what a word does for the inner being; that begins at step 3.1.

Read:
- Take one word at a time, and within it one occurrence at a time, in the verse of that occurrence.
- Read the evidence in this order: the verse text and the occurrence's stored structure (morph, unit, surface_kind, negator, party_kind, narrative); then the meaning sources for the code read together (sense_head, meaning_range, lsj, mounce), none picked and the others dropped; then the English rendering against the literal sense: does the English add or hide?
- Judge the meaning in context from the Strong's code and the verse, not from the English surface alone. Where occurrences show different stems or voices, say whether the subject does, undergoes or causes the act.
- The prompts are areas to explore; a prompt that does not apply is not answered.

Write:
- Fill `answer.rows`: for each word, its `readings`. One reading for each distinct way the word is used: the occurrences where it is used the same way are listed together in that reading's `occurrences` (occurrence ids or verse references); an occurrence used differently is its own reading.
- kind: term; face where the use in a verse departs from the word's usual sense.
- obs_text: concise; names the verse or verses; states what the word is and how it is used there (its object, setting, construction, what the morph shows); never the dictionary range, never the verse restated.
- basis: stated (the verse says it) or read (read from the structure or the context). grounds: what in the verse shows it.
- Every occurrence of the word is in exactly one reading; none is left out. A homonym or a name is recorded as such; a data error is named in grounds, not fixed.
- `older`: the older observations on the word's occurrences. Read each with the word (they are what was recorded before) and answer each in the row's `older`, once: keep (with `nature` evidence or inner_being: it stands as it is); restate (with `nature`, `new_text` and `checked`: what in the base data the new text was checked against); merge (with `into`: a live observation saying the same); consume (with `carriers`, ["this"] for this row's readings or observation ids, and `mapping`: what the old one says and which carrier states each part); delete_neither (with `reason`: it is neither evidence nor inner being); carry (with `to` a later step, 1.1 or 2.1, and `reason`: what that step is to consider); defer (with `collection`, `nature` and `finding`: another collection owns the rest). An older observation listed under another word is answered there.
- Where a reading, sense, enrichment or finding holds every occurrence of the row's subject, `occurrences` may be "all": the recorder names them.
- Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing written; correct the answer until it finds none, then -Action RecordWords -File <the answer file>. The record refuses the whole file on any fault and lists every fault.

## Refused when (by rule)

- DA-02: belongs to collection; the nodes do not carry the collections
- IB-07: is not marked evidence: an inner-being observation traces to evidence; an observation does not trace itself
- LR-01: is not closed (every row answered
- LR-02: the text names none of them; names its grounds in the words of the verse; are not words of the lexicon entries; are not words of the verses; the data holds no occurrence for this aspect; names the occurrences it is about; names no occurrence (fill occurrences; are already in another sense; are in no sense; no occurrence to adopt for
- LR-03: cannot be recorded as none; none needs its reason
- PC-01: is not a step of the layered reading; is not a live subgroup of; no live collection; has no live subgroup; cannot read ;  are required;  is required
- PC-02: answer (its `command` must be; is a list of {observation, action, reason; the answer holds no ; (fill.senses): at least one; this is not the answer of a read
- PC-03: not a ledger row of; is not a word of subgroup; occurrences that are not occurrences of; is not an older live observation on the occurrences of this row; is not an open old observation of this subgroup; adopt names a live observation; a deferral names a live collection; has no matching live verse_lexical row; both must be different live observations;  is not an occurrence of ; is not a live observation; is not a live node; does not exist;  is not a ; merge names a live observation to keep; defer names a live collection
- PC-04: kind must be one of; basis must be one of; role must be one of; route must be one of; tag must be one of; stage must be one of; nature must be one of; disposition must be observed; is not a node role; cannot be modified (allowed:; not in live cfg_enum ib_observation; , the item takes ; action is one of; names its marker, nature one of
- PC-05: only an open or an unvalidated row is recorded;  row is answered by its own command; the evidence validation of ; has no open row; its group is retired or missing; carry names a LATER step of; the loop is for one subgroup at a time; partner collection 
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

- RG-08 the-original: For every word that names an inner or bodily act, look at the original: the root's range in all three meaning sources read together, never one picked and the others dropped; the ESV renderings across its verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is open, record each, and mark the choice 'I read'.
- RG-14 morph-read: Morph is read, not carried: where occurrences of a word show different stems or voices, record whether the subject does, undergoes or causes the act.
- RG-16 homonym-and-data-error: A word that is only a homonym or a name, with no meaningful context, is recorded as such (tag no-human-context) and left. Data errors found while reading are flagged (tag data-error), not fixed in the reading.
- RG-17 catalogue-as-prompts: The question catalogue's questions are prompts for the areas to explore. A question that does not apply is not answered, and no answer is manufactured beyond what the verse shows.
- RG-21 grain: A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- RG-22 content-words-carry-impact: Content words carry the inner-being impact and are read even when no cluster tags them. Function words (particles, prepositions, conjunctions, suffixes, pronouns) get no observation of their own, except negators and connectives, which are read for what they do (RG-07). A T2 word never stands alone: it is read as the qualifier of what it binds to.
- RW-03 no-duplicates-multi-node: One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- RW-04 concise-verse-specific: Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- RW-08 slants-own-rows: Where the evidence points to more than one reading, each is its own observation with its own evidence.
- RW-09 reread-builds-on-prior: A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- RW-13 older-observations-answered-at-record: Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- RS-04 existing-checked-accept-modify-delete: When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- VA-03 consumption-is-verified-before-deletion: An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- VA-04 neither-evidence-nor-inner-being-is-deleted: An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.
- DA-02 a-node-per-occurrence-with-its-surfaces-collection: A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope (B:130), is not written and is listed.
- IB-07 inner-being-observations-trace-to-evidence: Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or on a live inner-being observation that itself traces to evidence (the trace chain of stage 4: a 3.2 behaviour traces the 3.1 elements it gathers, a 3.3 match the 3.1 and 3.2 observations it comes from; at most three links), unless it is recorded self-evidencing: it quotes its verse in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. A trace points first at existing evidence; an evidence observation is created only when none states the fact and it states what the nodes and the quotation do not. An inner-being observation traced to evidence not yet marked is pending, not failed.
- LR-01 a-step-opens-on-gates-and-derives-its-ledger: A step of the layered reading opens only when the grouping is finished (every surface placed in a subgroup or isolated with its reason, every subgroup holding a surface) and the previous step is closed; with -Subgroup the needs and gates are judged for that subgroup alone (#2538). Step S1 is read after the grouping; step 1.1 needs step S1 closed: every word of the subgroup (surface and lettered Strong's code) answered and validated. Opening derives one ledger row for each aspect the data demands (cfg_setting layer.reading); an aspect the data no longer demands is retired, a new one is added, and a second open changes nothing.
- LR-02 nodes-are-built-from-the-data: The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
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

2026-11-26T15:13:34Z

## batch

- words: 1
- words_left_after_this: 0

## prompts

- code: M0.1.1; question: In this verse, looking at this specific occurrence (its surface form and morph_code), what does this term's name/form show about its essential nature here?
- code: M0.1.2; question: In this verse, drawing on this term's lexicon entries but grounded in how it is actually used in this occurrence, what does it mean at the definitional level?
- code: M0.1.3; question: In this verse, what directional, relational, or constitutional implication does this term's name carry as it functions in this specific occurrence?
- code: M0.4.1; question: What is the grammatical/stem form of this term in this verse?
- code: M0.5.1; question: In this verse, what does this term's root meaning show about how it operates in this specific occurrence?
- code: M0.5.2; question: In this verse, what does this occurrence's own grammatical form (per its morph_code — e.g. noun, verb, adjective, participle) show about how the term operates here?
- code: M0.5.3; question: In this verse, given this term's known semantic range — the breadth of meaning it can carry, including idiomatic, analogical, or combinatorial senses — where does this occurrence sit within that range, and what does that show about how the term operates here?
- code: M0.5.4; question: In this verse, does this occurrence express a specific aspect — disposition versus act, received versus given, condition versus quality? Record which, or none.
- code: M0.5.5; question: In this verse, among this term's own related terms, is there one that functions as this occurrence's structural opposite? Record it, or none.
- code: M0.5.6; question: In this verse, among this term's own related terms, is there a person-type term relevant to this occurrence — one for a person who habitually possesses or exercises it? Record it, or none.
- code: M0.5.7; question: In this verse, among this term's own related terms, is there a supplication or seeking term relevant to this occurrence — one for the act of seeking it from another? Record it, or none.
- code: M0.5.8; question: In this verse, does this term's Testament context (OT Hebrew vs. NT Greek) affect how this specific occurrence should be interpreted, and if so, how? Record none if the Testament context makes no interpretive difference here.
- code: M0.5.9; question: In this verse, if this term is newly coined in the NT period, what does that coinage show about how it functions in this occurrence? Record none if not applicable or not relevant to this occurrence.
- code: M0.5.11; question: In this verse, where this occurrence's meaning diverges from the term's usual sense elsewhere, what nuance does that divergence carry here, and how does it compare to the word's other occurrences? Pay particular attention to this occurrence's own surface form/rendering — a marked or atypical surface form is often the visible trace of the divergence itself, not a separate fact. Record none if this occurrence matches the term's usual sense.

## words

- ledger_id: 2196; word: boast about; strong: G2745; lexicon: {"sense_head": "pride", "meaning_range": "something to boast about, boasting; pride, joy; <b>a glorying, boasting,</b> <ref='1Co.5.6'>1Cor. 5:6;</ref> <b>a ground</b> or <b>matter of glorying</b> or <b>boasting,</b> <ref='Rom.4.2'>Rom. 4:2;</ref> <b>joy, exultation,</b> <ref='Php.1.26'>Phil. 1:26;</ref> <b>complimentary testimony,</b> <ref='1Co.9.15, 16'>1Cor. 9:15, 16</ref>; <ref='2Co.9.3'>2Cor. 9:3</ref>", "lsj": "<b> καύχ-ημα</b>, <br /> <i>Doric dialect</i> <b>καύχ-ᾱμα</b>, ατος, τό, <b>a boast, vaunt</b>, [<a href=\"javascript:void(0)\" title=\" 5th c.BC: Pindarus Lyricus “I.” 5(4).51. \">Refs 5th c.BC+</a>]<br /><Level3><b>__2</b></Level3> <b>subject of boasting</b>, [<a href=\"javascript:void(0)\" title=\" 2nd c.AD: Lesbonax Rhetor 3.4 (_plural_), NT.Rom.4.2. \">NT+2nd c.AD+</a>]", "mounce": "something to boast about, boasting; pride, joy", "related": ["G2744 καυχάομαι to boast"]}; occurrences: [{"occurrence": 1475839, "reference": "Rom 4:2", "morph": "N-ASN", "unit": "boast about", "surface_kind": "own", "negator": false, "party_kind": null, "narrative": null, "verse": "For if Abraham was justified by works, he has something to boast about, but not before God."}]; older: []

## measured

- package_chars: 25798
- seconds: 0.13

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadWords",
 "collection": "boast",
 "subgroup": "boast about",
 "rows": [
  {
   "ledger_id": 2196,
   "word": "boast about|G2745",
   "readings": [
    {
     "kind": "term | face",
     "obs_text": "",
     "basis": "stated | read",
     "grounds": "",
     "occurrences": []
    }
   ],
   "older": []
  }
 ]
}
```
