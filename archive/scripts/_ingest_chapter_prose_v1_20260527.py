"""Ingest chapter prose into prose_section (catch-up / revised publishing).

Per v3_0 publication pipeline (researcher direction 2026-05-27): take an
input markdown file and insert/update prose_section rows. Two modes:

1. Single-chapter mode (--ch N):
   Take a single markdown file as one chapter's body.

2. Multi-chapter mode (--multi):
   Take a master markdown file containing all chapters demarcated by
   `## Chapter N — Title` (or similar) headings. Split, ingest each.

For each chapter ingested:
  - Looks up existing rows for (cluster, sc_v2_ch{N})
  - Computes the next version (max existing version + 1)
  - INSERTs a new prose_section row with that version
  - Sets supersedes_id = id of the prior latest row
  - Updates the prior latest row's superseded_by_id = new id

The new row's status is configurable (--status draft|approved, default draft).
If --approve is set, status='approved' and approved_at/approved_by populated.

Idempotent guard: if --body-hash matches the latest existing version's body,
no new row is inserted (avoids duplicate-version churn).

Usage examples:

  # Single chapter
  python scripts/_ingest_chapter_prose_v1_20260527.py \\
      --cluster M11 --ch 3 \\
      --input path/to/m11-ch3-revised.md

  # Whole publication in one file
  python scripts/_ingest_chapter_prose_v1_20260527.py \\
      --cluster M12 --multi \\
      --input path/to/m12-full-publication.md

  # Mark as approved after ingest
  python scripts/_ingest_chapter_prose_v1_20260527.py \\
      --cluster M03 --ch 2 \\
      --input revised-ch2.md --approve
"""
from __future__ import annotations
import argparse, hashlib, io, json, re, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def body_hash(body: str) -> str:
    return hashlib.sha256(body.strip().encode("utf-8")).hexdigest()[:16]


def split_multi_chapter(text: str) -> dict[int, tuple[str, str]]:
    """Split a master document into {ch_no: (heading, body)} sections.

    Looks for headings of the form '## Chapter N — Title' (em-dash, hyphen,
    colon variants accepted). Body extends from after the heading line to
    the next chapter heading or EOF.
    """
    ch_pat = re.compile(r"^##\s+(?:Chapter\s+)?(\d+)[\s—\-:]+(.+)$", re.MULTILINE)
    matches = list(ch_pat.finditer(text))
    result: dict[int, tuple[str, str]] = {}
    for i, m in enumerate(matches):
        ch_no = int(m.group(1))
        title = m.group(2).strip()
        body_start = m.end()
        body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        result[ch_no] = (title, body)
    return result


