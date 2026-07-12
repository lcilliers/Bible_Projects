# Family analysis — `worship-prostration-service` (Psalms)

> Single-source analysis, in isolation. Source: `verse-analysis/psalms/_base-sources/psalms__worship-prostration-service.json`. Scope: 13 meanings · 25 instances · 20 passages · all genre `poetic/wisdom`. Every claim is cited `reference · span_id · Dnnn(label)`. Nothing outside the file is used.

## Roster (meaning → lemma → cluster → instances)

| # | char_key | meaning | lemma | cluster | inst | outlier |
|---|---|---|---|---|---|---|
| 1 | H7812:worship | worship | H7812 (shachah) | **null / T2** | 9 | no |
| 2 | H5647:serv | Serve | H5647 (abad) | M36 Service | 4 | no |
| 3 | H7812:bowdown | bow down | H7812 (shachah) | **null / T2** | 2 | no |
| 4 | H5401:kis | Kiss | H5401 | **null / null** | 1 | no |
| 5 | H3519:being | being | H3519 (kabod) | M22 Praise | 1 | **yes** |
| 6 | H7812:bow | bow | H7812 (shachah) | **null / T2** | 1 | no |
| 7 | H3766:bowdown | bow down | H3766 (kara) | **null / null** | 1 | no |
| 8 | H5753:bow | bowed | H5753 (avah) | M10 Sin | 1 | **yes** |
| 9 | H7817:broughtlow | brought low | H7817 (shachach) | **null / null** | 1 | no |
| 10 | H1288:kneel | kneel | H1288 (barak) | M39 Blessing | 1 | no |
| 11 | H7364:wash | wash | H7364 (rachats) | **null / null** | 1 | no |
| 12 | H5647:worship | worship | H5647 (abad) | M36 Service | 1 | no |
| 13 | H5647:worshiper | worshipers | H5647 (abad) | M36 Service | 1 | no |

---

## 0. Data-integrity screen

### 0.1 D112(coupling) / D116(locus) field-swap — 16 of 25 transposed
Correct order (per method) = D116 a code (`internal:`/`external:`), D112 a phrase. **16/25 instances are swapped** (code sits in D112, phrase in D116) and must be read corrected:

Swapped: `Psa 106:19 · span 269630`, `Psa 132:7 · span 272979`, `Psa 95:6 · span 285490`, `Psa 96:9 · span 285614`, `Psa 97:7 · span 285692`, `Psa 99:5 · span 285825`, `Psa 99:9 · span 285854`, `Psa 100:2 · span 268783`, `Psa 106:36 · span 269722`, `Psa 138:2 · span 273316`, `Psa 108:1 · span 270083`, `Psa 95:6 · span 285491`, `Psa 107:39 · span 270007`, `Psa 95:6 · span 285492`, `Psa 102:22 · span 268998`, `Psa 97:7 · span 285687` — each has `D112(coupling)` = an `internal:`/`external:` code and `D116(locus)` = a "paired with…" phrase. Read corrected: locus = the code, coupling = the phrase.

Correctly ordered (8): `Psa 66:4 · span 281344`, `Psa 86:9 · span 284378`, `Psa 22:30 · span 275757`, `Psa 2:11 · span 276502`, `Psa 81:9 · span 283879`, `Psa 2:12 · span 276507`, `Psa 38:6 · span 277984`, `Psa 26:6 · span 276164` — D116 holds the code, D112 the phrase.

One further case, not a swap: `Psa 45:11 · span 278898 · D112(coupling)` = `none`, `D116(locus)` = `external:person` (code in the correct slot, coupling empty).

### 0.2 Network edges — no genuine internal network
Every `edges[]` entry on D105(bearer), D107(target) and most D112(coupling) is `item_type:"flag"` + `resolution:"inferred"` with `to_span` = the span's own id and `from_span:null` — i.e. **self-loops, not links**. These are discarded for the network.

Only **2 genuine `pair` edges** (`resolution:"span"`, to a different span) exist, both emanating from `Psa 66:4 · span 281344`:
- `D103(source)` → span **281335** ("before God's awesome deeds (v3)").
- `D112(coupling)` → span **281345** ("paired with singing praises to his name").

Both target spans (281335, 281345) are **not present in this file**, so neither edge can be resolved within scope. Net effect: **the 25 family spans form no internal network**; the only real links point outside the dataset. One-directional, sparse, unresolvable here.

