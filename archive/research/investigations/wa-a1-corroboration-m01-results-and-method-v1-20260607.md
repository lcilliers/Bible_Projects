# A1 · Verse-meaning corroboration — M01 full results + systematised method

> **Investigation / methodology · v1 · 2026-06-07 · CC.** Read-only (no DB writes). Anchored to
> `Workflow/methodology/wa-cluster-rollup-design.md` **open item A1** (the gravest data risk). This is the
> full M01 corroboration test (all 83 terms / 949 derived meanings) **and** the recorded process for
> systemising A1. Builds on the single-term demo `wa-a1-verse-meaning-corroboration-m01-ademoneo-v1`.
> Raw scan: `wa-a1-corroboration-scan-m01-v1-20260607.md`. Scanner: `scripts/_assess_verse_corroboration.py`.

---

## 1. What A1 corroborates (settled by this test)

**Basic verse-meaning corroboration = each verse's derived meaning (`verse_context.analysis_note`) must
realise one of the term's STEP lexical senses, and lie inside that term's *sense-set*.**

The decisive realisation from M01: a term does **not** have *a* meaning — it has a **sense-set** (an
envelope of senses), and **different verses realise different senses**. Examples found:

- **`ya.re` (H3372)** spans *be afraid · stand in awe · reverence/honour · terrify* — the registry already
  splits it at suffix level (**H3372G** = "frightening (DANGER)" vs **H3372H** = "awesome (god)").
- **`ra.gaz` (H7264)** spans *tremble/quake · be agitated/disturbed · rage/anger · political unrest* — and
  its verses realise each: anger ("be angry and do not sin", Ps 4:4), trembling at theophany (Ps 77:16),
  political unrest (Jer 50:34).
- **`cha.tat` (H2865)** spans *shattered/broken* (physical pole) vs *dismayed/terrified* (inner pole).

So corroboration is not "verse = the meaning" but **"which sense does this verse realise, and is it within
the envelope?"** — and it interacts directly with the **3 scope-poles** (inner / external / physical).

---

## 2. The systematised method (the process to record)

A1 is **high-volume** (~950 verses for one cluster; ~tens of thousands programme-wide). Reading every verse
by hand in an expensive model is the wrong cost shape. The method that emerged is a **3-tier triage** —
mechanical does the bulk, judgement is reserved for the genuinely uncertain.

| Tier | Who | What | M01 outcome |
|---|---|---|---|
| **T0 · Assemble** | CC (script) | Per verse, build the **STEP sense-set** (gloss + `step_search_gloss` + `short_def_mounce` + `meaning` + parsed `wa_meaning_sense`) and pair it with the derived meaning. | 83 terms, 949 meanings assembled |
| **T1 · Mechanical corroboration** | CC (script) | Lexical-overlap (stemmed) between sense-set tokens and the meaning text. Overlap → **provisionally corroborated**. No overlap → **residue**. | **921 / 949 (97.0%)** auto-corroborated; **28** residue |
| **T2 · Judgement** | AI / researcher | Read only the residue: synonym-miss (true align), genuine **drift/divergence**, or **pole** case. | 28 read → **28 true-align**, **0 divergent**, **3 notes** |

**Cost shape:** for M01, real judgement touched **28 verses, not 949** — a ~34× reduction. The mechanical
tier is a cheap script; only the residue costs model/researcher attention.

**Crucial caveat (keeps the method honest):** overlap is **necessary-not-sufficient** evidence —
no-overlap **≠ wrong**, it means *not mechanically confirmed, read it*. T1 cannot by itself certify
alignment (a meaning could echo a sense word yet still misread); its role is **triage**, surfacing the
residue. A heavier T2 audit (sampling the corroborated set) is a separate, optional pass (ties to A2).

### Verdict vocabulary (for the residue, and any T2 sample)
`ALIGNED` (realises a sense in the envelope) · `ALIGNED+NOTE` (realises a *secondary* sense worth recording —
reverence-of-a-dread-term, positive-awe, physical-pole metaphor) · `DRIFT` (within the field but stretched
past any listed sense) · `DIVERGENT` (outside the lexical envelope — **the flag that matters**) ·
`NO-MEANING` (relevant verse with no derived meaning yet — a coverage gap, not a corroboration result).

---

## 3. M01 results

- **83 terms · 1026 verse rows · 945 relevant · 949 with a derived meaning.**
- **Mechanically corroborated: 921 / 949 (97.0%).**
- **Residue adjudicated: 28 → all ALIGNED; 0 DRIFT; 0 DIVERGENT; 3 ALIGNED+NOTE.**
- **Net: 949 / 949 derived meanings corroborate to the term's STEP sense-set. Zero divergences.**
- **Coverage gap (separate from corroboration): 77 verse rows carry no derived meaning** (set-aside or
  not-yet-analysed) — to be checked under the coverage/mop-up discipline, not A1.

**Reading of the result:** M01's derived verse meanings are **disciplined** — they stay inside the lexical
envelope of their terms. The whole residue was the heuristic's own blind spots (synonyms + a stemming
quirk), not analytical error. That is a reassuring signal for the L3 meaning quality on this cluster, and a
clean validation that the tiered method finds the real signal cheaply.

