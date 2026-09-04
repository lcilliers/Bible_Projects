"""lexical.py — the `verse_lexical` engine: T1-T3 of the verse-lexical technique
(`iba/docs/WA-verse-reading-technique-v4-2026-08-05.md`), mechanised. Replaces
`report.verse_span_meaning`'s per-span dump with one row per CODE within a span, holding a
mechanically resolved — never interpreted — reading. Full design record:
`iba/app/reports/t1-t3-design-decisions-20260805.md`.

Reuses `versespanmeaningreport`'s exact-variant/base-fallback resolution and its sibling/base
ambiguity check (`_base`, `sibling_variant_codes`, `gloss_supported_by_tree`, `live_step_meaning`)
rather than re-deriving them — same underlying facts, this module adds role classification and
stem/voice selection on top, then persists the result instead of only rendering it.

Runs independent of T4-T9 and `report.passage_debate` — no awareness of either. Version-aware
writes: rewriting a (span_id, code_ordinal) soft-deletes the superseded row and inserts a fresh
one, the same convention `verse`/`span`/`strong` already use — never an in-place overwrite.
"""

from __future__ import annotations

import datetime
import pathlib
import re
import sqlite3

from . import reportkit
from .versespanmeaningreport import (
    _BASE_RE_FALLBACK, _base, _range_str, detect_verse_gaps, fetch_verses, gap_note,
    gloss_supported_by_tree, live_step_meaning, merge_verses_and_gaps, sibling_variant_codes,
)
from .stepapi import Step


def _fetch_spans(conn: sqlite3.Connection, verse_id: int) -> list[dict]:
    """Same shape as versespanmeaningreport.fetch_spans, plus `id` (needed as the FK this table
    keys on) — a local copy rather than modifying the retiring module."""
    return [dict(r) for r in conn.execute(
        "SELECT id, position, surface, strong_variant, morph_code, is_particle "
        "FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", (verse_id,),
    ).fetchall()]

# ── role classification ──────────────────────────────────────────────────────────────────────
# Hebrew: STEP reserves H9000-H9999 for grammatical formatives (article, prefixed prep/conj,
# pronominal suffixes, directional-he) — verified against every function-word code encountered
# this session (H9002/H9003/H9005/H9009/H9011/H9020/H9028/H9030/H9033/H9038/H9040).
#
# CORRECTED 2026-08-05, later same day: an earlier version of this module claimed codes in that
# range carry no stepGloss/no strong_meaning_parsed rows "by design" and skipped resolving them
# entirely (resolved_sense left NULL). That was never actually checked and was wrong — every
# H9xxx code DOES carry a real, short stepGloss (H9002='and', H9003='in/on/with', H9009='[the]',
# H9020='my', etc.) and a real strong_meaning_parsed row ("Prefix beth: in, among, with"). The old
# report.verse_span_meaning showed these; this module was silently dropping them, a real
# regression caught by the researcher. Fixed: role no longer gates resolution at all — every code,
# content or function, goes through the same resolve_code() pipeline. `role` is purely
# classification metadata now (is this an independent lexical item or a bound grammatical
# formative), independent of whether resolution itself succeeds (`status`).
#
# Every non-H9xxx Hebrew code (including standalone function words like H0413 "to" or H0834A
# "which," which DO carry real lexical content) is 'content'.
_H_FORMATIVE_RE = re.compile(r"^H9\d{3}[A-Z]?$")

# H0853-function-word-exception (escalation #1383, build spec §B.13): the Hebrew direct-object
# marker (stepGloss='[Obj.]') sits OUTSIDE the H9xxx reserved range but is grammatically a pure
# formative, not an independent lexical item — an explicit, evidence-commented exception SET,
# not a widened regex range (the design's own stated shape: "starting with H0853," not "H08xx").
# 10,521 pre-existing live rows corrected to role='function' by
# migration/build_verse_lexical_window1_layer1_layer2_v1_20260904.py; this is what keeps it
# correct for every future lexical.build run.
_H_FUNCTION_EXCEPTIONS = {"H0853"}

