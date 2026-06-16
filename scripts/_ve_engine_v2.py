"""_ve_engine_v2.py (2026-06-16) — FIRST working build of the verse-lexical engine per 01b v2.
TEST / DRY ONLY — writes no DB rows; outputs a comparison .md for the reviewed dump verses.

What it does, per term-in-verse:
  1. builds the MEASURE LAYER from STEP full-verse morphology (every word: strong + morph),
  2. derives the VE items by the 01b rules over that layer (original-language grounded),
  3. composes the narration (English equivalents, roles, multiples, UNRESOLVED placeholders),
  4. runs the read-back audit (founded / coverage) → a lexical_note.
Iteration-1: signal-lists are seeds (Strong's-based), clearly marked; harder roles → UNRESOLVED per
the expectation test (silent=NONE, only signal-present-but-unclear=UNRESOLVED).

  python scripts/_ve_engine_v2.py            # default: the M01/M23/M46 dump verses
"""
import sys, os, re, sqlite3, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
import morph_util
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SPAN = re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)

# ---- seed lists (Strong's-based; 01b iteration-1; expand later) ----
SEAT = {  # base Strong's -> constitutional level
    "H5315": "soul", "H5314": "soul", "G5590": "soul",
    "H3820": "heart", "H3824": "heart", "G2588": "heart",
    "H7307": "spirit", "G4151": "spirit",   # G4151/H7307 sense-gated below
    "H1320": "flesh", "G4561": "flesh",
}
SEAT_NONSEAT_SENSE = re.compile(r"\b(wind|breath|ghost|apparition|spirit\b.*dead|life)\b", re.I)  # gate hints
DIVINE = {"H3068", "H430", "H410", "H136", "H113", "H7706", "G2316", "G2962", "G2962"}
FACULTY_BY_CLUSTER = {  # R1 head-term faculty seed (cluster ~ characteristic)
    "M01": "affect", "M15": "cognition", "M23": "affect",
}
FACULTY_LEMMA = {  # R2 indirect: faculty signal lemmas (Strong's -> faculty)
    "H7200": "perception", "H2372": "perception", "G3708": "perception", "G1492": "perception",
    "H3045": "cognition", "G1097": "cognition", "G1492b": "cognition", "H995": "cognition",
    "H2142": "memory", "G3403": "memory",
    "H3372": "affect", "G5399": "affect", "H8055": "affect", "G5463": "affect",
    "H977": "volition", "G2309": "volition", "H7592": "volition",
}
INTENSIFIER = {"H7227": "many", "H7231": "many", "H3966": "very", "H3605": "all", "G4183": "many"}
FROM_PREP = {"H4480", "G575", "G1537"}                  # min / apo / ek -> received-from-outside
INHERENT_VALENCE = {"H7451": "sinful", "H7563": "sinful", "H6662": "righteous", "H6666": "righteous"}
PERCEPTION = {"G3708", "G1492", "G991", "G2334", "H7200", "H2372"}
COGNITION = {"G1380", "G1097", "H3045"}
PERC_COG = PERCEPTION | COGNITION
CAUSAL = {"H3588", "G3754", "G1063", "G1360"}           # ki / hoti / gar / dioti
COORD = {"H9002", "G2532"}                              # waw / kai
SPIRIT_BEINGS = {"G4151", "G1140", "H7307", "H7700"}    # pneuma / daimonion / ruach / shed
GRAMMAR = {"article", "preposition", "conjunction", "particle", "suffix"}  # POS that aren't content


def base(s):
    m = re.match(r"^([HG]\d+)", s or "")
    return m.group(1) if m else (s or "")


def person(morph):
    morph = morph or ""
    if "-" in morph:                          # Greek: person is the digit before S/P (number)
        m = re.search(r"([123])[SP]", morph)
        return int(m.group(1)) if m else None
    m = re.search(r"[123]", morph)            # Hebrew/Aramaic
    return int(m.group(0)) if m else None


def agree(morph):
    """(person, gender, number) — Hebrew verb '3ms'/noun 'ms'(3rd implicit); (None,..) for Greek/unparseable."""
    morph = morph or ""
    if "-" in morph:
        return (None, None, None)
    m = re.search(r"([123])([mfbc])([sp])", morph)        # verb: person+gender+number
    if m:
        return (int(m.group(1)), m.group(2), m.group(3))
    m = re.search(r"N\w?([mfbc])([sp])", morph)            # noun: 3rd person implicit
    if m:
        return (3, m.group(1), m.group(2))
    return (None, None, None)


