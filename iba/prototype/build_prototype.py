"""build_prototype.py — test the term -> sense -> span model against real STEP data.

PROTOTYPE. Not the application. It pulls one registry word from STEP and writes the
result as JSON files shaped like DB tables, with foreign keys between them, so the
model can be checked before anything is built.

The model under test (v6):

    word  --< word_term >--  term          the LEMMA   · holds the definition TREE
                               |
                               +--<  sense      the SUB-GLOSS · holds the HEAD  · has its own verses
                                        |
                                        +--<  span       ONE OCCURRENCE · names its sense
                                                 |
                                               verse

    A span does not carry a term. It carries a SENSE.
    The term is reached THROUGH the meaning.

THE FALSIFICATION TEST: every sense of a term must share a byte-identical definition
tree. If they do not, the tree is not the term's and the model is wrong. Reported per
term as tree_shared.

Read-only against STEP. Writes only to the prototype's own output folder.

Usage:
    python iba/prototype/build_prototype.py --word hypocrisy
    python iba/prototype/build_prototype.py --word spirit --max-senses 8
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "analytics"))

from analytics.step_client import StepClient  # noqa: E402

SPAN_RE = re.compile(r"<span[^>]*\bmorph='([^']*)'[^>]*\bstrong='([^']*)'[^>]*>([^<]*)</span>")
BASE_RE = re.compile(r"^([HG]\d+)([A-Z]?)$")
PARTICLE_RE = re.compile(r"^[HG]9\d{3}$")


def split_def(medium_def: str) -> tuple[str, str]:
    """A code's mediumDef is '<head>' + newline + the lemma's TREE.

    The head is THIS CODE's meaning. The tree is the LEMMA's full range.

    ⚠ step_client already converts STEP's <br> to newlines, so the split is on the
    first NEWLINE. Splitting on '<br>' (v1 of this prototype) never fired: every tree
    came out empty, and the tree_shared test passed vacuously because len({''}) == 1.
    A test that cannot fail is not a test.

    A code with no newline has a head and NO tree — a lemma with a one-line
    definition (H7280C 'to harden').
    """
    d = (medium_def or "").strip().lstrip(": ").strip()
    head, _, tree = d.partition("\n")
    return head.strip(), tree.strip()


def base_of(code: str) -> str:
    m = BASE_RE.match(code or "")
    return m.group(1) if m else code


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--word", required=True)
    ap.add_argument("--max-senses", type=int, default=26)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    out = pathlib.Path(a.out) if a.out else (ROOT / "iba" / "prototype" / "data" / a.word)
    out.mkdir(parents=True, exist_ok=True)
    c = StepClient()
    c.preflight()
    print(f"word: {a.word}   out: {out.relative_to(ROOT)}\n")

    # ── word ────────────────────────────────────────────────────────────────
    word_row = {"word_id": 1, "word": a.word, "source": "prototype 2026-07-17",
                "status": "approved"}

    # ── discover: the word's candidate codes ────────────────────────────────
    defs = c.get_meaning_terms(a.word).get("definitions", [])
    candidates = [d["strongNumber"] for d in defs
                  if d.get("strongNumber") and not PARTICLE_RE.match(d["strongNumber"])]
    print(f"[discover] meanings= -> {len(defs)} definitions, {len(candidates)} after particle filter")

    # ── term + sense: enumerate the SENSES of each lemma ────────────────────
    terms: dict[str, dict] = {}
    seen_base: set[str] = set()
    senses: dict[str, dict] = {}
    related: list[dict] = []

    for cand in candidates:
        v = c.get_vocab_info(cand)
        if not v:
            continue
        resolved = v["strong_number"]
        base = base_of(resolved)
        if base in seen_base:
            continue

        # every code sharing this base is a SENSE of this lemma
        family: list[dict] = []
        m = BASE_RE.match(resolved)
        if m and m.group(2):                       # the lemma has lettered senses
            for suf in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[: a.max_senses]:
                sv = c.get_vocab_info(f"{base}{suf}")
                if sv and sv["strong_number"] == f"{base}{suf}":
                    family.append(sv)
                elif family:
                    break                          # senses are contiguous; stop at the gap
        if not family:
            family = [v]                           # an unlettered code: its own lemma

        # ★ THE TERM IS THE SET OF CODES SHARING A TREE — not the base code.
        #
        # The letter suffix means two different things and the TREE tells them apart:
        #   A/B/C = HOMONYMS   — different lemmas sharing consonants, each with its OWN
        #                        tree (H2790A 'to engrave' vs H2790B 'to be silent')
        #   G/H/I/J = SENSES   — one lemma, sharing ONE tree (H7307G/H/I/J ruach)
        # A code with no tree is its own lemma with a one-line definition.
        groups: dict[str, list] = defaultdict(list)
        for s in family:
            tree = split_def(s["medium_def"])[1]
            groups[tree if tree else f"__own__{s['strong_number']}"].append(s)

        seen_base.add(base)
        for tree_key, group in groups.items():
            group.sort(key=lambda s: s["strong_number"])
            key = group[0]["strong_number"]        # the term's identity = its lowest code
            tree = "" if tree_key.startswith("__own__") else tree_key
            terms[key] = {
                "term_id": len(terms) + 1,
                "strongs": key,
                "base": base,
                "lexicon": "Hebrew" if base.startswith("H") else "Greek",
                "tree": tree,
                "sense_codes": [s["strong_number"] for s in group],
                "sense_count": len(group),
                "★ shares_base_with_other_terms": len(groups) > 1,   # a homonym split
            }
            for s in group:
                head, _ = split_def(s["medium_def"])
                senses[s["strong_number"]] = {
                    "sense_id": len(senses) + 1,
                    "term_id": terms[key]["term_id"],           # FK -> term
                    "strongs": s["strong_number"],
                    "head": head,                               # ★ THE SPAN'S MEANING
                    "gloss": s["gloss"],
                    "script_form": s["hebrew_unicode"],
                    "transliteration": s["transliteration"],
                    "occurrence_count": s["occurrence_count"],
                }
            for rw in group[0].get("related_words", []):
                related.append({"term_id": terms[key]["term_id"],
                                "related_strongs": rw.get("strong"),
                                "gloss": rw.get("gloss"),
                                "script_form": rw.get("form"),
                                "transliteration": rw.get("translit")})
        if len(groups) > 1:
            print(f"[term]  ★  {base:8} SPLITS into {len(groups)} terms (homonyms — different trees):")
            for tk, grp in groups.items():
                print(f"              {'+'.join(s['strong_number'] for s in grp):<28} "
                      f"{split_def(grp[0]['medium_def'])[0][:44]!r}")
        else:
            g = list(groups.values())[0]
            print(f"[term]     {base:8} 1 term, {len(g)} sense(s)   "
                  f"{', '.join(s['strong_number'] + '=' + repr(split_def(s['medium_def'])[0][:18]) for s in g[:4])}")

    word_term = [{"word_id": 1, "term_id": t["term_id"]} for t in terms.values()]

    # ── verses + spans: ONE call per sense gives both ───────────────────────
    verses: dict[str, dict] = {}
    spans: list[dict] = []
    for code, s in senses.items():
        rows = c._paginate_all(c._search_range, code)
        print(f"[verses]   {code:8} {len(rows):>4} verse(s)  ({s['gloss']!r})")
        for r in rows:
            osis = r.get("osisId")
            if not osis:
                continue
            if osis not in verses:
                verses[osis] = {"verse_id": len(verses) + 1, "osis_id": osis,
                                "reference": r.get("key"),
                                "text": c._strip_html(r.get("preview", "")),
                                "translation": "ESV", "step_version": c.version}
                # the preview IS the verse's full interlinear — every span, one call
                for i, (morph, strongs, surface) in enumerate(
                        SPAN_RE.findall(r.get("preview", ""))):
                    spans.append({
                        "span_id": len(spans) + 1,
                        "verse_id": verses[osis]["verse_id"],   # FK -> verse
                        "word_index": i,
                        "surface": surface.strip(),
                        "strongs": strongs,                     # may name several codes
                        "morph_code": morph,
                        "language": "Hebrew" if morph.startswith("H") else "Greek",
                        "sense_id": None,                       # FK -> sense; resolved below
                        "particles": [x for x in strongs.split() if PARTICLE_RE.match(x)],
                    })

    # ── ★ THE BACKTRACK: resolve each span to the SENSE it names ────────────
    by_code = {s["strongs"]: s for s in senses.values()}
    linked = unheld = 0
    for sp in spans:
        hit = [x for x in sp["strongs"].split() if x in by_code]
        if hit:
            sp["sense_id"] = by_code[hit[0]]["sense_id"]
            sp["★ meaning"] = by_code[hit[0]]["head"]           # the span's meaning, at ingest
            linked += 1
        else:
            unheld += 1

    # ── write the "tables" ──────────────────────────────────────────────────
    tables = {"word": [word_row], "term": list(terms.values()),
              "sense": list(senses.values()), "word_term": word_term,
              "term_related": related, "verse": list(verses.values()), "span": spans}
    for name, rows in tables.items():
        (out / f"{name}.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False),
                                          encoding="utf-8")
    (out / "_schema.json").write_text(json.dumps({
        "model": "word --< word_term >-- term --< sense --< span >-- verse",
        "grain": {"word": "one per English word", "term": "one per LEMMA (base Strong's)",
                  "sense": "one per SUB-GLOSS — the span's meaning",
                  "span": "one per word of a verse — names its SENSE",
                  "verse": "one per verse"},
        "foreign_keys": [
            {"from": "word_term.word_id", "to": "word.word_id"},
            {"from": "word_term.term_id", "to": "term.term_id"},
            {"from": "sense.term_id", "to": "term.term_id"},
            {"from": "term_related.term_id", "to": "term.term_id"},
            {"from": "span.verse_id", "to": "verse.verse_id"},
            {"from": "span.sense_id", "to": "sense.sense_id",
             "note": "★ THE BACKTRACK — a span names a SENSE, and reaches the term through it"},
        ],
        "counts": {k: len(v) for k, v in tables.items()},
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    # ── the verdict ─────────────────────────────────────────────────────────
    broken = [t["strongs"] for t in terms.values() if not t["★ tree_shared"]]
    multi = [t for t in terms.values() if t["sense_count"] > 1]
    print(f"\n{'='*66}")
    print(f"  terms {len(terms)} · senses {len(senses)} · verses {len(verses)} · spans {len(spans)}")
    print(f"  terms with >1 sense : {len(multi)}")
    print(f"  ★ tree shared across every sense : "
          f"{'ALL PASS' if not broken else 'FAILED for ' + ', '.join(broken)}")
    print(f"  spans linked to a sense we hold  : {linked:,} / {len(spans):,}"
          f"  ({unheld:,} name codes this word does not hold — other lemmas in the same verse)")
    print(f"{'='*66}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
