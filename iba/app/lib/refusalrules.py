"""refusalrules -- escalation #2637, plan v3 X4 (outputs/escalation/2637-build-plan-v3-20261126.md): every refusal of the analytic reading
package keyed to a configured rule, and printed in the packet of each read that can meet it.

The registry is cfg_setting layer.refusals (module layer):
  scan     the source the refusal sites are read from: `modules` (lib modules), `sinks` (the list names a check appends its problems to) and
           `exceptions` (the endings of the exception classes a refusal is raised with)
  entries  [{key, match, reads, site?}]: a refusal line that holds `match` is a refusal under the rule `key` (cfg_method_rule rule_key prefix, or
           B:<id> for a cfg_behaviour_rule). The first entry that matches wins; `site` ("module.function") narrows an entry to the sites of that
           function. `reads` are the reads (cfg_setting layer.read_types) whose commands can meet it.
  exempt   [{site, reason}]: functions of the scanned modules that are not on the reading path.
Each read's packet prints its refusals (readcommands.instruction: for_read), and the rule of each key is among the read's `rules`, so its text is
printed too. A refused command's message is annotated line by line with the key ([RW-03] ...) before it is shown and kept in read_failure
(handlers/collectionbuild._logged). The static test (iba/app/tools/temp_2637_refusal_keys_test_run.py) holds the registry to the source: every
site keyed, every key an active rule printed by each read of its entry, no entry that keys no site.

A site is an append to a sink, or a raise of a refusal exception, whose message has literal text. A site that ends by passing on the message of an
exception it caught, or the joined lines of a check (a wrapper: `{where}: {exc}`), need not be keyed: the raise of that exception, or the
lines, are. An entry may still key a wrapper's own words (`cannot read {file}: {exc}`).
"""
from __future__ import annotations

import ast
import json
import pathlib

SETTING = "layer.refusals"
_WRAPPED = {"exc", "why", "fail"}      # a message that ends with one of these passes on a caught exception or a check's own text


