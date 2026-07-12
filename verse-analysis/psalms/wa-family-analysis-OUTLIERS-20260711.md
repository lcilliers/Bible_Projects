# Family analysis — OUTLIERS (genuine crossovers) · Psalms · 2026-07-11

> Source (read in isolation): `verse-analysis/psalms/_base-sources/psalms__OUTLIERS.json`.
> Scope `outliers-genuine-crossovers`. Counts (meta): **112 meanings · 158 instances · 111 passages**.
> This is **not a family** — it is a **cross-cut**: the collected set of meanings whose term-based CLUSTER names a concept *unrelated (non-adjacent)* to their meaning-based FAMILY. It is a view of the **seams** of the classification, where the meaning-lens and the term-lens disagree. Every record carries `is_outlier=true` and an `outlier_note` naming the family, the family's *expected* cluster, and the *actual* term-cluster (verified: all 112 present). No single inner-being movement is claimed or forced.

---

## 0. Data-integrity screen (done first)

Computed across all 158 instances.

- **D112(coupling)/D116(locus) field-swap — 36 instances transposed.** In these, D116 "locus" holds a prose phrase and D112 "coupling" holds an `internal:`/`external:` code — the reverse of the correct order (D116 = code, D112 = phrase). Read them corrected. The 36 (by reference): Psa 130:5 (×2, spans 272822/272825), 107:22, 126:2, 126:5, 126:6, 132:9, 102:1, 99:5, 99:9, 107:32, 118:28, 94:11, 105:3, 106:5, 89:41, 94:5, 101:5, 106:16, 105:22, 129:2, 106:33, 109:16, 101:4, 104:34, 117:1, 106:47, 109:25, 105:2, 107:26, 106:25, 123:4, 94:21, 106:6, 94:20, 108:1. (Example: `Psa 130:5 · span 272822` — D116=`"paired with the soul's waiting and hope"`, D112=`"external:god"`; corrected → locus `external:god`, coupling `paired with the soul's waiting and hope`.) The remaining 122 are in correct order.
- **Self-loop "edges" — 0.** No `flag`+`inferred` edge points at its own span. Every edge in this file is a genuine `pair`/`span` link to a *different* span.
- **Genuine network — 71 pair-edges only.** Of the relational ledger, 71 are real cross-span links: 43 D112 coupling, 10 D107 target, 7 D103 source, 7 D108 manner, 3 D104 seat, 1 D105 bearer. Sparse: 71 edges over 158 instances (< 0.5 per span), and coupling-dominated.
- **seat(D104)="none"/absent — 151 of 158.** Only **7** instances name an interior seat: Psa 71:23 the lips · 77:2 the soul (nephesh) · 52:2 the tongue · 63:3 the lips · 63:1 the flesh · 69:32 the heart · 73:13 the hands.
- **manner(D108)="none"/absent — 136 of 158** (22 filled).
- **Absent dimensions (all 158):** D109 intensity — **absent everywhere (0)**; D110 specifier — **absent (0)**; D111 effect — **absent (0)**. D103 source present on only **7**; D113 prohibition on only **1** (`Psa 44:17 · D113` = negated, "we have NOT been false to your covenant"). D101 sense, D102 type, D104, D105 bearer, D106 operation, D107 target, D108, D112, D114 discovery, D115 role, D116 present on all 158 (values may be "none").
- **Cluster NULL / T2 — 0.** *No* outlier lands in a null or T2 cluster: the term-lens **always** assigns a concrete M-cluster, even for a meaning it clearly mis-fits (see §2d). There is no abstention escape-hatch — a keyword-slip meaning still receives a confident (wrong-for-the-reading) cluster. Flag this as a structural limitation of the term-lens, not a data gap.
- **role(D115) — uniform:** all 158 = `characteristic` (no qualifier/standalone in this cut).
- **bearer(D105):** the psalmist 65, the wicked 8, the enemies 7, the hearer 4, the worshippers 4, the people 3, the righteous 3, plus smaller groups — all human IB bearers; none is God's own attribute.

---

## 1. Coherence — does the label fit?

By design **no**, and that is the finding: `meta.scope.set = outliers-genuine-crossovers` is a **seam-cut, not a movement**. The 112 meanings span **30 distinct meaning-families** and land in **~34 distinct term-clusters**. The file must be read *as* disagreement, not as a coherent inner-being arc. The two lenses are:

