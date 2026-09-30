# L1-mechanical prototype — findings & R-decisions (M01 vs M02)

> **Investigation · v1 · 2026-06-07 · CC.** Read-only. Interprets the L1-mechanical prototype run on **M01
> (Fear)** and **M02 (Anger)** — `scripts/_prototype_l1_mechanical.py`, raw output
> `wa-l1-prototype-m01-m02-comparison-v1-20260607.md`. Resolves/informs **R2, R4, R6** (R7 morphology is the
> next pass). Feeds the V3_2 schema catalogue.

---

## 1. Headline comparison

| | M01 Fear | M02 Anger |
|---|---|---|
| Terms | 83 (74 H / 9 G) | 44 |
| Single-sense | 69 (83%) | 31 (70%) |
| Multi-sense | 14 (17%) | 13 (30%) |
| **Verses on multi-sense terms** | **468 / 945 (49%)** | **413 / 645 (64%)** |
| Pole-span terms | 12 | 7 |

**The key number is verse-weighted, not term-count:** the multi-sense terms are the *high-frequency* ones,
so although only 17–30% of terms are multi-sense, **~half (M01) to two-thirds (M02) of verses sit on them**.
**M02 is markedly more polysemous by verse weight** — anger terms carry more senses than fear terms. So the
"needs analysis" residue (multi-sense select + pole) is a **major fraction of verses**, and **varies by
cluster** — the mechanical L1 cannot be assumed to settle most verses outright; the proportion must be
measured per cluster.

## 2. R2 — single/multi-sense detection: **works, generalises, needs a homonym filter**

The detector (stem-branches + numbered senses + pole-span) classified both clusters sensibly:
- **Correct singles:** `fobeō`, `fobos`, `pa.chad` (dread), `yir.ah`, `e.mah` (Fear); `riv` (strife),
  `qe.tseph`, `za.am` (indignation) (Anger).
- **Correct multis:** `ya.re` (fear/awe/revere, 3 stems), `ba.hal` (dismay/haste/alarm, 4 stems), `cha.tat`
  (shatter/broken/dismayed, 4 stems); `cha.rah` (incensed/burn, 4 stems), `ka.as` (provoke/grieve/vex),
  `orgē` (anger + punishment), `qa.na` (jealous/envy/zealous).
- **Signal strength:** the Hebrew **stem** count is the strongest, cleanest signal; **Greek** terms have no
  stems so the detector leans on pole-span / prose (e.g. `orgē` caught only via its external pole). → R2 is
  reliable for Hebrew; Greek needs the prose-sense and pole signals (works, but softer).
- **Refinement needed — homonym contamination:** `che.mah` picked up *"bottle"* (a homonym water-skin),
  `cha.tat` *"scar"* — the sense-set must be **homonym-filtered** (the same `ya.re` "shoot/pour" / `adēmoneō`
  "puzzled" pattern). Without it, the detector and keywords inherit unrelated senses.

## 3. R4 — STEP-capture keywords: **good core, strip the noise**

Keyword candidates are mostly the right sense tokens (`fear, revere, afraid, awe` / `anger, burn, heat`),
but carry three noise classes to strip:
- **Meta-words:** `aramaic`, `equivalent`, `used`, `always`, `act`, `absolute`.
- **Scripture refs:** `eph`, `col`, `mt`, `lk` (from sense_text citations).
- **Homonym tokens** (see R2).
→ **R4 decision:** keyword capture = the sense-token set **minus** {meta-words, scripture-ref tokens,
homonym senses}; keep the head gloss + sense words + pole tag. Cheap to implement (extend the stop-list +
a ref/homonym filter).

## 4. R6 — pole assignment: **the hard one — lexical alone over-triggers; three kinds of "physical"**

This is where the two clusters diverge most, and where pure lexicon **fails**. The prototype flagged
"inner/physical" on many terms, but for **three different reasons** that must be told apart:

| Kind | Example | Is it really the physical pole? |
|---|---|---|
| **Literal physical** | `mish.bar` "waves" (M01) | **Yes** — a physical object/event used metaphorically for inner crushing. True physical-pole term. |
| **Bodily manifestation** | trembling: `cha.rad`, `ra.gaz`, `a.rats`, `pa.lats` (M01) | **Arguably** — trembling/shuddering is the *body's* expression of fear. Inner-with-physical-manifestation. Researcher call. |
| **Dead metaphor (heat)** | burning anger: `che.mah`, `cha.rah`, `cha.ron`, `cho.ri` (M02) | **No** — "burning/heat" is the conventional Hebrew *metaphor* for anger; the term is inner, not physical. |

So **M01's pole-span is mostly bodily-manifestation (trembling); M02's is mostly dead-metaphor (heat)** —
a real cluster difference. **Only one genuine *external* pole appeared:** `orgē` → *vengeance / punishment*
(anger that becomes divine retribution) — correctly caught, and exactly the inner→external bridge the
3-pole model exists for.

→ **R6 decision:** pole **cannot be assigned by lexicon alone.** Proposed rule: (a) a **literal-physical
lexicon** (waves, shatter, melt) → physical; (b) an **external lexicon** (punish, vengeance, judgment) →
external; (c) **everything else inner by default**, with **heat/tremble/melt flagged as *metaphor
candidates*** for a light judgement pass — **not** auto-assigned to physical. The metaphor cases are the
residue, per-verse, at L2/L3 (the `mish.bar` lesson generalises).

