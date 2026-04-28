"""_pilot_build_readiness_output_v1_20260426.py

Pilot generator for the Analysis Readiness Output `.md`, per
vc-corrective-strategy-v2 §4.

Reads a registry from the live DB and renders the canonical .md structure
(8 sections per §10.4 of the pivot proposal):

  1. Registry overview
  2. Term inventory (OWNER)
  3. Legacy-VC terms — UNVERIFIED UNDER v3 CONTRACTS
  4. v3-confirmed terms
  5. Cross-registry context
  6. Open flags carried forward
  7. Verbatim verse text
  8. Readiness verification

Pilot scope: read-only, file output only. No DB writes. No prose-store
write yet (that comes after the `.md` shape is settled).

Usage:
  python scripts/_pilot_build_readiness_output_v1_20260426.py --registry 67

Output:
  Sessions/Session_B/09_Analysis_output_logs/words/wa-{NNN}-{word}-readiness-output-v1-{YYYYMMDD}.md
"""
from __future__ import annotations
import argparse
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Sessions", "Session_B", "07_Analysis_Readiness_Status")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def open_db(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_registry(conn, no: int) -> dict:
    r = conn.execute("""
        SELECT id, no, word, verse_context_status, session_b_status,
               dim_review_status, dim_review_version, cluster_assignment,
               sb_classification, sb_classification_reasoning,
               carry_forward, inference_note, word_synopsis,
               phase1_status, phase1_term_count, phase1_verse_count
          FROM word_registry WHERE no = ?
    """, (no,)).fetchone()
    if r is None:
        raise SystemExit(f"Registry {no} not found")
    return dict(r)


