# #2538: ReadWords — the instruction block and a real package (v1, 2026-11-25)

Written by Claude, session 760131f7, for the researcher's review before the next command (ReadSenses) is built.
- **The package:** [`2538-readwords-sample-package-v1-20261125.json`](2538-readwords-sample-package-v1-20261125.json), exactly as ReadWords writes it. It was made on a test copy of iba.db (the 12:34 named snapshot with the three #2538 migrations applied), for thought, subgroup "meditating and pondering". Nothing was written to the live database.
- **Size and time:** 43,334 characters (about 10,833 tokens at characters ÷ 4) and 0.16 s. It holds 12 words; 1 word is left for the next package.
- **Parts, in characters:** instruction 8,192, prompts 3,092, words 27,291, answer 4,519.

## 1. The instruction block

**What this read is.** Step S1, the words of one subgroup (stage 1, the lexical analysis): each word -- a surface with its lettered Strong's code -- read in the verse of each of its occurrences, for what it is and how it is used there. Nothing here says what a word does for the inner being; that begins at step 3.1.

**How to read.**
1. Take one word at a time, and within it one occurrence at a time, in the verse of that occurrence.
2. Read the evidence in this order: the verse text and the occurrence's stored structure (morph, unit, surface_kind, negator, party_kind, narrative); then the meaning sources for the code read together (sense_head, meaning_range, lsj, mounce), none picked and the others dropped; then the English rendering against the literal sense: does the English add or hide?
3. Judge the meaning in context from the Strong's code and the verse, not from the English surface alone. Where occurrences show different stems or voices, say whether the subject does, undergoes or causes the act.
4. The prompts are areas to explore; a prompt that does not apply is not answered.

**What to write.**
1. Fill `answer.rows`: for each word, its `readings`. One reading for each distinct way the word is used: the occurrences where it is used the same way are listed together in that reading's `occurrences` (occurrence ids or verse references); an occurrence used differently is its own reading.
2. kind: term; face where the use in a verse departs from the word's usual sense.
3. obs_text: concise; names the verse or verses; states what the word is and how it is used there (its object, setting, construction, what the morph shows); never the dictionary range, never the verse restated.
4. basis: stated (the verse says it) or read (read from the structure or the context). grounds: what in the verse shows it.
5. Every occurrence of the word is in exactly one reading; none is left out. A homonym or a name is recorded as such; a data error is named in grounds, not fixed.
6. `older`: the older observations on the word's occurrences. Read each with the word (they are what was recorded before) and answer each in the row's `older`, once: keep (with `nature` evidence or inner_being: it stands as it is); restate (with `nature`, `new_text` and `checked`: what in the base data the new text was checked against); merge (with `into`: a live observation saying the same); consume (with `carriers`, ["this"] for this row's readings or observation ids, and `mapping`: what the old one says and which carrier states each part); delete_neither (with `reason`: it is neither evidence nor inner being); carry (with `to` a later step, 1.1 or 2.1, and `reason`: what that step is to consider); defer (with `collection`, `nature` and `finding`: another collection owns the rest). An older observation listed under another word is answered there.
7. Then: Collection-Build.ps1 -Action RecordWords -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.

**The rules this read keeps** (text read live from `cfg_method_rule` when the package is made):

- **RG-08 the-original:** For every word that names an inner or bodily act, look at the original: the root's range in all three meaning sources read together, never one picked and the others dropped; the ESV renderings across its verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is open, record each, and mark the choice 'I read'.
- **RG-14 morph-read:** Morph is read, not carried: where occurrences of a word show different stems or voices, record whether the subject does, undergoes or causes the act.
- **RG-16 homonym-and-data-error:** A word that is only a homonym or a name, with no meaningful context, is recorded as such (tag no-human-context) and left. Data errors found while reading are flagged (tag data-error), not fixed in the reading.
- **RG-17 catalogue-as-prompts:** The question catalogue's questions are prompts for the areas to explore. A question that does not apply is not answered, and no answer is manufactured beyond what the verse shows.
- **RG-21 grain:** A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- **RG-22 content-words-carry-impact:** Content words carry the inner-being impact and are read even when no cluster tags them. Function words (particles, prepositions, conjunctions, suffixes, pronouns) get no observation of their own, except negators and connectives, which are read for what they do (RG-07). A T2 word never stands alone: it is read as the qualifier of what it binds to.
- **RW-03 no-duplicates-multi-node:** One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- **RW-04 concise-verse-specific:** Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- **RW-08 slants-own-rows:** Where the evidence points to more than one reading, each is its own observation with its own evidence.
- **RW-09 reread-builds-on-prior:** A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- **RW-13 older-observations-answered-at-record:** Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- **RS-04 existing-checked-accept-modify-delete:** When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- **VA-03 consumption-is-verified-before-deletion:** An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- **VA-04 neither-evidence-nor-inner-being-is-deleted:** An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.

**The prompts** (areas to explore; one that does not apply is not answered):

- **M0.1.1:** In this verse, looking at this specific occurrence (its surface form and morph_code), what does this term's name/form show about its essential nature here?
- **M0.1.2:** In this verse, drawing on this term's lexicon entries but grounded in how it is actually used in this occurrence, what does it mean at the definitional level?
- **M0.1.3:** In this verse, what directional, relational, or constitutional implication does this term's name carry as it functions in this specific occurrence?
- **M0.4.1:** What is the grammatical/stem form of this term in this verse?
- **M0.5.1:** In this verse, what does this term's root meaning show about how it operates in this specific occurrence?
- **M0.5.2:** In this verse, what does this occurrence's own grammatical form (per its morph_code — e.g. noun, verb, adjective, participle) show about how the term operates here?
- **M0.5.3:** In this verse, given this term's known semantic range — the breadth of meaning it can carry, including idiomatic, analogical, or combinatorial senses — where does this occurrence sit within that range, and what does that show about how the term operates here?
- **M0.5.4:** In this verse, does this occurrence express a specific aspect — disposition versus act, received versus given, condition versus quality? Record which, or none.
- **M0.5.5:** In this verse, among this term's own related terms, is there one that functions as this occurrence's structural opposite? Record it, or none.
- **M0.5.6:** In this verse, among this term's own related terms, is there a person-type term relevant to this occurrence — one for a person who habitually possesses or exercises it? Record it, or none.
- **M0.5.7:** In this verse, among this term's own related terms, is there a supplication or seeking term relevant to this occurrence — one for the act of seeking it from another? Record it, or none.
- **M0.5.8:** In this verse, does this term's Testament context (OT Hebrew vs. NT Greek) affect how this specific occurrence should be interpreted, and if so, how? Record none if the Testament context makes no interpretive difference here.
- **M0.5.9:** In this verse, if this term is newly coined in the NT period, what does that coinage show about how it functions in this occurrence? Record none if not applicable or not relevant to this occurrence.
- **M0.5.11:** In this verse, where this occurrence's meaning diverges from the term's usual sense elsewhere, what nuance does that divergence carry here, and how does it compare to the word's other occurrences? Pay particular attention to this occurrence's own surface form/rendering — a marked or atypical surface form is often the visible trace of the divergence itself, not a separate fact. Record none if this occurrence matches the term's usual sense.

## 2. One word as the package carries it: meditate | H7878

10 occurrences and 5 older observations. The other 11 words have the same form.

```json
{
 "ledger_id": 816,
 "word": "meditate",
 "strong": "H7878",
 "lexicon": {
  "sense_head": "to muse",
  "meaning_range": "1) to put forth, mediate, muse, commune, speak, complain, ponder, sing; 1a) (Qal); 1a1) to complain; 1a2) to muse, meditate upon, study, ponder; 1a3) to talk, sing, speak; 1b) (Polel) to meditate, consider, put forth thoughts",
  "lsj": "",
  "mounce": "",
  "related": [
   "H7808 שֵׂחַ thought",
   "H7879 שִׂיחַ complaint",
   "H7881 שִׂיחָה meditation"
  ]
 },
 "occurrences": [
  {
   "occurrence": 1263232,
   "reference": "Psa 77:3",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "When I remember God, I moan; when I meditate, my spirit faints. Selah"
  },
  {
   "occurrence": 1263242,
   "reference": "Psa 77:6",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "I said, “Let me remember my song in the night; let me meditate in my heart.” Then my spirit made a diligent search:"
  },
  {
   "occurrence": 1267517,
   "reference": "Psa 77:12",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "I will ponder all your work, and meditate on your mighty deeds."
  },
  {
   "occurrence": 1267534,
   "reference": "Psa 119:15",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "I will meditate on your precepts and fix my eyes on your ways."
  },
  {
   "occurrence": 1251807,
   "reference": "Psa 119:23",
   "morph": "HVqi3ms",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "Even though princes sit plotting against me, your servant will meditate on your statutes."
  },
  {
   "occurrence": 1266382,
   "reference": "Psa 119:27",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "Make me understand the way of your precepts, and I will meditate on your wondrous works."
  },
  {
   "occurrence": 1265205,
   "reference": "Psa 119:48",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "I will lift up my hands toward your commandments, which I love, and I will meditate on your statutes."
  },
  {
   "occurrence": 1263698,
   "reference": "Psa 119:78",
   "morph": "HVqi1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "Let the insolent be put to shame, because they have wronged me with falsehood; as for me, I will meditate on your precepts."
  },
  {
   "occurrence": 1267546,
   "reference": "Psa 119:148",
   "morph": "HVqcc",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "My eyes are awake before the watches of the night, that I may meditate on your promise."
  },
  {
   "occurrence": 1265917,
   "reference": "Psa 145:5",
   "morph": "HVqc1cs",
   "unit": "meditate",
   "surface_kind": "own",
   "negator": false,
   "party_kind": null,
   "narrative": null,
   "verse": "On the glorious splendor of your majesty, and on your wondrous works, I will meditate."
  }
 ],
 "older": [
  {
   "observation": 15122,
   "stage": "prior-capture",
   "kind": "statement",
   "nature": null,
   "text": "Psalm 119 gives one person's whole experience of the insolent: \"The insolent utterly deride me, but I do not turn away from your law\" (119:51); \"The insolent smear me with lies, but with my whole heart I keep your precepts; their heart is unfeeling like fat\" (119:69–70); \"they have wronged me with falsehood; as for me, I will meditate on your precepts\" (119:78); \"The insolent have dug pitfalls for me; they do not live according to your law\" (119:85); \"let not the insolent oppress me\" (119:122); The insolent wander from the commandments (119:21). Against them each time, the speaker holds the law, meditates, and asks for a pledge.",
   "verses": [
    "Ps.119.51",
    "Ps.119.69",
    "Ps.119.70",
    "Ps.119.78",
    "Ps.119.122",
    "Ps.119.21"
   ]
  },
  {
   "observation": 15920,
   "stage": "prior-capture",
   "kind": "statement",
   "nature": null,
   "text": "Fainting across every component: heart: \"the whole heart faint\" // \"the whole head is sick\" (Isa 1:5); Lam 1:22; Psa 61:2; spirit [H]: Psa 142:3; 143:4; \"When I remember God, I moan; when I meditate, my spirit faints\" (Psa 77:3); soul: \"hungry and thirsty, their soul fainted within them\" (Psa 107:5); flesh: \"my flesh faints for you\" (Psa 63:1); life: \"When my life was fainting away, I remembered the Lord, and my prayer came to you\" (Jon 2:7) — fainting turns into remembering and prayer; Revisit 2026-09-28: In the same book, Jonah \"was faint\" under the east wind and asked to die (Jon 4:8). Fainting in ch. 2 turns to prayer; fainting in ch. 4 turns to a death-wish (Batch G §6).; For spirit-fainting in meditation (Psa 77:3), memory works either way: it deepens the fainting (Psa 77) or turns it (Psa 42:6). See Batch F §9.4.; bosom: \"their life is poured out on their mothers' bosom\" (Lam 2:12)",
   "verses": [
    "Isa.1.5",
    "Lam.1.22",
    "Ps.61.2",
    "Ps.142.3",
    "Ps.143.4",
    "Ps.77.3",
    "Ps.107.5",
    "Ps.63.1",
    "Jonah.2.7",
    "Jonah.4.8",
    "Lam.2.12"
   ]
  },
  {
   "observation": 15954,
   "stage": "prior-capture",
   "kind": "statement",
   "nature": null,
   "text": "Inner inquiry in sequence: \"let me meditate in my heart.' Then my spirit made a diligent search\" (Psa 77:6). The heart meditates, then the spirit searches.",
   "verses": [
    "Ps.77.6"
   ]
  },
  {
   "observation": 16012,
   "stage": "prior-capture",
   "kind": "statement",
   "nature": null,
   "text": "Remembering and the spirit: \"When I remember God, I moan; when I meditate, my spirit faints\" (Psa 77:3); \"Let me remember my song … meditate in my heart. Then my spirit made a diligent search\" (Psa 77:6) [H].",
   "verses": [
    "Ps.77.3",
    "Ps.77.6"
   ]
  },
  {
   "observation": 17569,
   "stage": "prior-capture",
   "kind": "statement",
   "nature": null,
   "text": "Psa 119:24. *\"Your testimonies are my delight; they are my counselors.\"* The verse before reads: *\"Even though princes sit plotting against me, your servant will meditate on your statutes\"* (119:23).",
   "verses": [
    "Ps.119.24",
    "Ps.119.23"
   ]
  }
 ]
}
```

## 3. The answer the reader fills (this word's row)

```json
{
 "ledger_id": 816,
 "word": "meditate|H7878",
 "readings": [
  {
   "kind": "term | face",
   "obs_text": "",
   "basis": "stated | read",
   "grounds": "",
   "occurrences": []
  }
 ],
 "older": [
  {
   "observation": 15122,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  },
  {
   "observation": 15920,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  },
  {
   "observation": 15954,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  },
  {
   "observation": 16012,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  },
  {
   "observation": 17569,
   "action": "keep | restate | merge | consume | delete_neither | defer | carry",
   "reason": ""
  }
 ]
}
```

## 4. Tested

The test plan (`iba/app/tools/temp_2538_readwords_test_run.py`, on a copy) passes 26 of 26 cases. The real answer recorded in case R19 is the live reading of these 13 words, with the 20 live answers to their older observations; every word is validated. The run took 2.4 s.
