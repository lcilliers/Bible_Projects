# Re-read automation — control-table worklist design

**Date:** 2026-07-09 · **Status:** proposed, infrastructure built, awaiting run-mode confirmation
**Scope:** Psalms re-read now; book-general (reusable for the whole study).

---

## 1. The problem

The per-chapter re-read is producing good work, but the operating rhythm requires the
researcher to press **"proc" between every chapter** — ~130 more times for Psalms alone,
and likely **thousands** across the whole study. That is unsustainable babysitting.

A previous attempt to relieve it ("batches of 5") failed the *wrong* way: with no
per-chapter structure, the reading collapsed into a single shallow pass over multiple
chapters — a quality **nono**. The requirement is therefore precise:

> **Automate the *trigger*, never the *reading*. Each chapter must still be read in
> isolation, one at a time, at full depth.**

## 2. What can and cannot be automated

| Element | Automatable? | Why |
|---|---|---|
| The **reading** (dimensions, discovery notes, pair resolution, lemma distinctions) | **No** | Genuine exegesis; done by the analyst per chapter. A script cannot produce it. |
| The **data pull** (verses + characteristic spans for the chapter) | Yes | Mechanical query. |
| **Apply** (soft-delete priors, insert span-id ledger, set process_marker) | Yes | Existing `_apply_reread_lexical_v1`. |
| **Gate check** (G10 completeness, G6 discovery-per-verse) | Yes | Existing inline check. |
| **Commit + progress** | Yes | git + monitor script. |
| The **trigger** between chapters | **Yes ← this is the win** | Replace the human keystroke with a worklist-driven loop. |

## 3. Why a control table prevents the batch-reading failure

The batch failure had no per-chapter boundary, so chapters bled together. The worklist
makes each chapter a **discrete, individually-gated transaction**:

1. one **JSON file** per chapter (`_read/psalm-0NN-reread-v1.json`),
2. its own **gate verification** (G10_miss=0, G6_no_disc=0) written back to the row,
3. its own **commit** (SHA recorded on the row),
4. status transitions **pending → in_progress → done** (or **needs_review** if gates fail).

Isolation is now enforced by the *mechanism*, not by the researcher's keystroke. If a
chapter were ever read shallowly, its discovery notes would be thin and the scored
read-back audit (the 9-gate + 25-unit audit) would catch it; a gate failure parks the
chapter as `needs_review` for attention rather than silently passing.

## 4. The control table

`reread_worklist` (created 2026-07-09) — one row per (book, chapter, provenance):

```
status        pending | in_progress | done | needs_review
char_spans    expected characteristic spans (from span index)
read_spans    spans with an active reread ve_lexical row
g10_miss      completeness-ledger misses at close   (0 = clean)
g6_no_disc    candidate verses without a discovery  (0 = clean)
committed_sha the chapter's commit
read_at, note
```

It is a **convenience ledger**, not the authority: `--seed` recomputes status from the
DB (a chapter is `done` iff every `role=characteristic` span has a reread row). The
`ve_lexical` rows + `process_marker` remain the source of truth. Seeded state today:
**150 chapters, 21 done, 129 pending, next = Ps 20.**

Driver: `scripts/_reread_worklist_v1_20260709.py` — `--seed | --next --claim | --close | --status`.

## 5. The loop (one invocation, many chapters, each isolated)

```
repeat until worklist empty OR context checkpoint OR needs_review:
    ch, verses, chars  ← worklist --next --claim        # claim, emit data pull
    <ANALYST READS ch at full depth>  → write psalm-0NN-reread-v1.json
    _apply_reread_lexical --in=…                         # apply span-id ledger
    gate check → g10, g6                                 # verify
    if g10==0 and g6==0:  git commit ; worklist --close --sha …   # done
    else:                 fix, or worklist --close (→ needs_review)  # park
```

One **proc** now drives a *run* of chapters, not a single chapter. The reading is
unchanged — still one chapter, fully, with lemma distinctions carried across (nefesh
senses, the anger family, chesed, the seats) — only the between-chapter wait is gone.

## 6. Honest cost note

Automation removes the *babysitting*, not the *underlying work*. Each chapter still
costs a real slice of model effort/tokens; a single invocation can carry roughly
**8–15 chapters** before context should checkpoint (fewer when chapters are large, as
Ps 18 was). So in practice one **proc** ≈ 8–15 chapters committed, then a progress
report and a single **proc** to continue — cutting the keystrokes by ~an order of
magnitude, with any gate-failing chapter surfaced for review.

## 7. Decision required — run mode

| Option | Behaviour | Note |
|---|---|---|
| **A. Continuous (recommended)** | One **proc** runs the worklist until context checkpoints (~8–15 ch), commits each, reports, then waits for a single **proc** to continue. Interruptible anytime. | Cleanest; every stop is a complete, committed state. |
| **B. Fixed chunk** | A set count per proc (e.g. 10), then stop and report. | Predictable cadence. |
| **C. Status quo** | One chapter per proc. | Maximum control, maximum babysitting. |

`needs_review` chapters are always surfaced regardless of mode.

## 8. Later option (not now): parallel isolated readers

Subagents could each read one chapter in a *separate* context (even stronger isolation)
and fan out for wall-clock savings. The catch is **cross-chapter lemma continuity** —
a chapter read in isolation loses the running register of established distinctions,
which is part of the quality bar. Deferred until the sequential loop is proven and, if
pursued, mitigated by handing each reader a lemma-register digest.
