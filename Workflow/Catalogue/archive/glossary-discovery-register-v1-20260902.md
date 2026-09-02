# Glossary deep-discovery register (v1) — living document

**Escalation:** #1377. **Purpose:** track, across however many sessions this actually takes, which
project documents have been read closely for project-specific terminology, per the researcher's
correction 2026-09-02: *"Wherever terminology are used with a specific meaning in the project that
is beyond the standard dictionary application, the term must be captured... this session is about
harnessing a shortfall that has perpetuated almost through the lifetime of the project."*

This is a **single living register** (`feedback_single_living_register`) — update this file in
place as each document/folder is worked through. Do not create a v2 for routine progress; only for
a real structural change to how the register itself works.

## Why the earlier fallout scan couldn't do this alone

The scan in `glossary-fallout-findings-v1-20260902.md` matched against `cfg_column`/`cfg_setting`/
`cfg_prose` TEXT — it can only ever find a term that appears in a live column name or in someone's
free-text description of one. It is **structurally blind** to any term that exists only in
narrative method/instruction prose with no corresponding DB column — proven live: reading ONE
164-line document (`wa-verse-analysis-method-v1-20260702.md`) surfaced **~15 new terms** (`grain`,
the Gate-1/Gate-2 span-admission scheme, a second `role` sense, `cohabitation`'s contested status,
`segmentation unit` types, `oracle`, the `owner term`/`OWNER` collision) — none of which the scan
could ever have found, because none of them is a column name or appears in a `cfg_column.use`
description. **The deep-discovery pass has to be an actual reading pass, document by document.**

## Scale, stated plainly

`find Workflow -type f` = 7,744 files, but 7,130 are CSVs (mostly `Workflow/schema/archive` schema
dumps — not narrative, not a terminology source). The real corpus is **510 `.md` files** (+ ~71
`.json`, mostly patches/extracts, lower priority) spread across:

| Folder | Current | +archive | Notes |
|---|---|---|---|
| `Instructions` | 25 | 35 | Authoritative method/pipeline docs — highest density, started here |
| `methodology` | 56 | 65 | Session design-decision logs — likely where "new word, same thing" actually happened |
| `Catalogue` | 19 | 7 | Observation/dimension catalogues — terminology-heavy by nature |
| `Programme` (prose, reports, prose-edits) | ~35 | ~50 | Programme prose itself, already partly covered by the fallout scan's prose read |
| `reference` | 8 | — | |
| `registry` | 4 | — | |
| `Global_rules` | 5 | — | Old rule-registry exports — likely defines terms `wa_rule_registry` once governed |
| `Tiers` / `Clusters` / `Sciences` | ~5 | ~67 | |
| `Chat_responses` | — | 16 | Researcher's own review notes — may contain terminology the docs never wrote down |

**One document at moderate density yielded ~15 new terms.** Even allowing most documents to be
far sparser than that (many are procedural/status logs, not concept-introducing), this is not a
one-sitting task. It is exactly the multi-session campaign the researcher's framing describes.

## Status

| Folder | Files | Read for terminology | Terms captured this pass |
|---|---|---|---|
| `Instructions` (current) | 25 | **1** (`wa-verse-analysis-method-v1-20260702.md`) | ~15 (in `glossary-draft-entries-v1-20260902.md`, batch 2) |
| `Instructions` (current) | 24 remaining | 0 | — |
| `Instructions/archive` | 35 | 0 | — |
| `methodology` (+archive) | 121 | 0 | — |
| `Catalogue` (+archive) | 26 | partial — the seed's own Parts 1-4 already mined this folder's `vocabulary-glossary-seed-v2` and its own sources | — |
| `Programme` (prose/reports/prose-edits) | ~85 | partial — `wa-programme-prose-extract-20260827.md` already read for #1377 v2 | — |
| `reference` | 8 | 0 | — |
| `registry` | 4 | 0 | — |
| `Global_rules` | 5 | 0 | — |
| `Tiers` / `Clusters` / `Sciences` (+archive) | ~72 | 0 | — |
| `Chat_responses/archive` | 16 | 0 | — |

## Next document, when this resumes

`Workflow/Instructions/wa-claudecode-instruction-v4_5-20260514.md` — the CC-facing authoritative
instruction, cross-referenced everywhere in `CLAUDE.md` §10, likely to define or assume several
more process terms. Then continue down the `Instructions` list in the order `ls` returned it
(recorded in `glossary-fallout-findings-v1-20260902.md`'s companion scan is NOT the same list —
use `Workflow/Instructions/*.md`, 25 files, non-archive first, then `archive/`).

## Not a decision made here

Whether to keep pushing through the full 510-document corpus in one continuous campaign, or to
prioritise (e.g. current/live docs across all folders before any archive, or highest-density
folders first) is the researcher's call, not assumed — flagged in the escalation update, not
decided by proceeding silently.
