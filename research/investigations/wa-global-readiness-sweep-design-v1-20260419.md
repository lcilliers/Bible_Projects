# wa-global-readiness-sweep — Design Workings (v1)

| Field | Value |
|---|---|
| Filename | wa-global-readiness-sweep-design-v1-20260419.md |
| Status | DRAFT — awaiting researcher markup |
| Purpose | Design workings for the new wa-global-readiness-sweep instruction. All open questions are captured in this file with proposed answers. Researcher marks up this file directly; Claude Code does not request answers in chat. |
| Next artefacts | (1) `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-readiness-sweep-instruction-v1_0-20260419.md` (the instruction itself); (2) optional `data/imports/WA/Workflow/Framework_B/Session_B/wa-claudecode-rules-v1_0-20260419.md` (CC-specific operating rules) |
| Produced | 2026-04-19 (updated same day to add §2.5 Prerequisite — DB-wide review) |
| Companion design doc | `outputs/investigations/wa-global-database-review-design-v1-20260419.md` — the DB-wide schema/FK/index review that runs **before** this sweep |

---

## How to Review This Document

1. Read sections in order.
2. Every **PROPOSED** decision is a concrete proposal. To accept, no action needed. To override, strike through and write the alternative.
3. Every **OPEN** question is something I need an answer on before the instruction can be finalised. Write your answer inline under the question.
4. Mark the document **APPROVED — PROCEED** at the bottom when ready for me to build the instruction.

---

## 1. Requirements — My Interpretation

Pulled verbatim from your direction on 2026-04-19:

| # | Requirement | Source |
|---|---|---|
| R1 | Filename root: `wa-global-readiness-sweep` | Direct |
| R2 | Same discipline as v1.6: segment → decide → prepare patch → get approval → apply | Direct |
| R3 | Patch format may be changed to suit CC method of operation | Direct |
| R4 | Must be rerunnable on the 6 words currently at Analysis Complete | Direct |
| R5 | All words except excluded words must be included (carry_forward = 1 filter) | Direct |
| R6 | Operation is done word by word | Direct |
| R7 | Claude AI role is null — this is Claude Code only | Direct |
| R8 | Tasks beyond CC's skill → recorded in a separate `.md` tasks file | Direct |
| R9 | Global general rules review included in the sweep | Direct |
| R10 | Global general rules apply to CC too (not only Claude AI) | Direct |
| R11 | CC may create its own rules | Direct |
| R12 | No chat-based Q&A. All workings, questions, decisions captured in `.md` files | Direct |
| R13 | `.md` files must support restart, backtrack, and asynchronous researcher review | Direct |

**Implicit requirements derived from the above:**

| # | Implicit requirement | Derivation |
|---|---|---|
| R14 | Sweep must be resumable from interruption (like v1.6 Session Start Protocol) | R13 |
| R15 | Sweep must be idempotent (re-running on a clean word is a no-op) | R4, R5 |
| R16 | Sweep must not disturb in-flight analytical work (the 6 completed words) | R4 |
| R17 | Sweep produces concrete patch + approval artefact per registry, not a monolithic programme-wide patch | R2, R6 |
| R18 | Observations log per sweep session (programme-level) plus per-registry sections | R13 |
| R19 | Researcher response vehicle is markup on `.md` files, not chat replies | R12, R13 |

---

## 2. Pipeline Position — Proposed

**PROPOSED:** The sweep sits *before* Stage 1 Analysis Readiness per word. It operates on the live database via SQL. Its output is: a clean, consistent data baseline across all non-excluded registries, such that per-word v1.6 Stage 1 can begin without hitting programme-wide inconsistencies.

