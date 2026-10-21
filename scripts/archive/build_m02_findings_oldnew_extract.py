"""build_m02_findings_oldnew_extract.py — emit two comparison MDs for AI-Chat assessment of M02 findings:
  (1) OLD findings (DB cluster_finding, 2026-05-16) — ordered by tier question, all rows per question
      (consolidated + per-characteristic, the 6-characteristic model ids 71-76).
  (2) NEW findings (Sessions-v2/M02-Anger/findings/, 2026-06-19, NOT yet in DB) — the 7 per-characteristic
      tier analyses (latest version each: c1-c4 v1_1, c5-c7 v1_0), re-ordered by tier question with each
      characteristic's answer grouped under the question; PLUS the cluster-wide synthesis findings appended.

Read-only. Canonical question order = wa_obs_question_catalogue 173-spine (126 active + 47 refit-folded),
numeric code sort. The NEW files answer the 126 current catalogue; folded questions get no new answer.
"""
import glob, os, re, sqlite3
DB = os.path.join("database", "bible_research.db")
NEW_DIR = "Sessions-v2/M02-Anger/findings"
OUT_OLD = f"{NEW_DIR}/WA-m02-findings-OLD-dbexport-bytier-v1-20260619.md"
OUT_NEW = f"{NEW_DIR}/WA-m02-findings-NEW-merged-bytier-v1-20260619.md"
CLUSTER_FINDINGS_FILE = f"{NEW_DIR}/wa-m02-cluster-findings-v1_0-20260619.md"

# the 7 new characteristics: filename-slug -> display label (in c-order)
NEW_CHARS = [
    ("c1", "C1 — Human kindled / burning anger"),
    ("c2", "C2 — Divine wrath"),
    ("c3", "C3 — Provoking to anger"),
    ("c4", "C4 — Jealousy / zeal"),
    ("c5", "C5 — Indignation"),
    ("c6", "C6 — Strife / quarrel"),
    ("c7", "C7 — Bitterness"),
]


def _codekey(code):
    m = re.match(r"T(\d+)\.(\d+)\.(\d+)", code or "")
    return tuple(int(g) for g in m.groups()) if m else (99, 99, 99)


def question_order(c):
    rows = c.execute("""SELECT obs_id, question_code, tier, question_text, deleted
        FROM wa_obs_question_catalogue
        WHERE tier IS NOT NULL AND (COALESCE(deleted,0)=0 OR review_note LIKE 'folded_into=%')""").fetchall()
    return sorted(rows, key=lambda r: _codekey(r["question_code"]))


def latest_file(slug):
    cands = sorted(glob.glob(f"{NEW_DIR}/wa-m02-{slug}-*-tieranalysis-v*-20260619.md"))
    return cands[-1] if cands else None  # v1_1 sorts after v1_0


def parse_new(slug):
    """parse a characteristic tier file -> {question_code: answer_text}"""
    f = latest_file(slug)
    if not f:
        return {}, None
    t = open(f, encoding="utf-8").read()
    ans = {}
    # markers like:  **T0.1.1** — answer text...  (until next **T#  / ## heading / --- / Evidence Base)
    for m in re.finditer(r"\*\*(T\d[\w.]*)\*\*\s*[—-]\s*(.*?)(?=\n\*\*T\d|\n## |\n---|\Z)",
                         t, re.S):
        ans[m.group(1)] = re.sub(r"\s*\n\s*", " ", m.group(2)).strip()
    return ans, os.path.basename(f)


