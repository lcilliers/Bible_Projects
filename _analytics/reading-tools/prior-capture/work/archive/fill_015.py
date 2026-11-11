import sys, re
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(15, "M01")
L = ["Lam.4.6"]
c.f("V1", "statement", "The last clause of Lam 4:6, \"and no hands were wrung for her\", is literally \"and hands did not writhe in / on her\" (wᵉlōʾ ḥālû bāh yādāyim): the verb H2342A ḥûl, qal perfect; \"hands\", dual, H3027G; bāh, \"in / on / with her\".", [17], verses=L)
c.f("V2", "statement", "The anguish is in the root: ḥûl is the writhing of pain and fear, and here its subject is hands, so the tie between hands and anguish is in the Hebrew.", [17], verses=L, flag="the paragraph at lines 35-40, which names no verse of its own")
c.f("V3", "term", "The English idiom \"wrung\", and \"for her\", are the translator's rendering of \"writhed in / on her\"; the Hebrew also allows the clause to be read as \"no hands turned on her\" (Sodom fell \"in a moment\", by no human hand, with no siege). Both are open in the words; the ESV chose the first, which puts grief or anguish over her into the clause.", [17], basis="read", verses=L, flag="the paragraph at lines 35-40")
ROW = {27: "the body writhing in labour or pain", 28: "trembling, of the earth and of people", 29: "the heart in anguish", 30: "no anguish felt", 31: "birth", 32: "dance, whirl, storm", 33: "waiting"}
for n, face in ROW.items():
    x = [re.sub(r"\s+", " ", y.replace("**", "").replace("*", "")).strip() for y in c.by_line[n]["text"].strip().strip("|").split(" | ")]
    c.f(f"R{n}", "term", f"The root ḥûl, \"to twist, whirl\", is rendered as {face}: {x[1]}.", [n], basis="stated")
c.f("H44", "statement", "A pull of verses where a hand word stands with the writhing or anguish words, with the neighbouring verses read, shows the body, and the hands first, as where fear and anguish are seen; almost none of these verses is in the narrative.", [44], basis="read", verses=L)
c.f("H49", "statement", "Hands fall with the report: \"our hands fall helpless; anguish has taken hold of us, pain as of a woman in labor\" (Jer 6:24); the king of Babylon, \"his hands fell helpless; anguish seized him\" (Jer 50:43).", [49, 50])
c.f("H53", "statement", "Hands and heart go together: \"all hands will be feeble, and every human heart will melt ... pangs and agony will seize them\" (Isa 13:7-8); \"Every heart will melt, and all hands will be feeble; every spirit will faint, and all knees will be weak as water\" (Eze 21:7), heart, hands, spirit and knees in one breath; \"All hands are feeble, and all knees turn to water\" (Eze 7:17).", [53, 54, 56])
c.f("H58", "statement", "Hands held as in labour: \"Why then do I see every man with his hands on his stomach like a woman in labor? Why has every face turned pale?\" (Jer 30:6).", [58])
c.f("H59", "statement", "Fear aims at the hands: \"Fear not, O Zion; let not your hands grow weak\" (Zep 3:16); \"they all wanted to frighten us, thinking, 'Their hands will drop from the work' ... But now, O God, strengthen my hands\" (Neh 6:9).", [59, 61])
c.f("H62", "term", "A translation going the other way: \"his courage failed\" (2Sa 4:1) renders the hand word (H3027I, glossed \"courage\") with \"drop\" (H7503), literally his hands dropped; the translator turned a body word into an inner word, and reading the English alone hides the body.", [62])
c.f("H66", "statement", "The answer comes through the hands too: \"Strengthen the weak hands, and make firm the feeble knees\" (Isa 35:3); \"you have strengthened the weak hands\" (Job 4:3); \"lift your drooping hands and strengthen your weak knees\" (Heb 12:12).", [66, 67])
c.f("S75", "statement", "Anguish over another, or none: \"no hands ... for her\" (Lam 4:6) and \"they felt no anguish\" (Jer 5:3).", [75], verses=["Lam.4.6", "Jer.5.3"])
c.f("S77", "statement", "Compassion is overturned in the same passage: \"The hands of compassionate women have boiled their own children\" (Lam 4:10); \"hands\" is in 4:6 and 4:10, two verses apart, and the verses do not join them.", [77], verses=["Lam.4.10", "Lam.4.6"])
c.f("S76", "statement", "Two punishments are weighed, the sudden and the drawn-out: \"Happier were the victims of the sword than the victims of hunger\" (Lam 4:9), with ʿāwōn and ḥaṭṭāʾt (M56).", [87], verses=["Lam.4.9"], flag="the table row at line 76, which names no verse of its own")
c.not_([1], "heading", "the title of the reading")
c.not_([7], "scope or method or process record", "the researcher's instruction for this reading, quoted")
c.not_([69], "heading", "the heading of the table of what else Lam 4:6 carries")
c.not_([85, 88, 90], "next-steps list", "the weave and forward items proposed")
c.done()
