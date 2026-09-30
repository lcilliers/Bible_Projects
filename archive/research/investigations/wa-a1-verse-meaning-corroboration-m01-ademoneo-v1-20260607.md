# A1 · Verse-meaning corroboration — first demonstration (M01, term 1 of 176)

> **Investigation / decision-support · v1 · 2026-06-07 · CC.** Read-only (no DB writes). Anchored to
> `Workflow/methodology/wa-cluster-rollup-design.md` **open item A1**. Purpose: make "basic verse-meaning
> corroboration" concrete by testing it on one term — does the AI-derived **verse meaning** sit *in line with*
> the term's **STEP lexical meaning**? This is the smallest, basic form of A1 (corroborate against STEP);
> the fuller form (several translations + divergence flag) is noted at the end.

---

## What A1 asks (anchored to the roll-up design)

The roll-up's L3 derives each verse's meaning by reading the actual verses together (clarify-by-corpus,
open questions) — but it has **no external corroboration step**. A1 is the gravest data risk: a verse meaning
can be internally coherent yet drift from what the word actually means. **Basic corroboration** = check the
derived verse meaning is *in line with the STEP meaning of the term*. This demonstration runs that check by
hand for one term so we can see what the step needs to do.

## Method

1. Take M01 (*Fear, Dread and Terror*), **first term by id** → **G0085 `adēmoneō`** ("be distressed"),
   an OWNER term, 3 occurrences (NT-only) — a clean, small set for a first pass.
2. **Summarise its STEP meaning** from the lexical fields (`step_search_gloss`, `short_def_mounce`, LSJ,
   parsed sense).
3. **Pull the verse meanings** (`verse_context.analysis_note`) for each of its verses.
4. **Compare** each verse meaning against the STEP meaning — aligned / drift / divergent.

---

## Step 1 — STEP meaning of `adēmoneō` (G0085), summarised

| Source field | Content |
|---|---|
| `step_search_gloss` / `word_analysis_gloss` | be distressed |
| `short_def_mounce` | to be troubled, distressed |
| Parsed sense (`wa_meaning_sense`) | "to be troubled, distressed; to be depressed, or dejected, **full of anguish or sorrow**" — Mt 26:37; Mk 14:33; Phil 2:26 |
| LSJ entry | "to be **sorely troubled or dismayed, be in anguish**; (ὑπό τινος) to be puzzled by…" |
| Occurrences | 3 (about), NT only |

**STEP summary (the corroboration baseline):** an inner state of **deep distress / trouble — anguish,
sorrow, dejection, dismay**. A heavy, agitated, sorrowful inner condition. (A secondary classical sense
"to be puzzled" appears in LSJ but is not the biblical sense.)

---

## Step 2 — Verse meanings of the term's verses, and the comparison

| # | Ref | Target word (ESV) | Derived verse meaning (`analysis_note`) | vs STEP meaning |
|---|---|---|---|---|
| 1 | **Mat 26:37** | troubled | "Jesus begins to be sorrowful and troubled in Gethsemane; the distress is a **deeply agitated inner state** engaging his soul as he faces the approaching suffering, manifesting as **anguished heaviness of spirit**." | **Aligned** — "anguished", "distress", "agitated inner state" map directly onto STEP's *anguish / troubled / distressed*. |
| 2 | **Mar 14:33** | greatly distressed | "Jesus begins to be **deeply distressed** in Gethsemane — this is a **severe inner anguish**, initiated in the soul as he faces what is coming, paired with being troubled at the same moment." | **Aligned** — "deeply distressed", "severe inner anguish" = STEP's *distressed / anguish / sorely troubled*. |
| 3 | **Phili 2:26** | distressed | "Epaphroditus was distressed because the Philippians had heard of his illness; the distress is **relational — an inner anguish** arising from concern about how his condition has troubled those he loves." | **Aligned** — "distress / inner anguish" matches STEP; adds the *relational cause* (situational, not a sense-shift). |

---

## Result

**3 / 3 verses aligned with the STEP meaning.** Every derived verse meaning lands inside STEP's semantic
envelope (*distress / trouble / anguish / sorrow*). No drift, no divergence, no false sense (the classical
"puzzled" sense is correctly absent). The verse meanings legitimately **add context** STEP cannot give —
*who* (Jesus / Epaphroditus), *the trigger* (approaching suffering / a loved one's worry), and *the inner
register* (heaviness of spirit, relational concern) — without contradicting the lexical sense.

This term **passes basic corroboration.**

---

## What this tells us for designing the A1 step

This hand-run shows the shape of the check the roll-up needs at/after L3. For corroboration to be a real
roll-up step, it needs:

1. **A baseline to corroborate against.** For G0085 it came from four fields stitched together
   (`step_search_gloss`, `short_def_mounce`, parsed `wa_meaning_sense`, LSJ). The step needs a defined
   **"STEP sense baseline"** per term — which fields, in what priority, and how the *biblical* sense is
   separated from classical/secondary senses (the LSJ "puzzled" sense had to be set aside by judgement).
2. **A verdict vocabulary.** Aligned / context-added / **drift** (still within sense but stretched) /
   **divergent** (outside the lexical sense — the flag that matters). Only the last two are worklist items.
3. **A home for the verdict + the divergence flag.** A1 currently has no field. Candidates: a
   `verse_context` column, an `cluster_observation` of a new type, or an **open-question / flag** row (ties
   to open items **E7** open-questions home, and the "open questions = corroboration worklist" note in L3).
4. **The translations dimension.** This run used ESV only (the stored `translation`). Full A1 wants the
   meaning checked against **several translations** so a quirk of one rendering doesn't drive the meaning.
   Not yet tested here — needs a multi-translation source decided (open item, ties to STEP pull).
5. **Where it sits in the roll-up.** This is a **post-L3 corroboration pass** (the meaning must exist
   first). Open question A2 (audit gates) — does it gate L3 before meanings roll up to L4, or run as a
   sweep? This clean term suggests a cheap automated first-pass (aligned cases need no human), reserving
   researcher attention for drift/divergent flags.

### Caveats on this being a *first* term
- `adēmoneō` is an **easy case**: 3 verses, one tight sense, two of them the same Gethsemane event. The
  corroboration step will be tested far harder by **valence-ambiguous / multi-sense terms** (e.g. `ya.re`
  H3372 — *fear* vs *revere*, which the gloss list already splits as "to fear" vs "to fear: revere"). The
  next demonstration should deliberately pick such a term to see corroboration catch a real sense-split.

---

## Decision needed (A1)

Confirm the **basic** A1 definition demonstrated here — *verse meaning must be in line with the term's STEP
sense; aligned passes, drift/divergent flag to a worklist* — and then decide the five design points above
(baseline definition, verdict vocabulary, verdict home, translations dimension, position in roll-up). Once
settled, A1 is encapsulable into the v3_1 instruction as a post-L3 corroboration pass.

---

*Source: `database/bible_research.db` — `mti_terms` / `wa_term_inventory` / `wa_meaning_sense` /
`verse_context` / `wa_verse_records`, term G0085, M01. Read-only.*
