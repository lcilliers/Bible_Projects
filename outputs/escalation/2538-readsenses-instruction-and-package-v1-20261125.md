# #2538: ReadSenses — the instruction block and a real package (v1, 2026-11-25)

Written by Claude, session 760131f7, for the researcher's review before the next command (ReadEnrichment, step 1.2) is built.
- **The package:** [`2538-readsenses-sample-package-v1-20261125.json`](2538-readsenses-sample-package-v1-20261125.json), exactly as ReadSenses writes it. It was made on a test copy of iba.db (the 12:34 named snapshot with the #2538 migrations, S1 of "meditating and pondering" recorded on the copy by ReadWords with the live reading). Nothing was written to the live database.
- **Size and time:** 19,524 characters (about 4,881 tokens at characters ÷ 4) and 0.1 s. The whole subgroup is one package: each occurrence goes into exactly one sense, so the read cannot be split.
- **What it holds:** 14 B1 observations on 28 occurrences, 1 occurrence in no reading (a function word of a phrase surface), 11 codes, 2 older observations.
- **Parts, in characters:** instruction 8,296, prompts 2, readings 6,662, occurrences_in_no_reading 115, codes 3,108, older 532, answer 475.
- **Every subgroup of thought, measured on a copy of live (data only, before the instruction):** meditating and pondering 9.9k; reasoning 17.2k; weighing and taking account of 39.6k; supposing and imagining 12.0k; thinking and thought 68.1k; the five one-word subgroups 0.8k to 1.8k. The largest package is about 80k characters (20k tokens); the limit is set at 100,000.

## 1. The instruction block

**What this read is.** Step 1.1, the senses of one subgroup (stage 1, B2): the word readings of step S1 gathered into senses by meaning in context. A sense is one meaning, of one or several surfaces and codes. Nothing here says what a sense does for the inner being; that begins at step 3.1.

**How to read.**
1. Read every B1 observation of the subgroup (`readings`: what each word is and how it is used in its verses, with the occurrences it holds), with the sense head and meaning range of each code (`codes`).
2. Gather by meaning in context: the readings, of any surface and any Strong's code of the subgroup, whose meaning in context is the same are one sense. The same surface may carry different senses; different surfaces may carry one. The grouping rests on the Strong's code, the lexicon and the verse, not on the English surface alone.
3. The subgroup shows words that may relate to each other and differentiate or accentuate senses. Each sense is named for its meaning.
4. Read the older observations (`older`) with the readings: one carried here from S1, or one that states what a sense is, is considered first, for correction rather than a new observation.

**What to write.**
1. Fill `answer.senses`, one entry for each sense. `carries`: the ids of the B1 observations it gathers; each B1 observation is carried by one sense. Where one B1 observation holds occurrences of two senses, leave it out of `carries` and name its occurrences (occurrence ids) in each sense's `occurrences`. Together every occurrence of the subgroup is in exactly one sense; an occurrence no reading holds (`occurrences_in_no_reading`) is named in a sense's `occurrences`.
2. kind: group. obs_text: names the sense and its meaning and names verses it holds in, as the package writes the references (for example Psa 77:6); concise; never the dictionary range copied, never a verse restated, never what the sense does for the inner being.
3. basis: read, with `grounds`: words copied exactly from the sense_head or the meaning_range of a code of the sense (the record checks them against the lexicon); or stated, where a verse says it.
4. A surface that fits no sense is not forced into one: stop and raise it; it goes back to the grouping (Step 2) with its reason.
5. `older`: answer each older observation shown, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` ["this"] for this answer's senses or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` 2.1 and `reason`), defer (with `collection`, `nature`, `finding`).
6. Then: Collection-Build.ps1 -Action RecordSenses -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.

**The rules this read keeps** (text read live from `cfg_method_rule` when the package is made):

- **RG-08 the-original:** For every word that names an inner or bodily act, look at the original: the root's range in all three meaning sources read together, never one picked and the others dropped; the ESV renderings across its verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is open, record each, and mark the choice 'I read'.
- **RG-15 difference-own-observation:** A difference, or a specific inference, is its own observation, never folded into another.
- **RG-21 grain:** A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- **RO11 one-row-per-code:** One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- **RW-03 no-duplicates-multi-node:** One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- **RW-04 concise-verse-specific:** Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- **RW-08 slants-own-rows:** Where the evidence points to more than one reading, each is its own observation with its own evidence.
- **RW-09 reread-builds-on-prior:** A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- **RW-13 older-observations-answered-at-record:** Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- **RS-04 existing-checked-accept-modify-delete:** When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- **LR-02 nodes-are-built-from-the-data:** The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
- **VA-03 consumption-is-verified-before-deletion:** An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- **VA-04 neither-evidence-nor-inner-being-is-deleted:** An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.

## 2. The data, as the package carries it

