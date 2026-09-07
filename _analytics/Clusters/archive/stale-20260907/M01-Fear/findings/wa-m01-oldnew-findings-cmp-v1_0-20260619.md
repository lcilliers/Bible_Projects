# M01 Fear — OLD vs NEW findings: content comparison

- **File:** `wa-m01-oldnew-findings-cmp-v1_0-20260619.md` · **Date:** 2026-06-19
- **Prefix:** WA · **Version:** v1_0
- **Compares:** `WA-m01-findings-OLD-dbexport-bytier-v1-20260619.md` (DB export of `cluster_finding`, 7-characteristic model) against `WA-m01-findings-NEW-merged-bytier-v1-20260619.md` (authored 2026-06-18, 11-characteristic model).
- **Scope:** content comparison, not statistical. Both files answer the identical tier catalogue (T0.1.1 → T7.3.4, same 47 `[refit]` questions); the question set is not in view here — only what the two say.
- **Method note:** every claim below is traceable to one or both files. Where the two files reach different conclusions this is stated as observation; my reading of *why* is labelled interpretation; the meaning for the programme is labelled reflection.

---

## 1. The headline: same spine, two different bodies

The two sets are not in conflict on the central theology of fear. They agree on the load-bearing claims. What differs is **the unit of analysis** (7 characteristics vs 11), **the mode of capture** (synthesised consolidation vs one data-grounded finding per question), and **what the finding is built out of** (verse-reading synthesis vs JSON-field evidence). Your expectation — "there should not be a large difference in principles" — holds. The differences are real but they are differences of *resolution and grounding*, not of doctrine.

---

## 2. Structural difference (observation)

### 2.1 The characteristic model — the single biggest difference

| | OLD | NEW |
|---|---|---|
| Model | 7 characteristics, M01-A … M01-G | 11 characteristics, c1 … c11 |
| Naming | Thematic/phenomenological ("Reverential Fear / Fear of God as Governing Orientation", "Terror as Overwhelming Force") | Lexical/affect-graded ("Reverent fear/awe", "Dread", "Terror", "Trembling", "Shuddering", "Dismay", "Alarm", "Anxiety", "Astonishment", "Cowardice") |
| Sub-structure | VCGs (e.g. M01-A-VCG-02) with anchor verses | Direct per-characteristic breakdown, no VCG layer |

**The crosswalk** (my mapping, drawn from the content of both — labelled interpretation where the fit is loose):

- **OLD M01-A** (Reverential Fear) → **NEW c1** (Reverent fear/awe). Clean one-to-one.
- **OLD M01-B** (Acute Fear and Alarm) → splits across **NEW c2** (Fear/afraid), **c8** (Alarm), and **c10** (Astonishment). OLD's "acute" bucket is decomposed.
- **OLD M01-C** (Terror as Overwhelming Force) → splits across **NEW c3** (Dread) and **c4** (Terror).
- **OLD M01-D** (Dismay and Inner Collapse) → **NEW c7** (Dismay). Clean.
- **OLD M01-E** (Trembling / Fear Made Somatic) → splits across **NEW c5** (Trembling) and **c6** (Shuddering/horror).
- **OLD M01-F** (Anticipatory Dread and Anxiety) → splits across **NEW c9** (Anxiety) and part of **c3** (Dread).
- **OLD M01-G** (Timidity and Cowardly Shrinking) → **NEW c11** (Cowardice). Clean.

So the NEW model is, in effect, the OLD model with four of its broader groups (B, C, E, F) broken into their lexical constituents. This is the structural fact that produces almost every downstream content difference.

### 2.2 Capture mode

- **OLD** answers each question twice over: a `[consolidated — whole cluster]` paragraph plus one paragraph per sub-group. For many questions the consolidated text is copied verbatim into each sub-group row (e.g. T0.1.3, T2.1.4) — an artefact of the DB export, not seven distinct findings. OLD also splices in *folded Session B findings* (e.g. the DIM-61-001 fobeō tripartite-structure note repeated under T1.2.1).
- **NEW** answers each question once, then gives a clean per-characteristic (c1–c11) enumeration underneath. No VCG layer, no consolidated/sub-group duplication.

### 2.3 Grounding