```
STEP Bible → Phase 1 (registration + extraction) → audit_word
       │
       ▼
Verse Context (Stage 1) — per word, Claude AI-driven
       │
       ▼
Dimension Review — per word or per cluster, Claude AI-driven
       │
       ▼
═════════════════════════════════════════════════════════════
PREREQUISITE — wa-global-database-review (separate instruction)
  Schema-level cleanup: FK graph, column inventory, index
  strategy, redundancy removal. Migration-based (M19+).
  Runs ONCE before the sweep; paused between runs if new
  schema issues are uncovered.
  Design doc: wa-global-database-review-design-v1-20260419.md
═════════════════════════════════════════════════════════════
       │
       ▼
═════════════════════════════════════════════════════════════
wa-global-readiness-sweep (this instruction) — CC-only
  Purpose: mechanical data-level audit + remediation
           across all carry_forward = 1 registries.
  Operates directly on the database via SQL.
  Produces per-registry remediation patches.
═════════════════════════════════════════════════════════════
       │
       ▼
Session B Stage 1 (Analysis Readiness — v1.6) — per word, Claude AI
       │
       ▼
Session B Stage 2 (Analysis Output) — per word, Claude AI
       │
       ▼
Session C → Session D
```

The sweep does **not** perform what Claude AI must perform. It surfaces those items for subsequent per-word processing by Claude AI under v1.6. This guarantees clean handoff.

---

## 2.5 Prerequisite — DB-Wide Review and Reorganisation (separate instruction)

**PROPOSED** — separate instruction, runs before this sweep.

### Why separate

The DB-wide review is qualitatively different from per-word sweep:

| Aspect | DB-wide review | Per-word sweep (this doc) |
|---|---|---|
| Operation type | DDL (schema changes) | DML (data corrections) |
| Tooling | `engine/migrate.py` — migrations M19+ | `scripts/apply_session_patch.py` — patches |
| Scope | Programme-wide, cross-cutting | Per registry |
| Frequency | One-off; rerun only if new schema issues surface | Rerunnable on every registry |
| Risk | High — breaks every script/query on mistake | Moderate — patch can be narrow |
| Reversibility | Hard — requires down-migration or full backup restore | Easy — soft-delete or field revert |
| Approval cadence | One big plan approved up front, per-migration gates thereafter | Per-registry patch approval |
| Blast radius if wrong | Every consumer: engine, analytics, exports, Claude AI extracts | One registry's data |

### What it covers

User's direction:

1. **Complex/unnecessary FK relationships** — reduce join count, hop count, extraction complexity. Audit the FK graph; propose simplifications (denormalise where it genuinely helps; remove FK where cascade is not needed; keep FK where referential integrity matters).
2. **Redundant, unused, or conflicting columns** — remove. Known candidates from CLAUDE.md §17.6:
    - `wa_term_inventory.god_as_subject` (superseded by `mti_term_flags`)
    - `wa_term_inventory.somatic_link` (superseded by `mti_term_flags`)
    - `wa_term_inventory.status_note` (NULL across all records)
    - `word_registry.inference_note` (researcher-set only; never pipeline-written)
    - `mti_terms.status_note` (written only by audit_word A10)
    - Probably more — audit will find them.
3. **Index optimisation** — add missing indexes for common queries; remove unused indexes; consolidate overlapping.
4. Implicit: **data type consistency** (TEXT dates vs ISO strings vs INTEGER timestamps), **constraint coverage** (NOT NULL where justified, CHECK constraints), **orphan row cleanup** (rows whose FK target has been deleted).

### Sequencing with this sweep

The DB-wide review must complete **before** this sweep runs, because:

- Per-word sweep queries assume schema shape. If columns are removed after sweep patches are written, patches break.
- Remediation patches must target the final schema, not the interim one.
- The readiness scorecard summarises schema-aligned counts; those counts shift if schema changes.

**Exception — partial overlap acceptable if:** DB-wide review leaves certain columns untouched that the sweep *depends on*. The DB-wide review change plan must explicitly list which columns are deferred so the sweep can proceed. This is a coordination question settled in the DB-wide review design doc.

### Handoff from DB-wide review to this sweep

The DB-wide review's completion artefact is a **Schema Completion Record** that states:
- Schema version is now v3.10.0 (or whatever)
- All planned migrations applied
- All dependent scripts updated
- Schema export regenerated
- CLAUDE.md §3 regenerated
- Sweep-blocking changes: NONE remaining

This sweep instruction cites that record as the entry precondition.

---

## 3. Scope Boundary — What CC Can and Cannot Check

