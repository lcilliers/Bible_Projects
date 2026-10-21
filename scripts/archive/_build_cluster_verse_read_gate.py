"""_build_cluster_verse_read_gate.py — READ-ONLY. The standard PER-CLUSTER GATE report produced as each
cluster finishes the verse-read: coverage, cross-cluster fan-out, flag rate, the mechanical tier profile of
the cluster's headline (highest-frequency) term, sample paragraphs, and flagged samples. No DB writes.

Usage:  python scripts/_build_cluster_verse_read_gate.py --cluster M15 --out <file>.md [--profile-term <mti_id>]
"""
import argparse, sqlite3, sys, os
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
PROF = [("type", 239), ("origin", 285), ("typology", 234), ("attributed_to_God", 225)]
FACULTY = {300: "affect", 291: "perception", 294: "cognition", 312: "moral-eval", 321: "relational",
           306: "volition", 315: "conscience", 297: "memory", 309: "agency", 303: "creativity"}

ap = argparse.ArgumentParser()
ap.add_argument("--cluster", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--profile-term", type=int, default=0)
a = ap.parse_args()
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
CL = a.cluster

own = c.execute("SELECT COUNT(*) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0", (CL,)).fetchone()[0]
rd = c.execute("""SELECT COUNT(*) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
                  AND EXISTS(SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id AND f.provenance='l2_meaning')""", (CL,)).fetchone()[0]
nterms = c.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CL,)).fetchone()[0]
own_para = c.execute("SELECT COUNT(*) FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id WHERE m.cluster_code=? AND f.provenance='l2_meaning'", (CL,)).fetchone()[0]
own_flag = c.execute("SELECT COUNT(*) FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id WHERE m.cluster_code=? AND f.provenance='l2_meaning' AND f.flagged_for_review=1", (CL,)).fetchone()[0]

L = [f"# {CL} — verse-read per-cluster gate", "",
     f"> READ-ONLY gate (`scripts/_build_cluster_verse_read_gate.py`). Coverage · fan-out · flag rate · "
     f"headline-term profile · samples. Not distillation — the cheap value-preservation check.", "",
     "## Coverage",
     f"- **{CL} own verses: {rd} / {own}** ({'COMPLETE' if rd >= own else 'GAP — ' + str(own-rd) + ' short'}); {nterms} active terms.",
     f"- **{own_para} {CL} paragraphs**; flagged **{own_flag} ({100*own_flag/own_para:.0f}%)** of own." if own_para else "- (no paragraphs)",
     ""]

# headline term = profile-term or highest-frequency own term
if a.profile_term:
    pt = a.profile_term
else:
    pt = c.execute("""SELECT vc.mti_term_id m, COUNT(*) n FROM verse_context vc JOIN mti_terms mm ON mm.id=vc.mti_term_id
                      WHERE mm.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0 GROUP BY vc.mti_term_id ORDER BY n DESC LIMIT 1""", (CL,)).fetchone()["m"]
t = c.execute("SELECT transliteration tl, strongs_number sn FROM mti_terms WHERE id=?", (pt,)).fetchone()
ptn = c.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (pt,)).fetchone()[0]
L.append(f"## Headline-term mechanical profile — {t['tl']} ({t['sn']}, {ptn} verses)")


def dist(obs):
    cnt = Counter()
    for r in c.execute("""SELECT f.finding_value v FROM finding f JOIN finding_question_link l ON l.finding_id=f.id
                          JOIN verse_context vc ON vc.id=f.verse_context_id
                          WHERE vc.mti_term_id=? AND f.provenance='l2_api' AND l.question_id=?""", (pt, obs)):
        cnt[(r["v"] or "").strip()[:26]] += 1
    return dict(cnt.most_common(6))


for lab, obs in PROF:
    L.append(f"- {lab}: {dist(obs)}")
fac = Counter()
for o, nm in FACULTY.items():
    n = c.execute("""SELECT COUNT(*) FROM finding f JOIN finding_question_link l ON l.finding_id=f.id JOIN verse_context vc ON vc.id=f.verse_context_id
                     WHERE vc.mti_term_id=? AND f.provenance='l2_api' AND l.question_id=? AND LOWER(f.finding_value) NOT IN ('none','')""", (pt, o)).fetchone()[0]
    if n: fac[nm] = n
L.append(f"- faculty engaged: {dict(fac.most_common())}")

# fan-out
L.append("\n## Cross-cluster fan-out (corpus paragraphs by cluster)")
L.append("| cluster | paragraphs |"); L.append("|---|---|")
for r in c.execute("SELECT m.cluster_code cc, COUNT(*) n FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id WHERE f.provenance='l2_meaning' GROUP BY m.cluster_code ORDER BY n DESC LIMIT 12"):
    L.append(f"| {r['cc']} | {r['n']} |")
ncl = c.execute("SELECT COUNT(DISTINCT m.cluster_code) FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id WHERE f.provenance='l2_meaning'").fetchone()[0]
L.append(f"\n_Corpus paragraphs now in **{ncl} clusters**._\n")

# sample own-cluster paragraphs
L.append(f"## Sample {CL} paragraphs")
for r in c.execute("""SELECT m.transliteration tl, vr.reference ref, f.finding_value para
                      FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id
                      JOIN verse_context vc ON vc.id=f.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                      WHERE m.cluster_code=? AND f.provenance='l2_meaning' AND LENGTH(f.finding_value)>140 ORDER BY f.id LIMIT 4""", (CL,)):
    L.append(f"\n**{r['tl']} · {r['ref']}** — {r['para'][:380]}")

os.makedirs(os.path.dirname(a.out), exist_ok=True)
open(a.out, "w", encoding="utf-8").write("\n".join(L))
print(f"{CL}: own {rd}/{own} | paragraphs {own_para} flagged {own_flag} | headline {t['tl']}; wrote {a.out}")