- **OLD** is synthesised from verse readings and VCG anchors. It reasons theologically and cites anchors (Pro 1:7, Exo 15:11, Psa 6:3). Counts are rare.
- **NEW** is built on JSON extract fields and quotes verses verbatim. It routinely reports `divine_involvement` counts, valence counts (righteous/commanded/forbidden/neutral/sinful), `type` distributions (action/status/quality), location counts, and `immediate_response` fill rates — and then quotes the verse (Psa 130:4, Exo 15:16, 2Ti 1:7).

**Reflection.** These are two genuinely different documentary genres doing the same job. OLD reads like a *finished interpretive synthesis*; NEW reads like a *grounded analytical workpaper* one stage before synthesis. For Session C (reader-facing), OLD's prose is closer to publishable; for audit and traceability (GR-PROC-002), NEW is far stronger because each claim is tied to a field value or a quoted verse.

---

## 3. Where the two AGREE on principle (observation)

The core findings are stable across both models:

1. **Fear is never borne by God as experiencer — it is creaturely.** OLD: "Scripture does not attribute fear as an inner experience to God." NEW: "`divine_involvement` = experiencer: 0 of 975 … never feels it." Same conclusion; NEW puts a number on it.
2. **Reverent fear of God is the one positively-ordered, created-design form.** Both single out M01-A / c1 as the equipping, commanded, righteous strand and treat the rest as conditions endured or resisted.
3. **The heart is the dominant constitutional seat.** OLD: "the heart is fear's primary constitutional home." NEW: "Heart is the dominant constitutional seat across the cluster (61 of the located records)."
4. **The cluster is overwhelmingly NOT spirit-level.** Both reach this explicitly.
5. **Isa 66:2 (trembling of the contrite spirit) is the clearest spirit-level case.** Both name it as the deepest, positive constitutional witness.
6. **Cowardice/timidity is the disordered pole, answered by 2Ti 1:7.** Both treat it as vice and both read the "spirit of power, love, self-control" as its counter.
7. **Reverent fear is epistemologically and relationally constitutive** (the beginning of wisdom; the posture for covenant). Both carry this.

**Reflection.** On the questions that matter most for the programme's governing question — where fear sits in the spirit/soul/heart/body structure, and what its place is in the divine image — the two models converge. That convergence under two independent capture methods is itself a quiet validation of the M01 conclusions.

---

## 4. Where the two genuinely DIVERGE on content (observation → interpretation)

These are the points worth your attention. They are not stylistic; they are different answers.

### 4.1 Mind-location — a direct conclusion conflict

- **OLD (T2.4.1):** the mind is "a secondary but evidenced constitutional location," specifically for M01-D (dismay disrupting thought, Dan 4:19; 7:28) and M01-F (anxiety as cognitive rumination).
- **NEW (T2.4.1):** "**No — uniformly. 'Mind' is never a recorded location in any of the eleven characteristics** (0 across the cluster)."

**Interpretation.** This is the methodology difference made visible. OLD *infers* mind-engagement from the verse content (dismay clearly disrupts thinking; anxiety clearly ruminates). NEW reports the **location field**, and the field carries no `mind` value anywhere. Both are "true" to their own method — but they hand the reader opposite headlines. NEW would say dismay/anxiety *affect* cognition (a faculty question, T3) without being *located* in the mind (a constitutional question, T2); OLD blurs that line. This is the cleanest example of why the two files feel different: OLD answers from meaning, NEW answers from data.

### 4.2 The second spirit-level case

- **OLD:** two spirit-level cases — Isa 66:2 trembling (M01-E) **and** 2Ti 1:7 timidity (M01-G), reading "the spirit God has not given" as a spirit-level constitutional location for cowardice.
- **NEW:** two spirit-level cases — Isa 66:2 trembling (c5) **and** Ecc 7:9 *bahal* dismay (c7). NEW records c11 cowardice as **silent** on spirit-location.

**Interpretation.** OLD treats the "spirit" in 2Ti 1:7 as locating timidity at the spirit level. NEW appears to read that "spirit" as the Spirit's *gift* rather than a claim about where cowardice sits constitutionally — so it does not count it as a location — and instead surfaces Ecc 7:9 from the *bahal* field. Worth a decision: is 2Ti 1:7 a spirit-*location* finding or a divine-gift finding? The two files have answered that differently.

