"""bootstrap_behaviour_rules_v1_20260818.py — ONE-OFF, idempotent: creates the operational-
behaviour cfg layer (escalation #715, researcher comments in
`Workflow/Chat_responses/comments-operational-behaviour-plan`, 2026-08-18 — "proceed with creating
the cfg.settings rows and the separate cfg_* tables for the different behaviours... Start with the
obvious ones. get them out of the way.").

**Scope, per the researcher directly: project-wide, not `iba/app/**` only.** `iba.db` is the right
DB to hold this (`governance.scope_iba_app`/`scope_iba_db` already make it the project's process-
control home for the *entire* project, not a sub-section), but the rules this layer governs apply
everywhere Claude operates — `bible_research.db` work, `Workflow/*`, `CLAUDE.md`, memory — not only
`iba/app/`.

**Cycle 1 of N ("the obvious ones") — what this bootstrap actually does:**

1. Two new tables: `cfg_behaviour_class` (the taxonomy: chat, terminal, sqlite, documentation,
   llm_output) and `cfg_behaviour_rule` (the actual rule content per class).
2. Seeds the four rules that were already fully scoped (governance-alignment register row 5,
   escalations #714/#715) and reworded as **definitive statements** per the researcher's explicit
   instruction ("worded as statements and is definitive, not open for interpretation") — the direct
   successors of `wa_rule_registry` GR-DB-001, GR-PROC-001, GR-REF-001, GR-PROG-009.
3. `governance.operational_behaviour_control` — the entry-point anchor setting.
4. `class='chat'` is created with **zero rule rows** — deliberately. Its actual content (CLAUDE.md
   §9, `docs/interaction-preferences.md`, `cfg_escalation.chat_routing`, the `feedback_*` memory
   set) is NOT "obvious" — it needs the project-wide `Workflow/*` + session-log survey and the
   CLAUDE.md/memory audit the researcher named as later cycles. Seeding it now with a partial or
   guessed rule set would misrepresent the class as populated when it isn't.

**Explicitly NOT done in this cycle** (the researcher's later-cycle items — tracked in
`iba/app/reports/operational-behaviour-rules-cfg-plan-20260818.md`, not repeated here):
survey of `Workflow/*` and session logs for prior (including failed) regulation attempts; the
CLAUDE.md/memory audit; consolidating `cfg_escalation.chat_routing` or any other pre-existing cfg
row into this structure; resolving which document is authoritative per class (`authoritative_doc`
is left NULL — undecided, not guessed); a deviation-monitoring/enforcement mechanism (`enforced_by`
on every seeded row says so honestly); quantifying impact on existing docs/data; redefining the
four-way procedural-document taxonomy the researcher named (planning / config-extract / history /
guidance). Each is a real follow-on item, not silently dropped.

    python -m iba.app.migration.bootstrap_behaviour_rules_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_DDL = """
