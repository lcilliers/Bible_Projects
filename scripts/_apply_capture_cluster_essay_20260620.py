"""_apply_capture_cluster_essay_20260620.py — capture a CC-authored cluster essay into prose_section.

The published cluster essay is a prose product drawn from the captured findings. Stored in prose_section
(type cluster_essay), cluster-level (characteristic_id NULL), author claude_code, status approved. Additive,
idempotent (skips a file already captured). FTS auto via triggers.

  python scripts/_apply_capture_cluster_essay_20260620.py --cluster M01 --file <path> --dry-run | --live
"""
import argparse, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-20T00:00:00Z"
TYPE = ("cluster_essay", "Cluster Essay (general-reader prose product)", 210)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--file", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    if not os.path.exists(a.file):
        print("MISSING:", a.file); return 2
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # section type
    r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (TYPE[0],)).fetchone()
    tid = r["id"] if r else None
    if not r and a.live:
        cur.execute("INSERT INTO prose_section_type (code,label,source_stage,sort_order,delete_flagged,created_at) VALUES (?,?, 'essay', ?, 0, ?)", (TYPE[0], TYPE[1], TYPE[2], STAMP))
        tid = cur.lastrowid
    body = open(a.file, encoding="utf-8").read()
    hm = re.search(r"^#\s+(.+)$", body, re.M)
    heading = (hm.group(1).strip() if hm else os.path.basename(a.file))[:300]
    src = os.path.basename(a.file)
    vm = re.search(r"-v(\d+)-", src); version = f"v{vm.group(1)}" if vm else "v1"
    exists = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code=? AND COALESCE(delete_flagged,0)=0", (src, a.cluster)).fetchone()
    print(f"[{'exists' if exists else 'INSERT'}] {a.cluster} cluster_essay · {len(body.split()):,}w · {src}")
    if a.dry_run:
        print("[DRY-RUN] no changes."); return 0
    if not exists:
        cur.execute("""INSERT INTO prose_section
            (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file,
             metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
            VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_code', ?, ?, ?, NULL, 0, ?)""",
            (tid, heading, body, len(body.split()), version, src,
             json.dumps({"layer": "cluster_essay", "audience": "general", "template": "wa-cc-cluster-essay-style-template-v1_0"}),
             a.cluster, STAMP))
    conn.commit()
    n = cur.execute("SELECT COUNT(*) FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id WHERE t.code='cluster_essay' AND COALESCE(ps.delete_flagged,0)=0").fetchone()[0]
    print(f"LIVE: cluster_essay rows now {n}. integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
