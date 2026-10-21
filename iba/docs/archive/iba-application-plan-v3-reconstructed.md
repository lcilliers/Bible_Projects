# Plan: Inner Being Analysis Programme — segmented, autonomous, DB-driven application

iba-application-plan-v3-reconstructed

This document is reconstructed from several documents to include different parts of the plan that is spread across the documents.

## Why is it reconstructed: 
AI lost portions of the work, mid stream in assembling the finding of the preparation of the second layers of the app, namely the analytic and findings section of the app.
The data layer of the plan, and the building of the app from the plan is largely complete and in operation, except for the rebuilding of the passages tables.  The working of the passages table have been defined.
The analytic layer plan is not complete. This is now fragmented and need further work for the plan to build the app.

AI scope of operation: Claude caused significant rework. The reasons are well documented over the past 6 months. Claude **does not have permission to work on this study** outside of the **scope of the IBA app**. Claude must use the **approved app methods for all updates and changes** to the IBA DB. If the methods to perform a task is not in the app, then Claude must **first assist the researcher to build the modules** in plan mode, update the IBA App and then run the task to update the DB.

## 1. Context — why the IBA App

### 1.1 What the study is

The **Inner Being Analysis Programme** (owner: le Roux Cilliers, sole researcher and final authority on scope and method) is a structured academic Bible-research programme whose object is **how Scripture expresses the workings of the human inner being** — Scripture's depiction of the whole inner life (moral, emotional, volitional, relational, vertical and horizontal), with no specific theological bias and the human in focus is in scope. It grew out of two earlier ~100-page AI studies (*Spirit, Soul and Body*; *The Holy Spirit*) whose findings **"appeared strong at first but deteriorated under further questioning"** and badly understated the inner being's characteristics. The programme therefore measures itself against the **two quality bars those studies failed: comprehensiveness (nothing understated) and robustness (findings that withstand deeper questioning).**

It works from an initial registry of ~214 inner-being words, growing over time, each mapped using the STEP Bible to its Hebrew/Greek originals via Strong's and captured in a SQLite database processed by a custom engine — but the word registry is **scaffolding, not the object.** The analytical unit is a **focus point**: a latent, emergent, dynamic configuration of the inner being that can never be observed or logged directly, only **inferred** from the **operations** a verse describes it performing. Hence the governing method — **infer, don't extract** (read the verse *backward*: this act happened, what inner reality produced it? — never *forward* by lexical surface); the object modelled as a **process / relational web** read off *what each verse does* rather than a grid of named parts; and validity established by **convergence** of independent witnesses (a mechanical-lexical floor + AI conceptual synthesis + scholarship, each grounded to verses and marked **STATED vs INFERRED**). Nine documented principles govern it (registry completeness; collate-before-analyse; no forced categories — patterns emerge from evidence; verses qualify by original-language occurrence; every finding substantiated with no guessing; read the data as a whole; the DB is the analytical memory; biblical lens primary / science secondary; synthesis bottom-up). 

### The **IBA App end point** 

**Raw data**: A corpus of **verses** from the Bible in the IBA db, sourced through STEP bible, describing the **workings of the inner being**, dissected by Strong, Strong meaning and into the span in the verses. The span is roughly earmarked as inner being relevant - called **characteristics**. 
**Study Unit**: The study units transition the **verses** to contextual units of Inner Being relevant **characteristics** verses, often found in passages, rather than individual verses. This consists of a 18 dimensions of lexical analysis for each characteristic in each study unit to confirm the role of the span in the workings of the Inner Being.
**analysis"": based on the lexical analysis, findings are held entirely in the DB (a finding for every verse — **silence is a valid finding**). Findings are based on the context of verse passages (study unit). The outcome of the findings are organised in a concordance (index of characteristics to verses), descriptions of the operations of the characteristics as evidenced from the lexical, and a contextual description of the meaning of the characteristic in the passage.
**outcome** : with the concordance, products are drawn from meanings — essays, study guides, ebooks/books, sermon series — for three audiences (scholar; leader/teacher; ordinary reader). 

### 1.2 Why an application, and why now

In a nutshell:-It is the only way to secure consistency and completeness in a study that is likely to span many months if not years.

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

### 1.3 The six months as an unintended proof of concept

Although the past six months were never framed as a proof of concept, that is what they turned out to be — and on that measure the time was well spent. They proved that **the Bible is a very rich source for understanding how the inner being works**; that **deep original-language word study, read within the context of each verse and its surrounding passage, surfaces observations of remarkable richness that no other approach brings to light**; and that **a consistent, methodical, deep reading across the whole of Scripture — every element accounted for — is the fundamental building block, because therein lies the evidence.** They also proved what the inner being *is*: **not merely a grouping of distinct phenomena, but an interrelated network of operations that behave dynamically under a wide range of influences, triggers, and effects.** And the failures themselves are part of the proof — they demonstrate that inner-being analysis **cannot be reduced to statistical tallies and the summing of a few elements to reach a conclusion.** The subject is real, it is deep, and it demands exactly the disciplined, verse-grounded, relationally-aware method the six months uncovered — which is precisely why abandoning it was rejected, and why the effort now goes into building software that can carry that method reliably.


