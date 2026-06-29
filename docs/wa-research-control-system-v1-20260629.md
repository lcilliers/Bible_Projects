# Research control system — taming the verse-fanout method

- **File:** docs/wa-research-control-system-v1-20260629.md · 2026-06-29 · living doc (decision log at the end).
- **Trigger (researcher):** the method is rewarding but *"very complex, a large number of threads in the air, hard to keep track, easy to lose focus; observations/findings all over the place and growing exponentially… immense risk of being lost/hidden/out of place; misconceptions may persist because not revisited."* Plus a stated personal constraint: *limited ability to re-read, forgets, cannot hover on many planes at once.*

## 1. The reassurance first
**Nothing is lost.** Every observation lives in **one** table, `ib_observation`, each with a `status` (resolved / needs-corroboration / open / silent) and a `reconsider_at` (the forward thread — where it must be revisited). The DB *is* the external memory. The discovery is sound; the data is not actually scattered — it is all in one place, queryable.

## 2. The real diagnosis (two faults, both fixable)
1. **No single current view.** There has been no one page that shows *the whole live state* — what is open, what to do next, what is at risk of being forgotten. So the only way to "know where we are" was to re-read many files — exactly what the researcher cannot do.
2. **Double-entry sprawl.** Observations were written to the DB *and* hand-copied into parallel `.md` files (the per-verse worklist, the observation extracts, the track observation tables). Two copies that **drift** and **multiply** — this is the "exponential, all over the place" feeling. The DB copy is canonical; the hand-copies are the problem.

## 3. The fix (a REDUCTION, not another layer)
**One place to write. One place to read.**

### (a) One place to read — the generated STATE page ✅ built
`scripts/_assess_study_state.py` → **`verse-analysis/_STATE.md`**. Generated from the DB, always current, never hand-edited. **Read this instead of re-reading the sprawl.** It carries:
- **Headline** — total/open/stale counts in three lines.
- **▶ FAN-OUT PLAN** — *the killer view*: every candidate next-verse ranked by **how many open threads it would close**. Turns "many threads in the air" into a single ordered to-do list. (Today it says: read **Eze 34:4** → closes 5 threads; then **Mark 7:21** → closes 3 incl. our current #42.)
- **OPEN THREADS by track** — every unresolved observation, its claim, where to go, and its **age** (so nothing rots unseen).
- **STALE** — open threads older than 7 days = the *"misconception persists because not revisited"* risk, surfaced automatically.
- **BY TRACK rollup · VERSE PROGRESS · RECENTLY RESOLVED** (spot-check for wrong closures).

This directly answers the three constraints: *can't re-read* → one page; *forgets* → the page is the memory, `reconsider_at` threads never lost; *can't hover on many planes* → the FAN-OUT PLAN collapses every plane into one ranked list.

### (b) One place to write — make the derived docs GENERATED
Stop hand-maintaining the worklist / observation-extract / track observation tables. They become **read-only renders** of `ib_observation` (a `--verse` / `--track` flag on a generator), produced on demand. Then:
- there is exactly **one** thing to edit (the DB), so nothing drifts;
- the `.md` files stop multiplying — they are regenerated, not accumulated;
- what stays **hand-authored** is only genuine authorship: the **synthesis / reading prose** in a track doc (and that, ideally, also becomes a DB `finding` so it too is captured, not loose).

## 4. Why this is self-limiting (the "exponential growth" fear)
Open threads **grow** when a new verse is read but **contract** when convergence resolves them (a resolved thread stops driving fan-out — the method's built-in brake). The STATE page makes that contraction *visible and steerable*: you can choose the verse that closes the most threads, so the open-list trends **down**, not up. The fear is real only if we never look at the whole; the page is the whole.

## 5. The discipline going forward (small, fixed)
1. **Write only to the DB** (`ib_observation`). Never hand-edit a derived `.md`.
2. **Read `_STATE.md`** at the start of every session and after each capture (`python scripts/_assess_study_state.py`). It is the orientation.
3. **Work top-down the FAN-OUT PLAN** — pick the verse that closes the most, prepare it (`_assess_verse_raw_data.py`), read it, capture, re-generate. Watch the open count fall.
4. **Clear STALE** periodically — the oldest open threads first, before they become entrenched misconceptions.

## 6. Decisions for you
- **D1 — Adopt `_STATE.md` as the single read-surface?** (built; re-run to refresh.)
- **D2 — Convert the hand-maintained derived docs to generated renders?** Stops the drift + multiplication. (The track *synthesis* prose stays authored.)
- **D3 — Keep the 7-day STALE flag, or a different cadence?**

## Decision log
- 2026-06-29 — proposal raised; `_STATE.md` generator built as a working first cut for reaction. Awaiting D1–D3.
