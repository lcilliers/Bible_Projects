"""Layer 1 (`verse_lexical`) rebuild — dissolve the old configuration, set the new one, prepare
for the full corpus-wide rebuild. Escalation #1706 Phase B (items 1-9), #1607 (D1/D3/D4), #1706
build session, 2026-09-16.

Researcher, verbatim, 2026-09-15: "the current lexical records will all be dumped. layer 1 has
materially changed and the table schema changed. your proposal must include the steps to desolve
the old lexical configuration, and set the new configuration. layer 1 will be processed in bulk to
produce fresh results for the entire corpus. I am no longer interested to try and reconcile old
data, and the discrepancies in the old data is not going to be 'fixed'."

**What this migration does, in order:**
1. Drops `verse_lexical.resolved_sense`, `.ambiguity_note`, `.language` (real schema change, not a
   cfg_column inactive flag — matches the project's own `drop_verse_meta_genre_column` precedent).
2. Deletes the 3 dropped columns' `cfg_column` rows (a row describing a column that no longer
   physically exists is itself a coherence-check violation, same lesson as CA-7's own mirror case).
3. Rewrites `role`'s `cfg_column.use` text for its new meaning (JSON array of cluster_strong.
   cluster_code, not the old content/function classifier — #1590's bug is retired-by-design, not
   patched).
4. Fixes `gloss_consistent_in_verse`'s `cfg_column.use` text — it already says "resolved_sense" but
   the actual check has been keyed on `surface` since escalation #1527 (2026-09-06); found stale
   while doing this migration, corrected in the same unit of work rather than left for later.
5. Rewrites `verse_meta_on_lexical_change` (the trigger that rolls verse_lexical rows up into
   verse_meta.language) to source language via `strong.language` (joined through
   `verse_lexical.strong`) instead of reading the now-dropped `verse_lexical.language` directly —
   same majority-vote logic, different source column.
6. Soft-deletes every currently-live `verse_lexical` row (`deleted=1`) — the full-rebuild
   precondition. THE REBUILD ITSELF IS NOT RUN BY THIS SCRIPT — run it separately afterward via
   `lexical.build`/`lexical.run` (or the corpus-wide driver script), so this migration's own
   before/after counts stay legible.
7. Marks `lexical.enrich` (cfg_step) inactive — its whole mechanism (`verse_lexical_note`) is
   superseded by the new `ib_observation` architecture (#1597 resolution-by-architecture,
   #1691/#1692 design-complete). Not deleted — the code stays (its LLM-calling infrastructure,
   `lexicalenrichgenerate.py`, is being adapted for the new Layer 2 `verse_meaning` stage, #1711),
   just flagged as no longer the live mechanism.

Safe to re-run: every step is guarded, no-ops if already applied. NOT safe to run twice with real
rebuild work in between and expect a clean re-soft-delete of only "old" rows — this is a one-time
cutover script, run once before the corpus-wide rebuild starts.

Usage:
    python iba/app/migration/rebuild_verse_lexical_layer1_v1_20260916.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

_NEW_TRIGGER_SQL = """
            CREATE TRIGGER verse_meta_on_lexical_change
            AFTER INSERT ON verse_lexical
            WHEN NEW.deleted = 0 AND NEW.strong IS NOT NULL
            BEGIN
                UPDATE verse_meta SET
                    language = (
                        SELECT s.language FROM verse_lexical vl
                        JOIN strong s ON s.strongNumber = vl.strong
                        WHERE vl.verse_id = NEW.verse_id AND vl.deleted = 0
                        AND s.language IS NOT NULL
                        GROUP BY s.language ORDER BY COUNT(*) DESC, s.language LIMIT 1
                    ),
                    updated_at = strftime('%Y-%m-%dT%H:%M:%SZ','now')
                WHERE verse_id = NEW.verse_id;
            END
