# Consolidated project structure — v5: two root branches, no wrapper, phased execution

Prepared for escalation #933. Two corrections from the researcher this round:

1. **No `Sessions/` wrapper.** *"why do we need a sessions folder on the root. we literally have
   two main branches on the root - raw data and analytics."* Agreed, and for a further reason
   beyond simplicity: `Sessions/` is also the retired pipeline's own name
   (`Sessions/Session_A`–`_D`, `Session_Clusters`) — keeping it as the new wrapper's name would
   reintroduce the exact terminology this whole redesign has been retiring. `raw-data/` and
   `analytics/` become root-level folders directly, not children of anything.
2. **Two-phase execution.** Phase 1: move raw data and analytics (v1–v3's content, now re-rooted
   per below). Phase 2, separately: operations/processing files (v4's content, including the
   IBA-merge question) — not attempted in the same pass as phase 1.

Still a design only for phase 1's shape — nothing moved yet. `#929` v2 stays the untouched
reference.

## 1. Phase 1 shape (raw data + analytics, the only thing this phase touches)

```
raw-data/
└── by-word/{word}/       <- Sessions/Session_A/, _B/, _C/, _D/ (1,445 files, moved whole)
                          <- research/discovery/{NNN}_{word}_step_data_*.{json,md} (637 files)
                          <- prose.detail_design DB exports (169 rows, export task, not a move)

analytics/
├── by-cluster/{M-code}-{Name}/   <- Sessions-v2/ (641), Sessions/Session_Clusters/ (2,006),
│                                    Workflow/Clusters/ (33), archive/Clusters/ (86)
├── by-book/{book}/                <- verse-analysis/{book}/ (2,835), iba/app/verse-analysis/
│                                     {book}/ (308)
├── verse/                         (placeholder -- not a real file location today, see v2 sec4)
├── passage/                       (placeholder, same caveat)
├── prose-findings/                (583 DB rows, export task)
├── prose-essay/                   (9 DB rows, export task)
└── prose-concordance/             (0 rows, not built)
```

Everything else from v4 (`methodology/`, `reports/`, `patches/`, `escalations/`, the technology-
driven root folders, the IBA-merge question) is **phase 2** — named, not touched, not designed
further in this pass.

## 2. What phase 1 alone still leaves open

The same generation/duplication questions from v1–v3 are exactly what phase 1's actual execution
will have to resolve, since they sit inside the branches phase 1 touches:

1. `Sessions-v2` vs. `Session_Clusters` — two generations of the cluster baseline, which is current.
2. The two `verse-analysis` trees — two generations of the book baseline, same question.
3. `prose.detail_design`/`Findings`/`Essays` export timing — whether phase 1 also triggers
   exporting the DB-resident prose to files, or leaves those three sub-buckets as placeholders
   until a later pass.

`iba/app/verse-analysis/` (308 files) is the one piece of `iba/`'s content phase 1 already commits
to moving, regardless of the phase-2 IBA-merge question — it's raw-data/analytics content, and the
researcher's instruction that "all raw data and analytic files in IBA should move" already settled
that independent of whether `iba/` itself stays a separate branch or merges later.
