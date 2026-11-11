import sys
sys.path.insert(0, "outputs/prior-capture/work")
from cap import Fill
c = Fill(16, "M01")
E = ["Esth.8.17"]
c.f("E1", "statement", "The second edict (Est 8:9-14) lets the Jews defend themselves; Mordecai goes out in royal robes and Susa rejoices (Est 8:15-16).", [44], verses=[f"Esth.8.{i}" for i in range(9, 17) if i != 12])
c.f("E2", "statement", "Est 8:17 holds two peoples under one decree: gladness and joy among the Jews, and fear among the peoples, which moved many of them to declare themselves Jews, \"for fear of the Jews had fallen on them\".", [45], verses=E)
c.f("E3", "statement", "The main operation in Est 8:17 is fear moving people to change sides: a public declaration made \"for fear\". The verse gives fear as the only reason; it names no conviction and no God, and the book of Esther never names God.", [45], verses=E, flag="the passage analysis at lines 49-51, which name no verse of their own")
c.f("E4", "link", "Est 8:17 is a third outcome of dread laid on a people, beside Rahab, whose heart melted at what she heard, and Moab, whose dread sent for a curse: taking on the name of the feared, \"for fear\".", [59], basis="read", verses=E)
c.f("E5", "statement", "Est 8:17 and 9:2 are dread with no named giver, so a reading must not say God laid this fear.", [61], basis="read", verses=["Esth.8.17", "Esth.9.2"])
c.f("Eface", "face", "Dread on a people that neither flees nor opposes: it joins the ones it fears (Est 8:17).", [59, 149], basis="read", verses=E, flag="the 'what it adds' paragraph, lines 56-57")
c.f("S1", "statement", "On the day the enemies \"hoped to gain the mastery\", \"the reverse occurred\" (Est 9:1); \"No one could stand against them, for the fear of them had fallen on all peoples\" (9:2); the officials helped, \"for the fear of Mordecai had fallen on them\" (9:3).", [69, 70, 71])
c.f("S2", "statement", "The main operation in Est 9:5 is not fear but acting at will (\"as they pleased\", the M18 word) against those who hated them; fear is in 9:2-3, and 9:2 states its effect: no one could stand.", [80], verses=["Esth.9.5", "Esth.9.2"], flag="the passage analysis at lines 73-75")
c.f("S3", "link", "With no one able to stand (Est 9:2), they \"did as they pleased\" (9:5): 9:5 is the outcome that completes the account of fear.", [80, 81, 150], basis="read", verses=["Esth.9.2", "Esth.9.5"])
EC = ["Eccl.12.1", "Eccl.12.3", "Eccl.12.4", "Eccl.12.5", "Eccl.12.7"]
c.f("K1", "statement", "Ecc 12:1-7 is one figure of old age, framed by \"Remember also your Creator in the days of your youth, before the evil days come\" (12:1) and ending \"the dust returns to the earth ... and the spirit returns to God who gave it\" (12:7).", [89, 91], verses=EC)
c.f("K2", "statement", "Inside the figure: \"the keepers of the house tremble, and the strong men are bent\" (Ecc 12:3); \"one rises up at the sound of a bird\" (12:4); then the fear of high places and of the road (12:5).", [92, 93], verses=EC)
c.f("K3", "statement", "The \"keepers of the house\" and the \"strong men\" are read as the body's own parts; the figure is not explained in the text.", [92], basis="read", verses=["Eccl.12.3"])
c.f("K4", "face", "Fear that comes as the body fails (Ecc 12:5): of high places and of the way out of doors, with the trembling of 12:3 and the startle at a bird in 12:4, set inside the call to remember the Creator before those days (12:1). It is not fear of a threat: the person is the one acted on, and the cause is age.", [99, 151], basis="read", verses=["Eccl.12.5", "Eccl.12.3", "Eccl.12.4", "Eccl.12.1"], flag="the 'what it adds' paragraph, lines 108-112")
PS = ["Ps.103.11", "Ps.103.13", "Ps.103.17"]
c.f("P1", "statement", "Psa 103:8-18 says \"those who fear him\" three times: the love \"as high as the heavens\" (103:11), the Father's compassion (103:13), and the steadfast love \"from everlasting to everlasting on those who fear him\" (103:17).", [119, 120, 121, 122], verses=PS)
c.f("P2", "statement", "The passage then says who they are: \"those who keep his covenant and remember to do his commandments\" (Psa 103:18); between these lines, \"he knows our frame; he remembers that we are dust\" (103:14).", [125], verses=["Ps.103.18", "Ps.103.14"])
c.f("P3", "statement", "The main operation in Psa 103:11 is God's steadfast love toward the one who fears him: the height word (M08) is a measure, and fear is the standing of the one loved.", [120, 152], basis="read", verses=["Ps.103.11"])
c.f("P4", "link", "Psa 103:17-18 joins fear to keeping and remembering: those who fear him are \"those who keep his covenant and remember to do his commandments\".", [139, 152], basis="read", verses=["Ps.103.17", "Ps.103.18"])
c.not_([18, 19, 20, 21, 28], "scope or method or process record", "what OT-97.37 holds: the verses marked forward to M01 and why, and which marks are not fear")
c.not_([24, 25, 26], "pointer with no content", "fear verses already carried in 10.12 or 10.9 or read and woven")
c.not_([53, 106], "scope or method or process record", "where the passage stands in the narrative now")
c.not_([154, 155, 156], "scope or method or process record", "what each reading would need as a register claim (rule 77)")
c.done()
