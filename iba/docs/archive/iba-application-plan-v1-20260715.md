# Plan: Inner Being Analysis Programme — segmented, autonomous, DB-driven application

> **How this document is organised.** The **plan** (§1–§5) carries the **principles, do's and don'ts, and the connecting tissue** — how the parts fit and why. The **detailed component designs** (table/rule/interface models) live in **appendixes**, each to be extracted to its own document on build: **A — Configurator**, **B — Schema design**, and more as they arise.

## 1. Context — why we are building this

### 1.1 What the study is

The **Inner Being Analysis Programme** (owner: le Roux Cilliers, sole researcher and final authority on scope and method) is a structured academic Bible-research programme whose object is **how Scripture expresses the workings of the human inner being** — Scripture's depiction of the whole inner life (moral, emotional, volitional, relational, vertical and horizontal), with no specific theological bias and the human in focus is in scope. It grew out of two earlier ~100-page AI studies (*Spirit, Soul and Body*; *The Holy Spirit*) whose findings **"appeared strong at first but deteriorated under further questioning"** and badly understated the inner being's characteristics. The programme therefore measures itself against the **two quality bars those studies failed: comprehensiveness (nothing understated) and robustness (findings that withstand deeper questioning).**

It works from an initial registry of ~214 inner-being words, growing over time, each mapped using the STEP Bible to its Hebrew/Greek originals via Strong's and captured in a SQLite database processed by a custom engine — but the word registry is **scaffolding, not the object.** The analytical unit is a **focus point**: a latent, emergent, dynamic configuration of the inner being that can never be observed or logged directly, only **inferred** from the **operations** a verse describes it performing. Hence the governing method — **infer, don't extract** (read the verse *backward*: this act happened, what inner reality produced it? — never *forward* by lexical surface); the object modelled as a **process / relational web** read off *what each verse does* rather than a grid of named parts; and validity established by **convergence** of independent witnesses (a mechanical-lexical floor + AI conceptual synthesis + scholarship, each grounded to verses and marked **STATED vs INFERRED**). Nine documented principles govern it (registry completeness; collate-before-analyse; no forced categories — patterns emerge from evidence; verses qualify by original-language occurrence; every finding substantiated with no guessing; read the data as a whole; the DB is the analytical memory; biblical lens primary / science secondary; synthesis bottom-up). The **end point** is two-part: a materially-evidenced findings corpus held entirely in the DB (a finding for every verse — **silence is a valid finding**), and the products drawn from it — essays, study guides, ebooks/books, sermon series — for three audiences (scholar; leader/teacher; ordinary reader). *(Sources: `CLAUDE.md` §1; `Workflow/methodology/wa-study-foundations.md` §0,§a–§d; `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` §13; `wa-METHOD-SYNTHESIS-verse-fanout-multicontributor-v1-20260627.md`; `wa-RESET-baseline-review-and-changeover-v1-20260625.md`.)*

### 1.2 Why an application, and why now

Over roughly **six months** the study has been attempted, reset, and re-attempted through an AI **chat interface**, and it has **failed repeatedly** — most recently a rule-grounded audit (2026-07-14) found **8 of 18 lexical dimensions fail their own written rules and 0 pass.** The multitude of failure reviews on file converge on a consistent set of **fundamental** causes — not bad luck:

- **Over-structuring an integrated subject** (the deepest root) — the impulse to impose tidy structure (one home per object, reconcile everything, drive the gate to zero) on human inner life, which is not systemisable; breaking the corpus into logical units has been the single greatest source of rework, each new structure a fresh fault line the AI falls over.
- **Method instability** — the organising unit was rebuilt four to five times (registry → dimension → term-similarity → characteristic → movements), each reset turning prior "completed" work into legacy-to-revisit.
- **Ungrounded frames read as findings (eisegesis)** — cold-read validation found ~70–85% of analytical claims imported meaning the verses don't carry; the grid was relabelling fixed lemma-constants (`faculty`, `type`) as per-verse discoveries. Plausibility ≠ truth.
- **Extraction mistaken for inference; regex/keyword-derived values** — mechanical extraction logged values the verse never stated; "coverage" was a mirage (the analytical layer reached ~9% of spans while verses were declared complete).
- **Completeness checked, not validity** — "done" was measured as passages/coverage, not sound reading; verse-meaning soundness — the gravest risk — carries a high error rate that only surfaces under critical challenge (the exact failure mode of the prior studies).
- **Rules not encoded — dependence on the model's memory** — the rules lived in prose and the model's memory, and the model repeatedly ignored them and "did its own thing"; a persistent drift between what was decided and what the live artefacts/tools actually do.
- **Analyst drift** — dimensions (e.g. `role`, `type`) and depth drifted mid-run, recording reading-order rather than the text.
- **The chat interface itself** — the work ran as a human-driven loop needing a "continue" every cycle; each cycle re-sent the full growing context and re-authored control logic by hand (which itself introduced bugs), with tens of GB of snapshot churn and forced context-window summarisations — expensive, slow, unreliable.
- **Point-solutions, silent gaps, AI-as-sole-quality-gate** — a standing tendency to patch, postpone, under-weight governance, not surface the full truth, and fabricate when unaudited (a scan gate silently non-operational across whole books; fabricated counts; a 4-month rework loop from one un-audited tool defect) — leading the researcher to no longer trust a single analysis.
- **Infrastructure fragility** — a 2026-06-03 DB loss (a Drive sync truncated the live database) cost ~6 weeks and was only partly recoverable because work was handler-based, not replayable patches.

The reconstruction's own bottom line: fix **two roots — stop over-structuring the subject, and close the gap between what was decided and what the live tools actually do — and most recurring failures stop.** Faced with this record, the first option considered was to **abandon the study as an unachievable objective.** Instead, building this standalone application — to **harness everything learned over the six months and finally enforce it in software** — is taken as the **last chance to rescue the project.** *(Sources: `outputs/markdown/project-reconstruction/01-…` + `02-failures-oversights-rework-log-20260614.md`; `wa-study-foundations.md` §0,§b; `wa-RESET-…-20260625.md` §2–4; `Workflow/Sessionlogs/wa-user-verbatim-messages-20260706.md`; `verse-analysis/proverbs/_reread/wa-proverbs-reread-RETROSPECTIVE-20260714.md`.)*

### 1.3 The six months as an unintended proof of concept

Although the past six months were never framed as a proof of concept, that is what they turned out to be — and on that measure the time was well spent. They proved that **the Bible is a very rich source for understanding how the inner being works**; that **deep original-language word study, read within the context of each verse and its surrounding passage, surfaces observations of remarkable richness that no other approach brings to light**; and that **a consistent, methodical, deep reading across the whole of Scripture — every element accounted for — is the fundamental building block, because therein lies the evidence.** They also proved what the inner being *is*: **not merely a grouping of distinct phenomena, but an interrelated network of operations that behave dynamically under a wide range of influences, triggers, and effects.** And the failures themselves are part of the proof — they demonstrate that inner-being analysis **cannot be reduced to statistical tallies and the summing of a few elements to reach a conclusion.** The subject is real, it is deep, and it demands exactly the disciplined, verse-grounded, relationally-aware method the six months uncovered — which is precisely why abandoning it was rejected, and why the effort now goes into building software that can carry that method reliably.

### 1.4 What the application must achieve and mitigate

The application exists to make the study reliable by moving the rules, the verse-grounding, and the gates **out of a model's memory and a chat loop and into enforced software**:

- **Rules encoded and enforced, not remembered** — every dimension rule, shape, enum, gate, and dependency lives in the configurator and is checked deterministically, so the model can no longer substitute its own method.
- **Mechanical validation is deterministic code; the API is used only for genuine inference** — and every model output is validated against the rules and retried, so extraction-masquerading-as-inference and regex artefacts cannot bank.
- **Completeness redefined as verse-level validity** — a run is "done" only when the content-validity gates pass, never when coverage is merely reached.
- **Autonomous** — no per-cycle babysitting, no context re-sending, no hand-re-authored control logic; runs are gated, tracked, resumable, and replayable in the DB (directly answering the DB-loss lesson).
- **Resists over-structuring** — the object stays a verse-grounded, inference-first, convergence-validated web; clusters/characteristics remain disposable scaffolding the software treats as such.
- **Faithful to the study's own principles and end-point** — DB as sole analytical memory; a finding for every verse with silence valid; STATED-vs-INFERRED provenance; comprehensiveness and robustness as the standing quality bars.

