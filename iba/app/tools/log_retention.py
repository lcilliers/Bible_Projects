"""log_retention.py — generate the run/escalation/validation_result log-retention & run-health
report (lib/retention.py). Read-only; no rows are pruned, archived, or deleted.

    python -m iba.app.tools.log_retention
"""

from __future__ import annotations

import pathlib
import sys

from ..lib.cfg import Cfg
from ..lib import retention


def main() -> int:
    cfg = Cfg()
    path = pathlib.Path(cfg.setting("retention.report_path", "iba/app/reports/log-retention.md"))
    out = retention.write_report(cfg, path)
    cfg.close()
    print(f"log-retention report written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
