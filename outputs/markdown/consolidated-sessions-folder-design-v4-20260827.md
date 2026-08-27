# A single consolidated `Sessions/` folder — v4: the Processing branch

Prepared for escalation #933. Adds the Processing branch, deliberately left undesigned in v1–v3
per the researcher's own sequencing. Per the researcher, Processing splits into three kinds of
thing, plus one large open question about `iba/` itself. Still a design only — nothing moved.
`#929` v2 stays the untouched reference; v1–v3 (Analytics/Raw Data) stand unchanged.

## 1. The three kinds of Processing content, and what stays put

**(a) Technology-driven root folders — not part of this consolidation, stay exactly where they
are.** These aren't analytic-file locations at all; they're where tooling itself expects to find
things: `.claude/`, `.env`, `scripts/` (code), `engine/` (code), `Logs/` (fixed by
`governance.session_log_dir`), `database/` (the DB files), `backups/`, `data/`, `memory/` (Claude's
own memory mirror), `.vscode/`, `.obsidian/`, `scratchpad_tmp/`. Named explicitly so the design
doesn't quietly imply moving them — it doesn't.

**(b) "Other files," largely in `Workflow/`** — the actual bulk of processing content, real counts
from the #929 v2 census: `Workflow/methodology/` (131), `archive/` (87, `Workflow`'s own local
archive, not the project-root one), `Programme/` (67), `Sessionlogs/` (61), `Instructions/` (57),
`Tiers/` (36), `Clusters/` (33 — process-tranche material, not analytic cluster content, despite
the name), `schema/` (18), `Sciences/` (10), `reference/` (8), `Chat_responses/` (6),
`Global_rules/` (5), `registry/` (4), `Catalogue/` (2), `Claude_API/` (1). Plus `docs/` (36, flat,
ungrouped, no fit in any of v1–v3's buckets) and `research/investigations/` (380 — process-focused
investigation notes, distinct from `research/discovery/`'s raw STEP pulls, which v3 already routed
to Raw Data).

**(c) "Reports" — the scattered pot.** Real locations, from the census: `outputs/markdown/` (202),
`outputs/integrity/` (43), `outputs/archive/` (40), `outputs/projections/` (9), `outputs/reports/`
(4), `iba/app/reports/` (466 — escalation histories + config-report snapshots, see §2),
`database/archive/file_manifest.json` (1, a frozen manifest artefact). This is exactly the "pot of
diverse files in many locations" the researcher named — no single existing folder is "the reports
folder" today; at least seven are.

## 2. The `iba/`-introduced duplication, and the open question

`iba/` has grown its own parallel processing locations, distinct from and unaware of the main
project's: `iba/docs/` (design proposals — the same *kind* of content as `Workflow/methodology/`
or `docs/`, just under `iba/`), `iba/app/reports/` (escalation histories and CONFIG-REPORT
snapshots — a reports location the main project's `outputs/reports/` doesn't know about),
`iba/config/` (the separate, not-yet-loadable configurator design, `GOVERNANCE.md` §6 — its own
small doc set). This is the same shape of problem v1–v3 found on the Analytics side
(`Sessions-v2`/`Session_Clusters`, the two `verse-analysis` trees) — a second location for the same
kind of content, grown because `iba/` was built as a self-contained subtree rather than as part of
the one project structure from the start.

**What's settled:** per the researcher, direct — *"all raw data and analytic files in IBA should
move"* — `iba/app/verse-analysis/` (308 files) already routes to `analytics/by-book/` under v3;
nothing new needed there.

**What's open, in the researcher's own words:** *"I am not sure if we should move IBA away from a
separate branch and incorporate it into the main project."* This is not answered here. Two
scenarios, sketched so the choice is concrete rather than abstract:

- **If `iba/` stays a separate branch:** its raw-data/analytics content still moves out (per v3,
  already settled), but its *processing* content (`iba/docs/`, `iba/app/reports/`, `iba/config/`)
  stays under `iba/` as `iba/`'s own local processing area — mirroring the main project's
  `Sessions/processing/` shape without merging into it.
- **If `iba/` incorporates into the main project:** `iba/docs/` folds into `Sessions/processing/`
  alongside `Workflow/methodology/`; `iba/app/reports/` folds into `Sessions/processing/reports/`
  alongside `outputs/reports/`; `iba/config/` either folds in too or is retired outright (it's
  already an unused, not-yet-loadable design per `GOVERNANCE.md` §6, a separate question from where
  it's filed). This is the larger move, and it touches live code paths (`iba/app/*.py` reads
  `iba/app/db/`, `iba/app/config/` by relative path throughout) — a real engineering change, not a
  file-management one, if it goes this way.

## 3. Proposed shape (Processing branch, both scenarios drawn)

```
Sessions/processing/
├── methodology/        <- Workflow/Instructions, Global_rules, methodology, Catalogue, reference,
│                          registry, schema, Sciences, Tiers, Sessionlogs, Programme, Chat_responses,
│                          Claude_API, docs/, research/investigations/
│                          [if IBA incorporates:] + iba/docs/
├── reports/             <- outputs/markdown, integrity, archive, projections, reports;
│                          database/archive/file_manifest.json
│                          [if IBA incorporates:] + iba/app/reports/
├── patches/             <- Sessions/Patches/, archive/patches/  (carried from v1/v2, unchanged)
└── escalations/         <- iba/app/reports/'s escalation-history files specifically, if kept as
                            its own numeric-id-keyed bucket rather than folded into reports/ generally
```

## 4. Open questions, running total across the whole design (v1–v4)

1. `Sessions-v2` vs. `Session_Clusters` (Analytics, cluster generations) — unresolved.
2. The two `verse-analysis` trees (Analytics, book-key generations) — unresolved.
3. `prose.detail_design`/`Findings`/`Essays` export timing (Raw Data / Analytics) — unresolved.
4. 137 `book_label`-less prose rows sorting into none of the three branches — unresolved.
5. **Whether `iba/` stays a separate branch or incorporates into the main project** — the largest
   open question in the whole design, named but not decided here, per the researcher's own stated
   uncertainty. Everything in §3 above is drawn both ways rather than picking one.
