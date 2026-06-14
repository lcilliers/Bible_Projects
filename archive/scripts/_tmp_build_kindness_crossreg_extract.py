"""_tmp_build_kindness_crossreg_extract.py

Implements DIR-20260501-001 — read-only cross-registry term extract for
R099 kindness Stage 2b. Produces a structured markdown file with per-term
sections A (identity + lexical foundation), B (verse-context groups),
C (anchor verses verbatim), D (all relevant verses verbatim).

Directive: Sessions/Session_B/words/099_kindness/obslog/
           wa-099-kindness-dir-001-crossreg-extract-v1-20260501.md

Output:    Sessions/Session_B/words/099_kindness/inputs/
           wa-099-kindness-crossreg-extract-v1-{YYYYMMDD}.md

Usage:
  python scripts/_tmp_build_kindness_crossreg_extract.py
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Sessions", "Session_B", "words", "099_kindness", "inputs")
TERMS_PRIORITY = [
    ("H2617A", 1, "Primary Hebrew kindness term — 169 corpus verses — essential"),
    ("G5544", 1, "Primary Greek abstract kindness noun — 7 corpus verses — essential"),
    ("H2623", 2, "Person characterised by chesed — 33 corpus verses — strongly recommended"),
    ("H2616A", 2, "Verbal root of chesed — 2 corpus verses — recommended"),
]
H2617_TRUNCATE_AT = 100  # per directive note 4


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def open_db() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def get_owner_term(conn, strongs: str) -> dict | None:
    """Pick the single OWNER row per Strong's (status IN extracted variants;
    owning_registry_fk populated). Excludes XREF copies and delete rows.
    """
    r = conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status, mt.md_version, mt.anchor_note,
               wr.no AS owner_reg_no, wr.word AS owner_word
          FROM mti_terms mt
          JOIN word_registry wr ON wr.id = mt.owning_registry_fk
         WHERE mt.strongs_number = ?
           AND mt.status IN ('extracted', 'extracted_thin')
           AND (mt.delete_flagged = 0 OR mt.delete_flagged IS NULL)
         LIMIT 1
    """, (strongs,)).fetchone()
    return dict(r) if r else None


def get_term_inv_id(conn, mti_id: int, strongs: str) -> int | None:
    """Resolve the matching wa_term_inventory.id (OWNER) for ancillary tables
    that key by term_inv_id (root_family, related_words, meaning_parsed)."""
    r = conn.execute("""
        SELECT ti.id
          FROM wa_term_inventory ti
         WHERE ti.strongs_number = ?
           AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
           AND (ti.term_owner_type IS NULL OR ti.term_owner_type = 'OWNER')
         LIMIT 1
    """, (strongs,)).fetchone()
    if r:
        return r['id']
    # Fallback: any active row for this strongs
    r = conn.execute("""
        SELECT id FROM wa_term_inventory
         WHERE strongs_number = ?
           AND (delete_flagged = 0 OR delete_flagged IS NULL)
         LIMIT 1
    """, (strongs,)).fetchone()
    return r['id'] if r else None


def get_meaning_parse(conn, ti_id: int) -> dict | None:
    if not ti_id:
        return None
    parsed = conn.execute("""
        SELECT id, top_sense_count, stem_count, has_causative_stem,
               has_domain_tags, parsed_at, parse_version
          FROM wa_meaning_parsed
         WHERE term_inv_id = ?
         ORDER BY id DESC LIMIT 1
    """, (ti_id,)).fetchone()
    if not parsed:
        return None
    senses = conn.execute("""
        SELECT level_code, level_depth, parent_level_code, sense_text,
               is_stem_label, stem_label, domain_tag
          FROM wa_meaning_sense
         WHERE parsed_meaning_id = ?
         ORDER BY sort_order, id
    """, (parsed['id'],)).fetchall()
    return {"parsed": dict(parsed), "senses": [dict(s) for s in senses]}


def get_root_family(conn, ti_id: int) -> dict | None:
    if not ti_id:
        return None
    r = conn.execute("""
        SELECT root_code, root_language, root_gloss, note
          FROM wa_term_root_family
         WHERE term_inv_id = ?
           AND (delete_flagged = 0 OR delete_flagged IS NULL)
         LIMIT 1
    """, (ti_id,)).fetchone()
    return dict(r) if r else None


