# Cluster Membership + Readiness Evaluation for Window 2 Input

- **filename:** 1525-cluster-membership-readiness-evaluation-v1-20260906.md
- **date:** 2026-09-06
- **escalation:** #1525 (spawned from #737)
- **status:** Corrected (2026-09-06, researcher instruction). The first pass below made two
  substantive errors, both retracted: (1) it called membership "sound" from a bare row-count check
  — non-empty is not sound; it never looked at the quality fields (`confidence`/`review_flag`/
  `alt_clusters`/`source`) already sitting in the schema, and §4 of that same pass listed the very
  checks needed to justify "sound" as *not attempted*, an internal contradiction. (2) it framed
  zero-Layer-2-coverage as a blocker needing a build — wrong: **Layer 2 is deliberately prepared
  on-demand, per cluster, at submission time, never in bulk** (researcher, this session — AI
  quality/consistency degrades on large repetitive passes), so 66-of-85 having no Layer 2 yet is
  not a finding at all, it's the process working as designed. §1 (Layer-2 strategy) and §2
  (membership quality, now with the actual quality-field data) are corrected below. §3–4 of the
  original pass stand.

---

## 0. Corrected framing: what "readiness" actually means

Readiness is not "does the cluster have content." Per the researcher, verbatim: *"readiness is
will the cluster work as the basis for analysis — is its shape, size, content, integrity, quality,
right."* Five axes, addressed separately below with what is now actually known vs still unknown:

| axis | what this pass can now say |
|---|---|
| **shape** | cluster verse-set sizes range 14–3,662 (median 565) — see §2c. Whether a given cluster's *definition* is internally coherent (not a grab-bag) is a semantic question, not answered by a count. |
| **size** | known (§2c) — some clusters (M67=14, M66=26) are tiny; whether that's correct (a genuinely narrow concept) or a residue of an unresolved split (like M10b/M10c/M27, §3.3 on the parent doc) is not distinguishable by size alone. |
| **content** | **not assessed here, and should not be bulk-assessed** — whether each individual strong genuinely belongs to its assigned cluster is a semantic judgement call, exactly the class of large-repetitive-judgement work the researcher's on-demand strategy is designed to avoid doing in bulk. This belongs per-cluster, at the time that cluster is chosen — same principle as Layer 2. |
| **integrity** | partially assessed — see §2b (`alt_clusters`/ambiguity, `review_flag`). No orphan/duplicate-row structural check run yet. |
| **quality** | assessed for the first time in this correction — see §2a (`confidence`/`source` mix). It is materially worse than "sound" implied. |

## 1. Layer 2 — retracted: this was never a "blocker," it's on-demand by design

The original pass reported "66 of 85 clusters have zero Layer-2 coverage" as if it were a gap
needing a corpus-wide build. **Retracted.** The researcher's actual strategy, stated directly:
Layer 2 is prepared **on-demand, per cluster, at the time that cluster is submitted for Window 2
analysis** — deliberately not a bulk pass, because AI quality and consistency degrade on large
repetitive tasks. Under that strategy, 66-of-85 having no Layer 2 yet is not a finding at all; it
is what "not yet chosen for analysis" looks like, for every cluster not yet chosen. There is
nothing to solve here and no sequencing recommendation to make on this basis. (The raw counts —
173 live `verse_lexical_note` rows, 19 clusters with 1–2 pilot verses each — remain accurate as
numbers; only the "this is a blocker" framing around them is withdrawn.)

## 2. Membership quality — corrected: "sound" retracted, actual quality-field data below

### 2a. Confidence and source — the real quality picture (`cluster_strong`, live M-cluster rows, n=3,717)

| `confidence` | rows | % |
|---|---|---|
| *(none recorded)* | 1,818 | 49% |
| heuristic | 1,262 | 34% |
| medium | 298 | 8% |
| high | 250 | 7% |
| low | 89 | 2% |