### 1.5 Capitalising on the work already done

The six months are the raw material this application harnesses, not a write-off. They produced: the **written rulebook** (the ve-lexical catalogue plus the cycle/method/readiness/integrity instructions); the **live 3.40.0 database and its measure layer** (verse, morphology, lexicon, spans); the **STEP integration and morphology parser**; a **body of working — if ad-hoc — pipeline scripts** covering every stage; the **deterministic validation gates** already built (readiness, content-validity, drift, the acceptance-sample scoreboard); the matured **focus-point / multi-contributor / infer-don't-extract model**; and — most valuably — the **dozen failure reviews that now serve as the design specification**, each documented failure being a thing the application is built to make impossible. The existing scripts are the **starting point** for the modules, and the failure record is the acceptance test the application must pass.

## 2. Researcher decisions (locked)

- **2.1 Language & framework — PowerShell is the framework.** PowerShell holds the **process logic and orchestration** and **calls Python modules** to do the work. (Windows Task Scheduler is *not* the launcher/framework.) The Python modules carry the DB / STEP / morphology / validation work; PowerShell sequences them, enforces the gates, and manages each run.
- **2.2 Rules, settings, and dependencies live in the configurator — never hard-coded.** The modules are **driven by rules and settings held in the configurator**; the **code methods *are* the process**; and the **process dependencies (which module needs which, in what order, under which gates) are all defined in the configurator, not in code.** Changing a study rule or the pipeline wiring is a configuration change, not a code change.
- **2.3 Build order — plan → whole framework → module-by-module → sustainability go/no-go before the study is touched.**
  1. **Detailed plan first** (this document, once agreed).
  2. **Build the framework for the entire end-to-end** — the full PowerShell orchestration + configurator + tracking + validation shell across all modules — *before* any single module is completed.
  3. **Complete each module and test it** within that frame, one at a time.
  4. **Only once the application concept is confirmed sustainable** is it applied to actually **re-run the study.** The re-run is gated on proving the concept, not assumed.
- **2.4 Existing scripts are a starting point, expected to be substantially rewritten.** The current `scripts/` / `engine/` code is where each module begins, but it is likely to be **substantially rewritten to be fit for purpose** (removing ad-hoc argv parsing, hard-coded provenance/paths, and the conventions that produced prior failures).
- **2.5 Cheapest working model, re-selectable.** The interpretive reads use the **cheapest model that produces valid results**, with the **model tier re-selectable via the configurator** if quality requires escalation. The deterministic validation gate carries quality; the tier is a setting, not a hard-coded choice.

## 3. Application architecture (high level, end-to-end)

The application is a **layered stack**: a PowerShell **framework** (interface + orchestration + run management) drives **Python functional modules** (the pipeline work), both reading a DB-backed **configurator** (rules, settings, dependencies) and sharing **reusable utilities**, over the SQLite **database** as the sole substrate. *(Folder name provisional — see parking lot.)*

```text
Operator ──▶ 3.3.1 Run interface (PowerShell verbs / "slash commands")
                     │
                     ▼
             ORCHESTRATION FRAMEWORK (PowerShell)  ── reads ──▶ 3.3.2 CONFIGURATOR (DB)
             run planner · gate enforcer · run manager           rules · settings · dependencies
             (tracking · debug · errors · checkpoints)                    ▲          │
                     │ invokes (per module, gated)                        │ read     │ read
                     ▼                                                    │          ▼
             3.3.4 FUNCTIONAL MODULES (Python) ── use ──▶ 3.3.3 REUSABLE UTILITIES (Python)
             s1…s9 pipeline segments                       DB · STEP · morphology · auth ·
                     │                                      validation engine · Claude API adapter
                     ▼
             DATABASE (SQLite: study data + app_* config/tracking)
```

### 3.1 Main modules and what they do

**A. Framework modules (PowerShell) — the process logic.**

- **Run interface** — the operator's command surface (verb set, "slash-command-like"); launches/inspects/resumes runs, edits config, sets debug. *(detailed in 3.3.1)*
- **Orchestrator** — reads the configurator, builds the **run plan** for a requested scope (which modules, in what order, with which dependencies and gates), executes modules, **activates prerequisites** when their outputs are missing/stale, and **enforces pre/post gates** (red = halt, amber = log-and-continue).
- **Run manager** — cross-cutting run-time: tracking (run + per-step status), structured logging, **debug controls** (levels), **error reporting**, checkpointing and **resume**, backups, and runtime limits. Everything persisted to `app_*` tables so a run is fully reconstructable.

**B. Service modules (Python) — shared capabilities.**

- **Configurator service** — read/write access to the rules, settings, and dependency graph; validates the config itself; versioned. *(detailed in 3.3.2)*
- **Validation engine** — the deterministic **[C]** rule checker (per-value + per-scope gates); used both as every module's pre/post gate and as the standalone Data-validation module.
- **Claude API adapter** — the only place the API is used; targeted interpretive **[I]** reads, tier chosen from config, rule-prompt cached, output validated → retried → (optionally) escalated.

**C. Functional modules (Python) — the study pipeline** (the nine segments): 1 Get data from STEP · 2 Characteristic-seed maintenance · 3 Prepare reading passage · 4 Stem-master maintenance · 5 Prepare lexical · 6 Characteristic maintenance · 7 Data validation · 8 Prepare data for analysis · 9 Characteristic findings. Each does one job, exposes a standard contract, and is wired by the configurator (its inputs, dependencies, and pre/post gates are config, not code). *(listed in 3.3.4; detailed per-module in a later phase.)*

### 3.2 The pipeline and how it flows

**End-to-end order** (config-defined; the arrows are dependencies, not hard-coded calls):

```text
1 STEP ingest ──▶ 2 Seed maintenance ──▶ ├─ 3 Prepare passage ─┐
                                          └─ 4 Stem master ─────┴─▶ 5 Prepare lexical ──▶ 6 Characteristic maintenance
                                                                                                   │
        9 Findings ◀── 8 Prepare for analysis ◀────────────────── 7 Data validation ◀─────────────┘
```

- **Every module runs inside a gated envelope:** `pre-validate → run → post-validate → checkpoint/track`. The pre/post checks are the validation engine driven by the configurator; a **red** pre-check refuses to run, a **red** post-check refuses to mark the module done.
- **Data validation (7) is dual-role:** it is the pre/post gate every other module calls, *and* a standalone module that runs the full battery (readiness, content-validity, drift, acceptance-sample) and updates the scoreboard. This is where **"done = verse-level validity, not coverage"** is enforced.
- **Dependency activation:** if a requested module's inputs are missing or stale, the orchestrator activates the prerequisite chain first (per the configurator's dependency graph) or halts red with a clear reason — no silent skipping.
- **Genre-aware routing:** passage-preparation and lexical-reading treatment vary by `verse.genre` (poetic two-phase vs narrative cross-verse vs discourse segmentation) — the routing is a configurator rule.
- **Scope & idempotence:** a run is scoped (e.g. by book, then passage, then term-in-verse), **resumable** from its last checkpoint, and **replayable** — all state in the DB, nothing in a chat transcript.
- **Autonomy:** once launched, the orchestrator drives the whole scope without per-cycle prompting; the operator watches the tracking tables / reports.

### 3.3 Building blocks

#### 3.3.1 The run interface (slash-command-like)

A small, consistent **verb set** the operator uses to drive and observe the application (implemented as PowerShell functions/dispatcher; "slash-command" feel). Indicative commands (full catalogue → parking lot):

- `run <module|pipeline> --scope <book|passage|term>` — launch a gated run.
- `status [run]` · `resume <run>` · `stop <run>` — run-time control.
- `validate --scope <…>` — run the validation battery / scoreboard without side-effects.
- `config show|set|load|version|diff` — inspect and change the configurator (rules/settings/dependencies).
- `debug <level>` · `report <run>` — debug controls and run reports.

Principle: the interface only *expresses intent*; **what actually happens is decided by the configurator**, not by command flags.

