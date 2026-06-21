# M02 findings — OLD (db-export) vs NEW (merged) comparison, and missing synergies

**File:** `wa-m02-oldnew-findings-compare-v1_0-20260619.md` · **Date:** 2026-06-19
**Prefix:** WA · **Reference:** m02 · **Version:** v1_0 (first issue)
**Prior output:** none this session. **Inputs:** `WA-m02-findings-NEW-merged-bytier-v1-20260619.md` (2378 lines) and `WA-m02-findings-OLD-dbexport-bytier-v1-20260619.md` (1149 lines).

**Change-control note (v1_0):** first issue. Comparison of the two M02 findings sets and identification of synergies the NEW set does not yet draw out.

**Scope and limits.** This rests only on the two findings files supplied. It does **not** draw on the four `ve_lexical` extracts, the seven source per-characteristic documents, or the OLD consolidated source (`WA-M02-consolidated-findings-v1-20260516`). Where a difference could be either a deliberate catalogue-refit decision or an accidental loss, that is stated and flagged for verification rather than asserted. Observation, interpretation, and reflection are kept distinct.

---

## Part A — Comparison

### A0. Provenance and method *(observation)*

| | OLD (db-export) | NEW (merged) |
|---|---|---|
| Source | `cluster_finding`, exported from `WA-M02-consolidated-findings-v1-20260516` | 7 per-characteristic tier analyses (c1–c7), authored 2026-06-19; merged in tier order |
| Model | 6 characteristics, ids 71–76 | 7 characteristics, c1–c7 |
| Catalogue | 173-question (47 refit-folded) | 126-question (47 refit-folded, no new answer) |
| Evidence base | VCG sub-groups (M02-A-VCG-01 … M02-F-VCG-07); named verses; prose | occurrence-level re-read of 4 `ve_lexical` extracts; 703 focus occurrences (671 + 32 tsur excluded), 0 orphans |
| Row form | consolidated row + one row per characteristic (much verbatim duplication) | one bullet per characteristic per question; cluster-wide synthesis appended |
| DB state | in DB (`cluster_finding`) | **not yet in DB** |

*Interpretation.* These are not two drafts of the same artefact. The OLD set is the **prior consolidated model committed to the database**; the NEW set is a **ground-up re-analysis on a changed model and a changed catalogue, anchored in the extract**. The NEW set is the more authoritative on data grounds (GR-DATA-002: the current extract governs), but it has not yet been persisted.

### A1. The characteristic model changed — and on a different axis *(observation + interpretation)*

The single most consequential difference.

| OLD (6) | → | NEW (7) | Nature of the change |
|---|---|---|---|
| 71 Divine Wrath as Judicial Force | → | C2 Divine wrath | rescoped: defined by **bearer (God)**, not by "judicial" register; absorbs judicial + burning |
| 72 Burning Rage and Inner Heat *(divine + human mixed)* | → | **split: C1 Human anger + C2 Divine wrath** | the decisive change — a **bearer split** (researcher DEC-2) |
| 73 Indignation and Moral Displeasure | → | C5 Indignation / displeasure / sullenness | retained; valence-graded |
| 74 Provocation — Anger Aroused | → | C3 Provoking to anger | retained; sharpened as a causative act |
| 75 Jealousy, Zeal and Possessive Passion | → | C4 Jealousy / zeal | retained |
| 76 Strife, Quarrel and Contentious Anger | → | C6 Strife / quarrel / contention | retained; sharpened with the faculty-NONE finding |
| *(none)* | → | **C7 Bitterness** | **new characteristic** (NT *pikria*, 4 verses) |

*Interpretation.* The organising axis shifted from **register/intensity** (judicial wrath vs burning rage) to **bearer / relation** (human anger / divine wrath / the act of provoking). This is consistent with GR-PROG-006 (characteristic-perspective, not term-centric, grouping). Three consequences follow:

1. It yields a clean **divine–human correspondence** frame (NEW F2) and a clean **valence-by-bearer** finding (NEW F4): the same heat-vocabulary is righteous when God bears it (C2), gravely sinful when a person directs it at God (C3), and morally double-valued in the human bearer (C1).
2. It introduces a risk OLD's combined char 72 did not carry: **C1/C2 boundary leakage** on a read-resolved field (Exo 4:14; 2Ki 13:3 leaked into C1), flagged in NEW F10.1 with an explicit circularity caution.
3. **C7 Bitterness** is genuinely new analytical territory, not a re-labelling of any OLD char.

### A2. Evidence grounding *(observation)*

OLD argues qualitatively from VCG sub-groups and named verses. NEW argues from **extract fields**: occurrence counts (e.g. C1 affect 196/228), valence tables (neutral / righteous / sinful / forbidden / commanded), faculty fields, morphology codes, book distributions, and lemma maps. *Interpretation:* the NEW set makes each claim traceable to a specific extract field (GR-PROC-002) in a way the OLD set cannot; this is an epistemic upgrade, not merely a presentational one.

### A3. New structural material in NEW *(observation)*

