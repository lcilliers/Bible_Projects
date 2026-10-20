"""session_routines_2173_v1_20261020.py -- escalation #2173 (and #2174): the config for the rebuilt
start-project and session-close routines, and the rule contradictions the audit found.

Proposals (researcher feedback recorded verbatim on #2173 v1-v12):
  outputs/markdown/session-routines-start-project-change-proposal-v1-20261020.md (P0-P5, S1-S6, G1-G12)
  outputs/markdown/session-routines-session-close-change-proposal-v1-20261020.md (SC1-SC14, G13-G14)
Researcher, chat 2026-10-20 (verbatim): "This is your domain, I am expecting you to do a
professional, complete, with proper controls, self audit job of preparing the code and updating the
tables and documentation." ... "I also not you created 2174 which is a subset of the work and must
also be included."

Developer Mode: every cfg_* write goes through configmaint.apply_logged (cfg_behaviour_rule 75),
run_id DEVMODE-2173-SESSION-ROUTINES-20261020. Idempotent (each row is compared before it is
written). One transaction. No schema change.

Usage:
    python -m iba.app.migration.session_routines_2173_v1_20261020 [--db PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

from iba.app.handlers.configmaint import apply_logged
from iba.app.lib.cfg import Cfg, DB_PATH

RUN_ID = "DEVMODE-2173-SESSION-ROUTINES-20261020"
THIS = "iba/app/migration/session_routines_2173_v1_20261020.py"
NOW = "2026-10-20T00:00:00Z"
SRC = ("Escalation #2173 (researcher, chat 2026-10-20, verbatim on #2173 v1-v12); proposals "
       "outputs/markdown/session-routines-start-project-change-proposal-v1-20261020.md and "
       "-session-close-change-proposal-v1-20261020.md")


def J(v) -> str:
    return json.dumps(v, ensure_ascii=False)


# ── cfg_enum (G1; P2) ────────────────────────────────────────────────────────────────────────
ENUMS = {
    "escalation_state_open": ["raised", "in-progress", "re-assigned"],
    "escalation_state_parked": ["on-hold"],
    "escalation_state_terminal": ["completed", "closed", "withdraw", "supersede"],
    "compliance_rule_status": ["engaged", "not engaged"],
}

# ── cfg_setting: key -> (module, value, use) ─────────────────────────────────────────────────
SETTINGS = {
    "escalation.context_report_path": ("escalation", "outputs/escalation/escalation-context.md",
        "#2173 P1: report of every file each open escalation names, resolved to its latest live "
        "version (Escalation.ps1 -Action Context; lib/escalationcontext.py)"),
    "escalation.context_file_extensions": ("escalation",
        [".md", ".csv", ".py", ".ps1", ".json", ".xlsx", ".txt", ".sql", ".html", ".jsonl"],
        "#2173 P1: the extensions that mark a file reference in escalation text"),
    "escalation.thread_audit_report_path": ("escalation", "outputs/escalation/escalation-thread-audit.md",
        "#2173 P5: thread audit report (Escalation.ps1 -Action ThreadAudit; lib/threadaudit.py)"),
    "escalation.worked_strand_escalations": ("escalation", {
        "M01": [1962], "M02": [1963], "M25": [1932], "M47": [1911, 2172], "M64": [1978, 1986],
        "M18": [1993], "M72": [1998], "M09": [2148], "M08": [2156], "M07": [2171]},
        "#2173 P5 T-d: per cluster, the escalations that carry its strand. A strand counts as "
        "worked only when every listed escalation is completed (read from state at audit time, "
        "never from memory); M47 lists #2172, so it is not worked while #2172 is open. Add a "
        "cluster here when its strand escalation is raised."),
    "compliance.dir": ("behaviour", "Logs/compliance/",
        "#2173 P2: folder of the session compliance files COMPLIANCE-<date>-<session8>.md"),
    "compliance.acknowledgement": ("behaviour",
        "I have read the governance settings, behaviour rules and escalation rules, and will "
        "comply with them.",
        "#2173 P2 C: the sentence the compliance file must carry (checked)"),
    "compliance.copy_shingle_words": ("behaviour", 3,
        "#2173 P2 B: n for the n-word runs used to tell a copied restatement from a reading"),
    "compliance.copy_share_max": ("behaviour", 0.6,
        "#2173 P2 B: a restatement whose n-word runs occur in the rule text at this share or more "
        "is a copy, not a reading (a finding)"),
    "compliance.copy_min_words": ("behaviour", 8,
        "#2173 P2 B: a restatement under this many words is not judged as a copy (a short line on "
        "the same subject shares most of its word runs with the rule without copying it)"),
    "compliance.engaged_statuses": ("behaviour", ["engaged"],
        "#2173 P2 D: the statuses whose rows need evidence at close"),
    "spine.meaning_lexicon_languages": ("validation", ["Greek"],
        "#2173 P3: languages whose strongs are checked for a strong_lexicon row (lsj, mounce). "
        "Evidence 2026-10-20: 25 Hebrew strongs sampled at random from STEP returned no lsjDefs "
        "and no shortDefMounce (LSJ and Mounce are Greek lexicons); every Greek strong has a row."),
    "narrative.quote_min_words": ("narrative", 2,
        "#2173 G14: quoted parts shorter than this many words are not quote-checked"),
    "session_close.no_record_messages": ("validation",
        ["/start-project", "/session-close", "/developer-mode", "/exit-developer-mode"],
        "#2173 SC3: session-start/close command names that are researcher messages needing no "
        "escalation record (compared normalised, with up to 12 characters of arguments)"),
    "session_close.message_min_words": ("validation", 4,
        "#2173 SC3: a researcher message shorter than this many words is never matched by text "
        "(it would be found inside almost any comment); it always needs its disposition"),
    "session_close.open_items_exclude": ("validation",
        ["iba/app/reports/*", "outputs/escalation/*", "outputs/narrative-register/*",
         "research/discovery/*"],
        "#2173 SC4(a): generated report folders whose headings are not authored Open items "
        "sections (the close report itself has one named 'Open items in the register')"),
    "session_close.held_words": ("validation",
        ["hold", "held", "later", "park", "parked", "defer", "postpone", "come back", "revisit",
         "check", "clarify", "follow-up", "follow up", "not done here"],
        "#2173 SC4(b): a researcher message with one of these words holds, defers or asks to "
        "check something; it needs its register item named (or 'not held: reason')"),
    "session_close.reading_scope": ("validation",
        ["_analytics/Clusters/*", "_analytics/cross-cluster-web/*"],
        "#2173 SC5(d): where reading files live (fnmatch; * crosses folders)"),
    "session_close.reading_file_pattern": ("validation", "(reading|account|ledger|weave)",
        "#2173 SC5(d): a changed file in reading_scope whose name matches this is a reading file "
        "and needs a placement per verse it names"),
    "session_close.placement_kinds": ("validation",
        ["told", "claim", "data", "forward", "held", "parked", "context"],
        "#2173 SC5(d), Q2: the first word of a verse's placement in a reading file; forward/held "
        "name an open OT-nn.n or #nnnn; told is checked against the narrative"),
    "session_close.log_sections": ("validation",
        ["1. Scope", "2. Escalations", "3. Files", "4. Decisions", "5. Open items", "6. Git"],
        "#2173 SC8/SC9: the six section headings of a session log, in the order of "
        "governance.session_log_required_content; section 4 lines name their targets (SC9); "
        "section 6 is written after the first commit (SC13)"),
    "session_close.build_scope": ("validation",
        ["iba/app/*.py", "iba/app/*.ps1", "iba/config/*", ".claude/hooks/*", ".claude/commands/*"],
        "#2173 SC10 (C3): code and config files that must be named in what BUILD.md gained"),
    "session_close.build_scope_exclude": ("validation",
        ["iba/app/reports/*", "*/__pycache__/*", "*.pyc"],
        "#2173 SC10: excluded from build_scope"),
    "session_close.state_path": ("validation", "iba/app/reports/session-close-state.json",
        "#2173 SC5(c): the register-check findings at the previous session's last close (the "
        "baseline that tells a new finding from a standing one)"),
    "session_close.final_commit_marker": ("validation", "session log git confirmation",
        "#2173 S6/SC13: the message text of a session-close's final (second) commit; at start, a "
        "newest commit without it means the last session did not complete its close"),
}

# ── governance settings restated (G2, G4, retired-name fix) ──────────────────────────────────
GOV = {
    "governance.session_log_triggers_commit": (
        "A /session-close cycle (.claude/commands/session-close.md) includes writing the "
        "session's log (governance.session_log_required_content) and ends in the full "
        "commit-and-push cycle in the same unit of work: the log is written, Session-Close.ps1 "
        "shows no open finding, everything outstanding is staged and committed with a proper "
        "message and pushed, then the log's git section (item 6) is written and committed alone "
        "('session log git confirmation') and pushed; confirm clean/pushed from the actual git "
        "output. Restated 2026-10-20 (#2173 G2): the earlier wording ('completing a session log "
        "OR completing a /session-close cycle') let October's closes commit with no log at all. "
        "Widened 2026-09-24 (#1875): \"ensure that the session-close will activate the commit "
        "rules also.\" Second commit: researcher 2026-10-20, \"use a second commit for the "
        "session log hash\". See CLAUDE.md section 12."),
    "governance.session_log_required_content": (
        "Every session has a session log in governance.session_log_dir (SESSION-LOG-<date>-"
        "<topic>.md) naming the session id and carrying six sections, headed as in "
        "session_close.log_sections: (1) date and a one-line scope summary of the session; (2) "
        "every escalation touched, by id, with its outcome (raised/updated/resolved/rejected) -- "
        "the actual ids, not narrative paraphrase; (3) every file or deliverable created or "
        "changed, with its path; (4) decisions made, distinguishing the researcher's own "
        "decisions from self_correctable fixes Claude made and closed, each naming where it was "
        "recorded (a file path, a cfg_* table, or #nnnn vN) -- checked by session-close SC9; (5) "
        "open items carried into the next session -- what is left, and for whom, by OT-nn.n or "
        "#nnnn; (6) the git state of the session's commit (governance.session_log_triggers_"
        "commit): branch, commit hash and the push output, from the actual git output, written "
        "after the first commit and committed alone. A log missing any of these is incomplete; "
        "session-close (SC8) fails without it. Restated 2026-10-20 (#2173 G4, Q3): it no longer "
        "repeats the folder; no log was written from 2026-09-30 to 2026-10-19 although this rule "
        "was printed at every start."),
    "governance.verse_gap_by_design": (
        "Researcher ruling 2026-07-29: a verse missing from iba.db's verse table (no `verse` row "
        "for that osisId) is BY DESIGN, not a data-integrity error. Verse-existence is gated on "
        "prior term discovery (concordance-driven per-Strong's onboarding, "
        "iba/app/handlers/raw.py:verses) -- do not escalate, flag, or attempt to backfill a "
        "missing verse as a bug. Full extent measured 2026-07-29: 2,049/31,086 verses (6.59%) "
        "missing, concentrated in genealogy/list-heavy books (1Chr 44%, Ezra 40%, Neh 31%, Josh "
        "23%, Num 17%); sample read of the missing verses' actual content judged the risk within "
        "tolerance for this study (see iba/app/reports/verse-existence-census-20260729.md). The "
        "base-extract and passage-debate reports (both since retired) noted each detectable gap "
        "inline (report.verse_gap_note) and skipped to the next available verse; the spine check "
        "never looks for a missing verse (#2173 P3). Restated 2026-10-20 (#2173): it named the "
        "two retired report steps as if live."),
}

GOV["governance.no_direct_github_publish"] = (
    "Bible_study_projects never publishes to GitHub itself (no Actions workflow, no push to a site "
    "repo). Narrative files reach learning4comfort only by Copy-NarrativeToLearning4Comfort.ps1, "
    "run on completion of a section of work, on request, and at /session-close when a chapter "
    "changed in the session (SC12). Restated 2026-10-20 (#2173 P0/SC12): it had run at every "
    "close, reporting every file 'unchanged'.")

# ── cfg_behaviour_rule: new rules (by rule_key) ───────────────────────────────────────────────
NEW_RULES = [
    ("documentation", "reading-file-placement-per-verse",
     "Every reading, account, ledger or weave file of a strand carries one placement for every "
     "verse it names: in a `## Placements` table (| verse | placement |) for a .md file, or a "
     "`placement` column beside `reference` for a .csv. The placement's first word is one of "
     "session_close.placement_kinds: told (a current chapter tells it), claim (a register claim "
     "source), data, forward OT-nn.n, held #nnnn, parked, or context (named only as the setting of "
     "another verse). A verse named with no placement, or placed 'told' when no chapter tells it, "
     "is a finding at session-close.",
     "Researcher, chat 2026-10-20 (#2173 Q2), verbatim, on a placement per verse in reading files: "
     "\"yes. not sure how else you would control it.\" It answers #2172: readings did not reliably "
     "reach the narrative and no control enforced completeness.",
     "session-close SC5(d) (handlers/session_close.py _sc5d) on every reading file changed in the "
     "session; settings session_close.reading_scope / reading_file_pattern / placement_kinds.",
     "mechanically_enforced"),
    ("documentation", "open-items-lines-carry-a-handle",
     "Every line of an `Open items` section in a project file names the register item that carries "
     "it: an OT-nn.n or OT-nn thread item, or an escalation #nnnn, that exists and is still open. A "
     "line with no handle, or a handle that is closed or does not exist, is a finding at "
     "session-close: raise the item (rule 21) or close the line.",
     "Researcher, chat 2026-10-20 (#2173), verbatim: \"confirm that each observation in the "
     "session was recorded in the claims tables and that each open/referred/to be clarified item "
     "is recorded in the open item register.\"",
     "session-close SC4(a) (handlers/session_close.py _sc4a) on every .md file changed in the "
     "session.",
     "mechanically_enforced"),
    ("chat", "session-compliance-restated-and-proved",
     "At every session start Claude writes the session compliance file (Compliance.ps1 -Action "
     "Template, compliance.dir): for every active governance setting, behaviour rule and "
     "escalation rule, what it requires in this session in Claude's own words, or 'not engaged' "
     "with the reason; the acknowledgement (compliance.acknowledgement); and, by id, every rule in "
     "conflict or not followed. start-project does not end until Compliance.ps1 -Action Check "
     "-Phase Start passes. During the session each engaged rule gains its evidence (a file, "
     "#nnnn vN, a commit, a command output); session-close (SC6) fails on an engaged rule with no "
     "evidence or with evidence that does not check.",
     "Researcher, chat 2026-10-20 (#2173 P2), verbatim: \"You print the config report, but you "
     "ignore the content. What step can I take as part of the behaviour section to ensure that you "
     "read and understood the governance and config rules and acknowledge that you will comply "
     "with it.\"; then \"incomplete\".",
     "Compliance.ps1 -Action Check -Phase Start (lib/compliance.check_start: a row per rule, none "
     "blank, none copied, the acknowledgement, retired-name rules named); Session-Close.ps1 SC6 "
     "(compliance.check_close). Not mechanical: whether a restatement is right -- the "
     "researcher's spot check.",
     "partially_enforced"),
    ("chat", "session-close-blocks-commit-on-open-findings",
     "Session-close commits nothing while Session-Close.ps1 shows an open finding (it exits 3). "
     "Each finding is fixed, or dispositioned in the compliance file's `## Close dispositions` "
     "with the open item that carries it (carried OT-nn.n / #nnnn), or -- only where the finding "
     "accepts it -- 'recorded in #n vN' / 'no record needed: reason' (a researcher message), "
     "'not held: reason' (a holding word), 'not scripture: reason' (a quotation). The check "
     "verifies every disposition; an unchecked one leaves the finding open.",
     "Researcher, chat 2026-10-20 (#2173 SC13 as designed): \"proceed with the session-close "
     "design\"; the commit is blocked while any finding is neither fixed nor carried by a named "
     "item.",
     "Session-Close.ps1 exit 3 while counts.open_findings > 0 (handlers/session_close.py "
     "_apply_dispositions verifies each disposition). Not mechanical: that the commit is not made "
     "despite the exit code -- the command text forbids it.",
     "partially_enforced"),
]

# behaviour rules restated / retired: id -> dict of changes
RULE_CHANGES = {
    43: dict(rule_text_replace=("a real `run` row, a `run_id`, `cfg_step` registration, and "
                                "`module_blocking` protection;",
                                "a real `run` row, a `run_id` and `cfg_step` registration (and "
                                "module_blocking protection once that gate is redesigned and "
                                "re-enabled: it is disabled since #859);")),
    47: dict(active=0, rule_text_prefix=(
        "RETIRED 2026-10-20 (#2173 audit): the table this rule keeps alive, "
        "wa_session_research_flags, was set inactive on 2026-09-24 by the researcher's "
        "bible_research.db prose-only ruling (GOVERNANCE.md section 81, which records that it "
        "overrode #833's deferral). The rule could no longer be followed. ORIGINAL TEXT: ")),
    54: dict(active=0, rule_text_prefix=(
        "RETIRED 2026-10-20 (#2173 audit): the table this rule writes to, wa_data_quality_flags, "
        "was set inactive on 2026-09-24 (GOVERNANCE.md section 81), so no flag can be raised in "
        "it; the prose-quality mechanism awaits its own rebuild if prose work resumes. ORIGINAL "
        "TEXT: ")),
    62: dict(rule_text_replace=("finding_verse_index (bible_research.db, 475,790 rows)",
                                "a bible_research.db index table (475,790 rows, since retired)")),
    74: dict(rule_text_replace=("is generated (Escalation.ps1 -Action Export -Type thread) and "
                                "regenerated at session-close.",
                                "is generated (Escalation.ps1 -Action Export -Type thread) and "
                                "regenerated at session-close when a thread row changed in the "
                                "session (SC12, #2173). Its quality, validity and integrity are "
                                "audited at every start (Escalation.ps1 -Action ThreadAudit, "
                                "#2173 P5).")),
}

# ── cfg_method_rule (G6, G7, G8) ─────────────────────────────────────────────────────────────
METHOD_NEW = ("spine.check", "spine-meaning-complete-against-step",
    "Every live strong has its meaning in the three core meaning tables, which are the extracts "
    "from STEP: strong_sense (head), strong_meaning_tree (the range, by the exact code) and "
    "strong_lexicon (lsj and mounce, for the languages in spine.meaning_lexicon_languages). "
    "Complete means: matches what STEP holds for that Strong's, not what a table or a "
    "classification would lead one to expect. A local gap (no live row, or empty text) is asked "
    "of STEP for that code: STEP holding content the table lacks is a FATAL spine finding, fixed "
    "on discovery by pulling it into the table; STEP holding nothing is the only gap by design, "
    "and is listed as such. The parse tables stay retired and are not read. Researcher, "
    "2026-10-20 (#2173 Q1), verbatim: \"you need to check that each strong have its meaning, the "
    "three tables are the extracts from STEP, so it is not about which table, it depend on what "
    "the STRONG has in step. parsed table stay retired. the check is done directly to the three "
    "core meaning tables.\"",
    "outputs/markdown/session-routines-start-project-change-proposal-v1-20261020.md (P3, Q1)",
    "handlers/spine.py compute() (strong -> meaning), run by Spine-Check.ps1 and session-close SC2")
METHOD_CHANGES = {
    66: dict(active=0, prefix=(
        "SUPERSEDED 2026-10-20 by spine-meaning-complete-against-step (#2173 G6, Q1): a missing "
        "meaning row is no longer accepted on the strong's classification; completeness is what "
        "STEP holds for the Strong's. ORIGINAL TEXT: ")),
    67: dict(text=(
        "Once the spine is sound, verse -> span -> strong -> the three core meaning tables "
        "(strong_sense, strong_meaning_tree, strong_lexicon) is the whole route for knowing a "
        "term's meaning in context during analysis; the parse tables are retired and not part of "
        "the route. Discovery of a missing meaning entry for a term significant to the analysis "
        "must TRIGGER the update of its meaning (pull it from STEP into those tables) at the point "
        "of discovery -- not merely logged for a later sweep, and not a proactive full-Bible pull "
        "-- researcher ruling 2026-09-10 (#1624: 'on discovery of a missing meaning entry - the "
        "update of meaning must be triggered'). The spine check now finds every such gap against "
        "STEP (spine-meaning-complete-against-step); raw.backfill_meaning pulls by book/passage; a "
        "per-term, analysis-triggered pull is a deferred build. Restated 2026-10-20 (#2173 G7): "
        "the earlier text routed meaning through the retired parse tables.")),
    68: dict(text=(
        "verse, span, strong and cluster are the study's spine and must stay in sync: every live "
        "span belongs to a live verse and every live verse has live spans (a verse with no verse "
        "row at all is a gap by design, governance.verse_gap_by_design); every Strong's code a "
        "live span names (span.strong_variant) resolves to a live strong row; every such strong "
        "resolves through cluster_strong to a live cluster (governance.base_data_spine, extended "
        "2026-09-21). A discovered desync is a FATAL ERROR, fixed on discovery, not merely logged "
        "or deferred -- researcher ruling 2026-09-10. handlers/spine.py checks all four; restated "
        "2026-10-20 (#2173 G8): the check had covered span -> strong only. History: 409 "
        "span-referenced codes had no strong row on 2026-09-09 (#1613); 0 on 2026-10-20.")),
}

# ── cfg_escalation (G9, G10, #2174) ──────────────────────────────────────────────────────────
ESC_CHANGES = {
    3: dict(rule_text=(
        "Running a module registered in cfg_utility (or a step registered in cfg_step) is to be "
        "blocked while it has an unresolved escalation against it (state is one of the open "
        "group, cfg_enum escalation_state_open, in practice raised or re-assigned). THE GATE IS "
        "DISABLED (escalation #859, 2026-08-26, researcher): the accumulated backlog made routing "
        "around it the normal response; it is commented out in run.py pending a redesign. "
        "Restated 2026-10-20 (#2173 G9): it named the inactive state 're-assign' and read as "
        "live."),
            enforced_by=(
        "Not enforced: run.py:run_step()'s third dispatch gate (#646) is commented out since "
        "2026-08-26 (#859) and must not be re-enabled without that redesign.")),
    6: dict(active=0, rule_text_prefix=(
        "RETIRED 2026-10-20 (#2174, decided inside #2173 by the researcher's instruction that "
        "#2174 is part of the #2173 work). It could not be followed: the related_activity column "
        "it relies on was removed from the escalation tables on 2026-08-27 (#909), and the "
        "function that applied it was removed on 2026-08-20. Its purpose -- finding the planning "
        "document of a package of escalations -- is now met by Escalation.ps1 -Action Context "
        "(#2173 P1), which finds every file named in any field of any version. ORIGINAL TEXT: ")),
    12: dict(rule_text=(
        "When an issue is set to next_action=approved (the terminal value an issue reaches via the "
        "reused manual vocabulary, per D11/D21 -- this rule originally referenced the now-withdrawn "
        "next_action=decided) and its resolution states a new or changed project/governance rule, "
        "or when a task changes user-facing app behaviour, the party closing it out raises a "
        "companion task naming the owning document it updates (full path, in its context) -- "
        "GOVERNANCE.md for a rule change, USER-GUIDE.md for user-facing behaviour -- in the same "
        "turn, not left to be remembered separately. A code change's BUILD.md entry remains "
        "governed independently (governance.build_md_on_code_change); this rule covers the "
        "documentation obligations that rule does not. Restated 2026-10-20 (#2173): it named "
        "from_id and related_activity, removed on 2026-08-27 (#909).")),
    17: dict(rule_text=(
        "T2 (escalation #2000; researcher, round 1: 'default to raised, but allow for asigning the "
        "status on create to on-hold or in progress'). A manual Raise defaults to 'raised' and may "
        "choose a state from cfg_enum escalation_raise_state. A thread is raised at on-hold unless "
        "a state is given, and never at 'raised'. Code-raised items (escalation.raise_) always land "
        "at 'raised'. Restated 2026-10-20 (#2173): the closing clause 'so module_blocking (rule 3) "
        "still fires on them' was untrue while that gate is disabled (#859).")),
    7: dict(rule_text=(
        "Any specific file mentioned in an escalation's text (short_description, comment, tried, "
        "resolution, context) must be given as its full repo-relative path (e.g. iba/app/run.py), "
        "never a bare filename (e.g. run.py) -- a bare filename doesn't help the researcher "
        "locate it, and in a large repo may not even be unique. Verified 2026-08-16: 'run.py' "
        "resolves to 5 different files in this repo. Restated 2026-10-20 (#2173 G10): "
        "related_activity no longer exists (#909); comment added."),
            enforced_by=(
        "Escalation.ps1 -Action Context (lib/escalationcontext.py, #2173 P1) reports every bare "
        "filename in an open escalation as a finding at each session start; writing the full "
        "path is the discipline of whoever writes the row.")),
}

# ── steps, reports, on_fail, utilities ───────────────────────────────────────────────────────
WORK_PACKAGES = [dict(name="session-compliance", ps_script="iba/app/ps/Compliance.ps1",
                      runs_over="none", chained=0, inactive=0)]
STEPS = [
    ("escalation-reporting", 4, "escalation.context", "iba.app.handlers.reports:escalation_context",
     "#2173 P1: every file each open escalation (raised, in-progress, re-assigned) names in any "
     "field of any version, resolved to its latest live version; findings missing / bare -- see "
     "lib/escalationcontext.py", "utility"),
    ("escalation-reporting", 5, "escalation.thread_audit",
     "iba.app.handlers.reports:escalation_thread_audit",
     "#2173 P5: thread quality, validity and integrity, T-a to T-g, each finding by thread item -- "
     "see lib/threadaudit.py", "utility"),
    ("session-compliance", 0, "compliance.template", "iba.app.handlers.compliance:template",
     "#2173 P2: writes this session's compliance file, one row per active governance setting, "
     "behaviour rule and escalation rule (never overwrites)", "utility"),
    ("session-compliance", 1, "compliance.check_start", "iba.app.handlers.compliance:check_start",
     "#2173 P2 B/C: every rule restated or 'not engaged' with a reason, none copied, the "
     "acknowledgement, every rule naming a retired thing named in the conflicts section", "utility"),
    ("narrative-register", 14, "narrative_register.quote_check",
     "iba.app.handlers.narrativeregister:quote_check",
     "#2173 G14: every quotation in -File (or in the lines it added against -Against) must be in "
     "the ESV text -- see lib/quotecheck.py", "utility"),
]
STEP_DOES = {
    ("escalation-reporting", "escalation.list"):
        "every escalation not yet closed (open: raised/in-progress/re-assigned; parked: on-hold -- "
        "cfg_enum escalation_state_open/_parked, #2173 G1), each with its full history inline, "
        "then the in-progress threads and the last 15 resolved -- see "
        "lib/escalation.py:write_list_report. On demand only (not run at start, #2173 P0).",
    ("spine-check", "spine.check"):
        "read-only check of the base-data spine (governance.base_data_spine): span -> strong, "
        "verse <-> span, strong -> cluster, and strong -> meaning (strong_sense, "
        "strong_meaning_tree, strong_lexicon; each local gap asked of STEP: content in STEP that "
        "the table lacks is FATAL, nothing in STEP is a gap by design). Persists a report every "
        "run; escalates only on a FATAL finding. Run by session-close (SC2), not at start "
        "(#2173 P3). The parse tables stay retired. See handlers/spine.py.",
    ("session-close", "session.close"):
        "read-only session-close detection (#1875, rebuilt #2173 SC1-SC14): session and window "
        "(fails without them); spine FATAL first; researcher's words recorded in escalation "
        "comments; open items in the register; analysis integrity (chapter changes recorded, "
        "quotes checked, register findings new or standing on touched chapters, reading "
        "placements); rule compliance evidence; session log and its decisions' targets; BUILD.md "
        "naming every changed code/config file; publish flags. Findings are cleared only by a fix "
        "or a checked disposition; Session-Close.ps1 exits 3 (commit blocked) while any is open.",
}
REPORTS = [
    dict(step="escalation.context", title="What the open escalations point to", show_toc=1,
         footer_text=None, output_kind="md", naming_scheme="dated", archive_dir="archive", inactive=0),
    dict(step="escalation.thread_audit", title="Thread audit", show_toc=1, footer_text=None,
         output_kind="md", naming_scheme="dated", archive_dir="archive", inactive=0),
    dict(step="narrative_register.quote_check", title="Quote check", show_toc=0, footer_text=None,
         output_kind="md", naming_scheme="dated", archive_dir="archive", inactive=0),
]
REPORT_TITLE = {"session.close": "Session close (#1875, rebuilt #2173)"}
SECTIONS = [  # step, ordinal, key, heading, toc
    ("escalation.context", 0, "items", "## Open escalations and their files", "Escalations"),
    ("escalation.thread_audit", 0, "findings", "## Findings by check", "Findings"),
    ("spine.check", 3, "meaning_by_design", "## Meaning gaps by design (STEP holds nothing)",
     "Meaning gaps by design"),
    ("session.close", 1, "sc1", "## SC1 Session and window", "SC1"),
    ("session.close", 2, "sc2", "## SC2 Spine (FATAL)", "SC2"),
    ("session.close", 3, "sc3", "## SC3 Researcher's words recorded", "SC3"),
    ("session.close", 4, "sc4", "## SC4 Open items in the register", "SC4"),
    ("session.close", 5, "sc5", "## SC5 Analysis integrity", "SC5"),
    ("session.close", 6, "sc6", "## SC6 Rule compliance", "SC6"),
    ("session.close", 7, "sc8", "## SC8 Session log", "SC8"),
    ("session.close", 8, "sc9", "## SC9 Decisions reached their targets", "SC9"),
    ("session.close", 9, "sc10", "## SC10 BUILD.md coverage", "SC10"),
    ("session.close", 10, "sc12", "## SC12 Publish", "SC12"),
]
SECTIONS_RETIRE = [("session.close", "escalation_gaps"), ("session.close", "governance_gaps"),
                   ("session.close", "build_gaps")]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
ON_FAIL = [
    ("compliance.template", "no-session", "report-continue",
     "the session could not be identified -- see the message"),
    ("compliance.check_start", "no-session", "report-continue",
     "the session could not be identified -- see the message"),
    ("compliance.check_start", "findings-open", "report-continue",
     "the compliance file does not pass the start check -- fix it and re-run (Compliance.ps1 exits 3)"),
    ("session.close", "findings-open", "report-continue",
     "session-close found open findings -- the commit is blocked until each is fixed or carried "
     "(Session-Close.ps1 exits 3); remediation is Claude's, not an approval cycle"),
    ("narrative_register.quote_check", "quotes-failing", "report-continue",
     "quotations not found in the ESV text -- correct them, or disposition each at session-close"),
    ("narrative_register.quote_check", "refused", "report-continue", REFUSED),
]
ON_FAIL_RETIRE = [("session.close", "gaps-found")]
UTILITIES = [
    ("escalationcontext", "iba/app/lib/escalationcontext.py",
     "escalationcontext.py -- what every open escalation points to (#2173 P1): every file named in "
     "any field of any version, resolved to its latest live version; findings missing / bare."),
    ("threadaudit", "iba/app/lib/threadaudit.py",
     "threadaudit.py -- thread quality, validity and integrity (#2173 P5), T-a to T-g by item."),
    ("compliance", "iba/app/lib/compliance.py",
     "compliance.py -- rule compliance read at start and proved at close (#2173 P2): delivery of "
     "the rules, the session compliance file, its start and close checks."),
    ("handlers_compliance", "iba/app/handlers/compliance.py",
     "handlers/compliance.py -- the compliance.template and compliance.check_start steps (#2173 P2).",
     "thin step wrappers: every setting is read in lib/compliance.py, which they call"),
    ("sessionwindow", "iba/app/lib/sessionwindow.py",
     "sessionwindow.py -- the running session, its start, git window and transcript; the "
     "last-session check at start (#2173 S6). Shared by start-up and session-close."),
    ("quotecheck", "iba/app/lib/quotecheck.py",
     "quotecheck.py -- the narrative quote check moved into the app (#2173 G14).",
     "pure functions over a connection: the callers read narrative.quote_min_words and pass it"),
    ("session_routines_2173_v1_20261020", THIS,
     "Developer Mode config migration for #2173/#2174 (this file).",
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
     "as the other Developer Mode migrations"),
]
UTILITY_PURPOSE = {
    "spine": "spine.py -- the base-data spine check (#1613; extended #2173 P3): span -> strong, "
             "verse <-> span, strong -> cluster, strong -> meaning against STEP. compute() is "
             "shared with session-close SC2. Read-only, always persists a report.",
    "session_close": "session_close.py -- session-close detection (#1875; rebuilt #2173 "
                     "SC1-SC14): findings with stable keys, cleared only by a fix or a checked "
                     "disposition; Session-Close.ps1 exits 3 while any is open. Remediation is "
                     "Claude's via .claude/commands/session-close.md.",
}


# ── apply ────────────────────────────────────────────────────────────────────────────────────
def _put(conn, report, table, key, row, label):
    where = " AND ".join(f'"{k}"=?' for k in key)
    cur = conn.execute(f'SELECT * FROM "{table}" WHERE {where}', list(key.values()))
    found = cur.fetchone()
    if found is None:
        apply_logged(conn, RUN_ID, table, "insert", {}, {**key, **row})
        report.append(f"  {table} {label}: inserted")
        return
    have = dict(zip([d[0] for d in cur.description], found))
    diff = {k: v for k, v in row.items() if have.get(k) != v}
    if diff:
        apply_logged(conn, RUN_ID, table, "update", key, diff)
        report.append(f"  {table} {label}: updated {sorted(diff)}")
    else:
        report.append(f"  {table} {label}: present -- skipped")


def run(cfg: Cfg) -> list[str]:
    conn = cfg.conn
    R: list[str] = []
    for name, values in ENUMS.items():
        for i, v in enumerate(values):
            _put(conn, R, "cfg_enum", {"name": name, "value": v}, {"ordinal": i, "inactive": 0},
                 f"{name} {v!r}")
    for key, (module, value, use) in SETTINGS.items():
        _put(conn, R, "cfg_setting", {"key": key}, {"value": J(value), "use": use, "module": module,
                                                    "inactive": 0}, key)
    for key, text in GOV.items():
        _put(conn, R, "cfg_setting", {"key": key}, {"value": J(text)}, key)
    # behaviour rules
    for cls, key, text, source, enforced, status in NEW_RULES:
        row = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (key,)).fetchone()
        fields = {"class": cls, "rule_text": text, "source": source, "enforced_by": enforced,
                  "active": 1, "enforcement_status": status}
        if row is None:
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {},
                         {"rule_key": key, "added_at": NOW, **fields})
            R.append(f"  cfg_behaviour_rule {key}: inserted")
        else:
            _put(conn, R, "cfg_behaviour_rule", {"id": row[0]}, fields, key)
    for rid, ch in RULE_CHANGES.items():
        cur = conn.execute("SELECT rule_text, active FROM cfg_behaviour_rule WHERE id=?", (rid,)).fetchone()
        text, active = cur[0], cur[1]
        new = {}
        if "rule_text_prefix" in ch and not text.startswith(ch["rule_text_prefix"][:20]):
            new["rule_text"] = ch["rule_text_prefix"] + text
        if "rule_text_replace" in ch and ch["rule_text_replace"][0] in text:
            new["rule_text"] = text.replace(*ch["rule_text_replace"])
        if "active" in ch and active != ch["active"]:
            new["active"] = ch["active"]
        _put(conn, R, "cfg_behaviour_rule", {"id": rid}, new, f"id {rid}") if new else \
            R.append(f"  cfg_behaviour_rule id {rid}: present -- skipped")
    # method rules
    step, key, text, src, enforced = METHOD_NEW
    row = conn.execute("SELECT id FROM cfg_method_rule WHERE rule_key=?", (key,)).fetchone()
    if row is None:
        nid = conn.execute("SELECT COALESCE(MAX(id),0)+1 FROM cfg_method_rule").fetchone()[0]
        ordn = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_method_rule WHERE step=?",
                            (step,)).fetchone()[0]
        apply_logged(conn, RUN_ID, "cfg_method_rule", "insert", {},
                     {"id": nid, "step": step, "rule_key": key, "rule_text": text, "source_doc": src,
                      "enforced_by": enforced, "ordinal": ordn, "active": 1})
        R.append(f"  cfg_method_rule {key}: inserted (id {nid})")
    else:
        _put(conn, R, "cfg_method_rule", {"id": row[0]},
             {"rule_text": text, "source_doc": src, "enforced_by": enforced, "active": 1}, key)
    for mid, ch in METHOD_CHANGES.items():
        text, active = conn.execute("SELECT rule_text, active FROM cfg_method_rule WHERE id=?",
                                    (mid,)).fetchone()
        new = {}
        if "prefix" in ch and not text.startswith(ch["prefix"][:20]):
            new["rule_text"] = ch["prefix"] + text
        if "text" in ch and text != ch["text"]:
            new["rule_text"] = ch["text"]
        if "active" in ch and active != ch["active"]:
            new["active"] = ch["active"]
        if mid == 68:
            new["enforced_by"] = "handlers/spine.py compute(): all four checks (#2173 P3)"
        _put(conn, R, "cfg_method_rule", {"id": mid}, new, f"id {mid}")
    # escalation rules
    for eid, ch in ESC_CHANGES.items():
        text, active = conn.execute("SELECT rule_text, active FROM cfg_escalation WHERE id=?",
                                    (eid,)).fetchone()
        new = {k: v for k, v in ch.items() if k in ("rule_text", "enforced_by")}
        if "rule_text_prefix" in ch and not text.startswith(ch["rule_text_prefix"][:20]):
            new["rule_text"] = ch["rule_text_prefix"] + text
        if "active" in ch:
            new["active"] = ch["active"]
        _put(conn, R, "cfg_escalation", {"id": eid}, new, f"id {eid}")
    # steps etc.
    for wp in WORK_PACKAGES:
        _put(conn, R, "cfg_work_package", {"name": wp["name"]},
             {k: v for k, v in wp.items() if k != "name"}, wp["name"])
    for wp, ordn, step, handler, does, kind in STEPS:
        _put(conn, R, "cfg_step", {"work_package": wp, "step": step},
             {"ordinal": ordn, "handler": handler, "scope": "none", "does": does, "inactive": 0,
              "kind": kind}, step)
    for (wp, step), does in STEP_DOES.items():
        _put(conn, R, "cfg_step", {"work_package": wp, "step": step}, {"does": does}, step)
    for rep in REPORTS:
        _put(conn, R, "cfg_report", {"step": rep["step"]},
             {k: v for k, v in rep.items() if k != "step"}, rep["step"])
    for step, title in REPORT_TITLE.items():
        _put(conn, R, "cfg_report", {"step": step}, {"title": title}, step)
    for step, ordn, key, heading, toc in SECTIONS:
        _put(conn, R, "cfg_report_section", {"step": step, "section_key": key},
             {"ordinal": ordn, "heading": heading, "toc_label": toc, "include": 1, "inactive": 0},
             f"{step}/{key}")
    for step, key in SECTIONS_RETIRE:
        _put(conn, R, "cfg_report_section", {"step": step, "section_key": key}, {"inactive": 1},
             f"{step}/{key} retired")
    for step, cond, path, msg in ON_FAIL:
        _put(conn, R, "cfg_on_fail", {"step": step, "condition": cond},
             {"path": path, "resolver": None, "message": msg, "route": "terminal", "inactive": 0},
             f"{step}/{cond}")
    for step, cond in ON_FAIL_RETIRE:
        _put(conn, R, "cfg_on_fail", {"step": step, "condition": cond}, {"inactive": 1},
             f"{step}/{cond} retired")
    for module, path, purpose, *exempt in UTILITIES:
        _put(conn, R, "cfg_utility", {"module": module},
             {"file_path": path, "purpose": purpose, "inactive": 0,
              "config_exempt": 1 if exempt else 0,
              "config_exempt_reason": exempt[0] if exempt else None}, module)
    for module, purpose in UTILITY_PURPOSE.items():
        _put(conn, R, "cfg_utility", {"module": module}, {"purpose": purpose}, module)
    return R


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=pathlib.Path, default=DB_PATH)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(a.db)
    conn = cfg.conn
    try:
        conn.execute("BEGIN")
        R = run(cfg)
        if a.dry_run:
            conn.rollback()
            R.append("DRY RUN -- rolled back")
        else:
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cfg.close()
    print("\n".join(R))
    print(f"{sum(1 for r in R if ': inserted' in r)} inserted, "
          f"{sum(1 for r in R if ': updated' in r)} updated, "
          f"{sum(1 for r in R if 'skipped' in r)} unchanged ({a.db})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
