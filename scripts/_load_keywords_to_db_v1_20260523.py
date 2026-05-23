"""Load inner-being keywords from discovery JSONs into verse_context.keywords.

Used for backfill — when a cluster's Pass A was run before keywords were embedded
in the API output (pre-2026-05-23 clusters), the per-sub-group keyword discovery
script produces JSON files that this loader ingests into the DB.

For new clusters running Pass A under the embedded flow (post-2026-05-23), the
keywords are written directly by the Pass A patch — this loader is not needed.

Usage:
  python scripts/_load_keywords_to_db_v1_20260523.py --json path/to/keywords.json
  python scripts/_load_keywords_to_db_v1_20260523.py --glob "Sessions/Session_Clusters/M10/files phase 5/wa-cluster-M10-*-keywords-v*.json"
"""
from __future__ import annotations
import argparse, glob, json, sqlite3, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def load_one(conn, path: Path, dry: bool) -> tuple[int, int, int]:
    """Returns (loaded, skipped, missing)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if "keywords_by_vc_id" not in data:
        raise ValueError(f"{path.name}: missing 'keywords_by_vc_id' — wrong file shape")
    loaded = skipped = missing = 0
    for vc_id_str, info in data["keywords_by_vc_id"].items():
        vc_id = int(vc_id_str)
        kws = info.get("keywords") or []
        if not kws:
            skipped += 1
            continue
        # Verify the row exists
        r = conn.execute(
            "SELECT keywords FROM verse_context WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (vc_id,)
        ).fetchone()
        if r is None:
            missing += 1
            continue
        # Normalise: lower-case, dedupe preserving order
        seen, kws_clean = set(), []
        for kw in kws:
            kw = (kw or "").strip().lower()
            if kw and kw not in seen:
                seen.add(kw)
                kws_clean.append(kw)
        payload = json.dumps(kws_clean, ensure_ascii=False)
        if not dry:
            conn.execute(
                "UPDATE verse_context SET keywords=? WHERE id=?",
                (payload, vc_id)
            )
        loaded += 1
    return loaded, skipped, missing


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="append", default=[],
                    help="Path to a keywords JSON file (repeatable)")
    ap.add_argument("--glob", default=None, help="Glob pattern matching keyword JSONs")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    paths: list[Path] = []
    if args.glob:
        paths.extend(Path(p) for p in glob.glob(args.glob))
    paths.extend(Path(p) for p in args.json)
    if not paths:
        print("No paths provided.")
        return 1
    paths = sorted({p.resolve() for p in paths})
    # Filter out the raw responses and analysis report files
    paths = [p for p in paths if "-keywords-raw-" not in p.name
             and "-keyword-analysis-" not in p.name]
    print(f"Loading from {len(paths)} file(s):")
    for p in paths:
        print(f"  {p.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    try:
        if not args.dry_run:
            conn.execute("BEGIN")
        total_loaded = total_skipped = total_missing = 0
        for p in paths:
            loaded, skipped, missing = load_one(conn, p, args.dry_run)
            print(f"  {p.name}: loaded={loaded}, skipped={skipped} (empty keywords), missing={missing} (vc_id not found)")
            total_loaded += loaded
            total_skipped += skipped
            total_missing += missing
        if args.dry_run:
            print("\n[DRY-RUN — no writes]")
        else:
            conn.commit()
            print(f"\nCOMMITTED. loaded={total_loaded} skipped={total_skipped} missing={total_missing}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
