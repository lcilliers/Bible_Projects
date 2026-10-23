# 2228 — Scope resolver: design (v1)

Escalation: #2228 v13. Status: design for your review; nothing is built (rule 105). This is tool 1 of
`outputs/escalation/2228-discovery-scope-and-known-v3-20261022.md` section 3. Facts are from
read-only checks of `iba/app/db/iba.db` and the code, 2026-10-22.

**What it does.** It takes any request and returns the collection of verses as a JSON file. It
reads only and writes no table. Later tools (the known-for-verses pack, the gap report and the
neighbour-verse review) call it as their first step, so every analysis starts from the same
collection.

---

## 1. The request

A request is one or more **selectors**, which add verses, and optional **filters**, which narrow
them. The selectors are combined as a union: a verse is in if any selector brings it in. Each
selector is given on the command line or, for long lists such as a batch, in a request file.

| Selector | Example | Resolves through | Notes |
|---|---|---|---|
| Cluster | `-Cluster M02` | `cluster_strong` (live rows) → `verse_lexical.strong` | One query for any number of clusters. M25 Life and death: 2,027 verses in 0.02 s. |
| Subgroup of a cluster | `-Subgroup <subgroup_code>` | `cluster_subgroup` → `cluster_subgroup_strong` → as for strongs | 13 subgroups exist today |
| Strand | `-Strand anger` | `reading_strand_strong` → as for strongs | A strand's word family |
| Word | `-Word anger` | `word_registry` → `word_strong` → as for strongs | |
| Strong | `-Strong "H0430,G3563G"` | `verse_lexical.strong`, exact code | **A bare code is decomposed to every derivative that occurs** (H0430 → H0430G, H0430H, …), by your rule (#2233). A suffixed code is taken as it is. A code that occurs nowhere is an error that names it and suggests the derivatives. |
| Verse | `-Verse "Psa 10:2; Luk 14:12-14; Rom 8"` | the existing reference parser, `narrativeregister.parse_refs` | Lists, ranges, ranges across chapters and whole chapters |
| Narrative chapter or block | `-Chapter 13` or `-Chapter 10.1 -Section "The bosom"` | `narrative_citation` (current rows) of the chapter's current blocks, or of the one block | The block is addressed as Narrative-Register.ps1 addresses it: by chapter number and heading. |
| Claim | `-Claim C-330` | `narrative_claim_source` (verse rows) | |
| Observation | `-Observation 12478` | `ib_node.verse_reference` | |
| Thread item, or a whole thread | `-Item OT-108.3` or `-Thread OT-108` | the item's kind: `verse`, `cluster`, `strong`, `chapter` or `strand`, each resolved as above | A whole thread is the union of its open items. The kinds `escalation`, `event` and `researcher` name no verse; they are reported, not resolved. |
| Request file | `-File request.json` | the same keys as above, as lists | For a batch or a long hand-picked list, so a group can be kept and re-run as it is |

**Filter: only some derivatives.** `-OnlyStrong "H3708A,H0639"` keeps only the verses in which one of
these codes occurs. This is the focus on a subset of the derivatives that you described. No other
filter is proposed.

**What it does not do: pull in verses through a narrative or claim.** A chapter, block or claim
gives only the verses it cites. Whether to pull in other verses is your judgement call, made in the
neighbour-verse review (tool 6), not by this tool.

## 2. The answer (JSON)

```json
{
  "request":  { "cluster": ["M02"], "only_strong": ["H3708A"] },
  "label":    "anger-bosom",
  "run_id":   "RUN-…-VERSESCOPE",
  "resolved_at": "2026-10-22T…Z",
  "selectors": [
    { "kind": "cluster", "value": "M02", "name": "Anger and wrath",
      "strongs": [ { "code": "H0639", "sense": "anger" } ], "verses": 681 }
  ],
  "verses": [
    { "verse_id": 17321, "osis": "Eccl.7.9", "reference": "Ecc 7:9",
      "routes": [ { "kind": "cluster", "value": "M02", "via": "H3708A" } ] }
  ],
  "not_resolved": [
    { "kind": "verse", "value": "Neh 7:63", "reason": "no verse row (by design: governance.verse_gap_by_design)" },
    { "kind": "item",  "value": "OT-108.15", "reason": "kind 'event' names no verse" }
  ],
  "counts": { "verses": 1, "selectors": 1, "not_resolved": 2 }
}
```

- **Every verse says why it is in (`routes`).** A verse brought in by two selectors carries both
  routes.
- **Codes are never shown bare:** a cluster carries its name and a strong its sense
  (`strong_sense.head`), by rule 100.
- **Nothing is dropped silently.** A reference with no verse row, a whole chapter the book does not
  have, a thread item with no verse, or a block that cites no verse is listed under `not_resolved`.
  A missing verse row is not an error (`governance.verse_gap_by_design`).
- **Verses are listed in canonical order** (`cfg_book_order`).
- **An empty result is an answer, not a failure:** zero verses, with the reasons.

**Where the file goes:** `outputs/verse-scope/<label>-v{n}-<YYYYMMDD>.json`, through the existing
versioned writer (`filingkit.versioned_path`, given the folder). A same-day re-run bumps `v{n}` and archives the earlier
version. The folder is a new setting, `verse_scope.output_dir`. The run also prints a one-line count
per selector. The JSON is the result; the console carries no content.

## 3. How it is built (inside the app)

| Part | What | Path |
|---|---|---|
| Library | `resolve(cfg, request) -> dict`: one function per selector kind, each a single set-based query (rule 71), returning `(verse_id, route)` rows. Reuses `parse_refs`/`VerseIndex` and the thread item kinds as `escalation.match_open_items` reads them. `lexicalscope.py` is not reused for strongs, because it scans all 378,182 `span` rows; the indexed `verse_lexical.strong` gives the same verses. | `iba/app/lib/versescope.py` |
| Handler | one step, `verse_scope.resolve`; writes the JSON and returns its path | `iba/app/handlers/versescope.py` |
| Entry point | `Verse-Scope.ps1 -Label <name> [selectors] [-OnlyStrong …] [-File …]`, through `run.py` as every tool does | `iba/app/ps/Verse-Scope.ps1` |
| Config | `cfg_utility` (library and handler), `cfg_work_package` `verse-scope`, `cfg_step` `verse_scope.resolve`, `cfg_setting` `verse_scope.output_dir`. No write grant: it writes no table. | through `apply_logged` |
| Documents | USER-GUIDE.md (how to run it), BUILD.md (the build record), the PS tools worksheet (new script, rule `governance.ps_worksheet_sync_on_change`). GOVERNANCE.md is not touched, because no new kind of config is added. | |

Before the build: #2233 (the bare-strong rule as a config row). The resolver implements that rule
and its docstring points to the row.

## 4. Test plan (run on a copy made with `dbsnapshot.copy_db`; results on #2228)

| # | Case | Expected |
|---|---|---|
| 1 | `-Cluster M25` | 2,027 verses; each route names a strong of M25 |
| 2 | Two clusters | the union; a verse in both carries two routes |
| 3 | `-Strong H0430` (bare) | every H0430 derivative in `verse_lexical`; the JSON lists them |
| 4 | `-Strong H0430H` (suffixed) | only that code |
| 5 | `-Strong H9999` (occurs nowhere) | an error naming it; no file |
| 6 | `-Cluster M02 -OnlyStrong H3708A` | only the verses holding H3708A |
| 7 | `-Verse "Rom 8"`, a range across chapters, a list | the right verse ids, in canonical order |
| 8 | A verse with no verse row | listed in `not_resolved` with the by-design reason |
| 9 | `-Chapter 13` and one block by heading | the cited verses of the current blocks only; a block with no citation reported |
| 10 | `-Claim` on a claim with a study-file source only | zero verses, with the reason |
| 11 | `-Observation` on one of the 63 with no node | zero verses, with the reason |
| 12 | `-Thread OT-108` | the union of its open verse, cluster, strong, chapter and strand items; event and researcher items reported |
| 13 | `-Strand`, `-Subgroup`, `-Word` | the word family's verses |
| 14 | `-File` with the same request as test 6 | the same verses as test 6 |
| 15 | Same label twice in a day | v1 is archived and v2 is written |
| 16 | Read-only | the copy's tables are unchanged (row counts before and after) |
| 17 | Speed | every case returns within seconds |

## 5. What is not in this design

- **Reading the verses' content** (observations, claims, files): that is the known-for-verses pack.
- **The cluster reading index:** a later design.
- **Keeping a collection as a named row in the database:** the request file plays that part.
  Proposed only if the later tools need it.
- **D1 of discovery v3** is still open (see chat). It concerns the gap report, not this tool.

## Decision for you

| # | Question | Your choice | Comment |
|---|---|---|---|
| R1 | Approve this design for the build (after #2233)? | | |
| R2 | The request file (`-File`) as the way to keep a group or batch, rather than a table of named collections? | | |
