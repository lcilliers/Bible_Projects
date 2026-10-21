"""seed_method_rules.py — ONE-OFF, idempotent: populates `cfg_method_rule` (build_method_rule_
table.py) with the discrete, nameable rules governing Steps 1-4 of the debate pipeline, transcribed
faithfully from their source documents. Direct DML (no write-grant step exists for this table yet —
matching `cfg_enum`'s own seeding precedent; ongoing edits go through `configmaint.propose`).

Deliberately not exhaustive of every sentence in the source docs — the Q1-Q12 interrogative and
Part B's full discipline notes stay in their own documents (`WA-interpretation-questions-v1.4`),
cited by `source_doc` here, not reproduced word-for-word as 20+ more rows. What's captured here is
every rule that is either (a) mechanically enforced by code today (`enforced_by` names where), or
(b) a discrete, nameable, potentially-tunable parameter the researcher singled out. Growing this
table further (e.g. giving each of Q1-Q12 its own row) is a natural next step, not done in this
first pass, given time — flagged in BUILD.md, not silently left incomplete.

    python -m iba.app.migration.seed_method_rules
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

RULES = [
    # (step, rule_key, rule_text, source_doc, enforced_by, ordinal)
    ("hib.set", "presumptive-candidate",
     "Every human mentioned -- named or collective, major or minor, however briefly -- is a "
     "presumptive candidate: anyone who acts, undergoes an act, thinks, speaks, refrains from "
     "acting, or is simply named as present. This holds even where the act looks purely outward, "
     "administrative, locational, or incidental -- the inner-being content may be hidden behind "
     "the act, with only the act stated in the text.",
     "WA-passage-read-guidance-v1.5 step 2 note f", None, 0),
    ("hib.set", "non-human-scope",
     "A non-human being is in scope only where its state/characteristics bear directly on a human "
     "in the same context -- otherwise the verse is set aside entirely.",
     "WA-passage-read-guidance-v1.5 step 2 notes b, d", None, 1),
    ("hib.set", "collective-stays-collective",
     "A tribe, nation, 'youths', 'gentiles' etc. is recorded as ONE HIB representing the "
     "collection -- not decomposed into individuals; any later operation involving it is a "
     "movement to/from a collection, not an individual.",
     "WA-passage-read-guidance-v1.5 step 2 note c", None, 2),
    ("hib.set", "referential-named-not-skipped",
     "Where a party is unnamed but implied by the verse or wider passage, name it as a referential "
     "HIB; never assert an inferred identity as settled fact.",
     "WA-passage-read-guidance-v1.5 step 2 note e", None, 3),
    ("hib.set", "referent-crux-resolution",
     "Where a pronoun or unnamed party is genuinely ambiguous (several readings all grammatically "
     "live), enumerate every live reading, give the textual grounds for each, adopt one "
     "explicitly (stating whether this is a directed/researcher call or this pass's own default), "
     "and keep the rejected alternatives on record.",
     "debate-analytic-process-digest-20260805.md Step 1 (T4 folded in)",
     "schema: hib_referent_option", 4),
    ("hib.set", "six-type-scheme",
     "Every HIB is typed along two axes: plurality (individual | collection) x specificity "
     "(named | unnamed | implicit) = six types: named_individual, unnamed_individual, "
     "named_collection, unnamed_collection, implicit_individual, implicit_collection.",
     "nahum-1-inner-being-training-20260803.md (researcher's own training pass)",
     "cfg_enum 'hib_kind' + operations.py:_valid_hib_kinds", 5),
    ("hib.set", "db-compare-adjudicate",
     "Read the verses in scope; compare the fresh reading against what's already in the DB; "
     "validate the list against the DB; where the fresh reading differs, adjudicate and correct "
     "the DB -- not blind re-derivation.",
     "researcher direction, 2026-08-06", "operations.py:_reconcile", 6),

    ("passage.build", "hib-continuity-boundary",
     "A passage is a run of consecutive verses bound together by continuity of the HIB(s) in "
     "focus -- not an arbitrary chapter/verse-count chunk. Verses stay in one passage while the "
     "same HIB(s) continue to be what the text is tracking; the boundary falls where the cast of "
     "HIBs genuinely changes, not at a chapter number.",
     "debate-analytic-process-digest-20260805.md Step 2", "passage.py:build", 0),
    ("passage.build", "min-shared-hibs",
     "Adjacent verses must share at least N HIBs (N = passage.min_shared_hibs) to be counted as "
     "continuing the same passage.",
     "debate-analytic-process-digest-20260805.md Step 2 (parameterised, researcher's own tuning "
     "knob)", "cfg_setting passage.min_shared_hibs + passage.py:build", 1),
    ("passage.build", "no-cross-chapter",
     "A passage run never crosses a chapter boundary, regardless of HIB continuity, unless "
     "passage.cross_chapter is explicitly set.",
     "handlers/passage.py (app convention, not itself in a method doc)",
     "cfg_setting passage.cross_chapter + passage.py:build", 2),
    ("passage.build", "review-over-threshold",
     "A run longer than passage.review_over verses is flagged needs_review, not blocked -- may be "
     "several passages under different HIB focuses batched together by convenience.",
     "debate-analytic-process-digest-20260805.md failure-mode (b)",
     "cfg_setting passage.review_over + passage.py:build", 3),
    ("passage.build", "protect-content-on-rebuild",
     "A passage already carrying live phenomena is protected on any rebuild -- left completely "
     "untouched, its verses excluded from fresh run-forming. Only content-free passages, and "
     "legacy (pre-hib-continuity) rows on the one-time transition, are freely rebuilt.",
     "researcher direction, 2026-08-06", "passage.py:build (protected/protected_verse_ids)", 4),

    ("phenomenon.set", "phase-separation",
     "The phenomena register (Step 3) must be completed for the WHOLE passage before any "
     "operation (Step 4) is written for ANY verse in it -- not interleaved verse-by-verse. "
     "Multi-chapter batched passages need the most vigilance here.",
     "WA-passage-read-guidance-v1.5 Phase 1 change-control note; the direct fix for the Amos 1-3 "
     "drift", "operations.py:phenomenon_set (passage.phenomena_complete_at gate) + "
     "operations.py:operation_set (refuses while NULL)", 0),
    ("phenomenon.set", "hidden-behind-act",
     "A phenomenon may be hidden behind a stated act or a refrained-from act, with only the act "
     "recorded in the text -- naming what the act is taken to evidence is exactly this step's job.",
     "WA-passage-read-guidance-v1.5 step 3 note e", None, 1),
    ("phenomenon.set", "warrant-required",
     "For every phenomenon isolated, record the specific textual warrant that grounds it (the "
     "verb, clause, or stated silence) and whether it is stated or inferred -- its own register "
     "entry, written before and independently of any operation.",
     "WA-passage-read-guidance-v1.5 step 3b", "schema: phenomenon.textual_warrant/status", 2),
    ("phenomenon.set", "not-literary-pattern",
     "A genuine literary/structural/genre observation is not a phenomenon -- log it once as an "
     "emergent question (Step 7) instead, never built into the phenomena register.",
     "WA-interpretation-questions-v1.4 Part B.12; WA-passage-read-guidance-v1.5 step 6 note c",
     None, 3),
    ("phenomenon.set", "control-total",
     "Every HIB crossed with every verse it appears in, in this passage, equals the exact number "
     "of phenomena-register entries (including explicit 'silent' entries) Step 3 must produce "
     "before it can be considered done -- known in advance, not dependent on trusting the pass to "
     "remember to cover everything.",
     "debate-analytic-process-digest-20260805.md Step 3 'how this gets controlled'; "
     "b3-b5-operations-schema-design-20260805.md",
     "operations.py:phenomenon_set (verse_hib pair-set vs live phenomenon pair-set comparison)", 4),
    ("phenomenon.set", "silence-is-a-finding",
     "'No phenomenon found, silent' is a valid RESULT of running the phenomenon check on a "
     "human-bearing clause, not an omission -- and not a valid substitute for running the check.",
     "WA-interpretation-questions-v1.4 Part B.4; WA-passage-read-guidance-v1.5 step 2 note f",
     "schema: phenomenon.status='silent'", 5),

    ("operation.set", "operation-from-phenomenon-only",
     "An operation may only originate from an already-registered phenomenon -- never identify a "
     "fresh phenomenon while writing one. If writing an operation reveals no genuine phenomenon "
     "underlies it, the Step 3 entry was mis-identified -- go back and correct it; do not paper "
     "over the mismatch.",
     "WA-interpretation-questions-v1.4 Part B.12",
     "schema: operation.phenomenon_id NOT NULL + operations.py:operation_set", 0),
    ("operation.set", "four-parts",
     "Every operation has: process (a state/status, or a movement -- come from / go to / impact "
     "on / emerge / go away / become evident); source; target; and an action-type label. Source "
     "and target may be singular, multiple, mixed, or non-existent.",
     "WA-passage-read-guidance-v1.5 step 1 note a", "schema: operation + operation_party", 1),
    ("operation.set", "source-vs-enablement",
     "Keep source of the interior state and source of enablement to act distinct -- a non-human "
     "being may be the stated source of an outcome or an enablement without the text sourcing the "
     "actor's own disposition; extending sourcing from outcome to interior is an interpretive step "
     "to flag, never to assume.",
     "WA-interpretation-questions-v1.4 Q4 / Part B.5", "schema: operation_party.enablement_only", 2),
    ("operation.set", "action-type-is-a-label",
     "The action-type is a short, natural, verb-based tag (e.g. 'gave', 'summoned/complied', "
     "'worshiped') -- a label for cross-passage/cross-book comparison, not a taxonomy; no "
     "controlled vocabulary is being built.",
     "WA-interpretation-questions-v1.4 Q11 / Part B.10", "schema: operation.action_type (free text)", 3),
    ("operation.set", "divine-mirroring-anchored",
     "Record a human/divine operation comparison (juxtaposition, difference, inversion) only "
     "where the text's own juxtaposition or wording anchors it -- a merely plausible resemblance "
     "is logged as an emergent question, never asserted or theologically elaborated.",
     "WA-interpretation-questions-v1.4 Q12 / Part B.11", None, 4),
    ("operation.set", "decision-enum",
     "decision = retain | set_aside | retain_referential | recorded_silence.",
     "WA-interpretation-questions-v1.4 Part C section 3", "schema: operation.decision (free text, "
     "not yet enum-enforced -- see cfg_enum follow-up)", 5),
]


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    if not _table_exists(conn, "cfg_method_rule"):
        raise RuntimeError("cfg_method_rule doesn't exist -- run build_method_rule_table.py first")

    existing = {(r["step"], r["rule_key"]) for r in conn.execute(
        "SELECT step, rule_key FROM cfg_method_rule").fetchall()}
    to_insert = [r for r in RULES if (r[0], r[1]) not in existing]
    if to_insert:
        conn.executemany(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES (?,?,?,?,?,?,1)", to_insert)
    conn.commit()
    print(f"rows inserted this run: {len(to_insert)}")
    print(f"rows already present: {len(RULES) - len(to_insert)}")
    print(f"total rules now for: " + ", ".join(
        f"{step} ({n})" for step, n in conn.execute(
            "SELECT step, COUNT(*) FROM cfg_method_rule GROUP BY step").fetchall()))


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