def load(conn) -> dict:
    """The registry from cfg_setting layer.refusals; an empty one where the setting is absent (a database the migration has not reached)."""
    r = conn.execute("SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (SETTING,)).fetchone()
    if r is None or not r[0]:
        return {"scan": {}, "entries": [], "exempt": []}
    return json.loads(r[0]) if isinstance(r[0], str) else r[0]


def key_of(reg: dict, text: str, site: str | None = None) -> str | None:
    """The rule key of one refusal line: the first entry whose `match` the line holds (and, where the entry names a site and the site is known,
    the same site; an entry narrowed to a site keys nothing where the site is not known, as on a refused command's message). None where no
    entry matches."""
    for e in reg.get("entries", []):
        if e.get("site") and e["site"] != site:
            continue
        if e["match"] in text:
            return e["key"]
    return None


def annotate(conn, message: str) -> str:
    """The message of a refused command with the rule key put before each line an entry matches ("  [RW-03] row 2: the same text as ...").
    A line already keyed, or one no entry matches (a heading such as "the file is refused, nothing written; problems:"), is left as it is."""
    reg = load(conn)
    if not reg.get("entries") or not message:
        return message
    out = []
    for line in str(message).split("\n"):
        body = line.lstrip()
        k = None if body.startswith("[") else key_of(reg, body)
        out.append(f"{line[:len(line) - len(body)]}[{k}] {body}" if k else line)
    return "\n".join(out)


def for_read(reg: dict, read: str) -> dict:
    """{rule key: [the refusal texts of that rule]} for one read: what its record and its gates refuse, printed in its packet."""
    by: dict = {}
    for e in reg.get("entries", []):
        if read in e.get("reads", []):
            by.setdefault(e["key"], [])
            if e["match"] not in by[e["key"]]:
                by[e["key"]].append(e["match"])
    return dict(sorted(by.items()))


def build(root: pathlib.Path, reg: dict) -> tuple[dict, list, list, int]:
    """The registry with the `reads` of each entry worked out from the source: the reads of every site the entry keys, by `site_reads`
    (module.function, or the module alone as its default). Returns (registry, unkeyed sites, entries that key no site, number of sites). A
    migration writes the registry only when both lists are empty; the static test holds the stored registry to the same."""
    sr = reg.get("site_reads", {})
    entries = [{k: v for k, v in e.items() if k != "reads"} for e in reg.get("entries", [])]
    sites = scan(root, reg)
    reads = [set() for _ in entries]
    unkeyed = []
    for s in sites:
        hit = next((i for i, e in enumerate(entries) if (not e.get("site") or e["site"] == s["site"]) and e["match"] in s["template"]), None)
        if hit is None:
            if not s["wrapper"]:
                unkeyed.append(s)
            continue
        reads[hit] |= set(sr.get(s["site"], sr.get(s["site"].split(".")[0], [])))
    order = reg.get("reads_order", [])
    for e, r in zip(entries, reads):
        e["reads"] = [x for x in order if x in r]
    dead = [e for e, r in zip(entries, reads) if not r]
    return {**reg, "entries": entries}, unkeyed, dead, len(sites)


def _template(node) -> str | None:
    """The message of a site with each computed part as {}; None where it is not built from text (a variable passed on whole)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) else "{}" for v in node.values)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = _template(node.left), _template(node.right)
        if left is None and right is None:
            return None
        return (left if left is not None else "{}") + (right if right is not None else "{}")
    return None


def _wrapper(node) -> bool:
    """A message that ends by passing on a caught exception or a check's own text (`{where}: {exc}`, `... nothing written: {exc}`)."""
    last = node.values[-1] if isinstance(node, ast.JoinedStr) and node.values else (node.right if isinstance(node, ast.BinOp) else node)
    if isinstance(last, ast.FormattedValue):
        last = last.value
    if isinstance(last, ast.Call) and isinstance(last.func, ast.Name) and last.func.id == "str" and last.args:
        last = last.args[0]
    if isinstance(last, ast.Call) and isinstance(last.func, ast.Attribute) and last.func.attr == "join":
        return True         # the joined lines are sites of their own
    return isinstance(last, ast.Name) and last.id in _WRAPPED


def _heading_only(template: str, headings: list) -> bool:
    """A message that is only a heading over a joined list of problems ("the file is refused, nothing written; problems:" + the lines): the lines
    are sites of their own."""
    lit = template
    for h in headings:
        lit = lit.replace(h, "")
    return not lit.replace("{}", "").strip(" :;,.\n")


def _messages(n, sinks: set, endings: tuple, calls: dict, returns: bool) -> list:
    """The message expressions a node puts out as refusals: an append to a sink, a sink extended by a list or a comprehension, a raise of a
    refusal exception, a call that names the refused condition (fail("refused", msg)), or, in a check function that returns its refusal text,
    a returned string."""
    if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "append"
            and isinstance(n.func.value, ast.Name) and n.func.value.id in sinks and n.args):
        return [n.args[0]]
    if isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name) and n.target.id in sinks:
        if isinstance(n.value, ast.ListComp):
            return [n.value.elt]
        if isinstance(n.value, ast.List):
            return list(n.value.elts)
    if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) and n.exc.args and ast.unparse(n.exc.func).split(".")[-1].endswith(endings):
        return [n.exc.args[0]]
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in calls:
        i = calls[n.func.id]
        if len(n.args) > i and isinstance(n.args[0], ast.Constant) and n.args[0].value == "refused":
            return [n.args[i]]
    if returns and isinstance(n, ast.Return) and n.value is not None:
        return [n.value]
    return []


def scan(root: pathlib.Path, reg: dict) -> list[dict]:
    """Every refusal site of the scanned modules: {site: stem.function, line, template, wrapper}, each once under its innermost function.
    `modules` are paths under iba/app without .py (lib/readcommands); `only` narrows a module to the named functions; the exempt functions are
    left out."""
    sc = reg.get("scan", {})
    sinks, endings, calls = set(sc.get("sinks", [])), tuple(sc.get("exceptions", [])), sc.get("calls", {})
    returning, only = set(sc.get("returns", [])), sc.get("only", {})
    exempt = {x["site"] for x in reg.get("exempt", [])}
    found = {}
    for mod in sc.get("modules", []):
        stem = mod.split("/")[-1]
        tree = ast.parse((root / "iba" / "app" / f"{mod}.py").read_text(encoding="utf-8"))
        fns = sorted((f for f in ast.walk(tree) if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef))), key=lambda f: f.lineno)
        for fn in fns:          # outer before inner: an inner function's sites are written last, under its own name
            if mod in only and fn.name not in only[mod]:
                continue
            site = f"{stem}.{fn.name}"
            for n in ast.walk(fn):
                args = _messages(n, sinks, endings, calls, site in returning)
                args = [y for a in args for y in ((a.body, a.orelse) if isinstance(a, ast.IfExp) else (a,))]
                for arg in args:
                    t = _template(arg)
                    if t is None or _heading_only(t, sc.get("headings", [])):
                        continue
                    found[(mod, n.lineno, t)] = {"site": site, "line": n.lineno, "template": t, "wrapper": _wrapper(arg)}
    return [s for k, s in sorted(found.items()) if s["site"] not in exempt]