### 3.1 What CC can fully handle (Path 1 — mechanical patch)

These correspond to v1.6 Section A, parts of B, parts of D/E, and much of G. All are pure SQL-level or pure FK-integrity checks with no analytical judgement:

| Check domain | Examples |
|---|---|
| Registry state (mechanical) | `verse_context_status`, `dim_review_status`, `cluster_assignment`, `carry_forward`, `unique_term_count`/`shared_term_count` integrity |
| Term data quality | Strong's format; `language` vs prefix mismatch; `mti_terms.status` controlled vocabulary; `term_owner_type` vs `mti_terms.status` consistency; `delete_flagged` integrity; `causative_form_present` NULL → 0 |
| Cross-table consistency | `wa_term_inventory.somatic_link` vs `mti_term_flags` (flag_id 3,4) per GR-DATA-003; deleted-term `delete_flagged` sync across tables |
| Three-number verse diagnostic | Per OWNER term: `span_match_count`, `total_verse_records`, `delete_flagged_count` — identify span filter failures, zero-extraction gaps, over-extraction |
| Group integrity | `group_code` format; duplicate codes; FK resolution; active anchor presence; `dominant_subject` = 'NONE' correctable from group description |
| Dimension index | NULL dimension, AUTOMATED confidence, `manual_override` NULL → 0, duplicate dimension rows per group |
| Supporting data | Dangling FKs (`parsed_meaning_id`), missing `NO_WORD_ANALYSIS` quality flag when meaning data absent, root family `root_code`/`root_language` integrity |
| Flag accounting (mechanical) | Phase2 flag counts; research flag counts by target; quality flag counts |
| Audit history | `word_run_states` REVIEW flags with `researcher_approved = 0` — surface, count, classify |

### 3.2 What CC cannot handle (must be surfaced, not resolved)

| Check domain | Path | Rationale |
|---|---|---|
| Verse-reading confirmation (e.g. `god_as_subject` plausibility) | Path 3 — note for per-word Stage 2a | Requires analytical judgement |
| Phase2 flag assessment (confirm/reject) | Path 3 or 5 — defer | Requires reading verses |
| Finding validity assessment | Path 3 — defer | Requires analytical judgement |
| B-target research flag resolution (types B, C, D) | Path 3 or 5 — defer | Requires analytical work |
| Catalogue question linking for findings | Path 5 — defer | Requires semantic matching beyond mechanical SQL |
| Dimension assignment verification | Path 3 — defer | Requires reading verses |
| Any RESEARCHER_DECISION | Path 4 — RD accumulator | Human judgement |
| Sub-process execution (Verse Context classification, Dimension Review) | Path 2 — directive | Claude AI must perform; CC produces directive, not runs process |
| Re-extraction (audit_word re-run) | Path 2 — directive | CC can execute under researcher approval; surfaced as directive |

**Proposed classification change from v1.6:** I introduce **Path 5 — Outstanding Task** for items that are beyond CC's skill but are not a researcher decision either. These get written to a persistent outstanding tasks `.md` file for subsequent processing (typically by Claude AI under v1.6 per-word Stage 1, or manually).

---

## 4. Proposed Artefact Set

### 4.1 Per-sweep session artefacts (programme-level)

| Artefact | Filename pattern | Purpose |
|---|---|---|
| Sweep session log | `outputs/session-logs/wa-global-readinesssweep-sessionlog-v{n}-{YYYYMMDD}.md` | Session boundary log: what session started/ended, position marker, which registries were touched |
| Sweep observations log | `outputs/session-logs/wa-global-readinesssweep-obslog-v{n}-{YYYYMMDD}.md` | Programme-level findings, cross-registry patterns, sweep-level progress record |
| Outstanding tasks file | `outputs/wa-global-outstanding-tasks-v{n}-{YYYYMMDD}.md` | Persistent. Tasks CC could not perform. Grows across sweeps. |
| RESEARCHER_DECISION accumulator | `outputs/wa-global-readinesssweep-rd-v{n}-{YYYYMMDD}.md` | Per-sweep RD items requiring researcher markup |
| Sweep completion record | Section within the session log | Final summary when sweep completes |
| Programme readiness scorecard | `outputs/reports/wa-global-readiness-scorecard-{YYYYMMDD}.md` | One-page summary of registry readiness levels across all words |

