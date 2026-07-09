"""_exploratory_anchor_gap_profile_v1_20260503.py — read-only.

Three views of the anchor coverage gap, post-cleanup:

  1. Registries with no anchors — fully unmoored
  2. OWNER terms with active classifications but no anchor
  3. Active verse_context rows not connected to any anchor (in their group/term)

For each view: counts, top examples, and severity tags.
"""
from __future__ import annotations

import os
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_MD = os.path.join("outputs", "markdown", "anchor-gap-profile-20260503.md")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    L = []
    L.append("# Anchor Gap Profile — Post-Cleanup")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  source: "
             "`scripts/_exploratory_anchor_gap_profile_v1_20260503.py`")
    L.append("")
    L.append("Three views of where anchors are missing in the analytical record. "
             "All counts reflect the state after today's three cleanup patches "
             "(POS noise Tier 1, R212→R122 merge, homonym mistarget).")
    L.append("")

    # Programme totals
    totals = conn.execute("""
        SELECT
          (SELECT COUNT(*) FROM word_registry WHERE phase1_status != 'Excluded') AS active_regs,
          (SELECT COUNT(*) FROM verse_context WHERE delete_flagged=0 AND is_anchor=1) AS total_anchors,
          (SELECT COUNT(*) FROM verse_context WHERE delete_flagged=0 AND is_relevant=1) AS total_relevant_vc,
          (SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged=0) AS active_groups
    """).fetchone()
    L.append("## Programme totals (active state)")
    L.append("")
    L.append(f"- Active registries (not Excluded): **{totals['active_regs']:,}**")
    L.append(f"- Active groups (`verse_context_group` not delete_flagged): **{totals['active_groups']:,}**")
    L.append(f"- Active relevant `verse_context` rows: **{totals['total_relevant_vc']:,}**")
    L.append(f"- Active anchor `verse_context` rows: **{totals['total_anchors']:,}**")
    L.append("")

    # ── View 1: Registries with no anchors ──────────────────────────────────
    L.append("## View 1 — Registries with no active anchors")
    L.append("")

    rows = conn.execute("""
        SELECT wr.no, wr.word, wr.phase1_status, wr.session_b_status,
               wr.cluster_assignment,
               (SELECT COUNT(*) FROM mti_terms mt
                  JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
                                            AND ti.term_owner_type='OWNER'
                                            AND ti.delete_flagged=0
                  JOIN wa_file_index fi ON fi.id=ti.file_id
                 WHERE fi.word_registry_fk = wr.id
                   AND mt.delete_flagged=0
                   AND mt.status NOT IN ('delete','excluded')) AS active_owner_terms,
               (SELECT COUNT(*) FROM verse_context vc
                  JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                  JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
                  JOIN wa_file_index fi ON fi.id=ti.file_id
                 WHERE fi.word_registry_fk = wr.id
                   AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
                   AND vr.delete_flagged=0 AND vc.delete_flagged=0
                   AND vc.is_relevant=1) AS rel_vc,
               (SELECT COUNT(*) FROM verse_context vc
                  JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                  JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
                  JOIN wa_file_index fi ON fi.id=ti.file_id
                 WHERE fi.word_registry_fk = wr.id
                   AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
                   AND vr.delete_flagged=0 AND vc.delete_flagged=0
                   AND vc.is_anchor=1) AS anchor_count
          FROM word_registry wr
         WHERE wr.phase1_status != 'Excluded' OR wr.phase1_status IS NULL
         ORDER BY wr.no
    """).fetchall()

    no_anchor = [r for r in rows if (r['anchor_count'] or 0) == 0]
    low_anchor = [r for r in rows if 0 < (r['anchor_count'] or 0) <= 2]

    L.append(f"**{len(no_anchor)} registries** have **zero** active anchors. "
             f"**{len(low_anchor)}** more have only 1–2 anchors (at-risk).")
    L.append("")
    L.append("### Zero-anchor registries")
    L.append("")
    L.append("| Reg | Word | Cluster | Active OWNER terms | Relevant vc | Status |")
    L.append("|---:|---|---|---:|---:|---|")
    for r in no_anchor:
        status_combo = (r['session_b_status'] or '?')
        L.append(f"| {r['no']} | {r['word']} | {r['cluster_assignment'] or '-'} | "
                 f"{r['active_owner_terms']} | {r['rel_vc']} | {status_combo} |")
    L.append("")
    L.append("### Low-anchor registries (1–2 anchors)")
    L.append("")
    L.append("| Reg | Word | Cluster | Active OWNER | Relevant vc | Anchors |")
    L.append("|---:|---|---|---:|---:|---:|")
    for r in sorted(low_anchor, key=lambda x: (x['anchor_count'] or 0, x['no'])):
        L.append(f"| {r['no']} | {r['word']} | {r['cluster_assignment'] or '-'} | "
                 f"{r['active_owner_terms']} | {r['rel_vc']} | {r['anchor_count']} |")
    L.append("")

    # ── View 2: OWNER terms with active vc but no anchor ────────────────────
    L.append("## View 2 — OWNER terms with active classifications but no anchor")
    L.append("")
    L.append("These terms have at least one relevant `verse_context` row, plus at least "
             "one active group, but no anchor has been designated. Without an anchor the "
             "group's meaning has no exemplar verse to ground the analytical reading.")
    L.append("")

    term_rows = conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status,
               wr.no AS reg_no, wr.word AS reg_word,
               (SELECT COUNT(*) FROM wa_verse_records vr
                 WHERE vr.term_inv_id = ti.id AND vr.delete_flagged=0) AS verses_pulled,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged=0
                   AND vc.is_relevant=1) AS rel_vc,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged=0
                   AND vc.is_anchor=1) AS anchors,
               (SELECT COUNT(*) FROM verse_context_group g
                 WHERE g.mti_term_id = mt.id AND g.delete_flagged=0) AS groups
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
          JOIN wa_file_index fi ON fi.id=ti.file_id
          JOIN word_registry wr ON wr.id=fi.word_registry_fk
         WHERE mt.delete_flagged=0
           AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
           AND wr.phase1_status != 'Excluded'
    """).fetchall()

    # Three cuts:
    # 2.1: terms with verses pulled but ZERO anchors anywhere (the analytical gap)
    no_anchor_term = [r for r in term_rows
                      if (r['verses_pulled'] or 0) > 0
                      and (r['anchors'] or 0) == 0]
    # 2.2: of those, ones with rel_vc > 0 (had analytical attention but no anchor)
    no_anchor_with_rel = [r for r in no_anchor_term if (r['rel_vc'] or 0) > 0]
    # 2.3: of those, ones with NO classifications at all (rel=0, groups=0)
    no_anchor_uninspected = [r for r in no_anchor_term
                             if (r['rel_vc'] or 0) == 0 and (r['groups'] or 0) == 0]
    # Stranded groups: anchor=0 but groups>0 (group exists but has no anchor)
    stranded_groups = [r for r in no_anchor_term if (r['groups'] or 0) > 0]

    L.append(f"**{len(no_anchor_term)} active OWNER terms** have verses pulled in but zero anchors:")
    L.append(f"  - With relevant vc rows but no anchor (analytical gap): {len(no_anchor_with_rel)}")
    L.append(f"  - With stranded group(s) but no anchor (group orphan): {len(stranded_groups)}")
    L.append(f"  - With no classifications at all (verses pulled, never inspected): {len(no_anchor_uninspected)}")
    no_anc_terms = no_anchor_term
    L.append("")
    # Group by registry
    by_reg = defaultdict(list)
    for r in no_anc_terms:
        by_reg[(r['reg_no'], r['reg_word'])].append(r)
    L.append("### Top 30 registries by no-anchor term count")
    L.append("")
    L.append("| Reg | Word | # terms missing anchor | Total verses pulled on those terms |")
    L.append("|---:|---|---:|---:|")
    summary = sorted(((no, word, len(items), sum(r['verses_pulled'] for r in items))
                     for (no, word), items in by_reg.items()),
                    key=lambda x: -x[2])
    for no, word, n_terms, n_v in summary[:30]:
        L.append(f"| {no} | {word} | {n_terms} | {n_v} |")
    L.append("")

    L.append("### Top 25 individual no-anchor terms by verses pulled")
    L.append("")
    L.append("| Reg | Word | Strong's | Translit | Gloss | Lang | Status | Groups | Rel vc | Verses |")
    L.append("|---:|---|---|---|---|---|---|---:|---:|---:|")
    for r in sorted(no_anc_terms, key=lambda x: -(x['verses_pulled'] or 0))[:25]:
        L.append(f"| {r['reg_no']} | {r['reg_word']} | `{r['strongs_number']}` | "
                 f"{r['transliteration'] or ''} | {(r['gloss'] or '')[:30]} | "
                 f"{r['language'][:1]} | `{r['status']}` | {r['groups']} | "
                 f"{r['rel_vc']} | {r['verses_pulled']} |")
    L.append("")

    # ── View 3: Active vc rows not connected to any anchor ──────────────────
    L.append("## View 3 — Active relevant verses not connected to any anchor")
    L.append("")
    L.append("Four sub-views at increasing scope:")
    L.append("- **3a:** relevant non-anchor vc row in a group with zero anchors (group-level orphan)")
    L.append("- **3b:** relevant non-anchor vc row whose group_id is NULL (no group attached)")
    L.append("- **3c:** relevant non-anchor vc row on a term that has zero anchors (term-level orphan)")
    L.append("- **3d:** canonical verse with active OWNER `wa_verse_records` but no anchor row anywhere in any registry (verse-level orphan)")
    L.append("")

    # 3a: rel verses in groups with no anchor
    rows_3a = conn.execute("""
        SELECT vc.id, vr.reference, mt.strongs_number, mt.gloss,
               wr.no AS reg_no, wr.word AS reg_word, g.group_code,
               (SELECT COUNT(*) FROM verse_context vc2
                 WHERE vc2.group_id = vc.group_id AND vc2.delete_flagged=0
                   AND vc2.is_anchor=1) AS group_anchor_count
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
          JOIN wa_file_index fi ON fi.id=ti.file_id
          JOIN word_registry wr ON wr.id=fi.word_registry_fk
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
          JOIN verse_context_group g ON g.id=vc.group_id
         WHERE vc.delete_flagged=0 AND vr.delete_flagged=0 AND ti.delete_flagged=0
           AND ti.term_owner_type='OWNER'
           AND vc.is_relevant=1 AND vc.is_anchor=0
           AND g.delete_flagged=0
    """).fetchall()
    rows_3a_orphan = [r for r in rows_3a if (r['group_anchor_count'] or 0) == 0]

    L.append(f"**3a — relevant verses in anchor-less groups: {len(rows_3a_orphan):,}** "
             f"(out of {len(rows_3a):,} total non-anchor relevant rows in active groups)")
    L.append("")

    # Group by group_code for 3a — top 20 anchor-less groups
    by_grp = defaultdict(list)
    for r in rows_3a_orphan:
        by_grp[(r['reg_no'], r['reg_word'], r['group_code'])].append(r)
    L.append(f"### 3a — Top 20 anchor-less groups by orphan-verse count")
    L.append("")
    L.append("| Reg | Word | Group | Strong's | Verses without anchor |")
    L.append("|---:|---|---|---|---:|")
    for (no, word, grp), items in sorted(by_grp.items(), key=lambda x: -len(x[1]))[:20]:
        s = items[0]['strongs_number']
        L.append(f"| {no} | {word} | `{grp}` | `{s}` | {len(items)} |")
    L.append("")

    # 3b: rel verses with group_id NULL
    rows_3b = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
          JOIN wa_file_index fi ON fi.id=ti.file_id
          JOIN word_registry wr ON wr.id=fi.word_registry_fk
         WHERE vc.delete_flagged=0 AND vr.delete_flagged=0 AND ti.delete_flagged=0
           AND ti.term_owner_type='OWNER'
           AND vc.is_relevant=1 AND vc.is_anchor=0
           AND vc.group_id IS NULL
           AND wr.phase1_status != 'Excluded'
    """).fetchone()[0]
    L.append(f"**3b — relevant verses with no group at all: {rows_3b:,}**")
    L.append("")

    # 3c: rel non-anchor vc rows on terms that have zero anchors
    rows_3c = conn.execute("""
        SELECT wr.no, wr.word, mt.strongs_number, mt.gloss, COUNT(*) AS n
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
          JOIN wa_file_index fi ON fi.id=ti.file_id
          JOIN word_registry wr ON wr.id=fi.word_registry_fk
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE vc.delete_flagged=0 AND vr.delete_flagged=0 AND ti.delete_flagged=0
           AND ti.term_owner_type='OWNER'
           AND vc.is_relevant=1 AND vc.is_anchor=0
           AND wr.phase1_status != 'Excluded'
           AND NOT EXISTS (
             SELECT 1 FROM verse_context vc2
              WHERE vc2.mti_term_id=vc.mti_term_id
                AND vc2.delete_flagged=0 AND vc2.is_anchor=1
           )
         GROUP BY wr.no, wr.word, mt.strongs_number, mt.gloss
         ORDER BY n DESC
    """).fetchall()
    total_3c = sum(r['n'] for r in rows_3c)
    L.append(f"**3c — relevant verses on terms with zero anchors (term-level orphan): {total_3c:,}** "
             f"across {len(rows_3c)} terms")
    L.append("")
    if rows_3c:
        L.append("### 3c — Top 25 terms by orphan vc count")
        L.append("")
        L.append("| Reg | Word | Strong's | Gloss | Orphan vc rows |")
        L.append("|---:|---|---|---|---:|")
        for r in rows_3c[:25]:
            L.append(f"| {r['no']} | {r['word']} | `{r['strongs_number']}` | {(r['gloss'] or '')[:30]} | {r['n']} |")
        L.append("")

    # 3d: canonical verses with no anchor anywhere
    L.append("### 3d — Canonical verses with active OWNER but no anchor anywhere")
    L.append("")
    canon = conn.execute("""
        WITH active_owner_verses AS (
          SELECT DISTINCT vr.book_id, vr.chapter, vr.verse_num, vr.reference
            FROM wa_verse_records vr
            JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
           WHERE vr.delete_flagged=0 AND ti.delete_flagged=0
             AND ti.term_owner_type='OWNER'
        )
        SELECT
          (SELECT COUNT(*) FROM active_owner_verses) AS total,
          (SELECT COUNT(*) FROM active_owner_verses aov
           WHERE EXISTS (
             SELECT 1 FROM verse_context vc
               JOIN wa_verse_records vr2 ON vr2.id=vc.verse_record_id
              WHERE vr2.book_id=aov.book_id AND vr2.chapter=aov.chapter
                AND vr2.verse_num=aov.verse_num
                AND vc.delete_flagged=0 AND vc.is_anchor=1
           )) AS anchored,
          (SELECT COUNT(*) FROM active_owner_verses aov
           WHERE NOT EXISTS (
             SELECT 1 FROM verse_context vc
               JOIN wa_verse_records vr2 ON vr2.id=vc.verse_record_id
              WHERE vr2.book_id=aov.book_id AND vr2.chapter=aov.chapter
                AND vr2.verse_num=aov.verse_num
                AND vc.delete_flagged=0 AND vc.is_anchor=1
           )) AS unanchored
    """).fetchone()
    L.append(f"- Total distinct canonical verses with active OWNER `wa_verse_records`: {canon['total']:,}")
    L.append(f"- Of those, anchored somewhere: **{canon['anchored']:,}** ({canon['anchored']/canon['total']*100:.1f}%)")
    L.append(f"- **Unanchored anywhere: {canon['unanchored']:,}** ({canon['unanchored']/canon['total']*100:.1f}%)")
    L.append("")

    # ── Summary ─────────────────────────────────────────────────────────────
    L.append("## Summary")
    L.append("")
    L.append(f"- Zero-anchor registries: **{len(no_anchor)}**")
    L.append(f"- 1-2 anchor registries: **{len(low_anchor)}**")
    L.append(f"- OWNER terms with verses pulled but no anchor: **{len(no_anchor_term)}** "
             f"(rel_vc>0: {len(no_anchor_with_rel)}, group orphan: {len(stranded_groups)}, "
             f"never inspected: {len(no_anchor_uninspected)})")
    L.append(f"- Relevant verses in anchor-less groups (3a): **{len(rows_3a_orphan):,}**")
    L.append(f"- Relevant verses with no group (3b): **{rows_3b:,}**")
    L.append(f"- Relevant verses on terms with zero anchors (3c): **{total_3c:,}**")
    L.append(f"- Canonical verses unanchored anywhere (3d): **{canon['unanchored']:,}**")
    L.append("")

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Wrote: {OUT_MD}")
    print()
    print(f"Zero-anchor registries: {len(no_anchor)}")
    print(f"Low-anchor registries (1-2): {len(low_anchor)}")
    print(f"OWNER terms with verses pulled but no anchor: {len(no_anchor_term)}")
    print(f"  rel_vc>0 (analytical gap): {len(no_anchor_with_rel)}")
    print(f"  group orphan: {len(stranded_groups)}")
    print(f"  never inspected: {len(no_anchor_uninspected)}")
    print(f"Relevant verses in anchor-less groups (3a): {len(rows_3a_orphan):,}")
    print(f"Relevant verses with no group (3b): {rows_3b:,}")
    print(f"Relevant verses on terms with zero anchors (3c): {total_3c:,}")
    print(f"Canonical verses unanchored anywhere (3d): {canon['unanchored']:,}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
