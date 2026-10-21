"""temp_2192_active_reach.py -- which iba/app Python modules serve an active function (#2192).
Temporary: archived once #2192 is done.

Entry points: iba/app/run.py, iba/app/init.py, the handler module of every ACTIVE cfg_step row,
every iba.app module a PS script, hook or settings file invokes (`python -m iba.app.x` or a path
under iba/app/), and iba.app modules imported by an active cfg_utility file outside iba/app.
Reach = entry points plus everything they import, transitively (imports inside functions count).
A module not reached serves no active function. Read-only.

Usage:  python iba/app/tools/temp_2192_active_reach.py [--detail]
"""
import ast
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
APP = ROOT / "iba" / "app"


def mod_of(path: pathlib.Path) -> str:
    return ".".join(path.relative_to(ROOT).with_suffix("").parts)


def scope() -> dict[str, pathlib.Path]:
    out = {}
    for p in APP.rglob("*.py"):
        parts = set(p.relative_to(ROOT).parts)
        if parts & {"migration", "archive", "__pycache__"} or p.stem == "__init__":
            continue
        out[mod_of(p)] = p
    return out


def imports(path: pathlib.Path) -> set[str]:
    pkg = mod_of(path).rsplit(".", 1)[0]
    found = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf8"))):
        if isinstance(node, ast.Import):
            found |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                up = pkg.split(".")
                up = up[:len(up) - node.level + 1]
                base = ".".join(up + ([base] if base else []))
            found.add(base)
            found |= {f"{base}.{a.name}" for a in node.names}
    return found


def main() -> int:
    mods = scope()
    conn = sqlite3.connect(f"file:{ROOT / 'iba/app/db/iba.db'}?mode=ro", uri=True)
    entry = {"iba.app.run": "dispatcher", "iba.app.init": "bootstrap"}
    for wp, step, handler in conn.execute(
            "SELECT work_package, step, handler FROM cfg_step WHERE inactive=0 AND handler IS NOT NULL"):
        entry.setdefault(handler.split(":")[0], f"active step {step}")
    callers = list((APP / "ps").glob("*.ps1")) + list(APP.glob("*.ps1"))
    callers += [p for p in (ROOT / ".claude").rglob("*") if p.is_file() and p.suffix in (".py", ".ps1", ".json", ".md")]
    for c in callers:
        text = c.read_text(encoding="utf8", errors="ignore")
        for m in re.findall(r"iba\.app\.[\w.]+", text):
            entry.setdefault(m.rstrip("."), f"called by {c.relative_to(ROOT).as_posix()}")
        for pkg, names in re.findall(r"from (iba\.app[\w.]*) import ([\w, ]+)", text):
            for n in names.split(","):
                n = n.strip().split(" ")[0]
                if n:
                    entry.setdefault(f"{pkg}.{n}", f"called by {c.relative_to(ROOT).as_posix()}")
        for m in re.findall(r"iba[\\/]app[\\/]([\w/\\]+)\.py", text):
            entry.setdefault("iba.app." + m.replace("\\", ".").replace("/", "."),
                             f"called by {c.relative_to(ROOT).as_posix()}")
    for (fp,) in conn.execute("SELECT file_path FROM cfg_utility WHERE inactive=0"):
        p = ROOT / fp
        if p.suffix == ".py" and p.exists() and not str(fp).startswith("iba/app/"):
            for m in imports(p):
                if m.startswith("iba.app."):
                    entry.setdefault(m, f"imported by active utility {fp}")
    reached, reason, todo = set(), {}, []
    for m, why in entry.items():
        if m in mods:
            todo.append(m)
            reason[m] = why
    while todo:
        m = todo.pop()
        if m in reached:
            continue
        reached.add(m)
        for i in imports(mods[m]):
            if i in mods and i not in reached:
                reason.setdefault(i, f"imported by {m}")
                todo.append(i)
    util = {r[0]: r[1] for r in conn.execute("SELECT file_path, inactive FROM cfg_utility")}
    unreached = sorted(set(mods) - reached)
    print(f"{len(mods)} modules in scope, {len(reached)} serve an active function, {len(unreached)} do not")
    for m in unreached:
        rel = mods[m].relative_to(ROOT).as_posix()
        print(f"  UNREACHED {rel}  (cfg_utility inactive={util.get(rel, 'unregistered')})")
    if "--detail" in sys.argv:
        for m in sorted(reached):
            print(f"  active {mods[m].relative_to(ROOT).as_posix()}: {reason[m]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
