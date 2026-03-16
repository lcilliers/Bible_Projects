# WA-051 | Distress | Phase 1 Context Notes

**Registry ID:** 051
**Source List:** High Confidence
**Date:** 2026-03-07
**Phase:** 1 — Linguistic and Contextual Data

---

## Purpose of This File

This file records contextual observations, source data quality issues, methodological decisions, and process notes arising from the Phase 1 analysis of WA-051 Distress. It supports transparency, reproducibility, and continuity across analysis sessions.

---

## Source Data

**Primary source file:** Word_distress.md (Registry 051, High Confidence)
**Classification:** High Confidence

The source file contains a header section identifying the primary terms, followed by 58 STEP-derived word analysis blocks covering Hebrew, Aramaic, and Greek terms related to distress. The file is one of the largest in the programme by term count.

---

## Methodological Decisions

### Sub-entry granularity
**Decision:** All STEP sub-entries retained as separate entries in the JSON.

**Rationale:** Contextual examination of the verse data for the tsa.rar root (H6887B/C/D/E) and the tsar root (H6862A/B/C/D) confirms genuine semantic differentiation between the sub-entries: the verse contexts show different registers (physical binding, inner suffering, interpersonal hostility, marital rivalry; and physical narrow space, inner distress, external enemy, physical flint respectively). STEP's sub-division is exegetically defensible, not merely lexical over-refinement.

**Ra.ah decision:** ra.ah H7451I and H7451C are retained as separate entries per instruction. A tentative contextual distinction is noted in the analysis (I-cluster tends toward named inner state of calamity; C-cluster tends toward harm-as-threat), but the evidence is not conclusive. This remains open for Phase 2.

### ba.hal double register
The verse data clearly separates ba.hal into a distress/terror register and a haste/hurry register. The PERIPHERAL classification has been applied consistently to the haste register verses. The question of whether these are two meanings of one root or one psycho-somatic concept covering both alarm and urgent action is preserved as an open question.

### 1Sa 16 evil spirit verses
The six ra (H7451A) verses involving the harmful spirit from God and Saul have been classified AMBIGUOUS rather than CORE. The inner torment dimension is real, but the nature of the agent (spiritual force) and the mechanism (divine sending) create a category that standard inner-being analysis cannot resolve without theological-exegetical work beyond Phase 1 scope. The classification reflects genuine uncertainty, not dismissal.

---

## Data Quality Issues

### 1. me.tsar (H4712) — wrong word analysis block
The word analysis block for me.tsar (H4712) in the source file displays the heading, meaning, occurrence count, and related words for riv (H7379 strife) rather than for me.tsar. This appears to be a copy-paste error introduced at some point in the STEP data extraction or source file preparation. Three verses are correctly attributed to me.tsar: Psa 116:3; Psa 118:5; Lam 1:3. The analysis for me.tsar has worked from the verse texts alone. Flagged as FORMAT_INCONSISTENCY / NO_WORD_ANALYSIS.

### 2. lupēros (G3077) — no STEP block
lupēros (distressing) appears in the related word list at the head of the source file but has no STEP body entry. No verses or meaning data are available for this term. Flagged as MISSING_TERM.

### 3. me.tsu.qah (metsuwqah) — in primary term list only
me.tsu.qah appears in the source file header as a primary term (with gloss distress, tightness, pressure) but has no dedicated STEP block in the body. It appears as a related word under other entries. The verse references associated with it in the primary term description (Deu 28:53; Isa 8:22) are covered under the tsa.rah and related terms' verse sets. Flagged as MISSING_TERM.

### 4. tsoq (H6695A) — single PERIPHERAL verse
The single occurrence of tsoq (Dan 9:25) is classified PERIPHERAL. The term's inner-being potential is not confirmed by the available evidence, though the root family is well attested in CORE contexts.

---

## Term Count Notes

