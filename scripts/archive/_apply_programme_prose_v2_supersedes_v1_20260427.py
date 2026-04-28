"""_apply_programme_prose_v2_supersedes_v1_20260427.py

Apply Architecture v2 updates to programme prose:

  1. Insert new prose_section_type row: prog_data_obslog_pipeline (chapter 4)
  2. Supersede 4 existing programme prose sections (v1 → v2):
       - prog_instr_session_b_readiness
       - prog_instr_session_b_output
       - prog_disc_two_ai
       - prog_data_questions
  3. Insert new prose_section row for prog_data_obslog_pipeline (v=1)

Source-of-truth for the v2 prose bodies:
  outputs/investigations/programme-prose-v2-recommendations-v1-20260427.md

Idempotent: re-running on a database where the supersedes have already
landed will skip cleanly.

Usage:
  python scripts/archive/_apply_programme_prose_v2_supersedes_v1_20260427.py
  python scripts/archive/_apply_programme_prose_v2_supersedes_v1_20260427.py --live
"""
from __future__ import annotations
import argparse
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


# ── v2 prose bodies (verbatim from programme-prose-v2-recommendations-v1) ───

PROSE_V2 = {}

PROSE_V2["prog_instr_session_b_readiness"] = """The Session B Analysis Readiness instruction governs the readiness phase of \
Session B — the stage that prepares a word for analytical work. Under \
Architecture v2 (effective 2026-04-27) this phase is owned end-to-end by \
Claude Code: AI's involvement is limited to receiving the readiness output \
and proceeding into Analysis Output.

Claude Code generates two paired artefacts per registry: a readiness `.md` \
(human-readable, structured into 14 sections covering registry overview, \
term inventory, lexical foundation, XREF terms, group landscape with \
dimensions, correlation signals, existing flags and findings, thin-evidence \
flags, verbatim verse text, legacy-VC notice, generic catalogue with \
embedded JSON, readiness verification, and open Session B items) and a \
readiness `.json` (machine-readable mirror). The structure is deterministic \
— same DB state produces byte-identical output modulo timestamp — and the \
generation can be re-run any time the database state changes.

The §N Open Session B Items section carries forward every `wa_session_b_findings` \
row at status `open` for the registry — Stage 2a observations from prior \
sessions that have not yet resolved, plus any anomalies CC raised during \
post-write validation of past obslogs. Each open item must reach one of \
four outcomes by the close of the upcoming analytical session: resolution \
via a Q&A pair, conversion to an SD pointer, raising as a new GAP catalogue \
question, or marking as no-longer-relevant with reason. The instruction \
treats §N as non-negotiable; an analytical session that closes leaving §N \
items open has not closed cleanly.

Pre-flight integrity checks run before the readiness output is issued. CC \
verifies anchor count consistency, dimension assignment coherence, term-\
status integrity, and group description versus dimension drift. When an \
inconsistency surfaces, CC writes a `wa_session_b_findings` row at status \
`open` with a `DATA_ANOMALY_*` finding type — making the anomaly visible \
to AI in the next session's §N. This bidirectional channel between CC's \
data validation and AI's analytical review is the mechanism by which the \
database and the analytical record stay coherent.

For revision sessions — when a registry has been analysed before and is \
being revisited — CC produces an additional artefact: the analytic status \
`.md`+`.json` companion, capturing lifecycle summary, resolved Q&A pairs, \
resolved SD pointers, not-relevant findings, prior chapters, anchor-verse \
analytical notes, and open items. AI for revision sessions reads both the \
readiness output (current data) and the analytic status (prior analysis) \
and produces an obslog reflecting any shifts.

Analysis Readiness is a discipline of preparation — under v2, it is the \
discipline of producing a data artefact that prompts AI to deal with every \
field it presents and to resolve every open item carried into the session. \
It does not itself produce analytical output; it produces the readiness \
state and the open-item agenda."""

