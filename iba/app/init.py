"""init.py — the app bootstrap. Prepare the environment; report ready.

The startup sequence, idempotent:
  1. validate the config seeds (cfgcheck) — refuse to start on incoherent config
  2. load the config into the DB if it is not already there (or --reload to reseed)
  3. build the data tables from the config if they are missing (or --reset to rebuild)
  4. pre-flight STEP — up AND answering with the tagged module
  5. orient on BUILD.md + GOVERNANCE.md — what's built, and how config governs it
  6. print every governance.* cfg_setting explicitly — the only real 'usage' a process rule has
     (added 2026-07-23, escalation #305 — see lib/cfgquality.find_orphan_configs)
  7. print the status

Run it before the first run of a session:
    python -m iba.app.init            # prepare + status (idempotent)
    python -m iba.app.init --reload   # reseed the config from the JSON
    python -m iba.app.init --reset    # rebuild the data tables (drops data)
"""

from __future__ import annotations

import argparse
import pathlib
import sqlite3
import sys

from .lib.cfg import Cfg, DB_PATH
from .lib import cfgload, db as dbmod

APP_DIR = pathlib.Path(__file__).resolve().parent


def _doc_orientation(path: pathlib.Path) -> str:
    """First heading + first blockquote line of a doc — enough to orient without dumping it."""
    if not path.exists():
        return f"MISSING — expected at {path}"
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = next((l.lstrip("#").strip() for l in lines if l.startswith("#")), path.name)
    blurb = next((l[2:].strip() for l in lines if l.startswith(">")), "")
    return f"{heading} — {blurb}"


def _config_loaded() -> bool:
    if not DB_PATH.exists():
        return False
    try:
        c = sqlite3.connect(DB_PATH)
        c.execute("SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
        c.close()
        return True
    except sqlite3.Error:
        return False


def _data_tables_exist(cfg: Cfg) -> bool:
    c = sqlite3.connect(DB_PATH)
    have = {r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    c.close()
    return set(cfg.tables()).issubset(have)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reload", action="store_true", help="reseed the config from the JSON")
    ap.add_argument("--reset", action="store_true", help="rebuild the data tables (DROPS data)")
    a = ap.parse_args()

    print("IBA app — startup")

    # 1-2. config
    if a.reload or not _config_loaded():
        try:
            _, counts = cfgload.load()
        except cfgload.ConfigRejected as e:
            print(f"  ✗ {e}", file=sys.stderr)
            return 1
        print(f"  ✓ config loaded ({sum(counts.values())} rows in {len(counts)} cfg_* tables)")
    else:
        print("  ✓ config already loaded (use --reload to reseed)")

    cfg = Cfg()
    print(f"    config_version: {cfg.config_version()}")

    # 3. data tables
    if a.reset or not _data_tables_exist(cfg):
        dbmod.build(reset_data=a.reset)
        print(f"  ✓ data tables {'rebuilt' if a.reset else 'created'} ({len(cfg.tables())} tables)")
    else:
        print(f"  ✓ data tables present ({len(cfg.tables())})")

    # 4. STEP pre-flight
    from .lib.stepapi import Step, StepUnavailable
    try:
        ev = Step(cfg).up()
        # report the EVIDENCE, not a bare 'up' — the known answer that proves it
        print(f"  ✓ STEP up and tagged ({ev['base']}, {ev['version']})")
        print(f"    known-answer probe: {ev['probe']} -> {ev['resolved']} "
              f"gloss {ev['gloss']!r}, {ev['verses']} verses")
        step_ok = True
    except StepUnavailable as e:
        print(f"  ⚠ STEP not ready: {e}")
        print(f"    start the local STEP server, then re-run this. Runs will refuse to start without it.")
        step_ok = False

    # 5. orientation — read before touching code or config; not a substitute for reading them in full
    print("\n  orientation (read before making changes):")
    print(f"    BUILD.md      {_doc_orientation(APP_DIR / 'BUILD.md')}")
    print(f"    GOVERNANCE.md {_doc_orientation(APP_DIR / 'GOVERNANCE.md')}")

    # 6. governance rules — read EXPLICITLY here, not just pointed at via the doc above. Per the
    # researcher's 2026-07-23 correction (escalation #305): a governance.* cfg_setting is a
    # process rule the AI must comply with, not a runtime application input, so it has no code
    # path that "applies its value" the way an ordinary setting does. Its only real 'usage' is
    # being surfaced here, at the one place every session is required to run before doing any
    # work — otherwise it's a rule that exists only as an unread database row.
    print("\n  governance rules (must be complied with this session):")
    for row in cfg.conn.execute(
            "SELECT key, value FROM cfg_setting WHERE module='governance' ORDER BY key"):
        print(f"    {row['key']}: {row['value']}")

    cfg.close()

    print("\nREADY." if step_ok else "\nREADY (config + DB) — waiting on STEP.")
    print("  first run:  iba\\app\\ps\\New-Word.ps1 -Word <word> -Source \"<why>\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
