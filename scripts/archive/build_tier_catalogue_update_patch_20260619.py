"""build_tier_catalogue_update_patch_20260619.py — emit the tier-catalogue refit as a reviewable JSON patch.

Source: Workflow/Tiers/wa-tier-catalogue-cc-update-v1_0-20260619.md (the executable distillation of the
v2_1 rewrite). Two operation classes over the 173 active tiered codes:
  A. TEXT-UPDATE  — 126 keep codes: set question_text to the de-biased rewritten form.
  B. SOFT-DELETE  — 47 obsolete codes: set deleted=1 + record the fold target in review_note.

Read-only on the DB (validation only). Writes the patch to Sessions/Patches/. Apply via
apply_session_patch.py (--dry-run first; researcher reviews before --live), per GR-PROG-005/GR-PROC-004.
"""
import json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DOC = "Workflow/Tiers/wa-tier-catalogue-cc-update-v1_0-20260619.md"
DB = os.path.join("database", "bible_research.db")
OUT = "Sessions/Patches/wa-tier-catalogue-refit-update-v1-20260619.json"
REFIT = "tier-catalogue v2_1 refit 2026-06-19"


def parse_doc():
    doc = open(DOC, encoding="utf-8").read()
    a_region = doc.split("## Operation A")[1].split("## Operation B")[0]
    b_region = doc.split("## Operation B")[1].split("## Post-run")[0]
    A = {m.group(1): m.group(2)
         for m in re.finditer(r'^- \*\*(T\d[\w.]*)\*\*\s*→\s*"(.+)"\s*$', a_region, re.M)}
    B = {}  # code -> (primary, reason)
    for m in re.finditer(r'^\|\s*(T\d[\w.]*)\s*\|\s*(T\d[\w.]*)\s*\|\s*(.+?)\s*\|', b_region, re.M):
        B[m.group(1)] = (m.group(2), m.group(3))
    return A, B


def validate(A, B):
    assert len(A) == 126, f"Operation A parsed {len(A)}, expected 126"
    assert len(B) == 47, f"Operation B parsed {len(B)}, expected 47"
    assert not (set(A) & set(B)), f"A/B overlap: {set(A) & set(B)}"
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    active = {r["question_code"] for r in c.execute(
        "SELECT question_code FROM wa_obs_question_catalogue WHERE deleted=0 AND tier IS NOT NULL")}
    allcodes = set(A) | set(B)
    assert allcodes == active, (f"code set != DB active. missing-from-doc={sorted(active-allcodes)} "
                                f"extra-in-doc={sorted(allcodes-active)}")
    bad = {k: v for k, (v, _) in B.items() if v not in A}
    assert not bad, f"fold-targets not in keep-set: {bad}"
    # text-updates must actually change the stored text (else no-op); report (not fatal — some may match)
    cur = {r["question_code"]: r["question_text"] for r in c.execute(
        "SELECT question_code, question_text FROM wa_obs_question_catalogue WHERE deleted=0 AND tier IS NOT NULL")}
    noop = [code for code, txt in A.items() if cur.get(code) == txt]
    return noop


def build(A, B):
    ops = []
    n = 0
    for code in sorted(A):
        n += 1
        ops.append({"op_id": f"OP-{n:03d}", "operation": "update", "table": "wa_obs_question_catalogue",
                    "match": {"question_code": code}, "set": {"question_text": A[code]}})
    for code in sorted(B):
        n += 1
        primary, reason = B[code]
        ops.append({"op_id": f"OP-{n:03d}", "operation": "update", "table": "wa_obs_question_catalogue",
                    "match": {"question_code": code},
                    "set": {"deleted": 1, "review_note": f"folded_into={primary} · {REFIT} · {reason}"}})
    patch = {
        "_patch_meta": {
            "patch_id": "wa-tier-catalogue-refit-update-v1-20260619",
            "registry_id": None, "word": "global", "produced_date": "20260619",
            "produced_by": "wa-tier-catalogue-cc-update-v1_0-20260619 (companion: v2_1 rewrite)",
            "patch_type": "CATALOGUE_UPDATE", "session_b_status": None,
            "description": (f"Tier-catalogue refit: {len(A)} keep-code question_text rewrites (de-biased v2_1) "
                            f"+ {len(B)} obsolete-code soft-deletes (deleted=1, fold target in review_note). "
                            "No inserts, no renumber, no hard delete. Operates on the 173 active tiered codes; "
                            "post-run active tiered = 126."),
        },
        "operations": ops,
        "_patch_summary": {"text_updates": len(A), "soft_deletes": len(B), "total_ops": len(ops),
                           "expected_post_run_active_tiered": 126},
    }
    return patch


def main():
    A, B = parse_doc()
    noop = validate(A, B)
    patch = build(A, B)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(patch, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"WROTE {OUT}")
    print(f"  text-updates: {len(A)} · soft-deletes: {len(B)} · total ops: {len(patch['operations'])}")
    if noop:
        print(f"  NOTE: {len(noop)} text-update(s) already match stored text (no-op on apply): {noop}")
    else:
        print("  all 126 text-updates change the stored text.")


if __name__ == "__main__":
    main()