# Greek has no equivalent reserved-range convention — verified only against G1722/G0505 this
# session, not exhaustively. Falls back to morph_code's own leading POS tag (Robinson/Byzantine-
# style). Unrecognised tags default to 'content' deliberately — misclassifying a real gap as
# "function, no content expected by design" is worse than the reverse.
_GREEK_FUNCTION_TAGS = ("PREP", "PRT", "CONJ", "ART")


def classify_role(strong_code: str | None, morph_slice: str | None) -> str:
    if strong_code and strong_code.startswith("H"):
        if _base(strong_code) in _H_FUNCTION_EXCEPTIONS:
            return "function"
        return "function" if _H_FORMATIVE_RE.match(strong_code) else "content"
    if strong_code and strong_code.startswith("G") and morph_slice:
        tag = morph_slice.split("-", 1)[0]
        if tag in _GREEK_FUNCTION_TAGS:
            return "function"
    return "content"


# ── stem/voice selection ─────────────────────────────────────────────────────────────────────
# Hebrew binyan letter (morph_code[2] for HV... codes) -> stem name, EMPIRICALLY VERIFIED against
# real strong_meaning_parsed text in this DB 2026-08-05 (no morph-code legend exists anywhere in
# this repo — checked). See bootstrap_verse_lexical.py's module docstring for the verification
# detail per letter. 'v' (Hishtaphel, H7812 "bow/worship," 13 occurrences) deliberately omitted —
# the source text lumps it under "(Hithpael)" with no independently labeled segment; left
# unmapped so it falls back to full-text presentation rather than a guessed extraction.
_HEBREW_STEM_MAP = {
    "q": "qal", "N": "niphal", "p": "piel", "P": "pual",
    "h": "hiphil", "H": "hophal", "t": "hithpael",
    "c": "tiphel", "u": "hothpael",
}

# Greek voice letter (2nd char of the TVM block, e.g. "PAP" -> A) -> voice name. Standard
# Robinson/Byzantine tagging convention — NOT independently re-verified against this DB's own
# strong_meaning_parsed text the way Hebrew was (today's Greek examples were non-verbs). Same
# safe-fallback applies if the label isn't found in the text.
_GREEK_VOICE_MAP = {"A": "active", "M": "middle", "P": "passive"}

_STEM_MARKER_RE = re.compile(r"^\(([A-Za-z]+)\)\s*(.*)$")
# strong_meaning_parsed.sense_code's own outline shape: '1)'/'2)' = root-level sense (a lemma can
# have more than one — e.g. H1288 has both a '1)' bless/kneel root AND a separate, non-stemmed '2)'
# TWOT-sourced sense); '1a)'/'1b)'... = a stem marker nested under root '1'; '1a1)'/'1a2)'... = a
# sub-sense nested under that stem. Restricting the stem search to LETTER-level codes (never
# digit-only root codes) is what rules out misreading a root-level citation marker like '(TWOT)'
# at '2)' as if it were a stem — TWOT-style citations only ever sit at root level in this data.
_LETTER_CODE_RE = re.compile(r"^(\d+)([a-z])\)$")


def _stem_name_for(strong_code: str, morph_slice: str | None) -> str | None:
    if not morph_slice:
        return None
    if strong_code.startswith("H") and morph_slice.startswith("HV") and len(morph_slice) >= 3:
        return _HEBREW_STEM_MAP.get(morph_slice[2])
    if strong_code.startswith("G") and morph_slice.startswith("V-"):
        parts = morph_slice.split("-")
        if len(parts) >= 2 and len(parts[1]) >= 2:
            return _GREEK_VOICE_MAP.get(parts[1][1])
    return None


