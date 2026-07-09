"""_exploratory_verse_context_record_v1_20260503.py — read-only prototype.

Builds a JSON record per verse with:
  - verse reference + verse text (ESV)
  - spans: per-span term/morph/english/original-language form + gloss + abbreviated meaning

Plus a sidecar 'term_extracts' node with one entry per unique Strong's referenced
across all spans in the requested verses, carrying full lexical + morphology data.

Sources:
  - Verse spans: STEP local API (OSHB for Hebrew, SBLG_th for Greek; ESV_th for English)
  - Term layer: local mti_terms + wa_term_inventory + wa_meaning_parsed + wa_lsj_parsed

Usage:
  python scripts/_exploratory_verse_context_record_v1_20260503.py \\
    --refs "Hos 11:9" "Gen 15:15" "Neh 9:17"
  python scripts/_exploratory_verse_context_record_v1_20260503.py \\
    --vid 78177 78178   # verse_record_ids
"""
from __future__ import annotations

import argparse
import html
import json
import os
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
OUT_JSON = os.path.join("outputs", "markdown", "verse-context-records-sample-20260503.json")

# OSHM / Robinson POS letters → readable
OSHM_POS = {
    "N": "noun", "V": "verb", "A": "adjective", "P": "pronoun",
    "R": "preposition", "S": "suffix", "T": "particle", "D": "adverb",
    "C": "conjunction", "I": "interjection",
}
OSHM_PARTICLE_SUB = {
    "n": "negative", "d": "definite-article", "j": "interjection",
    "o": "object-marker", "r": "relative", "i": "interrogative",
    "m": "demonstrative", "c": "conjunction-particle",
}
OSHM_GENDER = {"m": "masculine", "f": "feminine", "b": "common"}
OSHM_NUMBER = {"s": "singular", "p": "plural", "d": "dual"}
OSHM_STATE = {"a": "absolute", "c": "construct", "d": "determined"}
OSHM_VERB_STEM = {
    "q": "Qal", "n": "Niphal", "p": "Piel", "u": "Pual",
    "h": "Hiphil", "o": "Hophal", "t": "Hithpael",
}
OSHM_VERB_FORM = {
    "p": "perfect", "q": "imperfect", "i": "imperative",
    "r": "participle", "s": "passive participle", "c": "infinitive construct",
    "a": "infinitive absolute", "j": "jussive", "h": "cohortative",
    "w": "waw-consecutive",
}

# Robinson Greek mappings (compact)
ROBINSON_POS = {
    "N": "noun", "V": "verb", "A": "adjective",
    "P": "pronoun-personal", "F": "pronoun-reflexive",
    "D": "pronoun-demonstrative", "I": "pronoun-interrogative",
    "Q": "pronoun-correlative", "R": "pronoun-relative",
    "C": "pronoun-reciprocal", "S": "pronoun-possessive",
    "X": "pronoun-indefinite", "K": "pronoun-possessive-K",
    "T": "article",
}
ROBINSON_WORD = {"PREP": "preposition", "CONJ": "conjunction", "ADV": "adverb",
                 "INJ": "interjection", "COND": "conditional-particle",
                 "PRT": "particle", "ARAM": "aramaic", "HEB": "hebrew"}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def decode_oshm(code: str) -> dict:
    """Decode an OSHM morph code (e.g. 'oshm:HNcmsc/Sp1cs') into structured fields."""
    body = code.split(":", 1)[-1]
    parts = body.split("/")
    head_segments = []
    suffix_segment = None
    prefix_segments = []
    # Strip leading H/A from first segment
    if parts and parts[0] and parts[0][0] in ("H", "A"):
        parts[0] = parts[0][1:]
    for i, p in enumerate(parts):
        if not p:
            continue
        first = p[0]
        if first == "S":
            suffix_segment = p
        elif i < len(parts) - 1 and first in ("C", "D", "R", "T") and len(p) <= 3:
            prefix_segments.append(p)
        else:
            head_segments.append(p)
    # Pick the head — last non-suffix
    head = head_segments[-1] if head_segments else (parts[-1] if parts else "")
    pos_letter = head[0] if head else None
    pos_label = OSHM_POS.get(pos_letter, f"unknown:{pos_letter}")
    decoded = {
        "raw": code,
        "head": head,
        "pos": pos_label,
        "prefixes": prefix_segments,
        "suffix": suffix_segment,
    }
    # Decode head subfields when noun/adjective
    if head and head[0] in ("N", "A") and len(head) >= 5:
        # Format: Ncmsa = N + c (common) + m (masc) + s (sing) + a (absolute)
        # OR Ncmsc/Sp1cs
        if len(head) >= 5:
            decoded["category"] = head[1] if len(head) > 1 else None
            decoded["gender"] = OSHM_GENDER.get(head[2]) if len(head) > 2 else None
            decoded["number"] = OSHM_NUMBER.get(head[3]) if len(head) > 3 else None
            decoded["state"] = OSHM_STATE.get(head[4]) if len(head) > 4 else None
    elif head and head[0] == "V" and len(head) >= 5:
        # Verbs: V + stem + form + person + gender + number
        decoded["stem"] = OSHM_VERB_STEM.get(head[1]) if len(head) > 1 else None
        decoded["form"] = OSHM_VERB_FORM.get(head[2]) if len(head) > 2 else None
        decoded["person_gender_number"] = head[3:] if len(head) > 3 else None
    elif head and head[0] == "P" and len(head) >= 4:
        decoded["pronoun_type"] = head[1] if len(head) > 1 else None
        decoded["person"] = head[2] if len(head) > 2 else None
        decoded["gender"] = OSHM_GENDER.get(head[3]) if len(head) > 3 else None
        decoded["number"] = OSHM_NUMBER.get(head[4]) if len(head) > 4 else None
    elif head and head[0] == "T" and len(head) >= 2:
        decoded["particle_subtype"] = OSHM_PARTICLE_SUB.get(head[1])
    return decoded


