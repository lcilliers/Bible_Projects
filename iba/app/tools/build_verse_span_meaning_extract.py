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

UPDATED 2026-07-26 — live STEP disambiguation for AMBIGUOUS spans (session 20260726 root-caused why
this happens — handlers/raw.py:detail_one()'s write-time guard silently drops a sub-lettered code's
own tree whenever a sibling already occupies that base — but the DB-side fix needs a schema decision
not yet made). Confirmed live last session: STEP's call2_getInfo DOES return the exact queried code's
own mediumDef (e.g. H3581B's own "strength, power, might..." distinct from H3581A's "reptile"), the
DB just isn't storing it that way yet. So whenever a span's meaning_tree is flagged [AMBIGUOUS], this
report now calls STEP live for that EXACT code and adds its own labeled line — no more silent "look it
up yourself" gap. Scope is naturally small (only ambiguous spans call out, ~22 of Dan 1:1-7's 494),
per the project's API-reads-are-small-bounded-batches rule, not a bulk pull. Per-code memoised within
one run (a code repeated across verses is fetched once). **STEP is REQUIRED, not optional, for this
report now**: `main()` runs STEP's known-answer preflight (`step.up()`) up front and refuses to build
anything if it fails, matching this app's standing rule (init.py/USER-GUIDE.md: "runs refuse to start
without STEP") — a first version of this change instead let the report degrade to a DB-only note per
ambiguous span when STEP was down, which the researcher correctly rejected: this tool proceeded with
STEP down at all, the opposite of the app's own convention, and the "degraded" run was then reported
as a passing test instead of being stopped.

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


def live_step_meaning(step: "Step | None", code: str, live_cache: dict[str, str]) -> str:
    """Live, per-EXACT-code disambiguation via STEP call2_getInfo — used only for spans whose
    meaning_tree is [AMBIGUOUS] (base shared with siblings). Confirmed live 2026-07-25/26: STEP
    returns the exact queried code's own mediumDef (e.g. H3581B's own "strength, power, might..."
    distinct from sibling H3581A's "reptile") — the DB-side strong_meaning_tree just doesn't store
    it that way yet (handlers/raw.py:detail_one() write-time guard, root-caused but not yet fixed).
    Memoised per code for the life of one report run — a code repeated across verses/spans is
    fetched from STEP once, not per occurrence (bounded-batch discipline, not a bulk pull).
    `step` is None ONLY when build() decided to proceed without it, which itself only happens when
    the cfg_setting step.required_for_runs is explicitly false (default true — see build()); this
    is a config-authorized degrade, not a silent hardcoded fallback."""
    if code in live_cache:
        return live_cache[code]
    if step is None:
        text = "(STEP unavailable this run, step.required_for_runs=false — resolve manually against STEP for this exact code)"
        live_cache[code] = text
        return text
    try:
        vocabs = step.call2_getInfo(code).get("vocabInfos") or []
    except Exception as e:  # a transient hiccup mid-run, AFTER the up-front preflight passed —
                            # degrade this one line, not silently pretend STEP was never required
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
        text, covered = meaning_for_code(conn, code, step, live_cache)
        any_covered = any_covered or covered
        rendered.append(f"**{code}**: {text}" if len(codes) > 1 else text)
    return " <br> ".join(rendered), any_covered


def build(book: str, lo: int, hi: int, verse_lo: int | None = None,
         verse_hi: int | None = None, *, cfg: "Cfg") -> list[str]:
    """Reads step.required_for_runs (cfg_setting, module='step', default True — same setting
    init.py's own startup preflight reads, ONE source of truth, not a hardcoded copy of the rule
    duplicated per tool). Default True means: raises StepUnavailable if STEP's known-answer
    preflight fails, and the caller (main()) must refuse rather than produce a report that
    silently can't do the AMBIGUOUS-span disambiguation it exists to add (UPDATED 2026-07-26
    note above). Only if the researcher has explicitly set step.required_for_runs=false does this
    proceed STEP-down, with a DB-only note on every affected span instead of a resolved sense —
    a config-authorized degrade, not a silent default."""
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
        # build() reads step.required_for_runs itself (ONE source of truth, shared with
        # init.py's own startup preflight — see governance.rules_must_be_config_driven,
        # 2026-07-26). Default true means StepUnavailable propagates from build() when STEP is
        # down; caught here to print the refusal and exit non-zero, same as every other
        # STEP-dependent tool in iba/app/tools/ (build_strong_related_extract.py et al.).
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