def get_related_words(conn, ti_id: int) -> list:
    if not ti_id:
        return []
    rows = conn.execute("""
        SELECT strongs_number, transliteration, gloss, relationship_note
          FROM wa_term_related_words
         WHERE term_inv_id = ?
           AND (delete_flagged = 0 OR delete_flagged IS NULL)
         ORDER BY id
    """, (ti_id,)).fetchall()
    return [dict(r) for r in rows]


def get_groups(conn, mti_id: int) -> list:
    """Return active groups for the term, joined with wa_dimension_index for
    counts and dimension info. Each row: group identity + dimension data.
    """
    rows = conn.execute("""
        SELECT vcg.id AS group_id, vcg.group_code, vcg.context_description,
               vcg.notes,
               di.dimension, di.dimension_confidence, di.manual_override,
               di.dominant_subject,
               di.anchor_count, di.related_count, di.set_aside_count,
               di.total_verse_count, di.notes AS dim_notes
          FROM verse_context_group vcg
          LEFT JOIN wa_dimension_index di
                 ON di.verse_context_group_id = vcg.id
                AND (di.delete_flagged = 0 OR di.delete_flagged IS NULL)
         WHERE vcg.mti_term_id = ?
           AND (vcg.delete_flagged = 0 OR vcg.delete_flagged IS NULL)
         ORDER BY vcg.group_code, vcg.id
    """, (mti_id,)).fetchall()
    return [dict(r) for r in rows]


def get_verses_for_group(conn, mti_id: int, group_id: int,
                         is_anchor: bool | None = None,
                         is_relevant: bool | None = None) -> list:
    """Return verse_context rows for a (mti, group) joined with verse text
    via wa_verse_records. Filter on is_anchor / is_relevant when provided.
    """
    where = [
        "vc.mti_term_id = ?", "vc.group_id = ?",
        "(vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)",
    ]
    params: list = [mti_id, group_id]
    if is_anchor is not None:
        where.append("vc.is_anchor = ?")
        params.append(1 if is_anchor else 0)
    if is_relevant is not None:
        where.append("vc.is_relevant = ?")
        params.append(1 if is_relevant else 0)
    sql = f"""
        SELECT vc.id, vc.is_anchor, vc.is_relevant, vc.is_related,
               vc.set_aside_reason, vc.analysis_note, vc.notes,
               vr.reference, vr.verse_text, vr.target_word,
               vr.book_id, vr.chapter, vr.verse_num
          FROM verse_context vc
          LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
         WHERE {' AND '.join(where)}
         ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id
    """
    rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


# ---------- Renderers --------------------------------------------------


