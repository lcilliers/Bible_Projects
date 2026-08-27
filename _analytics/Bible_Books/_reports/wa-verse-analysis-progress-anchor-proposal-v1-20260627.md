# Verse-analysis progress anchor — proposal (for confirmation before DB write)

- **File:** wa-verse-analysis-progress-anchor-proposal-v1-20260627.md · 2026-06-27 · Author: Claude Code.
- **Intent (researcher):** record **progress of analysis against the verse index** — which verses are analysed (complete / partial) and which were **pulled into focus** by an analysed verse's observations and now await analysis. The fan-out generates a worklist; this anchor tracks it.
- **Status:** proposal — nothing written to the DB yet. Confirm the model below and I will build it.

## 1. The model — one new table `verse_analysis_progress`
One row per verse that has entered the work (analysed or pulled into focus). Keyed to `verse.id`. Everything is **re-derivable from `ib_observation`**, so it stays live.

| column | meaning |
|---|---|
| `verse_id` / `reference` | FK to the verse index |
| `status` | `complete` · `partial` · `in_focus` · `untouched` |
| `obs_count` | observations whose **origin** is this verse (i.e. analysis done *on* it) |
| `pulled_count` | how many observations **reference** it (brought it into focus) |
| `pulled_from` | the analysed verse(s) that pulled it in (provenance) |
| `open_dims` | the dimensions it could help **resolve** (why it's worth analysing — the fan-out priority) |
| `note`, `first_seen`, `last_updated` | housekeeping |

**Status vocabulary (proposed):**
- **complete** — fully fanned out, all operations swept all dimensions. → **Exo 1:13**
- **partial** — analysis begun, not finished. → **Gen 6:5**
- **in_focus** — referenced by an observation's `reconsider_at`/citation; *pending* analysis. → the 31 below
- **untouched** — in the index, never entered the work (the default; not stored as rows, it's "everything else")

**Open question for you (neighbour verses):** Exo 1:14 and Gen 6:6 were captured *inside* the focus verse's window (they carry observations) but were not independently fanned out. Proposed: mark them **partial**. (Alternative: fold them into the focus verse as "covered".)

## 2. What the anchor holds right now

### Analysed / touched (4)
| verse | proposed status | observations |
|---|---|---|
| **Exo 1:13** | complete | 21 |
| **Exo 1:14** | partial (neighbour, covered) | 2 |
| **Gen 6:5** | partial | 14 |
| **Gen 6:6** | partial (neighbour, covered) | 1 |

### Pulled into focus — pending analysis (31), grouped by the open question they would resolve
*This is the prioritised worklist: a verse is worth analysing insofar as it closes an open dimension.*

**Enslavement is valence-neutral? (Exo 1:13 · D10/D12)** — 2Ch 34:33 · Isa 43:23 · Isa 43:24
**Ruthlessness is condemned / kin-bounded? (Exo 1:13 · D10/D12/D9)** — Lev 25:43 · Lev 25:46 · Lev 25:53 · Eze 34:4
**Fear→cruelty; restraint = fear of God (Exo 1:13 · D2)** — Exo 1:8 · Exo 1:12 · Gen 20:11 · Deu 25:18 · Psa 36:1 · Ecc 8:9
**Anger→cruelty (Exo 1:13 · D2)** — Gen 49:7 · Pro 27:4
**Evil comes from the heart / within (Exo 1:13 + Gen 6:5 · D2/D4/D7)** — Jer 17:9 · Mar 7:21 · Mar 7:22 · Mar 7:23 · Mat 15:18 · Mat 15:19
**Heart as the forming/intending seat (Gen 6:5 · D1/D7/D11)** — 1Ch 28:9 · 1Ch 29:18 · 1Sa 16:7 · Isa 26:3 · Isa 29:16 · Hab 2:18
**The formed inclination / yetser & the potter (Gen 6:5 · D1/D7/D12)** — Gen 8:21 · Gen 6:7
**God's heart grieved (Gen 6:6 · D12)** — Eph 4:30 · Isa 63:10

## 3. How it advances
- A verse with `in_focus` status is picked up, fanned out → its own observations are captured → status flips to `partial`/`complete`, and **its** observations may pull in *new* verses (the worklist grows and contracts as open dimensions converge).
- `in_focus` rows and `open_dims` are **re-derived from `ib_observation`** on each refresh (a script), so the anchor never drifts from the observations.
- A simple roll-up (counts by status) gives the progress read at any time.

## 4. To confirm before I build
1. Status vocabulary (`complete`/`partial`/`in_focus`/`untouched`) — keep / change?
2. Neighbour verses (Exo 1:14, Gen 6:6) → `partial`, or fold into the focus verse?
3. Store `open_dims` (the resolve-priority) on each `in_focus` row — yes/no?
4. One table `verse_analysis_progress` as above — or do you want the focus *links* (origin→target, per open question) as a separate table too (richer, but two tables)?
