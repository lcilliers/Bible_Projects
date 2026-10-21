"""temp_2192_apply.py -- applies a #2192 comment-rewrite patch to one file. Temporary: archived
once #2192 is done.

Patch format: blocks headed `@@ START-END` (1-based, inclusive, original line numbers); the lines
under a header replace that range (none = delete). `{I}` in a new line is the indentation of the
range's first original line. Blocks are applied bottom-up, so every number refers to the original.

Usage:  python iba/app/tools/temp_2192_apply.py FILE PATCH
"""
import pathlib
import re
import sys


def main(target: str, patch: str) -> int:
    path = pathlib.Path(target)
    lines = path.read_bytes().decode("utf8").split("\n")   # each line keeps its own trailing \r
    blocks, cur = [], None
    for line in pathlib.Path(patch).read_text(encoding="utf8").splitlines():
        m = re.fullmatch(r"@@ (\d+)-(\d+)", line.strip())
        if m:
            cur = [int(m.group(1)), int(m.group(2)), []]
            blocks.append(cur)
        elif cur is not None:
            cur[2].append(line)
    blocks.sort(key=lambda b: b[0], reverse=True)
    last = None
    for start, end, new in blocks:
        if end < start or (last is not None and end >= last):
            print(f"bad or overlapping range {start}-{end}")
            return 1
        last = start
        indent = re.match(r"[ \t]*", lines[start - 1]).group(0)
        cr = "\r" if lines[start - 1].endswith("\r") else ""
        lines[start - 1:end] = [n.replace("{I}", indent) + cr for n in new]
    path.write_bytes("\n".join(lines).encode("utf8"))
    print(f"{path}: {len(blocks)} block(s) applied")
    return 0


def multi(patch: str) -> int:
    """A patch whose sections are headed `FILE <path>`: each section applied to its file."""
    import tempfile
    sections, cur = [], None
    for line in pathlib.Path(patch).read_text(encoding="utf8").splitlines():
        if line.startswith("FILE "):
            cur = [line[5:].strip(), []]
            sections.append(cur)
        elif cur is not None:
            cur[1].append(line)
    for target, body in sections:
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf8") as t:
            t.write("\n".join(body))
        if main(target, t.name):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(multi(sys.argv[1]) if len(sys.argv) == 2 else main(sys.argv[1], sys.argv[2]))
