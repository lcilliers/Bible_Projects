"""_apply_create_constitution_cluster.py — WRITES. Creates the new M47 'Constitution' cluster (the inner-being
seats & faculties: heart, soul, spirit, mind, flesh, conscience) and moves those terms out of FLAG into it,
re-routing their existing l2 findings' cluster_code too. Reversible via --undo. Researcher decision 2026-06-10
([[feedback_t2_reference_flag_reclassify]] resolved to Option A: the seats get their own home).

Usage:  python scripts/_apply_create_constitution_cluster.py [--dry-run] [--undo]
"""
import argparse, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
CODE = "M47"
NAME = "Constitution"
DESC = "Constitution: the inner-being seats and faculties (heart, soul, spirit, mind, flesh, conscience)"
# seat/faculty terms (Strong's) currently in FLAG → M47
SEATS = ["H3820A", "H3824", "G2588", "H5315G", "H7308", "G3563", "G4561", "G4893"]

ap = argparse.ArgumentParser()
ap.add_argument("--dry-run", action="store_true")
ap.add_argument("--undo", action="store_true")
a = ap.parse_args()
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
now = c.execute("SELECT strftime('%Y-%m-%dT%H:%M:%SZ','now')").fetchone()[0]
ph = ",".join("?" * len(SEATS))

if a.undo:
    n1 = c.execute(f"UPDATE mti_terms SET cluster_code='FLAG' WHERE cluster_code='{CODE}' AND strongs_number IN ({ph})", SEATS).rowcount
    n2 = c.execute(f"UPDATE finding SET cluster_code='FLAG' WHERE cluster_code='{CODE}'").rowcount
    c.execute(f"DELETE FROM cluster WHERE cluster_code='{CODE}'")
    if not a.dry_run:
        c.commit()
    print(f"{'WOULD undo' if a.dry_run else 'undid'}: terms->FLAG {n1}, findings->FLAG {n2}, dropped {CODE}")
    sys.exit(0)

terms = c.execute(f"SELECT id, strongs_number sn, transliteration tl FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0 AND strongs_number IN ({ph})", SEATS).fetchall()
print(f"{CODE} '{NAME}' — moving {len(terms)} seat/faculty terms from FLAG:")
for t in terms:
    nf = c.execute("SELECT COUNT(*) FROM finding WHERE mti_term_id=? AND provenance IN ('l2_api','l2_meaning')", (t["id"],)).fetchone()[0]
    print(f"   {t['sn']:8} {t['tl']:12} ({nf} l2 findings)")
exists = c.execute(f"SELECT 1 FROM cluster WHERE cluster_code='{CODE}'").fetchone()

if a.dry_run:
    print(f"[dry-run] would create cluster {CODE} (exists={bool(exists)}) and re-route the above terms + their findings. No writes.")
    sys.exit(0)

if not exists:
    gloss = ", ".join(f"{t['tl']} ({t['sn']})" for t in terms)
    c.execute("""INSERT INTO cluster(cluster_code, description, gloss, source, bucket, status, version, last_updated_date, short_name)
                 VALUES(?,?,?,?,?,?,?,?,?)""",
              (CODE, DESC, gloss, "flag_triage_2026-06-10", "NAMED", "Not started", "v1", now, NAME))
ids = [t["id"] for t in terms]
iph = ",".join("?" * len(ids))
n1 = c.execute(f"UPDATE mti_terms SET cluster_code='{CODE}' WHERE id IN ({iph})", ids).rowcount
n2 = c.execute(f"UPDATE finding SET cluster_code='{CODE}' WHERE mti_term_id IN ({iph}) AND cluster_code='FLAG'", ids).rowcount
c.commit()
print(f"created {CODE} '{NAME}'; moved {n1} terms FLAG->{CODE}; re-routed {n2} findings.")
left = c.execute("SELECT COUNT(DISTINCT id) FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"FLAG terms remaining: {left}")