PROSE_V2["prog_instr_session_b_output"] = """The Session B Analysis Output instruction governs the analytical production \
stage of Session B — where a word is read in depth and the programme's \
principal analytical output is written. Under Architecture v2 (effective \
2026-04-27), this stage takes the readiness `.md` (and, for revision \
sessions, also the analytic status `.md`) as input and produces a single \
comprehensive obslog `.md` as output. There are no AI-submitted patches.

The stage retains its three sub-stages. Stage 2a is the comprehensive \
reading — every verse in the registry read against the full verse context \
and the dimensional profile, with observations captured to the obslog as \
they arise. Stage 2b is the Q&A partitioning — findings from the reading \
are linked to catalogue questions, producing answers against existing \
universal questions, raising new GAP questions where the catalogue does \
not yet cover the surfaced pattern, and marking questions as not-applicable \
where the word's evidence does not engage the question's domain. Stage 2c \
is the analytic word output — five chapters of analytical prose (Word \
Characteristic Summary, Word Impact Description, Annotated Verse Evidence, \
Original Language Vocabulary, Connections and Research Pointers) plus a \
sixth section (Open Items) that compiles SD pointers for Session D.

Two disciplines are mandatory under v2. The first is citation discipline: \
every Stage 2b answer must cite its source observation as an OBS-NNN \
reference inline; every Stage 2c chapter substantive claim must cite at \
least one source — an OBS-NNN, a Q&A code, an SD pointer code, or an \
existing finding ID. Without these citations, CC's parser cannot link \
the answer to its evidence and the audit trail breaks. The second is the \
§N open-item discipline: every open Session B finding carried forward \
into the session — visible in §N of the readiness `.md` — must reach a \
resolution outcome before session close. The obslog records the chosen \
outcome path (Q&A, new GAP question, SD pointer, not-relevant) for each \
open item; CC's parser reads these closures and updates the lifecycle \
state. When an analytic revision is performed on a previously analysed \
registry, the same disciplines apply to revisited prose: chapters whose \
content is affected by the revision must be superseded with citation-\
disciplined versions covering the newly-resolved findings, ensuring the \
prose-versus-findings audit trail remains complete.

The obslog is the canonical artefact. Claude Code parses it into the \
database after the session: chapters write to the prose store, Q&A pairs \
populate the catalogue-link table, observations land as new findings, \
SD pointers and dimension references become flag and entity-link rows, \
anchor-verse analytical readings return to the verse_context table, new \
catalogue questions enter the question store, and review notes append to \
existing catalogue rows. Every category of analytical content has a \
defined target table; nothing the obslog records is silently dropped.

Closure is the writer's status_update operation, advancing \
`word_registry.session_b_status` to Analysis Complete. Session C opens on \
the chapter prose; Session D is notified of the SD pointers. Where \
Readiness prepares, Output produces — together they remain the pair, but \
under v2 their delivery mechanism is the obslog-to-DB capture pipeline, \
not the patch flow."""

# prog_disc_two_ai: keep first 3 paragraphs of v1, append v2 closing.
# We need to fetch v1 body and replace its closing paragraph.
# Strategy: load v1 body, split on '\n\n', keep first N-1 paragraphs,
# replace the final paragraph with the v2 closing.
PROSE_V2_TWO_AI_CLOSING = """The two agents interact through three structured artefacts: **patches**, \
**directives**, and **obslogs**. Patches remain the instrument for \
discrete database changes — Verse Context corrections, REPAIR work, \
dimension review writes — under the existing patch instruction. Directives \
remain the instrument for operations outside the patch format — schema \
migrations, ad-hoc queries, structural operations. Under Architecture v2 \
(2026-04-27), the **obslog** joins them as the canonical artefact for \
analytical sessions: Claude AI produces a comprehensive obslog `.md` and \
Claude Code parses it into the database via the Phase 2 writer pipeline. \
The writer maps every category of analytical content — observations, \
Q&A pairs, chapters, SD pointers, anchor-verse analyses, new catalogue \
questions, review notes, status updates — to its DB target table, with \
pre-write backup, transactional commit, and post-write validation.

The researcher sits at the gate between the two agents. Patches and \
directives are reviewed before Claude Code applies them. Obslogs follow \
the same discipline — Claude AI produces the obslog, the researcher \
reviews the analytical work, Claude Code parses it into the database. \
Under v2 this workflow is more integrated: Claude Code's role expanded \
to include the readiness output generation that prompts AI's analytical \
work, the analytic status generation that supports revision sessions, \
and the anomaly detection that surfaces data inconsistencies as open \
findings for AI to address in the next session. The bidirectional \
channel — AI's analytical observations and CC's data anomalies both \
landing as `wa_session_b_findings` rows for resolution — is the \
mechanism that keeps the analytical record and the database coherent."""

