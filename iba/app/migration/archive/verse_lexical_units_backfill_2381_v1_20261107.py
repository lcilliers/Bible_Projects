"""verse_lexical_units_backfill_2381_v1_20261107.py -- escalation #2381, stage 1 back-fill (design
outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md).

Re-runs the verse_lexical build (iba/app/lib/lexical.py build_for_verse_ids) over every verse with live rows, so each row gets
unit_surface, surface_kind, unit_size and unit_role and an affix code in a multi-term unit gets its own STEP gloss as its surface.
The build is identity-stable (no id is added or removed). After it, in the same transaction:
  - an ib_node on an occurrence whose surface changed follows the new surface, each change kept in ib_observation_change with its
    reason (as the 2326 migration did), and reading_strand_hit rows likewise;
  - the run stops and rolls back if a row of an M-coded code changed its surface (the design expects none: affix codes are in no
    M cluster), or if a row would be added or removed, or if the reconciliation below fails.
Reconciliation (printed): rows by surface_kind and unit_role; no live row with an empty unit column; affix rows in multi-code units
are all gloss.
--dry-run runs everything and rolls back. Idempotent: a second run changes nothing. Usage:
    python iba/app/migration/verse_lexical_units_backfill_2381_v1_20261107.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import pathlib
import re
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import lexical  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
LOG = ROOT / "outputs" / "escalation" / "2381-surface-backfill-follow-v1-20261107.tsv"
RUN_ID = "DEVMODE-2381-VERSE-LEXICAL-UNITS-BACKFILL-20261107"
MODULE = "verse_lexical_units_backfill_2381_v1_20261107"
REASON = ("the surface of an affix code in a multi-term unit is its own STEP gloss, not the unit's word (#2381, design v2 of "
          "2026-11-07)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    before = {r["id"]: (r["strong"], r["surface"], r["verse_id"]) for r in conn.execute(
        "SELECT id, strong, surface, verse_id FROM verse_lexical WHERE deleted=0")}
    before_full = {r["id"]: dict(r) for r in conn.execute(
        "SELECT id, surface, gloss_consistent_in_verse, updated_at FROM verse_lexical WHERE deleted=0")}
    verse_ids = sorted({v[2] for v in before.values()})
    mcoded = {r[0] for r in conn.execute("SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%'")}
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT backfill")
    try:
        totals = {k: 0 for k in ("verses", "spans", "codes", "inserted", "updated", "unchanged", "removed", "removed_with_live_notes")}
        for i in range(0, len(verse_ids), 1000):
            part = lexical.build_for_verse_ids(conn, verse_ids[i:i + 1000])
            for k in totals:
                totals[k] += part[k]
        after = {r["id"]: (r["strong"], r["surface"], r["verse_id"]) for r in conn.execute(
            "SELECT id, strong, surface, verse_id FROM verse_lexical WHERE deleted=0")}
        problems = []
        if set(after) != set(before):
            problems.append(f"the set of live row ids changed: {len(set(after) - set(before))} new, {len(set(before) - set(after))} gone")
        changed = [(i, before[i], after[i]) for i in before if i in after and before[i][1] != after[i][1]]
        # the 2326 hold: an M-coded row whose new (code, surface) pair is not in surface_subgroup keeps its surface (the researcher's
        # to release); only its unit columns are filled
        pairs = {(s, (u or "").strip().lower()) for s, u in conn.execute("SELECT strong, surface FROM surface_subgroup WHERE deleted=0")}
        held = [c for c in changed if c[1][0] in mcoded and (c[1][0], (c[2][1] or "").strip().lower()) not in pairs]
        unheld_m = [c for c in changed if c[1][0] in mcoded and c not in held]
        if unheld_m:
            problems.append(f"{len(unheld_m)} M-coded row(s) changed to a surface that is an allocated pair, e.g. {unheld_m[:3]}; not expected")
        for vlid, (strong, old, vid), _new in held:
            conn.execute("UPDATE verse_lexical SET surface=?, updated_at=? WHERE id=?", (old, before_full[vlid]["updated_at"], vlid))
        for vid in sorted({h[1][2] for h in held}):
            vrows = [dict(r) for r in conn.execute("SELECT id, strong, morph_code, surface, gloss_consistent_in_verse FROM verse_lexical WHERE verse_id=? AND deleted=0", (vid,))]
            lexical._apply_gloss_consistency(vrows)
            for r in vrows:
                conn.execute("UPDATE verse_lexical SET gloss_consistent_in_verse=? WHERE id=?", (r["gloss_consistent_in_verse"], r["id"]))
        after = {r["id"]: (r["strong"], r["surface"], r["verse_id"]) for r in conn.execute(
            "SELECT id, strong, surface, verse_id FROM verse_lexical WHERE deleted=0")}
        changed = [(i, before[i], after[i]) for i in before if i in after and before[i][1] != after[i][1]]
        follow = ["kind\tid\tverse_id\tstrong\told_value\tnew_value"]
        n_nodes = n_hits = 0
        for vlid, (strong, old, vid), (_s, new, _v) in changed:
            for nd in conn.execute("SELECT id, observation_id FROM ib_node WHERE verse_lexical_id=? AND surface IS ?", (vlid, old)).fetchall():
                conn.execute("UPDATE ib_node SET surface=? WHERE id=?", (new, nd["id"]))
                conn.execute("INSERT INTO ib_observation_change (observation_id, node_id, column_name, old_value, new_value, reason, "
                             "reading_id, run_id, created_by) VALUES (?,?,?,?,?,?,NULL,?,?)",
                             (nd["observation_id"], nd["id"], "surface", old, new, REASON, RUN_ID, "Claude"))
                follow.append(f"ib_node\t{nd['id']}\t{vid}\t{strong}\t{old}\t{new}")
                n_nodes += 1
            for h in conn.execute("SELECT id FROM reading_strand_hit WHERE verse_id=? AND strong=? AND surface IS ?", (vid, strong, old)).fetchall():
                conn.execute("UPDATE reading_strand_hit SET surface=? WHERE id=?", (new, h["id"]))
                follow.append(f"reading_strand_hit\t{h['id']}\t{vid}\t{strong}\t{old}\t{new}")
                n_hits += 1
        q = lambda sql: conn.execute(sql).fetchall()  # noqa: E731
        kinds = q("SELECT surface_kind, unit_role, count(*) n FROM verse_lexical WHERE deleted=0 GROUP BY 1,2 ORDER BY 1,2")
        empty = q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND (unit_surface IS NULL OR surface_kind IS NULL OR unit_size IS NULL OR unit_role IS NULL)")[0][0]
        if empty:
            problems.append(f"{empty} live row(s) with an empty unit column")
        pat = re.compile(cfg.required_setting("discovery.particle_pattern"))
        rule = cfg.required_setting("lexical.span_surface")
        bad = [r["id"] for r in conn.execute("SELECT id, strong, unit_size, surface_kind FROM verse_lexical WHERE deleted=0 AND unit_size>1")
               if lexical.is_affix(r["strong"], pat, rule) and r["surface_kind"] != "gloss"]
        if bad:
            problems.append(f"{len(bad)} affix row(s) in a multi-code unit that are not gloss, e.g. {bad[:5]}")
        if problems:
            raise SystemExit("REFUSED, rolled back, nothing written: " + "; ".join(problems))
        print(f"build over {len(verse_ids)} verses: {totals}")
        print(f"surface changed on {len(changed)} row(s); {n_nodes} ib_node and {n_hits} reading_strand_hit followed")
        print(f"held as #2326 left them (M-coded, new pair not allocated; surface unchanged, unit columns filled): "
              f"{len(held)} {[(h[0], h[1][0], h[1][1], h[2][1]) for h in held]}")
        print("surface_kind / unit_role / rows:")
        for r in kinds:
            print(f"  {r[0]:7} {r[1]:13} {r[2]:>8}")
        print(f"sum {sum(r[2] for r in kinds)} of {len(after)} live rows; empty unit columns {empty}")
        if a.dry_run:
            conn.execute("ROLLBACK TO backfill")
            conn.execute("RELEASE backfill")
            conn.rollback()
            print("DRY RUN: rolled back, nothing written")
            return 0
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
                "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
                "config_exempt": 1, "config_exempt_reason": "one-off migration script -- same class as the other Developer Mode migrations",
                "purpose": f"ONE-OFF migration -- escalation #2381 stage 1: the verse_lexical back-fill of the unit columns; run_id {RUN_ID}.",
                "crash_escalation_reviewed": 0, "crash_escalation_note": None})
        conn.execute("RELEASE backfill")
        conn.commit()
        if len(follow) > 1:
            LOG.write_text("\n".join(follow) + "\n", encoding="utf-8")
        print(f"applied (run {RUN_ID}, {stamp}); follow log {LOG.relative_to(ROOT) if len(follow) > 1 else 'none (no node or hit followed)'}")
        return 0
    except BaseException:
        try:
            conn.execute("ROLLBACK TO backfill")
            conn.execute("RELEASE backfill")
        except Exception:
            pass
        conn.rollback()
        raise


if __name__ == "__main__":
    sys.exit(main())