### 4.2 Per-registry artefacts

| Artefact | Filename pattern | Purpose |
|---|---|---|
| Per-registry observations section | Within the sweep obslog | Findings per registry |
| Per-registry remediation patch | `data/imports/WA/Patches/wa-{nnn}-{word}-readinesssweep-v{n}-{YYYYMMDD}.json` | Path 1 mechanical patch for this registry |
| Per-registry sub-process directive(s) | `data/imports/WA/Patches/wa-{nnn}-{word}-readinesssweep-dir-{seq}-{desc}-v{n}-{YYYYMMDD}.md` | Path 2 directive(s) if sub-processes needed |
| Per-registry completion record | Section within the sweep obslog | Summary for this registry at end of its pass |

### 4.3 Design workings and rules artefacts (non-sweep, one-off)

| Artefact | Filename | Purpose |
|---|---|---|
| This design doc | `outputs/investigations/wa-global-readiness-sweep-design-v1-20260419.md` | Design workings — this file |
| The instruction | `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-readiness-sweep-instruction-v1_0-20260419.md` | Final instruction (produced after design approved) |
| CC operating rules | `data/imports/WA/Workflow/Framework_B/Session_B/wa-claudecode-rules-v1_0-20260419.md` | CC-specific rules (if approved) |

---

## 5. Proposed Sweep Flow

The sweep is executed **per sweep session**. One session may cover one registry, a batch of registries, or (rarely) all in one go. Sessions can resume; position markers are in the observations log.

### 5.1 Session start — sweep-level

| Step | Action |
|---|---|
| S0 | Open or increment sweep obslog per GR-OBS-004 and GR-FILE-004. |
| S1 | Confirm **governing documents loaded**: global rules `[current]`, this instruction `[current]`, CC rules `[current]`, patch instruction `[current]`. Record the resolved version of each. |
| S2 | Check governing-document version drift: if any document has a newer version than recorded in the last sweep session, note in obslog. |
| S3 | Build worklist: `SELECT no, word FROM word_registry WHERE carry_forward = 1 ORDER BY no`. Record count. |
| S4 | Determine resume position: read progress record from obslog; first un-completed registry is the resume point. |
| S5 | Write `SESSION STARTED` record with worklist and resume position. |

### 5.2 Per-registry pass

For each registry `nnn` in worklist, starting from resume point:

| Phase | Name | Scope |
|---|---|---|
| R.A | Registry state | `word_registry` row checks |
| R.B | Term inventory | OWNER / XREF / Deleted term checks |
| R.C | Verse records | Verse quality + three-number diagnostic |
| R.D | Verse context groups | Group + anchor + set-aside checks |
| R.E | Dimension assignments | Dimension index checks |
| R.F | Flags, findings, catalogue | Counts + status checks |
| R.G | Supporting term data | Meaning parse, root family, related words, LSJ, cross-registry links |
| R.H | Consolidate + classify | Resolution path assignment for every anomaly |
| R.I | Patch construction | Build remediation patch from Path 1 items |
| R.J | Approval gate | Write patch + directive(s) to disk. **WAIT** — do not apply until researcher approval recorded in obslog. |
| R.K | Apply + verify | After approval: apply patch, verify via targeted SQL, record outcome |
| R.L | Registry completion record | Sign off on registry; move to next |

**Researcher approval gate (R.J):** The patch file is written to `data/imports/WA/Patches/`. The obslog records: `AWAITING APPROVAL: registry [nnn]. Patch file: [path]. Approval recorded by writing "APPROVED: [initials] [date]" next to the patch entry in the obslog. Or "REJECT: [reason]" to cancel.` CC polls the obslog at session resume; does not proceed until marked.

### 5.3 Session close — sweep-level

