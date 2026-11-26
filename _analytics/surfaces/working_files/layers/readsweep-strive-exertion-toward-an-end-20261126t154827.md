# ReadSweep -- strive / exertion toward an end -- step 2.1

## What to do

The sweep (B4) of one subgroup, after its 2.1 rows: every observation of the subgroup's scope still unmarked after B1 to B3 -- older observations on its occurrences that B1 carried forward and B2 and B3 did not take up, any carried to the sweep, and any other unmarked observation of the scope (for example the reading of an earlier grouping). Each is judged by its content. End state: none of the subgroup's observations is unmarked, except one deferred to a named collection.

Read:
- Take one older observation at a time (`older`): its text, its stage and kind, its verses, how many of its nodes are on this subgroup's occurrences and how many elsewhere, and the collections its nodes belong to.
- Judge it by what it states, not by its stage or kind: does it state what the data are or show, tied to a verse (evidence)? how something works in the inner being, based on evidence (inner being)? or neither?

Write:
- Fill `answer.older`, one entry for each observation, each answered once, with `reason`: what it states and why it is so judged.
- merge, with `into`: a live observation of the subgroup says the same in the same words. consume, with `carriers` (observation ids) and `mapping`: live observations already state what it says; every word occurrence of it must be on a live node of a carrier (VA-03), then it is deleted. keep, with `nature` evidence or inner_being: it stands as it is (an inner-being one waits for 3.1). delete_neither: it is neither evidence nor inner being; it is commented, then deleted with its nodes here (one held by other subgroups or collections loses only the nodes here). defer, with `collection`, `nature` and `finding`: another collection owns it; it is marked now and the finding is left to that collection.
- Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing written; correct the answer until it finds none, then -Action RecordSweep -File <the answer file>. The record refuses the whole file on any fault; every unmarked observation must be answered.

## Refused when (by rule)

