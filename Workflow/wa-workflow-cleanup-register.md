# Workflow folder cleanup — disposition register

> **Living document · Doc version: 1 · Last updated: 2026-06-04.**
> **Purpose:** go through every `Workflow/` subfolder and reduce each to **only the final
> authoritative version(s)**, archiving the rest (move → `archive/`, never delete; manifest-indexed,
> fully recoverable). One row per file. CC executes the **CLEAR** archives; **DECISION** rows are held
> for the researcher's markup (mark `keep` / `archive` / `relocate→…` in the Decision column).
> Reversible by design — `git log --follow` + the archive subfolders preserve everything.

**Disposition key:** `KEEP` = stays as authoritative · `ARCHIVE` = moved to the folder's `archive/`
(superseded/historical) · `DECISION` = needs your call before I move it.

---

## Workflow/Tiers/  — DONE (clear archives) · 3 decisions held

**Context:** the catalogue ground truth is the database (`wa_obs_question_catalogue`). The fresh
DB extract is therefore the single authoritative catalogue; every prior markdown/JSON render of the
catalogue, plus the tier-debate logs and tier-definition drafts, are superseded or historical.

### Kept (authoritative)
| File | Why |
|---|---|
| `wa-tier-questions-extract-v1-20260604.md` | **The** authoritative catalogue — 189 tier questions pulled live from the DB (schema 3.28.0). |

### Archived (CLEAR — moved to `Tiers/archive/`)
| File | Why superseded |
|---|---|
| `wa-obs-catalogue-tiered-v2_1-20260513.md` | Prior tiered-catalogue render (schema 3.21.0) — superseded by the 2026-06-04 DB extract. |
| `wa-obs-question-catalogue-extract-20260419.md` | Pre-tier full extract (194 Q, deleted=0) — superseded. |
| `wa-obs-catalogue-generic-v1-20260426.json` | Pre-tier generic source JSON (147 Q) — superseded by the tiered DB catalogue. *(the file you had open)* |
| `wa-obs-catalogue-with-links-20260416.json` | Old catalogue-with-links JSON — superseded. |
| `WA-obs-catalogue-tier-classification-v1-2026-04-28.md` | First-pass tier classification, working doc — superseded by the live `tier`/`component` columns in the DB. |
| `WA-obs-framework-first-tier-v1_1-2026-04-29.md` | Precursor to the consolidated framework-definitions. |
| `WA-obs-framework-second-tier-prelim-v1-2026-04-29.md` | Preliminary, superseded. |
| `WA-obslog-t1-second-tier-prelim-v1-2026-04-28.md` | Prelim obslog. |
| `WA-tier-T1-definition-v1-2026-04-29.md` | Single-tier draft — folded into framework-definitions. |
| `WA-tier-T2-draft-v1-2026-04-29.md` | Single-tier draft — folded into framework-definitions. |
| `WA-session-log-tier-framework-debate-v1-2026-04-28.md` | Tier-debate session log (process history). |
| `WA-session-log-tier-debate-session2-v1-2026-04-29.md` | Tier-debate session log. |
| `WA-session-log-tier-debate-session3-v1-2026-04-29.md` | Tier-debate session log. |
| `WA-session-log-tier-debate-final-v1-2026-04-29.md` | Tier-debate session log (final). |
| `WA-prose-suggested-edits-v2-2026-04-29.md` | Not a catalogue — prose edit suggestions, applied/spent. |

### Decisions held (NOT yet moved)
| File | Question | Decision |
|---|---|---|
| `WA-tier-framework-definitions-v1_2-2026-04-29.md` | This is the current **prose definition of all 8 tiers** (title/scope/boundaries). You're rewriting tier definitions in §c of `wa-study-foundations.md` right now, which will supersede it. Archive it now, or **keep until §c is finalised** so you can consult it while writing? | _______ |
| `wa-tpopb-findings-catalogue-extract-20260416.json` | **Not a tier doc** — it's a findings-catalogue extract that happens to live here. Archive, or relocate to `research/investigations/`? | _______ |
| `wa-tpopc-btarget-flags-extract-20260416.json` | **Not a tier doc** — B-target flags extract. Archive, or relocate to `research/investigations/`? | _______ |