# prog_data_questions: keep first 2 paragraphs, append v2 lifecycle/coverage block.
PROSE_V2_QUESTIONS_TAIL = """`wa_session_b_findings` is the programme's analytical journal. Under \
Architecture v2 (2026-04-27) it operates as an open-task lifecycle \
register: each row is an analytical observation or a CC-raised data \
anomaly that progresses through a defined lifecycle. The `status` field \
takes five values. A finding at `open` is a working observation \
awaiting resolution — typically a Stage 2a observation captured during \
a comprehensive reading, or a `DATA_ANOMALY_*` row CC wrote during \
post-write validation. A finding at `resolved_qa` has been linked to a \
catalogue question through `wa_finding_catalogue_links` — the question \
is the question, the source observation is the source, and the answer \
is recorded in the link's `session_b_note` field. A finding at \
`resolved_sd` has been converted to an SD pointer for Session D's \
cross-registry synthesis. A finding at `not_relevant` has been closed \
without analytical pickup, with reason captured. A finding at \
`superseded` has been replaced by a more precise finding through the \
`superseded_by_id` reference. Every analytical session works through \
its open findings: the obslog records the chosen outcome path for each, \
and Claude Code's writer updates the lifecycle state.

The Q&A architecture under v2 lives in two tables. The catalogue \
question is the question; the link in `wa_finding_catalogue_links` is \
the Q&A pair — finding_id pointing to the source observation, question_id \
pointing to the catalogue row, `session_b_note` carrying the answer \
text, and `coverage` taking one of four values. `full` records an \
ANSWERED Q&A with substantive evidence. `partial` records a PARTIALLY \
ANSWERED Q&A with qualification. `not_applicable` records a question \
the word's evidence does not engage — the link has no source finding \
(the table allows a null finding_id under M43) but records the \
not-applicable disposition with rationale. `no_finding` is filled by \
Claude Code's catalogue completeness sweep for any universal question \
not addressed by the analytical session — it surfaces silent misses \
and creates the backfill ledger for questions added to the catalogue \
later. With these four coverage values, every universal question for \
every analysed word produces a coverage row; the catalogue's coverage \
across the programme can be queried in a single SQL pass.

`wa_finding_entity_links` is the layer that grounds findings in the \
data. For every Q&A, Claude Code's writer creates entity-link rows \
recording which terms (mti_term_id), verses (verse_record_id), groups \
(verse_context_group.id), and dimensions (wa_dimension_index.id) the \
answer cites. The link table answers two queries that the prose alone \
cannot: which findings touch a particular verse — readable from the \
verse-link rows — and which findings speak to a particular dimension — \
readable from the dimension-link rows. Session D's cross-registry work \
reads from these link tables to discover findings that share verses or \
dimensions across registries.

The catalogue is generative. New questions arise from analytical work: \
GAP questions identify gaps in the programme's standing line of \
inquiry; word-specific extension questions surface the inquiries that \
a particular word's evidence made worth indexing for future passes \
on the same word. Under v2 these new questions enter `wa_obs_question_catalogue` \
through the writer pipeline, with `catalogue_version` field carrying \
the introduction marker (e.g. `v2.1-R067`). Review notes raised against \
existing questions land in the catalogue row's `review_note` column — \
the column added by migration M42 — preserving the audit trail of \
wording and validity observations that prior versions had no schema \
home for."""

