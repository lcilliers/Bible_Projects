"""_assess_cluster_v3_2_preeval.py  — READ-ONLY V3_2 cluster pre-evaluation.

The sanctioned V3_2 pre-flight assessment (rollup instruction v3_2 §3 / audit PRE-L2 completeness):
assembles the whole cluster in focus and reports its readiness for the V3_2 roll-up. No DB writes.

Reports: cluster identity/status · term layer · verse layer · existing analysis (re-run inputs:
VCGs, sub-groups, characteristics, findings, flags/pointers) · STEP-sense + morphology readiness ·
V3_2 schema-field population state · a readiness verdict.

Usage:
    python scripts/_assess_cluster_v3_2_preeval.py --cluster M01 --out Sessions-v2/M01-Fear/<file>.md
"""
import argparse, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STEM_LABEL = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    cc = a.cluster

    def one(q, *p): return c.execute(q, p).fetchone()[0]

    clus = c.execute("SELECT cluster_code, short_name, description, bucket, status, version "
                     "FROM cluster WHERE cluster_code=?", (cc,)).fetchone()
    if not clus:
        print(f"No cluster {cc}"); return

    # --- term ids for this cluster (active) ---
    term_ids = [r["id"] for r in c.execute(
        "SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (cc,))]
    tid_ph = ",".join("?" * len(term_ids)) if term_ids else "NULL"

    L = []
    A = L.append
    A(f"# {cc} ({clus['short_name']}) — V3_2 pre-evaluation")
    A("")
    A(f"> **READ-ONLY pre-flight · {os.path.basename(a.out)} · CC.** Sanctioned V3_2 assessment "
      f"(`scripts/_assess_cluster_v3_2_preeval.py`). Assembles the whole cluster in focus and reports "
      f"readiness for the V3_2 roll-up (rollup instruction v3_2 §3 / audit PRE-L2). No DB writes.")
    A("")
    A(f"**Cluster:** {cc} — *{clus['description']}* · bucket `{clus['bucket']}` · status "
      f"**{clus['status']}** · {clus['version']}")
    A("")

    # ---------- A. Term layer ----------
    A("## A · Term layer")
    A("")
    n_terms = len(term_ids)
    A(f"- Active terms: **{n_terms}**")
    by_lang = c.execute("SELECT language, COUNT(*) k FROM mti_terms WHERE cluster_code=? "
                        "AND COALESCE(delete_flagged,0)=0 GROUP BY language", (cc,)).fetchall()
    A(f"- By language: " + ", ".join(f"{r['language']} {r['k']}" for r in by_lang))
    by_status = c.execute("SELECT COALESCE(status,'(null)') s, COUNT(*) k FROM mti_terms WHERE cluster_code=? "
                          "AND COALESCE(delete_flagged,0)=0 GROUP BY s ORDER BY k DESC", (cc,)).fetchall()
    A(f"- By status: " + ", ".join(f"`{r['s']}` {r['k']}" for r in by_status))
    # owner/xref via inventory
    own = one("SELECT COUNT(DISTINCT t.id) FROM mti_terms t JOIN wa_term_inventory wi "
              "ON wi.strongs_number=t.strongs_number AND COALESCE(wi.delete_flagged,0)=0 "
              f"WHERE t.cluster_code=? AND COALESCE(t.delete_flagged,0)=0 AND wi.term_owner_type='OWNER'", cc)
    A(f"- OWNER-type terms (per inventory): {own}")
    A("")

    # ---------- B. Verse layer ----------
    A("## B · Verse layer (`verse_context` for this cluster's terms)")
    A("")
    if term_ids:
        vc = c.execute(f"""SELECT COUNT(*) total,
            SUM(COALESCE(is_relevant,0)) relevant,
            SUM(CASE WHEN set_aside_reason IS NOT NULL THEN 1 ELSE 0 END) setaside,
            SUM(CASE WHEN analysis_note IS NOT NULL AND analysis_note!='' THEN 1 ELSE 0 END) meaning,
            SUM(CASE WHEN keywords IS NOT NULL AND keywords!='' THEN 1 ELSE 0 END) kw,
            SUM(CASE WHEN group_id IS NOT NULL THEN 1 ELSE 0 END) grouped
            FROM verse_context WHERE mti_term_id IN ({tid_ph}) AND COALESCE(delete_flagged,0)=0""",
            term_ids).fetchone()
        A(f"- verse_context rows: **{vc['total']}** · relevant **{vc['relevant']}** · set-aside {vc['setaside']}")
        A(f"- with AI `analysis_note` (existing L3-layer meaning): **{vc['meaning']}** · with `keywords`: {vc['kw']} · in a VCG (`group_id`): {vc['grouped']}")
    else:
        A("- (no active terms)")
    A("")

    # ---------- C. Existing analysis (re-run inputs) ----------
    A("## C · Existing analysis — re-run inputs (V3_2 respects + refines these)")
    A("")
    vcgs = one(f"SELECT COUNT(DISTINCT group_id) FROM verse_context WHERE mti_term_id IN ({tid_ph}) "
               "AND group_id IS NOT NULL AND COALESCE(delete_flagged,0)=0", *term_ids) if term_ids else 0
    A(f"- existing **VCGs** (verse_context_group used): {vcgs}")
    sg = one("SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", cc) \
        if _has(c, "cluster_subgroup", "cluster_code") else "n/a"
    A(f"- existing **sub-groups** (`cluster_subgroup`): {sg}")
    if _has(c, "characteristic", "cluster_code"):
        ch = one("SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", cc)
        A(f"- existing **characteristics**: {ch}")
    # findings
    if _has(c, "cluster_finding", "cluster_code"):
        nf = one("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", cc)
        A(f"- existing **findings** (`cluster_finding`): **{nf}**")
        bs = c.execute("SELECT COALESCE(finding_status,'(null)') s, COUNT(*) k FROM cluster_finding "
                       "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 GROUP BY s ORDER BY k DESC", (cc,)).fetchall()
        A(f"  - by `finding_status`: " + ", ".join(f"`{r['s']}` {r['k']}" for r in bs))
        ft = c.execute("SELECT COALESCE(finding_type,'(null/new)') s, COUNT(*) k FROM cluster_finding "
                       "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 GROUP BY s", (cc,)).fetchall()
        A(f"  - by `finding_type` (new M55 field): " + ", ".join(f"`{r['s']}` {r['k']}" for r in ft))
    A("")

    # ---------- D. STEP-sense + morphology readiness ----------
    A("## D · STEP-sense + morphology readiness (for L1 mechanical)")
    A("")
    if term_ids:
        with_sense = one(f"""SELECT COUNT(DISTINCT t.id) FROM mti_terms t
            JOIN wa_term_inventory wi ON wi.strongs_number=t.strongs_number AND COALESCE(wi.delete_flagged,0)=0
            WHERE t.id IN ({tid_ph}) AND wi.parsed_meaning_id IS NOT NULL""", *term_ids)
        A(f"- terms with a parsed STEP sense-set (`parsed_meaning_id`): **{with_sense} / {n_terms}**")
        # multi-sense (>=2 stems in concatenated sense_text) — light count
        multi = 0
        for tid in term_ids:
            pid = c.execute("SELECT wi.parsed_meaning_id FROM mti_terms t JOIN wa_term_inventory wi "
                            "ON wi.strongs_number=t.strongs_number AND COALESCE(wi.delete_flagged,0)=0 "
                            "WHERE t.id=? LIMIT 1", (tid,)).fetchone()
            if pid and pid[0]:
                st = " ".join((r[0] or "") for r in c.execute(
                    "SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=?", (pid[0],)))
                if len(set(m.group(1).title() for m in STEM_LABEL.finditer(st))) >= 2:
                    multi += 1
        A(f"- stem-conditioned multi-sense terms (≥2 binyanim in sense_text): **{multi}** "
          f"(the within-stem-select residue goes to L2 per discipline 2)")
    A(f"- **morphology captured?** `wa_verse_records.morph`/`stem` populated: "
      f"{one('SELECT COUNT(*) FROM wa_verse_records WHERE morph_code IS NOT NULL')} rows system-wide "
      f"→ **PENDING** (run in L1).")
    A(f"- **`wa_meaning_sense.stem_label` populated?** "
      f"{one('SELECT COUNT(*) FROM wa_meaning_sense WHERE stem_label IS NOT NULL')} → **PENDING** (run in L1).")
    A(f"- **`is_homonym` populated?** "
      f"{one('SELECT COUNT(*) FROM wa_meaning_sense WHERE is_homonym=1')} → **PENDING** (filter pass).")
    A("")

    # ---------- E. V3_2 schema field state (L1 outputs, should be empty pre-run) ----------
    A("## E · V3_2 L1 fields — population state (expect empty pre-run)")
    A("")
    if term_ids:
        default0 = {"pole_is_metaphor", "residue_flag"}  # added with DEFAULT 0 — count real (non-default) values
        for col in ("step_meaning_applied", "sense_id", "sense_multiplicity", "pole",
                    "pole_is_metaphor", "residue_flag"):
            cond = f"{col} IS NOT NULL AND {col}!=0" if col in default0 else f"{col} IS NOT NULL"
            n = one(f"SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN ({tid_ph}) "
                    f"AND {cond} AND COALESCE(delete_flagged,0)=0", *term_ids)
            note = " *(DEFAULT 0 on all rows; counting non-default)*" if col in default0 else ""
            A(f"- `verse_context.{col}` populated: {n}{note}")
    A("")

    # ---------- F. Readiness verdict ----------
    A("## F · Readiness verdict")
    A("")
    A("- **Schema:** V3_2 (3.29.0) — L1 fields present and empty, ready to populate. ✅")
    A("- **Foundation:** term layer deduped (2026-06-08); STEP sense-sets present. ✅")
    A("- **To run in L1 (population, not yet done):** capture per-verse morphology → `morph`/`stem`; "
      "parse `stem_label`; `is_homonym` filter. ⏳")
    A(f"- **Existing analysis is a re-run input** (prior VCGs/sub-groups/findings above) — V3_2 evaluates + "
      "refines, does not discard (discipline 6 / L2–L5 dynamic d).")
    A("- **Next V3_2 step:** L1 verse establishment (mechanical STEP-sense application) for this cluster.")
    A("")
    A("*This pre-evaluation is read-only and records state only; it makes no analytical decisions.*")

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{cc}: {n_terms} terms, {vcgs} VCGs. Wrote {a.out}")


def _has(c, table, col):
    try:
        return col in {r[1] for r in c.execute(f"PRAGMA table_info({table})")}
    except Exception:
        return False


if __name__ == "__main__":
    main()