def build_old(c, qorder):
    L = ["# M02 OLD findings — DB export (cluster_finding), ordered by tier question — v1 · 2026-06-19", "",
         "> Source: `cluster_finding` (cluster_code=M02), from `WA-M02-consolidated-findings-v1-20260516` "
         "(6-characteristic model, ids 71-76). Per question: consolidated row + one per characteristic. For AI-Chat "
         "old/new comparison. 47 questions carry `[refit: question now folded]`.", ""]
    cur_tier = None; nfind = 0
    for q in qorder:
        rows = c.execute("""SELECT cf.characteristic_id, ch.short_name, cf.finding_status, cf.finding_text
            FROM cluster_finding cf LEFT JOIN characteristic ch ON ch.id=cf.characteristic_id
            WHERE cf.cluster_code='M02' AND cf.obs_id=? AND COALESCE(cf.delete_flagged,0)=0
            ORDER BY (cf.characteristic_id IS NOT NULL), cf.characteristic_id""", (q["obs_id"],)).fetchall()
        if q["tier"] != cur_tier:
            cur_tier = q["tier"]; L += ["", f"# {cur_tier}", ""]
        folded = " `[refit: question now folded]`" if q["deleted"] else ""
        L += [f"## {q['question_code']} — {q['question_text']}{folded}", ""]
        if not rows:
            L += ["_(no old finding rows)_", ""]; continue
        for r in rows:
            nfind += 1
            tag = "**[consolidated — whole cluster]**" if r["characteristic_id"] is None \
                else f"**[char {r['characteristic_id']} · {r['short_name']}]**"
            L += [f"- {tag} {r['finding_text']}", ""]
    return "\n".join(L), nfind


def build_new(qorder):
    parsed = {}; srcs = []
    for slug, label in NEW_CHARS:
        ans, src = parse_new(slug)
        parsed[slug] = ans
        srcs.append(f"{label}: {src or 'MISSING'}")
    L = ["# M02 NEW findings — merged, ordered by tier question (NOT yet in DB) — v1 · 2026-06-19", "",
         "> Source: the 7 per-characteristic tier analyses in `Sessions-v2/M02-Anger/findings/` (latest version "
         "each), authored 2026-06-19 on the 126-question current catalogue (7-characteristic c1–c7 model). Merged "
         "in tier-question order; each question shows every characteristic that answers it. Cluster-wide synthesis "
         "findings appended at the end. 47 refit-folded questions carry `[refit: question now folded]` and have no "
         "new per-characteristic answer (the new work used the 126-question catalogue).", "",
         "**Source files (right versions):**"] + [f"- {s}" for s in srcs] + [""]
    cur_tier = None; nans = 0
    for q in qorder:
        if q["tier"] != cur_tier:
            cur_tier = q["tier"]; L += ["", f"# {cur_tier}", ""]
        folded = " `[refit: question now folded]`" if q["deleted"] else ""
        code = q["question_code"]
        L += [f"## {code} — {q['question_text']}{folded}", ""]
        any_ans = False
        for slug, label in NEW_CHARS:
            if code in parsed[slug]:
                any_ans = True; nans += 1
                L += [f"- **[{label}]** {parsed[slug][code]}", ""]
        if not any_ans:
            L += ["_(no new per-characteristic answer for this code)_", ""]
    # append the cluster-wide synthesis findings verbatim
    L += ["", "---", "", "# Cluster-wide synthesis findings (M02)", "",
          "> Verbatim from `wa-m02-cluster-findings-v1_0-20260619.md` — cross-characteristic synthesis "
          "(F-points), organised by phenomenon not by tier.", ""]
    if os.path.exists(CLUSTER_FINDINGS_FILE):
        cf = open(CLUSTER_FINDINGS_FILE, encoding="utf-8").read()
        cf = cf.split("\n---\n", 1)[-1] if "\n---\n" in cf else cf  # drop ONLY the front-matter header block
        L.append(cf.strip())
    return "\n".join(L), nans, {slug: set(parsed[slug]) for slug, _ in NEW_CHARS}


def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    qorder = question_order(c)
    old_md, n_old = build_old(c, qorder)
    new_md, n_new, newsets = build_new(qorder)
    open(OUT_OLD, "w", encoding="utf-8").write(old_md)
    open(OUT_NEW, "w", encoding="utf-8").write(new_md)
    print(f"questions in spine: {len(qorder)} (126 active + 47 folded)")
    print(f"OLD: {n_old} finding rows -> {OUT_OLD}")
    print(f"NEW: {n_new} per-characteristic answers + cluster synthesis -> {OUT_NEW}")
    for slug, label in NEW_CHARS:
        print(f"   {slug}: {len(newsets[slug])} question-answers parsed")


if __name__ == "__main__":
    main()
