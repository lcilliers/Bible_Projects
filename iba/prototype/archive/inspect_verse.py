"""inspect_verse.py — select a verse; watch the backtrack; see what emerges.

PROTOTYPE. Reads only the JSON "tables" build_prototype.py wrote. No STEP, no DB.
That is the point: if the lexical analysis emerges from the tables alone, the model
carries it. If it needs anything else, it does not.

    span --sense_id--> sense --term_id--> term
     |                   |                  |
   morph, surface     THE HEAD          THE TREE
   the particles      = this span's      = the lemma's full range
                        meaning            (context, not the meaning)

Usage:
    python iba/prototype/inspect_verse.py --word peace --verse Num.6.26
    python iba/prototype/inspect_verse.py --word peace --list
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

# morph_code, decomposed only as far as the model needs to show its work
STATE = {"a": "absolute", "c": "construct", "d": "determined"}
GENDER = {"m": "masculine", "f": "feminine", "c": "common", "b": "both"}
NUMBER = {"s": "singular", "p": "plural", "d": "dual"}
POS = {"N": "noun", "V": "verb", "R": "preposition", "C": "conjunction",
       "T": "particle", "A": "adjective", "P": "pronoun", "D": "adverb", "S": "suffix"}
STEM = {"q": "Qal", "n": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil",
        "H": "Hophal", "t": "Hithpael", "r": "participle-r"}


def decompose(morph: str) -> str:
    """HNcfsc -> noun · common · feminine · singular · CONSTRUCT"""
    if not morph or len(morph) < 2:
        return ""
    body = morph[1:]
    pos = POS.get(body[0], body[0])
    bits = [pos]
    if body[0] == "N" and len(body) >= 5:
        bits += [GENDER.get(body[2], "?"), NUMBER.get(body[3], "?"),
                 (STATE.get(body[4], "?") or "").upper() if body[4] == "c" else STATE.get(body[4], "?")]
    elif body[0] == "V" and len(body) >= 2:
        bits.append(STEM.get(body[1], body[1]))
        if len(body) >= 3:
            bits.append({"p": "perfect", "w": "wayyiqtol", "i": "imperfect",
                         "r": "participle", "v": "imperative"}.get(body[2], body[2]))
    return " · ".join(b for b in bits if b and b != "?")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--word", required=True)
    ap.add_argument("--verse")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    d = ROOT / "iba" / "prototype" / "data" / a.word
    T = {n: json.loads((d / f"{n}.json").read_text(encoding="utf-8"))
         for n in ("word", "term", "sense", "verse", "span", "term_related")}
    sense = {s["sense_id"]: s for s in T["sense"]}
    term = {t["term_id"]: t for t in T["term"]}
    spans_by_verse: dict[int, list] = {}
    for s in T["span"]:
        spans_by_verse.setdefault(s["verse_id"], []).append(s)

    if a.list:
        rich = sorted(T["verse"],
                      key=lambda v: -sum(1 for s in spans_by_verse.get(v["verse_id"], [])
                                         if s["sense_id"]))
        print("verses carrying the most held senses:")
        for v in rich[:12]:
            n = sum(1 for s in spans_by_verse.get(v["verse_id"], []) if s["sense_id"])
            print(f"  {v['osis_id']:14} {n} held span(s)   {v['reference']}")
        return 0

    v = next((x for x in T["verse"] if x["osis_id"] == a.verse), None)
    if not v:
        print(f"{a.verse} is not in this word's pull.")
        return 1

    print("=" * 78)
    print(f"VERSE  {v['reference']}   ({v['osis_id']})   {v['translation']}/{v['step_version']}")
    print("=" * 78)
    print(f"{v['text'][:200]}\n")

    spans = sorted(spans_by_verse.get(v["verse_id"], []), key=lambda s: s["word_index"])
    held = [s for s in spans if s["sense_id"]]
    print(f"the verse has {len(spans)} spans; {len(held)} name a sense this word holds\n")

    print("-" * 78)
    print("ALL SPANS — every word of the verse is tagged")
    print("-" * 78)
    for s in spans:
        mark = "  <<<" if s["sense_id"] else ""
        print(f"  {s['word_index']:>2} {s['surface'][:18]:<18} {s['strongs']:<24} {s['morph_code']:<16}{mark}")

    for s in held:
        se = sense[s["sense_id"]]
        te = term[se["term_id"]]
        print()
        print("=" * 78)
        print(f"THE BACKTRACK — span {s['word_index']} · {s['surface']!r}")
        print("=" * 78)
        print(f"  SPAN    strongs   : {s['strongs']}")
        print(f"          morph     : {s['morph_code']}   →  {decompose(s['morph_code'])}")
        print(f"          language  : {s['language']}          ← a SPAN fact, not a term fact")
        if s["particles"]:
            print(f"          particles : {s['particles']}   ← attached to the word")
        print(f"      │")
        print(f"      │  span names the sense {se['strongs']}")
        print(f"      ▼")
        print(f"  SENSE   {se['strongs']}  {se['script_form']}  ({se['transliteration']})")
        print(f"      ★   HEAD      : {se['head']!r}        ←── THE SPAN'S MEANING")
        print(f"          gloss     : {se['gloss']!r}")
        print(f"          occurs    : {se['occurrence_count']}×")
        print(f"      │")
        print(f"      │  sense belongs to term {te['strongs']}")
        print(f"      ▼")
        print(f"  TERM    {te['strongs']}   {te['sense_count']} sense(s) of this lemma"
              + ("   ★ its base splits into other terms (homonyms)" if te["★ shares_base_with_other_terms"] else ""))
        print(f"          TREE      : {te['tree'][:150].replace(chr(10),' ')}")
        print(f"                      ←── the LEMMA's full range: context, NOT this span's meaning")
        sibs = [x for x in T["sense"] if x["term_id"] == te["term_id"] and x["sense_id"] != se["sense_id"]]
        if sibs:
            print(f"          the lemma's OTHER senses — real meanings, but NOT what this span says:")
            for x in sibs:
                print(f"            {x['strongs']}  {x['head']!r:28} {x['occurrence_count']:>4}×")
    return 0


if __name__ == "__main__":
    sys.exit(main())
