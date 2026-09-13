# Base-data spine integrity + discoverability check

> Generated 2026-09-11T16:29:12Z by `spine.check`. Read-only findings against the base-data spine (`governance.base_data_spine`, escalation #1613, researcher ruling 2026-09-10) — verse defines what's included, span defines how meaning is derived, strong is the operative anchor. The strong -> extended-meaning-parse check that used to run here was REMOVED 2026-09-11 (escalation #1681/#1684/#1686) — it checked coverage against strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed, which were retired and frozen on 2026-09-10 and are no longer maintained; see handlers/spine.py module docstring for the full history. FATAL findings need action.

- **FATAL** verse/span/strong desync (span-referenced codes with no live `strong` row): **0**

## Contents

- [Summary](#summary)
- [Integrity (FATAL)](#integrity-fatal)

<a id="summary"></a>
## Summary

0 verse/span/strong desync (FATAL)

<a id="integrity-fatal"></a>
## Integrity (FATAL)

**verse/span/strong sync** — 0 code(s) a live `span` row actually names with no live `strong` row. Sample: []
