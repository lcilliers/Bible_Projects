# Structural terms — clarification and correction

**Date:** 2026-05-18
**Author:** CC
**Purpose:** correct CC's structural framework after researcher 2026-05-18 noted that CC had been using "register" informally and had the cluster/characteristic relationship inverted. This document confirms the corrected hierarchy and lists CC's errors for record. **Decision blanks at §6 for researcher confirmation.**

---

## 1. CC's structural errors — what was wrong

### Error 1 — Inverted cluster/characteristic relationship

CC was treating M04 as **one characteristic** (joy/gladness/delight) with **many sub-group "register-variants"** of that single characteristic.

The correct view per researcher 2026-05-18:

> *"similar characteristics as represented by terms is a cluster. A cluster have sub groups which is characteristics that all work together form the cluster."*

So M04 is **a cluster of multiple characteristics**, not one characteristic with sub-variants. Each sub-group (M04-A, M04-B, … M04-P) is a distinct **characteristic**.

### Error 2 — Informal use of "register"

CC borrowed "register" from linguistics (variety-of-language-use) and used it to mean "mode/variety/family of inner-being content within a cluster's characteristic." This was an informal CC coinage with no formal definition in any instruction document.

Under the corrected hierarchy, "register" is **not needed** as a term. Each sub-group is just a *characteristic*. There is no separate "register" layer to name. CC should drop "register" from its vocabulary.

### Error 3 — Wasted analytical work in the v2 proposal

The v2 Phase 9 proposal framed Layer 2 (cluster-level aggregation) as "synthesise across the one characteristic's register-variants." Under the corrected hierarchy, Layer 2 is **synthesise across the cluster's multiple related characteristics** — a different analytical claim, though the mechanic remains the same.

---

## 2. The canonical definition of "inner-being characteristic"

