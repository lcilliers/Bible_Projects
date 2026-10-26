"""scope_resolver_2295_v1_20261026.py -- escalation #2295 (#2286 U5; build plan
outputs/escalation/2286-build-plan-v4-20261025.md section 6): the config of the occurrence-shaped scope resolver.

1. verse_scope.resolve's description: the occurrences, the home, the word through the surface, the scope items.
2. Behaviour rules B:119 scope-enters-through-surface and B:120 scope-home-and-multiplicity: their enforcement
   recorded.

The code is lib/versescope.py, handlers/versescope.py, ps/Verse-Scope.ps1 (-Home), lib/reading.py open_ and
lib/versecollate.py. cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive
path). Idempotent.

Usage:
    python iba/app/migration/scope_resolver_2295_v1_20261026.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2295-SCOPE-RESOLVER-20261026"
MODULE = "scope_resolver_2295_v1_20261026"
DOES = ("the scope resolver: any request (cluster, subgroup, strand, word, strong -- a bare code decomposed to its "
        "derivatives -- verse references, narrative chapter or block, claim, observation, thread item or thread, "
        "request file) -> the collection of verses as JSON, occurrence-shaped (version 2, #2295): each verse with its "
        "routes, its M-coded occurrences placed in their subgroups (two-sense flag, settlement, in scope, in the "
        "home) and its other words as context; a mapped M cluster or a subgroup enters through its (code, surface) "
        "pairs, a word through its surface (never word_strong), a scope item through its stored verses; the home is "
        "-Home or the subgroups and M clusters named, never a qualifier group or a T cluster; everything not resolved "
        "listed; -OnlyStrong narrows it (read-only) -- see lib/versescope.py (escalations #2228, #2295)")
RULES = {
    "scope-enters-through-surface": (
        "mechanically_enforced",
        "iba/app/lib/versescope.py Resolver.word (#2295): a word is matched to verse_lexical.surface and its "
        "occurrences; word_strong is not read by the resolver. Every scope (Verse-Scope.ps1, Reading.ps1 -Step Open, "
        "Verse-Collate, open items) is resolved there."),
    "scope-home-and-multiplicity": (
        "partially_enforced",
        "iba/app/lib/versescope.py (#2295): the home is -Home or the subgroups and M clusters named (reading.open: "
        "its subgroups of the home cluster, else the home cluster); a qualifier group is refused as a subgroup "
        "selector or a home and a T cluster as a home; each verse lists the other subgroups of its occurrences "
        "without adding verses, and a selector lists every subgroup its occurrences fall in. That a qualifying word "
        "is read for what it gives, the exceptional raising of a T code and the later second reading are delivered "
        "as context."),
}


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if one("SELECT does FROM cfg_step WHERE step='verse_scope.resolve'")[0] != DOES:
        ops.append(("cfg_step", "update", {"step": "verse_scope.resolve"}, {"does": DOES}))
    for key, (status, by) in RULES.items():
        r = one("SELECT id, enforcement_status, enforced_by FROM cfg_behaviour_rule WHERE class='study_method' AND "
                "rule_key=?", key)
        if (r[1], r[2]) != (status, by):
            ops.append(("cfg_behaviour_rule", "update", {"id": r[0]}, {"enforcement_status": status,
                                                                       "enforced_by": by}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2295 (#2286 U5): verse_scope.resolve's description and the "
                       f"enforcement of B:119 and B:120; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, set_ in ops:
            print(f"  {op:6} {t:20} {where or set_.get('module')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
