"""Retags the 251 existing M67 verse-reading `ib_observation` rows currently sitting under the
non-discriminating `answered-no-flag` (236) / `none` (15, never even a registered enum value)
tags, per escalation #1723 (v10-v15). `extend_tag_vocabulary_v1_20260917.py` registered the real,
close-read categories these rows actually state; this migration applies them retroactively by
pattern-matching each row's own `obs_text` (the reason is already stated in plain language --
the researcher's own point: tag exists so trends don't require re-reading every row by hand).

Deliberately conservative: only reclassifies a row when its `obs_text` unambiguously matches one
of the patterns below. Every row that doesn't match cleanly is LEFT AS-IS and counted separately
for manual review -- never guessed. Pattern precedence, checked in this order per row:

1. M0.5.9 (attestation) + wording indicating pre-NT/classical attestation -> `attested-pre-nt`
   (no rows in this dataset make the opposite NT-coinage claim, so `nt-coinage` gets 0 retags
   here -- registered for future use, not forced onto anything today).
2. M0.5.11 (alternative meaning) + "no notable divergence"/"within ... base gloss" wording ->
   `no-impact`.
3. M0.6.5 (relational) + "no other M-code" wording -> `sole-mcode-in-verse`.
4. Any question_code + explicit modifier/qualifier-of-another-word wording -> `qualifier-for-term`.
5. Remaining `tag='none'` rows (not matched above) -> `not-related-to-meaningful-word` (this was
   `none`'s actual, consistent meaning throughout -- "the sub-question's target item doesn't
   exist for this term").
6. Everything else (remaining `answered-no-flag` rows -- genuinely plain substantive answers:
   M0.1.1 naming, M0.5.1 primary-term, most D7.7.1 operation/party descriptions) is left
   untouched -- `answered-no-flag` is a legitimate value for those, not a defect.

Safe to re-run: idempotent (only touches rows still on `answered-no-flag`/`none`; already-retagged
rows are skipped).

Usage:
    python iba/app/migration/retag_answered_no_flag_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import re
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

# Order matters: negated-coinage / classical-attestation checked FIRST, since the real data
# phrases attestation as "not a NT(-period) coinage" -- a naive positive-coinage match without
# checking negation first misfires on exactly that wording (found live, fixed before applying).
ATTESTATION_NEGATED_COINAGE = re.compile(
    r"not (?:a |an )?(?:nt[- ]period |nt )?coinage|not coined in the nt", re.I)
ATTESTATION_PRE_NT = re.compile(
    r"(classical greek|from homer onward|attested (?:in|from) classical|prior to the nt|"
    r"before the nt period|well.attested classical)", re.I)
ATTESTATION_NT_COINAGE = re.compile(
    r"\bis an? nt[- ]period coinage\b|\bcoined in the nt period\b|\bnt coinage\b", re.I)
NO_IMPACT = re.compile(
    r"(no notable (?:surface )?divergence|sits (?:squarely |)within (?:its |the )?base gloss|"
    r"no notable shift)", re.I)
SOLE_MCODE = re.compile(
    r"no other m-code (?:characteristic )?(?:is present|co-occurs)", re.I)
NOT_APPLICABLE = re.compile(
    r"question (?:does not|doesn.t) apply|no .{0,20}question applicable|not applicable", re.I)
# Deliberately NOT matching the bare phrase "manner-of-action" -- found live (M0.5.2/M0.5.3
# false positives) that it also appears in unrelated grammatical-range/semantic-range answers
# describing the word's OWN general profile, not a specific instance of qualifying another word
# in this verse. Only the more specific, unambiguous phrasings below are matched.
QUALIFIER = re.compile(
    r"(adverbial qualifier|act-modifier|qualifies the earnest manner|"
    r"modifies an act\b|not itself the operation but|manner/resource applied|"
    r"intensifies (?:the manner|this)|qualifier of manner attached)", re.I)


def classify(question_code: str | None, obs_text: str) -> str | None:
    text = obs_text or ""
    if question_code == "M0.5.9":
        if NOT_APPLICABLE.search(text):
            return "not-related-to-meaningful-word"
        if ATTESTATION_NEGATED_COINAGE.search(text) or ATTESTATION_PRE_NT.search(text):
            return "attested-pre-nt"
        if ATTESTATION_NT_COINAGE.search(text):
            return "nt-coinage"
    if question_code == "M0.5.11" and NO_IMPACT.search(text):
        return "no-impact"
    if question_code == "M0.6.5" and SOLE_MCODE.search(text):
        return "sole-mcode-in-verse"
    if QUALIFIER.search(text):
        return "qualifier-for-term"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        "SELECT id, question_code, tag, obs_text FROM ib_observation "
        "WHERE tag IN ('answered-no-flag','none')").fetchall()

    plan: dict[int, str] = {}
    for r in rows:
        new_tag = classify(r["question_code"], r["obs_text"])
        if new_tag:
            plan[r["id"]] = new_tag
        elif r["tag"] == "none":
            plan[r["id"]] = "not-related-to-meaningful-word"

    by_new_tag: dict[str, int] = {}
    for t in plan.values():
        by_new_tag[t] = by_new_tag.get(t, 0) + 1
    left_untouched = len(rows) - len(plan)

    print(f"{len(rows)} candidate row(s) (answered-no-flag/none).")
    print(f"Reclassifying {len(plan)} row(s):")
    for t, n in sorted(by_new_tag.items()):
        print(f"  -> {t}: {n}")
    print(f"Left untouched (genuinely plain answered-no-flag, no confident match): "
          f"{left_untouched}")

    if args.dry_run or not plan:
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    for obs_id, new_tag in plan.items():
        conn.execute("UPDATE ib_observation SET tag=? WHERE id=?", (new_tag, obs_id))
    conn.commit()

    remaining = conn.execute(
        "SELECT COUNT(*) n FROM ib_observation WHERE tag IN ('answered-no-flag','none')"
    ).fetchone()["n"]
    print(f"Applied. Remaining answered-no-flag/none rows: {remaining} "
          f"(expected: {left_untouched} answered-no-flag, 0 none).")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
