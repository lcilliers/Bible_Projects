"""versespanmeaningreport.py — the governed copy of `tools/build_verse_span_meaning_extract.py`'s
verse : span : meaning extract, registered as a real report (`report.verse_span_meaning`) instead
of a one-off `tools/` script. Per established precedent (BUILD.md §17: "ported again into the app's
own governed copy — the tools/ scripts stay standalone/independent, not imported from"), this is a
separate copy, not an import of the tools/ module.

Output location is config, not hardcoded: `report.verse_analysis_output_dir` (base folder) +
a per-call `book_label` subfolder (e.g. "Daniel" — a caller-supplied parameter, not a setting,
same boundary as `table_export`'s -Out/-Table: which book folder a given call writes into varies
per invocation, it isn't a rule) + `report.verse_analysis_output_pattern` (filename template).

STEP is used for [AMBIGUOUS]-span live disambiguation (see tools/build_verse_span_meaning_extract.py's
2026-07-26 note for the full history). Reads the shared `step.required_for_runs` cfg_setting — same
row `init.py`'s own startup preflight reads (governance.rules_must_be_config_driven) — rather than
hardcoding its own copy of the rule.
"""

from __future__ import annotations

import pathlib
import re
import sqlite3

from . import reportkit
from .stepapi import Step, StepUnavailable

BASE_RE = re.compile(r"^([HG]\d+)([A-Z]?)$")


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
    ch, sep, vspec = spec.partition(":")
    if not sep:
        raise ValueError(f"range needs chapter:verse[-verse], e.g. 1:1-7 (got {spec!r})")
    if "-" in vspec:
        vlo, vhi = vspec.split("-", 1)
        return int(ch), int(vlo), int(vhi)
    n = int(vspec)
    return int(ch), n, n


def fetch_verses(conn: sqlite3.Connection, book: str, lo: int, hi: int,
                 verse_lo: int | None = None, verse_hi: int | None = None) -> list[dict]:
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


_STOP_TOKENS = {"to", "the", "a", "an", "of", "in", "on", "with", "and", "or", "be", "is",
               "for", "as", "by", "at", "from"}


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", (text or "").lower())
           if len(w) >= 3 and w not in _STOP_TOKENS}


def gloss_supported_by_tree(step_gloss: str, tree_text: str) -> bool:
    """True if the code's OWN stepGloss (fetched fresh per exact code, never base-collapsed —
    see handlers/raw.py:detail_one — so it is never itself wrong) shares real vocabulary with the
    base-keyed meaning_tree text. Confirmed 2026-07-26 (researcher's direct challenge on H0935G):
    of 470 sub-lettered codes sharing a base with a sibling, 362 (77%) are like H0935G/H0935P —
    the SAME root's different stems (Qal 'come' vs Hiphil 'bring'), where the shared tree is a
    normal single combined dictionary entry, already stem-labeled ("(Qal)...(Hiphil)..."), and
    stepGloss's own word already appears in it — NOT a genuine collapse/data-loss the way
    H3581A/B is (stepGloss 'strength' vs the shared tree's unrelated 'reptile' content, zero
    overlap). Flagging [AMBIGUOUS] and paying for a live STEP call for every sibling regardless
    was wrong: `strong.stepGloss` already answers the question for the H0935G-shaped majority
    with no ambiguity and no network call needed at all."""
    gloss_tok = _tokens(step_gloss)
    tree_tok = _tokens(tree_text)
    if not gloss_tok or not tree_tok:
        return False
    return bool(gloss_tok & tree_tok)


def sibling_variant_codes(conn: sqlite3.Connection, base: str, exclude: str) -> list[str]:
    rows = conn.execute(
        "SELECT strongNumber FROM strong WHERE (strongNumber = ? OR strongNumber LIKE ?) "
        "AND strongNumber != ? ORDER BY strongNumber",
        (base, base + "_", exclude),
    ).fetchall()
    return [r["strongNumber"] for r in rows]


def live_step_meaning(step: "Step | None", code: str, live_cache: dict[str, str]) -> str:
    if code in live_cache:
        return live_cache[code]
    if step is None:
        text = "(STEP unavailable this run, step.required_for_runs=false — resolve manually against STEP for this exact code)"
        live_cache[code] = text
        return text
    try:
        vocabs = step.call2_getInfo(code).get("vocabInfos") or []
    except Exception as e:
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
    siblings = sibling_variant_codes(conn, base, exclude=code)
    # A sibling existing is NOT itself ambiguity — most sub-lettered codes are the SAME root's
    # different stems (H0935G Qal "come" / H0935P Hiphil "bring"), sharing one legitimate combined
    # dictionary entry. Only flag + pay for a live STEP call when this code's OWN (never-collapsed)
    # stepGloss shares no real vocabulary with that shared entry — the actual signal of a genuine
    # base-collapse (H3581B "strength" vs the shared tree's unrelated "reptile" content).
    genuinely_ambiguous = bool(siblings) and meaning_text and not gloss_supported_by_tree(
        strong_row["stepGloss"], meaning_text)
    if meaning_text:
        warn = (f" [AMBIGUOUS - base shared with {', '.join(siblings)}, may not be specific "
                f"to {code}]" if genuinely_ambiguous else "")
        lines.append(f"meaning_tree (base {base}){warn}: {meaning_text}")
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


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c) if c is not None else "" for c in r) + " |")
    return L


