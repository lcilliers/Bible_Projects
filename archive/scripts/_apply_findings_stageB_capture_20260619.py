"""_apply_findings_stageB_capture_20260619.py — Stage B: capture NEW findings files as prose_section rows.

File-as-finding (no dissection): each findings file -> one prose_section row holding its whole body, tagged by
cluster_code + characteristic_id (per-char files) + a section_type. FTS is trigger-maintained (auto). Additive
only. Idempotent: skips a file already captured (same source_file, active). Dry-run previews.

  python scripts/_apply_findings_stageB_capture_20260619.py --dry-run
  python scripts/_apply_findings_stageB_capture_20260619.py --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-19T00:00:00Z"
AUTHOR = "claude_ai"
M01 = "Sessions-v2/M01-Fear/findings"
M02 = "Sessions-v2/M02-Anger/findings"

TYPES = [  # (code, label, sort_order)
    ("cf_cluster_synth", "Cluster Findings — Cluster Synthesis", 201),
    ("cf_char_synth",    "Cluster Findings — Characteristic Synthesis/Analysis", 202),
    ("cf_atomic",        "Cluster Findings — Atomic Lexical Findings (by question)", 203),
]


def latest(pattern):
    cands = sorted(glob.glob(pattern))
    return cands[-1] if cands else None


def build_filelist():
    """-> list of (cluster, c_number|None, type_code, path)"""
    items = []
    for c in range(1, 12):  # M01 per-char synth c01..c11
        p = latest(f"{M01}/wa-m01-c{c:02d}-*-synth-v1_*-20260619.md")
        if p: items.append(("M01", c, "cf_char_synth", p))
    items.append(("M01", None, "cf_cluster_synth", f"{M01}/wa-m01-cluster-synthesis-v1_0-20260619.md"))
    items.append(("M01", None, "cf_atomic", f"{M01}/WA-m01-findings-NEW-merged-bytier-v1-20260619.md"))
    for c in range(1, 8):  # M02 per-char tier analysis c1..c7 (latest version)
        p = latest(f"{M02}/wa-m02-c{c}-*-tieranalysis-v1_*-20260619.md")
        if p: items.append(("M02", c, "cf_char_synth", p))
    items.append(("M02", None, "cf_cluster_synth", latest(f"{M02}/wa-m02-cluster-synthesis-bytier-v1_*-20260619.md")))
    items.append(("M02", None, "cf_cluster_synth", f"{M02}/wa-m02-cluster-findings-v1_0-20260619.md"))
    return items


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # ensure section types
    typeids = {}
    for code, label, so in TYPES:
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        if r: typeids[code] = r["id"]
        elif a.live:
            cur.execute("INSERT INTO prose_section_type (code,label,source_stage,sort_order,delete_flagged,created_at) VALUES (?,?, 'findings', ?, 0, ?)", (code, label, so, STAMP))
            typeids[code] = cur.lastrowid
        else: typeids[code] = f"<new:{code}>"
    # char id map (char_seq = 100 + c)
    charid = {}
    for r in cur.execute("SELECT cluster_code, char_seq, id FROM characteristic WHERE source IN ('WA-m01-characteristics-v1.0-2026-06-16.md','wa-m02-ve-characteristics-v1_0-20260619.md') AND COALESCE(delete_flagged,0)=0"):
        charid[(r["cluster_code"], r["char_seq"] - 100)] = r["id"]

    items = build_filelist()
    print(f"files to capture: {len(items)}")
    n_ins = 0
    for cluster, cnum, tcode, path in items:
        if not path or not os.path.exists(path):
            print(f"   MISSING: {cluster} c{cnum} {tcode} -> {path}"); return 2
        body = open(path, encoding="utf-8").read()
        h = re.search(r"^#\s+(.+)$", body, re.M)
        heading = (h.group(1).strip() if h else os.path.basename(path))[:300]
        src = os.path.basename(path)
        vm = re.search(r"v(\d+_\d+)", src); version = vm.group(1) if vm else "v1_0"
        cid = charid.get((cluster, cnum)) if cnum else None
        exists = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code=? AND COALESCE(delete_flagged,0)=0", (src, cluster)).fetchone()
        tag = "exists" if exists else "INSERT"
        print(f"   [{tag}] {cluster} {('c'+str(cnum)) if cnum else 'cluster':7} {tcode:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not exists:
            meta = json.dumps({"layer": tcode, "c_number": cnum, "model": "11/7-char 2026-06-19"})
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author,
                 source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, ?, ?, ?, ?, ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, AUTHOR, src, meta, cluster, cid, STAMP))
            n_ins += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0
    conn.commit()
    print(f"\nLIVE: inserted {n_ins} prose_section rows.")
    for r in cur.execute("""SELECT ps.cluster_code, t.code, COUNT(*) n FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id
        WHERE t.code LIKE 'cf_%' AND COALESCE(ps.delete_flagged,0)=0 GROUP BY ps.cluster_code, t.code ORDER BY ps.cluster_code, t.code"""):
        print(f"   {r['cluster_code']} {r['code']:18} {r['n']}")
    print("FTS rows:", cur.execute("SELECT COUNT(*) FROM prose_section_fts").fetchone()[0], "· integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