- **Cluster-wide synthesis F1–F10** — cross-characteristic findings organised by phenomenon (vocabulary architecture, divine-human correspondence, three constitutional kinds, moral grading by bearer/direction, internal causal structure, relational symmetry/reversibility, binding to the moral order, developmental/eschatological orientation, cross-cluster bridges, data-quality). The completeness statement names this as the new contribution.
- **Anchor-verse map** (table).
- **Explicit data-quality flag register (F10).**
- **Completeness statement** (exhaustive assignment; 0 orphans).

OLD has none of these as discrete structures; its cross-characteristic work is scattered through `[E]` contrast notes and the per-question consolidated row.

### A4. Resolution of the standing M02 flags *(observation)*

| Standing flag (programme record) | OLD | NEW |
|---|---|---|
| C2 valence anomaly (7 divine-wrath occ. tagged sinful) | not surfaced | **surfaced** — F10.1 + F4 table footnote + circularity caution |
| C7 scope (OT bitterness-of-soul field) | n/a (no C7) | **developed** — F10.4, T7.1.8, F9 (marah/mar: Ruth 1:20; 1Sa 1:10; Job 7:11) |
| object_type under-population (programme-wide) | not surfaced | **surfaced** — F10.2 |
| `mode` field absent from M02 schema | not surfaced | **confirmed** — F10.6 (0/703) |

NEW also raises **new** flags: C1/C2 boundary leakage (F10.1), `tsur` mis-seeding (F10.5, 0/32 anger), and C6 procedural-sense filtering per GR-PROG-007 (F10.3).

### A5. What NEW reduced or folded *(observation + reflection)*

The 126-question catalogue **folds 47 questions** that OLD answered. The clearest reduction is **constitutional-level depth (Tier 2)**:

- OLD spread location analysis across **T2.1–T2.7** with per-faculty interpretation: heart-location (T2.3), mind-location (T2.4), soul-level beyond heart/mind (T2.5), body-part link with explicit **emphatic / functional / expressive / indicative / mediating** typing (T2.6), and body-direction including a **bi-directional** soul↔body reading (T2.7).
- NEW folds all of these into the single **T2.1.1 / T2.1.2 audit** (which does report seat counts: heart, soul, flesh) and marks T2.1.3, T2.1.4, T2.2.x, T2.3.x, T2.4.x, T2.5.x, T2.6.x as *"no new per-characteristic answer."*

What is **retained** in NEW (so not a loss): the full **Tier 3 faculty suite** — perception, cognition, memory, affect, creativity, volition, agency, **moral-evaluation (T3.8)**, **conscience (T3.9)**, conscientiousness (T3.10), relational (T3.11) — per characteristic, and a **richer T7.1 vocabulary arc** than OLD carried.

**Candidate losses — FLAGGED, not asserted** (resolvable only against the extract / source docs):

