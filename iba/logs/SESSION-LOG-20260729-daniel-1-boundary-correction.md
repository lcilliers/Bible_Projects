# Session log — 2026-07-29 — Daniel 1:7-21 corrected to 1:8-21 (passage-table audit finding)

Triggered by the researcher asking whether the `passage` table was up to date. A full audit
(debate_status vs. file content, `verse_count` vs. live `verse_passage` link count, anchor
uniqueness, no verse double-linked) found the mechanism was structurally sound everywhere except
one `verse_count` mismatch: `Dan 1:1-7` said 7, only 6 verses were actually live-linked.

## What this session found

Dan.1.7 is a genuine boundary verse shared between `Dan 1:1-7` and (as it turned out, mislabeled)
`Dan 1:7-21`. BUILD.md §28's own 2026-07-27 verification found this exact fact and called it
correct, because the DB's "one live owner per verse" invariant was satisfied (whichever range
processed later held the live link). What that verification never checked: which file's PROSE
actually analyses the verse. Reading `WA-dan-1-7-21-debate-v1.2-2026-07-27.md` directly showed it
contains only a one-paragraph "Dan 1:7 — carried by reference" stub, explicitly pointing back to
`WA-dan-1-1-7-debate` as where the verse is actually debated — never independent analysis. The
researcher named this precisely and directed the fix: the range should be `1:8-21`, matching
where the file's own real content begins.

## What was corrected

1. **New base extract**, `dan-1-8-21-verse-span-meaning.md` — generated via a direct
   `versespanmeaningreport.write_report()` call, deliberately bypassing the report-handler
   dispatcher (which would have inserted a second, duplicate `passage` row for the new range
   rather than correcting the existing one). 170/170 non-particle spans, 100% — the old range's
   183/183 included verse 7's own 13 spans, which never belonged to this analysis.
2. **New debate file**, `WA-dan-1-8-21-debate-v1.3-2026-07-29.md` — hand-corrected from v1.2: the
   "Dan 1:7 — carried by reference" stub removed; title/filename/version/change-control notes and
   the coverage statistic updated; every analytical conclusion for verses 1:8-21 left unchanged.
3. **Both superseded files archived**, not deleted:
   `archive/WA-dan-1-7-21-debate-v1.2-2026-07-27.md`,
   `archive/dan-1-7-21-verse-span-meaning-20260729-095948.md`.
4. **One-off migration**, `migration/correct_dan_1_boundary_range.py` (matching the established
   `reconcile_daniel_debate_paths.py` pattern): updates the `passage` row in place (`start_verse`
   7→8, `ref` 'Dan 1:7-21'→'Dan 1:8-21', both file paths, `anchor_verse_id` Dan.1.7→Dan.1.8,
   `verse_count` 15→14); soft-deletes the `verse_passage` link from `1:7-21` to Dan.1.7; restores
   (un-deletes) the link from `1:1-7` to Dan.1.7 — where it actually belongs. A follow-up direct
   fix (folded into the script) set `is_anchor=1` on the `1:8-21`/Dan.1.8 link, since only
   `anchor_verse_id` had been repointed at first, leaving the passage briefly with zero live
   anchors.
5. **Two other references to the old range corrected** (pointers only, no analytical content
   depended on them): `WA-dan-whole-book-read.md`'s coverage list and section heading; a plain
   citation inside `WA-dan-2-31-49-debate-v1.1`.

## Verified

Re-ran the full `passage`-table audit after the fix — all 23 live rows clean: every
`debate_status` matches its file's actual content, every `verse_count` matches its live
`verse_passage` link count (including the originally-flagged `Dan 1:1-7`, now correct because its
rightful link was restored, not because a number was edited), every passage has exactly one live
anchor matching its own `anchor_verse_id`, no verse is double-linked.

## Found, not chased (out of scope)

`WA-dan-whole-book-read.md` itself still has 17 unfilled `<!-- fill in -->` Resolution
placeholders — Daniel's whole-book-read was generated but never actually resolved, contrary to
the "complete" status recorded in [[project_iba_book_by_book_debate_phase]] since 2026-07-27.
Flagged, not fixed — resolving 17 items is a separate, much larger task than this boundary
correction and was not requested.

## Artifacts this session

- `iba/app/verse-analysis/Daniel/dan-1-8-21-verse-span-meaning.md` (new)
- `iba/app/verse-analysis/Daniel/WA-dan-1-8-21-debate-v1.3-2026-07-29.md` (new)
- `iba/app/verse-analysis/Daniel/archive/WA-dan-1-7-21-debate-v1.2-2026-07-27.md` (moved)
- `iba/app/verse-analysis/Daniel/archive/dan-1-7-21-verse-span-meaning-20260729-095948.md` (moved)
- `iba/app/migration/correct_dan_1_boundary_range.py` (new)
- `iba/app/verse-analysis/Daniel/WA-dan-whole-book-read.md` (2 range-label references corrected)
- `iba/app/verse-analysis/Daniel/WA-dan-2-31-49-debate-v1.1-2026-07-27.md` (1 citation corrected)
- `iba/app/BUILD.md` §36 (this correction documented)

## Open decisions / next steps

- Daniel's whole-book-read is genuinely incomplete (17 unfilled resolutions) — worth a dedicated
  session if the researcher wants Daniel brought fully into line with Jonah/Joel's completion
  shape, but not undertaken here.
- No other book was audited for the same class of boundary-sharing issue this session — Jonah and
  Joel's passage rows were already confirmed clean by the same audit; only Daniel had ranges old
  enough to predate the mechanised `passagetrack` system and its "carried by reference" convention.
