"""Researcher request after #2545: work through the surfaces that WordNet leaves with no pair (wordnet-surface-pairs-v3-20261123.xlsx, pairs = 0)
and state for each (a) whether it is clearly not an inner-being state or behaviour and (b) why it did not bind.

Input : the v3 workbook (sheet surface_pairs), behaviour-and-inner-state-surfaces-v3-20261109.csv (surface group, base word), collections-v3-20261123.csv
        (collection words), WordNet 3.0 at data/imports/wordnet (NLTK) for the senses shown.
        Strong's root: the surface's dominant codes (a lettered code held by at least a quarter of the surface's occurrences in the surfaces export) and the other
        single-word surfaces that hold the same code as a dominant code, where at most 12 surfaces hold it (a code shared by many is a grammatical or very
        general rendering and binds nothing).
Output: _analytics/surfaces/exports/wordnet-no-pair-review-v2-20261123.xlsx (adds the Strong's root columns and the manual-intervention class)
(a) is the assistant's reading from meaning (rule collections-are-built-on-surfaces-one-each: Claude decides by what the words mean); it is read from the
word and its senses, not from each verse, and is for the researcher's scrutiny. Nothing is regrouped or changed. Temporary script (temp_ prefix).
"""
import csv, collections, pathlib
import nltk
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font

ROOT = pathlib.Path(__file__).resolve().parents[3]
EXP = ROOT / "_analytics" / "surfaces" / "exports"
nltk.data.path.insert(0, str(ROOT / "data" / "imports" / "wordnet"))
from nltk.corpus import wordnet as wn

# (a) clearly not an inner-being state or behaviour: a generic evaluative, motion, quantity, speech, modal or time word, or an object (rule 129 wording)
NOT = {
 "above": "generic: a reference in a text", "arrayed": "generic: physical arrangement or dress", "ashes": "object: material",
 "aroma": "object: a smell, not a state of the person", "befits": "generic evaluative", "breakers": "object: waves",
 "cannot": "modal word", "days": "quantity: time", "divisions": "generic: groupings", "earthly": "generic evaluative",
 "exceedingly": "quantity: degree adverb", "flame": "object: fire", "formerly": "time adverb", "length": "quantity",
 "lengthen": "quantity", "span": "quantity: time or distance", "limitations": "generic", "manhood": "generic: being a man",
 "manifest": "generic verb", "more": "quantity", "most": "quantity", "must": "modal word", "nature": "generic",
 "numerous": "quantity", "plainly": "generic: manner adverb", "possible": "modal word", "profitable": "generic evaluative",
 "proof": "generic", "stout": "generic: physical description", "unseen": "generic", "uppermost": "spatial",
 "useless": "generic evaluative", "famine": "external condition, not a state of the person",
}
# (a) open: external, relational, bodily or an old sense; the researcher decides (what the study would need to see in the verses)
OPEN = {
 "bowels": "KJV 'bowels' = the seat of compassion and feeling: belongs if the study reads the old idiom; WordNet reads it as the intestine",
 "character": "a trait word (Rom 5:4): inner-being state or generic",
 "conversation": "KJV 'conversation' = manner of life (behaviour); the modern sense is speech",
 "crippled": "bodily condition: check whether the verses use it of the inner being",
 "disease": "bodily; it has its own collection: check whether the verses use it of the inner being",
 "diseased": "bodily; as for disease",
 "doctrine": "teaching content: nearer speech or an object of belief than a state",
 "equity": "KJV 'equity' = uprightness: probably a state; the modern sense is ownership",
 "fellowship": "a relation between people: relational, not clearly a state of one person",
 "brotherly": "relational quality ('brotherly love' is an attitude)",
 "heritage": "a possession or lot: external unless a verse uses it of a settled inner portion",
 "inherited": "a possession or lot: as for heritage",
 "hindrance": "external obstacle",
 "imprisoned": "external confinement: may be a figure for bondage",
 "liberty": "a status or freedom: opposite of bondage in the collections",
 "life-giving": "describes a spirit or word: generic unless it names a state",
 "objected": "a speech act",
 "aloud": "a speech manner; it has its own collection",
 "joking": "speech or conduct (jesting)",
 "plight": "an external situation (distress)",
 "renown": "reputation: external",
 "splendor": "an external quality (majesty); it has its own collection",
 "stronghold": "a structure, used as a figure of refuge; it has its own collection",
 "fortune": "external wealth",
 "walk": "a motion word; in Scripture 'walk' = manner of life (behaviour)",
 "within": "spatial; may mean 'in the heart'; it has its own collection",
 "raved": "speech or conduct of madness or folly",
 "safekeep": "unclear: a behaviour of keeping safe; not in WordNet",
}
# (b) where WordNet's own senses for the word are not the study's sense
SENSE = {
 "bowels": "WordNet's senses: the centre of the earth; the intestine", "breakers": "WordNet's senses: surf; a quarry worker; an electrical switch",
 "pant": "WordNet's first sense is the garment (the noun); the verb (to gasp, to long) has no partner on the list", "waver": "WordNet's first sense is 'someone who waves'",
 "steal": "WordNet's first sense is 'a bargain' or the baseball steal", "must": "WordNet's first sense is 'a necessary thing' or grape juice",
 "more": "WordNet's first sense is the statesman Thomas More", "stout": "WordNet's first sense is the ale", "charity": "WordNet's first sense is the organisation",
 "fortune": "WordNet's first sense is luck or a large sum", "ashes": "WordNet's first sense is the residue (and the ash tree)", "proof": "WordNet's first sense is evidence or a mathematical proof",
 "flame": "WordNet's first sense is combustion", "days": "WordNet's first sense is the length of a life or a rotation of the earth", "span": "WordNet's first senses are a duration and a distance",
 "walk": "WordNet's first sense is the act of travelling by foot or a baseball walk", "virtue": "no partner on the list", "fret": "WordNet's first sense is agitation; the second is a worn spot",
}