PROSE_V2["prog_data_obslog_pipeline"] = """Architecture v2 introduces a structured pipeline by which Session B \
analytical work is captured into the database. Where the patch flow \
moved discrete database changes from AI to CC, the obslog flow moves \
analytical content — observations, Q&A pairs, chapters, SD pointers, \
anchor-verse readings, new questions, review notes — from a \
comprehensive obslog `.md` to its DB target tables in a single \
transactional pass.

The pipeline runs in three phases. Phase 1 is parsing: Claude Code \
reads the obslog and produces a structured manifest in JSON, validated \
for completeness against declared counts. Phase 2 is writing: each \
manifest category is dispatched to its target table — observations \
become `wa_session_b_findings` rows, Q&A pairs become \
`wa_finding_catalogue_links` rows with entity links to verses and \
groups and dimensions, chapters become `prose_section` rows under \
section_type codes `sb_s2c_ch1` through `sb_s2c_ch5`, anchor-verse \
analytical readings update `verse_context.analysis_note`, new \
questions enter `wa_obs_question_catalogue`, review notes append to \
existing catalogue rows, and SD pointers and status updates land in \
their respective tables. Phase 3 is validation and anomaly raising: \
post-write, Claude Code verifies row counts, foreign-key integrity, \
and the catalogue-link coherence; data inconsistencies surface as \
`DATA_ANOMALY_*` findings at `status='open'`, carried into the next \
analytical session for AI to address.

Idempotency is structural. The writer's per-category logic checks for \
existing rows before inserting — re-running on the same obslog produces \
no duplicates. The pipeline is transactional: pre-write backup, \
single-transaction commit, all-or-nothing on failure. The schema \
supports this with M40 through M43, the four migrations that landed \
the architecture: a `verse_context.analysis_note` column for anchor-\
verse commentary, a `wa_prose_section_citations` table for the chapter-\
to-evidence audit trail, a `wa_obs_question_catalogue.review_note` \
column for catalogue maintenance, and a `wa_finding_catalogue_links.finding_id` \
nullability change to support the no-finding and not-applicable \
coverage states.

A revision session adds one further discipline: every chapter affected \
by the revision is superseded under v2.7 / v2.CC9, with citation-\
disciplined prose covering the newly-resolved findings. Claude Code's \
writer detects `SUPERSEDE: sb_s2c_ch{n}` blocks in the obslog, retires \
the prior `prose_section` row via the `superseded_by_id` chain, writes \
the new row at incremented version, and extracts inline citations into \
`wa_prose_section_citations` with FK resolution to findings, SD \
pointers, and Q&A links. A four-check coherence audit at session close \
verifies that every revision-resolved finding is cited, that every \
chapter that should be superseded has been, that citation FK resolution \
clears a 90% threshold per chapter, and that every anchor verse \
appears in at least one current chapter prose body. Failures surface \
as `DATA_ANOMALY_*` findings for the next session.

Two further artefacts complete the pipeline. The readiness `.md` and \
`.json`, generated before the analytical session, present every data \
field in the registry's current state with a clear destination and a \
prompt for the analyst — the field-level destination audit guarantees \
that nothing the readiness presents is silently passed over. The \
analytic status `.md`, generated for revision sessions, captures the \
prior analytical state — lifecycle summary, resolved Q&A pairs, \
resolved SD pointers, prior chapters, anchor analyses, open items — \
so that revision work has both the current data and the prior analysis \
in view. Together the readiness output, the obslog, and the analytic \
status form a closed loop: data state in, analytical work, capture to \
DB, anomalies surfaced for next session, revision input ready."""


def fetch_current_prose(conn, code: str):
    return conn.execute("""
        SELECT ps.id, ps.section_type_id, ps.body, ps.version, ps.heading
          FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
         WHERE pst.code = ?
           AND ps.registry_id IS NULL
           AND ps.superseded_by_id IS NULL
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
         LIMIT 1
    """, (code,)).fetchone()


def supersede_prose(conn, code: str, new_body: str, ts: str, source_file: str,
                    body_transform=None, dry: bool = True):
    """Supersede the current prose row for `code` with `new_body`.

    body_transform: optional callable(prior_body) -> new_body.
    Used for prog_disc_two_ai (keep first 3 paragraphs) and prog_data_questions
    (keep first 2 paragraphs) where v2 prose is appended to a v1 stem.
    """
    row = fetch_current_prose(conn, code)
    if not row:
        return {"action": "skipped", "reason": f"no current prose_section for code '{code}'"}
    prior_id, section_type_id, prior_body, prior_version, prior_heading = row[0], row[1], row[2], row[3], row[4]

    if body_transform:
        body = body_transform(prior_body)
    else:
        body = new_body

    if (prior_body or "").strip() == (body or "").strip():
        return {"action": "skipped", "reason": "body unchanged (idempotent)"}

    new_version = prior_version + 1

    if dry:
        return {"action": "would_supersede", "prior_id": prior_id, "new_version": new_version,
                "prior_len": len(prior_body or ""), "new_len": len(body),
                "section_type_id": section_type_id}

    cursor = conn.execute("""
        INSERT INTO prose_section
            (registry_id, section_type_id, heading, body, status,
             version, supersedes_id, author, source_file, created_at)
        VALUES (NULL, ?, ?, ?, 'draft', ?, ?, 'claude_code', ?, ?)
    """, (section_type_id, prior_heading, body, new_version, prior_id,
          source_file, ts))
    new_id = cursor.lastrowid
    conn.execute("""
        UPDATE prose_section
           SET superseded_by_id = ?, status = 'archived'
         WHERE id = ?
    """, (new_id, prior_id))
    return {"action": "superseded", "prior_id": prior_id, "new_id": new_id,
            "new_version": new_version, "new_len": len(body)}