def _range_str(lo: int, hi: int, verse_lo: int | None, verse_hi: int | None) -> str:
    if verse_lo is not None:
        return f"{lo}-{verse_lo}-{verse_hi}"
    return f"{lo}" if lo == hi else f"{lo}-{hi}"


def write_report(cfg, book: str, lo: int, hi: int, verse_lo: int | None = None,
                 verse_hi: int | None = None, book_label: str | None = None) -> pathlib.Path:
    """Reads step.required_for_runs (cfg_setting, module='step', default True — see
    tools/build_verse_span_meaning_extract.py's UPDATED 2026-07-26 note and BUILD.md §21 for why).
    Default True: raises StepUnavailable if STEP's preflight fails — the caller (handlers/reports.py)
    catches this and reports a clean fail(), not a crash. Only if the researcher has set it False
    does this proceed STEP-down, with a DB-only note per AMBIGUOUS span instead of a resolved sense.

    `book_label` is the human-facing subfolder name (e.g. "Daniel") — a per-call PARAMETER, not a
    setting, same boundary as `table_export`'s -Out/-Table (GOVERNANCE.md §14): which folder label
    a given call uses varies per invocation, it is not a rule. Defaults to the OSIS `book` code if
    not given.
    """
    required = cfg.setting("step.required_for_runs", True)
    step: Step | None = None
    try:
        ev = Step(cfg).up()
        step = Step(cfg)
        step_status = f"available ({ev['base']}, {ev['version']})"
    except StepUnavailable:
        if required:
            raise
        step_status = ("unavailable — step.required_for_runs=false, proceeding without live "
                       "disambiguation (AMBIGUOUS spans show a DB-only note)")
    live_cache: dict[str, str] = {}

    conn = cfg.conn
    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)
    range_str = _range_str(lo, hi, verse_lo, verse_hi)
    label = f"{lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else f"{lo}-{hi}"

    per_chapter_total: dict[int, int] = {}
    per_chapter_covered: dict[int, int] = {}
    verse_lines: list[str] = []
    for v in verses:
        spans = fetch_spans(conn, v["id"])
        for sp in spans:
            if not sp["is_particle"]:
                per_chapter_total[v["chapter"]] = per_chapter_total.get(v["chapter"], 0) + 1
                _, covered = meaning_for(conn, sp["strong_variant"], step, live_cache)
                if covered:
                    per_chapter_covered[v["chapter"]] = per_chapter_covered.get(v["chapter"], 0) + 1

        verse_lines.append(f"### {v['reference']}")
        verse_lines.append("")
        verse_lines.append(v["text"] or "")
        verse_lines.append("")
        verse_lines.append("| # | surface | strong | morph | particle | meaning |")
        verse_lines.append("| --- | --- | --- | --- | --- | --- |")
        for sp in spans:
            meaning, _ = meaning_for(conn, sp["strong_variant"], step, live_cache)
            verse_lines.append(
                f"| {sp['position']} | {sp['surface'] or ''} | {sp['strong_variant'] or ''} | "
                f"{sp['morph_code'] or ''} | {'yes' if sp['is_particle'] else ''} | {meaning} |")
        verse_lines.append("")

    intro = [
        "> Read-only extract for manual movement analysis. Verse order = osisId parsed numerically "
        "(chapter, verse), not table-id order. No candidate/passage data involved (that layer is "
        "retired). Meaning is only as complete as the Strong's codes registered so far via word "
        "onboarding.",
        "",
        f"> STEP live disambiguation (for [AMBIGUOUS] spans only): {step_status}",
    ]

    coverage_rows = [[ch, per_chapter_covered.get(ch, 0), tot,
                      f"{round(100 * per_chapter_covered.get(ch, 0) / tot) if tot else 0}%"]
                     for ch, tot in sorted(per_chapter_total.items())]
    sections = {
        "coverage": _tbl(["chapter", "covered", "total", "%"], coverage_rows),
        "verses": verse_lines,
    }

    L = reportkit.render_scaffold(conn, "report.verse_span_meaning", sections, intro=intro,
                                  book=book, range=label)

    output_dir = pathlib.Path(cfg.setting("report.verse_analysis_output_dir", "iba/app/verse-analysis"))
    pattern = cfg.setting("report.verse_analysis_output_pattern",
                         "{book}-{range}-verse-span-meaning.md")
    folder = book_label or book
    filename = pattern.format(book=book.lower(), range=range_str)
    path = output_dir / folder / filename

    reportkit.write_report(conn, "report.verse_span_meaning", path, L)
    return path
