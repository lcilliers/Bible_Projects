# Open Loops & Incomplete Methodology — register

> Reconstructed 2026-06-14 from the written record (two focused document readers, citation-required). This is the **"what is still open / not finalised / superseded-but-unmarked"** layer that the status reconstruction (01) did not capture. Companion to 01/02/03.
>
> **Scope note:** "open" here means *methodology/process* work — instructions not finalised, decisions awaiting approval, actions raised but unclosed, documents silently superseded. It is **not** data backlog.

---

## 0. CRITICAL — a master open-items register exists, and it may itself be stale

The project already maintains a living register: **`Workflow/Programme/Program_reports/wa-programme-open-items.md`** (v8, 2026-06-01) — **127 tracked items across §A–§Q** with OPEN / DECIDED / IN PROGRESS / DONE / DROPPED status. I had missed it in 01; it is the single most important artefact for "what's open."

**But it is dated 2026-06-01** — *before* three things that reshaped the programme:
- the **DB loss** (2026-06-03),
- the **foundations reset** (2026-06-04, which "closed down" the remediation frame as "the wrong frame"),
- the **L1/L2 verse-read = meaning pivot** (2026-06-07/09).

Much of the register is **publication/generator-focused** (Session C chapters, Ch8/appendix generation, prose-ingest scripts §F1–F14, publishing-instruction edits §B–§E). The verse-read pivot and the "be patient, accumulate before distilling" direction may have **overtaken** large parts of it. **So the #1 open question is: is this register still the live worklist, or has the 2026-06-04 reset superseded its publication/generator sections?** This is itself an instance of the drift we are fixing — an authoritative-looking register that may be partly stale, with no marker saying so.

> ⚠ **Confirm first:** which sections of `wa-programme-open-items.md` survive the 2026-06-04 reset, and re-date/re-issue it (or migrate it DB-resident) so there is one *current* open-items surface.

---

## 1. The three you named — confirmed open, with specifics

| # | Item | State | What's needed to close | Citation |
|---|---|---|---|---|
| a | **Filing / folder cleanup** | `wa-workflow-cleanup-register.md` + `wa-archive-decisions-for-guidance-v1-20260607.md`: ~42 disposition rows; several genuine judgement calls left as blank `____` cells; archiving **not executed** | Researcher completes the `____` decisions; CC executes the `git mv` archiving in one pass; record completion | (wa-workflow-cleanup-register.md §B — "Need your guidance"; wa-archive-decisions-for-guidance-v1-20260607.md §B `____`) |
| b | **Catalogue revisitation** | Two-layer VE/SYNTH tier catalogue (`wa-tier-catalogue-restructured-v2-20260611.md`) approved on paper, **but the DB is not yet modified** (old T-codes remain reference); catalogue-refit D1–D4 + verse-level-extraction-spec D1–D5 **pending researcher markup** (field set already in use) | Ratify the field/disposition decisions; modify `wa_obs_question_catalogue` (+ links) to the two-layer model; retire/relabel old T-codes | (wa-tier-catalogue-restructured-v2-20260611.md — "DB not yet modified; old T-codes remain"; memory feedback_catalogue_refit_four_principles "D1-D4 pending") |
| c | **V3_2 instruction not finalised** | `wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md` — **DRAFT**; one open dependency **B3** (L8b cross-cluster reconciliation mechanics); depends on two un-ratified upstream proposals (§2 below) | Resolve B3; ratify the phase-reshape + phase-1-mechanical proposals; run one cluster end-to-end (L1–L8a) as the live validation; mark finalised | (wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md — "DRAFT — for researcher review…One open dependency: B3") |

---

## 2. Open instruction / methodology / schema (DRAFT or awaiting approval)

