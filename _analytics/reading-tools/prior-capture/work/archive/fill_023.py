import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill, _clean
c = Fill(23, "M02")
c.f("U39", "unfitted", "Isa 57:17 has two qāṣap̄ rows: one sits on \"angry\" and the other on \"went on\"; the ESV has \"angry\" twice in the verse, and the second tag is on the wrong word.", [39], verses=["Isa.57.17"])
c.f("U40", "unfitted", "Zec 1:2 and 1:15: the noun qeṣep̄ stands beside its verb (\"angry with great anger\"); the ESV gives the noun as \"very\" and \"exceedingly\".", [40], verses=["Zech.1.2", "Zech.1.15"])
c.f("U44", "term", "H7110B (Hos 10:7, \"twig\") and H7111 (Joe 1:7, \"splintered\") are a different root from qeṣep̄; there is no anger in either verse.", [44], verses=["Hos.10.7", "Joel.1.7"])
c.f("S280", "statement", "2Ki 6:11 says \"greatly troubled\": there is no anger word in the verse.", [280], verses=["2Kgs.6.11"])
for n in range(286, 290):
    c.f(f"hand{n}", "statement", "The hand of the Lord stands with the anger (OT-06): " + _clean(c.by_line[n]["text"]).lstrip("- ").rstrip(".") + ".", [n])
c.not_(range(266, 278), "pointer with no content", "a verse or finding not placed in the chapters, listed by name")
c.not_([371, 372, 373], "weave or quote-check record", "the quote check and its corrections")
print(c.auto())
c.done()
