"""Re-classify M01 Phase 10 reconciliation v1 → v2 with cluster-centric dispositions.

Applies researcher's Option III decision (2026-05-16):
- 16 of 20 v1 CARRY-TO-SESSION-D items reclassified to ROUTE-TO-CLUSTER (named target cluster).
- 4 remain CARRY-TO-SESSION-D under strict criterion (programme-wide ≥3 clusters / methodological).
- 3 RESOLVED-BY-CATALOGUE unchanged.
- 1 SUPERSEDED unchanged.

Source: WA-M01-inherited-findings-reconciliation-v1-20260516.json (AI's output)
Output:
  - WA-M01-inherited-findings-reconciliation-v2-20260516.json
  - WA-M01-inherited-findings-reconciliation-v2-20260516.md
"""
from __future__ import annotations
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
M01 = REPO / "Sessions" / "Session_Clusters" / "M01"
V1_JSON = M01 / "WA-M01-inherited-findings-reconciliation-v1-20260516.json"
V2_JSON = M01 / "WA-M01-inherited-findings-reconciliation-v2-20260516.json"
V2_MD = M01 / "WA-M01-inherited-findings-reconciliation-v2-20260516.md"

# Re-classification map per proposal §5
#   key = (source_short, id), value = (new_disposition, target_cluster_or_session_d, rationale)
# source_short: "sbf" = wa_session_b_findings, "srf" = wa_session_research_flags
RECLASSIFICATION: dict[tuple[str, int], tuple[str, str, str]] = {
    # ROUTE-TO-CLUSTER — 16 items
    ("sbf", 71): ("ROUTE-TO-CLUSTER", "Anger cluster (future)",
        "Content is anger-governance vocabulary in source registry 4. No M01 fear terms. "
        "Belongs to Anger cluster's Session B / Phase 9 when that cluster is built."),
    ("sbf", 72): ("ROUTE-TO-CLUSTER", "Anger cluster (future)",
        "Compound anger-with-grief inner state in source registry 4. No M01 fear terms. "
        "Belongs to Anger cluster's analysis; bilateral grief overlap belongs to that cluster's T6.3."),
    ("sbf", 65): ("ROUTE-TO-CLUSTER", "Anxiety cluster (future)",
        "merimnaō dual register (affective worry vs volitional directed care) in source registry 7. "
        "No M01 fear terms. Belongs to Anxiety cluster's analysis."),
    ("sbf", 60): ("ROUTE-TO-CLUSTER", "Brokenness cluster (future)",
        "Dimensional uniformity of brokenness vocabulary in source registry 18. No M01 fear terms. "
        "Belongs to Brokenness cluster's analysis."),
    ("sbf", 31): ("ROUTE-TO-CLUSTER", "Distress cluster (future)",
        "riv prophetic-lawsuit group analytical question in source registry 51. No M01 fear terms. "
        "Belongs to Distress cluster's analysis."),
    ("sbf", 62): ("ROUTE-TO-CLUSTER", "Distress cluster (future)",
        "Vocabulary scope note for source registry 51. No M01 fear terms. "
        "Belongs to Distress cluster's analysis."),
    ("sbf", 47): ("ROUTE-TO-CLUSTER", "Wonder/Astonishment cluster (future)",
        "Wonder cluster Session B work for source registry 175. No M01 fear terms. "
        "Belongs to Wonder cluster's analysis."),
    ("sbf", 106): ("ROUTE-TO-CLUSTER", "Abomination cluster — T6 (future)",
        "Bilateral pattern: abomination ↔ new-covenant transformation. Per v2_1 §13.2.1 decision "
        "tree, bilateral cluster relationships are handled by the target cluster's T6 prompts (T6.3 "
        "causal/constitutive), not Session D. Belongs to Abomination cluster's analysis."),
    ("srf", 13): ("ROUTE-TO-CLUSTER", "Anger cluster — T6 (future)",
        "Bilateral pattern: anger governance ↔ spirit-level operation. Belongs to Anger cluster's "
        "T6.5 (distinctions) when that cluster is built. Not Session D under v2_1 strict criterion."),
    ("srf", 14): ("ROUTE-TO-CLUSTER", "Anger cluster — T6 (future)",
        "Bilateral pattern: anger ↔ abomination boundary (za.am verb/noun homonym split). Belongs "
        "to Anger cluster's T6.5 (distinctions). Not Session D under v2_1 strict criterion."),
    ("srf", 15): ("ROUTE-TO-CLUSTER", "Anger cluster — T7 (future)",
        "NT eschatological wrath theology (orgē Pauline + Revelation). Belongs to Anger cluster's "
        "T7.2/T7.3 (verse + science) and T6.3 (causal relationships with justice and atonement) "
        "when that cluster is built."),
    ("srf", 16): ("ROUTE-TO-CLUSTER", "Anger cluster (future)",
        "Data completeness note (G3709 orgē verse coverage thin). Belongs to Anger cluster's "
        "data-readiness work when that cluster is built. Operational, not Session D."),
    ("srf", 18): ("ROUTE-TO-CLUSTER", "Anger cluster — T6 (future)",
        "Bilateral pattern: paroxusmos dual valence (conflict ↔ catalysis in relational vocabulary). "
        "Belongs to Anger cluster's T6.3 (causal/constitutive relationships). Not Session D."),
    ("srf", 27): ("ROUTE-TO-CLUSTER", "Anxiety cluster (future)",
        "Data completeness note (G4329 prosdokia). Belongs to Anxiety cluster's data-readiness "
        "work. Operational, not Session D."),
    ("srf", 28): ("ROUTE-TO-CLUSTER", "Anxiety cluster (future)",
        "Data completeness note (G4328 prosdokaō). Belongs to Anxiety cluster's data-readiness "
        "work. Operational, not Session D."),
    ("srf", 142): ("ROUTE-TO-CLUSTER", "Abomination cluster — T6 (future)",
        "Bilateral vocabulary-sharing pattern: redemptive vocabulary inside moral-failure XREF "
        "context. Belongs to Abomination cluster's T6.4 (vocabulary/root sharing) when that cluster "
        "is built. Not Session D under v2_1 strict criterion."),

    # CARRY-TO-SESSION-D — 4 items (strict criterion: programme-wide ≥3 clusters or methodological)
    ("sbf", 59): ("CARRY-TO-SESSION-D", "Session D — divine pathos attribution pattern",
        "Programme-wide pattern: divine inner affective response attribution across multiple "
        "clusters (anguish, anger, compassion, grief, sorrow, mercy, jealousy, etc.). No single "
        "cluster's T6 captures the full attribution grammar. Truly cross-cluster under v2_1 strict "
        "criterion."),
    ("sbf", 61): ("CARRY-TO-SESSION-D", "Session D — spirit-soul boundary methodology",
        "Methodological observation: how spirit-level findings are framed across ALL clusters. "
        "Demonological-psychological interface affects every cluster with spirit-level content. "
        "No single cluster owns this; belongs to Session D programme-wide methodology."),
    ("srf", 122): ("CARRY-TO-SESSION-D", "Session D — commanded-inner-state pattern (≥3 clusters)",
        "Programme-wide pattern explicitly naming registries 11, 97, 42 'and likely others' — i.e. "
        "≥3 clusters. The pattern 'Scripture commanding specific inner orientations' is grammatical "
        "across clusters. Belongs to Session D under v2_1 strict criterion."),
    ("srf", 130): ("CARRY-TO-SESSION-D", "Session D — tripartite dimension pattern methodology",
        "Programme-wide methodological observation: does the orientation/affect/will-collapse "
        "tripartite pattern recur across negative-state clusters? Asks for cross-cluster testing. "
        "Belongs to Session D under v2_1 strict criterion."),
}


