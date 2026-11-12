"""link_group_b_surfaces_to_collections_2488_v1_20261112.py -- escalation #2488, Part A group B.

The researcher (2026-11-12, verbatim on #2488): the group B surfaces (behaviour or inner_being_state, linked to a collection only as associated, set_aside or
possible_opposite) are linked to the collections suggested in the workbook _analytics/surfaces/exports/study-surfaces-group-b-subgroup-fellows-v2-20261112.xlsx, sheet
'One row per surface' (the collection holding most of the member fellows of the surface's cluster subgroups); the tier is gathered; "the few remaining can be allocated to the
unassigned collection" (read as collection 'uncovered-words', the gathered collection of the 85 words in no collection).
For each surface of the sheet, in one transaction:
  - no live link of that term to that collection: a new link, tier gathered;
  - a live link of tier associated to that collection: superseded (the old link deleted=1, the new one gathered, superseded_by_id set), as collectionbuild.write does;
  - a live link of tier set_aside or possible_opposite to that collection: HELD, nothing written (an earlier judgement of the same pair), listed for the researcher;
  - surface_term.collection_state becomes placed (as Gather does), and a surface_event row (action set_tier) records the change.
The run stops and rolls back unless the counts equal the prediction taken first. Idempotent: a second run finds the pair already gathered and writes nothing.
    python iba/app/migration/link_group_b_surfaces_to_collections_2488_v1_20261112.py [--db PATH] [--dry-run]
"""
import argparse
import csv
import datetime
import pathlib
import sqlite3
import sys

import openpyxl

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
XLSX = ROOT / "_analytics" / "surfaces" / "exports" / "study-surfaces-group-b-subgroup-fellows-v2-20261112.xlsx"
LOG = ROOT / "outputs" / "escalation" / "2488-group-b-links-v1-20261112.tsv"
RUN_ID = "DEVMODE-2488-GROUP-B-LINKS-20261112"
BY = "devmode-2488"
UNASSIGNED = "uncovered-words"
REASON = ("Researcher 2026-11-12 (#2488): link the group B surfaces to the collections suggested by their cluster-subgroup fellows, tier gathered; "
          "those with no suggestion to the unassigned collection (uncovered-words)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    one = lambda s, *p: conn.execute(s, p).fetchone()[0]
    cid = {}
    for i, n in conn.execute("SELECT id, name FROM collection WHERE deleted=0"):
        if n in cid:
            raise SystemExit("collection name used twice: %r" % n)
        cid[n] = i
    ws = openpyxl.load_workbook(XLSX, read_only=True)["One row per surface"]
    rows = list(ws.iter_rows(values_only=True))[1:]
    plan = []   # (term, surface, collection id, collection name, existing link id or None, existing tier or None, action)
    for r in rows:
        term, surf, sug = r[0], r[1], r[3]
        name = sug or UNASSIGNED
        if name not in cid:
            raise SystemExit("unknown collection %r for %r" % (name, surf))
        ex = conn.execute("SELECT id, tier FROM collection_link WHERE deleted=0 AND term_id=? AND collection_id=?", (term, cid[name])).fetchone()
        if ex is None: act = "add"
        elif ex[1] == "gathered": act = "already"
        elif ex[1] == "associated": act = "supersede"
        elif ex[1] in ("set_aside", "possible_opposite"): act = "hold"
        else: act = "hold"
        plan.append((term, surf, cid[name], name, ex[0] if ex else None, ex[1] if ex else None, act))
    n = lambda act: sum(1 for p in plan if p[6] == act)
    live0 = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    pred = dict(rows=len(plan), add=n("add"), supersede=n("supersede"), hold=n("hold"), already=n("already"),
                live_after=live0 + n("add"), placed_added=n("add") + n("supersede"))
    print("predicted:", pred)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT g")
    try:
        done = dict(add=0, supersede=0)
        for term, surf, col, cname, old, oldtier, act in plan:
            if act in ("hold", "already"):
                continue
            if act == "supersede":
                conn.execute("UPDATE collection_link SET deleted=1, updated_at=?, run_id=? WHERE id=?", (now, RUN_ID, old))
            cur = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, shared, reason, run_id, created_by) VALUES (?,?,'gathered',0,?,?,?)",
                               (col, term, REASON, RUN_ID, BY))
            if act == "supersede":
                conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (cur.lastrowid, old))
            conn.execute("UPDATE surface_term SET collection_state='placed', updated_at=?, run_id=? WHERE id=?", (now, RUN_ID, term))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES ('surface_term',?,'set_tier','collection_link',?,?,?,?,?,?)",
                         (term, ("%s: %s" % (cname, oldtier)) if oldtier else None, "%s: gathered" % cname, BY, REASON, RUN_ID, BY))
            done[act] += 1
        got = dict(rows=len(plan), add=done["add"], supersede=done["supersede"], hold=n("hold"), already=n("already"),
                   live_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"),
                   placed_added=done["add"] + done["supersede"])
        dup = one("SELECT count(*) FROM (SELECT collection_id, term_id FROM collection_link WHERE deleted=0 GROUP BY 1,2 HAVING count(*)>1)")
        print("actual:   ", got, "| pairs with two live links:", dup)
        if got != pred or dup:
            raise RuntimeError("actual differs from predicted: rolled back")
        if a.dry_run:
            conn.execute("ROLLBACK TO g"); print("dry run: rolled back")
        else:
            LOG.parent.mkdir(parents=True, exist_ok=True)
            with open(LOG, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f, delimiter="\t"); w.writerow(["surface_term id", "surface", "collection", "existing tier", "action"])
                for term, surf, col, cname, old, oldtier, act in plan: w.writerow([term, surf, cname, oldtier or "", act])
            conn.execute("RELEASE g"); conn.commit(); print("committed; log", LOG)
    except Exception:
        conn.execute("ROLLBACK TO g"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
