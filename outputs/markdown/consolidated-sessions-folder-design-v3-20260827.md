# A single consolidated `Sessions/` folder — v3: three branches (Processing / Raw Data / Analytics)

Prepared for escalation #933. Supersedes v2 per the researcher's refinement: *"The current book
'Detail Design' is in effect the Raw Data... prose.detail_design goes to a separate main branch
for Raw Data... findings, essays, concordance all go the analytics branch. And all the underlying
files associated with this broad grouping flow together."* Still a design only — nothing moved.
`#929` v2 stays the untouched reference.

## 1. Three branches, not two

| branch | `prose_section_type.book_label` | live rows | what it holds |
|---|---|---|---|
| **Processing** | `Programme` | 51 | governance/method: escalations, methodology, instructions, process-focused investigations, database/table management, patches, config, and `prose.programme` itself (this document set's own Chapters 4–6) |
| **Raw Data** | `Detail design` | 169 | the working/intermediate material a finding is built *from* — STEP extracts, lexical data, and now, per this refinement, `prose.detail_design`'s own prose output too, because that prose is itself a description of raw material, not a refined result |
| **Analytics** | `Findings`, `Essays`, `Concordance` | 583 / 9 / 0 | the refined, reader-facing research output — cluster, book, verse, and passage groupings of findings, essays, and the not-yet-built concordance |

This resolves the exact difficulty v2 flagged and could not cleanly answer: whether
`Sessions/Session_A`–`_D` (1,445 files) should split between processing and raw-data file by file.
It doesn't split — **the whole of Session A–D moves into Raw Data as one thing**, because its
content (STEP extracts *and* the per-word technical/analysis-stage prose alike) is exactly what
`Detail design` = Raw Data now means.

## 2. Proposed shape

```
Sessions/
├── processing/            (not designed this round -- named only, per the researcher's own
│                           sequencing: results/findings-side work first)
│
├── raw-data/
│   └── by-word/{word}/    <- Sessions/Session_A/, _B/, _C/, _D/ (1,445 files, moved WHOLE,
│                              no internal splitting -- v2's flagged difficulty is resolved)
│                           <- research/discovery/{NNN}_{word}_step_data_*.{json,md} (637 files)
│                           <- prose.detail_design DB exports (169 rows -- not yet extracted to
│                              files anywhere; an export task, not a move, same caveat as v2)
│
└── analytics/
    ├── by-cluster/{M-code}-{Name}/   <- Sessions-v2/ (641), Sessions/Session_Clusters/ (2,006),
    │                                    Workflow/Clusters/ (33), archive/Clusters/ (86)
    ├── by-book/{book}/                <- verse-analysis/{book}/ (2,835), iba/app/verse-analysis/
    │                                    {book}/ (308)
    ├── verse/                         (placeholder -- see v2 sec4, unchanged: not a real file
    │                                    location today, lives inside by-book/ or only in iba.db)
    ├── passage/                       (placeholder, same caveat)
    ├── prose-findings/                (583 DB rows, not yet extracted to files)
    └── prose-essay/                   (9 DB rows, not yet extracted to files)
        prose-concordance/             (0 rows, not built)
```

## 3. What this changes from v2, concretely

- **Session_A–D** (1,445 files): v2 called this the hardest case, needing real re-sorting between
  processing and raw-data content mixed in the same folders. v3 resolves it — all of it is Raw Data
  now, moved as whole folders.
- **`research/discovery/`** (637 files): unchanged from v2 — raw STEP pulls, Raw Data, same as before.
- **Cluster/book groupings**: unchanged from v2 in substance, just re-homed under `analytics/`
  instead of a flat `by-cluster`/`by-book` at the results root — the same two open questions carry
  over unresolved (`Sessions-v2` vs. `Session_Clusters` generations; the two `verse-analysis` book-
  naming eras).
- **`verse`/`passage`**: unchanged — still not real file locations, still placeholders.
- **`prose.programme`**: unchanged in substance (Processing, undesigned this round) — now explicitly
  anchored to the same live `book_label` mechanism as the other three, rather than described only
  by example.

## 4. Open questions, updated

1. `Sessions-v2` vs. `Session_Clusters` — same as v1/v2, unresolved.
2. The two `verse-analysis` trees — same as v1/v2, unresolved.
3. Whether `prose.detail_design`'s 169 DB rows, and the 583/9 `Findings`/`Essays` rows, get
   exported to files as part of this consolidation, or stay DB-only with the folder structure
   waiting for them — an export-timing decision, not a mapping one.
4. The 137 prose rows with no `book_label` at all still don't sort into any of the three branches
   as things stand — naming this again since v3 doesn't change it.

`processing/` remains intentionally undesigned — the researcher's own sequencing puts it after this
branch, not before.