| `source` | rows | % | what it is |
|---|---|---|---|
| `old-system-migration` | 1,501 | 40% | carried over from the pre-IBA `bible_research.db` cluster table, never independently re-verified in IBA |
| `heuristic-family-grouping-v1-20260905` | 1,262 | 34% | **today's** mechanical keyword-regex rebuild (#236) — never manually verified |
| `llm-allocation-v1_3-20260811` | 633 | 17% | the Aug-11/12 LLM pass — the windows-debate register (W9/W10) and the #1006 review both document real failure modes in this pass (a noisy TF-IDF scorer, documented mis-fires like "brother"→Deceit) |
| `auto-precedent` | 311 | 8% | `clusterassign.py`'s gloss-matching tool — independently shown by #1006's own live M08 test to resolve correctly only ~13% of the time at fine-grained (sub-group) distinctions; its reliability at cluster-level assignment is not itself re-verified here |
| `manual-covenant-cluster-20260813` / `manual-backfill-triage-20260813` / `llm-reassignment-v1_1-20260811` | 10 | 0.3% | genuinely small, hand-touched |

**New finding from the per-cluster breakdown (Appendix B): 37 whole clusters — every one of
M48–M84, the codes created fresh by yesterday's family-reallocation rebuild — are 100% single-source.**
Every member strong in every one of these 37 clusters carries `source='heuristic-family-grouping-
v1-20260905'` and `confidence='heuristic'`; zero rows in any of them carry any other source,
any other confidence level, a `review_flag`, or an `alt_clusters` entry. This is not a spread of
mixed-quality membership — it is 37 clusters whose *entire* membership is one mechanical
keyword-regex pass, run once, yesterday, with no independent cross-check of any kind yet applied.
By contrast, **M32 (Covenant)** is the one cluster that is 100% `manual-covenant-cluster-20260813`
— the best-provenanced cluster in the taxonomy, small (9 strongs) but fully hand-touched.