def ingest_one(conn, cluster: str, ch_no: int, heading: str, body: str,
               status: str, author: str, approve: bool,
               source_path: str | None) -> tuple[int, str]:
    """Insert one prose_section row. Return (new_id, action_label)."""
    type_id = conn.execute(
        "SELECT id FROM prose_section_type WHERE code=?", (f"sc_v2_ch{ch_no}",)
    ).fetchone()
    if not type_id:
        raise RuntimeError(f"section_type sc_v2_ch{ch_no} not registered")
    type_id = type_id[0]

    # Find current latest version (top of supersession chain) for this (cluster, ch)
    latest = conn.execute("""
        SELECT id, version, body FROM prose_section
        WHERE cluster_code=? AND section_type_id=?
          AND superseded_by_id IS NULL AND COALESCE(delete_flagged,0)=0
        ORDER BY version DESC LIMIT 1
    """, (cluster, type_id)).fetchone()

    new_version = (latest["version"] + 1) if latest else 1
    new_hash = body_hash(body)

    # Idempotency: skip if body identical to current latest
    if latest and body_hash(latest["body"] or "") == new_hash:
        print(f"  ch{ch_no}: body identical to existing v{latest['version']} — skipping insert")
        return latest["id"], "unchanged"

    wc = len(body.split())
    metadata = json.dumps({
        "generator": "_ingest_chapter_prose_v1_20260527",
        "ingested_at": NOW,
        "source_path": source_path,
        "body_hash": new_hash,
        "ch_no": ch_no,
    })
    cur = conn.execute(
        "INSERT INTO prose_section "
        "(registry_id, section_type_id, heading, body, word_count, status, version, "
        " supersedes_id, superseded_by_id, author, created_at, approved_at, approved_by, "
        " metadata_json, source_file, delete_flagged, cluster_code, characteristic_id, cluster_subgroup_id) "
        "VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, ?, ?, ?, ?, 0, ?, NULL, NULL)",
        (type_id, heading, body, wc, status, new_version,
         latest["id"] if latest else None,
         author, NOW,
         NOW if approve else None,
         "manual_ingest" if approve else None,
         metadata, source_path, cluster),
    )
    new_id = cur.lastrowid
    # Chain: prior latest row's superseded_by_id = new_id
    if latest:
        conn.execute("UPDATE prose_section SET superseded_by_id=? WHERE id=?", (new_id, latest["id"]))
    return new_id, f"inserted v{new_version}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code")
    ap.add_argument("--input", required=True, help="Input markdown file")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--ch", type=int, help="Single-chapter mode: chapter number (1-7)")
    group.add_argument("--multi", action="store_true", help="Multi-chapter mode: file contains all chapters")
    ap.add_argument("--status", choices=["draft", "approved"], default="draft", help="Status (default: draft)")
    ap.add_argument("--approve", action="store_true", help="Alias for --status approved")
    ap.add_argument("--author", default="claude_ai", help="Author (default: claude_ai)")
    ap.add_argument("--heading", help="Override heading (single-chapter mode only)")
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        return 1
    text = input_path.read_text(encoding="utf-8")
    status = "approved" if args.approve else args.status

    # Resolve cluster
    conn = sqlite3.connect(DB, timeout=120.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 120000")
    c = conn.execute("SELECT cluster_code, description FROM cluster WHERE cluster_code=?", (args.cluster,)).fetchone()
    if not c:
        print(f"ERROR: unknown cluster {args.cluster!r}")
        return 1
    print(f"Cluster: {c['cluster_code']} ({c['description']})")
    print(f"Input: {input_path.relative_to(REPO) if input_path.is_relative_to(REPO) else input_path}")
    print(f"Mode: {'multi-chapter' if args.multi else f'single ch{args.ch}'}")
    print(f"Status: {status}  Author: {args.author}")
    print()

    # Build the (ch_no, heading, body) list
    plan: list[tuple[int, str, str]] = []
    if args.multi:
        sections = split_multi_chapter(text)
        if not sections:
            print("ERROR: no '## N Title' chapter headings found in multi-chapter input")
            return 1
        for ch_no in sorted(sections.keys()):
            heading, body = sections[ch_no]
            plan.append((ch_no, heading, body))
    else:
        # Single-chapter mode: use whole file body, derive heading from first H1 or arg
        if args.heading:
            heading = args.heading
        else:
            heading_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
            heading = heading_match.group(1) if heading_match else f"{args.cluster} Chapter {args.ch}"
        plan.append((args.ch, heading, text))

    print(f"Plan: {len(plan)} chapter(s) to ingest")
    for ch_no, heading, body in plan:
        print(f"  ch{ch_no}: {heading[:60]!r}  ({len(body.split())} words)")

    if not args.live:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    # Execute
    conn.execute("BEGIN IMMEDIATE")
    try:
        results = []
        for ch_no, heading, body in plan:
            new_id, action = ingest_one(
                conn, args.cluster, ch_no, heading, body,
                status, args.author, args.approve,
                str(input_path.relative_to(REPO)).replace("\\", "/") if input_path.is_relative_to(REPO) else str(input_path),
            )
            results.append((ch_no, new_id, action))
            print(f"  ch{ch_no}: {action} (id={new_id})")
        conn.commit()
        print(f"\nCOMMITTED at {NOW}")
        print(f"\nNext step (assemble combined publication from DB):")
        print(f"  python scripts/_assemble_cluster_publication_from_db_v1_20260527.py --cluster {args.cluster}")
    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
