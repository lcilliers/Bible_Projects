# Consolidated project structure — v6: trimmed to what's actually being built now

Prepared for escalation #933. Small adjustment per the researcher: *"drop verse & passage from the
folder structure, we not creating placeholders for now... prose.detail_design/finding/essays will
already have files and will be overwritten in prose in due course. there is no need to export those
files now."* No placeholders for content that doesn't exist as files yet — the design now only
shows the two buckets with real files behind them today.

## Phase 1 shape, trimmed

```
raw-data/
└── by-word/{word}/       <- Sessions/Session_A/, _B/, _C/, _D/ (1,445 files)
                          <- research/discovery/{NNN}_{word}_step_data_*.{json,md} (637 files)

analytics/
├── by-cluster/{M-code}-{Name}/   <- Sessions-v2/ (641) + Sessions/Session_Clusters/ (2,006)
│                                    + Workflow/Clusters/ (33) + archive/Clusters/ (86)
│                                    -- pending the researcher's own file-level inspection to
│                                    decide how these combine into one structure
└── by-book/{book}/                <- verse-analysis/{book}/ (2,835) + iba/app/verse-analysis/
                                       {book}/ (308) -- same, pending the researcher's own inspection
```

`verse/`, `passage/`, `prose-findings/`, `prose-essay/`, `prose-concordance/` all removed — none
had real files behind them; they were placeholders for future export work that isn't happening
now, and a folder with nothing in it doesn't belong in the design.

## Status: holding for the researcher's own inspection

The researcher is going to look at the actual `Sessions-v2`/`Session_Clusters` files and the two
`verse-analysis` trees directly before any further design or action — the two "how do these
combine" questions v1–v5 kept surfacing as open aren't going to be resolved by more analysis from
this side; they need eyes on the actual file content. Nothing further attempted here until that
review happens.
