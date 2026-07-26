"""build_verse_span_meaning_extract.py  (READ-ONLY, one-off)

Base-data extract for manual movement analysis: for a book (and chapter range), in true verse
sequence, render each verse's text followed by a table of its spans (surface, Strong's, morph)
and each span's meaning. No candidate/passage machinery involved — that layer is retired
(GOVERNANCE.md 15D); this reads only verse/span/strong*.

UPDATED 2026-07-25, THREE TIMES in the same day's line of work, all real regressions/defects this
report had silently picked up without being touched itself:

  1. Meaning source switched from the RAW, unparsed strong_meaning_tree.sense_text/strong_lexicon.
     mounce (HTML tags, un-scoped refs/notes, false comma-splitting — all bugs fixed this session,
     see lib/lexiconparse.py) to the CORRECTED, PARSED strong_meaning_parsed/strong_mounce_parsed
     tables (migration/bootstrap_lexicon_parsed_layer.py). strong_sense.head is dropped entirely —
     strong_meaning_parsed's glosses supersede it with the same underlying source, better parsed.
  2. Per-span meaning lookup is now PER-CODE, not per-row: since the SAME day's earlier span-model
     fix (BUILD.md 16), span.strong_variant can hold more than one code together (STEP's own HTML
     combines them on one <span> tag, e.g. "G1722 G0054" on "purity" — a real combined unit, not
     duplication). The old single blind lookup on the whole (possibly multi-code) string matched
     nothing for any combined row — confirmed live: 2636 of 5253 Daniel spans (50%) would have
     silently shown "no meaning captured" without this fix, despite real coverage existing.
  3. Researcher's correction (found live via H3581B): "the report is not working strictly with the
     strong variant" and "meaning means considering the three parse files together, not pick the
     first one." Both real. (a) The old renderer looked up strong_meaning_parsed by BASE lemma_key
     and presented it as if specific to the exact span code — but a base can be shared by genuine
     homonyms (H3581A "reptile" vs H3581B "strength", same accentedUnicode/transliteration,
     unrelated meanings), so the wrong sub-entry's sense could be shown with no indication it might
     not apply. Now labeled with its base and an explicit [AMBIGUOUS...] flag naming the sibling
     codes whenever the base isn't unique to this span's code — meaning_tree cannot be MADE
     code-specific (that's a property of the source data), but it can stop being presented as if it
     already were. (b) stepGloss/meaning_tree/lsj/mounce were a priority cascade (stop at the first
     non-empty), and lsj was excluded outright. Now all applicable sources are shown together, every
     time, each on its own labeled line — "(none)" where a source has nothing, not silently omitted.

Verse order is derived from osisId parsed as (chapter, verse) NUMERICALLY, not string-sorted and
not by verse.id (id reflects onboarding-run insertion order across many different word registrations,
not a clean by-book build) -- the same class of bug BUILD.md 5 already found once for book order.

Coverage caveat (real, not a defect): `strong`/etc. are only populated for Strong's codes that came
in through a word's own `raw.detail` onboarding (word_registry), not a full-Bible lexical import.
Most spans in an arbitrary passage will have NO row here yet. Each such span is rendered with an
explicit "(not yet registered)" marker, never a blank cell, and the report's own intro states the
coverage fraction per chapter so the gap is visible up front, not discovered mid-read.

Usage:
  python -m iba.app.tools.build_verse_span_meaning_extract --book Dan --chapters 1-3
  python -m iba.app.tools.build_verse_span_meaning_extract --book Dan --chapters 1
  python -m iba.app.tools.build_verse_span_meaning_extract --book Dan --range 1:1-7
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

BASE_RE = re.compile(r"^([HG]\d+)([A-Z]?)$")  # same pattern as handlers/raw.py:_base


def _base(code: str) -> str:
    m = BASE_RE.match(code or "")
    return m.group(1) if m else (code or "")


def parse_chapters(spec: str) -> tuple[int, int]:
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return int(lo), int(hi)
    n = int(spec)
    return n, n


def parse_range(spec: str) -> tuple[int, int, int]:
    """"chapter:verse-verse" (e.g. "1:1-7") or "chapter:verse" (e.g. "1:5") -> (chapter, lo, hi),
    a single-chapter verse-level range — for a study passage narrower than a whole chapter."""
    ch, sep, vspec = spec.partition(":")
    if not sep:
        raise ValueError(f"--range needs chapter:verse[-verse], e.g. 1:1-7 (got {spec!r})")
    if "-" in vspec:
        vlo, vhi = vspec.split("-", 1)
        return int(ch), int(vlo), int(vhi)
    n = int(vspec)
    return int(ch), n, n


def fetch_verses(conn: sqlite3.Connection, book: str, lo: int, hi: int,
                 verse_lo: int | None = None, verse_hi: int | None = None) -> list[dict]:
    """lo/hi bound the CHAPTER; verse_lo/verse_hi, if given, further bound the VERSE within that
    chapter range (only meaningful when lo == hi — a single-chapter verse-level slice)."""
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
        if not (lo <= ch_n <= hi):
            continue
        if verse_lo is not None and not (verse_lo <= vn_n <= verse_hi):
            continue
        out.append({"id": r["id"], "chapter": ch_n, "verse": vn_n,
                    "reference": r["reference"], "text": r["text"]})
    out.sort(key=lambda x: (x["chapter"], x["verse"]))
    return out


def fetch_spans(conn: sqlite3.Connection, verse_id: int) -> list[dict]:
    return [dict(r) for r in conn.execute(
        "SELECT position, surface, strong_variant, morph_code, is_particle "
        "FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", (verse_id,),
    ).fetchall()]


def sibling_variant_codes(conn: sqlite3.Connection, base: str, exclude: str) -> list[str]:
    """Every OTHER full strong code in `strong` sharing this base — e.g. base H3581 has both
    H3581A and H3581B, two genuinely different homonyms (confirmed live: H3581A="reptile",
    H3581B="strength", same accentedUnicode/transliteration, unrelated meanings). strong_
    meaning_tree/strong_meaning_parsed is base-keyed only (it collapses sub-entry letters), so
    when siblings exist its content is NOT reliably specific to any one of them — this is used to
    flag that ambiguity explicitly instead of silently presenting it as if it were."""
    rows = conn.execute(
        "SELECT strongNumber FROM strong WHERE (strongNumber = ? OR strongNumber LIKE ?) "
        "AND strongNumber != ? ORDER BY strongNumber",
        (base, base + "_", exclude),
    ).fetchall()
    return [r["strongNumber"] for r in rows]


def meaning_for_code(conn: sqlite3.Connection, code: str) -> tuple[str, bool]:
    """Returns (rendered meaning text for ONE Strong's code, covered?). Strictly per-code for
    every source keyed that way (strong, strong_lsj_parsed, strong_mounce_parsed); meaning_tree is
    base-keyed in the SOURCE data itself (cannot be made code-specific here), so it is labeled with
    its base and flagged when siblings make it ambiguous, never silently merged in as if exact.
    ALL THREE parse tables (meaning_tree, lsj, mounce) are shown together, every time — not a
    cascade that stops at the first one with content."""
    strong_row = conn.execute(
        "SELECT strongNumber, language, stepGloss FROM strong WHERE strongNumber=?",
        (code,),
    ).fetchone()
    if strong_row is None:
        return "(not yet registered)", False

    base = _base(code)
    lines = [f"stepGloss: {strong_row['stepGloss'] or '(none)'}"]

    meaning_rows = conn.execute(
        "SELECT gloss FROM strong_meaning_parsed WHERE lemma_key=? ORDER BY sort, id",
        (base,),
    ).fetchall()
    meaning_text = "; ".join(r["gloss"] for r in meaning_rows if r["gloss"])
    if meaning_text:
        siblings = sibling_variant_codes(conn, base, exclude=code)
        warn = (f" [AMBIGUOUS - base shared with {', '.join(siblings)}, may not be specific "
                f"to {code}]" if siblings else "")
        lines.append(f"meaning_tree (base {base}){warn}: {meaning_text}")
    else:
        lines.append(f"meaning_tree (base {base}): (none)")

    if strong_row["language"] == "Greek":
        lsj_rows = conn.execute(
            "SELECT gloss FROM strong_lsj_parsed WHERE strong=? AND row_type='lookup' "
            "ORDER BY id", (code,),
        ).fetchall()
        lsj_text = "; ".join(r["gloss"] for r in lsj_rows if r["gloss"])
        lines.append(f"lsj: {lsj_text or '(none)'}")

        mounce_rows = conn.execute(
            "SELECT mounce_parsed FROM strong_mounce_parsed WHERE strong=? ORDER BY id",
            (code,),
        ).fetchall()
        mounce_text = "; ".join(r["mounce_parsed"] for r in mounce_rows if r["mounce_parsed"])
        lines.append(f"mounce: {mounce_text or '(none)'}")

    return " <br> ".join(lines), True


def meaning_for(conn: sqlite3.Connection, strong_variant: str | None) -> tuple[str, bool]:
    """Returns (rendered meaning text, covered?). strong_variant may hold more than one code
    (STEP's HTML combines them on one <span> tag, e.g. "G1722 G0054" — see BUILD.md 16) — each is
    looked up and rendered separately, since a combined tag's codes can have very different
    coverage (a function word with none vs. a content word with plenty)."""
    if not strong_variant:
        return "(no Strong's code on this span)", False
    codes = strong_variant.split()
    rendered = []
    any_covered = False
    for code in codes:
        text, covered = meaning_for_code(conn, code)
        any_covered = any_covered or covered
        rendered.append(f"**{code}**: {text}" if len(codes) > 1 else text)
    return " <br> ".join(rendered), any_covered


def build(book: str, lo: int, hi: int, verse_lo: int | None = None,
         verse_hi: int | None = None) -> list[str]:
    db_path = Path(__file__).resolve().parents[1] / "db" / "iba.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)

    label = f"{lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else f"{lo}-{hi}"
    L = [f"# {book} {label} -- verse : span : meaning base-data extract", "",
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
    ap.add_argument("--chapters", help="whole-chapter range, e.g. 1-3 or 1")
    ap.add_argument("--range", dest="vrange",
                    help="single-chapter verse range, e.g. 1:1-7 -- for a study passage narrower "
                         "than a whole chapter. Mutually exclusive with --chapters.")
    ap.add_argument("--out", default=None, help="override output path")
    args = ap.parse_args()

    if bool(args.chapters) == bool(args.vrange):
        ap.error("give exactly one of --chapters or --range")

    if args.vrange:
        ch, vlo, vhi = parse_range(args.vrange)
        lo = hi = ch
        lines = build(args.book, lo, hi, vlo, vhi)
        topic = f"{args.book.lower()}-{ch}-{vlo}-{vhi}-verse-span-meaning"
    else:
        lo, hi = parse_chapters(args.chapters)
        lines = build(args.book, lo, hi)
        topic = f"{args.book.lower()}-{args.chapters}-verse-span-meaning"

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        cfg = Cfg()
        out_path = oneoff_path(cfg, topic)
        cfg.close()

    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
