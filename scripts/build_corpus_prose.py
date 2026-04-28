"""build_corpus_prose.py — Compile completed word-analysis chapters into a book.

Reads `prose_section` rows for every registry whose `session_b_status` is
'Analysis Complete' (or 'Session B Complete') and produces a single
book-style markdown file: word-by-word, each word with its 5 Stage 2c chapters
in chapter order. Optionally per-word breakouts and an included Phase A summary.

Output destination: `Workflow/Programme/Corpus_prose/`

Default output filename: `wa-corpus-prose-{YYYYMMDD}.md` (book) plus
`wa-corpus-prose-toc-{YYYYMMDD}.md` (table-of-contents).

Read-only against `database/bible_research.db`. No DB writes. No analytics.

Usage:
  # Default: book-style consolidated .md of all 'Analysis Complete' registries
  python scripts/build_corpus_prose.py

  # Single registry
  python scripts/build_corpus_prose.py --registry 30

  # Also produce per-word breakouts
  python scripts/build_corpus_prose.py --per-word

  # Include the Phase A summary (sa_s1_d1 — Word Summary) as an opener per word
  python scripts/build_corpus_prose.py --include-session-a

  # Custom output directory
  python scripts/build_corpus_prose.py --out-dir Workflow/Programme/Corpus_prose

  # Include words that are still 'In Progress' (e.g. for proof-reading)
  python scripts/build_corpus_prose.py --include-in-progress
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Programme", "Corpus_prose")

# Stage 2c chapter codes (from prose_section_type)
CHAPTER_ORDER = [
    ("sb_s2c_ch1", "Chapter 1 — Meaning"),
    ("sb_s2c_ch2", "Chapter 2 — How It Works"),
    ("sb_s2c_ch3", "Chapter 3 — Verses"),
    ("sb_s2c_ch4", "Chapter 4 — Language"),
    ("sb_s2c_ch5", "Chapter 5 — Interrelationships"),
]

# Default Session B completion statuses we include in the book
COMPLETE_STATUSES = ("Analysis Complete", "Session B Complete")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def get_registries(conn, registry_no: int | None, include_in_progress: bool) -> list:
    """Return word_registry rows for inclusion."""
    if registry_no is not None:
        rows = conn.execute(
            "SELECT * FROM word_registry WHERE no = ?", (registry_no,)
        ).fetchall()
        return [dict(r) for r in rows]

    statuses = list(COMPLETE_STATUSES)
    if include_in_progress:
        statuses += ["Pre-Analysis Complete", "In Progress"]
    placeholders = ",".join("?" * len(statuses))
    rows = conn.execute(
        f"SELECT * FROM word_registry WHERE session_b_status IN ({placeholders}) ORDER BY no",
        statuses,
    ).fetchall()
    return [dict(r) for r in rows]


def get_chapter_body(conn, registry_id: int, code: str) -> dict | None:
    """Return the current (non-superseded) chapter row for this slot, or None."""
    r = conn.execute("""
        SELECT ps.id, ps.heading, ps.body, ps.version, ps.author, ps.status,
               ps.created_at, length(ps.body) AS len
          FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
         WHERE ps.registry_id = ?
           AND pst.code = ?
           AND ps.superseded_by_id IS NULL
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
         LIMIT 1
    """, (registry_id, code)).fetchone()
    return dict(r) if r else None


def get_session_a_summary(conn, registry_id: int) -> dict | None:
    """Return the sa_s1_d1 Phase A Word Summary, if present."""
    r = conn.execute("""
        SELECT ps.heading, ps.body
          FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
         WHERE ps.registry_id = ?
           AND pst.code = 'sa_s1_d1'
           AND ps.superseded_by_id IS NULL
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
         LIMIT 1
    """, (registry_id,)).fetchone()
    return dict(r) if r else None


def render_word(reg: dict, conn, include_session_a: bool) -> tuple[str, dict]:
    """Render a single word's section. Returns (text, stats)."""
    L = []
    word_title = reg["word"].title()
    L.append(f"## {reg['no']:03d} — {word_title}")
    L.append("")

    # Frontmatter
    bits = []
    bits.append(f"**Status:** {reg.get('session_b_status') or '—'}")
    if reg.get("dim_review_status"):
        bits.append(f"**Dimension review:** {reg['dim_review_status']}")
    if reg.get("verse_context_status"):
        bits.append(f"**Verse Context:** {reg['verse_context_status']}")
    L.append("  ·  ".join(bits))
    L.append("")

    if reg.get("description"):
        L.append("> " + reg["description"].replace("\n", "\n> "))
        L.append("")

    if reg.get("word_synopsis"):
        L.append("**Synopsis:**")
        L.append("")
        L.append(reg["word_synopsis"])
        L.append("")

    chapters_present = 0
    chapters_missing = []

    if include_session_a:
        sa = get_session_a_summary(conn, reg["id"])
        if sa:
            L.append("### Phase A — Word Summary")
            L.append("")
            L.append(sa["body"])
            L.append("")

    for code, label in CHAPTER_ORDER:
        ch = get_chapter_body(conn, reg["id"], code)
        if not ch:
            chapters_missing.append(code)
            continue
        chapters_present += 1
        L.append(f"### {label}")
        L.append("")
        if ch.get("heading") and ch["heading"].lower() != label.split("—", 1)[1].strip().lower():
            # Chapter has a custom heading from author — show it
            L.append(f"_{ch['heading']}_")
            L.append("")
        L.append(ch["body"])
        L.append("")

    if chapters_missing:
        L.append(f"_Chapters not yet captured: {', '.join(chapters_missing)}_")
        L.append("")

    L.append("---")
    L.append("")

    stats = {
        "no": reg["no"],
        "word": reg["word"],
        "chapters_present": chapters_present,
        "chapters_missing": chapters_missing,
    }
    return "\n".join(L), stats


