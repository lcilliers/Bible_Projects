"""
export_word_json.py
───────────────────
CLI wrapper for analytics.word_export.

Usage:
    python scripts/export_word_json.py --registry=182
    python scripts/export_word_json.py --registry=182 --out=data/exports/
    python scripts/export_word_json.py --registry=182 --pretty

File naming: {word}_{registry}_full_{YYYYMMDD}.json
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from analytics.db_client import get_connection
from analytics.word_export import export_word


def main() -> int:
    ap = argparse.ArgumentParser(description="Export all data for a single word to JSON.")
    ap.add_argument("--registry", type=int, required=True,
                    help="word_registry.no value (e.g. 182 for Soul)")
    ap.add_argument("--out", metavar="DIR", default="data/exports",
                    help="Output directory (default: data/exports)")
    ap.add_argument("--pretty", action="store_true",
                    help="Pretty-print JSON with indentation")
    args = ap.parse_args()

    conn = get_connection()
    try:
        print(f"Exporting registry {args.registry}...")
        data = export_word(conn, args.registry)
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1
    finally:
        conn.close()

    word = data["_export"]["word"]
    date = data["_export"]["exported_at"][:10].replace("-", "")   # YYYYMMDD
    scope = data["_export"]["scope"]

    filename = f"{word}_{args.registry}_{scope}_{date}.json"
    out_dir  = args.out
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)

    indent = 2 if args.pretty else None
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=indent, ensure_ascii=False, default=str)

    size_kb = os.path.getsize(out_path) / 1024
    stats   = data["statistics"]
    print(f"  Word:     {word}  (registry {args.registry})")
    print(f"  Terms:    {stats['term_count']}")
    print(f"  Verses:   {stats['verse_count']}")
    print(f"  Files:    {len(data['files'])}")
    print(f"  Output:   {out_path}  ({size_kb:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