---

## Remaining Workflow subfolders — PROPOSED disposition (awaiting your markup)

> **Important finding:** these ten folders are **not** full of old versions — most hold a *single current
> version* of each governing doc. What clutters them is **working documents** (design notes, session logs,
> drafts, one-off analytics) sitting beside the authoritative references. So "archive the rest" is mostly a
> judgement about *which working docs are spent* — your call, not mine to guess on governing material.
>
> **What I auto-executed** (unambiguous only): 4 superseded schema snapshots + a `.bak` (schema/), a `.zip`
> + an `.html` dump (Sciences/). Everything below is **PROPOSED — nothing moved.** Mark each row
> `keep` / `archive` / `relocate→…` and I'll sweep them in one pass.

### `schema/`  — DONE (clear) + 2 decisions
- **KEEP:** `create_tables.sql` · `database-schema-v3.17.0-20260427.json` (newest snapshot on disk).
- **Archived (clear):** `database-schema-v3.10.0`, `-v3.11.0`, `-v3.14.0` (older snapshots) · `create_tables.sql.pre_DBR_bak`.
- **DECISION:** `ref-migration-m32-doc-sweep-20260420.md`, `ref-migration-m33-m35-doc-sweep-20260420.md` — historical migration notes. Archive? `____`
- **Note:** the newest on-disk snapshot is **3.17.0** but the live DB is **3.28.0** — all snapshots are stale. Want me to generate a fresh `database-schema-v3.28.0` snapshot? `____`

### `Sciences/`  — DONE (clear junk) + proposals
- **KEEP:** the **44** `wa-m{NN}-{word}-scienceextract-*` files (current per-cluster science pre-readings — actively required by Phase 9).
- **Archived (clear):** `files sience.zip` · `framework-b-discussion-soul-brain-ai.html`.
- **DECISION (working/log artefacts beside the references):**
  | File | Proposed | Decision |
  |---|---|---|
  | `Framework-B-SessionLog-2026-03-07.md` | archive (old session log) | `____` |
  | `wa-obslog-sci-extract-v1-20260513.md` | archive (obslog) | `____` |
  | `wa-sessionlog-sciextract-v1_0-20260513.md` | archive (session log) | `____` |
  | `wa-sessionlog-sciextract-final-v1_0-20260513.md` | archive (session log) | `____` |
  | `wa-prose-draft-purp-scienceandbible-v1-20260421.md` | relocate→Programme prose, or archive | `____` |
  | `wa-prose-draft-science-in-action-v4-20260513.md` | relocate→Programme prose, or archive | `____` |

### `Instructions/`  — mostly KEEP (governing `[current]` docs)
- **KEEP (authoritative current instructions/templates, per CLAUDE.md §10):** `wa-claudecode-instruction-v4_5` · `wa-patch-instruction-v2_11` · `wa-directive-instruction-v1_4` · `wa-dimensionreview-instruction-v3_3` · `wa-sessionb-analysis-output-v1_8` · `wa-sessionb-analysis-readiness-v1_10` · `wa-sessionb-cluster-instruction-v3_0` (active) · `wa-sessionc-cluster-overview-v1_0` · `wa-sessionc-cluster-ch1..ch7-instruction-v1_0` · `wa-sessionc-cluster-appendices-instruction-v1_0` · `wa-sessionc-cluster-style-method-v1_1` · `wa-cluster-publishing-instruction-v1_0` · `wa-versecontext-instruction-v3_10` · `wa-sessiond-orientation-v3_2` · `wa-sessiona-prose-instruction-v1_0` · `wa-global-readiness-sweep-instruction-v1_0` · `wa-global-sessionc-prose-rule-v1_1` · `wa-word-study-template-v2.1`.
- **DECISION:**
  | File | Note | Decision |
  |---|---|---|
  | `wa-database-schema-v3.14.0-20260421.json` | stray superseded schema snapshot (dup of the one archived in schema/) | archive `____` |
  | `wa-programme-prose-extract-20260424.json` | extract, not an instruction; newer `-20260506` lives in `Programme/programme_prose/` | relocate/archive `____` |
  | `wa-Session-A-Instruction-v8-final.docx` | superseded by the `audit_word` engine model + `wa-sessiona-prose-instruction`? or still the canonical Session A doc | `____` |
  | `wa-audit-framework-design-v0_1-20260526.md` | early audit design (audit now central in foundations) — live or superseded? | `____` |
  | `wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md` | one-off comparison; v3_0 now active | archive `____` |
  | `wa-v3-publication-pipeline-design-v1-20260527.md` | design that fed v3_0 | archive `____` |
  | `wa-v3_0-final-review-v1-20260527.md` | review that led to v3_0 adoption | archive `____` |
  | `wa-v3_0-phase-b-control-design-v1-20260527.md` | design that fed v3_0 | archive `____` |
  | `proposals/WA-disposition-catalogue-cluster-centric-proposal-v1-20260516.md` | proposal — adopted or superseded? | `____` |