**Two B1 readings** (of 14):

```json
[
 {
  "observation": 22673,
  "words": [
   "meditates|H1897"
  ],
  "kind": "term",
  "text": "In Psa 1:2 'meditates' is the steady murmuring over the law of the Lord, day and night: the delight of the person is taken up with it in repeated, low recitation and thought. The object is God's law and the time is the whole day and night.",
  "basis": "read",
  "grounds": "he meditates day and night",
  "occurrences": [
   {
    "occurrence": 1264096,
    "reference": "Psa 1:2"
   }
  ]
 },
 {
  "observation": 22674,
  "words": [
   "meditate|H1897"
  ],
  "kind": "term",
  "text": "In Jos 1:8, Psa 63:6 and Psa 143:5 'meditate' is to murmur over and turn over in thought what belongs to God: the Book of the Law in Joshua, God himself on the bed at night in Psa 63:6, and God's deeds in Psa 143:5. Jos 1:8 ties it to doing what is written.",
  "basis": "read",
  "grounds": "meditate on all that you have done",
  "occurrences": [
   {
    "occurrence": 1267554,
    "reference": "Psa 143:5"
   },
   {
    "occurrence": 1098636,
    "reference": "Jos 1:8"
   },
   {
    "occurrence": 1270659,
    "reference": "Psa 63:6"
   }
  ]
 }
]
```

**The occurrence in no reading:**

```json
[
 {
  "occurrence": 1264936,
  "reference": "Psa 104:34",
  "word": "meditation|H5921A",
  "readings_in_the_verse": [
   22680
  ]
 }
]
```

**Two codes** (of 11):

```json
{
 "G1760": {
  "surfaces": [
   "pondering"
  ],
  "sense_head": "to reflect on",
  "meaning_range": "to think, ponder, reflect; <b>to revolve thoroughly in the mind, consider carefully, ponder, reflect,</b> <ref='Act.10.19'>Acts 10:19</ref>*"
 },
 "G4820": {
  "surfaces": [
   "pondering"
  ],
  "sense_head": "to ponder/confer",
  "meaning_range": "to dispute with; to confer with, meet with; to ponder; to engage in (war); (<i>middle</i>) to help, assist; <i>primarily</i> <b>to throw together;</b> <i>absolute</i> <b>to meet and join,</b> <ref='Act.20.14'>Acts 20:14;</ref> <b>to meet</b> in war, <b>to encounter, engage with,</b> <ref='Luk.14.31'>Lk. 14:31</ref>; <b>to encounter</b> in discourse or dispute, <ref='Act.17.18'>Acts 17:18;</ref> <b>to consult together,</b> <ref='Act.4.15'>Acts 4:15;</ref> <i>middle</i> <b>to contribute, be of ser"
 }
}
```

**The older observations:**

```json
[
 {
  "observation": 12418,
  "stage": "strand-reading",
  "kind": "key-statement",
  "nature": null,
  "text": "hāgāh joins meditating, muttering and uttering in one word.",
  "verses": [
   "Ps.1.2",
   "Josh.1.8",
   "Ps.37.30",
   "Prov.8.7",
   "Job.27.4",
   "Isa.59.3",
   "Isa.59.13",
   "Prov.24.2",
   "Ps.2.1",
   "Ps.38.12"
  ]
 },
 {
  "observation": 20463,
  "stage": "prior-capture",
  "kind": "statement",
  "nature": null,
  "text": "meditate / meditation / muse | H1897 *hāgāh*, H7878 *śîaḥ*, H1902 *higgāyôn* | Ps 19:14 | Thought as inner murmuring",
  "verses": [
   "Ps.19.14"
  ]
 }
]
```

## 3. The answer the reader fills

```json
{
 "command": "ReadSenses",
 "collection": "thought",
 "subgroup": "meditating and pondering",
 "ledger_id": 846,
 "senses": [
  {
   "kind": "group",
   "obs_text": "",
   "basis": "read | stated",
   "grounds": "",
   "carries": [],
   "occurrences": []
  }
 ],
 "older": [
  {
   "observation": 12418,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  },
  {
   "observation": 20463,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  }
 ]
}
```

## 4. Tested

`iba/app/tools/temp_2538_readsenses_test_run.py`, on a copy after the ReadWords test: 26 of 26 cases pass, in 1.0 s. The real answer recorded is the live 1.1 reading of this subgroup: 8 senses, seven of them carrying 13 of the 14 B1 observations whole and one B1 observation split between two senses by its occurrences, with the 2 live answers to the older observations. The row is validated, every sense is marked evidence, every B1 observation is traced, and the next command named is ReadEnrichment. Refused whole, with nothing written: a wrong command, another row, a carried id that is not a B1 observation, one B1 observation carried twice, one carried by no sense, grounds not in the lexicon, older observations unanswered.
