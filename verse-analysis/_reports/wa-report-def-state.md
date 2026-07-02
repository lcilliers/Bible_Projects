# Report Definition — _STATE (whole-study progress / mission control)

- **Type:** living definition spec · Version 1 · 2026-06-30
- **Report class:** whole-study **rollup** → living generated page, no `-vN` (history in git)
- **Generator:** `scripts/_assess_study_state.py` (exists)
- **Output path:** `verse-analysis/_STATE.md`
- **Source of truth:** the DB only (`ib_observation` + `verse_analysis_progress`). Never hand-edited.

---

## 1. Purpose
The single-page **live state of the entire verse-fanout study** — "mission control." Read it instead of re-reading the sprawl. It says, at a glance: how much has been observed, what is open, and **what to read next and why**. Because it is generated from the DB on demand, it can never drift or go stale.

## 2. Input
- None. Always the whole study.
- `--stdout` to print instead of writing the file.

## 3. Source data
| Block | DB source |
|---|---|
| Observations (all fields) | `ib_observation` |
| Verse progress / roles | `verse_analysis_progress` |
| Stream key | `ib_observation.operation` (the "track") |
| Next-verse targets | verse refs parsed from `ib_observation.reconsider_at` |

## 4. Report structure (sections, in order — as implemented)
1. **Headline** — total observations · analysed verses · tracks · status spread (resolved / needs-corroboration / open / silent) · open-thread count · stale count.
2. **▶ Fan-out plan** — the verses to read next, ranked by how many open threads each closes (from `reconsider_at`), with the threads + tracks each touches.
3. **Open threads — by track** — every unresolved observation in full text, with its `→ go to` target.
4. **By track — rollup** — per-stream resolved / open / silent / total.
5. **By origin verse** — every analysed verse, the tracks it opened, and its status counts (so any verse is findable).
6. **Verse progress** — focus verses (in progress) + count of cross-referenced verses pending, from `verse_analysis_progress`.
7. **⚠ Stale** — open observations not revisited ≥7 days (misconception risk).
8. **Recently resolved** — last 10 closures, for spot-checking wrong closures.

## 5. Versioning & filing
- **Class:** whole-study rollup → **living page, no `-vN`.**
- Overwritten in place on each run (`verse-analysis/_STATE.md`). It is a snapshot of *now*; historical states are recoverable from git.
- "Do not hand-edit" banner is written into the file itself.

## 6. Constraints
- Read-only; regenerated on demand; always current by construction.
- Derives streams and next-targets purely from DB fields — no external list to maintain.

## 7. Build status & open items
- **Generator exists and is in use.** No build required.
- Optional alignment: when the Stream_observations and Verse_observation reports exist, the _STATE "go to" / "by origin verse" entries can link to them. Low priority.
