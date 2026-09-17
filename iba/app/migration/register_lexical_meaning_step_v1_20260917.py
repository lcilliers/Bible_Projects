"""Register `lexical.meaning` -- the `verse-reading` stage's execution step (escalation #1706
Phase C, 2026-09-17). This is the first piece of the actual Phase C build: registers the `cfg_step`
and `cfg_method_rule` rows the handler code (built in the same session, `handlers/lexical.py:
meaning`, `lib/versereadinggenerate.py`) depends on -- config before code, matching this project's
own established discipline.

What this stage does, per the day's own closed design chain: per-cluster (`#1711`), reads all 3
meaning sources as complementary evidence (`#1706` SS4A), presents every live role tag per word
including the currently-unwired ones (`#1706` role-data-presentation doc SS6, resolved), and
answers the catalogue questions confirmed live at this grain: `M0.1` (Name and Naming), `M0.5`
(Lexical and Semantic Analysis), and `D7.7` (operation-anchored permeability, role-T3).

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_lexical_meaning_step_v1_20260917.py [--db PATH] [--dry-run]
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

        if not row_exists(cur, "SELECT 1 FROM cfg_step WHERE step=?", ("lexical.meaning",)):
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                ("verse-lexical", 6, "lexical.meaning",
                 "iba.app.handlers.lexical:meaning", "cluster",
                 "The verse-reading stage (#1711): per-cluster, pre-subgroup Layer 2. Reads all 3 "
                 "meaning sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) "
                 "as complementary evidence for every strong the cluster's role-annotated word list "
                 "covers (verse_lexical.role, including currently-unwired role-T2/T6/T10-T15 tags, "
                 "not just the mechanically-wired subset), and answers M0.1 (Name and Naming), M0.5 "
                 "(Lexical and Semantic Analysis), and D7.7 (operation-anchored permeability) from "
                 "wa_obs_question_catalogue. Assembles the LLM payload and estimates cost; the live "
                 "API call and the DB write are separate, explicit steps (cost preview before "
                 "spend, never silent).",
                 "operations"))
            report.append("cfg_step lexical.meaning inserted")
        else:
            report.append("cfg_step lexical.meaning already present — skipped")

        rules = [
            ("read-3-sources-complementary",
             "Every strong's meaning is read from all 3 sources (strong_meaning_tree, "
             "strong_lexicon.lsj, strong_lexicon.mounce) as complementary evidence, never picking "
             "one and dropping the others. Researcher, verbatim, 2026-09-16: \"the important take "
             "away is to read meaning from all three tables because they are complementary, rather "
             "than replacing each other.\" Inherited directly from process (c)'s own rule 2, not a "
             "new principle for this stage.",
             "#1706 SS4A, 2026-09-16"),
            ("role-list-includes-unwired-tags",
             "The role-annotated word list given to the LLM includes every live role-cluster tag "
             "(cluster.cluster_code T2-T15) on a strong, not only the mechanically-wired subset "
             "(role-T4/T5/T7/T8/T9). Researcher's own registry-construction principle applies: "
             "\"the cost of over-inclusion is visible and recoverable; the cost of silent omission "
             "is invisible and not recoverable.\" Excluding the currently-unwired tags would "
             "silently reproduce the exact gap #1704's five-phase investigation diagnosed.",
             "#1706 role-data-presentation doc SS6, 2026-09-17"),
            ("per-cluster-scope-not-subgroup",
             "This stage runs per-cluster (all strongs the cluster's role list covers), anchored "
             "to the cluster as \"home\" -- not per-subgroup, since subgroups do not exist yet at "
             "this pre-subgroup stage. Confirmed scope grain, #1711 v11.",
             "#1711 v11, 2026-09-16"),
            ("answers-M0.1-M0.5-D7.7",
             "This stage's catalogue linkage: M0.1 (Name and Naming) derived from the strong's "
             "surface + its meaning in context; M0.5 (Lexical and Semantic Analysis) derived from "
             "the 3 meaning sources jointly; D7.7 (operation-anchored permeability, role-T3) where "
             "an action/operation word co-occurs with a party tag in the same verse. M0.1/M0.5 were "
             "T1.1/T7.1 before the 2026-09-17 catalogue realignment (#1712) -- same substance, "
             "renumbered codes.",
             "#1711 v11 + #1712 catalogue realignment, 2026-09-17"),
            ("needs-adjacent-verse-context-applies-here",
             "needs_adjacent_verse_context applies at this stage too, not only char-reading -- "
             "the checklist's own cross-cutting rule 5a already governs every flag-shaped "
             "observation the pipeline raises. When raised, obs_text must state explicitly what's "
             "outstanding and what the follow-up cross-check needs to establish.",
             "ib-observation-governing-rules-checklist rule 5a/5a-i/5b"),
            ("cost-bounded-small-batches",
             "Never a full-cluster-corpus push in one call. Batches capped the same way "
             "lexical.enrich's own write path already enforces (passage.max_verses-sized chunks), "
             "cost estimated and shown before any live API call, per "
             "project_api_reads_budget_bounded_small_batches.",
             "established project-wide convention, lexicalenrichgenerate.py precedent"),
        ]
        for rule_key, rule_text, source_doc in rules:
            if not row_exists(cur, "SELECT 1 FROM cfg_method_rule WHERE rule_key=?", (rule_key,)):
                cur.execute(
                    "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, "
                    "enforced_by, ordinal, active) VALUES (?,?,?,?,?,?,1)",
                    ("lexical.meaning", rule_key, rule_text, source_doc,
                     "lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17", 0))
                report.append(f"cfg_method_rule {rule_key} inserted")
            else:
                report.append(f"cfg_method_rule {rule_key} already present — skipped")

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
