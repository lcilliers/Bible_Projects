"""
meaning_parser.py
─────────────────
Meaning text parser — populates wa_meaning_parsed, wa_meaning_sense,
wa_meaning_stem, wa_lsj_parsed.

Hebrew numbered:  each line parsed with level_code before ')'.
                  Stem labels detected (Qal, Hiphil, etc.) and extracted.
Hebrew prose:     single sense node at level_code='1'; PROSE_ONLY warning.
Greek prose:      semicolon-split; each clause = one top-level node.
LSJ (Greek):      first segment = gloss; bracketed content → domains;
                  philosopher names → philosophical_note; etymology keywords → etymology_note.

Re-parse: run_parser() is idempotent — deletes existing rows and re-inserts.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from .constants import PARSER_VERSION
from .db import get_max_id

# Hebrew stem labels (canonical)
_STEM_LABELS = [
    "Qal", "Niphal", "Piel", "Pual", "Hiphil", "Hophal",
    "Hitpael", "Hitpoel", "Polel", "Pulal", "Polal",
]
_STEM_LABEL_RE = re.compile(
    r"^\s*\((" + "|".join(re.escape(s) for s in _STEM_LABELS) + r")\)\s*$",
    re.IGNORECASE,
)
_STEM_TYPE = {
    "Qal": "simple",
    "Niphal": "passive",
    "Piel": "causative",
    "Pual": "passive",
    "Hiphil": "causative",
    "Hophal": "passive",
    "Hitpael": "reflexive",
    "Hitpoel": "reflexive",
    "Polel": "other",
    "Pulal": "other",
    "Polal": "other",
}

# Top-level level_code pattern: starts with digit
_TOP_LEVEL_RE = re.compile(r"^(\d+[a-z]?)\)")
_OUTLINE_RE   = re.compile(r"^(\d+[a-z0-9]*)\)")


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _parent_level_code(code: str) -> str | None:
    """Derive parent from level_code by truncating last alphanumeric segment."""
    # e.g. "1a1" → "1a", "1a" → "1", "1" → None
    if not code:
        return None
    m = re.match(r"^(.+?)([a-z\d])$", code)
    if m and m.group(1):
        parent = m.group(1).rstrip("abcdefghijklmnopqrstuvwxyz").rstrip("0123456789")
        if parent:
            return parent
    return None


def _parse_hebrew_numbered(text: str) -> tuple[list[dict], list[dict], list[str]]:
    """Parse a numbered Hebrew meaning definition.

    Returns (sense_nodes, stem_nodes, warnings).
    """
    lines = [l.rstrip() for l in text.splitlines() if l.strip()]
    nodes = []
    stems: dict[str, dict] = {}  # stem_name → {sense_count, top_sense_text}
    warnings = []
    sort_order = 0
    current_stem = None

    for line in lines:
        # Check for stem label (Qal), (Hiphil), etc.
        stem_match = _STEM_LABEL_RE.match(line)
        if stem_match:
            stem_name = stem_match.group(1).capitalize()
            current_stem = stem_name
            if stem_name not in stems:
                stems[stem_name] = {"sense_count": 0, "top_sense_text": ""}
            nodes.append({
                "level_code":        current_stem.lower(),
                "level_depth":       1,
                "parent_level_code": None,
                "sense_text":        f"({stem_name})",
                "is_stem_label":     1,
                "stem_label":        stem_name,
                "domain_tag":        None,
                "sort_order":        sort_order,
            })
            sort_order += 1
            continue

        outline_match = _OUTLINE_RE.match(line)
        if outline_match:
            code = outline_match.group(1)
            text_part = line[outline_match.end():].strip()
            # Count leading alpha chars for depth
            depth = len(re.sub(r"\d", "", code)) + 1
            parent = _parent_level_code(code)
            nodes.append({
                "level_code":        code,
                "level_depth":       depth,
                "parent_level_code": parent,
                "sense_text":        text_part,
                "is_stem_label":     0,
                "stem_label":        None,
                "domain_tag":        None,
                "sort_order":        sort_order,
            })
            sort_order += 1
            if current_stem and current_stem in stems:
                stems[current_stem]["sense_count"] += 1
                if not stems[current_stem]["top_sense_text"]:
                    stems[current_stem]["top_sense_text"] = text_part[:120]
        else:
            # Continuation line — append to last node if present
            if nodes:
                nodes[-1]["sense_text"] = (nodes[-1]["sense_text"] + " " + line.strip()).strip()

    stem_list = []
    for sname, sdata in stems.items():
        stem_list.append({
            "stem_name":      sname,
            "stem_type":      _STEM_TYPE.get(sname, "other"),
            "sense_count":    sdata["sense_count"],
            "top_sense_text": sdata["top_sense_text"],
        })

    return nodes, stem_list, warnings


def _parse_hebrew_prose(text: str) -> tuple[list[dict], list[str]]:
    """Parse a prose Hebrew definition (no outline markers)."""
    nodes = [{
        "level_code":        "1",
        "level_depth":       1,
        "parent_level_code": None,
        "sense_text":        text.strip(),
        "is_stem_label":     0,
        "stem_label":        None,
        "domain_tag":        None,
        "sort_order":        0,
    }]
    return nodes, ["PROSE_ONLY"]


def _parse_greek_prose(text: str) -> tuple[list[dict], list[str]]:
    """Parse a Greek prose definition. Each semicolon-separated clause = one node."""
    clauses = [c.strip() for c in text.split(";") if c.strip()]
    if not clauses:
        clauses = [text.strip()]
    nodes = []
    for i, clause in enumerate(clauses):
        nodes.append({
            "level_code":        str(i + 1),
            "level_depth":       1,
            "parent_level_code": None,
            "sense_text":        clause,
            "is_stem_label":     0,
            "stem_label":        None,
            "domain_tag":        None,
            "sort_order":        i,
        })
    return nodes, []


def _parse_lsj(lsj_text: str) -> dict:
    """Extract structured fields from LSJ text."""
    if not lsj_text:
        return {}

    segments = re.split(r"\.\s+", lsj_text, maxsplit=1)
    gloss = segments[0].strip() if segments else ""

    # Domains — bracketed abbreviations
    domains = re.findall(r"\[([A-Za-z0-9 ,]+?)\]", lsj_text)

    # Philosophers
    philosopher_names = ["Plato", "Aristotle", "Plut", "Philo", "Josephus",
                         "Epicurus", "Stoic", "Democrit"]
    found_philosophers = [p for p in philosopher_names if p in lsj_text]
    philosophical_note = "; ".join(found_philosophers) if found_philosophers else None

    # Etymology
    etym_keywords = ["from", "deriv", "root", "akin", "cogn"]
    etym_sentences = [
        s.strip() for s in re.split(r"[.;]", lsj_text)
        if any(k in s.lower() for k in etym_keywords)
    ]
    etymology_note = "; ".join(etym_sentences[:2]) if etym_sentences else None

    # Cognate forms — comma-separated italics markers in raw text
    cognates = re.findall(r"\b([A-Z][a-z]+ós|[A-Z][a-z]+ē|[A-Z][a-z]+on)\b", lsj_text)

    return {
        "lsj_gloss":             gloss,
        "lsj_domains":           json.dumps(domains) if domains else None,
        "lsj_philosophical_note": philosophical_note,
        "lsj_etymology_note":    etymology_note,
        "lsj_cognate_forms":     json.dumps(cognates) if cognates else None,
    }


def _is_numbered(text: str) -> bool:
    return bool(_OUTLINE_RE.search(text[:200]))


def parse_term(vocab: dict) -> dict:
    """Parse vocab data for one term into structured parse result.

    Args:
        vocab: dict from step_client.get_vocab_info()

    Returns dict with keys:
        sense_nodes, stem_nodes, lsj_fields, meta
    """
    language = vocab.get("language", "Hebrew")
    meaning = vocab.get("medium_def", "") or ""
    lsj_text = vocab.get("lsj_entry", "") or ""
    strongs = vocab.get("strong_number", "")
    warnings = []

    # Parse meaning
    if not meaning:
        sense_nodes = []
        stem_nodes = []
    elif language in ("Hebrew", "Aramaic"):  # Aramaic is Hebrew-script (OSHB) — parse like Hebrew, not Greek
        if _is_numbered(meaning):
            sense_nodes, stem_nodes, w = _parse_hebrew_numbered(meaning)
            warnings.extend(w)
        else:
            sense_nodes, w = _parse_hebrew_prose(meaning)
            stem_nodes = []
            warnings.extend(w)
    else:  # Greek
        sense_nodes, w = _parse_greek_prose(meaning)
        stem_nodes = []
        warnings.extend(w)

    # Parse LSJ (Greek only)
    lsj_fields = _parse_lsj(lsj_text) if language == "Greek" and lsj_text else {}

    has_causative = any(
        n["stem_label"] in ("Hiphil", "Piel") for n in (stem_nodes or [])
    ) or bool(re.search(r"\b(Hiphil|Piel)\b", meaning, re.IGNORECASE))

    return {
        "sense_nodes": sense_nodes,
        "stem_nodes":  stem_nodes,
        "lsj_fields":  lsj_fields,
        "meta": {
            "top_sense_count":    sum(1 for n in sense_nodes if n["level_depth"] == 1 and not n["is_stem_label"]),
            "stem_count":         len(stem_nodes),
            "has_causative_stem": 1 if has_causative else 0,
            "has_domain_tags":    0,
            "parse_warnings":     json.dumps(warnings) if warnings else None,
        },
    }


def run_parser(conn, term_inv_id: int, vocab: dict) -> int:
    """Parse and persist meaning data for one term.

    Idempotent: deletes existing rows for term_inv_id before re-inserting.
    Returns wa_meaning_parsed.id.
    """
    strongs = vocab.get("strong_number", "")
    language = vocab.get("language", "Hebrew")

    # Delete existing parsing rows (idempotent re-parse)
    existing = conn.execute(
        "SELECT id FROM wa_meaning_parsed WHERE term_inv_id = ?", (term_inv_id,)
    ).fetchone()
    if existing:
        old_id = existing["id"]
        conn.execute("DELETE FROM wa_meaning_sense WHERE parsed_meaning_id = ?", (old_id,))
        conn.execute("DELETE FROM wa_meaning_stem  WHERE parsed_meaning_id = ?", (old_id,))
        conn.execute("DELETE FROM wa_lsj_parsed   WHERE term_inv_id = ?", (term_inv_id,))
        conn.execute("DELETE FROM wa_meaning_parsed WHERE id = ?", (old_id,))

    parsed = parse_term(vocab)
    meta = parsed["meta"]
    now = _now()

    # Insert root record
    next_id = get_max_id(conn, "wa_meaning_parsed") + 1
    conn.execute(
        """INSERT INTO wa_meaning_parsed
               (id, term_inv_id, strongs_number, language,
                top_sense_count, stem_count, has_causative_stem, has_domain_tags,
                parsed_at, parse_version, parse_warnings)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            next_id, term_inv_id, strongs, language,
            meta["top_sense_count"], meta["stem_count"],
            meta["has_causative_stem"], meta["has_domain_tags"],
            now, PARSER_VERSION, meta["parse_warnings"],
        ),
    )

    # Insert sense nodes
    for node in parsed["sense_nodes"]:
        conn.execute(
            """INSERT INTO wa_meaning_sense
                   (parsed_meaning_id, level_code, level_depth, parent_level_code,
                    sense_text, is_stem_label, stem_label, domain_tag, sort_order)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                next_id, node["level_code"], node["level_depth"],
                node["parent_level_code"], node["sense_text"],
                node["is_stem_label"], node["stem_label"],
                node["domain_tag"], node["sort_order"],
            ),
        )

    # Insert stem nodes
    for stem in parsed["stem_nodes"]:
        conn.execute(
            """INSERT INTO wa_meaning_stem
                   (parsed_meaning_id, stem_name, stem_type, sense_count, top_sense_text)
               VALUES (?, ?, ?, ?, ?)""",
            (next_id, stem["stem_name"], stem["stem_type"],
             stem["sense_count"], stem["top_sense_text"]),
        )

    # Insert LSJ record (Greek only)
    if parsed["lsj_fields"]:
        f = parsed["lsj_fields"]
        conn.execute(
            """INSERT INTO wa_lsj_parsed
                   (term_inv_id, raw_lsj, lsj_gloss, lsj_domains,
                    lsj_philosophical_note, lsj_etymology_note, lsj_cognate_forms,
                    parsed_at, parse_version)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                term_inv_id,
                vocab.get("lsj_entry", ""),
                f.get("lsj_gloss"), f.get("lsj_domains"),
                f.get("lsj_philosophical_note"), f.get("lsj_etymology_note"),
                f.get("lsj_cognate_forms"),
                now, PARSER_VERSION,
            ),
        )

    # Update FK on wa_term_inventory
    conn.execute(
        "UPDATE wa_term_inventory SET parsed_meaning_id = ? WHERE id = ?",
        (next_id, term_inv_id),
    )

    return next_id


def run_parser_for_file(conn, file_id: int, vocab_map: dict[str, dict]) -> dict:
    """Run the parser for all terms belonging to file_id.

    Args:
        vocab_map: {strongs_number → vocab dict from step_client}

    Returns: {"parsed": int, "errors": list[str]}
    """
    terms = conn.execute(
        "SELECT id, strongs_number, term_id FROM wa_term_inventory WHERE file_id = ?",
        (file_id,),
    ).fetchall()

    parsed_count = 0
    errors = []
    for term in terms:
        strongs = term["strongs_number"] or term["term_id"]
        vocab = vocab_map.get(strongs)
        if not vocab:
            errors.append(f"No vocab data for {strongs} — skipping parse")
            continue
        try:
            run_parser(conn, term["id"], vocab)
            parsed_count += 1
        except Exception as exc:
            errors.append(f"Parser error for {strongs}: {exc}")

    conn.commit()
    return {"parsed": parsed_count, "errors": errors}