From `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Chapter 1 / "Defining Inner Being":

> *"Inner-being characteristics are the non-physical, internal states, capacities, and expressions that constitute a person's invisible life — encompassing how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God."*

This is the **scope-defining definition**. Anything matching this is in scope; anything not matching it is out of scope.

---

## 3. The corrected hierarchy (CC's understanding — please confirm)

| Level | Term | Definition | Examples |
|---|---|---|---|
| 1 | **Characteristic** | An inner-being state, capacity, or expression per the working definition above. The atomic unit of inner-being study. | "exultation toward YHWH"; "communal festive joy"; "fear of God"; "material/sensory pleasure"; "evaluative goodness as moral faculty". |
| 2 | **Registry** | One of the 214 English-word anchors; one row per word in `word_registry`. Each registry represents one or more characteristics. Owns one or more terms. | *joy* (no=97), *fear* (no=61), *anger* (no=4), *grace* (no=68). |
| 3 | **Term** | A Hebrew/Greek/Aramaic Strong's word; belongs to one OWNER registry; carries the characteristic in specific verses. | H8057 sim.chah; G5479 chara; H3372 ya.re. |
| 4 | **Cluster** | An M-coded analytical grouping of *similar characteristics* — typically the related characteristics that work together to form an inner-being family. Multiple registries' terms contribute to one cluster. | M04 Joy/Gladness/Delight family; M01 Fear family; M02 Anger family. |
| 5 | **Sub-group** | Within a cluster, one of the constituent characteristics. The sub-groups work together to form the cluster. | M04-A Exultation in YHWH; M04-K Material/Sensory Pleasure; M04-L Evaluative Goodness. |
| 6 | **VCG** *(verse_context_group)* | A group of verses sharing a contextual meaning of a term; describes what the verses *say* about a sub-group's characteristic. Has a `context_description`. | M04-K-VCG-01 (Sacrificial pleasing aroma — ni.cho.ach corpus); M04-L-VCG-01 (Divine character goodness — ki-tov declarations). |
| 7 | **Tier** *(T0–T7)* | 189 prompts organised into 8 analytical-focus tiers. Cut across VCGs and sub-groups to articulate certain analytical areas (constitutional location, relational interface, manifestation, etc.). | T0 Divine Image and Created Design; T1 Definition; T2 Constitutional Location; T6 Structural Relationships. |

---

## 4. Relationships between layers

```
Inner-being scope (§ definition above)
    │
    └── Characteristic (atomic inner-being state/capacity/expression)
            │
            ├── Registry (English-word anchor for one or more characteristics)
            │       │
            │       └── Terms (Strong's words; OWNER per registry)
            │               │
            │               └── Verses (occurrences of the term)
            │
            └── Cluster (similar characteristics grouped for analytical work)
                    │
                    └── Sub-group (a characteristic within the cluster)
                            │
                            └── VCG (verses' contextual meaning about the characteristic)
                                    │
                                    └── (member verses with Pass A meanings)

Tiers (T0-T7, 189 prompts) cut ACROSS sub-groups and VCGs for focused
analytical coverage.
```

Key relational rules:

- A **term** belongs to one OWNER registry (cross-references possible via XREF mechanism).
- A **registry** typically represents one characteristic, but may represent more.
- A **cluster** groups multiple characteristics (each sub-group = one characteristic).
- A **sub-group** holds the VCGs that articulate its characteristic.
- A **VCG** describes what the verses say about its sub-group's characteristic.
- A **tier** is an analytical focus applied via the 189 prompts; tiers don't own data but cut across the structure.

---

## 5. Implications of the correction

### 5.1 Why the original 189 × sub-group rule was sound in principle

If each sub-group is **a distinct characteristic**, then the 189 questions × every sub-group + cluster scope was the right discipline at the start: each characteristic deserves its own full multi-dimensional analysis. The completeness mechanic was justified.

### 5.2 Why the dilution happened anyway

The researcher's diagnosis stands: when verse-volume forced sub-groups to be split into **sub-components of one characteristic** (rather than distinct characteristics), running the 189 sweep on each sub-component produced artificial repetition. Two distinct phenomena:

- **Genuine characteristic sub-groups** (e.g. M04-A Exultation in YHWH vs M04-K Material/Sensory Pleasure — analytically distinct characteristics): full 189 sweep is appropriate.
- **Sub-component sub-groups** (e.g. if M04-B had been split into M04-B1 OT-feast / M04-B2 NT-feast for size reasons, but both are one characteristic "communal festive joy"): running 189 on each split produces near-duplicate findings.

The current M04 sub-group set is mostly characteristic-level (per the labels) but may include some sub-components produced under verse-volume pressure. Researcher would need to identify which.

### 5.3 What this means for the v2 Phase 9 proposal

The v2 layered architecture **still works**, with one correction in framing:

- **Layer 1 (VCG synthesis)**: unchanged — VCGs are bounded synthesis units regardless of whether their sub-group is a characteristic or sub-component.
- **Layer 2 (cluster aggregation)**: rephrased — "synthesise per prompt across the cluster's multiple related characteristics," not "across the one characteristic's register-variants."
- **Layer 3 (selective sub-group)**: should differentiate genuine characteristics (warrant full sub-group sweep) from sub-components (don't warrant separate sweep; analytically merge with parent characteristic).
- **Completeness check**: pre-flight should verify each sub-group is a genuine characteristic at Phase 5 design; if it's a sub-component of another, mark it as such so findings work knows not to over-replicate.

This doesn't change the v2 mechanics; it changes how we describe what the layers are doing.

---

## 6. Decisions needed from researcher

| # | Question | Options | Your decision |
|---|---|---|---|
| 1 | Confirm the hierarchy in §3 is correct? | YES / NO / ADJUST: ... | _[YES / NO / ADJUST: ...]_ |
| 2 | Confirm "register" is informal-and-not-needed; CC drops it from vocabulary? | YES / KEEP-AS-DEFINED-TERM / OTHER | _[YES / KEEP / OTHER]_ |
| 3 | For M04 — should CC identify which of M04-A through M04-P are genuine characteristics vs sub-components-split-for-size, and propose consolidations where they're sub-components? | YES (identify and propose) / NOT YET (defer) / NEVER | _[YES / NOT YET / NEVER]_ |
| 4 | Does the v2 Phase 9 proposal (just reframed per §5.3 above) still hold, or does the structural correction change your decisions? | STANDS / RE-DECIDE: ... | _[STANDS / RE-DECIDE: ...]_ |
| 5 | Should CC sweep recent outputs (v1/v2 proposals, recent commit messages, memory items) and correct "register" usage where it appears? | YES (sweep and correct) / LEAVE-AS-IS | _[YES / LEAVE-AS-IS]_ |

---

## 7. Note on terms not yet covered

The prose mentions **dimensions** as a separate cross-registry analytical-grouping concept:

> *"A dimension is a named inner-being characteristic that a group of verses engages; it is assigned to a `verse_context_group` as the outcome of the Dimension Review analytical pass."*

Dimensions appear to be a programme-wide cross-cluster classification system applied to VCGs (the Dimension Review pass produces the labels). This is separate from the cluster/sub-group hierarchy above and was not part of the researcher's correction. CC has not used "dimension" recently and has not been muddling it with the cluster/sub-group/VCG structure.

If dimensions need to enter Phase 9 / findings work, the researcher can flag for a separate clarification.

---

*End of clarification. Mark §6 and ping me.*
