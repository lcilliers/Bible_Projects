import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
c = Fill(22, "M02")
c.f("U24", "unfitted", "1Sa 20:7 has two ḥārāh rows at one position: one span holds two codes in iba.db (an infinitive and a finite verb, HVqaa and HVqi3ms).", [24], verses=["1Sam.20.7"])
c.f("U25", "unfitted", "Jer 25:38 has two ḥārôn hits: the ESV renders the first \"sword\" (\"the sword of the oppressor\") and the second \"fierce anger\".", [25], verses=["Jer.25.38"])
for n in range(254, 258):
    c.f(f"hand{n}", "statement", "The hand of the Lord stands with the anger (OT-06): " + _clean(c.by_line[n]["text"]).lstrip("- ").rstrip(".") + ".", [n])
c.not_(range(234, 244), "pointer with no content", "a verse or finding not placed in the chapters, listed by name")
c.not_([333, 334, 335, 337], "weave or quote-check record", "the quote check and its corrections")
print(c.auto())
c.done()
