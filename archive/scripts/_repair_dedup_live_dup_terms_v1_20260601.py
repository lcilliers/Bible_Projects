"""Action 4b: soft-delete the empty duplicate mti_terms rows of the 55 live-dup strongs.

For each strongs with >1 live (delete_flagged=0) row: keep the canonical row
(most attachments; tie-break extracted-status then MIN id), soft-delete the others.
SAFETY ASSERT: every row to be soft-deleted must have ZERO attachments
(verse_context + vcg_term + mti_term_subgroup = 0). If any non-canonical row
carries attachments, ABORT (would orphan data). Same-cluster confirmed, so no
cluster judgement. Soft-delete only (reversible); no FK repointing needed.

DEFAULT IS DRY-RUN. Pass --apply. Single transaction, post-state asserted.
"""
import argparse
import sqlite3
from collections import defaultdict

DB = "database/bible_research.db"
EXTRACTED = ("extracted", "extracted_thin", "extracted_theological_anchor")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    cur = c.cursor()

    live = defaultdict(list)
    for r in cur.execute("SELECT id, strongs_number sn, COALESCE(status,'') st, cluster_code cc FROM mti_terms WHERE COALESCE(delete_flagged,0)=0"):
        live[r["sn"]].append(r)
    dups = {sn: rows for sn, rows in live.items() if len(rows) > 1}

    def attach(tid):
        v = cur.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        g = cur.execute("SELECT COUNT(*) FROM vcg_term WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        s = cur.execute("SELECT COUNT(*) FROM mti_term_subgroup WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
        return v + g + s

    to_delete = []  # (id, sn, canonical_id)
    for sn, rows in dups.items():
        att = {r["id"]: attach(r["id"]) for r in rows}
        canon = max(rows, key=lambda r: (att[r["id"]], 1 if r["st"] in EXTRACTED else 0, -r["id"]))
        for r in rows:
            if r["id"] == canon["id"]:
                continue
            if att[r["id"]] != 0:
                raise SystemExit(f"ABORT: {sn} non-canonical row id={r['id']} has {att[r['id']]} attachments — would orphan. Halting.")
            to_delete.append((r["id"], sn, canon["id"]))

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: live-dup strongs={len(dups)} | empty rows to soft-delete={len(to_delete)}")
    if not a.apply:
        for rid, sn, canon in to_delete[:12]:
            print(f"  soft-delete id={rid} ({sn}); canonical id={canon}")
        c.close(); return

    cur.execute("BEGIN")
    try:
        n = 0
        for rid, sn, canon in to_delete:
            cur.execute("UPDATE mti_terms SET delete_flagged=1, exclusion_reason=?, last_changed=datetime('now') WHERE id=? AND COALESCE(delete_flagged,0)=0",
                        (f"Live-dup dedup 2026-06-01: empty duplicate row of {sn}; canonical id={canon}.", rid))
            n += cur.rowcount
        if n != len(to_delete):
            c.rollback(); raise SystemExit(f"ABORT: updated {n} != {len(to_delete)} — rolled back.")
        # post-state: each formerly-dup strongs now has exactly 1 live row
        bad = []
        for sn in dups:
            live_now = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0", (sn,)).fetchone()[0]
            if live_now != 1:
                bad.append((sn, live_now))
        if bad:
            c.rollback(); raise SystemExit(f"ABORT: post-state not 1 live row for {bad[:5]} — rolled back.")
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: soft-deleted {n} empty duplicate rows; each of the {len(dups)} strongs now has exactly 1 live row.")
    c.close()


if __name__ == "__main__":
    main()
