"""_generate_cluster_comprehensive_v1_20260505.py — read-only with one
exception: the **session-open status transition** (see end of this docstring).

Comprehensive M-cluster extract — exposes every database fact connected to
each term in the cluster, plus registry-level / cross-cluster items that are
not yet term-linked.

Output convention:
  - Numbered paragraphs throughout (no bullet lists). Section headings use
    markdown headers; tables stay as tables; everything else uses
    "1.", "2.", … numbered list items so each item can be referenced.
  - No explicit truncation. Cell values are sanitised (newlines → space,
    triple-backticks stripped, pipes escaped) but full content is preserved.

Per-term (for each Strong's in the cluster):
  - Identity & meaning (mti_terms + wa_term_inventory)
  - All wa_verse_records for the term — verse_text, reference, group_id,
    set_aside_reason, is_relevant — plus full per-verse list of all term
    SPANS occurring in that verse (every Strong's that has a verse record
    at the same location)
  - Anchor-verse-resolved findings (finding ↔ verse where this term appears)
  - Group memberships (verse_context_group rows)
  - Findings — direct (Strong's mention) + via anchor verse
  - SD pointers — direct (strongs_reference / description)
  - Cross-refs, root-family, related-words, quality flags

Registry / cluster-level (not yet linked to a specific term):
  - Findings from M-contributor registries whose anchor verses don't
    resolve to any M-term
  - SD pointers from contributor registries with no Strong's hitting an
    M-term
  - Prose sections from contributor registries
  - Cluster-internal verse_context_group rows
  - Cross-cluster orphan findings + pointers (pointer to existing scan)

Usage:
  python scripts/_generate_cluster_comprehensive_v1_20260505.py --m-cluster M06

Session-open status transition (the documented exception to read-only):
  When the report is generated for a cluster currently at
  cluster.status='Not started', the script transitions the status to
  'Data - In Progress' as part of the same invocation. A row-level JSON
  backup is taken before the UPDATE. The transition is logged to stdout and
  reflected in cluster.last_updated_date. This replaces the dir-001 status-
  init directive (formerly required at session open per
  wa-sessionb-cluster-instruction §4.1 v1_4); the transition is now inline
  with first-data preparation rather than a separate ceremony. Idempotent:
  if status is anything other than 'Not started', no write occurs.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
SESSIONS_DIR = os.path.join("Sessions", "Session_Clusters")

STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")
ANCHOR_REF_RE = re.compile(
    r"\b(\d?[A-Za-z]{2,5})\s+(\d{1,3}):(\d{1,3})(?:-(\d{1,3}))?",
)
ANCHOR_PAREN_RE = re.compile(r"\([^)]*\)")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_version(out_dir: str, base_name: str, exts=("md", "json")) -> str:
    """Return next 'vN' for files named `{base_name}-v{N}-{YYYYMMDD}.{ext}`
    in `out_dir`, regardless of date. v1 if no prior file exists."""
    pat = re.compile(
        r"^" + re.escape(base_name)
        + r"-v(\d+)-\d{8}\.(?:" + "|".join(exts) + r")$"
    )
    max_v = 0
    if os.path.isdir(out_dir):
        for f in os.listdir(out_dir):
            m = pat.match(f)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def sanitise(s):
    """Sanitise text for embedding in a markdown table cell.

    Strips newlines/CR, escapes pipes, removes triple-backticks (which
    would break out of a table cell into a code block). NO truncation:
    full content preserved.
    """
    if not s:
        return ""
    s = str(s)
    s = s.replace("```", "")
    s = s.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
    s = s.replace("\t", " ")
    while "  " in s:
        s = s.replace("  ", " ")
    s = s.strip()
    s = s.replace("|", "\\|")
    return s


def build_book_lookup(conn):
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ).fetchall():
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    aliases = {
        "1cor": "1Co", "2cor": "2Co", "1th": "1Th", "2th": "2Th",
        "1jo": "1Jn", "2jo": "2Jn", "3jo": "3Jn",
        "song": "Sng", "ps": "Psa", "jn": "Joh",
        "mt": "Mat", "mk": "Mar", "lk": "Luk",
        "co1": "1Co", "co2": "2Co",
        "jas": "Jam", "phi": "Php", "phil": "Php", "phili": "Php",
        "1tim": "1Ti", "2tim": "2Ti", "1pet": "1Pe", "2pet": "2Pe",
        "ezek": "Eze", "zech": "Zec", "matt": "Mat",
        "1sam": "1Sa", "2sam": "2Sa", "1kgs": "1Ki", "2kgs": "2Ki",
        "1chr": "1Ch", "2chr": "2Ch",
        "deut": "Deu", "prov": "Pro", "eccl": "Ecc",
        "isa": "Isa", "jer": "Jer", "josh": "Jos", "judg": "Jdg",
    }
    for alt, canonical in aliases.items():
        if canonical.lower() in out:
            out[alt.lower()] = out[canonical.lower()]
    return out


def parse_anchor_verses(text, book_lookup):
    if not text:
        return
    cleaned = ANCHOR_PAREN_RE.sub("", text)
    for m in ANCHOR_REF_RE.finditer(cleaned):
        bk_token = m.group(1)
        chap = int(m.group(2))
        v1 = int(m.group(3))
        v2 = m.group(4)
        bid = book_lookup.get(bk_token.lower())
        if not bid:
            continue
        if v2 is None:
            yield (bid, chap, v1, f"{bk_token} {chap}:{v1}")
        else:
            for v in range(v1, int(v2) + 1):
                yield (bid, chap, v, f"{bk_token} {chap}:{v}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument(
        "--version", default="auto",
        help="vN override; default 'auto' = scan dir for highest vN, bump",
    )
    args = ap.parse_args()
    date = datetime.now().strftime("%Y%m%d")
    dest_dir = os.path.join(SESSIONS_DIR, args.m_cluster)
    os.makedirs(dest_dir, exist_ok=True)
    base = f"wa-cluster-{args.m_cluster}-comprehensive"
    version = (
        next_version(dest_dir, base, exts=("md",))
        if args.version == "auto" else args.version
    )
    out_path = os.path.join(dest_dir, f"{base}-{version}-{date}.md")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # --- 1. Cluster metadata
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code = ?", (args.m_cluster,)
    ).fetchone()
    if not cluster:
        print(f"ERROR: cluster {args.m_cluster} not found.")
        return 1
    print(f"Cluster {args.m_cluster}: {cluster['description']}")

    # --- 1b. Session-open status transition (documented exception to
    # read-only; see module docstring). If status == 'Not started', flip to
    # 'Data - In Progress' as part of first-data preparation. Idempotent:
    # any other status is a noop.
    if cluster["status"] == "Not started":
        now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        backup_dir = os.path.join("backups", "row_backups")
        os.makedirs(backup_dir, exist_ok=True)
        backup_path = os.path.join(
            backup_dir,
            f"cluster_{args.m_cluster}_pre_status_init_"
            f"{datetime.now().strftime('%Y%m%dT%H%M%S')}.json",
        )
        with open(backup_path, "w", encoding="utf-8") as fbk:
            json.dump(
                {
                    "trigger": "_generate_cluster_comprehensive_v1 session-open transition",
                    "timestamp": now_utc,
                    "row": dict(cluster),
                },
                fbk, indent=2, ensure_ascii=False,
            )
        conn.execute(
            "UPDATE cluster SET status = ?, last_updated_date = ? "
            "WHERE cluster_code = ? AND status = ?",
            ("Data - In Progress", now_utc, args.m_cluster, "Not started"),
        )
        conn.commit()
        print(
            f"  status: 'Not started' → 'Data - In Progress'  "
            f"(backup: {backup_path})"
        )
    else:
        print(f"  status: {cluster['status']!r}  (no transition)")

    # --- 2. Term metadata for cluster members
    # Post-M46: mti_terms.cluster_subgroup_id is gone — sub-group mapping
    # now lives in mti_term_subgroup (m:n). A term may belong to multiple
    # sub-groups (DEC-1..DEC-3 of m39-subgroup-multi-term-design-v1).
    term_rows = conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.gloss,
               mt.transliteration, mt.language, mt.status AS mti_status,
               mt.owning_registry_fk,
               mt.md_version, mt.vc_status,
               wr.no AS reg_no, wr.word AS reg_word,
               wr.cluster_assignment AS legacy_c_cluster,
               ti.id AS inv_id, ti.meaning AS inv_meaning,
               ti.short_def_mounce, ti.evidential_status,
               ti.term_owner_type, ti.occurrence_count,
               ti.retention_note
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
          LEFT JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
         WHERE mt.cluster_code = ?
           AND COALESCE(mt.delete_flagged,0) = 0
    """, (args.m_cluster,)).fetchall()
    by_strong = {}
    mti_ids_per_strong = defaultdict(set)
    for r in term_rows:
        s = r["strongs_number"]
        if s not in by_strong:
            by_strong[s] = dict(r)
        if r["mti_id"]:
            mti_ids_per_strong[s].add(r["mti_id"])
    strongs_list = list(by_strong.keys())
    all_mti_ids = set()
    for ids in mti_ids_per_strong.values():
        all_mti_ids.update(ids)
    print(f"  terms: {len(strongs_list)}  mti_ids: {len(all_mti_ids)}")

    # --- 2b. Sub-groups (cluster_subgroup) for this cluster
    subgroups = [dict(r) for r in conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order
          FROM cluster_subgroup
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0) = 0
         ORDER BY sort_order, subgroup_code
    """, (args.m_cluster,)).fetchall()]
    sg_by_id = {sg["id"]: sg for sg in subgroups}

    # mti_term_subgroup: term -> list of sub-group ids (m:n)
    mti_to_subgroup_ids: dict[int, list[int]] = defaultdict(list)
    if all_mti_ids:
        ph_mts = ",".join("?" * len(all_mti_ids))
        for r in conn.execute(f"""
            SELECT mts.mti_term_id, mts.cluster_subgroup_id
              FROM mti_term_subgroup mts
              JOIN cluster_subgroup cs
                ON cs.id = mts.cluster_subgroup_id
             WHERE mts.mti_term_id IN ({ph_mts})
               AND COALESCE(mts.delete_flagged,0) = 0
               AND COALESCE(cs.delete_flagged,0) = 0
        """, list(all_mti_ids)):
            mti_to_subgroup_ids[r["mti_term_id"]].append(
                r["cluster_subgroup_id"]
            )

    # Strong's -> list of sub-group ids (union across mti_ids of that strong)
    strong_to_sg_ids: dict[str, list[int]] = defaultdict(list)
    for s in strongs_list:
        seen = set()
        for mid in mti_ids_per_strong[s]:
            for sg_id in mti_to_subgroup_ids.get(mid, []):
                if sg_id not in seen:
                    seen.add(sg_id)
                    strong_to_sg_ids[s].append(sg_id)
    print(f"  sub-groups: {len(subgroups)}")

    # --- 3. Verses per term: wa_verse_records + verse_context
    print("Loading per-term verse records + verse_context...", flush=True)
    ph = ",".join("?" * len(all_mti_ids)) if all_mti_ids else ""
    verses_by_mti = defaultdict(list)
    if all_mti_ids:
        for r in conn.execute(f"""
            SELECT vr.id AS vr_id, vr.mti_term_id, vr.book_id, vr.chapter,
                   vr.verse_num, vr.reference, vr.verse_text, vr.testament,
                   vr.target_word, vr.span_strong_match
              FROM wa_verse_records vr
             WHERE COALESCE(vr.delete_flagged,0) = 0
               AND vr.mti_term_id IN ({ph})
             ORDER BY vr.book_id, vr.chapter, vr.verse_num
        """, list(all_mti_ids)).fetchall():
            verses_by_mti[r["mti_term_id"]].append(dict(r))

    # 3b. Per-verse term-spans — every Strong's that has a verse record at
    # any location occupied by a cluster term.
    print("Loading per-verse term-spans...", flush=True)
    spans_at_loc = defaultdict(list)
    if all_mti_ids:
        for r in conn.execute(f"""
            WITH cluster_locs AS (
              SELECT DISTINCT vr.book_id, vr.chapter, vr.verse_num
                FROM wa_verse_records vr
               WHERE COALESCE(vr.delete_flagged,0) = 0
                 AND vr.mti_term_id IN ({ph})
            )
            SELECT vr.book_id, vr.chapter, vr.verse_num,
                   vr.target_word, mt.strongs_number,
                   mt.transliteration, mt.gloss
              FROM wa_verse_records vr
              JOIN mti_terms mt ON mt.id = vr.mti_term_id
              JOIN cluster_locs cl
                ON cl.book_id = vr.book_id
               AND cl.chapter = vr.chapter
               AND cl.verse_num = vr.verse_num
             WHERE COALESCE(vr.delete_flagged,0) = 0
        """, list(all_mti_ids)).fetchall():
            spans_at_loc[
                (r["book_id"], r["chapter"], r["verse_num"])
            ].append({
                "strong": r["strongs_number"],
                "translit": r["transliteration"] or "",
                "gloss": r["gloss"] or "",
                "target_word": r["target_word"] or "",
            })

    # verse_context per (mti_term_id, verse_record_id)
    # Post-M46 a single (mti_term_id, verse_record_id) pair can have N rows
    # differing in cluster_subgroup_id (DEC-3 'both' verses route to multiple
    # sub-groups). All rows are collected here; the §2 verse rendering uses
    # cluster_subgroup_id to drive sub-group bucketing.
    vc_by_pair = defaultdict(list)
    if all_mti_ids:
        for r in conn.execute(f"""
            SELECT vc.verse_record_id, vc.mti_term_id, vc.group_id,
                   vc.cluster_subgroup_id,
                   vc.is_anchor, vc.is_relevant, vc.is_related,
                   vc.set_aside_reason, vc.notes, vc.delete_flagged
              FROM verse_context vc
             WHERE vc.mti_term_id IN ({ph})
        """, list(all_mti_ids)).fetchall():
            vc_by_pair[(r["mti_term_id"], r["verse_record_id"])].append(
                dict(r)
            )

    # --- 4. Group context (verse_context_group)
    # Post-M47: vcg.mti_term_id is gone — vcg ↔ term is m:n via vcg_term.
    # A vcg can therefore appear under multiple terms in the per-term §3
    # view (each occurrence is the same vcg_id with the same description).
    print("Loading verse_context_group entries...", flush=True)
    groups_by_mti = defaultdict(list)
    vcg_by_id: dict[int, dict] = {}
    if all_mti_ids:
        for r in conn.execute(f"""
            SELECT vcg.id AS group_id, vt.mti_term_id,
                   vcg.group_code, vcg.context_description, vcg.notes
              FROM verse_context_group vcg
              JOIN vcg_term vt ON vt.vcg_id = vcg.id
             WHERE COALESCE(vcg.delete_flagged,0) = 0
               AND COALESCE(vt.delete_flagged,0) = 0
               AND vt.mti_term_id IN ({ph})
             ORDER BY vcg.group_code
        """, list(all_mti_ids)).fetchall():
            row = dict(r)
            groups_by_mti[r["mti_term_id"]].append(row)
            # Note: vcg_by_id may receive the same vcg_id multiple times
            # (once per term it spans). The dict store is idempotent —
            # the meta is identical across rows for the same vcg_id.
            vcg_by_id[row["group_id"]] = row

    # --- 5. Findings + pointers
    print("Loading findings + SD pointers...", flush=True)
    book_lookup = build_book_lookup(conn)
    findings_direct = defaultdict(list)
    findings_via_anchor = defaultdict(list)
    findings_by_registry = defaultdict(list)
    pointers_direct = defaultdict(list)
    pointers_by_registry = defaultdict(list)

    mti_to_strong = {}
    for s, ids in mti_ids_per_strong.items():
        for mid in ids:
            mti_to_strong[mid] = s
    verse_index = defaultdict(set)
    for mid, vlist in verses_by_mti.items():
        s = mti_to_strong.get(mid)
        if not s:
            continue
        for v in vlist:
            verse_index[(v["book_id"], v["chapter"], v["verse_num"])].add(s)

    target_set = set(strongs_list)

    findings = conn.execute("""
        SELECT id, finding_id, registry_id, finding_type, finding,
               anchor_verses, status
          FROM wa_session_b_findings
         WHERE COALESCE(delete_flag,0) = 0
    """).fetchall()
    for f in findings:
        text = " | ".join([f["finding"] or "", f["anchor_verses"] or ""])
        for s in set(STRONGS_RE.findall(text)) & target_set:
            findings_direct[s].append(dict(f))
        if f["anchor_verses"]:
            anchor_strongs = set()
            anchor_refs_per_strong = defaultdict(list)
            for bid, chap, vnum, raw_ref in parse_anchor_verses(
                f["anchor_verses"], book_lookup
            ):
                for s in verse_index.get((bid, chap, vnum), set()):
                    anchor_strongs.add(s)
                    anchor_refs_per_strong[s].append(raw_ref)
            for s in anchor_strongs:
                rec = dict(f)
                rec["matched_anchor_refs"] = anchor_refs_per_strong[s]
                findings_via_anchor[s].append(rec)
        if f["registry_id"]:
            findings_by_registry[f["registry_id"]].append(dict(f))

    pointers = conn.execute("""
        SELECT id, registry_id, flag_label, flag_code, strongs_reference,
               cross_registry_id, priority, description, resolved
          FROM wa_session_research_flags
         WHERE COALESCE(resolved,0) = 0
           AND flag_code = 'SD_POINTER'
    """).fetchall()
    for p in pointers:
        sref = p["strongs_reference"] or ""
        text = " | ".join([p["description"] or "", sref])
        for s in set(STRONGS_RE.findall(text)) & target_set:
            pointers_direct[s].append(dict(p))
        if p["registry_id"]:
            pointers_by_registry[p["registry_id"]].append(dict(p))
        if p["cross_registry_id"]:
            pointers_by_registry[p["cross_registry_id"]].append(dict(p))

    # --- 6. Aux: cross-refs, root family, related words, quality flags
    print("Loading aux term data...", flush=True)
    cross_refs_by_strong = defaultdict(list)
    if strongs_list:
        ph_s = ",".join("?" * len(strongs_list))
        for r in conn.execute(f"""
            SELECT mt.strongs_number, mtcr.registry, mtcr.word, mtcr.part,
                   mtcr.word_data_reference
              FROM mti_terms mt
              JOIN mti_term_cross_refs mtcr ON mtcr.mti_term_id = mt.id
             WHERE mt.strongs_number IN ({ph_s})
        """, strongs_list).fetchall():
            cross_refs_by_strong[r["strongs_number"]].append(dict(r))

    root_family_by_strong = defaultdict(list)
    if strongs_list:
        for r in conn.execute(f"""
            SELECT ti.strongs_number, wrf.root_code, wrf.root_language,
                   wrf.root_gloss, wrf.note
              FROM wa_term_inventory ti
              JOIN wa_term_root_family wrf ON wrf.term_inv_id = ti.id
             WHERE ti.strongs_number IN ({ph_s})
               AND COALESCE(wrf.delete_flagged,0) = 0
        """, strongs_list).fetchall():
            root_family_by_strong[r["strongs_number"]].append(dict(r))

    related_words_by_strong = defaultdict(list)
    if strongs_list:
        for r in conn.execute(f"""
            SELECT ti.strongs_number AS source_strong,
                   wtrw.strongs_number AS related_strong,
                   wtrw.gloss AS related_gloss,
                   wtrw.transliteration AS related_translit,
                   wtrw.relationship_note
              FROM wa_term_inventory ti
              JOIN wa_term_related_words wtrw ON wtrw.term_inv_id = ti.id
             WHERE ti.strongs_number IN ({ph_s})
               AND COALESCE(wtrw.delete_flagged,0) = 0
        """, strongs_list).fetchall():
            related_words_by_strong[r["source_strong"]].append(dict(r))

    quality_flags_by_strong = defaultdict(list)
    if strongs_list:
        for r in conn.execute(f"""
            SELECT term_id AS strong, flag_id, description
              FROM wa_data_quality_flags
             WHERE term_id IN ({ph_s})
        """, strongs_list).fetchall():
            quality_flags_by_strong[r["strong"]].append(dict(r))

    term_flags_by_strong = defaultdict(list)
    if strongs_list:
        for r in conn.execute(f"""
            SELECT mt.strongs_number, mtf.*
              FROM mti_terms mt
              JOIN mti_term_flags mtf ON mtf.mti_term_id = mt.id
             WHERE mt.strongs_number IN ({ph_s})
        """, strongs_list).fetchall():
            term_flags_by_strong[r["strongs_number"]].append(dict(r))

    # --- 7. Prose sections from M-contributor registries
    m_registries = {by_strong[s]["owning_registry_fk"] for s in strongs_list
                    if by_strong[s].get("owning_registry_fk")}
    prose_sections = []
    if m_registries:
        ph_r = ",".join("?" * len(m_registries))
        prose_sections = [dict(r) for r in conn.execute(f"""
            SELECT ps.*, pst.code AS section_type_code
              FROM prose_section ps
              LEFT JOIN prose_section_type pst
                     ON pst.id = ps.section_type_id
             WHERE COALESCE(ps.delete_flagged,0) = 0
               AND ps.registry_id IN ({ph_r})
             ORDER BY ps.registry_id, ps.section_type_id
        """, list(m_registries)).fetchall()]

    # --- 7b. Connectivity health checks
    # The connectivity chain runs:
    #   wa_verse_records ← verse_context (group_id, cluster_subgroup_id)
    #   verse_context.group_id → verse_context_group (per-term meaning groups)
    #   verse_context.cluster_subgroup_id → cluster_subgroup
    #   mti_terms ↔ cluster_subgroup via mti_term_subgroup (m:n)
    # Anything that breaks this chain is invisible to the analyst unless
    # the report surfaces it. The health block below counts each break
    # and lists the offending rows when small.
    print("Computing connectivity health...", flush=True)
    health: dict[str, list] = {}

    # H1: active vc rows in this cluster with cluster_subgroup_id NULL
    health["H1_unrouted_vc"] = [
        dict(r) for r in conn.execute("""
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
                   vr.reference, mt.strongs_number
              FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
              JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
             WHERE mt.cluster_code=?
               AND vc.cluster_subgroup_id IS NULL
               AND COALESCE(vc.delete_flagged,0)=0
             ORDER BY mt.strongs_number, vr.reference
        """, (args.m_cluster,))
    ]

    # H2: active vc rows with is_relevant=1 but no group_id (relevant
    # but not yet placed in a meaning group)
    health["H2_relevant_no_group"] = [
        dict(r) for r in conn.execute("""
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
                   vr.reference, mt.strongs_number
              FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
              JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
             WHERE mt.cluster_code=?
               AND vc.is_relevant=1
               AND vc.group_id IS NULL
               AND COALESCE(vc.delete_flagged,0)=0
               AND (vc.set_aside_reason IS NULL OR vc.set_aside_reason='')
             ORDER BY mt.strongs_number, vr.reference
        """, (args.m_cluster,))
    ]

    # H3: vc.mti_term_id is not in the vcg's term set (post-M47 m:n).
    # Was: cross-term contamination based on the old 1:1 vcg.mti_term_id.
    # Now: contamination = no active vcg_term row links the vc's term
    # to its vcg. The 79 known instances post-M47 are vc rows pointing
    # at soft-deleted vcgs (pre-existing data quality issue).
    health["H3_vcg_term_mismatch"] = [
        dict(r) for r in conn.execute("""
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
                   vc.group_id,
                   vr.reference, mt.strongs_number AS vc_strong,
                   vcg.group_code,
                   COALESCE(vcg.delete_flagged,0) AS vcg_deleted
              FROM verse_context vc
              JOIN verse_context_group vcg ON vcg.id=vc.group_id
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
              JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
             WHERE mt.cluster_code=?
               AND COALESCE(vc.delete_flagged,0)=0
               AND NOT EXISTS (
                   SELECT 1 FROM vcg_term vt
                    WHERE vt.vcg_id = vc.group_id
                      AND vt.mti_term_id = vc.mti_term_id
                      AND COALESCE(vt.delete_flagged,0)=0
               )
             ORDER BY mt.strongs_number, vr.reference
        """, (args.m_cluster,))
    ]

    # H4: vc has cluster_subgroup_id set, but the term has no
    # mti_term_subgroup mapping to that sub-group — orphaned routing
    health["H4_subgroup_route_orphan"] = [
        dict(r) for r in conn.execute("""
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
                   vc.cluster_subgroup_id, vr.reference,
                   mt.strongs_number, cs.subgroup_code
              FROM verse_context vc
              JOIN mti_terms mt ON mt.id=vc.mti_term_id
              JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
              JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
             WHERE mt.cluster_code=?
               AND vc.cluster_subgroup_id IS NOT NULL
               AND COALESCE(vc.delete_flagged,0)=0
               AND NOT EXISTS (
                   SELECT 1 FROM mti_term_subgroup mts
                    WHERE mts.mti_term_id = vc.mti_term_id
                      AND mts.cluster_subgroup_id = vc.cluster_subgroup_id
                      AND COALESCE(mts.delete_flagged,0)=0
               )
             ORDER BY mt.strongs_number, vr.reference
        """, (args.m_cluster,))
    ]

    # H5: vcg rows with no active vc references (orphan meaning group).
    # Post-M47: vcg ↔ term is m:n; a vcg is "in this cluster" if any of
    # its terms belongs to the cluster. A multi-term vcg is reported once
    # with a comma-joined Strong's list.
    health["H5_orphan_vcg"] = [
        dict(r) for r in conn.execute("""
            SELECT vcg.id AS group_id, vcg.group_code,
                   vcg.context_description,
                   GROUP_CONCAT(DISTINCT mt.strongs_number) AS strongs_number
              FROM verse_context_group vcg
              JOIN vcg_term vt ON vt.vcg_id=vcg.id
              JOIN mti_terms mt ON mt.id=vt.mti_term_id
             WHERE mt.cluster_code=?
               AND COALESCE(vcg.delete_flagged,0)=0
               AND COALESCE(vt.delete_flagged,0)=0
               AND NOT EXISTS (
                   SELECT 1 FROM verse_context vc
                    WHERE vc.group_id=vcg.id
                      AND COALESCE(vc.delete_flagged,0)=0
               )
             GROUP BY vcg.id
             ORDER BY vcg.group_code
        """, (args.m_cluster,))
    ]

    # H6: terms in cluster with no mti_term_subgroup mapping
    health["H6_unassigned_terms"] = [
        dict(r) for r in conn.execute("""
            SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
                   mt.gloss
              FROM mti_terms mt
             WHERE mt.cluster_code=?
               AND COALESCE(mt.delete_flagged,0)=0
               AND NOT EXISTS (
                   SELECT 1 FROM mti_term_subgroup mts
                    WHERE mts.mti_term_id = mt.id
                      AND COALESCE(mts.delete_flagged,0)=0
               )
             ORDER BY mt.strongs_number
        """, (args.m_cluster,))
    ]

    # H7: terms with mti_term_subgroup mapping but no verse_context_group
    # rows at all (term placed in a sub-group but never had its verses
    # contextually grouped). Post-M47 vcg ↔ term is via vcg_term.
    health["H7_terms_without_vcg"] = [
        dict(r) for r in conn.execute("""
            SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
                   mt.gloss
              FROM mti_terms mt
              JOIN mti_term_subgroup mts ON mts.mti_term_id=mt.id
             WHERE mt.cluster_code=?
               AND COALESCE(mt.delete_flagged,0)=0
               AND COALESCE(mts.delete_flagged,0)=0
               AND NOT EXISTS (
                   SELECT 1 FROM vcg_term vt
                     JOIN verse_context_group vcg ON vcg.id=vt.vcg_id
                    WHERE vt.mti_term_id = mt.id
                      AND COALESCE(vt.delete_flagged,0)=0
                      AND COALESCE(vcg.delete_flagged,0)=0
               )
             GROUP BY mt.id
             ORDER BY mt.strongs_number
        """, (args.m_cluster,))
    ]

    # H8: vcgs whose active verses span multiple sub-groups. The analytical
    # principle is one-vcg-per-sub-group (a meaning belongs in one sub-group
    # context). Multi-sub-group spread arises when per-verse classification
    # (e.g. the M26 subject classifier) routes verses of the same vcg to
    # different sub-groups. Each split vcg is a candidate for: (a) promoting
    # minority BOUNDARY verses to the dominant sub-group, (b) reassigning
    # minority verses to a different vcg in their actual sub-group, or
    # (c) splitting the meaning into multiple vcgs.
    h8_rows = list(conn.execute("""
        SELECT vcg.id AS vcg_id, vcg.group_code,
               GROUP_CONCAT(DISTINCT mt.strongs_number) AS strongs_number,
               cs.subgroup_code, COUNT(DISTINCT vc.id) AS n_verses
          FROM verse_context_group vcg
          JOIN vcg_term vt ON vt.vcg_id=vcg.id
          JOIN mti_terms mt ON mt.id=vt.mti_term_id
          JOIN verse_context vc ON vc.group_id=vcg.id
          JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
         WHERE mt.cluster_code=?
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(vt.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY vcg.id, cs.subgroup_code
    """, (args.m_cluster,)))
    h8_by_vcg: dict = defaultdict(dict)
    h8_meta: dict = {}
    for r in h8_rows:
        h8_by_vcg[r["vcg_id"]][r["subgroup_code"]] = r["n_verses"]
        h8_meta[r["vcg_id"]] = (r["group_code"], r["strongs_number"])
    health["H8_vcg_spans_subgroups"] = []
    for vcg_id, dist in h8_by_vcg.items():
        if len(dist) <= 1:
            continue
        code, strong = h8_meta[vcg_id]
        total = sum(dist.values())
        dom_sg, dom_n = max(dist.items(), key=lambda kv: kv[1])
        minority_sgs = ", ".join(
            f"{sg}={n}" for sg, n in sorted(dist.items())
            if sg != dom_sg
        )
        health["H8_vcg_spans_subgroups"].append({
            "group_code": code,
            "strongs_number": strong,
            "n_subgroups": len(dist),
            "n_verses": total,
            "dom_sg": dom_sg,
            "dom_n": dom_n,
            "minority_n": total - dom_n,
            "minority_sgs": minority_sgs,
        })
    health["H8_vcg_spans_subgroups"].sort(
        key=lambda r: (-r["n_subgroups"], -r["n_verses"])
    )

    # Pre-compute per-sub-group vcg rollup for §2.N summary blocks.
    # sg_id -> { vcg_id -> verse_count }. Drives the "verse-context groups
    # in this sub-group" summary at the top of each §2.N section.
    sg_vcg_summary: dict[int, dict[int, int]] = defaultdict(
        lambda: defaultdict(int)
    )
    for r in conn.execute("""
        SELECT vc.cluster_subgroup_id, vc.group_id
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code=?
           AND vc.cluster_subgroup_id IS NOT NULL
           AND vc.group_id IS NOT NULL
           AND COALESCE(vc.delete_flagged,0)=0
    """, (args.m_cluster,)):
        sg_vcg_summary[r["cluster_subgroup_id"]][r["group_id"]] += 1

    # --- 8. Build output Markdown
    print("Writing output...", flush=True)
    L: list[str] = []
    def add(s=""): L.append(s)

    # Heading tracker for the table of contents. Each emitted section
    # heading registers its (level, display_title, anchor_id) here, and
    # gets a paired `<a id="..."></a>` HTML anchor inserted just before
    # so cross-references work in any markdown renderer.
    toc_entries: list[tuple[int, str, str]] = []

    def add_section(level: int, title: str, anchor_id: str) -> None:
        toc_entries.append((level, title, anchor_id))
        add(f'<a id="{anchor_id}"></a>')
        add(f"{'#' * level} {title}")

    add(f"# {args.m_cluster} {cluster['description']} — "
        "comprehensive term + verse exposure")
    add()
    add(f"**Generated:** {now_iso()}  ")
    add(f"**Cluster:** `{args.m_cluster}` "
        f"(bucket={cluster['bucket']}, status={cluster['status']}, "
        f"version={cluster['version']})  ")
    add(f"**Source:** `database/bible_research.db`  ")
    add()
    add("**Scope of this report:** every database fact that connects to a "
        "term in this cluster, exposed by term and by verse. Items currently "
        "linked only at registry / collection level (not yet resolvable to a "
        "specific term) are listed in the appendix as candidates for future "
        "linkage. Numbered paragraphs are used throughout to make every "
        "item directly referenceable.")
    add()
    add("---")
    add()
    # Reserved insertion point for the table of contents — populated
    # after the body is built so we know all the headings.
    toc_insert_idx = len(L)

    # § Cluster summary
    add_section(2, "§1. Cluster summary", "s1")
    add()
    n_h = sum(1 for s in strongs_list if by_strong[s]["language"] == "Hebrew")
    n_g = sum(1 for s in strongs_list if by_strong[s]["language"] == "Greek")
    sum_active = sum(len(verses_by_mti[mid]) for mid in all_mti_ids)
    add(f"1. Description: {cluster['description']}")
    add(f"2. Bucket / Status / Version: {cluster['bucket']} / "
        f"{cluster['status']} / {cluster['version']}")
    add(f"3. Last updated: {cluster['last_updated_date']}")
    add(f"4. Terms in cluster: **{len(strongs_list)}** "
        f"(Hebrew {n_h} · Greek {n_g})")
    add(f"5. Active OWNER verses (sum across terms): {sum_active}")
    add(f"6. Contributor registries: {len(m_registries)}")

    # ---- Verse status summary (added 2026-05-07; default in every run)
    # Status precedence per (vr_id, mti_id):
    #   G > SA > NR > P > UT  — most "advanced" wins per pair, matching the
    #   per-term verse table's status determination in §3.
    vstatus_count = defaultdict(int)
    vtestament_count = defaultdict(int)
    sa_reason_count = defaultdict(int)
    for mid in all_mti_ids:
        for v in verses_by_mti.get(mid, []):
            vc_recs = vc_by_pair.get((mid, v["vr_id"]), [])
            s = "UT"
            sa_text = None
            for r in vc_recs:
                if r.get("delete_flagged"):
                    continue
                if (r.get("group_id") and r["group_id"] > 0
                        and r.get("is_relevant") == 1):
                    s = "G"
                    break
            else:
                for r in vc_recs:
                    if r.get("delete_flagged"):
                        continue
                    if r.get("set_aside_reason"):
                        s = "SA"
                        sa_text = r["set_aside_reason"]
                        break
                else:
                    for r in vc_recs:
                        if r.get("delete_flagged"):
                            continue
                        if (r.get("is_relevant") == 1
                                and r.get("group_id") in (None, 0)
                                and not r.get("set_aside_reason")):
                            s = "P"
                            break
                    else:
                        for r in vc_recs:
                            if r.get("delete_flagged"):
                                continue
                            if (r.get("is_relevant") == 0
                                    and not r.get("set_aside_reason")):
                                s = "NR"
                                break
            vstatus_count[s] += 1
            vtestament_count[v.get("testament") or "?"] += 1
            if sa_text:
                sa_reason_count[(sa_text or "")[:80]] += 1

    n_total_v = sum(vstatus_count.values())
    add()
    add(f"**Verse status summary** ({n_total_v} active verses)")
    add()
    add("| Status | Count | % | Meaning |")
    add("|---|---:|---:|---|")
    status_meanings = {
        "G":  "group-assigned (analysed)",
        "SA": "set-aside (with reason)",
        "NR": "not-relevant (is_relevant=0)",
        "P":  "pending (relevant but no group yet)",
        "UT": "untouched (no verse_context row)",
    }
    for s in ("G", "SA", "NR", "P", "UT"):
        c = vstatus_count[s]
        pct = (100 * c / n_total_v) if n_total_v else 0
        add(f"| {s} | {c} | {pct:.1f}% | {status_meanings[s]} |")
    add(f"| **Total** | **{n_total_v}** | 100% | |")
    add()
    # Testament split
    ot = vtestament_count.get("OT", 0)
    nt = vtestament_count.get("NT", 0)
    other = n_total_v - ot - nt
    bits = [f"OT {ot}", f"NT {nt}"]
    if other:
        bits.append(f"other {other}")
    add(f"**By testament:** {' · '.join(bits)}")
    add()
    if sa_reason_count:
        n_sa = sum(sa_reason_count.values())
        add(f"**Set-aside reasons** ({n_sa} rows):")
        add()
        for reason, n in sorted(
            sa_reason_count.items(), key=lambda x: -x[1]
        )[:15]:
            add(f"- ({n}) {sanitise(reason)}")
        add()
    # Derive gloss list from current term metadata (cluster.gloss can be
    # stale after term reassignments; mti_terms is authoritative).
    derived_gloss_items = []
    for s in sorted(strongs_list, key=lambda x: (
        (by_strong[x].get("gloss") or "").lower(),
        (by_strong[x].get("transliteration") or "").lower(),
    )):
        m = by_strong[s]
        gloss = (m.get("gloss") or "").strip()
        translit = (m.get("transliteration") or "").strip()
        if gloss and translit:
            derived_gloss_items.append(f"{gloss} ({translit})")
        elif gloss:
            derived_gloss_items.append(gloss)
        elif translit:
            derived_gloss_items.append(translit)
    full_gloss = ", ".join(derived_gloss_items)
    add(f"7. Gloss list ({len(derived_gloss_items)} entries — every "
        f"distinct term currently in the cluster, disambiguated by "
        f"transliteration):")
    add()
    add(full_gloss)
    add()
    # Patch-authoring reference table — one row per term with the integer
    # (mti_id, md_version, vc_status) values AI needs for VCREVISE / VCNEW /
    # VCGROUP / VCVERSE patch authoring (input_versions, terms_covered,
    # match clauses). Sorted by Strong's number for predictable lookup.
    add("**Patch-authoring reference table:** integer values per term "
        "for the patch's `_patch_meta.terms_covered` (mti_id) and "
        "`_patch_meta.input_versions` (md_version). Sorted by Strong's.")
    add()
    add("| Strong's | Translit | mti_id | md_version | vc_status |")
    add("|---|---|---:|---:|---|")
    for s in sorted(strongs_list):
        m = by_strong[s]
        translit = (m.get("transliteration") or "").strip() or "—"
        add(
            f"| {s} | {translit} | "
            f"{m.get('mti_id')} | "
            f"{m.get('md_version') if m.get('md_version') is not None else 0} | "
            f"{m.get('vc_status') or '—'} |"
        )
    add()
    # Sub-group breakdown
    # Post-M46 a term can be in multiple sub-groups; the count below
    # therefore sums distinct (term, sub-group) pairings, not distinct terms.
    # "terms assigned" is the count of distinct Strong's that have ≥1
    # sub-group mapping.
    if subgroups:
        sg_term_count = defaultdict(int)
        for s in strongs_list:
            for sg_id in strong_to_sg_ids.get(s, []):
                sg_term_count[sg_id] += 1
        n_assigned = sum(1 for s in strongs_list
                         if strong_to_sg_ids.get(s))
        unassigned = sum(1 for s in strongs_list
                         if not strong_to_sg_ids.get(s))
        add(f"8. Sub-group breakdown ({len(subgroups)} sub-groups, "
            f"{n_assigned} terms assigned"
            + (f", {unassigned} unassigned" if unassigned else "")
            + "; counts below are distinct term-in-sub-group pairs and "
            + "may sum higher than `terms assigned` when terms span "
            + "multiple sub-groups):")
        add()
        add("| Sub-group | Label | Terms | Description |")
        add("|---|---|---:|---|")
        for sg in subgroups:
            n = sg_term_count.get(sg["id"], 0)
            add(
                f"| `{sanitise(sg['subgroup_code'])}` | "
                f"{sanitise(sg['label'])} | {n} | "
                f"{sanitise(sg['core_description'])} |"
            )
        if unassigned:
            add(
                f"| _(unassigned)_ | — | {unassigned} | "
                f"Terms in this cluster with no `mti_term_subgroup` row |"
            )
        add()

    # ----- §1.9 Connectivity health -------------------------------------
    # Surfaces breaks in the chain
    #   verse → verse_context → verse_context_group / cluster_subgroup
    #   ↔ mti_term_subgroup → cluster_subgroup
    # Each check has an Hn code so it can be referenced in the body.
    add("9. Connectivity health "
        "(broken or missing links along verse → vc → vcg / sub-group → term):")
    add()
    health_rows = [
        ("H1", "Active vc rows in cluster with `cluster_subgroup_id` NULL "
               "— verse not routed to any sub-group",
         len(health["H1_unrouted_vc"])),
        ("H2", "Active vc rows with `is_relevant=1` but `group_id` NULL "
               "— relevant verse not yet in a meaning group",
         len(health["H2_relevant_no_group"])),
        ("H3", "vc.mti_term_id is not in its vcg's term set "
               "(`vcg_term`) — cross-term contamination, or vc points "
               "at a soft-deleted vcg",
         len(health["H3_vcg_term_mismatch"])),
        ("H4", "vc.cluster_subgroup_id set but the term has no "
               "`mti_term_subgroup` link to that sub-group "
               "— orphaned verse routing",
         len(health["H4_subgroup_route_orphan"])),
        ("H5", "Active `verse_context_group` rows with no active vc "
               "references — orphan meaning group",
         len(health["H5_orphan_vcg"])),
        ("H6", "Cluster terms with no `mti_term_subgroup` mapping "
               "— term placed in cluster but unassigned to any sub-group",
         len(health["H6_unassigned_terms"])),
        ("H7", "Cluster terms with sub-group mapping but zero "
               "`verse_context_group` rows — sub-group placed but verses "
               "never contextually grouped",
         len(health["H7_terms_without_vcg"])),
        ("H8", "vcgs whose active verses span multiple sub-groups — "
               "the same meaning is routed to different sub-groups; "
               "candidates for promotion, reassignment, or split",
         len(health["H8_vcg_spans_subgroups"])),
    ]
    add("| Code | Check | Count |")
    add("|---|---|---:|")
    for code, desc, n in health_rows:
        marker = " ⚠" if n else ""
        add(f"| `{code}`{marker} | {desc} | {n} |")
    add()
    # Detail tables (only emit when non-zero, capped at 50 rows)
    HEALTH_DETAIL_CAP = 50

    def emit_health_table(code, headers, rows, cell_fns):
        if not rows:
            return
        add(f"_`{code}` detail (showing {min(len(rows), HEALTH_DETAIL_CAP)} of "
            f"{len(rows)}):_")
        add()
        add("| " + " | ".join(headers) + " |")
        add("|" + "|".join(["---"] * len(headers)) + "|")
        for r in rows[:HEALTH_DETAIL_CAP]:
            add("| " + " | ".join(fn(r) for fn in cell_fns) + " |")
        add()

    emit_health_table(
        "H1",
        ["vc_id", "Reference", "Strong's", "mti_id"],
        health["H1_unrouted_vc"],
        [lambda r: str(r["vc_id"]), lambda r: sanitise(r["reference"]),
         lambda r: r["strongs_number"], lambda r: str(r["mti_term_id"])],
    )
    emit_health_table(
        "H2",
        ["vc_id", "Reference", "Strong's", "mti_id"],
        health["H2_relevant_no_group"],
        [lambda r: str(r["vc_id"]), lambda r: sanitise(r["reference"]),
         lambda r: r["strongs_number"], lambda r: str(r["mti_term_id"])],
    )
    emit_health_table(
        "H3",
        ["vc_id", "Reference", "vc Strong's", "vcg code", "vcg deleted?"],
        health["H3_vcg_term_mismatch"],
        [lambda r: str(r["vc_id"]), lambda r: sanitise(r["reference"]),
         lambda r: r["vc_strong"], lambda r: r["group_code"] or "",
         lambda r: "yes" if r["vcg_deleted"] else "no"],
    )
    emit_health_table(
        "H4",
        ["vc_id", "Reference", "Strong's", "Sub-group"],
        health["H4_subgroup_route_orphan"],
        [lambda r: str(r["vc_id"]), lambda r: sanitise(r["reference"]),
         lambda r: r["strongs_number"], lambda r: r["subgroup_code"] or ""],
    )
    emit_health_table(
        "H5",
        ["group_id", "Code", "Strong's", "Description"],
        health["H5_orphan_vcg"],
        [lambda r: str(r["group_id"]), lambda r: r["group_code"] or "",
         lambda r: r["strongs_number"],
         lambda r: sanitise((r["context_description"] or "")[:120])],
    )
    emit_health_table(
        "H6",
        ["mti_id", "Strong's", "Translit", "Gloss"],
        health["H6_unassigned_terms"],
        [lambda r: str(r["mti_id"]), lambda r: r["strongs_number"],
         lambda r: r["transliteration"] or "",
         lambda r: r["gloss"] or ""],
    )
    emit_health_table(
        "H7",
        ["mti_id", "Strong's", "Translit", "Gloss"],
        health["H7_terms_without_vcg"],
        [lambda r: str(r["mti_id"]), lambda r: r["strongs_number"],
         lambda r: r["transliteration"] or "",
         lambda r: r["gloss"] or ""],
    )
    emit_health_table(
        "H8",
        ["vcg", "Term", "Verses", "Sub-groups", "Dominant",
         "Dom n", "Minority n", "Minority breakdown"],
        health["H8_vcg_spans_subgroups"],
        [lambda r: f"`{r['group_code']}`",
         lambda r: r["strongs_number"],
         lambda r: str(r["n_verses"]),
         lambda r: str(r["n_subgroups"]),
         lambda r: r["dom_sg"],
         lambda r: str(r["dom_n"]),
         lambda r: str(r["minority_n"]),
         lambda r: r["minority_sgs"]],
    )

    # ----- helper: status precedence over verse_context records ----------
    def vc_status(vc_recs):
        """Return (status_code, group_code_str, set_aside_reason).
        Post-2026-05-10: returns the vcg.group_code (e.g. '911-001'),
        not the bare integer id, so the verse table cross-references the
        per-sub-group vcg summary at the top of each §2.N section."""
        for r in vc_recs:
            if r.get("delete_flagged"):
                continue
            if (r.get("group_id") and r.get("group_id") > 0
                    and r.get("is_relevant") == 1):
                vcg = vcg_by_id.get(r["group_id"])
                code = (vcg and vcg.get("group_code")) or str(r["group_id"])
                return ("G", code, "")
        for r in vc_recs:
            if r.get("delete_flagged"):
                continue
            if r.get("set_aside_reason"):
                return ("SA", "", r["set_aside_reason"])
        for r in vc_recs:
            if r.get("delete_flagged"):
                continue
            if (r.get("group_id") in (None, 0)
                    and r.get("is_relevant") == 0
                    and not r.get("set_aside_reason")):
                return ("NR", "", "")
        for r in vc_recs:
            if r.get("delete_flagged"):
                continue
            if (r.get("group_id") in (None, 0)
                    and r.get("is_relevant") == 1
                    and not r.get("set_aside_reason")):
                return ("P", "", "")
        return ("UT", "", "")

    def spans_cell_for(loc):
        spans = spans_at_loc.get(loc, [])
        seen_sn = set()
        items = []
        for sp in spans:
            if sp["strong"] in seen_sn:
                continue
            seen_sn.add(sp["strong"])
            label = (
                f"{sp['strong']} {sp['translit']}"
                + (f" ({sp['gloss']})" if sp['gloss'] else "")
            )
            if sp["target_word"]:
                label += f" [{sp['target_word']}]"
            items.append(label)
        return "; ".join(items)

    # ----- §2. Verses by sub-group ---------------------------------------
    add_section(2, "§2. Verses by sub-group", "s2")
    add()
    add("All verses for cluster terms, grouped by the analytical sub-group "
        "the term belongs to. Within each sub-group the rows are sorted "
        "canonically (book · chapter · verse). The **Term** column shows the "
        "Strong's number and transliteration of the cluster term whose "
        "`wa_verse_records` row generated this entry; **Spans in verse** "
        "lists every term-span recorded at that verse location.")
    add()
    add("Status precedence: G = group-assigned (analysed) · "
        "SA = set-aside · NR = is_relevant=0 · "
        "P = pending in VC · UT = untouched (no VC row).")
    add()
    add("**ID columns:** `vr_id` is `wa_verse_records.id`; `mti_id` is "
        "`mti_terms.id` (also `wa_verse_records.mti_term_id` and "
        "`verse_context.mti_term_id`). Both are exposed so AI can author "
        "VCREVISE / VCNEW / VCVERSE patches directly from this report — "
        "no separate ID-resolver query needed. The `(vr_id, mti_id)` "
        "pair is the natural key for any `verse_context` operation.")
    add()

    # Bucket verse rows by subgroup id, with a sentinel 0 = unrouted.
    # Post-M46 the verse-level routing lives on verse_context.cluster_subgroup_id,
    # not on the term. A single wa_verse_records row (per mti_term_id) is
    # rendered under EACH sub-group its vc rows route to (so a 'both'-DEC-3
    # verse appears in M26-A1 and M26-A2). Verses with no active vc row, or
    # with vc.cluster_subgroup_id NULL, fall to bucket 0 (unrouted).
    sg_verse_rows = defaultdict(list)
    for s in strongs_list:
        meta = by_strong[s]
        for mid in mti_ids_per_strong[s]:
            for v in verses_by_mti.get(mid, []):
                vc_recs = vc_by_pair.get((mid, v["vr_id"]), [])
                # Distinct sub-group ids referenced by ACTIVE vc rows for
                # this (mti_term_id, vr_id). De-dupe here so a single verse
                # doesn't appear twice under the same sub-group when there
                # are multiple vc rows in the same bucket.
                sg_ids_for_v = []
                seen_sg = set()
                for vc in vc_recs:
                    if vc.get("delete_flagged"):
                        continue
                    sg_id = vc.get("cluster_subgroup_id")
                    if sg_id is None:
                        continue
                    if sg_id not in seen_sg:
                        seen_sg.add(sg_id)
                        sg_ids_for_v.append(sg_id)
                if not sg_ids_for_v:
                    sg_ids_for_v = [0]
                for sg_id in sg_ids_for_v:
                    sg_verse_rows[sg_id].append({
                        "strong": s,
                        "translit": meta.get("transliteration") or "",
                        "v": v,
                    })

    # De-dupe per (subgroup, term, location) so a term that appears
    # multiple times in the same verse only shows once in the row stream.
    for sg_id, rows in sg_verse_rows.items():
        seen = set()
        deduped = []
        for row in rows:
            v = row["v"]
            key = (row["strong"], v["book_id"], v["chapter"], v["verse_num"])
            if key in seen:
                continue
            seen.add(key)
            deduped.append(row)
        deduped.sort(key=lambda r: (
            r["v"]["book_id"], r["v"]["chapter"], r["v"]["verse_num"],
            r["strong"],
        ))
        sg_verse_rows[sg_id] = deduped

    sg_index = 0
    for sg in subgroups:
        sg_index += 1
        rows = sg_verse_rows.get(sg["id"], [])
        # Term list for this sub-group (terms whose mti_term_subgroup
        # mapping includes this sub-group). A term spanning multiple
        # sub-groups is listed under each.
        sg_terms = [
            (s, by_strong[s].get("transliteration") or "")
            for s in strongs_list
            if sg["id"] in strong_to_sg_ids.get(s, [])
        ]
        add_section(
            3,
            f"§2.{sg_index} `{sanitise(sg['subgroup_code'])}` — "
            f"{sanitise(sg['label'])}",
            f"s2-{sg_index}",
        )
        add()
        add(f"_{sanitise(sg['core_description'])}_")
        add()
        add(f"1. Terms in sub-group ({len(sg_terms)}): "
            + ", ".join(f"{s} {t}".strip() for s, t in sg_terms))
        # Verse-context groups in this sub-group: every distinct vcg whose
        # active verses route here. Lets the analyst see the meaning fabric
        # of the sub-group at a glance — this is the data that flows into
        # findings.
        vcg_counts_for_sg = sg_vcg_summary.get(sg["id"], {})
        if vcg_counts_for_sg:
            add(f"2. Verse-context groups in this sub-group "
                f"({len(vcg_counts_for_sg)}):")
            add()
            add("| Group code | Term | Description | Verses (here) |")
            add("|---|---|---|---:|")
            for vcg_id, n_v in sorted(
                vcg_counts_for_sg.items(),
                key=lambda kv: -kv[1],
            ):
                vcg = vcg_by_id.get(vcg_id)
                if not vcg:
                    add(f"| _(missing vcg id {vcg_id})_ | — | — | {n_v} |")
                    continue
                term_strong = mti_to_strong.get(vcg["mti_term_id"], "?")
                term_translit = (
                    by_strong.get(term_strong, {}).get("transliteration")
                    or ""
                )
                term_label = f"{term_strong} *{term_translit}*".strip()
                desc = vcg.get("context_description") or ""
                add(
                    f"| `{vcg.get('group_code') or '?'}` | "
                    f"{sanitise(term_label)} | "
                    f"{sanitise(desc)} | {n_v} |"
                )
            add()
            add(f"3. Verse rows ({len(rows)}, deduped by term × location):")
        else:
            add(f"2. Verse-context groups in this sub-group: (none)")
            add(f"3. Verse rows ({len(rows)}, deduped by term × location):")
        add()
        if not rows:
            add("(no verses)")
            add()
            continue
        add("| vr_id | mti_id | Reference | Term | Status | Group code | "
            "Set-aside reason | Spans in verse | Verse text |")
        add("|---:|---:|---|---|---|---|---|---|---|")
        for row in rows:
            v = row["v"]
            vc_recs = vc_by_pair.get((v["mti_term_id"], v["vr_id"]), [])
            status, gid, sar = vc_status(vc_recs)
            spans_text = spans_cell_for(
                (v["book_id"], v["chapter"], v["verse_num"])
            )
            term_label = f"{row['strong']} {row['translit']}".strip()
            add(
                f"| {v['vr_id']} | {v['mti_term_id']} | "
                f"{sanitise(v['reference'])} | "
                f"{sanitise(term_label)} | {status} | {gid} | "
                f"{sanitise(sar)} | "
                f"{sanitise(spans_text)} | "
                f"{sanitise(v.get('verse_text'))} |"
            )
        add()

    # Unrouted rows: vc rows with cluster_subgroup_id NULL (and any
    # verses for terms with no mti_term_subgroup mapping at all).
    if sg_verse_rows.get(0):
        sg_index += 1
        rows = sg_verse_rows[0]
        unassigned_terms = [
            (s, by_strong[s].get("transliteration") or "")
            for s in strongs_list if not strong_to_sg_ids.get(s)
        ]
        add_section(
            3,
            f"§2.{sg_index} _(unrouted / unassigned)_",
            f"s2-{sg_index}",
        )
        add()
        add("_Verses whose `verse_context.cluster_subgroup_id` is NULL, "
            "or whose term has no `mti_term_subgroup` mapping._")
        add()
        add(f"1. Terms ({len(unassigned_terms)}): "
            + ", ".join(f"{s} {t}".strip() for s, t in unassigned_terms))
        add(f"2. Verse rows ({len(rows)}):")
        add()
        add("| vr_id | mti_id | Reference | Term | Status | Group | "
            "Set-aside reason | Spans in verse | Verse text |")
        add("|---:|---:|---|---|---|---|---|---|---|")
        for row in rows:
            v = row["v"]
            vc_recs = vc_by_pair.get((v["mti_term_id"], v["vr_id"]), [])
            status, gid, sar = vc_status(vc_recs)
            spans_text = spans_cell_for(
                (v["book_id"], v["chapter"], v["verse_num"])
            )
            term_label = f"{row['strong']} {row['translit']}".strip()
            add(
                f"| {v['vr_id']} | {v['mti_term_id']} | "
                f"{sanitise(v['reference'])} | "
                f"{sanitise(term_label)} | {status} | {gid} | "
                f"{sanitise(sar)} | "
                f"{sanitise(spans_text)} | "
                f"{sanitise(v.get('verse_text'))} |"
            )
        add()

    # § Per-term sections
    add_section(2, "§3. Per-term comprehensive detail", "s3")
    add()
    add("Each term gets numbered sections: identity • meaning • "
        "anchor-verse linkages • groups • findings • pointers • auxiliary "
        "data. Verses are not repeated here — they are listed by sub-group "
        "in §2. Items linked only by registry are summarised here; "
        "exhaustive lists are in the appendix §4.")
    add()

    sorted_strongs = sorted(
        strongs_list,
        key=lambda s: -sum(
            len(verses_by_mti[mid]) for mid in mti_ids_per_strong[s]
        )
    )

    for s in sorted_strongs:
        m = by_strong[s]
        add("---")
        add()
        add_section(
            3,
            f"{s} {m['transliteration'] or ''} — {m['gloss'] or ''} "
            f"(`mti_id={m.get('mti_id')}`)",
            f"t-{s}",
        )
        add()

        # Identity (numbered)
        add("**Identity & meaning**")
        add()
        reg = (f"R{m['reg_no']:03d} {m['reg_word']}"
               if m.get("reg_no") else "—")
        sg_ids = strong_to_sg_ids.get(s, [])
        sg_label_parts = []
        for sg_id in sg_ids:
            sg = sg_by_id.get(sg_id)
            if sg:
                sg_label_parts.append(
                    f"`{sg['subgroup_code']}` ({sg['label']})"
                )
        sg_label = " · ".join(sg_label_parts) or "—"
        add(f"1. Strong's: `{s}` · Lang: "
            f"{m['language'] or '?'} · "
            f"Owner: {m.get('term_owner_type') or '—'}")
        add(f"2. Registry: {reg} · "
            f"Legacy C-cluster: "
            f"{m.get('legacy_c_cluster') or '—'}")
        add(f"3. Sub-group: {sg_label}")
        add(f"4. Term status: {m.get('mti_status') or '—'} · "
            f"Evidential: {m.get('evidential_status') or '—'} · "
            f"Occurrences: {m.get('occurrence_count') or 0}")
        # Patch-authoring reference values: AI uses these directly when
        # authoring VCREVISE / VCNEW / VCGROUP / VCVERSE patches — no
        # separate ID-resolver query needed.
        add(f"5. Patch-authoring refs: "
            f"`mti_id={m.get('mti_id')}` · "
            f"`md_version={m.get('md_version') if m.get('md_version') is not None else 0}` · "
            f"`vc_status={m.get('vc_status') or '—'}`")
        if m.get("short_def_mounce"):
            add(f"6. Mounce short-def: {m['short_def_mounce']}")
        if m.get("retention_note"):
            add(f"7. Retention note: {m['retention_note']}")
        add()

        if m.get("inv_meaning"):
            add("**Meaning text**")
            add()
            # Render meaning text as prose paragraph (preserve line breaks
            # only as paragraph breaks; otherwise it is one block)
            for line in m["inv_meaning"].split("\n"):
                if line.strip():
                    add(line.strip())
                    add()
            if not m["inv_meaning"].strip():
                add(m["inv_meaning"])
                add()

        # Verses are listed in §2 (by sub-group), not repeated here.
        verse_count = sum(
            len(verses_by_mti.get(mid, []))
            for mid in mti_ids_per_strong[s]
        )
        seen_locs = set()
        for mid in mti_ids_per_strong[s]:
            for v in verses_by_mti.get(mid, []):
                seen_locs.add(
                    (v["book_id"], v["chapter"], v["verse_num"])
                )
        add(f"**Verses:** {len(seen_locs)} distinct locations "
            f"(see §2 for the verse table grouped by sub-group).")
        add()

        # Group memberships
        all_group_rows = []
        for mid in mti_ids_per_strong[s]:
            all_group_rows.extend(groups_by_mti[mid])
        seen_g = set()
        groups = []
        for g in all_group_rows:
            if g["group_id"] in seen_g:
                continue
            seen_g.add(g["group_id"])
            groups.append(g)
        add(f"**Group memberships ({len(groups)})**")
        add()
        if not groups:
            add("(no `verse_context_group` rows for this term)")
            add()
        else:
            add("| Group ID | Code | Description | Notes |")
            add("|---|---|---|---|")
            for g in groups:
                add(
                    f"| {g['group_id']} | {sanitise(g['group_code'])} | "
                    f"{sanitise(g['context_description'])} | "
                    f"{sanitise(g['notes'])} |"
                )
            add()

        # Findings — direct
        flist = findings_direct.get(s, [])
        add(f"**Findings — direct (Strong's mention) ({len(flist)})**")
        add()
        if not flist:
            add("(none)")
            add()
        else:
            add("| Finding ID | Type | Anchor verses | Excerpt |")
            add("|---|---|---|---|")
            for f in flist:
                add(
                    f"| {sanitise(f['finding_id'])} | "
                    f"{sanitise(f['finding_type'])} | "
                    f"{sanitise(f['anchor_verses'])} | "
                    f"{sanitise(f['finding'])} |"
                )
            add()

        # Findings — via anchor
        falist = findings_via_anchor.get(s, [])
        seen_fpk = set()
        fa_unique = []
        for f in falist:
            if f["id"] in seen_fpk:
                continue
            seen_fpk.add(f["id"])
            fa_unique.append(f)
        add(f"**Findings — via anchor verse ({len(fa_unique)} unique)**")
        add()
        if not fa_unique:
            add("(none)")
            add()
        else:
            add("| Finding ID | Type | Matched anchor refs | Excerpt |")
            add("|---|---|---|---|")
            for f in fa_unique:
                refs = ", ".join(f.get("matched_anchor_refs") or [])
                add(
                    f"| {sanitise(f['finding_id'])} | "
                    f"{sanitise(f['finding_type'])} | "
                    f"{sanitise(refs)} | "
                    f"{sanitise(f['finding'])} |"
                )
            add()

        # SD pointers — direct
        plist = pointers_direct.get(s, [])
        add(f"**SD pointers — direct ({len(plist)})**")
        add()
        if not plist:
            add("(none)")
            add()
        else:
            add("| Pointer | Priority | Strong's ref | Description |")
            add("|---|---|---|---|")
            for p in plist:
                add(
                    f"| {sanitise(p['flag_label'])} | "
                    f"{sanitise(p['priority'])} | "
                    f"{sanitise(p['strongs_reference'])} | "
                    f"{sanitise(p['description'])} |"
                )
            add()

        # Auxiliary data (numbered sub-lists)
        xrefs = cross_refs_by_strong.get(s, [])
        rfam = root_family_by_strong.get(s, [])
        rels = related_words_by_strong.get(s, [])
        qfl = quality_flags_by_strong.get(s, [])
        tfl = term_flags_by_strong.get(s, [])

        if xrefs or rfam or rels or qfl or tfl:
            add("**Auxiliary data**")
            add()
        if xrefs:
            add(f"_Cross-references ({len(xrefs)}):_")
            add()
            for i, x in enumerate(xrefs, 1):
                add(f"{i}. {x['registry']} · {x.get('word','') or ''} · "
                    f"{x.get('word_data_reference','') or ''}")
            add()
        if rfam:
            add(f"_Root family ({len(rfam)}):_")
            add()
            for i, r in enumerate(rfam, 1):
                add(f"{i}. `{r['root_code']}` ({r['root_language']}): "
                    f"{r.get('root_gloss','') or ''}")
            add()
        if rels:
            add(f"_Related words ({len(rels)}):_")
            add()
            for i, r in enumerate(rels, 1):
                line = (
                    f"{i}. {r['related_strong']} "
                    f"{r.get('related_translit','') or ''} → "
                    f"{r.get('related_gloss','') or ''}"
                )
                if r.get("relationship_note"):
                    line += f" — {r['relationship_note']}"
                add(line)
            add()
        if qfl:
            add(f"_Data-quality flags ({len(qfl)}):_")
            add()
            for i, f in enumerate(qfl, 1):
                add(f"{i}. flag_id={f['flag_id']} · "
                    f"{f.get('description','') or ''}")
            add()
        if tfl:
            add(f"_Term flags ({len(tfl)}):_")
            add()
            for i, f in enumerate(tfl, 1):
                preview = ", ".join(
                    f"{k}={v}" for k, v in f.items()
                    if k not in ("strongs_number", "id") and v
                )
                add(f"{i}. {preview}")
            add()

    # § Appendix
    add("---")
    add()
    add_section(
        2,
        "§4. Appendix — items linked at registry or collection level",
        "s4",
    )
    add()

    # 3.1
    linked_finding_ids = set()
    for s in strongs_list:
        linked_finding_ids.update(f["id"] for f in findings_direct[s])
        linked_finding_ids.update(f["id"] for f in findings_via_anchor[s])
    registry_only_findings = []
    for reg_id in m_registries:
        for f in findings_by_registry.get(reg_id, []):
            if f["id"] not in linked_finding_ids:
                registry_only_findings.append(f)
    seen_f = set()
    reg_only_uniq = []
    for f in registry_only_findings:
        if f["id"] in seen_f:
            continue
        seen_f.add(f["id"])
        reg_only_uniq.append(f)
    add_section(
        3,
        f"§4.1 Findings from contributor registries with no "
        f"term-level link ({len(reg_only_uniq)})",
        "s4-1",
    )
    add()
    if not reg_only_uniq:
        add("(none)")
        add()
    else:
        add("These findings sit on a registry that contributes terms to "
            "this cluster, but their text and anchor verses don't resolve "
            "to any specific cluster term. Candidates for term-level "
            "enrichment.")
        add()
        add("| Finding ID | Type | Registry | Anchor verses | Excerpt |")
        add("|---|---|---|---|---|")
        for f in reg_only_uniq:
            reg_id = f["registry_id"]
            reg_label = "?"
            for s in strongs_list:
                m = by_strong[s]
                if m.get("owning_registry_fk") == reg_id:
                    reg_label = (f"R{m['reg_no']:03d} {m['reg_word']}"
                                 if m.get('reg_no') else "?")
                    break
            add(
                f"| {sanitise(f['finding_id'])} | "
                f"{sanitise(f['finding_type'])} | "
                f"{reg_label} | {sanitise(f['anchor_verses'])} | "
                f"{sanitise(f['finding'])} |"
            )
        add()

    # 3.2
    linked_pointer_ids = set()
    for s in strongs_list:
        linked_pointer_ids.update(p["id"] for p in pointers_direct[s])
    registry_only_pointers = []
    for reg_id in m_registries:
        for p in pointers_by_registry.get(reg_id, []):
            if p["id"] not in linked_pointer_ids:
                registry_only_pointers.append(p)
    seen_p = set()
    reg_only_p_uniq = []
    for p in registry_only_pointers:
        if p["id"] in seen_p:
            continue
        seen_p.add(p["id"])
        reg_only_p_uniq.append(p)
    add_section(
        3,
        f"§4.2 SD pointers from contributor registries with no "
        f"term-level link ({len(reg_only_p_uniq)})",
        "s4-2",
    )
    add()
    if not reg_only_p_uniq:
        add("(none)")
        add()
    else:
        add("| Pointer | Priority | Strong's ref | Description |")
        add("|---|---|---|---|")
        for p in reg_only_p_uniq:
            add(
                f"| {sanitise(p['flag_label'])} | "
                f"{sanitise(p['priority'])} | "
                f"{sanitise(p['strongs_reference'])} | "
                f"{sanitise(p['description'])} |"
            )
        add()

    # 3.3
    add_section(
        3,
        f"§4.3 Prose sections from contributor registries "
        f"({len(prose_sections)})",
        "s4-3",
    )
    add()
    if not prose_sections:
        add("(none)")
        add()
    else:
        add("Registry-level analytical prose. Useful as background; "
            "not term-linked.")
        add()
        add("| Reg | Section type | Heading | Status | Version | "
            "Word count |")
        add("|---|---|---|---|---|---:|")
        for ps in prose_sections:
            reg_id = ps["registry_id"]
            reg_label = "?"
            for s in strongs_list:
                m = by_strong[s]
                if m.get("owning_registry_fk") == reg_id:
                    reg_label = (f"R{m['reg_no']:03d}"
                                 if m.get('reg_no') else "?")
                    break
            add(
                f"| {reg_label} | "
                f"{sanitise(ps.get('section_type_code'))} | "
                f"{sanitise(ps['heading'])} | "
                f"{sanitise(ps.get('status'))} | "
                f"{ps.get('version') or ''} | "
                f"{ps.get('word_count') or 0} |"
            )
        add()

    # 3.4 Cluster-internal groups
    cluster_groups = set()
    for mid in all_mti_ids:
        for g in groups_by_mti[mid]:
            cluster_groups.add(g["group_id"])
    add_section(
        3,
        f"§4.4 Cluster-internal verse_context_group rows "
        f"({len(cluster_groups)})",
        "s4-4",
    )
    add()
    if not cluster_groups:
        add("(none)")
        add()
    else:
        add("Deduplicated list of all `verse_context_group` rows that "
            "appear in this cluster (post-M47: a vcg may be linked to "
            "multiple terms via `vcg_term`; the Strong's column is a "
            "comma-joined list of all linked terms).")
        add()
        ph_g = ",".join("?" * len(cluster_groups))
        all_groups = conn.execute(f"""
            SELECT vcg.id, vcg.group_code, vcg.context_description,
                   vcg.notes,
                   GROUP_CONCAT(DISTINCT mt.strongs_number) AS strongs_list
              FROM verse_context_group vcg
              LEFT JOIN vcg_term vt ON vt.vcg_id=vcg.id
                AND COALESCE(vt.delete_flagged,0)=0
              LEFT JOIN mti_terms mt ON mt.id=vt.mti_term_id
             WHERE vcg.id IN ({ph_g})
             GROUP BY vcg.id
             ORDER BY vcg.group_code
        """, list(cluster_groups)).fetchall()
        add("| Group ID | Code | Strong's (linked terms) | Description | Notes |")
        add("|---|---|---|---|---|")
        for g in all_groups:
            add(
                f"| {g['id']} | {sanitise(g['group_code'])} | "
                f"{sanitise(g['strongs_list'] or '—')} | "
                f"{sanitise(g['context_description'])} | "
                f"{sanitise(g['notes'])} |"
            )
        add()

    # 3.5
    add_section(3, "§4.5 Cross-cluster orphan findings/pointers", "s4-5")
    add()
    add("Findings + SD pointers that mention M-cluster vocabulary but "
        "originate from registries that do NOT contribute terms to this "
        "cluster — see "
        f"[wa-cluster-{args.m_cluster.lower()}-finding-orphans-v1-…]"
        "(../../../outputs/markdown/) for the full scan.")
    add()

    # ----- Build and splice the table of contents into the reserved slot
    toc_lines: list[str] = ['<a id="toc"></a>', "## Table of contents", ""]
    for level, title, anchor in toc_entries:
        indent = "  " * (level - 2) if level > 2 else ""
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    toc_lines.append("")
    toc_lines.append("---")
    toc_lines.append("")
    L[toc_insert_idx:toc_insert_idx] = toc_lines

    conn.close()

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
