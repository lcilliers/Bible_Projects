# M08 (Pride) — folder inventory + DB extract — 2026-08-28

> Escalation #1005. First book/cluster of the "explore existing cluster work" assessment. Summarises
> what's physically in `_analytics/clusters/M08-Pride/` and pulls everything the DB (`bible_research.db`
> = analysis/findings, `iba.db` = base data) holds about `cluster_code='M08'`. Raw DB rows also
> written as JSON alongside this file: [`Data/wa-m08-db-extract-v1-20260828.json`](Data/wa-m08-db-extract-v1-20260828.json).
> All files for this assessment are filed in this folder, per instruction — nothing written elsewhere.

## 1. Folder inventory — `_analytics/clusters/M08-Pride/` (172 files)

Five top-level areas, plus one loose file:

| area | files | date range | what it is |
|---|---|---|---|
| `Data/` | 2 | 2026-06-21 | VE-lexical raw extract (2-part JSON batch) — base data, not analysis |
| `M08/` | ~140 | 2026-05-05 → 2026-06-03 | the old phase-based cluster pipeline (Session B/C/D era) — the bulk of the folder |
| `essays/` | 3 | 2026-06-21 | published essay (md/docx/pdf) |
| `findings/` | 20 | 2026-06-21 | a second, later, differently-structured findings pass |
| (loose, root) | 1 | 2026-05-13 | `wa-m08-pride-scienceextract-v1_0-20260513.md` — earliest file in the folder |

### 1a. `M08/` — the phase-based pipeline (2026-05-05 to 2026-06-03)

An 11-phase pipeline, fully represented in the file names themselves: Phase 1 (UT/verse review) →
Phase 3 (constitution/constitution-debate) → Phase 4 (co-occurrence) → Phase 5 (sub-group
design/distribution-validation, 2 revisions) → Phase 7 (VCG design) → Phase 8.5 (boundary
resolution — logged directly in the DB, see §2c) → Phase 9 (per-characteristic findings +
cluster-synthesis) → Phase 10 (closure record) → Phase 11 (validation). Also: 5 numbered
directives (`dir-001` term-transfer through `dir-005` boundary-resolution), 4 iterations of a
"detail" spec (v1–v4, the earliest dated content in the folder, 2026-05-05 to 05-08), API raw
response logs (`passa-`, `UT-`), and later additions (`a6a7`, `b7-citation-extension`,
`comment-eval-applyspec`, `d1-exclude`, `pointer-dispositions`, all 2026-06-02/03 — a distinct,
later touch-up round on top of the May work).

Sub-folders inside `M08/` largely **duplicate each other at different snapshot points** — `files
phase 5` and `files phase 5 a` (v1 vs v2 of the same sub-group design), `files phase 7` and `files
phase 9 all files` (the same VCG-design set re-appearing), and `files phase 9` which is the
**cleanest, final version** of the Phase 9 output: 5 characteristic-findings files + a
cluster-synthesis findings file + a cluster-synthesis appendix, with one explicitly superseded file
moved to its own `archive/` (`...char1-...findings-v1-OLD-DISCIPLINE-20260521.md` — the researcher's
own prior discipline-correction, already self-documented in-folder). `inputs/` holds the 10
chapter/appendix input files feeding the essay. `publishing/` holds the finished essay (2026-05-27).

**This whole tier is thoroughly cross-checked against the DB (§2) — nothing here is orphaned.**
Every phase/characteristic/sub-group named in the files has a corresponding, matching DB row.

### 1b. `findings/` — the later, differently-structured pass (2026-06-21)

20 files, all dated the same day as `Data/`'s VE-lexical extract. Structured around **7
letter-coded sub-groups (a, b, c1, c2, d, e, f)** — a different partition from `M08/`'s
5-characteristic / 8-subgroup (A1–A4, B, C, D, E) structure. Each sub-group has a findings file
plus a paired "tier-answers" file (`wa-m08-a-self-exaltation-v1_0`, `wa-m08-a-tier-answers-v1_0`,
etc.), plus a findings-audit, a cluster-synthesis, a `prov-char-list` (the source for a *second* set
of characteristic definitions — see §2b), a session-log tier-synthesis, a set-asides file, and an
observation log. **This is the source of `characteristic` ids 185–191** (§2b) — a second
characteristic set for M08 that was never reconciled with the first.

## 2. DB extract — `cluster_code='M08'`

Full raw rows in [`Data/wa-m08-db-extract-v1-20260828.json`](Data/wa-m08-db-extract-v1-20260828.json).
Summary:

### 2a. `cluster` row (both DBs agree)

`M08` = "Pride" / "Pride, Arrogance and Boasting" · `status='Analysis Completed'` · `version='v6'`
· `bucket='NAMED'` · `source='meaning_v2'` · last updated `2026-05-21`. Full gloss carries 47
Hebrew/Greek headword entries. `iba.db`'s own `cluster` row (migrated 2026-08-11) matches exactly.

### 2b. `characteristic` — 12 rows, two unreconciled eras

| era | ids | char_seq | count | source |
|---|---|---|---|---|
| Old (May, matches `M08/`) | 14–18 | 1–5 | 5 | `WA-M08-subgroup-design-v2-20260520.md` + constitution-debate + boundary-resolution |
| New (June, matches `findings/`) | 185–191 | 101–107 | 7 | `wa-m08-prov-char-list-v1_1-20260621.md` |

**Old set (1–5):** Arrogant self-elevation · Presumptuous defiance · Boasting and self-display ·
Vain conceit · Pride of power and position. Each carries a full multi-sentence definition and a
provenance chain across 3 named source files.