| Step | Action |
|---|---|
| C1 | Finalise per-registry pass (do not end mid-phase if avoidable) |
| C2 | Verify obslog sections current (progress record, outstanding tasks written, RD accumulator written) |
| C3 | Produce sweep session log with resume instructions |
| C4 | Save obslog with version increment as next-session starting state |

### 5.4 Sweep completion

When worklist is fully processed:

| Step | Action |
|---|---|
| F1 | Produce final sweep completion record in obslog |
| F2 | Produce programme readiness scorecard |
| F3 | Outstanding tasks file carried forward (for subsequent Claude AI per-word Stage 1) |

---

## 6. Proposed Resolution Classification (Paths 1–5)

Extends v1.6's four-path framework with a fifth path for CC-specific skill-limit cases.

| Path | Scope | CC action |
|---|---|---|
| **1 — Mechanical fix** | Correctable by SQL update/insert with no analytical judgement | Add to the registry's remediation patch |
| **2 — Sub-process re-run** | Requires re-extraction, VC re-run, DimReview re-run, etc. | Produce plain-language directive file; await researcher approval; execute under normal CC workflow |
| **3 — Deferred to per-word Stage 1** | Requires analytical judgement that CC cannot perform but per-word v1.6 Stage 1 (Claude AI) will address | Record in outstanding tasks file, keyed to registry; tagged `DEFER_STAGE1` |
| **4 — RESEARCHER_DECISION** | Requires human judgement on direction | Add to RD accumulator file, marked OPEN; sweep pauses for that registry at R.J |
| **5 — Outstanding task (beyond CC skill)** | Not analytical, not researcher decision, but beyond CC's mechanical tooling (e.g. catalogue linking requiring semantic matching, missing applicator operation types, structural repair requiring new script) | Add to outstanding tasks file with tag identifying required capability |

**Resolution rule for CC:** Walk the paths 1 → 2 → 3 → 4 → 5 in order. Assign the *first* path that applies. Every anomaly must have exactly one path.

---

## 7. Proposed CC Operating Rules (new artefact)

**PROPOSED** — these would live in `wa-claudecode-rules-v1_0-20260419.md`. Global rules continue to govern. These are additions specific to how CC operates.

| Rule | Text |
|---|---|
| CC-LOAD-001 | CC confirms global rules file loaded at session start; states resolved version. Mirror of Claude AI's GR-LOAD-001. |
| CC-OBS-001 | All CC findings, decisions, and actions recorded in an observations log `.md` as they occur. Chat output is a pointer to the obslog, not the log itself. Mirror of GR-OBS-001. |
| CC-RD-001 | CC never asks questions in chat. Any question requiring researcher input is written to the RD accumulator `.md` file with proposed options and recommendation. |
| CC-SKILL-001 | If a task is beyond CC's tooling or skill, it is recorded in the outstanding tasks file with an explicit statement of what capability is missing. CC does not attempt to work around skill limits silently. |
| CC-PATCH-001 | CC writes patches to disk and awaits explicit approval recorded in the obslog before applying. Approval in chat is not sufficient under the new working protocol. |
| CC-RERUN-001 | CC operations must be rerun-safe. Re-running a sweep on a clean registry is a no-op (zero patch operations). |
| CC-FAIL-001 | If CC cannot verify the outcome of a patch or directive, it records the condition as a Path 4 RD item rather than proceeding uncertainly. |
| CC-SCOPE-001 | CC does not perform analytical judgement. Any check requiring verse reading, semantic assessment, or interpretative decision is surfaced as Path 3 or Path 5 — never resolved inline. |
| CC-LOCK-001 | CC respects per-registry locks (LOCK_SENTINEL). A registry under lock is skipped in the sweep with an obslog note; re-attempted in the next sweep session. |
| CC-VERSION-001 | CC checks schema version against EXPECTED_SCHEMA_VERSION at sweep start; refuses to proceed on mismatch. |
| CC-IDEM-001 | CC's remediation patches specify corrections, not operations. A patch that would apply the same correction twice is a bug; the build step must detect this. |

---

## 8. Worklist Scope and the 6 Completed Words

### 8.1 Filter proposal

