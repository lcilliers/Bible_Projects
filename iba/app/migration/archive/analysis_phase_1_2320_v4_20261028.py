"""analysis_phase_1_2320_v4_20261028.py -- escalation #2320: the rules the code enforced are config rows.

Researcher, chat 2026-10-28 (verbatim): "can I confirm that rules are configs, not hard recorded in the code."; then "I am more worried, that
you are building code that does not comply with governance. I am really disappointed in you. and YES fix your lack of compliance, no need to
ask me if you need to comply - the answer will always be yes. that is what governance is all about."

governance.rules_must_be_config_driven: no operational or process rule may exist only in code. The rules the Analysis_phase_1 build wrote
into the code (#2320 to #2328) are moved into cfg_setting rows, which the code now reads:
- reading.observation_rules (module reading): the stage a row is written under, the parts never absent, the kinds not used, the kinds
  that carry a route, the kinds that must record the primary operation, a chain and a party, the bears-on refusal, the merge rule;
- lexical.span_surface (module lexical): the look-back, the single-word gloss rule and the gloss separators of the surface of a code in a
  multi-code span (the particle pattern is the existing discovery.particle_pattern, read, not copied);
- report.cluster_folder_name_rule (module report): the machine form of the naming sentence of report.cluster_folder_naming_convention,
  whose own sentence becomes a pointer to it (one home for the rule);
- cfg_method_rule RS-08 restated to name the setting; the use text of reading.output_dir restated.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2320_v4_20261028.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2320-RULES-IN-CONFIG-20261028"
MODULE = "analysis_phase_1_2320_v4_20261028"
SRC = "#2320 (researcher, chat 2026-10-28)"

OBSERVATION_RULES = {
    "stage": "Analysis_phase_1",
    "parts_never_absent": ["sense", "evidence", "circumstance"],
    "unused_kinds": ["silence"],
    "route_required_kinds": ["party"],
    "route_allowed_kinds": ["party", "link"],
    "primary_operation": {"kind": "statement", "part": "primary_operation"},
    "chain": {"kind": "link", "part": "chain"},
    "party": {"kind": "party", "part": "party", "route_required": True},
    "bears_on_only_refused": True,
    "merge_same_text_only": True,
}
OBSERVATION_RULES_USE = (
    "the rules for stating an observation that Record enforces (#2320, spec 4.1 and 4.2; run via reading.record): stage = the value written "
    "as ib_observation.stage and ib_node.source_stage of what Analysis_phase_1 writes (a record of origin, never a filter); "
    "parts_never_absent = the parts of reading.observation_parts that are never stated absent; unused_kinds = kinds of "
    "reading.observation_parts that are not accepted on a kept observation (proposed for deletion); route_required_kinds and "
    "route_allowed_kinds = the kinds that must, or may, carry a route (cfg_enum observation_route); primary_operation, chain and party = "
    "the kind of observation that must record the part when a covered observation holds it, and for the party whether its route is "
    "required; bears_on_only_refused = an observation whose nodes all bear on an act (reading.node_roles bears_on) is refused, its nodes "
    "belong to the observation of the act; merge_same_text_only = a merge is for the same description only")
SPAN_SURFACE = {
    "look_back_words": 5,
    "single_word_gloss_only": True,
    "gloss_alternative_separators": "/:;,",
    "gloss_leading_words": ["to"],
}
SPAN_SURFACE_USE = (
    "the surface of a code in a multi-code span (#2326): STEP tags one span with all its codes and leaves some English untagged, so a code "
    "whose STEP gloss (strong.stepGloss) is not the span's word takes the untagged English word just before the span that is exactly "
    "its gloss. look_back_words = how many untagged words before the span are looked at; single_word_gloss_only = only a whole one-word "
    "alternative of the gloss counts ('be' is not 'to be ashamed'); gloss_alternative_separators = the characters that separate the "
    "alternatives of a gloss; gloss_leading_words = a leading word dropped from an alternative ('to ask'). A particle is "
    "discovery.particle_pattern. Read by iba/app/lib/lexical.py span_code_surfaces")
FOLDER_RULE = {
    "pattern": "{cluster_code} - {slug}",
    "ampersand_to_space": True,
    "lowercase": True,
    "drop_other_punctuation": True,
    "word_separator": "-",
}
FOLDER_RULE_USE = (
    "the name of a cluster's folder under _analytics/Clusters, machine form of the naming sentence of "
    "report.cluster_folder_naming_convention (#2328): pattern with {cluster_code} and {slug}; the slug is the cluster's short_name with "
    "& turned to a space, lowercased, all other punctuation dropped, spaces as word_separator. Read by "
    "iba/app/lib/filingkit.py cluster_folder_name")
RS08 = ("The observations of a verse state what the verse shows, and Record enforces it from cfg_setting reading.observation_rules: an "
        "observation that covers a relevant surface (a node with a characteristic or qualifier role) holds every part of spec 4.2 "
        "(reading.observation_parts), each in words or stated absent with the reason (the parts_never_absent never absent). The words that "
        "bear on an act are nodes of the observation of the act, never an observation of their own (bears_on_only_refused). One observation "
        "of the primary_operation kind names the primary operation; a stated chain has an observation of the chain kind; a stated party has "
        "an observation of the party kind with its route. A verse whose observations do not comply is not recorded.")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    for key, module, value, use in (
            ("reading.observation_rules", "reading", OBSERVATION_RULES, OBSERVATION_RULES_USE),
            ("lexical.span_surface", "lexical", SPAN_SURFACE, SPAN_SURFACE_USE),
            ("report.cluster_folder_name_rule", "report", FOLDER_RULE, FOLDER_RULE_USE)):
        if not one("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    prose = json.loads(one("SELECT value FROM cfg_setting WHERE key='report.cluster_folder_naming_convention'")[0])
    old = ("Name = {cluster.cluster_code} - {cluster.short_name lowercased, & and all other punctuation dropped, spaces as single hyphens} "
           "-- e.g. ")
    if old in prose:
        ops.append(("cfg_setting", "update", {"key": "report.cluster_folder_naming_convention"},
                    {"value": json.dumps(prose.replace(old, "Name per cfg_setting report.cluster_folder_name_rule (cluster_code - the "
                                                            "short_name as a slug) -- e.g. ", 1))}))
    row = one("SELECT id FROM cfg_method_rule WHERE rule_key LIKE 'RS-08 %' AND active=1")
    if row:
        ops.append(("cfg_method_rule", "update", {"id": row[0]}, {"rule_text": RS08, "source_doc": SRC,
                                                                  "enforced_by": "iba/app/lib/reading.py _validate_sheet; "
                                                                                 "iba/app/lib/observationrecord.py complete_parts"}))
    use_old = one("SELECT use FROM cfg_setting WHERE key='reading.output_dir'")[0]
    ops.append(("cfg_setting", "update", {"key": "reading.output_dir"}, {
        "use": "where Reading.ps1 files each reading (scope JSON, account, synergy, narrate), one folder per reading: a pattern whose "
               "{cluster_folder} is the home cluster's folder by report.cluster_folder_name_rule (#2228, #2328)"}) if use_old else None)
    ops = [o for o in ops if o]
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2320: the rules the code enforced are config rows; run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    ops = plan(conn)
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
