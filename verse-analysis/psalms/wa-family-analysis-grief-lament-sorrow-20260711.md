# Family analysis — `grief-lament-sorrow` (Psalms, in isolation)

> Source: `outputs/data/psalms-family-base-sources/psalms__grief-lament-sorrow.json` only. Method: `_family-analysis-method-20260711.md`. Every claim cites `reference · span_id · Dnnn(label)` into that file. Counts declared in `meta`: 22 meanings · 31 instances · 29 passages. All 31 instances read; tallies below reconcile to 31.

---

## 0. Data-integrity screen

### 0.1 D112(coupling) / D116(locus) field-swap
Correct order = D116(locus) a code (`internal:`/`external:`), D112(coupling) a phrase. **9 of 31 instances are transposed** (D112 holds the code, D116 holds a prose phrase); read them corrected:

| span_id · ref | D112 (as stored) | D116 (as stored) | corrected: locus / coupling |
|---|---|---|---|
| 271014 · Psa 116:8 | `internal:ib-state` | "paired with the delivered soul" | locus=internal:ib-state / coupling=delivered soul |
| 272582 · Psa 126:5 | `internal:ib-state` | "paired with reaping in joy" | locus=internal / coupling=reaping-in-joy |
| 268981 · Psa 102:20 | `internal:ib-state` | "paired with being set free" | locus=internal / coupling=being-set-free |
| 273270 · Psa 137:1 | `internal:ib-state` | "paired with remembering Zion" | locus=internal / coupling=remembering-Zion |
| 307464 · Psa 106:33 | `internal:ib-state` | "paired with the spirit and rash words" | locus=internal / coupling=spirit+rash-words |
| 269033 · Psa 102:5 | `internal:ib-state` | "paired with the wasted flesh" | locus=internal / coupling=wasted-flesh |
| 270010 · Psa 107:39 | `internal:ib-state` | "paired with being brought low" | locus=internal / coupling=brought-low |
| 269049 · Psa 102:9 | `internal:ib-state` | "paired with eating ashes" | locus=internal / coupling=eating-ashes |
| 272587 · Psa 126:6 | `internal:ib-state` | "paired with coming home in joy" | locus=internal / coupling=coming-home-in-joy |

The remaining 22 instances carry D116 as a code already (correct order); e.g. `278543 · Psa 42:3 · D116(locus)=internal:ib-state`, `281705 · Psa 69:10 · D116(locus)=external:god`, `283211 · Psa 78:40 · D116(locus)=external:god`. Only **two** loci are ever `external:god` (281705, 283211); every other filled locus is `internal:ib-state`.

### 0.2 Self-loop "edges" are not real links
Every D105(bearer)/D107(target)/D104(seat)/D106(operation)/D108(manner) edge with `item_type:flag`+`resolution:inferred` has `from_span:null, to_span=<own id>` — these are self-loops, **not** network links. The genuine `pair` edges (`resolution:span`, to a different span) are only **11**, and **all 11 point OUTSIDE the family's own 31 spans** (no to_span matches any family span_id):

1. `280318 · Psa 56:8 · D103(source)` → 280317
2. `280318 · Psa 56:8 · D112(coupling)` → 280316
3. `280095 · Psa 55:17 · D112(coupling)` → 280094
4. `282961 · Psa 77:3 · D108(manner)` → 282959
5. `282961 · Psa 77:3 · D112(coupling)` → 282959
6. `278619 · Psa 42:9 · D103(source)` → 278616
7. `278644 · Psa 43:2 · D103(source)` → 278641
8. `281705 · Psa 69:10 · D112(coupling)` → 281709
9. `282871 · Psa 77:10 · D112(coupling)` → 282875
10. `281117 · Psa 64:3 · D112(coupling)` → 281107
11. `280125 · Psa 55:2 · D112(coupling)` → 280122

One further non-self flag edge exists but is **not** a genuine link by the rule: `281705 · Psa 69:10 · D104(seat)=flag,inferred` → 281706 (different span, but a flag not a pair) — excluded from the network; noted as an unresolved seat pointer to "the soul".

### 0.3 seat(D104) / manner(D108) = "none"
- **seat "none": 29 of 31.** Only two filled: `281705 · Psa 69:10 · D104(seat)=the soul (inferred)` and `281117 · Psa 64:3 · D104(seat)=the tongue (inferred)` — and the latter is the *enemies'* speech-organ, not a seat of grief. Grief is left seat-less even where the verse text names heart/spirit (e.g. `277999 · Psa 38:8` "tumult of my heart"; `307464 · Psa 106:33` "made his spirit bitter") — those go D104(seat)=none.
- **manner "none": 23 of 31.** Filled 8: 278543, 280318, 282961, 278619, 278644, 281705, 282871, 281117.

