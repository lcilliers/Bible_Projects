"""utilities_2207_v1_20261022.py -- escalation #2207 item 2 (the utilities with no config), the parts
already approved (v4 D4/D5/D11, v7, v9). Code moved in the same unit of work:

- Batch monitoring scrapped: iba/app/lib/batchprogressreport.py and iba/app/ps/BatchProgress.ps1 to
  archive/; work package batch-progress-report, step report.batch_progress, its cfg_report and
  cfg_report_section rows and setting report.batch_progress_path retired. lib/batchcontrol.py (the
  skip-already-committed guard of the live LLM steps) is not touched: it is a decision in
  outputs/escalation/2207-item2-utility-decisions-v1-20261022.md.
- lib/lexicalenrich.py to archive/, with the handlers of the retired steps lexical.enrich and
  lexical.run (iba/app/handlers/lexical.py) and the lexical.run-only parts of
  lib/lexicalenrichgenerate.py.
- lib/taggingguidance.py definitions into cfg_setting ib_observation.tag_guidance and
  ib_observation.tag_stage_excluded, values exactly as they were in the code.
- Settings read only by the removed code (ORPHANS) retired, and the enum groups note_type and
  resolution_status, which only the removed Layer 2 briefing pack looked up (their table
  verse_lexical_note is already inactive in cfg_table).

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/utilities_2207_v1_20261022.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2207-UTILITIES-20261022"
MODULE = "utilities_2207_v1_20261022"

TAG_DATA = json.loads(r'''{
 "guidance": {
  "qualifier-for-term": "the word functions as a MODIFIER (manner, intensifier, or other state/measure/intensity enhancer) of another word's action or quality, rather than naming a disposition/operation/quality in its own right -- e.g. an adverb qualifying HOW an operation is performed, or an adjective qualifying another M-code noun (\"godly\" qualifying \"grief\").",
  "no-impact": "the occurrence's surface form/stepGloss carries no distinguishing nuance beyond the term's base sense -- a real 'no divergence' finding, not an absence of an answer. Contrast `alternative-meaning` (a real divergence IS found) and `surface-gloss-divergence` (the surface FORM itself, not just the sense, diverges from the dictionary gloss).",
  "not-related-to-meaningful-word": "the sub-question's target item (a contrast, a related word-form, a co-occurring item the question asks you to identify) genuinely does not exist or apply for this term/verse -- a real negative finding, not a shrug.",
  "sole-mcode-in-verse": "no other M-code characteristic co-occurs in this verse at all -- distinct from `no-direct-connection`, which means other M-codes ARE present but unrelated to this one.",
  "tightly-related": "this term's own role connects SUBSTANTIVELY to another M-code term present in the same scope -- a real causal/enabling/response/tension link, or the two share the same acting party -- not just topical co-presence in the same list or catalogue.",
  "no-direct-connection": "other M-code term(s) ARE present in this scope, but this term's own role does not meaningfully connect to them (no causal link, no shared party, no real interaction) -- distinct from `sole-mcode-in-verse`, where nothing else is present to connect to at all.",
  "cluster-pole-negative": "this term occupies the negative/negligent pole of a dual-natured cluster (e.g. idleness within a sloth-vs-diligence cluster).",
  "cluster-pole-positive": "this term occupies the positive/virtuous pole of a dual-natured cluster (e.g. diligence/zeal within a sloth-vs-diligence cluster).",
  "attested-pre-nt": "the term is attested in classical/pre-NT Greek or Hebrew usage, not coined in the NT period.",
  "nt-coinage": "the term (or this specific sense of it) has no attestation before the NT -- a NT-period coinage or semantic innovation.",
  "alternative-meaning": "this SPECIFIC occurrence genuinely supports MORE THAN ONE plausible reading/sense, and the data does not clearly settle which -- real ambiguity, not just a divergence from the usual sense (that's `surface-gloss-divergence` when it's the FORM, or a plain substantive answer when the sense is clear but simply different from elsewhere). State both/all candidate readings in `obs_text`, not just one.",
  "surface-gloss-divergence": "this occurrence's actual surface form (`span.surface`, the inflected text as it appears) diverges from its `stepGloss` dictionary-standard rendering in a way worth noting -- a form-level fact (e.g. an idiomatic rendering, a metaphorical extension the standard gloss doesn't capture), not a claim of multiple valid readings (`alternative-meaning`).",
  "no-human-context": "this strong is exclusively a homonym or proper name with no meaningful context for a human reader to analyse -- earmark it as such and stop; do not force an analysis where none is genuinely available (cfg_method_rule 'homonym-no-context-earmarked-and-left').",
  "data-error": "a data-quality issue noticed while reading (wrong cluster/subgroup membership, a broken span/verse link, a corrupted meaning source) -- flag it here, in its own section; never chase it down or fix it as part of this task (cfg_method_rule 'data-errors-flagged-separately').",
  "verse-grouping": "several of THIS strong's own occurrences, across different verses, share one genuinely alike reading -- group them under one finding rather than repeating the same point per verse. Requires visibility across a strong's full occurrence set; not meaningful at a single-verse grain.",
  "difference-inference": "a specific inference or distinction drawn from comparing THIS strong's own occurrences against EACH OTHER (morph-driven distinctions included -- e.g. whether a stem/voice variation across occurrences is meaning-relevant). Requires visibility across a strong's full occurrence set; not meaningful at a single-verse grain.",
  "could-not-resolve": "a genuine 'couldn't resolve' case -- state in `obs_text` what signal suggests it should be resolvable with further analysis, never a bare flag with no reason.",
  "needs_adjacent_verse_context": "this verse's own content is insufficient and an adjacent/surrounding verse would help -- state explicitly in `obs_text` what's outstanding and what the follow-up cross-check needs to establish. Resolution happens in a later analytic pass, never fetched ad hoc here.",
  "elevation-candidate": "this T2/T3-tagged (non-M-code) word's role in THIS verse suggests it names a distinct inner-being characteristic in its own right, not just a supporting role -- state the reason in `obs_text` (M0.8.1 only; escalation #1836). A later, separate process reviews elevation candidates for actual cluster promotion -- this tag only surfaces the candidate, it does not itself change any cluster/role assignment.",
  "answered-no-flag": "a genuinely plain, substantive answer that matches none of the other tags and has nothing else worth categorising (e.g. a straightforward root-meaning or primary-term identification) -- a LAST RESORT, not a default. Check every observation against the other tags above before reaching for this one."
 },
 "excluded": {
  "verse-reading": [
   "difference-inference",
   "verse-grouping"
  ],
  "char-subgroup": [],
  "char-reading": [],
  "char-answers": []
 }
}''')

# read only by the removed lexical.run (handlers/lexical.py)
ORPHANS = ["lexical.run_max_verses", "report.lexical_notes_output_pattern"]
# looked up only by the removed Layer 2 briefing pack; their table verse_lexical_note is inactive
ORPHAN_ENUM_GROUPS = ["note_type", "resolution_status"]

# (table, where, set)
RETIRE = [
    ("cfg_work_package", {"name": "batch-progress-report"}, {"inactive": 1}),
    ("cfg_step", {"work_package": "batch-progress-report", "step": "report.batch_progress"}, {"inactive": 1}),
    ("cfg_report", {"step": "report.batch_progress"}, {"inactive": 1}),
    ("cfg_setting", {"key": "report.batch_progress_path"}, {"inactive": 1}),
    ("cfg_utility", {"module": "batchprogressreport"},
     {"inactive": 1, "file_path": "iba/app/lib/archive/batchprogressreport.py"}),
    ("cfg_utility", {"module": "lexicalenrich"},
     {"inactive": 1, "file_path": "iba/app/lib/archive/lexicalenrich.py"}),
] + [("cfg_report_section", {"step": "report.batch_progress", "section_key": k}, {"inactive": 1})
     for k in ("summary", "running_now", "recent_committed", "recent_failures")] \
  + [("cfg_setting", {"key": k}, {"inactive": 1}) for k in ORPHANS]

SETTINGS = [
    {"key": "ib_observation.tag_guidance", "value": json.dumps(TAG_DATA["guidance"], ensure_ascii=False),
     "module": "cluster", "inactive": 0,
     "use": "#2207: the definition of each ib_observation.tag value, given to the model by every "
            "LLM-calling generator stage (lib/taggingguidance.guidance_block). A tag in cfg_enum "
            "ib_observation.tag with no definition here is not offered to any stage."},
    {"key": "ib_observation.tag_stage_excluded", "value": json.dumps(TAG_DATA["excluded"]),
     "module": "cluster", "inactive": 0,
     "use": "#2207: per generator stage, the tags it may not offer (lib/taggingguidance.tags_for_stage). "
            "verse-reading sees one verse at a time, so the cross-occurrence tags are excluded there."},
]


def _where_sql(where: dict) -> tuple[str, list]:
    return " AND ".join(f'"{k}"=?' for k in where), list(where.values())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    retire = RETIRE + [("cfg_enum", {"name": g, "value": v}, {"inactive": 1})
                       for g in ORPHAN_ENUM_GROUPS
                       for (v,) in conn.execute("SELECT value FROM cfg_enum WHERE name=? ORDER BY ordinal", (g,))]
    for table, where, set_ in retire:
        w, v = _where_sql(where)
        cur = conn.execute(f'SELECT {", ".join(chr(34) + c + chr(34) for c in set_)} FROM "{table}" '
                           f'WHERE {w}', v).fetchone()
        if cur is None:
            print(f"missing row: {table} {where}")
            return 1
        if list(cur) != list(set_.values()):
            ops.append((table, "update", where, set_))
    for row in SETTINGS:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (row["key"],)).fetchone():
            ops.append(("cfg_setting", "insert", {}, row))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2207 item 2: batch monitoring and lexicalenrich "
                       f"retired, tag definitions into cfg_setting, through configmaint.apply_logged "
                       f"under run_id {RUN_ID}. inactive=1 once applied."}))
    for t, op, where, set_ in ops:
        print(f"  {op} {t} {where or ''} {list(set_)}")
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