- **meaning-lens (family):** the read sense of the word in the verse, grouped by an ESV-keyword family.
- **term-lens (cluster):** master → 1 mti_term → 1 M-code cluster, driven by the lemma's dominant term-sense.

The interesting object is *where they pull apart*. §2 groups the pull-apart by family and by cluster; §3 names the mechanisms.

---

## 2. The disagreements — grouped

### 2a. By meaning-family (where the outliers come FROM)

Meanings per family (instances in brackets): praise-extol-sing 10(17) · desire-longing-appetite 9(11) · knowing-understanding 8(10) · hope-waiting 7(17) · joy-gladness 5(13) · trust-refuge-security 5(7) · wickedness-ungodliness 5(5) · prayer-petition-crying-out 4(7) · rebellion-stubbornness 4(7) · restoration-revival-satisfaction 4(6) · malice-enmity-persecution 4(5) · righteousness-integrity 4(5) · grief-lament-sorrow 4 · humility-lowliness-contrition 4 · inner-seat-heart-soul-spirit 4 · speech-mouth-tongue 4 · shame-confusion 3(6) · violence-cruelty 3(5) · anger-wrath-vexation 3 · faint-despair-languishing 3 · then 10 families with 1–2 meanings each (confession-forgiveness, deceit-falsehood, fear-of-god-awe, pride-arrogance-scoffing, worship-prostration-service, blessing, faith, strength, torah, wisdom).

The families that **leak most** are the large affect/utterance families (praise, joy, desire, knowing, hope) — precisely those whose head-words are high-polysemy Hebrew roots.

### 2b. By term-cluster (where the outliers LAND — the attractor clusters)

Meanings per actual cluster: **M42 Speech 10** · **M03 Grief 9** · **M15 Wisdom 7** · **M17 Counsel 6** · **M33 Peace 6** · M08 Pride 5 · M10 Sin 5 · M22 Praise 5 · M20 Doubt 4 · M30 Obedience 4 · M23 Strength 4 · M06 Hate 3 · M18 Hope 3 · M02 Anger 3 · M01 Fear 3 · M47 Constitution 3 · M29 Desire 3 · M26 Righteousness 3 · (rest 1–2).

Five **attractor clusters** absorb the bulk, each on a characteristic mechanism:

- **M42 Speech ← joy / knowing / grief / deceit / malice / confession.** Vocalised interior acts collapse onto the *utterance* verb. Chief donors: `ranan`/`rinnah` (joy→speech, 5 records — H7442 `joy`/`rejoice`/`glad`, H7440 `joy`/`glad`; e.g. `Psa 132:9 · span 272991 · D114` "let your saints SHOUT FOR JOY (ranan)… joy bursting into shout") and `hagah` (H1897 `meditat`/`ponder`, knowing→speech; `plot`, malice→speech; gloss "to mutter"). Also `shaag` groan (H7580), `nagad` tell/confess (H5046), `latsan` slander (H3960).
- **M03 Grief ← prayer / inner-seat / knowing / anger / speech / wickedness / hope.** Donors `siach` (H7879 `complaint`/`meditation`, gloss "complaint"), `ra'` (H7451 `malice`/`troubles`, gloss "bad/harm/evil"), `chul` (H2342 `wait`, gloss "to twist: writhe/tremble"), `tsarah` troubles (H6869), `yagah` provoked (H8428).
- **M15 Wisdom ← malice / prayer / speech / trust / grief / knowing.** Cognition/devising verbs read as plotting or perceiving: `chashab` devise (H2803 `plots`), `aram` be shrewd (H6191 `crafty`), `yaats` advise (H3289 `conspire`), `siach`/`siyach` muse (H7878 `complaint`/`tell`), `taam` perceive (H2938 `taste`).
- **M17 Counsel ← hope / malice / fear.** Dominated by `qavah` (H6960 `wait`/`hope`/`look`, 11+1+1 instances, gloss "to await; to collect") and `sabar` (H7663 `hope`, "to await; to inspect"); plus `sod` (H5475 `secret plots` malice→counsel, `friendship` fear→counsel, gloss "counsel"). The single largest meaning in the file — H6960 `wait`, 11 instances — sits here: waiting/hope termed **Counsel**, expected **M18 Hope**.
- **M33 Peace ← praise / restoration / trust.** Almost entirely `shabach` (H7623 `praise`/`Extol`/`commend`/`glory`, gloss "to soothe") — praise clustered Peace via the soothe-sense; plus `nocham` comfort (H5165) and `shalem` close (H7965).

