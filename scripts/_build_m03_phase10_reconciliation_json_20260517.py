"""Build M03 Phase 10 reconciliation JSON from AI's markdown + DB facts.

Per researcher directive 2026-05-17: where the destination cluster is identifiable,
apply `ROUTE-TO-CLUSTER → <cluster_code>` for the inherited rows. AI's markdown used
SUPERSEDED labels with rationales that match ROUTE-TO-CLUSTER semantics — this script
applies the brief's directive (and the user's confirming directive) explicitly.

Destination mapping:
  R023 compassion (235 rows: 181 sbf + 54 srf) → M05 Love, Compassion and Kindness
    M05 owns 9 R023 terms; this is R023's analytical home.
  R108 meditation (2 rows: 1 sbf + 1 srf) → M17 Counsel, Planning and Purpose
    Meditation's natural cluster.
  R005 anguish BOUNDARY-M01-H7661 (1 srf row) → M01 Fear (originating cluster)
  R051 distress BOUNDARY-M02-H6696B/H7379 (2 srf rows) → M02 Anger (originating)

  R002 agony DIM-002-001..004 (4 sbf rows) → SUPERSEDED
    Dimension-review findings; cluster pivot superseded the dimension framework.
    The 3 specific term groups referenced (H2258A/B, H2259, H4865) are status='excluded'.
  R086 impurity DIM-086-001 (1 sbf row) → SUPERSEDED
    Dimension-review finding; cluster pivot superseded the dimension framework.

  R013 bitterness DIM-13-001 (1 sbf row) → FOLD-INTO-PROMPT (M03 T1.2/T1.3) [AI]
  R072 groaning DIM-072-001 (1 sbf row) → RESOLVED-BY-CATALOGUE (M03 T2.1/T4.6) [AI]

Output: Sessions/Session_Clusters/M03/WA-M03-inherited-findings-reconciliation-v1-20260517.json
"""
from __future__ import annotations
import json, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
OUT = REPO / "Sessions" / "Session_Clusters" / "M03" / "WA-M03-inherited-findings-reconciliation-v1-20260517.json"
CLUSTER = "M03"

# Per-row overrides where AI's decision is preserved (M03-internal dispositions)
# {(source, id): (disposition, target, rationale)}
AI_PRESERVED: dict[tuple[str, int], tuple[str, str, str]] = {
    ("wa_session_b_findings", 73): (
        "FOLD-INTO-PROMPT",
        "T1.2 (Kind) and T1.3 (Boundary) — [CLUSTER]",
        "DIM-13-001 raises whether biblical bitterness operates in two structural "
        "registers (affective quality vs dispositional-character). M03's Phase 9 "
        "Part 1 T1.2.1 and T1.3.2 identify M03-G as affective-quality bitterness; "
        "the dispositional-character register transferred to M02 (pikria, pikros) "
        "at Phase 3. Fold note: M03-G corpus (Gen 26:35, Job 9:18, Pro 14:10, Pro "
        "17:25, Lam 3:15, Col 3:19, Rev 10:9-10) consistently evidences (a) "
        "affective quality arising from grief/suffering/divine dealings; "
        "register (b) belongs to M02. Two registers are independent, not sequential."
    ),
    ("wa_session_b_findings", 63): (
        "RESOLVED-BY-CATALOGUE",
        "T2.1.2 [E-VCG-02] + T4.6.1 [E-VCG-02] — M03",
        "DIM-072-001 (G4726 stenagmos — the Spirit's inarticulate groaning in Rom 8) "
        "is fully addressed by M03 Phase 9 T2.1.2 (spirit-level location, Rom 8:26 "
        "anchor) and T4.6.1 (Spirit interceding within believer's spirit). "
        "The Spiritual/God-ward dimension classification for stenagmos in M03-E-VCG-02 is confirmed."
    ),
}

# Researcher-decision rows (no clean single-cluster destination) — keep RESEARCHER-DECISION
# Currently empty — all other rows have an identified destination per user directive
RESEARCHER_DECISION: dict[tuple[str, int], str] = {}