**Nearly half of all M-cluster membership (49%) carries no confidence score at all, and 74%
(migration + today's heuristic) has never been checked by a human or a rigorous process.** "Sound"
was not a supportable word for this. The honest statement: membership is **structurally present
and traceable** (every row has a `source`), but **substantively unverified** at scale — consistent
with, not contradicting, the researcher's own on-demand strategy: content-correctness checking
belongs at the point a cluster is actually chosen, the same principle as Layer 2 (§0/§1), not as a
blanket audit attempted here.

### 2b. Integrity signals already in the schema (partial — flagged for use, not fully worked here)

- **634 of 3,717 rows (17%) carry a populated `alt_clusters`** — the assignment tool itself
  recorded another plausible cluster for these, i.e. self-flagged ambiguity.
- **89 rows (2.4%) carry `review_flag=1`** — explicitly marked for review and, as far as this pass
  can tell, not yet reviewed.
- Per the 7 codes named in #737 §3.3, confidence mix varies sharply and is worth reading before any
  is chosen: M27 (48 members) is 56% `medium`/`high`, no `review_flag`s — comparatively solid; M29
  (40 members) carries 4 `review_flag=1` rows and a `low`/`medium` mix; M32 (9 members) is entirely
  `NULL`/`medium`, no high-confidence rows at all, smallest of the 7.

### 2c. Size distribution (the "shape/size" axis, structural only)

Verse-set sizes across all 85 M-clusters: min 14 (M67), p10 85, median 565, p90 1,604, max 3,662.
Ten smallest: M67 (14), M66 (26), M54 (45), M69 (49), M75 (50), M62 (72), M82 (75), M32 (82), M53
(85), M52 (96). A small verse-set is not itself a defect — some inner-being concepts are genuinely
narrow — but it is exactly the kind of fact that should be checked against the cluster's own
definition (does "Sloth & Diligence," M67, genuinely have only 14 verses of content, or is it
another M10b/M10c/M27-shaped split artefact?) at the point that cluster is chosen, not assumed
either way here.

## 3. Escalation #1523 (772 no-word / 829 sibling-conflict exceptions) — re-examined in light of the new design

Not resolved here (it stays yours to close), but checked against the new full-verse-comprehensive
design (proposal §2 Step 5: "the full verse with all phenomena is analysed, not a subset"): your
own 2026-09-05 comment on #1523 predicted these exceptions "wash out naturally once those verses
get analysed at the verse level." That prediction is **structurally consistent** with the design
as now specified — because Window 2 reads a verse's full phenomenon set regardless of which
cluster nominally owns which term in it, a term flagged as a "sibling conflict" (shared with
another cluster) is never treated as an obstacle; it simply appears as one more phenomenon in the
same full-verse read. **Recommendation: leave #1523 parked as-is** — this evaluation doesn't
supply new handling for it; it confirms the handling you already expect will emerge on its own.

## 4. What this evaluation did not attempt (named, for a next increment)

- **Content correctness** — whether each individual strong genuinely belongs to its assigned
  cluster (a semantic read, not a count) — deliberately not bulk-attempted, per §0/§1's on-demand
  principle; belongs at the point a cluster is chosen.
- **Structural integrity beyond §2b** — no check yet for orphaned `cluster_strong` rows (pointing
  at a `strong` with no live `verse_lexical` row) or duplicate/conflicting rows for the same strong
  within one cluster.
- The M10b/M10c/M27 provenance spot-check (which process actually produced today's 43/20/48-member
  counts, against the 2026-08-13 review's proposed split) — a bounded, cheap check, not attempted
  here.
- Any check of M17/M29/M31/M32 specifically beyond the confidence-mix data now in §2b — no other
  open question exists for these 4 on record.

## 5. Recommendation for sequencing

**Corrected.** There is no corpus-wide blocker and no bulk task being recommended — that
recommendation is retracted along with the Layer-2-build framing (§1). The actual state: structural
facts (size, confidence/source mix, flagged/ambiguous counts) are now known and were cheap to
compute because they involve no repetitive judgement; **content-correctness and Layer-2 completion
both belong per-cluster, on-demand, at the moment a cluster is actually chosen** — consistent with
the researcher's stated strategy throughout. This evaluation's real contribution is the quality
data in §2, which should inform *which* cluster is chosen first (proposal §5 item 6) — e.g.
weighting toward a cluster with a cleaner confidence mix (like M27) over one that is majority
`NULL`-confidence migration data, if a cleaner first exemplar is wanted — not whether to run
anything in bulk beforehand.

---

## Appendix A — Every query run, exactly (researcher request, 2026-09-06: "what tests did you
perform... did you extract any membership data, what did you evaluate")

All against `iba.db`, read-only connection, every WHERE clause shown; nothing else was run.

1. **Coverage/presence, per M-cluster** —
   `cluster` JOIN `cluster_strong` (`deleted=0`) JOIN `verse_lexical` (`vl.strong=cs.strong`,
   `deleted=0`) LEFT JOIN `verse_lexical_note` (`vln.verse_id=vl.verse_id`, `deleted=0`), filtered
   `cluster_code LIKE 'M%' AND cluster.deleted=0`, grouped by `cluster_code`, counting
   `COUNT(DISTINCT cs.strong)`, `COUNT(DISTINCT vl.verse_id)`, `COUNT(DISTINCT vln.verse_id)`.
   → 85/85 non-empty; 66 zero-Layer-2; 19 with 1–2 covered verses.
2. **Corpus-wide tagging gap** — `COUNT(DISTINCT strong)` in live `verse_lexical` (15,451) minus
   `COUNT(DISTINCT strong)` in live `cluster_strong`, any code (7,327) → 8,124 by subtraction. A
   second, independently-written query using `NOT EXISTS` on the same two tables, run later in the
   background, returned **8,375** for what was intended as the same question. **Not reconciled** —
   the two queries are not provably asking the identical thing (the second's `NOT EXISTS` clause
   structure differs) and this was never resolved before the underlying figure was dropped from the
   report entirely (superseded by §1's correction). Flagged here rather than silently left out.
3. **How much of the gap is inside the curated pool** — of the untagged strongs, `COUNT(DISTINCT
   vl.strong)` where `vl.strong IN (SELECT strong_variant FROM candidate_seed WHERE deleted=0)` →
   21, against 1,806 distinct `strong_variant` values in live `candidate_seed`.
4. **Quality-field aggregates** — `cluster_strong` filtered `cluster_code LIKE 'M%' AND deleted=0`
   (n=3,717), grouped separately by `confidence`, by `source`, by `review_flag`, and a `SUM(CASE
   WHEN alt_clusters IS NOT NULL AND alt_clusters != '' THEN 1 ELSE 0 END)`. → the §2a/§2b figures.
5. **Size distribution** — same join as query 1, `COUNT(DISTINCT vl.verse_id)` per cluster, sorted;
   min/p10/median/p90/max computed over the 85 values in Python, not SQL. → §2c.
6. **Per-code confidence mix for the 7 named codes** — query 4's grouping re-run with `WHERE
   cluster_code = ?` for each of M10b/M10c/M17/M27/M29/M31/M32 individually.
7. **Full per-cluster raw breakdown (this revision)** — query 4's `CASE WHEN` aggregates computed
   per cluster instead of totalled, one row per M-cluster → Appendix B below, the actual extracted
   membership data, not a summary of it.

**Explicitly not run, at any point:** any query or read against a strong's own gloss/meaning text
compared to its cluster's definition; any read of the `rationale` free-text field (present on
every `cluster_strong` row — known from the 2026-08-13 m10bc review's own quoted examples, e.g.
`"precedent conflict: M10[P1]; M10b[P2] | accepted"`, but not pulled fresh here); any read of
`cluster.gloss`/`cluster.description` text for internal coherence; any read of actual verse text;
any check for duplicate or orphaned `cluster_strong` rows. Everything reported in this document is
**metadata about how an assignment was made and how many exist** — not a check that any individual
assignment is correct.

## Appendix B — Full per-M-cluster raw data (query 7), all 85 clusters

`strongs` = distinct live members. `no_conf`/`heuristic`/`medium`/`high`/`low` = `confidence`
value counts (sum to `strongs`). `flagged` = `review_flag=1` count. `ambiguous` = `alt_clusters`
populated count. `src_*` = `source` value counts (also sum to `strongs`).

| code | short_name | strongs | no_conf | heuristic | medium | high | low | flagged | ambiguous | src_migration | src_heuristic_rebuild | src_llm | src_precedent | src_manual |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M01 | Fear & Awe | 122 | 96 | 4 | 14 | 7 | 1 | 1 | 22 | 91 | 4 | 22 | 5 | 0 |
| M02 | Anger & Wrath | 89 | 55 | 1 | 11 | 16 | 6 | 6 | 33 | 52 | 1 | 33 | 3 | 0 |
| M03 | Grief & Lament | 155 | 106 | 11 | 14 | 16 | 8 | 8 | 38 | 88 | 11 | 38 | 18 | 0 |
| M04 | Joy & Gladness | 75 | 63 | 0 | 4 | 6 | 2 | 2 | 12 | 59 | 0 | 12 | 4 | 0 |
| M05 | Kindness & Friendship | 111 | 68 | 11 | 18 | 11 | 3 | 3 | 32 | 53 | 11 | 32 | 15 | 0 |
| M06 | Malice & Enmity | 129 | 55 | 35 | 9 | 21 | 9 | 9 | 39 | 45 | 35 | 39 | 10 | 0 |
| M07 | Shame & Confusion | 51 | 28 | 3 | 14 | 5 | 1 | 1 | 20 | 27 | 3 | 20 | 1 | 0 |
| M08 | Pride & Arrogance | 95 | 69 | 8 | 4 | 13 | 1 | 1 | 18 | 55 | 8 | 18 | 14 | 0 |
| M09 | Humility & Lowliness | 37 | 21 | 11 | 1 | 4 | 0 | 0 | 5 | 16 | 11 | 5 | 5 | 0 |
| M10 | Violence & Cruelty | 67 | 29 | 33 | 3 | 1 | 1 | 1 | 5 | 17 | 33 | 5 | 12 | 0 |
| M10b | Wickedness | 43 | 29 | 0 | 10 | 1 | 3 | 3 | 14 | 28 | 0 | 14 | 1 | 0 |
| M10c | Defilement | 20 | 10 | 0 | 7 | 0 | 3 | 3 | 10 | 9 | 0 | 10 | 1 | 0 |
| M11 | Turning & Repentance | 24 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 6 | 12 | 0 | 6 | 0 |
| M12 | Righteousness & Integrity | 81 | 24 | 39 | 9 | 9 | 0 | 0 | 18 | 23 | 39 | 18 | 1 | 0 |
| M13 | Faith & Faithfulness | 35 | 19 | 10 | 3 | 3 | 0 | 0 | 6 | 18 | 10 | 6 | 1 | 0 |
| M14 | Deceit & Falsehood | 100 | 64 | 8 | 7 | 12 | 9 | 9 | 28 | 49 | 8 | 28 | 15 | 0 |
| M15 | Knowing & Understanding | 115 | 74 | 9 | 17 | 14 | 1 | 1 | 32 | 67 | 9 | 32 | 7 | 0 |
| M16 | Wisdom & Folly | 68 | 22 | 37 | 4 | 4 | 1 | 1 | 9 | 22 | 37 | 9 | 0 | 0 |
| M17 | Counsel | 30 | 24 | 0 | 2 | 4 | 0 | 0 | 6 | 17 | 0 | 6 | 7 | 0 |
| M18 | Desire & Longing | 97 | 18 | 65 | 12 | 2 | 0 | 0 | 14 | 14 | 65 | 14 | 4 | 0 |
| M19 | Trust & Refuge | 36 | 24 | 3 | 4 | 5 | 0 | 0 | 9 | 20 | 3 | 9 | 4 | 0 |
| M20 | Doubt & Discouragement | 35 | 25 | 3 | 1 | 5 | 1 | 1 | 7 | 18 | 3 | 7 | 7 | 0 |
| M21 | Fasting & Piety | 56 | 44 | 0 | 7 | 4 | 1 | 1 | 12 | 35 | 0 | 12 | 9 | 0 |
| M22 | Praise & Song | 69 | 43 | 14 | 1 | 8 | 3 | 3 | 12 | 42 | 14 | 12 | 1 | 0 |
| M23 | Strength & Courage | 132 | 103 | 12 | 12 | 4 | 1 | 1 | 17 | 90 | 12 | 17 | 13 | 0 |
| M24 | Faintness & Despair | 167 | 90 | 45 | 19 | 6 | 7 | 7 | 32 | 69 | 45 | 32 | 21 | 0 |
| M25 | Life & Death | 32 | 27 | 2 | 0 | 3 | 0 | 0 | 3 | 20 | 2 | 3 | 7 | 0 |
| M26 | Judgment & Condemnation | 68 | 57 | 2 | 4 | 4 | 1 | 1 | 9 | 54 | 2 | 9 | 3 | 0 |
| M27 | Evil | 48 | 27 | 0 | 18 | 3 | 0 | 0 | 21 | 15 | 0 | 21 | 12 | 0 |
| M28 | Envy & Greed | 66 | 45 | 4 | 11 | 4 | 2 | 2 | 17 | 41 | 4 | 17 | 4 | 0 |
| M29 | Desire | 40 | 30 | 0 | 5 | 1 | 4 | 4 | 10 | 23 | 0 | 10 | 7 | 0 |
| M30 | Rebellion & Stubbornness | 55 | 20 | 24 | 2 | 6 | 3 | 3 | 11 | 20 | 24 | 11 | 0 | 0 |
| M31 | Faith | 18 | 14 | 0 | 3 | 0 | 1 | 1 | 4 | 13 | 0 | 4 | 1 | 0 |
| M32 | Covenant | 9 | 5 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| M33 | Rest & Peace | 67 | 53 | 4 | 4 | 4 | 2 | 2 | 11 | 45 | 4 | 10 | 7 | 0 |
| M34 | Patience & Perseverance | 43 | 31 | 5 | 3 | 3 | 1 | 1 | 7 | 24 | 5 | 7 | 7 | 0 |
| M35 | Being Tested | 26 | 18 | 5 | 3 | 0 | 0 | 0 | 3 | 17 | 5 | 3 | 1 | 0 |
| M36 | Worship & Service | 30 | 17 | 4 | 4 | 5 | 0 | 0 | 9 | 13 | 4 | 9 | 4 | 0 |
| M37 | Firstborn & Foreknowledge | 36 | 28 | 0 | 8 | 0 | 0 | 0 | 8 | 22 | 0 | 8 | 6 | 0 |
| M38 | Restoration & Revival | 56 | 27 | 17 | 2 | 4 | 6 | 6 | 12 | 7 | 17 | 12 | 20 | 0 |
| M39 | Gift & Favor | 32 | 28 | 2 | 1 | 1 | 0 | 0 | 2 | 16 | 2 | 2 | 12 | 0 |
| M41 | Being Heard | 23 | 13 | 7 | 3 | 0 | 0 | 0 | 3 | 13 | 7 | 3 | 0 | 0 |
| M42 | Prayer & Petition | 92 | 31 | 38 | 4 | 15 | 4 | 4 | 23 | 23 | 38 | 23 | 8 | 0 |
| M43 | Prophecy & Vision | 27 | 16 | 8 | 3 | 0 | 0 | 0 | 3 | 13 | 8 | 3 | 3 | 0 |
| M44 | Covenant & Fellowship | 46 | 32 | 8 | 5 | 1 | 0 | 0 | 6 | 21 | 8 | 6 | 11 | 0 |
| M45 | Renewal & Transformation | 30 | 22 | 0 | 0 | 7 | 1 | 1 | 8 | 14 | 0 | 8 | 8 | 0 |
| M46 | Wealth & Riches | 45 | 30 | 6 | 1 | 6 | 2 | 2 | 9 | 25 | 6 | 9 | 5 | 0 |
| M47 | Inner Seat | 50 | 32 | 13 | 3 | 2 | 0 | 0 | 5 | 32 | 13 | 5 | 0 | 0 |
| M48 | Astonishment & Wonder | 15 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 |
| M49 | Thanksgiving | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| M50 | Grace & Mercy | 31 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 31 | 0 | 0 | 0 |
| M51 | Love & Devotion | 22 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| M52 | Encouragement | 8 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| M53 | Dishonor & Disgrace | 22 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| M54 | Torah & Obedience | 6 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 |
| M55 | Destruction & Ruin | 45 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 0 | 45 | 0 | 0 | 0 |
| M56 | Sin & Guilt | 41 | 0 | 41 | 0 | 0 | 0 | 0 | 0 | 0 | 41 | 0 | 0 | 0 |
| M57 | Corruption & Perversion | 31 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 31 | 0 | 0 | 0 |
| M58 | Wickedness | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| M59 | Release & Reconciliation | 15 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 |
| M60 | Confession & Forgiveness | 9 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 |
| M61 | Purity & Holiness | 48 | 0 | 48 | 0 | 0 | 0 | 0 | 0 | 0 | 48 | 0 | 0 | 0 |
| M62 | Truth & Sincerity | 20 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 |
| M63 | Reasoning & Interpretation | 38 | 0 | 38 | 0 | 0 | 0 | 0 | 0 | 0 | 38 | 0 | 0 | 0 |
| M64 | Will & Resolve | 28 | 0 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 28 | 0 | 0 | 0 |
| M65 | Speech & Tongue | 22 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| M66 | Madness & Recklessness | 12 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 |
| M67 | Sloth & Diligence | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| M68 | Hope & Waiting | 20 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 |
| M69 | Self-Control & Zeal | 14 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 |
| M70 | Lifting & Bearing | 11 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 |
| M71 | Glory & Splendor | 22 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| M72 | Authority & Dominion | 46 | 0 | 46 | 0 | 0 | 0 | 0 | 0 | 0 | 46 | 0 | 0 | 0 |
| M73 | Sickness & Weakness | 46 | 0 | 46 | 0 | 0 | 0 | 0 | 0 | 0 | 46 | 0 | 0 | 0 |
| M74 | Keeping & Guarding | 17 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 0 | 0 | 0 |
| M75 | Disobedience & Lawlessness | 13 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 |
| M76 | Walk & Conduct | 8 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| M77 | Stumbling & Trial | 18 | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 |
| M78 | Slavery & Bondage | 22 | 0 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| M79 | Salvation & Ransom | 11 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 |
| M80 | Blessing | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 |
| M81 | Memory (act) | 14 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 |
| M82 | Reminder & Report | 12 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 |
| M83 | Seeking & Inquiring | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 |
| M84 | Outcry & Shouting | 23 | 0 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 23 | 0 | 0 | 0 |

*(M40 is not a live cluster code — not an omission; there is no M40 row in the live `cluster` table.)*
