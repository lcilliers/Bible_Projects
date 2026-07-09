"""Assemble a cluster publication from prose_section (DB-canonical source).

Per v3_0 publication pipeline (researcher direction 2026-05-27): the
prose_section table is the canonical source for cluster publication prose.
This script reads the latest active version of each chapter (sc_v2_ch1..ch7)
for a cluster and assembles them into a combined Markdown document.

"Latest active version" resolution:
  - WHERE cluster_code = {code}
  - AND section_type_id = sc_v2_ch{N}.id
  - AND COALESCE(delete_flagged, 0) = 0
  - AND superseded_by_id IS NULL  (top of the supersession chain)
  - ORDER BY version DESC LIMIT 1

Output: Sessions/Session_Clusters/{CODE}/published/wa-cluster-{CODE}-publication-v{N}-{YYYYMMDD}.md

Usage:
    python scripts/_assemble_cluster_publication_from_db_v1_20260527.py --cluster M03
    python scripts/_assemble_cluster_publication_from_db_v1_20260527.py --cluster M01 --output /path/to/out.md

If --status-filter approved is set, only chapters with status='approved' are
emitted. Default emits all latest versions regardless of status (publication
draft).
"""
from __future__ import annotations
import argparse, io, re, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = datetime.now(timezone.utc).strftime("%Y%m%d")


def find_next_version(out_dir: Path, cluster: str) -> int:
    pat = re.compile(rf"^wa-cluster-{cluster}-publication-v(\d+)-\d+\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return max_v + 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code (M01, M03, etc.)")
    ap.add_argument("--output", help="Output path (default: auto-derived)")
    ap.add_argument("--status-filter", choices=["draft", "approved", "any"], default="any",
                    help="Only include chapters with this status (default: any)")
    ap.add_argument("--include-status-marker", action="store_true",
                    help="Include the per-chapter status (draft/approved) in headings")
    args = ap.parse_args()

    cluster = args.cluster
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    # Cluster meta
    c = conn.execute("SELECT description, short_name, status FROM cluster WHERE cluster_code=?", (cluster,)).fetchone()
    if not c:
        print(f"ERROR: unknown cluster {cluster!r}")
        return 1

    # Get the latest active version of each chapter
    chapters: dict[int, sqlite3.Row] = {}
    status_filter_sql = ""
    params: list = [cluster]
    if args.status_filter != "any":
        status_filter_sql = "AND ps.status = ?"
        params.append(args.status_filter)

    rows = conn.execute(f"""
        SELECT pst.code AS type_code, pst.chapter_no, pst.label,
               ps.id, ps.heading, ps.body, ps.word_count, ps.version,
               ps.status, ps.author, ps.created_at, ps.approved_at
        FROM prose_section ps
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE ps.cluster_code = ?
          AND pst.code LIKE 'sc_v2_ch%'
          AND ps.superseded_by_id IS NULL
          AND COALESCE(ps.delete_flagged, 0) = 0
          {status_filter_sql}
        ORDER BY pst.chapter_no, ps.version DESC
    """, params).fetchall()
    for r in rows:
        ch = r["chapter_no"]
        if ch not in chapters:  # take first (latest version per chapter due to ORDER BY)
            chapters[ch] = r

    missing = [n for n in range(1, 8) if n not in chapters]
    if missing:
        print(f"WARNING: missing chapters: {missing}")
    print(f"Chapters resolved: {sorted(chapters.keys())} (out of 7)")

    # Build output
    out_lines: list[str] = []
    out_lines.append(f"# {c['description']}")
    out_lines.append("")
    out_lines.append(f"_Cluster: `{cluster}` · {c['short_name'] or ''}_")
    out_lines.append(f"_Assembled from prose_section at {NOW}_")
    out_lines.append("")
    out_lines.append("**Status by chapter:**")
    out_lines.append("")
    for n in sorted(chapters.keys()):
        r = chapters[n]
        out_lines.append(f"- Ch{n} {r['label'].split(' — ', 1)[-1]} — v{r['version']} {r['status']}{'  (' + str(r['word_count']) + 'w)' if r['word_count'] else ''}")
    out_lines.append("")
    out_lines.append("---")
    out_lines.append("")

    # Each chapter
    for n in sorted(chapters.keys()):
        r = chapters[n]
        ch_title = r["label"].split(" — ", 1)[-1].replace("Ch", "Chapter ")
        ch_title = re.sub(r"^Chapter (\d)", lambda m: f"Chapter {m.group(1)}", ch_title)
        if args.include_status_marker:
            ch_title = f"{ch_title}  _[{r['status']} v{r['version']}]_"
        out_lines.append(f"## {ch_title}")
        out_lines.append("")
        # If body starts with its own H1, strip it (we already have the master title)
        body = r["body"] or ""
        body_lines = body.splitlines()
        # Strip leading H1 if present
        skip_until = 0
        for i, ln in enumerate(body_lines[:20]):
            if ln.startswith("# "):
                skip_until = i + 1
                # Also skip subsequent blank lines + a metadata block if present
                while skip_until < len(body_lines) and (body_lines[skip_until].strip() == "" or body_lines[skip_until].startswith("**")):
                    if body_lines[skip_until].strip() == "" and skip_until > 0 and not body_lines[skip_until-1].startswith("**"):
                        break
                    skip_until += 1
                break
        body_clean = "\n".join(body_lines[skip_until:]).strip()
        # Strip EVIDENCE preservation markers
        body_clean = re.sub(r"<!--\s*EVIDENCE:.*?-->.*?<!--\s*/EVIDENCE\s*-->", "", body_clean, flags=re.DOTALL)
        out_lines.append(body_clean)
        out_lines.append("")
        out_lines.append("---")
        out_lines.append("")

    # Write
    out_dir = REPO / "Sessions" / "Session_Clusters" / cluster / "published"
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.output:
        out_path = Path(args.output)
    else:
        v = find_next_version(out_dir, cluster)
        out_path = out_dir / f"wa-cluster-{cluster}-publication-v{v}-{TODAY}.md"

    out_path.write_text("\n".join(out_lines), encoding="utf-8")
    total_words = sum((r["word_count"] or 0) for r in chapters.values())
    print(f"\nWrote: {out_path.relative_to(REPO)}")
    print(f"  Chapters: {len(chapters)}/7")
    print(f"  Total words: {total_words:,}")
    print(f"  Output size: {out_path.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
