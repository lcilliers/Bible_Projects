"""Build the goodness (R067) citations list.

For each ACTIVE Session-B finding for R067, show ALL forms of support that
exist in the data, not just the rows in `wa_finding_entity_links`:

  - structured verse / group citations (entity_links rows),
  - catalogue Q&A back-references,
  - DIM-finding ↔ OBS-finding resolution chain (currently captured ONLY in
    finding-text prose because no DIM finding in the DB has its
    `related_finding_id` populated),
  - cross-finding references (one OBS finding referenced by another),
  - inline Strong's-number references in the finding text (term-level
    support that exists but was never extracted to entity_links),
  - inline verse-reference patterns in the finding text (verse-level
    support that exists but was never extracted to entity_links).

The orphan classification at the bottom of each entry only fires when none
of the above is present. This means findings that ARE supported (just not
in the structured way the writer pipeline was supposed to produce) no
longer read as orphans.
"""
from __future__ import annotations

import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

OUT = "research/investigations/word_deep_dive/goodness/goodness-5-citations.md"


STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")
DIM_REF_RE = re.compile(r"\bDIM-\d+-\d+\b")
OBS_REF_RE = re.compile(r"\bOBS-\d{2,3}-(?:OBS-)?\d{2,3}\b")
SP_REF_RE = re.compile(r"\bSP-\d{3}-\d{3}\b")
GAP_REF_RE = re.compile(r"\bGAP-[A-Z0-9]+-\d{3}\b")
QA_REF_RE = re.compile(r"\bQ&?A?-?\d{2,3}\b|\bQ\d{2,3}\b")
GROUP_CODE_RE = re.compile(r"\b\d{3,4}-\d{3}\b")


def find_verse_refs(text: str, book_codes: set[str]) -> list[str]:
    """Return distinct verse references like 'Psa 34:8' or 'Mic 6:8' found in text.

    Uses the `books.short_code` whitelist to avoid false positives like 'Mod 12:34'.
    """
    if not text:
        return []
    out: list[str] = []
    seen: set[str] = set()
    # Pattern: 1-2 digit book prefix optional + 3-letter capitalized code + space + chap:vrs
    pat = re.compile(r"\b(\d?\s?[A-Z][a-z]{2})\s+(\d+):(\d+)(?:[–—\-]\d+)?\b")
    for m in pat.finditer(text):
        code, ch, vs = m.group(1).strip(), m.group(2), m.group(3)
        # Normalise '1 Co' -> '1Co' etc.
        code_norm = code.replace(" ", "")
        if code_norm in book_codes:
            ref = f"{code_norm} {ch}:{vs}"
            if ref not in seen:
                seen.add(ref)
                out.append(ref)
    return out


