"""Generic fill for the M02 phenomena documents: claim bullets with their indented evidence bullets are one observation;
tables go through Fill.auto(); headings, verse lists, the method and 'bearing on earlier work' sections are passed over.
Usage: fill_phen.py <reading_file id> [<regex of the first heading that starts the passed-over tail>]"""
import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
fid = int(sys.argv[1])
tail_re = sys.argv[2] if len(sys.argv) > 2 else r"R-V"
c = Fill(fid, "M02")
FL = open(c.d["file"]["path"], encoding="utf-8").read().replace("\r", "").split("\n")
first = next(i for i, t in enumerate(FL, 1) if re.match(r"##\s+1\.", t))
tail = next((i for i, t in enumerate(FL, 1) if t.startswith("## ") and re.search(tail_re, t)), len(FL) + 1)


def tidy(s):
    s = re.sub(r"\(v[23]\)\s*", "", s)
    for _ in range(3):
        s = re.sub(r"\s*\([^()]*§[^()]*\)", "", s)
    s = _clean(s)
    return re.sub(r"^[-\d.]+\s+", "", s).strip()


def indent(t):
    return len(t) - len(t.lstrip(" "))


# 1. before the first numbered section, and the tail: passed over
for n in sorted(c.by_line):
    if n < first or n >= tail:
        c.not_(n, "scope or method or process record", "how the reading was done, what it changed in earlier work and its status: a record of the process")
# 2. headings, verse lists, notes
for n in sorted(c.by_line):
    if n in c.ANS:
        continue
    t = c.by_line[n]["text"]
    k = c.by_line[n]["line_kind"]
    if k == "heading" or t.startswith("#"):
        c.not_(n, "heading", "the heading of a phenomenon, with the verses it covers")
    elif k == "paragraph" and t.startswith("Verses:"):
        c.not_(n, "reference list", "the verses of a phenomenon, listed")
    elif k == "paragraph" and t.startswith(">"):
        c.not_(n, "scope or method or process record", "a note of correction in place")
# 3. claims with their evidence
i = first
while i < tail:
    t = FL[i - 1]
    if re.match(r"-\s", t):
        j, group = i + 1, [i]
        while j < tail and FL[j - 1].strip() and indent(FL[j - 1]) > 0:
            group.append(j)
            j += 1
        lines = [g for g in group if g in c.by_line and g not in c.ANS]
        if lines:
            claim = tidy(FL[i - 1])
            kids = [tidy(FL[g - 1]) for g in group[1:] if FL[g - 1].strip()]
            text = claim.rstrip(".:;") + (": " + "; ".join(k.rstrip(".") for k in kids) if kids else "") + "."
            read = bool(re.search(r"\bI read\b", text))
            vs, fl = None, None
            if not c.verses_of(lines):                       # bare references that did not resolve: the section heading's verse
                h = next((k for k in range(i, first - 1, -1) if FL[k - 1].startswith("## ") and k in c.by_line and c.verses_of([k])), None)
                if h:
                    vs, fl = c.verses_of([h])[:1], "verse taken from the section heading: the claim's references are bare"
            c.f(f"g{i}", "statement", text, lines, basis="read" if read else "stated", verses=vs, flag=fl)
        i = j
    else:
        i += 1
# 4. paragraphs that state something, tables, the rest
for n in sorted(c.by_line):
    if n in c.ANS:
        continue
    if c.by_line[n]["line_kind"] == "paragraph":
        c.f(f"p{n}", "statement", tidy(c.by_line[n]["text"]).rstrip(".") + ".", [n], basis="read" if "I read" in c.by_line[n]["text"] else "stated")
print(c.auto())
c.done()
