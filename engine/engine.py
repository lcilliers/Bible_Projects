"""
engine.py
─────────
Session A v9 Automation Engine — CLI entry point.

Usage examples:
    python -m engine.engine --migrate
    python -m engine.engine --migrate --dry-run
    python -m engine.engine --db-status

    python -m engine.engine --register --word="sorrow" --source="High Confidence"

    python -m engine.engine --mode=new_word --registry=42 --terms=H0015,H0016
    python -m engine.engine --mode=new_word --registry=42 --terms=H0015 --dry-run
    python -m engine.engine --mode=new_word --registry=42 --terms=H0015 --force

    python -m engine.engine --mode=gap_fill                        (bulk — all Pending words)
    python -m engine.engine --mode=gap_fill  --streams=S1,S2        (bulk — selected stages only)
    python -m engine.engine --mode=gap_fill  --registry=42           (single-word gap patch)
    python -m engine.engine --mode=gap_fill  --registry=42 --streams=S3,S4

    python -m engine.engine --mode=audit_word --registry=42
    python -m engine.engine --mode=audit_word --registry=42 --skip-span-backpop

    python -m engine.engine --report --registry=42
    python -m engine.engine --report --registry=42 --format=markdown

    python -m engine.engine --export-word --registry=42

    python -m engine.engine --clear-lock --registry=42
    python -m engine.engine --clear-lock --registry=42 --force

    python -m engine.engine --check-locks
"""

from __future__ import annotations

import argparse
import sys
import os

# Ensure analytics/ is importable when running as a module from project root
_ROOT = os.path.join(os.path.dirname(__file__), "..")
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from .constants import ENGINE_VERSION, EXPECTED_SCHEMA_VERSION
from .db import get_connection, get_schema_version
from .migrate import run_migrations, check_version
from .backup import pre_migration_backup, pre_run_backup, post_run_backup
from .register import run_register, run_clear_lock, check_stale_locks
from .new_word import run_new_word
from .gap_fill import run_gap_fill, run_bulk_gap_fill
from .audit_word import run_audit_word
from .report import print_word_report

try:
    from analytics.word_export import export_word as _export_word
    _EXPORT_AVAILABLE = True
except ImportError:
    _EXPORT_AVAILABLE = False


def _build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="engine",
        description=f"Session A v9 Automation Engine v{ENGINE_VERSION}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--version", action="version",
                    version=f"engine {ENGINE_VERSION} (schema target {EXPECTED_SCHEMA_VERSION})")

    # ── Subcommand flags (mutually exclusive intent) ─────────────────────────
    mode_group = ap.add_mutually_exclusive_group()
    mode_group.add_argument("--migrate",     action="store_true",
                            help="Run schema migrations (v2.x → 3.0.0)")
    mode_group.add_argument("--db-status",   action="store_true",
                            help="Report current schema version + engine control tables")
    mode_group.add_argument("--register",    action="store_true",
                            help="Register a new word in word_registry")
    mode_group.add_argument("--mode",        choices=["new_word", "gap_fill", "audit_word"],
                            help="Engine mode to run")
    mode_group.add_argument("--report",      action="store_true",
                            help="Print word overview report")
    mode_group.add_argument("--export-word", action="store_true",
                            help="Export all data for a word to JSON (data/exports/)")
    mode_group.add_argument("--clear-lock",  action="store_true",
                            help="Clear an IN_PROGRESS sentinel from word_registry")
    mode_group.add_argument("--check-locks", action="store_true",
                            help="Report all active IN_PROGRESS sentinels")

    # ── Shared options ────────────────────────────────────────────────────────
    ap.add_argument("--registry", type=int, metavar="N",
                    help="word_registry.no (sequence number) for the target word")
    ap.add_argument("--dry-run",  action="store_true",
                    help="Analyse/validate only — no DB writes")
    ap.add_argument("--force",    action="store_true",
                    help="Force operation (overwrite existing data / bypass stale-lock timeout)")
    ap.add_argument("--verbose",  action="store_true",
                    help="Extra output for migrations and diagnostics")
    ap.add_argument("--db",       metavar="PATH",
                    help="Path to SQLite database (defaults to analytics/bible_research.db)")
    ap.add_argument("--pause",    action="store_true",
                    help="Pause at key checkpoints for manual verification (new_word mode)")
    ap.add_argument("--add-book-code", metavar="SOURCE=OSIS",
                    help='Register a book name alias (e.g. --add-book-code "Psalms=Ps")')

    # ── --migrate options ─────────────────────────────────────────────────────
    ap.add_argument("--to", metavar="MXX",
                    help="Stop migration at this step (e.g. --to=M05)")

    # ── --mode=new_word options ───────────────────────────────────────────────
    ap.add_argument("--terms", metavar="H1234,G5678",
                    help="Comma-separated Strong's numbers for --mode=new_word")

    # ── --mode=gap_fill options ───────────────────────────────────────────────
    ap.add_argument("--streams", metavar="S3,S4",
                    help="Comma-separated stream IDs for --mode=gap_fill (default: all)")

    # ── --mode=audit_word options ─────────────────────────────────────────────
    ap.add_argument("--skip-span-backpop", action="store_true",
                    help="(deprecated) Skip span back-population in --mode=audit_word")
    ap.add_argument("--interactive", action="store_true",
                    help="Enable per-category approve/skip gate in --mode=audit_word")
    ap.add_argument("--extract-file", metavar="PATH",
                    help="Explicit Step 1 JSON path for --mode=audit_word (default: auto-select latest)")

    # ── --register options ────────────────────────────────────────────────────
    ap.add_argument("--word",     metavar="\"sorrow\"",
                    help="English word to register (--register)")
    ap.add_argument("--source",   metavar="\"High Confidence\"",
                    help="source_list value for --register")
    ap.add_argument("--category", metavar="\"Emotion\"",
                    help="category_hint value for --register (optional)")

    # ── --report options ──────────────────────────────────────────────────────
    ap.add_argument("--format",   choices=["text", "markdown"],
                    default="text", metavar="FORMAT",
                    help="Output format for --report: text (default) or markdown")

    return ap