def transform_two_ai(prior_body: str) -> str:
    """Keep first 3 paragraphs of v1 prog_disc_two_ai; append v2 closing."""
    paras = prior_body.split("\n\n")
    keep = paras[:3]  # first 3 paragraphs unchanged
    return "\n\n".join(keep) + "\n\n" + PROSE_V2_TWO_AI_CLOSING


def transform_questions(prior_body: str) -> str:
    """Keep first 2 paragraphs of v1 prog_data_questions; append v2 lifecycle block."""
    paras = prior_body.split("\n\n")
    keep = paras[:2]
    return "\n\n".join(keep) + "\n\n" + PROSE_V2_QUESTIONS_TAIL


def insert_new_section_type_and_prose(conn, ts: str, source_file: str, dry: bool):
    """Insert prose_section_type for prog_data_obslog_pipeline + matching prose_section row."""
    code = "prog_data_obslog_pipeline"
    existing = conn.execute(
        "SELECT id FROM prose_section_type WHERE code = ?", (code,)
    ).fetchone()
    if existing:
        section_type_id = existing[0]
        st_action = "exists"
    elif dry:
        section_type_id = None
        st_action = "would_insert"
    else:
        cur = conn.execute("""
            INSERT INTO prose_section_type
                (code, label, source_stage, lifecycle_tag, chapter_no,
                 description, expected_length_min, expected_length_max,
                 sort_order, delete_flagged, created_at)
            VALUES (?, 'Programme — Obslog-to-DB capture pipeline', 'programme',
                    NULL, 4,
                    'Architecture v2 obslog→DB pipeline: parse → write → audit. Companion to prog_data_database in chapter 4 (data architecture).',
                    2500, 3500, 31, 0, ?)
        """, (code, ts))
        section_type_id = cur.lastrowid
        st_action = "inserted"

    body = PROSE_V2["prog_data_obslog_pipeline"]

    if section_type_id:
        existing_ps = conn.execute("""
            SELECT id FROM prose_section
             WHERE section_type_id = ? AND registry_id IS NULL
               AND superseded_by_id IS NULL
               AND (delete_flagged = 0 OR delete_flagged IS NULL)
        """, (section_type_id,)).fetchone()
        if existing_ps:
            return {"section_type": st_action, "prose_section": "exists"}

    if dry:
        return {"section_type": st_action, "prose_section": "would_insert", "body_len": len(body)}

    conn.execute("""
        INSERT INTO prose_section
            (registry_id, section_type_id, heading, body, status,
             version, author, source_file, created_at)
        VALUES (NULL, ?, 'Programme — Obslog-to-DB capture pipeline', ?, 'draft',
                1, 'claude_code', ?, ?)
    """, (section_type_id, body, source_file, ts))
    return {"section_type": st_action, "prose_section": "inserted",
            "section_type_id": section_type_id, "body_len": len(body)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR, f"bible_research_pre_prose_v2_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    ts = now_iso()
    source_file = "programme-prose-v2-recommendations-v1-20260427.md"

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        if args.live:
            conn.execute("BEGIN")

        results = {}

        # 1. Insert new section_type + prose_section for prog_data_obslog_pipeline
        results["prog_data_obslog_pipeline"] = insert_new_section_type_and_prose(
            conn, ts, source_file, dry=not args.live,
        )

        # 2. Supersede 4 existing programme prose sections
        results["prog_instr_session_b_readiness"] = supersede_prose(
            conn, "prog_instr_session_b_readiness",
            PROSE_V2["prog_instr_session_b_readiness"],
            ts, source_file, dry=not args.live,
        )
        results["prog_instr_session_b_output"] = supersede_prose(
            conn, "prog_instr_session_b_output",
            PROSE_V2["prog_instr_session_b_output"],
            ts, source_file, dry=not args.live,
        )
        results["prog_disc_two_ai"] = supersede_prose(
            conn, "prog_disc_two_ai", "",  # body computed from v1 stem
            ts, source_file, body_transform=transform_two_ai,
            dry=not args.live,
        )
        results["prog_data_questions"] = supersede_prose(
            conn, "prog_data_questions", "",
            ts, source_file, body_transform=transform_questions,
            dry=not args.live,
        )

        if args.live:
            conn.commit()
            print("[LIVE] committed.\n")
        else:
            print("[DRY-RUN] no writes attempted.\n")

    finally:
        conn.close()

    print("--- Summary ---")
    for code, info in results.items():
        print(f"  {code:42s}: {info}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
