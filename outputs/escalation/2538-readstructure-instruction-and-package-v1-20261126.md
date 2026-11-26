# #2538: ReadStructure — the instruction block and two real packages (v1, 2026-11-26)

Written by Claude, session 760131f7, for the researcher's review before the next command (ReadSweep, B4) is built.
- **The packages**, exactly as ReadStructure writes them, for thought, subgroup "reasoning", made on a test copy: the named snapshot pre-2538-findings-apply with every #2538 migration applied (#2568), and S1, 1.1 and 1.2 of "reasoning" recorded on the copy from the live readings. Nothing was written to the live database.
  - [`2538-readstructure-sample-package-double-meaning-v1-20261126.json`](2538-readstructure-sample-package-double-meaning-v1-20261126.json): the first package, 3 double-meaning rows, 36 verses, 54,001 characters, 0.09 s. Parts: instruction 9,704, senses 2,891, verses 34,676, rows 5,665, answer 801.
  - [`2538-readstructure-sample-package-pairing-v1-20261126.json`](2538-readstructure-sample-package-pairing-v1-20261126.json): the first pairing package, 15 rows (one for each partner collection), 14 verses, 50,936 characters, 0.01 s. Parts: instruction 9,704, senses 2,891, verses 16,343, rows 17,581, answer 4,159.
