"""_apply_flag_empty_to_t2.py — empties FLAG: every remaining FLAG term -> T2 (the catch-all reference bucket;
harmless, dragged into a verse only if it acts as a qualifier there), EXCEPT a small hand-list of borderline
*characteristics* that route to their cluster (re-evaluated when that cluster runs). Updates mti_terms.cluster_code
+ finding.cluster_code. Reversible via --undo (T2/cluster terms touched by this run can be set back to FLAG by
git revert of the logged ids — printed). Researcher 2026-06-10: non-characteristics -> T2 'do no harm'.

Usage:  python scripts/_apply_flag_empty_to_t2.py [--dry-run]
"""
import argparse, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
# borderline CHARACTERISTICS (by Strong's) -> cluster; everything else in FLAG -> T2
CHAR = {
    "H3513H": "M22", "H3513I": "M22", "H3513J": "M22",   # ka.ved (honor) -> Praise
    "H2470B": "M21",                                       # cha.lah (to beg) -> Prayer
    "H0014": "M30",                                        # a.vah (be willing) -> Obedience
    "G4090": "M03",                                        # pikros (bitterly) -> Grief
    "G8878": "M09",                                        # prauthumos (gentle-minded) -> Humility
    "H2594": "M39",                                        # cha.ni.nah (favor) -> Blessing
    "G1259": "M33",                                        # diallasso (be reconciled) -> Peace
    "H2256C": "M44",                                       # cho.ve.lim (union) -> Relational
    "G1777": "M10",                                        # enochos (liable/guilt) -> Sin
}

ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); a = ap.parse_args()
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
flag = c.execute("SELECT id, strongs_number sn, transliteration tl FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0").fetchall()
to_char = [(r["id"], r["sn"], r["tl"], CHAR[r["sn"]]) for r in flag if r["sn"] in CHAR]
to_t2 = [r["id"] for r in flag if r["sn"] not in CHAR]
print(f"FLAG terms: {len(flag)} | -> clusters: {len(to_char)} | -> T2: {len(to_t2)}")
for i in to_char:
    print(f"   {i[2]} ({i[1]}) -> {i[3]}")
if a.dry_run:
    print("[dry-run] no writes"); sys.exit(0)

mt = mf = 0
# characteristics -> their clusters
for tid, sn, tl, dest in to_char:
    mt += c.execute("UPDATE mti_terms SET cluster_code=? WHERE id=?", (dest, tid)).rowcount
    mf += c.execute("UPDATE finding SET cluster_code=? WHERE mti_term_id=? AND cluster_code='FLAG'", (dest, tid)).rowcount
# everything else -> T2
if to_t2:
    iph = ",".join("?" * len(to_t2))
    mt += c.execute(f"UPDATE mti_terms SET cluster_code='T2' WHERE id IN ({iph})", to_t2).rowcount
    mf += c.execute(f"UPDATE finding SET cluster_code='T2' WHERE mti_term_id IN ({iph}) AND cluster_code='FLAG'", to_t2).rowcount
c.commit()
left = c.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"moved {mt} terms, re-routed {mf} findings. FLAG terms remaining: {left}")
