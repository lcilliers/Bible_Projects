"""build_verse_span_meaning_extract.py  (READ-ONLY, one-off)

Base-data extract for manual movement analysis: for a book (and chapter range), in true verse
sequence, render each verse's text followed by a table of its spans (surface, Strong's, morph)
and each span's meaning (Hebrew: strong_sense.head + strong_meaning_tree.sense_text; Greek: the
same plus strong_lexicon.mounce). No candidate/passage machinery involved — that layer is retired
(GOVERNANCE.md 15D); this reads only verse/span/strong*.

Verse order is derived from osisId parsed as (chapter, verse) NUMERICALLY, not string-sorted and
not by verse.id (id reflects onboarding-run insertion order across many different word registrations,
not a clean by-book build) -- the same class of bug BUILD.md 5 already found once for book order.

Coverage caveat (real, not a defect): `strong`/`strong_sense`/etc. are only populated for Strong's
codes that came in through a word's own `raw.detail` onboarding (word_registry), not a full-Bible
lexical import. Most spans in an arbitrary passage will have NO row here yet. Each such span is
rendered with an explicit "(no meaning captured -- word not yet registered)" marker, never a blank
cell, and the report's own intro states the coverage fraction per chapter so the gap is visible up
front, not discovered mid-read.

Usage:
  python -m iba.app.tools.build_verse_span_meaning_extract --book Dan --chapters 1-3
  python -m iba.app.tools.build_verse_span_meaning_extract --book Dan --chapters 1
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from iba.app.lib.cfg import Cfg
from iba.app.lib.reportkit import oneoff_path


def parse_chapters(spec: str) -> tuple[int, int]:
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return int(lo), int(hi)
    n = int(spec)
    return n, n


def fetch_verses(conn: sqlite3.Connection, book: str, lo: int, hi: int) -> list[dict]:
    rows = conn.execute(
        "SELECT id, osisId, reference, text FROM verse WHERE osisId LIKE ? AND deleted=0",
        (f"{book}.%",),
    ).fetchall()
    out = []
    for r in rows:
        parts = (r["osisId"] or "").split(".")
        if len(parts) != 3 or parts[0] != book:
            continue
        _, ch, vn = parts
        if not ch.isdigit() or not vn.isdigit():
            continue
        ch_n, vn_n = int(ch), int(vn)
        if lo <= ch_n <= hi:
            out.append({"id": r["id"], "chapter": ch_n, "verse": vn_n,
                        "reference": r["reference"], "text": r["text"]})
    out.sort(key=lambda x: (x["chapter"], x["verse"]))
    return out


def fetch_spans(conn: sqlite3.Connection, verse_id: int) -> list[dict]:
    return [dict(r) for r in conn.execute(
        "SELECT position, surface, strong_variant, morph_code, is_particle "
        "FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", (verse_id,),
    ).fetchall()]


def meaning_for(conn: sqlite3.Connection, strong_variant: str | None) -> tuple[str, bool]:
    """Returns (rendered meaning text, covered?)."""
    if not strong_variant:
        return "(no Strong's code on this span)", False
    strong_row = conn.execute(
        "SELECT strongNumber, language, stepGloss FROM strong WHERE strongNumber=?",
        (strong_variant,),
    ).fetchone()
    if strong_row is None:
        return "(no meaning captured -- word not yet registered)", False
    parts = []
    sense = conn.execute("SELECT head FROM strong_sense WHERE strong=?", (strong_variant,)).fetchone()
    if sense and sense["head"]:
        parts.append(sense["head"])
    tree = conn.execute(
        "SELECT sense_text FROM strong_meaning_tree WHERE lemma_key=? ORDER BY sort",
        (strong_variant,),
    ).fetchall()
    tree_text = "; ".join(t["sense_text"] for t in tree if t["sense_text"])
    if tree_text and tree_text not in parts:
        parts.append(tree_text)
    if strong_row["language"] == "Greek":
        lex = conn.execute("SELECT mounce FROM strong_lexicon WHERE strong=?", (strong_variant,)).fetchone()
        if lex and lex["mounce"] and lex["mounce"] not in parts:
            parts.append(f"Mounce: {lex['mounce']}")
    if not parts and strong_row["stepGloss"]:
        parts.append(strong_row["stepGloss"])
    return (" | ".join(parts) if parts else "(strong row present, no sense text)"), True


def build(book: str, lo: int, hi: int) -> list[str]:
    db_path = Path(__file__).resolve().parents[1] / "db" / "iba.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    verses = fetch_verses(conn, book, lo, hi)

    L = [f"# {book} {lo}-{hi} -- verse : span : meaning base-data extract", "",
         "> Read-only extract for manual movement analysis. Verse order = osisId parsed numerically "
         "(chapter, verse), not table-id order. No candidate/passage data involved (that layer is "
         "retired). Meaning is only as complete as the Strong's codes registered so far via word "
         "onboarding -- coverage per chapter is stated below, not silently omitted.", ""]

    per_chapter_total: dict[int, int] = {}
    per_chapter_covered: dict[int, int] = {}
    for v in verses:
        spans = fetch_spans(conn, v["id"])
        for sp in spans:
            if sp["is_particle"]:
                continue
            per_chapter_total[v["chapter"]] = per_chapter_total.get(v["chapter"], 0) + 1
            _, covered = meaning_for(conn, sp["strong_variant"])
            if covered:
                per_chapter_covered[v["chapter"]] = per_chapter_covered.get(v["chapter"], 0) + 1

    L.append("## Meaning coverage (non-particle spans, this range)")
    L.append("")
    L.append("| chapter | covered | total | % |")
    L.append("| --- | --- | --- | --- |")
    for ch in sorted(per_chapter_total):
        tot = per_chapter_total[ch]
        cov = per_chapter_covered.get(ch, 0)
        L.append(f"| {ch} | {cov} | {tot} | {round(100 * cov / tot) if tot else 0}% |")
    L.append("")
    L.append("---")
    L.append("")

    for v in verses:
        L.append(f"## {v['reference']}")
        L.append("")
        L.append(v["text"] or "")
        L.append("")
        spans = fetch_spans(conn, v["id"])
        L.append("| # | surface | strong | morph | particle | meaning |")
        L.append("| --- | --- | --- | --- | --- | --- |")
        for sp in spans:
            meaning, _ = meaning_for(conn, sp["strong_variant"])
            L.append(f"| {sp['position']} | {sp['surface'] or ''} | {sp['strong_variant'] or ''} | "
                     f"{sp['morph_code'] or ''} | {'yes' if sp['is_particle'] else ''} | {meaning} |")
        L.append("")

    conn.close()
    return L


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True, help="OSIS book code as stored in verse.osisId, e.g. Dan")
    ap.add_argument("--chapters", required=True, help="e.g. 1-3 or 1")
    ap.add_argument("--out", default=None, help="override output path")
    args = ap.parse_args()

    lo, hi = parse_chapters(args.chapters)
    lines = build(args.book, lo, hi)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        cfg = Cfg()
        out_path = oneoff_path(cfg, f"{args.book.lower()}-{args.chapters}-verse-span-meaning")
        cfg.close()

    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
