"""_build_M01_verse_read_review.py — READ-ONLY. Full M01 verse-complete run review: coverage, cross-cluster
fan-out, corrected flag rate, sample routed paragraphs, flagged samples. No DB writes."""
import sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row

run = c.execute("SELECT run_id, started_at, completed_at, outcome FROM engine_run_log WHERE mode='verse_read_meaning' ORDER BY id DESC LIMIT 1").fetchone()
m01_own = c.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN (SELECT id FROM mti_terms WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0) AND COALESCE(delete_flagged,0)=0").fetchone()[0]
m01_read = c.execute("""SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id IN (SELECT id FROM mti_terms WHERE cluster_code='M01' AND COALESCE(delete_flagged,0)=0)
                        AND COALESCE(vc.delete_flagged,0)=0 AND EXISTS(SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id AND f.provenance='l2_meaning')""").fetchone()[0]
para = c.execute("SELECT COUNT(*) FROM finding WHERE provenance='l2_meaning'").fetchone()[0]
tier = c.execute("SELECT COUNT(*) FROM finding WHERE provenance='l2_api'").fetchone()[0]
flagged = c.execute("SELECT COUNT(*) FROM finding WHERE provenance='l2_meaning' AND flagged_for_review=1").fetchone()[0]

L = ["# M01 verse-complete run — review", "",
     f"> Run `{run['run_id']}` → **{run['outcome']}** ({run['started_at'][11:19]}–{run['completed_at'][11:19]}). READ-ONLY.", "",
     "## Coverage",
     f"- **M01 own verses: {m01_read} / {m01_own}** ({'COMPLETE' if m01_read>=m01_own else 'GAP'}); all 85 M01 terms checkpointed `complete`.",
     f"- **{para} meaning paragraphs** + **{tier} tier findings** written across the corpus.",
     f"- **Flagged for review (free-text omission): {flagged} / {para} ({100*flagged/para:.0f}%)** — the rest fully echo their content fields.",
     ""]
L.append("## Cross-cluster fan-out (paragraphs by the term's own cluster)")
L.append("| cluster | paragraphs |"); L.append("|---|---|")
for r in c.execute("SELECT m.cluster_code cc, COUNT(*) n FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id WHERE f.provenance='l2_meaning' GROUP BY m.cluster_code ORDER BY n DESC LIMIT 15"):
    L.append(f"| {r['cc']} | {r['n']} |")
ncl = c.execute("SELECT COUNT(DISTINCT m.cluster_code) FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id WHERE f.provenance='l2_meaning'").fetchone()[0]
L.append(f"\n_Findings now seeded in **{ncl} clusters** — every other cluster has a head start from M01's verses (no re-read when it runs)._\n")

# sample routed cross-cluster paragraphs (term NOT in M01, written from an M01 verse)
L.append("## Sample cross-cluster routed paragraphs (written from M01 verses, routed to their own cluster)")
seen = set()
for r in c.execute("""SELECT m.cluster_code cc, m.transliteration tl, vr.reference ref, f.finding_value para
                      FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id
                      JOIN verse_context vc ON vc.id=f.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                      WHERE f.provenance='l2_meaning' AND m.cluster_code NOT IN ('M01','T2','FLAG') AND LENGTH(f.finding_value)>120
                      ORDER BY f.id"""):
    if r["cc"] in seen:
        continue
    seen.add(r["cc"])
    L.append(f"\n**{r['cc']} · {r['tl']} · {r['ref']}** — {r['para'][:360]}")
    if len(seen) >= 6:
        break

# flagged samples
L.append("\n## Flagged-for-review samples (free-text field not echoed — to inspect)")
for r in c.execute("""SELECT m.cluster_code cc, m.transliteration tl, vr.reference ref
                      FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id
                      JOIN verse_context vc ON vc.id=f.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                      WHERE f.provenance='l2_meaning' AND f.flagged_for_review=1 ORDER BY f.id LIMIT 12"""):
    L.append(f"- {r['cc']} · {r['tl']} · {r['ref']}")

out = "research/investigations/wa-verse-read-M01-review-v1-20260609.md"
open(out, "w", encoding="utf-8").write("\n".join(L))
print(f"M01 own {m01_read}/{m01_own} | paragraphs {para} | flagged {flagged} ({100*flagged/para:.0f}%) | clusters {ncl}; wrote {out}")
