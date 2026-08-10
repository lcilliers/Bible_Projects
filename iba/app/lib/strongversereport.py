"""strongversereport.py — on-demand verse restatement, by ONE Strong's reference. Formalises the
2026-08-10 preview work (`iba/app/reports/g2128-verse-lexical-by-strong-sample-20260810.md` and
`g2127-verse-lexical-by-strong-sample-20260810.md`) into a real, config-driven report.

Design, carried over from the two samples (researcher's own answers, verbatim):

1. **Scope = one Strong's code, ALL its verses** (not one example verse) — every verse
   `verse_lexical.strong` matches this exact code, whole Bible. This is what keeps volume
   manageable: a registry word's full verse set can run into the thousands (see
   `verse-lexical-by-registry-20260810.md`); one Strong's code is orders of magnitude smaller —
   G2128 was 8 verses, G2127 was 40.
2. **Inline annotation**, not a separate table — the verse text stays intact, with only the
   matched span's surface text annotated in place: `**surface** [strong: senses]`.
3. **Exact-variant senses only** — every `strong_meaning_parsed` row for THIS strong_variant
   exactly, never a sibling/base-collapsed fallback (unlike `wordregistryspanreport.py`, which
   falls back to the base lemma for a sub-lettered code with no rows of its own — that fallback is
   deliberately NOT used here, since this report's whole reason to exist is per-span exactness).
4. **Collisions never silently dropped.** The G2127 test found a real bug in plain substring
   search (`"bless"` inside `"blessing"`) — fixed with a word-boundary regex, verified against
   every row in both test cases. A surface that still doesn't match exactly once (0 or >1 matches)
   is flagged `UNRESOLVED` in the output, never guessed.

Two data shapes G2128 (the first, easier test) never exercised, found building G2127, both handled
explicitly here:
- **Combined-tag spans** — STEP tags more than one Strong's code on one rendering unit (e.g.
  `strong_variant='G2532 G2127'`). `verse_lexical.strong` decomposes these into one row per code
  (querying `span.strong_variant` by exact string MISSES them — a real bug in the first draft of
  the G2127 preview, fixed before this was built). Labelled `{strong}+{other codes} combined tag`
  in the annotation rather than presented as a pure single-code occurrence.
- **Empty-surface spans** — the other half of a combined tag can carry no independent English
  surface text at all. Cannot be inline-substituted; rendered as a structured aside under the
  verse instead.

STEP's `call2_getInfo` "count" field (`strong.count`) is dictionary-wide, not a verse count —
root-caused live 2026-08-10 (BUILD.md sec88). Shown here only as a labelled caveat, never used for
anything.
"""

from __future__ import annotations

import pathlib
import re

from . import reportkit
from .stepapi import Step, StepUnavailable

STEP_ID = "report.strong_verse"


def _canon_key(osis_id: str, book_order: dict[str, int]) -> tuple:
    parts = (osis_id or "").split(".")
    book = book_order.get(parts[0], 999) if parts else 999
    ch = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    vs = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
    return (book, ch, vs)


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c) if c is not None else "" for c in r) + " |")
    return L


def _live_step_total(cfg, strong: str) -> str:
    """Best-effort live cross-check against STEP's own verse-search (`call3_strong`) — NOT a hard
    requirement (unlike e.g. `versespanmeaningreport.py`, where STEP is core to the feature
    itself). Here it only confirms the local `verse_lexical` count is complete; the report's core
    rendering is 100% local-DB-driven either way, so a STEP-down run still produces a full report,
    just without this one cross-check line."""
    try:
        step = Step(cfg)
        step.up()
        total, _ = step.call3_strong(strong)
        return f"live STEP `call3_strong` total: **{total}**"
    except StepUnavailable as e:
        return f"live STEP cross-check unavailable this run ({e}) — local count only, not verified"


