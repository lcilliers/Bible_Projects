"""bootstrap_behaviour_rules_cycle4_v1_20260818.py — ONE-OFF, idempotent. Escalation #715 cycle 4:
executes escalation #732's approved decision (a 6th behaviour class, named `development`) after
escalation #733's structural read-through (done first, per the researcher's own sequencing —
"if it is suggested to first do 733... then proceed") found the base to build on top of.

**#733's read-through, what it actually checked (not assumed):**
  - Re-read the 6 densest existing rules for literal duplication (the epistemic-discipline cluster:
    chat.factual-discipline-no-guessing, chat.show-evidence-dont-smooth-over,
    llm_output.inferential-not-confirmed, llm_output.no-unsubstantiated-superlatives,
    documentation.source-of-truth-is-written-record,
    llm_output.derive-from-instruction-not-prior-unreviewed-output) — genuinely distinct facets
    (proceeding / reporting-format / labelling / a specific labelling instance / citation /
    derivation-source), not duplicates. No merge needed.
  - Grepped all live (non-migration) code for references to the two docs retired in cycle 3 — none
    found; nothing left pointing at a dead location.
  - Checked cfg_write_grant for cfg_behaviour_class/cfg_behaviour_rule — correct (configmaint.propose).
  - **Found real staleness**: `cfg_behaviour_class.description` for `chat` still read "No rules
    seeded yet" after cycle 3 populated it with 9 rows — fixed directly (not a new rule, a stale
    fact).
  - **Found a real completeness gap**: three build cycles of this very system, and zero
    `USER-GUIDE.md` coverage — despite `governance.User_Guide_scope` already stating the guide
    "must reflect the latest state of all the tools." The rule existed; nothing enforced it.
  - **Found two of #732's "other items" already fully covered**, avoiding exactly the duplication
    #733 warned about: temp-file discipline is already `governance.scripts_and_routines`;
    script-folder-destination is already `governance.scripts_ps_dir`/`governance.scripts_python_dir`.
    Neither gets a new rule here.
  - **Found the operational-behaviour module itself had no supporting PS script** — reachable only
    via raw sqlite3/ad-hoc Python across 3 cycles. Built `iba/app/lib/behaviour.py` +
    `iba/app/ps/Behaviour.ps1` (registered separately, not by this migration) before writing the
    rule that names this exact gap, so the rule ships with its own compliance already true.

**This migration (cycle 4 proper — #732's content):**
  - New `cfg_behaviour_class` row: `development`.
  - 5 new `cfg_behaviour_rule` rows under it (2 moved in from memory, 3 genuinely new).
  - `governance.engineering_documentation_folder` — designates `iba/docs/` for IBA-side
    planning/design content (procedural_document_taxonomy category (a)); main-project-side
    consolidation is explicitly out of scope here (a separate, larger, not-yet-decided item,
    parked alongside escalation #650's filing review).

    python -m iba.app.migration.bootstrap_behaviour_rules_cycle4_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NOW = "2026-08-18T10:15:00Z"

_NOT_ENFORCED = (
    "not yet mechanically checked -- deviation-monitoring mechanism is still a follow-on cycle "
    "(escalation #715 addendum)"
)

_CLASS = (
    "development",
    None,
    "Engineering/method discipline for how work on this project itself gets done -- fix the cause "
    "not the instance, prefer simple steps over engineered designs, and the completeness "
    "disciplines (a supporting PS script per interactive module, docs kept in sync with code, "
    "every open item routed through escalation) that keep the rest of this mechanism actually "
    "enforced rather than just declared. Added 2026-08-18, escalation #732.",
)

_RULES = [
    ("development", "root-fix-not-one-off",
     "A defect that is an instance of a class (a shared method, an extractor, a pipeline step is "
     "wrong) is fixed at the shared mechanism so every future case is correct, not remediated "
     "case-by-case while the mechanism stays broken. A one-off/per-item patch is rarely "
     "appropriate, and never appropriate when the problem may recur.",
     "docs/interaction-preferences.md 'Root Fix, Not One-Off'; memory feedback_root_fix_not_one_off"),
    ("development", "simple-steps-not-engineered-designs",
     "Work is built in simple, direct steps. A machinery-heavy design (extra abstraction layers, "
     "generalised frameworks, speculative configurability) for a problem that a simple step would "
     "solve is overengineering, not thoroughness.",
     "memory feedback_simple_steps_not_engineered_designs"),
    ("development", "open-items-route-through-escalation",
     "Every open item discovered anywhere in the project's work -- a code review finding, a "
     "validation run's output, a documentation sweep, a data-quality check -- is recorded in the "
     "escalation table (`governance.escalation.scope`), not left as a silent fix, a code comment, "
     "or a mention buried in a report with no tracked row. `chat.chat-items-become-escalations` is "
     "this same principle's chat-conversation-timing instance (same turn it's raised in "
     "conversation); this rule is the general case, for anywhere else an open item surfaces.",
     "researcher, 2026-08-18 (escalation #732): 'add/move the config for all open items to be "
     "controlled through escalation to this section'; governance.escalation.scope"),
    ("development", "every-interactive-module-needs-ps-script",
     "Any module that a researcher or Claude operates by hand -- not purely internal library code "
     "called only by other code -- has a dedicated PS entry point under `governance.scripts_ps_dir` "
     "(`iba/app/ps/`). A module reachable only via raw Python or raw SQL is a usability and audit "
     "gap, found live 2026-08-18 against this very system: 3 build cycles of "
     "`cfg_behaviour_class`/`cfg_behaviour_rule` before `Behaviour.ps1` existed.",
     "researcher, 2026-08-18 (escalation #732)"),
    ("development", "user-guide-updated-same-unit-of-work",
     "A change to a tool, module, or user-facing behaviour is not complete until `USER-GUIDE.md` "
     "reflects it, in the same unit of work -- `governance.User_Guide_scope` states what the guide "
     "must cover (\"the latest state of all the tools\"); this rule states when it's updated. Found "
     "violated live 2026-08-18: 3 build cycles of the operational-behaviour system (escalation "
     "#715) had zero `USER-GUIDE.md` coverage before this rule existed.",
     "researcher, 2026-08-18 (escalation #732); governance.User_Guide_scope; "
     "same shape as governance.build_md_on_code_change for BUILD.md"),
]

_SETTINGS = [
    ("governance.engineering_documentation_folder",
     "iba/docs/ is the designated home for IBA-side engineering/planning documentation (design "
     "docs, plans, gap analyses, investigation write-ups) -- procedural_document_taxonomy category "
     "(a). Already functioning as this in practice (30+ files); this setting states it as "
     "governance rather than leaving it implicit. Main-project-side consolidation of the "
     "equivalent scattered content (docs/, research/investigations/, Workflow/methodology/) is a "
     "separate, larger, not-yet-decided item, parked alongside escalation #650's filing review -- "
     "not resolved here.",
     "boundary/location decision -- engineering documentation folder, escalation #732 cycle 4"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    cls, doc, desc = _CLASS
    if not conn.execute("SELECT 1 FROM cfg_behaviour_class WHERE class=?", (cls,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_behaviour_class (class, authoritative_doc, description, added_at, "
            "inactive) VALUES (?,?,?,?,0)",
            (cls, doc, desc, _NOW))
        report.append(f"cfg_behaviour_class ({cls}) added")
    else:
        report.append(f"cfg_behaviour_class ({cls}) already present")

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

    for key, value, use in _SETTINGS:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                (key, f'"{value}"', use, "governance"))
            report.append(f"cfg_setting ({key}) added")
        else:
            report.append(f"cfg_setting ({key}) already present")

    conn.commit()
    conn.close()

    print("operational-behaviour cfg bootstrap (cycle 4 -- new `development` class, escalation "
          "#732, after #733's structural read-through):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
