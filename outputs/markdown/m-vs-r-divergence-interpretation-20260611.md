# M vs R divergence — interpretation (VE-01 / obs 395)

> 2026-06-11. Companion to `m-vs-r-divergence-20260611.md` (raw candidate dump). **M** = mechanical
> term-gloss (lexical range, constant per term). **R** = verse-specific read sense. Goal: isolate
> term-in-verses where R is *materially* different from M (the read landed *outside* the lexical range,
> not merely disambiguated *within* it).

## Headline

The crude lexical-overlap method flags **1,439 of 3,702** comparable pairs (39%) as "material". **Reading the
actual rows proves this is NOT the materially-different set** — it is a mixture, and only a minority is genuine.
Lexical overlap cannot tell **synonymy** (wrath ≈ anger) or **spelling** (honour ≠ honor) from real
sense-divergence, so it over-states by ~3–4×. This is a textbook case of the standing rule: *the count
misleads; read the content.*

## The 1,439 decomposes into three kinds

| kind | approx size | material? | what it is |
|---|---|---|---|
| **Synonym-within-range** | majority (incl. all 367 M02) | **No** | R picks a correct synonym the gloss didn't spell letter-for-letter. `che.mah` R="fury" vs M="rage, wrath"; `cha.ron` R="wrath" vs M="anger, heat, burning"; `antilogia` R="dispute" vs M="argument". The read is right and in-range; the stemmer just can't see synonymy. Spelling variants too (`ka.vod` honour/honor). |
| **Empty mechanical gloss** | 60 rows / **22 terms** | No (data gap) | The term's mechanical obs-395 value is blank, so *any* read trivially "diverges". Terms: `sha.ma`, `ka.phar`, `ka.tat`, `a.zan`, … — a mechanical-backfill item, not a divergence. |
| **Genuine sense-divergence** | a minority (the prize) | **Yes** | R lands in a *different semantic field* than the gloss. See below. |

## The genuine material-divergence class (what we were actually looking for)

Reading the non-M02, non-empty rows, the real divergences cluster into four recognisable patterns:

- **Polysemy (broad-gloss → specific sense).** The standout is **`pneuma` (M25)**: M="wind, breath" → R=
  "the Holy Spirit" / "the human spirit" / "a bodiless spirit, ghost" / "the spirit of adoption". The gloss
  names the *literal* sense; the read supplies the sense actually in play. Confirms the broad-gloss-polysemy
  under-detection noted earlier ([[project_l2_multicluster_learnings_20260609]]).
- **Homonym / rank-vs-onset.** `archō` (M08): M="to be first (in rank/power)" → R="to begin" (inchoative).
- **Physical / literal pole vs inner.** `ka.phar` (M38): atone → "to coat/cover with pitch"; `ka.tat` (M24):
  → "beaten/crushed (of warriors)".
- **Morphology-driven stem sense.** Hiphil `sha.ma` "cause-to-hear = proclaim/declare" vs Qal "obey/hear";
  `cha.zaq` "strengthen" → "seize / take hold of".

These are exactly the **multi-sense terms** — the cases where a single mechanical lexical sense is least
meaningful and the verse-read adds the most. They are the same kind of term as the coverage gap (the broad
seat/framework terms): where M is weak, R is doing the real work.

## Conclusion & options

1. **Lexical overlap cannot isolate "materially different"** — synonymy + spelling defeat it. The true set is
   a fraction of 1,439 and must be separated by a **semantic read**, not a statistic.
2. **22 terms have an empty mechanical gloss** — a clean, finite backfill item, independent of this analysis.
3. The genuine class is **polysemy / homonym / physical-pole / morphology-stem** — `pneuma` is the exemplar.

**Suggested next step (cheap):** a CC read pass over the candidate pool (start with the 221 non-M02
ZERO-overlap rows) judging each *within-range* vs *outside-range/different-sense* → yields the precise
materially-different list. Alternatively, fix the 22 empty glosses first.