# DIM findings that the cluster pivot superseded (R002, R086 — registry-internal dimension questions)
# Their analytical content is no longer queryable under the cluster model.
SUPERSEDED_DIM: dict[tuple[str, int], str] = {
    ("wa_session_b_findings", 56): "R002 DIM-002-001 — registry-internal dimension question about R002's agōn-/basanizō- sub-families. The cluster pivot replaced the dimension framework; R002 terms are now distributed across M03/M10/M17/M23/M24/M27/M34/M35/M44 by characteristic, dissolving the original dimension structure. Finding is structurally obsolete under v2_2.",
    ("wa_session_b_findings", 57): "R002 DIM-002-002 — concerns H2258A/B (pledge) groups now status='excluded'. Finding addresses a dimension classification for terms removed from analysis. Superseded.",
    ("wa_session_b_findings", 58): "R002 DIM-002-003 — concerns H2259 (cho.vel pilot) now status='excluded'. Finding addresses a dimension classification for a term removed from analysis. Superseded.",
    ("wa_session_b_findings", 64): "R002 DIM-002-004 — concerns H4865 (mish.be.tsot filigree) now status='excluded'. Finding addresses a dimension classification for a term removed from analysis. Superseded.",
    ("wa_session_b_findings", 108): "R086 DIM-086-001 — registry-internal dimension question about akathartos unclean spirit. The cluster pivot replaced the dimension framework; akathartos is in M03-BOUNDARY (basanizō corpus) and R086 terms are distributed across M03/M07/M10/M12/M18/T2 by characteristic. The occupation/liberation model is a cross-cluster topic now better addressed by Session D or T6 bilateral findings. Dimension-framing superseded.",
}

# Registry → destination cluster routing rules
# (registry_no, originating_cluster_for_BOUNDARY_flag) → destination cluster
REGISTRY_ROUTING: dict[int, dict] = {
    23: {"cluster": "M05", "label": "M05 Love, Compassion and Kindness",
         "note": "R023 compassion's analytical home — M05 owns 9 R023 OWNER terms."},
    108: {"cluster": "M17", "label": "M17 Counsel, Planning and Purpose",
          "note": "R108 meditation's natural cluster — Counsel/Planning/Purpose."},
}

# srf BOUNDARY rows route back to their originating cluster
BOUNDARY_ROUTING: dict[int, dict] = {
    678: {"cluster": "M01", "label": "M01 Fear, Dread and Terror — Phase 12 BOUNDARY closure",
          "note": "M01-BOUNDARY-H7661 sha.vats pending researcher decision; route back to M01 for closure follow-up."},
    686: {"cluster": "M02", "label": "M02 Anger, Wrath and Indignation — Phase 12 BOUNDARY closure",
          "note": "M02-BOUNDARY-H6696B tsur pending researcher decision; route back to M02 for closure follow-up."},
    687: {"cluster": "M02", "label": "M02 Anger, Wrath and Indignation — Phase 12 BOUNDARY closure",
          "note": "M02-BOUNDARY-H7379 riv pending researcher decision; route back to M02 for closure follow-up."},
}


def fetch_inherited(conn) -> tuple[list[dict], list[dict]]:
    sbf = list(conn.execute("""
        SELECT wsbf.id, wsbf.finding_id, wsbf.finding_type, wr.no AS registry_no, wr.word AS registry_word
        FROM wa_session_b_findings wsbf
        JOIN word_registry wr ON wr.id = wsbf.registry_id
        WHERE wr.no IN (
            SELECT DISTINCT wr2.no FROM word_registry wr2
            JOIN mti_terms mt ON mt.owning_registry_fk = wr2.id
            WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
        ) AND wsbf.status IN ('open','pending','confirmed')
        ORDER BY wsbf.id
    """, (CLUSTER,)))
    srf = list(conn.execute("""
        SELECT wsrf.id, wsrf.flag_code, wsrf.strongs_reference, wr.no AS registry_no,
               wr.word AS registry_word, SUBSTR(wsrf.description, 1, 200) AS description_head
        FROM wa_session_research_flags wsrf
        JOIN word_registry wr ON wr.id = wsrf.registry_id
        WHERE wr.no IN (
            SELECT DISTINCT wr2.no FROM word_registry wr2
            JOIN mti_terms mt ON mt.owning_registry_fk = wr2.id
            WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
        ) AND COALESCE(wsrf.resolved,0)=0
        ORDER BY wsrf.id
    """, (CLUSTER,)))
    return [dict(r) for r in sbf], [dict(r) for r in srf]


