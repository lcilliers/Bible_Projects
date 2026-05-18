"""M04 retrofit Step 5: parse AI's VCG-design output + apply.

Parses the 6 batch files in `Sessions/Session_Clusters/M04/files vcg design/`.
- 322 disposition lines (ASSIGN-EXISTING-VCG or CREATE-NEW-VCG)
- 18 unique new VCG codes (anchor + description metadata embedded below from obslog)
- 85 ASSIGN-EXISTING dispositions (8 of which are cross-sub-group per researcher direction)

Mode:
  --dry-run    Parse + validate; report; no DB writes.
  --apply      Parse + validate + apply (transactional).
"""
from __future__ import annotations
import argparse
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SOURCE = "M04-step5-vcg-design-20260518"
INPUT_DIR = Path("Sessions/Session_Clusters/M04/files vcg design")
OUT_REPORT = Path(f"Sessions/Session_Clusters/M04/WA-M04-step5-vcg-design-applied-v1-{TODAY}.md")

DISP_RE = re.compile(
    r"^vc=(\d+)\s+(ASSIGN-EXISTING-VCG|CREATE-NEW-VCG)\s+(\S+)\s*[—–\-]+\s*(.+?)$",
    re.IGNORECASE,
)

# ----- 18 new VCGs: anchor + description (lifted from the obslog summary) -----
# Format: { code: { anchor_vc_id, anchor_ref, description } }
NEW_VCG_META = {
    # M04-N (Horizontal Relational)
    "M04-N-VCG-01": {
        "anchor_vc_id": 9661,
        "anchor_ref": "Mic 1:16",
        "description": "Horizontal relational pleasantness — parental attachment and the value of near neighbour. Inner-being-in-relationship: pleasantness directed at persons in horizontal bonds (parental delight; neighbourly value).",
    },
    "M04-N-VCG-02": {
        "anchor_vc_id": 44868,
        "anchor_ref": "Rev 13:3",
        "description": "Captivating marvel at a powerful entity — beast-wonder as dangerous horizontal captivation. The collective awe drawn out by an extraordinary (but corrupt) figure; inner-being-as-captivation.",
    },
    # M04-P (Corrupt/Illicit)
    "M04-P-VCG-01": {
        "anchor_vc_id": 32677,
        "anchor_ref": "Eze 20:28",
        "description": "Misdirected sacrificial delight — ni.cho.ach aroma directed to idols rather than YHWH. The pleasing-aroma worship-act with corrupt object: inner-being-as-disordered-worship.",
    },
    "M04-P-VCG-02": {
        "anchor_vc_id": 10669,
        "anchor_ref": "Eze 23:12",
        "description": "Lustful captivation — che.med craving directed toward foreign military splendour. Inner-being-as-illicit-desire that drives spiritual adultery.",
    },
    "M04-P-VCG-03": {
        "anchor_vc_id": 35728,
        "anchor_ref": "Hab 3:14",
        "description": "Predatory exultation — a.li.tsut as sinister inner gladness in cruelty against the poor. Inner-being-as-corrupt-rejoicing in destruction.",
    },
    # M04-M (Pleasing as Obedience)
    "M04-M-VCG-01": {
        "anchor_vc_id": 32643,
        "anchor_ref": "Lev 1:17",
        "description": "Sacrificial-obedience pleasing aroma — ni.cho.ach in righteous cultic worship. The pleasing aroma rising as the inner-being mark of correctly-offered sacrifice.",
    },
    "M04-M-VCG-02": {
        "anchor_vc_id": 17930,
        "anchor_ref": "1Sa 15:22",
        "description": "Doing what is good and right in God's sight — obedient inner orientation as covenantal-good. Tov as the term for the soul's directed orientation toward what God approves; obedience as the inner-being measure of what is good.",
    },
    # M04-C (NT Joy — new VCG within existing sub-group)
    "M04-C-VCG-06": {
        "anchor_vc_id": 18448,
        "anchor_ref": "Col 3:15",
        "description": "Pauline and heavenly thanksgiving — eucharistia/eucharistos as Godward gratitude. Thanksgiving as constitutionally located (heart; spirit), commanded, and producing community/devotional fruit; distinct from chairo/chara joy in its directed-gratitude register.",
    },
    # M04-O (Circumstantial Gladness)
    "M04-O-VCG-01": {
        "anchor_vc_id": 19665,
        "anchor_ref": "Pro 25:25",
        "description": "Good news and the refreshing word — the soul's response to speech, message, or news received as good. Inner-being-as-circumstantial-pleasure at a beneficial communication.",
    },
    "M04-O-VCG-02": {
        "anchor_vc_id": 18058,
        "anchor_ref": "Hos 2:7",
        "description": "Better-than comparatives — the soul's comparative assessment of circumstances. Tov used to name a preferred circumstance against an alternative, with the inner-being faculty operating as comparative-evaluator.",
    },
    "M04-O-VCG-03": {
        "anchor_vc_id": 17981,
        "anchor_ref": "1Sa 16:23",
        "description": "Wellbeing as flourishing — the experienced state of goodness in body, kingdom, or covenant context. Inner-being content carried by 'it was well with him' / 'good hand of God' language.",
    },
    "M04-O-VCG-04": {
        "anchor_vc_id": 18029,
        "anchor_ref": "Neh 2:18",
        "description": "God's good hand and covenantal promise-goodness; makarismos blessedness. The inner-being state of being under sustained divine favour and the recognition of received blessedness.",
    },
    # M04-K (Material/Sensory)
    "M04-K-VCG-01": {
        "anchor_vc_id": 32636,
        "anchor_ref": "Gen 8:21",
        "description": "Sacrificial pleasing aroma (ni.cho.ach) — the dominant righteous-worship register. God's receptive inner satisfaction at correctly-offered sacrifice; the foundational instance (Gen 8:21) sets the pattern for all subsequent ni.cho.ach offerings.",
    },
    "M04-K-VCG-02": {
        "anchor_vc_id": 9586,
        "anchor_ref": "Isa 47:1",
        "description": "Sensory luxury and pampered ease (a.nog, ta.a.nug, a.las) — the refined-comfort inner register, ranging from genuine domestic pleasantness through dainty privilege to siege-curse-inverted luxury.",
    },
    "M04-K-VCG-03": {
        "anchor_vc_id": 17996,
        "anchor_ref": "Pro 15:17",
        "description": "Wisdom better-than comparatives involving material goods — tov used in wisdom-literature paradigms where a modest material good is judged superior to abundance with corruption. Inner-being-as-evaluative-discrimination of material/relational alternatives.",
    },
    # M04-L (Evaluative Goodness)
    "M04-L-VCG-01": {
        "anchor_vc_id": 63123,
        "anchor_ref": "Gen 1:31",
        "description": "Divine character goodness — 'the Lord is good' / ki-tov declarations and the Gen 1 creation appraisals ('God saw that it was good'). The divine evaluative faculty operating on creation and on God's own character; the doxological refrain 'for he is good, for his steadfast love endures forever.'",
    },
    "M04-L-VCG-02": {
        "anchor_vc_id": 17923,
        "anchor_ref": "Mic 6:8",
        "description": "Moral-evaluative appraisal of persons and actions — tov as the inner-being faculty by which conduct, character, and choice are weighed and named good or not-good. Mic 6:8 as the definitional anchor for the soul's faculty of moral judgement.",
    },
    "M04-L-VCG-03": {
        "anchor_vc_id": 17993,
        "anchor_ref": "Pro 8:11",
        "description": "Wisdom's surpassing worth — wisdom evaluated as better than gold, silver, or jewels. The inner-being faculty by which wisdom's superlative value is recognised and named.",
    },
}