def _select_stem_text(rows: list[tuple[str, str]], stem_name: str | None) -> tuple[str, bool]:
    """rows: ordered (sense_code, gloss) pairs from strong_meaning_parsed. Narrows to the matched
    stem's own branch — its marker row plus every 'root+letter+...' sub-sense row under it — PLUS
    the shared root-level summary row (found by matching sense_code, not by position: the digit-
    only code with the same leading digit as the matched branch). Dropping that root summary was
    the exact regression the researcher caught 2026-08-05 — STEP nests every stem's senses under
    one umbrella root sense (e.g. H7200's root '1)' "to see, look at, inspect, perceive, consider"
    is what Qal/Niphal/etc. below it all specialise), so a stem-narrowed reading without it loses
    real meaning, not just tidies punctuation. Falls back to every row's text, in original order,
    when stem_name is unknown or no letter-level row names it — a safe fallback (full range shown,
    not a guessed pick), not a hedge."""
    if stem_name:
        for code, gloss in rows:
            letter_m = _LETTER_CODE_RE.match(code)
            marker_m = _STEM_MARKER_RE.match((gloss or "").strip())
            if letter_m and marker_m and marker_m.group(1).lower() == stem_name:
                root, letter = letter_m.group(1), letter_m.group(2)
                prefix = f"{root}{letter}"
                texts = [g for c, g in rows if c == f"{root})"]  # the shared root summary, if any
                for c, g in rows:
                    if c.startswith(prefix):
                        m = _STEM_MARKER_RE.match((g or "").strip())
                        piece = m.group(2).strip() if m else (g or "").strip()
                        if piece:
                            texts.append(piece)
                return "; ".join(texts), True
    return "; ".join(g for _, g in rows if g), False


# ── resolution, per code ─────────────────────────────────────────────────────────────────────

def resolve_code(conn: sqlite3.Connection, code: str, morph_slice: str | None,
                 step: "Step | None", live_cache: dict[str, str],
                 base_pattern: str = _BASE_RE_FALLBACK) -> dict:
    """One code's full verse_lexical row content (minus span_id/verse_id/code_ordinal, which the
    caller fills in). Mirrors versespanmeaningreport.meaning_for_code's exact-variant/base-
    fallback/ambiguity decision (reused, not re-derived) then adds stem/voice narrowing."""
    role = classify_role(code, morph_slice)
    row = {"strong": code, "morph_code": morph_slice, "role": role,
          "status": "unregistered", "resolved_sense": None, "ambiguity_note": None,
          "language": None}

    strong_row = conn.execute(
        "SELECT strongNumber, language, stepGloss FROM strong WHERE strongNumber=?",
        (code,)).fetchone()
    if strong_row is None:
        return row
    row["language"] = strong_row["language"]

    base = _base(code, base_pattern)
    exact_rows = conn.execute(
        "SELECT sense_code, gloss FROM strong_meaning_parsed WHERE strong_variant=? "
        "ORDER BY sort, id", (code,)).fetchall()
    exact_variant = bool(exact_rows)
    rows = exact_rows if exact_variant else conn.execute(
        "SELECT sense_code, gloss FROM strong_meaning_parsed WHERE lemma_key=? AND "
        "strong_variant=? ORDER BY sort, id", (base, base)).fetchall()
    sense_rows = [(r["sense_code"] or "", r["gloss"]) for r in rows if r["gloss"]]

    if not sense_rows:
        row["status"] = "resolved"
        row["resolved_sense"] = f"stepGloss: {strong_row['stepGloss'] or '(none)'}"
        return row

    siblings = sibling_variant_codes(conn, base, exclude=code)
    joined = "; ".join(g for _, g in sense_rows)
    genuinely_ambiguous = (bool(siblings) and not exact_variant and
                          not gloss_supported_by_tree(strong_row["stepGloss"], joined))
    if genuinely_ambiguous:
        row["ambiguity_note"] = (
            f"base {base} shared with {', '.join(siblings)}, base-fallback text may not be "
            f"specific to {code} — STEP live: {live_step_meaning(step, code, live_cache)}")

    stem_name = _stem_name_for(code, morph_slice)
    text, narrowed = _select_stem_text(sense_rows, stem_name)

    sense = f"stepGloss: {strong_row['stepGloss'] or '(none)'} — {text}"
    if strong_row["language"] == "Greek":
        lsj = conn.execute(
            "SELECT gloss FROM strong_lsj_parsed WHERE strong=? AND row_type='lookup' "
            "ORDER BY id", (code,)).fetchall()
        mounce = conn.execute(
            "SELECT mounce_parsed FROM strong_mounce_parsed WHERE strong=? ORDER BY id",
            (code,)).fetchall()
        lsj_text = "; ".join(r["gloss"] for r in lsj if r["gloss"])
        mounce_text = "; ".join(r["mounce_parsed"] for r in mounce if r["mounce_parsed"])
        if lsj_text:
            sense += f" | lsj: {lsj_text}"
        if mounce_text:
            sense += f" | mounce: {mounce_text}"

    row["status"] = "resolved"
    row["resolved_sense"] = sense
    return row


