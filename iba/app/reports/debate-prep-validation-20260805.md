# Debate prep — script/config validation after the lexical (T1-T3/span_reading) rework

**Date:** 2026-08-05
**Purpose:** before running a chapter debate against the new lexical, check the state of the
scripts/config that changed under it (BUILD.md §56-58, `t1-t3-design-decisions-20260805.md`).
Investigation only — no decisions made here; the items below need the researcher's call.

## 1. What's already confirmed working

- `span_reading.build` / `report.span_reading` (the T1-T3 engine, `verse-span-reading` work
  package) — verified end-to-end against **Dan 8:1-27** specifically (27 verses, 362 spans, 593
  codes, 100% resolved), including the two regression fixes (§57 function-word suppression, §58
  `sense_code` root-level stem selection) re-verified after the fix.
- `report.passage_debate`'s `BaseExtractMissing` gate — swapped 2026-08-05 from a filesystem
  check against the old `verse_span_meaning` MD to a DB check against `span_reading`. Researcher-
  approved (`RUN-RETIRE-VSM-001`). Confirmed live in `lib/passagedebatereport.py:140-147`.
- The accidental overwrite of `WA-dan-8-1-27-debate.md` during gate testing was caught
  (`reportkit`'s archive-on-regenerate) and fully restored via `git checkout` — `git diff` against
  HEAD is empty, working tree clean.
- `configmaint.validate` reports cfg_* **structurally coherent** — 0 orphan settings/enums/report
  paths/book-order/connection keys/candidate rules.

## 2. Outstanding — needs a decision before scripts are "prepared"

### a) `configmaint.validate` is PAUSED on 2 advisory findings (`RUN-20260805_160047_649-CONFIGMAINT`)

**6 stale `filled_by`** (`cfg_column.filled_by` names a step now `inactive=1`):

| # | Column | filled_by | Read |
|---|---|---|---|
| 1 | `passage.book_label` | `report.verse_span_meaning` | genuinely dormant — the step is retired everywhere, nothing writes this column via it any more |
| 2 | `passage.verse_span_meaning_path` | `report.verse_span_meaning` | same |
| 3 | `passage.verse_span_meaning_written_at` | `report.verse_span_meaning` | same |
| 4 | `passage.debate_path` | `report.passage_debate` | **likely a false positive** — `report.passage_debate` is still active under `chapter-generate` ordinal 1; it's only `inactive=1` under the separate standalone `passage-debate-report` work package. The checker (`cfgquality.find_filled_by_referencing_inactive_step`) matches on step name alone, not per-work-package, so a step active in one package and dormant-by-design in another (kept "for recovery reruns") reads as stale either way. |
| 5 | `passage.debate_written_at` | `report.passage_debate` | same as #4 |
| 6 | `passage.debate_status` | `report.passage_debate` | same as #4 |

**1 stale governance doc:** `GOVERNANCE.md` last modified 2026-08-02, before the newest applied
`cfg_change_detail` (2026-08-05T12:35:41Z — the `RUN-RETIRE-VSM-001` retirement). Per
`governance.governance_md_on_rule_change` this should have an entry and doesn't yet.

None of this blocks `span_reading`/`report.passage_debate` from running correctly today — #1-3
are dormant fields nothing depends on for the debate path, #4-6 look like a modeling artifact of
the still-open `chapter-generate` question below, not a real defect. But the run is sitting
**PAUSED waiting for an Approve/Reject/Revise answer**, and self-approving isn't something I'll do
without your say — this isn't the pre-authorized backlog-clearing case.

### b) `chapter-generate` restructuring — explicitly left open in the design record

From `t1-t3-design-decisions-20260805.md` §"Explicitly open / deferred", item 1: *"`chapter-
generate`'s restructuring — needs a decision when this is built (retire vs. reshape)."* Right now
it's a chained work package with ordinal 0 (`report.verse_span_meaning`) retired/inactive and only
ordinal 1 (`report.passage_debate`) live — a one-step chain of what used to be two. It still runs
(nothing errors), but it's an orphaned shape, and it's the direct cause of finding #4-6 above.

### c) Already-filled debates built on the old lexical — also explicitly deferred

Same doc, item 2: *"Already-filled `passage_debate` docs (Hosea/Daniel/Obadiah/Jonah/Joel/Micah)
were built on the *old* extract. Whether they get re-checked against the fixed T1-T3 data, or left
as historical — to be decided later."*

**This directly concerns `WA-dan-8-1-27-debate.md`, the file open in the IDE this session.** It
is already filled (Version 1.0, dated 2026-07-27) and cites the *old* method-doc versions in its
own front matter (`WA-passage-read-guidance-v1.3-2026-07-27.md`,
`WA-interpretation-questions-v1.2-2026-07-27.md`) — current `cfg_setting` now points at v1.5
(2026-08-02) and v1.4 (2026-08-02) respectively. So this specific debate is stale on two counts:
built before the T1-T3 fix, and cites superseded guidance-doc versions.

## 3. What I need from you before running anything

1. **Which chapter is this session's debate target?** Dan 8 already has a filled debate (pre-
   dating the lexical fix and current guidance versions) — is this session re-checking/re-doing
   Dan 8 specifically, or moving to a chapter that hasn't been debated yet?
2. **The `configmaint.validate` escalation** — Approve (acknowledge #1-6 as known/expected given
   the still-open `chapter-generate` decision), Reject (treat as needing a fix first), or Revise?
3. **`chapter-generate`'s shape** — leave the orphaned one-step chain as-is for now, or resolve it
   (retire the whole work package since `report.passage_debate` is invoked directly anyway, or
   reshape it around `verse-span-reading` + `report.passage_debate`)? Your call per the design
   record — not something I'll default past.