#### 3.3.2 The configurator *(the elaborate, load-bearing element)*

> **Detailed design: its own document `studyapp/docs/configurator-design.md` — drafted in Appendix A of this plan until we exit plan mode to build.**

The single source of truth for **what the application does, in what order, under which rules** — DB-backed (authoritative), seeded from a human-editable file, versioned, and self-validated. It holds three distinct bodies of content:

- **(a) Study rules (the encoded rulebook).** Per-`ve_nr` dimension definitions (shape: value/pair/event/flag/note; enum domains; pair-direction; mandatory-not-none; self-interpretable); resolution states; Screen-0 consequences; genre-mandatory ledgers; and the gate definitions (integrity I1–I13, verse-coverage, content-validity V1/V2/V3, drift, acceptance-sample). This is what replaces "the model remembering the rules."
- **(b) Pipeline definition (the process wiring).** The modules, their **order**, their **dependency graph**, the **pre/post gates** each must pass, enable/disable flags, scope rules, and genre routing — so the flow in 3.2 is *data*, not code.
- **(c) Settings (operational parameters).** Model tier (re-selectable) and escalation policy; DB path; STEP configuration; provenance tags; thresholds and retry/limits; debug levels; backup/replay policy; budget caps.

Design stance: **nothing about rules, wiring, or run-behaviour is hard-coded** — the code provides *methods*; the configurator provides *the process*. Because this element is elaborate, its internal schema, how rules are expressed, how the config is itself validated and versioned, and how it is edited are all called out in the parking lot for a dedicated design pass.

#### 3.3.3 Reusable utilities

Shared services used by both the framework and the functional modules, so no capability is re-implemented (or re-authored per cycle — a named prior failure):

- **DB access layer** — single standard path, live-schema-aware, transactional, backup-aware.
- **Configurator maintenance** — the **sole write-path** to the configurator: load the seed → **self-validate** (A.5) → version; plus targeted edits (`config set`), version **diff**, and **rollback**; every change audited in `cfg_change_log`. (The read side is the configurator service, 3.1B; this is the update/maintain side.)
- **STEP client** — the local STEP server, with results **cached into the DB** (read persisted `lexicon`/`verse_morphology` first).
- **Morphology parser** — canonical morph-code / stem derivation.
- **Authentication & secrets** — `.env`/key handling (STEP, `ANTHROPIC_API_KEY`), never logged or exported.
- **Validation engine** (3.1B) and **Claude API adapter** (3.1B) — shared by every module that needs them.
- **Git operations** — programmatic commit / branch / push under the project's git discipline (incremental commits, message + branch conventions); keeps outputs and the config seed versioned in git alongside the DB (a second recovery line to the DB-loss lesson).
- **File management** — **archiving** (superseded files → `archive/`), **renaming/versioning** (same-name → version-bump per `file-organisation-rules`), and **manifest update** (rebuild the `file_manifest` after any output or move). Enforces filing-as-first-class governance so nothing is silently overwritten or lost.
- **Common functions** — span/passage/provenance helpers, logging/telemetry, result contracts for PS↔Python.

#### 3.3.4 Functional modules

The nine pipeline segments, each a Python module with a **standard contract** (declares its inputs, dependencies, and pre/post gates *from the configurator*; reports to the run manager):

