# #2538: ReadEnrichment — the instruction block and a real package (v1, 2026-11-26)

Written by Claude, session 760131f7, for the researcher's review before the next command (ReadStructure, step 2.1) is built.
- **The package:** [`2538-readenrichment-sample-package-v1-20261126.json`](2538-readenrichment-sample-package-v1-20261126.json), exactly as ReadEnrichment writes it, for thought, subgroup "reasoning" (the one subgroup with a 1.2 reading recorded live to test against). It was made on a test copy (the named snapshot pre-2538-findings-apply with the #2538 migrations, S1 and 1.1 of "reasoning" recorded on the copy from the live readings). Nothing was written to the live database.
- **Size and time:** 35,765 characters (about 8,941 tokens at characters ÷ 4) and 0.1 s: 7 senses, 21 codes, 41 occurrences, 0 older observations.
- **Parts, in characters:** instruction 7,667, prompts 2, senses 3,671, occurrences_in_no_sense 2, codes 23,299, older 2, answer 806. The lexicon of the codes is most of it: this read is about the lexicon.
- **Every subgroup of thought, measured on a copy of live:** the largest package, "thinking and thought", is about 95,000 characters; "weighing and taking account of" about 57,000; the five one-word subgroups about 9,000 to 11,000. The limit is 110,000.

## 1. The instruction block

**What this read is.** Step 1.2, the enrichment of one subgroup (stage 1, B2): for each sense of step 1.1, what the Strong's codes of its occurrences say. The lexicon is the point of this read. Nothing here says what a sense does for the inner being; that begins at step 3.1.

**How to read.**
1. Take one sense at a time (`senses`: its text from step 1.1, its codes, words and occurrences).
2. Read the lexicon of each of its codes (`codes`: sense_head, meaning_range, lsj, mounce, related), the three meaning sources read together, none picked and the others dropped.
3. Validate the sense against its codes: do the lexicon entries bear out the meaning the sense names? Where they do not, say so in the enrichment; the sense is not changed here.
4. Where one surface carries several codes in the sense, read what each code adds.

**What to write.**
1. Fill `answer.enrichments`: one entry for each sense, named by `sense` (the id of its 1.1 observation); every sense has exactly one. The enrichment takes the sense's occurrences.
2. kind: enrichment. obs_text: a short definition from the lexicon entries; names the codes that link the sense to its usage and what different codes of one surface add; names verses the sense holds in, as the package writes the references (for example Psa 77:6); concise; never the lexicon copied whole, never a verse restated, never what the sense does for the inner being.
3. basis: read, with `grounds`: words copied exactly from the lexicon of a code of the sense (sense_head, meaning_range, lsj or mounce; the record checks them); or stated, where a verse says it.
4. Where the lexicon does not bear out the sense, the enrichment says so with its grounds; a missing lexicon entry is named, never filled from memory (RW-11).
5. `older`: answer each older observation shown, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` ["this"] for this answer's enrichments or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` 2.1 and `reason`), defer (with `collection`, `nature`, `finding`).
6. Then: Collection-Build.ps1 -Action RecordEnrichment -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.

**The rules this read keeps** (text read live from `cfg_method_rule` when the package is made):

- **RG-08 the-original:** For every word that names an inner or bodily act, look at the original: the root's range in all three meaning sources read together, never one picked and the others dropped; the ESV renderings across its verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is open, record each, and mark the choice 'I read'.
- **RG-21 grain:** A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- **RO11 one-row-per-code:** One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- **RW-03 no-duplicates-multi-node:** One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- **RW-04 concise-verse-specific:** Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- **RW-09 reread-builds-on-prior:** A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- **RW-11 missing-is-named:** Missing data in the base extract is named as a gap, never substituted from memory or outside knowledge.
- **RW-13 older-observations-answered-at-record:** Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- **RS-04 existing-checked-accept-modify-delete:** When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- **LR-02 nodes-are-built-from-the-data:** The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
- **VA-03 consumption-is-verified-before-deletion:** An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- **VA-04 neither-evidence-nor-inner-being-is-deleted:** An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.

## 2. The data, as the package carries it

**One sense** (of 7):

