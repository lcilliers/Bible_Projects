"""surfacejudge.py -- the verdict on every (Strong's code, English surface) pair of the corpus (escalation #2354, plan v5).

One judgement per distinct surface string, not per occurrence. A pair is one of three kinds, read from verse_lexical
(multi-code spans carry the span's English on every code, BUILD 428, working log finding 28):
  particle     the code is H9xxx: settled by a rule on the code (qualifier, with a use), no model call
  own          the code has an occurrence in a span with a single non-particle code: the surface is the code's own
  span_shared  the code occurs only in spans with 2+ non-particle codes: the surface is the unit's English
The model call (Ollama, settings in cfg_setting module `ollama`) judges the own and span_shared pairs of one surface
string; the answers are written to a batch file first (settings surface_judge.batch_dir) -- nothing here writes the
database. Every verdict is inferential (B:4) until the researcher confirms it.
"""
from __future__ import annotations

import json
import pathlib
import re
import time
import urllib.request

from .cfg import Cfg

PARTICLE_GLOB = "H9[0-9][0-9][0-9]"
# use of each particle code, read from its STEP gloss (strong.stepGloss); one small table, reviewed once
PARTICLE_USE = {
    "H9002": "conjunction", "H9003": "preposition", "H9004": "preposition", "H9005": "preposition",
    "H9006": "preposition", "H9007": "conjunction", "H9008": "particle", "H9009": "article", "H9010": "article",
    "H9011": "particle", "H9012": "particle", "H9013": "particle", "H9014": "other",
}  # H9020 to H9049 are pronouns (possessive and personal)

PROMPT = """You classify one English word or phrase as it appears in the ESV Bible, for a study of how Scripture describes the human inner being.
English: "{surface}"
It translates these Hebrew/Greek words (code: dictionary gloss; kind):
{codes}

For EACH code, give the group of this English as it translates that code:
- behaviour: something a person does or undergoes, inwardly or outwardly (an act, feeling, thought, speech, choice)
- inner_being_state: a standing condition or characteristic of a person's inner being (righteous, wicked, wise, proud)
- being: an entity: a person, God, a spirit, an angel, or a part of a person such as the heart or the soul
- qualifier: describes, locates or links something and is not itself a behaviour, state or being. This includes pronouns (who they name is settled when the verse is read), prepositions, adverbs, conjunctions, articles, numerals and degree words. For a qualifier give the use: {uses}.
- not_allocated: you cannot tell, or the English does not render this code
Kind "own": the English is this code's own rendering. Kind "span_shared": the English renders a unit of several words, so judge the English as the unit, and use the code's gloss only as a hint.
Answer JSON only, one entry per code in the order given:
{{"pairs":[{{"code":"H0000","group":"...","use":null,"reason":null}}]}}
"use" only for qualifier (else null). "reason" only for qualifier and not_allocated, under 12 words (else null)."""


class JudgeError(Exception):
    pass


def particle_use(strong: str) -> str:
    if strong in PARTICLE_USE:
        return PARTICLE_USE[strong]
    if re.fullmatch(r"H90[2-4]\d", strong):
        return "pronoun"
    return "other"


def prepare(conn) -> None:
    """Temp table of live spans with the count of non-particle codes (once per connection)."""
    conn.execute("DROP TABLE IF EXISTS temp.np_count")
    conn.execute(f"CREATE TEMP TABLE np_count AS SELECT span_id, COUNT(*) k FROM verse_lexical "
                 f"WHERE deleted=0 AND NOT strong GLOB '{PARTICLE_GLOB}' GROUP BY span_id")
    conn.execute("CREATE INDEX temp.ix_np_count ON np_count(span_id)")


def pairs_of(conn, surface: str) -> list[dict]:
    """The distinct codes of a surface string (lower-cased), with kind, occurrences and gloss. prepare() first."""
    out = []
    for strong, occ, one in conn.execute(
            f"SELECT v.strong, COUNT(*), SUM(COALESCE(n.k, 0) = 1) FROM verse_lexical v "
            f"LEFT JOIN temp.np_count n ON n.span_id = v.span_id "
            f"WHERE v.deleted=0 AND lower(v.surface)=? GROUP BY v.strong ORDER BY COUNT(*) DESC, v.strong",
            (surface,)):
        kind = "particle" if re.fullmatch(r"H9\d{3}", strong) else ("own" if one else "span_shared")
        g = conn.execute("SELECT stepGloss FROM strong WHERE strongNumber=? AND deleted=0", (strong,)).fetchone()
        out.append({"strong": strong, "kind": kind, "occ": occ, "gloss": (g[0] if g and g[0] else "") or "(no gloss)"})
    return out