### 0.3 D104(seat) / D108(manner) = "none"
- **D104(seat) = "none" on all 25/25** instances. The interior locus of the act is never named — even where the verse text names the heart / whole self (`Psa 108:1 · span 270083 · D114`: "with all my being… my heart is steadfast").
- **D108(manner) = "none" on all 25/25** instances — despite manner-rich verse text ("with fear" Psa 2:11; "with gladness" Psa 100:2; "in the splendor of holiness" Psa 96:9; "with my whole heart" Psa 108:1/138:1). Manner is textually available but uncoded throughout.

### 0.4 Absent dimensions
Across all 25 instances: **D109(intensity), D110(specifier), D111(effect), D113(prohibition) are entirely absent.** D103(source) is present on **only 1** instance (`Psa 66:4 · span 281344 · D103(source)`). Notably D113(prohibition) is absent even where the verse states an explicit ban — `Psa 81:9 · span 283879` ("you shall not bow down to a foreign god"); the forbidden sense is carried only inside `D101(sense)` ("shachah, forbidden") and `D114(discovery)`, never as a prohibition flag.

### 0.5 Cluster null / T2
- **Null cluster: 16/25 instances** across 7 meanings. Of these, 12 carry `all_candidates = "T2(Supplementary)"` — the three shachah meanings (`H7812:worship` 9, `H7812:bowdown` 2, `H7812:bow` 1) — and 4 carry `all_candidates = null` (`H5401:kis` 1, `H3766:bowdown` 1, `H7817:broughtlow` 1, `H7364:wash` 1). The dominant term of the family (shachah, the actual "worship/prostration" verb) **cannot be typed by the term-cluster machinery** — it resolves only to T2 (supplementary/qualifier).
- Typed: M36 Service (6: `H5647:serv` 4 + `H5647:worship` 1 + `H5647:worshiper` 1), M22 Praise (1, outlier), M10 Sin (1, outlier), M39 Blessing (1). = 9/25.

### 0.6 Outliers (flagged in-file)
Two `is_outlier:true`, both with the same `outlier_note` (family expects M36 Service):
- `Psa 108:1 · span 270083` — `H3519:being` (kabod), cluster **M22 Praise**, `D102(type)` = **faculty**.
- `Psa 38:6 · span 277984` — `H5753:bow` "bowed" (avah, "to twist/pervert"), cluster **M10 Sin**, `D102(type)` = **state**.

### 0.7 Other data gaps
- `Psa 26:6 · span 276164` — `esv_word` is `null` (surface "wash" present).
- Meaning-level `evidence.stems` / `morph_codes` null for `H5401:kis`, `H3766:bowdown`, `H7817:broughtlow`, `H7364:wash`, `H3519:being` (instance-level morph is present).
- `is_passage_anchor:true` on only 2 instances: `Psa 86:9 · span 284378`, `Psa 108:1 · span 270083`.

---

## 1. Coherence — does the label fit the data?
**Partly.** The label's dominant sense (cultic homage / prostration to God) is well-borne, but the English-keyword grouping fuses **three distinct inner-being movements** and cuts across a direction axis. This is a first-class finding.

**(A) Homage / prostration before God** — the coherent core (~15 instances). shachah worship/bow before God (`Psa 66:4 · 281344`, `Psa 86:9 · 284378`, `Psa 95:6 · 285490`, `Psa 96:9 · 285614`, `Psa 99:5 · 285825`, `Psa 99:9 · 285854 · D101(sense)` "worship (shachah)"), abad serve the LORD (`Psa 100:2 · 268783`, `Psa 102:22 · 268998 · D101(sense)` "worship (abad)"), kara bow down + barak kneel (`Psa 95:6 · 285491`, `Psa 95:6 · 285492`), homage in kiss (`Psa 2:12 · 276507 · D101(sense)` "kiss the Son"), and approach-purity (`Psa 26:6 · 276164 · D101(sense)` "wash my hands in innocence"). All `D116(locus)`-corrected `external:god`, `D115(role)` characteristic.

**(B) The same posture mis-directed — idolatrous / forbidden / human-ward homage** (~5 instances). Same acts, wrong object: `Psa 106:19 · 269630 · D114` "worshiped a metal image"; `Psa 106:36 · 269722 · D114` "served (abad) their idols"; `Psa 97:7 · 285687 · D101(sense)` "worshipers of images (abad)"; `Psa 81:9 · 283879 · D101(sense)` "bow down (shachah, **forbidden**)"; `Psa 45:11 · 278898 · D116(locus)` = **external:person** (the bride bowing to the king, her human lord). Arguably the same movement (homage) at its negative/mis-aimed pole — the data separates it by object, not by act.