def parse_dispositions():
    disp = []
    for fp in sorted(INPUT_DIR.glob("WA-M04-step5-vcg-design-batch*.md")):
        for line in fp.read_text(encoding="utf-8").splitlines():
            m = DISP_RE.match(line.strip())
            if not m:
                continue
            disp.append({
                "vc_id": int(m.group(1)),
                "kind": m.group(2).upper(),
                "target": m.group(3),
                "rationale": m.group(4),
                "source": fp.name,
            })
    return disp


def validate(disp, conn):
    errors = []
    warnings = []

    # Build existing VCG code map (active M04 VCGs)
    existing_codes = {
        r[0]: r[1] for r in conn.execute(
            """
            SELECT vcg.group_code, vcg.id FROM verse_context_group vcg
            WHERE COALESCE(vcg.delete_flagged,0)=0
              AND EXISTS (
                SELECT 1 FROM vcg_term vt
                JOIN mti_terms mt ON mt.id=vt.mti_term_id
                WHERE vt.vcg_id=vcg.id AND mt.cluster_code='M04'
                  AND COALESCE(vt.delete_flagged,0)=0
              )
            """
        ).fetchall()
    }

    # Build sub-group code map
    sg_map = {
        r[0]: r[1] for r in conn.execute(
            "SELECT subgroup_code, id FROM cluster_subgroup WHERE cluster_code='M04' AND COALESCE(delete_flagged,0)=0"
        ).fetchall()
    }

    # Expected vc_id set (pending VCG assignment)
    expected_vcs = {
        r[0] for r in conn.execute(
            """
            SELECT vc.id FROM verse_context vc
            JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
            WHERE cs.cluster_code='M04'
              AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
              AND vc.group_id IS NULL
            """
        ).fetchall()
    }
    actual_vcs = {d["vc_id"] for d in disp}
    missing = expected_vcs - actual_vcs
    extra = actual_vcs - expected_vcs
    if missing:
        errors.append(f"Missing {len(missing)} expected vc_ids: {sorted(missing)[:10]}{'...' if len(missing)>10 else ''}")
    if extra:
        errors.append(f"Extra {len(extra)} unexpected vc_ids: {sorted(extra)[:10]}")

    # Check duplicate vc_id dispositions
    seen_vc = set()
    for d in disp:
        if d["vc_id"] in seen_vc:
            errors.append(f"Duplicate disposition for vc={d['vc_id']}")
        seen_vc.add(d["vc_id"])

    # Validate targets: each target must be either (a) an existing M04 VCG code, or
    # (b) a known-new VCG code (in NEW_VCG_META). The kind field (ASSIGN-EXISTING
    # vs CREATE-NEW) is informational — once AI has named a new VCG, subsequent
    # batches may legitimately refer to it as "ASSIGN-EXISTING" within the AI session,
    # even though from CC's perspective it's still being created in this apply pass.
    for d in disp:
        if d["target"] not in existing_codes and d["target"] not in NEW_VCG_META:
            errors.append(
                f"vc={d['vc_id']}: target {d['target']!r} is neither an existing M04 VCG code nor a known new VCG code in NEW_VCG_META"
            )

    # New VCG codes must not collide with existing
    new_codes = set(NEW_VCG_META.keys())
    for code in new_codes:
        if code in existing_codes:
            errors.append(f"New VCG code {code!r} already exists in active M04 VCGs")

    # Anchor sanity — each new VCG's anchor_vc_id must be a member (across all kinds)
    for code in new_codes:
        meta = NEW_VCG_META.get(code, {})
        anchor_vc = meta.get("anchor_vc_id")
        members = {d["vc_id"] for d in disp if d["target"] == code}
        if anchor_vc and anchor_vc not in members:
            errors.append(f"VCG {code!r}: anchor vc={anchor_vc} is not a member of the disposition list ({len(members)} members)")

    return errors, warnings, existing_codes, sg_map


