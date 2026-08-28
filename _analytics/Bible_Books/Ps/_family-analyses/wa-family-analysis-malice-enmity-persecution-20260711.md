# Family analysis — `malice-enmity-persecution` (Psalms), in isolation

> Source: `verse-analysis/psalms/_base-sources/psalms__malice-enmity-persecution.json` only. Scope `meta.scope.family = "malice-enmity-persecution"`. Counts (meta): **26 meanings · 56 instances · 35 passages**. Every claim cites `reference · span_id · Dnnn(label)` into that file. Method: `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md`.

---

## 0. Data-integrity screen (done first)

**0.1 D112(coupling)/D116(locus) field-swap — 22 of 56 instances are transposed.** The correct order is D116 locus = an `internal:`/`external:` code and D112 coupling = a prose phrase. In 22 instances the code sits in D112 and the phrase in D116, so they must be read swapped. The 22 (each `reference · span_id`): Psa 101:3·268831, Psa 105:25·269448, Psa 118:7·271180, Psa 120:6·272320, Psa 129:5·272715, Psa 97:10·285631, Psa 109:20·270239, Psa 109:29·270287, Psa 109:17·270204, Psa 109:18·270213, Psa 109:28·270280, Psa 106:41·269759, Psa 109:5·270329, Psa 106:42·269763, Psa 129:3·272702, Psa 129:3·272703, Psa 109:4·270321, Psa 109:6·270336, Psa 105:25·269451, Psa 109:3·270296, Psa 103:6·269189, Psa 109:16·270198. In every case the true D116(locus) code is `internal:ib-state` and the true D112(coupling) is the "paired with…" phrase. All figures below use the corrected reading. The remaining 34 instances are in correct order (D116 a code, D112 a phrase or `none`).

**0.2 Self-loop "edges" are not network.** The file carries **158** flag-edges of the form `item_type:"flag"` + `resolution:"inferred"` whose `to_span` equals the span's own id (the D105/D107/D112 inferred flags echoed as edges). These are self-loops, **not** links. Only genuine `pair`/`resolution:"span"` edges to a *different* span are network (§ "The network").

**0.3 seat(D104)/manner(D108) = "none".** Seat is unfilled in **54 of 56** — only Psa 62:4·280962·D104(seat)=`inwardly / the heart` and Psa 52:2·279806·D104(seat)=`the tongue`. Manner is unfilled in **48 of 56**; the 8 filled are listed in §5.

**0.4 Absent dimensions — across ALL 56 instances.** D109(intensity), D110(specifier), D111(effect), D113(prohibition) are **absent from every instance** (0/56 present). D103(source) is present in only **3** (Psa 68:1·281446, Psa 69:4·281864, Psa 64:2·281107).

**0.5 Cluster NULL / T2.** No T2. **15 instances carry a NULL term-cluster** (`cluster.code = None`) — the term-cluster cannot type them: Psa 109:17·270204, Psa 109:18·270213, Psa 109:28·270280 (curse H7045/H7043); Psa 62:4·280962 (curse); Psa 106:42·269763, Psa 56:1·280224 (oppress H3905); Psa 103:6·269189, Psa 119:121·271354, Psa 119:122·271360 (oppress H6231); Psa 55:11·280043 (oppression H8496); Psa 109:6·270336 (accuser H7854); Psa 105:25·269451 (deal-craftily H5230); Psa 10:9·306005 (lurk H0693); Psa 89:22·284629 (outwit H5377); Psa 109:16·270198 (pursue H7291). The entire oppression / cursing / pursuit / ambush stratum is essentially **unclustered** — the M-code layer only types the hatred core.

**0.6 Other integrity notes.** Bearer(D105) is `resolution:"inferred"` in **all 56** — no bearer is stated on the span. Role(D115) = `characteristic` in **all 56** (no qualifier/standalone). One instance carries a null `esv_word`: Psa 139:21·273472.

---

## 1. Coherence — does the label fit? (first-class finding)

**The family label fuses at least five distinct inner-being movements.** The keyword grouping "malice-enmity-persecution" has swept together dispositions, affects, cognitions and actions that do not form one movement. Grouped by cluster + lemma:

