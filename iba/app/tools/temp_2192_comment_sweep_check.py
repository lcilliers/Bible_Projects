"""temp_2192_comment_sweep_check.py -- safety check for the #2192 comment sweep, and the listing it
works from. Temporary: archived once #2192 is done.

  check  : every changed .py file against HEAD -- compiles, and its AST with docstrings removed is
           identical (so only comments and docstrings changed). Exit 1 on any difference.
  blocks FILE : print the file's comment and docstring lines with line numbers.
  count  : history-marker lines per file, in the #2192 scope.

Usage:  python iba/app/tools/temp_2192_comment_sweep_check.py check|count|blocks FILE
"""
import ast
import difflib
import io
import pathlib
import re
import subprocess
import sys
import tokenize

ROOT = pathlib.Path(__file__).resolve().parents[3]
MARK = re.compile(r"(escalation #\d+|20\d\d-\d\d-\d\d|found (live|during|while)|researcher[, ]+"
                  r"(verbatim|ruling|chat)|verbatim|was (wrong|broken)|previously|used to|"
                  r"no longer|superseded|retired)", re.I)


def scope() -> list[pathlib.Path]:
    files = [p for p in (ROOT / "iba/app").rglob("*.py")
             if not set(p.relative_to(ROOT).parts) & {"migration", "archive", "__pycache__"}
             and not p.name.startswith("temp_")]
    return sorted(files + list((ROOT / ".claude/hooks").glob("*.py")))


def stripped(src: str, indent=None) -> str:
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = node.body
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                node.body = body[1:] or [ast.Pass()]
    return ast.dump(tree, include_attributes=False, indent=indent)


def doc_lines(src: str):
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        is_doc = tok.type == tokenize.STRING and tok.string.lstrip("rbuRBU").startswith(('"""', "'''"))
        if tok.type == tokenize.COMMENT or is_doc:
            for i, line in enumerate(tok.string.splitlines()):
                yield tok.start[0] + i, line


def check() -> int:
    out = subprocess.run(["git", "diff", "--name-only", "HEAD", "--", "*.py"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    bad = 0
    for rel in out:
        p = ROOT / rel
        if not p.exists() or "migration" in p.parts or p.name.startswith("temp_"):
            continue
        new = p.read_text(encoding="utf8")
        old = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True,
                             text=True, encoding="utf8").stdout
        try:
            compile(new, rel, "exec")
            same = stripped(old) == stripped(new)
        except SyntaxError as e:
            print(f"FAIL {rel}: does not compile: {e}")
            bad += 1
            continue
        print(f"{'ok  ' if same else 'FAIL'} {rel}" + ("" if same else ": code changed"))
        if not same:
            diff = difflib.unified_diff(stripped(old, 1).splitlines(), stripped(new, 1).splitlines(),
                                        lineterm="", n=6)
            print("\n".join(list(diff)[:40]))
        bad += 0 if same else 1
    print(f"{len(out)} changed file(s), {bad} failing")
    return 1 if bad else 0


def count() -> int:
    tot = 0
    rows = []
    for p in scope():
        n = sum(1 for _, line in doc_lines(p.read_text(encoding="utf8")) if MARK.search(line))
        tot += n
        if n:
            rows.append((n, p.relative_to(ROOT).as_posix()))
    for n, f in sorted(rows, reverse=True):
        print(n, f)
    print(f"total {tot} in {len(rows)} files")
    return 0


def blocks(path: str) -> int:
    src = (ROOT / path).read_text(encoding="utf8")
    raw = src.split("\n")
    for n, line in doc_lines(src):
        trailing = line.startswith("#") and not raw[n - 1].lstrip().startswith("#")
        print(f"{n}{' T' if trailing else ''}: {line}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1]
    sys.exit(check() if cmd == "check" else count() if cmd == "count" else blocks(sys.argv[2]))