- **How the 66 rows of "reasoning" go out:** one item at a time, in 9 packages: double-meaning (3 rows), qualifier (1), entity (1), direction (1), then pairing in five packages (15, 15, 15, 13, 2 rows). Every package is between 20,000 and 58,312 characters (limit 60,000), each made in under 0.1 s. A row sent and not answered is sent again only when every open row has been sent; `-Item` picks an item.
- **The verses are given once per package**, compactly: one line for each word of the verse, from the stored structure (position, surface, Strong's code, morph, then what the pairing makes of it). A `*` marks the subgroup's own words. The loader's full form of the verses of "reasoning" is 120,466 characters; this is how the package stays small.

## 1. The instruction block

**What this read is.** Step 2.1, the structure of one subgroup (stage 1, B3): what stands with the subgroup's words in each verse, read from the stored structure. One item at a time: double-meaning (a surface with more than one code), qualifier (negators and the word each reaches, adjectives, adverbs, prepositional qualifiers), entity (who is named or referred to), direction (from whom to whom, by the grammar), pairing (one row for each partner collection: its words in the verses shared with the subgroup). Nothing here says what anything does for the inner being; that begins at step 3.1.

**How to read.**
1. Take one row at a time (`rows`): what it asks, its occurrences (`as`: member, the subgroup's word; partner, the other word), and its verses.
2. Read each verse (`verses`) from its stored structure, one line for each word: * marks an occurrence of the subgroup; then the position, surface, Strong's code and morph, and what the pairing makes of the word (its type, the qualifier it carries, a negator, a party, the collections of a word of another collection). Nothing is evaluated that is not stored.
3. Where each word stands: its side and distance from the subgroup's word, from the positions. Adjacency is not scope: a negator or qualifier is read for the word it reaches by the grammar.
4. A pairing row shows the WordNet control for its partner collection: a pairing WordNet gives and the verses do not show is one to look for; a pairing only the verses show has no control.
5. Differences in meaning are read from the base data (the Strong's code, the morph, the construction), not from the English alone. The subgroup's 1.1 senses (`senses`) are what the findings build on.

**What to write.**
1. Fill `answer.rows`: for each row, disposition observed with its `findings`, or none with its `reason` (where the row allows none: nothing of the item stands with the subgroup in its verses).
2. One finding for each distinct thing the structure shows; the same finding in several verses is ONE finding naming all its occurrences; a verse that shows something different is its own finding. Together the findings name every occurrence of the row (occurrence ids or verse references), each in one finding.
3. kind: as the template gives it (pairing; relation for direction; face for double-meaning). obs_text: concise; names the verses it holds in, as the package writes the references (for example Act 18:4); states what the structure shows (which word, where it stands, what it reaches or gives by the grammar); never a verse restated, never what it does for the inner being.
4. basis: stated (the verse says it) or read (read from the structure), with `grounds`: words copied exactly from the verses it is tied to (the record checks them).
5. Each subgroup's surface has its own finding; none joins two subgroups. A data error is named in grounds, not fixed.
6. `older`: answer each older observation shown under the row, once: keep (with `nature`), restate (with `nature`, `new_text`, `checked`), merge (with `into`), consume (with `carriers` ["this"] or observation ids, and `mapping`), delete_neither (with `reason`), carry (with `to` and `reason`), defer (with `collection`, `nature`, `finding`). One listed under another row is answered there.
7. Then: Collection-Build.ps1 -Action RecordStructure -File <the answer file> (-Check to preview). The record refuses the whole file on any fault and lists every fault.

**The rules this read keeps** (text read live from `cfg_method_rule` when the package is made):

- **RG-14 morph-read:** Morph is read, not carried: where occurrences of a word show different stems or voices, record whether the subject does, undergoes or causes the act.
- **RG-16 homonym-and-data-error:** A word that is only a homonym or a name, with no meaningful context, is recorded as such (tag no-human-context) and left. Data errors found while reading are flagged (tag data-error), not fixed in the reading.
- **RG-21 grain:** A word is read per its lettered Strong's code (its grain), never the bare lemma (B:113). The occurrences of a word with several senses are related per grain and never aggregated across grains: related verses are same-grain occurrences.
- **RO11 one-row-per-code:** One observation per finding, never a duplicate description; a finding applying to several verses or words carries several nodes, each with the word's role in it.
- **RW-03 no-duplicates-multi-node:** One observation per finding: the same description is never written twice. Applied to another verse, word or scope it gains a node on the existing observation.
- **RW-04 concise-verse-specific:** Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss.
- **RW-08 slants-own-rows:** Where the evidence points to more than one reading, each is its own observation with its own evidence.
- **RW-09 reread-builds-on-prior:** A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them.
- **RW-11 missing-is-named:** Missing data in the base extract is named as a gap, never substituted from memory or outside knowledge.
- **RW-13 older-observations-answered-at-record:** Every older live observation with a live node on an occurrence of the row (a stage that is not the build's own) is answered in fill.older when the row is recorded, once: keep or restate (each with its marker), merge into a named observation, consume (live observations carry its meaning, stated in words, verified before it is deleted), delete as neither (comment first), or defer to a named collection (marked now; only the finding is left to that collection). An observation already marked by the validation, answered in a build or deferred is not asked again. A new observation whose text equals that of another live observation of the collection is refused, the other named. LayerCheck re-derives both from the tables. The end state of a collection's build is that every observation of its scope is marked and fixed or deleted, every word node complete or with its reason, and each deferral owned by a named collection.
- **RS-04 existing-checked-accept-modify-delete:** When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and need no separate approval. Nothing is physically deleted.
- **LR-02 nodes-are-built-from-the-data:** The nodes of a layer observation are the occurrences the aspect demands (a word's occurrences, the group's occurrences, the partner's occurrences in the verses they share), written by the recorder with the collection and the subgroup of each surface; they are never typed. An item answered by senses (word-sense) names, for each sense, the occurrences it holds for, and together the senses cover every occurrence; the recorder checks them against the data. The interpretation is the observation text, founded in what the evidence shows (basis stated or read, B:131) and tied to its verses (the text names them and does not restate them): the items of every step (S1, 1.1, 1.2, 2.1) state what the dictionary, the verses and the stored structure show of a word and never what a word does for the inner being; their nodes carry the role lexical and no route. The whole file is checked and written in one transaction; any problem refuses all of it. A row answered again withdraws its earlier observations with the reason.
- **LR-03 none-needs-a-permitted-reason:** An aspect is recorded as none only where its item allows it (cfg_setting layer.reading none_allowed) and with its reason in words. A group definition and a group's Strong's enrichment are always observed.
- **DA-02 a-node-per-occurrence-with-its-surfaces-collection:** A node is on one occurrence (verse_lexical_id) and carries the collection of its surface (a supportive node, the collection of the surface it supports); a node already on the observation for the same occurrence is not written twice, and takes the role. A node with no collection to carry, or on a verse out of scope (B:130), is not written and is listed.
- **VA-03 consumption-is-verified-before-deletion:** An older observation is deleted as consumed only when live observations carry its meaning: every word occurrence of it is on a live node of a carrier or named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed or replaced, and the consumption is kept as `consumed_by`. An observation that holds more than one finding is split first.
- **VA-04 neither-evidence-nor-inner-being-is-deleted:** An observation that is neither evidence nor inner being contributes nothing to the purposes of the observations (researcher, 2026-11-22): it is commented with its reason and the word occurrences no other live observation holds, then deleted. An observation already marked, or one another observation traces, is not deleted this way.

## 2. The data, as the package carries it

**One pairing row:**

```json
{
 "ledger_id": 847,
 "item": "pairing",
 "subject": "abase",
 "asks": "Which words of this partner collection stand with the subgroup's surfaces in the verses they share, where does each stand (side and distance, from the stored structure), and which stand out? The WordNet control for this collection is shown. Write one finding for each distinct thing the structure shows; a finding holds the verses it holds in as its nodes.",
 "none_allowed": true,
 "verses": [
  "Dan 4:34"
 ],
 "occurrences": [
  {
   "occurrence": 1383059,
   "reference": "Dan 4:34",
   "surface": "reason",
   "strong": "H4486",
   "as": "member"
  },
  {
   "occurrence": 1383053,
   "reference": "Dan 4:34",
   "surface": "lifted",
   "strong": "H5191",
   "as": "partner"
  }
 ],
 "older": [],
 "wordnet_control": "WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)"
}
```

**One verse, with its structure lines:**

```json
{
 "reference": "Dan 4:34",
 "text": "At the end of the days I, Nebuchadnezzar, lifted my eyes to heaven, and my reason returned to me, and I blessed the Most High, and praised and honored him who lives forever, for his dominion is an everlasting dominion, and his kingdom endures from generation to generation;",
 "words": [
  " 0 at H9005 AR",
  " 1 end H7118 ANcbsc",
  " 1 and H9002 AC | connective",
  " 2 days H3118 ANcmpd",
  " 2 [the] H9010 ATa",
  " 3 i H0576B APp1bs",
  " 4 nebuchadnezzar H5020 ANpm | entity (human); party human",
  " 5 lifted H5191 AVqp1cs | word of another collection; collections abase",
  " 5 [the] H9010 ATa",
  " 6 eyes H5870 ANcmpc",
  " 7 heaven H8065 ANcmpd",
  " 7 to/for H9005 AR",
  " 7 my H9020 ASp1bs",
  "*8 reason H4486 ANcbsc | member of this collection",
  " 8 and H9002 AC",
  " 9 returned H8421G AVqi3ms | word of another collection; collections return",
  " 9 me H9030 ASp1bs",
  " 10 to H5922 AR",
  " 10 my H9020 ASp1bs",
  " 11 blessed H1289 AVpp1cs | word of another collection; collections bless",
  " 11 [the] H9010 ATa",
  " 12 most high H5943 AAabsd | qualifier candidate; qualifier morph: adjective",
  " 12 and H9002 AC | connective",
  " 12 to/for H9005 AR",
  " 13 praised H7624 AVpp1cs | word of another collection; collections commend",
  " 13 [the] H9010 ATa",
  " 14 honored H1922 AVpp1cs | word of another collection; collections honor",
  " 15 lives H2417 AAabsc | word of another collection; qualifier morph: adjective; collections live",
  " 15 and H9002 AC | connective",
  " 15 to/for H9005 AR",
  " 16 forever H5957 ANcbsd | qualifier candidate; qualifier qualifier subgroup: Forever, ever, always (a quality of time)",
  " 17 dominion H7985 ANcbsc",
  " 17 dominion H1768 AC | connective",
  " 18 everlasting H5957 ANcbsa | word of another collection; qualifier qualifier subgroup: Forever, ever, always (a quality of time); collections continual",
  " 19 dominion H7985 ANcbsc",
  " 19 his H9023 ASp3ms",
  " 20 kingdom H4437 ANcfsc",
  " 20 and H9002 AC | connective",
  " 21 endures from H5974 AR",
  " 21 his H9023 ASp3ms",
  " 22 generation H1859 ANcbsa",
  " 23 generation H1859 ANcbsa",
  " 23 and H9002 AC | connective"
 ]
}
```

## 3. Claude's reading of the double-meaning package (the test's real answer)

No 2.1 reading is recorded live, so the test records this reading of the first package. Each surface of the subgroup with more than one code has one face observation, holding all its occurrences, specification v5 section 3:

- **reason** (basis read; grounds "let us reason together"): The surface reason renders eighteen codes. As a noun of the mind it is G3056 in 1Pe 3:15 (an account given), H4486 in Dan 4:34 and Dan 4:36 (understanding restored) and G2138 in Jam 3:17 (open to persuasion); as a verb it is H3198 in Isa 1:18 (to argue a case together). Elsewhere it is part of a phrase of cause: H6440I in Gen 41:31, H5921A, H1697M, H3651C, G1223, G5124, G0156, G2596, G0302, G1352, G5484, G1519 and H1961, and H2600 in Job 1:9 for without cause.
- **reasoned** (basis read; grounds "I reasoned like a child"): The surface reasoned carries two codes: G1256 in Act 17:2, Act 17:17, Act 18:4, Act 18:19 and Act 24:25, where Paul discourses with others, and G3049 in 1Co 13:11, where a child reckons for himself.
- **reasoning** (basis read; grounds "the reasoning of their hearts"): The surface reasoning carries two codes: G1261 in Luk 9:47, the reasoning held within the hearts of the disciples, and G1256 in Act 19:8 and Act 19:9, where Paul argues with others in the synagogue and the hall of Tyrannus.

## 4. Tested

`iba/app/tools/temp_2538_readstructure_test_run.py`, on a copy: 27 of 27 pass, in 1.0 s. Among the cases:
- every row carries exactly the occurrences the recorder demands;
- every verse of the rows is in the package once, with its text and structure lines;
- the nine packages carry all 66 rows once, each within the limit;
- `-Item pairing` gives pairing rows, each with its WordNet control;
- the reading above is recorded: three face observations, every row validated, every finding marked evidence and traced to a 1.1 sense, and the next command named ReadStructure while 63 rows are open;
- refused whole, with nothing written: a wrong command, a foreign row, a bad disposition, none without its reason, an occurrence left out, grounds not in the verses, and a text naming none of its verses.

**Found and fixed in the test.**
- The size limit at first left out the instruction, the senses and the answer template; it now counts them.
- A subgroup word with no pairing in its verse ("reason", G5484, in Eph 3:14) lacked its `*`; the mark now comes from the subgroup's occurrences.
