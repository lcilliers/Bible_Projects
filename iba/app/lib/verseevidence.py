"""verseevidence.py -- the evidence a reader needs on a verse, read from the tables (escalation #2528, moved from lib/reading.py so that the layered reading and the
narrative steps share one copy): what the meaning sources hold of the codes of the verses in hand, the verse in its passage, and the flags on an earlier observation of a verse.
Read-only. Nothing here decides; each function returns what the tables hold.
"""
from __future__ import annotations

import json

from . import observationrecord as orec


def _setting(cfg, key: str):
    v = cfg.required_setting(key)
    return json.loads(v) if isinstance(v, str) else v


def meaning(cfg, conn, testament_of: dict) -> dict:
    """{code: what the tables hold of its meaning} for the codes of the verses in hand (cfg_setting reading.sheet_meaning, #2329): the
    meaning tree rows, the sense head, the STEP gloss, the related words and, for the testaments named, the lexicon. By the exact code
    (a suffixed code is never read as its base), one set-based query per table (B:71). A source with nothing held reads as empty, so the
    reading names the gap and does not fill it from memory."""
    want = _setting(cfg, "reading.sheet_meaning")
    SJ = json.dumps(sorted(testament_of))
    out = {s: {} for s in testament_of}
    if want.get("tree"):
        for s in out:
            out[s]["tree"] = []
        for s, code, text in conn.execute("SELECT strong_variant, sense_code, sense_text FROM strong_meaning_tree WHERE deleted=0 AND "
                                          "strong_variant IN (SELECT value FROM json_each(?)) ORDER BY strong_variant, sort, id", (SJ,)):
            out[s]["tree"].append({"sense_code": code, "text": text})
    if want.get("sense"):
        for s in out:
            out[s]["sense"] = None
        for s, head in conn.execute("SELECT strong, head FROM strong_sense WHERE deleted=0 AND strong IN (SELECT value FROM json_each(?))",
                                    (SJ,)):
            out[s]["sense"] = head
    if want.get("step_gloss"):
        for s in out:
            out[s]["step_gloss"] = None
        for s, gloss in conn.execute("SELECT strongNumber, stepGloss FROM strong WHERE strongNumber IN (SELECT value FROM json_each(?))",
                                     (SJ,)):
            out[s]["step_gloss"] = gloss
    if want.get("related"):
        for s in out:
            out[s]["related"] = []
        for s, rs, form, tr, gloss in conn.execute(
                "SELECT strong, related_strong, related_form, related_transliteration, related_gloss FROM strong_related WHERE deleted=0 "
                "AND strong IN (SELECT value FROM json_each(?)) ORDER BY strong, id", (SJ,)):
            out[s]["related"].append({"strong": rs, "form": form, "transliteration": tr, "gloss": gloss})
    lex = want.get("lexicon")
    if lex:
        cols = lex["columns"]
        pick = [s for s, t in testament_of.items() if t in lex["testaments"]]
        for s in pick:
            out[s]["lexicon"] = {}
        for row in conn.execute(f"SELECT strong, {', '.join(cols)} FROM strong_lexicon WHERE deleted=0 AND strong IN "
                                "(SELECT value FROM json_each(?))", (json.dumps(pick),)):
            out[row[0]]["lexicon"] = dict(zip(cols, row[1:]))
    return out


def passage(conn, osis: str, window: int = 2) -> list[dict]:
    book, ch, v = osis.split(".")
    want = [f"{book}.{ch}.{n}" for n in range(max(1, int(v) - window), int(v) + window + 1)]
    rows = {r[0]: r for r in conn.execute("SELECT osisId, reference, text FROM verse WHERE deleted=0 AND osisId IN "
                                          f"({','.join('?' * len(want))})", want)}
    return [{"verse": rows[o][1], "text": rows[o][2]} for o in want if o in rows]


def existing_flags(cfg, o, node_roles: list, dups: dict) -> list[dict]:
    """The flags on an earlier observation `o` (an ib_observation row) of a verse, with a proposed fix where there is one: a description live more than once, a kind the rules
    do not use, a tag that is not a kind, parts that are not one of the items of reading.observation_items, and an observation whose nodes all bear on an act.
    `node_roles` are the roles of its live nodes on the verse; `dups` is {trimmed text: [ids]} of the descriptions live more than once among the observations in hand."""
    out = []
    rl_ = orec.rules(cfg)
    kinds = orec.kinds(cfg)
    groups = orec.node_role_groups(cfg)
    same = dups.get((o["obs_text"] or "").strip())
    if same:
        keep = same[0]
        if o["id"] != keep:
            out.append({"code": "duplicate_description", "text": f"the same description is live as observation {keep} (all copies: {same})",
                        "propose": {"action": "merge", "into": keep, "reason": f"duplicate of observation {keep} (the same description), merged when the verse was worked (#2323)"}})
        else:
            out.append({"code": "duplicate_description", "propose": None, "text": f"other live copies of this description: {same[1:]}; each is merged into this one"})
    if o["tag"] in rl_["unused_kinds"]:
        out.append({"code": "unused_kind", "text": f"the kind {o['tag']!r} is not used (reading.observation_rules unused_kinds): a surface with no inner-being role is not recorded",
                    "propose": {"action": "delete", "reason": f"the kind {o['tag']} is not used: a surface with no inner-being role is not recorded (spec 4.1; #2323)"}})
    elif o["tag"] not in kinds:
        out.append({"code": "kind_not_in_parts", "propose": None,
                    "text": f"the tag {o['tag']!r} is not a kind of observation ({[k for k in kinds if k != 'silence']}): read what it says and modify the tag, or delete the observation"})
    if any(r in groups["relevant"] for r in node_roles):
        perr: list = []
        orec.check_item_parts(cfg, json.loads(o["parts"]) if o["parts"] else None, o["tag"], o["basis"], o["route"], "", perr)
        if perr:
            out.append({"code": "parts_not_an_item", "propose": None,
                        "text": "it covers a relevant surface but is not one of the items of reading.observation_items (modify `parts`, `tag` or `basis`, or delete it): "
                                + "; ".join(x.lstrip(": ") for x in perr)})
    if node_roles and all(r in groups["bears_on"] for r in node_roles):
        out.append({"code": "bears_on_only", "propose": None,
                    "text": "every node it holds bears on an act (object, relational target, enactment): those words are nodes of the observation of the act: move them there "
                            "(node modify `observation_id`) and delete this one, or give it its characteristic or qualifier node"})
    return out