def decode_robinson(code: str) -> dict:
    body = code.split(":", 1)[-1]
    head = body.split("-", 1)[0] if "-" in body else body
    decoded = {"raw": code, "head": head}
    if head in ROBINSON_WORD:
        decoded["pos"] = ROBINSON_WORD[head]
    elif head and head[0] in ROBINSON_POS:
        decoded["pos"] = ROBINSON_POS[head[0]]
        decoded["features"] = body
    else:
        decoded["pos"] = f"unknown:{head}"
    return decoded


def fetch_verse_with_spans(reference_osis: str, version: str,
                           session: requests.Session) -> dict | None:
    """Fetch a verse via STEP masterSearch using a reference token, return
    parsed spans. We use a passage-ish trick: search for a common Strong's that
    occurs in the verse, then filter results.

    Simpler: STEP supports `passage` via a different endpoint variant. We try a
    few; this prototype uses the masterSearch hit cache by querying a reference
    range. Since we already have the ESV verse text in our DB, we just need
    the original-language span data, which we obtain via the OSHB/SBLG search
    on a Strong's known to be in the verse.

    For the prototype, we take a different path: query OSHB/SBLG passage HTML
    via /rest/passage/getPassageText/{version}/{reference} — see
    https://www.stepbible.org/passage/.
    """
    paths = [
        f"/rest/bibles/getBibleText/{version}/{reference_osis}",
        f"/rest/passage/biblePassage/{version}/{reference_osis}",
        f"/rest/passage/getPassageText/{version}/{reference_osis}",
    ]
    for path in paths:
        try:
            r = session.get(f"{BASE}{path}", timeout=10)
            if r.status_code == 200 and 'errorMessage' not in r.text[:200]:
                return r.json() if r.headers.get('content-type','').startswith('application/json') else {"_html": r.text}
        except Exception:
            pass
    return None


def fetch_via_search(reference: str, version: str,
                     session: requests.Session,
                     known_strong: str = None) -> dict | None:
    """Fetch a verse via STEP's reference-based passage search.

    Endpoint: /rest/search/masterSearch/reference={ref}|version={version}
    Response shape: {value: <HTML with morph+strong spans>, osisId, ...}
    """
    osis = reference.replace(" ", ".").replace(":", ".")
    url = f"{BASE}/rest/search/masterSearch/reference={osis}|version={version}"
    try:
        r = session.get(url, timeout=10)
        if r.status_code != 200 or 'errorMessage' in r.text[:200]:
            return None
        data = r.json()
        val = data.get("value", "")
        if val:
            return {"_html": val, "osisId": data.get("osisId")}
    except Exception:
        return None
    return None


SPAN_RE = re.compile(
    r"<span\s+morph='(?P<morph>[^']+)'\s+strong='(?P<strong>[^']+)'\s*>(?P<text>[^<]*)</span>"
)


def parse_spans(html_text: str) -> list[dict]:
    """Extract all morph+strong spans from verse HTML."""
    spans = []
    for m in SPAN_RE.finditer(html_text or ""):
        spans.append({
            "morph": m.group("morph"),
            "strong": m.group("strong"),
            "text": html.unescape(m.group("text")),
        })
    return spans


