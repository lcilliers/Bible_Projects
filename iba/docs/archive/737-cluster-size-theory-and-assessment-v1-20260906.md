# Cluster Size — Theory and Per-Cluster Assessment

- **filename:** 737-cluster-size-theory-and-assessment-v1-20260906.md
- **date:** 2026-09-06
- **escalation:** #737 (extends #1525's readiness evaluation and the size dimension raised there)
- **status:** Part A is reasoned judgement (labelled as such where it is an estimate, not a
  measured fact). Part B is a live query, full 85-cluster coverage.

---

## Part A — Theory

### A1. How is a cluster's "size" actually determined?

Three distinct measures exist, and they answer different questions:

- **Membership size** (`cluster_strong` row count) — how many distinct words define the cluster.
  A *breadth* measure. Doesn't by itself say how much reading work the cluster represents.
- **Verse-set size** (distinct verses reached via `cluster_strong` → `verse_lexical`) — how many
  verses actually need a debate pass. This is the **operative size for readiness/consumption**,
  because the proposal's Step 1 explicitly gathers *verses*, not strongs, and Step 4 reads one
  verse at a time.
- **Concentration** (what share of a cluster's verse-set comes from its single most-frequent
  member strong) — a size-adjacent signal I hadn't checked before. It answers a different
  question: is this cluster a genuine family of interlocking words, or effectively "one word's
  verses, with a handful of others attached"? A cluster can be large in verse-count and still be,
  in substance, dominated by one lemma.

### A2. How will size actually be consumed?

Per the proposal (Steps 3/3b/4), the atomic unit handed to the debate step is **one verse**: full
verse, every phenomenon in it, checked against the earmarked catalogue (≈59 HIB-relevant
questions), with backward/forward context pulled in as needed. That is inherently slow,
attention-heavy work per verse — not a lookup or a classification pass. Given the researcher's
explicit standing principle this session (AI quality and consistency degrade on large repetitive
tasks, which is exactly why Layer 2 is on-demand and never bulk), **the same principle applies
here**: a cluster's verses cannot be run through as one undifferentiated pass regardless of count.
They need to be consumed in bounded sittings, each producing findings that persist (this is what
Step 3b's "fold in prior findings for already-touched verses" mechanism is *for* — it's what makes
a multi-session cluster coherent across sessions, not just what handles cross-cluster overlap).

**Consequence: a cluster's verse-set size determines how many sessions it will take to complete —
not whether it can be done.** A 14-verse cluster is one sitting. A 3,662-verse cluster is not a
different *kind* of task, but it is a much longer-running one, and it introduces a risk that small
clusters don't have: **cross-session consistency drift** — does session 50's judgement on an
ambiguous case match session 3's? That risk, not raw infeasibility, is what "large" actually means
here.

### A3. What is "too large"? (my own estimate — no measured project figure exists yet)

No per-session verse throughput has ever been established for this method at this depth (it's
never been run for real at any cluster). I'd rather say that plainly than assert a false-precision
number. My own reasoned estimate, given the depth of what one verse requires (identify every HIB,
formulate every phenomenon, walk ~59 catalogue questions, ground each in evidence, check adjacent
verses, record the unresolved ones explicitly): a sustainable session is probably in the **low
tens of verses** — I'd guess 15–30 — not hundreds. **This should be calibrated empirically from
the first real submission, not assumed from this estimate.** Given that, I'd reframe "too large"
away from a rejection threshold (nothing here should be excluded just for being big) and toward a
**scheduling and consistency-management question**: a cluster whose verse-set implies many dozens
or hundreds of sessions needs an explicit plan for maintaining judgement consistency across that
many sittings before it's submitted — that plan doesn't exist yet, for any cluster.

---

## Part B — Assessment: size suitability of all 85 M-clusters

Bands by verse-set size, illustrative session count shown at my own estimated 20-verses/session
rate (labelled illustrative — see A3), and a concentration flag where the single largest member
strong accounts for ≥55% of the cluster's own verses.

