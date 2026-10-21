"""bootstrap_passage_debate_sync.py — ONE-OFF, idempotent: registers `passage.debate_sync` (the
debate-status re-sync step — see `handlers/passage.py:debate_sync`) as a real dispatcher work
package/step, matching the established pattern `bootstrap_passage_debate_report.py` used for
`report.passage_debate` — direct `cfg_*` inserts, not routed through `configmaint.propose`
row-by-row (GOVERNANCE.md §9B/§14, same infrastructure-registration carve-out).

**Why this exists.** `report.passage_debate` writes a scaffold and `passagetrack.record_debate`
records its tracked status in the same call — but that call only ever fires once, immediately
after the scaffold is written, when the file still holds every `<!-- fill in -->` placeholder. No
step previously re-checked `passage.debate_status` after the researcher/AI filled the scaffold in
by hand, so the tracked status could only ever legitimately read `scaffold`. A live session
(2026-07-30) found this gap while starting Micah's passage debates and, instead of stopping, read
`BUILD.md` history and diffed archived Jonah/Joel/Obadiah output files to infer how those books'
rows ever reached `filled` — exactly the doc/output-archaeology pattern
`governance.past_precedent_investigation_signals_missing_config` (GOVERNANCE.md §3B, escalation
#409, approved same day) now bans as a substitute for closing a real config gap. This migration
closes the gap itself: a registered step, read-only against the debate file, that re-checks it for
the fill-in marker and updates the tracked `passage` row via the existing, already-tested
`passagetrack.record_debate` — it does not regenerate or rewrite the debate file (that stays
`report.passage_debate`'s job; rerunning IT on an already-filled range would overwrite real content
with a blank scaffold, per `report.passage_debate`'s own BUILD.md entry).

A pure DB-mutation step (kind='operations', no file output of its own) — no `cfg_report`/
`cfg_report_section` rows, matching `passage.build`/`candidate.curate`/`lexicon.parse`'s pattern,
not `report.passage_debate`'s (which writes a report file).

    python -m iba.app.migration.bootstrap_passage_debate_sync
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "passage-debate-sync"
PS_SCRIPT = "iba/app/ps/PassageDebate-Sync.ps1"
STEP = "passage.debate_sync"
HANDLER = "iba.app.handlers.passage:debate_sync"
DOES = ("re-syncs `passage.debate_status` for an already-generated `report.passage_debate` "
       "scaffold against its CURRENT on-disk content — read-only against the debate file "
       "(does not rewrite or regenerate it), DB-write only to the tracked `passage` row's "
       "`debate_status`/`debate_written_at` via the existing `passagetrack.record_debate`; the "
       "missing half of the report.passage_debate lifecycle before this (write_scaffold writes, "
       "nothing re-checked status after manual fill-in) — GOVERNANCE.md §3B")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (WP,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                    "complete_message, next_step_hint, paused_message, inactive) "
                    "VALUES (?,?,'book',0,NULL,NULL,NULL,0)", (WP, PS_SCRIPT))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (WP, STEP)).fetchone():
        conn.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                    "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                     (WP, 0, STEP, HANDLER, "book", DOES, "operations"))
        report.append(f"cfg_step {STEP!r} added")
    else:
        report.append(f"cfg_step {STEP!r} already present")

    _on_fail = [
        ("no-debate-file", "report-stop",
         "no report.passage_debate output tracked yet for this exact book/range — run "
         "PassageDebate-Report.ps1 first (report.passage_debate)", "terminal"),
        ("debate-file-missing", "report-stop",
         "the tracked debate_path no longer exists on disk — was it moved or deleted outside "
         "the app?", "terminal"),
    ]
    for condition, path, message, route in _on_fail:
        if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                            (STEP, condition)).fetchone():
            conn.execute(
                "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, "
                "inactive) VALUES (?,?,?,?,?,?,0)",
                (STEP, condition, path, None, message, route))
            report.append(f"cfg_on_fail ({STEP}, {condition}) added")
        else:
            report.append(f"cfg_on_fail ({STEP}, {condition}) already present")

    conn.commit()
    conn.close()

    print("passage-debate-sync bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
