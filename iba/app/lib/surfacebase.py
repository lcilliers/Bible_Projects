"""surfacebase.py -- the base form of a surface word, asked of the Ollama server (escalation #2359, researcher
2026-11-04: "ask Ollama to determine the base form of the remaining words ... the rule of similar root meaning must
be maintained").

The list is a JSON file of English words beside the batch file (<surface_judge.batch_dir>/<Batch><suffix>, the suffix
is cfg_setting surface_judge.base_input_suffix): {"words": [...]}. Each word is put to the server on its own, with no
verse, no Hebrew or Greek code and no neighbouring word. The model answers a base word and the relation of the word
to it (one of cfg_setting surface_judge.base_relations: inflection, derivation, none); `none` means the word has no
base of the same root meaning. The answers are appended to a batch file, one JSON line per word, as each finishes;
nothing here writes the database. Every answer is inferential (B:4) until the researcher confirms it.

Server, checks, ssh tunnel and call are those of lib/surfacejudge.py (cfg_setting modules `ollama` and
`surface_judge`); the question, the relations and the shape of a usable base are cfg_setting rows too.
"""
from __future__ import annotations

import json
import pathlib
import re
import time

from . import surfacejudge as sj
from .cfg import Cfg

BaseError = sj.JudgeError


def settings(cfg: Cfg) -> dict:
    """The server and limits (surfacejudge.settings) plus the base-form question, relations and base pattern."""
    vals = sj.settings(cfg)
    keys = ["surface_judge.base_prompt", "surface_judge.base_relations", "surface_judge.base_form_pattern",
            "surface_judge.base_input_suffix"]
    got = {k.split(".", 1)[1]: cfg.setting(k) for k in keys}
    missing = [k for k, v in zip(keys, got.values()) if v is None]
    if missing:
        raise BaseError(f"cfg_setting missing: {missing}")
    if "{surface}" not in got["base_prompt"]:
        raise BaseError("cfg_setting surface_judge.base_prompt has no {surface} place")
    if not isinstance(got["base_relations"], list) or "none" not in got["base_relations"]:
        raise BaseError("cfg_setting surface_judge.base_relations is a JSON list of the relations, including none")
    try:
        re.compile(got["base_form_pattern"])
    except re.error as exc:
        raise BaseError(f"cfg_setting surface_judge.base_form_pattern is not a regular expression: {exc}") from None
    vals.update(got)
    return vals


def input_words(vals: dict, out: pathlib.Path) -> list[str]:
    """The words to ask about, from the input file beside the batch file."""
    path = out.with_name(out.stem + vals["base_input_suffix"])
    if not path.exists():
        raise BaseError(f"the input list {path.as_posix()} does not exist (a JSON file {{\"words\": [...]}})")
    try:
        words = json.loads(path.read_text(encoding="utf-8"))["words"]
    except Exception as exc:
        raise BaseError(f"the input list {path.as_posix()} is not a JSON object with a list 'words': {exc}") from None
    if not isinstance(words, list) or not all(isinstance(w, str) and w.strip() for w in words):
        raise BaseError(f"the input list {path.as_posix()}: 'words' must be a list of non-empty strings")
    seen, out_words = set(), []
    for w in words:
        if w not in seen:
            seen.add(w)
            out_words.append(w)
    return out_words


def check_answer(ans: dict, word: str, vals: dict) -> list[str]:
    """Reasons the answer is not usable (empty list when it is). The rule of similar root meaning is in the
    question; here the shape is held: a known relation, and for inflection or derivation a base that is one
    word of the configured pattern and is not the word itself."""
    if not isinstance(ans, dict):
        return ["not an object"]
    rel = ans.get("relation")
    if rel not in vals["base_relations"]:
        return [f"relation {rel!r}"]
    base = ans.get("base")
    if rel == "none":
        if base not in (None, "", word):
            return [f"relation none but base {base!r} is not the word"]
        return []
    if not isinstance(base, str) or not re.fullmatch(vals["base_form_pattern"], base):
        return [f"base {base!r} does not match the pattern"]
    if base == word:
        return [f"relation {rel} but base is the word itself"]
    return []


def ask_word(vals: dict, word: str) -> dict:
    """One word, one call (one retry). A failed word is recorded with relation null and is tried again on the
    next run."""
    t0 = time.time()
    prompt = vals["base_prompt"].replace("{surface}", word)
    errors, ans, meta = [], None, {}
    for attempt in (1, 2):
        try:
            got, meta = sj.ask(vals, prompt)
        except Exception as exc:  # network, timeout or unparsable JSON
            errors.append(f"call failed: {exc}")
            continue
        bad = check_answer(got, word, vals)
        if not bad:
            ans = got
            break
        errors.append(f"attempt {attempt}: " + "; ".join(bad))
    rel = ans["relation"] if ans else None
    rec = {"surface": word, "relation": rel,
           "base": (ans.get("base") or word) if ans else None,
           "reason": (ans.get("reason") or None) if ans else None,
           "judged_by": vals["model"] if ans else None, "errors": errors, "secs": round(time.time() - t0, 1)}
    rec.update({k: v for k, v in meta.items() if v is not None})
    return rec


def run_words(vals: dict, words: list[str], out: pathlib.Path, limit: int | None = None, emit=None) -> dict:
    """Ask about each word once, appending one JSON line per word as it finishes (flushed). Resumable: a word
    already answered (relation not null) is skipped, a word that failed is tried again. `limit` is the most words
    asked in this run. The server is checked first (JudgeError, nothing written, when it does not answer); the run
    halts after surface_judge.max_consecutive_failures words in a row with no usable answer. Ctrl+C stops after the
    word in hand is written. The ssh tunnel (ollama.tunnel_local_port) is open for the whole run."""
    with sj.server_route(vals) as route:
        sj.preflight(route)
        done = {w for w, r in sj.read_batch(out).items() if r.get("relation")}
        out.parent.mkdir(parents=True, exist_ok=True)
        did = failed = streak = 0
        stopped = halted = False
        try:
            for w in words:
                if w in done:
                    continue
                if limit is not None and did + failed >= limit:
                    break
                rec = ask_word(route, w)
                with out.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    f.flush()
                if rec["relation"]:
                    did += 1
                    streak = 0
                else:
                    failed += 1
                    streak += 1
                if emit:
                    emit(f"{w!r}: {rec['relation']} {rec['base']!r} {rec['secs']} s"
                         + (f"  {rec['errors'][-1][:120]}" if not rec["relation"] else ""))
                if streak >= int(route["max_consecutive_failures"]):
                    halted = True
                    break
        except KeyboardInterrupt:
            stopped = True
    return {"asked": did, "failed": failed, "stopped": stopped, "halted": halted}


def status(vals: dict, words: list[str], out: pathlib.Path) -> dict:
    """How far a batch file has got against the input list: answered per relation, failed (tried, no usable
    answer) and left."""
    got = sj.read_batch(out)
    per = {r: 0 for r in vals["base_relations"]}
    failed = 0
    for w in words:
        r = got.get(w)
        if r is None:
            continue
        if r.get("relation") in per:
            per[r["relation"]] += 1
        else:
            failed += 1
    answered = sum(per.values())
    return {"list": len(words), "answered": answered, "per_relation": per, "failed": failed,
            "left": len(words) - answered - failed, "not_on_list": len(set(got) - set(words))}