1. **Hatred / enmity (affect–disposition)** — cluster **M06(Hate)**, ~30 instances: `sane` H8130 (23; e.g. Psa 139:22·273476·D101=`hate (sane) with completeness`), `sinah` H8135 (Psa 109:5·270329, Psa 139:22·273478, Psa 109:3·270296), `satam` grudge H7852 (Psa 55:3·280179·D101=`bear a grudge / cherish enmity (satam)`), `satan`-accuse H7853 (Psa 109:4·270321, 109:20·270239, 109:29·270287). This is the label's true centre — a felt aversion/enmity.
2. **Scheming / plotting (cognition–craft)** — the **outliers**: `chashab` H2803 M15(Wisdom) (Psa 36:4·277532·D101=`he plots trouble on his bed`, Psa 52:2·279806), `aram` H6191 M15(Wisdom) (Psa 83:3·283994), `hagah` H1897 M42(Speech) (Psa 2:1·276494·D101=`peoples plot in vain`), `sod` H5475 M17(Counsel) (Psa 64:2·281107), plus M14(Deceit) `chephes` H2665 (Psa 64:6·281141) and `nakal` H5230 (Psa 105:25·269451). A cognitive/deceptive movement, not enmity-as-affect.
3. **Cursing (verbal malice)** — NULL-cluster H7045/H7043 (Psa 109:17·270204, 109:18·270213, 109:28·270280, 62:4·280962·D101=`curse (qalal - inwardly they curse)`).
4. **Oppression / persecution (action–status against the sufferer)** — NULL-cluster: `lachats` H3905 (Psa 106:42·269763, 56:1·280224), `ashaq` H6231 (Psa 103:6·269189, 119:121·271354, 119:122·271360), `tok` H8496 (Psa 55:11·280043), `radaph` pursue H7291 (Psa 109:16·270198), `arab` lurk H0693 (Psa 10:9·306005·D101=`lurks like a lion to seize`), `charash` plow H2790 M14 (Psa 129:3·272702, 272703), `nasha` outwit H5377 (Psa 89:22·284629).
5. **Accusation (adversarial/legal)** — `satan` H7853/H7854 (Psa 109:6·270336·D101=`accuser (satan)`, 109:20·270239, 109:29·270287).

**A second, orthogonal split cuts through movement 1**: the same lemma `sane` is read as **righteous aversion** (the IB hating evil) in Psa 101:3·268831 (bearer David), Psa 119:104·271237 / 119:113·271295 / 119:128·271377 / 119:163·271607, Psa 26:5·276157·D101=`hate the assembly of evildoers`, Psa 45:7·278987 (the king hating wickedness, D107 target=`wickedness`/span), Psa 97:10·285631 (bearer `those who love God`), Psa 139:21·273471 / 139:22·273476, **and** as **malicious enmity** (the wicked hating the psalmist/God/people/Zion) in the majority (e.g. Psa 118:7·271180, Psa 129:5·272715, Psa 83:2·283991, Psa 89:23·284638, Psa 105:25·269448). One keyword therefore fuses a virtue and its opposite. This is the sharpest coherence finding: the family is not one movement but a **relational field of hostility** whose valence (righteous vs malicious) is fixed only by bearer/target, not by the term.

---

## 2. The core movement — hatred/enmity as disposition→affect (M06)

**Type is context-read, not lemma-fixed.** Across the 56 the D102(type) split is: disposition 19, action 19, status 11, affect 4, cognition 2, volition 1. The single lemma `sane` (H8130) alone is typed **disposition** (Psa 101:3·268831·D102=`disposition`), **affect** (Psa 139:21·273471·D102=`affect`), **action** (Psa 44:7·278847·D102=`action`) and **status** (Psa 68:1·281446·D102=`status`). The data reads the *same enmity* now as settled bent, now as felt heat, now as deed, now as standing condition — a first-class observation that "hatred" in this corpus is a movement crossing the disposition/affect/action/status boundary rather than one fixed faculty-type.

**Hardening from act to owned state.** Psa 139:22·273478·D114(discovery) reads sinah as "the aversion has hardened from act into a fixed, owned disposition" (D101=`hatred (sinah) as settled state`), and Psa 139:22·273476·D106(operation)=`the hatred is brought to total, unqualified completeness - no reservation left`. The interior is shown totalising and setting its own aversion.