1. **Get data from STEP** — ingest/refresh the measure layer (verse · morphology · lexicon) from STEP.
2. **Characteristic-seed maintenance** — maintain the candidate seed (`char_candidate` + tags; `ib_characteristic` registry).
3. **Prepare reading passage** — build passages (consecutive candidate-bearing verses) + verse-coverage.
4. **Stem-master maintenance** — build/maintain the stem/morphology master (new; derived from morphology).
5. **Prepare lexical** *(interpretive core)* — per passage/char, produce the genre-mandatory ledger via the API adapter, gated by the validation engine; write `ve_lexical`.
6. **Characteristic maintenance** — derive/maintain `ib_characteristic`; write back roles; families/clusters as disposable scaffolding.
7. **Data validation** — the full gate battery + scoreboard (also every module's pre/post gate).
8. **Prepare data for analysis** — projections/extracts for downstream analysis.
9. **Characteristic findings** — capture/produce evidenced findings from validated lexicals.

*(Per-module inputs/outputs/gates/tables and the substantial rewrite of each reference script are a later phase.)*

### 3.4 The role of the database

- **A new database.** The application starts a **fresh, purpose-built database** rather than continuing the current one. The live DB carries six months of legacy and quarantine tables, method-reset debris, unregistered migration debt (M61–M66), and a `ve_lexical` that mixes ~620k live+legacy rows. A clean DB *is* the "close the gap between what was decided and what the live artefacts are" fix — it avoids inheriting the mess and lets the schema be designed around the data lifecycle below.
- **Schema reuse, made fit for purpose.** It takes the **current DB's schema design as the starting point** — the proven measure layer (verse · morphology · lexicon · spans), the run-tracking pattern, the ve_lexical / pair model — and **redesigns what caused failure** (clean provenance, enforced layer separation, the `cfg_*`/`app_*` tables, no orphan legacy). Sound raw/base data can be imported from the current DB where it is clean.
- **DB principles:**
  - **Sole source of truth** — if it is not in the DB it does not exist; no key observation, rule, or state lives outside it; no parallel documents, no model memory.
  - **The DB drives the application** — it holds the **configurator** (rules · settings · dependencies), the **engine's control/state** (runs · checkpoints · worklist), and the **manifest** (what exists, where, with what provenance). The application reads its own behaviour from the DB.
  - **The DB holds results in four distinct layers (the data lifecycle):**
    1. **Raw data** — untouched from external sources (STEP verse / morphology / lexicon); **immutable**, never overwritten by later processing.
    2. **Base data** — after conversion and methodological processing (spans, passages, stems, seeds) — the mechanical substrate.
    3. **Interpretations** — the analytical layer (findings, observations) from the reads, each marked **STATED vs INFERRED**.
    4. **Prose** — human-digestible components (narratives, digests) derived from the interpretations.
  - **Layer separation + provenance + replayability** — each layer is distinct and provenance-stamped; raw is immutable; every write is a **replayable patch, not an in-place handler**, so a loss is recoverable (the 2026-06-03 lesson).

#### 3.4.1 Data migration (old DB → new DB)

**Governing rule:** migrate what is **raw or expensively-sourced and known-clean**; **regenerate** everything deterministic; and **never carry the failed analysis forward** — archive it read-only as reference, not as authoritative data. The old DB is preserved **read-only as the reference archive** (for provenance and old-vs-new comparison); the new DB is the sole authority.

**Disposition by layer:**

| layer | data | disposition | why |
|---|---|---|---|
| Raw | `verse`, `verse_morphology` (+raw), `lexicon` | **Migrate as-is** (validated) | clean, immutable external-source data; re-fetching from STEP is redundant |
| Base — entry | `word_registry`, `mti_terms`, `wa_term_inventory`, `wa_verse_records` | **Migrate, cleaned** | 6 months of registry curation is worth keeping — but dedup (OT-DBR-009), status-clean, drop orphans on import |
| Base — spans | `verse_span_index` (structural columns only) | **Migrate structure, strip analysis** | keep the mechanical span (verse/word/surface/strongs/morph/stem); **drop** `role`/`char_candidate`/`characteristic`/`ib_char_id` |
| Base — derived | passages, stems, seed/candidate stamping | **Regenerate** | deterministic; rebuilt by the modules, never migrated |
| Interpretations | `ve_lexical` (the reads), `ib_characteristic`, `finding`/findings | **Archive as reference; regenerate** | this is the **failed layer** the re-run replaces — never authoritative in the new DB |
| Interpretations | verification tables (`ve_dimension_scoreboard`, `ve_lexical_verification`, `ve_verification_sample`) | **Migrate as reference / baseline** | the acceptance-test baseline the new build must beat |
| Prose | narratives / digests | **Archive as reference; regenerate** | built on the failed analysis |
| Config / control | `cfg_*`, `app_*`, run history | **New (author fresh)** | rulebook + run state authored in the new model; old run history stays in the archive |
| Legacy / quarantine | `ve_lexical_legacy`, `*_backup`, `*_quarantine_*`, unregistered-migration debris | **Drop** | do not carry the mess forward |

**How it runs:** migration is a **governed, one-time build step** (its own module, under the same rules as everything else). The new DB is stood up with the fit-for-purpose schema, then import runs **in order — raw → cleaned registry/term → stripped spans** — each step **validated on entry** (row-count / FK / null / dedup gates), **provenance-stamped** `migrated-from-<old>@<date>`, written as **replayable patches**, and logged in `app_*`. The base-derived layers (stems, seed, passages) are then **regenerated by the normal modules**, not migrated. A **reconciliation report** (raw-layer parity; registry completeness; old-vs-new diffs for anything regenerated) closes the migration before any study run begins.

**Cross-DB traceability (retain old references).** Because the old DB is **not dropped** and **not everything migrates**, every migrated *and* regenerated row **retains its old-DB identifiers** — old primary keys / FK references, verse references, dimension references — as **reference metadata columns** (e.g. `src_old_id`, `src_old_ref`), so anything in the new DB is **discoverable back in the old DB** for cross-DB queries. Held as *reference values only*, never as a live foreign key into the old DB (that coupling would be brittle). *(Noted risk: this back-link can drift or rot over time — keep it as inert provenance metadata, and treat old-DB lookups as best-effort, not guaranteed. → parking lot.)*

#### 3.4.2 New schema design (principles)

The new schema is **derived, not copied** — the current DB's design is the reference, but the new model is built to the principles below. *(The table-and-relationship model itself is developed in **Appendix B → `schema-design.md`**.)*

**Do:**

- **One authoritative home per fact**, organised by the four data layers — a fact lives in exactly one layer/table.
- **Raw is immutable** — external-source tables are write-once; downstream layers reference, never mutate them.
- **Provenance on every derived row** — source · method · run · version, and STATED-vs-INFERRED where interpretive; every write traceable.
- **Retain old-DB reference keys** — migrated/regenerated rows carry their old-DB identifiers (old PK/FK, verse refs, dimension refs) as **reference metadata** (not live FKs) for cross-DB discoverability (per 3.4.1).
- **Reuse the proven shape** — the measure layer (verse · morphology · lexicon · spans) and the run-tracking pattern.
- **Explicit relationships** — real foreign keys; the **span-id is the join key** (never Strong's-encoded endpoints); manifest tables record what exists and where.
- **Config and control are first-class** — `cfg_*` (definition) and `app_*` (runtime state) are part of the schema, not bolted on.

**Don't:**

- **No legacy/quarantine carry-over** — the accumulated mess (mixed ve_lexical rows, `*_backup`/`*_quarantine_*`, unregistered-migration debris) does not exist in the new schema.
- **No analytical values on mechanical tables** — the failed pattern of stamping interpretation onto spans; layers stay separated.
- **No implicit/undocumented supersession** — schema changes go through the app's own idempotent, versioned migration, never hand-applied outside it.
- **No orphan-tolerant structure** — the candidate⇒verse-record invariant and FK integrity are enforced by the schema + gates, not by convention.

### 3.5 Process management

Cross-cutting run-time governance (owned by the framework's run manager, called out as a first-class concern):

- **Backup** — scheduled full backups **plus pre-operation snapshots** before any write module; off-site/NAS copy; every write captured as a **replayable patch** so state is reconstructable.
- **Restore** — point-in-time restore from backups/snapshots; verify-after-restore; the replayable-patch log enables partial recovery.
- **Logging** — structured, **levelled** (the debug controls); per-run and per-step; secrets never logged.
- **Tracking** — run log, per-step status, checkpoints, metrics, and structured errors in `app_*`; a run is fully reconstructable from the DB and **pinned to the config version it used**.

### 3.6 Outputs

The DB is authoritative; **files are derived, human-facing artefacts** — never the source, always regenerable:

- **Role of files** — external exchange and human consumption (extracts/projections for analysis, review packs, prose deliverables). Nothing authoritative lives only in a file.
- **Reviews** — human-review artefacts (validation reports, the dimension scoreboard, sample audits) produced for the researcher to sign off.
- **Error reports** — structured per-run error output for triage.
- **Filing rules** — output location, naming, and **versioning** conventions (per the project's file-organisation rules); superseded outputs archived, never overwritten.
- **Formatting** — consistent, templated formats (md / csv / json) per output type, so downstream consumers (and AI review) get a stable shape.

### 3.7 Controls

Controls are how the application *guarantees* two things: that the **data is valid**, and that the **process is accountable and reversible**. Every control is **defined in the configurator** (what applies to which data type / process), **executed by the validation engine + run manager**, and **recorded in the DB** — never a matter of a model's judgement in the moment.

#### 3.7.1 Data controls — what makes data valid

- **Validity is per data-type.** Each of the four data layers has its own control set; a unit is "valid" only when it passes the controls configured for its type:
  - **Raw** — ingest controls: source-parity, completeness, no-null, FK integrity. Immutable once passed.
  - **Base** — regeneration controls: derived correctly from raw (span/passage/stem parity) + the integrity invariants (I1–I13, coverage).
  - **Interpretation** — read-validity controls: dimension rules (shape/enum/pair-direction/self-interpretable/mandatory-not-none), ledger completeness, content-validity (V1/V2/V3), drift, the acceptance sample, and STATED-vs-INFERRED provenance.
  - **Prose** — derivation controls: every claim traceable to an interpretation; nothing un-grounded.
- **How it is checked.** The validation engine runs the configured controls **as each unit is written** (the pre/post gates of §3.2); results go to `app_validation_result`; **red halts, amber flags for review, nothing that fails a red control banks.** Every unit therefore carries a queryable validity state — `valid / invalid / amber-review / unchecked` — and completeness is measured as *validity*, not row counts.

#### 3.7.2 Process controls — accountability & reversibility

Every run is fully answerable and undoable:

- **When did it run** — the run log: start/end, **config version used**, scope, and trigger/operator.
- **What did it do** — the per-step record: module, inputs, the writes it made (**as replayable patches**), and metrics.
- **What was the outcome** — status (success / halted / failed), which gates passed/failed, errors, and the validation results.
- **Backtrack** — every write is a **replayable patch + pre-op snapshot**, and provenance-stamped, so any run or step can be **reversed** to its prior state and its writes cleanly identified and removed.
- **Rerun** — runs are **idempotent and resumable**: resume from a checkpoint, or re-run a scope fresh (discarding the prior run's writes by provenance). Reruns are **pinned to a config version** for reproducibility, and honour the study rule *"discard the prior finding, read the data fresh"* — so a rerun is a first-class control, not a patch-over.

These controls sit on §3.5's infrastructure (backup/restore/logging/tracking) and the `app_*` tables; their **definitions** (which control applies where) live in the configurator (Appendix C §C.4, §C.10).

## 4. Grounding facts (from exploration — carry into detailed design)

- Live DB `database/bible_research.db` is **schema 3.40.0**; `create_tables.sql`/JSON are **stale** → build models from the live DB. `migrate.py` registry ends at M60 (M61–M66 applied by scripts) → the app owns its `app_*` tables via its **own idempotent migration**, never relying on `engine --migrate`.
- Measure layer present: `verse` (`passage_id, is_passage_anchor, process_marker, genre`), `verse_morphology` (surface·strongs·morph_code·pos·**stem**), `lexicon` (Strong's gloss). Live-model `ve_lexical` must be filtered by `pair_kind IS NOT NULL` / `source_provenance` (620k rows include legacy+quarantine).
- `ANTHROPIC_API_KEY` present in `.env`. STEP is **local** (`localhost:8989`, no key, **no cache**); env-var names in the client currently mismatch `.env` — standardise in the configurator.
- Run-tracking pattern to mirror: `engine_run_log` / `engine_stream_checkpoint` / `word_run_state` / `term_fetch_log`.
- Rules are almost all **[C] mechanically checkable**; only Screen 0, role assignment, and the semantic content of sense/operation/reading + pair-bindings are **[I]** (need the model).
- No dedicated **stem-master** table exists (derive from `verse_morphology`).

## 5. Parking lot — points needing a home (raised while architecting; to elaborate in later phases)

- **Naming & layout:** application/folder name (was "studyapp"); PS-framework vs Python-module folder structure; repo location under project root.
- **Configurator internals** → now designed in **Appendix A** (→ `configurator-design.md`); residual opens tracked there (rule-expression vs a small DSL, how a gate's check is stored, editing UX beyond seed files, versioning granularity/rollback).
- **Data-layer / new-DB build-out** → the fit-for-purpose schema for the four layers (3.4); the migration disposition is in **3.4.1**, but the **schema redesign per layer**, the cleaning rules for the registry/term import (OT-DBR-009 dedup), and formalising the migration debt (M61–M66) remain a design pass alongside the configurator.
- **Cross-DB back-link maintenance** → the retained old-DB reference keys (3.4.1) can drift/rot as the old DB ages; decide the guarantee level (best-effort vs verified), whether a periodic reconciliation is needed, and exactly which references are worth carrying.
- **PS ↔ Python interface contract:** invocation mechanism (subprocess + JSON in/out?), structured result + error propagation, exit-code semantics, streaming/progress.
- **Run interface:** the full command catalogue; interactive vs scripted; how "slash commands" map onto PowerShell.
- **Model & cost:** which concrete cheapest model; escalation policy and per-dimension tiering; prompt-cache strategy; **budget caps**; how far the deterministic gate can carry quality before human review is needed.
- **Interpretive-quality safety net:** spot-check / human-in-the-loop policy for [I] outputs; how Screen 0 and role assignment (interpretive) are handled at the [C]/[I] boundary.
- **Data strategy:** in-place vs staging writes; the app `source_provenance` tag; backup/replay policy; the migration-debt (M61–M66) — does the app formalise/back-fill it.
- **Re-run strategy:** does the app first **redo the 8 failed dimensions**, or full re-run; relationship to existing data (supersession, provenance); what the sustainability go/no-go (2.3.4) actually measures.
- **Genre routing specifics:** poetic two-phase, discourse segmentation, prophetic oracle-passage variants.
- **Convergence / multi-contributor:** where the **scholarship** witness enters (Zotero?), and how STATED-vs-INFERRED provenance is recorded across contributors.
- **Stem-master:** first-class persisted table vs derive-on-demand.
- **Scope & parallelism:** book vs passage vs term granularity; concurrency limits.
- **Analysis & findings (least-defined):** the study's higher-order outputs (cross-word syntheses, cross-cluster account) sit beyond segment 9 — when/how they enter.
- **Observability:** existing email-alert infra; run reports; what "progress" looks like without a chat.
- **Testing:** parity tests against reference scripts; a regression suite; using the failure reviews as explicit acceptance tests.

---

## Appendix A — Configurator design *(draft; to be extracted to `studyapp/docs/configurator-design.md` on build)*

### A.1 Purpose & principles

The configurator is the **DB-resident definition of everything the application does** — the encoded rulebook, the pipeline wiring, and the operational settings — so that **no rule, dependency, or behaviour is hard-coded**. The code supplies *methods*; the configurator supplies *the process*. Principles:

- **Declarative** — config says *what*; code does *how*.
- **Single source of truth** — the DB config is authoritative at runtime; the human-editable seed files are only *inputs* to it.
- **Self-validating** — invalid config is caught **before** any study run (bad wiring never executes).
- **Versioned & auditable** — every load stamps a version; every change is logged; **every run is pinned to the config version it used** (reproducible).
- **Human-readable seed** — the researcher can read and edit the rulebook and wiring directly.

### A.2 What it holds (three domains)

1. **Study rules (the encoded rulebook)** — per-dimension definitions, enum vocabularies, genre ledgers, Screen-0 consequences, and the validation gates.
2. **Pipeline definition (the process wiring)** — the modules, their order, dependency graph, and the pre/post gates each must pass.
3. **Settings (operational parameters)** — model tier + escalation, DB path, STEP config, provenance tags, thresholds/limits, debug levels, backup/replay policy, budget caps.

Whichever domain, the **atomic unit is a Rule** — a structured object with a fixed **anatomy** (A.10), tagged by the **process** it governs (A.11) and its **kind** (the C.14 sections). The configurator is therefore a *rule store*, queryable along both axes ("all rules governing lexicon", "all enum rules").

### A.3 Structure — the `cfg_*` tables (indicative)

| table | holds | key columns |
|---|---|---|
| `cfg_setting` | operational parameters (domain 3) | scope, key, value, value_type, description |
| `cfg_enum` | controlled vocabularies | enum_group, value, ordinal, notes |
| `cfg_dimension` | the per-`ve_nr` rulebook | ve_nr, label, shape, pair_from, pair_to, mandatory, self_interpretable, derivation `[C\|I]`, enum_group, definition, rule_ref |
| `cfg_ledger` | genre × role mandatory dims | genre, role, ve_nr |
| `cfg_gate` | validation gates | gate_code, name, gate_type, severity, check_spec, scope |
| `cfg_module` | functional modules | module_code, name, ordinal, enabled, handler, description |
| `cfg_dependency` | the dependency graph | module_code, depends_on, activation `[auto\|halt]`, condition |
| `cfg_module_gate` | which gates run pre/post per module | module_code, phase `[pre\|post]`, gate_code, on_fail `[halt\|warn]` |
| `cfg_route` | genre routing rules | genre, treatment, params |
| `cfg_version` / `cfg_change_log` | version + audit of config | version_id, loaded_at, source_hash, note / (version_id, table, key, old, new) |

### A.4 How it works (lifecycle)

1. **Author/edit** the seed files under `config/` (YAML/JSON) — the human-readable rulebook + wiring + settings.
2. **`config load`** → **self-validates** (A.5) → writes `cfg_*` → stamps a new `cfg_version` (with a hash of the seed).
3. **Runtime** — the framework (PowerShell) and modules (Python) read `cfg_*` through the config API; **no file reads during a run**.
4. **Reproducibility** — every run records the `cfg_version` it used; a run can be replayed against the exact config.
5. **Change** — edit seed + reload (phase 1); `config set` for single settings (later); a UI (future). All audited in `cfg_change_log`.

### A.5 Config self-validation (runs at load, before any study run)

- every `enum_group` referenced by a dimension/gate exists in `cfg_enum`;
- every `ve_nr` in `cfg_ledger` exists in `cfg_dimension`; every pair-dim has `pair_from`/`pair_to`;
- every `gate_code` in `cfg_module_gate` exists in `cfg_gate`; every `depends_on` in `cfg_dependency` exists in `cfg_module`;
- the dependency graph is **acyclic**; every module `handler` resolves;
- **invalid config → load rejected with a precise error; no run proceeds on invalid config.**

### A.6 Access

- **Python** — a `config` read module: `get_setting`, `get_dimension`, `get_ledger(genre, role)`, `get_gates(module, phase)`, `get_dependencies(module)`.
- **PowerShell** — a thin config accessor (queries `cfg_*` or calls the Python config module) so the orchestrator can build the run plan.
- Both read the **same `cfg_*` tables** — one source.
- **Write/maintain** — all changes go through the **Configurator-maintenance utility** (3.3.3): the single write-path (load · validate · version · edit · diff · rollback), audited in `cfg_change_log`. No module writes `cfg_*` directly.

### A.7 Worked example (how one rule flows with zero hard-coding)

- `cfg_enum(locus)` = {internal:ib-state, external:god, external:person, …}.
- `cfg_dimension` row for **ve_nr 116 (locus)**: shape=`value`, mandatory=1, self_interpretable=1, derivation=`C`, enum_group=`locus`.
- `cfg_gate('V1_locus_domain')`: type=value-domain, severity=red, check = value ∈ enum(`locus`).
- `cfg_module('prepare_lexical')` + `cfg_module_gate(prepare_lexical, post, V1_locus_domain, halt)`.
- **At run time:** `prepare_lexical` post-validate loads the `locus` enum + the gate from config and checks every locus value; any off-domain value **halts** the module. Nothing about locus — the model, the vocabulary, the gate, or the wiring — is in code; it is all configuration. Change the enum or the gate → behaviour changes with no code edit.

### A.8 Config-specific open questions

- **Rule expression** — plain rows vs a small rule DSL for complex gates; how a gate's `check_spec` is stored (named Python check + parameters? a query id? an expression?).
- **[I] interpretive rules** — how Screen 0, role assignment, and read-guidance are represented in config (prompt fragments / guidance text) vs left to the model.
- **Editing UX** — beyond seed-file + reload (validation-aware editor? command surface? later UI).
- **Versioning** — granularity, diffing, rollback; relationship between `cfg_*` (definition) and `app_*` (runtime state).
- **Precedence** — seed-file vs live DB edits when both change.

### A.9 Running index of configuration segments / nodes  *(LIVING — add as we surface them; the point is to spot what's missing)*

Every node below is a distinct configurable thing that needs a home + a canonical value + a status (LIVE/LEGACY). Grouped by candidate config section (C.14). `[ ]` = not yet designed.

**Vocabularies / enums**
- [ ] Lexical enums — resolution · role · type · object-type · locus · device · direction · pair_kind · genre · gate · segment-unit-type
- [ ] Status vocabularies — session_b_status · verse_context_status · phase1_status · evidential_status · term_owner_type · source_list · dimensional-weight · cluster.status · observation.status/provenance · prose_section.status/author
- [ ] Flag-code sets — research_flags (17) · phase2_flags (25) · crosslink_type (11) · data_quality_flags (9)

**Dimensions**
- [ ] Dimension definitions (ve_nr 101–118: shape · pair-direction · mandatory · derivability [C]/[I] · genre applicability)
- [ ] Dimension value-rules (self-interpretable; assess-from-qualifier / never-ABSENT)
- [ ] Dropped/deprecated-dimension register

**Characteristics / seed / registry**
- [ ] Word registry (the ~214 words; growth policy; registry-path rule)
- [ ] Candidate-seed rules (seed layers; char_candidate; over-inclusive/non-exhaustive)
- [ ] `ib_characteristic` keying/grain (base-lemma + ESV; two-phase build)
- [ ] Characteristic families / clusters (disposable scaffolding — if retained at all)

**Ledgers**
- [ ] Genre × role mandatory ledgers (poetic-base vs M16; per-role: characteristic/qualifier/standalone)

**Gates, measures & verdicts**
- [ ] Integrity invariants (I1–I13) · [ ] Readiness verdict classes + check groups §A–F · [ ] Verse-coverage gate
- [ ] Content-validity V1/V2/V3 · [ ] Band-drift · [ ] Success measures G0–G10 · [ ] Acceptance-sample config (n · threshold)
- [ ] Two-gate content-span rule · [ ] Sanity-check gate + rollup-by-role · [ ] Per-cycle/book-close cadence gates · [ ] Synthesis-B gates

**Pipeline & wiring**
- [ ] Module registry (the segments) · [ ] Module order · [ ] Dependency graph · [ ] Per-module pre/post gates
- [ ] Staged sequence · [ ] Candidate⇒verse-record invariant · [ ] Passage rule (char-continuity params) · [ ] Stage-0 layout
- [ ] Genre routing (poetic 2-phase · discourse D/S/C/T/F · prophetic oracle · prose cross-verse · Phase-0 backfill)
- [ ] Worklist definitions · [ ] Two-orthogonal-axes rule

**Screen & role model**
- [ ] Screen 0 (IB-relevance) · [ ] bearer≠God · [ ] role homes + per-role ledgers · [ ] outward-glory→standalone · [ ] char-driven-read

**Read-quality & guardrails ([I] guidance the app enforces)**
- [ ] LRT · [ ] read-back/self-check · [ ] digestion budget · [ ] passage-reading checkback gate · [ ] resist-grouping · [ ] completeness≠validity · [ ] meaning-grounded-not-imported

**Principles (standing guidance)**
- [ ] The nine principles · [ ] focus-point model · [ ] infer-don't-extract · [ ] convergence-validity · [ ] STATED/INFERRED · [ ] multi-contributor · [ ] scaffolding-not-reality

**Controls**
- [ ] Data-control sets per data-type (raw/base/interpretation/prose) · [ ] Process-control policy (backtrack/rerun/idempotence) · [ ] Cadences (cycle size · snapshot every N · rebuild every N · batch size)

**Provenance & completion**
- [ ] Provenance tags/markers (read-2026 · source_provenance · process_marker · migrated-from) · [ ] Cross-DB old-ref map
- [ ] Completion definitions (verse-level validity) · [ ] silence-is-a-finding · [ ] soft-delete discipline · [ ] field-authority (canonical column per fact)

**Naming / filing / patterns**
- [ ] File-naming patterns · [ ] Label patterns · [ ] Versioning rules · [ ] Filing rules (archiving triggers · living-doc)
- [ ] **Folder structure** (app layout + output-tree homes: verse-analysis/{book}, archive/, outputs/…) · [ ] Output formats · [ ] Zero-pad rules
- [ ] Patch-type registry + operations · [ ] Directive spec (5 elements) · [ ] two-and-only-two change mechanisms

**Governance rules**
- [ ] Global rules (GR-*) · [ ] Programme flags (FLAG-*) · [ ] Interaction protocols · [ ] Behaviour guardrails (no-forced-structure · plausibility≠truth · all-work-in-DB · rules-encoded · root-fix · remove-discretion)

**Settings & constants**
- [ ] Model tier + escalation policy · [ ] Budget/cost caps · [ ] STEP config · [ ] DB path · [ ] Backup/retention/NAS policy · [ ] Secrets/keys · [ ] Engine constants/thresholds

**Reference / version registers**
- [ ] Reconciliation/canonical-value register (C.13) · [ ] LIVE/LEGACY supersession register · [ ] Config schema (`cfg_*`) · [ ] Config self-validation rules (A.5) · [ ] Config version register

**Study end-point / products (further out — flagged so they aren't forgotten)**
- [ ] Three orders of output (records · syntheses · account) · [ ] Audiences (scholar/leader/reader) · [ ] Milestones M1–M3 · [ ] Science-lens policy (secondary corroborator) · [ ] Standing-question catalogue (VE/SYNTH)

### A.10 The anatomy of a rule *(what a rule IS — the attributes every rule carries)*

Every rule in the configurator is a structured object with these attributes (mapping the researcher's questions):

| researcher's question | attribute | what it holds |
|---|---|---|
| what it is | **statement** | the rule's plain assertion |
| how it is defined | **form** | how expressed: enum-domain · threshold · shape / pair-direction · gate-check · procedure · principle · pattern · setting |
| where does it come from | **authority** | the authoritative decision/document it derives from (the rule's own provenance) |
| where is it found | **reference** | the doc §/`[current]` pointer where it is stated |
| what is its make-up | **composition** | its parts: subject · condition · value/threshold · scope |
| where is it located | **location** | the `cfg_*` node/table that stores it |
| what is it meaning | **intent** | what it means / why it exists (semantics) |
| when is it right/true/correct | **satisfaction** | the pass condition — when the data or process complies |
| how is it validated | **validation** | the check that enforces it: **[C]** deterministic code/gate, or **[I]** model + gate + retry |

Plus lifecycle attributes on every rule: **id · governs (process) · kind · status (LIVE/LEGACY) · version · canonical-or-alias-of**. This anatomy is the answer to "how it needs to be captured": one `cfg_rule` core carrying these attributes, with kind-specific sub-tables (enum values, dimension shape, gate spec, ledger membership) hanging off it. *(Reshapes A.3 toward a rule-centric schema — see A.8.)*

### A.11 Rules grouped by process *(the second axis — mirrors the pipeline / functional modules)*

Rules are indexed not only by kind (C.14) but by the **process they govern**. The by-process rule-sets (each ≈ a functional module):

1. **Registry (initial word list)** — what qualifies a word as inner-being; registry-path (existing-first); growth/addition policy; `source_list`/`origin`; registry-dimension tags. *(≈ module 2)*
2. **Fetch from STEP** — what to fetch and how; Strong's resolution + suffix handling; pagination / 60-cap sectioning; retry; **cache-to-DB-first**. *(≈ module 1)*
3. **Raw data** — what "raw" is; **immutability**; source-parity / completeness / no-null / FK controls; provenance stamping. *(≈ module 1 output / measure layer)*
4. **Verses / passages** — passage rule (char-continuity; anchor; ≥2 / single-verse; no whole-chapter); verse-coverage; genre routing; candidate⇒verse-record invariant. *(≈ module 3)*
5. **Lexicon (the per-term lexical layer)** — sense = STEP sub-gloss authority; the ve_nr dimension rules + ledgers; self-interpretable / never-ABSENT; grain; stem master. *(≈ module 5)* *(⚠ naming: "lexicon" here = the lexical-decomposition layer, distinct from the Strong's-gloss `lexicon` table — reconcile the term.)*
6. **Characteristics** — Screen 0; candidate seed; role model + per-role ledgers; `ib_characteristic` meaning-keying; char-driven read. *(≈ module 6)*
7. **Findings / observations** — finding = universal DB unit; STATED-vs-INFERRED; silence-is-a-finding; validity-by-convergence; the observation-record fields. *(≈ module 9)*

A rule may govern more than one process (e.g. provenance rules span all). Querying a process returns its full governing rule-set — which is also what a module loads before it runs.

### A.12 How the configuration is captured — JSON seed → DB

**Medium: per-section JSON seed files now; the DB is authoritative at runtime later.** The configuration is captured as JSON under `config/` — human-editable, **git-versioned** (diffable history), and well-suited to heterogeneous sections. At build time a **loader** self-validates them (A.5) and writes them into the new DB (authoritative at runtime, A.4). *(Why JSON now, not the DB: the new fit-for-purpose DB isn't built yet and we won't touch the old one; JSON is the seed layer the design already calls for, and it captures diverse, still-evolving sections cleanly.)*

**Common envelope + section-specific `spec`** — every item shares the A.10 rule-anatomy envelope; its `spec` is shaped per kind, and the loader validates each kind against its own spec-schema (this is how "different sections need separate elements" is honoured):

```json
// config/dimensions.json — one entry
{
  "id": "dim.116.locus",
  "governs": ["lexicon", "characteristics"],
  "kind": "dimension",
  "status": "LIVE", "version": 1,
  "authority": "researcher 2026-07-04",
  "reference": "wa-ve-lexical-catalogue-v1 §9",
  "intent": "classify the target/bearer entity as IB-internal vs external",
  "satisfaction": "value in enum:locus",
  "validation": { "axis": "C", "check": "value-in-domain", "enum": "locus", "severity": "red" },
  "spec": { "ve_nr": 116, "shape": "value", "mandatory": true, "self_interpretable": true, "derivation": "C", "enum": "locus" }
}
```

**File layout** (one file per config section; a rule is listed once and referenced by process via `process-index.json`):

```text
config/
  enums.json · dimensions.json · ledgers.json · gates.json
  pipeline.json      (modules · order · dependencies · module-gates)
  screen-role.json · read-quality.json · principles.json · provenance.json
  patterns.json      (file/label/patch/directive/versioning)
  governance.json    (GR-* / FLAG-* / interaction protocols)
  settings.json · reconciliations.json (canonical + LIVE/LEGACY) · process-index.json
  _manifest.json     (config version + per-file hash)
```

**Rework / expand:** editing = edit the JSON + reload; git is the history; `reconciliations.json` records the C.13 canonical-value decisions as we make them; per-kind spec-schemas let each section grow independently. Populating these files is the **first concrete build artifact** and doubles as continuing the configurator design in a proper medium.

---

## Appendix B — New DB schema design *(draft; to be extracted to `studyapp/docs/schema-design.md` on build)*

> The home for **deriving the new table-and-relationship model**, built to the principles in §3.4 and §3.4.2. Populated in a dedicated design pass; below is the frame and the layer→table families to derive against.

### B.1 Derivation approach

- Start from the **live 3.40.0 schema** (the only authoritative reference — the `.sql`/JSON files are stale) as the shape to keep or improve.
- **Keep what's proven** (measure layer, the ve_lexical value/pair/event/flag model, the run-tracking pattern); **redesign what failed** (provenance, layer separation, config/control tables, integrity).
- **Map every table to exactly one layer** (raw · base · interpretation · prose, + config + control), with naming that signals the layer.
- Fix keys, FKs, provenance columns, and the manifest **before** enumerating every table.

### B.2 Table families by layer (to derive)

- **Raw** (measure layer, write-once from STEP): verse · verse_morphology · lexicon.
- **Base** (mechanical/deterministic): span index · stem master · passages · term registry · candidate seed.
- **Interpretation** (provenance + STATED/INFERRED): the per-verse lexical (`ve_lexical` successor) · findings · observations · characteristics.
- **Prose** (derived, human-facing): narratives · digests.
- **Config** (`cfg_*`): the configurator (Appendix A).
- **Control** (`app_*`): runs · steps · checkpoints · worklist · validation results · manifest.

### B.3 Conventions (to fix in the design pass)

- Naming (layer-prefixed), primary keys, FK style, the span-id join rule, provenance columns (source · method · run_id · version · stated/inferred), immutable-append vs soft-delete, timestamps.
- The **manifest** — which tables record "what exists, where, with what provenance" — and how completeness/coverage is queried from it (completeness = verse-level validity, not row counts).
- The **migration mechanism** — the app's own idempotent, versioned migration; never reliant on `engine --migrate` (M61–M66 debt).

### B.4 Open (schema-specific)

- Exact successor design for `ve_lexical` (the pair/value/event/flag model, cleaned of legacy).
- Interpretations: **append-only + supersession (replayable)** vs update-in-place.
- The stem-master table shape (none exists today).
- How the four layers physically separate (name-prefixes vs separate schemas vs attached DBs).
- A **table-by-table reuse-vs-redesign pass** over the live 3.40.0 tables.

---

## Appendix C — Configurator content inventory (collation) *(working list; feeds Appendix A)*

> Collated from three scans — (1) Instructions/Catalogue/schema (dimension rules · gates · vocab), (2) Global_rules/reference/constants (governance · patterns · settings), (3) methodology/memory (principles · process · guardrails). **Every item below must find a home in the configurator.** Two cross-cutting facts shape the model: **(i)** many enums have the *same concept defined 3–4 ways* with divergent values across docs / DB `wa_vocab_*` / SQL free-text columns — the configurator must store **one canonical value + its aliases/supersession** (see C.13); **(ii)** the method is **mid-paradigm-shift**, so every item carries a **status: LIVE / LEGACY / MOVING**, and the configurator holds the current rule and marks the superseded (versioned).

### C.1 Controlled vocabularies & enums
Lexical dimension enums: **resolution** (span/inferred/unknown/none-silent) · **role** (⚠4 variants) · **type** (action/status/quality) · **object-type** (person/God/group/thing/abstract/spiritual-being) · **locus** · **device** (12) · **direction** (6) · **pair_kind** (pair/value/event/flag/note) · **genre** (6) · **gate** (1-primary/2-relevant) · **segment-unit type** (D/S/C/T/F). Status/pipeline vocabularies: **session_b_status**, **verse_context_status**, **phase1_status**, **source_list**, **registry dimensions** (14), **origin**, **dimensional-weight** (PRIMARY/SECONDARY/PERIPHERAL), **evidential_status** (5), **term_owner_type** (OWNER/XREF), **language/testament**, **mti_terms.status**, **cluster.status**, **cluster_finding.finding_status**, **observation.status/provenance**, **prose_section.status/author** (the only SQL-CHECK enums). Flag-code sets: **research_flags** (17), **phase2_flags** (25), **crosslink_type** (11), **data_quality_flags** (9). *Values live in REF doc + DB `wa_vocab_set`/`wa_vocab_member` (canonical post-M32) — SQL enforces almost none. Pull members from the live DB.*

### C.2 Dimension rules (ve_nr 101–118)
Per ve_nr: **shape** (value/pair/event/flag/note) · **pair-direction** (e.g. source driver→term, target term→object, bearer human→term) · **mandatory-or-none** · **morphology-derivability** [C]/[I] (8 reliable, 6 partial, 115 read-only, 114 note) · **genre applicability** (103/111 cross-verse). Governing value-rules: **self-interpretable** (readable without the verse) · **assess-from-qualifier / never silently ABSENT** (109/110/111/117/118 record `none`). Dropped dims (valence/hidden/cohabitation/related_tier). ⚠ master-list drift (CAT 101–118 vs cycle 101–116).

### C.3 Genre-mandatory ledgers (genre × role → ve_nr set)
Poetic base-M (07-11) vs expanded **M16** (07-14) · narrative adds 103/111 · per-role ledgers (characteristic full / qualifier reduced / standalone minimal) · **`none` written not omitted**. ⚠ the 07-11↔07-14 change is a hard reconcile (C.13).

### C.4 Validation gates, measures & verdicts
**Integrity** I1–I13 (I12 == D1/D2; ⚠ numbering) · **readiness** verdict classes (READY / READY-WITH-DEBT / NOT READY) + check groups §A–§F + **verse-coverage** arithmetic · **content-validity** V1 value-domain / V2 band-drift / V3 tag-consistency · **G0–G10** success measures · **scored read-back audit** (25-unit stratified / 2–3-passage per-cycle; ≥90% sound, zero fidelity fail) · **two-gate content-span** rule · **sanity-check** gate + rollup-by-role · **per-cycle/book-close cadence** gates · **synthesis-B** gates (emergence/validity/singleton/Logos-L1.5/no-isolation). *(The n=200/95% acceptance rule you set this session is not yet in any doc — it becomes config here.)*

### C.5 Process / pipeline wiring rules
Staged sequence (seed→term→verse-record→passage→read→integrity) · **candidate⇒verse-record invariant** (I2, halt-and-restore) · two orthogonal axes (char_candidate vs role) · **passage rule** (char-continuity v2; anchor=first; single-verse allowed; ≥2 maximal; no whole-chapter) · Stage-0 whole-book layout precompute · per-verse DB-update ledger (key on span-id) · ib_characteristic meaning-keyed grain (base-lemma + ESV) · seed layers (registry→synonyms→judgement→discovery) · worklist definitions (missing/incorrect lexical) · registry-path (every char is a registered term) · single-authoritative-doc-set rule · finding = universal DB unit · grain = per-occurrence sub-gloss.

### C.6 Genre routing rules
Poetic two-phase (Phase-1 per-verse cross-verse-OFF; Phase-2 whole-poem) · discourse segmentation (D/S/C/T/F + multi) · Proverbs F-frame split · prophetic oracle-passage · prose cross-verse-ON (+103/111) · Phase-0 chapter backfill (sparse measure layer) · narrative span-depth vs movement-depth (debt).

### C.7 Screen 0 & role model
Screen 0 IB-relevance (human inner being = lens; God = arena) · **bearer ≠ God** · God-qualifier never standalone (widen passage) · pure-God verse yields no char · outward-glory → standalone · role homes {characteristic/qualifier/standalone/uncertain} (⚠ enum + qualifier flip-flop) · per-role ledgers (D2) · char-driven read (not span-sweep).

### C.8 Read-quality rules (the [I] read-guidance the app enforces)
Lexical Revelation Test (7 checks, step-3 gate) · read-back / self-check · depth-no-drift / multi-lens / each-chapter-as-first · digestion budget (~12 spans, poetic-tunable) · **passage-reading checkback gate** · resist-grouping / preserve-distinctions · **band-drift** distributional check · **completeness ≠ validity** · meaning-grounded-not-imported · verify-contributor-reference-first.

### C.9 Methodological principles & governance guardrails
Principles: the **nine principles** · focus-point (7 properties) · **infer-don't-extract** · validity-by-convergence · **STATED-vs-INFERRED** · multi-contributor spiderweb · characteristics→movements · scaffolding-not-reality · term=sense-not-lemma · whole-inner-life scope · working-definition + 3 tests. Guardrails (from failure reviews): **no forced structure** · a-failed-structure-is-data · **plausibility ≠ truth** · measurement-informs-never-decides · **all-work-in-DB** · **rules-must-be-encoded** · root-fix-not-one-off · remove-discretion/mechanical-first · bias-to-surface-not-discard · char-list-validates-never-imputes · ground-in-per-verse-VARYING-evidence · traceability/cold-read · confirm-before-acting / review-via-files / proceed-autonomously-once-set · filing-first-class · weight-governance-layers.

### C.10 Provenance, completion & DB-discipline conventions
read-2026 / source_provenance / process_marker markers · **completeness = verse-level validity** (not coverage) · **silence is a valid finding** (STATE_SILENT) · set-aside = reversible soft-delete · all-findings-are-drafts (sift earns robustness) · baseline-then-delta · reproducibility (re-read → same result) · soft-delete discipline (no physical deletes) · field-authority (canonical column per fact).

### C.11 Naming / label / patch / directive patterns & filing
File-name patterns (23) · label patterns (11) · **versioning rule** (same-name→bump; `-v{n}` vs governing `-v{major}_{minor}` ⚠) · living-document rule · per-tree homes · archiving triggers · **patch-type registry** (~15–20; DB canonical) + operation types + 6-check self-check · **directive spec** (5 required elements) · two-and-only-two change mechanisms · output-format-by-purpose · zero-pad rules (Strong's 4, chapter 3).

### C.12 Global governance rules, interaction protocols, thresholds, constants & settings
**GR-*** rules (cadence · data-discipline · referencing GR-REF-002 · file GR-FILE-* · process · programme-model GR-PROG-* · researcher-direction) · **FLAG-*** programme flags (incl. FLAG-010 blocking gate) · **interaction protocols** (confirm-before-acting · outputs-to-md · factual-discipline · terminal) · **engine constants** (EXPECTED_SCHEMA_VERSION, thresholds HIGH_FREQ/THIN_DATA/…, sentinels, retention, stale-lock) · **cadences** (cycle ~12 passages, snapshot every 5, rebuild every ~5, batch 5–8) · **settings** (STEP url/version/timeout + local-server + 60-cap, DB path ⚠, backup/retention/NAS, secrets/`ANTHROPIC_API_KEY`, model tier). ⚠ gaps: no explicit cost/token-budget rule; no NAS/off-site policy in files.

### C.13 Reconciliations & live-vs-legacy *(the design-critical decisions the configurator must resolve — one canonical value each)*
1. **`role` enum** — 4 divergent value-sets → pick one canonical + alias map.
2. **Mandatory ledger** — 07-11 poetic-base vs 07-14 M16 (109/110/111/117/118 optional→mandatory; 103/111 per-span vs Phase-2).
3. **ve_nr master list** — 101–118 (CAT) vs 101–116 (cycle).
4. **Integrity numbering** — "I1–I11" vs actual I1–I13 (I12 double-named D1/D2).
5. **Resolution-state vocab** — 3 variants across CAT/01b/collection.
6. **Controlled-vocab home** — REF doc vs DB `wa_vocab_*` vs SQL free-text vs patch synced-copy (4 stores).
7. **Acceptance sample** — 25-unit / 2–3-passage (docs) vs the n=200/95% set this session — decide the canonical.
8. **Live vs legacy paradigm** — pre-reset (tier / 189-question / cluster / Session-A–D) vs RESET (focus-point / verse-fan-out / movement); config captures LIVE, marks LEGACY, records supersession edges (change-over 2026-06-25; qualifier 07-07↔07-12; passage-rule v1→v2→char-continuity).

### C.14 What this implies for the configurator's segments
The inventory groups naturally into these **config sections** (refining the three domains + `cfg_*` tables in Appendix A): **(1) Vocabularies/enums** · **(2) Dimensions** · **(3) Ledgers** · **(4) Gates, measures & verdicts** · **(5) Pipeline & wiring** (modules · order · dependencies · staged-sequence · passage rule · seed · genre routing) · **(6) Screen & role model** · **(7) Read-quality & guardrails** (the [I] guidance + the checkback gates the app enforces) · **(8) Principles** (standing guidance) · **(9) Provenance & completion** · **(10) Patterns & filing** · **(11) Governance rules** (GR/FLAG + interaction protocols) · **(12) Settings & constants** · **(13) a Reconciliation/version register** (canonical-value decisions + LIVE/LEGACY supersession). Appendix A's `cfg_*` set expands to cover these — notably a **status/version field on every config item** and an **alias/supersession** structure.

**Still to pull for completeness** (named by the scans, outside their scope): live-DB `wa_vocab_set`/`wa_vocab_member` member rows; the `Workflow/Tiers/` catalogue (exact standing-question counts + the VE/SYNTH question inventory); `database-schema-v3.35.0-…json` full column/enum inventory; the versecontext `vc_status` R1–R3 rules; the registry-management vocab.
