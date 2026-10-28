"""verse_lexical_multi_code_span_surface_2326_v1_20261028.py -- escalation #2326: the surface of a code in a multi-code span.

Researcher, chat 2026-10-28 (verbatim): "the surface for H5750 on the verse is wrong. according to STEP it is 'still' not alive. I have
noticed that you regularly have the wrong surface for multi-span items"; then "Correct them" (verse_lexical itself, for the occurrences
where the code's own surface differs from the span's word).

STEP tags one span with all the codes aligned to a rendering unit and leaves some English untagged, so the build wrote the span's word
as the surface of every code of it. iba/app/lib/lexical.py `span_code_surfaces` now gives a code that is not a particle and whose STEP
gloss (strong.stepGloss) is a single word the untagged English word just before the span that is exactly that gloss; the build
(`build_for_verse`) uses it for every later build. This migration brings the rows already built to the same surface:
- verse_lexical.surface and gloss_consistent_in_verse of each occurrence that differs, in place (identity-stable, #1520: the id stays,
  so nodes and notes that name it still do);
- ib_node.surface of the nodes that name such an occurrence and hold the old surface, each change kept in ib_observation_change;
- reading_strand_hit.surface of the strand hits keyed on the old surface (verse, Strong, surface);
- NOT the occurrences of an M-coded code whose new (code, surface) pair is not in surface_subgroup: changing them would leave a pair
  unallocated, and a cluster with an unallocated pair is not read until it is allocated (rule 118). They are listed in the record
  and left as they are until the pairs are allocated.
Every old and new value is written to outputs/escalation/2326-verse-lexical-surface-changes-v1-20261028.tsv (the way back). The
database is copied first with the backup API (never a plain file copy: the WAL).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/verse_lexical_multi_code_span_surface_2326_v1_20261028.py [--db PATH] [--dry-run]
"""
import argparse
import collections
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import lexical  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2326-MULTI-CODE-SPAN-SURFACE-20261028"
MODULE = "verse_lexical_multi_code_span_surface_2326_v1_20261028"
RECORD = ROOT / "outputs/escalation/2326-verse-lexical-surface-changes-v1-20261028.tsv"
BACKUP = ROOT / "backups/iba-pre-2326-surface-20261028.db"


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn):
    """[(verse_lexical id, verse_id, strong, old surface, new surface)] to change, and the held ones."""
    mcoded = {r[0] for r in conn.execute("SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%'")}
    pairs = collections.defaultdict(set)
    for s, surf in conn.execute("SELECT strong, surface FROM surface_subgroup WHERE deleted=0"):
        pairs[s].add((surf or "").strip().lower())
    change, held = [], []
    vids = [r[0] for r in conn.execute("SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0")]
    for vid in vids:
        spans = [dict(r) for r in conn.execute("SELECT id, position, surface, strong_variant FROM span WHERE verse_id=? AND deleted=0 "
                                               "ORDER BY position", (vid,))]
        surf = lexical.span_code_surfaces(conn, vid, spans)
        if not surf:
            continue
        for (span_id, ordinal), new in surf.items():
            r = conn.execute("SELECT id, strong, surface FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0",
                             (span_id, ordinal)).fetchone()
            if r is None or r["surface"] == new:
                continue
            row = (r["id"], vid, r["strong"], r["surface"], new)
            if r["strong"] in mcoded and new.lower() not in pairs[r["strong"]]:
                held.append(row)
            else:
                change.append(row)
    return change, held


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    change, held = plan(conn)
    ids = [c[0] for c in change]
    nodes = conn.execute("SELECT count(*) FROM ib_node n JOIN verse_lexical vl ON vl.id=n.verse_lexical_id WHERE n.verse_lexical_id IN "
                         f"({','.join(str(i) for i in ids) or 'NULL'}) AND n.surface=vl.surface").fetchone()[0]
    if a.dry_run:
        print(f"DRY RUN -- {len(change)} occurrence(s) in {len({c[1] for c in change})} verse(s) to change, {len(held)} held "
              f"(M-coded, new pair not allocated), {nodes} node(s) to follow; nothing written")
        return 0
    if a.db == DEFAULT_DB:
        BACKUP.parent.mkdir(exist_ok=True)
        if not BACKUP.exists():
            conn.commit()
            copy_db(BACKUP, pathlib.Path(a.db))
    stamp = now()
    lines = ["kind\tid\tverse_id\tstrong\told_value\tnew_value"]
    n_nodes = n_hits = 0
    with conn:
        for (vlid, vid, strong, old, new) in change:
            conn.execute("UPDATE verse_lexical SET surface=?, updated_at=? WHERE id=?", (new, stamp, vlid))
            lines.append(f"verse_lexical\t{vlid}\t{vid}\t{strong}\t{old}\t{new}")
            for nd in conn.execute("SELECT id, observation_id FROM ib_node WHERE verse_lexical_id=? AND surface=?", (vlid, old)).fetchall():
                conn.execute("UPDATE ib_node SET surface=? WHERE id=?", (new, nd["id"]))
                conn.execute("INSERT INTO ib_observation_change (observation_id, node_id, column_name, old_value, new_value, reason, "
                             "reading_id, run_id, created_by) VALUES (?,?,?,?,?,?,NULL,?,?)",
                             (nd["observation_id"], nd["id"], "surface", old, new,
                              "the surface of this code in a multi-code span is its own STEP gloss, not the span's word (#2326)",
                              RUN_ID, "Claude"))
                lines.append(f"ib_node\t{nd['id']}\t{vid}\t{strong}\t{old}\t{new}")
                n_nodes += 1
            for h in conn.execute("SELECT id FROM reading_strand_hit WHERE verse_id=? AND strong=? AND surface=?",
                                  (vid, strong, old)).fetchall():
                conn.execute("UPDATE reading_strand_hit SET surface=? WHERE id=?", (new, h["id"]))
                lines.append(f"reading_strand_hit\t{h['id']}\t{vid}\t{strong}\t{old}\t{new}")
                n_hits += 1
        # gloss_consistent_in_verse needs the whole verse's rows (keyed on surface): recomputed for the verses touched
        for vid in sorted({c[1] for c in change}):
            rows = [dict(r) for r in conn.execute("SELECT id, strong, morph_code, surface, gloss_consistent_in_verse FROM verse_lexical "
                                                   "WHERE verse_id=? AND deleted=0", (vid,))]
            keep = {r["id"]: r["gloss_consistent_in_verse"] for r in rows}
            lexical._apply_gloss_consistency(rows)
            for r in rows:
                if r["gloss_consistent_in_verse"] != keep[r["id"]]:
                    conn.execute("UPDATE verse_lexical SET gloss_consistent_in_verse=?, updated_at=? WHERE id=?",
                                 (r["gloss_consistent_in_verse"], stamp, r["id"]))
                    lines.append(f"verse_lexical.gloss_consistent_in_verse\t{r['id']}\t{vid}\t{r['strong']}\t{keep[r['id']]}\t"
                                 f"{r['gloss_consistent_in_verse']}")
        for (vlid, vid, strong, old, new) in held:
            lines.append(f"HELD (new pair not in surface_subgroup)\t{vlid}\t{vid}\t{strong}\t{old}\t{new}")
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
                "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
                "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                        "as the other Developer Mode migrations",
                "purpose": f"ONE-OFF migration -- escalation #2326: verse_lexical.surface of a code in a multi-code span set to its "
                           f"own STEP gloss; run_id {RUN_ID}. inactive=1 once applied."})
    record = RECORD if a.db == DEFAULT_DB else pathlib.Path(a.db).with_suffix(".surface-changes.tsv")      # a test copy never writes the real record
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(chr(10).join(lines) + chr(10), encoding="utf-8")
    print(f"{len(change)} occurrence(s) changed in {len({c[1] for c in change})} verse(s); {n_nodes} node(s) and {n_hits} strand hit(s) "
          f"followed; {len(held)} held (M-coded, new pair not allocated); record {record}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
