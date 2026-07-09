"""Dissolve ORPHAN old-format VCGs via the v3_0 Phase-C.3 method.

A2 reframed: old-VCG dissolution is per-cluster Phase C work, NOT a programme-wide
soft-delete. 498 of the 567 active old VCGs belong to clusters (in-progress /
not-started / re-analysis) and are dissolved in place when each cluster runs
Phase C. The remnant = old VCGs whose terms are ALL excluded/uncluster (no term
in any real M-cluster) -> no cluster's Phase C will ever reach them. Those are
dissolved here, with the proper C.3 ops:

  1. verse_context.group_id = NULL   (detach affected vc rows; audited for reversal)
  2. verse_context_group.delete_flagged = 1   (soft-delete the VCG)
  3. vcg_term.delete_flagged = 1   (soft-delete its term links)

Orphan criterion: active, old-format group_code (^digits-digits), and 0 live
verse_context rows whose mti_term is in a real M-cluster.

DEFAULT IS DRY-RUN. Pass --apply. Single transaction. Audit -> research/investigations/.
"""
import argparse
import os
import re
import sqlite3

DB = "database/bible_research.db"
AUDIT = "research/investigations/orphan-old-vcg-dissolution-audit-20260601.md"
OLD_RE = re.compile(r"^\d+-\d+")
M_RE = re.compile(r"^M\d")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    cur = c.cursor()

    termcl = {r["id"]: r["cluster_code"] for r in cur.execute("SELECT id, cluster_code FROM mti_terms")}
    old_active = [r["id"] for r in cur.execute("SELECT id, group_code gc, COALESCE(delete_flagged,0) df FROM verse_context_group")
                  if r["gc"] and OLD_RE.match(r["gc"]) and r["df"] == 0]
    ph = ",".join("?" * len(old_active))

    # which old VCGs have ANY live verse_context term in a real M-cluster?
    has_m = set()
    vc_rows = {}  # group_id -> list of vc ids (live)
    for r in cur.execute(f"SELECT id, group_id g, mti_term_id mt FROM verse_context WHERE group_id IN ({ph}) AND COALESCE(delete_flagged,0)=0", old_active):
        vc_rows.setdefault(r["g"], []).append(r["id"])
        cc = termcl.get(r["mt"])
        if cc and M_RE.match(cc):
            has_m.add(r["g"])
    orphans = [g for g in old_active if g not in has_m]
    aff_vc = sum(len(vc_rows.get(g, [])) for g in orphans)

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: orphan old VCGs (no term in any M-cluster): {len(orphans)} | live verse_context to detach: {aff_vc}")

    # audit (vc_id, old group_id) for reversibility
    oph = ",".join("?" * len(orphans)) if orphans else "NULL"
    audit_rows = cur.execute(f"SELECT id vc_id, group_id g FROM verse_context WHERE group_id IN ({oph}) AND COALESCE(delete_flagged,0)=0", orphans).fetchall() if orphans else []
    L = ["# Orphan old-VCG dissolution audit", "",
         f"**Mode:** {'APPLY' if a.apply else 'DRY-RUN'} · 2026-06-01 · orphan VCGs: {len(orphans)} · verse_context detached: {aff_vc}",
         "Reversal: restore verse_context.group_id from this list; clear delete_flagged on the VCG + vcg_term ids.", "",
         "| verse_context.id | old group_id |", "|---|---|"]
    for r in audit_rows:
        L.append(f"| {r['vc_id']} | {r['g']} |")
    os.makedirs(os.path.dirname(AUDIT), exist_ok=True)
    with open(AUDIT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"audit: {AUDIT}")

    if not a.apply or not orphans:
        c.close(); return

    cur.execute("BEGIN")
    try:
        n_vc = cur.execute(f"UPDATE verse_context SET group_id=NULL WHERE group_id IN ({oph}) AND COALESCE(delete_flagged,0)=0", orphans).rowcount
        n_vcg = cur.execute(f"UPDATE verse_context_group SET delete_flagged=1 WHERE id IN ({oph})", orphans).rowcount
        n_vt = cur.execute(f"UPDATE vcg_term SET delete_flagged=1 WHERE vcg_id IN ({oph}) AND COALESCE(delete_flagged,0)=0", orphans).rowcount
        if n_vcg != len(orphans):
            c.rollback(); raise SystemExit(f"ABORT: VCG soft-delete {n_vcg} != {len(orphans)} — rolled back.")
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: detached {n_vc} verse_context (group_id NULL); soft-deleted {n_vcg} VCGs + {n_vt} vcg_term rows.")
    c.close()


if __name__ == "__main__":
    main()
