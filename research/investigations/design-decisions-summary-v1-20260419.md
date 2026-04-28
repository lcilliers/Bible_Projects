# Design Decisions Summary — Status and Open Items

| Field | Value |
|---|---|
| Filename | design-decisions-summary-v1-20260419.md |
| Status | LIVE — snapshot of 2026-04-19 PM |
| Purpose | Single-glance status of all design docs and what still needs your markup. Supports the "continue to prepare for database level work" ask. |
| Produced | 2026-04-19 |

---

## 1. Design Doc Status

| Doc | File | Status | Open Qs |
|---|---|---|---|
| Prose-in-SQLite advice | `prose-in-sqlite-advice-v1-20260419.md` | **RESOLVED** 2026-04-19 | 0 |
| Session A extract advice | `session-a-extract-section-types-advice-v1-20260419.md` | **RESOLVED** 2026-04-19 (all 7 Q's) | 0 |
| Prose store design | `wa-prose-store-design-v1-20260419.md` | **APPROVED — PROCEED** (marked at §13) | 0 blocking · minor §4 fixes noted |
| DB-wide review design | `wa-global-database-review-design-v1-20260419.md` | **DRAFT — awaiting markup** | **12** |
| Readiness sweep design | `wa-global-readiness-sweep-design-v1-20260419.md` | **DRAFT — awaiting markup** | **14** |
| Dimensions extract | `outputs/reports/wa-dimensions-extract-20260419.md` | Reference artefact | — |
| Question catalogue extract | `outputs/reports/wa-obs-question-catalogue-extract-20260419.md` | Reference artefact | — |

---

## 2. What's Ready to Produce

Once the DB-wide review design Q1–Q12 are resolved (§3 below), I can produce:

1. **DB-wide review instruction** (`data/imports/WA/Workflow/Framework_B/Session_B/wa-global-database-review-instruction-v1_0-20260419.md`) — the authoritative instruction CC follows to run the audit, change plan, migrations, script updates, execution, and closeout.
2. **CC operating rules** (`data/imports/WA/Workflow/Framework_B/Session_B/wa-claudecode-rules-v1_0-20260419.md`) — governs how CC works under the new file-based / no-chat-Q&A protocol.

The prose store design is already approved. It is part of Phase C of the DB-wide review instruction (migrations M_P1–M_P6). Its open items (§4 column alignment, Session C v2/v3 labels) are non-blocking — they can be fixed in the same editing pass that finalises the seed rows.

The readiness sweep design can be left for now — the sweep runs **after** the DB review. Its Q1–Q14 are best resolved once the DB review has landed.

---

## 3. Still to Decide — DB-Wide Review (Q1–Q12)

Each question has a concrete recommendation. You can accept the full block by writing `ACCEPT ALL RECOMMENDATIONS` at the bottom, or mark up individual answers in the DB review design doc itself.

| # | Question | My recommendation | Impact if deferred |
|---|---|---|---|
| Q1 | Instruction filename | `wa-global-database-review-instruction-v1_0-20260419.md` | confirmed |
| Q2 | Scope: all tables or only `wa_*` programme tables | All tables | |
| Q3 | CC designs AND applies migrations with per-migration approval | Yes, with explicit G3 approval per migration | would need external migration authoring otherwise |
| Q4 | Archive scripts updated when columns change | No — `archive/scripts/` left untouched | risks breaking archive scripts; historical anyway |
| Q5 | Historical patches rewritten on schema change | No — history immutable | breaks provenance if rewritten |
| Q6 | Backup retention for pre-migration snapshots | 6 months minimum, outside rolling 10 | data loss risk if short retention |
| Q7 | When does per-word sweep start relative to DB review | After all Phase A–F complete | overlapping scope coordinates badly |
| Q8 | Change plan granularity | Per-table sections | can regroup at output time |
| Q9 | Touch `mti_terms` table | Yes, with extra care and explicit G3 per change | mti_terms is recent architecture — high risk if wrong |
| Q10 | Update DB-access layers (`engine/db.py`, `analytics/db_client.py`) first | Yes — Phase D priority; prevents cascade breakage | schema changes break scripts otherwise |
| Q11 | External tools / new dependencies | None — plain SQL + stdlib sqlite3 | adds supply chain if otherwise |
| Q12 | Coordination with 6 Analysis-Complete words | Extracts regenerated after Phase F; analysis narratives historical | otherwise extracts go stale silently |

**Quick decision options:**

- **[ ] ACCEPT ALL RECOMMENDATIONS** — proceed with the above 12 answers. Fastest path to instruction production.
- **[X] INDIVIDUAL MARKUP** — mark up DB review design doc §12 directly; I wait for each answer.
- **[ ] CONDITIONAL ACCEPT** — accept all EXCEPT the items I mark below; I address those individually.

Q1 - agree
Q2 - all tables
Q3 - Yes, with explicit G3 approval per migration 
Q4 - Archive all redundant scripts
Q5 - No instructions will be modified for separately for new methods
Q6 - agree
Q7 - after the migration phases are complete
Q8 - change plan per phase - many tables are related, so migration phase will be multi table
Q9 - migration to have precedence of sweep - sweep may have to be adjusted following the migration
Q10 - some of the historic instructions will have to be reviewed and adjusted this will take place after migration.
Q11 - there is no external tool dependencies.
Q12 - the 6 completed words will go through the same process and be reprocessed.

Items to review individually (if CONDITIONAL ACCEPT): ________________________________


---

## 4. Still to Decide — Readiness Sweep (Q1–Q14) — *NOT BLOCKING NOW*

The sweep runs after the DB-wide review. These answers can be given at the end of the DB review work when scheduling the sweep. Deferred — no action needed today.

Summary of what's in the sweep doc (for awareness):
- Patch type for sweep remediation (new READINESSSWEEP vs REPAIR variant) — Q1
- Separate CC rules file — Q2 (**already decided YES** via the DB review scope)
- Outstanding tasks file scope — Q3
- Sweep session granularity — Q4
- Pre-sweep tooling verification — Q5
- Approval gate mechanism — Q6
- In-flight word behaviour (the 6 completed words) — Q7
- Idempotence self-check — Q8
- FLAG-010 relationship — Q9
- Rules governance for CC rules file — Q10
- Reporting format — Q11
- Integration with existing CC ops — Q12
- Sweep identifier naming — Q13
- Per-registry patch rejection handling — Q14

---

## 5. Non-Blocking — Prose Store §4 Seed Table

Status: catalogue edited, approved at §13, but the table has layout issues that should be cleaned up before the migration seed data is written.

**To fix when you return to the file:**

1. **Column alignment** — chapter names are in `lifecycle_tag` column; schema §3.1 reserves `lifecycle_tag` for 'v1'/'v2'/'v3' (Session C lifecycle only). Chapter names belong in `label`. The simplest fix: move each cell from `lifecycle_tag` → `label`, and set `lifecycle_tag = NULL` except for Session C (where it's 'v1').
2. **Formatting** — line 218 has a tab character before "Original Language Vocabulary"; line 226 missing space before `2` in `|2 |`. Minor.
3. **Session C v2 / v3** — only v1 listed. Either add v2/v3 rows or mark them as "to be seeded when those lifecycle versions are specified". Non-blocking — v1 is sufficient for initial seed.
4. **Session A codes** — user went with positional (`sa_s1_d1` … `sa_s1_d6`). Consistent; no change needed.
5. **Session A ordering** — Summary → Meaning → Verses → Terms → Pointers → Questions. Researcher's choice.

These fixes don't block the DB review instruction. They can be made during the migration authoring pass (Phase C of the DB review).

Validate - these fixes was done.
---

## 6. Next-Step Options

Pick one to drive the next session:

**Option A — Fast path: accept DB review recommendations in bulk**

1. You mark ACCEPT ALL on §3 above
2. I produce:
    a. DB-wide review instruction v1.0 (full document, ~1500–2000 lines)
    b. CC operating rules v1.0 (~300–500 lines)
    c. Prose store §4 cleanup pass (fix alignment, Session C lifecycle note)
3. You review the produced instruction
4. Approve → CC begins Phase A (schema audit) on live DB

**Option B — Review first: mark up DB review design individually**

1. You go through `wa-global-database-review-design-v1-20260419.md` §12 Q1–Q12 and answer each
2. I produce the instruction per your answers
3. Same downstream from there

**Option C — Produce draft instruction now with placeholders**

1. I produce a DRAFT instruction using my recommendations for all 12 questions; placeholders where your judgement is unclear
2. You mark up the DRAFT instruction directly
3. Cleaner than back-and-forth on the design doc; rougher first artefact

**My recommendation: Option A.** The questions are low-stakes; the recommendations are well-justified; fastest path to the actual work. You retain the ability to revise any decision during Phase A audit if something surfaces.

---

## 7. Researcher Decision

**Chosen option:** [ ] A  [ X ] B  [ ] C  [ ] other (specify)

All reviews have been done.  Sweep review postponed to after migration.

**If Option A — confirm ACCEPT ALL:** [ ] yes

**Individual overrides (if any):**  
 
 
 

**Date:**  
**Reviewer:** le Roux Cilliers

---

*End of summary v1 — 2026-04-19*
