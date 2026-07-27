"""backfill_passage_tracking_daniel.py — ONE-OFF, idempotent: back-fills `passage`/
`verse_passage` tracking rows (`lib/passagetrack.py`, `migration/repurpose_passage_tracking.py`)
for the five Daniel ranges already processed before the tracking feature existed. Calls the same
`passagetrack.record_extract`/`record_debate` functions the live report handlers now call — no
separate logic, so a backfilled row is indistinguishable from one produced by a real run. Reads
only (verse text, the already-written extract/debate files); does not regenerate or touch any
report file.

    python -m iba.app.migration.backfill_passage_tracking_daniel
"""

from __future__ import annotations

import pathlib
import sys

from ..lib.cfg import Cfg
from ..lib import passagetrack

RANGES = [
    # (chapter, verse_lo, verse_hi, extract_filename, debate_filename)
    (1, 1, 7, "dan-1-1-7-verse-span-meaning.md", "WA-dan-1-1-7-debate-v1.1-2026-07-27.md"),
    (1, 7, 21, "dan-1-7-21-verse-span-meaning.md", "WA-dan-1-7-21-debate-v1.1-2026-07-27.md"),
    (2, 1, 16, "dan-2-1-16-verse-span-meaning.md", "WA-dan-2-1-16-debate-v1.1-2026-07-27.md"),
    (2, 17, 30, "dan-2-17-30-verse-span-meaning.md", "WA-dan-2-17-30-debate-v1.1-2026-07-27.md"),
    (2, 31, 49, "dan-2-31-49-verse-span-meaning.md", "WA-dan-2-31-49-debate.md"),
]
BOOK_DIR = pathlib.Path("iba/app/verse-analysis/Daniel")


def main() -> int:
    cfg = Cfg()
    report: list[str] = []
    for ch, vlo, vhi, extract_name, debate_name in RANGES:
        extract_path = BOOK_DIR / extract_name
        debate_path = BOOK_DIR / debate_name
        if not extract_path.exists():
            report.append(f"Dan {ch}:{vlo}-{vhi}: SKIPPED — {extract_path} not found")
            continue
        pid = passagetrack.record_extract(cfg, "Dan", ch, ch, vlo, vhi, "Daniel", extract_path)
        line = f"Dan {ch}:{vlo}-{vhi}: passage_id={pid}, extract backfilled"
        if debate_path.exists():
            passagetrack.record_debate(cfg, "Dan", ch, ch, vlo, vhi, "Daniel", debate_path)
            line += ", debate backfilled"
        else:
            line += f", debate SKIPPED — {debate_path} not found"
        report.append(line)
    cfg.conn.commit()          # Cfg.close() does not commit (only Db.close() does) — direct
                                # cfg.conn writes here need an explicit commit before closing.
    cfg.close()

    print("Daniel passage-tracking backfill:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