**PROPOSED:** Worklist = all registries where `carry_forward = 1` AND `delete_flagged = 0`. No filter on `session_b_status`.

This means:
- 6 words at Analysis Complete (compassion, fellowship, forgiveness, grace, love, mercy) — INCLUDED
- All words at Pre-Analysis Complete — INCLUDED
- All words at Ready for Analysis / Verse Context Reset — INCLUDED
- Words at VC Complete but not yet Pre-Analysis — INCLUDED
- Words at VC In Progress — INCLUDED (phase R.A will flag VC-incomplete as hard gate note)
- Words at session_b_status = NULL — INCLUDED only if carry_forward = 1
- Excluded (~30 words with carry_forward = 0) — NOT INCLUDED

### 8.2 How the 6 completed words are handled

**PROPOSED:** Sweep runs phases R.A–R.H normally. The remediation patch is *additive only* — it does not reset `session_b_status`. If structural issues are found that invalidate completed analysis, the finding is recorded as Path 4 RD (`RESEARCHER_DECISION: registry [nnn] completed but has structural issue [x]. Recommend REPAIR-ANALYSIS-RERUN vs mechanical-patch-only.`). Researcher chooses path.

### 8.3 Mid-flight words

**PROPOSED:** Words at VC In Progress (grace 68, suffering 214) — sweep runs phases R.A–R.G as data read. Patch is constructed only for Path 1 items that are *independent of* the in-flight VC work. Path 2 items held pending VC completion.

---

## 9. Patch Type and Filename — Proposed

### 9.1 Patch type

**OPEN — decide one:**

- **Option A:** New patch type `READINESSSWEEP` added to patch spec. Pros: distinct traceability; clean semantics. Cons: applicator change required.
- **Option B:** Reuse `REPAIR` type with scenario `READINESSSWEEP`. Pros: no applicator change. Cons: conflates with REPAIR cascade scenarios.
- **Option C:** Reuse `PREANALYSIS` type. Pros: simplest path; same applicator. Cons: semantically wrong (these are not pre-analysis patches per v1.6); breaks naming convention for the 6 Analysis-Complete words.

**My recommendation: Option A — new type READINESSSWEEP.** Rationale: it is not a REPAIR (no cascade reset), not a PREANALYSIS (not tied to per-word Stage 1). The patch spec can be extended; applicator change is small.

### 9.2 Patch filename

**PROPOSED:** `wa-{nnn}-{word}-readinesssweep-v{n}-{YYYYMMDD}.json` — matches GR-FILE-001/007/009.

### 9.3 Internal patch_id

**PROPOSED:** `PATCH-{YYYYMMDD}-{nnn}-READINESSSWEEP-V{n}` for applicator compatibility.

---

## 10. Governing Documents to Cite in the Instruction

Per GR-REF-002 (`[current]` token):

- `wa-global-general-rules [current]` — applies to CC too (per user directive R10)
- `wa-reference [current]` — vocabulary, schema reference
- `wa-claudecode-instruction [current]` — existing CC responsibilities
- `wa-claudecode-rules [current]` (to be produced if approved)
- `wa-patch-instruction [current]` — patch construction
- `wa-directive-instruction [current]` — Path 2 directives
- `wa-sessionb-analysis-readiness [current]` — referenced for handoff semantics (not subordinate to)
- `wa-versecontext-instruction [current]` — Path 2 VC sub-process
- `wa-dimensionreview-instruction [current]` — Path 2 DimReview sub-process

---

## 11. Mapping v1.6 Sections → Sweep Phases

For reviewer context. `●` = CC performs mechanically. `◐` = CC performs partially (mechanical only). `○` = CC surfaces for per-word Claude AI Stage 1.

