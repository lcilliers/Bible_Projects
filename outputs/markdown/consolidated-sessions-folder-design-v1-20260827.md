# A single consolidated `Sessions/` folder — design only, nothing moved

Prepared for escalation #933, building directly on the #929 v2 census (left untouched as the
reference baseline). **This is a proposal to look at, not an executed plan** — no file has moved.

## 1. The baselines actually found in the corpus

Going back through the v2 census with "what is this folder actually keyed on" as the question,
five real baselines emerge, plus two more that don't fit the cluster/book/word/verse set the
researcher recalled but are large enough to need their own place:

| baseline | what it's keyed on | current locations (with real file counts, from #929 v2) |
|---|---|---|
| **Cluster** | M-code (M01…M47, FLAG, T2) | `Sessions-v2/{code}-{Name}/` (641), `Sessions/Session_Clusters/{code}/` (**2,006** — the single largest holding in the project), `Workflow/Clusters/` (33), `archive/Clusters/` (86) |
| **Book** | one of the 66 biblical books | `verse-analysis/{book}/` (2,835, lowercase full names — `daniel`, `psalms`), `iba/app/verse-analysis/{book}/` (308, Title-Case/abbreviated — `1 Chronicles`, `1Cor`) — **two trees, same baseline, different key format** |
| **Word / registry** | one of the ~214 English inner-being words | `Sessions/Session_A/` (415), `Sessions/Session_B/` (974, currently organised by *pipeline stage* first and word second — see §3), `Sessions/Session_C/` (42), `Sessions/Session_D/` (14), `research/discovery/{NNN}_{word}_*` (637) |
| **Verse** | not actually its own top-level folder anywhere — it's the *grain inside* the book folders | `verse-analysis/{book}/readings/`, `/phase1-views/`, `/_seg/` all hold verse- or passage-level files *within* a book folder, not a separate cross-book verse index. If a cross-book verse baseline is wanted (e.g. "everything touching Gen 6:5, wherever it sits"), nothing today provides that view — it would be a new index, not a folder move. |
| **Escalation** (id) | a numeric escalation id | `iba/app/reports/{id}-escalation-history-*.md` (part of 466) |
| **Programme / method** | not word/book/cluster-scoped at all — governance, instructions, methodology | `Workflow/Instructions/`, `Global_rules/`, `Programme/`, `methodology/`, `Catalogue/`, `reference/`, `registry/`, `schema/`, `Sciences/`, `Tiers/`, `docs/`, `iba/docs/` (combined ~900+) |
| **Patches** | a database change, not a content baseline | `Sessions/Patches/`, `archive/patches/`, patch JSON mixed into `Workflow/Sessionlogs/` |

`research/investigations/` (380) and `outputs/*` (~319) don't key on any of the above cleanly
either — they're exploratory notes and one-off reports, cross-cutting by nature. `iba/app/config/`'s
CONFIG-REPORT snapshots (310) are IBA's own operational documentation, not really "analytic
content" — flagged as a judgement call, not folded in as if it obviously belongs.

## 2. Proposed single-folder shape

```
Sessions/
├── by-cluster/{M-code}-{Name}/
├── by-book/{book}/
├── by-word/{word}/
├── escalations/{id}/
├── programme/
├── patches/
├── research/
├── reports/
├── config-reports/                (flagged, see above -- may belong under iba/ instead)
└── archive/                        one shared archive, replacing the 4 different archiving
                                     shapes v2 §2 found (local sibling, tree-wide, project-root
                                     mirror, none at all)
```

## 3. What actually lands where — real examples, not every path

**`by-cluster/M01-Fear/`** would receive `Sessions-v2/M01-Fear/*` (106 files) directly, plus
`Sessions/Session_Clusters/M01/*` — but `Session_Clusters` holds **far more** (2,006 across all
clusters vs. `Sessions-v2`'s 641), and the two are not simply additive: they may be two different
generations of the same cluster's work (an earlier and a later pass), not two different kinds of
content. **Which one is current and which is superseded is not established anywhere today** — this
consolidation is the point at which that has to be decided, cluster by cluster, not assumed.

**`by-book/daniel/`** would receive `verse-analysis/daniel/*` (25 files) directly. Whether
`iba/app/verse-analysis/Daniel/*` (its Title-Case counterpart) merges into the same folder or
stays distinguishable depends on whether it's the same work under a different naming era, or a
genuinely separate later effort — again a real question, not a mechanical rename.

**`by-word/fear/`** would receive `Sessions/Session_A/*/fear*`, the relevant slices of
`Session_B/01_Verse_Context_Process_input/` through `12_Session_B_Status/` for that word,
`Session_C/*/fear*`, and `research/discovery/106_fear_step_data_*` (illustrative numbering) — this
is the baseline requiring the most re-slicing, since `Session_B` today is organised
stage-first/word-second (12 numbered folders, each containing every word's file for that stage),
and word-first/stage-second is the opposite cut.

**`escalations/920/`** would receive `iba/app/reports/920-escalation-history-*.md` — mechanical,
no ambiguity.

**`programme/`** would receive `Workflow/Instructions/`, `Global_rules/`, `Programme/`,
`methodology/`, `docs/`, `iba/docs/` more or less as-is — the least contested bucket, since none of
it is word/cluster/book-keyed to begin with.

## 4. Open questions this design surfaces, not resolves

1. **`Sessions-v2` vs. `Session_Clusters`** — same baseline (cluster), very different volumes. Is
   one simply superseded by the other? If so, the smaller or the larger one being current isn't
   obvious from file count alone.
2. **Two `verse-analysis` trees, two naming eras** — merge, or keep as two generations under one
   book folder (e.g. `by-book/daniel/{gen1,gen2}/`)?
3. **`Session_B`'s stage-first organisation** doesn't cut cleanly into a word-first bucket without
   real re-slicing work, not a folder move.
4. **Should config-reports (`iba/app/config/`) count as "analytic files" at all**, or stay
   IBA-operational and out of scope of this consolidation?
5. **No existing verse-level cross-book index** — if a true "verse" baseline is wanted (not just
   verse-content living inside a book folder), that's new work, not a move.

None of these five are answered here — each is a real decision the researcher is better placed to
make than a file count is.
