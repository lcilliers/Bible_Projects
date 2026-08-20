"""bootstrap_behaviour_rules_cycle3_v1_20260818.py — ONE-OFF, idempotent. Escalation #715, cycle 3:
completes the sweeps the researcher named directly (2026-08-18): "survey the /workflow/* folder for
rules that should belong in this work... survey the session logs for indicators of missing or
misused rules... behaviour rules captured in claude.md and claude memory must also be included."

Sources pulled this cycle (all real, not from memory — read live before extracting):
  - `docs/interaction-preferences.md` (main-project chat protocol, main project side, never
    IBA-homed before this) -> mostly `chat`
  - `CLAUDE.md` §9 (compact summary of the same) -> confirms/dedupes against interaction-preferences
  - `Workflow/Instructions/wa-operational-governance-v1_0-20260614.md` (a prior, now-orphaned
    consolidation attempt — see its own retirement banner) -> git/commit content to `terminal`,
    backup/durability content to `sqlite`, per two new `governance.behaviour_boundary.*` settings
    this migration also adds (researcher's own fallback: "if in doubt define it and let it live in
    settings.governance to set the boundaries")
  - `cfg_escalation.chat_routing` (already DB-resident) -> cross-referenced, not duplicated, from a
    new `chat` rule (`documentation.single-authority-pointer-not-copy` forbids restating it verbatim
    in a second table; the existing row keeps its enforcement wiring)
  - `feedback_*` memory entries confirmed as pure operational-behaviour rules (not project facts),
    checked one at a time against the live memory file content, not assumed from the index line

Explicitly NOT pulled this cycle (deliberate, not an oversight):
  - `docs/file-organisation-rules.md` / filing content — belongs to escalation #650 (on-hold,
    "dependent on a deeper review of the statement of affairs"), a separately parked item; folding
    it in here would preempt that decision.
  - `feedback_simple_steps_not_engineered_designs` / `feedback_root_fix_not_one_off` / other
    engineering-taste memories that don't cleanly fit any of the 5 existing classes — flagged as a
    "6th class?" open question in the escalation raised alongside this migration, not force-fit.
  - Any content already covered by an existing rule (deduped by hand, not just by rule_key).

    python -m iba.app.migration.bootstrap_behaviour_rules_cycle3_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NOW = "2026-08-18T09:30:00Z"

_NOT_ENFORCED = (
    "not yet mechanically checked -- deviation-monitoring mechanism is still a follow-on cycle "
    "(escalation #715 addendum)"
)

_RULES = [
    # --- chat (was empty; docs/interaction-preferences.md + CLAUDE.md §9 + feedback_* memory) ---
    ("chat", "askuserquestion-banned",
     "The AskUserQuestion tool is never used in this project (blocked at config level, "
     "`.claude/settings.json` permissions.deny, after three prior memory-only warnings failed). "
     "A question answerable from the DB/code is investigated and answered with facts, not asked. "
     "A genuine researcher judgement call is written to a `.md` review file with options and a "
     "decision blank, pointed to in plain chat. A single short clarifying question with no real "
     "menu of options is asked in plain chat text.",
     "docs/interaction-preferences.md 'AskUserQuestion Tool — BANNED'; CLAUDE.md top banner"),
    ("chat", "confirm-before-nontrivial-work",
     "Before executing a non-trivial instruction, the instruction is summarised as understood, the "
     "planned approach/scope/files-affected are stated, and explicit approval is waited for before "
     "proceeding. Trivial single-step tasks are exempt. Once a plan is explicitly approved, its "
     "individual steps proceed without re-confirming each one — see "
     "`proceed-autonomously-once-rules-are-stable`.",
     "docs/interaction-preferences.md 'Instruction Confirmation Protocol'; CLAUDE.md §9 #1"),
    ("chat", "output-to-file-not-chat-only",
     "All substantive output and workings (analysis, plans, decisions, intermediate results, "
     "reports) are written to a `.md` file before being presented; chat carries only alerts, a "
     "brief summary, and a pointer to the file — never the full deliverable in chat alone.",
     "docs/interaction-preferences.md 'Output & Workings Stream Protocol'; CLAUDE.md §9 #2"),
    ("chat", "factual-discipline-no-guessing",
     "Work proceeds only from explicit, verified facts. Guessing, unstated assumptions, and filling "
     "gaps with speculation are not permitted; when information is missing or unclear, work stops "
     "and a real question is asked (never via AskUserQuestion) before proceeding. Distinct from "
     "`llm_output.inferential-not-confirmed`, which labels content already produced — this rule "
     "governs not proceeding at all without the facts.",
     "docs/interaction-preferences.md 'Factual Discipline Protocol'; CLAUDE.md §9 #3"),
    ("chat", "cost-awareness-flag-cheaper-path",
     "Where a task can be done more cheaply without sacrificing the outcome, the cheaper path is "
     "advised before acting — flagging a more expensive model on routine work, a whole-file read "
     "where targeted Read/Grep would do, a subagent where a direct query is enough, a duplicate "
     "artefact, or a live run where dry-run-then-live is safer.",
     "CLAUDE.md §9 #6 'Cost Awareness'"),
    ("chat", "chat-items-become-escalations",
     "A genuine open item, discovered anomaly, or judgement call raised or surfaced in chat "
     "conversation is recorded as an escalation in the same turn it's identified, not left standing "
     "only in chat prose. Full rule (including the closed-decision exemption) and its mechanical "
     "enforcement live at `cfg_escalation.chat_routing` — this row is a pointer into that table, "
     "not a restatement, per `documentation.single-authority-pointer-not-copy`.",
     "cfg_escalation.chat_routing (existing row, cross-referenced not duplicated)"),
    ("chat", "proceed-autonomously-once-rules-are-stable",
     "Once a rule or plan is explicitly set and stable, it is run to completion without stopping at "
     "every step to re-confirm — `confirm-before-nontrivial-work` governs starting new or "
     "non-trivial work, not re-litigating an already-approved plan's individual steps.",
     "memory feedback_proceed_autonomously_on_stable_rules"),
    ("chat", "close-the-loop-not-just-report",
     "A review or investigation task is not complete at 'found it, here's a doc' — the fix is "
     "implemented, verified, and the verified outcome is reported, not just the finding, unless the "
     "task was explicitly scoped as investigation-only.",
     "memory feedback_close_the_loop_not_just_investigate_and_report"),
    ("chat", "show-evidence-dont-smooth-over",
     "When reporting database state or investigation results, the actual query/sample data is "
     "shown, not a rounded-off or smoothed summary that hides messiness or uncertainty. A "
     "structural check passing (FK/not-null/enum) is a different claim from the values being fit "
     "for purpose, and reporting must not conflate the two.",
     "memory feedback_verify_db_claims_via_visible_tooling, "
     "feedback_structural_validation_is_not_value_quality_validation"),

    # --- terminal (was 1 rule; PowerShell protocol, git/commit boundary, memory) ---
    ("terminal", "readonly-commands-no-permission-needed",
     "Running a read-only command (checking system, file, or database state) needs no upfront "
     "permission. A command that modifies the database or codebase stays within the scope of an "
     "already-approved task.",
     "docs/interaction-preferences.md 'PowerShell / Terminal Protocol'"),
    ("terminal", "git-commit-and-push-together",
     "A git commit and its push are one unit — a commit is never left unpushed. Commits happen "
     "incrementally across a session, as units of work complete, not only gathered at session end. "
     "Classified under `terminal` (not a separate class) per "
     "`governance.behaviour_boundary.git_commit`.",
     "Workflow/Instructions/wa-operational-governance-v1_0-20260614.md §1; CLAUDE.md §12; "
     "memory feedback_commit_incrementally"),
    ("terminal", "heredoc-powershell-only",
     "A multi-line here-string for a command argument is written in PowerShell syntax (`@'...'@`), "
     "never Bash heredoc syntax — the two terminal tools in this environment do not share that "
     "convention.",
     "memory feedback_heredoc_only_in_powershell"),
    ("terminal", "diagnose-reported-errors-dont-route-around",
     "When the researcher pastes a console/terminal error, that error is the thing to diagnose and "
     "fix — it is never quietly routed around (completing the step a different way) with the step "
     "then reported as done. A reported failure is resolved or explicitly explained, not sidestepped.",
     "memory feedback_dont_sidestep_reported_ps_errors"),
    ("terminal", "verify-fix-against-synthetic-and-real-case",
     "A fix is not reported as done until tested against both a synthetic bad-input case and real "
     "data; when the same fix is applied at multiple sites, each site is individually re-verified, "
     "not assumed fixed because the pattern matched elsewhere.",
     "memory feedback_verify_before_reporting_fixed"),

    # --- sqlite (backup/durability boundary) ---
    ("sqlite", "writes-must-be-replayable",
     "Study/analytic work is captured in the database via a replayable mechanism (a patch file the "
     "applicator can re-run, a registered utility, or an engine run) — an interactive/ad-hoc "
     "database mutation that cannot be replayed from a record is a durability risk, not a shortcut. "
     "Classified under `sqlite` (not a separate class) per "
     "`governance.behaviour_boundary.backup_recovery`. Direct incident: an uncaptured interactive "
     "mutation contributed to the 2026-06-03 DB-loss incident (~6 weeks of work lost).",
     "Workflow/Instructions/wa-operational-governance-v1_0-20260614.md §2 'Core safeguard rule'"),

    # --- documentation ---
    ("documentation", "guidance-baked-into-authoritative-record",
     "New researcher guidance, rules, corrective decisions, or method changes given during a "
     "session are captured in the authoritative record the same session — a `cfg_*` row where the "
     "content is config-governable per `governance.rules_must_be_config_driven`, otherwise the "
     "owning document named for that content type — not left standing only in a memory file or a "
     "one-off findings doc.",
     "docs/interaction-preferences.md 'Bake Guidance into the Authoritative Instructions'"),
    ("documentation", "no-hedge-in-complete-records",
     "A record or report marked complete does not hedge with a 'see raw data if needed' pointer in "
     "place of a resolved answer — either the point is resolved directly, or it is flagged "
     "explicitly as unresolved. There is no quiet third option.",
     "memory feedback_no_hedge_pointers_in_complete_records"),
    ("documentation", "single-living-register-update-in-place",
     "An ongoing investigation or tracked-item register is one living document, updated in place as "
     "it evolves — reversed items are struck through or annotated, not deleted, and a second "
     "competing document for the same tracked set is never started.",
     "memory feedback_single_living_register"),
    ("documentation", "source-of-truth-is-written-record",
     "A claim about project state, history, or a prior decision is grounded in the written record "
     "(files, database, manifest) and cited, not asserted from memory or recollection.",
     "memory feedback_source_of_truth_is_written_record"),
    ("documentation", "consolidation-doc-must-be-load-bearing-or-retired",
     "A document created specifically to consolidate scattered operational rules is only as good as "
     "its live enforcement — if nothing in the actual startup/session-read path points to it, it is "
     "stale by construction and is retired (banner + pointer, provenance kept) rather than left to "
     "drift silently, however recently it was written or however strongly it claims to be canonical "
     "internally.",
     "this sweep's own finding: wa-operational-governance-v1_0-20260614.md and "
     "docs/project-orientation-core-memory-map.md, both dated 2026-06-14, neither read by the "
     "current start-project skill or iba/app/GOVERNANCE.md — both retired 2026-08-18"),

    # --- llm_output ---
    ("llm_output", "no-unsubstantiated-superlatives",
     "A superlative claim ('most', 'clearest', 'strongest', and similar) is not written unless every "
     "candidate was actually checked against it — an unverified superlative is exactly the kind of "
     "unearned-confidence claim `inferential-not-confirmed` already forbids, made concrete.",
     "memory feedback_avoid_unsubstantiated_superlatives"),
    ("llm_output", "derive-from-instruction-not-prior-unreviewed-output",
     "New analytical work is derived from the authoritative instruction document, never from a "
     "prior run's unreviewed output file used as an implicit template — an unreviewed pass may "
     "itself be wrong, and copying its shape propagates the error silently.",
     "memory feedback_never_model_output_on_prior_unreviewed_pass"),
]

_BOUNDARY_SETTINGS = [
    ("governance.behaviour_boundary.git_commit",
     "Git/commit discipline is classified under the `terminal` behaviour class (command/script-"
     "execution discipline), not a separate class -- committing and pushing is itself a terminal "
     "operation with a definable 'done' state. Content: cfg_behaviour_rule "
     "(terminal, git-commit-and-push-together).",
     "boundary decision -- git/commit class placement, escalation #715 cycle 3"),
    ("governance.behaviour_boundary.backup_recovery",
     "Backup/recovery and data-durability discipline is classified under the `sqlite` behaviour "
     "class (database-interaction discipline), not a separate class -- ensuring a write is "
     "replayable/captured is a database-state concern. Content: cfg_behaviour_rule "
     "(sqlite, writes-must-be-replayable).",
     "boundary decision -- backup/durability class placement, escalation #715 cycle 3"),
    ("governance.procedural_document_taxonomy",
     "A procedural document (going forward) is exactly one of: (a) planning/investigatory -- "
     "plans, explorations, decision docs; (b) config-extract -- generated (not hand-authored) from "
     "cfg_* for easier digesting, e.g. CONFIG-REPORT.md, cfg-rules-overview-*; (c) history-of-"
     "changes -- BUILD.md-shaped change records, arguably DB/engine-resident rather than a document "
     "long-term; (d) guidance/baseline instructions -- GOVERNANCE.md, USER-GUIDE.md, CLAUDE.md-"
     "shaped. Researcher's own framing, 2026-08-18 (comments-operational-behaviour-plan). Applying "
     "this taxonomy to the full existing document set is not done here -- a follow-on cycle.",
     "the 4-way procedural-document taxonomy named directly by the researcher, escalation #715 "
     "cycle 3 -- not yet applied to the existing document set"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for class_, rule_key, rule_text, source in _RULES:
        if not conn.execute(
                "SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
                (class_, rule_key)).fetchone():
            conn.execute(
                "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, "
                "enforced_by, added_at, active) VALUES (?,?,?,?,?,?,1)",
                (class_, rule_key, rule_text, source, _NOT_ENFORCED, _NOW))
            report.append(f"cfg_behaviour_rule ({class_}.{rule_key}) added")
        else:
            report.append(f"cfg_behaviour_rule ({class_}.{rule_key}) already present")

    for key, value, use in _BOUNDARY_SETTINGS:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                (key, f'"{value}"', use, "governance"))
            report.append(f"cfg_setting ({key}) added")
        else:
            report.append(f"cfg_setting ({key}) already present")

    conn.commit()
    conn.close()

    print("operational-behaviour cfg bootstrap (cycle 3 -- interaction-preferences/CLAUDE.md/"
          "operational-governance/memory sweep):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