def render_book(registries: list, conn, include_session_a: bool) -> str:
    L = []
    L.append("# Word Analysis Corpus — Programme Reading")
    L.append("")
    L.append(f"_Generated {now_iso()}_")
    L.append("")
    L.append(f"_{len(registries)} word(s) included._")
    L.append("")
    L.append("---")
    L.append("")

    for reg in registries:
        text, _stats = render_word(reg, conn, include_session_a)
        L.append(text)
    return "\n".join(L)


def render_toc(stats_list: list) -> str:
    L = []
    L.append("# Word Analysis Corpus — Table of Contents")
    L.append("")
    L.append(f"_Generated {now_iso()}_")
    L.append("")
    L.append("| Reg | Word | Chapters | Notes |")
    L.append("|---:|---|---:|---|")
    for s in stats_list:
        notes = ""
        if s["chapters_missing"]:
            notes = f"missing: {', '.join(s['chapters_missing'])}"
        L.append(f"| {s['no']:03d} | {s['word'].title()} | {s['chapters_present']}/5 | {notes} |")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build word-analysis corpus prose book")
    ap.add_argument("--registry", type=int, default=None, help="Single registry no")
    ap.add_argument("--out-dir", default=OUT_DIR)
    ap.add_argument("--per-word", action="store_true",
                    help="Also produce one .md per word in the same folder")
    ap.add_argument("--include-session-a", action="store_true",
                    help="Include the Phase A Word Summary as an opener per word")
    ap.add_argument("--include-in-progress", action="store_true",
                    help="Also include 'Pre-Analysis Complete' and 'In Progress' words")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    registries = get_registries(conn, args.registry, args.include_in_progress)
    if not registries:
        print("No registries match the criteria.")
        return 1

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = today_compact()

    # Always: consolidated book
    book_text = render_book(registries, conn, args.include_session_a)
    suffix = f"-r{args.registry:03d}" if args.registry else ""
    book_path = out_dir / f"wa-corpus-prose{suffix}-{today}.md"
    book_path.write_text(book_text, encoding="utf-8")
    print(f"Wrote book:  {book_path}  ({book_path.stat().st_size:,} bytes)")

    # TOC
    stats_list = []
    for reg in registries:
        _t, st = render_word(reg, conn, args.include_session_a)
        stats_list.append(st)
    toc_path = out_dir / f"wa-corpus-prose-toc{suffix}-{today}.md"
    toc_path.write_text(render_toc(stats_list), encoding="utf-8")
    print(f"Wrote TOC:   {toc_path}")

    # Per-word
    if args.per_word:
        for reg in registries:
            text, _stats = render_word(reg, conn, args.include_session_a)
            slug = reg["word"].lower().replace(" ", "_")
            pw_path = out_dir / f"wa-{reg['no']:03d}-{slug}-corpus-prose-{today}.md"
            pw_path.write_text(text, encoding="utf-8")
            print(f"Wrote word:  {pw_path}")

    # Console summary
    print()
    print(f"Words rendered: {len(registries)}")
    full = sum(1 for s in stats_list if not s["chapters_missing"])
    partial = len(stats_list) - full
    print(f"  Full (5/5 chapters): {full}")
    print(f"  Partial:             {partial}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
