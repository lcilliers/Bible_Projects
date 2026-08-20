"""reset_escalation_tables_20260820.py — one-off, researcher-directed.

Researcher, live 2026-08-20, after a cascade of design/implementation defects found across one
session (short_description column-spec violations, originator misattribution on >=39 rows,
cfg_escalation rows claiming enforcement by a function that no longer exists, escalation_history
storing cumulative text instead of per-version deltas, the deep-history report silently dropping
7 of 19 columns, the state-derivation/validation rule engine having no config representation at
all): *"the system is not ready for production ... export the data in the both tables to a json.
and delete all the records in both tables. Then go back and do a proper design and
implementation."*

Exports `escalation` and `escalation_history` verbatim to JSON (full fidelity, nothing summarised
or dropped), then deletes every row from both and resets their id sequences so the rebuilt system
starts clean. `escalations_old` (the PRE-vious reset's frozen table, 723 rows, already inactive) is
untouched — this is a second, unrelated archival, not a merge with it.

Run: python -m iba.app.migration.reset_escalation_tables_20260820
"""

from __future__ import annotations

import datetime
import json
import pathlib

from ..lib.cfg import Cfg
from ..lib.db import Db

_STAMP = "20260820"
_ARCHIVE_DIR = pathlib.Path(__file__).resolve().parent.parent / "db" / "archive"


def main() -> None:
    cfg = Cfg()
    db = Db(cfg)

    esc_rows = [dict(r) for r in db.rows("SELECT * FROM escalation ORDER BY id")]
    hist_rows = [dict(r) for r in db.rows("SELECT * FROM escalation_history ORDER BY escalation_id, version")]

    _ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    esc_path = _ARCHIVE_DIR / f"escalation-export-{_STAMP}.json"
    hist_path = _ARCHIVE_DIR / f"escalation_history-export-{_STAMP}.json"
    meta = {
        "exported_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "reason": "researcher-directed full reset, 2026-08-20 -- system not ready for production, "
                 "see iba/docs/ for the design record this preceded",
        "row_count": len(esc_rows),
    }
    esc_path.write_text(json.dumps({"meta": meta, "rows": esc_rows}, indent=2, default=str),
                        encoding="utf-8")
    meta_h = {**meta, "row_count": len(hist_rows)}
    hist_path.write_text(json.dumps({"meta": meta_h, "rows": hist_rows}, indent=2, default=str),
                         encoding="utf-8")
    print(f"  exported {len(esc_rows)} escalation rows -> {esc_path}")
    print(f"  exported {len(hist_rows)} escalation_history rows -> {hist_path}")

    if "escalation" not in cfg.may_write("escalation") or "escalation_history" not in cfg.may_write("escalation"):
        raise PermissionError("write-grant violation: 'escalation' may not write escalation/escalation_history")

    db.conn.execute("DELETE FROM escalation_history")
    db.conn.execute("DELETE FROM escalation")
    db.conn.execute("DELETE FROM sqlite_sequence WHERE name IN ('escalation', 'escalation_history')")
    db.conn.commit()

    n_esc = db.rows("SELECT COUNT(*) n FROM escalation")[0]["n"]
    n_hist = db.rows("SELECT COUNT(*) n FROM escalation_history")[0]["n"]
    print(f"  post-delete counts: escalation={n_esc}, escalation_history={n_hist}")
    assert n_esc == 0 and n_hist == 0, "delete did not clear both tables"

    db.close()
    cfg.close()
    print("\nBoth tables emptied and id sequences reset. escalations_old (723 rows, already "
         "inactive from the 2026-08-19 reset) is untouched.")


if __name__ == "__main__":
    main()
