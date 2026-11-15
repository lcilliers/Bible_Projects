"""layers_housekeeping_2505_v1_20261115.py -- escalation #2505 (researcher, 2026-11-15: "G10 - the concept process was part of prototyping. it was abandoned. it is replaced by the collections and
surface groups. G11 - there is a lot of house keeping to do around layer 1 and 2 - we are not moving forward until you have completed all the house keeping").

Writes (all cfg_* through configmaint.apply_logged, one run, one transaction):
  1. behaviour rule 119 keeps its enforcement status mechanically_enforced (the first migration of #2505 set it to partially_enforced; the resolver that enforces it did not change);
     the layers rule says that its layers are not the Layer 1 and Layer 2 of the verse_lexical build (the name collision);
  2. the stale `shared` flags of the member links (IndexCheck finding shared-flag-without-a-second-link, 274 on 2026-11-14): shared set to 0, each change a surface_event (action correct) with its reason;
  3. the concept prototype retired: its rows soft-deleted (concept 101, concept_subgroup 411, concept_domain 14), its tables and columns (and collection.concept_id) inactive in config, the Concept-Edit
     tool (work package, 4 steps with their routed conditions, 3 utilities, 7 write grants) inactive. The scripts move to their archive folders by the runner of this migration (the file paths here are the archive paths).
Idempotent. A named rollback snapshot is taken before a live apply.

Usage:
    python iba/app/migration/layers_housekeeping_2505_v1_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2505-LAYERS-HOUSEKEEPING-20261115"
MODULE = "layers_housekeeping_2505_v1_20261115"
REASON = ("#2505 housekeeping (researcher 2026-11-15): the flag says the term is a member of more than one collection, and it has no second live member link; set to 0 "
          "(IndexCheck finding shared-flag-without-a-second-link, collection-index-check-v1-20261114.md)")
CONCEPT_TABLES = ("concept", "concept_subgroup", "concept_domain")
CONCEPT_STEPS = ("concept_edit.list", "concept_edit.describe", "concept_edit.add_domain", "concept_edit.set_deleted")
CONCEPT_UTILITIES = {"Concept-Edit.ps1": "iba/app/ps/archive/Concept-Edit.ps1", "conceptedit": "iba/app/lib/archive/conceptedit.py", "handlers_conceptedit": "iba/app/handlers/archive/conceptedit.py"}
NAMING = "These are the layers of the collection reading; they are not the Layer 1 and Layer 2 of the verse_lexical build (lexical.enrich)."
UTILITY = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2505: housekeeping of layers 1 and 2; run_id {RUN_ID}.", 1,
           "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def stale_shared(conn, tiers):
    ph = ",".join("?" * len(tiers))
    out = []
    for lid, cid, tid, tier in conn.execute(f"SELECT id, collection_id, term_id, tier FROM collection_link WHERE deleted=0 AND shared=1 AND tier IN ({ph})", tiers).fetchall():
        n = conn.execute(f"SELECT count(*) FROM collection_link WHERE deleted=0 AND term_id=? AND tier IN ({ph})", [tid] + list(tiers)).fetchone()[0]
        if n < 2:
            out.append((lid, cid, tid, tier))
    return out


def plan(conn, tiers):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if conn.execute("SELECT enforcement_status FROM cfg_behaviour_rule WHERE id=119").fetchone()[0] != "mechanically_enforced":
        ops.append(("cfg_behaviour_rule", "update", {"id": 119}, {"enforcement_status": "mechanically_enforced"}))
    r = conn.execute("SELECT id, rule_text FROM cfg_behaviour_rule WHERE rule_key='collection-reading-runs-in-layers'").fetchone()
    if r and NAMING not in r[1]:
        ops.append(("cfg_behaviour_rule", "update", {"id": r[0]}, {"rule_text": r[1] + " " + NAMING}))
    for t in CONCEPT_TABLES:
        if has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=? AND inactive=0", t):
            ops.append(("cfg_table", "update", {"database": "iba", "name": t}, {"inactive": 1}))
        if has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND inactive=0", t):
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": t}, {"inactive": 1}))
    if has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='collection' AND name='concept_id' AND inactive=0"):
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "collection", "name": "concept_id"}, {"inactive": 1}))
    for w, t in conn.execute("SELECT writer, table_name FROM cfg_write_grant WHERE inactive=0 AND (table_name IN ('concept','concept_subgroup','concept_domain') AND writer!='migration' OR writer LIKE 'concept_edit.%')").fetchall():
        ops.append(("cfg_write_grant", "update", {"writer": w, "table_name": t, "database": "iba"}, {"inactive": 1}))
    for s in CONCEPT_STEPS:
        if has("SELECT 1 FROM cfg_on_fail WHERE step=? AND inactive=0", s):
            ops.append(("cfg_on_fail", "update", {"step": s}, {"inactive": 1}))
        if has("SELECT 1 FROM cfg_step WHERE step=? AND inactive=0", s):
            ops.append(("cfg_step", "update", {"step": s}, {"inactive": 1}))
    if has("SELECT 1 FROM cfg_work_package WHERE name='concept-edit' AND inactive=0"):
        ops.append(("cfg_work_package", "update", {"name": "concept-edit"}, {"inactive": 1}))
    for m, path in CONCEPT_UTILITIES.items():
        if has("SELECT 1 FROM cfg_utility WHERE module=? AND (inactive=0 OR file_path!=?)", m, path):
            ops.append(("cfg_utility", "update", {"module": m}, {"inactive": 1, "file_path": path}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", UTILITY[0]):
        ops.append(("cfg_utility", "insert", {}, {"module": UTILITY[0], "file_path": UTILITY[1], "purpose": UTILITY[3], "inactive": UTILITY[2], "config_exempt": UTILITY[4],
                                                  "config_exempt_reason": UTILITY[5], "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    tiers = list(cfg.setting("collection.member_tiers"))
    ops = plan(conn, tiers)
    flags = stale_shared(conn, tiers)
    live = {t: conn.execute(f"SELECT count(*) FROM {t} WHERE deleted=0").fetchone()[0] for t in CONCEPT_TABLES}
    print(f"predicted: {len(ops)} cfg write(s); {len(flags)} stale shared flags to reset; live concept rows to soft-delete {live}")
    if a.dry_run:
        return 0
    if not ops and not flags and not any(live.values()):
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2505-housekeeping', named=True)}")
    try:
        conn.execute("SAVEPOINT layers_housekeeping")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for lid, cid, tid, tier in flags:
            conn.execute("UPDATE collection_link SET shared=0, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE id=?", (RUN_ID, lid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES ('collection_link',?,'correct','shared','1','0','migration',?,?,'migration')",
                         (lid, REASON, RUN_ID))
        for t in CONCEPT_TABLES:
            conn.execute(f"UPDATE {t} SET deleted=1, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE deleted=0", (RUN_ID,))
        after = {t: conn.execute(f"SELECT count(*) FROM {t} WHERE deleted=0").fetchone()[0] for t in CONCEPT_TABLES}
        left = len(stale_shared(conn, tiers))
        if left or any(after.values()):
            raise RuntimeError(f"actual differs from predicted: stale flags left {left}, live concept rows {after}: rolled back")
        conn.execute("RELEASE layers_housekeeping")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO layers_housekeeping")
        conn.execute("RELEASE layers_housekeeping")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); {len(flags)} shared flags reset; concept rows soft-deleted {live}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
