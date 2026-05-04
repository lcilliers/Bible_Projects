# Catalogue v2 — Data Adequacy Assessment

**Generated:** 2026-04-30
**Catalogue source:** [WA-obs-question-catalogue-v2-2026-04-29.json](WA-obs-question-catalogue-v2-2026-04-29.json) — 8 tiers, 56 components, 189 prompts.
**Database state:** schema v3.17.0 after migration applied at backups/`bible_research_pre_obs_catalogue_v2_20260430.db`.

**Purpose.** For each component in the v2 catalogue, identify (a) what data must be present in the DB for the prompts to be answerable, (b) which existing tables/fields supply that data, and (c) whether the data is adequate, partial, or absent. The output is a coverage map for catalogue v2 — what is ready, what needs analyst capture, what needs schema work.

**Coverage codes:**
- ✅ **Adequate** — data exists in structured DB form sufficient to answer the prompts.
- ⚠️ **Partial** — data partially exists; some prompts answerable from current sources, others need additional capture.
- 🚧 **Gap** — no structured DB capture; prompts answerable only by reading prose or by analyst inference at runtime.

**Note on extraction.** "Available when the prompts are extracted" means: when the data package for a registry is built (currently `_tmp_build_word_data_package.py`, future canonical extractor TBD), the extract carries enough structured data alongside each component's prompts that an AI can answer them without reading the entire DB or external prose. Adequacy here is judged from that perspective.

---

## T0 — Divine Image and Created Design

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T0.1 | Divine Nature Reflected | 3 | Verses where God is said to possess this characteristic; verses about God's character | `wa_verse_records` (verse_text, reference) joined via `verse_context` to OWNER groups; `verse_context_group.context_description` | ✅ Adequate (verse text + group descriptions present) |
| T0.2 | Created Purpose | 3 | Creation / design / pre-fall verse evidence; future-orientation verses (eschatological) | `wa_verse_records.verse_text`; verse classification within OWNER groups | ✅ Adequate |
| T0.3 | Image-Bearer Expression | 3 | Verses linking the characteristic to image-of-God; presence/absence reading | `wa_verse_records` + cross-registry shared anchors (R195-image / similar registries) | ⚠️ Partial — need to surface explicit image-of-God registry cross-link if not already present |
| T0.4 | Typological Significance | 3 | Verses where the characteristic is used typologically (covenantal, eschatological, christological) | `wa_verse_records.verse_text`; analyst judgment on typology | 🚧 Gap — typological use is interpretive; no structured DB capture beyond verse text |

**T0 summary:** ✅ for T0.1/T0.2; ⚠️ for T0.3; 🚧 for T0.4. The verse-text and group-description corpus carries the raw material; typological judgment is analyst work that would need a structured capture field if we want to query it later.

---

## T1 — Definition

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T1.1 | Name and Naming | 3 | Registry word; Hebrew/Greek primary terms; root meanings | `word_registry.word`; `wa_term_inventory` (OWNER); `mti_terms.transliteration`, `gloss` | ✅ Adequate |
| T1.2 | Kind | 3 | Working description of the characteristic; constitutional location; faculties; impact | `word_registry.description`, `inference_note`, `word_synopsis` | ✅ Adequate |
| T1.3 | Boundary | 3 | Structural opposite; what the word excludes / resists | None directly. Captured in narrative findings (`wa_session_b_findings.finding`) for v2 words; not for pre-v2 | ⚠️ Partial — captured in finding bodies for v2 words only; no structured field |
| T1.4 | Modes of Operation | 3 | Distinct verse-context groups under each OWNER term | `verse_context_group` per OWNER term | ✅ Adequate (groups ARE the modes) |
| T1.5 | Immediate Response | 3 | Verses showing inner-being response on encounter | `wa_verse_records.verse_text`; finding bodies | ⚠️ Partial — verses present; "immediate response" framing is analyst inference at runtime |
| T1.6 | Sustained Effect | 3 | Verses showing what the characteristic produces over time | `wa_verse_records.verse_text`; finding bodies | ⚠️ Partial — same as T1.5 |
| T1.7 | Conditions of Reception | 3 | Verses on enabling/blocking conditions | `wa_verse_records.verse_text`; finding bodies | ⚠️ Partial |
| T1.8 | Dimension Classification | 3 | Primary dimension; secondary dimensions | `word_registry.dimensions` (registry-level); per-group dimension assignments stored only in obslog narrative | ⚠️ Partial — registry-level present; per-group dimensions are in narrative only (see SP-067-014/-016 etc. as worked examples) |