def obj_type(w):
    if any(s in DIVINE for s in w["strongs"]): return "God"
    if any(s in SPIRIT_BEINGS for s in w["strongs"]): return "spiritual-being"
    if re.search(r"S.?[123]", w["m0"]) or w["pos"] == "pronoun": return "person"
    if w["pos"] == "noun": return "thing/abstract"
    return None


def finite_verb(morph):
    return morph_util.morph_category(morph) == "verb" and person(morph) is not None


def concise(md, gloss):
    md = (md or "").strip()
    if not md:
        return gloss
    md = re.split(r"[\n;]", md)[0].strip()
    md = re.sub(r"^\d+[a-z]?\)\s*", "", md)
    return md[:60]


class LexDB:
    """vocab() backed by the persisted `lexicon` table (no live STEP)."""
    def __init__(s, cur): s.cur = cur; s.c = {}
    def vocab(s, strong):
        b = base(strong)
        if b not in s.c:
            r = s.cur.execute("SELECT medium_def, gloss, transliteration, original_unicode, language, occurrence_count "
                              "FROM lexicon WHERE strong=?", (b,)).fetchone()
            s.c[b] = dict(r) if r else {}
        return s.c[b]


def load_words(cur, verse_id):
    """ordered words from the persisted measure layer (verse_morphology):
    {i, text, strongs[], morphs, m0, lang, pos, person, finite}."""
    words = []
    for r in cur.execute("SELECT word_index, surface, strongs, morph_code, language, pos, person "
                         "FROM verse_morphology WHERE verse_id=? ORDER BY word_index", (verse_id,)):
        morphs = (r["morph_code"] or "").split()
        m0 = morphs[0] if morphs else ""
        words.append({"i": r["word_index"], "text": r["surface"] or "",
                      "strongs": [base(x) for x in (r["strongs"] or "").split()],
                      "morphs": morphs, "m0": m0, "lang": r["language"], "pos": r["pos"],
                      "person": r["person"], "finite": (r["pos"] == "verb" and r["person"] is not None)})
    return words


def find_term(words, strong):
    b = base(strong)
    for w in words:
        if b in w["strongs"]:
            return w
    return None


