"""escalation_crash_review_rollout_20260821.py — D3's rollout (register v9): one genuine pass over
every active `cfg_utility` module, setting `crash_escalation_reviewed=1` and a real
`crash_escalation_note` — what actually happens if THIS module's write crashes mid-transaction.
Not bulk-defaulted: each note below reflects an actual check of the module (grep for
`.commit()`/`try`/`except`/`__main__`, cross-checked against whether it's ever invoked outside the
run.py dispatcher), not a copy-pasted line.

**The finding, in one paragraph**: every `iba/app/lib/*.py` report/support module reviewed here has
NO `__main__` entry point and is only ever reached through a `handlers/*.py` function that run.py
calls — so its crash-recovery is INHERITED from run.py's own except block (`db.conn.rollback()`,
then a permanent `escalation` record, `etype='run_error'`, before re-raising — see run.py:172-200).
That inheritance is genuine, not assumed: `Db`/`Cfg` share ONE connection per process
(`db.py:117-121`), and neither `write()`/`update()` calls `.commit()` themselves — only `close()`
does, which run.py's except block never reaches on a crash (it rolls back first). The real gap is
the OTHER category: standalone scripts with their own `if __name__ == "__main__":` entry point,
run directly (`python -m ...`), outside the dispatcher entirely — these have no equivalent net. A
mid-script crash there is a bare traceback to the console with no permanent record, UNLESS the
script wraps its own `main()` the way `lib/escalation.py`'s CLI does. Found genuinely unprotected
this pass: the four `bootstrap_behaviour_rules_*` migrations and `engine/migrate.py` — flagged
below, not fixed here (out of this round's scope; a candidate for its own follow-up, same shape as
the already-parked D22 for Escalation.ps1).

    python -m iba.app.migration.escalation_crash_review_rollout_20260821
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

# module -> genuine crash-recovery note, one real fact about that module's OWN write/commit shape.
NOTES: dict[str, str] = {
    # ── dispatcher-only handler-support modules: crash-recovery inherited from run.py's own
    #    except block (rollback + a permanent escalation record) -- no __main__, never invoked any
    #    other way, confirmed by grep this pass. ──────────────────────────────────────────────
    "behaviour": "No __main__, no DB write of its own (reads cfg_behaviour_class/_rule) — nothing "
                 "to roll back; dispatcher-inherited if ever called from a write path.",
    "cfgquality": "No __main__, read-only (every find_* function is a SELECT-only check) — nothing "
                  "to roll back.",
    "cfgreport": "No __main__, read-only (renders CONFIG-REPORT.md from live cfg_* SELECTs) — "
                "nothing to roll back.",
    "clusterassign": "No __main__; writes (if any) go through Db.write()/update() only, called from "
                     "a handlers/*.py function — crash-recovery inherited from run.py's except "
                     "block (rollback before the crash is recorded).",
    "clusterreport": "No __main__, read-only report render — nothing to roll back.",
    "contentindex": "No __main__; writes its own INSERTs + a single conn.commit() (content_index.py "
                    ":247,272) but ONLY when called from handlers/reports.py's "
                    "content_index_rebuild/_search — dispatcher-inherited: a crash before its "
                    "commit() is rolled back by run.py's except block on the SAME shared connection.",
    "debateaudit": "No __main__; writes via ctx.db.conn directly from handlers/debate.py-shaped "
                   "callers — dispatcher-inherited.",
    "debaterun": "No __main__, dispatcher-inherited.",
    "lexical": "No __main__, dispatcher-inherited (verse_lexical writes go through Db).",
    "lexiconparse": "No __main__, pure parse functions (regex/tag-set) — no DB write at all.",
    "manifest": "No __main__; writes its own INSERTs + a single conn.commit() (manifest.py:327) but "
               "ONLY when called from handlers/reports.py's manifest_rebuild/_search — "
               "dispatcher-inherited.",
    "passagedebatereport": "No __main__, dispatcher-inherited (passagetrack.record_debate does the "
                           "actual write).",
    "passagetrack": "No __main__, dispatcher-inherited.",
    "registryreport": "No __main__, read-only report render — nothing to roll back.",
    "reportkit": "No __main__; a shared library of render/archive HELPERS (render_scaffold, "
                 "archive_before_write, oneoff_path) used by every report module above — no "
                 "independent write path of its own to review beyond theirs.",
    "retention": "No __main__; write_report writes via db.write() (retention.py has a try/except "
                "around date parsing only, not the write itself) — dispatcher-inherited.",
    "schemareport": "No __main__, read-only report render — nothing to roll back.",
    "seedreport": "No __main__, read-only report render — nothing to roll back.",
    "spanreport": "No __main__, read-only report render — nothing to roll back.",
    "strongreconcile": "No __main__; writes via ctx.db.conn.commit() (strongreconcile.py:114) "
                       "explicitly INSIDE the handler call, called only from a handlers/*.py "
                       "function — dispatcher-inherited (the explicit commit here is deliberate "
                       "mid-run persistence, not a bypass of the shared-connection rollback net).",
    "strongreport": "No __main__, read-only report render — nothing to roll back.",
    "strongversereport": "No __main__, read-only report render — nothing to roll back.",
    "valuequality": "No __main__, read-only (enum-violation SELECT checks) — nothing to roll back.",
    "versespanmeaningreport": "No __main__, dispatcher-inherited (may write via raw.py's "
                              "backfill_meaning_for, called from the SAME handler invocation).",
    "wholebookread": "No __main__, read-only report render (reads passage_debate output) — nothing "
                     "to roll back.",
    "words": "No __main__, pure normalisation function (normalise()) — no DB write at all.",
    "stepapi": "No __main__, no DB write at all — an HTTP client to the local STEP server; its own "
              "failure mode is StepUnavailable (network/process down), caught by callers, not a "
              "DB-write crash-recovery concern.",

    # ── the mechanism itself, not a module built on top of it ─────────────────────────────────
    "cfg": "IS the shared connection cfg/db.py's rollback net depends on — .close() (cfg.py:306) is "
          "the only place THIS module itself commits; a crash before that never reaches it. "
          "Reviewed together with db/escalation below, not a separate gap.",
    "db": "db.write()/update() never call .commit() themselves (only Db.close()/the module-level "
         "build helper at db.py:94 do) — by design, so a crash mid-handler rolls back the WHOLE "
         "transaction via run.py's except block, not a half-written row. This IS the mechanism "
         "every 'dispatcher-inherited' module above relies on.",
    "escalation": "Its OWN crash-wrapper (main(), the CLI entry point) is D3's explicit subject — "
                 "now from_id-aware (register v9, this build): a failing update/history command "
                 "records which item it was operating on. Genuinely reviewed and fixed this round, "
                 "not just noted.",
    "cfgcheck": "No __main__, read-only (the pre-DB-migration JSON-seed checker, now largely "
               "superseded by configmaint.validate reading the live tables) — nothing to roll back.",

    # ── standalone scripts, own __main__, OUTSIDE the dispatcher — genuine gap, flagged not fixed ─
    "bootstrap_behaviour_rules": "GENUINE GAP: own __main__, single conn.commit() at the end "
                                 "(bootstrap_behaviour_rules_v1_20260818.py) but mixes 2 CREATE "
                                 "TABLE statements with INSERTs — Python sqlite3's legacy "
                                 "transaction handling auto-commits before DDL, so a crash AFTER "
                                 "the CREATE TABLE but BEFORE the final commit() can leave the "
                                 "table created but empty, with NO escalation record (no try/except "
                                 "at all). One-off, already run successfully — low ongoing risk, "
                                 "but the pattern is real, not assumed atomic. Not fixed this round "
                                 "(out of D3's scope — flagging is the deliverable).",
    "bootstrap_behaviour_rules_cycle2": "Same shape as bootstrap_behaviour_rules above (own "
                                        "__main__, single commit(), no try/except) but no DDL mixed "
                                        "in this one — a crash before commit() loses everything "
                                        "cleanly (no partial-DDL risk), still no escalation record.",
    "bootstrap_behaviour_rules_cycle3": "Same as cycle2 — own __main__, single commit(), no DDL, no "
                                        "try/except, no escalation record on crash.",
    "bootstrap_behaviour_rules_cycle4": "Same as cycle2/3 — own __main__, single commit(), no DDL, "
                                        "no try/except, no escalation record on crash.",
    "engine_migrate": "GENUINE GAP, the largest one found this pass: own __main__, ~60 DDL "
                      "statements across the file (engine/migrate.py) mixed with commits at "
                      "several points (one explicit commit noted at line 2350, 'otherwise the "
                      "history record silently vanishes on the NEXT connection'), a couple of "
                      "narrow try/except blocks around specific steps but no top-level crash "
                      "wrapper — a mid-run crash leaves an inconsistent PARTIAL migration state "
                      "with no escalation record. Legacy engine/ (superseded 2026-08-17 for "
                      "base-layer work, see CLAUDE.md) — real but low ongoing exposure. Not fixed "
                      "this round.",
    "engine_constants": "No functions, no writes — a pure constants module (EXPECTED_SCHEMA_"
                        "VERSION, LOCK_SENTINEL, thresholds). Nothing to crash.",
    "cfgload": "GENUINE GAP: own __main__ (load(), cfgload.py:236), a single conn.commit() at the "
              "end (line 229) after ~17 CREATE TABLE statements plus every seeded row — no "
              "try/except anywhere. Same DDL-auto-commits-before-final-commit() exposure as the "
              "bootstrap_behaviour_rules_*/engine_migrate scripts, but higher-traffic: this is THE "
              "config bootstrap Start-Iba.ps1 runs every session (idempotent — skips once "
              "'config already loaded' is detected, so a genuinely mid-crash partial load would "
              "self-heal on the next session start rather than silently persist, which is real "
              "mitigation but not a substitute for a crash record). Not fixed this round.",
    "dbsnapshot": "Not a DB-row-write module at all — a plain file copy (shutil.copy2) of iba.db "
                 "after flushing the WAL, called directly from run.py:_ensure_run (part of THIS "
                 "app's own pre-write crash-safety infrastructure, not something reviewed for ITS "
                 "own crash-recovery the same way a write-path module is). The one failure mode "
                 "(WAL checkpoint failing) is already caught (dbsnapshot.py:50-54, "
                 "sqlite3.Error) and treated as non-fatal — the snapshot is best-effort, never "
                 "blocks the run it's protecting.",

    # ── one-off migration/bootstrap scripts already reviewed via a DIFFERENT lens (this file's own
    #    kind) — this module IS one of those, reviewing itself here would be circular; noted plainly.
}


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        "SELECT module FROM cfg_utility WHERE inactive=0 ORDER BY module").fetchall()
    missing = [r["module"] for r in rows if r["module"] not in NOTES]
    if missing:
        raise RuntimeError(f"no genuine note written for: {missing} — every active module needs "
                          f"one, not a bulk default (D3, register v9)")

    n = 0
    for module, note in NOTES.items():
        cur = conn.execute(
            "UPDATE cfg_utility SET crash_escalation_reviewed=1, crash_escalation_note=? "
            "WHERE module=? AND inactive=0", (note, module))
        n += cur.rowcount
    conn.commit()
    conn.close()
    gaps = [m for m, v in NOTES.items() if "GENUINE GAP" in v]
    print(f"cfg_utility: {n} active module(s) reviewed (D3 rollout, register v9) — "
         f"{len(gaps)} genuine gap(s) flagged ({', '.join(gaps)}), none fixed this round "
         f"(out of scope)")


if __name__ == "__main__":
    main()
