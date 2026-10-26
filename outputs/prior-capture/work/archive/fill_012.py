"""Fill of capture-012 (fear observation ledger, unit 1), findings written from the document by hand (#2305)."""
import json, glob, pathlib, re
OUT = pathlib.Path("outputs/prior-capture")
src = sorted(glob.glob(str(OUT / "capture-012-2*.json")))[-1]
d = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
vw, by_line, CL = d["verse_words"], {l["line_no"]: l for l in d["lines"]}, "M01"
IDS = {**d["october_same_prefix"], **d["october"]}
F, ANS = [], {}


def verses_of(lines):
    out = []
    for n in lines:
        for r in by_line[n]["refs"]:
            if r["verse"] and r["verse"] not in out:
                out.append(r["verse"])
    return out


def nodes(verses, text, disp=None, note=None):
    out, seen = [], set()
    low = (text or "").lower()
    for v in verses:
        ws = [w for w in vw.get(v, []) if w["surface"] and any(c[0] == "M" for c in w["clusters"]) and
              re.search(chr(92) + "b" + re.escape(w["surface"].lower()) + chr(92) + "b", low)]
        if not ws:
            out.append({"verse": v})
        for w in ws:
            k = (v, w["strong"], w["surface"])
            if k not in seen:
                seen.add(k)
                n = {"verse": v, "strong": w["strong"], "surface": w["surface"],
                     "role": "characteristic" if CL in w["clusters"] else "standalone"}
                if CL in w["clusters"]:
                    n["cluster"] = CL
                out.append(n)
    for n in out:
        if disp:
            n["disposition"] = disp
        if note:
            n["disposition_note"] = note
    return out


def f(key, kind, text, lines, basis="stated", route=None, stable=None, disp=None, note=None, traced=(), flag=None):
    ns = nodes(verses_of(lines), text, disp, note) + [{"traced": t} for t in traced]
    F.append({"key": key, "kind": kind, "text": text, "basis": basis, "route": route, "stable_key": stable,
              "flag": flag, "nodes": ns})
    for n in lines:
        ANS.setdefault(n, {}).setdefault("captured", []).append(key)


f("U1", "unfitted", "The \"negated\" flag misses some \"Do not be afraid\" verses (1Sa 4:20, Gen 35:17), where the negator "
  "is not tagged T5 within two words; the face column was assigned by reading, not by the flag.", [32])
FACES = [
    (41, "A", "fear felt before a threat or a person: afraid, feared, fear, fearful and exceedingly, with an enemy, a king, an army, a place, the sword or being found out as the object; the subject is the one who fears."),
    (42, "B", "fear felt before God's presence or act: afraid, feared, fear and awe, with God himself, his fire, his act or the place he is met as the object."),
    (43, "C", "fear spoken against: \"Do not fear\", \"Fear not\", \"I will not fear\", \"not afraid\"; a speaker (God, an angel, a prophet, a leader, a midwife, Boaz, Jael, Absalom, the psalmist to himself) addresses the fear and a ground is given."),
    (44, "D", "fearing God as a way of life: fear, fears, feared, fearing, reverence, God-fearing and worship; not a passing state but a standing, commanded, learned, taught, given, lived, joined with walking, serving, keeping and turning from evil."),
    (45, "E", "awe or reverence toward people: revere and stood in awe, with father and mother, Joshua as Moses, and the king as the object."),
    (46, "F", "what inspires fear: awesome, awesome deeds, terrifying, fearsome, to be feared, awe-inspiring, terrible and fearfully; the word describes the one or thing feared, not the one who fears: God, his name, deeds, day, a place, an angel, a wilderness, a nation, creatures, the human frame."),
    (47, "G", "nations and peoples made to fear: the fear is laid on others, by God or because of his people."),
    (48, "H", "fearing other gods: the object is a god that is not the Lord."),
    (49, "I", "not fearing: absence of fear, of God or of consequence (did not fear, without fear, not afraid to)."),
    (50, "J", "other faces: fear rendered as a manner of acting (cautious, shuns, reveres, the word feared)."),
]
for ln, letter, txt in FACES:
    f(f"Face{letter}", "face", f"Face {letter}, {txt}", [ln], basis="read")

