# STEP morphology — the per-verse sense signal we already have but don't capture

> **Investigation · v1 · 2026-06-07 · CC.** Read-only (STEP API + DB reads; no writes). Tests the
> researcher's hypothesis that *"STEP has already done the hard work to analyse a multi-sense verse, just not
> downloaded."* **It has — via per-occurrence morphology (the verbal stem).** Feeds the Phase-1 mechanical
> reframe (`Workflow/methodology/wa-phase1-mechanical-meaning-reframe-v1-20260607.md`) and rollup open item
> A1. STEP server: `http://localhost:8989` (ESV_th).

---

## The hypothesis and the finding

**Hypothesis:** for a multi-sense term, STEP may already encode which sense a given verse realises.

**Finding — yes, mechanically, through the verbal *stem*.** Every STEP verse span carries a `morph`
attribute, e.g. for `ya.re` (H3372):

```
Gen 3:10 "afraid"   <span morph='HVqw1cs'  strong='H3372G'>   → HV q … = Qal
Exod 15:11 "awesome"<span morph='HVNrmsa'  strong='H3372H'>   → HV N … = Niphal
```

The 3rd character is the **binyan (stem)**: `q`=Qal · `N`=Niphal · `p`=Piel · `h`=Hiphil · `P`=Pual ·
`H`=Hophal · `t`=Hithpael. And the lexical sense-tree (BDB, stored in `wa_meaning_sense`) is **branched by
that same stem**:

```
1a (Qal)    1a1 to fear, be afraid · 1a2 stand in awe · 1a3 reverence, honour, respect
1b (Niphal) 1b1 be feared/dreadful · 1b2 cause astonishment and awe · 1b3 inspire reverence/godly fear
1c (Piel)   make afraid, terrify
```

So **the per-verse stem selects the sense-branch.** This is a real, downloadable, per-occurrence
disambiguation that STEP supplies — and that the programme currently discards.

## Demonstration — `ya.re` stem distribution (from STEP morph, all occurrences)

| Code (suffix) | Verses | Qal | Niphal | Piel | Pole (registry) | Reading |
|---|---|---|---|---|---|---|
| **H3372G** ("frightening / DANGER") | 187 | 174 | 11 | 1 | fear/dread | Niphal e.g. Deut 1:19 *"terrifying"* = *be feared/dreadful* (1b1) |
| **H3372H** ("awesome / GOD") | 107 | 74 | **33** | 0 | reverence/awe | Niphal e.g. Exod 15:11 *"awesome"* = *inspire awe / be held in awe* (1b2/1b3) |

The Niphal share jumps from 6% (danger code) to 31% (god code) — the morphology **correlates with the
pole** the registry already assigned at suffix level. Niphal → the *be-feared / awe-inspiring* branch; Piel
→ the *terrify* (causative) branch; Qal → the *experience fear/awe* branch. **The stem mechanically picks
the branch.**

## What this gives the Phase-1 mechanical reframe

A new **mechanical disambiguation layer** for multi-sense terms, before any AI:

1. **Per-verse morphology → stem** (from STEP `morph`, already in the HTML we pull).
2. **Stem → sense-branch** (the BDB tree is stem-labelled).
3. **Narrows the sense-set** to the stem's branch — resolving a large share of stem-conditioned polysemy
   (very common in Hebrew verbs) **with zero interpretation.**

This shrinks the "needs advanced analysis" residue again: a `ya.re` Niphal verse is *mechanically* the
awe/be-feared branch; only **within-stem** polysemy (a Qal `ya.re` that could be plain fear *or* reverence —
Gen 28:17 vs a reverence Qal) still needs context. Stem does much of the multi-sense work for free.

## The gap — we capture neither signal

- **`wa_verse_records` has no morphology column.** The `get_verse_records*` client **strips** the HTML; the
  `morph` attribute is thrown away. We store plain verse text only.
- **`wa_meaning_sense.is_stem_label` / `.stem_label` are columns that exist but are populated `0 / 16005`.**
  The stem branches (`1a (Qal)`, `1b (Niphal)`…) sit **inside `sense_text`** as raw text, never parsed into
  the structured stem field. So the stem→sense mapping is present but not queryable.

Both are **already in the source** (STEP HTML morph; BDB stem labels in the def). Capturing them is
extraction + parse work, not new analysis.

## Limits (keep it honest)

- Morphology resolves **stem-conditioned** polysemy, not **within-stem** polysemy (Qal *fear* vs Qal
  *reverence*) — that residue still needs context/corpus.
- Greek morphology (tense/voice/mood) is less sense-bearing than Hebrew binyan, but voice (middle/passive)
  and deponency still matter for some terms; worth a parallel check on a Greek multi-sense term.
- The pole the *registry* assigned (G/H suffix) already encodes some of this; the morph adds the
  **per-verse** resolution the suffix can't (a single code still mixes Qal and Niphal).

## Recommendations (for the reframe / v3_1)

1. **Capture per-occurrence morphology at extraction.** `get_verse_records_with_html` already returns the
   raw HTML; add a parse of the target span's `morph` into a new `wa_verse_records` column (e.g.
   `morph_code`, `stem`).
2. **Parse the stem branches** of the sense tree into `wa_meaning_sense.stem_label` / `is_stem_label` (the
   columns are waiting).
3. **Add stem→sense-branch as a mechanical Phase-1 layer** (between "attach sense-set" and "select"): it
   pre-narrows multi-sense terms by stem, leaving a smaller within-stem residue for the light analytic pass.
4. **Follow-ups worth a probe** (not done here): whether STEP exposes a per-occurrence *sense number* or
   interlinear gloss beyond morph; and the Greek-voice equivalent on a Greek multi-sense term (`fobeō`).

---

*Confirms the researcher's intuition: the multi-sense analysis is partly pre-done in STEP, as morphology —
capture it rather than re-derive it.*