### 2c. The dominant family→cluster edges (by meaning count)

4× hope-waiting→M17(Counsel) · 4× joy-gladness→M42(Speech) · 4× praise→M08(Pride) · 4× praise→M33(Peace) · 3× rebellion→M20(Doubt) · 3× shame-confusion→M06(Hate) · 3× desire→M18(Hope) · 3× desire→M02(Anger) · 2× prayer→M03(Grief) · 2× knowing→M42(Speech) · 2× malice→M15(Wisdom) · 2× desire→M47(Constitution) · 2× inner-seat→M03(Grief) · 2× wickedness→M26(Righteousness). These recurring edges are the *seams* — the same lens-disagreement firing on a shared lemma.

### 2d. Cluster forced onto an ill-fitting meaning (the "no-abstention" cases)

Because the term-lens never returns null/T2 (§0), some meanings receive a confidently *wrong-for-the-reading* cluster — the FAMILY membership, not the cluster, is the error (keyword slip), yet the cluster still commits:

- `Psa 90:10 · H0205 'trouble' · cluster M10(Sin)` inside **praise-extol-sing** family — `aven` (iniquity/trouble; `Psa 55:3 · span 280176 · D114` "they drop TROUBLE (aven) upon me"). The praise-family membership is a surface-keyword slip; M10 Sin is the true home.
- `H8668 'salvation' · M38(Salvation)` inside **wickedness-ungodliness** family (expected M27 Evil); `H7451 'troubles' · M03(Grief)` same family — the wickedness family absorbed a salvation word and a harm word; the cluster is right, the family loose.
- `H5766 'wrong' · M10(Sin)` inside **righteousness-integrity**; `H0898 'faithless' · M10(Sin)` inside **faith-faithfulness-truth**; `H5647→H5753 'bow' · M10(Sin)` inside **worship-prostration-service** (`awah`, gloss "to twist; to pervert"). In each the term-cluster names the moral fact correctly and the meaning-family is the over-reach.

---

## 3. The recurring reasons the two lenses diverge (as the data shows them)

Every record's `evidence.lexical_gloss` (attested inventory) and `D114` discovery-note supply the mechanism. Four recur; there is **no fifth-category null/T2** (see §0).

**(i) Homograph / single-lemma polysemy — the largest driver.** One lemma carries two attested glosses; the read sense gives the family, a *different* gloss gives the cluster.
- `halal` H1984, gloss "to shine; …to boast: praise; to boast: boast; rave madly": `glory`/`exult` (praise & joy families) → **M08 Pride** via the boast-sense (`Psa 63:11 · span 281035 · D114` "all who swear by him shall EXULT (halal)").
- `rum` H7311, gloss "to exalt; be rotten": `exalt`/`extol`/`higher`/`Exalt` (praise) → **M08 Pride** via be-high (`Psa 99:5 · span 285822 · D114` "let not the rebellious EXALT (rum) themselves").
- `nephesh` H5315, gloss "soul: appetite; soul; life; …": `craved`/`pleasure` (desire) & `courage` (strength) → **M47 Constitution** — the lemma *is* 'soul' (`Psa 78:18 · span 283056 · D114` "the food they CRAVED (nephesh) — the soul-appetite").
- `hagah` H1897 "to mutter" → **M42 Speech** for meditate/ponder (knowing) and plot (malice).
- `ranan`/`rinnah` H7442/H7440 "cry / to overcome; to sing" → **M42 Speech** for joy (5 records) — the joyful *shout*.
- affect-swaps that are really homographs: `ragaz` H7264 "to tremble" → **M01 Fear** though read `angry` (anger family); `gur` H1481 "to dread; to sojourn; to quarrel" → **M01 Fear** though read `strife` (violence); `qinah`/`qanah` H7068/H7065 "jealousy / be jealous" → **M02 Anger** though read `zeal`/`envious` (desire).

**(ii) Keyword false-positive (meaning-family membership is the error).** The ESV surface word pulled the record into a family it does not belong to; the term-cluster is correct. Clearest: `aven` 'trouble' in praise-family (§2d); `shamar` H8104 "to keep: obey/guard" read `Mark`/`avoided` in knowing & speech families → **M30 Obedience**; 'salvation'/'faithless'/'wrong'/'bow' in §2d. Here the *family* keyword, not the cluster, is the mis-grouping.