| v1.6 check | Sweep phase | CC coverage | Path(s) CC can assign |
|---|---|---|---|
| Section A.0 — Statistics pre-read | R.A | ● | 1, 3 |
| Section A.1 — audit_word history | R.A | ● | 1, 3, 4 |
| Section A — Registry record | R.A | ● | 1, 4 |
| Section B1 — OWNER terms (fields) | R.B | ● | 1, 3, 4 |
| Section B1 — Three-number verse diagnostic | R.B / R.C | ● | 1, 2, 4 |
| Section B2 — XREF terms | R.B | ● | 1, 4 |
| Section B3 — Deleted terms | R.B | ● | 1 |
| Section C — Verse record quality | R.C | ● | 1, 3, 4 |
| Section D1 — Groups | R.D | ● | 1, 4 |
| Section D2 — Anchor verses | R.D | ● | 1, 2, 4 |
| Section D3 — Set-aside reasons | R.D | ● | 3 |
| Cross-check D1 — dominant_subject | R.D | ◐ | 1 (NONE→description), 4 (NULL) |
| Section E — Dimension assignments | R.E | ● | 1, 2, 4 |
| Cross-check E1 — one dim per group | R.E | ● | 2, 4 |
| Cross-check E2 — Somatic dim vs flags | R.E | ◐ | 3 |
| Cross-check E3 — Theological dim vs god_as_subject | R.E | ◐ | 3 |
| Section F1-5 — Flags/findings/catalogue counts | R.F | ● | (orient only) |
| Section G1 — Meaning parse | R.G | ● | 1, 3 |
| Section G2 — Root families | R.G | ● | 1 |
| Section G3 — Related words | R.G | ○ | 3 |
| Section G4 — LSJ | R.G | ○ | — |
| Section G5 — Cross-registry links | R.G | ● | — |
| Step 1.3a — Phase2 flags assessment | (not in sweep) | ○ | 3 (outstanding) |
| Step 1.3b — Findings catalogue linking | (not in sweep) | ○ | 5 (outstanding — semantic match) |
| Step 1.3c — B-target flag resolution | R.F (partial) | ◐ | 3, 5 (outstanding for types B/C/D) |

**Interpretation:** The sweep covers v1.6 Step 1.2 mechanically. It does NOT cover Step 1.3. Step 1.3 work remains for per-word Claude AI. This is the correct division — CC does mechanical prep; Claude AI does analytical prep.

---

## 12. Open Design Questions — ALL RESOLVED 2026-04-19

Researcher decision (2026-04-19): batch acceptance of all CC recommendations. Individual outcomes recorded below.

### Q1 — Patch type decision — RESOLVED

Decision: **Option A** — new `READINESSSWEEP` patch type. Applicator extension tracked via outstanding task OT-DBR-003 alongside the PROSE operations.

### Q2 — Separate CC rules file? — RESOLVED

Decision: **Yes** — already delivered as `wa-claudecode-rules-v1_0-20260419.md` (Active — approved 2026-04-19).

### Q3 — Outstanding tasks file scope — RESOLVED

Decision: **Global persistent file** across all sweeps. Already in use at `outputs/wa-global-outstanding-tasks-v1-20260419.md` (carried across DB review and future sweep sessions).

### Q4 — Sweep session granularity — RESOLVED

Decision: **Flexible** — default full worklist; invocation flags `--scope=registry:N` and `--scope=cluster:C17` narrow scope. Position marker persists regardless.

### Q5 — Pre-sweep tooling verification — RESOLVED

Decision: **Yes** — phase S1 pre-flight checks schema version, applicator version, and open applicator gaps. Fail-fast on staleness.

### Q6 — Researcher approval gate mechanism — RESOLVED

Decision: **Inline in obslog**. Researcher writes `APPROVED: [date]` (or `REJECT: [reason]`) next to the patch entry; CC polls the obslog at session resume.

### Q7 — In-flight word behavior — RESOLVED

Decision: **(a) with safeguard.** Sweep runs on the 6 reset-to-`Verse Context Reset` words normally; patches additive only; structural invalidations surfaced as Path 4 RD.

### Q8 — Idempotence verification — RESOLVED

Decision: **Yes** — phase R.K includes idempotence self-check. Re-running phases R.A–R.H on a just-patched registry must produce zero new Path 1 items. Gaps surfaced as Path 4 RD.

### Q9 — Relationship to FLAG-010 — RESOLVED

Decision: **Exempt.** Sweep is mechanical (not analysis). FLAG-010 status is checked and surfaced per registry in phase R.F.

