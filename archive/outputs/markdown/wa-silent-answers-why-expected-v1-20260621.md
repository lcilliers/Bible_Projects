# Silent answers — why silent, and is the silence expected?

- **File:** wa-silent-answers-why-expected-v1-20260621.md · **Date:** 2026-06-21 · **Author:** Claude Code · Read-only audit.
- **Builds on:** wa-silent-answers-by-cluster-char-v1-20260621.md (the per-char counts) and the full inventory in `outputs/markdown/_silent_inventory_working.json` (every silent question-ID + its stated reason, per characteristic).
- **Scope:** the captured tier-answer bodies — **M03, M04, M05, M06** (29 characteristics). M01 has no per-characteristic split; M02's per-char files are on disk but uncaptured. (See §6.)

## 1. Headline

**The silences are, almost without exception, reasonably expected.** Reading every isolated silent answer against its stated reason, each falls into one of six causes below — five of which are *expected by construction*, and one of which (defining) is itself a finding. **No "should-be-there-but-isn't" gaps were found in M04/M05/M06.** The one real lever is a single uniform band of *data-shape* silences (cause B) that is silent across nearly every characteristic programme-wide and is recoverable only by a different kind of pass.

## 2. The six causes of silence

| # | Cause | What it is | Expected? |
|---|---|---|---|
| **A** | **Faculty-not-engaged** | The catalogue probes 11 inner faculties × 3 sub-questions (engage? / effect? / pattern?). A characteristic engages only its *signature* faculties; the rest go silent — so these silences are the **inverse image of each characteristic's faculty signature**. | Yes — a *finding*, not a gap |
| **B** | **Data-shape** | The per-occurrence lexical extract structurally cannot answer questions about **development over time, formation, relational differentiation, or eschatology** (T5 formative, T1.6 over-time, T4.5 within-vs-across-bonds / covenantal, T4.3.3/T4.4 uptake, T6.3 constituent, T0.2.3 eschatology). The same questions are silent across *every* characteristic. | Yes — uniform; **recoverable via a verse-narrative pass**, not per-char lexical rework |
| **C** | **Register / structural** | No spiritual-being interface (T4.6) anywhere; no constitutional seat (T2) for the *outward/relational* characteristics (reproach, enmity, the bodily-but-unseated grief sub-types). | Yes |
| **D** | **Defining** | The absence *is* the finding: gentleness never engages **affect**; enmity, cruelty and friendship have **no divine instance**; compassion never engages **cognition**; the whole love-family never engages **creativity**. | Yes — *meaningful*; surface as findings |
| **E** | **Lexical-fit** | The catalogue asks about a *term-type* (person-type term, supplication term, NT-coinage, named opposite) the cluster's vocabulary simply does not contain (T7.1.x). | Yes |
| **F** | **Thin-evidence** | The sub-corpus is too small to assess (M06 enmity = 9 occ, loathing = 29 occ; reasons read "too few to assess"). | Yes given N — **widen the term seed** if more coverage is wanted |

**Key interpretive point.** Because of cause A, a characteristic's *silence count largely measures how narrow/focused it is*. High silence = a focused characteristic (gentleness, hatred engage few faculties); low silence = a broad one (love engages most). Silence is therefore a **coverage signature, not a quality defect**.

## 3. Verdict by cluster

**M03 Grief (10 chars).** Silents concentrate in **location** (no constitutional seat for felt-but-unlocated or outward sub-types — weeping, sighing), **lexical-fit** (T7.1 term-types), and the uniform data-shape items (T0.2.3 eschatology, T1.6 over-time). All expected. ⚠ *Caveat:* M03 answers in prose ("No mind-location", "Negative —") rather than a "Silent" marker, so it cannot be counted mechanically — a reliable M03 count needs a manual read.

**M04 Joy (7 chars).** The **same** silence profile across all seven: **faculty-not-engaged** (joy is affect-led — it does not engage perception/cognition/volition/moral-evaluation/agency at the pattern level: cause A) + the uniform **data-shape** band (relational differentiation T4.5, formation T5, constituent T6.3: cause B). All expected. *One exception worth noting, not a gap:* **G Soothing/pleasing-aroma** is silent at T7.3 because it denotes *divine satisfaction*, not a human inner state — which is the already-flagged scope doubt about whether it is a human inner-being characteristic at all (a researcher decision, carried in the M04 distillation).

**M05 Love (6 chars).** Low silence for the broad members (Love, Compassion, Kindness ≈ 2 faculty silents each); the meaningful silences are **defining**: **Gentleness** is silent on affect, perception and conscience (it is mind-governed); **Friendship** is silent at T0.1.1 (no divine bearer) and **Compassion** at cognition (pre-deliberative). Plus register (no spiritual-being interface, cause C). All expected; the defining ones are findings.

**M06 Hate (6 chars).** The most silence, from three expected causes stacked: **faculty-not-engaged** (hatred engages only 3 of 11 faculties: cause A), **data-shape** (heavy T5 formative/suffering/sanctification — the M06 synthesis already names this "data-shape limited, recoverable via a verse-narrative pass": cause B), and **defining** (enmity and cruelty have **no divine instance** — T0 silent: cause D). **Enmity** and **loathing** add **thin-evidence** silences (small sub-corpora: cause F). All expected.

## 4. The one real lever — the data-shape band (cause B)

The single most uniform silence across the whole programme is the **developmental/relational band**: T5 (formation, suffering, sanctification, eschatology), T1.6 (sustained over-time effect), T4.5 (operation within vs across relational/covenant bounds), T4.3.3/T4.4 (reception conditions), T6.3 (constituent/production relationships), T0.2.3 (created-design future). These are silent for **almost every characteristic in every cluster**, for one reason: the **per-occurrence lexical extract cannot see them** — they require reading verses *in sequence and context*.

**Implication:** if these answers are wanted, the route is a **verse-narrative pass** over the corpus (e.g. the Joseph, Amnon, Saul–David arcs for grief/hate), applied programme-wide — not per-characteristic lexical re-work. This is one decision affecting one band of questions across all clusters, not 29 separate tasks.

## 5. Genuine gaps

**None identified in M04/M05/M06.** Every silence the detector flagged as a candidate gap resolved, on reading its stated reason, to cause A (faculty signature) or cause B (data-shape). M03 cannot be confirmed mechanically (prose style), but its visible silences are all cause C/E/B. So the corpus's silence is, on this evidence, *honest and expected* — absences of evidence the analysis correctly declined to invent.

## 6. Loose ends / to extend coverage

- **M03 reliable count** — needs a manual semantic read (prose negatives defeat mechanical detection).
- **M01 / M02** — M01 has no per-characteristic tier split (only by-tier merged findings); M02's per-char `cN-…-tieranalysis` files are on disk but were never captured into `prose_section`. Capture M02 + re-cut M01 per-characteristic to bring them into this audit.
- **Thin clusters (M06 enmity, loathing)** — widen the NT term seed if cross-testament coverage is wanted.
- **Standardise the marker** — adopt M06's "X of Y per tier" coverage line across all tier-answer files so silence becomes a queryable field rather than four prose conventions.

---

*Full per-question inventory (every silent question-ID + the author's stated reason, per characteristic) is in `outputs/markdown/_silent_inventory_working.json`.*
