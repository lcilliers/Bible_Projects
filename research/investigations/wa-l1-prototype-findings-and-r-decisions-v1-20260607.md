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

## 5. What still needs the morphology pass (R7)

The multi-sense terms classified above are largely **stem-conditioned** (the "N stems" terms). R7 —
capturing per-verse morphology and narrowing by stem — is what tells us **how much of the 49%/64%
multi-sense verse load resolves mechanically by stem**, leaving the true within-stem residue for L2. That is
the next prototype pass (STEP morph for the multi-sense terms of both clusters), and it directly sizes the
L2 analytical load.

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

The mechanical L1 generalises across both clusters, but the prototype proves **pole (R6) is the part that
resists pure mechanisation** (metaphor vs literal vs manifestation) and that the **multi-sense load is large
and cluster-variable** — so L1 mechanises *meaning-anchoring* and *keywords* cleanly, while *pole* and
*multi-sense selection* stay partly judgement. **Next:** run the R7 morphology pass on both clusters to size
the stem-resolved fraction, then settle the V3_2 schema against §7. Hold V3_2 until R7 is in.
