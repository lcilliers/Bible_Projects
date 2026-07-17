"""stepapi.py — the three STEP calls the raw run makes.

Reads its connection and routes from `config/step.json`. Nothing hard-coded here
except the parse of the interlinear HTML (which is a fact about STEP's output, not
a choice) and the forward-walk over the 60-cap.

    call1_meanings(word)   -> the seed strongs + verses
    call2_getInfo(strong)  -> the strong's detail (the meaning)
    call3_strong(strong)   -> the strong's verses, each preview a full interlinear
    parse_spans(preview)   -> the verse decomposed into one row per CODE (O3)

Read-only against STEP. `up()` is the pre-flight: reachable AND tagged.
"""

from __future__ import annotations

import json
import pathlib
import re

import requests

CFG = json.loads((pathlib.Path(__file__).resolve().parent.parent / "config" / "step.json").read_text(encoding="utf-8"))
CONN = CFG["connection"]
BASE = CONN["base_url"].rstrip("/")
VERSION = CONN["version"]
TIMEOUT = int(CONN["timeout_seconds"])
CAP = int(CFG["cap"])

# one span per CODE: capture morph, strong, surface for each <span>
SPAN_RE = re.compile(r"<span[^>]*\bmorph='([^']*)'[^>]*\bstrong='([^']*)'[^>]*>([^<]*)</span>")
PARTICLE_RE = re.compile(r"^[HG]9\d{3}$")

# Canonical OSIS book order — REQUIRED for the forward-walk. The frontier must be
# the canonically-last verse of a page, and book order is NOT alphabetical
# ("Gen" precedes "Exod"). A string sort silently mis-walked and under-returned
# G5485 by 39 verses in testing.
_OSIS_ORDER = [
    "Gen", "Exod", "Lev", "Num", "Deut", "Josh", "Judg", "Ruth",
    "1Sam", "2Sam", "1Kgs", "2Kgs", "1Chr", "2Chr", "Ezra", "Neh", "Esth",
    "Job", "Ps", "Prov", "Eccl", "Song",
    "Isa", "Jer", "Lam", "Ezek", "Dan", "Hos", "Joel", "Amos", "Obad",
    "Jonah", "Mic", "Nah", "Hab", "Zeph", "Hag", "Zech", "Mal",
    "Matt", "Mark", "Luke", "John", "Acts",
    "Rom", "1Cor", "2Cor", "Gal", "Eph", "Phil", "Col",
    "1Thess", "2Thess", "1Tim", "2Tim", "Titus", "Phlm",
    "Heb", "Jas", "1Pet", "2Pet", "1John", "2John", "3John", "Jude", "Rev",
]
_OSIS_IDX = {b: i for i, b in enumerate(_OSIS_ORDER)}


class StepUnavailable(RuntimeError):
    pass


def _get(path: str) -> dict:
    r = requests.get(f"{BASE}/{path.lstrip('/')}", timeout=TIMEOUT)
    r.raise_for_status()
    d = r.json()
    if "errorMessage" in d:
        raise RuntimeError(f"STEP error for {path!r}: {d['errorMessage']}")
    return d


def up() -> None:
    """Pre-flight: STEP reachable AND answering with the tagged module.

    Resolves the probe code first (a base code answers a Strong's search with 0),
    then checks it returns verses — an untagged module returns 0 with no error.
    """
    try:
        d = _get(CFG["apis"]["call2_getInfo"]["route"].format(version=VERSION, strong="H0430"))
    except requests.RequestException as e:
        raise StepUnavailable(f"STEP not reachable at {BASE} ({type(e).__name__}). Start the local server.") from e
    vocabs = d.get("vocabInfos") or []
    if not vocabs or not vocabs[0].get("stepGloss"):
        raise StepUnavailable(f"STEP up but no lexicon for the probe under {VERSION!r} — version not present.")
    resolved = vocabs[0].get("strongNumber", "H0430")
    total = _get(CFG["apis"]["call3_strong"]["route"].format(version=VERSION, strong=resolved)).get("total", 0)
    if total < 1:
        raise StepUnavailable(f"STEP up but the module is NOT TAGGED — a Strong's search returned {total}.")


def call1_meanings(word: str) -> dict:
    return _get(CFG["apis"]["call1_meanings"]["route"].format(version=VERSION, word=word))


def call2_getInfo(strong: str) -> dict:
    return _get(CFG["apis"]["call2_getInfo"]["route"].format(version=VERSION, strong=strong))


def _canon_key(osis: str) -> tuple:
    """(book_order, chapter, verse) — book by CANONICAL index, not its name."""
    parts = osis.split(".")
    book = _OSIS_IDX.get(parts[0], 999)
    ch = int(re.sub(r"\D.*", "", parts[1]) or 0) if len(parts) > 1 else 0
    vs = int(re.sub(r"\D.*", "", parts[2]) or 0) if len(parts) > 2 else 0
    return (book, ch, vs)


def call3_strong(strong: str) -> tuple[int, list[dict]]:
    """Return (reported_total, results). Forward-walks the 60-cap and self-validates."""
    route = CFG["apis"]["call3_strong"]["route"]
    first = _get(route.format(version=VERSION, strong=strong))
    total = first.get("total", 0)
    if total == 0:
        return 0, []
    if total <= CAP:
        return total, first.get("results", [])
    # forward-walk
    seen: dict[str, dict] = {}
    start, end = "Gen.1.1", "Rev.22.21"
    for _ in range(400):
        d = _get(route.format(version=VERSION, strong=strong) + f"|reference={start}-{end}")
        rows = d.get("results", [])
        if not rows:
            break
        for it in rows:
            oid = it.get("osisId") or it.get("key", "")
            if oid and oid not in seen:
                seen[oid] = it
        if d.get("total", 0) <= len(rows):
            break
        frontier = max(rows, key=lambda it: _canon_key(it.get("osisId") or it.get("key", "")))
        nxt = (frontier.get("osisId") or "").split("!")[0]
        if not nxt or nxt == start:
            break
        start = nxt
    return total, list(seen.values())


def strip_html(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def parse_spans(preview: str) -> list[dict]:
    """Decompose a verse preview into ONE ROW PER CODE (O3).

    A surface word maps to N codes ('earth' -> H0776G H9002 H9009). Each code is a
    row at its own running position; the surface repeats; particles fall out as
    their own rows.
    """
    out: list[dict] = []
    pos = 0
    for morph_list, strong_list, surface in SPAN_RE.findall(preview):
        strongs = strong_list.split()
        morphs = morph_list.split()
        for i, code in enumerate(strongs):
            out.append({
                "position": pos,
                "surface": surface.strip(),
                "strong_variant": code,
                "morph_code": morphs[i] if i < len(morphs) else None,
                "is_particle": 1 if PARTICLE_RE.match(code) else 0,
            })
            pos += 1
    return out