- Total related terms in STEP list: 58
- Terms with no STEP block: 2 (lupēros G3077, me.tsu.qah)
- Terms with corrupted STEP block: 1 (me.tsar H4712)
- Aramaic terms: 2 (be.esh H0888, ke.ra H3735)
- Single-occurrence terms: 5 (tsoq H6695A; mu.a.qah H4157; ke.ra H3735; tsa.rar H6887E; tsa.rah H6869C)
- Terms with no CORE verses: tsar H6862D (hard, entirely PERIPHERAL); tsa.rar H6887E (to rival, entirely PERIPHERAL); tsoq H6695A (PERIPHERAL)

---

## OT/NT Register Observations: Process Notes

Eight open questions (OQ-051-01 through OQ-051-08) have been identified in the analysis file arising from observable OT/NT differences in how the distress vocabulary functions. The methodology followed is:

1. Patterns identified by examining verse context across the full CORE and EXTENDED verse sets for both Hebrew and Greek terms.
2. The observations are stated descriptively without importing Framework B categories or drawing Phase 2 conclusions.
3. Each open question is precisely worded to preserve the exegetical or anthropological question for Phase 2 overlay.
4. No conclusions are drawn about the significance of the differences; the questions are preserved as open inquiries.

The eight open questions cover:
- The formative/productive function of thlipsis versus the crisis function of tsa.rah (OQ-01)
- The Christological location of distress vocabulary in the NT (OQ-02)
- The productive/moral grief sub-category in lupeō that has no OT parallel (OQ-03)
- The etymological tethering of OT distress to adversarial causation absent in NT (OQ-04)
- The exclusive application of adēmoneō to Jesus and Epaphroditus (OQ-05)
- ba.hal's two registers and the possible psycho-somatic connection (OQ-06)
- The 1Sa 16 evil spirit passage and inner life under spiritual influence (OQ-07)
- stenochōreō applied to restricted affections in 2Cor 6:12 (OQ-08)

These questions collectively point toward a broader Phase 2 inquiry: whether the observable differences in how distress functions across the Testaments reflect a theological development, an anthropological development, or both.

---

## Cross-Registry Links Identified

Ten cross-registry links have been recorded in the JSON:

- Anger (via cha.rah H2734 shared root)
- Grief (via lupeō G3076 and odunaō G3600)
- Bitter (via mar H4751)
- Pain (via ke.ev/ka.av root family)
- Anguish (via sunochē G4928 and tsu.qah H6695B)
- Fear (via ba.hal H0926)
- Shame (via ra.ah semantic overlap)
- Humility (via tsa.rah in 2Ch 33:12 as humility-trigger)
- Pride (via qa.shah hardening)

The number and variety of cross-links in this word set are high. Distress occupies a hub position in the inner-being word network: it connects to anger (cha.rah), grief (lupeō), fear (ba.hal), bitterness (mar), and pain (ke.ev) through shared terms, and to humility and pride through functional/semantic overlap. This hub position suggests that in Phase 2, Distress will be one of the anchor words for mapping the relational structure of the inner-being vocabulary.

---

## Session Notes

Phase 1 analysis was initiated following two preparatory sessions:
1. An initial source data review session identifying the 58-term inventory, data quality issues, and the open question about ra.ah sub-entry consolidation.
2. A methodology session in which the instruction to apply additional contextual rigour was received and confirmed: (a) examine verse contexts to determine whether sub-entries reveal genuinely distinct categories; (b) identify OT/NT register differences; (c) preserve any signals of a potential OT/NT difference in the inner person's relationship to suffering as precisely-worded open questions (Option A methodology).

This additional rigour has been applied across all three output files. The analysis will be reviewed after the next word in the programme is completed to assess whether the OT/NT register observation methodology should be incorporated into the standing specification.

---

## Output Files for This Card

| File | Description |
|---|---|
| WA-051-Distress-data-2026-03-07.json | Term inventory, verse classifications, cross-links, data quality flags |
| WA-051-Distress-analysis-2026-03-07.md | Root family analysis, verse pattern analysis, open questions |
| WA-051-Distress-context-2026-03-07.md | This file — source notes, methodological decisions, process record |