| Item | Type | Open status | Citation |
|---|---|---|---|
| Verse-analysis methodology **v4** | methodology | "DRAFT for review" (2026-06-06); not adopted into the instruction set | (wa-verse-analysis-methodology.md — "Doc version: 4 · DRAFT for review") |
| **Phase-reshape v3_1** (light Phase A + deep VCG read) | methodology | Proposal; "Not yet applied to the live v3_0 instruction" | (wa-cluster-phase-reshape-v3_1-proposal.md — "DRAFT for review…fold into v3_1") |
| **Phase-1 mechanical-meaning reframe** (STEP-mechanical L1) | methodology | "To be folded into the design docs if confirmed"; rests on M01 97%-mechanical corroboration finding | (wa-phase1-mechanical-meaning-reframe-v1-20260607.md) |
| **Audit design v1** | design | L1 spec complete; **L2–L8 audit checks stubbed/awaiting design** as each level settles | (wa-cluster-audit-design-v1-20260607.md) |
| **Disposition catalogue v2_1** (ROUTE-TO-CLUSTER vs CARRY-TO-SESSION-D) | instruction | "PROPOSAL — awaiting researcher approval before applying as v2_1" | (WA-disposition-catalogue-cluster-centric-proposal-v1-20260516.md) |
| **Schema population passes** | schema | M55 added columns but deferred populating `wa_meaning_sense.stem_label`/`is_homonym` and per-occurrence `morph_code`/`stem` (run within L1 of first cluster); homonym detection rule flagged `〔CONSULT〕` | (wa-v3_2-schema-migration-plan-v1-20260607.md §3) |
| **Schema snapshot + migration registry drift** | schema | On-disk schema snapshots stale (newest **3.17.0** vs live **3.31.0**); migration registry registers M01–M39 but **M40–M54 applied outside the registry** | (wa-workflow-cleanup-register.md §A; live `schema_version` = 3.31.0) |
| **Obslog template** | methodology | Decided CC must write workings to an obslog continuously; standard template not yet drafted | (wa-sessionlog-20260528-end-of-session-v1.md — "Obslog template…should write a starter template") |

---

## 3. Open analytical work (from the register + session logs)

| Item | Status | Note | Citation |
|---|---|---|---|
| **v2_5 methodology pivot** (scope correction; BOUNDARY-resolution gate; re-examination workflow §16; co-occurrence check §17) | DECIDED, **not drafted** | Researcher: "Draft → approve → apply. Do NOT short-cut." Blocks BOUNDARY cleanup | (wa-sessionlog-20260517-methodology-pivot-end-of-session-v1.md) |
| **BOUNDARY cleanup — hard gate** | OPEN, large backlog | **17 clusters validated 2026-05-31 → 0 pass / 17 fail, all demoted to "Analysis - In Progress"**; 39+ pending flags across M01/M02/M03/M06/M15 | (wa-programme-open-items.md §G, §M4b) |
| **Large-gap root-cause (§I)** | OPEN — **step 1, gates everything** | M04/M07/M08/M09 each missing ~1000+ findings vs generator expectation; cause (obs_id/question_code keying?) undiagnosed | (wa-programme-open-items.md §I, §F3) |
| **Generator/script fixes §F1–F14** | mostly OPEN | Remove Ch8/appendix gen; prose-ingest scripts; closure-contract F14 "design drafted, awaiting review" — **currency-questionable post-pivot (see §0)** | (wa-programme-open-items.md §F) |
| **Stray SB/SD findings §K/§L** | OPEN | 702 stray Session-B findings + 440 unresolved SB/SD research flags across 10 clusters; needs a conversion session | (wa-programme-open-items.md §K, §L) |
| **M11 parked (Type 3 cluster)** | PARKED | 4 directions in park notice, none chosen; Phase 3 verdicts not applied | (wa-sessionlog-20260526-cluster-architecture-question-v1.md) |
| **Architecture probe** (lens-free read on 20–30 multi-lens verses, ~$200–400) | OPEN, not run | Would test whether the 45-characteristic frame imposes "lens-screening bias" | (wa-sessionlog-20260526…v1.md §6.4) |
| **Column-wise + reverse-primacy redesign** | DECIDED 2026-06-11, **not implemented** | Needs engine refactor (read/dimensions/meaning/write are one streamed call now) + meaning-derived template + new dimensions | (wa-sessionlog-20260611-ve-exploration-and-meaning-diagnosis-v1.md) |
| **OT-DBR-009 mti_terms dedup** | OPEN, deferred | 41 dupes, 2,209 dup verse_context; "not executed (non-blocking for now)" | (wa-sessionlog-20260609…v1.md §2) |
| **Distillation / synthesis layer** | INTENTIONAL HOLD | Roll verse-read through many clusters before distilling | (wa-sessionlog-20260609…v1.md §10) |
| **Foundations §c/§d** | BLOCKED | Awaiting researcher QA markup; gates the verse-meaning audit-surface work | (wa-sessionlog-20260604-end-of-session-v1.md) |
| **Science extracts (h)** | OPEN gap | Not yet in the DB | (wa-study-foundations.md §b) |