- **L1 — Spirit-level seat of anger/provocation.** OLD T2.1 carried Eze 3:14 (rage as "felt inner heat in his spirit"), Act 17:16 (Paul's spirit provoked), and 1Sa 11:6 (Spirit-empowered anger). NEW's T2.1.1 audit lists heart/soul/flesh/conscience for C1/C3, and T2.10.1 states "no spirit→soul→body sequence." The spirit level appears **under-represented** in NEW. This may be a verse-set difference rather than a dropped finding — needs checking whether these verses are in the four extracts and how they were assigned across c1–c7.
- **L2 — Phinehas-zeal typology (human→divine direction).** OLD T0.4 (char 75) read Phinehas' atoning zeal as typological. NEW C4 T0.4 records "narrative/wisdom, no typology" for the human pole. Possible dropped reading — verify.
- **L3 — Body→soul feedback.** OLD T2.7 raised a bi-directional reading (envy rotting the bones reinforcing the inner state). NEW T2.7.1 records "no body-to-soul feedback shown — silent." A softening of OLD's reflection.

*Reflection.* The NEW set is methodologically stronger across the board, and its F1–F10 synthesis captures most cross-characteristic structure the OLD set only gestured at. The reductions are concentrated in the **constitutional sub-mapping** — precisely the area closest to the programme's governing question (the spirit–soul–body boundary, GR-PROG-002). That makes L1 in particular worth confirming before it is treated as a deliberate simplification.

---

## Part B — Missing synergies in the NEW findings

"Synergy" here = a connection (cross-characteristic, cross-cluster, or cross-tier) that the NEW material supports but has **not yet drawn out** in the per-characteristic answers or in F1–F10. Each is tagged by how firmly the NEW text alone supports it.

**S1 — Spirit-level seat synergy (cross-tier T2; Framework A interface).** *Conditional on L1.* If Eze 3:14 / Act 17:16 / 1Sa 11:6 are in the extract, then C1 (human anger) and C3 (provoking) have a **spirit-level** engagement that NEW's T2.1.1 audit does not register, and 1Sa 11:6 (Spirit-empowered anger) is a direct **Framework A ↔ Framework B** interface. This is exactly the constitutional-mapping synergy F3 ("three constitutional kinds") gestures toward but stops short of. *Support: needs verse verification.*

**S2 — C5 Indignation ↔ M03 Grief bridge, omitted from F9.** F9 lists two anger↔grief seams to M03 (the *kaˈaˈs* "vexation/grief" term, and the OT bitterness-of-soul field). It omits a **third**: C5's sullen/dejected edge (1Ki 21:4 "vexed and sullen") and 2Cor 7:11 ("godly grief produces … indignation") make **indignation itself the hinge between wrath and grief**. NEW states this per-characteristic (C5 T6.5, T1.3.3) but does not carry it into the F9 Session-D bridge set. *Support: fully supported by the NEW text.*

**S3 — Fire/burning conceptual-metaphor synergy binding C4 to C1/C2.** F1 correctly notes C4 (jealousy) runs on a **distinct root** from the burning-heat family. But C4 is repeatedly **fire** imagery — "fire of his jealousy" (Zep 1:18; Eze 36:5), "vehement flame" (Song 8:6). At the level of **conceptual metaphor** (not lexical root), the fire image binds C4 to C1/C2. OLD carried this as the heat-metaphor finding (its T7.3 science material); NEW's F1, by stressing distinct roots, **understates** the shared-metaphor synergy. *Support: fully supported by the NEW text (the fire-of-jealousy verses are in NEW).* 

**S4 — Registry 213 (listen / shaˈma) cross-registry link not carried to F9.** F7 observes the *shaˈma* "hearing" co-occurrence (13×) and its resonance with the newly-added Registry 213 (listen) — anger is gated by what is *heard*, and provoked by the covenant word heard and disobeyed. This is a genuine cross-registry synergy, but it sits only as an observation in F7; it is **not** in F9's Session-D bridge list. Given Reg 213 was recently added to the programme, this is timely to flag. *Support: fully supported by the NEW text.*

**S5 — Integrate valence (F4) × direction (F6) into one matrix.** F4 grades each characteristic by valence; F6 maps the relational directions (God→human, human→God, human→human) and their reversibility. F4 explicitly says valence is set by **bearer + direction** — yet the two tables are presented separately. A single **bearer × direction × valence** matrix would make the claim structural (e.g. human→God provocation ≈ wholly sinful C3; divine→human wrath ≈ neutral/righteous C2; human zeal→God ≈ righteous C4) and would directly strengthen the F2 divine-human correspondence dimension. *Support: fully supported by the NEW text (both tables present).* 

**S6 — A chronic/settled vs acute/kindled axis grouping C5 + C7.** NEW positions C7 (bitterness) as the "settled root" of the anger family (F5) and C5 (indignation) as the "cooler, settled" displeasure with a sullen edge. Both are the **chronic/settled** members against the **acute/kindled** C1/C2. NEW treats them separately; the chronic-vs-acute axis is a latent cross-characteristic synergy that could organise C5 + C7 as a pair. *Support: fully supported by the NEW text.*

**S7 — Within-C1 righteous vs wounded-pride exemplar contrast.** OLD made the moral-direction contrast explicit with paired exemplars ([E] contrasts: Nehemiah/Moses righteous anger vs Saul/Eliab wounded-pride anger). NEW quantifies the same reality as a **valence split** (C1 righteous 13 / sinful 58) but does not narrate the exemplar-pair structure that makes the boundary legible for a reader. The synergy (the *direction of the trigger* discriminating righteous from disordered anger) is implicit in the numbers but not drawn out. *Support: fully supported by the NEW text.*

**S8 — Phinehas-zeal typology (human pole).** *Conditional on L2.* If retained, human zeal functioning typologically (Num 25:11–13 atoning zeal) is a divine-human correspondence synergy across T0.4 and F2 that NEW's C4 currently records as absent. *Support: needs verification against OLD source / extract.*

---

## Recommendation and the open interpretive choice

The NEW set should be regarded as the **current authoritative analysis** (extract-grounded, valence-graded, synthesised) and is a clear advance on the OLD db-export. Two things remain to settle, and the second is a researcher decision:

1. **Synthesis additions (S2–S7)** are fully supported by the NEW text and could be folded into the cluster-wide synthesis (chiefly: extend F9 with S2 and S4; add the F4×F6 matrix S5; note S3, S6, S7) **before** the NEW findings are persisted to the database.
2. **The interpretive choice (L1/L2/L3, S1/S8):** whether the spirit-level seat, the Phinehas-zeal typology, and the body→soul feedback reading were **deliberately folded** by the 126-question catalogue refit, or were **lost in transit** and should be recovered. This cannot be settled from the two findings files alone — it needs a targeted check against the four `ve_lexical` extracts and the seven source per-characteristic documents.

*How would you like to proceed?* I can (a) draft the S2–S7 synthesis additions as concrete inserts to the cluster-wide synthesis, and/or (b) specify the exact verse-and-field checks needed to resolve L1/L2/L3 against the extract — but the verse-level verification itself depends on data this session does not hold.