```json
{
 "sense": 22688,
 "text": "Reasoning as argument put to other people: Paul reasons with Jews and others in the synagogue, the market and the hall of Tyrannus and before Felix, and the Lord invites the people to argue the case out together. The word is spoken argument with a hearer and a matter, aimed at persuading or setting right; the Greek verb is of discourse and the Hebrew verb of arguing a case. Verses: Act 17:2, Act 17:17, Act 18:4, Act 18:19, Act 24:25, Act 19:8, Act 19:9, Isa 1:18.",
 "codes": [
  "G1256",
  "H3198"
 ],
 "words": [
  "reasoned|G1256",
  "reasoning|G1256",
  "reason|H3198"
 ],
 "occurrences": [
  "Act 19:8",
  "Act 24:25",
  "Isa 1:18",
  "Act 19:9",
  "Act 17:17",
  "Act 17:2",
  "Act 18:4",
  "Act 18:19"
 ]
}
```

**The lexicon of its first code:**

```json
{
 "G1256": {
  "surfaces": [
   "reasoned",
   "reasoning"
  ],
  "sense_head": "to dispute",
  "meaning_range": "to reason, discuss, discourse; to argue, dispute; <b>to discourse, argue, reason,</b> <ref='Act.17.2, 17; 24.12'>Acts 17:2, 17; 24:12</ref>; <b>to address, speak to,</b> <ref='Heb.12.5'>Heb. 12:5;</ref> <b>to contend, dispute,</b> <ref='Mrk.9.34'>Mk. 9:34</ref>; Jude 9",
  "lsj": "<b> διαλέγω</b>, <br /> <b>pick out,</b> [<a href=\"javascript:void(0)\" title=\" 5th c.BC: Herodotus Historicus 8.107, 113, 5th-6th c.BC: Xenophon Historicus “Oeconomicus” 8.9, etc.\">Refs 5th c.BC+</a>]; πτῶμα <b>glean</b> fallen olives, [<a href=\"javascript:void(0)\" title=\" “PFay.” 102.20 \">Refs</a>]; compare διαλέγειν· ἀνακαθαίρειν, [<a href=\"javascript:void(0)\" title=\" 5th c.AD(?): Hesychius Legal icographus \">Refs 5th c.AD+</a>]; <b>select, separate,</b> [<a href=\"javascript:void(0)\" title=\" 5th-6th c.BC: Plato Philosophus “Leges” 735b \">Refs 5th c.BC+</a>]; <b>examine, check</b> documents, [<a href=\"javascript:void(0)\" title=\" “PFay.” 11.26 (2nd c.BC), etc. \">Refs 2nd c.BC+</a>]<br /><Lev",
  "mounce": "to reason, discuss, discourse; to argue, dispute",
  "related": [
   "G0483 ἀντιλέγω to dispute",
   "G0557 ἀπελεγμός discredit",
   "G1223 διά through/because of",
   "G1246 διακατελέγχομαι to refute",
   "G1258 διάλεκτος language",
   "G1649 ἔλεγξις rebuke",
   "G1650 ἔλεγχος rebuke",
   "G1651 ἐλέγχω to rebuke",
   "G1827 ἐξελέγχω to convict",
   "G1951 ἐπιλέγω to call/choose",
   "G2639 καταλέγω to enrol",
   "G3004G λέγω to say: says"
  ]
 }
}
```

## 3. The answer the reader fills

```json
{
 "command": "ReadEnrichment",
 "collection": "thought",
 "subgroup": "reasoning",
 "ledger_id": 846,
 "enrichments": [
  {
   "sense": 22688,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 22689,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 22690,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 22691,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 22692,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 22693,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  },
  {
   "sense": 22694,
   "kind": "enrichment",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": ""
  }
 ],
 "older": []
}
```

## 4. Tested

`iba/app/tools/temp_2538_readenrichment_test_run.py`, on a copy after the words and senses test plans for "reasoning" (26 of 26 each): 24 of 25 pass, the 25th blocked because "reasoning" has no older observation at 1.2 (the refusal of unanswered older observations is proven at S1 and 1.1). The real answer recorded is the live 1.2 reading of "reasoning", each enrichment matched to its sense by the occurrences it holds: the row validated, every enrichment marked evidence, every sense traced, every code with a node, the next command named ReadStructure. Refused whole, with nothing written: a wrong command, another row, an unknown sense, a sense enriched twice, a sense left without its enrichment, grounds not in the lexicon.

**Found and fixed in the test.** A 1.1 sense of the group that "reasoning" replaced (observation 22308, ledger row 574 of the deleted group 13) was still live on the test copy, because a step opened for one subgroup never retires the rows of groups that no longer exist; it was taken as one of the subgroup's senses. `layerreading.trace_targets` now leaves out the observations of rows of a deleted or retired group. On live that observation is already deleted; LayerCheck on a copy of live validates the same 188 of 195 rows before and after the change, and the loop-order test passes 8 of 8.
