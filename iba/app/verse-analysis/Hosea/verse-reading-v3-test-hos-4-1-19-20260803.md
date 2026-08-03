# Verse reading test — Hosea 4:1-19 — applying WA-verse-reading-technique-v3

> Test run of `WA-verse-reading-technique-v3-2026-08-03.md` (Final), second application after the Obadiah 1:1-21 pass. Input: `hos-4-verse-span-meaning.md` (`report.verse_span_meaning` extract). Run as two strictly separated phases across the whole passage, per the document's own gating: **Phase 1 (T1-T5) completed for every verse before Phase 2 (T6-T9) begins for any verse.**
>
> **Legend** (carried over from the Obadiah pass): `[v]` = the cited sense comes from a STEP-tagged `variant` entry. `[bf]` = the cited sense comes from a `base ... fallback` entry (no specific variant resolved; the full undisambiguated base-gloss range is what's actually available). Applied to verbs and semantically load-bearing nouns; grammatical formatives are read but not individually tagged.
>
> **New in this pass:** Hosea 4 surfaces a recurring pattern not seen in the Obadiah test — several spans carry a person/number/possessive suffix that does not match either the surface English word or the surrounding grammar (a 1cs "my" suffix landing on "lack"/"wood" where "my people" is clearly meant; "they"/"their" surfaces sitting on tagged 3ms/3fs singular suffixes at vv8, 12, 18, 19). These are recorded below as **data anomalies**, kept distinct from T2 (lexical-range) and T3 (morph/aspect) flags, since they read as tokenization artifacts in this specific extract rather than genuine grammatical ambiguity in the underlying Hebrew. Also new: a T4 referent crux at v7 where the row's own tagged suffixes run opposite to the received English translation (a "glory"/"shame" possessor swap, touching a known class of Hebrew textual crux) — recorded per T4 rather than silently following the translation's premise.

---

## Phase 1 — T1-T5 (base lexical reading), whole passage

### Hos 4:1

"Hear" (H8085G [bf], Qal imperative 2mp) the word (H1697G [bf]) of the Lord (H3068G [v]), O children (H1121G [bf]) of Israel (H3478 [v]), for the Lord (H3068G [v]) has a controversy (H7379 [v] + H3588A [v]) with the inhabitants (H3427 [v], Qal active participle masc. plural construct — "those dwelling," durative, not a punctual act — + H5973A [v]) of the land (H0776G [bf] + H9009 [v]); there is no (H0369 [v]) faithfulness (H0571G [bf] + H3588A [v]) or steadfast love (H2617A [bf] + H0369 [v] + H9002 [v]), and no (H0369 [v]) knowledge (H1847 [v] + H9002 [v]) of God (H0430G [bf]) in the land (H0776G [bf] + H9009 [v]).

**T2 flags.** H8085's own lexical range extends to "to hear, obey" — in a covenant-lawsuit summons ("Hear!"), the operative sense may well be "heed/obey," a sense stated in the word's own range, not merely "perceive by ear." H7379 (*riv*) is an explicitly legal/technical term — "strife, controversy, dispute; case at law" — a covenant-lawsuit term, not casual disagreement. H1847 (*da'at*) extends to "discernment, understanding, wisdom," broader than bare factual knowing — relevant since "knowledge of God" recurs as a major term through this chapter (vv1, 6).

**T5 — genre-conventional element expected but absent.** A classic covenant-lawsuit (*rib*) opening conventionally summons witnesses (e.g. "heaven and earth," cf. Deut.32.1, Isa.1.2, Mic.6.1-2). No witness-summons formula accompanies the LORD's stated *riv* (H7379) here — recorded as an observed absence.

---

### Hos 4:2

"Swearing" (H0422 [v], Qal infinitive absolute), "lying" (H3584 [v], Piel infinitive construct), "murder" (H7523 [v], Qal infinitive absolute), "stealing" (H1589 [v], Qal infinitive absolute), and "committing adultery" (H5003 [v], Qal infinitive absolute); "they break all bounds" (H6555 [v], Qal perfect 3cp) and "bloodshed" (H1818 [v] + H9002 [v]) "follows" (H5060 [v], Qal perfect 3cp) "bloodshed" (H1818 [v] + H9003 [v]).

**T3 note.** Five successive infinitive-absolute/infinitive-construct forms (spans 0-4) list the offenses as bare, unconjugated actions — a distinct Hebrew stylistic device, a chain of infinitives functioning almost as a naming-list of sins, not ordinary finite-verb clauses. Only "break" (span 5) and "follows" (span 7) are finite (Qal perfect 3cp), giving the crimes-list its own grammatical shape distinct from the surrounding narrative — the same device recurs at v18 ("whoring... they have whored").

---

### Hos 4:3

"Therefore" (H5921A [bf] + H3651C [v]) "the land" (H0776G [bf] + H9009 [v]) "mourns" (H0056 [v], Qal imperfect 3fs), "and all" (H3605 [v]) "who dwell" (H3427 [v], Qal active participle masc. sing.) "in it languish" (H0535 [v], morph HVPq3ms — its own range gives "(Qal) pass participle... to be weak; (Pulal) to be or grow feeble" — a condition suffered, not an act performed), "and also the beasts" (H2416C [v] + H9003 [v] ×2 + H9034 [v]) "of the field" (H7704G [v] + H9009 [v]) "and the birds" (H5775 [v] + H9002 [v] + H9003 [v]) "of the heavens" (H8064 [v] + H9009 [v]), "and even the fish" (H1709H [v] + H1571 [v] + H9002 [v]) "of the sea" (H3220G [v] + H9009 [v]) "are taken away" (H0622 [v], Niphal imperfect 3mp, **passive**).

**T3 flag.** H0622 "taken away" is Niphal imperfect 3mp — explicitly passive, "are gathered/removed"; the creatures are acted upon, not acting, matching the covenant-curse logic of the verse (the land and its creatures suffer the consequence, they do not cause it).

---

### Hos 4:4

"Yet" (H0389 [v]) "let no one" (H0408 [v] + H0376I [v]) "contend" (H7378 [v], Qal jussive 3ms), "and let none" (H0376I [v]) "accuse" (H3198 [v], Hiphil jussive 3ms + H0408 [v] + H9002 [v]), "for with you" (H5971A [bf] + H9002 [v]) "is my contention" (H7378 [v] + H9004 [v] + H9021 [v]), "O priest" (H3548 [v]).

**T1/T2 flag — significant.** The surface gloss "with you" is tagged to **H5971A**, whose own lexical range is *exclusively* "nation, people; persons, members of one's people" — no sense of "with" appears anywhere in this range. Read from the row rather than the English gloss (T1), this looks like a code/tokenization mismatch: Hebrew *ʿim* ("with") and *ʿam* ("people") are orthographically close but distinct roots, and the row appears to have tagged the "people" root where a "with" preposition is expected. This also touches a known text-critical crux in this verse — translations diverge here (some read "for your people are like those who contend with the priest" rather than "for with you is my contention, O priest"). The row itself does not adjudicate this; it is recorded as found, not silently corrected.

**T4 — open naming point.** The singular vocative "priest" is not resolved by this row alone as either a single figure or the priesthood generically — flagged for follow-up given the priest-material continuing through vv5-9.

---

### Hos 4:5

"You shall stumble" (H3782 [v], morph HVqq2ms — a Qal perfect-with-vav form; see T3 note) "by day" (H3117G [v] + H9009 [v]); "the prophet" (H5030 [v] + H1571 [v]) "also shall stumble" (H3782 [v], HVqq3ms, same form) "with you" (H3915 [v] + H5973A [v] + H9031 [v]) "by night"; "and I will destroy" (H1820 [v], Qal perfect 1cs) "your" (H9021 [v]) "mother" (H0517 [v]).

**T3 note.** Both instances of "stumble" share the identical lexeme+morph shape. This extract's own morph-code key is not spelled out anywhere in the raw data, so the second aspect-letter ("q," distinct from the "p" = perfect seen at e.g. H2398 "sinned" HVqp3cp in v7) is read functionally — a perfect-with-vav form carrying forward the surrounding future/continuing sense — rather than asserted as a confirmed decode. Flagged rather than guessed past.

**T4 — open naming point.** "Your mother" is read in context as Israel personified (a recurring prophetic figure — mother = the nation), not a literal individual; no competing candidate is evidenced in the row itself, so this is not treated as a multi-candidate crux.

---

### Hos 4:6

"My people" (H5971A [bf]) "are destroyed" (H1820 [v], Niphal perfect 3cp, passive) "for" (H9006 [v]) "lack" (H1097 [v] + H9020 [v]) "of knowledge" (H1847 [v] + H9009 [v]); "because" (H3588A [v]) "you have rejected" (H3988A [bf], Qal perfect 2ms) "knowledge" (H1847 [v] + H9009 [v] + H0859A [v], the last an explicit independent "you" pronoun reinforcing the already-marked 2ms verb), "I reject" (H3988A [bf], morph HVqu1cs — a first-person volitional-shaped form, "I will surely reject") "you from" (H9006 [v]) "being a priest" (H3547 [v] + H9031 [v]) "to me"; "and since you have forgotten" (H7911 [v], morph HVqw2ms — a vav-form) "the law" (H8451 [v]) "of your God" (H0430G [bf]), "I" (H0589 [v], independent pronoun, emphatic) "also" (H1571 [v]) "will forget" (H7911 [v], Qal imperfect 1cs) "your" (H9021 [v]) "children" (H1121A [bf]).

**Data anomaly.** The 1cs possessive suffix (H9020, "my") is tagged on **"lack"** (span 3), not on "people" (span 0, which carries no suffix in this tokenization) — the sense clearly intends "my people," not "my lack." Recorded as found per T1, not corrected. (The first of a repeating pattern in this extract — see vv8, 12, 18, 19.)

**T4 — open naming point.** "Your children" (span 18) is read as the priest's own line/descendants, continuing the second-person address to the priest running since v4 — the contextually natural reading, no competing referent evidenced in the row.

---

### Hos 4:7

"The more" (H3651C [v] + H9048 [v]) "they increased" (H7235A [bf], Qal infinitive construct, idiom "according to their multiplying"), "the more they sinned" (H2398 [v], Qal perfect 3cp) "against me; I will change" (H4171 [v], Hiphil imperfect 1cs) "their glory" (H3519 [v] + H9005 [v] + H9030 [v]) "into shame" (H7036 [v] + H9003 [v] + H9028 [v]).

**T4 — referent crux, the possessor of "glory"/"shame".** Genuinely live readings, per T4:
1. **The received translation's assignment** (ESV etc.): "their glory" (the people's, 3mp) is changed into (unpossessed) "shame."
2. **The row's own tagged suffixes, read literally**: "glory" (span 4) carries H9005 ("to/for") + **H9030**, a **1cs** suffix ("to/for me"), not a 3mp ("their"); "shame" (span 5) carries **H9028**, a **3mp** suffix ("their") — the opposite assignment from reading 1: "I will change **MY** glory into **THEIR** shame."

Adopted for this pass: **reading 2** (per-row) — grounded directly in H9030 on "glory" and H9028 on "shame." T1 requires working from the row's own data rather than the English gloss, and here the divergence is a suffix-level fact, not an inference. Reading 1 (the received/traditional rendering) is kept on record, though this row's own suffix tags do not themselves support it. This pattern — a first-person statement about the LORD's own glory/shame apparently softened toward a third-person reading — matches a class of textual crux traditionally associated with *Tiqqun Sopherim* scribal corrections elsewhere in the Hebrew Bible; this technique does not adjudicate that text-critical history, only records what the row itself tags.

---

### Hos 4:8

"They feed" (H0398 [v], Qal imperfect 3mp) "on my" (H9020 [v]) "people's" (H5971A [bf]) "sin" (H2403B [bf]); "they" (H9023 [v], tagged **3ms** "his," though the surface reads plural "they" — see T3 flag) "are greedy" (H5375O [bf] + H9028 [v] + H5315L [bf], idiom "lift up the appetite/soul to," i.e. "set their desire on") "for their iniquity" (H5771G [bf] + H0413 [v] + H9002 [v]).

**T3 flag.** Span 3 is tagged H9023, glossed "his" (3ms singular), not a 3mp form — surface plural "they" sits on a tagged singular suffix. Recorded per T3 as a fact of the row, not silently reconciled.

**T4 — open naming point.** "They/his" most plausibly continues the priest(s) addressed in vv4-9 (feeding on the people's sin-offerings is a priestly practice) — the contextually natural reading, not a competing multi-candidate crux, since no alternative referent is grammatically evidenced within the row.

---

### Hos 4:9

"And it shall be" (H1961 [v], morph HVqq3ms) "like people" (H5971A [bf] + H9004 [v]), "like priest" (H3548 [v] + H9004 [v]); "I will punish" (H6485H [v], HVqq1cs) "them for their ways" (H1870G [v] + H5921A [bf] + H9033 [v]) "and repay" (H7725K [bf], Hiphil imperfect 1cs) "them" (H9005 [v] + H9033 [v]) "for their deeds" (H4611 [v] + H9002 [v] + H9023 [v]).

**T4.** "People"/"priest" comparison — both explicitly paired categories within-verse, continuing directly from vv4-8's priest material; "them" resolves to the same paired referent, no open crux.

---

### Hos 4:10

"They shall eat" (H0398 [v], morph HVqq3cp), "but not" (H3808 [v]) "be satisfied" (H7646 [v] + H9002 [v], Qal imperfect 3mp); "they shall play the whore" (H2181 [v], Hiphil perfect 3cp — the lexicon's own Hiphil sub-range directly lists "to commit fornication," so this sense is stated via the lexicon, not inferred, per T2), "but not" (H3808 [v]) "multiply" (H6555 [v] + H9002 [v], Qal imperfect 3mp); "because they have forsaken" (H5800A [bf], Qal perfect 3cp) "the Lord" (H3068G [v] + H3588A [v] + H0853 [v], object marker) "to" (H9005 [v]) "cherish" (H8104I [bf], Qal infinitive construct, idiom "to keep/give heed to") —

**T2 flag.** H2181's Hiphil range lists "to commit fornication" as a direct sub-sense alongside the causative senses ("to cause to commit adultery," "to force into prostitution") — the non-causative reading used here is a stated member of the tagged form's own range, not an inference from a causative form read loosely.

**T5.** The fertility-cult futility pattern (eat/not satisfied, whore/not multiply) is itself a genre-conventional covenant-curse element (cf. Deut.28) — present here, not absent; noted rather than flagged missing.

---

### Hos 4:11

— "whoredom" (H2184 [v]), "wine" (H3196 [v] + H9002 [v]), "and new wine" (H8492 [v] + H9002 [v]), "which take away" (H3947G [bf], Qal imperfect 3ms) "the understanding" (H3820A [bf], lit. "heart").

**T1 note.** Read in context with v10 (nearby rows read together, per T1, not in isolation) — "whoredom, wine, and new wine" are the direct objects of v10's "to cherish"; the verse-break falls mid-sentence.

---

### Hos 4:12

"My people" (H5971A [bf]) "inquire" (H7592 [v] + H9023 [v], Qal imperfect 3ms, "his") "of a piece of wood" (H6086G [v] + H9003 [v] + H9020 [v], tagged **1cs** "my" — see data anomaly below), "and their walking staff" (H4731 [v] + H9002 [v]) "gives them oracles" (H5046 [v] + H9023 [v], Hiphil imperfect 3ms, "his"). "For" (H9005 [v]) "a spirit" (H7307G [bf] + H9033 [v] + H3588A [v]) "of whoredom" (H2183 [v]) "has led them astray" (H8582 [v], Hiphil perfect 3ms — the lexicon's own Hiphil range directly includes "to cause to err, mislead," matching this sense per T2), "and they have left their God" (idiom, H0430G [bf] + H9028 [v] + H8478H [v] + H9006 [v], lit. "from under their God") "to play the whore" (H2181 [v], morph HVqw3mp — a vav-form).

**Data anomaly.** "Wood" is tagged with a **1cs** possessive suffix (H9020, "my"), matching neither the English translation ("a piece of wood," no possessor named) nor the parallel span 3 ("their walking staff," correctly unmarked for 1cs). Recorded as found — the third instance of a 1cs suffix landing on an unexpected span in this passage (cf. vv4, 6), suggesting a systematic tokenization pattern in this extract, worth surfacing to the researcher rather than resolving verse-by-verse.

---

### Hos 4:13

"They sacrifice" (H2076 [v], Piel imperfect 3mp) "on the tops" (H7218I [v]) "of the mountains" (H2022G [v] + H9009 [v]) "and burn offerings" (H6999H [v], Piel imperfect 3mp) "on the hills" (H1389I [v] + H9009 [v] + H9002 [v]), "under" (H8478G [v]) "oak" (H0437 [v]), "poplar" (H3839 [v] + H9002 [v]), "and terebinth" (H0424 [v] + H9002 [v]), "because their shade" (H6738 [v]) "is good" (H2896A [bf] + H3588A [v]). "Therefore" (H5921A [bf]) "your daughters" (H1323G [v]) "play the whore" (H2181 [v] + H9024 [v] + H5921A [bf] + H3651C [v], Qal imperfect 3fp), "and your brides" (H3618G [v] + H9002 [v] + H9026 [v]) "commit adultery" (H5003 [v] + H9026 [v], Piel imperfect 3fp).

**T4 — open naming point.** The address shifts from the singular priest (vv4-9) to a plural "your" with daughters/brides — whether this is still priest-directed or addressed to the nation broadly is not resolved by this row alone; recorded as an open observation, not a competing grammatical-candidate crux.

---

### Hos 4:14

"I will not punish" (H6485H [v], Qal imperfect 1cs) "your daughters" (H1323G [v] + H5921A [bf]) "when they play the whore" (H2181 [v], Qal imperfect 3fp), "nor your brides" (H3618G [v] + H5921A [bf] + H9002 [v]) "when" (H3588A [v] + H9026 [v]) "they commit adultery" (H5003 [v] + H9026 [v] + H3588A [v]); "for the men themselves" (H1992 [v], independent pronoun, emphatic + H3588A [v]) "go aside" (H6504 [v], Piel imperfect 3mp) "with" (H5973A [v]) "prostitutes" (H2181 [v] + H9009 [v], Qal active participle fem. plural) "and sacrifice" (H2076 [v], Piel imperfect 3mp) "with cult prostitutes" (H6948 [v] + H9009 [v] + H5973A [v] + H9002 [v]); "and a people" (H5971A [bf] + H9002 [v]) "without" (H3808 [v]) "understanding" (H0995 [v] + H3808 [v], Qal imperfect 3ms + negation) "shall come to ruin" (H3832 [v], Niphal imperfect 3ms, passive).

**T4 — referent crux resolved within-verse.** "The men themselves" (span 6, H1992) — the emphatic independent pronoun explicitly redirects the blame just stated in this same verse away from the daughters/brides onto the men, grounded directly in the pronoun's marked, emphatic placement — a directly-stated redirection, not an inference requiring enumeration of competing readings.

---

### Hos 4:15

"Though" (H0518A [v]) "you play the whore" (H2181 [v], Qal active participle masc. sing.), "O Israel" (H3478 [v] + H0859A [v], independent pronoun reinforcing the vocative), "let not Judah" (H3063G [bf]) "become guilty" (H0816 [v] + H0408 [v], Qal jussive 3ms). "Enter" (H0935G [bf], Qal jussive 2mp) "not into Gilgal" (H1537G [v] + H9009 [v]), "nor go up" (H5927G [v], Qal jussive 2mp) "to Beth-aven" (H1007 [v]), "and swear" (H7650 [v], Niphal jussive 2mp + H0408 [v] + H9002 [v]) "not, 'As the Lord" (H3068G [v]) "lives'" (H2416A [v]).

**T4.** Two distinct named parties — Israel (addressed directly) and Judah (referred to in the third person, warned not to follow) — both explicit within-verse, no open crux.

**T5.** Gilgal and Beth-aven are named as illicit worship sites — a recognised convention in Hosea of naming specific cult locations (cf. Hos.9.15, 10.5, 12.11) — present here, not absent.

---

### Hos 4:16

"Like" (H3588A [v]) "a stubborn" (H5637 [v], Qal active participle fem. sing.) "heifer" (H6510 [v] + H9004 [v]), "Israel" (H3478 [v]) "is stubborn" (H5637 [v], Qal perfect 3ms); "can the Lord" (H3068G [v] + H9038 [v], "them" 3mp) "now" (H6258 [v]) "feed" (H7462B [bf], Qal imperfect 3ms) "them like" (H9004 [v]) "a lamb" (H3532 [v]) "in a broad pasture" (H4800 [v] + H9003 [v])?

**T4.** "Them" (3mp) resolves to Israel as a collective, matching the singular "Israel is stubborn" of the same verse read distributively; no competing candidate.

---

### Hos 4:17

"Ephraim" (H0669G [v]) "is joined" (H2266 [v], Qal passive participle masc. sing. construct — a durative/ongoing state, "is joined," not a single past event) "to idols" (H6091 [v]); "leave him" (H9005 [v] + H9033 [v]) "alone" (H5117 [v], Hiphil imperative 2ms, idiom "let be").

**T4.** "Ephraim" is named explicitly for the first time in this chapter — the northern-kingdom tribal name, used elsewhere in Hosea as a byname for Israel; no open referent within this short verse.

---

### Hos 4:18

"When their drink" (H5435 [v]) "is gone" (H5493H [v], Qal perfect 3ms), "they play the harlot most certainly" (H2181 [v], morph HVhaa — Hiphil infinitive absolute + H9028 [v] "their," an intensifying construction, matching the stacked-infinitive device already seen at v2) — "they have whored" (H2181 [v], Hiphil perfect 3cp); "their" (H9024 [v], tagged **3fs** "her" — see data anomaly) "rulers" (H4043 [v], literally "shields" — see T2 flag) "dearly love" (H0157G [bf], Qal perfect 3cp) "shame" (H7036 [v] + H0157G [bf], the second "love" tag attached here with an imperative-shaped morph — see data anomaly).

**T2 flag.** H4043 ("shield, buckler") is rendered "rulers" — the figurative sense ("protectors/nobles") is not itself a listed member of the word's own lexical range, which lists only the literal object. Recorded as an inference from imagery, per T2, not a lexicon-stated sense.

**Data anomalies.** (a) "Their" (surface) sits on a tagged **3fs** ("her") suffix, not 3mp — recorded as found, matching the recurring gender/number mismatch pattern in this extract (cf. vv8, 12, 19). (b) The final span re-tags H0157G ("love") with an imperative-shaped morph, duplicating the previous span's already-read Qal perfect 3cp of the same root one span earlier — recorded as an apparent tokenization/data anomaly, not resolved.

---

### Hos 4:19

"A wind" (H7307H [bf]) "has wrapped" (H6887B [v], Qal perfect 3ms) "them" (H9034 [v], "her" 3fs) "in its wings" (H3671 [v] + H9003 [v] + H0853 [v], object marker + H9034 [v]), "and they shall be ashamed" (H0954 [v], morph HVqu3mp + H9024 [v] "her" 3fs) "because of their" (H9028 [v]) "sacrifices" (H2077 [v] + H9006 [v]).

**Data anomaly.** Several 3fs suffixes (H9034, H9024) run through this verse where the surface reads as plural/collective ("them," "their") — consistent with the recurring gender/number mismatch pattern already flagged at vv8, 12, 18 in this same extract; recorded as observed, not normalized.

**T5 — genre-conventional element expected but absent, passage close.** The chapter closes on unresolved judgment (shame, ruin) with no covenant-restoration or reconciliation promise appended — a genre element present at the close of other units in Hosea (e.g. ch.2's ending) is textually absent here.

---

## Phase 2 — T6-T9 (inner-being stamps)

Begun only after Phase 1 above is complete for the whole passage, per the document's gating. *IB* = human-only. *Agent* = the doer (noun), human or non-human. *Process* = state/condition/faculty words tied to an IB. *action* = the verb. Stamps stack; indicative/preliminary only, no relational analysis performed.

| Verse | Stamped word (surface) | Stamp(s) |
|---|---|---|
| 4:1 | children of Israel | *IB* |
| 4:1 | Hear | *action* |
| 4:1 | Lord (span 2) | *Agent* (non-human) |
| 4:1 | Lord (span 6) | *Agent* (non-human) |
| 4:1 | inhabitants | *IB* |
| 4:1 | controversy | *Process* |
| 4:1 | faithfulness | *Process* |
| 4:1 | steadfast love | *Process* |
| 4:1 | knowledge | *Process* |
| 4:1 | God | *Agent* (non-human) |
| 4:2 | swearing | *action* |
| 4:2 | lying | *action* |
| 4:2 | murder | *action* |
| 4:2 | stealing | *action* |
| 4:2 | adultery | *action* |
| 4:2 | break | *action* |
| 4:2 | bloodshed | *Process* |
| 4:2 | follows | *action* |
| 4:3 | land | *Agent* (non-human, personified) |
| 4:3 | mourns | *action* |
| 4:3 | all who dwell | *IB* |
| 4:3 | languish | *Process*, *action* |
| 4:3 | beasts | *Agent* (non-human) |
| 4:3 | birds | *Agent* (non-human) |
| 4:3 | fish | *Agent* (non-human) |
| 4:3 | taken away | *action* |
| 4:4 | no one / none | *IB* (unnamed) |
| 4:4 | contend | *action* |
| 4:4 | accuse | *action* |
| 4:4 | you | *IB* |
| 4:4 | contention | *Process* |
| 4:4 | priest | *IB* |
| 4:5 | you | *IB* |
| 4:5 | stumble | *action* |
| 4:5 | prophet | *IB* |
| 4:5 | destroy | *action* |
| 4:5 | your mother | *IB* (figure for the nation, flagged) |
| 4:6 | my people | *IB* |
| 4:6 | destroyed | *Process*, *action* |
| 4:6 | knowledge | *Process* |
| 4:6 | you | *IB* |
| 4:6 | rejected | *action* |
| 4:6 | priest | *IB* |
| 4:6 | forgotten | *action* |
| 4:6 | law | *Process* |
| 4:6 | God | *Agent* (non-human) |
| 4:6 | I | *Agent* (non-human, the LORD) |
| 4:6 | forget | *action* |
| 4:6 | your children | *IB* |
| 4:7 | they | *IB* |
| 4:7 | increased | *action* |
| 4:7 | sinned | *action* |
| 4:7 | I | *Agent* (non-human) |
| 4:7 | change | *action* |
| 4:7 | glory | *Process* (possessor uncertain — see referent crux) |
| 4:7 | shame | *Process* (possessor uncertain — see referent crux) |
| 4:8 | they | *IB* |
| 4:8 | feed | *action* |
| 4:8 | my people | *IB* |
| 4:8 | sin | *Process* |
| 4:8 | greedy | *Process*, *action* |
| 4:8 | iniquity | *Process* |
| 4:9 | people | *IB* |
| 4:9 | priest | *IB* |
| 4:9 | I | *Agent* (non-human) |
| 4:9 | punish | *action* |
| 4:9 | ways | *Process* |
| 4:9 | repay | *action* |
| 4:9 | deeds | *Process* |
| 4:10 | they | *IB* |
| 4:10 | eat | *action* |
| 4:10 | satisfied | *Process*, *action* |
| 4:10 | whore | *action*, *Process* |
| 4:10 | multiply | *action* |
| 4:10 | forsaken | *action* |
| 4:10 | Lord | *Agent* (non-human) |
| 4:10 | cherish | *action* |
| 4:11 | whoredom | *Process* |
| 4:11 | wine / new wine | *Process* |
| 4:11 | take away | *action* |
| 4:11 | understanding | *Process* |
| 4:12 | my people | *IB* |
| 4:12 | inquire | *action* |
| 4:12 | staff | *Agent* (non-human, grammatical subject of "gives oracles") |
| 4:12 | oracles / gives oracles | *action* |
| 4:12 | spirit of whoredom | *Agent* (non-human) |
| 4:12 | astray | *action*, *Process* |
| 4:12 | God | *Agent* (non-human) |
| 4:12 | whore | *action* |
| 4:13 | they | *IB* |
| 4:13 | sacrifice | *action* |
| 4:13 | burn offerings | *action* |
| 4:13 | your daughters | *IB* |
| 4:13 | whore | *action* |
| 4:13 | your brides | *IB* |
| 4:13 | adultery | *action* |
| 4:14 | I | *Agent* (non-human) |
| 4:14 | punish | *action* |
| 4:14 | your daughters | *IB* |
| 4:14 | whore | *action* |
| 4:14 | your brides | *IB* |
| 4:14 | adultery | *action* |
| 4:14 | the men themselves | *IB*, *Agent* |
| 4:14 | go aside | *action* |
| 4:14 | prostitutes | *IB* |
| 4:14 | sacrifice | *action* |
| 4:14 | cult prostitutes | *IB* |
| 4:14 | people without understanding | *IB*, *Process* |
| 4:14 | ruin | *Process*, *action* |
| 4:15 | you | *IB* |
| 4:15 | Israel | *IB* |
| 4:15 | whore | *action* |
| 4:15 | Judah | *IB* |
| 4:15 | become guilty | *Process*, *action* |
| 4:15 | Enter | *action* |
| 4:15 | go up | *action* |
| 4:15 | swear | *action* |
| 4:15 | Lord | *Agent* (non-human) |
| 4:16 | heifer | *Agent* (non-human) |
| 4:16 | Israel | *IB* |
| 4:16 | stubborn | *Process* (×2) |
| 4:16 | Lord | *Agent* (non-human) |
| 4:16 | feed | *action* |
| 4:16 | them | *IB* |
| 4:16 | lamb | *Agent* (non-human) |
| 4:17 | Ephraim | *IB* |
| 4:17 | joined | *Process*, *action* |
| 4:17 | him | *IB* |
| 4:17 | alone (leave alone) | *action* |
| 4:18 | drink | *Process* |
| 4:18 | gone | *action* |
| 4:18 | they themselves (whoring) | *IB* |
| 4:18 | whoring / whored | *action* |
| 4:18 | rulers | *IB* (H4043 literally "shields," figurative reading, see T2 flag) |
| 4:18 | love | *action* |
| 4:18 | shame | *Process* |
| 4:19 | wind | *Agent* (non-human) |
| 4:19 | wrapped | *action* |
| 4:19 | them | *IB* |
| 4:19 | ashamed | *Process*, *action* |
| 4:19 | sacrifices | *Process* |

---

## Self-check (T1-T9)

- **T1** — every row in every verse's span table was read; nearby-row context was used throughout (most notably v10/v11, read as one continuous sentence across the verse break).
- **T2** — every cited verb/content-noun marked `[v]`/`[bf]`; flags raised where the lexical range did or did not support a reading: v1's hear/*riv*/*da'at* range notes, v4's H5971A "people"-vs-"with" mismatch, v10/v12's Hiphil senses confirmed as lexicon-stated (not inferred), v18's H4043 shield-to-ruler figurative inference flagged as *not* lexicon-stated.
- **T3** — morph cited for every main verb; genuine anomalies recorded, not normalized: v3/v8's passive/singular-vs-plural forms, v5's unresolved "q"-aspect letter named as a functional reading rather than a confirmed decode (this extract's morph-code key is not spelled out anywhere in the source data).
- **T4** — one full multi-candidate crux completed (v7's glory/shame possessor swap, adopting the per-row suffix reading against the received translation, with the traditional reading kept on record); v14's emphatic-pronoun redirection recorded as directly stated, not a manufactured multi-candidate enumeration; all other unnamed/ambiguous referents recorded as open naming gaps, kept distinct from true cruxes.
- **T5** — genre-conventional absences recorded at v1 (missing witness-summons) and v19 (missing restoration/reconciliation close); the futility-curse pattern at v10 and the named cult-sites at v15 noted as *present*, not flagged as missing, to keep the absence-recording honest (not padded).
- **New field — data anomalies** — a recurring pattern of person/number/possessive-suffix mismatches between the surface English and the tagged Strong's data was found across this extract (vv4, 6, 8, 12, 18, 19) — markedly more frequent than in the Obadiah test pass. Recorded per-verse rather than silently resolved; worth the researcher's attention as a possible extract-level tokenization issue, not 19 independent grammatical curiosities.
- **T6-T9** — run only after T1-T5 was complete for the whole passage, per the gating rule. Every human reference stamped *IB* (including "your mother," v5, as a figure for the nation, flagged as such); non-human agentive nouns (land, beasts, birds, fish, staff, spirit of whoredom, heifer, lamb, wind, the LORD) stamped *Agent*, never *IB*; one stamp flagged uncertain (v18 "rulers," literally "shields").
- **Traceability** — every sense, grammatical call, referent, absence, anomaly, and stamp above is traceable to a specific span's strong/morph/meaning_tree field, not to an English keyword match.

**Known limitation of this pass, stated plainly:** done manually, verse by verse, in one continuous sitting — the same condition noted in the Obadiah v3 test pass. Several morph-code aspect letters (the character after the stem letter — e.g. "q" vs "p" vs "w" vs "u") are not spelled out anywhere in the raw data or in the technique doc itself; readings of those letters here are functional, cross-verse-pattern inferences, not confirmed decodes from an authoritative key, and are flagged as such throughout rather than presented as settled. This chapter also surfaced a materially higher rate of surface-vs-tag person/number mismatches than the Obadiah pass (six verses vs. none) — worth weighing as a possible property of this specific extract before generalising conclusions about the technique's own reliability from one passage to the next.
