"""bare_strong_rule_2233_v1_20261022.py -- escalation #2233: the researcher's rule that a bare Strong's
code is always decomposed to its derivatives, as a cfg_behaviour_rule row (it stood only in memory and a
docstring). Delivered at point of use for the two tools that take Strong's codes from a request
(Verse-Scope.ps1, Strand-Reading.ps1). Enforced by iba/app/lib/versescope.py (decompose).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/bare_strong_rule_2233_v1_20261022.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2233-BARE-STRONG-20261022"
MODULE = "bare_strong_rule_2233_v1_20261022"
KEY = "bare-strong-decomposed-to-derivatives"
TEXT = ("Study work never works with a bare Strong's code. A bare code that is referenced (H0430) is always "
        "decomposed to its derivatives: every lettered code of that base that occurs in verse_lexical (H0430G, "
        "H0430H, ...). A bare code that occurs itself has no derivatives and is taken as it is, as is a suffixed "
        "code. The collection of verses taken into analysis may then be focused on a subset of the derivatives.")
SOURCE = ("Researcher, chat 2026-10-22 (verbatim, #2228 v9): \"there is a rule that we do not work with bare "
          "strongs, but always with the derivatives. so when a bare strong is referenced, it must always be "
          "decomposed to its derivatives. however, the collection of verses that goes into analysis may be "
          "focussed on a subset of the derivatives.\" Captured in config by escalation #2233.")
ENFORCED = "iba/app/lib/versescope.py (Resolver.decompose): every Strong's code a request names, the scope resolver"
SCOPES = [("ps", "Verse-Scope.ps1"), ("ps", "Strand-Reading.ps1")]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    row = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (KEY,)).fetchone()
    rid = row[0] if row else conn.execute("SELECT max(id) FROM cfg_behaviour_rule").fetchone()[0] + 1
    if not row:
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": rid, "class": "study_method", "rule_key": KEY, "rule_text": TEXT, "source": SOURCE,
            "enforced_by": ENFORCED, "added_at": datetime.datetime.now(datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"), "active": 1, "enforcement_status": "mechanically_enforced",
            "deliver_when": "always"}))
    for kind, value in SCOPES:
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind=? AND scope_value=?",
                   f"B:{rid}", kind, value):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{rid}", "scope_kind": kind,
                                                         "scope_value": value, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2233: cfg_behaviour_rule {KEY} and its point-of-use "
                       f"scopes; run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
