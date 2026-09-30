# Analysis-phase stream robustness assessment — 2026-08-28

> Requested by the researcher while thinking through the analysis-phase approach: three
> complementary entry points — **by book**, **by cluster** (strong-grouped), **by characteristic**
> (narrower band, cross-book/cross-cluster, assembled from the other two) — all resting on the same
> foundation: verse, in passage context, read through the lexicon. This assesses the current
> robustness of each stream, live against `iba.db` and `bible_research.db` (active tables only,
> per instruction) cross-checked against what's actually on disk under `_analytics/`.

## 0. The shared foundation — base verse→lexical layer

Checked first because all three streams depend on it. Per-book coverage in `iba.db`:

- **All 66 canonical books: verse and `verse_lexical` (L4b, the mechanical role/sense reading)
  coverage is ~100%** (a handful of books sit at 99.0–99.8%, single-digit verse gaps each — not a
  systemic hole). This holds regardless of book, cluster, or registry status.
- This is a genuinely different (much stronger) fact than "registry through lexical is complete,"
  which was the framing checked earlier this session — that framing is scoped to registry-linked
  strongs specifically; the underlying verse/lexical data itself, keyed by verse rather than by
  strong-registry, is essentially whole-Bible complete already.

**Conclusion: the base layer is not the risk for any of the three streams.** The robustness
question for each stream is entirely about what's been built *on top of* this foundation.

## 1. By-book stream

Two very different things both live under "by book," and they're at very different stages.

**(a) Base lexical reading (§0 above) — ~100% for every book.** If "by book" means "can I read
any book's verses through the lexicon," the answer is yes, uniformly, already.

