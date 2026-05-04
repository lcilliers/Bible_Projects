"""_exploratory_unclassified_verse_sample_v1_20260504.py — read-only.

Per-verse sample builder. Picks N distinct verses that have at least one
unclassified OWNER term, and for each one packages:
  - verse_text + all_spans (full morph decode)
  - terms_to_classify: programme-relevant Strong's in this verse with no
    existing verse_context row
  - term_extracts: lexical foundation per Strong's (gloss, senses excerpt)

Output JSON is consumed by _exploratory_brief_verse_router_v1_20260504.py.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import random
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

import requests

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
POS_JSON = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.json")
BASE = os.getenv("STEP_LOCAL_URL", "http://localhost:8989").rstrip("/")
CONTENT_POS = {"noun", "verb", "adjective"}
SPAN_RE = re.compile(
    r"<span\s+morph='(?P<morph>[^']+)'\s+strong='(?P<strong>[^']+)'\s*>(?P<text>[^<]*)</span>"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_via_search(reference, version, session):
    osis = reference.replace(" ", ".").replace(":", ".")
    url = f"{BASE}/rest/search/masterSearch/reference={osis}|version={version}"
    try:
        r = session.get(url, timeout=10)
        if r.status_code != 200 or 'errorMessage' in r.text[:200]:
            return None
        data = r.json()
        val = data.get("value", "")
        if val:
            return {"_html": val}
    except Exception:
        return None
    return None


def parse_spans(html_text):
    return [
        {"morph": m.group("morph"), "strong": m.group("strong"),
         "text": html.unescape(m.group("text"))}
        for m in SPAN_RE.finditer(html_text or "")
    ]


def get_term_meta(conn, strong):
    r = conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               mt.status, mt.owning_registry_fk
          FROM mti_terms mt
         WHERE mt.strongs_number = ? AND mt.delete_flagged = 0
    """, (strong,)).fetchone()
    if not r:
        return None
    base = dict(r)
    if r["owning_registry_fk"]:
        rw = conn.execute(
            "SELECT no, word FROM word_registry WHERE id = ?",
            (r["owning_registry_fk"],)
        ).fetchone()
        if rw:
            base["owning_registry"] = f"R{rw['no']:03d} {rw['word']}"
    ti = conn.execute("""
        SELECT ti.short_def_mounce, ti.meaning, ti.lsj_entry, ti.parsed_meaning_id,
               ti.step_search_gloss, ti.word_analysis_gloss
          FROM wa_term_inventory ti
         WHERE ti.strongs_number = ? AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
         LIMIT 1
    """, (strong,)).fetchone()
    if ti:
        base.update(dict(ti))
    return base


def get_term_extract(conn, strong):
    meta = get_term_meta(conn, strong)
    if not meta:
        return None
    return {
        "strong": meta["strongs_number"],
        "transliteration": meta["transliteration"],
        "gloss": meta["gloss"],
        "language": meta["language"],
        "status": meta["status"],
        "owning_registry": meta.get("owning_registry"),
        "step_search_gloss": meta.get("step_search_gloss"),
        "word_analysis_gloss": meta.get("word_analysis_gloss"),
        "short_def_mounce": meta.get("short_def_mounce"),
        "meaning_excerpt": (meta.get("meaning") or "")[:600],
    }


def decode_morph(code, language):
    body = code.split(":", 1)[-1]
    if language == "Hebrew":
        parts = body.split("/")
        if parts and parts[0] and parts[0][0] in ("H", "A"):
            parts[0] = parts[0][1:]
        non_suffix = [p for p in parts if p and not p.startswith("S")]
        head = non_suffix[-1] if non_suffix else (parts[-1] if parts else "")
        first = head[0] if head else "?"
        pos_map = {"N": "noun", "V": "verb", "A": "adjective", "P": "pronoun",
                   "R": "preposition", "T": "particle", "D": "adverb",
                   "C": "conjunction", "S": "suffix"}
        return {"raw": code, "head": head, "pos": pos_map.get(first, f"unknown:{first}")}
    else:
        head = body.split("-", 1)[0]
        word_tags = {"PREP": "preposition", "CONJ": "conjunction",
                     "ADV": "adverb", "INJ": "interjection",
                     "PRT": "particle", "COND": "conditional-particle"}
        if head in word_tags:
            return {"raw": code, "head": head, "pos": word_tags[head]}
        letter_map = {"N": "noun", "V": "verb", "A": "adjective",
                      "P": "pronoun-personal", "T": "article"}
        first = head[:1]
        return {"raw": code, "head": head, "pos": letter_map.get(first, f"unknown:{head}")}


