"""memory_rules_to_config_v1_20261021.py -- escalation #2184 (option E of the #2179 review; element
of the IBA app reset, #2177): memory holds only what config cannot.

Researcher, 2026-10-21, verbatim: "There should be no instance of the same rule in multiple
documents." The control map (cfg_control_home, kind claude_memory) gives memory only who the
researcher is and pointers. Every live rule that existed only as a Claude memory file is added here
as a cfg_behaviour_rule; the memory files themselves are archived (record:
outputs/escalation/2184-memory-dispositions-v1-20261021.md).

Also: cfg_behaviour_class.authoritative_doc for 'chat' and 'terminal' pointed at
docs/interaction-preferences.md, whose content is rules 16-24 and 25-29; with the file archived,
the rules are the authority and the column is cleared.

Every write through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/memory_rules_to_config_v1_20261021.py [--db PATH]
"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2184-MEMORY-RULES-20261021"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DELIVERY = "Context-delivered at session start (rule 81)."


def src(slugs: str, extra: str = "") -> str:
    return (f"Moved from Claude memory ({slugs}) 2026-10-21, escalation #2184; the memory files are "
            f"archived in the memory folder's archive/." + (" " + extra if extra else ""))


RULES = [
    ("chat", "fix-standard-violations-dont-ask",
     "When work deviates from an already established, documented standard or pattern, it is fixed "
     "at once, not offered as a question ('should I fix it?'). A question is for a genuine new "
     "decision (rule 44), not for conforming to what is already settled.",
     src("feedback_fix_standard_violations_dont_ask; feedback_column_alignment_is_claudes_job_not_a_question_back")),
    ("chat", "read-instruction-in-whole-chat-context",
     "Each researcher instruction is read against the whole conversation, not only the last "
     "exchange; an escalation is scoped by everything the researcher has said about it.",
     src("feedback_read_researcher_comment_in_whole_chat_context")),
    ("chat", "names-not-bare-codes",
     "Codes are never shown bare: a cluster code with its full name, a dimension or step code with "
     "its name, a transliteration with its gloss. Design documents use descriptive names, never "
     "invented short codes that only make sense inside one document.",
     src("feedback_use_cluster_full_names; feedback_name_dimensions_not_just_codes; "
         "feedback_translit_always_with_gloss; feedback_use_descriptive_nomenclature_not_invented_codes")),
    ("chat", "ready-to-run-commands",
     "When the researcher is to run a command (an approval, a PS step), Claude gives the complete, "
     "ready-to-run PowerShell command in chat, not a pointer to the Excel tool sheet.",
     src("feedback_present_ready_to_run_ps_commands")),
    ("chat", "status-reports-checked-facts-only",
     "A status, close-out or summary report states only checked facts, each with the context needed "
     "to read it: no inferred dependency stated as fact, no bare number. It is concise and grouped "
     "by the researcher's own framing of the question, with its limits stated and its open items "
     "put in the register.",
     src("feedback_no_unchecked_claims_in_status_reports; feedback_report_shape_that_worked_ot02")),
    ("development", "match-established-convention-when-extending",
     "A new item added to an established, convention-governed structure (a catalogue, a naming "
     "scheme, a schema pattern, a document's register) matches the existing items' convention.",
     src("feedback_match_established_convention_when_extending")),
    ("development", "check-new-rules-against-existing-first",
     "Before a new cfg_behaviour_rule or governance setting is proposed, the live rule corpus is "
     "searched for one that already covers it, conflicts with it or should be amended instead.",
     src("feedback_check_new_rules_against_existing_governance_first")),
    ("development", "diagnosis-is-not-licence-to-build",
     "Diagnosing a gap, even with the researcher's general direction, is not authorisation to design "
     "and build the fix in the same pass: a design goes to the researcher as decision_required "
     "first, and design or build work (schema change, new mechanism, new code) is never raised as "
     "self_correctable.",
     src("feedback_design_build_needs_checkpoint_not_just_diagnosis; feedback_design_work_is_never_self_correctable")),
    ("development", "no-per-item-approval-steps-in-designs",
     "A workflow Claude designs does not insert per-item researcher approval steps or an end gate "
     "by default: Claude runs the lifecycle, the researcher's chat feedback is recorded verbatim, "
     "and an approval request is made only with the data needed to decide.",
     src("feedback_no_approval_steps_researcher_feedback_in_chat")),
    ("sqlite", "enumerate-link-tables-before-orphan-verdict",
     "Before a record is called unlinked, orphaned or unmapped, every junction or link table that "
     "references it is enumerated: linkage often lives in a subsidiary table.",
     src("feedback_enumerate_link_tables_first")),
    ("terminal", "tool-layer-escaping-checks",
     "Text written through the tool layer is checked for corruption: a backslash-b can land as byte "
     "0x08 (write it as bytes([92,98]) and check the file); in PowerShell double-quoted strings a "
     "backslash does not escape a dollar sign (use single quotes or a backtick); Bash mangles "
     "PowerShell here-strings (rule 27).",
     src("feedback_backslash_b_becomes_backspace_byte; feedback_powershell_dollar_escaping")),
    ("study_method", "read-verses-before-asking",
     "A question a verse reading could answer (e.g. whether a word belongs in a strand) is answered "
     "by reading the verses, never passed to the researcher.",
     src("feedback_read_verses_before_asking_researcher")),
    ("study_method", "surface-is-the-sensitivity-lens",
     "In any strand or word pull, verse_lexical.surface is analysed per Strong's first: the surface "
     "shows the different interpretations of the root that the gloss or suffix alone can miss.",
     src("feedback_surface_is_the_sensitivity_lens")),
    ("study_method", "filters-are-working-aids",
     "A pre-reading filter (e.g. buckets that split verses before reading) is a working aid the "
     "readings absorb; it is never raised as a standing decision item for the researcher.",
     src("feedback_filters_are_working_aids_not_decision_items")),
    ("study_method", "narrative-is-story-claims-are-derived",
     "The narrative is the story and is never cut into claims. A claim is a statement derived from "
     "sources beyond the mere text of a verse; quoting a verse is not a claim (rule 77).",
     src("feedback_narrative_is_story_claims_are_derived_statements")),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        for cls, key, text, source in RULES:
            if not conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
                                (cls, key)).fetchone():
                apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {}, {
                    "class": cls, "rule_key": key, "rule_text": text, "source": source,
                    "enforced_by": DELIVERY, "added_at": NOW, "active": 1,
                    "enforcement_status": "context_delivered"}); n += 1
        for cls in ("chat", "terminal"):
            row = conn.execute("SELECT authoritative_doc FROM cfg_behaviour_class WHERE class=?",
                               (cls,)).fetchone()
            if row and row[0]:
                apply_logged(conn, RUN_ID, "cfg_behaviour_class", "update", {"class": cls},
                             {"authoritative_doc": None}); n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