### 3.1 Why the 28 residue were all true alignments (heuristic limits to fix)
- **Synonym misses** (T1 has no thesaurus): *terror↔terrified*, *panic↔alarm*, *intimidated↔afraid*,
  *frightened↔afraid*, *shudder↔quiver*, *fear↔dread*. → add a small **fear-domain synonym map** to T1.
- **Stemming quirk:** double-suffix words mis-stem (`distress`→`distres` vs `distressed`→`distress`;
  `trembling`/`tremble`; `disturbance`/`disturb`). → improve the stemmer or match on shared prefix.

### 3.2 The three ALIGNED+NOTE cases — exemplars of what A1 should record
These are *not* errors; they are the secondary-sense / pole realisations A1 exists to make visible:

| Term · Ref | Sense realised | Why it matters |
|---|---|---|
| **`pa.chad` H6343 · 2Ch 19:7** | "fear of the LORD" as an **inward ethical constraint** | A *dread/terror* term realised as **reverence** — the dread→reverence bridge (the `ya.re` G/H split in another term). Record as the reverence sub-sense. |
| **`a.yom` H0366 · Song 6:10** | beauty "awe-inspiring as an army" | A *terrible/dreadful* term realised as **positive awe** (valence flip). The overwhelm is inner; the trigger is beauty, not threat. |
| **`mish.bar` H4867 · Psa 88:7** | "waves overwhelm… crush the inner person" | A **physical-pole** term (literal sea-waves) used **metaphorically** for inner crushing. Corroborates the *physical* sense; inner-being relevance is by metaphor → pole note. |

These three are the live evidence that the corroboration verdict must carry a **sense-realised** field and a
**pole** flag, not just pass/fail.

### 3.3 The full 28-row adjudication
The residue rows (with the derived meaning and STEP sense-tokens for each) are in the raw scan
(`wa-a1-corroboration-scan-m01-v1-20260607.md`, Residue table); the T2 verdict for every one is **ALIGNED**,
the three in §3.2 carrying NOTEs. Residue by term: `ba.hal`(2), `ke.ra`,
`emfobos`(4), `ekfobos`, `gur`, `fobeō`, `cha.rad`, `a.rats`, `pa.chad`(2), `ra.gaz`(10), `ya.re`(H3373),
`a.yom`, `mish.bar`, `be.hal` — **all ALIGNED**, the three above carrying NOTEs.

---

## 4. What this settles for the A1 design (for v3_1)

1. **Definition — confirmed.** Corroborate the derived meaning against the term's **STEP sense-set**;
   aligned passes; **DIVERGENT** is the flag that matters. *(M01 produced none — good, and a useful
   negative-control that the method doesn't manufacture false alarms.)*
2. **Baseline source — confirmed.** The STEP sense-set = `mti_terms.gloss` + `wa_term_inventory`
   (`step_search_gloss`, `short_def_mounce`, `meaning`) + parsed `wa_meaning_sense`. Outlier homonyms
   (e.g. `ya.re` "(TWOT) to shoot, pour"; `adēmoneō` LSJ "puzzled") must be **excluded by judgement** —
   the baseline needs a "biblical-sense vs homonym" filter.
3. **Method — confirmed.** Mechanical T1 triage + T2 residue judgement. Reusable scanner already built
   (`scripts/_assess_verse_corroboration.py`), cluster-parametrised — runs programme-wide.
4. **Verdict needs a home and structure** (ties E7): a `sense_realised` value + a `pole` flag + a
   `corroboration_verdict` enum. Candidate: columns on `verse_context`, or a typed `cluster_observation`,
   or a flag row. **Decision pending.**
5. **Where it sits in the roll-up** (ties A2): a **post-L3 pass** (meaning must exist first). T1 can run
   automatically as each VCG's meanings land; the residue gate is the human/AI touch-point before L4.

### Open decisions to put to the researcher
- **D-A1-a · Verdict home & fields** — which table carries `corroboration_verdict` / `sense_realised` /
  `pole`? (links E7, E4).
- **D-A1-b · Translations dimension** — M01 used the single stored ESV rendering. Full A1 wanted *several
  translations* so one quirky rendering can't drive the meaning. Worth it, or is STEP-sense corroboration
  enough? (cost vs assurance).
- **D-A1-c · T1 recall upgrades** — adopt the fear-domain synonym map + stemmer fix before the programme run
  (cuts residue noise).
- **D-A1-d · T2 depth** — residue-only (cheap), or also a **sampled audit of the corroborated 97%** (catches
  the necessary-not-sufficient gap)? Sets the A1↔A2 boundary.
- **D-A1-e · Homonym filter** — how the baseline excludes non-biblical senses (manual per-term note vs rule).

---

## 5. Recommendation

Adopt the tiered method as the A1 step. It is **cheap, reusable, and already validated on a full cluster**:
97% mechanical, judgement on 3% residue, zero divergence on M01. Before the programme run, apply the two T1
recall fixes (synonym map + stemmer) so the residue is genuine-uncertainty rather than heuristic noise, and
settle the verdict-home decision so results are recorded in the DB, not just these `.md`s.

*Next demonstrable step if you want it: run the same scanner on a cluster more prone to valence-splits
(e.g. an anger/desire cluster) to stress the DIVERGENT verdict that M01 never triggered.*
