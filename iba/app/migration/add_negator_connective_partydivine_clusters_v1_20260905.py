"""add_negator_connective_partydivine_clusters_v1_20260905.py — ONE-OFF. Part of the
cfg_lexical_code_class -> cluster de-cfg-ification (escalation #1499, researcher's own granularity
test, verbatim 2026-09-05): "a) why separate from T2 - what benefit will it have in analysis - for
instance, if a bucket is in support of a specific tier question, that will make the analysis more
efficient... b) the buckets must not over engineer and have a separate bucket for each minute
group. take any other bucket like m15 - these are buckets of strongs with a same type of relation
to each other. this is the right granularity."

Applying that test to the 20 rows still sitting in cfg_lexical_code_class (part 1, T4/Adversarial,
already built -- add_adversarial_cluster_v1_20260905.py):

  - NEGATOR (7 codes): all share exactly one relation (negation), all support the same live
    analytical question (verse_lexical.is_negator / polarity reading). ONE bucket: T5.
  - CONNECTIVE (6 codes, causal/coordinating/purpose): kept as ONE bucket, T6 -- NOT split into 3
    by sub-type. Causal=2/coordinating=3/purpose=1 codes each is exactly the "minute group" test
    (b) warns against; "connective/clause-linking function" is itself the one shared relation at
    the M15 grain, the causal/coordinating/purpose distinction stays in cluster_strong.rationale
    per row, not a separate top-level code each.
  - PARTY_DIVINE (7 codes): directly answers real catalogue questions (T4.3.1/T4.4.1/T4.6.1 in the
    observation catalogue -- a different T-numbering scheme entirely, see the glossary's own T1
    disambiguation entry). ONE bucket: T7.

Mechanics, in iba.db, one transaction, direct writes (same `writer='migration'` territory as T4):
reallocate (UPDATE in place) every code currently at T2; INSERT fresh where no live cluster_strong
row exists yet (G3756/G3761 for negator, G2424 for party_divine -- gaps in the original 2026-08-11
mechanical sweep, not previously classified at all). G2962H is explicitly left untouched at its
existing M23 assignment -- a different, already-established classification, not part of this
cleanup (its only live cluster_strong row is M23, not T2, so "reallocate from T2" does not apply).

Idempotent: checks each code's current cluster_code before acting.

    python -m iba.app.migration.add_negator_connective_partydivine_clusters_v1_20260905
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_CLUSTERS = [
    ("T5", "Negator", "T5 - Negator: a strong expressing grammatical negation (not/no) -- one "
     "relation shared by every member, directly supporting verse_lexical.is_negator/polarity "
     "reading. Referent/function classification, orthogonal to the thematic M-code axis."),
    ("T6", "Connective", "T6 - Connective: a strong functioning as a clause-linking word "
     "(causal/coordinating/purpose) -- kept as one bucket per the researcher's own granularity "
     "test (2026-09-05): the finer causal/coordinating/purpose distinction is real but too small "
     "a grouping (1-3 codes each) to earn its own top-level cluster code; it is recorded in each "
     "row's own rationale instead. Referent/function classification, orthogonal to the thematic "
     "M-code axis."),
    ("T7", "Party-Divine", "T7 - Party-Divine: a strong referring to the divine party (God/the "
     "LORD/Christ) -- referent-identity classification, orthogonal to the thematic M-code axis; "
     "directly supports observation-catalogue party-kind questions (a different T-numbering "
     "scheme, see the glossary's own T1 disambiguation entry). A code can carry both an M-cluster "
     "assignment and this one."),
]

# (strong, target_cluster_code, note) -- reallocate if currently T2, insert fresh if no row exists.
_ITEMS = [
    ("H0408", "T5", "lo, negator particle -- evidence-checked live against strong.stepGloss"),
    ("H3808", "T5", "lo, negator particle -- evidence-checked live against strong.stepGloss"),
    ("H3809", "T5", "la, negator particle (Aramaic) -- evidence-checked live"),
    ("G3756", "T5", "ou, negator particle -- evidence-checked live (no prior cluster_strong row)"),
    ("G3361", "T5", "me, negator particle -- evidence-checked live"),
    ("G3760", "T5", "oudepote, negator particle -- evidence-checked live"),
    ("G3761", "T5", "oude, negator particle -- evidence-checked live (no prior cluster_strong row)"),
    ("H3588A", "T6", "ki, causal connective ('because'/'for') -- evidence-checked live"),
    ("G1063", "T6", "gar, causal connective ('for') -- evidence-checked live"),
    ("H9002", "T6", "waw, coordinating connective ('and') -- evidence-checked live"),
    ("G2532", "T6", "kai, coordinating connective ('and') -- evidence-checked live"),
    ("G1161", "T6", "de, coordinating connective ('but'/'and') -- evidence-checked live"),
    ("G2443", "T6", "hina, purpose connective ('so that'/'in order that') -- evidence-checked live"),
    ("H0430G", "T7", "elohim, gloss 'God' -- evidence-checked live, escalation #1383 v32"),
    ("H0410G", "T7", "el, gloss 'God' -- evidence-checked live, escalation #1383 v32"),
    ("H0410L", "T7", "el, gloss 'God' (variant sense) -- evidence-checked live, escalation #1383 v32"),
    ("H0410K", "T7", "el, gloss 'God' (variant sense) -- evidence-checked live, escalation #1383 v32"),
    ("H3068G", "T7", "YHWH, gloss 'the LORD' -- evidence-checked live, escalation #1383 v32"),
    ("G2316", "T7", "theos, gloss 'God' -- evidence-checked live, escalation #1383 v32"),
    ("G5547", "T7", "christos, gloss 'Christ' -- evidence-checked live, escalation #1383 v32"),
    ("G2424", "T7", "iesous, gloss 'Jesus' -- evidence-checked live (no prior cluster_strong row), "
     "escalation #1383 v32"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        for code, short_name, description in _CLUSTERS:
            exists = conn.execute(
                "SELECT 1 FROM cluster WHERE cluster_code=?", (code,)).fetchone()
            if not exists:
                conn.execute(
                    "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
                    "VALUES (?, ?, ?, '', 0)", (code, short_name, description))
                report.append(f"cluster {code} '{short_name}' created")
            else:
                report.append(f"cluster {code} already exists -- no-op")

        for strong, target, note in _ITEMS:
            row = conn.execute(
                "SELECT id, cluster_code, rationale FROM cluster_strong "
                "WHERE strong=? AND deleted=0", (strong,)).fetchone()
            if row is None:
                conn.execute(
                    "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, "
                    "deleted, rationale) VALUES (?, ?, 'migration-20260905-decfgification', "
                    "datetime('now'), 0, ?)",
                    (strong, target, f"new assignment 2026-09-05 (no prior cluster_strong row) "
                                      f"-- {note}"))
                report.append(f"{strong}: inserted fresh at {target}")
                continue
            if row["cluster_code"] == target:
                report.append(f"{strong}: already {target} -- no-op")
                continue
            if row["cluster_code"] != "T2":
                report.append(f"{strong}: currently {row['cluster_code']} (not T2) -- left "
                               f"untouched, not part of this reallocation")
                continue
            new_rationale = (row["rationale"] or "") + (
                f" | relocated T2->{target} 2026-09-05 (de-cfg-ification, researcher-approved "
                f"granularity test, escalation #1499). {note}")
            conn.execute(
                "UPDATE cluster_strong SET cluster_code=?, rationale=? WHERE id=?",
                (target, new_rationale, row["id"]))
            report.append(f"{strong}: reallocated T2 -> {target} (id={row['id']})")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("add_negator_connective_partydivine_clusters_v1_20260905:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
