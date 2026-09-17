"""Extends `ib_observation.tag`'s `cfg_enum` vocabulary per escalation #1723 (v11-v14) --
researcher-driven, closely-read design: "tag is not just because it is peculiar, but also a
statement of value that can be used for categorisation is filtering. ... it is not possible to
search and read the text to identify trends, and import[ant] observations, [the] tag serve[s]
this."

Live data check found `answered-no-flag` at 236/305 (77%) of all M67 verse-reading observations
and `none` at 15/305 -- and `none` was never even a registered enum value (no write-time
validation existed on `tag` at all, unlike `question_code` which was just fixed the same day).
Close-reading (not skimming) what those rows actually say surfaced real, recurring, filterable
facts that were being flattened into the two non-discriminating catch-alls:

- `qualifier-for-term`: the word functions as a MODIFIER (manner/intensifier) of another word's
  action or quality, not as the HEAD naming a disposition/operation/quality in its own right.
  Recurs across D7.7.1 (11/14 sampled answered-no-flag rows use manner/qualifier/adverbial
  language), M0.5.4 ("act-modifier versus disposition-noun"), M0.5.7 ("modifies [the seeking
  verb] ... not a request FOR earnestness"), and M0.6.5 (qualifies another M-code word directly,
  e.g. G2316 "godly" qualifying grief in 2Cor.7.11).
- `no-impact`: the occurrence's surface/stepGloss carries no distinguishing nuance versus the
  base sense (the M0.5.11 "sits within its base gloss ... no notable divergence" pattern).
- `not-related-to-meaningful-word`: the sub-question's target item genuinely does not exist/apply
  for this term (the M0.5.4/M0.5.6/M0.5.7-"none" pattern -- no contrast, no person-type noun, no
  seeking-term -- distinct from `no-impact`, which is about surface-vs-base sense specifically).
- `sole-mcode-in-verse`: no other M-code characteristic co-occurs in this verse at all (the
  M0.6.5 "stands alone as the sole M-coded element" pattern) -- distinct from the existing
  `no-direct-connection` (other M-codes ARE present, just unrelated to this one).
- `cluster-pole-negative` / `cluster-pole-positive`: which side of a cluster's dual-natured
  spectrum the term occupies (M0.1.1/M0.5.4's negative/negligent-pole vs positive/diligent-pole
  distinction, e.g. G0692 "negated-act pole" vs G4710's positive "energetic, focused
  application"). No `cfg_enum`/`cfg_column` name collision found against the retired (provenance
  -only, bible_research.db) C-code/tier-grid dimensional-weight scheme -- checked live, clear.
- `attested-pre-nt` / `nt-coinage`: whether the term is classical/pre-NT-attested vocabulary or
  an NT-period coinage (the M0.5.9 attestation-history pattern, e.g. "a well-attested Classical
  Greek term (Herodotus, Sophocles, Aristotle)"). Explicit pair chosen over a single tag with
  absence-implies-the-other, because a paired scheme is what actually supports filtering in
  either direction -- the whole point of this exercise.

`none` is deliberately NOT added to the enum -- it was never a real category, just an unvalidated
literal string that leaked through; the companion write-time validation (`recordingpass.py`,
`_validate_tag`) now rejects it going forward the same way `_validate_question_code` rejects a
bare `M0.1`/`M0.5`.

Safe to re-run: idempotent (INSERT OR IGNORE by name+value).

Usage:
    python iba/app/migration/extend_tag_vocabulary_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

NEW_TAGS = [
    ("qualifier-for-term", 12),
    ("no-impact", 13),
    ("not-related-to-meaningful-word", 14),
    ("sole-mcode-in-verse", 15),
    ("cluster-pole-negative", 16),
    ("cluster-pole-positive", 17),
    ("attested-pre-nt", 18),
    ("nt-coinage", 19),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    existing = {r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag'")}
    to_add = [(v, o) for v, o in NEW_TAGS if v not in existing]

    print(f"{len(to_add)} new tag value(s) to add: {[v for v, _ in to_add]}")
    if existing & {v for v, _ in NEW_TAGS}:
        print(f"Already present (skipped): {sorted(existing & {v for v, _ in NEW_TAGS})}")

    if args.dry_run:
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    for value, ordinal in to_add:
        conn.execute(
            "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
            ("ib_observation.tag", value, ordinal))
    conn.commit()

    total = conn.execute(
        "SELECT COUNT(*) n FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0"
    ).fetchone()["n"]
    print(f"Added {len(to_add)} value(s). Active ib_observation.tag values now: {total}.")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
