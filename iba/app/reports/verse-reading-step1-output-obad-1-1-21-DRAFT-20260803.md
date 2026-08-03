# Step 1 draft output — verse reading (lexical, isolated) — Obadiah 1:1-21

> DRAFT. Not written to DB — no table/format has been approved yet (see [verse-reading-step1-format-draft-20260803.md](verse-reading-step1-format-draft-20260803.md)). Every record below was built strictly from that single verse's own span/meaning_tree entries in `obad-1-verse-span-meaning.md` — no reaching into neighbouring verses, the passage debate, or the whole-book-read, even where the answer to a flagged `unresolved_items` question is knowable from context. That is the isolation rule being tested here.

## Cross-verse findings surfaced by running the format across the whole passage

These weren't visible from the single-verse (v1) test. Flagging them because they bear directly on your open format questions and on the step 2/3 design:

1. **Pronoun-referent chain is the dominant "unresolved" pattern.** Edom/Esau is named explicitly only at vv1 (Edom), 6, 8, 9, 10 (Jacob, its counterpart), 18 (Esau again) — everywhere else (vv2-5, 7, 15, 16) the addressee is a bare 2ms pronoun with no in-verse antecedent. Strict isolation means most verses in this passage cannot name their own subject. This is exactly the complexity you flagged for step 2 ("cannot be reliably determined by a quick scan") — it's not occasional, it's the passage's default state.
2. **A grammatical number shift at v16**: "you have drunk" is 2mp (plural), diverging from the 2ms singular used everywhere else in vv2-15. Isolation surfaces this as a fact without resolving whether the addressee becomes a collective/people at that exact point — a real candidate-determination question, not decidable from v16 alone.
3. **v3 has an internal 2ms/3ms mismatch**: "you who live... who say" carries a 3ms possessive suffix ("his heart") where the rest of the verse is 2ms ("your heart," "deceived you"). A gloss-level reading smooths this away; the lexical reading doesn't.
4. **Two distinct Strong's entries for "Esau"** are used across the passage and never merged: H6215H (the person/lineage, vv6, 18) vs. H6215I ("Mount Esau," the place, vv8, 9, 21). Reading verse-by-verse in isolation keeps these apart, which a paraphrase reading would likely collapse into one.
5. **v20's "host" is a translation gloss, not a lexical one** — the underlying Strong's (H2426) means "rampart/fortress," not "army/population." Flagged rather than silently accepted, per your point 1 (lexical, not gloss).
6. **v11/13/14 share an unnamed "his"** (wealth, gates, fugitives, survivors) that never resolves within any of those three verses individually — each flags it independently rather than one verse borrowing the answer from another.

## Records