**(iii) Genuine adjacent-concept crossover (both lenses defensible; the act truly straddles).** The interior act legitimately belongs to two movements.
- `siach` H7879/H7878 (complaint / muse / meditation) genuinely straddles **grief · prayer · wisdom** — read `complaint` in prayer & grief, `meditation`/`tell` in knowing, landing in M03 and M15 (`Psa 102:1 · span 268894 · D114` "pours out his COMPLAINT (siach)… grief laid before God").
- `qavah` H6960 (await/hope) → **M17 Counsel**: waiting-as-hope vs the collect/gather term-sense; 11 instances, the file's largest crossover.
- `nacham` H5162 (comfort / be sorry / relent) → **M05 Love** in restoration-family — genuinely straddles comfort · repentance.
- `shuv`/`chayah` revive H7725/H2421 → **M45 Transformation** / **M25 Life** in restoration-family — restoration truly overlaps return and life.

**(iv) T2 / null cluster — none present.** Flag positively: the term-lens issued *zero* null/T2 verdicts across 158 crossovers. Where a meaning genuinely defies its family (e.g. 'salvation' inside wickedness), the lens still forces a concrete cluster rather than abstaining — so mechanism (ii) and mechanism (iv) never co-occur; the false-positive is *masked* by a confident cluster rather than surfaced as unclassifiable.

---

## 4. The network (genuine pair-edges only)

71 real cross-span links (self-loops excluded, §0), coupling-heavy (43/71). They bind an outlier span to a neighbour in the *same verse's* arc, not across the cut — e.g. `Psa 52:9 · span 279870` couples to span 279866 (D112), sources from 279873 (D103), targets 279871 (D107); `Psa 71:23 · span 282154` sources from 282159 (D103, "his soul which God has redeemed") and couples to 282156 (D112). The network says nothing about the *classification* seam — it is local verse-internal welding — and is too sparse (<0.5 edges/span, only 3 seat and 1 bearer edge) to carry an inner-being anatomy on its own.

## 5. The interior anatomy the data actually names

Thin, because this cut is defined by the *lens disagreement*, not by rich interior filling. Only the **7 named seats** (§0: lips ×2, tongue, flesh, heart, hands, soul/nephesh) and **7 named sources** (all God-referential: God's name is good `Psa 52:9`, God's steadfast love `Psa 63:3`, the soul God redeemed `Psa 71:23`, etc.) are attested. D109/D110/D111 give nothing. Type(D102) skews to **action (54)** and **state/status (50)** over affect (20)/volition (12)/cognition (8)/faculty (5) — consistent with the donors being *verbs of doing/uttering* (shout, mutter, exalt, plot) whose action-sense is exactly what the term-lens keys on.

## 6. What could not be derived

- **Intensity (D109), specifier (D110), effect (D111): entirely absent** — no gradation, no scope-narrowing, no downstream effect recoverable for any of the 158.
- **Seat unstated on 151/158, manner on 136/158, source on 151/158** — the interior locus of most crossover acts is simply not given here.
- **The D112/D116 swap** must be corrected on 36 instances before any locus/coupling reading (§0); uncorrected they read backwards.
- **No null/T2 signal** — the file cannot show *which* crossovers the term-lens found genuinely hard, because it never abstains; hardness is inferable only from the family↔cluster distance, not from a cluster flag.
- The **why** behind each specific mti_term→cluster assignment (e.g. why `qavah` sits in M17 Counsel rather than M18 Hope) is not in this file — `all_candidates` shows a single candidate per record, so the term-lens decision is opaque here.

---

## 7. Summary

This is the **seam-set of the Psalms classification**: 112 meanings / 158 instances where the meaning-lens (family) and the term-lens (cluster) disagree, spanning 30 families → 34 clusters — not one movement. The disagreement is dominated by **single-lemma polysemy (homographs)** (halal→Pride, rum→Pride, ranan→Speech, hagah→Speech, nephesh→Constitution), with **utterance verbs collapsing to M42 Speech**, **devising/musing verbs to M15 Wisdom**, and **qavah/sabar (wait/hope) to M17 Counsel** as the three sharpest recurring seams; a minority are true adjacent crossovers (`siach` grief↔prayer↔wisdom) or meaning-family keyword slips masked by a confident cluster (`aven` 'trouble', 'salvation'-in-wickedness). Data-integrity: 36 D112/D116 swaps to correct, 0 false self-loops, 71 sparse local pair-edges, seat/manner/source almost entirely "none", D109/D110/D111 wholly absent, and **zero null/T2** — the term-lens never abstains, so it masks rather than flags the cases it fits worst.
