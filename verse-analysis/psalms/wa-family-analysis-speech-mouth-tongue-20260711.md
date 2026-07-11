# Family analysis — `speech-mouth-tongue` (Psalms), in isolation

> Source: `outputs/data/psalms-family-base-sources/psalms__speech-mouth-tongue.json` only.
> Scope: 24 meanings · 42 instances · 34 passages. Genre uniformly `poetic/wisdom`. Every finding cites `reference · span · Dnnn(label)` into that file. British spelling.

---

## 0. Data-integrity screen (done first)

### 0.1 D112(coupling) / D116(locus) field-swap
Correct order = D116 a code (`internal:`/`external:`), D112 a phrase. The following **10 instances are transposed** (D112 holds the code, D116 holds a prose phrase) and must be read corrected — swap the two values:

| Reference · span | D112 (as stored) | D116 (as stored) |
|---|---|---|
| Psa 107:22 · 269935 | `external:god` | "paired with thanksgiving and joy" |
| Psa 92:15 · 285190 | `external:god` | "paired with proclaiming God as rock" |
| Psa 92:2 · 285199 | `external:god` | "paired with declaring his faithfulness" |
| Psa 102:21 · 268988 | `external:god` | "paired with his praise in Jerusalem" |
| Psa 96:3 · 285574 | `external:god` | "paired with telling of salvation" |
| Psa 118:17 · 271077 | `external:god` | "paired with living to tell them" |
| Psa 106:2 · 269636 | `external:god` | "paired with praising" |
| Psa 106:33 · 307465 | `internal:ib-state` | "paired with the embittered spirit" |
| Psa 105:2 · 269416 | `external:god` | "paired with singing" |
| Psa 96:2 · 285568 | `external:god` | "paired with declaring his glory" |

Corrected, all ten read: D116(locus) = the code, D112(coupling) = the "paired with…" phrase. The other 32 instances are already in correct order (D116 a code, D112 a phrase). Note the swap is systematic: every swapped case is a "paired with…" locus phrase mis-filed under coupling and a locus-code mis-filed under coupling — the reader must not take D112 `external:god`/`internal:ib-state` at face value in these ten.

### 0.2 Self-loop "edges" are not links
The overwhelming majority of `edges[]` are self-loops: `item_type:"flag"`, `resolution:"inferred"`, `from_span:null`, `to_span` = the span's own id (bearer D105, target D107, coupling D112, seat D104, manner D108 all recur as self-loops). These are **not** network edges. Only `pair` edges (`resolution:"span"`, `from_span`→a different `to_span`) are genuine.

Genuine `pair` edges exist on 11 instances, but **almost all point to spans outside this file's 42-span set** (they link to sibling words in the same verse — targets/couplings/sources that are not themselves speech-family members, e.g. 281288→281292/281284, 282765→282743, 279685→279687). Only **two genuine edges have both endpoints inside this family** (see §The network).

### 0.3 seat(D104) / manner(D108) = "none"
- **D104 seat = "none" in 39 of 42.** Only 3 name a seat, all speech-organs: mouth (Psa 71:15 · 282067; Psa 51:15 · 279685 "mouth / opened lips"), tongue (Psa 71:24 · 282162).
- **D108 manner = "none" in 35 of 42.** The 7 filled: Psa 71:15 · 282067 ("all the day, beyond his knowledge"), Psa 51:15 · 279685 ("with lips God has opened"), Psa 75:9 · 282765 ("forever"), Psa 71:17 · 282089 ("taught from youth, still proclaiming"), Psa 71:18 · 282099 ("even to old age"), Psa 73:8 · 282514 ("loftily"), Psa 71:24 · 282162 ("all the day long").

### 0.4 Absent dimensions
- **D109 intensity, D110 specifier, D111 effect, D113 prohibition — absent across all 42 instances.** None ever coded.
- **D103 source — effectively absent: filled once only** (Psa 75:9 · 282765 · D103(source) = "of the God who executes judgment", pair→282743). The other 41 carry no source.

### 0.5 Cluster NULL / T2
- **26 of 42 instances cannot be M-typed by their term-cluster:** 24 have `cluster.code = null` **and** `all_candidates = null`; 2 (Psa 145:21 · 274133; Psa 141:3 · 308114, both lemma H6310 "mouth") have `code = null` but `all_candidates = "T2(Supplementary)"` — typed only as a supplementary/qualifier, per memory `feedback_t2_reference_flag_reclassify`.
- The null-cluster instances are chiefly the saphar (H5608), dabar (H1696), and lexeme-name meanings (H3956 tongue, H3001 dried-up, H0981 spoke-rashly, H1319 basar).
- Real M-clusters: **M42 Speech = 10 instances** (H5046 declare/proclaim/tell ×8, H1897 talk/tell ×2), **M41 Remembrance = 2** (H8085 shama declare/proclaim), plus the 4 flagged outliers below.