rows = list(csv.DictReader(open(EXP / "behaviour-and-inner-state-surfaces-v3-20261109.csv", encoding="utf-8-sig")))
single = {r["surface"] for r in rows if " " not in r["surface"].strip()}
cnt = collections.defaultdict(collections.Counter)
for r in rows:
    if r["surface"] in single and r["strong"]:
        cnt[r["surface"]][r["strong"]] += 1
dom = {sf: {k: v for k, v in c.items() if v / sum(c.values()) >= 0.25} for sf, c in cnt.items()}
holders = collections.defaultdict(set)
for sf, ks in dom.items():
    for k in ks:
        holders[k].add(sf)
base_of, coll_of = collections.defaultdict(set), collections.defaultdict(set)
base_members = collections.defaultdict(set)
for r in rows:
    if r["surface"] in single:
        base_of[r["surface"]].add(r["base_word"])
        base_members[r["base_word"]].add(r["surface"])
        if r["collection"]:
            coll_of[r["surface"]].add(r["collection"])
cv = list(csv.DictReader(open(EXP / "collections-v3-20261123.csv", encoding="utf-8-sig")))
MEMBER = {"core", "synonym", "gathered", "phrase"}
coll_words = collections.defaultdict(set)
for r in cv:
    if r["tier"] in MEMBER and " " not in r["word"].strip():
        coll_words[r["collection"]].add(r["word"].lower())
word_colls = collections.defaultdict(set)
for r in cv:
    word_colls[r["word"].lower()].add(r["collection"])

wb = load_workbook(EXP / "wordnet-surface-pairs-v3-20261123.xlsx", read_only=True)
none = [(r[0], r[1], r[2]) for r in wb["surface_pairs"].iter_rows(min_row=2, values_only=True) if r[3] == 0]
pairs_of = {r[0]: r[3] for r in wb["surface_pairs"].iter_rows(min_row=2, values_only=True)}