**Band distribution:**

| band | clusters |
|---|---|
| Very Large (1,600+ verses) | 9 |
| Large (800–1,599) | 22 |
| Medium (300–799) | 27 |
| Small (100–299) | 17 |
| Tiny (<100) | 10 |

### The 9 Very Large clusters — not a first-exemplar candidate; need a consistency plan before submission

| code | short_name | verses | concentration | ~sessions @20 |
|---|---|---|---|---|
| M42 | Prayer & Petition | 3,662 | 27% | ~183 |
| M65 | Speech & Tongue | 3,092 | 31% | ~155 |
| M47 | Inner Seat | 2,713 | 20% | ~136 |
| M23 | Strength & Courage | 2,604 | 24% | ~130 |
| M15 | Knowing & Understanding | 2,528 | 35% | ~126 |
| M22 | Praise & Song | 2,100 | 16% | ~105 |
| M24 | Faintness & Despair | 1,937 | 12% | ~97 |
| M25 | Life & Death | 1,646 | 21% | ~82 |
| M26 | Judgment & Condemnation | 1,604 | 13% | ~80 |

None of these are concentration-flagged — their size is genuinely spread across many distinct
words, not one dominant lemma. That makes them *good* clusters substantively, but the ~80–183
session range means a real multi-session consistency mechanism needs to exist before any of them
is a sensible submission.

### Concentration flags (≥55%) — worth a shape check before submission, most look natural, two don't

| code | short_name | verses | concentration | top strong | note |
|---|---|---|---|---|---|
| M67 | Sloth & Diligence | 14 | **86%** | G4710 | Tiny + almost entirely one word — this looks less like a "family of like phenomena" and more like a single-lemma leftover. Worth checking whether it should even be a standalone cluster. |
| M58 | Wickedness | 179 | **77%** | H7451I | **Shares its exact `short_name` ("Wickedness") with M10b** — a naming collision. Combined with high concentration and modest size, this looks like it may be an unresolved duplicate/split artefact of M10b, not a distinct cluster. Flagged as a genuine open question, not decided here. |
| M41 | Being Heard | 1,424 | 63% | H8085G ("hear") | Looks natural — the concept is definitionally built on the "hear" verb. |
| M80 | Blessing | 459 | 63% | H1288 ("bless") | Looks natural, same reasoning. |
| M81 | Memory (act) | 377 | 59% | H2142 ("remember") | Looks natural, same reasoning. |
| M49 | Thanksgiving | 193 | 58% | H3034 ("give thanks") | Looks natural, same reasoning. |

Four of the six read as ordinary verb-centred clusters where one core lemma naturally dominates —
not a defect. **M67 and M58 are the two worth actually asking about** before either is submitted.

### Tiny clusters (<100 verses, 10 total) — lowest-risk on size alone, completable in 1–5 sessions

M52 (96), M53 (85), M32 (82), M82 (75), M62 (72), M75 (50), M69 (49), M54 (45), M66 (26), M67 (14,
flagged above). These are the cheapest possible way to pilot the *process itself* — if the goal is
to test the mechanism (Step 1–4, the JSON handoff, the catalogue framework) with minimal size risk
before committing to a larger cluster, one of these (M32 — already the best-provenanced cluster in
the taxonomy, per #1525 — being the standout) is a lower-risk first move than a Medium cluster.

### Revisiting my own earlier M27 recommendation

My prior opinion (this session) called M27 "moderate... neither trivial nor unmanageably large."
Checked properly now: **M27 is 781 verses, ~39 sessions at my own illustrative rate** — near the
top of the Medium band, not small. That doesn't reverse the recommendation (it's nowhere near the
9 Very Large outliers, and its membership provenance is still the best of any substantial cluster),
but "moderate" undersold the actual commitment. **Two honest options, not decided here:** submit
M27 first and accept ~39 sessions as the real size of a first exemplar, or pilot the process on a
Tiny cluster (M32) first — cheaply proving the mechanism — before committing to M27's longer run.