def disposition_for(source: str, row: dict) -> tuple[str, str, str]:
    """Return (disposition, target, rationale) for the given row."""
    key = (source, row["id"])

    # 1. AI-preserved analytical dispositions (M03-internal)
    if key in AI_PRESERVED:
        return AI_PRESERVED[key]

    # 2. Researcher-decision overrides (currently empty)
    if key in RESEARCHER_DECISION:
        return ("RESEARCHER-DECISION", "Researcher", RESEARCHER_DECISION[key])

    # 3. Superseded DIM rows (R002, R086)
    if key in SUPERSEDED_DIM:
        return ("SUPERSEDED", "(no replacement — dimension framework retired)", SUPERSEDED_DIM[key])

    # 4. BOUNDARY srf rows → originating cluster
    if source == "wa_session_research_flags" and row["id"] in BOUNDARY_ROUTING:
        rule = BOUNDARY_ROUTING[row["id"]]
        return ("ROUTE-TO-CLUSTER", rule["label"], rule["note"])

    # 5. Registry-based routing (R023 → M05; R108 → M17)
    reg = row["registry_no"]
    if reg in REGISTRY_ROUTING:
        rule = REGISTRY_ROUTING[reg]
        if source == "wa_session_b_findings":
            kind = row["finding_type"]
            rationale = (
                f"R{reg:03d} {row['registry_word']} finding ({kind}, {row['finding_id']}) "
                f"belongs to {rule['cluster']}'s analytical scope. {rule['note']}"
            )
        else:
            rationale = (
                f"R{reg:03d} {row['registry_word']} flag "
                f"({row['flag_code']}{', '+row['strongs_reference'] if row.get('strongs_reference') else ''}) "
                f"belongs to {rule['cluster']}'s analytical scope. {rule['note']}"
            )
        return ("ROUTE-TO-CLUSTER", rule["label"], rationale)

    # Fallback — should not happen if all routing rules are complete
    return ("RESEARCHER-DECISION", "Researcher",
            f"Routing rule missing for source={source} reg={row['registry_no']} id={row['id']}")


def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    sbf_rows, srf_rows = fetch_inherited(conn)
    conn.close()

    print(f"DB inherited counts: sbf={len(sbf_rows)} srf={len(srf_rows)} total={len(sbf_rows)+len(srf_rows)}")

    reconciliations: list[dict] = []

    for r in sbf_rows:
        disposition, target, rationale = disposition_for("wa_session_b_findings", r)
        reconciliations.append({
            "source": "wa_session_b_findings",
            "id": r["id"],
            "finding_id": r["finding_id"],
            "registry_no": r["registry_no"],
            "registry_word": r["registry_word"],
            "finding_type": r["finding_type"],
            "disposition": disposition,
            "target": target,
            "rationale": rationale,
        })

    for r in srf_rows:
        disposition, target, rationale = disposition_for("wa_session_research_flags", r)
        reconciliations.append({
            "source": "wa_session_research_flags",
            "id": r["id"],
            "flag_code": r["flag_code"],
            "strongs_reference": r["strongs_reference"],
            "registry_no": r["registry_no"],
            "registry_word": r["registry_word"],
            "disposition": disposition,
            "target": target,
            "rationale": rationale,
        })

    summary = Counter(r["disposition"] for r in reconciliations)
    print("\nDisposition summary:")
    for k, v in sorted(summary.items()):
        print(f"  {k:<24}: {v}")
    print(f"  {'TOTAL':<24}: {len(reconciliations)}")

    # Per-target counts for ROUTE-TO-CLUSTER
    route_targets = Counter(r["target"] for r in reconciliations if r["disposition"] == "ROUTE-TO-CLUSTER")
    print("\nROUTE-TO-CLUSTER targets:")
    for k, v in sorted(route_targets.items()):
        print(f"  {k}: {v}")

    doc = {
        "cluster_code": CLUSTER,
        "phase": 10,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "governing_instruction": "wa-sessionb-cluster-instruction-v2_2-20260516 §13",
        "catalogue_version": "v2_1",
        "source_markdown": "WA-M03-inherited-findings-reconciliation-v1-20260517.md",
        "cc_adjustment_note": (
            "JSON built by CC from AI's markdown + DB facts. Per researcher directive "
            "2026-05-17 (\"move all items to identified destination cluster\"), R023 "
            "compassion rows route to M05 (its analytical home — 9 R023 OWNER terms in M05); "
            "R108 meditation rows route to M17; M01/M02 BOUNDARY-pending flags route back "
            "to originating closure. R002/R086 DIM-review findings marked SUPERSEDED "
            "(cluster pivot replaced dimension framework). AI's specific M03-internal "
            "dispositions for R013 bitterness (FOLD-INTO-PROMPT) and R072 groaning "
            "(RESOLVED-BY-CATALOGUE) preserved verbatim. AI's SUPERSEDED/CARRY-TO-SD "
            "labels for R023 rows replaced with explicit ROUTE-TO-CLUSTER → M05 per directive."
        ),
        "total_rows": len(reconciliations),
        "dispositions_summary": dict(summary),
        "route_to_cluster_targets": dict(route_targets),
        "reconciliations": reconciliations,
    }

    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote: {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