**T1 summary:** ✅ for T1.1/T1.2/T1.4; ⚠️ for the rest. The biggest structured gap is per-group dimension assignment — the data is in obslog narrative, not in any column on `verse_context_group`.

---

## T2 — Constitutional Location and Boundaries

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T2.1 | Spirit-Level Location | 4 | Verses linking characteristic to spirit/`ruach`/`pneuma` | `wa_verse_records.verse_text` containing 'spirit' / `ruach` / `pneuma`; cross-registry link to spirit registry | ⚠️ Partial — text-scan possible; structured cross-link data is sparse |
| T2.2 | Soul-Level Location | 3 | Verses linking characteristic to soul/`nephesh`/`psyche` | Same pattern as T2.1 | ⚠️ Partial |
| T2.3 | Heart | 3 | Verses linking characteristic to heart/`leb`/`kardia` | Same pattern; co-occurrence with R183 (heart) registry | ⚠️ Partial — co-occurrence data exists; heart-locating semantics is analyst inference |
| T2.4 | Mind | 3 | Verses linking characteristic to mind/`nous`/related Hebrew | Same pattern; co-occurrence with mind registry | ⚠️ Partial |
| T2.5 | Other Soul Subsets | 3 | Other inner-locations Scripture might surface | Verse text scan | ⚠️ Partial |
| T2.6 | Body — Significance | 3 | Body-part links; significance type (emphatic / functional / expressive / indicative / mediating) | None directly; analyst classification | 🚧 Gap — no structured field; would need `wa_finding_entity_links` extension or a new `body_link_type` capture |
| T2.7 | Body — Direction | 3 | Direction of body-soul relationship | None directly | 🚧 Gap — interpretive; no structured field |
| T2.8 | Body — Deposit | 3 | Constitutional-deposit evidence | None directly | 🚧 Gap |
| T2.9 | Origin and Source | 3 | Where the characteristic originates (within / external / divine / generational) | None directly; surfaceable from finding bodies | ⚠️ Partial — captured in narrative for v2 words |
| T2.10 | Constitutional Movement | 3 | Movement across constitutional levels | None directly | 🚧 Gap |

**T2 summary:** ⚠️ for T2.1–T2.5/T2.9; 🚧 for T2.6–T2.8/T2.10. T2 is the largest gap area — five components have no structured DB source. The verse text supports text-scan for spirit/soul/heart/mind, but body-link semantics, direction, deposit, and movement require analyst capture that the current schema doesn't provide.

---

## T3 — The Inner Faculties

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T3.1 | Perception | 3 | Sensory-language verses; sixth-perception evidence | Verse text scan for inner-sense terms; co-occurrence with perception registries | ⚠️ Partial |
| T3.2 | Cognition | 3 | Knowing/understanding/discerning verse evidence | Same; co-occurrence with R104/cognition registries | ⚠️ Partial |
| T3.3 | Memory | 3 | Memory verbs in verse text | Same | ⚠️ Partial |
| T3.4 | Affect | 3 | Emotion/feeling verse evidence | Same | ⚠️ Partial |
| T3.5 | Creativity | 3 | Origination/imagination verse evidence | Same | 🚧 Gap — sparse cross-registry coverage |
| T3.6 | Volition | 3 | Choosing/preferring verse evidence | Same; R173 (will) cross-registry data | ⚠️ Partial |
| T3.7 | Agency | 3 | Action/initiation verse evidence | Same | ⚠️ Partial |
| T3.8 | Moral Evaluation | 3 | Right/wrong/good/true verse evidence | Same | ⚠️ Partial |
| T3.9 | Conscience | 3 | Sin/guilt/conviction verse evidence | Same; R55 (conscience) cross-registry data | ⚠️ Partial |
| T3.10 | Conscientiousness | 3 | Integrated moral-action verse evidence | Same | 🚧 Gap |
| T3.11 | Relational Capacity | 3 | Connection-with-other verse evidence | Same | ⚠️ Partial |

