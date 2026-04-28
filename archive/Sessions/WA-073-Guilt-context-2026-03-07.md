# WA-073 | Guilt | Phase 1 Context Notes

**Registry ID:** 073
**Source List:** High Confidence
**Date:** 2026-03-07
**Phase:** 1 — Linguistic and Contextual Data

---

## Purpose of This File

This file records source data quality issues, methodological decisions, and process notes for the Phase 1 analysis of WA-073 Guilt. It supports transparency, reproducibility, and continuity across sessions.

---

## Source Data

**Primary source file:** word_guilt.md (Registry 073, High Confidence)
**Classification:** High Confidence

The source file contains a header section with primary terms, STEP suggestions, and a related-words list, followed by STEP word analysis blocks for most entries. The file is large (~2,316 lines) due to extensive verse sets for cha.ta (to sin) and a.von (iniquity), both of which have broad biblical distributions.

---

## Source File Structure Issues

### 1. Missing STEP blocks: enochos and katakrima
The two Greek primary terms identified in the source file header — enochos (G1777, guilty, liable) and katakrima (G2631, condemnation, verdict of guilt) — appear only in the header description and related-words list. Neither has a STEP word analysis block or verse set in the body of the file. This is the most significant data gap in the set. The source file's own STEP suggestion names katakrima (Rom 8:1) as the theological resolution of guilt, making its absence particularly notable.

### 2. cha.ta verse duplication
The cha.ta (H2403) and cha.ta.ah (H2401) verse sets appear to have been reproduced twice in the source file — the same verses appear starting around line 1700 a second time. This does not represent two different entries; it appears to be a copy-paste error in the source file preparation. The verse set was processed once using the unique verse set only.

### 3. a.sham dual entry
a.sham appears as both H0816 (verb: to be guilty, 35x) and H0817 (noun: guilt offering, 46x). These are correctly treated as two entries, sharing a root but distinct in function and verse context.

---

## Methodological Decisions

### Sub-entry granularity
All entries have been retained as separate items in the JSON. The a.sham H0816/H0817 split has been confirmed as reflecting genuine functional differentiation in the verse contexts: H0816 verses centre on the inner act of incurring or recognising guilt; H0817 verses centre on the cultic instrument that addresses guilt. The four a.sham-root entries (H0816, H0817, H0818, H0819) are kept distinct and treated as covering a complete cycle: the verb (incurring/recognising guilt), the noun-state (being guilty), the abstract noun (the accumulated guiltiness), and the cultic noun (the offering that addresses it).

### chin.nam inclusion
chin.nam (H2600, for nothing, without cause) is included because it functions as the guilt set's counter-concept — the vocabulary for unjust accusation and suffering without cause. Its primary inner-being relevance is in the Job cluster (the question of whether Job's suffering is deserved) and in the Psalms persecution texts (innocent suffering at the hands of unjust adversaries). The extensive peripheral content (commercial, legal, prophetic uses) has been classified PERIPHERAL.

### na.sa verse set
The na.sa (H5375J) verb has 659 total occurrences but the guilt-relevant sub-entry J covers only those instances where the lifting/carrying is applied to guilt, iniquity, or sin. The verse classification has treated the ritual/cultic bearing-of-iniquity verses as PERIPHERAL (they presuppose guilt but are procedurally focused) and the Isa 53:12 instance as the primary CORE verse. The observation that na.sa covers both accumulation and removal of guilt within the same root has been flagged as a data quality note for Phase 2 attention.

---

## OT/NT Register Observations: Process Notes

Eight open questions (OQ-073-01 through OQ-073-08) have been identified in the Analysis MD. The methodology follows the same Option A approach applied in Registry 051 (Distress): patterns are identified descriptively from verse context, differences are stated without importing Framework B categories or Phase 2 conclusions, and each question is precisely worded to preserve the exegetical or anthropological question as an open inquiry.

The eight open questions cover:
- The absence of an OT equivalent to suneidēsis — a named inner moral-monitoring faculty (OQ-01)
- a.von's three-layer semantic structure fusing act, guilt, and consequence (OQ-02)
- na.sa as both guilt-bearing and guilt-removing in the same root (OQ-03)
- The missing enochos and katakrima and their effect on NT legal/resolution vocabulary (OQ-04)
- The Gen 42:21 intersection of guilt and distress as a cross-registry signal (OQ-05)
- The OT guilt-as-weight versus Pauline guilt/sin-as-indwelling-power (OQ-06)
- The seared conscience as deteriorated guilt-faculty (OQ-07)
- The Isa 53 convergence of a.von, a.sham, and na.sa around the Servant's nefesh (OQ-08)

The most theoretically significant of these for the programme is OQ-02 (the three-layer a.von structure) and OQ-06 (the weight/power contrast between the Testaments). Both raise the foundational question of whether guilt in the OT is primarily an ontological category (a condition of standing before God that carries its own consequence) and whether the NT partially psychologises it (through suneidēsis) while simultaneously deepening the ontological claim (through the indwelling sin-power in Rom 7).

---

## Cross-Registry Links Identified

Six cross-registry links have been recorded in the JSON:

- Shame (via Ezr 9:6-7 and Dan 9:8: guilt and shame co-experienced in confession)
- Humility (via Hos 5:15 and Lev 26:41: guilt as trigger for seeking God and humbling)
- Grief (via Psa 31:10; 38:4, 18: guilt-iniquity producing grief and somatic deterioration)
- Distress (Registry 051, via Gen 42:21 and lament Psalm parallel structure)
- Pride (via Rom 6 sin-as-dominating-power overlapping with Pride's inner-orientation)
- Anger (via the consistent a.von → divine wrath connection in Exo 20:5; Num 14:18; Ezr 9; Dan 9:16)

The intersection with Distress (Registry 051) is particularly notable: Gen 42:21 directly connects guilt (a.shem) and distress (tsa.rah from the Joseph narrative's own vocabulary) in a single verse that explicitly names the causal chain. This is the only verse identified across both analyses where the two registries are lexically linked within a single sentence.

---

## Structural Observation: Guilt as Hub

Like Distress (Registry 051), the Guilt word set occupies a hub position in the inner-being word network. It connects to Shame (co-experienced in confession), Grief (guilt produces somatic deterioration), Humility (guilt-recognition triggers humbling), and Distress (guilt causes distress; distress can confront the guilty). These connections suggest that in Phase 2, Guilt and Distress will be two closely related anchor words for mapping the relational structure of the inner-being vocabulary. The six cross-registry connections in Guilt compare to the ten identified in Distress; the overlap in connecting terms (Shame, Grief, Humility) confirms that these words form a cluster in the inner-being network.

---

## Session Notes

This is a complete single-session Phase 1 analysis. The additional rigour methodology (within-root contextual differentiation, OT/NT register comparison, anthropological signal preservation as Open Questions) has been applied throughout. The source file was read in full sections (lines 1–600, 600–1200, 1200–2316) before analysis began.

---

## Output Files for This Card

| File | Description |
|---|---|
| WA-073-Guilt-data-2026-03-07.json | Term inventory, verse classifications, cross-links, data quality flags |
| WA-073-Guilt-analysis-2026-03-07.md | Root family analysis, verse pattern analysis, open questions |
| WA-073-Guilt-context-2026-03-07.md | This file — source notes, methodological decisions, process record |