### 0.6 Outliers (`is_outlier=true`) — genuine non-adjacent crossovers
4 meanings / 4 instances the family's expected M42(Speech) does not own:
- Psa 17:4 · 274854 — H8104 "avoided" → **M30 Obedience**
- Psa 73:8 · 282514 — H7451 "malice" → **M03 Grief**
- Psa 12:4 · 272765 — H1396 "prevail" → **M23 Strength**
- Psa 105:2 · 269416 — H7878 "tell" (siach) → **M15 Wisdom**

M41 Remembrance (H8085, Psa 106:2 · 269636; Psa 26:7 · 276170) is **not** flagged outlier — treated as adjacent to Speech.

### 0.7 Uniform fields
- **D115 role = "characteristic" in all 42** — no qualifier, no standalone.
- **D105 bearer is `resolution:"inferred"` (flag) in all 42** — never a stated value; every bearer is inferred and self-looped, never a real link.
- All bearers are the human inner being (psalmist, worshippers, the healed/redeemed, saints, fathers/children, "we your people", the aged righteous, Moses, all mankind; and negatively the enemies, the wicked, foreigners, boasters, the false visitor). Screen 0 (memory `feedback_ib_screen_first_god_is_arena`) passes: God is the arena/object of the speech, not the bearer.

---

## 1. Coherence — does the label fit its data?

**Partly. The keyword grouping `speech-mouth-tongue` fuses (at least) three distinct inner-being movements, held together by lexical form (mouth/tongue/lips/verbs-of-saying) rather than one movement.** The 4 outlier flags (§0.6) already register the fusion. The three movements:

- **A — Testimony / proclamation of God (dominant, ~30 instances).** Coherent core: the outward voicing of the renewed, grateful, or delivered inner life (saphar, nagad, shama, basar, siach, hagah, dabar). This is the movement the label most nearly names.
- **B — Deceptive / evil / self-sovereign speech (~9 instances).** A counter-movement: speech as the mask or weapon of a split interior (mouth vs heart). Opposite valence to A; only the organ/verb keyword unites them.
- **C — Non-speech keyword-crossovers (~3 instances).** Grouped purely by surface word: Psa 22:15 · 275617 "dried up" (D102 = **state**: the tongue *physically* sticks to the jaws, bodily desiccation, not a speech act), Psa 17:4 · 274854 "avoided" (D102 = **volition**: M30 Obedience — avoidance, caught only by "word of your lips"), and the disciplinary Psa 141:3 · 308114 "guard over my mouth" (speech-*restraint*, distinct from both telling and deceiving).

So: one coherent dominant movement (A) with a genuine antithetical movement (B) and a residue of keyword-only crossovers (C). The label is a lexical family, not a single characteristic. This fusion is itself a first-class finding.

---

## 2. Movement A — Testimony: telling / declaring / recounting / proclaiming God's deeds

The family's centre of gravity. D102(type) = **action** (majority) or **volition** (vows: Psa 22:22 · 275671; Psa 145:6 · 274165; Psa 40:5 · 278347; Psa 26:7 · 276170; Psa 145:11 · 274049; Psa 35:28 · 277451). D106(operation) is consistently an *event* of telling-forth. Corrected D116(locus) is `external:god` (the deed is God's) or `external:person` (handed to the next generation).