def settings(cfg: Cfg) -> dict:
    keys = ["host", "model", "timeout_seconds", "keep_alive", "num_ctx", "temperature", "max_codes_per_call"]
    got = {k: cfg.setting(f"ollama.{k}") for k in keys}
    missing = [k for k, v in got.items() if v is None]
    if missing:
        raise JudgeError(f"cfg_setting ollama.* missing: {missing}")
    return got


def ask(cfg_vals: dict, prompt: str) -> tuple[dict, dict]:
    body = {"model": cfg_vals["model"], "stream": False, "think": False, "format": "json",
            "keep_alive": cfg_vals["keep_alive"],
            "options": {"temperature": cfg_vals["temperature"], "num_ctx": cfg_vals["num_ctx"]},
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(cfg_vals["host"] + "/api/chat", json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=cfg_vals["timeout_seconds"]) as r:
        resp = json.loads(r.read())
    return json.loads(resp["message"]["content"]), {
        "out_tokens": resp.get("eval_count"), "prompt_tokens": resp.get("prompt_eval_count"),
        "tok_s": round(resp["eval_count"] / (resp["eval_duration"] / 1e9), 1) if resp.get("eval_duration") else None}


def check_answer(ans: dict, sent: list[dict], groups: list[str], uses: list[str]) -> list[str]:
    """Reasons the answer is not usable (empty list when it is)."""
    bad = []
    got = ans.get("pairs") if isinstance(ans, dict) else None
    if not isinstance(got, list):
        return ["no 'pairs' list"]
    by = {p.get("code"): p for p in got if isinstance(p, dict)}
    for s in sent:
        p = by.get(s["strong"])
        if p is None:
            bad.append(f"{s['strong']} missing")
            continue
        if p.get("group") not in groups:
            bad.append(f"{s['strong']} group {p.get('group')!r}")
        elif p["group"] == "qualifier" and p.get("use") not in uses:
            bad.append(f"{s['strong']} qualifier use {p.get('use')!r}")
        elif p["group"] != "qualifier" and p.get("use") not in (None, "", "null"):
            bad.append(f"{s['strong']} use given for {p['group']}")
    return bad


def judge_surface(cfg: Cfg, conn, surface: str, vals: dict, groups: list[str], uses: list[str]) -> dict:
    """One surface string: the rule on its particle codes, the model on the others (up to max_codes_per_call a call)."""
    t0 = time.time()
    pairs = pairs_of(conn, surface)
    rows, calls, errors = [], [], []
    for p in pairs:
        if p["kind"] == "particle":
            rows.append({"strong": p["strong"], "kind": "particle", "occ": p["occ"], "group": "qualifier",
                         "use": particle_use(p["strong"]), "reason": None, "judged_by": "rule:particle_code"})
    model_pairs = [p for p in pairs if p["kind"] != "particle"]
    step = int(vals["max_codes_per_call"])
    for i in range(0, len(model_pairs), step):
        chunk = model_pairs[i:i + step]
        codes = "\n".join(f"{p['strong']}: {p['gloss']}; {p['kind']}" for p in chunk)
        prompt = PROMPT.format(surface=surface, codes=codes, uses=", ".join(uses))
        ans, meta = None, {}
        for attempt in (1, 2):
            try:
                ans, meta = ask(vals, prompt)
            except Exception as exc:  # network, timeout or unparsable JSON
                errors.append(f"call failed: {exc}")
                ans = None
                continue
            bad = check_answer(ans, chunk, groups, uses)
            if not bad:
                break
            errors.append(f"attempt {attempt}: " + "; ".join(bad))
            ans = None
        calls.append(meta)
        by = {p["code"]: p for p in (ans or {}).get("pairs", [])} if ans else {}
        for p in chunk:
            a = by.get(p["strong"])
            rows.append({"strong": p["strong"], "kind": p["kind"], "occ": p["occ"],
                         "group": a["group"] if a else None, "use": (a.get("use") or None) if a else None,
                         "reason": (a.get("reason") or None) if a else None,
                         "judged_by": vals["model"] if a else None})
    return {"surface": surface, "rows": rows, "calls": calls, "errors": errors, "secs": round(time.time() - t0, 1)}


def run(cfg: Cfg, conn, surfaces: list[str], out: pathlib.Path) -> None:
    """Judge the surfaces not yet in the batch file (resumable); one JSON line per surface."""
    vals = settings(cfg)
    groups, uses = cfg.enum("surface_pair_verdict.surface_group"), cfg.enum("surface_pair_verdict.use")
    prepare(conn)
    done = set()
    if out.exists():
        done = {json.loads(line)["surface"] for line in out.read_text(encoding="utf-8").splitlines() if line}
    out.parent.mkdir(parents=True, exist_ok=True)
    for s in surfaces:
        if s in done:
            continue
        rec = judge_surface(cfg, conn, s, vals, groups, uses)
        with out.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"{s!r}: {len(rec['rows'])} pairs, {rec['secs']} s, errors {len(rec['errors'])}", flush=True)


