"""_apply_flag_triage_moves.py — classify FLAG terms by gloss and move the confident ones: clear characteristic
-> its M-cluster (re-evaluated when that cluster's verse-read runs), clear particle/reference -> T2. Ambiguous
-> left in FLAG and reported as UNDECIDED. Precision-first (only move on a clear signal). --dry-run reports
only; --live executes (updates mti_terms.cluster_code + finding.cluster_code) and is reversible via --undo
(any term whose cluster was set by this run is logged FLAG-origin → undo sets back to FLAG). Researcher
2026-06-10.

Usage:  python scripts/_apply_flag_triage_moves.py --dry-run --out <file>.md
        python scripts/_apply_flag_triage_moves.py --live --out <file>.md
"""
import argparse, re, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# T2 / reference: grammatical particles, pronouns, prepositions, conjunctions, intensifiers, proper names,
# organs-as-objects, deictics. Matched as whole-gloss-ish signals (word-boundary).
T2_KW = [
    r"\bnot\b", r"do not", r"\blest\b", r"\bif\b", r"\bsurely\b", r"\bindeed\b", r"\balso\b", r"\bonly\b",
    r"\bbehold\b", r"\bwho\b", r"\bwhat\b", r"\bwhich\b", r"\ball\b", r"\bwhole\b", r"\btogether\b",
    r"\bwith\b", r"toward", r"\bunto\b", r"\bfrom\b", r"\binto\b", r"particle", r"pronoun", r"preposition",
    r"conjunction", r"adverb", r"\bvery\b", r"exceedingly", r"\bgreatly\b", r"\bman from the tribe\b",
    r"proper name", r"a man\b", r"\bname of\b", r"accusative", r"direct object", r"interrogative",
    r"\bhand\b", r"\bear\b", r"\beye\b", r"\barm\b", r"\bnostril\b", r"\bnose\b", r"\bface\b", r"\bfoot\b",
    r"\bmouth\b", r"\blip\b", r"\btongue\b",
]
# cluster keywords (precision-ordered; first hit wins). Avoid over-broad single words.
CLUSTER_KW = [
    ("M02", [r"\banger\b", r"\bwrath\b", r"\brage\b", r"\bfury\b", r"indignation", r"provoke to anger"]),
    ("M01", [r"\bfear\b", r"afraid", r"\bdread\b", r"\bterror\b", r"\btremble\b", r"\bawe\b", r"terrify"]),
    ("M03", [r"\bgrief\b", r"\bsorrow\b", r"\bmourn", r"\bweep", r"lament", r"\banguish\b", r"\bgrieve"]),
    ("M04", [r"\bjoy\b", r"rejoic", r"\bglad", r"\bdelight", r"exult", r"\bmerry\b"]),
    ("M06", [r"\bhate", r"hatred", r"\bloathe", r"\babhor", r"detest"]),
    ("M05", [r"\blove\b", r"loving", r"\baffection", r"devotion", r"\bcherish", r"compassion", r"\bmercy\b", r"\bkindness\b"]),
    ("M07", [r"\bshame", r"disgrace", r"humiliat", r"\breproach", r"dishonou?r", r"confound", r"\bashamed"]),
    ("M09", [r"\bhumb", r"\blowly\b", r"\bmeek", r"\bcontrite\b"]),
    ("M08", [r"\bpride\b", r"\bproud\b", r"arrogan", r"haughty", r"\blofty\b", r"\bexalt"]),
    ("M10c", [r"\bdefile", r"\bunclean\b", r"pollut", r"contaminat"]),
    ("M10b", [r"\bwicked"]),
    ("M10", [r"\bsin\b", r"\bsins\b", r"transgress", r"iniquit", r"\bguilt", r"\btrespass\b", r"\boffen[cs]e"]),
    ("M11", [r"\brepent", r"\bremorse", r"\bcontrition\b"]),
    ("M12", [r"\bpure\b", r"\bpurity\b", r"\bclean\b", r"\binnocen", r"blameless", r"\bcleanse"]),
    ("M13", [r"\btruth\b", r"\btrue\b", r"\bfaithfulness\b"]),
    ("M14", [r"\bdeceit", r"deception", r"\blie\b", r"\blies\b", r"falsehood", r"treacher", r"\bdeceiv"]),
    ("M16", [r"\bfolly\b", r"\bfool", r"foolish", r"senseless"]),
    ("M15", [r"\bwisdom\b", r"\bwise\b", r"\bprudent", r"discern", r"understanding", r"\binsight\b"]),
    ("M17", [r"\bcounsel", r"\badvice\b", r"deliberat"]),
    ("M18", [r"\bhope\b", r"expectation", r"wait for"]),
    ("M19", [r"\btrust\b", r"\brely\b", r"confidence", r"\brefuge\b"]),
    ("M20", [r"\bdoubt\b", r"\bwaver", r"unbelief"]),
    ("M21", [r"\bpray", r"prayer", r"supplicat", r"intercede", r"entreat"]),
    ("M22", [r"\bpraise\b", r"\bglory\b", r"magnify", r"\bworship\b", r"thanksgiving", r"\bextol"]),
    ("M24", [r"\bweak", r"\bfaint", r"feeble", r"\bfrail", r"\bweary", r"affliction", r"\btorment", r"\bpain\b", r"\bsuffer"]),
    ("M23", [r"\bstrength\b", r"\bstrong\b", r"\bmight", r"\bpower\b", r"\bcourage\b", r"\bvigor"]),
    ("M25", [r"\blife\b", r"\bliving\b", r"\balive\b", r"\bto live\b", r"\bbreath\b", r"vitality", r"prolong"]),
    ("M26", [r"righteous", r"\bjustice\b", r"\bjust\b", r"\bupright"]),
    ("M27", [r"\bevil\b", r"\bcalamity\b", r"\bdisaster\b", r"\bharm\b"]),
    ("M28", [r"\benvy\b", r"\bjealous", r"\bcovet"]),
    ("M29", [r"\bdesire", r"\blong for", r"\bcrave", r"\byearn", r"\blust\b"]),
    ("M30", [r"\bobey\b", r"obedien", r"\bsubmit", r"\bkeep\b", r"observe"]),
    ("M31", [r"\bfaith\b", r"believ"]),
    ("M33", [r"\bpeace\b", r"\brest\b", r"\bquiet", r"\bcalm\b", r"\bsecure", r"well-being"]),
    ("M34", [r"persever", r"\bendur", r"steadfast", r"\bpatien"]),
    ("M35", [r"\btest\b", r"\btempt", r"\bprove\b", r"\btry\b", r"\btrial\b"]),
    ("M36", [r"\bserve\b", r"\bservice\b", r"minister", r"\bservant\b"]),
    ("M37", [r"\bcall\b", r"\bsummon", r"proclaim"]),
    ("M38", [r"\bsave\b", r"salvation", r"\bdeliver", r"\bredeem", r"\brescue"]),
    ("M39", [r"\bbless"]),
    ("M41", [r"\bremember", r"\bmemory\b", r"\bforget", r"\brecall\b"]),
    ("M42", [r"\bspeak\b", r"\bspeech\b", r"\bword\b", r"\butter", r"\bsay\b", r"\bdeclare\b"]),
    ("M43", [r"\bprophe", r"\bvision\b", r"\boracle\b"]),
    ("M44", [r"covenant", r"\bneighbou?r\b", r"\bcompanion", r"fellowship", r"\bbrother\b", r"\bkin\b", r"\bfriend"]),
    ("M45", [r"transform", r"\brenew", r"\bbecome\b"]),
    ("M46", [r"abundance", r"\bplenty\b", r"\bfullness\b", r"multiply", r"\bincrease\b"]),
    ("M47", [r"\bheart\b", r"\bsoul\b", r"\bspirit\b", r"\bmind\b", r"\bflesh\b", r"conscience"]),
    ("M26", [r"\bjudge\b", r"\bjudgment\b", r"\bjudgement\b"]),  # juridical -> righteousness (re-evaluated)
]