CREATE TABLE IF NOT EXISTS cfg_behaviour_class (
    class            TEXT PRIMARY KEY,
    authoritative_doc TEXT,
    description      TEXT NOT NULL,
    added_at         TEXT NOT NULL,
    inactive         INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS cfg_behaviour_rule (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    class        TEXT NOT NULL REFERENCES cfg_behaviour_class(class),
    rule_key     TEXT NOT NULL,
    rule_text    TEXT NOT NULL,
    source       TEXT NOT NULL,
    enforced_by  TEXT,
    added_at     TEXT NOT NULL,
    active       INTEGER NOT NULL DEFAULT 1,
    UNIQUE(class, rule_key)
);
"""

_NOW = "2026-08-18T06:30:00Z"

_NOT_ENFORCED = (
    "not yet mechanically checked -- deviation-monitoring mechanism is a follow-on cycle "
    "(researcher, 2026-08-18: 'validation of these rules must include mechanisms to flag "
    "deviation from the defined rules. This deviation must be monitored ongoing.')"
)

_CLASSES = [
    ("chat", "The interaction protocol and communication discipline between Claude and the "
             "researcher -- turn-taking, confirmation-before-acting, output-to-file, cost "
             "awareness. Distinct from llm_output, which governs epistemic trust in generated "
             "content regardless of channel. No rules seeded yet -- see module docstring."),
    ("terminal", "Command/script execution discipline -- what 'done' means when running an "
                "operation (a script, a migration, a build step), independent of which "
                "operation."),
    ("sqlite", "Database-interaction discipline for any project database (bible_research.db, "
              "iba.db) -- verifying live state before acting on it, regardless of which DB."),
    ("documentation", "Single-authority content referencing across the project's guides and "
                      "instruction documents (USER-GUIDE.md, GOVERNANCE.md, BUILD.md, README.md, "
                      "CLAUDE.md, docs/interaction-preferences.md, Workflow/Instructions/*, and "
                      "this cfg_* system itself) -- one owning source per content type, pointer "
                      "not copy."),
    ("llm_output", "Epistemic discipline for content generated via an LLM/API call (Claude's own "
                   "output, a subagent's report, WebSearch synthesis, automated classification) "
                   "-- inferential vs confirmed labelling, regardless of which channel produced "
                   "it."),
]

_RULES = [
    ("sqlite", "verify-before-acting",
     "Before any operation that depends on database state (row counts, flag values, "
     "existence/absence of a record, referential integrity, or the presence of a prior write), "
     "that state must be verified directly against the live database. Acting on assumed, "
     "remembered, or previously-reported state is a violation regardless of how recent or "
     "reliable the prior report seemed.",
     "wa_rule_registry GR-DB-001 (obsolete 2026-08-17, superseded_by='iba.db cfg_* configuration "
     "system')"),
    ("terminal", "step-not-done-without-validated-output",
     "A step expected to produce an output (a file, a database write, a report) is not complete "
     "until that output has been confirmed to exist and matches what the step was supposed to "
     "produce. Reporting a step as done on the strength of the command appearing to succeed, "
     "without that confirmation, is a violation.",
     "wa_rule_registry GR-PROC-001 (obsolete 2026-08-17, superseded_by='iba.db cfg_* "
     "configuration system')"),
    ("documentation", "single-authority-pointer-not-copy",
     "Each piece of operational or process content has exactly one authoritative source -- a "
     "cfg_* row where one exists, otherwise one named document. Any other document or response "
     "needing that content points to the authoritative source by name/section; it does not "
     "restate, paraphrase, or duplicate it. A rule may not exist in both a document and a cfg_* "
     "row at the same time -- once a rule is captured in cfg_*, its document version is replaced "
     "with a pointer, not left standing alongside it.",
     "wa_rule_registry GR-REF-001 (obsolete 2026-08-17, superseded_by='iba.db cfg_* "
     "configuration system'); 'no reason to have a rule both in a document and in the config' "
     "per researcher comment 2026-08-18"),
    ("llm_output", "inferential-not-confirmed",
     "Any claim, classification, or connection produced via an LLM or API call -- including "
     "Claude's own output, a subagent's report, or an automated classification pass -- that is "
     "not directly grounded in verifiable source data must be labelled inferential, not "
     "confirmed. An inferential label may not be silently upgraded to confirmed without new, "
     "citable supporting evidence.",
     "wa_rule_registry GR-PROG-009 (obsolete 2026-08-17, superseded_by='iba.db cfg_* "
     "configuration system'); reframed by the researcher 2026-08-18 as the general API/LLM-use "
     "discipline rule, not only an analytical-finding label"),
]


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES (?,?,?,?)",
                    (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?,0)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _utility(conn, module, file_path, purpose, report):
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        conn.execute("INSERT INTO cfg_utility (module, file_path, purpose, inactive) "
                    "VALUES (?,?,?,0)", (module, file_path, purpose))
        report.append(f"cfg_utility {module!r} added")
    else:
        report.append(f"cfg_utility {module!r} already present")


def _write_grant(conn, writer, table_name, report):
    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
            (writer, table_name)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                    "VALUES (?,?,'iba',0)", (writer, table_name))
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) added")
    else:
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) already present")


def _table_and_columns(conn, name, grain, use, columns, report):
    if not conn.execute("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_table (database, name, grain, \"use\") VALUES ('iba',?,?,?)",
                    (name, grain, use))
        report.append(f"cfg_table {name!r} added")
    else:
        report.append(f"cfg_table {name!r} already present")
    for ordinal, (col, coltype, ispk, notnull, colnuse) in enumerate(columns):
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
                (name, col)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by) "
                "VALUES ('iba',?,?,?,?,?,?,0,NULL,NULL,?,NULL,NULL,"
                "'migration/bootstrap_behaviour_rules_v1_20260818.py')",
                (name, col, ordinal, coltype, ispk, notnull, colnuse))
            report.append(f"cfg_column ({name}.{col}) added")
        else:
            report.append(f"cfg_column ({name}.{col}) already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    conn.executescript(_DDL)
    report.append("cfg_behaviour_class + cfg_behaviour_rule tables ensured")

    _enum(conn, "config_module", "behaviour", report)

    _setting(conn, "governance.operational_behaviour_control",
             '"Project operational behaviour (chat, terminal, sqlite, documentation, llm_output, '
             'and any further class identified) is governed by cfg_behaviour_class + '
             'cfg_behaviour_rule -- scope is the WHOLE PROJECT, not iba/app/** only (researcher, '
             '2026-08-18). A rule lives in exactly one place: once captured here, its document '
             'version is replaced with a pointer, never left standing alongside it. Where a '
             'class boundary is unclear, the boundary is defined explicitly as a '
             'governance.behaviour_boundary.<topic> setting rather than left implicit."',
             "entry-point anchor for the operational-behaviour cfg layer -- part (a) of "
             "escalation #715", "governance", report)

    for class_, description in _CLASSES:
        if not conn.execute("SELECT 1 FROM cfg_behaviour_class WHERE class=?", (class_,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_behaviour_class (class, authoritative_doc, description, "
                "added_at, inactive) VALUES (?,NULL,?,?,0)", (class_, description, _NOW))
            report.append(f"cfg_behaviour_class {class_!r} added (authoritative_doc: undecided)")
        else:
            report.append(f"cfg_behaviour_class {class_!r} already present")

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

    _write_grant(conn, "configmaint.propose", "cfg_behaviour_class", report)
    _table_and_columns(conn, "cfg_behaviour_class",
                       "one row per operational-behaviour class",
                       "the taxonomy for governance.operational_behaviour_control -- chat, "
                       "terminal, sqlite, documentation, llm_output, and any further class "
                       "identified in later consolidation cycles.",
                       [("class", "TEXT", 1, 1, "the behaviour-class key (e.g. 'sqlite') -- "
                        "referenced by cfg_behaviour_rule.class"),
                        ("authoritative_doc", "TEXT", 0, 0, "the single document authoritative "
                        "for this class's non-cfg content, once decided (single-authority "
                        "discipline, class='documentation' rule) -- NULL until the doc-mapping "
                        "consolidation cycle runs; not guessed"),
                        ("description", "TEXT", 0, 1, "what this behaviour class covers and how "
                        "it's distinct from its neighbours"),
                        ("added_at", "TEXT", 0, 1, "when the class was registered"),
                        ("inactive", "INTEGER", 0, 1, "0=active, 1=retired (kept for history)")],
                       report)
    _write_grant(conn, "configmaint.propose", "cfg_behaviour_rule", report)
    _table_and_columns(conn, "cfg_behaviour_rule",
                       "one row per rule within a behaviour class",
                       "the actual rule content per class -- worded as definitive statements, "
                       "not open for interpretation (researcher instruction 2026-08-18). Replaces "
                       "prose-only rules in CLAUDE.md/memory/wa_rule_registry as they're migrated "
                       "in through later consolidation cycles.",
                       [("id", "INTEGER", 1, 1, "surrogate key"),
                        ("class", "TEXT", 0, 1, "which cfg_behaviour_class this rule belongs to"),
                        ("rule_key", "TEXT", 0, 1, "short kebab-case identifier, unique within "
                        "its class"),
                        ("rule_text", "TEXT", 0, 1, "the rule itself, as a definitive statement -- "
                        "if the rule involves a choice, the choices and which applies when are "
                        "spelled out here, not left implicit"),
                        ("source", "TEXT", 0, 1, "provenance -- which prior rule/doc/researcher "
                        "statement this was derived from"),
                        ("enforced_by", "TEXT", 0, 0, "the mechanical check that flags deviation "
                        "from this rule, if one exists yet -- honestly NULL/'not yet' where none "
                        "does (researcher instruction: deviation must be monitored ongoing, a "
                        "follow-on build item)"),
                        ("added_at", "TEXT", 0, 1, "when the rule was registered"),
                        ("active", "INTEGER", 0, 1, "0=retired, 1=live")],
                       report)

    _utility(conn, "bootstrap_behaviour_rules",
            "iba/app/migration/bootstrap_behaviour_rules_v1_20260818.py",
            "One-off migration: creates cfg_behaviour_class/cfg_behaviour_rule and seeds cycle-1 "
            "('the obvious ones') content -- GR-DB-001/GR-PROC-001/GR-REF-001/GR-PROG-009 reworded "
            "as definitive statements. Escalation #715.", report)

    conn.commit()
    conn.close()

    print("operational-behaviour cfg bootstrap (cycle 1 -- the obvious ones):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
