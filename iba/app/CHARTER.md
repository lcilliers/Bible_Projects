# CHARTER.md — what the IBA app is, in the researcher's own words (2026-08-15)

> **This document exists so the app's purpose is never in doubt again.** It was dictated directly
> by the researcher on 2026-08-15, in the middle of a session that found the app's own history —
> 69 session logs, 113 `BUILD.md` sections, 43 `GOVERNANCE.md` sections, all individually rigorous
> — never once added up to a single statement of what the whole thing is *for*. This is that
> statement. It does not replace `GOVERNANCE.md` (the mechanism), `BUILD.md` (the history), or
> `USER-GUIDE.md` (how to run it) — it sits above all three as the objective they each serve, and
> the standard every one of them is judged against.
>
> **If any future decision, design, or build conflicts with this document, this document wins** —
> the same standing GOVERNANCE.md already grants the live `cfg_*` config over its own prose. Update
> this file only on the researcher's own direct instruction, never by inference.

---

## 1. The objective, verbatim intent

The IBA app was authored by the researcher **to serve as the single driver of all operational work
in this project.**

That means, concretely:

1. **Every component of what the project does must work through the app — not loose,
   standalone instructions.** A script that does real work but isn't registered in the app is a
   violation of this objective, not a convenience.
2. **All rules for operations must be defined in the configs** (`cfg_*` tables in `iba/app/db/
   iba.db`) — not in code literals, not in doc-only convention, not in memory. This is the
   existing rule `governance.rules_must_be_config_driven` already states for individual settings;
   this charter elevates it to the app's whole reason for existing.
3. **The primary interface is the terminal, via PowerShell scripts** (`iba/app/ps/*.ps1`) — every
   one of them listed in `cfg_work_package`.
4. **A number of modules already exist** — the operational work that actually does the study
   (raw ingestion, registry, lexicon, passage, candidate, narrative generation, …) — each listed in
   the configs. This is the existing `cfg_step.kind='operations'` classification (§27,
   `GOVERNANCE.md`).
5. **A number of utilities operate around the modules** — configuration maintenance, reporting,
   retention, export, search, … — each also listed in the configs. This is the existing
   `cfg_step.kind='utility'` classification, paired with a `cfg_utility` row per supporting library
   module (§26, `GOVERNANCE.md`).
6. **Nothing should exist that is not specified in the app.** No unregistered script. No ungoverned
   utility. No rule that lives only in a doc, a comment, or an AI's memory of a past session. If it
   runs, it is a `cfg_work_package`/`cfg_step`; if it decides something, that decision is a
   `cfg_setting`/`cfg_enum`/`cfg_*` row a live check can see.

## 2. Where the app actually stands today — stated plainly, not glossed over

**To date, the app has only integrated `iba/`.** Everything the app governs — its modules, its
utilities, its config, its data — lives inside the `iba/` folder. **Nothing outside `iba/` has been
integrated with the app.** The rest of the project (`Sessions/`, `Sessions-v2/`, `Workflow/`,
`scripts/`, `engine/`, `docs/`, `database/bible_research.db`, and everything else at the repo root)
still operates exactly as it always has — through standalone scripts and manual process, the same
"loose instructions" §1 above rules out.

**Bringing that outside work under the app is the task the researcher started this morning
(2026-08-15)** — the first concrete step was `manifest.rebuild`/`manifest.search` (§3, below),
which indexes the whole project tree from inside the app for the first time. It is one step, not
the whole task. The task is not complete, and this charter does not claim otherwise.

## 3. What this charter does NOT yet settle

This document states the *objective*. It does not itself:

- Refactor the `iba.db` schema to fit that objective cleanly (proposed, not started).
- Produce the full, current, whole-system specification — the thing the last hour of this session
  established doesn't exist anywhere, assembled instead from 225 individually-coherent but never
  rolled-up entries (session logs + `BUILD.md` + `GOVERNANCE.md`).
- Resolve the open `iba/config/` vs `iba/app/` fork (`GOVERNANCE.md` §6) — two configurators, only
  one of which the running app actually reads.
- Bring anything outside `iba/` under the app beyond the one step named in §2.

Those are the next pieces of work, each requiring its own plan and the researcher's approval before
execution — per the same discipline this session has already been running under. This charter is
the fixed point they all now have to build toward; it is deliberately not, itself, that work.

## 4. Two operating modes — Developer Mode and App Mode

Established at this app's original design discussion; re-stated verbatim by the researcher on
2026-08-31 after a session spent routing ordinary code fixes through `configmaint.propose`'s
per-row research-approval gate — and after this section's own first draft got the mechanism wrong
(a per-table classification Claude would self-apply mid-session, which the researcher rejected
outright: *"you should not be allowed to swap between developer mode and standard mode on the
fly"*). Full account: `GOVERNANCE.md` §69, memory `feedback_developer_mode_vs_app_mode_operating_
model`.

**The mode is a property of the SESSION, chosen by the researcher at login/session-start —
never mid-session, and never self-selected by Claude.** There is no in-app mechanism that switches
it; nothing in `iba/`'s code or config decides which mode is active. Claude infers which mode a
given session is in from the permissions it actually has (a standard session hits the harness's
own permission classifier on anything requiring elevation — that IS the signal), never by judging
"this table feels like a Developer Mode table."

**Developer Mode** — a session the researcher explicitly starts with full ("sysadmin") permissions,
for building/fixing the app itself: any code, any config, any table, without the standard
`configmaint.propose` per-row approval gate. Every applicable rule (this charter, `GOVERNANCE.md`,
`cfg_behaviour_rule`) must still be checked and applied — full permissions is not licence to skip
research. Every development task still gets an escalation item as the durable record.

**App Mode (standard)** — the default session type: standard Claude Code permissions, used both
for real operation of the app and for testing anything built in a Developer Mode session (a
Developer Mode session's own work is never tested in that same session — testing happens in a
fresh, standard-permission session). In App Mode, every `cfg_*` change — no exceptions for any
table, "mechanism" or otherwise — goes through the full `configmaint.propose` → researcher
approval → apply cycle, exactly as it always has. Only registered modules/utilities run (the PS
scripts under `iba/app/ps/`, dispatched through `python -m iba.app.run`) — no ad-hoc scripts, no
raw DB pokes. This is §1's own "every component... must work through the app" rule.
