"""fix_stage1_governance_gaps_v1_20260922.py -- ONE-OFF, idempotent. Escalation #1824, researcher
instruction 2026-09-22, verbatim: "all the work you did today and yesterday must be FULLY
GOVERNANCE compliant. audit it and confirm positive that you checked every config, every utility,
every code change, every instruction affected."

Full audit run against every BUILD.md entry #306-318 (2026-09-21/22, the actual "today and
yesterday" scope) plus a column-by-column cfg_column/cfg_enum sweep of ib_observation/ib_node.
Found 5 real gaps, fixed here (see BUILD.md #319 for the full write-up):

1. `lexical.meaning_max_strongs_per_batch` (BUILD #311, 2026-09-21) -- read by
   iba/app/handlers/lexical.py's own chunking logic (the actual cost-driving cap, replaced verse-
   count chunking after 3 failed live attempts), but never registered in cfg_setting -- silently
   running on its hardcoded fallback (8) this whole time, invisible to config governance.
2. `lexical.meaning_max_verses_per_batch` -- the OLD setting #1 replaced, still registered and
   live but read by zero live code (confirmed: grep across iba/app/handlers + iba/app/lib finds
   only this migration's own reference). Marked inactive, not deleted -- same "soft-delete,
   auditable" discipline this project uses everywhere else.
3. `cfg_method_rule` `answers-M0.1-M0.5-D7.7` (step=lexical.meaning) was stale relative to live
   code from BUILD #316 (2026-09-22, this session's own cluster-agnostic correction) -- its text
   still described M0.6.5/M0.6.6/D7.7.1 as answered only for "this cluster's own home strong(s)"
   with a later cluster's pass building on an earlier one's finding, when the live code (and
   catalogue) has answered every M-code strong regardless of home cluster since #316. Updated to
   match.
4. The #1824 "governing principle" this session has followed rigorously since v11 -- every
   correction to ib_observation happens ONLY as a byproduct of record_one_observation() processing
   a real, fresh LLM answer, never an offline script -- existed only in a design doc's prose and
   BUILD.md narrative text, never a registered cfg_behaviour_rule. A real, if self-caught,
   violation of governance.rules_must_be_config_driven. Registered here.
5. `report.stage1_coverage_validation_path` (BUILD #315, 2026-09-22, this session's own gap) --
   the coverage-validation report lexical.py writes on every live call had its path hardcoded as
   an f-string rather than config-defined, unlike the established precedent
   (report.batch_progress_path, report.lexical_notes_output_pattern) governance.reports_must_
   persist's own "config-defined report path" requirement implies. Registered here; the code
   change to actually read it lives in the same commit as this migration, not in this file.

Safe to re-run: every insert/update is guarded.

    python -m iba.app.migration.fix_stage1_governance_gaps_v1_20260922
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def row_exists(cur, sql, params) -> bool:
    return cur.execute(sql, params).fetchone() is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        # 1. Register the setting the code actually reads.
        if not row_exists(cur, "SELECT 1 FROM cfg_setting WHERE key=?",
                          ("lexical.meaning_max_strongs_per_batch",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("lexical.meaning_max_strongs_per_batch", "8",
                 "Cap on cumulative distinct M-code strongs per lexical.meaning batch -- the real "
                 "cost driver for M0.7's front-loaded per-strong question volume (escalation "
                 "#1825/#1826/#1827, 2026-09-21). Replaced the old verse-count cap "
                 "(lexical.meaning_max_verses_per_batch, now inactive) after a fixed verse count "
                 "was confirmed live to never reliably bound output when strong-density varies "
                 "3.5x between chunks. Read by _chunk_verses_by_strong_density() "
                 "(iba/app/handlers/lexical.py) -- found live 2026-09-22 (escalation #1824 "
                 "governance audit) that this setting was never actually registered despite being "
                 "load-bearing since #311; the code was silently running on this same fallback "
                 "value the whole time.", "lexical"))
            report.append("cfg_setting lexical.meaning_max_strongs_per_batch inserted")
        else:
            report.append("cfg_setting lexical.meaning_max_strongs_per_batch already present — skipped")

        # 2. Deprecate the setting no code reads anymore.
        cur.execute("SELECT inactive, use FROM cfg_setting WHERE key=?",
                   ("lexical.meaning_max_verses_per_batch",))
        row = cur.fetchone()
        if row is not None and row[0] == 0:
            cur.execute(
                "UPDATE cfg_setting SET inactive=1, use=? WHERE key=?",
                (f"{row[1]} -- SUPERSEDED 2026-09-21 by lexical.meaning_max_strongs_per_batch "
                 f"(escalation #1825/#1826/#1827): fixed verse-count chunking couldn't reliably "
                 f"bound output when strong-density varies (confirmed live, 3.5x spread across "
                 f"M67's own chunks). No live code reads this key anymore (confirmed live via "
                 f"grep, escalation #1824 governance audit, 2026-09-22). Marked inactive, not "
                 f"removed -- auditable history.",
                 "lexical.meaning_max_verses_per_batch"))
            report.append("cfg_setting lexical.meaning_max_verses_per_batch marked inactive")
        elif row is not None:
            report.append("cfg_setting lexical.meaning_max_verses_per_batch already inactive — skipped")
        else:
            report.append("cfg_setting lexical.meaning_max_verses_per_batch not found — nothing to deprecate")

        # 3. Update the stale method rule to match live cluster-agnostic behaviour (BUILD #316).
        cur.execute("SELECT rule_text FROM cfg_method_rule WHERE rule_key=? AND step=?",
                   ("answers-M0.1-M0.5-D7.7", "lexical.meaning"))
        row = cur.fetchone()
        new_text = (
            "This stage's catalogue linkage: M0.1 (Name and Naming) derived from the strong's "
            "surface + its meaning in context; M0.5 (Lexical and Semantic Analysis) derived from "
            "the 3 meaning sources jointly -- both word-level, answered once ever per strong, "
            "front-loaded for every M-code strong in the verse regardless of cluster (#1723/#1820). "
            "D7.7 (operation-anchored permeability, role-T3), M0.6.5 (relational, single-vantage), "
            "and M0.6.6 (whole-network synthesis, added #1819 2026-09-21) are all answered for "
            "EVERY M-code strong present in roles_in_verse, not just the pass's own home cluster's "
            "strong -- corrected 2026-09-22 (escalation #1824 v14/v15, researcher: \"verse reading "
            "is supposed to be agnostic to cluster definition. every M-code word has the same "
            "status in the verse and need to be treated the same\"); the prior text here described "
            "the pre-correction home-strong-only scoping, now stale. Fed progressively via each "
            "question's own prior-context stream (per-verse, not globally-once) so a later pass "
            "touching an already-read verse builds on, not duplicates, what's already there -- "
            "and, since #1824 v18 (2026-09-22), does not even attempt an already-fully-covered "
            "verse at all (whole-verse batch exclusion). M0.1/M0.5 were T1.1/T7.1 before the "
            "2026-09-17 catalogue realignment (#1712) -- same substance, renumbered codes."
        )
        if row is not None and row[0] != new_text:
            cur.execute(
                "UPDATE cfg_method_rule SET rule_text=? WHERE rule_key=? AND step=?",
                (new_text, "answers-M0.1-M0.5-D7.7", "lexical.meaning"))
            report.append("cfg_method_rule answers-M0.1-M0.5-D7.7 (lexical.meaning) text updated")
        elif row is not None:
            report.append("cfg_method_rule answers-M0.1-M0.5-D7.7 (lexical.meaning) already current — skipped")
        else:
            report.append("cfg_method_rule answers-M0.1-M0.5-D7.7 (lexical.meaning) not found — nothing to update")

        # 4. Register the #1824 governing principle as a real behaviour rule, not just prose.
        if not row_exists(cur, "SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?",
                          ("stage1-corrections-only-via-real-rerun",)):
            cur.execute(
                "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
                "added_at, active, enforcement_status) VALUES (?,?,?,?,?,datetime('now'),1,?)",
                ("sqlite", "stage1-corrections-only-via-real-rerun",
                 "Every correction to ib_observation (update, withdraw, consolidate) happens ONLY "
                 "as a byproduct of record_one_observation() (iba/app/lib/recordingpass.py) "
                 "processing a real, fresh LLM answer for the exact occurrence in question -- "
                 "never a standalone script that edits or derives content for existing rows "
                 "without a genuine new answer behind it. Researcher correction, escalation #1824 "
                 "v11, verbatim: \"none of the correction are done as fixes. they are all done as "
                 "the result of the update routine that runs on the json output that you got from "
                 "LLM... you should not reach back into the base data.\" An earlier design draft "
                 "for this same escalation proposed exactly such an offline backfill/consolidation "
                 "script and was rejected on these grounds. Reconciliation is therefore inherently "
                 "incremental: a verse's stale/duplicate data only gets cleaned up when that verse "
                 "is genuinely reprocessed (lexical.meaning -Force, #1824 Fix 3) -- there is no "
                 "batch-cleanup lever and none should be built.",
                 "escalation #1824 v11, 2026-09-22",
                 "iba/app/lib/recordingpass.py:record_one_observation (no automated check exists "
                 "yet that a future script complies -- structurally known, not mechanically "
                 "enforced)", "buildable_not_built"))
            report.append("cfg_behaviour_rule stage1-corrections-only-via-real-rerun inserted")
        else:
            report.append("cfg_behaviour_rule stage1-corrections-only-via-real-rerun already present — skipped")

        # 5. Register the coverage-validation report path (was hardcoded in lexical.py).
        if not row_exists(cur, "SELECT 1 FROM cfg_setting WHERE key=?",
                          ("report.stage1_coverage_validation_pattern",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("report.stage1_coverage_validation_pattern",
                 '"outputs/stage1-coverage-validation-{cluster_code}-{run_id}.csv"',
                 "Where lexical.meaning's own per-run coverage-validation report "
                 "(stage1coverage.validate_coverage, BUILD #315) is written, every live call -- "
                 "{cluster_code}/{run_id} substituted by the caller. Was a hardcoded f-string in "
                 "iba/app/handlers/lexical.py; governance.reports_must_persist's own \"config-"
                 "defined report path\" requirement (matching the established "
                 "report.batch_progress_path / report.lexical_notes_output_pattern precedent) "
                 "means it should have been this from the start -- found live 2026-09-22, "
                 "escalation #1824 governance audit.", "report"))
            report.append("cfg_setting report.stage1_coverage_validation_pattern inserted")
        else:
            report.append("cfg_setting report.stage1_coverage_validation_pattern already present — skipped")

        # Self-register in cfg_utility, inactive=1 once applied — same one-off-migration pattern
        # every other script in this directory follows.
        self_path = "iba/app/migration/fix_stage1_governance_gaps_v1_20260922.py"
        if not row_exists(cur, "SELECT 1 FROM cfg_utility WHERE file_path=?", (self_path,)):
            cur.execute(
                "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
                "VALUES (?,?,?,1,0)",
                ("fix_stage1_governance_gaps_v1_20260922", self_path,
                 "ONE-OFF migration, escalation #1824 -- fixes 5 real governance gaps found by a "
                 "full audit of 2026-09-21/22's Stage 1 work (2 unregistered/orphaned cfg_setting "
                 "keys, 1 stale cfg_method_rule, 1 undocumented behaviour rule, 1 hardcoded report "
                 "path). inactive=1 once applied -- a one-off, not a reusable routine."))
            report.append("cfg_utility (self) added")
        else:
            report.append("cfg_utility (self) already present")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