def main():
    data = json.loads(V1_JSON.read_text(encoding="utf-8"))
    reclassifications = data["reconciliations"]

    src_map = {"wa_session_b_findings": "sbf", "wa_session_research_flags": "srf"}

    # Apply re-classification
    new_summary: dict[str, int] = {
        "RESOLVED-BY-CATALOGUE": 0,
        "FOLD-INTO-PROMPT": 0,
        "NEW-CLUSTER-FINDING": 0,
        "SUPERSEDED": 0,
        "ROUTE-TO-CLUSTER": 0,
        "CARRY-TO-SESSION-D": 0,
        "RESEARCHER-DECISION": 0,
    }
    for r in reclassifications:
        src_short = src_map[r["source"]]
        key = (src_short, r["id"])
        if key in RECLASSIFICATION:
            new_disp, new_target, new_rat = RECLASSIFICATION[key]
            r["disposition_v1_was"] = r["disposition"]
            r["target_v1_was"] = r["target"]
            r["rationale_v1_was"] = r["rationale"]
            r["disposition"] = new_disp
            r["target"] = new_target
            r["rationale"] = new_rat
            r["reclassified_by"] = "CC under researcher Option III decision (2026-05-16)"
        new_summary[r["disposition"]] += 1

    out = {
        "cluster_code": "M01",
        "cluster_word": "fear",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "phase": 10,
        "version": "v2",
        "supersedes": "WA-M01-inherited-findings-reconciliation-v1-20260516.json",
        "governing_instruction": "wa-sessionb-cluster-instruction-v2_1-20260516 §13.2 (cluster-centric dispositions)",
        "reclassification_note": (
            "v1 (AI output) used the v2_0 disposition catalogue which conflated 'belongs to another "
            "cluster's Session B' with 'truly cross-cluster Session D'. v2 applies v2_1 strict "
            "criterion: bilateral cluster relationships → ROUTE-TO-CLUSTER (handled by target "
            "cluster's T6); only ≥3-cluster programme-wide or methodological observations → "
            "CARRY-TO-SESSION-D. Researcher direction: Option III (CC re-classifies; no AI "
            "round-trip)."
        ),
        "total_rows": len(reclassifications),
        "disposition_summary_v2": new_summary,
        "reconciliations": reclassifications,
    }
    V2_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote: {V2_JSON.relative_to(REPO)}")
    print()
    print("Disposition distribution (v2):")
    for k, v in new_summary.items():
        print(f"  {k}: {v}")

    # Generate v2 markdown
    md_lines: list[str] = []
    md_lines.append("# WA-M01-inherited-findings-reconciliation-v2-20260516")
    md_lines.append("")
    md_lines.append(f"**Cluster:** M01 — Fear, Dread and Terror  ")
    md_lines.append(f"**Phase:** 10 — Inherited-finding reconciliation  ")
    md_lines.append(f"**Version:** v2 (cluster-centric dispositions)  ")
    md_lines.append(f"**Supersedes:** [WA-M01-inherited-findings-reconciliation-v1-20260516.md](WA-M01-inherited-findings-reconciliation-v1-20260516.md)  ")
    md_lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_1-20260516 §13.2  ")
    md_lines.append(f"**Authored by:** Researcher direction (Option III) + CC re-classification of v1 (AI output)  ")
    md_lines.append(f"**Generated:** {out['generated_at']}  ")
    md_lines.append("")
    md_lines.append("## Re-classification context")
    md_lines.append("")
    md_lines.append("v1 (AI's Phase 10 output) used the v2_0 §13.2 disposition catalogue, which conflated two distinct routings under `CARRY-TO-SESSION-D`:")
    md_lines.append("")
    md_lines.append("- (a) findings belonging to **another cluster's Session B / Phase 9**, and")
    md_lines.append("- (b) findings concerning **truly cross-cluster phenomena** (≥3 clusters or methodological).")
    md_lines.append("")
    md_lines.append("v2 applies the v2_1 strict cluster-centric criterion: bilateral cluster relationships are handled by the target cluster's **T6** prompts within its own Phase 9. Session D scope is **few and specific** — only programme-wide ≥3-cluster patterns and methodological observations.")
    md_lines.append("")
    md_lines.append("**Outcome:** 16 of the original 20 `CARRY-TO-SESSION-D` items reclassified to `ROUTE-TO-CLUSTER` with named target cluster. 4 remain `CARRY-TO-SESSION-D` under strict criterion.")
    md_lines.append("")
    md_lines.append("## Disposition distribution (v2)")
    md_lines.append("")
    md_lines.append("| Disposition | Count |")
    md_lines.append("|---|---:|")
    for k, v in new_summary.items():
        md_lines.append(f"| `{k}` | {v} |")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Reclassifications per row")
    md_lines.append("")
    # Group by disposition
    by_disp: dict[str, list[dict]] = {k: [] for k in new_summary.keys()}
    for r in reclassifications:
        by_disp[r["disposition"]].append(r)

    for disp in ("RESOLVED-BY-CATALOGUE", "SUPERSEDED", "ROUTE-TO-CLUSTER", "CARRY-TO-SESSION-D"):
        items = by_disp[disp]
        if not items:
            continue
        md_lines.append(f"### {disp} ({len(items)})")
        md_lines.append("")
        for r in items:
            src_short = src_map[r["source"]]
            row_id = r["id"]
            reg_word = r.get("registry_word", "?")
            md_lines.append(f"#### {src_short}.id={row_id} — {reg_word}")
            md_lines.append("")
            md_lines.append(f"- **Disposition:** `{r['disposition']}`")
            md_lines.append(f"- **Target:** {r['target']}")
            md_lines.append(f"- **Rationale:** {r['rationale']}")
            if "disposition_v1_was" in r:
                md_lines.append(f"- _v1 was:_ `{r['disposition_v1_was']}` — _v1 target:_ {r['target_v1_was']}")
            md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_lines.append("*End of v2 reconciliation document.*")
    V2_MD.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote: {V2_MD.relative_to(REPO)}")


if __name__ == "__main__":
    main()