def render_section_a(term: dict, ti_id: int | None,
                     parse: dict | None, root: dict | None,
                     related: list) -> list[str]:
    L: list[str] = []
    s = term['strongs_number']
    L.append(f"### {s} — {term['transliteration']} \"{term['gloss']}\"")
    L.append("")
    L.append(f"**Identity:** mti={term['id']} · ti={ti_id or '—'} · "
             f"language={term['language']} · status={term['status']} · "
             f"md_v={term['md_version']}")
    L.append(f"**Owner registry:** {term['owner_reg_no']:03d} ({term['owner_word']})")
    L.append("")
    if parse and parse.get('parsed'):
        p = parse['parsed']
        n_senses = p['top_sense_count']
        L.append(f"**Meaning parse** (parser v{p.get('parse_version', '—')}, "
                 f"parsed {p.get('parsed_at', '—')}): {n_senses} top sense(s) · "
                 f"stems={p.get('stem_count', 0)} · "
                 f"causative={'True' if p.get('has_causative_stem') else 'False'} · "
                 f"domain_tags={'True' if p.get('has_domain_tags') else 'False'}")
        L.append("")
        senses = parse.get('senses') or []
        top = [s for s in senses if (s.get('level_depth') or 0) == 1]
        sub = [s for s in senses if (s.get('level_depth') or 0) > 1]
        L.append("**Senses (top-level):**")
        L.append("")
        if not top:
            L.append("- _none parsed_")
        else:
            for s in top:
                code = s.get('level_code') or '—'
                txt = (s.get('sense_text') or '').strip()
                L.append(f"- `{code}`: {txt}")
        L.append("")
        if sub:
            L.append(f"**Sub-senses (depth > 1): {len(sub)} entries**")
            L.append("")
            shown = sub[:20]
            for s in shown:
                code = s.get('level_code') or '—'
                parent = s.get('parent_level_code') or '—'
                txt = (s.get('sense_text') or '').strip()
                L.append(f"- `{code}` (parent `{parent}`): {txt}")
            if len(sub) > 20:
                L.append(f"- _… {len(sub) - 20} additional sub-senses omitted_")
            L.append("")
    else:
        L.append("**Meaning parse:** _no parsed-meaning row in DB_")
        L.append("")

    if root:
        rg = root.get('root_gloss') or ''
        rl = root.get('root_language') or ''
        rn = root.get('note') or ''
        L.append(f"**Root family:** `{root['root_code']}` ({rl}) — {rg}"
                 + (f" · _{rn}_" if rn else ""))
        L.append("")
    else:
        L.append("**Root family:** _no row_")
        L.append("")

    if related:
        L.append(f"**Related words ({len(related)} total"
                 + (f"; sample of 20" if len(related) > 20 else "")
                 + "):**")
        L.append("")
        sample = related[:20]
        for r in sample:
            rs = r.get('strongs_number') or '—'
            tr = r.get('transliteration') or ''
            gl = r.get('gloss') or ''
            note = r.get('relationship_note') or ''
            line = f"- `{rs}` {tr} \"{gl}\""
            if note:
                line += f" — _{note}_"
            L.append(line)
        if len(related) > 20:
            L.append(f"- _… {len(related) - 20} additional related entries omitted_")
        L.append("")
    else:
        L.append("**Related words:** _none recorded_")
        L.append("")
    return L


def render_section_b(term: dict, groups: list) -> list[str]:
    L: list[str] = []
    s = term['strongs_number']
    L.append(f"### {s} — {len(groups)} active group(s)")
    L.append("")
    if not groups:
        L.append("_No active groups for this term._")
        L.append("")
        return L
    for g in groups:
        gc = g['group_code']
        rel = g.get('related_count') or 0
        anc = g.get('anchor_count') or 0
        sa = g.get('set_aside_count') or 0
        tot = g.get('total_verse_count') or 0
        dim = g.get('dimension') or '—'
        conf = g.get('dimension_confidence') or '—'
        ds = g.get('dominant_subject') or '—'
        cd = (g.get('context_description') or '').strip()
        notes = (g.get('notes') or '').strip()
        L.append(f"**Group `{gc}`** ({rel} related · {anc} anchor · "
                 f"{sa} set-aside · {tot} total · "
                 f"dimension: {dim} · confidence: {conf} · "
                 f"dominant_subject: {ds})")
        if cd:
            L.append(f"  - *{cd}*")
        if notes:
            L.append(f"  - notes: {notes}")
        L.append("")
    return L


def fmt_verse_line(v: dict, marker: str) -> list[str]:
    ref = v.get('reference') or '—'
    target = v.get('target_word') or ''
    text = (v.get('verse_text') or '').strip()
    set_aside = (v.get('set_aside_reason') or '').strip()
    head = f"- **{ref}** {marker}"
    if target:
        head += f" *target: {target}*"
    out = [head]
    if text:
        # Markdown blockquote, single-paragraph
        out.append(f"  > {text}")
    if set_aside:
        out.append(f"  _set-aside reason: {set_aside}_")
    return out


def render_section_c(term: dict, groups: list, conn) -> list[str]:
    L: list[str] = []
    s = term['strongs_number']
    L.append(f"### {s} — anchor verses (verbatim)")
    L.append("")
    if not groups:
        L.append("_No groups; no anchor verses._")
        L.append("")
        return L
    total_anchors = 0
    for g in groups:
        gc = g['group_code']
        anchors = get_verses_for_group(conn, term['id'], g['group_id'],
                                       is_anchor=True)
        if not anchors:
            continue
        total_anchors += len(anchors)
        L.append(f"**Group `{gc}`** — anchor verses ({len(anchors)}):")
        L.append("")
        for v in anchors:
            L.extend(fmt_verse_line(v, "🔵 (✓)"))
        L.append("")
    if total_anchors == 0:
        L.append("_No anchor verses recorded for any group._")
        L.append("")
    return L