**New set (101–107):** A-Self-exaltation · B-Settled pride · C1-Presumption/defiance toward God
and authority · C2-Insolence/contempt toward others · D-Boasting and glorying (two poles) ·
E-Conceit/being puffed-up · F-Self-love/self-sufficiency. Shorter, single-line definitions.

**Both sets are live (`delete_flagged=0` on every row) — nothing marks one as superseding the
other.** The overlap is substantial in content (old CHAR-1 "Arrogant self-elevation" ≈ new A+B; old
CHAR-2 "Presumptuous defiance" ≈ new C1; old CHAR-3 "Boasting" ≈ new D; old CHAR-4 "Vain conceit"
≈ new E) but the new set also splits what the old set treated as one register (C1 vs C2 —
God/authority-directed vs neighbour-directed contempt) and adds one the old set didn't separate out
(F, self-love/self-sufficiency, though the old M08-A4 sub-group's `filautos` term already covered
this ground as part of a broader "general dispositional" bucket). **Reconciling these two sets is
the single largest open item this assessment surfaces.**

### 2c. `cluster_subgroup` / `characteristic_subgroup` — 9 rows (old set only), fully documented

8 active + 1 correctly soft-deleted (`M08-BOUNDARY`, dissolved 2026-05-21 with a clean resolution
note: its one term, G0193 *akratēs*, was promoted into `M08-A4`). The 8 active sub-groups split
CHAR-1 four ways by "seat of pride" (heart / eyes-and-outward-bearing / national-collective /
general-dispositional) and give CHAR-2 through CHAR-5 one sub-group each. Every sub-group carries a
real verse-grounded `core_description` (specific references named, e.g. Deu 8:14, Isa 2:11, Eze
28:2) — this is genuine textual analysis, not placeholder scaffolding.

### 2d. `cluster_observation` — 5 rows, all `status='confirmed'`, all resolved same-day-to-Phase-9

This is the strongest evidence of disciplined method in the old-era work:

1. **CHAR-1's 4-way volume-split** (151/293 = 51.5% of the cluster) — explicit rule citation
   (v2_8 §8.0 rule 2), confirmed against Phase 9 output with exact totals (165 E + 20 S + 4 G).
2. **M08-C ↔ M22 (praise/glory) register-adjacency** — the *same* Greek vocabulary
   (`kauchaomai`/`ha.lal`) expresses both self-boasting (M08) and God-directed glorying (M22),
   distinguished at verse level, not lexeme level. Flagged for M22 to pick up when it opens.
3. **M08-E ↔ M23 (strength/dominion) misuse-of-faculty pairing** — M08-E's terms carry their
   *primary* register in M23; they stay in M08 because their specific verses show the faculty
   turned to self-exaltation. Same cross-cluster hand-off logic as #2.
4. **Phase 5.5 set-aside of 174 verses** (122 M22-register + 52 narrative/neutral) — a documented,
   reasoned exclusion, not silent data loss: corpus reduced 470 → 296 → 293 substantive verses,
   with the excluded verses named as recoverable for M22 later.
5. **Phase 8.5 BOUNDARY resolution** — the G0193 promotion decision (§2c), with the full
   researcher-decision rationale recorded.

**Every one of these 5 observations is exactly the kind of cross-cluster linkage and disciplined
verse-accounting the researcher named as the deciding factor for "is this worth harvesting."** They
also point forward directly at M22 and M23 — both currently "Not started" per the earlier
stream-robustness assessment.

### 2e. `cluster_finding` — 1,134 rows (1,038 live, 96 deleted; **~91.5% retention** — much better
than the base per-verse `finding` table's project-wide ~8% retention)

| finding_status | live | deleted |
|---|---|---|
| finding | 747 | 40 |
| cluster_synthesis | 173 | 16 |
| silent | 114 | 27 |
| gap | 4 | 13 |

`silent` entries are catalogue questions explicitly answered "no evidence" rather than skipped —
another discipline signal (absence recorded, not just omitted).

### 2f. `finding` (base per-verse table) — 679 live rows for M08, all `level=VERSE`,
`finding_status=ANSWERED`, `provenance='l2_meaning'`

**Caution for anyone reusing the earlier stream-robustness numbers:** this 679 is NOT the
hand-authored analytical content (that's §2e, `cluster_finding`) — it's the base meaning-parse
layer. Don't conflate the two when judging how much real analysis M08 carries.

### 2g. `iba.db` base-data cross-check

`cluster_strong` (`iba.db`): **87 distinct strongs tagged M08**, of which **66 carry a
`word_registry` link and 21 don't** — the same registry-gap pattern quantified project-wide
earlier this session, present here at cluster scale too.

## 3. What this means for the harvest assessment (not decided here)

- **The old-era (`M08/`, May 2026) work is genuinely disciplined**: reasoned verse set-asides,
  confirmed cross-cluster observations pointing at specific future clusters, a real audit trail
  from raise to Phase-9 resolution, an already-self-corrected "OLD-DISCIPLINE" file archived in
  place. This is strong, concrete support for the researcher's ">50% has value" instinct — for
  this cluster, in this era, the fraction looks considerably higher than 50%.
- **The two characteristic sets (§2b) were never reconciled** — this is the one clear defect, and
  it's a scoping/consolidation task, not a quality problem with either set individually.
- **Two of the five cluster_observations are literally instructions to future clusters (M22, M23)**
  — harvesting M08 properly means those two clusters inherit real, already-worked cross-references
  when they open, not a cost sunk only in M08 itself.