Representative, all cited:
- **saphar (H5608)** — Psa 107:22 · 269935 · D101(sense) "tell (saphar)", D114(discovery) "testimony sung"; Psa 22:22 · 275671 · D106(operation) "the turn: the self vows to tell God's name… dereliction giving way to proclamation" (the psalm's hinge, D114); Psa 66:16 · 281288; Psa 71:15 · 282067 (D104 seat = "the mouth"); Psa 73:28 · 282479 · D114 "crisis resolved issuing in testimony"; Psa 78:3–6 · 306762 / 283199 / 283355 · the generational chain (fathers → coming generation → their children); Psa 102:21 · 268988; Psa 145:6 · 274165 · D114 "the interior overflows into public telling"; Psa 96:3 · 285574; Psa 118:17 · 271077 · D114 "the testimony the spared life exists for"; Psa 75:1 · 282701; Psa 79:13 · 283498 · "thanksgiving become transmission".
- **nagad (H5046)** — Psa 51:15 · 279685 · D104 seat "the mouth / opened lips", D114 "the outward voicing of the renewed inner life", D108 manner "with lips God has opened"; Psa 75:9 · 282765 · the **only D103(source)** = God the Judge; Psa 92:15 · 285190; Psa 92:2 · 285199; Psa 40:5 · 278347 · D114 "the interior cannot keep silent about deeds beyond counting"; Psa 71:17 · 282089 and Psa 71:18 · 282099 · lifelong witness "still going"; Psa 64:9 · 281156 · fear turning to testimony.
- **shama (H8085, M41)** — Psa 106:2 · 269636; Psa 26:7 · 276170 "proclaim thanksgiving aloud".
- **basar (H1319)** — Psa 96:2 · 285568 "tell of his salvation from day to day".
- **siach (H7878, M15 outlier)** — Psa 105:2 · 269416 "tell / muse on… worship as rehearsal".
- **hagah (H1897)** — Psa 71:24 · 282162 · D104 seat "the tongue", D114 "testimony as the constant murmur of the tongue (cf Ps 1:2)"; Psa 35:28 · 277451 "unceasing testimony".
- **dabar (H1696)** — Psa 145:11 · 274049 "tell the kingdom's glory".
- **mouth (H6310, T2)** — Psa 145:21 · 274133 · D102 **affect**: "my mouth will speak the praise… widening the self's praise to all creation".

Recurrent internal logic (from D106/D114): distress or deliverance **turns into** speech — the interior that cannot stay silent (Psa 40:5 · 278347; Psa 22:22 · 275671; Psa 73:28 · 282479; Psa 64:9 · 281156). Testimony is repeatedly coupled (corrected D112) with thanksgiving/joy/singing/praise (Psa 107:22 · 269935; Psa 75:1 · 282701; Psa 26:7 · 276170).

## 3. Movement B — Deceptive, evil, self-sovereign speech (the split interior)

Antithesis of A. D102(type) here is typically **cognition** — the source flags the *mind/heart* behind false speech. All bearers are the wicked/enemies (human IB, negatively).
- Psa 5:9 · 280756 · H3956 "tongue" · D114 "no truth in their mouth… their throat an open grave; they flatter with their tongue" — the smooth speech masks a death-dealing inside.
- Psa 28:3 · 276351 · H1696 "speak" · D101 "peace on the lips, evil in the heart"; D114 "the mouth offers peace, the heart hides harm".
- Psa 41:6 · 278469 · H1696 "utters" · "empty words, while his heart gathers iniquity" — hollow sympathy masking inner malice.
- Psa 144:8 · 274017 and Psa 144:11 · 273961 · H1696 "speak" · "whose mouths speak lies" (deliberately read as two: v8 states, v11 marks the deceit as the persisting reason for the cry, per D114).
- Psa 73:8 · 282514 · H7451 "malice" (M03 outlier) · D102 **status**; D108 manner "loftily"; the evil *ra* behind the words.
- Psa 12:4 · 272765 · H1396 "prevail" (M23 outlier) · D101 "'with our tongue we will prevail'"; D114 "the interior claims total ownership of its speech and denies any lord over it; pride located in the mouth" — autonomy, not deceit proper.
- Psa 106:33 · 307465 · H0981 "spoke rashly" (bata) · Moses at Meribah, "the one lapse that cost him the land" — negative speech from an embittered spirit (corrected D116 locus = "paired with the embittered spirit").

**Positive hinge inside B:** Psa 15:2 · 274621 · H1696 "speaks" · D101 "speaks truth in his heart", D114 "the interior itself is truthful; he does not lie even to himself" — the exact inverse of the mask (D102 cognition, but righteous). It belongs with B as its counter-pole (inner truthfulness vs inner duplicity), not with A's outward proclamation.

## 4. Movement C — Speech-discipline and non-speech crossovers

- **Speech-restraint:** Psa 141:3 · 308114 · H6310 "mouth" (T2) · D101 "guard over the mouth"; D106 "asking that the speech be sentried… the interior policing its own exits"; D102 **volition**. A distinct movement — governing the mouth, neither telling nor deceiving.
- **Obedient avoidance (keyword-only):** Psa 17:4 · 274854 · H8104 "avoided" (M30 Obedience outlier) · "by the word of your lips I have avoided the ways of the violent"; D102 volition. The characteristic is chosen non-participation; only "word/lips" pulls it into the family.
- **Bodily desiccation (keyword-only):** Psa 22:15 · 275617 · H3001 "dried up" (M-null) · D102 **state**; "my strength is dried up… my tongue sticks to my jaws" — physical collapse toward death, no speech-act at all; grouped solely by "tongue".

---

## The network (genuine pair edges only)

Per §0.2, only two genuine `pair` edges have **both endpoints inside this family**, and both fall within **Psalm 71**:
- Psa 71:17 · 282089 —D112(coupling)→ Psa 71:18 · 282099 (proclaim → proclaim; "continued in proclaiming to the next generation").
- Psa 71:24 · 282162 —D112(coupling)→ Psa 71:15 · 282067 (talk/hagah → tell/saphar; "the lifelong testimony").

These knit the four Ps 71 speech-spans (71:15 tell, 71:17 proclaim, 71:18 proclaim, 71:24 talk) into one small "lifelong-witness" cluster — the only intra-family sub-network the data supports. Every other genuine pair edge (Psa 66:16 · 281288→281292/281284; Psa 71:15 · 282067→282068/282081; Psa 73:28 · 282479→282482/282477; Psa 51:15 · 279685→279687; Psa 75:9 · 282765→282743/282766/282767; Psa 71:18 · 282099→282100/282097; Psa 75:1 · 282701→282703/282696; Psa 73:8 · 282514→282512; Psa 71:24 · 282162→282163; Psa 64:9 · 281156→281158/281159) points to spans **outside this file's scope** and so cannot be characterised here. **The family network is therefore extremely sparse and one-Psalm-local; there is effectively no cross-passage inner-being web in this dataset.**

---

## The interior anatomy the data actually names

Assembling only filled dimensions:
- **Seats (D104), 3 only:** the mouth (Psa 71:15 · 282067; Psa 51:15 · 279685), the tongue (Psa 71:24 · 282162). All are speech-organs; no interior faculty (heart/soul/spirit) is coded as seat anywhere.
- **The heart is named in the reading but never coded as a seat.** The mouth-vs-heart split — the source's central insight in Movement B — lives only in D101/D106/D114 prose (Psa 15:2 · 274621 "truth in his heart"; Psa 28:3 · 276351 "evil is in their hearts"; Psa 41:6 · 278469 "his heart gathers iniquity"). D104 leaves it "none". This is an uncoded seat.
- **Source (D103), 1 only:** Psa 75:9 · 282765 — God the Judge as the source of the declared word.
- **Couplings (D112, corrected):** testimony bound to thanksgiving/joy/singing/praise (A); deceit bound to the hidden heart/mask (B, e.g. "peace-mask" Psa 28:3 · 276351, "empty-words-heart-malice" Psa 41:6 · 278469).
- **Bearers (D105):** exclusively human IB, always inferred; positive speakers (the delivered/grateful/faithful, the generational chain) vs negative speakers (enemies, wicked, boasters, the false friend, Moses' lapse).

---

## What could not be derived from this source

1. **No source-of-motion (D103) for 41/42** — what *moves* the interior to speak is uncoded except once (Psa 75:9 · 282765).
2. **No interior seat for 39/42 (D104="none")**; the mouth/heart antithesis that the prose turns on is never captured in the seat dimension.
3. **No manner for 35/42 (D108="none").**
4. **D109 intensity, D110 specifier, D111 effect, D113 prohibition entirely absent** — the data cannot grade how strong, how qualified, to what effect, or whether prohibited; e.g. the "guard the mouth" restraint (Psa 141:3 · 308114) has no D113 prohibition coded despite being a restraint.
5. **26/42 instances carry no real cluster** (null, or T2-only) — the term-cluster cannot type the largest verb (saphar) or the bare organ-nouns.
6. **The D112/D116 swap (10 instances, §0.1)** makes coupling/locus unreliable at face value for those spans; corrected here but a data defect in the source.
7. **The network is uncharacterisable beyond Ps 71** — all other genuine edges leave the file's span-set, so the wider inner-being web is out of scope for isolation analysis.
8. **Movement fusion:** the family is a keyword grouping; whether A (testimony) and B (deceit) are one movement or two cannot be settled from within the file — the data shows opposite valence with only lexical form in common. Recorded as an open finding, not resolved.
9. **D105 bearer never stated, always inferred** — no instance gives the speaker as coded data; the human-IB attribution rests on inference throughout.

---

## Summary

`speech-mouth-tongue` in Psalms is, at core, one strong inner-being movement — **the interior that will not stay silent, turning deliverance and gratitude into the telling of God's deeds** (~30 of 42 instances; saphar/nagad/shama/basar/siach/hagah/dabar) — fused by keyword with a genuine **antithetical movement of deceptive, split-interior speech** (~9 instances; mouth-vs-heart), plus a residue of **speech-discipline and non-speech crossovers** (~3). The 4 flagged outliers (M30/M03/M23/M15) confirm the grouping is lexical, not a single characteristic. The evidence is thin on anatomy: seat filled 3×, source 1×, manner 7×, four dimensions wholly absent, 26/42 untyped by cluster, 10 instances field-swapped, and the inner-being network reduces to two edges inside Psalm 71.