# ── build + version-aware write, per span ────────────────────────────────────────────────────

def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── Layer 1 mechanical fields (escalation #1383, build spec §B.5/§C.1) ────────────────────────
# position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/
# party_kind — computed unconditionally for every code, no selection (method-and-drift-
# mitigation doc §1-2, cfg_method_rule `mechanical-columns-run-on-every-code-no-selection`).

def load_code_classes(conn: sqlite3.Connection) -> dict[str, set[str]]:
    """base strong_code -> set of live cfg_lexical_code_class classes. Loaded once per build call
    (see build_for_range/build_for_verse_ids) and threaded through, same pattern as `live_cache`
    — this table is small (~20 rows) but every-code-every-verse re-querying it would still be
    wasteful at corpus scale. `lexical-code-class-lookup-not-hardcoded`: this IS the queried
    lookup that rule requires, never a hardcoded dict in this module."""
    out: dict[str, set[str]] = {}
    for r in conn.execute(
            "SELECT strong_code, class FROM cfg_lexical_code_class WHERE active=1"):
        out.setdefault(r["strong_code"], set()).add(r["class"])
    return out


def _code_classes_for(code: str, code_classes: dict[str, set[str]],
                      base_pattern: str) -> set[str]:
    return code_classes.get(_base(code, base_pattern), set())


_PARTY_CLASS_TO_KIND = {"party_divine": "divine", "party_human": "human",
                        "party_angelic": "non_human"}


def _testament_for(conn: sqlite3.Connection, book: str) -> str | None:
    r = conn.execute("SELECT ordinal FROM cfg_book_order WHERE book=?", (book,)).fetchone()
    if r is None or r["ordinal"] is None:
        return None
    return "OT" if r["ordinal"] <= 38 else "NT"


def _narrative_morph_for(morph_slice: str | None, language: str | None,
                         sibling_codes: list[str]) -> str | None:
    """Hebrew only (narrative-morph-hebrew-only). wayyiqtol: this code's own morph is
    'HV<stem><TAM>...' with TAM='w' at 0-based index 3. az_imperfect_opening: same shape with
    TAM='i' (imperfect) AND some OTHER code in the SAME span has a base strong of H0227
    ("az"/"then") — verified live, Exod.15.1 (H7891 HVqi3ms + H0227A HD, same span).
    `sibling_codes`: every OTHER code's own `strong` in this same span (bare, not base-stripped —
    the `H0227%` prefix check below already covers every variant suffix)."""
    if language != "Hebrew" or not morph_slice or not morph_slice.startswith("HV") or len(morph_slice) < 4:
        return None
    tam = morph_slice[3]
    if tam == "w":
        return "wayyiqtol"
    if tam == "i" and any(c.startswith("H0227") for c in sibling_codes):
        return "az_imperfect_opening"
    return None


def _layer1_fields(row: dict, span: dict, sibling_codes: list[str], language: str | None,
                   testament: str | None, code_classes: dict[str, set[str]],
                   base_pattern: str) -> None:
    """Mutates `row` (a resolve_code() result) in place, adding the 7 per-row Layer-1 fields —
    everything except gloss_consistent_in_verse, which needs the whole verse's rows (computed
    separately, see _apply_gloss_consistency below)."""
    row["position"] = span["position"]
    row["surface"] = span["surface"]
    row["language"] = language
    row["testament"] = testament
    code = row["strong"]
    classes = _code_classes_for(code, code_classes, base_pattern) if code else set()
    row["is_negator"] = 1 if "negator" in classes else None
    party_class = next((c for c in classes if c in _PARTY_CLASS_TO_KIND), None)
    row["party_kind"] = _PARTY_CLASS_TO_KIND.get(party_class) if party_class else None
    row["narrative_morph"] = _narrative_morph_for(row["morph_code"], language, sibling_codes)


def _apply_gloss_consistency(verse_rows: list[dict]) -> None:
    """Mutates every row in `verse_rows` in place — gloss_consistent_in_verse=0 iff this row's
    own (strong, morph_code) pair has >1 distinct resolved_sense among this verse's own rows,
    else 1 (never NULL — per §D.1). Needs the WHOLE verse's resolved rows, not just one span's,
    hence a separate pass after every span in the verse has been resolved."""
    groups: dict[tuple, set] = {}
    for r in verse_rows:
        if r["strong"] is None or r["morph_code"] is None:
            continue
        key = (r["strong"], r["morph_code"])
        groups.setdefault(key, set()).add(r["resolved_sense"])
    for r in verse_rows:
        if r["strong"] is None or r["morph_code"] is None:
            r["gloss_consistent_in_verse"] = 1
            continue
        key = (r["strong"], r["morph_code"])
        r["gloss_consistent_in_verse"] = 1 if len(groups[key]) <= 1 else 0


def write_readings_for_span(conn: sqlite3.Connection, span_id: int, verse_id: int,
                            resolved: list[dict]) -> dict:
    """Version-aware: for each code_ordinal, soft-deletes any current (deleted=0) row and inserts
    a fresh one — always, even when content is unchanged, so created_at reflects the last run that
    confirmed it (cheap; verse_lexical is not high-write-volume). Returns counts."""
    c = {"inserted": 0, "superseded": 0}
    now = _now()
    for ordinal, r in enumerate(resolved):
        existing = conn.execute(
            "SELECT id FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0",
            (span_id, ordinal)).fetchone()
        if existing:
            conn.execute("UPDATE verse_lexical SET deleted=1 WHERE id=?", (existing["id"],))
            c["superseded"] += 1
        conn.execute(
            "INSERT INTO verse_lexical (span_id, verse_id, code_ordinal, strong, morph_code, "
            "role, status, resolved_sense, ambiguity_note, created_at, deleted, position, "
            "surface, language, testament, is_negator, narrative_morph, "
            "gloss_consistent_in_verse, party_kind) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,0,?,?,?,?,?,?,?,?)",
            (span_id, verse_id, ordinal, r["strong"], r["morph_code"], r["role"], r["status"],
             r["resolved_sense"], r["ambiguity_note"], now,
             r.get("position"), r.get("surface"), r.get("language"), r.get("testament"),
             r.get("is_negator"), r.get("narrative_morph"),
             r.get("gloss_consistent_in_verse", 1), r.get("party_kind")))
        c["inserted"] += 1
    return c


def build_for_verse(conn: sqlite3.Connection, verse_id: int, step: "Step | None",
                    live_cache: dict[str, str], base_pattern: str = _BASE_RE_FALLBACK,
                    code_classes: dict[str, set[str]] | None = None) -> dict:
    c = {"spans": 0, "codes": 0, "inserted": 0, "superseded": 0}
    if code_classes is None:          # safe default for a direct/standalone caller
        code_classes = load_code_classes(conn)

    verse_row = conn.execute("SELECT osisId FROM verse WHERE id=?", (verse_id,)).fetchone()
    book = verse_row["osisId"].split(".", 1)[0] if verse_row else None
    testament = _testament_for(conn, book) if book else None

    spans = _fetch_spans(conn, verse_id)
    per_span_resolved: list[tuple[dict, list[dict]]] = []
    for sp in spans:
        codes = (sp["strong_variant"] or "").split()
        morphs = (sp["morph_code"] or "").split()
        if not codes:
            continue
        resolved = [
            resolve_code(conn, code, morphs[i] if i < len(morphs) else None, step, live_cache,
                        base_pattern)
            for i, code in enumerate(codes)
        ]
        for i, r in enumerate(resolved):
            sibling_codes = [c for j, c in enumerate(codes) if j != i]
            _layer1_fields(r, sp, sibling_codes, r["language"], testament,
                          code_classes, base_pattern)
        per_span_resolved.append((sp, resolved))

    # gloss_consistent_in_verse needs the WHOLE verse's rows — one pass after every span resolved.
    all_rows = [r for _, resolved in per_span_resolved for r in resolved]
    _apply_gloss_consistency(all_rows)

    for sp, resolved in per_span_resolved:
        counts = write_readings_for_span(conn, sp["id"], verse_id, resolved)
        c["spans"] += 1
        c["codes"] += len(resolved)
        c["inserted"] += counts["inserted"]
        c["superseded"] += counts["superseded"]
    return c


def build_for_range(conn: sqlite3.Connection, book: str, lo: int, hi: int,
                    verse_lo: int | None, verse_hi: int | None, step: "Step | None") -> dict:
    live_cache: dict[str, str] = {}
    code_classes = load_code_classes(conn)
    totals = {"verses": 0, "spans": 0, "codes": 0, "inserted": 0, "superseded": 0}
    for v in fetch_verses(conn, book, lo, hi, verse_lo, verse_hi):
        counts = build_for_verse(conn, v["id"], step, live_cache, code_classes=code_classes)
        totals["verses"] += 1
        for k in ("spans", "codes", "inserted", "superseded"):
            totals[k] += counts[k]
    return totals


def build_for_verse_ids(conn: sqlite3.Connection, verse_ids: list[int],
                        step: "Step | None") -> dict:
    """Same shape as `build_for_range`, but scoped to an explicit verse_id list rather than a
    book/chapter range — for a per-WORD rebuild (2026-08-10, `raw.lexical`, the `new-word` chain's
    closing step: "checking that the lexicals for the verses are correct with the parse values").
    `build_for_verse` is already version-aware (soft-deletes a superseded row, never overwrites in
    place — see its own `write_readings_for_span` call), so re-running this for a verse whose
    parse values haven't changed since the last build is a safe, cheap no-op; a verse whose
    `strong_meaning_parsed`/span content HAS changed gets its `verse_lexical` rows corrected in
    place. Dedups the input (a word's strongs can share a verse many times over)."""
    live_cache: dict[str, str] = {}
    totals = {"verses": 0, "spans": 0, "codes": 0, "inserted": 0, "superseded": 0}
    for vid in dict.fromkeys(verse_ids):     # de-dup, preserve order
        counts = build_for_verse(conn, vid, step, live_cache)
        totals["verses"] += 1
        for k in ("spans", "codes", "inserted", "superseded"):
            totals[k] += counts[k]
    return totals


# ── on-demand report — DB is the source, this is a render, never an independent write ────────

def _render_component(r: sqlite3.Row) -> str:
    if r["status"] == "unregistered":
        return f"{r['strong']} [{r['role']}]: (not yet registered)"
    text = f"{r['strong']} [{r['role']}]: {r['resolved_sense']}"
    if r["ambiguity_note"]:
        text += f" [AMBIGUOUS — {r['ambiguity_note']}]"
    return text


def _tbl(headers: list[str], rows: list[list]) -> list[str]:
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c) if c is not None else "" for c in r) + " |")
    return L


