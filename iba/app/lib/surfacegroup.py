"""surfacegroup -- module 1 of 5 of the surface cycle, the group corrections (escalation #2361, stage 2).

The judge (Surface-Judge) puts every surface in one of four groups. A word of collection a (behaviour or inner_being_state) can have a base that
the judge put in 'being' or 'other' (the base was judged alone, without the sense its derived words show). The recorded repoint of 2026-11-04
(#2359, 56 changes, 52 held pairs) corrected such bases from their derived words. This module is that rule, as a function of the tables:

  a pair is a surface of collection a whose base the structure finds OUTSIDE collection a (the structure result base_outside_input of
  lib/surfacestructure.py, which carries the base's group); the pairs of one base are read together:
    - every pair must be an inflection (cfg_base_construct.result_kind in setting group.repoint_apply_kinds) and the derived words must be
      in one group: otherwise the base is HELD (a flag held_pair for the researcher), never changed;
    - a base already carrying a held_pair flag (a human reading of an earlier run) is left to that reading;
    - a base in a group of setting group.repoint_auto_base_groups is repointed to the group of its derived words (state corrected, a surface_event
      correct with the derived words as the reason);
    - a base in another group (being) is PROPOSED: a flag held_pair, and it is repointed only when the researcher names it (-Base).
  Everything is inferential until the researcher confirms it (B:4). The rules are cfg_setting rows (module group); no code default.
"""
from __future__ import annotations

import datetime
import re

from . import surfacestructure as ss

SETTING_KEYS = ["group.repoint_apply_kinds", "group.repoint_auto_base_groups"]
PAIR = re.compile(r"(.+?) \((\S+?), (.*)\)$")


class GroupError(Exception):
    """A setting is missing or an input is unusable: routed as 'refused', nothing written."""


def read_settings(cfg) -> dict:
    vals = {k: cfg.setting(k) for k in SETTING_KEYS}
    missing = [k for k, v in vals.items() if v is None]
    if missing:
        raise GroupError(f"cfg_setting missing: {missing}")
    return vals


def pairs_from(result: dict, constructs: list[dict]) -> dict:
    """{base: [(derived, derived_group, construct, result_kind, base_group)]} from the structure result."""
    rk = {c["id"]: c["result_kind"] for c in constructs}
    out: dict = {}
    for r in result["surfaces"]:
        for e in r["base_outside_input"]:
            m = PAIR.match(e)
            out.setdefault(m.group(1), []).append((r["surface"], r["group"], m.group(2), rk.get(m.group(2)), m.group(3)))
    return out


def propose(pairs: dict, flagged: dict, vals: dict) -> dict:
    """Pure: {'apply': {base: (new_group, base_group, [pairs])}, 'review': {base: ...}, 'held': {base: (reason, [pairs])}, 'skipped': [bases]}.
    flagged is {base: text of its open or settled held_pair flags}. The INFLECTION pairs of a base decide its group; a pair of another kind
    never changes a group and is held (a flag) unless a flag already names its derived word; a base whose inflection pairs a flag already names
    is left to that reading (skipped). review and held are written as held_pair flags; apply is written as a correction."""
    out = {"apply": {}, "review": {}, "held": {}, "skipped": []}
    kinds_ok = set(vals["group.repoint_apply_kinds"])
    for base, ps in sorted(pairs.items()):
        notes = flagged.get(base, "")
        ips = [p for p in ps if p[3] in kinds_ok]
        nps = [p for p in ps if p[3] not in kinds_ok and f"{p[0]} (" not in notes]
        bg = ps[0][4]
        held_reason = []
        held_pairs = list(nps)
        if nps:
            held_reason.append("the change is not an inflection (" + ", ".join(sorted({p[3] or "?" for p in nps})) + "): the word class or form may differ")
        if ips and any(f"{p[0]} (" in notes for p in ips):
            out["skipped"].append(base)
        elif ips:
            groups = {p[1] for p in ips}
            if len(groups) > 1:
                held_reason.append("the derived words of this base are in different groups (" + ", ".join(sorted(groups)) + ")")
                held_pairs += ips
            elif bg in vals["group.repoint_auto_base_groups"]:
                out["apply"][base] = (next(iter(groups)), bg, ips)
            else:
                out["review"][base] = (next(iter(groups)), bg, ips)
        if held_reason:
            out["held"][base] = ("; ".join(held_reason), held_pairs)
    return out


def _because(ps) -> str:
    return "; ".join(f"{p[0]} ({p[1]}) [{p[2]}]" for p in sorted(ps))


def load(conn, cfg):
    """(structure result, constructs, pairs, flagged bases) from the tables."""
    vals = ss.read_settings(cfg)
    surfaces, cons, outside = ss.load_inputs(conn, cfg)
    res = ss.analyse(surfaces, cons, outside, vals)
    flagged: dict = {}
    for sf, note in conn.execute("SELECT t.surface, f.note FROM surface_flag f JOIN surface_term t ON t.id=f.subject_id "
                                 "WHERE f.subject_kind='surface_term' AND f.kind='held_pair' AND f.deleted=0"):
        flagged[sf] = flagged.get(sf, "") + " " + (note or "")
    return res, cons, pairs_from(res, cons), flagged


def write(conn, run_id: str, plan: dict, named: set) -> dict:
    """Apply: corrections for 'apply' and for the 'review' bases the researcher named; held_pair flags for the rest. One transaction by the caller."""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tid = {r[0]: r[1] for r in conn.execute("SELECT surface, id FROM surface_term WHERE deleted=0")}
    done = {"corrected": 0, "flagged": 0}
    todo = {b: v for b, v in plan["apply"].items()}
    todo.update({b: v for b, v in plan["review"].items() if b in named})
    for base, (new, bg, ps) in todo.items():
        why = (f"inflection of an (a) word; base judged {bg}; group taken from the derived words, which agree; because of: {_because(ps)}")
        by = "researcher named it" if base in named else "rule group.repoint"
        conn.execute("UPDATE surface_term SET surface_group=?, group_state='corrected', group_reason=?, updated_at=?, run_id=? WHERE id=?",
                     (new, why, now, run_id, tid[base]))
        conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                     "VALUES ('surface_term',?,'correct','surface_group',?,?,'surface-group',?,?,'surface-group')",
                     (tid[base], bg, new, f"{by}; {why}", run_id))
        done["corrected"] += 1
    to_flag = [(b, ps[0][4], reason, ps) for b, (reason, ps) in plan["held"].items()]
    to_flag += [(b, bg, f"base judged {bg}: a group change needs the researcher's reading of the sense (name it with -Base)", ps)
                for b, (new, bg, ps) in plan["review"].items() if b not in named]
    for base, bg, reason, ps in to_flag:
        note = f"base word held in group {bg}; derived words not applied: {_because(ps)}; {reason}"
        conn.execute("INSERT INTO surface_flag (subject_kind, subject_id, kind, note, status, run_id, created_by) VALUES ('surface_term',?,'held_pair',?, 'open', ?, 'surface-group')",
                     (tid[base], note, run_id))
        done["flagged"] += 1
    return done