def derive(unit, words, step):
    """unit: dict(strong, target_word, gloss, cluster, coterms[list of (translit,gloss,cluster,strong)]).
    returns list of (item, value, cite) and the audit."""
    out = []
    term = find_term(words, unit["strong"])
    ti = term["i"] if term else None

    # 1 sense (target_word + lemma medium_def) [P9 english]
    md = concise(step.vocab(unit["strong"]).get("medium_def"), unit["gloss"])
    out.append(("sense", f'{unit["tw"]} (lemma: {md})', "STEP per-occurrence + medium_def"))

    # 2 type (POS)
    pos = term["pos"] if term else None
    tmap = {"verb": "action", "noun": "status", "adjective": "quality"}
    out.append(("type", tmap.get(pos, "UNRESOLVED"), f"POS={pos}"))

    # 4 mode (column)
    if term:
        out.append(("mode", morph_util.morph_readable(term["m0"]), "morph"))

    # 3 compound (co-terms, gloss, role)
    for tr, gl, cc, st in unit["coterms"]:
        role = "qualifier" if cc == "T2" else ("shares-seat" if base(st) in SEAT else "partner")
        out.append(("compound", f'{tr} "{gl}" ({cc}) — role: {role}', "co-occurs in verse"))

    # 5 location (seat lemma in verse, sense-gated; unclear -> UNRESOLVED)
    for w in words:
        for st in w["strongs"]:
            if st in SEAT:
                lvl = SEAT[st]
                gloss = (step.vocab(st).get("medium_def") or "")
                if st in ("G4151", "H7307") and SEAT_NONSEAT_SENSE.search(w["text"] + " " + gloss):
                    out.append(("location", "UNRESOLVED", f"seat-term {st} present but sense may be non-seat ('{w['text']}')"))
                else:
                    out.append(("location", lvl, f"seat-term {st} ('{w['text']}')"))
                break

    # N3 how — the finite verb the TERM is the subject of (agreement); else nearest acting verb (term=object)
    COPULA = {"G1510", "G1096", "G5225"}
    gv = None
    agreeing = []
    if ti is not None and term:
        tp, tg, tn = agree(term["m0"])
        fins = [w for w in words if w["finite"] and w["i"] != ti and abs(w["i"] - ti) <= 4]
        agreeing = [w for w in fins if agree(w["m0"])[0] == tp and agree(w["m0"])[2] == tn]
        gv = min(agreeing or fins, key=lambda w: abs(w["i"] - ti)) if (agreeing or fins) else None
        if gv and term["pos"] == "adjective" and gv["strongs"][0] in COPULA:
            gv = None                                       # "were afraid": copula is not a meaningful 'how'
        if gv:
            kind = "term=subject" if gv in agreeing else "term=object"
            out.append(("how", f'{gv["text"]} ({gv["strongs"][0]})', f"governing verb · {kind}"))

    # N1 object — what the governing verb acts on (only when the term is the verb's subject; not the term) + object-type
    obj = None
    if gv is not None and gv in agreeing:
        after = [w for w in words if gv["i"] < w["i"] <= gv["i"] + 2 and w["i"] != ti and w["text"]]
        obj = next((w for w in after if re.search(r"S.?[123]", w["m0"]) or w["pos"] in ("noun", "pronoun")
                    or (w["lang"] == "Greek" and re.search(r"-A", w["m0"]))), None)
        if obj:
            out.append(("object", obj["text"], f"object of '{gv['text']}'"))
            ot = obj_type(obj)
            if ot:
                out.append(("object-type", ot, "from object lemma/morph"))

    # experiencer — the bearer: possessive suffix on/adjacent to the term; else the subject of its verb
    exp_p = None
    cand_words = ([term] if term else []) + [w for w in words if ti is not None and 0 < abs(w["i"] - ti) <= 1]
    for w in cand_words:
        if any(re.search(r"S.?[123]", m) for m in w["morphs"]):
            exp_p = next(person(m) for m in w["morphs"] if re.search(r"S.?[123]", m))
            break
    if exp_p is None and gv is not None and gv in agreeing:
        exp_p = gv["person"]
    if exp_p:
        out.append(("experiencer", {1: "self", 2: "other (addressed)", 3: "other"}[exp_p], f"person={exp_p}"))

    # 8 divine involvement (divine lemma -> state role) [C-3/C-5]
    div = next((w for w in words if any(s in DIVINE for s in w["strongs"])), None)
    if div is not None:
        role = "agent/subject" if div["finite"] or div["person"] == 3 else "present"
        if gv is not None and abs(div["i"] - gv["i"]) <= 1:
            role = "agent/subject"
        out.append(("divine-involvement", role, f"divine lemma '{div['text']}'"))

    # 7 faculty (R1 head-term by cluster; R2 indirect by faculty-lemma near term)
    fac = []
    r1 = FACULTY_BY_CLUSTER.get(unit["cluster"])
    if r1: fac.append((r1, "R1 head-term"))
    if ti is not None:
        for w in words:
            for st in w["strongs"]:
                if st in FACULTY_LEMMA and abs(w["i"] - ti) <= 3:
                    fac.append((FACULTY_LEMMA[st], f"R2 '{w['text']}'"))
    seen = set()
    for f, c in fac:
        if f not in seen:
            seen.add(f); out.append(("faculty", f, c))

    # N4 intensity
    for w in words:
        for st in w["strongs"]:
            if st in INTENSIFIER and ti is not None and abs(w["i"] - ti) <= 3:
                out.append(("intensity", f'{INTENSIFIER[st]} ({w["text"]})', f"intensifier near term"))

    # 13 relational (preposition attached to term + its object) — light
    if ti is not None:
        for w in words:
            if (w["pos"] == "preposition") and abs(w["i"] - ti) <= 1:
                out.append(("relational", f'{w["text"]}', "preposition adjacent to term"))

    # 6 origin (expectation test): 'from' preposition (min/apo/ek) near term -> received; else silent NONE
    if ti is not None and any(s in FROM_PREP for w in words if abs(w["i"] - ti) <= 2 for s in w["strongs"]):
        out.append(("origin", "received-from-outside", "'from' preposition (min/apo/ek) near term"))

    # valence (expectation test): term-inherent moral lemma -> value; else silent NONE (never imputed)
    v_inh = next((INHERENT_VALENCE[s] for s in (term["strongs"] if term else []) if s in INHERENT_VALENCE), None)
    if v_inh:
        out.append(("valence", v_inh, "term-inherent valence"))

    # N2 cause (expectation test): for an affect, the perceived/conceived object that triggered it
    facs = [v for (it, v, _c) in out if it == "faculty"]
    causal_near = ti is not None and any(s in CAUSAL for w in words if abs(w["i"] - ti) <= 2 for s in w["strongs"])
    if "affect" in facs:
        if obj is not None and gv is not None and gv["strongs"][0] in PERC_COG:
            out.append(("cause", f'{obj["text"]} (perceived)', f"object of '{gv['text']}'"))
        elif causal_near:
            out.append(("cause", "UNRESOLVED", "causal conjunction near term; cause unclear"))

    # 11 immediate-response (expectation test): the coordinated REACTION after the term (verb incl. participle;
    # not the governing verb, not a perception/cognition verb = that's the cause)
    if ti is not None:
        cands = [w for w in words if w["i"] > ti and w["pos"] == "verb" and (gv is None or w["i"] != gv["i"])
                 and not any(s in PERC_COG for s in w["strongs"])]
        if cands:
            cv = min(cands, key=lambda w: w["i"])
            between = [w for w in words if ti < w["i"] < cv["i"]]
            if any(s in COORD for w in between for s in w["strongs"]) or any(w["pos"] == "conjunction" for w in between):
                ro = next((w for w in words if cv["i"] < w["i"] <= cv["i"] + 2 and w["pos"] == "noun"), None)
                out.append(("immediate-response", cv["text"] + (f' {ro["text"]}' if ro else ""), "coordinated reaction after term"))

    # ---- audit (founded + coverage) ----
    founded = all(c for (_i, _v, c) in out)
    content = [w for w in words if w["pos"] not in GRAMMAR and w["text"]]
    named = set()
    if term: named.add(term["i"])
    cobases = [base(c[3]) for c in unit["coterms"]]
    for w in content:
        acc = (w is term) or (gv and w["i"] == gv["i"]) \
            or (ti is not None and w["finite"] and abs(w["i"] - ti) <= 2) \
            or any(s in SEAT or s in DIVINE or s in INTENSIFIER or s in FACULTY_LEMMA or s in SPIRIT_BEINGS or s in PERC_COG for s in w["strongs"]) \
            or any(s in cobases for s in w["strongs"])
        if acc: named.add(w["i"])
    gaps = [w["text"] for w in content if w["i"] not in named]
    audit = f"founded={'yes' if founded else 'NO'}; coverage gaps (content words not yet accounted): {gaps if gaps else 'none'}"
    out.append(("lexical_note", f"[audit] {audit}", "read-back audit"))
    return out


