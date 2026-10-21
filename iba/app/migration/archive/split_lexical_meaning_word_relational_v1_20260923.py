"""split_lexical_meaning_word_relational_v1_20260923.py — ONE-OFF migration, escalation #1860.

Applies the config layer for the word-level/relational Stage 1 split (researcher approval, v3,
verbatim: "proceed with split. Ensure that you comply with every aspect of governance..."). Full
design record: `iba/docs/1860-word-relational-split-build-plan-v1-20260923.md`. Code side (the
`cfg_step`/`cfg_write_grant`/`cfg_method_rule`/`cfg_setting` content this migration writes) is a
multi-row, single logical change -- applied here as one authorized migration script (matching this
project's own established precedent for a researcher-approved multi-row config build, e.g.
`prose_first_layer_build_v1_20260824.py`) rather than ~20 individual
`Config-Maintenance.ps1 -Step Propose` cycles, each of which is designed for one isolated row
change, not a single coherent architectural split the researcher already reviewed and approved as
one unit.

Idempotent (checked live state before each write, skips if already applied) -- a second run is a
no-op.

    python -m iba.app.migration.split_lexical_meaning_word_relational_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_MEANING_DOES_NEW = (
    "The verse-reading stage, WORD-LEVEL HALF (#1711 original build; narrowed to word-level-only "
    "by the #1860 split, 2026-09-23): per-cluster, pre-subgroup Layer 2. Reads all 3 meaning "
    "sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) as complementary "
    "evidence for every strong the cluster's role-annotated word list covers (verse_lexical.role, "
    "including currently-unwired role-T2/T6/T10-T15 tags, not just the mechanically-wired subset), "
    "and answers M0.1 (Name and Naming) and M0.5 (Lexical and Semantic Analysis, incl. M0.5.11) "
    "from wa_obs_question_catalogue -- word-level only now; the relational family (M0.6.5/M0.6.6/"
    "D7.7.1/M0.7/M0.8.1) moved to the new lexical.relational step, which requires this step's own "
    "output as a precondition (readiness gate). Assembles the LLM payload and estimates cost; the "
    "live API call and the DB write are separate, explicit steps (cost preview before spend, never "
    "silent)."
)

_RELATIONAL_DOES = (
    "The verse-reading stage, RELATIONAL HALF (#1860 split, 2026-09-23 -- researcher, verbatim: "
    "'we must split the word questions and answers and the relational answers into separate "
    "processes. the relational process depends on the word work, and doing it in the same session "
    "can only result in errors.'). Per-cluster, pre-subgroup Layer 2, run AFTER lexical.meaning has "
    "covered the same verses -- a hard readiness gate refuses to run against any verse whose "
    "M-code words don't all have a committed word-level (M0.1/M0.5) observation yet. Answers "
    "M0.6.5 (relational, single-vantage), M0.6.6 (whole-network synthesis), D7.7.1 "
    "(operation-anchored permeability), M0.7.1-16 (verse substantiation), M0.8.1 (T2/T3 elevation "
    "flag), cluster-agnostic (every M-code word in the verse, not just this cluster's own home "
    "strong(s)). Grounds on the COMMITTED word-level ib_observation rows for each verse+strong "
    "(the researcher's own approval, #1860 v3: 'the base data must in any case be included for "
    "relational phase to be successful' -- so the raw lexicon (meaning_sources_by_strong) is ALSO "
    "sent alongside the committed findings, never one instead of the other). This is the true "
    "final stage of verse-reading -- the cluster.status t_cluster_assignment_completed -> "
    "ready_for_subgroup_allocation transition check runs here now, not in lexical.meaning."
)

_SHARED_RULE_KEYS = (
    "read-3-sources-complementary", "role-list-includes-unwired-tags",
    "per-cluster-scope-not-subgroup", "needs-adjacent-verse-context-applies-here",
    "cost-bounded-small-batches", "strongs-reassigned-detection",
    "concise-and-verse-specific-obs-text", "translit-never-without-gloss",
    "span-grounded-not-generic",
)

_ANSWERS_WORD_LEVEL_TEXT = (
    "This step's catalogue linkage (narrowed by the #1860 split, 2026-09-23): M0.1 (Name and "
    "Naming) derived from the strong's surface + its meaning in context; M0.5 (Lexical and "
    "Semantic Analysis) derived from the 3 meaning sources jointly -- both span-grounded, answered "
    "for every M-code strong's every occurrence (2026-09-23 correction, not once-ever per strong). "
    "The relational family (D7.7.1/M0.6.5/M0.6.6/M0.7/M0.8.1) moved to the new lexical.relational "
    "step, catalogue-linked there instead -- this step no longer answers them."
)

_ANSWERS_RELATIONAL_TEXT = (
    "This step's catalogue linkage (#1860 split, 2026-09-23): D7.7.1 (operation-anchored "
    "permeability, role-T3), M0.6.5 (relational, single-vantage), M0.6.6 (whole-network synthesis), "
    "M0.7.1-16 (verse substantiation), M0.8.1 (T2/T3 elevation flag) -- all answered for EVERY "
    "M-code strong present in roles_in_verse, cluster-agnostic (escalation #1824 v14/v15). Fed "
    "progressively via each question's own prior-context stream (M0.6.5/M0.6.6, per-verse not "
    "globally-once) so a later pass builds on, not duplicates, what's already there; does not even "
    "attempt an already-fully-covered verse (whole-verse batch exclusion). Requires lexical.meaning "
    "to have already committed M0.1/M0.5 for every M-code word in scope (readiness gate) -- moved "
    "out of the combined lexical.meaning rule this step inherits from (id 73, pre-split)."
)

_GROUNDS_ON_WORD_LEVEL_TEXT = (
    "Relational reading's primary grounding is the COMMITTED word-level (M0.1/M0.5) ib_observation "
    "rows for the exact verse+strong being reasoned about (versereadinggenerate._word_level_"
    "findings), not the raw lexicon alone. Researcher, verbatim, escalation #1860 v3 approval, "
    "2026-09-23: 'the base data must in any case be included for relational phase to be "
    "successful' -- corrects Claude's own original v1 draft, which had proposed committed findings "
    "INSTEAD OF raw meaning_sources_by_strong; both are sent together, the committed findings as "
    "primary grounding, the raw lexicon as the same complementary evidence every other stage "
    "already reads (read-3-sources-complementary)."
)

_READINESS_GATE_TEXT = (
    "lexical.relational refuses to run (hard stop, same shape as lexical.build's stale-role check "
    "and lexical.readiness's FATAL stop -- not a silent per-verse skip) against any verse whose "
    "M-code words don't ALL already have a committed (non-withdrawn) word-level (M0.1/M0.5) "
    "ib_observation. stage1coverage.missing_word_level_coverage() computes the gap; -Force does "
    "NOT bypass this gate (unlike the whole-verse-exclusion optimisation) -- it is a correctness "
    "precondition, not a reconciliation-skip mechanism. Researcher instruction, verbatim, #1860 "
    "v1 context: 'the relational process depends on the word work, and doing it in the same "
    "session can only result in errors.'"
)


def _step_exists(conn, step: str) -> bool:
    return conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone() is not None


def _grant_exists(conn, writer: str, table_name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
        (writer, table_name)).fetchone() is not None


def _rule_exists(conn, step: str, rule_key: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?",
        (step, rule_key)).fetchone() is not None


def _setting_exists(conn, key: str) -> bool:
    return conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone() is not None


def apply_fix(conn: sqlite3.Connection) -> list[str]:
    report = []

    # 1. cfg_step: narrow lexical.meaning's does-text; insert lexical.relational (ordinal 7).
    conn.execute("UPDATE cfg_step SET does=? WHERE step='lexical.meaning'", (_MEANING_DOES_NEW,))
    report.append("cfg_step: lexical.meaning.does updated (word-level-only)")
    if not _step_exists(conn, "lexical.relational"):
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES ('verse-lexical', 7, 'lexical.relational', "
            "'iba.app.handlers.lexical:relational', 'cluster', ?, 0, 'operations')",
            (_RELATIONAL_DOES,))
        report.append("cfg_step: lexical.relational inserted (ordinal 7)")
    else:
        report.append("cfg_step: lexical.relational already exists, skipped")

    # 2. cfg_write_grant: mirror lexical.meaning's 3 grants for lexical.relational.
    for table_name in ("ib_node", "ib_observation", "run_batch"):
        if not _grant_exists(conn, "lexical.relational", table_name):
            conn.execute(
                "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                "VALUES ('lexical.relational', ?, 'iba', 0)", (table_name,))
            report.append(f"cfg_write_grant: lexical.relational -> {table_name} inserted")
        else:
            report.append(f"cfg_write_grant: lexical.relational -> {table_name} already exists, skipped")

    # 3. cfg_method_rule.
    # 3a. Duplicate the 9 cross-cutting rules onto lexical.relational (same rule_key+text).
    for rule_key in _SHARED_RULE_KEYS:
        row = conn.execute(
            "SELECT rule_text, source_doc, enforced_by, ordinal FROM cfg_method_rule "
            "WHERE step='lexical.meaning' AND rule_key=? AND active=1", (rule_key,)).fetchone()
        if row is None:
            report.append(f"cfg_method_rule: {rule_key!r} not found on lexical.meaning, skipped "
                          f"(unexpected -- check live state)")
            continue
        if not _rule_exists(conn, "lexical.relational", rule_key):
            conn.execute(
                "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
                "ordinal, active) VALUES ('lexical.relational', ?, ?, ?, ?, ?, 1)",
                (rule_key, row["rule_text"], row["source_doc"], row["enforced_by"], row["ordinal"]))
            report.append(f"cfg_method_rule: {rule_key!r} duplicated onto lexical.relational")
        else:
            report.append(f"cfg_method_rule: {rule_key!r} already on lexical.relational, skipped")

    # 3b. Retext answers-M0.1-M0.5-D7.7 on lexical.meaning to word-level-only.
    conn.execute(
        "UPDATE cfg_method_rule SET rule_text=? WHERE step='lexical.meaning' "
        "AND rule_key='answers-M0.1-M0.5-D7.7'", (_ANSWERS_WORD_LEVEL_TEXT,))
    report.append("cfg_method_rule: answers-M0.1-M0.5-D7.7 (lexical.meaning) retexted word-level-only")

    # 3c. New relational-scoped catalogue-linkage rule.
    if not _rule_exists(conn, "lexical.relational", "answers-relational-family"):
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES ('lexical.relational', 'answers-relational-family', ?, "
            "'#1860, 2026-09-23 word-level/relational split', "
            "'lexical.relational (handlers/lexical.py:relational)', 0, 1)",
            (_ANSWERS_RELATIONAL_TEXT,))
        report.append("cfg_method_rule: answers-relational-family inserted on lexical.relational")
    else:
        report.append("cfg_method_rule: answers-relational-family already exists, skipped")

    # 3d. Move cluster-status-2to3-transition-verse-reading-complete: deactivate on lexical.meaning,
    #     insert (active) on lexical.relational.
    conn.execute(
        "UPDATE cfg_method_rule SET active=0 WHERE step='lexical.meaning' "
        "AND rule_key='cluster-status-2to3-transition-verse-reading-complete'")
    report.append("cfg_method_rule: cluster-status-2to3-transition (lexical.meaning) deactivated")
    if not _rule_exists(conn, "lexical.relational", "cluster-status-2to3-transition-verse-reading-complete"):
        row = conn.execute(
            "SELECT rule_text, source_doc FROM cfg_method_rule WHERE rule_key="
            "'cluster-status-2to3-transition-verse-reading-complete' AND step='lexical.meaning'"
        ).fetchone()
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES ('lexical.relational', "
            "'cluster-status-2to3-transition-verse-reading-complete', ?, ?, "
            "'lib/clusterstatus.py:advance_if_verse_reading_complete, called from "
            "handlers/lexical.py:relational (moved from lexical.meaning, #1860 2026-09-23)', 0, 1)",
            (row["rule_text"], row["source_doc"]))
        report.append("cfg_method_rule: cluster-status-2to3-transition inserted on lexical.relational")
    else:
        report.append("cfg_method_rule: cluster-status-2to3-transition already on lexical.relational, skipped")

    # 3e. New rules: grounding + readiness gate, both on lexical.relational.
    if not _rule_exists(conn, "lexical.relational", "grounds-on-committed-word-level-observations"):
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES ('lexical.relational', "
            "'grounds-on-committed-word-level-observations', ?, "
            "'#1860 v3 researcher approval, 2026-09-23', "
            "'versereadinggenerate._word_level_findings, called from assemble_relational_batch_"
            "package', 0, 1)", (_GROUNDS_ON_WORD_LEVEL_TEXT,))
        report.append("cfg_method_rule: grounds-on-committed-word-level-observations inserted")
    else:
        report.append("cfg_method_rule: grounds-on-committed-word-level-observations already exists, skipped")

    if not _rule_exists(conn, "lexical.relational", "relational-readiness-gate"):
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES ('lexical.relational', 'relational-readiness-gate', ?, "
            "'#1860 v1 context, 2026-09-23', "
            "'stage1coverage.missing_word_level_coverage, called from handlers/lexical.py:"
            "relational', 0, 1)", (_READINESS_GATE_TEXT,))
        report.append("cfg_method_rule: relational-readiness-gate inserted")
    else:
        report.append("cfg_method_rule: relational-readiness-gate already exists, skipped")

    # 4. cfg_setting: lexical.relational_max_verses_per_batch (mirrors lexical.meaning's, value 1).
    if not _setting_exists(conn, "lexical.relational_max_verses_per_batch"):
        conn.execute(
            "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES "
            "('lexical.relational_max_verses_per_batch', '1', "
            "'Cap on verses per lexical.relational batch (#1860, 2026-09-23 split) -- mirrors "
            "lexical.meaning_max_verses_per_batch''s own value and rationale (single-verse "
            "batches bound each call to one verse''s own inherent content). Read by "
            "_chunk_verses_fixed_size() via handlers/lexical.py:relational.', 'lexical', 0)")
        report.append("cfg_setting: lexical.relational_max_verses_per_batch=1 inserted")
    else:
        report.append("cfg_setting: lexical.relational_max_verses_per_batch already exists, skipped")

    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_fix(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