**T3 summary:** Mostly ⚠️ — verse text + co-occurrence carry the raw signal but no structured "engages-faculty-X" flag exists per finding. To answer T3 prompts well, the analyst (or AI at extraction time) infers faculty engagement from finding text. **A potential schema addition:** `wa_session_b_findings.engaged_faculties` (TEXT, comma-separated faculty codes drawn from a controlled vocabulary). This would make T3 prompts queryable.

---

## T4 — Relational Interfaces

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T4.1 | Divine Interface — God to Human | 4 | Verses showing God's disposition toward person | Verse text + group descriptions | ✅ Adequate |
| T4.2 | Divine Interface — Human to God | 4 | Verses showing person's response to God | Verse text + group descriptions | ✅ Adequate |
| T4.3 | Human Interface — Giving | 4 | Verses on extending characteristic to others | Verse text | ⚠️ Partial — present in text, structured "directionality" not captured |
| T4.4 | Human Interface — Receiving | 4 | Verses on receiving characteristic | Verse text | ⚠️ Partial |
| T4.5 | Human Interface — Boundaries | 4 | Verses showing characteristic across relational boundaries | Verse text | ⚠️ Partial |
| T4.6 | Spiritual Beings Interface | 4 | Verses on angels/adversarial spirits + characteristic | Verse text scan; small set of registries | 🚧 Gap — programme acknowledges this is underrepresented |

**T4 summary:** ✅ for the divine pair; ⚠️ for human; 🚧 for spiritual beings — matches the programme's own statement in the framework prose that T4.6 is a recognised gap.

---

## T5 — Formative and Developmental Dimension

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T5.1 | Nature of Transformation | 3 | Verses on what the characteristic changes | Verse text + finding bodies | ⚠️ Partial |
| T5.2 | Sequence of Inner States | 3 | Verses showing sequence/progression | Verse text | 🚧 Gap — sequence is interpretive |
| T5.3 | Mechanism of Change | 3 | How transformation occurs | Verse text + finding bodies | ⚠️ Partial |
| T5.4 | Suffering and Affliction | 3 | Verses linking to suffering as formative context | Verse text + co-occurrence with R190/R191 (suffering / affliction) | ⚠️ Partial |
| T5.5 | Formation and Sanctification | 3 | Verses on long-arc formation | Verse text | ⚠️ Partial |
| T5.6 | Eschatological Trajectory | 3 | Verses on future fullness | Verse text | ⚠️ Partial |
| T5.7 | Deposit Consequence | 3 | What sustained operation produces over time | None directly | 🚧 Gap — feeds from T2.8 which is also a gap |

**T5 summary:** ⚠️ across the board with two 🚧. T5 prompts are highly inferential — verse text supplies the raw material, but mechanism/sequence/trajectory are analyst judgments not currently captured structurally.

---

## T6 — Structural Relationships with Other Characteristics

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T6.1 | Co-occurrence | 3 | Other registries that share verses | Computed from `wa_verse_records` cross-registry shared verses | ✅ Adequate (computed at extract time) |
| T6.2 | Sequential Relationships | 3 | Which characteristics precede / follow / accompany | Verse text + finding bodies | 🚧 Gap |
| T6.3 | Causal and Constitutive Relationships | 4 | Whether one produces another | Finding bodies | ⚠️ Partial |
| T6.4 | Vocabulary and Root Sharing | 4 | Shared Strong's root families across registries | `wa_term_root_family`; `mti_terms.transliteration` | ✅ Adequate |
| T6.5 | Distinctions | 4 | Where overlap requires differentiation | Finding bodies; SD pointers | ⚠️ Partial |
| T6.6 | Shared Verse Anchors | 3 | Verses anchoring multiple registries | Computed from `verse_context.is_anchor` cross-registry | ✅ Adequate (computed at extract time) |
| T6.7 | Dimensional Sharing | 3 | How many of this registry's dimensions are shared with another | `word_registry.dimensions` across registries | ⚠️ Partial — requires per-group dimensions (T1.8 gap feeds in) |

