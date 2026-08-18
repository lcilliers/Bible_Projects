"""bootstrap_behaviour_rules_cycle2_v1_20260818.py — ONE-OFF, idempotent. Escalation #715, cycle 2:
draft rule rows from the three `Workflow/*` usage guides found during the cycle-2 survey (dated
2026-08-15, never previously folded into `cfg_behaviour_rule`):

  - `Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md` §5 "What NOT to do" -> `llm_output`
  - `Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md` -> `sqlite` (new content only;
    the guide's "verify, don't just trust" section overlaps the already-seeded
    `sqlite.verify-before-acting` rule and isn't repeated here)
  - `Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md` -> `documentation` (one Claude-relevant
    rule out of an otherwise researcher-facing doc)

`chat` class gets nothing from this pass — none of the three source docs are about the
human-Claude interaction protocol; that's still CLAUDE.md §9/docs/interaction-preferences.md/
memory, a separate audit not done yet.

    python -m iba.app.migration.bootstrap_behaviour_rules_cycle2_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NOW = "2026-08-18T08:00:00Z"

_NOT_ENFORCED = (
    "not yet mechanically checked -- deviation-monitoring mechanism is still a follow-on cycle "
    "(escalation #715 addendum)"
)

_RULES = [
    ("llm_output", "sdk-dependency-decision",
     "Adding the `anthropic` SDK (or any second Python dependency for Claude-API calls) requires "
     "raising it as its own decision first. The IBA app's single-dependency policy (`requests` "
     "only, per USER-GUIDE.md) is deliberate, not an oversight.",
     "Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md §2/§5"),
    ("llm_output", "no-hardcoded-call-params",
     "Model IDs, token ceilings, cost rates, cost caps, and output paths for any Claude-API-calling "
     "step are `cfg_setting` rows, never literals inside a handler.",
     "Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md §1/§5"),
    ("llm_output", "cost-cap-before-call",
     "A live Claude-API call is preceded by a pre-call cost estimate and a hard cost-cap check: "
     "hard-refuse over the cap (no call, no escalation, nothing spent); escalate for approval "
     "below the cap. No live call happens before this two-step gate.",
     "Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md §1/§5"),
    ("llm_output", "usage-log-required",
     "Every live Claude-API call's real `usage` block (not the pre-call estimate) is logged to an "
     "append-only CSV usage log. Skipping this write leaves the project's cost ledger with no "
     "record the call ever happened.",
     "Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md §1/§5"),
    ("llm_output", "sonnet-default-model",
     "Claude Sonnet 5 is the default model for high-volume structured analytic-phase work. Using "
     "a more expensive model (Opus) requires a specific stated reason, not a default choice.",
     "Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md §3/§5"),
    ("llm_output", "never-expose-api-key",
     "The Claude API key's value is never written, logged, or printed anywhere -- not in a "
     "report, an escalation payload, a chat response, or a commit.",
     "Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md §2/§5"),

    ("sqlite", "readonly-by-default",
     "Open a database connection read-only by default when browsing or checking a claim against "
     "iba.db or bible_research.db; use a write connection only with a specific reason.",
     "Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md"),
    ("sqlite", "never-write-via-adhoc-tool",
     "Never write to iba.db or bible_research.db directly through an ad-hoc SQL tool (the VS Code "
     "SQLite extension or equivalent). bible_research.db writes go through "
     "scripts/apply_session_patch.py against a JSON patch; iba.db config writes go through "
     "Config-Maintenance.ps1 -Step Propose; iba.db data writes go through the app's own "
     "registered utilities. Use direct inspection to see a problem, then route the actual fix "
     "through the governed path.",
     "Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md"),
    ("sqlite", "dont-assume-which-database",
     "Don't assume which database a table lives in. bible_research.db (prose + analytic "
     "findings) and iba.db (process control + the entire base data layer) have a defined split; "
     "a 'no such table' error usually means the wrong database was opened, not a typo.",
     "Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md"),
    ("sqlite", "query-file-conventions",
     "An ad-hoc SQL scratch file worth keeping is saved to scripts/ (not left in whatever folder "
     "happened to be open), prefixed SQLite_, and named for what it actually checks -- not left "
     "untitled. A file worth re-running is committed like any other script; a genuinely one-off "
     "query that's been answered can be deleted rather than accumulate.",
     "Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md"),

    ("documentation", "obsidian-copy-not-authoritative",
     "An Obsidian-edited copy of a DB-generated `.md` file is never authoritative. The database "
     "row is the source of truth for prose, findings, and config -- editing the file doesn't "
     "change the database, and a regenerated export overwrites the edit.",
     "Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md"),
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

    conn.commit()
    conn.close()

    print("operational-behaviour cfg bootstrap (cycle 2 -- Workflow/* guide sweep):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
