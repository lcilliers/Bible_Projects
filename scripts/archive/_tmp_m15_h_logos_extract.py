"""Extract M15-H (Logos) terms, VCGs+verses, and findings to a single .md.
Read-only — for the researcher to author M15-H's core_description."""
import sqlite3, sys, os
from collections import defaultdict
from datetime import datetime
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

SG_CODE = "M15-H"
sg = conn.execute("SELECT * FROM cluster_subgroup WHERE subgroup_code=?", (SG_CODE,)).fetchone()
sg = dict(sg)
sg_id = sg["id"]

lines = []
def w(s=""): lines.append(s)

w(f"# {SG_CODE} (Logos) — review extract")
w(f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} — for authoring core_description._")
w()
w(f"**Sub-group row:**")
for k in ("subgroup_code","label","core_description","status","version","sort_order","notes","last_updated_date"):
    val = sg.get(k)
    if val in (None, "", 0) and k != "sort_order":
        val = "_(empty)_"
    w(f"- `{k}` : {val}")
w()
w("---")
w()

# Terms
w("## Terms placed in M15-H")
w()
terms = conn.execute("""
    SELECT mt.strongs_number, mt.language, mt.transliteration, mt.gloss,
           mt.owning_word, mt.anchor_note, mt.status, mts.placement_note
      FROM mti_term_subgroup mts
      JOIN mti_terms mt ON mt.id=mts.mti_term_id
     WHERE mts.cluster_subgroup_id=? AND COALESCE(mts.delete_flagged,0)=0
       AND COALESCE(mt.delete_flagged,0)=0
     ORDER BY mt.language DESC, mt.strongs_number
""", (sg_id,)).fetchall()
if not terms:
    w("_No terms placed yet._")
else:
    w("| Strong's | H/G | Translit. | Gloss | Owning word | Status | Anchor note | Placement note |")
    w("|---|---|---|---|---|---|---|---|")
    for t in terms:
        lang = (t["language"] or "").lower()
        ld = "H" if lang.startswith("h") else ("G" if lang.startswith("g") else "")
        w(f"| {t['strongs_number']} | {ld} | {t['transliteration'] or ''} | "
          f"{(t['gloss'] or '')[:60]} | {t['owning_word'] or ''} | {t['status'] or ''} | "
          f"{(t['anchor_note'] or '')[:60]} | {(t['placement_note'] or '')[:60]} |")
w()
w("---")
w()

# VCGs + verses (anchors first, then full verse population)
w("## Meaning groups (VCGs) and verses in M15-H")
w()
vcgs = conn.execute("""
    SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description
      FROM verse_context_group vcg
      JOIN verse_context vc ON vc.group_id=vcg.id
     WHERE vc.cluster_subgroup_id=?
       AND vcg.group_code LIKE 'M15-%-VCG%'
       AND COALESCE(vcg.delete_flagged,0)=0
       AND COALESCE(vc.delete_flagged,0)=0
     ORDER BY vcg.group_code
""", (sg_id,)).fetchall()

for vcg in vcgs:
    w(f"### {vcg['group_code']}")
    w()
    w(f"**Context description:**")
    w(f"> {vcg['context_description'] or '_(empty)_'}")
    w()
    # Anchors
    anchors = conn.execute("""
        SELECT vc.is_anchor, vc.analysis_note, vc.notes,
               vr.reference, vr.verse_text,
               mt.strongs_number, mt.transliteration, mt.language
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE vc.group_id=? AND COALESCE(vc.delete_flagged,0)=0
         ORDER BY vc.is_anchor DESC, vr.book_id, vr.chapter, vr.verse_num
    """, (vcg["id"],)).fetchall()
    anchor_rows = [a for a in anchors if a["is_anchor"]]
    other_rows = [a for a in anchors if not a["is_anchor"]]
    if anchor_rows:
        w("**Anchor verses:**")
        w()
        for a in anchor_rows:
            w(f"- **{a['reference']}** ({a['strongs_number']} {a['transliteration']})")
            w(f"  > {(a['verse_text'] or '').strip()}")
            if a["analysis_note"]:
                w(f"  _Meaning here:_ {a['analysis_note']}")
            w()
    if other_rows:
        w(f"**Other verses ({len(other_rows)}):**")
        w()
        for a in other_rows:
            note = ""
            if a["analysis_note"]:
                note = f" — {a['analysis_note'][:80]}"
            w(f"- {a['reference']} ({a['strongs_number']} {a['transliteration']}){note}")
            w(f"  > {(a['verse_text'] or '').strip()[:200]}")
        w()
    w("---")
    w()

# Findings
w("## Findings in M15-H (by tier)")
w()
findings = conn.execute("""
    SELECT cf.finding_status, cf.finding_text,
           q.question_code, q.tier, q.section, q.component_title, q.question_text
      FROM cluster_finding cf
      JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
     WHERE cf.cluster_subgroup_id=? AND COALESCE(cf.delete_flagged,0)=0
     ORDER BY q.tier, q.question_code
""", (sg_id,)).fetchall()

by_tier = defaultdict(list)
for f in findings:
    by_tier[f["tier"]].append(dict(f))

if not findings:
    w("_No findings recorded for M15-H._")
else:
    for tier in sorted(by_tier.keys()):
        flist = by_tier[tier]
        w(f"### {tier} — {len(flist)} findings")
        w()
        by_section = defaultdict(list)
        for f in flist:
            by_section[f["section"] or ""].append(f)
        for section, items in by_section.items():
            w(f"**{section}**")
            w()
            for f in items:
                status = f["finding_status"]
                badge = "_(silent)_" if status == "silent" else ("_(gap)_" if status == "gap" else "")
                qtext = (f["question_text"] or "")[:140]
                w(f"- *{f['question_code']}* {badge} — _{qtext}_")
                w(f"  → {f['finding_text'].strip()}")
            w()

w()
w("---")
w()
w(f"**Counts:** terms={len(terms)} · VCGs={len(vcgs)} · findings={len(findings)}")

out = "Sessions/Session_Clusters/M15/wa-cluster-M15-H-logos-review-v1-20260512.md"
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Wrote: {out}")
print(f"Size:  {os.path.getsize(out):,} bytes")
print(f"Terms={len(terms)}  VCGs={len(vcgs)}  Findings={len(findings)}")
conn.close()
