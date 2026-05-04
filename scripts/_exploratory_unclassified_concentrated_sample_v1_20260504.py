"""_exploratory_unclassified_concentrated_sample_v1_20260504.py — read-only.

Like _exploratory_unclassified_sample_v1_20260504.py, but pulls all pairs
from one or two specified Strong's numbers (concentrated test cohort).

Usage:
  python scripts/_exploratory_unclassified_concentrated_sample_v1_20260504.py \
      --strongs H3045 --n 100 --out outputs/markdown/foo.json
  python scripts/_exploratory_unclassified_concentrated_sample_v1_20260504.py \
      --strongs H3045,H4672 --n 100
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
from datetime import datetime, timezone

import requests

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
BASE = os.getenv("STEP_LOCAL_URL", "http://localhost:8989").rstrip("/")
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
    extract = {
        "strong": meta["strongs_number"],
        "transliteration": meta["transliteration"],
        "gloss": meta["gloss"],
        "language": meta["language"],
        "status": meta["status"],
        "owning_registry": meta.get("owning_registry"),
        "step_search_gloss": meta.get("step_search_gloss"),
        "word_analysis_gloss": meta.get("word_analysis_gloss"),
        "short_def_mounce": meta.get("short_def_mounce"),
        "meaning": (meta.get("meaning") or "")[:1500],
        "lsj_entry": (meta.get("lsj_entry") or "")[:1500] if meta.get("lsj_entry") else None,
    }
    if meta.get("parsed_meaning_id"):
        senses = conn.execute("""
            SELECT level_code, level_depth, parent_level_code, sense_text, domain_tag
              FROM wa_meaning_sense
             WHERE parsed_meaning_id = ?
             ORDER BY sort_order LIMIT 30
        """, (meta["parsed_meaning_id"],)).fetchall()
        extract["senses"] = [dict(s) for s in senses]
    rf = conn.execute("""
        SELECT root_code, root_language, root_gloss, note
          FROM wa_term_root_family rf
          JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
         WHERE ti.strongs_number = ? AND ti.term_owner_type='OWNER'
           AND ti.delete_flagged=0 AND rf.delete_flagged=0
         LIMIT 5
    """, (strong,)).fetchall()
    extract["root_family"] = [dict(r) for r in rf]
    return extract


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


def select_pairs_for_strongs(conn, strongs_list, n):
    quoted = ",".join("'" + s + "'" for s in strongs_list)
    rows = conn.execute(f"""
        SELECT vr.id AS vr_id, mt.id AS mti_id, mt.strongs_number,
               wr.no AS reg_no, wr.word AS reg_word, vr.reference
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
    if not rows:
        return []
    rng = random.Random(20260504)
    by_strong = {}
    for r in rows:
        by_strong.setdefault(r["strongs_number"], []).append(
            (r["vr_id"], r["mti_id"])
        )
    for k in by_strong:
        rng.shuffle(by_strong[k])
    if len(strongs_list) == 1:
        return by_strong.get(strongs_list[0], [])[:n]
    selected = []
    per = n // len(strongs_list)
    for s in strongs_list:
        selected.extend(by_strong.get(s, [])[:per])
    if len(selected) < n:
        for s in strongs_list:
            extra = by_strong.get(s, [])[per:]
            for p in extra:
                if len(selected) >= n:
                    break
                selected.append(p)
            if len(selected) >= n:
                break
    return selected[:n]


def build_record(conn, vr_id, mti_id, session, cache):
    vr = conn.execute("""
        SELECT id, book_id, chapter, verse_num, reference, verse_text,
               target_word, term_inv_id
          FROM wa_verse_records WHERE id = ?
    """, (vr_id,)).fetchone()
    if not vr:
        return None
    mt = conn.execute("""
        SELECT strongs_number, language FROM mti_terms WHERE id = ?
    """, (mti_id,)).fetchone()
    if not mt:
        return None
    ref = vr["reference"]
    record = {
        "verse_record_id": vr["id"],
        "mti_term_id": mti_id,
        "reference": ref,
        "verse_text": vr["verse_text"],
        "target_word_in_pull": vr["target_word"],
        "strong_being_analysed": mt["strongs_number"],
        "spans_decoded": [],
    }
    if ref not in cache:
        all_spans = []
        for version in ("OSHB", "SBLG_th"):
            result = fetch_via_search(ref, version, session)
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
        cache[ref] = all_spans
    record["spans_decoded"] = cache[ref]
    return record


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strongs", required=True,
                    help="comma-separated Strong's, e.g. H3045 or H3045,H4672")
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    strongs_list = [s.strip() for s in args.strongs.split(",") if s.strip()]
    if not strongs_list:
        print("ERROR: --strongs required", file=sys.stderr)
        return 2

    tag = "-".join(strongs_list)
    out_path = args.out or os.path.join(
        "outputs", "markdown",
        f"unclassified-sample-{args.n}-pairs-{tag}-{today_compact()}.json"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print(f"Selecting {args.n} unclassified pairs for {strongs_list}...")
    pairs = select_pairs_for_strongs(conn, strongs_list, args.n)
    print(f"Selected: {len(pairs)} pairs")

    session = requests.Session()
    cache = {}
    records = []
    seen_strongs = set()
    for i, (vr_id, mti_id) in enumerate(pairs, 1):
        rec = build_record(conn, vr_id, mti_id, session, cache)
        if not rec:
            continue
        records.append(rec)
        seen_strongs.add(rec["strong_being_analysed"])
        if i % 10 == 0:
            print(f"  [{i}/{len(pairs)}] built")

    term_extracts = {}
    for s in seen_strongs:
        ext = get_term_extract(conn, s)
        if ext:
            term_extracts[s] = ext

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_pairs": len(records),
            "n_unique_strongs": len(term_extracts),
            "n_unique_verses": len(set(r["reference"] for r in records)),
            "strongs_filter": strongs_list,
            "selection_criteria": "unclassified pairs concentrated on specified Strong's",
            "source": "STEP local API + local DB",
        },
        "verses": records,
        "term_extracts": term_extracts,
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
    print(f"Wrote: {out_path}")
    print(f"Unique verses: {payload['meta']['n_unique_verses']} · "
          f"unique strongs: {payload['meta']['n_unique_strongs']}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
