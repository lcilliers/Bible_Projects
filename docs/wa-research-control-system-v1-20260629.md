# Research control system — taming the verse-fanout method

- **File:** docs/wa-research-control-system-v1-20260629.md · 2026-06-29 · living doc (decision log at the end).
- **Trigger (researcher):** the method is rewarding but *"very complex, a large number of threads in the air, hard to keep track, easy to lose focus; observations/findings all over the place and growing exponentially… immense risk of being lost/hidden/out of place; misconceptions may persist because not revisited."* Plus a stated personal constraint: *limited ability to re-read, forgets, cannot hover on many planes at once.*

## 1. The reassurance — corrected (researcher, 2026-06-29)
**Most is captured; not all.** The *dimensioned* observations live in one table, `ib_observation`, each with a `status` and a `reconsider_at`. **But the researcher is right:** there is a real category of thought the dimension structure does **not** hold — observations that *"do not have a home in the dimensions structure, are out of place but relevant further down the track, provide context for the observations but are not captured in the observation as such."* These connective/contextual thoughts are the ones genuinely at risk of being lost. **The dimension table is the atoms; it was never the whole.** The missing home is the **story** (see §3c). So: the data is recoverable, but the system needs a *second* canonical layer for the narrative/contextual tissue — not just the dimensioned atoms.

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
Stop hand-maintaining the worklist / observation-extract / track observation tables. They become **read-only renders** of `ib_observation`, produced on demand. There is then exactly **one** thing to edit for the atoms (the DB), so nothing drifts and the `.md` files stop multiplying.

### (c) The missing layer — the EMERGING STORY, in the DB prose store (researcher)
The fan-out method *"fundamentally means we have an emerging **story**, where many parts of the story are work-in-progress at the same time."* The dimensioned observations are the **atoms**; the story is the **readable narrative** that digests them — and it is also the **home for the contextual/floating thoughts** the dimension structure cannot hold (the §1 correction).

This already exists in the DB and was designed for exactly this: **`prose_section`** — typed (`prose_section_type`), **versioned in place** (`supersedes_id` / `superseded_by_id`), full-text searchable (`prose_section_fts`), linkable to track/characteristic. It is *"originally designed to let me digest the results in readable format"* — principle intact, only its **content is stale** (all legacy-method: cluster essays, Session A/B/C; newest 2026-06-21).

**Revive it for the fan-out method.** Add new section types for the new unit of work — e.g. a **focus-point / track narrative** ("the ruthlessness story so far") and a **verse reading**. Each is a living, versioned prose section: the work-in-progress story, updated in place as observations accumulate, holding the connective context that has no dimension. This is what the researcher *reads to digest* — the counterpart to `_STATE.md` (which the researcher reads to *steer*).

### The architecture in one line
**Three canonical layers in the DB, two generated read-surfaces:**
| layer | home | what it holds | you… |
|---|---|---|---|
| **Atoms** | `ib_observation` | the D1–D13 dimensioned observations | capture |
| **Story** | `prose_section` (revived) | the emerging narrative per track/verse + the contextual/floating thoughts | write & read |
| **Control** | `_STATE.md` (generated) | what's open, what to read next, what's stale | read & steer |

`verse-analysis/*.md` raw extracts stay as **generated inputs**; worklists/observation-tables become **generated renders**. Nothing canonical lives loose in a hand-edited file.

## 4. Why this is self-limiting (the "exponential growth" fear)
Open threads **grow** when a new verse is read but **contract** when convergence resolves them (a resolved thread stops driving fan-out — the method's built-in brake). The STATE page makes that contraction *visible and steerable*: you can choose the verse that closes the most threads, so the open-list trends **down**, not up. The fear is real only if we never look at the whole; the page is the whole.

## 5. The discipline going forward (small, fixed)
1. **Write only to the DB** (`ib_observation`). Never hand-edit a derived `.md`.
2. **Read `_STATE.md`** at the start of every session and after each capture (`python scripts/_assess_study_state.py`). It is the orientation.
3. **Work top-down the FAN-OUT PLAN** — pick the verse that closes the most, prepare it (`_assess_verse_raw_data.py`), read it, capture, re-generate. Watch the open count fall.
4. **Clear STALE** periodically — the oldest open threads first, before they become entrenched misconceptions.

## 6. Decisions for you
- **D1 — Adopt `_STATE.md` as the single CONTROL surface?** (built; open `verse-analysis/_STATE.md` and react to its structure/readability before committing.)
- **D2 — Revive `prose_section` as the STORY layer?** Add new section types (focus-point/track narrative · verse reading) and write the emerging story there, in the DB — versioned, searchable, the place you *read to digest* and where contextual/floating thoughts get a home. *(This replaces the earlier "hand-authored synthesis in .md" idea — the story goes in the DB, not loose files.)*
- **D3 — Make the derived `.md` (worklist / observation tables) generated renders?** Stops drift + multiplication.
- **D4 — A home for floating/contextual thoughts:** inside the track's prose story (narrative context), or a discrete "parking-lot note" capture too? (What feels natural to you?)
- **D5 — STALE cadence:** keep 7 days, or other?

## Open question to resolve next
The story layer (D2) is the bigger build and the one that answers "digest in readable format" + the floating-thought gap. Recommended sequence: **confirm `_STATE.md` (D1) first** (cheap, built), then **design the two new prose section types and revive the store (D2)** as the next focused piece — one at a time, so we don't add complexity while trying to reduce it.

## Decision log
- 2026-06-29 — proposal raised; `_STATE.md` generator built as a working first cut.
- 2026-06-29 — researcher comments folded in: (i) revive `prose_section` as the readable STORY layer; (ii) the method is an *emerging story, many parts WIP at once*; (iii) `_STATE` promising but to be judged on the real file; (iv) **correction** — not every thought is captured; contextual/floating observations have no home in the dimension structure → the story layer is that home. Architecture reframed to **3 canonical layers (atoms / story / control)**. Awaiting D1–D5.

researcher comments

Do we need to make proper use of the prose section in the database.  this was originally designed to allow me to digest the results in readable format.  Prose at the moment is stale, old, but the principle and intent is not.

The fan out method fundamentally means we have an emerging story, where many parts of the story is work in progress at the same time.

I like to idea of the _status, but would have to see how it looks like, and how it reads and is structured to allow me to comment on its usefulness.

I am not sure that your statement of very observation is captured is really true - there are a lot of observations that is going around, that does not have a home in the dimensions structure, that is out of place, but relevant further down the track, that provides context for the observations, but is not captured in the observation as such.