### 1.5 Capitalising on the work already done

The six months are the raw material this application harnesses, not a write-off. They produced: the **written rulebook** (the ve-lexical catalogue plus the cycle/method/readiness/integrity instructions); the **live 3.40.0 database and its measure layer** (verse, morphology, lexicon, spans); the **STEP integration and morphology parser**; a **body of working — if ad-hoc — pipeline scripts** covering every stage; the **deterministic validation gates** already built (readiness, content-validity, drift, the acceptance-sample scoreboard); the matured **focus-point / multi-contributor / infer-don't-extract model**; and — most valuably — the **dozen failure reviews that now serve as the design specification**, each documented failure being a thing the application is built to make impossible. The existing scripts are the **starting point** for the modules, and the failure record is the acceptance test the application must pass.

## IBA Application rules

The application exists to make the study reliable by moving the rules, the verse-grounding, and the gates **out of a model's memory and a chat loop and into enforced software**:

- **Rules encoded and enforced, not remembered** — every dimension rule, shape, enum, gate, and dependency lives in the configurator and is checked deterministically, so the model can no longer substitute its own method.
- **Mechanical validation is deterministic code; the API is used only for genuine inference** — and every model output is validated against the rules and retried, so extraction-masquerading-as-inference and regex artefacts cannot bank.
- **Completeness redefined as verse-level validity** — a run is "done" only when the content-validity gates pass, never when coverage is merely reached.
- **Autonomous** — no per-cycle babysitting, no context re-sending, no hand-re-authored control logic; runs are gated, tracked, resumable, and replayable in the DB (directly answering the DB-loss lesson).
- **Resists over-structuring** — the object stays a verse-grounded, inference-first, convergence-validated web; clusters/characteristics remain disposable scaffolding the software treats as such.
- **Faithful to the study's own principles and end-point** — DB as sole analytical memory; a finding for every verse with silence valid; STATED-vs-INFERRED provenance; comprehensiveness and robustness as the standing quality bars.

## 2. IBA App Development framework

### How it fits together

- **2.1 Language & framework — PowerShell is the framework.** PowerShell holds the **process logic and orchestration** and **calls Python modules** to do the work. (Windows Task Scheduler is *not* the launcher/framework.) The Python modules carry the DB / STEP / morphology / validation work; PowerShell sequences them, enforces the gates, and manages each run.
- **2.2 Rules, settings, and dependencies live in the configurator — never hard-coded.** The modules are **driven by rules and settings held in the configurator**; the **code methods *are* the process**; and the **process dependencies (which module needs which, in what order, under which gates) are all defined in the configurator, not in code.** Changing a study rule or the pipeline wiring is a configuration change, not a code change.
- **2.3 Build order — plan → whole framework → module-by-module → sustainability go/no-go before the study is touched.**
  1. **Detailed plan first** (this document, once agreed).
  2. **Build the framework for the entire end-to-end** — the full PowerShell orchestration + configurator + tracking + validation shell across all modules — *before* any single module is completed.
  3. **Complete each module and test it** within that frame, one at a time.
  4. **Only once the application concept is confirmed sustainable** is it applied to actually **re-run the study.** The re-run is gated on proving the concept, not assumed.
- **2.4 Existing scripts are a starting point, expected to be substantially rewritten.** The current `scripts/` / `engine/` code is where each module begins, but it is likely to be **substantially rewritten to be fit for purpose** (removing ad-hoc argv parsing, hard-coded provenance/paths, and the conventions that produced prior failures).
- **2.5 Cheapest working model, re-selectable.** The interpretive reads use the **cheapest model that produces valid results**, with the **model tier re-selectable via the configurator** if quality requires escalation. The deterministic validation gate carries quality; the tier is a setting, not a hard-coded choice.

### High level Schema

The IBA DB contains the entire study - nothing in the study exists if it is not in the DB.

#### Tables

The **word_registry** table contains the seed characteristic like words and is connected through **word_strong**
The **Strong** table contain the STEP Bible equivalent of the original language terminology that relates to the register. The meaning of the strong is supported by **lemma_inventory** , **strong_lexicon**, strong_meaning_tree, **strong_sense**
The **verse** table contains all the verses, as identified by STEP that contains a related Strong linked with **strong_verse**
The **span** table breaks down the verses into the individual words used in the verses
The **candidate-seed** table tag each span as potentially related to the inner being
The **span-candidate** table applies the seed to the verse span
The **passage** table is the study units and is connected to the verses with **verse_passage**
The **cfg_** group of tables is the core configuration rules of the app.
The **escalation** table is the configuration of messages 
The **run** table contains the operating modules 
The **validate_result** contains the validation outcomes of the run

**Claude note**: The role of the engine table in the app is outstanding

The following tables have not yet been built
Concordance
VE_lexical
Char_Operations
Char_meaning

#### Views

vw_passages_by_book

### 3. Application architecture (high level, end-to-end)

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

## Detail App design

### Configurations


### Utilities


### User Interaction


### Validation and errors

### Operation Modules