## 5. R7 — morphology: a PARTIAL mechanical resolver (~14–22% of stem-conditioned verses)

Ran per-verse STEP morphology for the stem-conditioned Hebrew terms (raw:
`wa-l1-prototype-r7-morph-m01-m02-v1-20260607.md`). *(Methodology note: a `wa_term_inventory` join fan-out
inflated the first run; fixed to one inventory row per term — the numbers below are deduplicated. The
mechanical prototype in §1–4 was not affected.)*

- **M01:** 10 stem-conditioned terms, 506 verb-occurrences, **116 (22%) stem-disambiguated** (moved off the
  majority stem-branch).
- **M02:** 7 terms, 227 occurrences, **33 (14%) stem-disambiguated**.

**What the stem resolves — more than sub-senses:**
- The **off-majority slice (~14–22%)** is settled cleanly by stem, and for several terms the stem resolves
  the **pole** or **voice**, not just a shade of sense:
  - **Pole:** `cha.tat` — Qal *"shattered, broken"* (**physical**) vs Niphal *"dismayed"* (**inner**):
    morphology *resolves the pole split.*
  - **Voice / causation:** `cha.rad` Qal *"tremble"* vs Hiphil *"drive in terror, rout an army"*; `ka.as`
    Qal *"be vexed/angry"* (experience) vs Hiphil *"provoke to anger"* (cause it in another).
- The **majority slice (~80%)** stays in the dominant stem, which often still spans sub-senses (Qal `ya.re`
  = fear / awe / reverence) → the **within-stem residue** for L2 per-verse select.

**It confirms the R6 metaphor finding:** the burning-anger terms (`cha.rah`) are **Qal-dominant** (the heat
sits in the majority stem, *not* stem-separated) — so the "burning" is a **dead metaphor**, not a
stem-conditioned physical pole. Where the physical pole is *real*, it **is** stem-conditioned (`cha.tat`
Qal) and morphology catches it. So morphology is also an **R6 input**: a stem-separated physical branch =
likely real pole; an un-separated heat/tremble term = metaphor candidate.

**Conclusion:** morphology is a **valuable *partial* aid** — capture it (R7 schema: `morph_code`/`stem`),
use it to (a) settle the off-majority slice, (b) resolve stem-conditioned **pole** and **voice** splits, and
(c) feed R6. It does **not** remove the within-stem select residue (~80% of stem-conditioned verses), which
stays the L2 analytical load.

## 6. Recommendations for the R-decisions (for V3_2)

- **R1 — confirm:** mechanical-L1 reframe stands; the prototype runs end-to-end on two clusters.
- **R2 — adopt** the stems+senses+pole-span detector; **add a homonym filter** to the sense-set. Reliable for
  Hebrew, softer for Greek (lean on prose + pole).
- **R4 — adopt** sense-token keywords **with the noise filter** (meta-words, scripture refs, homonyms).
- **R6 — do NOT auto-assign pole from lexicon.** Literal-physical + external lexicons only; default inner;
  **flag metaphor candidates (heat/tremble/melt) for judgement.** Pole is partly mechanical, partly the L2/L3
  residue.
- **R7 — run the morphology pass next** to size the stem-resolved vs within-stem residue.
- **R3 / R5 / E9 (dual-meaning fields, existing-notes, field names):** the prototype shows L1 needs to store,
  per verse: `sense_multiplicity`, the selected `sense_id` (multi only), `pole` (+ `pole_is_metaphor` flag),
  `keywords`, and to **preserve** `analysis_note`. Decide the field layout against this list in the V3_2
  schema pass.

## 7. Schema implications surfaced (seed the V3_2 catalogue)

- `verse_context`: `sense_multiplicity`, `sense_id`, `pole`, **`pole_is_metaphor`** (new — from R6),
  `keywords` (STEP-capture), `step_meaning_applied`, `residue_flag`.
- `wa_meaning_sense`: a **homonym/biblical-sense filter** flag (so the sense-set excludes `che.mah`-bottle,
  `ya.re`-shoot).
- `wa_verse_records`: `morph_code` / `stem` (R7).
- `cluster_finding`: `finding_type`, scope anchors, `needs_research` (from E7).

---

## Recommendation

The mechanical L1 **generalises across both clusters** and the R-series is now resolved enough to settle
V3_2. The honest division of labour the prototype establishes:

- **Mechanical at L1 (clean):** meaning-anchoring (corroboration-by-construction), STEP-capture keywords
  (R4, with noise + homonym filters), single/multi detection (R2), morphology capture + stem-narrow (R7).
- **Mechanical-but-partial:** the stem settles ~14–22% of stem-conditioned verses (off-majority slice),
  incl. some pole/voice splits.
- **Stays judgement (the L2 residue, by design):** within-stem multi-sense **select** (~80% of
  stem-conditioned verses), and **pole** where it is metaphor (heat/tremble/melt) rather than stem-separated
  physical (R6 — `pole_is_metaphor` flag).

**V3_2 can now proceed.** Settle the schema against §7 (the field list), encode R6 as *default-inner +
metaphor-flag + literal/external lexicons*, add the homonym filter to the sense-set, and capture
morphology/stem. The remaining judgement (within-stem select, metaphor pole) is correctly the L2 analytical
load — not a gap, but the deliberate boundary between mechanical L1 and analytical L2.
