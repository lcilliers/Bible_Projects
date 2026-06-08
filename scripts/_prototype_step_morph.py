"""_prototype_step_morph.py — READ-ONLY prototype. Pulls STEP preview HTML per verse and extracts the
per-word MORPHOLOGY (morph code) for a term's own span, decoding part-of-speech and (for Hebrew verbs) the
STEM — the signal that selects a BDB sense-branch (S2 sense-resolution). Reports coverage + stem distribution.
NO DB writes. This validates whether a STEP morph backfill into wa_verse_records.morph_code/stem is viable.

STEP HTML shape (confirmed): <span morph='HNcfsa HC HR' strong='H1674 H9002 H9003'>anxiety</span>
  - morph and strong are whitespace-aligned lists; pick the morph at the index of the matching strong code.
  - morph code: [H|G] + POS letter (V verb, N noun, A adj, ...) + parsing. Hebrew verb stem = char after 'V'.

Usage:  python scripts/_prototype_step_morph.py --cluster M01 [--limit N] --out <file>.md
        python scripts/_prototype_step_morph.py --strongs H3372,H6342,H1674 --out <file>.md
"""
import argparse, os, re, sqlite3, sys
sys.path.insert(0, os.path.join("scripts", "analytics"))
sys.stdout.reconfigure(encoding="utf-8")
from step_client import StepClient
DB = os.path.join("database", "bible_research.db")

SPAN = re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)
HEB_STEM = {"q": "Qal", "N": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil", "H": "Hophal",
            "t": "Hithpael", "o": "Polel", "O": "Polal", "r": "Hithpolel", "v": "Hithpael",
            "f": "Hithpalpel", "j": "Pilpel", "l": "Pulal", "D": "Pealal",
            "c": "Tiphil", "u": "Polpal"}
POS = {"V": "verb", "N": "noun", "A": "adjective", "P": "pronoun", "R": "preposition",
       "C": "conjunction", "D": "adverb", "T": "particle", "S": "suffix"}


def base(code):
    m = re.match(r"^([HG]\d+)", code or "")
    return m.group(1) if m else (code or "")


def decode(morph):
    """Return (lang, pos, stem) from a single morph token like HVqi2ms / GN-NSF."""
    if not morph:
        return ("", "", "")
    lang = "Hebrew" if morph[0] == "H" else ("Greek" if morph[0] == "G" else "")
    body = morph[1:].lstrip("-")
    pos = POS.get(body[0], body[0] if body else "")
    stem = ""
    if lang == "Hebrew" and body[:1] == "V" and len(body) > 1:
        stem = HEB_STEM.get(body[1], f"?{body[1]}")
    return (lang, pos, stem)


def morph_for(html, strong):
    """Find the morph token matching `strong` (exact, else base) in any span of the verse HTML."""
    want = strong; wbase = base(strong)
    for morph_attr, strong_attr, _txt in SPAN.findall(html):
        scodes = strong_attr.split(); mcodes = morph_attr.split()
        for i, sc in enumerate(scodes):
            if sc == want or base(sc) == wbase:
                return mcodes[i] if i < len(mcodes) else (mcodes[0] if mcodes else "")
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster")
    ap.add_argument("--strongs")
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    if a.strongs:
        terms = [(s, s, "") for s in a.strongs.split(",")]
    else:
        rows = c.execute(
            "SELECT strongs_number, transliteration, language FROM mti_terms "
            "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY strongs_number", (a.cluster,)).fetchall()
        terms = [(r["strongs_number"], r["transliteration"], r["language"]) for r in rows][:a.limit]

    sc = StepClient()
    L = [f"# STEP morph extraction — viability prototype ({a.cluster or a.strongs})", ""]
    L.append("> READ-ONLY (`scripts/_prototype_step_morph.py`). Pulls STEP preview HTML per verse and extracts "
             "the term's own `morph` code; decodes POS + Hebrew verb STEM (the BDB sense-branch selector). "
             "Measures coverage = share of the term's verses where a morph was recoverable. No DB writes.")
    L.append("")
    L.append("| Term | Lang | verses | morph found | % | POS | stems (verbs) |")
    L.append("|---|---|---|---|---|---|---|")
    grand_v = grand_m = 0
    for strong, tl, lang in terms:
        try:
            recs, html = sc.get_verse_records_with_html(strong)
        except Exception as e:
            L.append(f"| {strong} {tl} | {lang} | ERR | {str(e)[:30]} | | | |"); continue
        nv = len(recs); found = 0; posc = {}; stemc = {}
        for r in recs:
            m = morph_for(html.get(r["osisId"], ""), strong)
            if m:
                found += 1
                _lg, p, st = decode(m)
                posc[p] = posc.get(p, 0) + 1
                if st:
                    stemc[st] = stemc.get(st, 0) + 1
        grand_v += nv; grand_m += found
        pct = f"{100*found/nv:.0f}%" if nv else "—"
        poss = ", ".join(f"{k}:{v}" for k, v in sorted(posc.items(), key=lambda x: -x[1]))
        stems = ", ".join(f"{k}:{v}" for k, v in sorted(stemc.items(), key=lambda x: -x[1])) or "—"
        L.append(f"| {strong} {tl} | {lang} | {nv} | {found} | {pct} | {poss} | {stems} |")
    L.append("")
    L.append(f"**Overall coverage: {grand_m}/{grand_v} "
             f"({100*grand_m/grand_v:.0f}% of occurrences had a recoverable morph)**." if grand_v else "no verses")
    L.append("")
    L.append("> Viability read: high coverage + clean stem decode ⇒ a STEP morph backfill into "
             "`wa_verse_records.morph_code`/`stem` is worth running (would make S2 sense-resolution, 84% of "
             "verses, STEP-mechanical). Greek terms carry tense/voice/mood rather than a Hebrew stem.")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"coverage {grand_m}/{grand_v}; wrote {a.out}")


if __name__ == "__main__":
    main()
