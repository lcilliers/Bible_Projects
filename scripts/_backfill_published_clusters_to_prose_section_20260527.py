"""Backfill prose_section from existing M01/M03/M15 chapter drafts.

Per researcher direction 2026-05-27: the three published clusters have
chapter-draft markdown files on disk. Populate prose_section with these
so the v3_0 pipeline can use the prose store as its canonical source.

Source files:
  M01: Sessions/Session_Clusters/M01/Published/wa-cluster-M01-ch{1..7}-draft-v{1,2}-20260523.md
  M03: Sessions/Session_Clusters/M03/published/wa-cluster-M03-ch{1..7}-draft-v1-2026-05-17.md
  M15: Sessions/Session_Clusters/M15/published/WA-M15-ch{1..7}-draft-v{1,2,3}-20260512.md

For each chapter file we insert one prose_section row with:
  section_type_id   = sc_v2_ch{N}'s id
  cluster_code      = M01 | M03 | M15
  characteristic_id = NULL (these are cluster-scope chapters)
  heading           = first H1 heading from the file
  body              = full file content
  word_count        = word count
  status            = 'approved'    (M03 published)
                    | 'draft'       (M01, M15 — drafts authored, not formally approved)
  version           = parsed from filename (v1, v2, v3)
  supersedes_id     = id of prior version (chain v1 -> v2 -> v3)
  author            = 'claude_ai'  (these were AI-authored chapter drafts)
  source_file       = relative path
  metadata_json     = {"generator": "manual_chapter_draft", "source_path": ...}

Versioning chain: when ch1 has v1 and v2, the v2 row's supersedes_id points
at the v1 row's id, and the v1 row's superseded_by_id points at the v2 row's id.

Idempotent: skipped if the (cluster_code, section_type_id, version) row
already exists.
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# (cluster, status, dir, file_glob_pattern, version_re)
SOURCES = [
    ("M01", "draft",
     REPO / "Sessions" / "Session_Clusters" / "M01" / "Published",
     re.compile(r"^wa-cluster-M01-ch(\d)-draft-v(\d+)-\d+\.md$")),
    ("M03", "approved",
     REPO / "Sessions" / "Session_Clusters" / "M03" / "published",
     re.compile(r"^wa-cluster-M03-ch(\d)-draft-v(\d+)-\d{4}-\d{2}-\d{2}\.md$")),
    ("M09", "approved",
     REPO / "Sessions" / "Session_Clusters" / "M09" / "publishing",
     re.compile(r"^wa-cluster-M09-ch(\d)-draft-v(\d+)-\d+\.md$")),
    ("M15", "draft",
     REPO / "Sessions" / "Session_Clusters" / "M15" / "published",
     re.compile(r"^WA-M15-ch(\d)-draft-v(\d+)-\d+\.md$")),
]


def parse_first_h1(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def main(live: bool) -> int:
    print(f"=== Backfill published clusters → prose_section — mode={'LIVE' if live else 'DRY-RUN'} ===")
    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")
    conn.row_factory = sqlite3.Row

    type_id = {r["code"]: r["id"] for r in conn.execute(
        "SELECT id, code FROM prose_section_type WHERE code LIKE 'sc_v2_ch%' AND COALESCE(delete_flagged,0)=0"
    ).fetchall()}
    print(f"Section type lookup loaded: {len(type_id)} sc_v2_ch types")

    # Gather all files to ingest, organised by (cluster, ch_no, version)
    plan: list[tuple[str, str, int, int, Path]] = []
    for cluster, status, src_dir, pat in SOURCES:
        if not src_dir.exists():
            print(f"  WARN: source dir does not exist: {src_dir.relative_to(REPO)}")
            continue
        for f in sorted(src_dir.iterdir()):
            if not f.is_file():
                continue
            m = pat.match(f.name)
            if not m:
                continue
            ch_no = int(m.group(1))
            ver = int(m.group(2))
            plan.append((cluster, status, ch_no, ver, f))
    print(f"Files to ingest: {len(plan)}")

    # Pre-check for duplicates (idempotency)
    existing = {(r["cluster_code"], r["section_type_id"], r["version"])
                for r in conn.execute(
                    "SELECT cluster_code, section_type_id, version FROM prose_section "
                    "WHERE cluster_code IN ('M01','M03','M15') AND COALESCE(delete_flagged,0)=0"
                ).fetchall()}
    plan_filtered = []
    for cluster, status, ch_no, ver, path in plan:
        sec_id = type_id.get(f"sc_v2_ch{ch_no}")
        if sec_id is None:
            print(f"  SKIP: no section_type for sc_v2_ch{ch_no}")
            continue
        key = (cluster, sec_id, ver)
        if key in existing:
            print(f"  SKIP (exists): {cluster} ch{ch_no} v{ver}")
            continue
        plan_filtered.append((cluster, status, ch_no, ver, path, sec_id))
    print(f"Files to insert (post-dedup): {len(plan_filtered)}")

    if not live:
        print("\n[DRY-RUN — no writes]")
        for cluster, status, ch_no, ver, path, sec_id in plan_filtered[:10]:
            print(f"  + {cluster} ch{ch_no} v{ver} ({status}) <- {path.name}")
        if len(plan_filtered) > 10:
            print(f"  ... and {len(plan_filtered)-10} more")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        inserted_ids: dict[tuple[str, int, int], int] = {}
        for cluster, status, ch_no, ver, path, sec_id in plan_filtered:
            body = path.read_text(encoding="utf-8")
            heading = parse_first_h1(body) or f"{cluster} — Ch{ch_no}"
            wc = len(body.split())
            metadata = json.dumps({
                "generator": "manual_chapter_draft_backfill",
                "generator_version": "_backfill_published_clusters_to_prose_section_20260527",
                "source_path": str(path.relative_to(REPO)).replace("\\", "/"),
                "ch_no": ch_no,
                "ingested_at": NOW,
            })
            cur.execute(
                "INSERT INTO prose_section "
                "(registry_id, section_type_id, heading, body, word_count, status, version, "
                " supersedes_id, superseded_by_id, author, created_at, approved_at, approved_by, "
                " metadata_json, source_file, delete_flagged, cluster_code, characteristic_id, cluster_subgroup_id) "
                "VALUES (NULL, ?, ?, ?, ?, ?, ?, NULL, NULL, 'claude_ai', ?, "
                " ?, ?, ?, ?, 0, ?, NULL, NULL)",
                (sec_id, heading, body, wc, status, ver, NOW,
                 NOW if status == "approved" else None,
                 "manual_backfill" if status == "approved" else None,
                 metadata, str(path.relative_to(REPO)).replace("\\", "/"),
                 cluster),
            )
            inserted_ids[(cluster, ch_no, ver)] = cur.lastrowid

        # Link supersession chains: for each (cluster, ch_no), set v_n.supersedes_id = v_{n-1}.id
        chain_links = 0
        for (cluster, ch_no, ver), row_id in inserted_ids.items():
            prev_id = inserted_ids.get((cluster, ch_no, ver - 1))
            if prev_id is not None:
                cur.execute("UPDATE prose_section SET supersedes_id=? WHERE id=?", (prev_id, row_id))
                cur.execute("UPDATE prose_section SET superseded_by_id=? WHERE id=?", (row_id, prev_id))
                chain_links += 1
        print(f"\nInserted {len(inserted_ids)} prose_section rows")
        print(f"Created {chain_links} supersession chain-links")
        conn.commit()
        print(f"COMMITTED at {NOW}")

        # Verify FTS sync (trigger should have indexed automatically)
        n_fts = conn.execute(
            "SELECT COUNT(*) FROM prose_section_fts WHERE cluster_code IN ('M01','M03','M15')"
        ).fetchone()[0]
        print(f"prose_section_fts rows with cluster_code in (M01/M03/M15): {n_fts}")
    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
