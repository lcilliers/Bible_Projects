---
name: feedback-ai-package-self-declaration
description: "AI-facing input packages must explicitly declare required inputs and whether a brief is needed. The package's first lines tell AI what to load before reading further."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

When CC prepares any input package for an AI session, the package must **self-declare** at the top of every constituent document:

- Whether a **brief** is required, and where it lives
- The complete list of **required inputs** the AI session must load: brief (if any), structural input docs, governing instruction docs, global rules, prior session artefacts (e.g. constitution debate, prior Phase outputs)
- Any **researcher pre-decisions** already made that AI must not re-litigate (e.g. "M04 sub-groups M04-A through M04-P already exist; do not propose alternatives")
- Any **out-of-scope** items (e.g. "the 77 HOLD verses are out of scope for this task")

**Why:** stated 2026-05-18 — "you need to write into your instructions for preparing packages to AI to clearly indicate if a brief is required, and if the document requires any other inputs such as the instructions or global rules." Without a self-declaration, the researcher cannot tell at a glance whether a package is ready to hand off, and the AI session may run without all required context (causing rework or misaligned output).

**How to apply:**

1. **Every AI-facing input doc starts with a "Required inputs" block** at the top, immediately after the title and metadata. Format:

   ```markdown
   ## Required inputs (load before reading further)

   | # | Document | Purpose |
   |---|---|---|
   | 1 | This brief | Primary instructions for the task |
   | 2 | Structural input doc — `path/to/...` | Per-item data (verses, findings, etc.) |
   | 3 | `wa-sessionb-cluster-instruction-v2_5-20260518.md` — §11A and §18.2 | Governing instruction |
   | 4 | `wa-global-general-rules` [current] | Global rules |
   | 5 | Prior outputs — `path/to/...` (if any) | Context |
   ```

2. **Default pairing: brief + structural input.** Most AI tasks pair a brief (~150–300 lines, the primary read) with one or more structural input docs (data tables, verse lists). Brief is read first; AI loads structural docs as referenced.

3. **No-brief exception** — for trivial atomic per-row tasks (e.g. JSON-template + API Pass A meaning record), the structural input itself may be the only document. The structural input must still declare at the top: "No brief required — this document is self-contained" + Required-inputs block.

4. **Researcher pre-decisions** belong in the brief, not buried in the structural input. The brief opens with a short "Context & pre-decisions" section: what's already been decided, what AI should not re-question, what's out of scope.

5. **Quality expectations** belong in the brief: how a "good" output looks, anti-patterns to avoid, output format with at least one worked example.

6. **Cross-link** — brief points to structural input by path; structural input points to brief by path. Both files declare the same Required-inputs list.

**Existing precedent / extension:** [[feedback-phase-brief-standard-practice]] already establishes the brief-alongside pattern for v2_0 Phases 3/5/7/9/10. This memory item extends it to **all** AI-facing packages (Phase 8.5, audit-fix dispositions, re-examination work, etc.) and adds the self-declaration requirement.

**Operational consequence for CC:** when CC builds an AI input package, the next-step prompt should always offer "I'll build the brief alongside" or, if a brief isn't needed, justify why ("trivial atomic task — structural input is self-contained, header attached").

Related: [[feedback-phase-brief-standard-practice]], [[feedback-review-via-files-not-chat]], [[feedback-working-style]].
