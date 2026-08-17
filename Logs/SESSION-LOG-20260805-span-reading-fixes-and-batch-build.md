# SESSION LOG — 2026-08-05 — `span_reading` regressions fixed, batch-built across 6 completed books

Continuation of the same day's design/build session (`SESSION-LOG-20260805-t1-t3-verse-span-
meaning-redesign.md`, `t1-t3-design-decisions-20260805.md`). Covers everything since that log:
two real regressions found and fixed post-build, a second failed attempt at a concatenated
"lexical verse" line, a comparative check against the old (pre-IBA, pre-reset) programme's own
lexical-view artifact, and a first batch build across all 6 completed books.

## What happened, in sequence

1. **Regression 1 (BUILD.md §57).** Researcher caught, comparing against the retired
   `report.verse_span_meaning`'s own output: grammatical-formative codes (`H9xxx`) were showing
   `[function]` with no gloss at all — a real content loss, not a display choice. Root cause: an
   unverified claim (that `H9xxx` codes "carry no stepGloss by design") baked into
   `resolve_code`'s early-return branch. Checked directly against the DB once challenged — every
   `H9xxx` code DOES carry a real stepGloss and `strong_meaning_parsed` row. Fixed: `role` no
   longer gates resolution at all; it's now pure classification metadata over a `status` field
   (`resolved`/`unregistered`) that applies uniformly to content and function codes alike. The
   false claim was corrected everywhere it was written (code comments, migration docstring, live
   `cfg_column.use` text via governed `configmaint.propose`), not just the behavior.
2. **Regression 2 (BUILD.md §58), same day, deeper.** Researcher's own STEP screenshot (Dan 8:2
   "saw") showed the root-level sense ("to see, look at, inspect, perceive, consider") missing
   from every stem-narrowed reading. Traced to the actual cause: `strong_meaning_parsed` already
   carries a hierarchical `sense_code` (`'1)'`/`'1a)'`/`'1a1)'`...) that `_bucket_by_stem` never
   read, instead regex-scanning gloss *text* for `(StemName)` markers — which silently dropped
   the digit-only root row every time, and (checked against a second word, `H1288`) would have
   misread a root-level citation marker like `(TWOT)` as a stem, had it ever fired. Rebuilt
   `_select_stem_text` on `sense_code`'s real hierarchy instead of text-guessing — fixes both.
3. **"Lexical verse" concatenation tried a second time, on request, and removed again.**
   Researcher asked to retry given the function-word fix. Rebuilt (raw `stepGloss` per component,
   concatenated in stored order, explicitly unpolished) and shown honestly rather than assumed
   better. Confirmed worse in one respect: function words now resolving meant every prefix/suffix
   appeared as its own trailing token in non-reading order (`"year in/on/with"` instead of "in the
   year"), compounding `stepGloss`'s own punctuation artifacts. Researcher: *"it does not work or
   serve a purpose."* Removed cleanly, dead code removed with it — second time this exact idea
   has failed for the same structural reason (flattening loses the grouping that makes the
   per-span table work).
4. **DB volume / read volume sizing**, on request — measured, not projected: full-corpus
   `span_reading` ≈ 534,075 rows / ~123 MB content (one clean build); a single chapter's rendered
   report ≈ 34,000 tokens (Dan 8, 27 verses) — reinforces the existing 3-chapters/session
   guideline (`token-consumption-diagnostic-20260802.md`) rather than introducing a new concern.
   Also flagged: version-aware soft-deletes accumulate indefinitely (2,372 superseded rows from
   just this session's own re-testing on one 27-verse chapter) — not yet decided whether/when old
   versions get purged.
5. **Compared against the old (pre-IBA) programme's own lexical-view artifact**
   (`verse-analysis/daniel/phase1-views/wa-dan8-phase1-lexical-view-20260704.md`), on request.
   Finding: that file's "sense=X" field is the English surface word restated, not real lexical
   resolution; no stem/morph handling; but it DOES attempt relational tagging (bearer/operation/
   target) and direct M-cluster characteristic assignment in the same pass, via a heuristic it
   explicitly flags as unreliable in nearly every row (`discovery=bearer unreliable`). Read as
   independent confirmation of this session's core design principle: asserting an unverified
   relational guess alongside an honesty caveat is not the same as resolving it — exactly the
   shortcut `span_reading`'s T1-T3/T4-T9 boundary was built to rule out.
6. **Batch build across all 6 completed books.** `span_reading.build` + `report.span_reading` run
   for chapter 1 of Hosea/Jonah/Joel/Obadiah/Micah (Daniel ch8 already built from earlier
   testing). All 6 clean, 100% resolved: Dan 8 (593/593), Hos 1 (209/209), Jonah 1 (388/388),
   Joel 1 (299/299), Obad 1 (394/394), Mic 1 (279/279).

## State at close

`span_reading` now has representative, verified data across all 6 completed books, ready for the
researcher to judge against a rebuilt debate. Next step, researcher-directed: reset session,
begin building the debate module (T4-T9 integration with `report.passage_debate`) — explicitly
deferred researcher's-own work per the original design record, not attempted this session.

`configmaint.validate` clean of everything except the same 2 pre-existing advisory findings noted
in the prior session log (stale `filled_by` on 3 `passage.*` columns now genuinely orphaned by the
old routine's retirement; `GOVERNANCE.md` staleness check) — both still open, still the
researcher's call, not defaulted on.