def apply_directive(disp, existing_codes, conn):
    """Apply in a single transaction: INSERT VCGs + vcg_term + UPDATE verse_context + anchor flag."""
    cur = conn.cursor()
    cur.execute("BEGIN")
    counts = Counter()

    try:
        # 1. INSERT new verse_context_group rows
        new_vcg_id_map = {}  # code → id
        new_codes = sorted({d["target"] for d in disp if d["kind"] == "CREATE-NEW-VCG"})
        for code in new_codes:
            meta = NEW_VCG_META[code]
            cur.execute(
                """
                INSERT INTO verse_context_group (group_code, context_description, notes, delete_flagged)
                VALUES (?, ?, ?, 0)
                """,
                (
                    code,
                    meta["description"],
                    f"[Step 5 VCG design 2026-05-18] Anchor: {meta['anchor_ref']} (vc={meta['anchor_vc_id']}). Created by AI per researcher-approved plan; see batch files in Sessions/Session_Clusters/M04/files vcg design/.",
                ),
            )
            new_vcg_id_map[code] = cur.lastrowid
            counts["new_vcg_inserted"] += 1

        # 2. INSERT vcg_term links — one per (new VCG, term) pair
        # Member set spans ALL dispositions targeting a new VCG, regardless of kind
        # (AI may have used ASSIGN-EXISTING-VCG for a VCG it created earlier in the
        # same session — semantically the vc is a member either way).
        members_by_vcg = defaultdict(set)  # code → set of mti_term_id
        for d in disp:
            if d["target"] not in NEW_VCG_META:
                continue  # ASSIGN to a truly-existing VCG — no new vcg_term needed
            term_row = cur.execute("SELECT mti_term_id FROM verse_context WHERE id=?", (d["vc_id"],)).fetchone()
            if term_row:
                members_by_vcg[d["target"]].add(term_row[0])
        for code, term_ids in members_by_vcg.items():
            vcg_id = new_vcg_id_map[code]
            for term_id in term_ids:
                cur.execute(
                    """
                    INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date)
                    VALUES (?, ?, ?, 0, ?, ?)
                    """,
                    (vcg_id, term_id, f"[Step 5 VCG design 2026-05-18] Term placed in {code}", NOW_UTC, NOW_UTC),
                )
                counts["vcg_term_inserted"] += 1

        # 3. UPDATE verse_context.group_id for each disposition
        target_id_map = dict(existing_codes)  # start with existing
        target_id_map.update(new_vcg_id_map)  # add new

        for d in disp:
            tid = target_id_map[d["target"]]
            cur.execute(
                """
                UPDATE verse_context SET group_id=?,
                    notes = COALESCE(notes, '') || char(10) || ?
                WHERE id=? AND COALESCE(delete_flagged,0)=0
                """,
                (
                    tid,
                    f"[Step 5 VCG design 2026-05-18] {d['kind']} {d['target']}: {d['rationale'][:200]}",
                    d["vc_id"],
                ),
            )
            counts["vc_group_id_updated"] += cur.rowcount

        # 4. UPDATE verse_context.is_anchor=1 for each new VCG's anchor
        for code, meta in NEW_VCG_META.items():
            if code not in new_vcg_id_map:
                continue
            cur.execute(
                "UPDATE verse_context SET is_anchor=1 WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (meta["anchor_vc_id"],),
            )
            counts["anchor_set"] += cur.rowcount

        conn.commit()
        return counts, new_vcg_id_map
    except Exception:
        conn.rollback()
        raise