def get_owner_terms(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT mt.id AS mti, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status, mt.vc_status, mt.md_version,
               ti.id AS ti_id, ti.term_owner_type
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND mt.delete_flagged = 0
           AND mt.status NOT IN ('delete', 'excluded')
         ORDER BY mt.language DESC, mt.strongs_number
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_xref_terms(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT mt.id AS mti, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status, mt.vc_status,
               ti.id AS ti_id,
               -- find the OWNER registry for this strongs
               (SELECT wr2.no || ' ' || wr2.word FROM wa_term_inventory ti2
                  JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
                  JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
                 WHERE ti2.strongs_number = mt.strongs_number
                   AND ti2.term_owner_type = 'OWNER'
                   AND ti2.delete_flagged = 0 LIMIT 1) AS owner_registry
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'XREF'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND mt.delete_flagged = 0
           AND mt.status NOT IN ('delete', 'excluded')
         ORDER BY mt.strongs_number
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_term_state(conn, mti_id: int, ti_id: int) -> dict:
    """Per-term verse / group / vc-row counts and the active groups."""
    counts = conn.execute("""
        SELECT
          (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id=? AND vr.delete_flagged=0) AS verses_active,
          (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id=? AND vr.delete_flagged=1) AS verses_deleted,
          (SELECT COUNT(*) FROM verse_context_group g WHERE g.mti_term_id=? AND g.delete_flagged=0) AS groups_active,
          (SELECT COUNT(*) FROM verse_context_group g WHERE g.mti_term_id=? AND g.delete_flagged=1) AS groups_dissolved,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0) AS vc_rows_active,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0 AND vc.is_relevant=1) AS vc_relevant,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0 AND vc.is_relevant=0 AND vc.set_aside_reason IS NOT NULL) AS vc_set_aside
    """, (ti_id, ti_id, mti_id, mti_id, mti_id, mti_id, mti_id)).fetchone()

    groups = conn.execute("""
        SELECT id, group_code, context_description, notes,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = vcg.id AND vc.delete_flagged=0 AND vc.is_relevant=1) AS rel_n,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = vcg.id AND vc.delete_flagged=0 AND vc.is_anchor=1) AS anchor_n
          FROM verse_context_group vcg
         WHERE mti_term_id = ? AND delete_flagged = 0
         ORDER BY group_code
    """, (mti_id,)).fetchall()

    return {**dict(counts), "groups": [dict(g) for g in groups]}


def get_term_verses(conn, ti_id: int, mti_id: int) -> list:
    """All active verses for this term, with their verse_context state."""
    rows = conn.execute("""
        SELECT vr.id AS vr_id, vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               vr.verse_text, vr.target_word, vr.span_strong_match,
               vc.id AS vc_id, vc.is_relevant, vc.is_anchor, vc.is_related,
               vc.set_aside_reason, vc.notes,
               g.group_code
          FROM wa_verse_records vr
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                    AND vc.mti_term_id = ?
                                    AND vc.delete_flagged = 0
          LEFT JOIN verse_context_group g ON g.id = vc.group_id
         WHERE vr.term_inv_id = ?
           AND vr.delete_flagged = 0
         ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (mti_id, ti_id)).fetchall()
    return [dict(r) for r in rows]


def get_open_flags(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT flag_code, flag_label, priority, session_target, raised_date,
               session_raised, description
          FROM wa_session_research_flags
         WHERE registry_id = ?
           AND (resolved = 0 OR resolved IS NULL)
         ORDER BY priority DESC, id
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_schema_version(conn) -> str:
    r = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    return r[0] if r else "unknown"


def render_term_block(term: dict, state: dict, label: str) -> list:
    """One block per term — used for both legacy-VC and v3-confirmed sections."""
    L = []
    L.append(f"#### `{term['strongs_number']}` — {term['transliteration'] or ''} \"{term['gloss'] or ''}\"")
    L.append("")
    L.append(f"- **mti_term_id:** `{term['mti']}` · **language:** {term['language']} · **status:** `{term['status']}`")
    L.append(f"- **vc_status:** `{term['vc_status'] or 'NULL'}` · **md_version:** `{term['md_version'] or '-'}`")
    L.append(f"- **Verses:** {state['verses_active']} active, {state['verses_deleted']} deleted")
    L.append(f"- **Active groups:** {state['groups_active']} · dissolved: {state['groups_dissolved']}")
    L.append(f"- **verse_context rows:** {state['vc_rows_active']} active "
             f"({state['vc_relevant']} relevant · {state['vc_set_aside']} set-aside)")
    if state['groups']:
        L.append("")
        L.append("**Active groups:**")
        L.append("")
        for g in state['groups']:
            L.append(f"- `{g['group_code']}` — {g['rel_n']} relevant · {g['anchor_n']} anchor verse(s)")
            desc = (g['context_description'] or '').strip()
            if desc:
                L.append(f"  - *{desc}*")
            if g['notes']:
                L.append(f"  - notes: {g['notes']}")
    L.append("")
    return L


def render_verses_for_term(term: dict, verses: list) -> list:
    L = []
    L.append(f"### `{term['strongs_number']}` — {term['transliteration'] or ''} \"{term['gloss'] or ''}\" "
             f"({len([v for v in verses if v.get('vc_id')])} classified / {len(verses)} verses)")
    L.append("")
    if not verses:
        L.append("_No active verses._")
        L.append("")
        return L
    # Group by group_code for readability (set-asides go last)
    by_group: dict = defaultdict(list)
    for v in verses:
        key = v.get('group_code') or ('SET-ASIDE' if v.get('vc_id') and v['is_relevant'] == 0 else 'UNCLASSIFIED')
        by_group[key].append(v)
    # Sort: real group codes first, then SET-ASIDE, then UNCLASSIFIED
    def sort_key(k):
        if k == 'UNCLASSIFIED': return (2, k)
        if k == 'SET-ASIDE': return (1, k)
        return (0, k)
    for group_key in sorted(by_group.keys(), key=sort_key):
        items = by_group[group_key]
        L.append(f"**Group `{group_key}`** ({len(items)} verse{'s' if len(items)!=1 else ''})")
        L.append("")
        for v in items:
            anchor = " 🔵" if v.get('is_anchor') else ""
            relevant = "✓" if v.get('is_relevant') == 1 else ("✗" if v.get('is_relevant') == 0 else "—")
            sa = f" [set_aside: {v['set_aside_reason']}]" if v.get('set_aside_reason') else ""
            target = f" *target: {v['target_word']}*" if v.get('target_word') else ""
            L.append(f"- **{v['reference']}**{anchor} ({relevant}){sa}{target}")
            text = (v.get('verse_text') or '').strip().replace('\n', ' ')
            if text:
                L.append(f"  > {text}")
            if v.get('notes'):
                L.append(f"  - notes: {v['notes']}")
        L.append("")
    return L


def build(conn, registry_no: int) -> str:
    reg = get_registry(conn, registry_no)
    owners = get_owner_terms(conn, reg['id'])
    xrefs = get_xref_terms(conn, reg['id'])
    flags = get_open_flags(conn, reg['id'])
    schema = get_schema_version(conn)
    ts = now_iso()
    today = today_compact()

    # Per-term state
    states = {}
    for t in owners + xrefs:
        states[t['mti']] = get_term_state(conn, t['mti'], t['ti_id'])

    # Partition owners by vc_status
    legacy_owners = [t for t in owners if (t['vc_status'] or 'not_done') in ('not_done', 'to_revise')]
    v3_owners = [t for t in owners if t['vc_status'] == 'vc_completed']

    L: list[str] = []

    # Header
    L.append(f"# wa-{registry_no:03d}-{reg['word']} — Analysis Readiness Output")
    L.append("")
    L.append(f"_Pilot generation · v1 · {ts} · schema {schema}_")
    L.append("")
    L.append(f"_Strategy: vc-corrective-strategy-v2 §4 · pilot per execution-roadmap step 2_")
    L.append("")
    L.append(f"_Source of truth: live DB at generation time. Regenerate to refresh._")
    L.append("")
    L.append("---")
    L.append("")

    # 1. Registry overview
    L.append("## 1. Registry overview")
    L.append("")
    L.append(f"- **Registry no:** {reg['no']}")
    L.append(f"- **Word:** {reg['word']}")
    L.append(f"- **verse_context_status:** `{reg['verse_context_status'] or 'NULL'}`")
    L.append(f"- **session_b_status:** `{reg['session_b_status'] or 'NULL'}`")
    L.append(f"- **dim_review_status:** `{reg['dim_review_status'] or 'NULL'}` "
             f"(version `{reg['dim_review_version'] or '-'}`)")
    L.append(f"- **cluster_assignment:** `{reg['cluster_assignment'] or 'NULL'}`")
    L.append(f"- **sb_classification:** `{reg['sb_classification'] or 'NULL'}`")
    L.append(f"- **carry_forward:** `{reg['carry_forward']}`")
    L.append(f"- **phase1_status:** `{reg['phase1_status'] or 'NULL'}` "
             f"(phase1_term_count={reg['phase1_term_count'] or 0}, "
             f"phase1_verse_count={reg['phase1_verse_count'] or 0})")
    L.append("")
    if reg['inference_note']:
        L.append("**Researcher inference_note (verbatim):**")
        L.append("")
        for line in (reg['inference_note'] or '').split('\n'):
            L.append(f"> {line}")
        L.append("")
    if reg['word_synopsis']:
        L.append("**Researcher word_synopsis (verbatim):**")
        L.append("")
        for line in (reg['word_synopsis'] or '').split('\n'):
            L.append(f"> {line}")
        L.append("")
    if reg['sb_classification_reasoning']:
        L.append("**sb_classification_reasoning:**")
        L.append("")
        for line in reg['sb_classification_reasoning'].split('\n'):
            L.append(f"> {line}")
        L.append("")
    L.append("---")
    L.append("")

    # 2. Term inventory (OWNER)
    L.append(f"## 2. Term inventory — OWNER terms ({len(owners)} total: {len(v3_owners)} v3-confirmed, "
             f"{len(legacy_owners)} legacy-VC)")
    L.append("")
    L.append("| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc_rows (rel/sa) |")
    L.append("|---|---|---|---|---|---|---:|---:|---:|---|")
    for t in owners:
        s = states[t['mti']]
        L.append(f"| `{t['strongs_number']}` | {t['transliteration'] or ''} | {(t['gloss'] or '')[:30]} | "
                 f"{t['language'][:1]} | `{t['status']}` | "
                 f"**`{t['vc_status'] or 'NULL'}`** | {t['md_version'] or '-'} | "
                 f"{s['verses_active']} | {s['groups_active']}/{s['groups_dissolved']} | "
                 f"{s['vc_relevant']}/{s['vc_set_aside']} |")
    L.append("")
    L.append("---")
    L.append("")

    # 3. Legacy-VC terms — UNVERIFIED UNDER v3 CONTRACTS
    L.append("## 3. Legacy-VC terms — UNVERIFIED UNDER v3 CONTRACTS")
    L.append("")
    if not legacy_owners:
        L.append("**No legacy-VC terms in this registry.** All OWNER terms are at `vc_status='vc_completed'` — classifications were performed under v3_x contracts.")
        L.append("")
    else:
        L.append(f"**{len(legacy_owners)} term(s) below carry classification rows from pre-v3 work.**")
        L.append("")
        L.append("> **Analytical instruction:** These classifications are legacy. Treat the existing groups, anchor designations, and verse-level set-asides shown below as **the available state of evidence** — facts on the ground. The VC programme has not re-classified these under v3 contracts.")
        L.append(">")
        L.append("> If during analysis you conclude that a finding depends *materially* on a verse classification, group description, or anchor designation from this section — i.e. the finding would change under a plausible alternative classification — emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change.")
        L.append(">")
        L.append("> If the finding is robust to the classification uncertainty, document the legacy-source fact in the finding's audit trail and proceed.")
        L.append("")
        for t in legacy_owners:
            for line in render_term_block(t, states[t['mti']], 'legacy'):
                L.append(line)
    L.append("---")
    L.append("")

    # 4. v3-confirmed terms
    L.append(f"## 4. v3-confirmed terms ({len(v3_owners)})")
    L.append("")
    if not v3_owners:
        L.append("_None._")
        L.append("")
    else:
        L.append("Trusted within v3 grouping doctrine. Materiality protocol does not apply.")
        L.append("")
        for t in v3_owners:
            for line in render_term_block(t, states[t['mti']], 'v3'):
                L.append(line)
    L.append("---")
    L.append("")

    # 5. Cross-registry context
    L.append("## 5. Cross-registry context")
    L.append("")
    L.append(f"### XREF terms in this registry ({len(xrefs)})")
    L.append("")
    if not xrefs:
        L.append("_None._")
    else:
        L.append("| strongs | translit | gloss | OWNER registry | status |")
        L.append("|---|---|---|---|---|")
        for t in xrefs:
            L.append(f"| `{t['strongs_number']}` | {t['transliteration'] or ''} | "
                     f"{(t['gloss'] or '')[:30]} | {t['owner_registry'] or '?'} | `{t['status']}` |")
    L.append("")
    # SD pointers
    sd = conn.execute("""
        SELECT srf.flag_code, srf.flag_label, srf.priority, srf.description
          FROM wa_session_research_flags srf
         WHERE srf.registry_id = ? AND srf.flag_code = 'SD_POINTER'
           AND (srf.resolved = 0 OR srf.resolved IS NULL)
    """, (reg['id'],)).fetchall()
    L.append(f"### SD_POINTER flags ({len(sd)})")
    L.append("")
    if not sd:
        L.append("_None._")
    else:
        for r in sd:
            L.append(f"- **{r['flag_label']}** (priority {r['priority']})")
            if r['description']:
                L.append(f"  - {r['description'][:300]}")
    L.append("")
    L.append("---")
    L.append("")

    # 6. Open flags carried forward
    other_flags = [f for f in flags if f['flag_code'] != 'SD_POINTER']
    L.append(f"## 6. Open flags carried forward ({len(other_flags)})")
    L.append("")
    if not other_flags:
        L.append("_None._")
    else:
        L.append("| flag_code | label | priority | session | raised |")
        L.append("|---|---|---|---|---|")
        for f in other_flags:
            L.append(f"| `{f['flag_code']}` | {(f['flag_label'] or '')[:50]} | "
                     f"{f['priority'] or '-'} | {f['session_target'] or '-'} | {f['raised_date'] or '-'} |")
        L.append("")
        for f in other_flags:
            L.append(f"#### {f['flag_label'] or f['flag_code']}")
            L.append("")
            if f['description']:
                for line in f['description'].split('\n'):
                    L.append(f"> {line}")
            L.append("")
    L.append("---")
    L.append("")

    # 7. Verbatim verse text
    L.append(f"## 7. Verbatim verse text — all OWNER terms")
    L.append("")
    L.append("Each verse listed with its current verse_context state (group_code, relevance, set-aside reason, anchor designation). This is the analyst's primary text source — DB consultation is not needed for verse text.")
    L.append("")
    for t in owners:
        verses = get_term_verses(conn, t['ti_id'], t['mti'])
        for line in render_verses_for_term(t, verses):
            L.append(line)
    L.append("---")
    L.append("")

    # 8. Readiness verification
    L.append("## 8. Readiness verification")
    L.append("")
    L.append(f"- **Generated at:** `{ts}`")
    L.append(f"- **Schema version:** `{schema}`")
    md_versions = sorted({t['md_version'] for t in owners if t['md_version']})
    L.append(f"- **OWNER term md_versions present:** {md_versions or '(none / legacy)'}")
    L.append("")
    # Quick checks
    issues = []
    if reg['verse_context_status'] is None:
        issues.append("verse_context_status is NULL — registry may be excluded.")
    if reg['session_b_status'] == 'Verse Context Reset':
        issues.append("session_b_status is 'Verse Context Reset' — this registry is in the reset cohort and should not be processed under v2 lighter-touch path.")
    L.append("**Stage 1 quick checks:**")
    L.append("")
    L.append(f"- Registry status fields populated: {'✓' if (reg['verse_context_status'] or reg['session_b_status']) else '✗'}")
    L.append(f"- OWNER term inventory non-empty: {'✓' if owners else '✗'}")
    L.append(f"- All OWNER terms have at least 1 verse: "
             f"{'✓' if all(states[t['mti']]['verses_active'] > 0 for t in owners) else '✗'}")
    L.append(f"- Researcher fields preserved (inference_note / word_synopsis): "
             f"{'partial' if (reg['inference_note'] or reg['word_synopsis']) else 'none — researcher narrative absent'}")
    L.append("")
    if issues:
        L.append("**Notes / concerns:**")
        for i in issues:
            L.append(f"- {i}")
        L.append("")

    L.append("---")
    L.append("")
    L.append(f"*End of readiness output — wa-{registry_no:03d}-{reg['word']}.*")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    conn = open_db(args.db)
    md = build(conn, args.registry)
    reg = get_registry(conn, args.registry)
    out_dir = OUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    fname = (args.out or
             f"wa-{args.registry:03d}-{reg['word']}-readiness-output-v1-{today_compact()}.md")
    out_path = os.path.join(out_dir, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    sz = os.path.getsize(out_path)
    print(f"Wrote: {out_path}  ({sz:,} bytes / {sz/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
