"""_apply_findings_stageA_characteristics_20260619.py — Stage A of the M01/M02 findings capture.

Create the NEW characteristic rows (M01 c1-c11, M02 c1-c7) parsed from the characteristic-definition files.
Additive only (no existing rows touched; old characteristics handled in Stage C). Idempotent: skips a
characteristic already present for (cluster, char_seq, source). Dry-run shows what would be created.

  python scripts/_apply_findings_stageA_characteristics_20260619.py --dry-run
  python scripts/_apply_findings_stageA_characteristics_20260619.py --live
"""
import argparse, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-19T00:00:00Z"
M01_FILE = "Sessions-v2/M01-Fear/Analysis/WA-m01-characteristics-v1.0-2026-06-16.md"
M02_FILE = "Sessions-v2/M02-Anger/findings/wa-m02-ve-characteristics-v1_0-20260619.md"


def parse_m01(path):
    """### N. Name(...)\\n<description line>  -> (seq, short_name, definition)"""
    t = open(path, encoding="utf-8").read()
    region = t.split("## A. The characteristics")[1].split("## B.")[0]
    out = []
    for m in re.finditer(r"^### (\d+)\.\s+(.+?)\n(.+?)(?:\n-|\n###|\Z)", region, re.S | re.M):
        seq = int(m.group(1)); name = m.group(2).strip()
        desc = re.sub(r"\s*\n\s*", " ", m.group(3)).strip()
        out.append((seq, name, desc))
    return out


def parse_m02(path):
    """### C{n} — Name — N occ\\nWhat the verse is about: ...  -> (seq, short_name, definition)"""
    t = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^### C(\d+)\s+—\s+(.+?)\n(?:What the verse is about:\s*)?(.+?)(?:\nPrincipal|\n###|\Z)",
                         t, re.S | re.M):
        seq = int(m.group(1))
        name = re.sub(r"\s+—\s+\d+\s*occ.*$", "", m.group(2)).strip()
        desc = re.sub(r"\s*\n\s*", " ", m.group(3)).strip()
        out.append((seq, name, desc))
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    plan = [("M01", M01_FILE, parse_m01(M01_FILE), os.path.basename(M01_FILE)),
            ("M02", M02_FILE, parse_m02(M02_FILE), os.path.basename(M02_FILE))]
    created = 0
    for cluster, path, chars, src in plan:
        print(f"\n== {cluster}: {len(chars)} characteristics parsed from {src} ==")
        if len(chars) != (11 if cluster == "M01" else 7):
            print(f"   ABORT: expected {'11' if cluster=='M01' else '7'} characteristics, parsed {len(chars)}"); return 2
        for seq, name, desc in chars:
            exists = cur.execute("SELECT id FROM characteristic WHERE cluster_code=? AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0",
                                 (cluster, 100 + seq, src)).fetchone()
            tag = "exists" if exists else "CREATE"
            print(f"   c{seq:<2} [{tag}] {name}  —  {desc[:70]}…")
            if a.live and not exists:
                # char_seq offset +100 to avoid the UNIQUE(cluster_code,char_seq) collision with the legacy
                # 7/6-char model (seq 1-7); the new model is identified by id + source; legacy gets restricted in Stage C.
                cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                    VALUES (?,?,?,?,?, 'v1.0', ?, 0, ?, ?)""",
                    (cluster, 100 + seq, name, desc, src,
                     f"11/7-char model 2026-06-19 (findings capture Stage A); model c{seq}; char_seq=100+{seq} to avoid legacy seq collision",
                     STAMP, STAMP)); created += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0
    conn.commit()
    print(f"\nLIVE: created {created} characteristics.")
    print("verify — active characteristic counts by cluster/source:")
    for r in cur.execute("SELECT cluster_code, source, COUNT(*) n FROM characteristic WHERE cluster_code IN ('M01','M02') AND COALESCE(delete_flagged,0)=0 GROUP BY cluster_code, source ORDER BY cluster_code"):
        print(f"   {r['cluster_code']} · {str(r['source'])[:40]:40} {r['n']}")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