**(b) The debate/phenomenon pipeline (`iba.passage`/`phenomenon`/`debate_change_detail` —
escalation #737's own subject)** — this is the actual interpretive analysis layer, and it tells a
much narrower story:

| book | passages | span_meaning written | debated | phenomena_complete |
|---|---|---|---|---|
| Hos | 14 | 14 | 14 | 0 |
| Dan | 13 | 10 | 12 | 2 |
| Mic | 7 | 7 | 7 | 0 |
| Jonah | 4 | 4 | 4 | 0 |
| Joel | 3 | 3 | 3 | 0 |
| Obad | 1 | 1 | 1 | 0 |
| **all other 60 books** | **0** | **0** | **0** | **0** |

- **Only 6 of 66 books (9%) have any debate-pipeline record at all.** Matches the book-by-book
  debate phase memory (Dan/Jonah/Joel/Obad/Mic/Hos done; Amos never started in this pipeline).
- Even within those 6 books, **41 of 42 passages sit at `debate_status='filled'`, not
  `'complete'`** — only 2 (both in Dan) have reached `phenomena_complete_at`. "Touched" is the
  right word; "revision" undersells how early-stage most of it still is even where started.
- Revision-signal tables are thin so far: `passage_insufficiency` = 1 row, `passage_emergent_
  question` = 4, `passage_validation_note` = 4 — not yet a rich record of what needs fixing,
  likely because so little has reached a stage where that kind of review would surface it.

**File-side (`_analytics/Bible_Books/`), for context:** file counts per book track two different
eras layered on top of each other — pre-reset July work (phase1-views, oracle-synthesis readings —
e.g. Amos has 22 files from 2026-07-04 despite zero rows in the live debate pipeline) and the
current debate-pipeline output for the 6 done books, plus one placeholder-only file for most other
books (a single whole-book `verse-lexical` batch extract, not book-by-book debate work). **Ps
(1,054 files) and Prov (921 files) are dramatically ahead of everything else** — both are the
source books behind the characteristic index (§3).

**Robustness read:** the *base* is solid everywhere; the *debate-analysis* layer is real but
covers 9% of books and is itself mostly mid-stream, not finished, within that 9%.

## 2. By-cluster stream

From `bible_research.db` (`cluster`/`cluster_finding`/`cluster_observation`/`finding`), cross-
checked against `_analytics/clusters/` file depth — the two agree closely.

**Cluster status distribution (49 clusters: 47 M-codes + FLAG + T2):**

| status | count | clusters |
|---|---|---|
| Analysis Completed / (Terms Added) | 14 | M01, M02, M03, M04, M06, M07, M08, M09, M10, M15, M20, M26, M39, M46 |
| Ready for re-analysis | 1 | M05 |
| Structurally Ready | 2 | M11, M38 |
| Merged into M10 | 2 | M10b, M10c (folded 2026-06-23) |
| **Not started** | **30** | everything else, incl. FLAG and T2 |

File counts corroborate this almost exactly: the 14 "Analysis Completed" clusters plus M11/M38/M05
carry 47–353 files each; every "Not started" cluster sits at 2–10 files (scaffold only). One
housekeeping note: `_analytics/clusters/M32` (27 files) has **no corresponding row in the live
`cluster` table at all** — worth a look before treating it as real cluster content.

**A finding that changes the robustness picture, not visible from status alone:** even "Not
started" clusters carry substantial **live (non-deleted) verse-level findings already** —
e.g. M23 Strength (Not started): 1,589 live findings; M47 Constitution (Not started): 1,620;
M25 Life (Not started): 1,337. The underlying verse-finding evidence is broadly present across
almost every cluster; what "Not started" actually means is that the cluster-level catalogue-
prompted synthesis pass hasn't run — not that the evidence itself is missing.

**The bigger caution, project-wide:** the `finding` table's own `cfg_table` description states
roughly 92% of its ~438k rows carry `delete_flagged=1`. That attrition shows directly in the
per-cluster numbers — e.g. M01 Fear: 27,336 all-time findings, only 1,066 (3.9%) still live;
M15 Wisdom: 45,802 all-time, 1,735 (3.8%) live. **Whatever "done" clusters actually stand on today
is the small live residual, not the historical volume** — that residual is what a robustness
review should be checked against, not the bigger all-findings number.

**Robustness read:** the 14 "Analysis Completed" clusters are genuinely the most-worked stream of
the three, but "completed" rests on a live-findings base that's typically 4-10% of everything ever
generated for that cluster — worth confirming that residual is sufficient before leaning on the
"Completed" label. The 30 "Not started" clusters are not evidence-empty — they have real live
verse findings sitting unused, which changes what "starting" a cluster would actually take
(synthesis over existing evidence, not fresh evidence-gathering from zero).

## 3. By-characteristic stream

This is the least-developed of the three, more so than either "large part... done" framing would
suggest.

**Live table (`ib_characteristic`, 1,634 rows, rebuilt 2026-07-11 on a meaning-key):**
- **100% of rows carry `status='surfaced'`** — no row has progressed past initial surfacing to any
  later stage (no "reviewed," "synthesized," or similar exists as a status yet).
- **100% of rows have `gist`, `colour_range`, `junctions`, `open_questions`, and `discovery_doc`
  all NULL** — every field intended to hold the actual cross-book synthesis (the characteristic's
  own definition, its relational junctions, open questions) is unpopulated. What exists is a raw
  meaning-keyed index (one row per lemma+reading+book instance), not yet an assembled
  characteristic.
- **Only 2 distinct books are represented: `book_scope=19` (Psalms, 877 rows) and `book_scope=20`
  (Proverbs, 757 rows)** — the entire table is Ps/Prov only, generated in a single batch
  (2026-07-11/14) directly off those two books' unusually deep book-level work (§1). It has never
  been extended to any other book.
- `cluster`/`cluster_all` are populated for only 625–686 of the 1,634 rows (38–42%) — even the
  cluster-linkage half of "between strong and cluster" is partial within the two books it does
  cover.

**File-side (`_analytics/characteristics/`, 20 files):** all dated 2026-07-02/03/07 — pre-dates
the `ib_characteristic` rebuild entirely. Early exploratory discovery docs for ~9 named
characteristics (being-known, desire/appetite, fear-of-the-Lord, formation-by-relation, love-aheb,
self-mastery, speech-outflow, the-felt-interior, the-heart, trust-refuge), one deep single-word
case study (ruthlessness, 7 files), a coverage audit, a method-guardrail note, and a full dump of
the now-legacy 277-row `characteristic` table. None of this reflects `ib_characteristic`'s own
output — that lives only in the DB, has no exported file record at all.

**Robustness read:** "by characteristic" as the researcher describes it (cross-book, cross-cluster,
narrower band) **does not exist yet as working output** — what exists is a single-batch, two-book,
unsynthesized meaning-key index. It is real, well-formed raw material (1,634 correctly meaning-
keyed entries), but every field that would make it function as a *characteristic* rather than an
*index entry* is empty, and it has never left Psalms/Proverbs.

## Summary across the three streams

| stream | base foundation | analysis-layer coverage | what "done" rests on |
|---|---|---|---|
| By book | ~100% all 66 books | 6/66 books (9%) touched by debate pipeline; 2/42 passages fully complete even there | thin, early-stage, but real where it exists |
| By cluster | ~100% (verse findings exist broadly, even in "Not started" clusters) | 14/49 "Analysis Completed"; 30/49 "Not started" (but not evidence-empty) | live-findings residual, typically 4–10% of all-time volume per cluster |
| By characteristic | ~100% (same foundation) | 1,634-row raw index, 2 books only (Ps/Prov), 0% synthesized | essentially a pilot, not yet a working stream |

The common dependency (§0) is solid everywhere. The three streams are at genuinely different
maturities — book-debate and cluster-analysis are both real but partial and largely unfinished
even within their own scope; characteristic is the least mature, a single-batch pilot on two books
with none of its synthesis fields populated yet.

## 4. Addendum — the "70% of OT books touched" claim, checked against method eras

Raised by the researcher directly: "I know there is much more bits and pieces done, but poorly
captured. 70% of the Old Testament books have gone through at least 1 analysis phase." Checked
against file-date evidence, `_analytics/Bible_Books/`:

**By folder-presence alone, 24/39 OT books (62%) carry a real analysis-phase subfolder**
(`phase1-views`/`readings`/`_synthesis`/etc., not just the single placeholder file) — in the same
ballpark as "70%," and the researcher's own qualifier ("poorly captured") already anticipates that
a file-folder proxy will undercount work sitting elsewhere.

**The more important finding: within that 62–70%, the file dates cluster into distinct, largely
incompatible method eras — this changes what "harvest and validate" actually means per book:**

- **Era A (~2026-06-27 to 07-05):** the pre-reset "characteristics" framing (`phase1-views`,
  `readings`/oracle-synthesis, `_seg` segmentation) — present in essentially every one of the 24
  books. Doubly superseded: the characteristics framing itself was closed 2026-06-25 (before most
  of these files' own dates — meaning some of this was produced *after* its own framing was
  already retired), and the whole study method was later closed 2026-08-03.
- **Era B (~2026-07-26 to 08-03), concentrated in Dan/Amos/Hos:** early debate-pipeline output
  (`whole-book-read`, `verse-span-meaning`, `debate` archives) — built on the pre-failure version
  of the method. Memory `project_iba_verse_reading_v3_judged_failed_consistency_unresolved`:
  this v3 reading was tested on Jonah 3 and judged FAILED — the proximate trigger for the
  2026-08-03 closure. Salvage value here is not just a capture-quality question; it needs
  re-examination against the specific failure mode found, book by book.
- **Era C (2026-08-05 onward, current v4/IBA method, post-reopening):** matches the live
  `iba.db` schema vocabulary exactly (HIB, operation, phenomenon, reconciliation). **Checked
  across all 24 books — this era is essentially Dan-only.** Every other book's only post-08-05
  file is the single uniform 2026-08-09 `verse-lexical` batch export — which is base-layer
  re-derivation (§0), not analysis; it is not additional analysis work.
- **Dan specifically is the one real exception, and a concrete data point for the harvest
  question:** its `_analytics/Bible_Books/Dan/` tree carries dozens of current-method files
  (chapter-by-chapter `verse-lexical`, `debate-report`, `hib-set-by-type` and
  `hib-set-reconciliation` through v5, `operation-set-reconciliation`, `phenomenon-set-
  reconciliation`, `closing-set-reconciliation`) spanning chapters 1–4 and 8, iterated
  2026-08-05 through 08-08. **This is substantially more than the 13 `passage` rows / 2
  `phenomena_complete` the live DB shows for Dan (§1)** — meaning even Dan's own current-method
  work has a real file→DB harvest gap, distinct from (and cheaper to close than) the
  method-validity question Era A/B carry.

**What this means for the researcher's two questions:**

- **(a) Harvesting is not one task, it's at least three, with different risk profiles per era:**
  Era C (Dan only) is a straightforward reconciliation/promotion job — the work is trustworthy,
  it just needs syncing into `passage`/`phenomenon`. Era A/B (everything else touched) requires
  deciding, before any harvest effort, whether pre-failure/pre-reset content can be salvaged at
  all against the current method's bar — that's a validity question, not a filing question.
- **(b) The redo-vs-harvest cost calculus is not uniform across the 62–70%** — it's likely closest
  to "harvest" for Dan specifically, and closest to "the old material is raw ore at best, mine
  observations from it but don't trust its conclusions" for the Era A/B majority. A single
  project-wide answer probably isn't the right shape for this decision.

Not decided here — this is the researcher's own call, laid out as an option to consider rather
than a recommendation: a **bounded pilot on Dan** (the one book with a real Era-C file/DB gap)
would produce actual cost-per-unit data for "harvest and validate" before committing to either
path at scale for the other 23 books.
