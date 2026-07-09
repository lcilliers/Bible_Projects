"""Set aside the genuinely-orphaned Session B/D pointers as non-evidenced.

Researcher direction 2026-06-01: set aside the 30 orphaned findings + 72 orphaned
flags. 'Orphaned' = NO linkage route at all (recomputed here with the exact logic
of inspect_pointer_full_linkage_v1_20260601.py, so the target set is precise).

Disposition (NOT a delete — set aside, record preserved):
  - wa_session_b_findings : status='set_aside_non_evidenced' + resolution_note
  - wa_session_research_flags (pointer codes): resolved=1 + resolved_date + resolved_note

DEFAULT IS DRY-RUN. Pass --apply to write. Single transaction, rowcount asserted.
"""
import argparse
import re
import sqlite3

DB = "database/bible_research.db"
VERSE_RE = re.compile(r"\b([1-3]?\s?[A-Z][a-zA-Z]{1,4})\.?\s+(\d{1,3}):(\d{1,3})")
FLAG_CODES = ("SD_POINTER", "SB_FINDING", "SB_INNER_BEING", "SD_CLUSTER")
REASON_F = "Set aside non-evidenced 2026-06-01: no linkage route (no cluster_link / tier-question / verse / Session C / SD-ref)."
REASON_FL = "Set aside non-evidenced 2026-06-01: no linkage route (no cluster_link / strongs-ref / verse / prose-citation)."


def hasverse(*t):
    return any(x and VERSE_RE.search(x) for x in t)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    cur = c.cursor()

    cat = {r["finding_id"] for r in cur.execute("SELECT DISTINCT finding_id FROM wa_finding_catalogue_links WHERE COALESCE(delete_flagged,0)=0")}
    cited = {r["cited_sd_pointer_id"] for r in cur.execute("SELECT DISTINCT cited_sd_pointer_id FROM wa_prose_section_citations WHERE cited_sd_pointer_id IS NOT NULL")}

    orphan_f = []
    for r in cur.execute("SELECT id, anchor_verses av, finding, cluster_link cl, session_c_chapter scc, sd_pointer_ref sdr, related_finding_id rfi, status FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0 AND status IS NOT 'set_aside_non_evidenced'"):
        if r["cl"]:
            continue
        if r["id"] in cat:
            continue
        if (r["av"] and r["av"].strip()) or hasverse(r["finding"]):
            continue
        if r["scc"] or r["sdr"] or r["rfi"]:
            continue
        orphan_f.append(r["id"])

    orphan_fl = []
    for r in cur.execute(f"SELECT id, flag_label flb, description d, cluster_link cl, strongs_reference sr, COALESCE(resolved,0) res FROM wa_session_research_flags WHERE flag_code IN ({','.join('?'*len(FLAG_CODES))})", FLAG_CODES):
        if r["res"] or r["cl"] or (r["sr"] and r["sr"].strip()):
            continue
        if hasverse(r["flb"], r["d"]):
            continue
        if r["id"] in cited:
            continue
        orphan_fl.append(r["id"])

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: orphan findings={len(orphan_f)} | orphan flags={len(orphan_fl)}")
    if not a.apply:
        c.close(); return

    cur.execute("BEGIN")
    try:
        nf = 0
        for fid in orphan_f:
            cur.execute("UPDATE wa_session_b_findings SET status='set_aside_non_evidenced', resolution_note=? WHERE id=?", (REASON_F, fid))
            nf += cur.rowcount
        nfl = 0
        for flid in orphan_fl:
            cur.execute("UPDATE wa_session_research_flags SET resolved=1, resolved_date=datetime('now'), resolved_note=? WHERE id=?", (REASON_FL, flid))
            nfl += cur.rowcount
        if nf != len(orphan_f) or nfl != len(orphan_fl):
            c.rollback(); raise SystemExit(f"ABORT: rowcounts {nf}/{nfl} != {len(orphan_f)}/{len(orphan_fl)} — rolled back.")
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: set aside {nf} findings (status=set_aside_non_evidenced) + {nfl} flags (resolved + note).")
    c.close()


if __name__ == "__main__":
    main()
