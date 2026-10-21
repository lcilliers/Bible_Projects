"""build_verse_span_strongtree_extract.py  (READ-ONLY, one-off)

Literal, non-interpretive base-data dump, per verse, in verse sequence:
  a) the verse record (every column, verse table)
  b) the span records for that verse (every column, span table, position order)
  c) for each DISTINCT strong_variant appearing in (b), every strong_meaning_tree row
     keyed on that lemma_key (every column, sort order)

No merged "meaning" field, no morph decoding, no grouping/interpretation of any kind --
raw table records only, kept together per verse. Verse order = osisId parsed as
(chapter, verse) numerically, not table-id order (verse.id reflects onboarding-run
insertion order, not a clean by-book build).

Usage:
  python -m iba.app.tools.build_verse_span_strongtree_extract --book Dan --chapter 1 --verses 1-7
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from iba.app.lib.cfg import Cfg
from iba.app.lib.reportkit import oneoff_path


def parse_range(spec: str) -> tuple[int, int]:
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return int(lo), int(hi)
    n = int(spec)
    return n, n


def fetch_verses(conn: sqlite3.Connection, book: str, chapter: int, v_lo: int, v_hi: int) -> list[sqlite3.Row]:
    rows = conn.execute(
        "SELECT * FROM verse WHERE osisId LIKE ? AND deleted=0", (f"{book}.{chapter}.%",),
    ).fetchall()
    out = []
    for r in rows:
        parts = (r["osisId"] or "").split(".")
        if len(parts) != 3 or parts[0] != book or not parts[2].isdigit():
            continue
        vn = int(parts[2])
        if v_lo <= vn <= v_hi:
            out.append((vn, r))
    out.sort(key=lambda t: t[0])
    return [r for _, r in out]


def render_row(row: sqlite3.Row) -> list[str]:
    """Verbatim -- the raw column value as stored, no Python repr() escaping/quoting."""
    return [f"- `{k}` = {row[k] if row[k] is not None else ''}" for k in row.keys()]


BASE_RE = re.compile(r"^([HG]\d+)([A-Z]?)$")


def base_lemma(code: str) -> str | None:
    """strong_meaning_tree is keyed on the BASE lemma (no sub-letter) -- one tree per lemma,
    shared across sub-lettered strong_variants (BUILD.md D3). Returns None if code has no
    sub-letter (nothing to fall back to)."""
    m = BASE_RE.match(code or "")
    if m and m.group(2):
        return m.group(1)
    return None


def build(book: str, chapter: int, v_lo: int, v_hi: int) -> list[str]:
    db_path = Path(__file__).resolve().parents[1] / "db" / "iba.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    verses = fetch_verses(conn, book, chapter, v_lo, v_hi)

    L = [f"# {book} {chapter}:{v_lo}-{v_hi} -- literal verse / span / strong_meaning_tree dump", "",
         "> Raw table records only, no merging or decoding, kept together per verse. "
         "(a) verse table row, (b) span table rows in position order, "
         "(c) strong_meaning_tree rows for every DISTINCT strong_variant in (b), in first-seen order.",
         ""]

    for v in verses:
        L.append(f"## {v['reference']}")
        L.append("")
        L.append("### a) verse record")
        L.append("")
        L += render_row(v)
        L.append("")

        spans = conn.execute(
            "SELECT * FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", (v["id"],),
        ).fetchall()

        L.append("### b) span records")
        L.append("")
        cols = spans[0].keys() if spans else []
        L.append("| " + " | ".join(cols) + " |")
        L.append("| " + " | ".join("---" for _ in cols) + " |")
        for sp in spans:
            L.append("| " + " | ".join(str(sp[c]) if sp[c] is not None else "" for c in cols) + " |")
        L.append("")

        seen: list[str] = []
        for sp in spans:
            sv = sp["strong_variant"]
            if sv and sv not in seen:
                seen.append(sv)

        L.append("### c) strong_meaning_tree records, per distinct strong_variant")
        L.append("")
        for sv in seen:
            L.append(f"**{sv}**")
            L.append("")
            tree_rows = conn.execute(
                "SELECT * FROM strong_meaning_tree WHERE lemma_key=? ORDER BY sort", (sv,),
            ).fetchall()
            matched_key = sv
            if not tree_rows:
                fallback = base_lemma(sv)
                if fallback:
                    tree_rows = conn.execute(
                        "SELECT * FROM strong_meaning_tree WHERE lemma_key=? ORDER BY sort", (fallback,),
                    ).fetchall()
                    matched_key = fallback
            if not tree_rows:
                L.append(f"- (no strong_meaning_tree row for `{sv}`, tried base lemma too)")
            else:
                if matched_key != sv:
                    L.append(f"- (no row for `{sv}` itself -- these rows are its base lemma `{matched_key}`, "
                              f"per BUILD.md D3: one tree per lemma, shared across sub-lettered variants)")
                for t in tree_rows:
                    L += render_row(t)
            L.append("")

        L.append("---")
        L.append("")

    conn.close()
    return L


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", required=True, type=int)
    ap.add_argument("--verses", required=True, help="e.g. 1-7 or 4")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    v_lo, v_hi = parse_range(args.verses)
    lines = build(args.book, args.chapter, v_lo, v_hi)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        cfg = Cfg()
        out_path = oneoff_path(cfg, f"{args.book.lower()}-{args.chapter}-{args.verses}-verse-span-strongtree")
        cfg.close()

    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
