"""_assess_l2_triage.py — READ-ONLY. Runs the L2 MECHANICAL pass + ADEQUACY TRIAGE on every verse of a term:
mechanical outcome (stem→sense-branch, type, sub-shade count) + complexity signals (shade ambiguity, object
lean, negation, multi-term array, homonym) → first-cut verdict ACCEPT / API / RESEARCHER. Tests, on a hard
term, the real split and whether the adequacy signals are right. NO DB writes.

Triage is a JUDGEMENT on the mechanical outcome (feedback_l2_mechanical_api_triage): default ACCEPT, API the
exception, RESEARCHER the uncertain middle. The object-heuristic (fear-of-God→reverence / fear-of-threat→
dread) is a *mechanical aid* to resolve the within-stem shade; whether to trust it is a calibration choice,
so the report shows the split both with and without trusting it.

Usage:  python scripts/_assess_l2_triage.py --strongs H3372G --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
HEB_STEM = {"q": "Qal", "N": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil", "H": "Hophal", "t": "Hithpael"}
STEM_MARK = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)
SUBSHADE = re.compile(r"\d+[a-z]\d+\)")
GOD = re.compile(r"\b(lord|god|almighty|most high|holy one)\b", re.I)
THREAT = re.compile(r"\b(enemy|enemies|sword|army|armies|war|slay|kill|death|die|pursue|afraid of|nations|"
                    r"hand of|king of|wrath|destroy|terror|siege|flee)\b", re.I)
NEG = re.compile(r"\b(not be afraid|do not fear|fear not|be not afraid|have no fear|not fear|fear no|"
                 r"without fear|no fear)\b", re.I)
POSm = {"V": "ACTION", "N": "STATUS", "A": "QUALITY"}


def stem_of(m):
    if not m or m[0] != "H": return ""
    b = m[1:].lstrip("-")
    return HEB_STEM.get(b[1], "") if b[:1] == "V" and len(b) > 1 else ""


def pos_of(m):
    if not m: return "?"
    p = m[1] if m[0] == "H" and len(m) > 1 else (m[2] if m[0] == "G" and len(m) > 2 and m[1] == "-" else m[0])
    return POSm.get(p, "·")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--strongs", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"]) for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    clus = {r["id"]: r["cluster_code"] for r in c.execute("SELECT id, cluster_code FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 AND cluster_code NOT IN ('FLAG') AND cluster_code IS NOT NULL")}
    inv = c.execute("SELECT m.id id, m.transliteration tl, ti.parsed_meaning_id pmid FROM mti_terms m "
                    "LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number AND COALESCE(ti.delete_flagged,0)=0 "
                    "WHERE m.strongs_number=? GROUP BY m.id LIMIT 1", (a.strongs,)).fetchone()
    tl = inv["tl"]
    # sense branches + sub-shade counts
    branches = {}
    if inv["pmid"]:
        st = c.execute("SELECT group_concat(sense_text,'\n') s FROM wa_meaning_sense WHERE parsed_meaning_id=?", (inv["pmid"],)).fetchone()["s"] or ""
        marks = list(STEM_MARK.finditer(st))
        nnum = len(set(re.findall(r"(?:^|\n)\s*(\d+)\)\s", st)))
        for i, m in enumerate(marks):
            end = marks[i+1].start() if i+1 < len(marks) else len(st)
            seg = st[m.end():end]
            branches[m.group(1).capitalize()] = len(SUBSHADE.findall(seg))
    else:
        nnum = 0

    # this term's verses + the full array at each reference
    refs = [r[0] for r in c.execute("SELECT DISTINCT reference FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL", (inv["id"],))]
    qr = ",".join("?"*len(refs))
    arr = defaultdict(list); text = {}; mine = {}
    for r in c.execute(f"SELECT reference, verse_text, transliteration, morph_code, stem, mti_term_id FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND reference IN ({qr})", refs):
        arr[r["reference"]].append(r)
        if r["verse_text"]: text[r["reference"]] = r["verse_text"]
        if r["mti_term_id"] == inv["id"]: mine[r["reference"]] = r

    verd = Counter(); sig = Counter(); rows = []
    for ref in refs:
        r = mine[ref]; txt = text.get(ref, "") or ""
        stem = r["stem"] or stem_of(r["morph_code"])
        nsub = branches.get(stem, 0)
        others = [x for x in arr[ref] if x["mti_term_id"] in clus and clus[x["mti_term_id"]] != clus.get(inv["id"]) and clus[x["mti_term_id"]] != "T2"]
        narr = len([x for x in arr[ref] if clus.get(x["mti_term_id"]) == clus.get(inv["id"]) and x["mti_term_id"] != inv["id"]])
        g, th, ng = bool(GOD.search(txt)), bool(THREAT.search(txt)), bool(NEG.search(txt))
        shade_amb = nsub > 1
        # first-cut verdict
        if stem == "Piel" or nsub <= 1:
            v = "ACCEPT(clean)"
        elif ng:
            v = "ACCEPT(neg)"          # fear negated/displaced — readable mechanically
        elif g and not th:
            v = "ACCEPT(rev-lean)"     # fear of God → reverence
        elif th and not g:
            v = "ACCEPT(dread-lean)"   # fear of threat → dread
        elif g and th:
            v = "RESEARCHER"           # both objects present → genuinely ambiguous
        else:
            v = "API"                  # no object signal → needs a read
        verd[v] += 1
        if shade_amb: sig["shade_ambiguous"] += 1
        if g: sig["god_obj"] += 1
        if th: sig["threat_obj"] += 1
        if ng: sig["negation"] += 1
        if others: sig["cross_cluster"] += 1
        if narr: sig["same_cluster_array"] += 1
        rows.append((ref, stem, nsub, g, th, ng, len(others), v, re.sub(r"\s+", " ", txt)[:80]))

    n = len(refs)
    L = [f"# L2 mechanical + triage — hard case: {a.strongs} {tl} ({n} verses)", ""]
    L.append("> READ-ONLY (`scripts/_assess_l2_triage.py`). Mechanical pass (stem→branch, type, sub-shade) + "
             "adequacy signals → first-cut triage ACCEPT/API/RESEARCHER. Object-heuristic resolves the "
             "within-stem shade where it can; the rest escalates. No DB writes.")
    L.append("")
    L.append(f"**Sense-branch sub-shades:** " + ", ".join(f"{k}:{v}" for k, v in branches.items()) +
             f" · numbered senses (homonym watch): {nnum}")
    L.append("")
    L.append("## Triage split (first-cut)")
    L.append(""); L.append("| verdict | verses | % |"); L.append("|---|---|---|")
    for k, v in verd.most_common():
        L.append(f"| {k} | {v} | {100*v/n:.0f}% |")
    acc = sum(v for k, v in verd.items() if k.startswith("ACCEPT"))
    L.append(f"| **ACCEPT total** | **{acc}** | **{100*acc/n:.0f}%** |")
    L.append(f"| **escalate (API+RESEARCHER)** | **{n-acc}** | **{100*(n-acc)/n:.0f}%** |")
    L.append("")
    L.append("**If the object-heuristic is NOT trusted** (treat every shade-ambiguous Qal/Niphal as escalate): "
             f"ACCEPT(clean) only = {verd['ACCEPT(clean)']} ({100*verd['ACCEPT(clean)']/n:.0f}%); "
             f"escalate = {n-verd['ACCEPT(clean)']} ({100*(n-verd['ACCEPT(clean)'])/n:.0f}%).")
    L.append("")
    L.append("## Signal frequency")
    for k, v in sig.most_common():
        L.append(f"- {k}: {v} ({100*v/n:.0f}%)")
    L.append("")
    for bucket in ("API", "RESEARCHER", "ACCEPT(rev-lean)", "ACCEPT(dread-lean)", "ACCEPT(neg)", "ACCEPT(clean)"):
        ex = [x for x in rows if x[7] == bucket][:6]
        if not ex: continue
        L.append(f"## Sample — {bucket}")
        L.append(""); L.append("| Ref | stem | nsub | God | Thr | Neg | other | verse |"); L.append("|---|---|---|---|---|---|---|---|")
        for ref, stem, nsub, g, th, ng, no, v, t in ex:
            L.append(f"| {ref} | {stem} | {nsub} | {'Y' if g else ''} | {'Y' if th else ''} | {'Y' if ng else ''} | {no} | {t} |")
        L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{a.strongs} {tl}: {n} verses; ACCEPT {acc} ({100*acc/n:.0f}%); escalate {n-acc}; "
          f"clean-only ACCEPT {verd['ACCEPT(clean)']}; wrote {a.out}")


if __name__ == "__main__":
    main()
