# Fan-out structure — per-track .md files (proposal for discussion)

- **File:** Workflow/methodology/wa-fanout-track-structure-proposal-v1-20260628.md · 2026-06-28 · Author: Claude Code.
- **Trigger (researcher):** each track of a verse's fan-out should be its own .md — (a) easier to follow/digest, tracks differ, each has its own observations; (b) when the next verse in a track is analysed it can sit *adjacent* to the related verses — "one fan-out for all the verses in the track."
- **Status:** proposal — nothing restructured yet.

## The key realisation
Reason (b) is bigger than (a). It says the **track is a cross-verse unit**, not just a section of one verse. A "ruthlessness track" is *all* the `perek` verses (Exo 1:13, 1:14, Lev 25:43/46/53, Eze 34:4) read together — exactly the set we just made M06. So the track **is the focus-point-in-construction**: gather every verse where an operation occurs, accumulate observations, watch convergence.

## Two models
**A — verse-anchored, track sub-files.** `wa-exo-001-013-track-ruthlessness.md` etc. under the verse's book folder.
- ✓ clean per-verse · ✗ a track's verses are scattered across many book folders → does NOT satisfy (b).

**B — track-anchored, cross-verse (your (b)).** One doc per track that accumulates *all* its verses.
- ✓ all related verses adjacent → comparison + convergence visible; this is how a focus point builds · ✗ a single verse's content is split across the tracks it opens.

## Recommendation — HYBRID (thin verse index + cross-verse track docs)
- **Per-verse = a thin INDEX**: the verse text, neighbours, and the **tracks it opens** (links). The entry point, not the content. `verse-analysis/{Book}/wa-{book}-{ccc}-{vvv}-fanout.md`.
- **Per-track = the content, cross-verse**: one doc per operation, accumulating every verse in it + the raw evidence + observations. This is where analysis lives and grows.
- **Why hybrid:** it satisfies (b) (tracks accumulate verses) *and* keeps a per-verse entry point; and it matches the data — `ib_observation` already keys observations by **`operation`** (= the track) + `origin_verse`, so the track view is just a group-by we already support.

## Proposed layout
```
verse-analysis/
  {Book}/ wa-{book}-{ccc}-{vvv}-fanout.md     ← thin verse index → links to the tracks it opens
  _tracks/{M-cluster}/
       wa-track-{operation}-{anchor}.md       ← cross-verse: ALL verses in the track + observations
         e.g. _tracks/M06/wa-track-ruthlessness-H6531.md  (Exo 1:13, 1:14, Lev 25:43/46/53, Eze 34:4)
              _tracks/M36/wa-track-enslavement-H5647.md
```

## Design questions for you
1. **Track granularity** — is a track a **term** (`perek` H6531), or a **characteristic/focus point** (M06 Cruelty/Ruthlessness, which spans `perek`+`arits`+`akzar`)? *(lean: term-anchored track files, grouped under the cluster/characteristic folder — so cruelty = several term-tracks that converge.)*
2. **Location** — `_tracks/{cluster}/` (groups tracks by cluster), or flat `_tracks/`? *(lean: by cluster.)*
3. **The verse index** — keep the rich per-verse fanout, or reduce it to a thin index once the content lives in track docs? *(lean: thin index; content in tracks.)*
4. **Migration** — split the current Exo 1:13 monolith into: a thin `…-013-fanout` index + `_tracks/M06/wa-track-ruthlessness-H6531.md` + `_tracks/M36/wa-track-enslavement-H5647.md`. Do this as the worked example?

## Note
This dovetails with the integration build: as each orphan term becomes an OWNER term with its verses (perek done), its **track doc is the natural place its verses + observations accumulate** — the term integration and the track fan-out are the same motion from two ends.