def select_unclassified_verses(conn, n, pos_lookup, strongs_filter=None):
    """Return list of (reference, [(vr_id, mti_id, strong), ...]) for verses
    with at least one unclassified content-POS OWNER term.

    If strongs_filter is given, restrict to verses where at least one of those
    Strong's is among the unclassified OWNER pairs. The verse's full
    terms_to_classify list still includes ALL its unclassified OWNER terms,
    not just the filter target."""
    content = [s for s, p in pos_lookup.items() if p in CONTENT_POS]
    quoted = ",".join("'" + s + "'" for s in content)
    rows = conn.execute(f"""
        SELECT vr.id        AS vr_id,
               vr.reference AS reference,
               mt.id        AS mti_id,
               ti.strongs_number AS strong,
               wr.no        AS reg_no,
               wr.word      AS reg_word
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
          JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                            AND mt.delete_flagged=0
                            AND mt.status IN ('extracted','extracted_thin')
         WHERE vr.delete_flagged=0
           AND wr.phase1_status != 'Excluded'
           AND ti.strongs_number IN ({quoted})
           AND NOT EXISTS (
             SELECT 1 FROM verse_context vc
              WHERE vc.verse_record_id = vr.id
                AND vc.mti_term_id = mt.id
                AND vc.delete_flagged = 0
           )
    """).fetchall()
    by_ref = defaultdict(list)
    for r in rows:
        by_ref[r["reference"]].append({
            "vr_id": r["vr_id"], "mti_id": r["mti_id"],
            "strong": r["strong"],
            "owning_registry": f"R{r['reg_no']:03d} {r['reg_word']}",
        })
    refs = list(by_ref.keys())
    if strongs_filter:
        wanted = set(strongs_filter)
        refs = [r for r in refs
                if any(t["strong"] in wanted for t in by_ref[r])]
    rng = random.Random(20260504)
    rng.shuffle(refs)
    selected = []
    for ref in refs[:n]:
        selected.append((ref, by_ref[ref]))
    return selected


def build_verse_record(conn, reference, terms_in_verse, session, span_cache):
    if reference not in span_cache:
        all_spans = []
        for version in ("OSHB", "SBLG_th"):
            result = fetch_via_search(reference, version, session)
            if not result:
                continue
            for s in parse_spans(result.get("_html", "")):
                language = "Hebrew" if version == "OSHB" else "Greek"
                term_meta = get_term_meta(conn, s["strong"])
                d = decode_morph(s["morph"], language)
                all_spans.append({
                    "language": language,
                    "strong": s["strong"],
                    "original_text": s["text"],
                    "morph_raw": s["morph"],
                    "morph_decoded": d,
                    "gloss": term_meta["gloss"] if term_meta else None,
                    "owning_registry": term_meta.get("owning_registry") if term_meta else None,
                })
        span_cache[reference] = all_spans
    vr = conn.execute(
        "SELECT verse_text FROM wa_verse_records WHERE reference = ? "
        "AND delete_flagged = 0 LIMIT 1", (reference,)
    ).fetchone()
    return {
        "reference": reference,
        "verse_text": vr["verse_text"] if vr else None,
        "all_spans": span_cache[reference],
        "terms_to_classify": [
            {
                "verse_record_id": t["vr_id"],
                "mti_term_id": t["mti_id"],
                "strong": t["strong"],
                "owning_registry": t["owning_registry"],
            }
            for t in terms_in_verse
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--strongs", default=None,
                    help="comma-separated Strong's to concentrate on; verses "
                         "must contain at least one as an unclassified OWNER term")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    strongs_filter = None
    if args.strongs:
        strongs_filter = [s.strip() for s in args.strongs.split(",") if s.strip()]

    tag = ""
    if strongs_filter:
        tag = "-" + "-".join(strongs_filter)
    out_path = args.out or os.path.join(
        "outputs", "markdown",
        f"unclassified-verse-sample-{args.n}-verses{tag}-{today_compact()}.json"
    )

    with open(POS_JSON, encoding="utf-8") as f:
        pos_lookup = {k: v.get("pos") for k, v in json.load(f)["results"].items()}

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print(f"Selecting {args.n} unclassified verses"
          + (f" (concentrated on {strongs_filter})" if strongs_filter else "")
          + "...")
    chosen = select_unclassified_verses(conn, args.n, pos_lookup, strongs_filter)
    print(f"Selected: {len(chosen)} verses")
    total_pairs = sum(len(t) for _, t in chosen)
    print(f"Total terms-to-classify across these verses: {total_pairs}")

    session = requests.Session()
    span_cache = {}
    verse_records = []
    seen_strongs = set()
    for i, (ref, terms) in enumerate(chosen, 1):
        rec = build_verse_record(conn, ref, terms, session, span_cache)
        if not rec["verse_text"]:
            continue
        verse_records.append(rec)
        for t in rec["terms_to_classify"]:
            seen_strongs.add(t["strong"])
        if i % 10 == 0:
            print(f"  [{i}/{len(chosen)}] built")

    term_extracts = {}
    for s in seen_strongs:
        ext = get_term_extract(conn, s)
        if ext:
            term_extracts[s] = ext

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_verses": len(verse_records),
            "n_terms_to_classify": sum(len(v["terms_to_classify"]) for v in verse_records),
            "n_unique_strongs": len(term_extracts),
            "strongs_filter": strongs_filter,
            "selection_criteria": (
                "verses with at least one unclassified content-POS OWNER term"
                + (f" (concentrated on {strongs_filter})" if strongs_filter else "")
            ),
            "source": "STEP local API + local DB",
        },
        "verses": verse_records,
        "term_extracts": term_extracts,
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
    print(f"Wrote: {out_path}")
    print(f"Verses: {payload['meta']['n_verses']} · "
          f"terms-to-classify: {payload['meta']['n_terms_to_classify']} · "
          f"unique strongs: {payload['meta']['n_unique_strongs']}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