def render_section_d(term: dict, groups: list, conn,
                     truncate_at: int | None = None) -> list[str]:
    """Render all relevant verses per group. If truncate_at is set and the
    cumulative relevant-verse count exceeds it, truncate and note."""
    L: list[str] = []
    s = term['strongs_number']
    L.append(f"### {s} — all relevant verses (verbatim)")
    L.append("")
    if not groups:
        L.append("_No groups; no relevant verses._")
        L.append("")
        return L
    cumulative = 0
    truncated = False
    for g in groups:
        if truncated:
            break
        gc = g['group_code']
        relevant = get_verses_for_group(conn, term['id'], g['group_id'],
                                        is_relevant=True)
        if not relevant:
            continue
        rendered_in_group = 0
        L.append(f"**Group `{gc}`** — all relevant verses ({len(relevant)}):")
        L.append("")
        for v in relevant:
            if truncate_at is not None and cumulative >= truncate_at:
                truncated = True
                remaining_in_group = len(relevant) - rendered_in_group
                L.append(f"_… truncation at {truncate_at} verses per directive note 4. "
                         f"Group `{gc}` has {remaining_in_group} more relevant verse(s); "
                         "subsequent groups (if any) not rendered. Full set available on request._")
                L.append("")
                break
            anchor = v.get('is_anchor') == 1
            marker = "🔵 (✓)" if anchor else "(✓)"
            L.extend(fmt_verse_line(v, marker))
            cumulative += 1
            rendered_in_group += 1
        L.append("")
    return L


