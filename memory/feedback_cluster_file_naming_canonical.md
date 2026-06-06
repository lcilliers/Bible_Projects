---
name: feedback-cluster-file-naming-canonical
description: "Canonical naming convention for files inside Sessions/Session_Clusters/{CODE}/ — always wa-cluster-{CODE}-... (lowercase prefix + cluster segment + CAPS code)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

For any file CC creates at the top level of `Sessions/Session_Clusters/{CODE}/`, the canonical naming convention is:

**`wa-cluster-{CODE}-{kind}-v{n}-{YYYYMMDD}.{ext}`**

- `wa-cluster-` — lowercase prefix with literal `cluster` segment (makes scope explicit)
- `{CODE}` — cluster code in CAPS (`M01`, `M07`, `M46`) — cluster codes are conventionally CAPS in the DB; the filename mirrors that
- `{kind}` — descriptor of artefact (e.g. `dir-001-term-transfer`, `phase9-char1-arrogant-self-elevation-brief`, `constitution`, `subgroup-design`, `vcg-creation`)
- `v{n}` — integer version, no leading zero
- `{YYYYMMDD}` — compact date

**Why:** Aligns with [[file-organisation-rules]] §2.1 (all-lowercase rule with explicit carve-out only for governing instruction docs `WA-DocumentName-...`). Cluster artefacts are not in the carve-out.

**How to apply:**
- When generating any new cluster-folder file via Write / scripts / AI session direction, use `wa-cluster-{CODE}-...`. Never `WA-{CODE}-...` (the CAPS-no-cluster variant).
- When directing AI sessions to produce files, specify the canonical filename in the brief's "After you finish" section so AI doesn't default to `WA-{CODE}-...`.
- For Phase 9 char findings, the canonical form is `wa-cluster-{CODE}-phase9-char{N}-{short-name}-findings-v{n}-{date}.md`.
- For sub-group VCG design files where the sub-group code is `{CODE}-{letter}` (e.g. M07-A), the filename uses just the letter: `wa-cluster-M07-A-vcg-design-v1-{date}.md` — NOT `wa-cluster-M07-M07-A-...` (doubled-prefix bug seen in older M07 work and corrected on 2026-05-21).

**Exceptions retained:**
- `wa-obslog-{CODE}-{kind}-...` — observation logs are a distinct category, kept as-is.
- `wa-global-...` and `wa-sessionlog-...` — programme-level artefacts, different naming category.

**Reference:** [[docs/cluster-naming-assessment-20260521.md]] documents the 2026-05-21 cleanup that renamed 312 CAPS-prefix files + deleted 13 duplicate lowercase-code variants + 7 pass-2 anomalies across 13 clusters (M01–M08, M15, M20, M26, M32, M39, M46).

The scripts that generate cluster-folder files (e.g. the per-cluster Phase 9 builders at [[scripts/_build_m08_characteristic_phase9_package_20260521.py]]) have been updated to emit the canonical form. If you clone an M0X builder for a new cluster, the substitution patterns continue forward.