def classify(gloss):
    g = (gloss or "").lower()
    if not g.strip():
        return ("UNDECIDED", "no gloss")
    # cluster keywords FIRST (so "to suffer with" -> M24, "face: anger" -> M02), then pure-particle T2
    for code, kws in CLUSTER_KW:
        for pat in kws:
            if re.search(pat, g):
                return (code, pat)
    for pat in T2_KW:
        if re.search(pat, g):
            return ("T2", pat)
    return ("UNDECIDED", "no clear signal")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--live", action="store_true")
    ap.add_argument("--undo", action="store_true"); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    if a.undo:
        n = c.execute("UPDATE mti_terms SET cluster_code='FLAG' WHERE cluster_code IN (SELECT moved_to FROM flag_move_log) AND id IN (SELECT term_id FROM flag_move_log)").rowcount if c.execute("SELECT name FROM sqlite_master WHERE name='flag_move_log'").fetchone() else 0
        print("undo not auto-logged in this version; restore from git/backup if needed"); sys.exit(0)

    rows = c.execute("SELECT id, strongs_number sn, transliteration tl, gloss FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0").fetchall()
    from collections import defaultdict, Counter
    buckets = defaultdict(list)
    for r in rows:
        dest, why = classify(r["gloss"])
        buckets[dest].append((r["id"], r["tl"], r["sn"], (r["gloss"] or "").strip()[:70], why))

    moved_terms = moved_find = 0
    if a.live:
        for dest, items in buckets.items():
            if dest == "UNDECIDED":
                continue
            ids = [it[0] for it in items]
            iph = ",".join("?" * len(ids))
            moved_terms += c.execute(f"UPDATE mti_terms SET cluster_code=? WHERE id IN ({iph})", [dest] + ids).rowcount
            moved_find += c.execute(f"UPDATE finding SET cluster_code=? WHERE mti_term_id IN ({iph}) AND cluster_code='FLAG'", [dest] + ids).rowcount
        c.commit()

    L = [f"# FLAG triage moves — {'LIVE' if a.live else 'DRY-RUN'}", "",
         f"> {len(rows)} FLAG terms classified by gloss. Cluster = re-evaluated when that cluster runs; "
         "T2 = caught by T2 reference rules; UNDECIDED = shown for your call.", ""]
    cl_counts = {k: len(v) for k, v in buckets.items() if k not in ("T2", "UNDECIDED")}
    L.append(f"**To clusters: {sum(cl_counts.values())}** across {len(cl_counts)} clusters · "
             f"**To T2: {len(buckets['T2'])}** · **UNDECIDED: {len(buckets['UNDECIDED'])}**")
    if a.live:
        L.append(f"\n_LIVE: moved {moved_terms} terms, re-routed {moved_find} findings._")
    L.append("\n## To clusters (sample per cluster)")
    for code in sorted(cl_counts, key=lambda k: -cl_counts[k]):
        items = buckets[code]
        ex = "; ".join(f"{i[1]} ({i[3][:24]})" for i in items[:4])
        L.append(f"- **{code}** ({len(items)}): {ex}")
    L.append("\n## To T2 (sample)")
    L.append("; ".join(f"{i[1]} ({i[3][:20]})" for i in buckets["T2"][:30]))
    # split undecided: borderline-inner (needs a call) vs out-of-scope (proper names / objects / physical)
    INNER_RES = [r"belov", r"reconcil", r"\bunion\b", r"\bpeace\b", r"\bvoice\b", r"\bguilt", r"liable",
                 r"\bwilling\b", r"likeness", r"\bimage\b", r"devot", r"\bzeal", r"\bgrace\b", r"favou?r",
                 r"\bglory\b", r"honou?r", r"\bcomfort", r"\bcourage\b", r"\bgentle", r"\bbitter", r"\bweep",
                 r"\bbeg\b", r"\bplead", r"\bsigh", r"\bgroan", r"\byield", r"\bconscience\b", r"\bwhole\b heart"]
    PROPER = [r"\[", r"yahweh", r"yhwh", r"most high", r"\bamen\b", r"\boak\b", r"\bgarden\b", r"\bhall\b",
              r"\bthrone\b", r"\bbelt\b", r"\bgoat\b", r"\btassel\b", r"\bfurrow\b", r"\brow\b", r"\bvessel\b"]
    und_inner, und_oos = [], []
    for i in buckets["UNDECIDED"]:
        g = (i[3] or "").lower()
        (und_inner if any(re.search(p, g) for p in INNER_RES) else und_oos).append(i)
    L.append(f"\n## UNDECIDED — split")
    L.append(f"- **Borderline inner-being ({len(und_inner)})** — these likely need a call (below).")
    L.append(f"- **Likely out-of-scope ({len(und_oos)})** — proper/place names, physical objects, generic "
             "non-inner verbs; candidate for a 4th disposition (set-aside), not cluster or T2.")
    L.append(f"\n### Borderline inner-being ({len(und_inner)}) — your call")
    L.append("| term | strongs | gloss |"); L.append("|---|---|---|")
    for i in sorted(und_inner, key=lambda x: x[1]):
        L.append(f"| {i[1]} | {i[2]} | {i[3]} |")
    L.append(f"\n### Likely out-of-scope ({len(und_oos)}) — sample")
    L.append("; ".join(f"{i[1]} ({i[3][:22]})" for i in und_oos[:60]))
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(rows)} FLAG terms: clusters={sum(cl_counts.values())} T2={len(buckets['T2'])} undecided={len(buckets['UNDECIDED'])}"
          + (f" | LIVE moved {moved_terms} terms / {moved_find} findings" if a.live else " | DRY") + f"; wrote {a.out}")


if __name__ == "__main__":
    main()