### 0.4 Absent dimensions
Across **all 31 instances**, these are entirely absent: **D109 intensity, D110 specifier, D111 effect, D113 prohibition.** Also **D103 source appears on only 3** instances (280318, 278619, 278644). D101 sense, D102 type, D105 bearer, D106 operation, D107 target, D112 coupling, D114 discovery, D115 role, D116 locus are present throughout; D104 seat and D108 manner present-but-mostly-"none" (0.3).

### 0.5 Cluster NULL / T2 — the term-cluster cannot type 6 instances
- **NULL cluster (code+candidates null): 3** — `280095 · Psa 55:17` & `282961 · Psa 77:3` (H1993 moan / hamah); `280125 · Psa 55:2` (H1949 moan / hum).
- **T2(Supplementary), code null: 3** — `278619 · Psa 42:9` & `278644 · Psa 43:2` (H6937 mourn / qadar); `277341 · Psa 35:14` (H6937 lament / qadar).

Note the significance: the very words that name the family — **"mourn"/"lament" (qadar) are T2, "moan" (hamah/hum) is NULL** — i.e. the label's own keywords are untyped by the term-cluster layer.

### 0.6 Outliers (`is_outlier:true`, 4)
Family expects M03(Grief); these carry a non-adjacent cluster:
- `307464 · Psa 106:33` bitter (marah) → **M30(Obedience)**
- `277999 · Psa 38:8` groan (sha'ag) → **M42(Speech)**
- `280660 · Psa 5:1` groaning (hagig) → **M15(Wisdom)**
- `276913 · Psa 32:4` heavy (kabed) → **M22(Praise)**

Non-outlier but non-M03 (adjacent, per file): `283211 · Psa 78:40` grieved (atsab) → M24(Weakness); `284514 · Psa 88:9` sorrow (oni) → M24(Weakness).

### 0.7 Bearer is always inferred
Every D105(bearer) is `resolution:inferred` — no bearer is textually explicit in the ledger. Bearers named: the psalmist (majority), David (278543, 278619, 278644), the sower(s) (272582, 272587), the people (283769, 270010), the exiles (273270), the prisoners (268981, 283471), the poor/needy (306021), the wicked (281117), Moses (307464), "they" (283211). All are human / human-group (Screen 0 passes: no instance makes God the bearer).

---

## 1. Coherence — does the label fit its data?

**Largely, with fusion.** 19 of 31 instances carry cluster **M03(Grief)** and form one coherent movement — the human interior in lament: weeping / tears / groaning / moaning / mourning / sorrow. The label `grief-lament-sorrow` fits this core.

But the keyword grouping has **fused four distinct movements** into the family:

1. **Lament/weeping core (dominant, ~24 instances).** The sufferer's own grief given voice or fluid: tears (5×, H1832), weeping (H1065/H1058/H1832), groaning (H0603/H0585/H7580/H1901), moaning (H1993/H1949), mourning (H6937), sorrow (H3015/H6040), appeal-as-grief (H2470). Bearer = the psalmist / afflicted people. This IS grief-lament-sorrow.

2. **Enemy malice aimed outward — not the sufferer's grief (1).** `281117 · Psa 64:3 · D101=bitter (mar), D105(bearer)=the wicked, D107(target)=the blameless, D104(seat)=the tongue` — venomous speech shot at the innocent. A hostility movement wrongly gathered under "grief" by the shared gloss "bitter".

3. **Human action that grieves God — God as recipient (1–2).** `283211 · Psa 78:40 · D101=grieve/pain (atsab), D105(bearer)=they, D107(target)=to God, D116(locus)=external:god` — rebels wounding God; the IB in motion is the rebels', God the one pained. Similarly `307464 · Psa 106:33` "they made his spirit bitter" — Moses embittered by the people (marah, M30 Obedience outlier). These are provocation/embittering, not lament.

4. **Cognition ABOUT grief, not instances of it (2).** `276619 · Psa 30:5 · D102(type)=cognition` — the settled insight "weeping tarries the night, joy at morning"; `273492 · Psa 139:24 · D102(type)=cognition, D101=grievous (otseb) way in me` — an invited interior self-audit for wrong. Both are reflective/volitional, gathered by the "griev-/weep-" surface, not felt sorrow.

**Finding:** the family is *grief-coherent at its M03 core* but the keyword net has pulled in (2) enemy-speech malice, (3) God-as-recipient provocation, and (4) reflective cognition — three movements distinct from lament (5 instances total; 281117, 283211, 307464, 276619, 273492).

---

## 2. The movements evidenced (cited)

### 2.1 Weeping / tears — grief made fluid
Tears (H1832, D101 sense "tears (dimah)") recur as the body's overflow: `271014 · Psa 116:8` (eyes delivered from tears), `272582 · Psa 126:5` (sow in tears), `278543 · Psa 42:3` (tears as food day and night, D108(manner)="his food day and night"), `280318 · Psa 56:8` (God bottles the tears; D103(source) pair→280317, D112(coupling) pair→280316), `283769 · Psa 80:5` (bread/drink of tears). Also beki `269049 · Psa 102:9` (mingled with drink), and the verbs bakah `273270 · Psa 137:1` (wept remembering Zion), `281705 · Psa 69:10` (wept + humbled soul, D104(seat)=the soul, D116(locus)=external:god), `272587 · Psa 126:6` (goes out weeping), and `281971 · Psa 6:6` (D101 "nightly weeping floods the bed", D102 affect). D106(operation) is uniformly "weep"; D107(target) inferred (e.g. "then be delivered" 271014, "at the memory of Zion" 273270).

### 2.2 Groaning / moaning — pre-verbal distress voiced
Groans/sighing: anaqah/enqah `268981 · Psa 102:20` (prisoners' groans God hears), `283471 · Psa 79:11` (groans come before God), the needy `306021 · Psa 12:5 · D106(operation)="the inarticulate groan that summons rescue"`; anachah `269033 · Psa 102:5` (loud groaning wears the bones); sha'ag `277999 · Psa 38:8` (groan from the heart's tumult, M42 outlier); hagig `280660 · Psa 5:1 · D101="groaning God is asked to consider", D106="a groaning too deep for words"` (M15 outlier). Moaning: hamah `280095 · Psa 55:17` (moan with complaint; D112 pair→280094) & `282961 · Psa 77:3` (moan when remembering God; D108 & D112 pair→282959); hum `280125 · Psa 55:2` (wordless moan of a heart in commotion; D112 pair→280122). Recurring D107(target)="before God" — the groan is Godward petition without words.

### 2.3 Mourning — going about darkly
qadar `278619 · Psa 42:9` & `278644 · Psa 43:2` (verbatim "why do I go mourning", D103(source) pairs→278616/278641 = the felt divine forgetting/rejection + enemy oppression); qadar as lament `277341 · Psa 35:14` (mourning enemies as kin, T2). D106(operation)="mourn".

### 2.4 Sorrow / grief-as-state
yagon `270010 · Psa 107:39` (the afflicted brought low); oni `284514 · Psa 88:9` (eye dims through sorrow, M24); challothi `282871 · Psa 77:10 · D101="grief / my appeal", D106="name the grief / resolve to appeal"` — the psalm's hinge: naming the wound pivots toward remembering God's deeds (D112 pair→282875).

### 2.5 The emergent grief→joy/rescue arc (from D114 discovery + corrected loci)
Repeatedly grief is coupled to a turn: `276619 · Psa 30:5 · D114` "weeping tarries the night, but JOY comes with the morning"; `272582/272587 · Psa 126:5-6 · D114` sow in tears → reap with shouts of joy; `271014 · Psa 116:8 · D114` "grief dried by deliverance"; `306021 · Psa 12:5 · D114` the groan "moves God to rise"; `268981 · Psa 102:20 · D114` groans → "set free"; `282871 · Psa 77:10 · D114` grief-named → "doorway to hope". This grief-seeds-deliverance movement is the strongest cross-instance pattern the discovery notes name.

### 2.6 The three non-lament intrusions (see §1)
Enemy bitterness `281117 · Psa 64:3`; humans grieving God `283211 · Psa 78:40` and embittering Moses `307464 · Psa 106:33`; reflective cognition `276619 · Psa 30:5` and self-audit `273492 · Psa 139:24`.

### 2.7 D102(type) spread and its inconsistency
Types used: state (~12), action (~9), affect (~4), status (~3), cognition (~2). No faculty/volition/disposition. **Typing is inconsistent for one phenomenon:** "tears" is typed *state* (271014, 272582, 283769) yet *status* (278543, 280318); weeping is *state* (273270, 272587), *affect* (281971), and *cognition* (276619). Flag as a data-quality note — the same grief-surface receives divergent D102 values.

---

## 3. The network (genuine pair edges only)
Eleven pair edges (§0.2), **all leaving the family** — there is **no intra-family link**; the grief instances do not connect to one another in the ledger. The network is sparse and outward-only:
- **Source pairs (what causes the grief):** 280318→280317 (God who bottles the tears, Psa 56:8); 278619→278616 & 278644→278641 (felt divine forgetting/rejection + enemy oppression, Psa 42:9 / 43:2).
- **Coupling pairs (what the grief is bound to):** 280318→280316 (restless tossings); 280095→280094 & 280125→280122 (the spoken complaint / restlessness, Psa 55); 282961→282959 (remembering God, Psa 77:3, also its manner); 281705→281709 (the mourning that became reproach, Psa 69:10); 282871→282875 (resolve to remember God's deeds, Psa 77:10); 281117→281107 (the secret plots, Psa 64:3).
- **Manner pair:** 282961→282959 (in remembrance of God).

Directionality: every pair has `direction:null` — orientation is not encoded. So the network gives *undirected, family-exiting* links only; it cannot show grief-to-grief progression internally.

---

## 4. The interior anatomy the data actually names
Assembling only filled fields:
- **Seats:** almost none. `the soul` (281705, Psa 69:10) and `the tongue` (281117, Psa 64:3, and that is the enemy's organ). Grief in this family is **seat-unnamed**; heart/spirit appear in verse text but not in D104.
- **Sources (D103, 3 only):** God who treasures the tears (Psa 56:8); the felt divine forgetting/rejection + enemy oppression (Psa 42:9 / 43:2). Grief's cause is elsewhere left to D114 prose, not the D103 field.
- **Couplings (corrected):** grief bound to deliverance/joy (116:8, 126:5-6), to the complaint/restlessness (55:2,17), to remembrance of God (77:3,10), to the wasted body (102:5), to being brought low / set free (107:39, 102:20).
- **Loci:** overwhelmingly `internal:ib-state`; `external:god` only twice (Psa 69:10 weeping-before-God; Psa 78:40 grieving God).
- **Operations (D106):** weep · groan · moan · mourn · suffer-sorrow · name-the-grief — the verbs of lament, present on every instance.
- **Bearers:** human throughout, but always inferred (§0.7).

---

## 5. What could not be derived (from this source)
1. **Intensity (D109), specifier (D110), effect (D111), prohibition (D113): absent everywhere** — grief's degree, its precise qualifier, its downstream effect, and any prohibition are not recorded for any of the 31 instances.
2. **Seat of grief: underivable for 29/31**, and even where the verse names heart/spirit the ledger sets D104=none. Where in the interior grief sits is essentially unrecorded.
3. **Source (D103) underivable for 28/31** — only 3 instances state what moves the grief.
4. **Manner underivable for 23/31.**
5. **Directionality of the network: null on every edge** — no grief-progression can be read off the pairs; and with zero intra-family links, this file alone cannot show how one grief-term relates to another.
6. **6 instances are cluster-untyped** (3 NULL, 3 T2, §0.5), including the label's own keywords mourn/lament (qadar) and moan (hamah/hum) — the term-cluster layer cannot confirm they belong to Grief from within this file.
7. **4 outliers** carry foreign clusters (M30/M42/M15/M22, §0.6); whether they are grief at all is contested by the term-cluster.
8. **D102(type) is internally inconsistent** for identical surfaces (§2.7) — the file cannot be trusted to type grief uniformly.
9. **9 instances need the D112/D116 correction** (§0.1) before their coupling/locus can be read; uncorrected, their locus reads as prose and coupling as a code.

---

## Summary
`grief-lament-sorrow` (Psalms): 22 meanings / 31 instances, coherent at its 19-instance **M03(Grief)** lament-core (weeping · tears · groaning · moaning · mourning · sorrow, bearer=the human sufferer, locus internal, operation=weep/groan/mourn), with a recurrent **grief→joy/rescue** arc; but the keyword net fuses in enemy-malice (Psa 64:3), human-grieving-God (Psa 78:40 / 106:33) and reflective cognition (Psa 30:5 / 139:24), the network's 11 genuine edges all exit the family (no internal links, direction null), grief is almost entirely **seat-less** and lacks intensity/specifier/effect/prohibition throughout, 9 instances need the D112/D116 swap corrected, and the label's own keywords mourn/lament/moan are cluster-untyped (T2/NULL).
