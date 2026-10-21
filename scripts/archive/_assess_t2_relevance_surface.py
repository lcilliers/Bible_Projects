"""_assess_t2_relevance_surface.py  — READ-ONLY.

Surface which parked T2 ("Supplementary") terms are likely relevant to a real cluster, by overlapping each
T2 term's STEP sense-set against every named cluster's sense-envelope. idf-weighted so distinctive matches
rank above ubiquitous fear/anger/etc. tokens. No DB writes. Serves the eventual T2 rework (no-orphans).

Usage:
    python scripts/_assess_t2_relevance_surface.py --out research/investigations/<file>.md [--min-score 0.5]
"""
import argparse, math, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

STOP = set("""a an and or the of to be is are was were in on at as by for with from into onto upon that this
these those it its he she his her him they them their have has had not no any one some all such which who
whom whose when where while because so then than also more most very own same other another each every both
few many much s t qal niphal piel hiphil hithpael pual hophal twot bdb means also spelled cause caused make
made get got thing things person someone something state condition manner way like unto""".split())
SUFFIXES = ("ingly", "ing", "edly", "ed", "ied", "ies", "ness", "ment", "ful", "less", "ity", "ly", "es", "s")
WORD = re.compile(r"[a-zA-Z]+")
PAREN = re.compile(r"\([^)]*\)")  # strip "(ya.re)" transliterations from gloss lists

def stem(w):
    w = w.lower()
    for suf in SUFFIXES:
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[: -len(suf)]
    return w

def toks(text):
    if not text:
        return set()
    text = PAREN.sub(" ", text)
    out = set()
    for m in WORD.findall(text):
        if len(m) < 3:
            continue
        s = stem(m)
        if s in STOP or len(s) < 3:
            continue
        out.add(s)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-score", type=float, default=0.5)
    ap.add_argument("--top", type=int, default=3, help="candidate clusters shown per term")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # ---- cluster envelopes (named clusters only; exclude the parking/flag buckets) ----
    envelopes = {}   # code -> (short_name, token set)
    for r in c.execute("SELECT cluster_code, short_name, gloss FROM cluster "
                       "WHERE cluster_code NOT IN ('T2','FLAG') AND gloss IS NOT NULL"):
        envelopes[r["cluster_code"]] = (r["short_name"] or r["cluster_code"], toks(r["gloss"]))

    # document frequency of each token across cluster envelopes (for idf weighting)
    df = {}
    for _name, tk in envelopes.values():
        for t in tk:
            df[t] = df.get(t, 0) + 1
    N = len(envelopes)
    def idf(t):
        return math.log((N + 1) / (df.get(t, 0) + 1)) + 1.0  # smoothed

    # ---- T2 terms + their STEP sense tokens ----
    terms = c.execute("SELECT id, strongs_number, transliteration, gloss, owning_word "
                      "FROM mti_terms WHERE cluster_code='T2' AND COALESCE(delete_flagged,0)=0").fetchall()

    rows = []  # (score, strongs, translit, gloss, owning_word, [ (code,name,score,matched) ... ])
    for t in terms:
        inv = c.execute("SELECT step_search_gloss, short_def_mounce, meaning, parsed_meaning_id "
                        "FROM wa_term_inventory WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",
                        (t["strongs_number"],)).fetchone()
        sense_text = ""
        if inv and inv["parsed_meaning_id"]:
            for s in c.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=?",
                               (inv["parsed_meaning_id"],)):
                sense_text += " " + (s["sense_text"] or "")
        baseline = " ".join(filter(None, [
            t["gloss"], inv["step_search_gloss"] if inv else "", inv["short_def_mounce"] if inv else "",
            inv["meaning"] if inv else "", sense_text]))
        term_tokens = toks(baseline)
        if not term_tokens:
            continue
        # score every cluster
        scored = []
        for code, (name, env) in envelopes.items():
            matched = term_tokens & env
            if not matched:
                continue
            score = sum(idf(m) for m in matched)
            scored.append((score, code, name, sorted(matched, key=lambda m: -idf(m))))
        if not scored:
            continue
        scored.sort(reverse=True)
        top = scored[: args.top]
        rows.append((top[0][0], t["strongs_number"], t["transliteration"], t["gloss"],
                     t["owning_word"], top))

    rows.sort(reverse=True)
    surfaced = [r for r in rows if r[0] >= args.min_score]

    L = []
    L.append("# T2 (Supplementary) — STEP-sense relevance surfacing")
    L.append("")
    L.append("> READ-ONLY (`scripts/_assess_t2_relevance_surface.py`). Overlaps each parked T2 term's STEP "
             "sense-set against every named cluster's sense-envelope, idf-weighted so **distinctive** matches "
             "rank. A high score = the term's lexical sense lands in that cluster's semantic field → a "
             "candidate home for the eventual T2 rework. Candidate ≠ decision: the researcher judges.")
    L.append("")
    L.append(f"- T2 active terms scored: **{len(rows)}** (of 620; the rest had no cluster-token overlap)")
    L.append(f"- Surfaced at score ≥ {args.min_score}: **{len(surfaced)}**")
    L.append("")
    L.append("## Surfaced candidates (strongest first)")
    L.append("")
    L.append("| Score | T2 term | Gloss | Parked-under | Top candidate cluster(s) — matched sense tokens |")
    L.append("|---|---|---|---|---|")
    for score, sn, tr, gl, ow, top in surfaced:
        cands = "  ·  ".join(
            f"**{code} ({name})** {sc:.1f} [{', '.join(mt[:5])}]" for sc, code, name, mt in top)
        L.append(f"| {score:.1f} | {sn} {tr} | {gl} | {ow or ''} | {cands} |")
    L.append("")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Scored {len(rows)} T2 terms; surfaced {len(surfaced)} at >= {args.min_score}. Wrote {args.out}")

if __name__ == "__main__":
    main()
