# Proverbs re-read — retrospective & learnings

- **Date:** 2026-07-14
- **Scope reviewed:** the 59 cycle logs, the two book-close docs, this session's transcript (cycles 39–59 + book-close), and DB/engine table results.
- **Purpose:** tease out (a) areas for improvement, (b) duplicate work, (c) rework & how to avoid it, (d) what worked well, (e) processing cost — and turn them into concrete action items.

## Headline numbers (measured)
| metric | value |
|---|--:|
| cycles (this + prior windows) | 59 + 1 orphan + book-close |
| read-2026 characteristics (book 20) | **1,969** |
| read-2026 active `ve_lexical` rows | **21,659** |
| emergent / orphan discoveries (old model missed) | **230** spans |
| reading JSON files produced | **713** (4.8 MB) |
| cycle log files | **59** |
| commits this window (cycles 39–59 + close) | **22** |
| DB snapshots created over the read | **~60** (16 retained ≈ **12.8 GB**) |
| single DB snapshot size | **0.80 GB** |
| DB size now / at programme baseline | **799 MB** / 165 MB |
| `ve_lexical` soft-deleted (programme-wide) | **174,023** |
| verses read / total | **823 / 915** (+ 92 assessed skips) |

---

## (d) What worked well — keep doing

1. **The standing per-cycle loop was disciplined and reproducible.** snapshot → pull → build → apply-each-passage-in-isolation → 7-gate conformance → ib_char rebuild → log → commit → push. **All 59 cycles came back conformance-clean.** The isolation (no parallelism) held quality high, as intended.
2. **Verse-first, char-by-char, distinct-facet reading.** Recurring proverbs (quarrelsome wife 21:9/25:24, prudent-vs-simple 22:3/27:12, the sluggard's six facets) were read for *what each verse does*, never flattened — the "difference between repeated spans is the finding" rule paid off.
3. **Screen 0 (God-is-arena) held consistently.** `external:god` clustered exactly at the theological hinges (24:12 weighs the heart; 22:23/23:11 pleads the poor's cause; 25:22 rewards enemy-kindness; 28:9 loathes the disobedient's prayer; 28:13 mercy on the penitent).
4. **Emergent/orphan discovery was tracked, not silent.** 230 spans the old model missed were stamped (`emergent-read-2026` / `orphan-reread-2026`) — an auditable record of what the reread added.
5. **Deliberate, logged skips.** Strict verse-bounded reading (no imputing) — every skip documented in the cycle log and later verified at book-close (the 13 passage-skips + 92 verse-skips all reconciled).
6. **The 7-gate conformance check caught issues at the point of writing**, keeping quality uniform across 59 cycles rather than deferring to a big end-audit.
7. **Reusable, span-id-based engine scripts.** `_apply_reread_lexical`, the ib_char rebuild, and the measures runner are parameter-driven. Critically, **being span-id-based let the orphan gap be closed by verse without restructuring passages.**
8. **Read-2026 pairs are span-id encoded (819/819).** The reread met its own structural requirement (the baseline's central defect was that *all* old pairs were Strong's-encoded) — unblocking G5/G9.
9. **Incremental commit + push per cycle + per-cycle DB snapshot** gave excellent recoverability.
10. **The book-close audit itself worked** — it is what caught the coverage gap and produced a real baseline→delta (G1/G2/G10 → 0, G6 438→9).

---

## (a) Areas for improvement

### A1 — ★ The verse-coverage blind spot (the biggest learning)
The read was **passage-driven**, but **116 of 915 verses had `passage_id = NULL`** and were structurally invisible to the loop. This went **undetected until the book-close audit** — 13% of verses (24 with real IB content, incl. Agur's contentment prayer 30:7-8 and faintheartedness 24:10) were never pulled. "Complete" was declared at the *passage* level while the *verse* level was 87%.
- **Root cause:** completeness was measured as passages-read, and the per-cycle conformance was passage-range-scoped — neither could see verses outside the passage structure.
- **Fix:** a **verse-coverage pre-flight** (every verse ∈ a passage or an explicit skip-list; block the read until totals reconcile) at book-start, and a cheap **book-wide verse-coverage assertion each cycle**. Redefine "book complete" as **verse-level**, not passage-level.

### A2 — Legacy leftover chars were not auto-resolved
The apply engine writes read-2026 roles on emitted spans but does **not** demote the *other* old-model char spans on a read verse. This left **123 leftover chars** (e.g. 22:4's reward-trio) that had to be demoted in a manual book-close pass. → apply should **auto-demote (or loudly flag) non-selected old chars on read verses**, so the read layer is authoritative in one pass.

### A3 — Conformance SQL was re-authored inline every cycle
The 7-gate check was hand-written each cycle (copy-paste). This is exactly where a prior-session bug lived (`span_id` vs `verse_span_id`). → wrap it in **one reusable, parameterized script** (verse-span-id list *or* passage range).

### A4 — The measures runner conflates legacy + read layers
`_check_reread_measures_v3` reports on the whole span-index (segment model), so "final" numbers were confusing (150 non-conformant chars that were **all legacy**) until legacy was demoted. → add a `--layer read-2026` scope, or define book-close as **demote-then-measure**.

### A5 — Out-of-order passage IDs made "resume at next id" fragile
Passage ids do not track verse order (22:5 and 22:6 sit far apart), so "resume at max id + 1" occasionally confused the sequence and contributed to the orphan blind spot. → track a **canonical verse-progress marker**, not a passage-id high-water mark.

### A6 — Book-general tooling gaps
The family-grouping script was **hardcoded to book 19**; it needed parameterizing (`--book`) mid-close. → audit all reread tooling for book-generality up front.

### A7 — Early-cycle quality wasn't back-checked
6 empty-`107`(target)-value rows survived from cycles 1–3 (Pro 1:29–2:3, prior-session output). Per-cycle gates didn't catch empty *values* (only missing *rows*). → a book-wide **content-completeness (G7) sweep** before declaring done.

### A8 — Operational friction
CRLF↔LF warning on every commit; a **silent push no-op** once (upstream tracking lost in a prior history-rewrite). → add **`.gitattributes`** for line-endings; **verify upstream** after any history rewrite.

---

## (b) Duplicate work

1. **ib_char full rebuild ran ~60× (once per cycle).** The rebuild is O(book) — it re-links **all** ~1,900 spans every time. 59 full rebuilds where an incremental link + a cheap I7 check would do. **Biggest avoidable compute.**
2. **Conformance SQL re-authored every cycle** (see A3) — the same ~40 lines typed 60 times.
3. **The orphan re-read (24 verses) at book-close** duplicated the main sweep's purpose — a second reading pass that a complete passage structure (A1) would have folded into one.
4. **3× rebuild+regroup at book-close** (after each of the demotion batches) — the demotions could have been batched, then rebuilt once.
5. **Not duplication (by design):** re-reading recurring proverbs for their distinct facet is the *method*, not waste — flag so it is never "optimised away."

---

## (c) Rework & how to avoid it

| rework done | cost | avoid by |
|---|---|---|
| 24 orphan verses re-read at close | +1 cycle | verse-coverage pre-flight (A1) |
| 123 legacy chars demoted at close | manual pass | apply auto-demote (A2) |
| family-grouping parameterized mid-close | small | book-general tooling up front (A6) |
| 3× rebuild/regroup after demotions | compute | batch demotions, rebuild once (b4) |
| prior-session `span_id`→`verse_span_id` fix | a bug | reusable conformance script (A3) |
| the "100%" claim corrected to 87%→verse-complete | credibility | verse-level completeness definition (A1) |

---

## (e) Processing cost

**Disk (dominant, and reducible):**
- **~60 full DB snapshots** created over the read, **0.80 GB each** ≈ **~48 GB of write churn** (pruned to 16 files ≈ 12.8 GB retained). The per-cycle `cp` snapshot is the single largest cost driver. Per existing guidance (*prune-or-skip pre-op snapshots*), this is over-cautious given git commits + the apply's own safety.
- **174k soft-deleted `ve_lexical` rows** accumulated programme-wide (the reread superseded old rows via soft-delete). The DB is now **799 MB** (from 165 MB). A periodic **hard-purge of ancient soft-deletes** would reclaim space.

**Compute:**
- **59 full ib_char rebuilds** (O(book) each) + **60 conformance passes** + **713 apply calls**. The repeated full rebuild is the compute hotspot.

**Tokens (the real cost — proxies, no exact telemetry):**
- Drivers, in order: (1) **per-cycle input pulls** — 12 passages with *full* span dumps including every function word; (2) **rich 11-dim lexical prose × ~1,900 chars**; (3) **repeated conformance/rebuild boilerplate** re-emitted each cycle. One context-window summarization occurred (long session).
- **Reduce by:** pulling **only candidate/char + role spans** (not every function word) in the input; a reusable conformance script (fewer re-emitted tokens); and batching the rebuild.

**Git:** 79 commits in the day's window, 713 small JSONs + 59 logs tracked — manageable.

---

## Recommended action items (root-fix, in priority order)
1. **Verse-coverage gate** in `_check_book_lexical_readiness` — assert every verse ∈ passage/skip-list; block read until reconciled. Redefine "complete" as verse-level. *(prevents the A1 gap on the next book)*
2. **Reusable 7-gate conformance script** (span-id list or passage range) — retire inline SQL. *(A3)*
3. **apply auto-demote / flag** non-selected old chars on read verses. *(A2)*
4. **Batch the ib_char rebuild** — cheap I7 check per cycle, full rebuild at book-close + periodic. *(b1 — biggest compute win)*
5. **Snapshot cadence every N cycles** (or git-only) instead of every cycle. *(e — biggest disk win)*
6. **`--layer read-2026`** scope on the measures runner; define book-close as demote-then-measure. *(A4)*
7. **`.gitattributes`** for line-endings; verify upstream after history rewrites. *(A8)*
8. **Periodic hard-purge** of ancient soft-deleted `ve_lexical`. *(e)*
9. Leaner input pulls (candidate/char/role spans only). *(e — token win)*

*These should be baked into the authoritative reread instruction + the book-readiness runner, not left in memory only (per GR guidance that researcher learnings go into the dated instruction docs).*