def write_report(cfg, word: str, strong: str, word_id: int) -> pathlib.Path:
    conn = cfg.conn
    q = lambda sql, p=(): conn.execute(sql, p).fetchall()

    rows = q(
        "SELECT vl.id vl_id, vl.verse_id, v.osisId, v.reference, v.text, "
        "s.position, s.surface, s.strong_variant, s.morph_code "
        "FROM verse_lexical vl "
        "JOIN verse v ON v.id=vl.verse_id "
        "JOIN span s ON s.id=vl.span_id "
        "WHERE vl.strong=? AND vl.deleted=0 "
        "ORDER BY v.id, s.position", (strong,))

    book_order = cfg.book_order()
    by_verse: dict[int, list] = {}
    order: list[int] = []
    for r in rows:
        if r["verse_id"] not in by_verse:
            by_verse[r["verse_id"]] = []
            order.append(r["verse_id"])
        by_verse[r["verse_id"]].append(r)
    order.sort(key=lambda vid: _canon_key(by_verse[vid][0]["osisId"], book_order))

    n_rows, n_verses = len(rows), len(order)

    strong_row = q("SELECT stepGloss, stepTransliteration, language, count FROM strong "
                  "WHERE strongNumber=? AND deleted=0", (strong,))
    strong_row = strong_row[0] if strong_row else None

    senses = q("SELECT sense_code, row_type, gloss FROM strong_meaning_parsed "
              "WHERE strong_variant=? AND deleted=0 ORDER BY sort, id", (strong,))

    live_check = _live_step_total(cfg, strong)

    # Facts filtered for emptiness on their OWN list, kept separate from the leading paragraph +
    # blank-line separator — an earlier version filtered the whole `intro` list for `!= ""` in
    # one pass, which also ate the intentional blank line between the paragraph and this bullet
    # list (confirmed live: `blessing-G2127-verse-lexical-v1-20260810.md` rendered the first
    # bullet directly abutting the blockquote, no separating blank line). Fixed before this was
    # reported as done.
    facts = [
        f"- registry word: **{word}** (id {word_id})",
        f"- Strong's: **{strong}**" + (f" — {strong_row['stepGloss']}" if strong_row and strong_row['stepGloss'] else ""),
        (f"- transliteration: *{strong_row['stepTransliteration']}*, language: {strong_row['language']}"
         if strong_row else "- *(no `strong` row for this code)*"),
        f"- `verse_lexical` occurrences: **{n_rows}** ({n_verses} verse{'s' if n_verses != 1 else ''}) "
        f"— {live_check}",
        (f"- STEP lexicon count (dictionary-wide, NOT verse-scoped — see BUILD.md sec88): "
         f"{strong_row['count']}" if strong_row else ""),
    ]
    intro = [
        f"> Generated by `{STEP_ID}`. On-demand verse restatement for ONE Strong's reference — "
        f"every verse `verse_lexical.strong` matches this exact code (whole Bible), with only "
        f"that occurrence annotated inline; the rest of each verse is untouched.", "",
    ] + [f for f in facts if f != ""]

    sections: dict[str, list[str]] = {}

    if senses:
        S = [f"**{len(senses)}** sense(s), exact `strong_variant='{strong}'` match only — no "
            f"sibling/base-collapsed fallback:", ""]
        S += [f"- {(s['gloss'] or '')}" for s in senses]
        sense_text = "; ".join(s["gloss"] for s in senses if s["gloss"])
    else:
        S = [f"*(no `strong_meaning_parsed` rows for this exact code — {strong} carries no "
            f"parsed sense data yet)*"]
        sense_text = "(no sense data captured)"
    sections["senses"] = S

    if not order:
        sections["verses"] = [f"*(no `verse_lexical` occurrences for {strong} yet — not built in "
                             f"any processed book)*"]
    else:
        V = []
        for vid in order:
            rs = by_verse[vid]
            text = rs[0]["text"] or ""
            ref = rs[0]["reference"]
            replacements = []
            asides = []
            for r in rs:
                surf = r["surface"] or ""
                codes = r["strong_variant"].split()
                combined = len(codes) > 1
                tag = (f"{strong}+{'+'.join(c for c in codes if c != strong)} combined tag"
                      if combined else strong)
                if surf == "":
                    asides.append(
                        f"  - *(this occurrence, position {r['position']}, morph "
                        f"`{r['morph_code']}`, is the empty-surface half of combined tag "
                        f"`{r['strong_variant']}` — no independent English surface text; cannot "
                        f"be inline-annotated)*")
                    continue
                matches = list(re.finditer(r"\b" + re.escape(surf) + r"\b", text))
                if len(matches) != 1:
                    asides.append(
                        f"  - **UNRESOLVED**: surface {surf!r} (position {r['position']}) "
                        f"matched {len(matches)} time(s) in this verse's text, not 1 — not "
                        f"annotated, needs manual check rather than a guess")
                    continue
                start, end = matches[0].span()
                marker = f"**{surf}** [{tag}: {sense_text}]"
                replacements.append((start, end, marker))
            out = text
            for start, end, marker in sorted(replacements, key=lambda t: t[0], reverse=True):
                out = out[:start] + marker + out[end:]
            V.append(f"### {ref}")
            V.append("")
            V.append(f"> {out}")
            V.append("")
            V.extend(asides)
            if asides:
                V.append("")
        sections["verses"] = V

    L = reportkit.render_scaffold(conn, STEP_ID, sections, intro=intro, word=word, strong=strong)

    output_dir = pathlib.Path(cfg.setting("report.strong_verse_output_dir",
                                          "iba/app/verse-analysis/word_registry"))
    out = output_dir / word.lower().replace(" ", "-") / f"{word.lower().replace(' ', '-')}-{strong}-verse-lexical.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out = reportkit.write_report(conn, STEP_ID, out, L)
    return out
