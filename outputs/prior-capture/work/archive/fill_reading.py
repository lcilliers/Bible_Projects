"""Fill for a verse-by-verse reading document (M07 style): each labelled bullet is one observation by its label.
Usage: fill_reading.py <reading_file id> <cluster> [<regex of the first heading of the closing summary section>]"""
import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
fid, cl = int(sys.argv[1]), sys.argv[2]
tail_re = sys.argv[3] if len(sys.argv) > 3 else r"What (batch|the trial)"
c = Fill(fid, cl)
FL = open(c.d["file"]["path"], encoding="utf-8").read().replace("\r", "").split("\n")
first = next((i for i, t in enumerate(FL, 1) if re.match(r"##\s+1\.", t)), 1)
tail = next((i for i, t in enumerate(FL, 1) if t.startswith("## ") and re.search(tail_re, t)), len(FL) + 1)


def tidy(s):
    s = re.sub(r"^\s*-\s*", "", s)
    s = _clean(s)
    return s.strip()


kind_n = {}
for n in sorted(c.by_line):
    t = c.by_line[n]["text"]
    k = c.by_line[n]["line_kind"]
    s = tidy(t)
    low = s.lower()
    if t.startswith("#") or k == "heading":
        c.not_(n, "heading", "the heading of a verse reading, quoting the verse")
    elif k == "table row":
        c.not_(n, "reference list", "a table of passages and their verses")
    elif n < first:
        c.not_(n, "scope or method or process record", "the instruction, method and scope of the reading")
    elif low.startswith(("earlier reading", "earlier readings")):
        c.not_(n, "scope or method or process record", "where the passage is already cited in the narrative")
    elif low.startswith("pointer"):
        c.not_(n, "pointer with no content", "a pointer to another verse, reading or thread")
    elif n >= tail:
        if re.match(r"(not told anywhere|pointers kept|routes:|\*?\*?corrections)", low) or low.startswith(("not told", "pointers", "routes")):
            c.not_(n, "scope or method or process record", "placement notes and routes: a record of the work")
        elif t.lstrip().startswith("- ") and n < tail + 25 and "responses" not in low and not re.match(r"\d\.", low):
            c.f(f"f{n}", "face", s.rstrip(".") + ".", [n], basis="read")
        else:
            c.f(f"t{n}", "statement", s.rstrip(".") + ".", [n], basis="read" if "i read" in low else "stated")
    else:
        kind = "statement"
        if low.startswith("face"):
            kind = "face"
        elif low.startswith("relational observation"):
            kind = "link"
        elif low.startswith("the original"):
            kind = "term"
        basis = "read" if ("i read" in low or kind in ("face", "link")) else "stated"
        c.f(f"b{n}", kind, s.rstrip(".") + ".", [n], basis=basis)
print(c.auto())
c.done()