def write_report(disp, counts, errors, warnings, dry_run, new_vcg_id_map):
    # Per-target distribution
    target_counts = Counter(d["target"] for d in disp)
    new_codes = sorted(NEW_VCG_META.keys())

    L = []
    L.append("# M04 Step 5 — VCG design applied report")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    L.append(f"**Mode:** {'DRY RUN' if dry_run else 'LIVE'}")
    L.append(f"**Source:** 6 batch files in `{INPUT_DIR}`")
    L.append(f"**Total dispositions:** {len(disp)}")
    n_create = sum(1 for d in disp if d["kind"] == "CREATE-NEW-VCG")
    n_assign = sum(1 for d in disp if d["kind"] == "ASSIGN-EXISTING-VCG")
    L.append(f"  - CREATE-NEW-VCG: {n_create} (across {len(new_codes)} new VCGs)")
    L.append(f"  - ASSIGN-EXISTING-VCG: {n_assign}")
    L.append("")

    if errors:
        L.append("## Validation errors")
        L.append("")
        for e in errors:
            L.append(f"- {e}")
        L.append("")
    if warnings:
        L.append("## Warnings")
        L.append("")
        for w in warnings[:30]:
            L.append(f"- {w}")
        L.append("")

    L.append("## New VCGs created")
    L.append("")
    L.append("| Code | id | Members | Anchor | Description (excerpt) |")
    L.append("|---|---:|---:|---|---|")
    for code in new_codes:
        meta = NEW_VCG_META[code]
        members = target_counts.get(code, 0)
        vid = new_vcg_id_map.get(code, "—") if not dry_run else "—"
        desc = meta["description"][:90].replace("|", "\\|")
        L.append(f"| `{code}` | {vid} | {members} | {meta['anchor_ref']} (vc={meta['anchor_vc_id']}) | {desc} |")
    L.append("")

    L.append("## Disposition distribution by target")
    L.append("")
    L.append("| Target VCG | Type | Count |")
    L.append("|---|---|---:|")
    for tgt, n in target_counts.most_common():
        ttype = "NEW" if tgt in NEW_VCG_META else "existing"
        L.append(f"| `{tgt}` | {ttype} | {n} |")
    L.append("")

    if not dry_run:
        L.append("## Apply outcome")
        L.append("")
        for k, v in counts.items():
            L.append(f"- {k}: {v}")
        L.append("")

    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.write_text("\n".join(L), encoding="utf-8")
    print(f"Report written: {OUT_REPORT}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if not (args.dry_run or args.apply):
        ap.error("Must pass --dry-run or --apply")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    disp = parse_dispositions()
    print(f"Parsed {len(disp)} dispositions")

    errors, warnings, existing_codes, sg_map = validate(disp, conn)
    if errors:
        print(f"\n!! VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        if args.apply:
            print("\nApply blocked.")
            write_report(disp, {}, errors, warnings, dry_run=False, new_vcg_id_map={})
            return

    if warnings:
        print(f"\nWarnings: {len(warnings)}")
        for w in warnings[:10]:
            print(f"  - {w}")

    if args.dry_run:
        print("\nDRY RUN — no DB writes.")
        write_report(disp, {}, errors, warnings, dry_run=True, new_vcg_id_map={})
    else:
        counts, new_vcg_id_map = apply_directive(disp, existing_codes, conn)
        print(f"\nApplied: {dict(counts)}")
        # Post-apply: verses still lacking group_id
        n = conn.execute(
            """
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id=vc.mti_term_id
            WHERE mt.cluster_code='M04' AND vc.is_relevant=1
              AND COALESCE(vc.delete_flagged,0)=0 AND vc.group_id IS NULL
            """
        ).fetchone()[0]
        print(f"Post-apply: {n} M04 is_relevant verses still lacking group_id (should be 0).")
        write_report(disp, counts, errors, warnings, dry_run=False, new_vcg_id_map=new_vcg_id_map)

    conn.close()


if __name__ == "__main__":
    main()
