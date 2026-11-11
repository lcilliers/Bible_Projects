# #2477 Collection evidence report: plan for an intelligent report

Researcher instruction (2026-11-11): an intelligent report; the CSV becomes an Excel workbook with each listing as its own sheet; the Markdown fixes all the problems found and builds the collection extract up so that no list stands without saying what it is listed for.

Code: `iba/app/lib/collectionevidence.py` (builder and renderer), `iba/app/handlers/collectionbuild.py` (Evidence action, file writing), `iba/app/ps/Collection-Build.ps1` (parameters). Output stays in `surfaces.exports_root` (rule B:128, #2475). No table is written; the report stays a view of stored rows.

## What is wrong now (from #2477), each with its fix

| # | Problem | Fix in the Markdown | Fix in the workbook |
|---|---|---|---|
| 1 | 1059 of 2461 observation headings are withdrawn and deleted, listed beside live ones; engagement work is buried | Live observations only in the body, grouped by stage (engagement first). Withdrawn ones are counted per stage, with the reason from `ib_observation_change`, in a closing section, not as cards | Sheet `Observations` (live), sheet `Withdrawn observations` (with reason) |
| 2 | Claims reached by verse are about humility, pride and anger, not the search words | Two groups: claims resting on an observation of these words (direct), and claims reached only because they cite a verse where a member word stands (by verse only). Each by-verse claim states the verse, the member word in it and its Strong's code, and is labelled as a claim about the verse, not about the collection | Sheet `Claims` with a `reaches by` column (observation or verse) and the verse and word that reached it |
| 3 | 30 of 169 `find` rows carry a Strong's code other than H4672 or G2147 (21 of them surface_kind shared) | Occurrences are grouped by Strong's code first. The codes whose stored lemma or STEP gloss is the member word are the main table; the other codes sit in a separate "shared surface" table headed by the stored `surface_kind`, the unit's word and the unit role. Nothing is judged; the split is by stored fields only | Sheet `Occurrences` with a `kind` column; sheet `Strong's codes` |
| 4 | Faults list 1113 live nodes on deleted observations as node ids only | Each fault is a short table: node, observation, observation status, the verse and word, with a one-line statement of what the rule found; counts first | Sheet `Faults`, one row per finding with these columns |
| 5 | Phrases (tier phrase) are absent from the report | A "Phrases" section: each phrase, the route that attached it (strong or english, from the link reason, with the researcher quotation cut), and whether it has any observation. Stated as not members | Sheet `Phrases` |
| 6 | 3.6 MB, 38195 lines; a lookup, not a read | The Markdown holds the argument of the collection; the repeated detail (Strong's trees, LSJ, Mounce, cluster tables, change history, verse-by-verse node lists) moves to the workbook and is cited by sheet name | The workbook holds every row, one sheet per listing |

## Markdown structure (each part says what it is listed for)

1. **What this report is and how to read it**: scope, the tiers that count as members, the sheets of the workbook, what is not in the report.
2. **The collection at a glance**: members by Strong's code (the Hebrew or Greek words behind the English surfaces), with occurrences, verses and engagement counts in one table, so the reader sees what the collection stands on before anything else.
3. **Each base word (Strong's code) in turn**: its meaning in one paragraph (STEP gloss, sense head, first level of the meaning tree, related terms); its occurrences in Scripture order with the verse text once and the member word marked; then what was recorded for those occurrences: the engagement verdict (silence or use, with its reasoning), other live observations, and the claims.
4. **Where the collection stands in the study**: occurrences with and without engagement; live observations by stage and status; claims direct and by verse; the narrative sections that tell them.
5. **Claims and the narrative**: direct claims with their sections; by-verse claims, labelled; the telling of each.
6. **Phrases attached to the collection.**
7. **Stored-data faults** (problem 4) and the **withdrawn-observation account** (problem 1).
8. **Sources**: the joins in words, and the tables read with the meaning recorded in `cfg_table` and `cfg_column`.

## Excel workbook

One file, `collection-evidence-<name>-v<n>-<yyyymmdd>.xlsx`, written with `openpyxl` (installed, 3.1.5). Sheets: `Read me` (what each sheet lists and why, its source tables, counts, generated stamp), `Collection`, `Links`, `Members`, `Occurrences`, `Strong's codes`, `Meaning trees`, `Related terms`, `LSJ and Mounce`, `Cluster assignments`, `Placements`, `Observations`, `Observation nodes`, `Withdrawn observations`, `Change history`, `Claims`, `Claim sources`, `Narrative`, `Phrases`, `Faults`. Header row frozen, filters on, widths set. The CSV is removed: the Evidence action writes the .md and the .xlsx, and the CSV writer and header constants go. The earlier CSV files stay in the archive folder.

## Settings and documents

The name and version come from `collection.evidence_name` and the filing rule as now; the `.csv` handling in `collectionbuild.py` becomes `.xlsx`. USER-GUIDE.md (Collection-Build Evidence), the help text of `Collection-Build.ps1` and BUILD.md are updated (E:12, `governance.build_md_on_code_change`). The manifest is rebuilt after the files are written.

## Test

Build the report for `search`, and for one verse list. Check against direct queries of the tables: every sheet's row count equals the count of the stored rows it lists; every live observation of the scope appears once; the withdrawn observations are counted equal to the 1059 found; no withdrawn card is in the body; the 30 rows with a code other than H4672 or G2147 appear in the shared table; each by-verse claim shows its reaching verse and word; the Markdown size is reported against 3.6 MB. The actual counts are reported (B:24).

## Defaults I have chosen (say if you want any different)

- A by-verse claim stays in the report, labelled, so nothing stored is hidden.
- The own-versus-shared split uses stored fields only, never a judgement that a code is an error.
- Strong's entries keep every stored item, in the workbook; the Markdown carries one paragraph per code.
- The CSV is removed outright, not kept beside the workbook.
