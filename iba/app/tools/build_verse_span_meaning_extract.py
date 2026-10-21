"""build_verse_span_meaning_extract.py  (READ-ONLY, one-off)

Base-data extract for manual movement analysis: for a book (and chapter range), in verse order,
each verse's text followed by a table of its spans (surface, Strong's, morph) and each span's
meaning. Reads only verse/span/strong*.

Meaning comes from the parsed tables (strong_meaning_parsed, strong_lsj_parsed,
strong_mounce_parsed), looked up per code (a span's strong_variant can hold several codes, e.g.
"G1722 G0054"). All sources are shown together, each on its own labelled line ("(none)" where
empty). meaning_tree prefers the exact strong_variant row; a base-fallback row is flagged
[AMBIGUOUS] when the code's own stepGloss shares no vocabulary with it, and STEP is then called
live for that exact code (memoised per code per run). STEP is required (step.required_for_runs):
the run refuses to build if STEP's preflight fails.

Verse order is osisId parsed as (chapter, verse) numerically, not string order or verse.id.

Coverage: `strong` holds only codes onboarded through a word or backfill, so many spans render
"(not yet registered)", and the intro states the coverage fraction per chapter.

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
from iba.app.lib.stepapi import Step, StepUnavailable

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
    """Every OTHER full strong code in `strong` sharing this base (e.g. H3581A "reptile" and H3581B
    "strength"): used to flag a base-keyed meaning row that may not apply to this code."""
    rows = conn.execute(
        "SELECT strongNumber FROM strong WHERE (strongNumber = ? OR strongNumber LIKE ?) "
        "AND strongNumber != ? ORDER BY strongNumber",
        (base, base + "_", exclude),
    ).fetchall()
    return [r["strongNumber"] for r in rows]


_STOP_TOKENS = {"to", "the", "a", "an", "of", "in", "on", "with", "and", "or", "be", "is",
               "for", "as", "by", "at", "from"}


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", (text or "").lower())
           if len(w) >= 3 and w not in _STOP_TOKENS}


def gloss_supported_by_tree(step_gloss: str, tree_text: str) -> bool:
    """True if the code's own stepGloss (fetched per exact code) shares real vocabulary with the
    base-keyed meaning_tree text: most siblings are the same root's stems (H0935G Qal 'come' / H0935P
    Hiphil 'bring') sharing one legitimate entry, so only no overlap (H3581B 'strength' vs 'reptile')
    marks a genuine collapse."""
    gloss_tok = _tokens(step_gloss)
    tree_tok = _tokens(tree_text)
    if not gloss_tok or not tree_tok:
        return False
    return bool(gloss_tok & tree_tok)


def live_step_meaning(step: "Step | None", code: str, live_cache: dict[str, str]) -> str:
    """Live, per-exact-code meaning via STEP call2_getInfo, for spans whose meaning_tree is
    [AMBIGUOUS]. Memoised per code for one run. `step` is None only when step.required_for_runs is
    explicitly false (a config-authorised degrade)."""
    if code in live_cache:
        return live_cache[code]
    if step is None:
        text = "(STEP unavailable this run, step.required_for_runs=false — resolve manually against STEP for this exact code)"
        live_cache[code] = text
        return text
    try:
        vocabs = step.call2_getInfo(code).get("vocabInfos") or []
    except Exception as e:  # a transient failure after the preflight passed: degrade this one line
        text = f"(STEP lookup failed for {code} mid-run: {e} — resolve manually against STEP)"
        live_cache[code] = text
        return text
    if not vocabs:
        text = f"(STEP returned no vocabInfo for {code})"
        live_cache[code] = text
        return text
    v = vocabs[0]
    resolved = v.get("strongNumber", code)
    medium_def = re.sub(r"<br\s*/?>", "; ", v.get("mediumDef", ""), flags=re.IGNORECASE)
    medium_def = re.sub(r"\s+", " ", medium_def).strip()
    text = f"{resolved}: {medium_def or '(STEP has no mediumDef for this code)'}"
    live_cache[code] = text
    return text


def meaning_for_code(conn: sqlite3.Connection, code: str, step: "Step | None",
                     live_cache: dict[str, str]) -> tuple[str, bool]:
    """Returns (rendered meaning text for ONE Strong's code, covered?). Per code for every source
    keyed that way; meaning_tree is labelled with its base when it comes from a base row. All three
    parse tables are shown together, every time."""
    strong_row = conn.execute(
        "SELECT strongNumber, language, stepGloss FROM strong WHERE strongNumber=?",
        (code,),
    ).fetchone()
    if strong_row is None:
        return "(not yet registered)", False

    base = _base(code)
    lines = [f"stepGloss: {strong_row['stepGloss'] or '(none)'}"]

    # prefer this code's own exact-variant row; fall back to the base row for legacy data
    meaning_rows = conn.execute(
        "SELECT gloss FROM strong_meaning_parsed WHERE strong_variant=? ORDER BY sort, id",
        (code,),
    ).fetchall()
    exact_variant = bool(meaning_rows)
    if not exact_variant:
        meaning_rows = conn.execute(
            "SELECT gloss FROM strong_meaning_parsed WHERE lemma_key=? AND strong_variant=? "
            "ORDER BY sort, id", (base, base),
        ).fetchall()
    meaning_text = "; ".join(r["gloss"] for r in meaning_rows if r["gloss"])
    siblings = sibling_variant_codes(conn, base, exclude=code)
    # an exact strong_variant match is this code's own content, never ambiguous; only a base fallback
    # needs the gloss-overlap check (and a live STEP call when there is no overlap)
    genuinely_ambiguous = (bool(siblings) and meaning_text and not exact_variant and
                          not gloss_supported_by_tree(strong_row["stepGloss"], meaning_text))
    if meaning_text:
        tag = f"variant {code}" if exact_variant else f"base {base} fallback"
        warn = (f" [AMBIGUOUS - base shared with {', '.join(siblings)}, may not be specific "
                f"to {code}]" if genuinely_ambiguous else "")
        lines.append(f"meaning_tree ({tag}){warn}: {meaning_text}")
    else:
        lines.append(f"meaning_tree (base {base}): (none)")
    if genuinely_ambiguous:
        lines.append(f"STEP live ({code}, code-specific): "
                     f"{live_step_meaning(step, code, live_cache)}")

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


def meaning_for(conn: sqlite3.Connection, strong_variant: str | None, step: "Step | None",
                live_cache: dict[str, str]) -> tuple[str, bool]:
    """Returns (rendered meaning text, covered?). Each code of a combined strong_variant is looked up
    and rendered separately."""
    if not strong_variant:
        return "(no Strong's code on this span)", False
    codes = strong_variant.split()
    rendered = []
    any_covered = False
    for code in codes:
        text, covered = meaning_for_code(conn, code, step, live_cache)
        any_covered = any_covered or covered
        rendered.append(f"**{code}**: {text}" if len(codes) > 1 else text)
    return " <br> ".join(rendered), any_covered


def build(book: str, lo: int, hi: int, verse_lo: int | None = None,
         verse_hi: int | None = None, *, cfg: "Cfg") -> list[str]:
    """Reads step.required_for_runs (module 'step', default True; the same setting init.py's preflight
    reads). True: raises StepUnavailable if STEP's preflight fails, and main() refuses. False: proceeds
    STEP-down with a DB-only note on each affected span."""
    required = cfg.setting("step.required_for_runs", True)
    step: Step | None = None
    try:
        ev = Step(cfg).up()
        step = Step(cfg)
        step_status = f"available ({ev['base']}, {ev['version']})"
    except StepUnavailable:
        if required:
            raise  # let main() print the refusal and exit non-zero — no degraded path here
        step_status = ("unavailable — step.required_for_runs=false, proceeding without live "
                       "disambiguation (AMBIGUOUS spans show a DB-only note)")
    live_cache: dict[str, str] = {}

    db_path = Path(__file__).resolve().parents[1] / "db" / "iba.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)

    label = f"{lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else f"{lo}-{hi}"
    L = [f"# {book} {label} -- verse : span : meaning base-data extract", "",
         "> Read-only extract for manual movement analysis. Verse order = osisId parsed numerically "
         "(chapter, verse), not table-id order. No candidate/passage data involved (that layer is "
         "retired). Meaning is only as complete as the Strong's codes registered so far via word "
         "onboarding -- coverage per chapter is stated below, not silently omitted.", "",
         f"> STEP live disambiguation (for [AMBIGUOUS] spans only): {step_status}", ""]

    per_chapter_total: dict[int, int] = {}
    per_chapter_covered: dict[int, int] = {}
    for v in verses:
        spans = fetch_spans(conn, v["id"])
        for sp in spans:
            if sp["is_particle"]:
                continue
            per_chapter_total[v["chapter"]] = per_chapter_total.get(v["chapter"], 0) + 1
            _, covered = meaning_for(conn, sp["strong_variant"], step, live_cache)
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
            meaning, _ = meaning_for(conn, sp["strong_variant"], step, live_cache)
            L.append(f"| {sp['position']} | {sp['surface'] or ''} | {sp['strong_variant'] or ''} | "
                     f"{sp['morph_code'] or ''} | {'yes' if sp['is_particle'] else ''} | {meaning} |")
        L.append("")

    conn.close()
    return L


def main() -> int:
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

    cfg = Cfg()
    try:
        # build() raises StepUnavailable when STEP is required and down: print the refusal and exit
        # non-zero, like every other STEP-dependent tool
        try:
            if args.vrange:
                ch, vlo, vhi = parse_range(args.vrange)
                lo = hi = ch
                lines = build(args.book, lo, hi, vlo, vhi, cfg=cfg)
                topic = f"{args.book.lower()}-{ch}-{vlo}-{vhi}-verse-span-meaning"
            else:
                lo, hi = parse_chapters(args.chapters)
                lines = build(args.book, lo, hi, cfg=cfg)
                topic = f"{args.book.lower()}-{args.chapters}-verse-span-meaning"
        except StepUnavailable as e:
            print(f"STEP not ready: {e}")
            print("start the local STEP server, then re-run this. Refusing to build a report "
                  "without it (step.required_for_runs=true; this report depends on STEP for "
                  "AMBIGUOUS-span disambiguation).")
            return 1

        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            out_path = oneoff_path(cfg, topic)
    finally:
        cfg.close()

    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