# ---- surface-only judging (researcher, 2026-11-02: take the list of surfaces and apply the test to it) ----------
WORD_PROMPT = """You classify one English word or phrase as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Give the group of this English as it is used in the Bible:
- behaviour: something a person does or undergoes, inwardly or outwardly (an act, feeling, thought, speech, choice)
- inner_being_state: a standing condition or characteristic of a person's inner being (righteous, wicked, wise, proud)
- being: an entity: a person, God, a spirit, an angel, or a part of a person such as the heart or the soul
- qualifier: describes, locates or links something and is not itself a behaviour, state or being. This includes pronouns (who they name is settled when the verse is read), prepositions, adverbs, conjunctions, articles, numerals and degree words. For a qualifier give the use: {uses}.
- not_allocated: you cannot tell
Judge the English as it reads, by what kind of word it is and what it says. "also" gives a second group only if the English is commonly used in a second, different way (for example "long" as a time word and "long" as a desire).
Answer JSON only: {{"group":"...","use":null,"also":null,"reason":null}}
"use" only for qualifier (else null). "also" is another group from the list or null. "reason" only for qualifier and not_allocated, under 10 words (else null)."""


def check_word(ans: dict, groups: list[str], uses: list[str]) -> list[str]:
    if not isinstance(ans, dict):
        return ["not an object"]
    bad = []
    if ans.get("group") not in groups:
        bad.append(f"group {ans.get('group')!r}")
    elif ans["group"] == "qualifier" and ans.get("use") not in uses:
        bad.append(f"qualifier use {ans.get('use')!r}")
    if ans.get("also") not in (None, "", "null") and ans.get("also") not in groups:
        bad.append(f"also {ans.get('also')!r}")
    return bad


def judge_word(vals: dict, surface: str, groups: list[str], uses: list[str]) -> dict:
    """One surface string, one call (one retry). A failed word is recorded with group null and is retried on the next run."""
    t0 = time.time()
    prompt = WORD_PROMPT.format(surface=surface, uses=", ".join(uses))
    errors, ans, meta = [], None, {}
    for attempt in (1, 2):
        try:
            got, meta = ask(vals, prompt)
        except Exception as exc:  # network, timeout or unparsable JSON
            errors.append(f"call failed: {exc}")
            continue
        bad = check_word(got, groups, uses)
        if not bad:
            ans = got
            break
        errors.append(f"attempt {attempt}: " + "; ".join(bad))
    rec = {"surface": surface, "group": ans["group"] if ans else None,
           "use": (ans.get("use") or None) if ans else None,
           "also": (ans.get("also") if ans and ans.get("also") not in ("", "null") else None) if ans else None,
           "reason": (ans.get("reason") or None) if ans else None,
           "judged_by": vals["model"] if ans else None, "errors": errors, "secs": round(time.time() - t0, 1)}
    rec.update({k: v for k, v in meta.items() if v is not None})
    return rec


def surface_list(conn, limit: int | None = None) -> list[tuple[str, int]]:
    """Every distinct live surface string of verse_lexical, lower-cased, most frequent first, with its occurrences."""
    sql = ("SELECT lower(surface), COUNT(*) FROM verse_lexical WHERE deleted=0 AND surface IS NOT NULL "
           "AND trim(surface)<>'' GROUP BY 1 ORDER BY 2 DESC, 1")
    return conn.execute(sql + (f" LIMIT {int(limit)}" if limit else "")).fetchall()


def run_words(cfg: Cfg, surfaces: list[str], out: pathlib.Path) -> None:
    """Judge each surface once. Appends one JSON line per word as it finishes (flushed); resumable: words already
    judged (group not null) are skipped, words that failed are tried again."""
    vals = settings(cfg)
    groups, uses = cfg.enum("surface_pair_verdict.surface_group"), cfg.enum("surface_pair_verdict.use")
    done = set()
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            if line:
                r = json.loads(line)
                if r.get("group"):
                    done.add(r["surface"])
    out.parent.mkdir(parents=True, exist_ok=True)
    for s in surfaces:
        if s in done:
            continue
        rec = judge_word(vals, s, groups, uses)
        with out.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
        print(f"{s!r}: {rec['group']} {rec['use'] or ''} {rec['secs']} s", flush=True)
