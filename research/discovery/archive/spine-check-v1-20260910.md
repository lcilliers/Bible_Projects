# Base-data spine integrity + discoverability check

> Generated 2026-09-10T04:19:05Z by `spine.check`. Read-only findings against the base-data spine (`governance.base_data_spine`, escalation #1613, researcher ruling 2026-09-10) — verse defines what's included, span defines how meaning is derived, strong is the operative anchor; these three plus the extended-meaning/parse layer below `strong` must stay in sync. FATAL findings need action; discoverability findings are backlog, not a gate.

- **FATAL** verse/span/strong desync (span-referenced codes with no live `strong` row): **409**
- **FATAL** strong_meaning_tree lemma with no strong_meaning_parsed row: **2**
- **FATAL** strong_lexicon text with no matching lsj/mounce parse: **2**
- discoverability: M-code strongs in analyzed verses missing parse: **0**
- discoverability: word_strong strongs missing parse: **2**

## Contents

- [Summary](#summary)
- [Integrity (FATAL)](#integrity-fatal)
- [Discoverability](#discoverability)

<a id="summary"></a>
## Summary

409 verse/span/strong desync (FATAL)
2 + 2 strong-meaning-parse break (FATAL)
0 M-code strongs in analyzed verses missing parse (discoverability)
2 word_strong strongs missing parse (discoverability)

<a id="integrity-fatal"></a>
## Integrity (FATAL)

**verse/span/strong sync** — 409 code(s) a live `span` row actually names with no live `strong` row. Sample: ['G0007G', 'G0010', 'G0084', 'G0107', 'G0131', 'G0174', 'G0257', 'G0284', 'G0300', 'G0325', 'G0354', 'G0638', 'G0643', 'G0689', 'G0702']

**strong -> extended meaning -> parse** — 2 `strong_meaning_tree` lemma(s) with no `strong_meaning_parsed` row (['G6507', 'G7167']); 2 `strong_lexicon` row(s) with real lsj/mounce text but no matching parsed row (['G6507', 'G7167']).

<a id="discoverability"></a>
## Discoverability

**M-code strongs in analyzed verses, missing parse** (0, of 10 verse(s) with live Layer-2 notes): []

**word_strong strongs missing parse** (2 of 3494 distinct linked codes): ['G6507', 'G7167']
