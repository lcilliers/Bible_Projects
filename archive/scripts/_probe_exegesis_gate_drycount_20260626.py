"""_probe_exegesis_gate_drycount_20260626.py — READ-ONLY dry-run.
Runs the tuned VE engine derive() over a cluster (default M12) or the whole DB and counts how many
VERSES would be GATED by the L1.5 Logos exegesis gate.

Mechanical gate triggers the engine CAN detect (a lower bound — figurative/theologically-loaded are
interpretive and surface only in the read, so they are NOT counted here):
  - distributed-movement  : any unit emits  isolable=no  (verse opens with causal/coord conj → read WITH prev)
  - heavy-UNRESOLVED      : count of UNRESOLVED / pending-read values across the verse's units

No DB writes. Usage:
  python scripts/_probe_exegesis_gate_drycount_20260626.py            # M12
  python scripts/_probe_exegesis_gate_drycount_20260626.py --all      # whole DB
"""
import sys, os, sqlite3, time
sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding="utf-8")
import importlib.util
spec = importlib.util.spec_from_file_location("ve2", os.path.join(os.path.dirname(__file__), "_ve_engine_v2.py"))
ve2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(ve2)

DB = os.path.join("database", "bible_research.db")
ALL = "--all" in sys.argv

conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
cur = conn.cursor()
step = ve2.LexDB(cur)

clause = "" if ALL else "AND m.cluster_code='M12'"
units_rows = cur.execute(f"""
    SELECT vc.id vcid, vr.transliteration translit, m.gloss gloss, m.strongs_number strong,
           m.cluster_code cluster, vr.reference ref, vr.target_word tw
    FROM verse_context vc
    JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
    JOIN mti_terms m ON m.id=vc.mti_term_id
    WHERE COALESCE(vc.delete_flagged,0)=0 {clause}
    ORDER BY vr.reference""").fetchall()

# group units by reference; cache measure layer + coterms per verse
by_ref = {}
for u in units_rows:
    by_ref.setdefault(u["ref"], []).append(u)

t0 = time.time()
verse_stat = {}   # ref -> {isolable_no:bool, unresolved:int, units:int}
n_units = 0
for ref, urows in by_ref.items():
    vrow = cur.execute("SELECT id FROM verse WHERE reference=?", (ref,)).fetchone()
    words = ve2.load_words(cur, vrow["id"]) if vrow else []
    coterms_all = cur.execute("""
        SELECT DISTINCT vr.transliteration tr, m.gloss gl, m.cluster_code cc, m.strongs_number st
        FROM verse_context vc2
        JOIN wa_verse_records vr ON vr.id=vc2.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        JOIN mti_terms m ON m.id=vc2.mti_term_id
        WHERE vr.reference=? AND COALESCE(vc2.delete_flagged,0)=0""", (ref,)).fetchall()
    iso_no = False; unres = 0
    for u in urows:
        n_units += 1
        unit = dict(u)
        unit["coterms"] = [(c["tr"], c["gl"], c["cc"], c["st"]) for c in coterms_all if c["st"] != u["strong"]]
        try:
            items = ve2.derive(unit, words, step)
        except Exception as e:
            verse_stat.setdefault(ref, {"iso": False, "unres": 0, "units": 0, "err": str(e)})
            continue
        for (it, v, _c) in items:
            if it == "isolable" and v == "no":
                iso_no = True
            if isinstance(v, str) and ("UNRESOLVED" in v or v == "pending-read"):
                unres += 1
    s = verse_stat.setdefault(ref, {"iso": False, "unres": 0, "units": 0})
    s["iso"] = s["iso"] or iso_no
    s["unres"] += unres
    s["units"] += len(urows)
dt = time.time() - t0

verses = len(verse_stat)
iso_n = sum(1 for s in verse_stat.values() if s["iso"])
u_ge1 = sum(1 for s in verse_stat.values() if s["unres"] >= 1)
u_ge2 = sum(1 for s in verse_stat.values() if s["unres"] >= 2)
u_ge3 = sum(1 for s in verse_stat.values() if s["unres"] >= 3)
gated_iso_or_u2 = sum(1 for s in verse_stat.values() if s["iso"] or s["unres"] >= 2)
errs = sum(1 for s in verse_stat.values() if s.get("err"))

scope = "ALL CLUSTERS" if ALL else "M12 (Purity)"
print(f"=== Exegesis-gate dry-count · {scope} ===")
print(f"units processed      : {n_units}")
print(f"distinct verses      : {verses}")
print(f"derive() errors      : {errs}")
print(f"runtime              : {dt:.1f}s  ({dt/max(n_units,1):.3f}s/unit)")
print("-- mechanical gate triggers (verse-level) --")
print(f"distributed (isolable=no)      : {iso_n:5d}  ({100*iso_n/verses:.1f}%)")
print(f"UNRESOLVED >=1 field           : {u_ge1:5d}  ({100*u_ge1/verses:.1f}%)")
print(f"UNRESOLVED >=2 fields          : {u_ge2:5d}  ({100*u_ge2/verses:.1f}%)")
print(f"UNRESOLVED >=3 fields          : {u_ge3:5d}  ({100*u_ge3/verses:.1f}%)")
print(f"GATED (isolable=no OR UNRES>=2): {gated_iso_or_u2:5d}  ({100*gated_iso_or_u2/verses:.1f}%)")