def main() -> int:
    conn = sqlite3.connect(os.path.join("database", "bible_research.db"))
    conn.row_factory = sqlite3.Row
    book_codes = {
        r["short_code"] for r in conn.execute("SELECT short_code FROM books").fetchall()
    }
    book_codes |= {r["abbreviation"] for r in conn.execute("SELECT abbreviation FROM books").fetchall()}

    # Group code whitelist for this registry (e.g. '884-001', '885-001')
    group_codes = {
        r["group_code"]
        for r in conn.execute(
            """
            SELECT g.group_code
            FROM verse_context_group g
            JOIN mti_terms mt ON mt.id = g.mti_term_id
            WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = 67)
            AND (g.delete_flagged = 0 OR g.delete_flagged IS NULL)
            """,
        ).fetchall()
    }

    # Term transliteration whitelist for this registry (OWNER + XREF)
    term_translits = conn.execute(
        """
        SELECT DISTINCT ti.term_id, ti.transliteration
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.registry_id = 67
        AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
        AND ti.transliteration IS NOT NULL AND ti.transliteration != ''
        """,
    ).fetchall()
    # Filter out very short transliterations that would produce false positives
    term_translit_map = {
        r["transliteration"]: r["term_id"] for r in term_translits
        if r["transliteration"] and len(r["transliteration"]) >= 4
    }

    parts: list[str] = []
    P = parts.append

    P("# Goodness — Citations List (R067)\n")
    P(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    P("**Sources:** `wa_session_b_findings` × `wa_finding_entity_links` × `wa_verse_records` × `verse_context_group` × `wa_finding_catalogue_links`.\n")
    P("Each entry in this file is a Session B finding for R067, with every form of support shown:\n")
    P("- **Cited verses (structured)** — `wa_finding_entity_links` with `entity_type='verse'`. Verse text reproduced verbatim.")
    P("- **Cited groups (structured)** — `entity_type='group'` links with the group's description.")
    P("- **Catalogue Q&A back-references** — `wa_finding_catalogue_links` rows pointing to this finding.")
    P("- **Resolved by / Resolves** — for DIM-N-NNN findings, the OBS finding(s) whose text references this DIM as resolved. (The pipeline never populates `wa_session_b_findings.related_finding_id` so this chain is recovered by text-scanning the OBS finding bodies — see §0 below.)")
    P("- **Cross-finding references** — other OBS findings whose text mentions this finding's id.")
    P("- **Strong's references in body** — Strong's numbers appearing in the finding text but not extracted to structured links.")
    P("- **Verse references in body** — verse-pattern hits in the finding text but not extracted to structured links.")
    P("- **Orphan** — only when none of the above exists.\n")
    P("Findings are listed in type order then `finding_id`. DIM-67-* and DATA_ANOMALY_* findings appear alongside OBS-067-* findings.\n")
    P("## §0. Method note on text-scan support recovery\n")
    P("`wa_session_b_findings.related_finding_id`, `superseded_by_id`, and `resolution_note` are populated on **0 of 146** DIMENSION_REVIEW findings DB-wide. The DIM ↔ OBS resolution chain is therefore captured exclusively in the prose of OBS finding bodies (e.g. an OBS body whose first sentence is `\"DIM-67-001: core analytical question — ...\"` is the resolving finding for DIM-67-001). This report scans for that pattern and reports it as supporting evidence so DIM findings are not misclassified as orphan. Same approach for inline Strong's and verse references that the writer left in prose instead of extracting to `wa_finding_entity_links` — they are real support, just not structured.\n")
    P("---\n")

    # Counts
    n_total = conn.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id = 67 AND delete_flag = 0",
    ).fetchone()[0]
    n_with_verses = conn.execute(
        """
        SELECT COUNT(DISTINCT f.id) FROM wa_session_b_findings f
        JOIN wa_finding_entity_links l ON l.finding_id = f.id AND l.entity_type = 'verse'
        WHERE f.registry_id = 67 AND f.delete_flag = 0
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        """,
    ).fetchone()[0]
    n_with_groups = conn.execute(
        """
        SELECT COUNT(DISTINCT f.id) FROM wa_session_b_findings f
        JOIN wa_finding_entity_links l ON l.finding_id = f.id AND l.entity_type = 'group'
        WHERE f.registry_id = 67 AND f.delete_flag = 0
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        """,
    ).fetchone()[0]
    n_uncited = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_b_findings f
        WHERE f.registry_id = 67 AND f.delete_flag = 0
        AND f.finding_type = 'OBSERVATION'
        AND NOT EXISTS (
            SELECT 1 FROM wa_finding_entity_links l
            WHERE l.finding_id = f.id
            AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        )
        """,
    ).fetchone()[0]
    P(f"**Structured-link counts:** {n_total} active findings  ·  {n_with_verses} with verse citations  ·  {n_with_groups} with group citations  ·  {n_uncited} OBSERVATION findings with no entity-link rows at all.\n")
    P("_The text-scan recovery in this report reclassifies most of those uncited findings as supported via at least one of: DIM↔OBS resolution chain, inbound cross-finding reference, outbound cross-finding reference, inline Strong's number, term transliteration match, inline verse reference, or inline group-code reference. The truly orphan count appears in §X at the foot of this file._\n")
    P("\n---\n")

    findings = conn.execute(
        """
        SELECT id, finding_id, finding_type, status, raised_date, finding,
               anchor_verses, thin_evidence
        FROM wa_session_b_findings
        WHERE registry_id = 67 AND delete_flag = 0
        ORDER BY
            CASE finding_type
                WHEN 'DIMENSION_REVIEW' THEN 0
                WHEN 'OBSERVATION' THEN 1
                ELSE 2
            END,
            finding_id
        """,
    ).fetchall()

    # Build a finding-id → row map of all R067 findings for cross-reference scanning.
    by_fid = {f["finding_id"]: f for f in findings}

    truly_orphan: list[str] = []

    for f in findings:
        P(f"## {f['finding_id']}  ·  {f['finding_type']}  ·  status `{f['status']}`")
        meta = f"_Raised {f['raised_date']}._"
        if f["thin_evidence"]:
            meta += "  **thin_evidence=1**"
        P(meta + "\n")

        P("**Finding.**\n")
        P("> " + (f["finding"] or "_(empty)_").replace("\n", "\n> "))
        P("")

        if f["anchor_verses"]:
            P(f"**`anchor_verses` field:** `{f['anchor_verses']}`\n")

        # Cited verses
        verses = conn.execute(
            """
            SELECT vr.id, vr.reference, vr.verse_text, vr.target_word, vr.term_id, vr.transliteration
            FROM wa_finding_entity_links l
            JOIN wa_verse_records vr ON vr.id = l.entity_id
            WHERE l.finding_id = ? AND l.entity_type = 'verse'
            AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
            ORDER BY vr.book_id, vr.chapter, vr.verse_num
            """,
            (f["id"],),
        ).fetchall()
        if verses:
            P(f"**Cited verses ({len(verses)}):**\n")
            seen_refs = set()
            for v in verses:
                if v["reference"] in seen_refs:
                    continue
                seen_refs.add(v["reference"])
                txt = (v["verse_text"] or "").replace("\n", " ").strip()
                P(f"- **{v['reference']}** ({v['term_id']} *{v['transliteration']}*) — {txt}")
            P("")

        # Cited groups
        groups = conn.execute(
            """
            SELECT g.group_code, g.context_description, mt.strongs_number
            FROM wa_finding_entity_links l
            JOIN verse_context_group g ON g.id = l.entity_id
            JOIN mti_terms mt ON mt.id = g.mti_term_id
            WHERE l.finding_id = ? AND l.entity_type = 'group'
            AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
            ORDER BY g.group_code
            """,
            (f["id"],),
        ).fetchall()
        if groups:
            P(f"**Cited groups ({len(groups)}):**\n")
            for g in groups:
                P(f"- **{g['group_code']}** ({g['strongs_number']}) — {g['context_description']}")
            P("")

        # Catalogue Q&A links
        qa = conn.execute(
            """
            SELECT q.question_code, q.question_text, l.coverage, l.session_b_note, q.section, q.deleted
            FROM wa_finding_catalogue_links l
            JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
            WHERE l.finding_id = ?
            AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
            ORDER BY q.question_code
            """,
            (f["id"],),
        ).fetchall()
        if qa:
            P(f"**Catalogue Q&A links ({len(qa)}):**\n")
            for q in qa:
                tag = ""
                if q["deleted"]:
                    tag = " *(catalogue row soft-deleted)*"
                P(f"- **{q['question_code']}** [{q['coverage']}]{tag} — {(q['question_text'] or '')[:160]}")
            P("")

        # --- Text-scan support recovery ---
        # 1) DIM ← OBS resolution chain: if this is a DIM, find OBS findings
        #    in the same registry whose body text mentions this finding_id.
        #    If this is an OBS, find DIM findings whose id this OBS resolves.
        resolves_chain: list[str] = []
        if f["finding_type"] == "DIMENSION_REVIEW" and f["finding_id"]:
            for other_fid, other in by_fid.items():
                if other_fid == f["finding_id"]:
                    continue
                if other["finding_type"] != "OBSERVATION":
                    continue
                if other["finding"] and f["finding_id"] in other["finding"]:
                    resolves_chain.append(other_fid)
        resolves_dim: list[str] = []
        if f["finding_type"] == "OBSERVATION" and f["finding"]:
            for dim_ref in DIM_REF_RE.findall(f["finding"]):
                if dim_ref in by_fid and dim_ref != f["finding_id"]:
                    resolves_dim.append(dim_ref)

        if resolves_chain:
            P(f"**Resolved by ({len(resolves_chain)} OBS finding(s)):** " + ", ".join(resolves_chain) + "\n")
        if resolves_dim:
            P(f"**Resolves DIM finding(s):** " + ", ".join(sorted(set(resolves_dim))) + "\n")

        # 2a) Inbound: other findings whose body mentions this finding's id
        #     (excluding the resolution chain already shown).
        cross_refs_in: list[str] = []
        if f["finding_id"]:
            for other_fid, other in by_fid.items():
                if other_fid == f["finding_id"]:
                    continue
                if other_fid in resolves_chain:
                    continue
                if other["finding"] and f["finding_id"] in other["finding"]:
                    cross_refs_in.append(other_fid)
        if cross_refs_in:
            P(f"**Referenced by ({len(cross_refs_in)} other finding(s)):** " + ", ".join(cross_refs_in[:20]) +
              (f" _(+{len(cross_refs_in) - 20} more)_" if len(cross_refs_in) > 20 else "") + "\n")

        # 2b) Outbound: other findings this body references.
        cross_refs_out: list[str] = []
        if f["finding"]:
            for other_fid in by_fid:
                if other_fid == f["finding_id"]:
                    continue
                if other_fid in resolves_dim:
                    continue
                if other_fid in f["finding"]:
                    cross_refs_out.append(other_fid)
        if cross_refs_out:
            P(f"**References ({len(cross_refs_out)} other finding(s)):** " + ", ".join(cross_refs_out[:20]) +
              (f" _(+{len(cross_refs_out) - 20} more)_" if len(cross_refs_out) > 20 else "") + "\n")

        # 3a) Inline Strong's references
        body_strongs: list[str] = []
        if f["finding"]:
            seen_s: set[str] = set()
            for m in STRONGS_RE.findall(f["finding"]):
                if m not in seen_s:
                    seen_s.add(m)
                    body_strongs.append(m)
        if body_strongs:
            P(f"**Strong's references in body:** " + ", ".join(body_strongs) + "\n")

        # 3b) Term transliteration matches (e.g. 'agathos', 'agathōsunē')
        body_translits: list[str] = []
        if f["finding"]:
            for tl, term_id in term_translit_map.items():
                if tl in f["finding"] and term_id not in body_strongs:
                    body_translits.append(f"{tl} ({term_id})")
        if body_translits:
            P(f"**Term transliterations in body:** " + ", ".join(body_translits) + "\n")

        # 4a) Inline verse references not already in the structured cited-verse list
        cited_refs = {v["reference"] for v in verses}
        inline_verses = [v for v in find_verse_refs(f["finding"] or "", book_codes) if v not in cited_refs]
        if inline_verses:
            P(f"**Verse references in body (not in entity_links):** " + ", ".join(inline_verses) + "\n")

        # 4b) Inline group-code references not already in the structured cited-group list
        cited_groups_set = {g["group_code"] for g in groups}
        inline_groups: list[str] = []
        if f["finding"]:
            seen_g: set[str] = set()
            for m in GROUP_CODE_RE.findall(f["finding"]):
                if m in group_codes and m not in cited_groups_set and m not in seen_g:
                    seen_g.add(m)
                    inline_groups.append(m)
        if inline_groups:
            P(f"**Group references in body (not in entity_links):** " + ", ".join(inline_groups) + "\n")

        # 5) Orphan check
        any_support = (
            verses or groups or qa or resolves_chain or resolves_dim
            or cross_refs_in or cross_refs_out or body_strongs
            or body_translits or inline_verses or inline_groups
        )
        if not any_support:
            P("_(no structured links and no body-text references — truly orphan)_\n")
            truly_orphan.append(f["finding_id"])

        P("---\n")

    if truly_orphan:
        P(f"\n## §X. Truly orphan findings ({len(truly_orphan)})\n")
        P("Findings with no support in any of the seven categories above. These are the findings that warrant follow-up — distinct from the larger group whose support is real but unstructured.\n")
        for fid in truly_orphan:
            P(f"- {fid}")
    else:
        P("\n## §X. Truly orphan findings (0)\n_All findings carry support in at least one form (structured or text-recovered)._\n")

    out_path = OUT
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"Wrote {out_path} ({sum(len(p) for p in parts):,} chars / {len(parts)} lines)")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