---

## 4. Superseded-but-NOT-marked (silent supersession) — the issue you flagged

These documents are *replaced* by later ones but carry **no in-document "superseded" marker**, are **not** in `archive/`, and in some cases are still cited as authoritative (incl. by CLAUDE.md §10). Silent supersession is a primary drift source.

| Earlier doc (still presented as live) | Superseded by | Evidence |
|---|---|---|
| `wa-sessionb-cluster-instruction-v3_0-20260527.md` | V3_2 rollup design + instruction (2026-06-07) | CLAUDE.md §10 still lists v3_0 as authoritative; v3_2 is the new base | 
| `wa-v2_9-vs-v3_0-cycle-comparison-v1`, `wa-v3-publication-pipeline-design-v1`, `wa-v3_0-final-review-v1`, `wa-v3_0-phase-b-control-design-v1` (all 2026-05-27) | V3_2 base (2026-06-07) | Listed for archiving in cleanup guidance, no in-doc marker |
| `wa-audit-framework-design-v0_1-20260526.md` (DRAFT) | `wa-cluster-audit-design-v1-20260607.md` | v0.1 pre-V3_2; v1 is the rollup-integrated design |
| `wa-cluster-remediation-orchestrator-design-v1-20260602`, `…-playbook-v1-20260601`, `…-aspect-spec-v1-20260601` | Remediation **closed 2026-06-04**; V3_2 rollup replaces it | "Closed down — it was the wrong frame" |
| `WA-tier-framework-definitions-v1_2-2026-04-29.md` | §c of `wa-study-foundations.md` (in-progress rewrite) | Held pending §c completion |
| `wa-programme-open-items.md` v8 (2026-06-01) — **publication/generator sections** | The 2026-06-04 reset + verse-read pivot (uncertain extent) | See §0; ⚠ confirm |

> **Recommendation (cheap, high-value):** adopt a one-line header convention — `> **SUPERSEDED** (date) by \`<doc>\`. See <pointer>.` — applied whenever a doc is *replaced* (not merely archived). This makes drift visible instead of silent. Better still per the all-work-in-DB principle: a small DB-resident **supersession ledger** (doc → superseded_by → date → reason).

---

## 5. What this means (the implication)

The reliability problem is **bigger than CLAUDE.md + memory being stale.** Decisions, supersessions, open actions, and an entire 127-item register live in **scattered, separately-dated documents with no single *current* "what is open / what is authoritative" surface** — and at least one authoritative-looking register (`wa-programme-open-items.md`) predates the last two pivots without a marker. That is precisely why work re-opens and re-derives.

**Two concrete fixes flow from this** (for your decision, not yet actioned):
1. **One live open-items + supersession surface** (DB-resident per all-work-in-DB, or one dated master doc), re-issued after each pivot — replacing the scattered registers.
2. **Supersession markers** on replaced docs (§4) so the repo's "live vs dead" is self-evident.

These, plus the CLAUDE.md refresh and memory trim already planned, address the drift at its root rather than per-symptom.