- DA-02: belongs to collection; the nodes do not carry the collections
- IB-07: is not marked evidence: an inner-being observation traces to evidence; an observation does not trace itself
- LR-01: is not closed (every row answered
- PC-01: is not a step of the layered reading; is not a live subgroup of; no live collection; has no live subgroup; cannot read ;  are required;  is required
- PC-02: answer (its `command` must be; is a list of {observation, action, reason; named twice; answered twice; this is not the answer of a read
- PC-03: is not an older live observation on the occurrences of this row; not in the unmarked observations of this subgroup; is not an open old observation of this subgroup; is not an unmarked older observation of; a deferral names a live collection; has no matching live verse_lexical row; both must be different live observations;  is not an occurrence of ; is not a live observation; is not a live node; does not exist;  is not a ; merge names a live observation to keep; defer names a live collection
- PC-04: basis must be one of; role must be one of; route must be one of; tag must be one of; stage must be one of; nature must be one of; the sweep answers with one of; cannot be modified (allowed:; not in live cfg_enum ib_observation; action is one of; names its marker, nature one of
- PC-05: comes after its 2.1 rows; the evidence validation of ; the sweep waits for every current subgroup; the sweep left ; has no open row; its group is retired or missing; has no sweep row; carry names a LATER step of; the loop is for one subgroup at a time; partner collection 
- PC-06:  s, more than 
- PC-07: cfg_setting layer.reading is missing; cfg_setting layer.scan; layer.reading step ; (apply iba/app/migration/archive/; the code is ahead of the config; have no nature in cfg_setting layer.reading; the read names rule(s) not active; is empty: run install_nature; are not ib_observation.tag values;  is missing
- RS-04: unmarked older observation(s) have no answer; older observation(s) are still unmarked
- RW-01: needs its reason, in words; say in words what was checked; say what it states that the existing record does not; state the finding the collection is to close; say in words which words it relies on; say in words why the word supports no finding; is the last word node of observation; already holds that occurrence: drop the node instead; its occurrence is on no live node of; carry gives its reason in words
- RW-03: is already live as observation; the same text as; a merge is for the same description
- RW-04: is a bare negation with no actual content
- RW-13: are still open in the ledger; have no answer in fill.older; its fate is not recorded; is not in the change log of observation; the change log does not show it
- RW-14: the statement used more than
- VA-03: name the carrying observations; the mapping is stated in words; occurrence(s) are on no node of; not carried needs its reason
- VA-04: the reason says why it is neither evidence nor inner being; only an observation that is neither is deleted here; repair those traces first; node(s) outside this subgroup
- VA-05: the reason says, in words, what the observation states; a deferred observation is marked now

## The rules

- VA-04 neither-evidence-nor-inner-being-is-deleted: An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.
- VA-05 the-marker-follows-content-not-stage: Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being, based on evidence, a building block of the stage 5 claims. The marker (ib_observation.nature) follows the content and purpose of the observation, never its stage (RS-04): an observation of any stage may be inner being when it traces to evidence. One that states both is split. The marker is set when the observation is created, by the item that is answered (cfg_setting layer.reading items.<item>.nature); a finding file never sets it; the validation changes it only where the content shows the item's nature does not hold.
- RW-01 changed-only-by-reading: No observation is changed except by a reading, and every change is recorded with its reason. An observation no longer supported by the verse is soft-deleted, with the reason.
- RS-04 existing-checked-accept-modify-delete: When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
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
- RW-03 no-duplicates-multi-node: One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- RW-04 concise-verse-specific: Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- RW-13 older-observations-answered-at-record: Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- RW-14 every-lookup-is-pinpointed: A lookup of related data in the build or the validation is by an indexed column and takes a chunk of ids (cfg_setting layer.scan chunk); none runs once for each item of a list, and a statement that uses more work than layer.scan max_vm_ops is stopped and named, nothing written (lib/scanguard.py). The tests refuse a statement of the build whose query plan scans a table (layer.scan scan_ok lists the temporary tables a statement may scan).
- VA-03 consumption-is-verified-before-deletion: An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.

## item

sweep

## made

2026-11-26T15:48:27Z

## older

- observation: 16995
  stage: prior-capture
  kind: statement
  text: 0. Data notes: Pre-filters from the handoff do not apply here. None of "Holy Spirit" (M61), "declares the Lord" (M42) or "Lord of hosts" (M72) falls in Batch C clusters. Nothing was removed.; "Seek my life" is one idiom, not inner seeking. About 40 of the 96 M83 verses are *biqqēš nephesh* — "seek (someone's) life" (1Sa 20:1; 23:15; 1Ki 19:10, 14; Jer 11:21; 19:7; 21:7; 22:25; 34:20–21; 44:30; 46:26; 49:37; Psa 35:4; 38:12; 40:14; 54:3; 63:9; 70:2; 86:14; Mat 2:20; Rom 11:3; etc.). Here *nephesh* is life as the object of hostile pursuit. It is reported in §7.5 and not mixed with the soul that seeks.; "Lacks sense" is "lacking heart" (H2638 + H3820A, d1): Pro 7:7; 9:4, 16; 10:13, 21; 11:12; 12:11; 15:21; 17:18; 24:30; 6:32; Ecc 10:3. H2638 "lacking" is filed under M18 Desire. It is a lack, not a desire. See §1.5. → Ruling R1.; "Pleasant" (H2896A *ṭôv*) is mostly generic "good / better". It accounts for 59 M18 pairs. The inner-being uses ("glad / merry / good of heart", "good to the soul", "better … in spirit") are kept in §1.6. Generic "better" is noted and not used (Num 11:18; Judg 9:2; Dan 1:15; 2Sa 18:3; Gen 1:21).; "Striving after wind" (H7469 *reʿût rûaḥ* "longing/pursuit" + rûaḥ *wind*, d1) is the Ecclesiastes refrain (Ecc 1:14; 2:11, 17, 26; 4:4, 6; 6:9). It is correctly a desire + wind pairing. See §1.9.; "Whole heart" is *lēv shālēm* (H8003 "complete", d1). It is filed under M34 Patience. In the verses it means an undivided, integral heart, not endurance. See §5.1. → Ruling R2.; "Contrite" (H1793A) is filed under M11 Turning. The verses are about a crushed spirit and heart (Psa 34:18; Isa 57:15), not about turning. They are kept in §8.4. → Ruling R3.; Misfiled tags, noted and not used: H6569 "refuse" = *dung*, read as "refuse" (M30): the flesh-skin-dung-burned sacrificial verses (Exo 29:14; Lev 4:11; 8:17; 16:27; Num 19:5); also Eze 32:5 "carcass" and Job 41:23 "folds of his flesh".; H0014 "be willing" filed under M30 because it appears as "would not" (1Ch 11:19; 2Sa 23:17 "he would not drink it"). It is kept only where it is the heart's or spirit's refusal (Exo 10:27; Deu 2:30; Eze 3:7).; "As you yourself live, I will not leave you" (2Ki 2:2, 4, 6; 4:30): an oath formula. H5800A "leave" → M30.; Gen 2:24 "leave … one flesh" → M30.
  verses: ["1Chr.11.19", "1Kgs.19.10", "1Kgs.19.14", "1Sam.20.1", "1Sam.23.15", "2Kgs.2.2", "2Kgs.2.4", "2Kgs.2.6", "2Kgs.4.30", "2Sam.18.3", "2Sam.23.17", "Deut.2.30", "Eccl.1.14", "Eccl.10.3", "Eccl.2.11", "Eccl.2.17", "Eccl.2.26", "Eccl.4.4", "Eccl.4.6", "Eccl.6.9", "Exod.10.27", "Exod.29.14", "Ezek.3.7", "Ezek.32.5", "Gen.1.21", "Gen.2.24", "Isa.57.15", "Jer.11.21", "Jer.19.7", "Jer.21.7", "Jer.22.25", "Jer.34.20", "Jer.34.21", "Jer.44.30", "Jer.46.26", "Jer.49.37", "Judg.9.2", "Lev.16.27", "Lev.8.17", "Matt.2.20", "Num.11.18", "Num.19.5", "Prov.10.13", "Prov.10.21", "Prov.11.12", "Prov.12.11", "Prov.15.21", "Prov.17.18", "Prov.24.30", "Prov.6.32", "Prov.7.7", "Prov.9.16", "Prov.9.4", "Ps.34.18", "Ps.35.4", "Ps.38.12", "Ps.40.14", "Ps.54.3", "Ps.63.9", "Ps.70.2", "Ps.86.14", "Rom.11.3"]
  nodes_here: 7
  nodes_elsewhere: 117
  collections: ["abase", "depart", "desire", "fill", "heart", "live", "repent", "search", "strive", "wise"]

## measured

- package_chars: 18320
- seconds: 0.01

## The answer form (fill it in the JSON file, `answer`)

```json
{
 "command": "ReadSweep",
 "collection": "strive",
 "subgroup": "exertion toward an end",
 "older": [
  {
   "observation": 16995,
   "action": "keep | delete_neither | defer",
   "nature": "evidence | inner_being",
   "reason": ""
  }
 ]
}
```
