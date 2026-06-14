"""Build the goodness (R067) QA list.

For each ACTIVE catalogue question, show what R067 has on file. Three
buckets:
  (a) substantive answer (coverage='full' or 'partial' linked to a finding)
  (b) explicit non-answer (coverage='no_finding' or 'not_applicable',
      with the rationale captured in session_b_note)
  (c) silent — no link row at all between the question and any R067 finding

Section ordering matches the catalogue. Each question shows its full text
followed by R067's answer text (when available) — the answer text is the
finding text from `wa_session_b_findings`, with the catalogue link's
`session_b_note` shown when present.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

OUT = "research/investigations/word_deep_dive/goodness/goodness-4-qa-list.md"


def main() -> int:
    conn = sqlite3.connect(os.path.join("database", "bible_research.db"))
    conn.row_factory = sqlite3.Row

    parts: list[str] = []
    P = parts.append

    P("# Goodness — Q&A List (R067)\n")
    P(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    P("**Source:** `wa_obs_question_catalogue` × `wa_finding_catalogue_links` × `wa_session_b_findings`. Active rows only on both sides; soft-deleted catalogue rows (e.g. the migrated GAP-N / GAP-S series) are excluded.\n")
    P("**Scope filter:** universal generic sections (Sections 1–5), the Q-COV evidence-flag set, and the word's own Extensions section. Word-specific Extensions belonging to other registries (Compassion / Forgiveness / Love / Mercy Extensions) are excluded by design — they don't apply to goodness.\n")

    # In-scope filter: Sections 1-5 + Q-COV + Goodness Extensions
    SCOPE_FILTER = """
        (deleted = 0 OR deleted IS NULL)
        AND (
            section LIKE 'Section %'
            OR section = 'Evidence-Flag Research Questions'
            OR section = 'Goodness Extensions'
        )
    """
    # Counts
    n_active_q = conn.execute(
        f"SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE {SCOPE_FILTER}",
    ).fetchone()[0]
    n_excluded = conn.execute(
        """
        SELECT COUNT(*) FROM wa_obs_question_catalogue
        WHERE (deleted = 0 OR deleted IS NULL)
        AND section IN ('Compassion Extensions','Forgiveness Extensions','Love Extensions','Mercy Extensions')
        """,
    ).fetchone()[0]
    P(f"_In-scope: {n_active_q} questions.  Excluded as out-of-scope: {n_excluded} questions (other words' Extensions)._\n")
    n_links = conn.execute(
        f"""
        SELECT COUNT(*) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        WHERE f.registry_id = 67 AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        AND {SCOPE_FILTER.replace('deleted', 'q.deleted').replace('section', 'q.section')}
        """,
    ).fetchone()[0]
    n_full = conn.execute(
        f"""
        SELECT COUNT(DISTINCT l.question_id) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        WHERE f.registry_id = 67 AND l.coverage IN ('full','partial')
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        AND {SCOPE_FILTER.replace('deleted', 'q.deleted').replace('section', 'q.section')}
        """,
    ).fetchone()[0]
    n_nonans = conn.execute(
        f"""
        SELECT COUNT(DISTINCT l.question_id) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        WHERE f.registry_id = 67 AND l.coverage IN ('no_finding','not_applicable')
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        AND {SCOPE_FILTER.replace('deleted', 'q.deleted').replace('section', 'q.section')}
        """,
    ).fetchone()[0]
    n_questions_addressed = conn.execute(
        f"""
        SELECT COUNT(DISTINCT l.question_id) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        WHERE f.registry_id = 67 AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        AND {SCOPE_FILTER.replace('deleted', 'q.deleted').replace('section', 'q.section')}
        """,
    ).fetchone()[0]
    n_silent = n_active_q - n_questions_addressed
    P(f"**Coverage summary** (against {n_active_q} active catalogue questions):\n")
    P(f"- Substantive answer (full/partial): **{n_full}** questions")
    P(f"- Explicit non-answer (no_finding / not_applicable): **{n_nonans}** questions")
    P(f"- Silent (no link row at all): **{n_silent}** questions")
    P(f"- Total Q&A finding-catalogue link rows for R067: **{n_links}**\n")

    # Walk catalogue ordered by section, in-scope only
    sections = conn.execute(
        f"""
        SELECT DISTINCT section
        FROM wa_obs_question_catalogue
        WHERE {SCOPE_FILTER}
        ORDER BY section
        """,
    ).fetchall()

    for sec in sections:
        section = sec["section"]
        questions = conn.execute(
            f"""
            SELECT q.obs_id, q.question_code, q.question_text, q.scope, q.source_word, q.source_registry_no
            FROM wa_obs_question_catalogue q
            WHERE q.section = ?
            AND {SCOPE_FILTER.replace('deleted', 'q.deleted').replace('section', 'q.section')}
            ORDER BY q.question_code, q.obs_id
            """,
            (section,),
        ).fetchall()
        # Count R67 coverage in this section
        n_section_full = 0
        n_section_nonans = 0
        n_section_silent = 0
        for q in questions:
            cov = conn.execute(
                """
                SELECT l.coverage FROM wa_finding_catalogue_links l
                JOIN wa_session_b_findings f ON f.id = l.finding_id
                WHERE f.registry_id = 67 AND l.question_id = ?
                AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                """,
                (q["obs_id"],),
            ).fetchall()
            covs = [c["coverage"] for c in cov]
            if any(c in ("full", "partial") for c in covs):
                n_section_full += 1
            elif any(c in ("no_finding", "not_applicable") for c in covs):
                n_section_nonans += 1
            else:
                n_section_silent += 1
        P(f"\n## {section}")
        P(f"_{len(questions)} questions · R067: {n_section_full} answered, {n_section_nonans} non-answer, {n_section_silent} silent_\n")

        # Source-word display: only for Extensions sections (word-specific by
        # section). For universal Sections 1-5 and Q-COV, the source_word
        # field is provenance only (most universal questions are sourced
        # from Grace R068 because they were drafted there first and then
        # promoted to universal scope) — showing "source: Grace" on every
        # universal question reads as if grace questions are being asked of
        # goodness, which is wrong.
        section_is_extension = section.endswith(" Extensions")

        for q in questions:
            scope_tag = ""
            if section_is_extension and q["source_word"] and q["source_registry_no"]:
                scope_tag = f" · source word: R{q['source_registry_no']:03d} {q['source_word']}"
            elif q["scope"] and q["scope"] not in ("universal", None):
                scope_tag = f" · scope: `{q['scope']}`"

            P(f"### {q['question_code']}  (obs_id={q['obs_id']}){scope_tag}")
            P(f"**Q.** {q['question_text']}\n")

            # Pull R67 links + finding text
            links = conn.execute(
                """
                SELECT l.coverage, l.session_b_note, l.pattern_type, l.status,
                       f.finding_id, f.finding, f.finding_type
                FROM wa_finding_catalogue_links l
                JOIN wa_session_b_findings f ON f.id = l.finding_id
                WHERE f.registry_id = 67 AND l.question_id = ?
                AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                ORDER BY l.coverage DESC, f.finding_id
                """,
                (q["obs_id"],),
            ).fetchall()

            if not links:
                P("**R067 answer:** _silent — no link row in `wa_finding_catalogue_links` for this question._\n")
                continue

            # Group by coverage
            by_cov: dict[str, list] = {}
            for l in links:
                by_cov.setdefault(l["coverage"], []).append(l)

            # Substantive first
            for cov in ("full", "partial"):
                if cov not in by_cov:
                    continue
                items = by_cov[cov]
                P(f"**R067 answer ({cov}):**\n")
                # Show session_b_note once if all items share it (the obslog
                # writer typically attaches the same answer text to multiple
                # source findings).
                notes = {l["session_b_note"] for l in items if l["session_b_note"]}
                if len(notes) == 1:
                    P("> " + (notes.pop() or "").replace("\n", "\n> "))
                    P("")
                    P(f"_Sourced from {len(items)} finding(s): " + ", ".join(l["finding_id"] for l in items) + "_\n")
                else:
                    for l in items:
                        if l["session_b_note"]:
                            P(f"_From {l['finding_id']}:_")
                            P("> " + (l["session_b_note"] or "").replace("\n", "\n> "))
                        else:
                            P(f"_From {l['finding_id']}:_  (link row has no session_b_note; finding text:)")
                            P("> " + (l["finding"] or "")[:600].replace("\n", "\n> "))
                        P("")

            for cov in ("no_finding", "not_applicable"):
                if cov not in by_cov:
                    continue
                items = by_cov[cov]
                P(f"**R067 disposition ({cov}):**\n")
                notes = {l["session_b_note"] for l in items if l["session_b_note"]}
                if notes:
                    for n in notes:
                        P("> " + (n or "").replace("\n", "\n> "))
                else:
                    P("_(no rationale captured in session_b_note)_")
                P(f"_Sourced from: " + ", ".join(l["finding_id"] for l in items) + "_\n")

            # Other coverage values
            for cov in by_cov:
                if cov in ("full", "partial", "no_finding", "not_applicable"):
                    continue
                P(f"**R067 link with coverage=`{cov}`:**")
                for l in by_cov[cov]:
                    P(f"- from {l['finding_id']}: {(l['session_b_note'] or '')[:200]}")
                P("")

    out_path = OUT
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"Wrote {out_path} ({sum(len(p) for p in parts):,} chars / {len(parts)} lines)")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