**Loyalty-aversion (bind to God's cause).** Psa 139:21·273471·D106(operation)=`the psalmist's aversion binds itself to God's cause - hating those who hate God`; its counter-span Psa 139:21·273472·D106 reads the enemies' own hatred "DIRECTED at God". The movement here is the IB fastening its hatred onto an allegiance (D114·273471: "the interior fastens its hatred to God's enemies as an extension of allegiance").

**Aversion-as-separation.** Psa 26:5·276157·D106(operation) reads the enmity as chosen distancing — "the interior refuses the fellowship of the corrupt" (D114·276157), D107(target)=`separation`.

---

## 3. The scheming movement — cognition/craft (outliers + Deceit)

The interior is shown **devising**: Psa 2:1·276494·D102(type)=`cognition`, D106(operation)=`the raging becomes scheming - the peoples devise a plot, though it is empty/vain`; Psa 36:4·277532·D102=`cognition`, D106=`he plots trouble while on his bed … scheming in the place of rest`. Craft is read at Psa 83:3·283994·D101=`crafty (aram)`, Psa 105:25·269451·D101=`deal craftily (nakal)`, Psa 64:6·281141·D101=`diligent search / plot (chephes)`, Psa 64:2·281107·D101=`secret plot / council (sod)`. That this stratum arrives as **outliers** (is_outlier=true for H2803, H6191, H1897, H5475) confirms §1: scheming is a neighbouring movement drawn in by keyword, not native to the hatred cluster.

## 4. The persecution/oppression movement — action on a sufferer

Predatory action: Psa 10:9·306005·D102(type)=`volition`, D106=`he lurks in ambush like a lion … patient predation`; Psa 109:16·270198·D101=`pursue (radaph)`, D107(target)=`the poor and needy to death`; Psa 129:3·272703·D101=`plow (charash)`, D107=`long furrows on the back`. Oppression as action/status: Psa 56:1·280224·D101=`oppress / crush (lachats)`, Psa 103:6·269189·D102=`status`, D101=`oppressed (ashaq)` (the *sufferer's* side), Psa 55:11·280043·D101=`oppression (tok - oppression and fraud)`. These are largely **NULL-cluster** (0.5) — the term layer does not type them.

## 5. seat · source · manner — the little the data fills

- **Seat (D104)** filled twice only: Psa 62:4·280962·D104=`inwardly / the heart` (curse read as inward reality beneath outward blessing — D114·280962: "the true reality beneath the outward blessing") and Psa 52:2·279806·D104=`the tongue` (plotting located in the organ of speech).
- **Source (D103)** filled 3×, all by God's answering act: Psa 68:1·281446·D103=`scattered when God arises (v1)`; Psa 69:4·281864·D103=`on whom God's indignation is asked to fall (v24)`; Psa 64:2·281107·D103=`at which God shoots his arrow (v7)`. The enmity's "source" the data records is not its origin but its *terminus in divine judgement*.
- **Manner (D108)** filled 8×: Psa 69:4·281864=`more in number than the hairs of his head`; Psa 62:4·280962=`inwardly, secretly`; Psa 56:1·280224=`all day long`; Psa 52:2·279806=`like a sharpened razor`; Psa 55:3·280179=`in anger`; Psa 55:11·280043=`never departing the marketplace`; Psa 64:6·281141=`diligent, thorough`; Psa 64:2·281107=`in secret`. Manner clusters on **secrecy, ceaselessness, and sharpness**.

## 6. The network (genuine pair edges only)

Only **19 genuine `pair`/`resolution:"span"` edges** exist, on **12 of 56 instances** (21%). Every one links **outward to a span that is not a master in this family** (companion words in the same verse — e.g. `279537`, `281443`, `281509`); **no master links to another master in this family**. The network is therefore **sparse and one-directional**, with no internal family cross-linking. The genuine edges (`from_span → to_span · Dnnn`):

- Psa 50:17·279536 → 279537 · D107(target=discipline) and D112(coupling) — hatred of discipline welded to "casting God's words behind him".
- Psa 68:1·281446 → 281443 · D103(source), → 281509 · D112(coupling=`paired with the wicked who perish`).
- Psa 69:4·281864 → 281785 · D103(source), → 281869 · D112(coupling=`paired with those who attack with lies`).
- Psa 62:4·280962 → 280959 · D112(coupling — the inward curse under the outward blessing).
- Psa 45:7·278987 → 278988 · D107(target=wickedness), → 278985 · D112(coupling=`paired with loving righteousness`).
- Psa 56:1·280224 → 280220 · D112(coupling=`paired with the trampling`).
- Psa 52:2·279806 → 279807 · D107(target=destruction) and D112(coupling).
- Psa 55:12·280054 → 280055 · D112(coupling — the insolent self-exalting).
- Psa 55:3·280179 → 280178 · D108(manner=`in anger`) and D112(coupling).
- Psa 55:11·280043 → 280044 · D112(coupling=`paired with fraud`).
- Psa 64:6·281141 → 281138 · D112(coupling — the perfected scheme).
- Psa 64:2·281107 → 306458 · D103(source), → 281117 · D112(coupling=`bitter words and laid snares`).

The recurring link is **D112 coupling**: enmity is bound to its companion motion (a paired act of speech, scheming, or its judgement). The near-total absence of within-family edges means the file gives **no evidence that these hostility-movements interlock with each other** — only with their in-verse companions.

## 7. The interior anatomy the data actually names

Assembling only filled seats/sources/couplings, the interior this family names is thin:
- **Seats:** heart/inward (Psa 62:4·280962), tongue (Psa 52:2·279806) — and by discovery-note the "bed"/place of rest as scene of scheming (Psa 36:4·277532·D114). Nothing else (soul, ruach, eye, reins) is named.
- **Locus (D116, corrected):** `internal:ib-state` 46 · `external:person` 6 · `external:god` 4. The enmity is overwhelmingly read as an internal IB-state, with a minority located on an external person (e.g. Psa 44:7·278847·D116=`external:person`) or against God (Psa 81:15·283815, Psa 83:2·283991, Psa 89:23·284638, Psa 89:22·284629, all D116=`external:god`).
- **Couplings named:** hate-your-haters (139:21·273471), complete-hatred (139:22·273476), counts-as-enemies (139:22·273478), plot-on-bed (36:4·277532), lurk-and-seize (10:9·306005), plot-vain (2:1·276494), haters-of-God (139:21·273472). These are the only inner "compounds" the data spells out.

## 8. What could not be derived

- **Intensity (D109), specifier (D110), effect (D111), prohibition (D113):** absent in **all 56** — no gradation, sub-typing, consequence, or "forbidden" reading is recoverable from this source.
- **Seat:** unread in 54/56 — for the hatred core the interior *organ* is never located.
- **Source (D103):** unread in 53/56 — what originates the enmity is not given (the 3 present record its judgement-terminus, not its rise).
- **Bearer:** stated on **no** span (all inferred) — every "whose IB" is a reader inference, not a span datum.
- **Cluster:** 15 instances (cursing/oppression/pursuit/ambush/accusation stratum) are un-typed by the term layer (NULL).
- **Network:** 158 self-loops are non-edges; the 19 real edges reach only outside the family, so **inter-movement structure within the family is not evidenced**.
- **Righteous vs malicious valence:** the file gives no dimension that fixes it (D109 valence-type is absent); it is discernible only by reading bearer against target — a gap the source cannot close on its own.

## 9. Summary

The `malice-enmity-persecution` family is **not one inner-being movement but a relational field of hostility** fusing ≥5 strata — hatred/enmity (M06, the true core), scheming (outliers M15/M42/M17 + M14), cursing, oppression/persecution, and accusation — and further split by a virtue/vice fault-line running through the single lemma `sane` (righteous aversion vs malicious enmity). The data is anatomically thin (seat 2/56, source 3/56, intensity/specifier/effect/prohibition 0/56), read entirely as inferred-bearer `characteristic`s, mostly `internal:ib-state`, with a sparse outward-only network and a 22-instance D112/D116 swap that must be corrected before reading. Its richest evidenced motions are the **totalising/hardening of hatred into owned state** (Psa 139:22) and **loyalty-aversion binding the IB's hatred to God's cause** (Psa 139:21).