**T6 summary:** ✅ for T6.1/T6.4/T6.6 (mechanically computable); ⚠️ for T6.3/T6.5/T6.7; 🚧 for T6.2. T6 is the strongest tier in terms of mechanical computability.

---

## T7 — Evidential and Methodological Foundation

| Comp | Title | Prompts | Required data | DB source | Coverage |
| --- | --- | ---: | --- | --- | --- |
| T7.1 | Lexical and Semantic Analysis | 10 | Hebrew/Greek terms; root meanings; sub-senses; LXX bridging; NT coinage | `mti_terms`, `wa_term_inventory`, `wa_meaning_parsed` (7,449 rows), `wa_meaning_sense` (15,956 rows), `wa_lsj_parsed` (2 rows — sparse!) | ⚠️ Partial — meaning_parsed and meaning_sense are rich; lsj_parsed is sparse |
| T7.2 | Verse and Literary Interpretation | 6 | Verse role-in-sentence; logical structure; literary form (narrative/psalm/etc); contextual setting | `wa_verse_records.verse_text` + `books.testament`, `books.book_order`; literary form not stored | ⚠️ Partial — verse text + book metadata; literary form / contextual setting are interpretive |
| T7.3 | Human Science Frameworks | 4 | Psychology/moral philosophy/etc lenses applied | None — interpretive lenses applied at analysis time | 🚧 Gap by design — programme prose explicitly states human science is a sanity-check, not stored content |

**T7 summary:** ⚠️ for T7.1/T7.2; 🚧 for T7.3 (intentional). The biggest specific gap is `wa_lsj_parsed` — 2 rows DB-wide; LSJ data exists for very few terms.

---

## Cross-tier summary

| Status | Components | % |
| --- | ---: | ---: |
| ✅ Adequate | 12 | 21% |
| ⚠️ Partial | 32 | 57% |
| 🚧 Gap | 12 | 21% |

**Pattern.** T0/T6 are mechanically strongest (anchored in verse data + computable cross-registry stats). T2 (constitutional location) and T5 (formative/developmental) are the weakest — they ask interpretive questions for which no structured capture currently exists. T3 (inner faculties) is uniformly partial — verse text supports the inquiry but no structured "engages-faculty-X" flag exists.

## Concrete capture proposals (for researcher decision)

If you want to harden the structured coverage, these are the candidate schema additions in priority order. None are required for v2 prompts to be *answerable* (the verse text and finding bodies do the work) — but they would make the answers *queryable*:

1. **`verse_context_group.dimension_assignment`** (TEXT) — closes T1.8 / T6.7. Per-group dimension assignment currently lives in obslog narrative; lifting it into the group row would let extracts state dimension data as fact rather than inference.
2. **`wa_session_b_findings.engaged_faculties`** (TEXT, controlled-vocab list) — closes T3.1–T3.11. Each finding could declare which inner faculties (perception / cognition / memory / affect / volition / etc.) the finding engages, queryable for cross-word patterns.
3. **`verse_context.body_part_link`** + **`body_link_type`** (TEXT, TEXT) — closes T2.6/T2.7. Where a verse links the characteristic to a body part, capture the body part and the link type (emphatic/functional/expressive/indicative/mediating) on the verse_context row.
4. **`wa_session_b_findings.tier_component`** (TEXT) — links each finding to the v2 tier/component it answers. Replaces the v1 `wa_finding_catalogue_links` model with a tighter typed reference. Optional — the existing link table can carry this if extended.

None of the four are urgent. v2 catalogue extraction will work today — the prompts are answerable from the existing data. The schema additions only become valuable when you want to *query the answers* across the corpus, not just produce them per word.

---

## Action items surfaced by this assessment

1. **Update `_tmp_build_word_data_package.py`** to surface the new tier/component prompts and group the existing data sections under the relevant tiers — so AI gets prompts and answer data in one extract. *(In progress.)*
2. **Document the four capture proposals** above for future researcher decision.
3. **No urgent schema work needed** — extraction can begin now against catalogue v2.
