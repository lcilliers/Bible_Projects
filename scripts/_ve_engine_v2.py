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
from step_client import StepClient
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


def finite_verb(morph):
    return morph_util.morph_category(morph) == "verb" and person(morph) is not None


def concise(md, gloss):
    md = (md or "").strip()
    if not md:
        return gloss
    md = re.split(r"[\n;]", md)[0].strip()
    md = re.sub(r"^\d+[a-z]?\)\s*", "", md)
    return md[:60]


class Step:
    def __init__(s): s.sc = StepClient(); s.h = {}; s.v = {}
    def html(s, strong, ref):
        key = base(strong)
        if key not in s.h:
            try:
                s.h[key] = s.sc.get_verse_records_with_html(key)
            except Exception:
                s.h[key] = ([], {})
        recs, second = s.h[key]
        osis = next((r.get("osisId") for r in recs if r.get("ref") == ref), None)  # select THIS verse
        if osis and isinstance(second, dict) and osis in second:
            return second[osis]
        return next(iter(second.values())) if isinstance(second, dict) and len(second) == 1 else ""
    def vocab(s, strong):
        if strong not in s.v:
            try: s.v[strong] = s.sc.get_vocab_info(base(strong))
            except Exception: s.v[strong] = {}
        return s.v[strong]


def measure_layer(html):
    """ordered words: {i, text, strongs[], morph, lang, pos, person, finite}."""
    words = []
    for i, (morphs, strongs, text) in enumerate(SPAN.findall(html or "")):
        m0 = morphs.split()[0] if morphs.split() else ""
        words.append({"i": i, "text": text.strip(), "strongs": [base(x) for x in strongs.split()],
                      "morphs": morphs.split(), "m0": m0, "lang": morph_util.morph_language(m0),
                      "pos": morph_util.morph_category(m0), "person": person(m0),
                      "finite": finite_verb(m0)})
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

    # N1 object — what the governing verb acts on (only when the term is the verb's subject; not the term)
    if gv is not None and gv in agreeing:
        after = [w for w in words if gv["i"] < w["i"] <= gv["i"] + 2 and w["i"] != ti and w["text"]]
        obj = next((w for w in after if re.search(r"S.?[123]", w["m0"]) or w["pos"] in ("noun", "pronoun")
                    or (w["lang"] == "Greek" and re.search(r"-A", w["m0"]))), None)
        if obj:
            out.append(("object", obj["text"], f"object of '{gv['text']}'"))

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

    # origin / valence / cause / response / effect — expectation test: silent -> NONE (no row) for now

    # ---- audit (founded + coverage) ----
    founded = all(c for (_i, _v, c) in out)
    content = [w for w in words if w["pos"] not in GRAMMAR and w["text"]]
    named = set()
    if term: named.add(term["i"])
    for w in content:
        # accounted if it's the term, a co-term strong, a seat, the gov verb, divine, intensifier, faculty
        acc = (w is term) or (gv and w["i"] == gv["i"]) or any(s in SEAT or s in DIVINE or s in INTENSIFIER or s in FACULTY_LEMMA for s in w["strongs"]) \
              or any(s in [base(c[3]) for c in unit["coterms"]] for s in w["strongs"])
        if acc: named.add(w["i"])
    gaps = [w["text"] for w in content if w["i"] not in named]
    audit = f"founded={'yes' if founded else 'NO'}; coverage gaps (content words not yet accounted): {gaps if gaps else 'none'}"
    out.append(("lexical_note", f"[audit] {audit}", "read-back audit"))
    return out


def narrate(unit, items):
    by = {}
    for (it, v, _c) in items:
        by.setdefault(it, []).append(v)
    def g(k): return by.get(k, [])
    cl = [f'In {unit["ref"]}, {unit["translit"]} ("{unit["gloss"]}")']
    if g("sense"): cl.append(f'sense: {g("sense")[0]}')
    if g("type"): cl.append(f'a {g("type")[0]}')
    if g("mode"): cl.append(f'in {g("mode")[0]} form')
    if g("location"): cl.append("located in the " + ", ".join(g("location")))
    if g("experiencer"): cl.append(f'experienced by {g("experiencer")[0]}')
    if g("faculty"): cl.append("engaging the " + ", ".join(g("faculty")) + " faculty")
    if g("how"): cl.append(f'operating by {g("how")[0]}')
    if g("object"): cl.append("acting on " + ", ".join(g("object")))
    if g("divine-involvement"): cl.append(f'God: {g("divine-involvement")[0]}')
    if g("intensity"): cl.append("intensity " + ", ".join(g("intensity")))
    if g("compound"): cl.append("combining with " + "; ".join(g("compound")))
    if g("relational"): cl.append("directed " + ", ".join(g("relational")))
    return cl[0] + " — " + ", ".join(cl[1:]) + "."


def main():
    refs = ["2Sa 1:9", "Psa 94:19", "Psa 139:23", "Luk 24:5", "Luk 24:37",
            "2Cor 5:6", "2Cor 7:16", "Exo 27:3", "Deu 31:20", "Psa 20:3", "Pro 11:25"]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    step = Step()
    out = ["# VE engine v2 — test run on the reviewed dump verses (DRY, no DB writes) — 2026-06-16", "",
           "> First build per 01b v2. Iteration-1 seed lists. Compare to `wa-raw-dump-with-narration-M01-M23-M46-20260615.md`.", ""]
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
        html = step.html(units[0]["strong"], ref)
        words = measure_layer(html)
        vt = cur.execute("SELECT verse_text FROM wa_verse_records WHERE reference=? LIMIT 1", (ref,)).fetchone()[0]
        out.append(f"## {ref}\n\n_{vt}_\n")
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
