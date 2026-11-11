"""Fill for readings built of blocks: a lead-in paragraph with its bullets (or a bullet with indented evidence) is one
observation; tables go through Fill.auto(); headings, verse lists and process sections are passed over.
Usage: fill_block.py <reading_file id> <cluster> [<regex of the first heading of the passed-over tail>]"""
import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
fid, cl = int(sys.argv[1]), sys.argv[2]
tail_re = (sys.argv[3] or None) if len(sys.argv) > 3 else None
skip = {int(x) for x in sys.argv[4].split(",")} if len(sys.argv) > 4 else set()
c = Fill(fid, cl)
FL = open(c.d["file"]["path"], encoding="utf-8").read().replace("\r", "").split("\n")
first = next((i for i, t in enumerate(FL, 1) if re.match(r"##\s+\d+\.", t)), 1)
tail = next((i for i, t in enumerate(FL, 1) if tail_re and t.startswith("## ") and re.search(tail_re, t)), len(FL) + 1)


def tidy(s):
    s = re.sub(r"\(v[23]\)\s*", "", s)
    for _ in range(3):
        s = re.sub(r"\s*\([^()]*§[^()]*\)", "", s)
    s = _clean(s)
    return re.sub(r"^[-\d.]+\s+", "", s).strip()


def indent(t):
    return len(t) - len(t.lstrip(" "))


for n in sorted(c.by_line):
    k, t = c.by_line[n]["line_kind"], c.by_line[n]["text"]
    if n < first or n >= tail:
        c.not_(n, "scope or method or process record", "the scope, method and status of the reading, or its closing record of the work")
    elif k == "heading" or t.startswith("#"):
        c.not_(n, "heading", "the heading of a group or passage, with the verses it covers")
    elif k == "paragraph" and re.match(r"(Verses|Set verses):", t):
        c.not_(n, "reference list", "the verses of a group, listed")
    elif k == "paragraph" and t.startswith(">"):
        c.not_(n, "scope or method or process record", "a note")
i = first
while i < tail:
    t = FL[i - 1]
    if not t.strip() or t.startswith(("#", "|", ">")):
        i += 1
        continue
    # one block: consecutive non-blank lines that are not table rows or headings
    j = i
    while j < tail and FL[j - 1].strip() and not FL[j - 1].startswith(("#", "|", ">")):
        j += 1
    block = list(range(i, j))
    head = FL[i - 1]
    if not re.match(r"\s*-\s", head):                       # a lead-in paragraph with its bullets
        groups = [block]
    else:                                                    # top-level bullets, each with its indented evidence
        groups, cur = [], []
        for g in block:
            if indent(FL[g - 1]) == 0 and re.match(r"-\s", FL[g - 1]) and cur:
                groups.append(cur)
                cur = []
            cur.append(g)
        groups.append(cur)
    for grp in groups:
        lines = [g for g in grp if g in c.by_line and g not in c.ANS]
        if not lines:
            continue
        if grp[0] in skip or tail_re == "ALL":
            c.not_(lines, "scope or method or process record", "a record of the work (register items, checks, scope), not a finding")
            continue
        claim = tidy(FL[grp[0] - 1])
        kids = [tidy(FL[g - 1]) for g in grp[1:] if FL[g - 1].strip()]
        text = claim.rstrip(".:;") + (": " + "; ".join(k.rstrip(".") for k in kids) if kids else "") + "."
        vs, fl = None, None
        if not c.verses_of(lines):
            prev = [k for k in sorted(c.by_line) if k < min(lines) and c.verses_of([k])]
            if prev:
                vs, fl = c.verses_of([prev[-1]])[:1], "verse taken from the nearest earlier line: the references are bare"
        c.f(f"g{grp[0]}", "statement", text, lines, basis="read" if re.search(r"\bI read\b", text) else "stated", verses=vs, flag=fl)
    i = j
print(c.auto())
c.done()