**(C) Affliction-prostration / abasement — a genuinely different movement** (2 instances, `D102(type)` = state, not action). Fused only by the English "bow(ed) down / brought low": `Psa 38:6 · 277984 · D101(sense)` "utterly bowed down, mourning all day" (avah, M10 Sin — the body folded by grief, `D114`: "the interior's mourning bends the whole frame") and `Psa 107:39 · 270007 · D101(sense)` "brought low (shachach)" (abasement "through oppression, evil, and sorrow"). These are involuntary bending under grief/oppression — **not worship** — and belong to a distinct inner movement.

**(D) Outlier self-in-praise.** `Psa 108:1 · 270083 · D101(sense)` "being (kabod)" — the whole self engaged in praise, `D102(type)` = **faculty** (M22 Praise). This is the *organ/whole-self* term, not a prostration act; it rides in on the family only via co-text.

**Verdict:** the family is coherent as **"the posture of homage"** and reads as one movement when (A) and (B) are held together on a God-vs-idol/person direction axis. But it **mis-includes movement (C)** — two grief-abasement *states* — and one whole-self praise *faculty* (D), which are not homage. Report these as fused-in, not native.

---

## 2. The movements / operations evidenced

### 2.1 shachah — worship / prostrate (the family spine; 12 instances, all null/T2)
`D101(sense)` "worship (shachah)" / "bow down (shachah)". Overwhelmingly `D102(type)` = action. Bearers (`D105`, all inferred, all self-loops): the corporate/universal congregation — "all the earth" (`Psa 66:4 · 281344`, `Psa 96:9 · 285614`), "all the nations" (`Psa 86:9 · 284378`), "the worshippers" (`Psa 95:6 · 285490`, `Psa 99:5 · 285825`, `Psa 99:9 · 285854`), "the people" (`Psa 132:7 · 272979`), "the gods / all" (`Psa 97:7 · 285692`), plus the negative bearers "the fathers" (`Psa 106:19 · 269630`) and "you (Israel)" forbidden (`Psa 81:9 · 283879`), the psalmist (`Psa 138:2 · 273316`) and the bride (`Psa 45:11 · 278898`). Movement: bodily homage/prostration, `D107(target)` God / footstool / holy mountain / temple — except the mis-aimed metal-image, foreign-god and human-lord targets. The verb never types to a cluster (T2 only) — the study machinery treats prostration as a *qualifier*, not a characteristic-cluster, though `D115(role)` = characteristic on every instance.

### 2.2 abad — serve / worship (6 instances, M36 Service)
`D102(type)` splits: **action** for present cultic service (`Psa 100:2 · 268783` "serve the LORD with gladness"; `Psa 102:22 · 268998` "worship (abad)"; `Psa 97:7 · 285687` worshipers-of-images, `D102` = status) but **volition** for the future/willed turn (`Psa 22:30 · 275757 · D102(type)` volition, `D106(operation)`: "posterity shall serve God… the praise carried forward in time"; `Psa 2:11 · 276502 · D114`: "the interior reorients from casting-off to serving; fear… the fitting posture of the once-rebellious"). abad thus carries the family's only explicit **volitional reorientation** — service as a chosen turning of the inner being from revolt to submission.

### 2.3 kara / barak — bow-down + kneel (2 instances, Psa 95:6)
Paired body-verbs at the same verse: `Psa 95:6 · 285491 · D101(sense)` "bow down (kara)" (null cluster) and `Psa 95:6 · 285492 · D101(sense)` "kneel (barak)" (M39 Blessing — lemma "to bless" repurposed as physical kneeling). `D116(locus)`-corrected external:god. Together with the shachah "worship" at the same verse (`285490`) this is the file's densest single-verse homage cluster (three postures in one line: worship + bow + kneel).

### 2.4 Volitional / preparatory homage (Psa 2 and Psa 26)
- `Psa 2:12 · 276507 · D101(sense)` "kiss the Son", `D102(type)` volition, `D114`: "the once-conspiring will now does homage" — homage embodied under threat of wrath.
- `Psa 26:6 · 276164 · D101(sense)` "wash my hands in innocence", `D102(type)` volition, `D106(operation)`: "approaching worship with a cleansed conscience" — the interior purification that *precedes* drawing near (`D114`: "clean conscience as the ticket to the altar").

### 2.5 Grief-abasement (Psa 38, Psa 107) — states, fused-in (see §1C)
`Psa 38:6 · 277984` and `Psa 107:39 · 270007`, `D102(type)` = state. Not volitional homage; the body bent by grief/oppression. Distinct movement.

### 2.6 Whole-self praise (Psa 108) — faculty, outlier (see §1D)
`Psa 108:1 · 270083 · D102(type)` faculty, `D106(operation)`: "worship with the whole self".

---