def main() -> int:
    ap = _build_parser()
    args = ap.parse_args()

    # Default action: print help if nothing specified
    if not any([args.migrate, args.db_status, args.register, args.mode,
                args.report, getattr(args, "export_word", False),
                args.clear_lock, args.check_locks,
                args.add_book_code]):
        ap.print_help()
        return 0

    # ── --add-book-code ────────────────────────────────────────────────────────────────────────
    if args.add_book_code:
        print("[INFO] --add-book-code is no longer supported. "
              "Book aliases are resolved via the book_code_variants table in the database.",
              file=sys.stderr)
        return 1

    # ── Open DB connection ────────────────────────────────────────────────────
    conn = get_connection(args.db or None)

    # ── --db-status ───────────────────────────────────────────────────────────
    if args.db_status:
        ver = get_schema_version(conn)
        print(f"Schema version:   {ver or '(schema_version table missing)'}")
        print(f"Expected version: {EXPECTED_SCHEMA_VERSION}")
        needs = ver != EXPECTED_SCHEMA_VERSION
        print(f"Migration needed: {'YES' if needs else 'no'}")
        # Control tables
        for tbl in ["engine_run_log", "word_run_state", "engine_stream_checkpoint", "term_fetch_log"]:
            exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tbl,)
            ).fetchone()
            n = conn.execute(f"SELECT COUNT(*) AS c FROM {tbl}").fetchone()["c"] if exists else 0
            print(f"  {tbl:<35} {'present' if exists else 'MISSING':10} rows={n}")
        return 0

    # ── --migrate ─────────────────────────────────────────────────────────────
    if args.migrate:
        ver, needs = check_version(conn)
        print(f"Current schema: {ver or '(unknown)'}  "
              f"Target: {EXPECTED_SCHEMA_VERSION}  "
              f"Needs migration: {'yes' if needs else 'no'}")
        if not needs:
            print("Already at target version. Nothing to do.")
            return 0
        if not args.dry_run:
            pre_migration_backup(ver or "unknown")
        applied = run_migrations(conn, dry_run=args.dry_run,
                                  stop_at=args.to, verbose=True)
        if applied:
            print(f"\nApplied: {', '.join(applied)}")
        else:
            print("No migrations applied.")
        return 0

    # ── --register ────────────────────────────────────────────────────────────
    if args.register:
        if not args.word:
            print("[ERROR] --register requires --word", file=sys.stderr)
            return 1
        if not args.source:
            print("[ERROR] --register requires --source", file=sys.stderr)
            return 1
        result = run_register(conn, args.word, args.source, args.category)
        print(f"Registry no: {result['no']}  id: {result['id']}")
        return 0

    # ── --check-locks ─────────────────────────────────────────────────────────
    if args.check_locks:
        locks = check_stale_locks(conn)
        if not locks:
            print("No active IN_PROGRESS sentinels found.")
        else:
            print(f"Active IN_PROGRESS sentinels ({len(locks)}):")
            for lk in locks:
                stale_mark = " [STALE]" if lk["stale"] else ""
                print(f"  no={lk['no']:4}  {lk['word']:<20}  "
                      f"run_id={lk['run_id']}  {lk['age']}{stale_mark}")
        return 0

    # ── --clear-lock ──────────────────────────────────────────────────────────
    if args.clear_lock:
        if not args.registry:
            print("[ERROR] --clear-lock requires --registry=N", file=sys.stderr)
            return 1
        result = run_clear_lock(conn, args.registry, force=args.force)
        if result["cleared"]:
            print(f"Lock cleared for registry {args.registry}.")
        else:
            print(f"[INFO] {result['reason']}")
        return 0 if result["cleared"] else 1

    # ── --report ──────────────────────────────────────────────────────────────
    if args.report:
        if not args.registry:
            print("[ERROR] --report requires --registry=N", file=sys.stderr)
            return 1
        print_word_report(conn, args.registry, format=args.format)
        return 0
    # ── --export-word ─────────────────────────────────────────────────────────
    if getattr(args, "export_word", False):
        if not args.registry:
            print("[ERROR] --export-word requires --registry=N", file=sys.stderr)
            return 1
        if not _EXPORT_AVAILABLE:
            print("[ERROR] analytics.word_export is not importable.", file=sys.stderr)
            return 1
        import json as _json
        from datetime import datetime, timezone
        print(f"Exporting registry {args.registry}...")
        try:
            data = _export_word(conn, args.registry)
        except ValueError as exc:
            print(f"[ERROR] {exc}", file=sys.stderr)
            return 1
        word     = data["_export"]["word"]
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        filename = f"{word}_{args.registry}_full_{date_str}.json"
        out_dir  = os.path.join(_ROOT, "data", "exports")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as fh:
            _json.dump(data, fh, indent=2, ensure_ascii=False, default=str)
        size_kb = os.path.getsize(out_path) / 1024
        stats   = data["statistics"]
        print(f"  Word     : {word}  (registry {args.registry})")
        print(f"  Terms    : {stats['term_count']}  |  Verses: {stats['verse_count']}")
        print(f"  File     : {out_path}  ({size_kb:.1f} KB)")
        return 0
    # ── --mode ────────────────────────────────────────────────────────────────
    if args.mode:
        # gap_fill without --registry = bulk mode; all others require --registry.
        if not args.registry and args.mode != "gap_fill":
            print(f"[ERROR] --mode={args.mode} requires --registry=N", file=sys.stderr)
            return 1

        if args.mode == "new_word":
            if not args.terms:
                print("[ERROR] --mode=new_word requires --terms=H1234,G5678", file=sys.stderr)
                return 1
            strongs_list = [t.strip() for t in args.terms.split(",") if t.strip()]
            if not args.dry_run:
                pre_run_backup(f"NEW_WORD-reg{args.registry}")
            result = run_new_word(
                conn, args.registry, strongs_list,
                dry_run=args.dry_run, force=args.force,
                pause=args.pause,
            )
            if not args.dry_run and result["outcome"] in ("COMPLETE", "PARTIAL"):
                post_run_backup(f"NEW_WORD-reg{args.registry}")
            return 0 if result["outcome"] in ("COMPLETE", "PARTIAL", "DRY_RUN") else 1

        if args.mode == "gap_fill":
            streams = [s.strip() for s in args.streams.split(",")] if args.streams else None
            if args.registry:
                # Single-word gap patch (existing behaviour).
                if not args.dry_run:
                    pre_run_backup(f"GAP_FILL-reg{args.registry}")
                result = run_gap_fill(
                    conn, args.registry, streams=streams, dry_run=args.dry_run,
                )
                if not args.dry_run and result["outcome"] == "COMPLETE":
                    post_run_backup(f"GAP_FILL-reg{args.registry}")
                return 0 if result["outcome"] in ("COMPLETE", "DRY_RUN") else 1
            else:
                # Bulk initialization pass across all Pending words.
                if not args.dry_run:
                    pre_run_backup("BULK_GAP_FILL")
                result = run_bulk_gap_fill(conn, stages=streams, dry_run=args.dry_run)
                if not args.dry_run and result["outcome"] == "COMPLETE":
                    post_run_backup("BULK_GAP_FILL")
                return 0 if result["outcome"] in ("COMPLETE", "DRY_RUN") else 1

        if args.mode == "audit_word":
            if not args.dry_run:
                pre_run_backup(f"AUDIT_WORD-reg{args.registry}")
            result = run_audit_word(
                conn, args.registry,
                dry_run=args.dry_run,
                interactive=getattr(args, "interactive", False),
                extract_file=getattr(args, "extract_file", None),
            )
            if not args.dry_run and result["outcome"] == "COMPLETE":
                post_run_backup(f"AUDIT_WORD-reg{args.registry}")
            return 0 if result["outcome"] in ("COMPLETE", "DRY_RUN") else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
