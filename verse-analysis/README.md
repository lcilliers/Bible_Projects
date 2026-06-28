# verse-analysis/ — home of the verse-fanout inner-being method

> **Doc version:** 1 · **Last updated:** 2026-06-27 · living document (edit in place; git is the history).

This tree holds **all work products of the verse-fanout method** — the method that starts from a single verse, fans out to all related evidence, and digests it into inner-being observations. It superseded the cluster method (`Sessions-v2/`).

## What lives here (and what does not)
- **Here:** per-verse **raw source collections** (inputs, incl. researcher-added Logos/Claude material) and **regenerable extracts** (verse + observations), plus cross-verse reports.
- **NOT here — the source of truth is the DB:** observations live in `ib_observation`; analysis progress in `verse_analysis_progress`. Files are inputs or exports, never the record of findings.
- **NOT here — method/governance docs** live in `Workflow/` (see Method docs below).

## Two layers (2026-06-28)
- **RAW (per-verse):** `{Book}/wa-{book}-{ccc}-{vvv}-fanout-*.md` — the verse's inputs (morphology, spiderweb, Logos/Claude extracts, the full-window read). Preserve.
- **WORKED (cross-verse):** `_tracks/{cluster}/wa-track-{operation}-{anchor}.md` — one doc per **track** (an inner-being operation), accumulating **every verse in that track** + its observations. A track is the **focus-point-in-construction**. Observations live in `ib_observation` (keyed by `operation` = the track); the track doc presents + synthesises them across verses.
- A verse "opens" one or more tracks; a track collects many verses. (Design: `_reports/wa-fanout-track-structure-proposal-v1-20260628.md`.)

## Structure
```
verse-analysis/
  README.md                 ← this file
  _reports/                 ← cross-verse roll-ups (progress, worklist, anchor + structure design)
  _tracks/{M-cluster}/      ← WORKED layer: one doc per operation, cross-verse
    wa-track-{operation}-{anchor}.md     e.g. _tracks/M06/wa-track-ruthlessness-H6531.md
  {Book}/                   ← RAW layer: one folder per book, DB short_code (Gen, Exo, Lev …)
    wa-{book}-{ccc}-{vvv}-fanout-v{n}-{date}.md        ← RAW source collection (input — preserve)
    wa-{book}-{ccc}-{vvv}-observations-v{n}-{date}.md  ← verse + observations extract (regenerable)
```
- **Flat within each book** (no per-verse subfolder). A file appears only when its verse is actually worked.
- **Naming:** chapter and verse **zero-padded to 3 digits** so the whole canon sorts (`Exo-001-013`, `Psa-119-176`). The DB reference (`Exo 1:13`) stays canonical; the padded form is the file encoding.
- **File types:** `fanout` = raw collection (irreplaceable input) · `observations` = extract regenerated from `ib_observation`.

## How to find a verse
- The file: `verse-analysis/{Book}/wa-{book}-{ccc}-{vvv}-*`.
- Its observations (live): `ib_observation WHERE origin_verse='{ref}'`.
- Its progress + what it pulled into focus: `verse_analysis_progress WHERE reference='{ref}' OR xref_verse='{ref}'`.
- Or `python scripts/build_file_manifest.py --search "{book} {c} {v}"`.

## Method docs (governance — in `Workflow/`)
- `Workflow/methodology/wa-METHOD-SYNTHESIS-verse-fanout-multicontributor-v1-*.md` — master synthesis (read first).
- `Workflow/methodology/wa-verse-fanout-operating-model-v1-*.md` — the operating model.
- `Workflow/methodology/wa-IB-verse-dimensions-definition-v1-*.md` — dimension definitions.
- `Workflow/Catalogue/wa-IB-verse-dimensions-catalogue-v1-*.md` — D1–D12 controlled codes.
- `Workflow/methodology/wa-verse-meaning-fanout-index-design-v1-*.md` — the verse↔evidence spiderweb index.

## Current contents (2026-06-28)
- **Exo/** — Exo 1:13 (analysis in progress; fanout + observations).
- **Lev/** — Lev 25:43 (analysed; 3 streams — fear-of-god/dominion/ruthlessness; fanout + observations).
- **Gen/** — Gen 6:5 (partial; fanout + observations).
- **_tracks/** — `M01/` fear-of-god (`yare` H3372) · `M06/` ruthlessness (`perek` H6531) · `M23/` dominion (`radah` H7287) · `M36/` enslavement (`abad` H5647).
- **_reports/** — verse-analysis progress anchor design + fan-out track-structure proposal.