def _art(word):
    return "an" if word[:1].lower() in "aeiou" else "a"


def narrate(unit, items):
    by = {}
    for (it, v, _c) in items:
        by.setdefault(it, []).append(v)
    def g(k): return [x for x in by.get(k, []) if x != "UNRESOLVED"]
    def unr(k): return any(x == "UNRESOLVED" for x in by.get(k, []))
    cl = []
    if g("sense"): cl.append(f'carries the sense "{g("sense")[0]}"')
    elif unr("sense"): cl.append("[sense: UNRESOLVED]")
    if g("type"): cl.append(f'as {_art(g("type")[0])} {g("type")[0]}')
    if g("mode"): cl.append(f'in {g("mode")[0]} form')
    if g("location"): cl.append("located in the " + ", ".join(g("location")))
    elif unr("location"): cl.append("[location: UNRESOLVED]")
    if g("origin"): cl.append("originating " + ", ".join(g("origin")))
    if g("experiencer"): cl.append("borne by " + ", ".join(g("experiencer")))
    if g("faculty"): cl.append("engaging the " + ", ".join(g("faculty")) + " faculty")
    if g("how"): cl.append("operating by " + ", ".join(g("how")))
    if g("object"):
        ot = g("object-type")
        cl.append("acting on " + ", ".join(g("object")) + (f' ({ot[0]})' if ot else ""))
    if g("cause"): cl.append("caused by " + ", ".join(g("cause")))
    elif unr("cause"): cl.append("[cause: UNRESOLVED]")
    if g("divine-involvement"): cl.append("God's role: " + ", ".join(g("divine-involvement")))
    if g("valence"): cl.append("valence " + ", ".join(g("valence")))
    if g("intensity"): cl.append("intensity " + ", ".join(g("intensity")))
    if g("immediate-response"): cl.append("issuing in " + ", ".join(g("immediate-response")))
    if g("compound"): cl.append("combining with " + "; ".join(g("compound")))
    if g("relational"): cl.append("directed " + ", ".join(g("relational")))
    return f'In {unit["ref"]}, {unit["translit"]} ("{unit["gloss"]}") ' + ", ".join(cl) + "."