### `Global_rules/`  — KEEP current
- **KEEP:** `wa-global-rules-all-v2` · `wa-global-rules-startup-v2` · `wa-global-rules-extract-20260427` (json+md).
- **DECISION:** `gr-obs-001-consolidation-draft-v3-20260426.md` — draft; consolidated into the rules yet? archive `____`

### `reference/`  — KEEP current snapshots
- **KEEP:** `wa-file-patterns-extract-20260420` (json+md) · `wa-label-patterns-extract-20260420` (json+md) · `wa-patch-types-extract-20260420` (json+md) · `wa-reference-snapshot-20260421.json`.
- **DECISION:** `Phase2-Flag-Types-Reference.docx` — superseded by the evidence-flag redesign (M29–M31)? archive `____`

### `registry/`  — KEEP current
- **KEEP:** `wa-registry-management-guide-v5_10-20260418.md` (governing doc).
- **DECISION (point-in-time snapshots — DB is the live source):**
  | File | Decision |
  |---|---|
  | `inner-being-words-snapshot-20260425.md` | `____` |
  | `wa-global-banked-registries-summary-20260420.md` | `____` |
  | `wa-registry-overview-20260411.json` (stale; newer overviews exist under Programme/) | archive `____` |

### `Clusters/`  — mixed reference + working analytics
- **KEEP (reference):** `wa-cluster-catalogue-v1-20260505` (json+md) · `wa-cluster-overview-20260530.md` · `wa-cluster-science-topics-v1-20260513.md` · `wa-flag-cluster-classification-v1_0-20260601.json`.
- **DECISION (working analytics / superseded):**
  | File | Note | Decision |
  |---|---|---|
  | `wa-cluster-status-20260502.md` | superseded by `cluster-overview-20260530`? | archive `____` |
  | `wa-cluster-observation-resolution-20260527.md` | working output | `____` |
  | `wa-cross-cluster-gloss-analytics-v1-20260526.md` | working analytics | `____` |
  | `wa-finding-citation-backfill-20260527.md` | one-off backfill log | archive `____` |
  | `wa-vcg-analytics-v1-20260527.md` | working analytics | `____` |
  | `wa-vcg-analytics-m05-deep-dive-v1-20260527.md` | working analytics | `____` |
  | `wa-vcg-analytics-citation-correction-v1-20260527.md` | one-off correction log | archive `____` |