f("FE14", "statement", "\"Do not fear\" nearly always comes with a ground, introduced by \"for\": \"for I am with you\" (Gen 26:24; Isa 41:10; 43:5; Jer 1:8; Jer 42:11; Deu 20:1; Deu 31:8); \"I have given him into your hand\" (Num 21:34; Deu 3:2; Jos 8:1; 10:8; 11:6); \"I have redeemed you\" (Isa 43:1); \"I am your shield\" (Gen 15:1); \"God has heard the voice of the boy\" (Gen 21:17); \"you have borne a son\" (Gen 35:17; 1Sa 4:20); \"I will show you kindness\" (2Sa 9:7); \"those who are with us are more than those who are with them\" (2Ki 6:16); idols \"cannot do evil\" (Jer 10:5); \"am I in the place of God? ... I will provide for you\" (Gen 50:19, 21); \"for God has come to test you\" (Exo 20:20).", list(range(80, 91)), stable="fear:FE-14", disp="told", note="W; touches 10.9, 10.10, 11")
f("FE15", "statement", "\"Do not fear\" is paired with other commands: \"be strong and courageous\" (Deu 31:6; Jos 10:25; 1Ch 22:13; 28:20; 2Ch 32:7); \"do not be dismayed\" (Deu 1:21; 31:8; Jos 8:1; 2Ch 20:15, 17; Isa 41:10); \"stand firm, and see the salvation of the Lord\" (Exo 14:13); \"Remember the Lord, who is great and awesome\" (Neh 4:14); \"remember what the Lord your God did\" (Deu 7:18); \"Be careful, be quiet\" (Isa 7:4); \"let your hands be strong\" (Zec 8:13); \"let not your hands grow weak\" (Zep 3:16); \"Peace be with you\" (Dan 10:19); \"Peace to you\" (Gen 43:23; Judg 6:23).", list(range(92, 102)), stable="fear:FE-15", disp="told", note="W (the M23 and M24 neighbours enter only as far as these verses reach); touches 10.1, 10.7")
f("FE34", "party", "What God does toward those who fear him, one verse each: steadfast love (Psa 103:11, 17); compassion \"as a father shows compassion\" (Psa 103:13); \"The friendship of the Lord is for those who fear him\" (Psa 25:14); he instructs (Psa 25:12); \"the eye of the Lord is on those who fear him\" (Psa 33:18); \"The angel of the Lord encamps around those who fear him\" (Psa 34:7); no lack (Psa 34:9); food (Psa 111:5); \"fulfills the desire ... hears their cry\" (Psa 145:19); \"takes pleasure in\" (Psa 147:11); goodness stored up (Psa 31:19); salvation near (Psa 85:9); a banner (Psa 60:4); a heritage (Psa 61:5); the book of remembrance (Mal 3:16); \"the sun of righteousness shall rise\" (Mal 4:2).", list(range(126, 142)), route="B", stable="fear:FE-34", disp="told", note="W; touches 10.9")
f("FE38", "statement", "The same root is used of people held in reverence: \"revere his mother and his father\" (Lev 19:3); \"they stood in awe of [Joshua] just as they had stood in awe of Moses\", on the day \"the Lord exalted Joshua\" (Jos 4:14); awe of Solomon \"because they perceived that the wisdom of God was in him to do justice\" (1Ki 3:28); \"fear the Lord and the king\" (Pro 24:21); \"feared the Lord and Samuel\" (1Sa 12:18).", [150], stable="fear:FE-38", disp="told", note="W; touches 10.10")
f("FE39", "use", "Turned onto what is feared, the root describes: God himself, \"the great, the mighty, and the awesome God\" (Deu 10:17; 7:21), the great and awesome God \"who keeps covenant and steadfast love\" in three prayers (Neh 1:5; 9:32; Dan 9:4); his name (Psa 99:3; 111:9; Deu 28:58); his deeds (Psa 66:3, 5; 145:6; 106:22; Exo 34:10; Isa 64:3); his day, \"great and very awesome; who can endure it?\" (Joe 2:11, 31; Mal 4:5); a place (Gen 28:17); an angel's appearance (Jdg 13:6); the wilderness, \"great and terrifying\" (Deu 1:19; 8:15); an invading nation, \"dreaded and fearsome\" (Hab 1:7); a people \"feared near and far\" (Isa 18:2, 7); the living creatures' rims and the crystal expanse (Eze 1:18, 22); the human frame, \"I am fearfully and wonderfully made\" (Psa 139:14).", list(range(152, 164)), stable="fear:FE-39", disp="told", note="RS (11 §4: the root moves from the one who fears to the one feared); touches 10.9, 11 §4")
f("FE43", "statement", "Not fearing, of God or of consequence: \"you do not yet fear the Lord God\" (Exo 9:30); \"Do you not fear me? ... Do you not tremble before me?\" (Jer 5:22); \"They do not say in their hearts, 'Let us fear the Lord'\" (Jer 5:24); \"How is it you were not afraid to put out your hand to destroy the Lord's anointed?\" (2Sa 1:14); \"Why then were you not afraid to speak against my servant Moses?\" (Num 12:8); the wicked shoot \"suddenly and without fear\" (Psa 64:4); also Hos 10:3; Jer 3:8; 44:10; Psa 55:19.", list(range(168, 175)), stable="fear:FE-43", disp="told", note="W; touches 12, 10.8")
f("FE45", "use", "The root is rendered as a manner of acting: \"One who is wise is cautious and turns away from evil, but a fool is reckless\" (Pro 14:16); \"he who shuns an oath\" (Ecc 9:2); \"he who reveres the commandment will be rewarded\" (Pro 13:13); among Pharaoh's servants \"whoever feared the word of the Lord ... hurried his slaves and his livestock into the houses\" (Exo 9:20).", list(range(177, 181)), stable="fear:FE-45", disp="told", note="W; touches 10.7, 10.8")
f("C193", "link", "Before and after God acts, the same people and the same root are afraid of the threat, then fear the Lord (Exo 14:10 then 14:31; Jon 1:5, 10 then 1:16).", [193], traced=[IDS["fear:FE-12"]])
f("C196", "link", "Heart near or far: fear taught by men while \"their hearts are far from me\" set against fear put \"in their hearts\" (Isa 29:13; Jer 32:40).", [196], traced=[IDS["fear:FE-23"], IDS["fear:FE-24"]])
f("C197", "link", "One verse carries both values of the word: \"Do not fear ... that the fear of him may be before you\" (Exo 20:20); \"they feared the Lord but also served their own gods\" beside \"They do not fear the Lord\" (2Ki 17:33-34).", [197], traced=[IDS["fear:FE-20"], IDS["fear:FE-35"]])
f("S250", "silence", "The woman of Tekoa's \"the people have made me afraid\" (2Sa 14:15) is part of a staged story (2Sa 14:2-3); the verse stays in face A as data only.", [250], disp="data")

