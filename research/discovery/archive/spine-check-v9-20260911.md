# Base-data spine integrity + discoverability check

> Generated 2026-09-11T03:17:58Z by `spine.check`. Read-only findings against the base-data spine (`governance.base_data_spine`, escalation #1613, researcher ruling 2026-09-10) — verse defines what's included, span defines how meaning is derived, strong is the operative anchor; these three plus the extended-meaning/parse layer below `strong` must stay in sync. FATAL findings need action; discoverability findings are backlog, not a gate.

- **FATAL** verse/span/strong desync (span-referenced codes with no live `strong` row): **0**
- **FATAL** strong_meaning_tree lemma with no strong_meaning_parsed row: **1**
- **FATAL** strong_lexicon text with no matching lsj/mounce parse: **0**
- discoverability: M-code strongs in analyzed verses missing parse: **0**
- discoverability: word_strong strongs missing parse: **0**

## Contents

- [Summary](#summary)
- [Integrity (FATAL)](#integrity-fatal)
- [Discoverability](#discoverability)

<a id="summary"></a>
## Summary

0 verse/span/strong desync (FATAL)
1 + 0 strong-meaning-parse break (FATAL)
0 M-code strongs in analyzed verses missing parse (discoverability)
0 word_strong strongs missing parse (discoverability)

<a id="integrity-fatal"></a>
## Integrity (FATAL)

**verse/span/strong sync** — 0 code(s) a live `span` row actually names with no live `strong` row. Sample: []

**strong -> extended meaning -> parse** — 1 `strong_meaning_tree` lemma(s) with no `strong_meaning_parsed` row (['H1506']); 0 `strong_lexicon` row(s) with real lsj/mounce text but no matching parsed row ([]).

<a id="discoverability"></a>
## Discoverability

**M-code strongs in analyzed verses, missing parse** (0, of 10 verse(s) with live Layer-2 notes): []

**word_strong strongs missing parse** (0 of 3494 distinct linked codes): []