def write_report(cfg, book: str, lo: int, hi: int, verse_lo: int | None = None,
                 verse_hi: int | None = None, book_label: str | None = None) -> pathlib.Path:
    """Reads verse_lexical — never re-derives from span/strong/strong_meaning_parsed. If nothing
    has been built yet for this exact range, that's `no-readings` (handlers/reports.py catches
    it) — run lexical.build first (ordinal 0 of the same work package)."""
    conn = cfg.conn
    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)
    range_str = _range_str(lo, hi, verse_lo, verse_hi)
    label = f"{lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else f"{lo}-{hi}"

    gaps = detect_verse_gaps(verses, verse_lo)
    per_chapter_total: dict[int, int] = {}
    per_chapter_covered: dict[int, int] = {}
    verse_lines: list[str] = []
    any_readings = False

    for ch, vn, kind, v in merge_verses_and_gaps(verses, gaps):
        if kind == "gap":
            verse_lines.append(gap_note(cfg, book, book_label, ch, vn))
            verse_lines.append("")
            continue

        spans = conn.execute(
            "SELECT id, position, surface, is_particle FROM span WHERE verse_id=? AND deleted=0 "
            "ORDER BY position", (v["id"],)).fetchall()
        rows = []
        for sp in spans:
            components = conn.execute(
                "SELECT * FROM verse_lexical WHERE span_id=? AND deleted=0 ORDER BY code_ordinal",
                (sp["id"],)).fetchall()
            if components:
                any_readings = True
            if not sp["is_particle"]:
                for c in components:
                    per_chapter_total[v["chapter"]] = per_chapter_total.get(v["chapter"], 0) + 1
                    if c["status"] == "resolved":
                        per_chapter_covered[v["chapter"]] = (
                            per_chapter_covered.get(v["chapter"], 0) + 1)
            reading = (" + ".join(_render_component(c) for c in components)
                      if components else "(not yet built — run lexical.build)")
            rows.append([sp["position"], sp["surface"] or "", reading])

        verse_lines.append(f"### {v['reference']}")
        verse_lines.append("")
        verse_lines.append(v["text"] or "")
        verse_lines.append("")
        verse_lines += _tbl(["#", "surface", "reading"], rows)
        verse_lines.append("")

    intro = [
        "> On-demand extract, generated from `verse_lexical` (never an independent write) — the "
        "resolved T1-T3 reading, connected units and morph-selected sense, not a per-code dump. "
        "Verse order = osisId parsed numerically, not table-id order.",
    ]
    if not any_readings:
        intro.append("")
        intro.append("> **Nothing built yet for this range** — run `lexical.build` first.")

    coverage_rows = [[ch, per_chapter_covered.get(ch, 0), tot,
                      f"{round(100 * per_chapter_covered.get(ch, 0) / tot) if tot else 0}%"]
                     for ch, tot in sorted(per_chapter_total.items())]
    sections = {
        "coverage": _tbl(["chapter", "resolved", "total", "%"], coverage_rows),
        "verses": verse_lines,
    }

    L = reportkit.render_scaffold(conn, "report.verse_lexical", sections, intro=intro,
                                  book=book, range=label)

    output_dir = pathlib.Path(cfg.required_setting("report.verse_analysis_output_dir"))
    pattern = cfg.required_setting("report.verse_lexical_output_pattern")
    folder = book_label or book
    filename = pattern.format(book=book.lower(), range=range_str)
    path = output_dir / folder / filename

    path = reportkit.write_report(conn, "report.verse_lexical", path, L)
    return path
