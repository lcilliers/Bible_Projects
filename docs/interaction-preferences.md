# Interaction Preferences — Claude Code

This file is the authoritative record of communication protocols between the researcher (leRoux) and Claude Code. Claude Code must read and apply these protocols at the start of every session.

---

## Instruction Confirmation Protocol

Before executing ANY instruction (except trivial single-step tasks):
1. Summarise the instruction as understood
2. State what I plan to do (approach, files affected, scope)
3. WAIT for explicit researcher approval before proceeding

This applies to every new chat session, without exception.

---

## Output & Workings Stream Protocol

All workings (reasoning, plans, steps) and all outputs must be streamed to `.md` files so the researcher can review and contribute to them.

- Never present final output only in chat — always write it to a `.md` file first
- Workings (analysis steps, decisions made, intermediate results) must also be captured in `.md` format
- Files should be placed in a logical location within the workspace (`docs/`, `outputs/`, or a relevant subfolder)
- The researcher may edit these files to correct or contribute, and those edits must be respected in subsequent steps

---

## Factual Discipline Protocol

Do not guess, make assumptions, or offer unsolicited opinions.

- Work only with the facts and inputs explicitly provided
- Do not invent context, fill in gaps with assumptions, or speculate without being asked
- Opinions and recommendations must only be given when explicitly requested
- If anything is unclear or information is missing — STOP and ask before proceeding

---

## PowerShell / Terminal Protocol

It is not necessary to ask for permission before running PowerShell or terminal commands to read system state or execute approved work. Commands that modify the database or codebase should still be consistent with approved tasks.

## Root Fix, Not One-Off (researcher direction 2026-07-13)

Fix the **cause**, not the instance. A one-off / per-term / per-book / per-file patch is **rarely appropriate, and NEVER appropriate when the problem may recur.** When a defect is an instance of a class (a shared method, an extractor, a pipeline step is wrong), fix it at the shared mechanism so every future case is correct — do not remediate case-by-case and leave the mechanism broken. If you catch yourself hand-patching one case of a recurring problem, stop and fix the root. (Worked example: the STEP multi-variant verse drop was fixed in `word_study_extract`, not patched per Proverbs term.)

## Bake Guidance into the Authoritative Instructions

Researcher guidance, rules, decisions, and corrective actions must be written into the **authoritative instruction docs** (`Workflow/Instructions/`), not only into memory or a findings file — the written authoritative record is the source of truth (GR-REF-002). Add a dated amendment to the owning doc, then mirror a pointer in memory.
