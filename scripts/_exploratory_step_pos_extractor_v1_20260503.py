"""_exploratory_step_pos_extractor_v1_20260503.py — read-only.

Builds a Strong's -> Part-of-Speech lookup by querying STEP's local API:

  /rest/search/masterSearch/strong={strong}|version={OSHB|SBLG_th}

The response contains verse HTML with `<span morph='oshm:...' strong='H...'>` tags
per word. We extract the morph code attached to the target Strong's number,
aggregate across all hit verses (60 max per query), and pick the most-frequent
POS letter as that Strong's POS.

OSHM scheme (Hebrew, OSHB) — second char after lang prefix:
  N noun  V verb  A adjective  P pronoun  R preposition  S suffix
  T particle (with subtypes: Tn negation, Td definite article, Tj interjection,
             To object marker, Tr relative, etc.)  D adverb  C conjunction

SBLG_th scheme (Greek) — second char similar but with different letter mappings:
  N noun  V verb  A adjective  R pronoun  P preposition  C conjunction
  D adverb  T particle/article  I interjection  X other

Defaults to first 100 Strong's for the sample run; pass --all to do everything.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone

import requests

DB_PATH = os.path.join("database", "bible_research.db")
OUT_JSON = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.json")
OUT_MD = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.md")

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

BASE = os.getenv("STEP_LOCAL_URL", "http://localhost:8989").rstrip("/")
MORPH_SPAN_RE = re.compile(
    r"<span\s+morph='(?P<morph>[^']+)'\s+strong='(?P<strong>[^']+)'"
)

# OSHM POS letter -> readable POS label (the second char after lang prefix)
HEBREW_POS = {
    "N": "noun", "V": "verb", "A": "adjective", "P": "pronoun",
    "R": "preposition", "S": "suffix", "T": "particle", "D": "adverb",
    "C": "conjunction",
}
# Greek (Robinson scheme used by SBLG_th) — word-tag and single-letter codes
# Word-tags: PREP, CONJ, ADV, INJ, COND, PRT, ARAM, HEB
# Single letters: N(oun), V(erb), A(djective), P(ersonal pronoun), T(article),
#                 F(reflexive pron), D(demonstrative pron), I(interrogative pron),
#                 Q(correlative pron), R(relative pron), C(reciprocal pron),
#                 S(possessive pron), X(indefinite pron), K(possessive)
GREEK_WORD_TAG = {
    "PREP": "preposition", "CONJ": "conjunction", "ADV": "adverb",
    "INJ": "interjection", "COND": "conditional-particle",
    "PRT": "particle", "ARAM": "aramaic", "HEB": "hebrew",
    "T": "article", "N": "noun", "V": "verb", "A": "adjective",
    "P": "pronoun-personal", "F": "pronoun-reflexive",
    "D": "pronoun-demonstrative", "I": "pronoun-interrogative",
    "Q": "pronoun-correlative", "R": "pronoun-relative",
    "C": "pronoun-reciprocal", "S": "pronoun-possessive",
    "X": "pronoun-indefinite", "K": "pronoun-possessive",
}

# Particle subtypes (third char) - useful for finer classification
HEBREW_PARTICLE_SUB = {
    "n": "negative", "d": "definite-article", "j": "interjection",
    "o": "object-marker", "r": "relative", "i": "interrogative",
    "m": "demonstrative", "c": "conjunction-particle",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalise_strong(s: str) -> str:
    """Pass the Strong's through unchanged.

    STEP's masterSearch keys on the FULL Extended Strong's identifier,
    including suffix letters (e.g. H4480A, H2617A, H5971G). Stripping the
    suffix returns 0 hits.
    """
    return s


def fetch_morphs_for_strong(strong: str, version: str, session: requests.Session,
                            timeout: int = 20) -> list[str]:
    """Return list of morph codes attached to this Strong's across all hit verses."""
    bare = normalise_strong(strong)
    url = f"{BASE}/rest/search/masterSearch/strong={bare}|version={version}"
    try:
        r = session.get(url, timeout=timeout)
        if r.status_code != 200:
            return []
        data = r.json()
    except Exception:
        return []
    morphs = []
    for hit in data.get("results", []):
        preview = hit.get("preview") or ""
        for m in MORPH_SPAN_RE.finditer(preview):
            if m.group("strong") == bare or m.group("strong") == strong:
                morphs.append(m.group("morph"))
    return morphs


_GREEK_LEAD_RE = re.compile(r"^([A-Z]+)")


