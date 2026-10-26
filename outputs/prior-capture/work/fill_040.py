import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
c = Fill(40, "M07")
T = lambda n: _clean(c.by_line[n]["text"]).lstrip("- ").strip()
for n in (68, 123, 159, 200, 223, 280):
    c.f(f"s{n}", "statement", T(n).rstrip(".") + ".", [n])
for n in (152, 158, 161, 162, 163, 164, 166):
    c.f(f"t{n}", "term", T(n).rstrip(".") + ".", [n])
for n in range(255, 262):
    c.f(f"f{n}", "face", "Seen in the verses: " + T(n).rstrip(".") + ".", [n], basis="read")
c.not_([110, 118, 119, 121, 134, 135, 136, 190, 191], "surface or gloss table", "a table row of a Strong's number, its gloss, hits and surface")
c.not_([227, 228, 229, 230], "scope or method or process record", "the verses forwarded to M07 or decided in other strands: a record of the work")
c.not_([249], "scope or method or process record", "where shame stands in the narrative now")
c.done()