REC = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10, 71: 11, 72: 12, 73: 13, 102: 16, 103: 17, 104: 18,
       105: 19, 106: 20, 112: 21, 113: 22, 114: 23, 115: 24, 116: 25, 117: 26, 118: 27, 119: 28, 120: 29, 121: 30, 122: 31,
       123: 32, 124: 33, 142: 35, 143: 36, 144: 37, 164: 40, 165: 41, 166: 42, 175: 44, 181: 46}
for n, k in REC.items():
    ANS[n] = {"already_recorded": [IDS[f"fear:FE-{k:02d}"]]}
NOT = {203: ("pointer with no content", "a verse held for unit 2")}
for n in (229, 235, 247):
    NOT[n] = ("weave or quote-check record", "where observations were woven into the chapters")
NOT[254] = ("weave or quote-check record", "the quote corrections made after the unit 2 quote check")
for n, (c, r) in NOT.items():
    ANS[n] = {"not_an_observation": c, "reason": r}
for l in d["lines"]:
    l["answer"] = ANS.get(l["line_no"])
d["findings"] = F
missing = [l["line_no"] for l in d["lines"] if not l["answer"]]
(OUT / "work" / "capture-012-filled.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
print(len(F), "findings;", sum(len(x["nodes"]) for x in F), "nodes; unanswered:", missing)
