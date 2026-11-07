"""verse_lexical_units_2381_v1_20261107.py -- escalation #2381, stage 1 (design
outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md, approved by the researcher 2026-11-07).

A multi-term unit (one STEP span with several codes) was stored as separate rows that all carried the unit's word. This stage
gives verse_lexical the columns that tell the code's own word from the unit's rendering, and the config that sets them:

  schema (iba.db): verse_lexical gains unit_surface TEXT, surface_kind TEXT, unit_size INTEGER, unit_role TEXT (additive,
    nullable; no row is touched here, lexical.build fills them);
  config (through configmaint.apply_logged, Developer Mode migration):
    - cfg_column rows for the four columns, and the new use text of verse_lexical.surface;
    - cfg_enum verse_lexical.surface_kind (own, shared, gloss) and verse_lexical.unit_role (sole, head, content_part, prefix,
      suffix, affix);
    - cfg_setting lexical.span_surface gains prefix_morph_classes, suffix_morph_classes and not_affix_codes;
    - cfg_utility: this migration is registered.
Idempotent. Usage:
    python iba/app/migration/verse_lexical_units_2381_v1_20261107.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2381-VERSE-LEXICAL-UNITS-20261107"
MODULE = "verse_lexical_units_2381_v1_20261107"
SRC = "escalation #2381, design v2 of 2026-11-07 (outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md)"

COLUMNS = [  # name, ordinal, type, use, expectation
    ("unit_surface", 21, "TEXT",
     "the whole rendering of the multi-term unit this code belongs to: span.surface, on every row of the unit. For a code in a "
     "one-code unit it equals surface. The unit is read as one item (lexical.unit_view); this is the multi-term meaning, kept apart "
     "from the code's own surface", None),
    ("surface_kind", 22, "TEXT",
     "how far surface is this code's own: own (its own word in the verse: a one-code unit, the one content code of a unit with "
     "affixes, or a content code whose exact word the look-back found), shared (a content code of a unit with two or more content "
     "codes whose word could not be found: surface is the unit's rendering and the owner is not decided), gloss (an affix code: "
     "surface is its own STEP gloss)", "enum.verse_lexical.surface_kind"),
    ("unit_size", 23, "INTEGER", "the number of codes in the unit (the span): 1 is not a multi-term unit", None),
    ("unit_role", 24, "TEXT",
     "what this code is in its unit: sole (the unit's only code), head (the one content code of a unit with affixes), "
     "content_part (one of several content codes), prefix or suffix (an affix, by the morph class in cfg_setting "
     "lexical.span_surface), affix (an affix whose morph class is in neither list)", "enum.verse_lexical.unit_role"),
]
SURFACE_USE = ("the English that belongs to THIS code (#2381): its own word, or for an affix code its own STEP gloss; see "
               "surface_kind. The whole unit's rendering is unit_surface. Filled by lexical.build from span.surface and the rules "
               "in cfg_setting lexical.span_surface")
ENUMS = {
    "verse_lexical.surface_kind": ["own", "shared", "gloss"],
    "verse_lexical.unit_role": ["sole", "head", "content_part", "prefix", "suffix", "affix"],
}
NEW_RULES = {"prefix_morph_classes": ["HC", "HT", "HR", "AC", "AT", "AR"],
             "suffix_morph_classes": ["HS", "AS"],
             "not_affix_codes": ["G9315", "G9577"]}
RULES_USE_ADD = (" #2381: prefix_morph_classes and suffix_morph_classes are the starts of the morph code that tell an affix code "
                 "(discovery.particle_pattern) as a prefix or a suffix of its unit; not_affix_codes are codes the pattern takes "
                 "that are content words (two Greek codes)")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for name, ordinal, typ, use, exp in COLUMNS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='verse_lexical' AND name=?", name):
            ops.append(("cfg_column", "insert", {}, {"database": "iba", "table_name": "verse_lexical", "name": name, "ordinal": ordinal,
                        "type": typ, "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None, "fk": None, "use": use,
                        "expectation": exp, "source": SRC, "filled_by": "lexical.build", "inactive": 0}))
    cur = conn.execute("SELECT use FROM cfg_column WHERE database='iba' AND table_name='verse_lexical' AND name='surface'").fetchone()[0]
    if cur != SURFACE_USE:
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "verse_lexical", "name": "surface"},
                    {"use": SURFACE_USE, "source": SRC}))
    for enum, values in ENUMS.items():
        for i, v in enumerate(values):
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", enum, v):
                ops.append(("cfg_enum", "insert", {}, {"name": enum, "value": v, "ordinal": i, "inactive": 0}))
    row = conn.execute("SELECT value, use FROM cfg_setting WHERE key='lexical.span_surface'").fetchone()
    val = json.loads(row[0])
    if any(k not in val for k in NEW_RULES):
        ops.append(("cfg_setting", "update", {"key": "lexical.span_surface"},
                    {"value": json.dumps({**val, **{k: v for k, v in NEW_RULES.items() if k not in val}}),
                     "use": row[1] if RULES_USE_ADD in (row[1] or "") else (row[1] or "") + RULES_USE_ADD}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 0,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2381 stage 1: verse_lexical unit columns and their config; run_id {RUN_ID}.",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    have = {r[1] for r in conn.execute("PRAGMA table_info(verse_lexical)")}
    alters = [c for c in COLUMNS if c[0] not in have]
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(alters)} column(s) to add, {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {where or set_.get('name') or set_.get('module') or set_.get('key')}")
        return 0
    if not alters and not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT vlu")
        for name, _o, typ, _u, _e in alters:
            conn.execute(f"ALTER TABLE verse_lexical ADD COLUMN {name} {typ}")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE vlu")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO vlu")
        conn.execute("RELEASE vlu")
        raise
    print(f"applied (run {RUN_ID}): {len(alters)} column(s), {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