def get_term_meta(conn: sqlite3.Connection, strong: str) -> dict | None:
    """Fetch term-level meta from local DB."""
    r = conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               mt.status, mt.owning_registry_fk
          FROM mti_terms mt
         WHERE mt.strongs_number = ? AND mt.delete_flagged = 0
    """, (strong,)).fetchone()
    if not r:
        return None
    base = dict(r)
    # Owning registry word
    if r["owning_registry_fk"]:
        rw = conn.execute(
            "SELECT no, word FROM word_registry WHERE id = ?",
            (r["owning_registry_fk"],)
        ).fetchone()
        if rw:
            base["owning_registry"] = f"R{rw['no']:03d} {rw['word']}"
    # Pull abbreviated meaning + senses
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


def get_term_extract(conn: sqlite3.Connection, strong: str) -> dict | None:
    """Fetch the full term extract: meaning, senses, stems, root family, LSJ.
    Mirrors the lexical foundation rendered in §2 of the Session A .md."""
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
    # Parsed meaning structure
    if meta.get("parsed_meaning_id"):
        senses = conn.execute("""
            SELECT level_code, level_depth, parent_level_code, sense_text, domain_tag
              FROM wa_meaning_sense
             WHERE parsed_meaning_id = ?
             ORDER BY sort_order
             LIMIT 30
        """, (meta["parsed_meaning_id"],)).fetchall()
        extract["senses"] = [dict(s) for s in senses]
        stems = conn.execute("""
            SELECT stem_name, stem_type, sense_count, top_sense_text
              FROM wa_meaning_stem
             WHERE parsed_meaning_id = ?
        """, (meta["parsed_meaning_id"],)).fetchall()
        extract["stems"] = [dict(s) for s in stems]
    # Root family
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


def build_verse_record(conn, vid: int = None, reference: str = None,
                       session: requests.Session = None) -> dict:
    """Build the JSON record for one verse."""
    if vid:
        vr = conn.execute("""
            SELECT id, book_id, chapter, verse_num, reference, verse_text,
                   target_word, span_strong_match, term_inv_id
              FROM wa_verse_records WHERE id = ?
        """, (vid,)).fetchone()
    else:
        # Look up the first vc record matching the reference text
        vr = conn.execute("""
            SELECT id, book_id, chapter, verse_num, reference, verse_text,
                   target_word, span_strong_match, term_inv_id
              FROM wa_verse_records
             WHERE reference = ? AND delete_flagged = 0
             LIMIT 1
        """, (reference,)).fetchone()
    if not vr:
        return {"error": f"verse not found: vid={vid} ref={reference}"}

    ref = vr["reference"]
    record = {
        "verse_record_id": vr["id"],
        "reference": ref,
        "verse_text": vr["verse_text"],
        "target_word_in_pull": vr["target_word"],
        "spans_hebrew": [],
        "spans_greek": [],
        "spans_decoded": [],
    }

    # Determine which language version to query
    # OT books: book_id <= 39, NT: > 39 (typical, but verify)
    # We'll query both OSHB and SBLG and use whichever returns data
    osis = ref.replace(" ", ".").replace(":", ".")
    for version in ("OSHB", "SBLG_th"):
        result = fetch_via_search(ref, version, session)
        if not result:
            continue
        spans = parse_spans(result.get("_html", ""))
        if not spans:
            continue
        decoded = []
        for s in spans:
            d = decode_oshm(s["morph"]) if version == "OSHB" else decode_robinson(s["morph"])
            term_meta = get_term_meta(conn, s["strong"])
            decoded.append({
                "language": "Hebrew" if version == "OSHB" else "Greek",
                "strong": s["strong"],
                "original_text": s["text"],
                "morph_raw": s["morph"],
                "morph_decoded": d,
                "gloss": term_meta["gloss"] if term_meta else None,
                "abbreviated_meaning": (
                    (term_meta.get("step_search_gloss") if term_meta else None)
                    or (term_meta.get("word_analysis_gloss") if term_meta else None)
                    or (term_meta.get("short_def_mounce") if term_meta else None)
                    or (term_meta["gloss"] if term_meta else None)
                ),
                "owning_registry": term_meta.get("owning_registry") if term_meta else None,
            })
        if version == "OSHB":
            record["spans_hebrew"] = decoded
        else:
            record["spans_greek"] = decoded
        record["spans_decoded"].extend(decoded)
    return record


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vid", type=int, nargs="*", default=[])
    ap.add_argument("--refs", nargs="*", default=[])
    args = ap.parse_args()

    if not args.vid and not args.refs:
        # Default sample: Hos 11:9 (the user's diagnostic example) + Gen 15:15 + Neh 9:17
        args.refs = ["Hos 11:9", "Gen 15:15", "Neh 9:17"]

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    session = requests.Session()

    records = []
    for v in args.vid:
        records.append(build_verse_record(conn, vid=v, session=session))
    for r in args.refs:
        records.append(build_verse_record(conn, reference=r, session=session))

    # Build term_extracts: union of all unique Strong's referenced
    seen = set()
    term_extracts = {}
    for rec in records:
        for span in rec.get("spans_decoded", []):
            s = span["strong"]
            if s in seen:
                continue
            seen.add(s)
            ext = get_term_extract(conn, s)
            if ext:
                term_extracts[s] = ext

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_verses": len(records),
            "n_unique_strongs": len(term_extracts),
            "source": "STEP local API (OSHB / SBLG_th masterSearch) + local DB term layer",
        },
        "verses": records,
        "term_extracts": term_extracts,
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)

    print(f"Wrote: {OUT_JSON}")
    print(f"Verses: {len(records)} · Unique Strong's: {len(term_extracts)}")
    for rec in records:
        if "error" in rec:
            print(f"  {rec.get('error')}")
        else:
            n_h = len(rec.get("spans_hebrew", []))
            n_g = len(rec.get("spans_greek", []))
            print(f"  {rec['reference']:<14} vid={rec['verse_record_id']:>6}  H={n_h}  G={n_g}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