### `Programme/`  (4 subfolders)
- **`Corpus_prose/`** — KEEP `wa-corpus-prose-20260428.md` + `-toc-`. (current corpus prose)
- **`programme_prose/`** — KEEP `wa-programme-prose-extract-20260506` (json+md). (newest)
- **`Program_reports/`**
  - **KEEP:** `wa-programme-open-items.md` (the single living register) · `wa-programme-cluster-audit-v3-20260603.md` + `wa-programme-cluster-summary-20260603.md` (latest audit) · `cost management 20260426.md`.
  - **DECISION:**
    | File | Note | Decision |
    |---|---|---|
    | `wa-programme-cluster-audit-v1` / `-v2-20260603.md` | superseded by v3 same day | archive `____` |
    | `wa-programme-status-report-20260427.md` | superseded by newer state? | `____` |
    | `programme-snapshot-20260425.md` | old snapshot | archive `____` |
    | `wa-registry-overview-20260501.json` | old overview | archive `____` |
    | `wa-database-integrity-check-20260427.json` | old check | archive `____` |
    | `wa-global-database-*-20260419` (audit/changeplan/completion/execution/migration-M19-M28/scriptupdates — **6 files**) | spent DB-migration working logs | archive `____` |
    | `wa-global-dimreview-flag-normalisation-20260419.md` · `wa-global-session5-unblock-sequence-20260419.md` | spent working logs | archive `____` |
    | `WA-M15-journey-reflection-v2-20260513.docx` · `WA-lessons-learned-v1-20260513.docx` | keep as records? | `____` |
  - **NOTE:** `Program_reports/` is per filing rules a *reports* folder; many of these are session/working logs that arguably belong in `archive/` or `Sessionlogs/`.
- **`programme_analysis/`** — appears to be **entirely historical** (status reports 20260330–20260420, dimension/root-family extracts, dir-result analyses, `word_registry.json`/`.csv`). **Proposed: archive the whole folder's contents** except anything you still consult. Mark exceptions: `____`

### `methodology/`  — large mix; KEEP the live foundations doc
- **KEEP:** `wa-study-foundations.md` (active living doc) · the `wa-v3_0-refinement-{0..4}-*-20260529` set + `wa-v3_0-refinement-discussion-v1` (recent v3_0 refinement — confirm still live `____`) · `wa-cluster-remediation-orchestrator-design-v1-20260602` / `wa-cluster-remediation-playbook-v1-20260601` / `wa-cluster-audit-aspect-spec-v1-20260601` (recent — **but** remediation was closed down 2026-06-04; archive these? `____`).
- **PROPOSED ARCHIVE (historical — Apr design notes, session logs, obslogs, per-word audit logs, superseded obs-question catalogues):** the `wa-023-compassion-*`, `wa-111/103/067-*`, `WA-obs-question-*-catalogue` (compassion/mercy/love/forgiveness — superseded by the DB catalogue), `wa-dim-*`, `wa-global-*` (Apr session logs/extracts), `WA-SessionLog-*`, `WA-SessionTranscript-*`, `WA-VerticalPass-*`, `*.docx` design notes, `flag-tables-extract-20260414.json`, `framework-b-research-posture-and-pathway.html`, `wa-sessionlog-v1-2026-04-13.md`, etc. — **~45 files.** I'll list each explicitly for your tick once you confirm the approach. Confirm bulk-archive of the April historical set? `____`

### `Sessionlogs/`  — historical logs (lighter touch by rule)
- Per filing rules §3.12, **logs are historical records and stay** unless explicitly superseded. This folder is ~80 files, almost all April global session logs + a few recent end-of-session logs.
- **Proposed:** KEEP the recent end-of-session logs (`wa-sessionlog-2026{0513,0514,0517,0526,0528,0601,0604}-*`) and the term-anchor-reset log; **archive the dense April-2026 `wa-global-*` process-log set** (the rules/flags/sessionb redesign logs from 20260414–20260421) into `Sessionlogs/archive/`. Confirm? `____`
- Also: `PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json` (a patch, belongs in `Sessions/Patches/archive/`) and two `.zip`/`files.zip` → archive `____`.

---

## Working notes
- _2026-06-04:_ Register created. **Tiers/** clear-archives executed (15 files); 3 decisions held.
- _2026-06-04:_ Auto-executed unambiguous archives: **schema/** (3 old snapshots + 1 `.bak`), **Sciences/** (`.zip` + `.html`).
- _2026-06-04:_ Full proposed disposition written for the remaining 8 folders — **nothing else moved**; awaiting researcher markup of the `____` cells. These folders are mostly single-version current docs cluttered by spent *working* documents; the archiving judgement is the researcher's.