out = []
for s, grp, inwn in none:
    mates = sorted(m for b in base_of[s] if b for m in base_members[b] if m != s)
    cols = word_colls.get(s.lower(), set()) | coll_of[s]
    cmates = sorted({w for c in cols for w in coll_words.get(c, ()) if w != s.lower() and w in {x.lower() for x in single}})
    if s in NOT:
        a, anote = "clearly not", NOT[s]
    elif s in OPEN:
        a, anote = "researcher to decide", OPEN[s]
    else:
        a, anote = "belongs", ""
    # (b)
    if inwn != "yes":
        if "’" in s or "'" in s:
            kind, why = "not in WordNet: possessive", "WordNet holds the plain word; my lookup did not strip the possessive ('s). A defect in my lookup, fixable."
        elif "-" in s:
            kind, why = "not in WordNet: hyphenated compound", "WordNet does not hold this compound; its parts are not looked up."
        elif s.startswith("un") or s.endswith(("ness", "ings", "ly", "er")):
            kind, why = "not in WordNet: derived form", "WordNet does not hold this derived form (prefix or suffix)."
        else:
            kind, why = "not in WordNet", "WordNet does not hold the word."
    else:
        if s in SENSE:
            kind, why = "WordNet senses are not the study's sense", SENSE[s]
        elif mates:
            kind, why = "WordNet holds it and its base-mates as unrelated words", "no shared sense, derivation or similar-to with: " + ", ".join(mates[:6])
        elif cmates:
            kind, why = "no WordNet relation to its collection-mates", "WordNet gives no synonym, derivation or similar-to with: " + ", ".join(cmates[:6])
        else:
            kind, why = "no WordNet relation to any surface on the list", "none of its WordNet senses reaches another surface"
    roots = {k: sorted(holders[k] - {s}) for k in dom.get(s, {}) if 1 < len(holders[k]) <= 12}
    root_txt = "; ".join(f"{k} (x{dom[s][k]}): " + ", ".join(v[:6]) for k, v in roots.items())
    dom_txt = ", ".join(f"{k} x{v}" for k, v in sorted(dom.get(s, {}).items()))
    if a == "clearly not":
        mi, who = "1 reallocate to other (confirm)", "researcher"
    elif a == "researcher to decide":
        mi, who = "2 decision needed", "researcher"
    elif roots:
        mi, who = "5 bind by Strong's root (confirm)", "researcher"
    elif inwn != "yes":
        mi, who = "4 not in WordNet: lookup or study base", "assistant"
    elif mates:
        mi, who = "6 bind by study base word (decide the link type)", "researcher"
    elif kind.startswith("WordNet senses are not"):
        mi, who = "3 conflicting sense: read the verses", "researcher"
    else:
        mi, who = "7 no relation: needs reading", "researcher"
    out.append((s, grp, inwn, a, anote, kind, why, ", ".join(sorted(cols))[:80], ", ".join(mates[:8]), dom_txt, root_txt, mi, who))

mc = collections.Counter(x[11] for x in out)
c = collections.Counter(x[3] for x in out)
k = collections.Counter(x[5] for x in out)
wbk = Workbook()
ws = wbk.active; ws.title = "README"
for line in [
    "Surfaces with no WordNet pair in wordnet-surface-pairs-v3-20261123.xlsx, worked through one by one (researcher's request after #2545).",
    "(a) is the assistant's reading from meaning, for the researcher's scrutiny: 'clearly not' = a generic evaluative, motion, quantity, speech, modal or time word or an object (the rule 129 wording); 'researcher to decide' = external, relational, bodily or an old sense, with what would settle it; 'belongs' = an inner-being state or behaviour as the study defines it. Read from the word and its senses, not from each verse. Nothing is regrouped or changed.",
    "(b) is the reason the surface did not bind; the sense notes come from WordNet's first senses.",
    "Strong's root: strong_dominant_codes = the lettered codes held by at least a quarter of the surface's occurrences (x = occurrences); strong_root_partners = the other single-word surfaces that hold the same code as a dominant code, when at most 12 surfaces do (a wider code is a general rendering and binds nothing). A partner through one occurrence is weak.",
    "manual_intervention: " + "; ".join(f"{a}: {n}" for a, n in sorted(mc.items())) + ". who_acts says whether the researcher decides or confirms, or the assistant can fix it (no decision).",
    f"{len(out)} surfaces: " + "; ".join(f"{a}: {n}" for a, n in c.most_common()) + ".",
    "Reasons: " + "; ".join(f"{a}: {n}" for a, n in k.most_common()) + "."]:
    ws.append([line])
ws.column_dimensions["A"].width = 180
w2 = wbk.create_sheet("review")
head = ["surface", "surface_group", "in_wordnet", "a_inner_being_or_behaviour", "a_note", "b_reason_kind", "b_detail", "collections_of_the_surface", "base_mates_on_list",
        "strong_dominant_codes", "strong_root_partners", "manual_intervention", "who_acts"]
w2.append(head)
for cell in w2[1]: cell.font = Font(bold=True)
for r in sorted(out, key=lambda x: (x[11], x[0])):
    w2.append(list(r))
w2.freeze_panes = "A2"
for i, wdt in enumerate([18, 18, 11, 22, 60, 44, 70, 30, 40, 30, 70, 44, 12], 1):
    w2.column_dimensions[w2.cell(1, i).column_letter].width = wdt
wbk.save(EXP / "wordnet-no-pair-review-v2-20261123.xlsx")
print(len(out), dict(c)); print(dict(k)); print(dict(sorted(mc.items())))
print("belongs by class:", dict(collections.Counter(x[11] for x in out if x[3] == "belongs")))