### 4.3 Resolution that the OLD model could not surface

Because NEW separates dread / terror / shuddering / alarm / astonishment, it states distinctions the OLD coarser grouping cannot:

- **c4 terror reaching the soul as much as the heart** (soul 3 ≥ heart 3) — "the first characteristic where terror reaches the soul." OLD's M01-C folds terror into a force-on-the-person reading and does not isolate this.
- **c9 anxiety's near-total divine silence** ("agent 1 … images almost nothing of God's nature … furthest from the divine image of any fear"). OLD's M01-F bundles anxiety with anticipatory dread and does not isolate this striking near-silence.
- **c10 astonishment as a distinct borderline-with-awe characteristic** — entirely absent as a named thing in OLD (it lives inside M01-B).

**Reflection.** This is the chief *gain* of the NEW model: finer characteristics expose findings that were invisible at the 7-group resolution. The corresponding *cost* is that the NEW model fragments the unified theological picture that OLD's named groups carry so well — e.g. OLD's "Terror as Overwhelming Force" reads as one coherent theological idea; NEW's c3+c4 read as two lexical buckets that the reader must reassemble.

### 4.4 Eschatological / future-fullness orientation

- **OLD (T0.2.3):** comparatively rich — Rev corpus for M01-A, restoration promises for M01-E, "salvation and quiet rest" for M01-D — reads the cluster as carrying a real orientation toward a purified future fear.
- **NEW (T0.2.3):** "**Largely silent in the lexical fields; thin eschatological markers only** … the cluster is not characteristically future-oriented."

**Interpretation.** Again the method gap: OLD's theological reading finds eschatological shape that the NEW lexical-field scan does not register as a *field* signal (NEW routes those readings to T7.2 as inferential). Not a contradiction so much as a difference in what each is willing to assert without a field to stand on (cf. GR-PROG-009: inferential is not confirmed).

---

## 5. What each model does better (reflection)

**OLD is stronger at:**
- Coherent theological synthesis ready for a reader.
- Holding a characteristic together as one idea (the named groups carry meaning).
- Surfacing typology/eschatology by interpretive reading.
- Integrating prior Session B findings (the folded DIM notes).

**NEW is stronger at:**
- Traceability: each claim sits on a field value or quoted verse (GR-PROC-002 compliance).
- Honesty about silence: it records "silent / 0 / thin" explicitly and per-characteristic rather than smoothing it into prose.
- Resolution: the 11-way split exposes findings the 7-way grouping hides (c4 soul-depth, c9 divine-silence, c10 astonishment).
- Discipline against over-reading: it declines to assert mind-location or eschatological orientation that the fields do not carry, routing inferential material to T7.2.

---

## 6. Open questions for the researcher (interpretive forks — paused)

1. **Which characteristic model governs going forward** — the 7 (OLD) or the 11 (NEW)? Several published M01 chapters and the Session B C1–C7 tier docs were built on the 7-group model; the NEW findings are 11-group. A decision here cascades.
2. **Mind-location (§4.1):** adopt NEW's field-literal "mind = 0" or OLD's "secondary-but-evidenced"? This affects the T2 constitutional map directly.
3. **2Ti 1:7 (§4.2):** is it a spirit-*location* finding or a divine-*gift* finding? The two files disagree.
4. **The gains in §4.3** (c4 soul-depth, c9 divine-silence, c10 astonishment): should these be carried back into the synthesis/publication layer even if the 7-group model is retained as the reader-facing frame?

---

## 7. Where additional data would help (highlighted, not assumed)

- A **crosswalk table in the database** mapping the 7 OLD characteristics to the 11 NEW ones would let CC verify that no OLD VCG content is orphaned by the re-grouping.
- The NEW file references valence/location *counts* but the underlying **record-level export** is not in hand here; confirming the NEW counts against the current versioned extract (GR-DATA-004) would close the loop before any reconciliation is acted on.
- The OLD file's **folded Session B findings** (DIM-61-001 etc.) do not appear in the NEW set; whether they were deliberately dropped or simply not yet merged is not determinable from the two files alone.
