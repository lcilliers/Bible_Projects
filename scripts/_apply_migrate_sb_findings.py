"""_apply_migrate_sb_findings.py — migrate Session B findings (wa_session_b_findings) into the universal
`finding` table (schema M56). Per researcher rule (feedback_session_b_findings_resolved_through_l2):
- has related_finding_id            -> CLOSED (defer to the related finding)
- verse-anchored, no reference       -> OPEN (L2 work item) + finding_verse_link rows (anchor verses)
- else (non-verse-anchored)          -> CLOSED if SB status is a closed kind, else OPEN (term/cluster-level)
Level = CLUSTER (primary M-code from cluster_link) else GLOBAL. Idempotent (skips already-migrated by
source_legacy_ref). Reversible (delete finding/finding_verse_link rows where provenance='session_b_migration').

Usage:  python scripts/_apply_migrate_sb_findings.py --dry-run --out <file>.md
        python scripts/_apply_migrate_sb_findings.py --live    --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
CLOSED_SB = {"resolved_qa", "resolved_sd", "confirmed", "superseded", "folded", "set_aside",
             "set_aside_non_evidenced"}
MCODE = re.compile(r"^M\d+[a-z]?$")


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    now = c.execute("SELECT datetime('now')").fetchone()[0]

    already = {r[0] for r in c.execute(
        "SELECT source_legacy_ref FROM finding WHERE provenance='session_b_migration' AND source_legacy_ref IS NOT NULL")}
    sb = c.execute("SELECT * FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0").fetchall()

    stat = Counter(); lvl = Counter(); nlinks = 0; nmig = 0; nskip = 0
    for r in sb:
        slr = f"SB:{r['finding_id']}"
        if any(x and x.startswith(slr + "|") for x in already):
            nskip += 1; continue
        clusters = [x.strip() for x in (r["cluster_link"] or "").split(",") if x.strip()]
        primary = next((x for x in clusters if MCODE.match(x)), None)
        level = "CLUSTER" if primary else "GLOBAL"
        anchored = bool((r["anchor_verses"] or "").strip())
        has_ref = r["related_finding_id"] is not None
        sbstatus = r["status"]
        if has_ref:
            status = "CLOSED"
        elif anchored:
            status = "OPEN"
        else:
            status = "CLOSED" if sbstatus in CLOSED_SB else "OPEN"
        full_slr = f"{slr}|type:{r['finding_type']}|reg:{r['registry_id']}|clusters:{r['cluster_link']}|sbstatus:{sbstatus}"
        stat[status] += 1; lvl[level] += 1; nmig += 1
        if a.live:
            cur = c.execute(
                "INSERT INTO finding (level, cluster_code, finding_value, finding_status, provenance, "
                "source_legacy_ref, created_at, last_updated_date, delete_flagged) "
                "VALUES (?,?,?,?,?,?,?,?,0)",
                (level, primary, r["finding"], status, "session_b_migration", full_slr,
                 r["raised_date"] or now, now))
            fid = cur.lastrowid
            if anchored:
                for ref in [x.strip() for x in (r["anchor_verses"]).split(",") if x.strip()]:
                    c.execute("INSERT INTO finding_verse_link (finding_id, reference, role, created_at, delete_flagged) "
                              "VALUES (?,?,?,?,0)", (fid, ref, "anchor", now))
                    nlinks += 1
        elif anchored:
            nlinks += len([x for x in (r["anchor_verses"]).split(",") if x.strip()])
    if a.live:
        conn.commit()

    L = [f"# Session B findings → `finding` migration — {'LIVE' if a.live else 'DRY-RUN'}", ""]
    L.append("> `scripts/_apply_migrate_sb_findings.py`. Migrates wa_session_b_findings into the universal "
             "finding table; verse-anchored unresolved → OPEN + finding_verse_link (L2 work items). "
             "Idempotent · reversible (provenance='session_b_migration').")
    L.append("")
    L.append(f"**{nmig} migrated · {nskip} already-present (skipped) · {nlinks} verse-anchor links.**")
    L.append("")
    L.append("| status | n |"); L.append("|---|---|")
    for k, v in stat.most_common(): L.append(f"| {k} | {v} |")
    L.append("")
    L.append("| level | n |"); L.append("|---|---|")
    for k, v in lvl.most_common(): L.append(f"| {k} | {v} |")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{'LIVE' if a.live else 'DRY'}: migrated {nmig}, skipped {nskip}, links {nlinks}; "
          f"status {dict(stat)}; level {dict(lvl)}; wrote {a.out}")


if __name__ == "__main__":
    main()