## 3. The network
- **No internal network** among the 25 family spans (see §0.2). All bearer/target/coupling edges are inferred self-loops.
- **2 genuine `pair` edges**, both from `Psa 66:4 · span 281344`: `D103(source)` → 281335 and `D112(coupling)` → 281345 — both targets absent from this file, hence unresolvable in scope. So the family's only real relational hooks reach *outside* the worship group (to a "God's-awesome-deeds" source-span and a "singing-praises" coupling-span at Psa 66), and cannot be described further here.

Consequence: the interior "web" the method seeks is, within this source, **flat** — 25 isolated homage-acts with no derivable span-to-span movement.

## 4. The interior anatomy actually named
Assembling only filled dimensions (seat and manner are void throughout):
- **Seat (D104):** none named anywhere (0/25). The interior organ of worship is unlocalised.
- **Locus (D116, corrected):** `external:god` for the God-ward homage core; `external:person` once (`Psa 45:11 · 278898`); `internal:ib-state` for the volitional/abasement/self cases (`Psa 2:11 · 276502`, `Psa 22:30 · 275757`, `Psa 2:12 · 276507`, `Psa 26:6 · 276164`, `Psa 38:6 · 277984`, `Psa 108:1 · 270083`, and — corrected from the swap — `Psa 106:19 · 269630`, `Psa 106:36 · 269722`, `Psa 107:39 · 270007`, `Psa 97:7 · 285687`).
- **Coupling (D112, corrected):** the phrase-couplings bind worship to adjacent cultic acts — "singing praises" (`Psa 66:4 · 281344`), "glorifying his name" (`Psa 86:9 · 284378`), "bowing and kneeling" (`Psa 95:6 · 285490`), "trembling before him" (`Psa 96:9 · 285614`), "exalting God" (`Psa 99:5 · 285825`, `Psa 99:9 · 285854`), "giving thanks" (`Psa 138:2 · 273316`), "the heart and singing" (`Psa 108:1 · 270083`), and to the will's states "serve-in-fear" (`Psa 2:11 · 276502`), "kiss-the-son" (`Psa 2:12 · 276507`), "wash-in-innocence" (`Psa 26:6 · 276164`).
- **Role (D115):** characteristic on all 25.
- **Type (D102) distribution:** action 17, volition 4, state 2, faculty 1, status 1.
- **Source (D103):** named once only — worship arising "before God's awesome deeds" (`Psa 66:4 · 281344`).

The anatomy the data *names* is therefore: an **outward, God-directed act (locus external:god)**, coupled to song/thanks/exaltation, occasionally arising from a willed interior turn (internal:ib-state) — but with **no seat, no manner, no intensity, and essentially no relational movement** recorded.

## 5. What could not be derived (from this source)
1. **Where worship sits in the interior** — D104(seat) void 25/25; not derivable even at heart-naming verses (Psa 108:1, Psa 86:11, Psa 138:1).
2. **How worship is performed** — D108(manner) void 25/25, though the verse text supplies manner ("with fear", "with gladness", "in the splendor of holiness", "with my whole heart"). A systematic miss.
3. **Intensity / specifier / effect / prohibition** — D109/D110/D111/D113 absent throughout; the explicit ban at Psa 81:9 is not coded as D113.
4. **What drives worship** — D103(source) present on 1/25 only.
5. **The inner-being network** — no resolvable span-to-span edges within scope; the 2 genuine pairs point to spans not in the file.
6. **Cluster typing of the core verb** — shachah (12 instances) resolves to T2/null only; 16/25 instances untyped.
7. **Corrected coupling/locus required** — 16/25 must be de-swapped before use (§0.1); an uncorrected read inverts internal/external for two-thirds of the data.
8. **Two members are not this movement** — `Psa 38:6 · 277984` and `Psa 107:39 · 270007` (grief-abasement states), plus outlier faculty `Psa 108:1 · 270083`, are fused in by keyword, not by shared inner motion.

## 6. Summary
The family is a broadly coherent **homage/prostration-before-God** movement — shachah (spine, but untypable/T2), abad service (M36, the only volitional reorientation), and paired body-postures kara/barak/kiss/wash — bound to song, thanks and exaltation and directed `external:god`. Its integrity is compromised by (a) a D112/D116 swap in 16/25 instances, (b) an essentially empty relational layer (no internal edges; 2 genuine pairs both point off-file), (c) blanket-void seat and manner despite textual support, and (d) keyword-fusion of two grief-**abasement states** (Psa 38:6; Psa 107:39) and one whole-self praise **faculty** (Psa 108:1) that are not the same inner movement. The clearest distinctions the data *does* carry are the **direction axis** (God vs idol/foreign-god/human-lord: Psa 106:19, 106:36, 97:7, 81:9, 45:11) and the **volitional turn** in abad/kiss (Psa 2:11, 2:12, 22:30, 26:6).