def main():
    refs = ["2Sa 1:9", "Psa 94:19", "Psa 139:23", "Luk 24:5", "Luk 24:37",
            "2Cor 5:6", "2Cor 7:16", "Exo 27:3", "Deu 31:20", "Psa 20:3", "Pro 11:25"]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    step = LexDB(cur)
    out = ["# VE engine v2 — test run on the reviewed dump verses (reads DB measure layer) — 2026-06-16", "",
           "> Per 01b v2. Measure layer read from `verse_morphology`/`lexicon` (no live STEP). Iteration-1 seed lists.", ""]
    timings = []
    MAX_SEC = float(os.environ.get("VE_MAX_SEC", "30"))
    for ref in refs:
        units = cur.execute("""SELECT vc.id vcid, vr.transliteration translit, m.gloss gloss, m.strongs_number strong,
            m.cluster_code cluster, vr.reference ref, vr.target_word tw
            FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            JOIN mti_terms m ON m.id=vc.mti_term_id
            WHERE vr.reference=? AND COALESCE(vc.delete_flagged,0)=0 AND m.cluster_code IN ('M01','M23','M46')""", (ref,)).fetchall()
        if not units: continue
        t0 = time.time()
        vrow = cur.execute("SELECT id FROM verse WHERE reference=?", (ref,)).fetchone()
        words = load_words(cur, vrow["id"]) if vrow else []
        vt = cur.execute("SELECT verse_text FROM wa_verse_records WHERE reference=? LIMIT 1", (ref,)).fetchone()[0]
        out.append(f"## {ref}  _(measure layer: {len(words)} words from DB)_\n\n_{vt}_\n")
        for u in units:
            coterms = cur.execute("""SELECT DISTINCT vr.transliteration tr, m.gloss gl, m.cluster_code cc, m.strongs_number st
                FROM verse_context vc2 JOIN wa_verse_records vr ON vr.id=vc2.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
                JOIN mti_terms m ON m.id=vc2.mti_term_id
                WHERE vr.reference=? AND m.strongs_number<>? AND COALESCE(vc2.delete_flagged,0)=0""", (ref, u["strong"])).fetchall()
            unit = dict(u); unit["coterms"] = [(c["tr"], c["gl"], c["cc"], c["st"]) for c in coterms]
            items = derive(unit, words, step)
            out.append(f"### {unit['translit']} ({unit['strong']}, {unit['cluster']}) — target '{unit['tw']}'")
            for (it, v, c) in items:
                out.append(f"- **{it}**: {v}  · _{c}_")
            out.append(f"\n**NARRATION:** {narrate(unit, items)}\n")
        dt = time.time() - t0
        timings.append((ref, dt, len(units)))
        out.append(f"_⏱ {dt:.2f}s · {len(units)} unit(s) · {dt/len(units):.2f}s/unit_\n")
        if dt > MAX_SEC:
            out.append(f"\n**⛔ CIRCUIT-BREAKER: {ref} took {dt:.1f}s > {MAX_SEC}s threshold — aborting bulk run.**")
            print(f"ABORT: {ref} {dt:.1f}s > {MAX_SEC}s"); break
    if timings:
        tot = sum(d for _r, d, _n in timings); nu = sum(n for _r, _d, n in timings)
        out += ["", "## ⏱ Timing monitor", "", "| verse | secs | units | s/unit |", "|---|---|---|---|"]
        for r, d, n in timings:
            out.append(f"| {r} | {d:.2f} | {n} | {d/n:.2f} |")
        out.append(f"| **TOTAL** | **{tot:.2f}** | **{nu}** | **{tot/nu:.2f}** |")
        out.append(f"\n_Circuit-breaker: aborts any verse over **{MAX_SEC}s** (env `VE_MAX_SEC`). "
                   f"At {tot/nu:.2f}s/unit a ~40,739-unit bulk run ≈ **{tot/nu*40739/3600:.1f}h** — STEP fetches dominate; "
                   f"pre-cache the measure layer + vocab before any bulk write._")
    p = "research/VE-lexical/wa-ve-engine-v2-testrun-20260616.md"
    open(p, "w", encoding="utf-8").write("\n".join(out))
    print("WROTE", p)
    print("\n".join(out))


if __name__ == "__main__":
    main()