"""


def column_exists(cur, table: str, col: str) -> bool:
    return any(r[1] == col for r in cur.execute(f"PRAGMA table_info({table})"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        # 5 (moved first — SQLite refuses to DROP COLUMN while a trigger still references it,
        #    "error in trigger verse_meta_on_lexical_change after drop column: no such column:
        #    NEW.language", found live running this migration). Rewrite the trigger BEFORE
        #    dropping verse_lexical.language.
        existing_trigger = cur.execute(
            "SELECT sql FROM sqlite_master WHERE type='trigger' AND "
            "name='verse_meta_on_lexical_change'").fetchone()
        if existing_trigger and "s.language" in (existing_trigger[0] or ""):
            report.append("trigger verse_meta_on_lexical_change already rewritten — skipped")
        else:
            cur.execute("DROP TRIGGER IF EXISTS verse_meta_on_lexical_change")
            cur.execute(_NEW_TRIGGER_SQL)
            report.append("trigger verse_meta_on_lexical_change rewritten "
                          "(sources language via strong.language, not the dropped "
                          "verse_lexical.language)")

        # 1. Drop the 3 columns.
        for col in ("resolved_sense", "ambiguity_note", "language"):
            if column_exists(cur, "verse_lexical", col):
                cur.execute(f"ALTER TABLE verse_lexical DROP COLUMN {col}")
                report.append(f"DROPPED verse_lexical.{col}")
            else:
                report.append(f"verse_lexical.{col} already absent — skipped")

        # 2. Delete their cfg_column rows.
        for col in ("resolved_sense", "ambiguity_note", "language"):
            deleted = cur.execute(
                "DELETE FROM cfg_column WHERE database='iba' AND table_name='verse_lexical' "
                "AND name=?", (col,)).rowcount
            report.append(f"cfg_column verse_lexical.{col} row deleted ({deleted} row)")

        # 3. Rewrite role's cfg_column.use.
        cur.execute(
            "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='verse_lexical' "
            "AND name='role'",
            ("REDESIGNED 2026-09-16 (#1706 Phase B item 3, #1607 D1/D4) — bare JSON array of "
             "every live cluster_strong.cluster_code for this strong (T-codes AND M-codes, e.g. "
             "'[\"T5\",\"M12\"]'), not an array of objects. Replaces the old content/function "
             "morph-tag classifier (escalation #1590's bug — Greek article tag 'T' misclassified "
             "content instead of function — is retired-by-design, not patched: the whole "
             "classify_role() mechanism is deleted, not fixed). Also the base-data readiness "
             "signal itself (#1606 D1): an empty array means zero cluster_strong allocation, the "
             "exact FATAL condition `lexical.readiness` Leg 3 and the pre-run "
             "unready_codes_in_scope() validator both check for.",))
        report.append("cfg_column verse_lexical.role use text rewritten")

        # 4. Fix gloss_consistent_in_verse's stale use text (found live doing this migration —
        #    the check has been keyed on `surface`, not `resolved_sense`, since escalation #1527,
        #    2026-09-06; the cfg_column row was never updated to match. Corrected here, same unit
        #    of work, not left for a separate pass.)
        cur.execute(
            "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='verse_lexical' "
            "AND name='gloss_consistent_in_verse'",
            ("1 unless this (strong, morph_code) pair carries >1 distinct SURFACE value among "
             "this verse's own rows — mechanical data-quality check. CORRECTED 2026-09-16 (#1706 "
             "Phase B migration): this row previously said 'resolved_sense', stale since "
             "escalation #1527 (2026-09-06) rekeyed the actual check to `surface` — "
             "resolved_sense is a pure function of (strong, morph_code) with no per-occurrence "
             "signal, so a same-code-different-sense check against it could never fire; `surface` "
             "(the aligned translation word) genuinely does vary by occurrence.",))
        report.append("cfg_column verse_lexical.gloss_consistent_in_verse use text corrected "
                      "(was stale since 2026-09-06)")

        # 6. Soft-delete every current verse_lexical row — the full-rebuild precondition.
        #    "Dumped" = soft-delete, already explicitly instructed 2026-09-09/10 (#1706 doc's own
        #    correction record) — not a hard delete.
        live_before = cur.execute(
            "SELECT COUNT(*) FROM verse_lexical WHERE deleted=0").fetchone()[0]
        if live_before:
            cur.execute("UPDATE verse_lexical SET deleted=1 WHERE deleted=0")
            report.append(f"soft-deleted {live_before} live verse_lexical row(s) "
                          f"— rebuild precondition")
        else:
            report.append("no live verse_lexical rows to soft-delete — already clean")

        # 7. Retire lexical.enrich (superseded by ib_observation, not deleted).
        step_row = cur.execute(
            "SELECT inactive FROM cfg_step WHERE step='lexical.enrich'").fetchone()
        if step_row and step_row[0] == 0:
            cur.execute(
                "UPDATE cfg_step SET inactive=1, does=does || ' RETIRED 2026-09-16 (#1706 Phase "
                "B): this verse_lexical_note-based mechanism is superseded by the new "
                "ib_observation architecture (#1597 resolution-by-architecture, #1691/#1692 "
                "design-complete). Code kept, not deleted — lexicalenrichgenerate.py''s "
                "LLM-calling infrastructure is being adapted for the new Layer 2 verse_meaning "
                "stage (#1711), not thrown away.' WHERE step='lexical.enrich'")
            report.append("cfg_step lexical.enrich marked inactive (superseded, code retained)")
        else:
            report.append("cfg_step lexical.enrich already inactive or absent — skipped")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
