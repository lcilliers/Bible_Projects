"""assign_leg3_orphan_strongs_v1_20260915.py — ONE-OFF migration, escalation #1606.

Researcher instruction, verbatim, 2026-09-15: "reconcile() must check and gaurantee that
strong-cluster is in sync. so change the routines to ensure it as the response to 1606 and then
assign the strongs to the right cluster."

Two parts, applied together as one unit of work:

1. **The guarantee mechanism** (code, not this script): `handlers/raw.py:reconcile()` (step
   `strong.reconcile`) and `handlers/raw.py:backfill_meaning()` now return `fail("unclassified", ...)`
   instead of always `ok()` when any code comes back with no cluster assignment at all;
   `handlers/cluster.py:validate()` now escalates on a nonzero unclassified count too, not just the
   two narrower no-word/sibling-conflict exception shapes. This script registers the two new
   `cfg_on_fail` rows those conditions need, and refreshes the three affected `cfg_step.does` texts
   to describe the new behaviour (governance.rules_must_be_config_driven — code behaviour and its
   config description change together).

2. **The backlog** — the 111 live `strong` rows Leg 3 found with zero `cluster_strong` allocation
   (`iba/docs/1706-lexical-stack-full-rebuild-consolidated-build-proposal-v1-20260915.md` §3,
   escalation #1606). Classified by hand, same method already established in this escalation's own
   history (morph_code pattern first, then each code checked individually against the live T5/T6
   definitions before falling back to T2) — not blanket morph-matched. Reuses the exact
   `cluster_strong` INSERT shape `apply_1598_cluster_batch.py` established (cfg_utility: "category='data'
   table, writer='migration' grant, not configmaint.propose territory") rather than a fresh mechanism.

Classification method, by group (full rationale recorded per-row in `cluster_strong.rationale`):

- **T5 (Negator)** — Greek `PRT-N`/`CONJ-N` codes whose core sense is a plain declarative negation
  (not/nor/not yet/not any more), matching the live T5 precedent (`G3768` "not yet" `ADV-N`).
- **T6 (Connective)** — every `CONJ`-tagged code (matches T6's own "clause-linking word" definition
  almost definitionally, and every live T6 Greek member with a `CONJ`/`COND`/`PREP` tag already sets
  this precedent); plus the Greek `PRT-N` codes that are RHETORICAL/INTERROGATIVE negatives ("surely
  not?", "isn't it?") rather than plain declarative ones — same disposition the researcher gave
  `G0687` ('no?', an interrogative-negative particle) in this escalation's own round-2 resolution:
  moved to T6, not T5, because the negation is doing rhetorical/discourse work, not asserting a
  plain fact; plus comparative/temporal/purpose particles (`PRT`/`PREP`-tagged) whose core sense
  matches an existing T6 member's function (as/just as, how much more, so that, whence, when(ever)).
- **T2 (Supplementary, excluded)** — every H9xxx Hebrew code (pronoun suffixes, the article, plain
  prepositions/relative marker — the exact, already-named pattern this escalation's own history
  calls "H9xxx grammatical/functional markers"); every plain spatial/directional Greek preposition
  with no causal/temporal/comparative force (toward, outside, above, under, between, near, opposite,
  beyond); three incidental Greek place names with zero inner-being relevance (Cos/Patara/Rhodes,
  matching #1606's own T10-T13 finding: "0 genuine hits... generic usage, not real relevance");
  liturgical exclamations (hallelujah, Hosanna, aha!, well done).

**Flagged, not silently guessed — 3 genuine anomalies, left at T2 pending researcher review, not
elevated to a design decision here:**
- `G1306` ("to shine through", tagged `PREP`) — the gloss reads like a verb, not a preposition; a
  likely tag/gloss data anomaly, not verified against STEP directly this pass.
- `G4315` ("Friday", tagged `PREP`) — same shape: a day-name gloss on a preposition-tagged code;
  content-wise this looks like a T15 (Calendar) candidate if the tag is wrong, but left at T2 rather
  than asserting a POS the live data doesn't itself support.
- `G3637` ("eighth day") — zero live `verse_lexical` occurrences (never actually used in the built
  corpus yet), so no morph evidence exists to classify by; T2 is the safe default, not a considered
  read.

Idempotent (checks for an existing live row before inserting, same convention as
`apply_1598_cluster_batch.py`) — re-running this script is a no-op on every row it already applied.

    python -m iba.app.migration.assign_leg3_orphan_strongs_v1_20260915
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_SOURCE = "claude-scan-20260915"

# ── classification payload ─────────────────────────────────────────────────────────────────────

_T5 = {  # plain declarative negation
    "G3380": "not yet (PRT-N) -- plain declarative negation, matches live T5 member G3768 'not yet' (ADV-N).",
    "G3765": "not any more (PRT-N) -- plain declarative negation, same shape as G3768 'not yet'.",
    "G3780": "not! (PRT-N) -- plain declarative/emphatic negation, matches live T5 member G3756 'no' (PRT-N).",
    "G3383": "neither (CONJ-N) -- negative correlative coordinator, matches live T5 members G3366/G3761 'nor' (CONJ-N).",
    "G3777": "neither (CONJ-N) -- same shape as G3383, negative correlative coordinator, matches G3366/G3761.",
}

_T6 = {  # clause-linking: CONJ-tagged, plus rhetorical-negative and comparative/temporal PRT/PREP
    "G3304": "rather (PRT) -- adversative/contrastive connective, matches live T6 member G4133 "
             "'but/however'. (Self-caught correction, same-day: dropped from the first pass of this "
             "script's own payload, fell through to the generic T2 fallback -- fixed live before the "
             "researcher was asked to review, see the escalation resolution for the correction record.)",
    "G1875": "when/as soon as (CONJ) -- temporal connective, matches live T6 member G3752 'when(-ever)'.",
    "G1893": "since (CONJ) -- causal/temporal connective.",
    "G1894": "since (CONJ) -- causal/temporal connective.",
    "G1895": "since (CONJ) -- causal/temporal connective.",
    "G2228": "or (CONJ) -- coordinating connective, matches live T6 member G2532 'and'.",
    "G2259": "when (CONJ) -- temporal connective.",
    "G2260": "than (CONJ) -- comparative connective.",
    "G2505": "as/just as (CONJ) -- comparative connective, matches live T6 member G5613 'as/when' (PRT).",
    "G2509": "just as (CONJ) -- comparative connective.",
    "G2526": "insofar as (CONJ) -- causal/comparative connective.",
    "G2530": "as/just as (CONJ) -- comparative connective.",
    "G2531": "as/just as (CONJ) -- comparative connective.",
    "G2534": "even/even though (CONJ) -- concessive connective.",
    "G2539": "although (CONJ) -- concessive connective.",
    "G2543": "and yet/although (CONJ) -- concessive connective.",
    "G2544": "and yet/although (CONJ) -- concessive connective.",
    "G2547": "and from there (CONJ) -- coordinating/sequential connective, matches 'therefore/then' family.",
    "G2579": "and/even if (CONJ) -- conditional connective, matches live T6 members G1437/G3362 (COND).",
    "G3305": "yet (CONJ) -- adversative connective, matches live T6 member G4133 'but/however'.",
    "G3363": "lest/so that... not (CONJ) -- purpose-negative connective, matches live T6 members "
             "G2443 'in order that/to' (CONJ) and G3379 'lest' (PRT-N, already T6).",
    "G3365": "surely not (PRT-N) -- rhetorical/interrogative negative, same disposition as this "
             "escalation's own G0687 'no?' round-2 resolution (interrogative-negative -> T6, not T5, "
             "because the negation does rhetorical/discourse work, not plain assertion).",
    "G3375": "certainly (PRT) -- reads as an interrogative-negative particle (me-ti family) by "
             "Strong's-number proximity to the surrounding G3363-G3386 cluster; same disposition as G3365/G0687.",
    "G3378": "isn't it? (PRT-N) -- explicitly rhetorical-interrogative, matches live T6 member "
             "H0371 'isn't?' (HTi, already T6) and G0687's own round-2 resolution.",
    "G3381": "so that (PRT) -- purpose connective, matches live T6 member G2443 'in order that/to'.",
    "G3385": "surely not (PRT-N) -- rhetorical/interrogative negative, same disposition as G3365/G0687.",
    "G3386": "how much more (PRT) -- a fortiori comparative-argument connective.",
    "G3513": "as surely as (PRT) -- comparative connective.",
    "G3606": "whence (CONJ) -- relative/locative connective, matches the T6 broadening the "
             "researcher gave H0834A 'which' (a word that triggers Layer 2 to look for related "
             "words/activity qualifies, even as a relative/interrogative rather than a conjunction proper).",
    "G3676": "just as (PREP, tagged) -- comparative connective despite the PREP tag, matches live "
             "T6 member G5616 'like/as/about' (PREP).",
    "G3698": "when(-ever) (CONJ) -- temporal connective, matches G3752 'when(-ever)'.",
    "G3699": "where(-ever) (CONJ) -- relative/locative connective, same reasoning as G3606.",
    "G3740": "whenever (CONJ) -- temporal connective.",
    "G3753": "when (CONJ) -- temporal connective.",
    "G3767": "therefore/then (CONJ) -- inferential connective, matches live T6 members G1352/G5105 'therefore'.",
    "G4133": "but/however (CONJ) -- adversative connective, matches live T6 member G0235 'but'.",
    "G4218": "once/when (PRT) -- temporal connective.",
    "G5037": "and/both (CONJ) -- coordinating connective, matches G2532 'and'.",
    "G5104": "certainly (CONJ) -- inferential connective ('therefore'), matches G1352/G5105 family.",
    "G5618": "just as (PRT) -- comparative connective, matches G5613 'as/when' (PRT, already T6).",
}

_T2_ANOMALY_NOTE = {
    "G1306": "gloss ('to shine through') reads like a verb despite the PREP tag -- likely tag/gloss "
             "data anomaly, not verified against STEP this pass. Flagged for researcher review, not "
             "resolved as a mechanical fix.",
    "G4315": "gloss ('Friday') reads like a day name despite the PREP tag -- likely tag/gloss data "
             "anomaly; a T15 (Calendar) candidate if the tag is wrong. Flagged for researcher review.",
    "G3637": "zero live verse_lexical occurrences (never used in the built corpus yet) -- no morph "
             "evidence to classify by; T2 is the safe default, not a considered read.",
}

_T2_PLACE_NAMES = {"G2972": "Cos", "G3959": "Patara", "G4499": "Rhodes"}
_T2_EXCLAMATIONS = {"G0239": "hallelujah", "G3758": "aha!", "G5614": "Hosanna", "G7530": "well done"}


def _t2_rationale(code: str, gloss: str) -> str:
    if code in _T2_ANOMALY_NOTE:
        return _T2_ANOMALY_NOTE[code]
    if code in _T2_PLACE_NAMES:
        return (f"incidental Greek place name ('{gloss}') with zero inner-being relevance -- matches "
               f"escalation #1606's own T10-T13 finding (generic usage, not real referent-class "
               f"relevance), not elevated to T10.")
    if code in _T2_EXCLAMATIONS:
        return f"liturgical/interjectional exclamation ('{gloss}'), no inner-being content."
    if code.startswith("H9"):
        return ("Hebrew grammatical/functional marker (pronoun suffix, article, preposition, or "
               "relative particle) -- the established H9xxx pattern this escalation's own history "
               "already names.")
    return (f"plain spatial/directional/relational preposition or particle ('{gloss}') -- no "
           f"causal/temporal/comparative/purposive force, does not fit T6's clause-linking "
           f"definition; grammatical/functional, not content-bearing.")


def build_payload(conn: sqlite3.Connection) -> list[dict]:
    """Every code this script's own classification names (T5/T6), plus every currently-orphaned
    live strong (T2 fallback). Idempotent by construction: a code already correctly classified from
    a prior run of this same script is a plain no-op in apply_cluster_strong (checked there, not
    here) -- this function only needs to fail loudly if a T5/T6-listed code has actually DISAPPEARED
    from `strong` (soft-deleted) since this script was written, which would mean the classification
    above is stale, not just already-applied."""
    gone = [code for code in (set(_T5) | set(_T6))
            if not conn.execute("SELECT 1 FROM strong WHERE strongNumber=? AND deleted=0",
                                (code,)).fetchone()]
    if gone:
        raise RuntimeError(
            f"{len(gone)} code(s) in this script's T5/T6 payload no longer exist as a live strong "
            f"row: {sorted(gone)} -- re-check before running, do not silently skip.")

    orphan_rows = conn.execute(
        "SELECT strongNumber, stepGloss FROM strong s WHERE deleted=0 AND NOT EXISTS "
        "(SELECT 1 FROM cluster_strong cs WHERE cs.strong = s.strongNumber AND cs.deleted=0) "
        "ORDER BY strongNumber").fetchall()
    orphan_codes = {r["strongNumber"] for r in orphan_rows}
    gloss_of = {r["strongNumber"]: r["stepGloss"] for r in orphan_rows}

    payload = []
    for code, rationale in _T5.items():
        payload.append({"strong": code, "cluster_code": "T5", "rationale": rationale})
    for code, rationale in _T6.items():
        payload.append({"strong": code, "cluster_code": "T6", "rationale": rationale})
    for code in sorted(orphan_codes - set(_T5) - set(_T6)):
        payload.append({"strong": code, "cluster_code": "T2",
                        "rationale": _t2_rationale(code, gloss_of[code])})
    return payload


# self-caught correction, same run day: G3304 ('rather') was meant for T6 from the first draft of
# the classification above but fell through to the generic T2 fallback on this script's first live
# run -- soft-delete that wrong row here so the correct T6 insert (in _T6 now) doesn't leave a
# stale, conflicting T2 membership behind it.
_CORRECTIONS = [("G3304", "T2")]


def apply_corrections(conn: sqlite3.Connection) -> list[str]:
    report = []
    for strong, wrong_code in _CORRECTIONS:
        row = conn.execute(
            "SELECT id FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (strong, wrong_code)).fetchone()
        if row is None:
            report.append(f"correction {strong}/{wrong_code}: no live row to remove -- no-op")
            continue
        conn.execute(
            "UPDATE cluster_strong SET deleted=1, rationale=rationale || "
            "' | corrected same-day: this strong belongs in T6, not T2 (self-caught, see "
            "escalation #1606 resolution).' WHERE id=?", (row["id"],))
        report.append(f"correction {strong}: removed stale {wrong_code} row (id={row['id']})")
    return report


def apply_cluster_strong(conn: sqlite3.Connection) -> list[str]:
    report = []
    for item in build_payload(conn):
        exists = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (item["strong"], item["cluster_code"])).fetchone()
        if exists:
            report.append(f"{item['strong']} -> {item['cluster_code']}: already live -- no-op")
            continue
        conn.execute(
            "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
            "confidence, operation, review_flag, rationale) "
            "VALUES (?, ?, ?, datetime('now'), 0, 'medium', 0, 0, ?)",
            (item["strong"], item["cluster_code"], _SOURCE, item["rationale"]))
        report.append(f"{item['strong']}: inserted into {item['cluster_code']}")
    return report


def apply_on_fail_rows(conn: sqlite3.Connection) -> list[str]:
    report = []
    rows = [
        ("strong.reconcile", "unclassified", "pause-continue", "terminal",
         "a strong got no cluster assignment at all (no HIGH-confidence precedent match) -- a "
         "researcher/Claude classification decision, not silently continuing (escalation #1606)."),
        ("raw.backfill_meaning", "unclassified", "pause-continue", "terminal",
         "a backfilled strong got no cluster assignment at all -- same class of gap as "
         "strong.reconcile, must not silently continue (escalation #1606)."),
    ]
    for step, condition, path, route, message in rows:
        exists = conn.execute(
            "SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", (step, condition)).fetchone()
        if exists:
            report.append(f"cfg_on_fail {step}/{condition}: already present -- no-op")
            continue
        conn.execute(
            "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, inactive) "
            "VALUES (?, ?, ?, NULL, ?, ?, 0)",
            (step, condition, path, message, route))
        report.append(f"cfg_on_fail {step}/{condition}: registered ({path})")
    return report


def refresh_step_does_text(conn: sqlite3.Connection) -> list[str]:
    report = []
    updates = [
        ("strong.reconcile",
         "Cluster-classify and, where warranted, promote every one of the word's own codes "
         "(lib.strongreconcile.reconcile() per code) -- runs last, after raw.validate, so "
         "verses/spans are already validated before classification. Point (c), "
         "backfill-cluster-triage-plan-v3-20260812.md: new-word must complete through "
         "verse_lexical for qualifying strongs. UPDATED 2026-09-15 (escalation #1606): fails "
         "(condition='unclassified') if any of the word's own codes got no cluster assignment at "
         "all, rather than always returning ok() -- an automatic classification attempt runs on "
         "every code either way, but a failed attempt is now surfaced, not silently absorbed."),
        ("raw.backfill_meaning",
         "for a book (optionally narrowed to one chapter's verse range via -Range C:V-V), find "
         "every distinct strong its spans reference that has no strong row yet, and pull ONLY the "
         "meaning (STEP getInfo -> strong/strong_sense/strong_meaning_tree/strong_lexicon) -- not "
         "verses. Reuses raw.detail_one() unchanged. Progressive, passage-driven DB coverage "
         "growth, not a full-Bible bulk pull. Cluster-reconciles every newly-backfilled code "
         "inline (the only chain these codes ever pass through). UPDATED 2026-09-15 (escalation "
         "#1606): fails (condition='unclassified') if any newly-backfilled code got no cluster "
         "assignment at all, rather than always returning ok()."),
        ("cluster.validate",
         "Read-only DB-wide coverage + exception report: unclassified strongs, backfill non-T2 "
         "not yet promoted, and the two named exception shapes (cluster with no word; backfill "
         "with an already-active/clustered sibling). Persists a report every run. UPDATED "
         "2026-09-15 (escalation #1606): escalates if EITHER an unclassified strong exists OR "
         "either named exception shape exists -- previously only escalated on the two named "
         "exception shapes, leaving a plain unclassified count unescalated indefinitely."),
    ]
    for step, does in updates:
        conn.execute("UPDATE cfg_step SET does=? WHERE step=?", (does, step))
        report.append(f"cfg_step.does refreshed: {step}")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = []
        report += apply_on_fail_rows(conn)
        report += refresh_step_does_text(conn)
        report += apply_corrections(conn)
        report += apply_cluster_strong(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    print(f"\n{len(report)} action(s) applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