def _hebrew_pos_token(code: str) -> str | None:
    """OSHM compound parser. Returns the POS letter of the HEAD lemma.

    OSHM compound layout:
      H<head>                       single word (head)
      H<prefix>/<head>              clitic prefix + head     (e.g. HC/Pp1cs   = wa-ani 'and I' -> head=P)
      H<head>/S<sfxFeat>            head + clitic suffix     (e.g. HNcmsc/Sp1cs = name-his -> head=N)
      H<prefix>/<head>/S<sfxFeat>   prefix + head + suffix   (e.g. HC/Ncmsc/Sp1cs)

    Rule: strip the lang prefix (H/A) from the first segment, then return the
    first letter of the LAST non-suffix segment (i.e. last segment whose first
    letter is not 'S'). Clitic prefixes (C/D/R) precede the head; suffixes (S)
    follow it; the head is whichever non-suffix segment is rightmost.
    """
    body = code.split(":", 1)[-1]
    parts = body.split("/")
    if not parts:
        return None
    first = parts[0]
    if first and first[0] in ("H", "A"):
        first = first[1:]
    parts[0] = first
    parts = [p for p in parts if p]
    non_suffix = [p for p in parts if not p.startswith("S")]
    if non_suffix:
        return non_suffix[-1][0]
    if parts:
        return parts[-1][0]
    return None


def _greek_pos_token(code: str) -> str | None:
    """Robinson: 'robinson:P-1GP' -> 'P'; 'robinson:PREP' -> 'PREP'.

    Strategy: take the head before the first hyphen; if it's a known word-tag
    (PREP/CONJ/ADV/INJ/COND/PRT) keep it as-is, else use the first letter.
    """
    body = code.split(":", 1)[-1]
    head = body.split("-", 1)[0]
    if head in {"PREP", "CONJ", "ADV", "INJ", "COND", "PRT", "ARAM", "HEB"}:
        return head
    return head[:1] if head else None


def derive_pos(morphs: list[str], language: str) -> dict:
    """Aggregate morph codes; return dominant POS + all observed token counts."""
    tokens = Counter()
    for code in morphs:
        token = (_hebrew_pos_token(code) if language == "Hebrew"
                 else _greek_pos_token(code))
        if token:
            tokens[token] += 1
    if not tokens:
        return {"pos": None, "dominant_token": None, "counts": {}}
    table = HEBREW_POS if language == "Hebrew" else GREEK_WORD_TAG
    dominant_token, _ = tokens.most_common(1)[0]
    pos_label = table.get(dominant_token, f"unknown:{dominant_token}")
    return {
        "pos": pos_label,
        "dominant_token": dominant_token,
        "counts": dict(tokens),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=100,
                    help="Limit number of Strong's to process (sample mode). "
                         "Use --all to process the full corpus.")
    ap.add_argument("--all", action="store_true",
                    help="Process every active OWNER Strong's (~2,617).")
    ap.add_argument("--strongs", nargs="*",
                    help="Restrict to a specific list of Strong's (e.g. H0589 H3808).")
    ap.add_argument("--sleep", type=float, default=0.05,
                    help="Sleep between requests (seconds).")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    if args.strongs:
        rows = []
        for s in args.strongs:
            r = conn.execute(
                "SELECT strongs_number, transliteration, gloss, language "
                "FROM mti_terms WHERE strongs_number = ? LIMIT 1", (s,)
            ).fetchone()
            if r:
                rows.append(dict(r))
            else:
                rows.append({"strongs_number": s, "transliteration": "?",
                             "gloss": "?", "language": "Hebrew" if s.startswith("H") else "Greek"})
    else:
        limit_clause = "" if args.all else f"LIMIT {args.limit}"
        rows = conn.execute(f"""
            SELECT DISTINCT mt.strongs_number, mt.transliteration, mt.gloss, mt.language
              FROM mti_terms mt
              JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                       AND ti.term_owner_type = 'OWNER'
                                       AND ti.delete_flagged = 0
             WHERE mt.delete_flagged = 0
             ORDER BY mt.strongs_number
             {limit_clause}
        """).fetchall()
        rows = [dict(r) for r in rows]

    print(f"Processing {len(rows)} Strong's...")
    session = requests.Session()
    results = {}
    for i, row in enumerate(rows, 1):
        strong = row["strongs_number"]
        lang = row["language"]
        version = "OSHB" if lang == "Hebrew" else "SBLG_th"
        morphs = fetch_morphs_for_strong(strong, version, session)
        pos_info = derive_pos(morphs, lang)
        results[strong] = {
            "strong": strong,
            "transliteration": row["transliteration"],
            "gloss": row["gloss"],
            "language": lang,
            "n_samples": len(morphs),
            **pos_info,
        }
        if i % 20 == 0 or i == len(rows):
            print(f"  [{i}/{len(rows)}] {strong} ({lang}) -> {pos_info['pos']}")
        if args.sleep:
            time.sleep(args.sleep)

    # Summary
    pos_dist = Counter(r["pos"] for r in results.values())
    print()
    print("--- POS distribution across processed Strong's ---")
    for pos, n in pos_dist.most_common():
        print(f"  {str(pos):20s}  {n}")

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_processed": len(results),
            "scope": "all" if args.all else
                     (f"strongs={args.strongs}" if args.strongs else f"first {args.limit}"),
            "source": "STEP local API (OSHB + SBLG_th masterSearch morph codes)",
        },
        "results": results,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"\nWrote: {OUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
