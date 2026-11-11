import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
c = Fill(21, "M02")
for n in range(235, 241):
    c.f(f"hand{n}", "statement", "The hand of the Lord stands with the anger (OT-06): " + _clean(c.by_line[n]["text"]).lstrip("- ").rstrip(".") + ".", [n])
for n in range(249, 254):
    c.f(f"heat{n}", "statement", "The heat family outside the anger tag (ḥāmam, OT-15): " + _clean(c.by_line[n]["text"]).lstrip("- ").rstrip(".") + ".", [n])
c.not_([323, 324, 326, 327], "weave or quote-check record", "the quote check and its corrections")
print(c.auto())
c.done()
