"""build_m01_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M01 findings:
  (1) OLD findings (in DB cluster_finding, 2026-05-16) — ordered by tier question, all rows per question
      (consolidated + per-subgroup), each labelled.
  (2) NEW findings (Sessions-v2/M01-Fear/findings/, 2026-06-18, NOT yet in DB) — one finding per question,
      ordered by the same tier-question spine.

Read-only. Canonical question order = wa_obs_question_catalogue (tier, component_code, prompt_seq), ALL 173
codes incl. refit-soft-deleted (both finding sets were authored on the 173 spine).
"""
import glob, os, re, sqlite3
DB = os.path.join("database", "bible_research.db")
NEW_DIR = "Sessions-v2/M01-Fear/findings"
OUT_OLD = "Sessions-v2/M01-Fear/findings/WA-m01-findings-OLD-dbexport-bytier-v1-20260619.md"
OUT_NEW = "Sessions-v2/M01-Fear/findings/WA-m01-findings-NEW-merged-bytier-v1-20260619.md"


def _codekey(code):
    # "T2.10.1" -> (2, 10, 1) so components/sub-questions sort numerically (T2.9 before T2.10)
    m = re.match(r"T(\d+)\.(\d+)\.(\d+)", code or "")
    return tuple(int(g) for g in m.groups()) if m else (99, 99, 99)


def question_order(c):
    # the 173-question spine the findings were authored on = currently-active (126) + refit-folded (47);
    # excludes the 16 earlier DROP-list codes (deleted with no fold note).
    rows = c.execute("""SELECT obs_id, question_code, tier, component_code, component_title, question_text, deleted
        FROM wa_obs_question_catalogue
        WHERE tier IS NOT NULL
          AND (COALESCE(deleted,0)=0 OR review_note LIKE 'folded_into=%')""").fetchall()
    return sorted(rows, key=lambda r: _codekey(r["question_code"]))


def build_old(c, qorder):
    L = ["# M01 OLD findings — DB export (cluster_finding), ordered by tier question — v1 · 2026-06-19", "",
         "> Source: `cluster_finding` (cluster_code=M01), from `WA-M01-consolidated-findings-v1-20260516`. "
         "Per question: a consolidated row (whole-cluster) + one row per sub-group (M01-A…G, the 7-characteristic "
         "model). For AI-Chat old/new comparison. 47 questions carry `[refit: question now folded]`.", ""]
    cur_tier = None
    nfind = 0
    for q in qorder:
        rows = c.execute("""SELECT cf.characteristic_id, ch.short_name, cf.cluster_subgroup_id,
                   sg.subgroup_code, sg.label, cf.finding_status, cf.finding_text
            FROM cluster_finding cf
            LEFT JOIN characteristic ch ON ch.id = cf.characteristic_id
            LEFT JOIN cluster_subgroup sg ON sg.id = cf.cluster_subgroup_id
            WHERE cf.cluster_code='M01' AND cf.obs_id=? AND COALESCE(cf.delete_flagged,0)=0
            ORDER BY (cf.characteristic_id IS NOT NULL), cf.characteristic_id""", (q["obs_id"],)).fetchall()
        if q["tier"] != cur_tier:
            cur_tier = q["tier"]; L += ["", f"# {cur_tier}", ""]
        folded = " `[refit: question now folded]`" if q["deleted"] else ""
        L += [f"## {q['question_code']} — {q['question_text']}{folded}", ""]
        if not rows:
            L += ["_(no old finding rows)_", ""]; continue
        for r in rows:
            nfind += 1
            if r["characteristic_id"] is None:
                tag = "**[consolidated — whole cluster]**"
            else:
                tag = f"**[{r['subgroup_code'] or r['characteristic_id']} · {r['short_name'] or r['label']}]**"
            L += [f"- {tag} {r['finding_text']}", ""]
    return "\n".join(L), nfind


def build_new(qorder):
    # parse each tier file into {question_code: block-text}
    blocks = {}
    for f in sorted(glob.glob(f"{NEW_DIR}/WA-m01-findings-t*-v1_0-2026-06-18.md")):
        t = open(f, encoding="utf-8").read()
        # split on level-2 question headings "## T#.# — ..."
        parts = re.split(r"(?m)^## (T\d[\w.]*) — ", t)
        # parts: [pre, code1, body1, code2, body2, ...]
        for i in range(1, len(parts), 2):
            code = parts[i]
            body = parts[i + 1]
            # trim trailing tier-completeness / end-of-file material at the next top-level or hr that starts a new section
            body = re.split(r"(?m)^## Tier .* completeness|^\*End of", body)[0]
            blocks[code] = body.strip()
    L = ["# M01 NEW findings — merged, ordered by tier question (NOT yet in DB) — v1 · 2026-06-19", "",
         "> Source: `Sessions-v2/M01-Fear/findings/WA-m01-findings-t0..t7-v1_0-2026-06-18.md` (authored 2026-06-18, "
         "11-characteristic c1–c11 model, one finding per question). Merged in tier-question order for AI-Chat "
         "old/new comparison. 47 questions carry `[refit: question now folded]`.", ""]
    cur_tier = None
    nfind = 0
    for q in qorder:
        if q["tier"] != cur_tier:
            cur_tier = q["tier"]; L += ["", f"# {cur_tier}", ""]
        folded = " `[refit: question now folded]`" if q["deleted"] else ""
        code = q["question_code"]
        L += [f"## {code} — {q['question_text']}{folded}", ""]
        if code in blocks:
            nfind += 1
            L += [blocks[code], ""]
        else:
            L += ["_(no new finding parsed for this code)_", ""]
    return "\n".join(L), nfind, set(blocks)


def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    qorder = question_order(c)
    old_md, n_old = build_old(c, qorder)
    new_md, n_new, new_codes = build_new(qorder)
    open(OUT_OLD, "w", encoding="utf-8").write(old_md)
    open(OUT_NEW, "w", encoding="utf-8").write(new_md)
    qcodes = {q["question_code"] for q in qorder}
    print(f"questions in spine: {len(qorder)}")
    print(f"OLD: {n_old} finding rows -> {OUT_OLD}")
    print(f"NEW: {n_new} question-findings -> {OUT_NEW}")
    missing = sorted(qcodes - new_codes)
    extra = sorted(new_codes - qcodes)
    if missing: print(f"  NEW codes missing vs spine ({len(missing)}): {missing}")
    if extra: print(f"  NEW codes not in spine ({len(extra)}): {extra}")
    if not missing and not extra: print("  NEW codes match the 173-question spine exactly.")


if __name__ == "__main__":
    main()