### Q10 — Rules governance — RESOLVED

Decision: **Yes to all three.** `wa-claudecode-rules [current]` is a Companion Document, part of the `[current]` corpus, and listed in "What to Attach at Session Start".

### Q11 — Reporting format — RESOLVED

Decision: **(b) clustered with summary rows.** Programme Readiness Scorecard presented hierarchically: programme summary → per-cluster (C01–C22) summary → per-registry rows within each cluster.

### Q12 — Integration with existing Claude Code operations — RESOLVED

Decision: **Supplement, not supersede.** The sweep surfaces issues and issues Path 2 directives for audit_word re-runs; the standard audit_word flow executes them under researcher approval. Sweep does not directly invoke audit_word.

### Q13 — Sweep identifier — RESOLVED

Decision: **Yes** — `SWEEP-YYYYMMDD-NNN` sequential per day. Stored in obslog header; carried on all artefacts.

### Q14 — Handling per-registry patch rejection — RESOLVED

Decision: **Skip registry with note; record rejection in RD accumulator invites reason.** Sweep continues; rejected registry becomes eligible again in a subsequent sweep session after the reason is addressed.

---

## 13. Proposed Instruction Structure (section skeleton)

Once this design doc is approved, the instruction will contain these sections:

1. Header + metadata
2. Governing Rules (cites global rules + CC rules + patch instruction + directive instruction)
3. Change Log
4. Pipeline Position
5. What to Attach at Session Start
6. Governing Disciplines (CC-specific)
7. Scope — Worklist Definition and Exclusions
8. Resolution Classification Framework (Paths 1–5)
9. Tracking Document Structure (obslog, tasks file, RD file, scorecard)
10. Session Start Protocol (S0–S5)
11. Session Close Protocol (C1–C4)
12. Fallback Protocol (per failure mode)
13. Sweep-level Pre-flight Check (schema, tooling, applicator gaps, rules currency)
14. Per-Registry Phases R.A through R.L (full specification of each phase)
15. Patch Construction and Format
16. Approval Gate Protocol
17. Application and Verification
18. Idempotence Self-Check
19. Registry Completion Record Format
20. Sweep Completion Record Format
21. Programme Readiness Scorecard — Format and Generation
22. Outstanding Tasks File — Format and Maintenance
23. Integrity Rules (sweep-specific, numbered GS-01 onward)
24. Appendix A — SQL check library (one entry per check)
25. Appendix B — Resolution path decision rules
26. Appendix C — Rerun matrix (what changes on second/third run of a clean registry)

---

## 14. Proposed CC Rules Document Structure (section skeleton)

Once approved, `wa-claudecode-rules-v1_0-20260419.md` will contain:

1. Header + metadata
2. Relationship to `wa-global-general-rules` (CC rules supplement, do not replace)
3. Rule index
4. Full rule text per CC-nnn-nnn
5. Companion documents and cross-refs
6. Change log

---

## 15. Next Steps — Expected Markup Sequence

1. Researcher reads this doc, marks up answers to Q1–Q14 and any PROPOSED items.
2. Researcher writes `APPROVED — PROCEED` below, with date.
3. Claude Code produces:
    a. `wa-global-readiness-sweep-instruction-v1_0-20260419.md`
    b. `wa-claudecode-rules-v1_0-20260419.md` (if Q2 = Yes)
    c. Updates this design doc to v2 with "final" status.
4. Claude Code runs a trial sweep on a small scope (single registry) to validate before full-programme run.

---

## 16. Approval

**Researcher approval:**

Status: [X] APPROVED — PROCEED  [ ] REVISIONS REQUESTED — see markup

Date: 2026-04-19

Reviewer: le Roux Cilliers

Notes: All Q1–Q14 resolved adopting CC recommendations. Design approved. Proceed to produce the wa-global-readiness-sweep-instruction v1.0, incorporating post-DBR schema awareness (mti_term_flags joins replace dropped columns; wa_dimension_index is 15-col; prose store is operational; word_synopsis column exists on word_registry).

---

*End of design workings v1 — 2026-04-19*
