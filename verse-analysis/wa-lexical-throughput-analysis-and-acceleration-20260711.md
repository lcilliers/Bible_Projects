# Lexical-creation throughput — is it really a year? Grounded re-estimate + acceleration levers

**2026-07-11.** Prompted by the observation: "Psalms took ~3 full days; ×66 books ≈ a year of full-time work." This checks that against the actual DB span-counts and separates the real cost from three extrapolation errors.

## The headline: the "year" is a ~4–8× overcount

Work does **not** scale by *book*. It scales by *candidate span* (the unit actually read). Psalms is the single worst book to extrapolate from.

| measure | value |
|---|--:|
| Candidate/roled spans, whole OT | **35,238** across 39 books |
| — Psalms | **6,615** (18.8% of all spans, but only 9.6% of verses → **2× the average density**) |
| — Psalms status | **DONE** (97% under `read-2026`) |
| — Remaining OT | **28,623 spans across 38 books**, all at 0% char-arc read |
| NT (27 books) | spans **not yet extracted**; verses not even fully loaded — a **separate, upstream** pipeline |

Psalms is the inner-life book *par excellence* — soul/heart/fear/trust on nearly every verse. It is **2× the next-biggest book** (Isaiah 3,195) and **~15× the median** book. **20 of the 38 remaining OT books have under 500 spans each** — a fraction of a single Psalms batch.

## Three compounding errors in the "×66 = a year" estimate

1. **Extrapolated per-book from the biggest book.** The right unit is spans. By spans, the *entire remaining OT* is 28,623 — only ~4.3× the Psalms load, not 65×.
2. **Counted a one-time rework as steady-state.** ~1 of the 3 Psalms days was **re-reading Book I** (Ps 1–41, ~2,357 spans) because it predated the IB-screen. That was remediation, not first-pass. Every future book is read **first-time-right** and skips it.
3. **Counted sequential single-threaded pace as the ceiling.** I read one batch per turn, hand-writing each builder. That is the slowest possible configuration.

## Grounded re-estimate (by spans, the real unit)

- **Psalms first pass** (excluding the Book I remediation): ~4,260 spans in ~2 days → **~2,000–2,200 spans/day** at my sequential pace, *and this rate came down over the run as the scaffolding matured.*
- **Remaining OT (28,623 spans):** at that rate, **~13–15 working days sequential.** Even conservatively (unfamiliar books, ~1,500/day), **~3 weeks.** Not a year.
- **NT:** genuinely more per-verse (span-extraction from scratch, not a re-read) → **scope separately**, do not fold into the OT rate.

So the OT lexical read is **weeks, not a year** — *before* any parallelism.

## The big lever: this work is embarrassingly parallel

Every psalm / chapter / book is independent. The Psalms bottleneck was **me, reading sequentially** — not the method. The mechanical scaffolding is now a finished, reusable asset (the `Reading` ledger lib, the finish→close→verify pipeline, the 100%-coverage gate, the auto-standalone fallback, the integrity sweep). A multi-agent workflow can fan out:

> **read** (N agents, one passage/chapter each, char-arc + Screen 0) → **build JSON** → **verify** (coverage + G10 + IB-screen + G9b — all already scripted) → researcher reviews *samples*, not every span.

At a 10–16-agent concurrency cap this compresses the **reading** wall-clock ~8–12×. The 28,623 remaining OT spans become **a few days of wall-clock**, not weeks.

### But be honest about what parallelism does and doesn't buy

- **The gates verify structure/completeness/integrity — not correctness.** Fidelity, eisegesis, movement-quality, and valid-`none`-vs-missed-pair can only be caught by the **scored read-back audit + researcher review** (per memory `project_reread_success_gates_and_scored_audit`). Parallelism raises *throughput* but shifts the binding constraint to **review bandwidth** — and le Roux is the sole authority on methodology. If every char must be personally validated, *that* is the real rate limit, and it is a review problem, not a reading problem.
- **Fan-out risks templated, shallow reading** — the exact thing the method forbids (`feedback_each_chapter_first_principles_find_the_gems`). The Psalms quality came from reading each psalm on its own terms. Mitigations: a strong per-agent prompt (Screen 0 + operation-focus + resist-grouping baked in), an **adversarial verify stage** (a second agent tries to refute each char's operation-read), and a **sampled human audit** per book before it's banked.

## What actually made Psalms slow (and won't recur)

| cost | recurs? |
|---|---|
| Building the ledger lib + pipeline + fallback | **No** — done, reusable |
| Book I remediation (a full second pass) | **No** — first-time-right now |
| Learning the per-genre ledger / Screen 0 discipline | **No** — baked into the method |
| Sequential one-batch-per-turn pace | **Only if we stay sequential** |
| The irreducible core: reading each span's operation | **Yes** — this is the actual work, and it is the value |

## Recommendation

1. **Stop extrapolating from Psalms.** Track progress in spans (35,238 OT total; 6,615 done). The remaining OT is ~4× Psalms, not 65×.
2. **Pilot a parallel workflow on ONE mid-size book** (e.g. Proverbs — next priority per memory, 2,899 spans; or a single prophet ~400–700 spans) to calibrate agent reading quality against the Psalms standard. Ship it through the same gates + a scored read-back audit. **Only scale to the OT if the quality holds.**
3. **Keep every book first-time-right** (IB-screen from the first pass) so nothing needs a Book-I-style remediation tax.
4. **Scope the NT separately** — it needs span-extraction (STEP pull + term curation) before any reading, a different and larger per-verse cost. Don't let its unknown fold into the OT estimate.

**Bottom line:** the OT lexical read is **~3 weeks sequential, or days with a parallel workflow** — the "year" figure triple-counts the biggest book, a one-time rework, and single-threaded pace. The genuine open question is not reading throughput but **QA/review bandwidth** and **holding reading quality under fan-out** — and both have concrete mitigations (gates + adversarial verify + sampled audit).

*Filed 2026-07-11. Read-only analysis over `verse_span_index` / `verse` / `books`. Figures are candidate/roled spans (`char_candidate=1 OR role IN ('characteristic','qualifier')`).*