```json
[
  {
    "osisId": "Obad.1.1", "book": "Obadiah", "chapter": 1, "verse": 1,
    "lexical_reading": "A vision (H2377 — prophetic oracle) belonging to Obadiah (H5662R). Introduced as formal reported speech: 'thus says' (H0559) the Lord God (H0136/H3069) concerning Edom (H0123G). An unspecified 'we' report having heard (H8085G) a report (H8052) from the Lord (H3068G), and that a messenger (H6735A) has been sent (H7971G) among the nations (H1471A). Closes with a quoted summons: 'rise' (H6965J, hostile sense, not neutral 'stand') — repeated — 'against her for battle' (H4421).",
    "unresolved_items": ["subject of 'we have heard'", "identity of the messenger"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.2", "book": "Obadiah", "chapter": 1, "verse": 2,
    "lexical_reading": "'Behold' (H2009) introduces a first-person divine declaration: 'I will make' (H5414I, 1cs) 'you' (H0859A, 2ms) 'small' (H6996B, insignificant) 'among the nations' (H1471A). 'You shall be utterly' (H3966) 'despised' (H0959, passive form — held in contempt).",
    "unresolved_items": ["2ms addressee not named within this verse"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.3", "book": "Obadiah", "chapter": 1, "verse": 3,
    "lexical_reading": "'The pride' (H2087, arrogance) 'of your heart' (H3820A) 'has deceived' (H5377) 'you' (2ms, unnamed), 'who live' (H7931) 'in the clefts' (H2288) 'of the rock' (H5553H — elsewhere used of Jehovah as stronghold, fig.), 'in your lofty' (H4791) 'dwelling' (H7675), 'who say' (H0559 — carries a 3ms suffix, 'his heart,' not the 2ms 'your heart' used earlier in the same verse) '\"Who' (H4310) 'will bring [me] down' (H3381) 'to the ground' (H0776H)?\"'",
    "unresolved_items": ["2ms addressee not named", "internal 2ms/3ms suffix mismatch (deceived-you/your-heart vs. his-heart) not resolved, flagged as-is"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.4", "book": "Obadiah", "chapter": 1, "verse": 4,
    "lexical_reading": "'Though you soar aloft' (H1361 — spans both literal height and figurative arrogance; not disambiguated by this verse alone) 'like the eagle' (H5404), 'though your nest is set' (H7760A) 'among the stars' (H3556), 'from there I will bring you down' (H3381), 'declares' (H5002, formal prophetic utterance formula) 'the Lord' (H3068G) — first explicit naming of the first-person speaker running since v2.",
    "unresolved_items": ["2ms addressee not named", "H1361 literal-vs-figurative sense not resolved in-verse"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.5", "book": "Obadiah", "chapter": 1, "verse": 5,
    "lexical_reading": "Two rhetorical hypotheticals: 'if thieves' (H1590) 'came' (H0935G) 'to you,' 'if plunderers' (H7703, to violently despoil) 'came by night' (H3915) — 'how you have been destroyed!' (H1820, Niphal — cut off/undone) — 'would they not steal' (H1589) 'only enough for themselves' (H1767)? 'If grape gatherers' (H1219) 'came, would they not leave' (H7604) 'gleanings' (H5955)?",
    "unresolved_items": ["2ms addressee not named"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.6", "book": "Obadiah", "chapter": 1, "verse": 6,
    "lexical_reading": "'How Esau' (H6215H, person/lineage sense — the addressee explicitly named for the first time since v1's 'Edom') 'has been pillaged' (H2664, Niphal — searched out/exposed), 'his treasures' (H4710) 'sought out' (H1158, Niphal).",
    "unresolved_items": [],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.7", "book": "Obadiah", "chapter": 1, "verse": 7,
    "lexical_reading": "'All your allies' (H0582+H1285, lit. 'men of your covenant') 'have driven you' (H7971G) 'to your border' (H1366G); 'those at peace with you' (H7965G, covenant-peace) 'have deceived you' (H5377); 'they have prevailed' (H3201); 'those who eat your bread' (H3899H) 'have set' (H7760A) 'a trap' (H4204) 'beneath you' (H8478G); 'you have no' (H0369) 'understanding' (H8394 — a named faculty).",
    "unresolved_items": ["2ms addressee not named (last named at v6)", "three betrayer-groups named only by relation, not proper name"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.8", "book": "Obadiah", "chapter": 1, "verse": 8,
    "lexical_reading": "Rhetorical question, first-person divine speech: 'Will I not on that day' — 'declares the Lord' (H5002/H3068G) — 'destroy' (H0006, Piel) 'the wise men' (H2450) 'out of Edom' (H0123G), 'and understanding' (H8394 — the same faculty flagged as lost/betrayed-against in v7) 'out of Mount Esau' (H2022G+H6215I — place-sense, distinct entry from H6215H used in v6).",
    "unresolved_items": [],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.9", "book": "Obadiah", "chapter": 1, "verse": 9,
    "lexical_reading": "'Your mighty men' (H1368) 'shall be dismayed' (H2865), 'O Teman' (H8487H, a named region of Edom, addressed 2ms) 'so that every man' (H0376I) 'from Mount Esau' (H2022G+H6215I, place-sense) 'will be cut off' (H3772I) 'by slaughter' (H6993).",
    "unresolved_items": ["whether 'Teman' stands for a human population or is purely toponymic is not resolved in-verse — directly relevant to step 2 candidate work"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.10", "book": "Obadiah", "chapter": 1, "verse": 10,
    "lexical_reading": "'Because of the violence' (H2555) 'done to your brother' (H0251G, kinship term) 'Jacob' (H3290 — the first human proper name other than Edom/Esau/Obadiah), 'shame' (H0955) 'shall cover you' (H3680), 'and you shall be cut off' (H3772I) 'forever' (H5769G).",
    "unresolved_items": ["2ms addressee not named by proper name; only the kinship claim ('your brother Jacob') is given"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.11", "book": "Obadiah", "chapter": 1, "verse": 11,
    "lexical_reading": "'On the day that you stood' (H5975G — a verb of static presence, not attack) 'aloof, on the day that strangers' (H2114A) 'carried off' (H7617) 'his wealth' (H2428H) 'and foreigners' (H5237) 'entered' (H0935G) 'his gates and cast lots' (H3032/H1486) 'for Jerusalem' (H3389, named) — 'you were like one of them' (H0259).",
    "unresolved_items": ["'his' (wealth, gates) refers to a third party never named within this verse"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.12", "book": "Obadiah", "chapter": 1, "verse": 12,
    "lexical_reading": "Three-part prohibition: 'do not gloat' (H7200G, lit. 'look at [with satisfaction]') 'over the day of your brother' (H0251G) 'in the day of his misfortune' (H5235); 'do not rejoice' (H8055) 'over the people' (H1121G, lit. 'sons of') 'of Judah' (H3063G, named); 'do not boast' (H6310G+H1431, idiom 'make the mouth great') 'in the day of distress' (H6869B).",
    "unresolved_items": ["2ms addressee (the one commanded) not named within this verse; 'Judah' here resolves the wronged-party referent left open at v11"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.13", "book": "Obadiah", "chapter": 1, "verse": 13,
    "lexical_reading": "'Do not enter' (H0935G) 'the gate' (H8179G) 'of my people' (H5971A, 1st-person possessive) 'in the day of their calamity' (H0343); 'do not gloat' (H7200G) 'over his disaster' (H7451C) 'in the day of his calamity'; 'do not loot' (H7971G, idiom 'stretch out [the hand]') 'his wealth' (H2428H).",
    "unresolved_items": ["speaker behind 'my people' not nameable in-verse", "'his' (disaster/wealth) again an unnamed third party, as in v11"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.14", "book": "Obadiah", "chapter": 1, "verse": 14,
    "lexical_reading": "'Do not stand' (H5975G — the identical lexeme as v11's 'stood aloof') 'at the crossroads' (H6563) 'to cut off' (H3772I) 'his fugitives' (H6412A); 'do not hand over' (H5462, idiom 'shut up/deliver up') 'his survivors' (H8300) 'in the day of distress' (H6869B).",
    "unresolved_items": ["'his' (fugitives/survivors) — same unnamed third party as vv11/13"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.15", "book": "Obadiah", "chapter": 1, "verse": 15,
    "lexical_reading": "'For the day of the Lord' (H3068G) 'is near' (H7138) 'upon all the nations' (H1471A). 'As you have done' (H6213A, Qal, active) 'it shall be done to you' (H6213A, Niphal — identical verb root, active then passive); 'your deeds' (H1576) 'shall return' (H7725G) 'on your own head' (H7218A).",
    "unresolved_items": ["2ms addressee not named in-verse"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.16", "book": "Obadiah", "chapter": 1, "verse": 16,
    "lexical_reading": "'For as you have drunk' (H8354, 2mp — plural, diverging from the 2ms singular used vv2-15) 'on my holy' (H6944G, 1st-person possessive) 'mountain' (H2022G), 'so all the nations' (H1471A) 'shall drink' (H8354) 'continually' (H8548); 'they shall drink and swallow' (H3886A), 'and shall be' (H1961) 'as though they had never been.'",
    "unresolved_items": ["2mp (plural) morph on 'drunk' diverges from the singular addressee elsewhere — not resolved whether the addressee becomes collective at this point"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.17", "book": "Obadiah", "chapter": 1, "verse": 17,
    "lexical_reading": "'But in Mount Zion' (H2022G+H6726, named) 'there shall be' (H1961) 'those who escape' (H6413); 'and it shall be holy' (H6944G — the same term used of the defiled mountain at v16, here restored); 'and the house of Jacob' (H1004M+H3290, named — recurs from v10) 'shall possess' (H3423H) 'their own possessions' (H4180).",
    "unresolved_items": [],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.18", "book": "Obadiah", "chapter": 1, "verse": 18,
    "lexical_reading": "'The house of Jacob' (H3290) 'shall be a fire' (H0784), 'and the house of Joseph' (H3130G, named — new to the passage) 'a flame' (H3852), 'and the house of Esau' (H6215H, person-sense, matching v6) 'stubble' (H7179); 'they shall burn' (H1814) 'them and consume' (H0398) 'them, and there shall be no' (H3808) 'survivor' (H8300) 'for the house of Esau, for the Lord' (H3068G) 'has spoken' (H1696G).",
    "unresolved_items": [],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.19", "book": "Obadiah", "chapter": 1, "verse": 19,
    "verse_gap_note": "no verse row in iba.db for this osisId (governance.verse_gap_by_design) — skipped, no lexical reading possible",
    "status": "gap"
  },
  {
    "osisId": "Obad.1.20", "book": "Obadiah", "chapter": 1, "verse": 20,
    "lexical_reading": "'The exiles' (H1546) 'of this host' (H2426 — lexically 'rampart/fortress,' not a population term; the English 'host' is a translation gloss beyond the base lexical sense) 'of the people' (H1121G) 'of Israel' (H3478, named) 'shall possess' (H3423H) 'the land' (the underlying span, H0834A, is the relative particle 'which,' not a noun — 'land' is supplied in translation) 'of the Canaanites' (H3669A, named) 'as far as Zarephath' (H6886, named); 'and the exiles of Jerusalem' (H3389, named) 'who are in Sepharad' (H5614, named) 'shall possess the cities' (H5892B) 'of the Negeb' (H5045G, named).",
    "unresolved_items": ["'host' (H2426) is a lexical mismatch against its own translation — flagged, not silently accepted"],
    "status": "draft"
  },
  {
    "osisId": "Obad.1.21", "book": "Obadiah", "chapter": 1, "verse": 21,
    "lexical_reading": "'Saviors' (H3467 — a participle, lit. 'those who deliver/save,' not a fixed title) 'shall go up' (H5927G) 'to Mount Zion' (H2022G+H6726) 'to rule' (H8199) 'Mount Esau' (H2022G+H6215I, place-sense, matching vv8/9); 'and the kingdom' (H4410) 'shall be the Lord's' (H1961+H3068G).",
    "unresolved_items": ["'Saviors' names a function, not identified individuals — who they are is not resolvable from this verse alone"],
    "status": "draft"
  }
]
```