# ---------- Main -------------------------------------------------------


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    conn = open_db()
    ts = now_iso()
    out_path = os.path.join(OUT_DIR, f"wa-099-kindness-crossreg-extract-v1-{today_compact()}.md")

    L: list[str] = []
    L.append("# wa-099-kindness — Cross-Registry Term Extract (DIR-20260501-001)")
    L.append("")
    L.append(f"_Generated: {ts} · schema 3.17.0 · read-only extract — no DB writes._")
    L.append("")
    L.append("**Directive:** [`wa-099-kindness-dir-001-crossreg-extract-v1-20260501.md`]"
             "(../obslog/wa-099-kindness-dir-001-crossreg-extract-v1-20260501.md)")
    L.append("")
    L.append("**Purpose:** supplementary source material for R099 kindness Stage 2b. "
             "Four kindness-cluster terms owned by other registries (H2617A chesed → R103, "
             "G5544 chrēstotēs → R067, H2623 chasid → R103, H2616A chasad → R023) extracted "
             "from the live database for analytical use alongside the R099 readiness output. "
             "OWNER assignments unchanged.")
    L.append("")
    L.append("**Schema adaptations** (per directive note 3): the directive's "
             "column references `mti_terms.owning_registry_id`, `verse_context_group.dimension_id` "
             "/`dimension_confidence` /`dominant_subject` /count fields, and `verse_context.verse_ref`/`target_word` "
             "do not exist as such in v3.17.0. Adapted to: `mti_terms.owning_registry_fk` → "
             "`word_registry.id`; group counts + dimension via `wa_dimension_index` joined on "
             "`verse_context_group_id`; verse reference + target_word via `wa_verse_records` joined "
             "on `verse_context.verse_record_id`. Meaning senses keyed on `wa_meaning_sense.level_code` "
             "/`level_depth`/`parent_level_code` (not `sense_code`/`depth`).")
    L.append("")
    L.append("---")
    L.append("")

    L.append("## Section map")
    L.append("")
    L.append("Per term (priority order: H2617A → G5544 → H2623 → H2616A):")
    L.append("- **A.** Term identity + lexical foundation (meaning parse, senses, root family, related words)")
    L.append("- **B.** Verse-context groups (group_code, dimension, counts, descriptions)")
    L.append("- **C.** Anchor verses (verbatim text)")
    L.append("- **D.** All relevant verses (verbatim text — H2617A truncated at "
             f"{H2617_TRUNCATE_AT} verses per directive note 4)")
    L.append("")

    confirmation_rows: list[tuple] = []
    for strongs, priority, rationale in TERMS_PRIORITY:
        term = get_owner_term(conn, strongs)
        L.append("---")
        L.append("")
        if not term:
            L.append(f"## {strongs} — _OWNER row not found in mti_terms_")
            L.append("")
            confirmation_rows.append((strongs, None, None, None, None, None))
            continue
        L.append(f"## {strongs} — {term['transliteration']} \"{term['gloss']}\" "
                 f"(owner R{term['owner_reg_no']:03d} {term['owner_word']}, priority {priority})")
        L.append("")
        L.append(f"_Rationale per directive: {rationale}_")
        L.append("")
        ti_id = get_term_inv_id(conn, term['id'], strongs)
        parse = get_meaning_parse(conn, ti_id) if ti_id else None
        root = get_root_family(conn, ti_id) if ti_id else None
        related = get_related_words(conn, ti_id) if ti_id else []
        groups = get_groups(conn, term['id'])
        L.append("### A. Term identity and lexical foundation")
        L.append("")
        L.extend(render_section_a(term, ti_id, parse, root, related))
        L.append("### B. Verse-context groups")
        L.append("")
        L.extend(render_section_b(term, groups))
        L.append("### C. Anchor verses (verbatim)")
        L.append("")
        L.extend(render_section_c(term, groups, conn))
        L.append("### D. All relevant verses (verbatim)")
        L.append("")
        truncate = H2617_TRUNCATE_AT if strongs == 'H2617A' else None
        L.extend(render_section_d(term, groups, conn, truncate_at=truncate))

        n_groups = len(groups)
        total_rel = sum((g.get('related_count') or 0) for g in groups)
        total_anc = sum((g.get('anchor_count') or 0) for g in groups)
        anchor_count_actual = sum(
            len(get_verses_for_group(conn, term['id'], g['group_id'], is_anchor=True))
            for g in groups
        )
        confirmation_rows.append(
            (strongs, term['owner_reg_no'], n_groups, total_rel, total_anc, anchor_count_actual)
        )

    # --- Completion confirmation panel ---
    L.append("---")
    L.append("")
    L.append("## Completion Confirmation")
    L.append("")
    L.append("**Query 1 — term identity confirmed (OWNER row, status IN ('extracted','extracted_thin')):**")
    L.append("")
    L.append("| Strong's | Owner reg | Word | Status |")
    L.append("|---|---:|---|---|")
    for strongs, _, _, _, _, _ in confirmation_rows:
        term = get_owner_term(conn, strongs)
        if term:
            L.append(f"| {strongs} | {term['owner_reg_no']:03d} | {term['owner_word']} | {term['status']} |")
        else:
            L.append(f"| {strongs} | — | _not found_ | — |")
    L.append("")
    L.append("**Query 2 — group counts per term (active groups; counts via wa_dimension_index):**")
    L.append("")
    L.append("| Strong's | Active groups | Total related | Total anchors |")
    L.append("|---|---:|---:|---:|")
    for strongs, _, n_groups, total_rel, total_anc, _ in confirmation_rows:
        if n_groups is not None:
            L.append(f"| {strongs} | {n_groups} | {total_rel} | {total_anc} |")
    L.append("")
    L.append("**Query 3 — anchor verse rows per term (verse_context.is_anchor=1, not delete_flagged):**")
    L.append("")
    L.append("| Strong's | Anchor verse rows |")
    L.append("|---|---:|")
    for strongs, _, _, _, _, anchor_actual in confirmation_rows:
        if anchor_actual is not None:
            L.append(f"| {strongs} | {anchor_actual} |")
    L.append("")
    L.append("**Query 4 — file written:** see footer for path + byte size.")
    L.append("")

    out_text = "\n".join(L) + "\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_text)
    sz = os.path.getsize(out_path)
    print(f"Wrote: {out_path}  ({sz:,} bytes / {sz/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
