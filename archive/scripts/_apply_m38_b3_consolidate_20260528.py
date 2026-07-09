"""Consolidate M38 B.3 outputs: merge M38-A repaired, fix small gaps in E/F/G,
produce final unified VCG creation JSON.

Surgical fixes (per diagnose output):
  - M38-E: missing vc_id 29608
  - M38-F: 2 undeclared duplicates (9050, 9047), 1 extra (51531 — belongs to A)
  - M38-G: 1 undeclared duplicate (13837), 1 missing (13831)

Small repair API call resolves these.
"""
from __future__ import annotations
import json, os, re, sqlite3, sys, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY=") and "ANTHROPIC_API_KEY" not in os.environ:
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            break

import anthropic

DB = "database/bible_research.db"
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
OUT_DIR = Path("Sessions/Session_Clusters/M38")
MAPPING_PATH = OUT_DIR / "WA-M38-subgroup-mapping-v2-20260528.json"
ORIGINAL_UNIFIED_PATH = OUT_DIR / "WA-M38-vcg-creation-v1-20260528.json"
M38A_REPAIRED_PATH = OUT_DIR / "WA-M38-M38-A-vcg-repaired-20260528.json"
FINAL_UNIFIED_PATH = OUT_DIR / f"WA-M38-vcg-creation-v2-{DATE}.json"

MODEL = "claude-sonnet-4-6"


def diagnose_subgroup(sg_data: dict, expected_verses: set[int]) -> dict:
    """Return missing/undeclared_dups/extras for a sub-group's VCG data."""
    vcgs = sg_data.get("vcgs", [])
    all_v = []
    for v in vcgs:
        for vc in v["verses"]:
            all_v.append(vc)
    c = Counter(all_v)
    distinct = set(c.keys())
    declared = {d["vc_id"] for d in sg_data.get("dual_memberships", [])}
    actual_dups = {vc for vc, n in c.items() if n > 1}
    return {
        "missing": expected_verses - distinct,
        "extras": distinct - expected_verses,
        "undeclared_dups": actual_dups - declared,
        "declared_dups": declared & actual_dups,
        "vcgs": vcgs,
    }


def main():
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    expected_by_sg = {sg["subgroup_code"]: set(sg["verses"]) for sg in mapping["subgroups"]}

    # Load original B.3 unified (has B,C,D,E,F,G from first run; A was failure)
    original = json.loads(ORIGINAL_UNIFIED_PATH.read_text(encoding="utf-8"))
    subgroups = dict(original.get("subgroups", {}))

    # Replace M38-A with the repaired version
    m38a_repaired = json.loads(M38A_REPAIRED_PATH.read_text(encoding="utf-8"))
    subgroups["M38-A"] = m38a_repaired

    # Diagnose each sub-group, identify fixes needed
    diagnoses = {}
    affected_vc_ids = []
    for code, sg_data in subgroups.items():
        expected = expected_by_sg.get(code, set())
        d = diagnose_subgroup(sg_data, expected)
        diagnoses[code] = d
        # Items needing API repair: missing + undeclared_dups
        for vc in d["missing"]:
            affected_vc_ids.append((code, vc, "missing"))
        for vc in d["undeclared_dups"]:
            affected_vc_ids.append((code, vc, "undeclared_dup"))

    print("Diagnosis summary:")
    for code in sorted(diagnoses.keys()):
        d = diagnoses[code]
        print(f"  {code}: missing={len(d['missing'])} extras={len(d['extras'])} "
              f"undecl_dups={len(d['undeclared_dups'])} decl_dups={len(d['declared_dups'])}")

    # Also: drop extras (vc_ids not in expected set for the sub-group)
    # First do this cheap surgery, then API repair for the rest

    for code, sg_data in subgroups.items():
        expected = expected_by_sg.get(code, set())
        new_vcgs = []
        for vcg in sg_data["vcgs"]:
            new_verses = [vc for vc in vcg["verses"] if vc in expected]
            new_vcg = dict(vcg)
            new_vcg["verses"] = new_verses
            # Ensure anchor is in verses
            if new_vcg.get("anchor_vc_id") not in new_verses and new_verses:
                new_vcg["anchor_vc_id"] = new_verses[0]
            new_vcgs.append(new_vcg)
        sg_data["vcgs"] = new_vcgs

    # Re-diagnose after extras removal
    for code, sg_data in subgroups.items():
        expected = expected_by_sg[code]
        diagnoses[code] = diagnose_subgroup(sg_data, expected)

    # Collect API repair targets
    repair_needed = []
    for code, d in diagnoses.items():
        for vc in d["missing"]:
            repair_needed.append((code, vc, "missing"))
        for vc in d["undeclared_dups"]:
            repair_needed.append((code, vc, "undeclared_dup"))

    print(f"\nRepair targets after dropping extras: {len(repair_needed)}")
    for code, vc, kind in repair_needed:
        print(f"  {code}: {kind} vc_id={vc}")

    if repair_needed:
        # Build small API call
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row
        vc_ids = list({vc for _, vc, _ in repair_needed})
        placeholders = ",".join("?" * len(vc_ids))
        verse_rows = {r["vc_id"]: dict(r) for r in conn.execute(f"""
            SELECT vc.id AS vc_id, vr.reference, vc.analysis_note, vc.keywords,
                   mt.strongs_number, mt.transliteration
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE vc.id IN ({placeholders})
        """, vc_ids)}

        # Build prompt with affected sub-groups' VCG descriptions
        affected_sgs = sorted({code for code, _, _ in repair_needed})
        user_parts = []
        for code in affected_sgs:
            user_parts.append(f"\n=== {code} VCG descriptions ===\n")
            for vcg in subgroups[code]["vcgs"]:
                user_parts.append(f"**{vcg['provisional_code']}** ({len(vcg['verses'])} current): {vcg['context_description']}\n")

        user_parts.append("\n=== Verses to assign ===\n")
        for code, vc, kind in repair_needed:
            r = verse_rows.get(vc)
            if not r:
                continue
            kw = json.loads(r["keywords"]) if r["keywords"] else []
            user_parts.append(f"vc_id={vc} (sub-group {code}, {kind}) {r['strongs_number']} {r['transliteration'] or ''} {r['reference']}")
            user_parts.append(f"  meaning: {r['analysis_note']}")
            user_parts.append(f"  kw: {kw}")

        user_parts.append(f"\nFor each vc_id above, return the single VCG within its sub-group to which it belongs.")

        sys_prompt = """You are Claude AI repairing Phase B.3 VCG coverage. For each presented vc_id (with its sub-group context), pick ONE existing VCG within that sub-group based on the verse's Pass A meaning. No new VCGs. No splits.

OUTPUT (strict JSON):

{
  "assignments": [
    {"vc_id": <int>, "vcg": "M38-X-VCG-NN"},
    ...
  ]
}

Every affected vc_id must appear once.
"""

        if "ANTHROPIC_API_KEY" not in os.environ:
            print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
            sys.exit(1)
        print(f"\nCalling {MODEL} for cross-subgroup repair...")
        client = anthropic.Anthropic()
        t0 = time.time()
        resp = client.messages.create(
            model=MODEL,
            max_tokens=4000,
            system=[{"type": "text", "text": sys_prompt}],
            messages=[{"role": "user", "content": "\n".join(user_parts)}],
        )
        text = resp.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("```", 2)[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.strip("`").strip()
        data = json.loads(text)
        dt = time.time() - t0
        print(f"[done {dt:.1f}s] in={resp.usage.input_tokens:,} out={resp.usage.output_tokens:,}")

        # Apply
        repair_lookup = {a["vc_id"]: a["vcg"] for a in data.get("assignments", [])}
        for code, vc, kind in repair_needed:
            target_vcg = repair_lookup.get(vc)
            if not target_vcg:
                print(f"  ⚠ no assignment returned for vc_id={vc}")
                continue
            if kind == "missing":
                # Add to target VCG
                for vcg in subgroups[code]["vcgs"]:
                    if vcg["provisional_code"] == target_vcg:
                        if vc not in vcg["verses"]:
                            vcg["verses"].append(vc)
                            vcg["verses"].sort()
                        break
            elif kind == "undeclared_dup":
                # Remove from all VCGs except target
                for vcg in subgroups[code]["vcgs"]:
                    if vcg["provisional_code"] != target_vcg and vc in vcg["verses"]:
                        vcg["verses"].remove(vc)
                # Ensure target has it
                for vcg in subgroups[code]["vcgs"]:
                    if vcg["provisional_code"] == target_vcg and vc not in vcg["verses"]:
                        vcg["verses"].append(vc)
                        vcg["verses"].sort()
                        break

    # Final sanity check + report
    final_distinct_total = 0
    issues = []
    for code, sg_data in subgroups.items():
        expected = expected_by_sg.get(code, set())
        d = diagnose_subgroup(sg_data, expected)
        final_distinct = len(set(vc for vcg in sg_data["vcgs"] for vc in vcg["verses"]))
        final_distinct_total += final_distinct
        if d["missing"] or d["extras"] or d["undeclared_dups"]:
            issues.append((code, d))

    # Write final unified JSON
    out = {
        "_meta": {
            "cluster_code": "M38",
            "date": DATE,
            "subgroups_processed": list(subgroups.keys()),
        },
        "subgroups": subgroups,
    }
    FINAL_UNIFIED_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== FINAL ===")
    print(f"Sub-groups: {len(subgroups)}")
    expected_total = sum(len(v) for v in expected_by_sg.values())
    print(f"Final distinct vc_ids across all sub-groups: {final_distinct_total} / expected {expected_total}")
    for code in sorted(subgroups.keys()):
        sg_data = subgroups[code]
        n_distinct = len(set(vc for vcg in sg_data["vcgs"] for vc in vcg["verses"]))
        n_expected = len(expected_by_sg[code])
        n_vcgs = len(sg_data["vcgs"])
        marker = "✓" if n_distinct == n_expected else "⚠"
        print(f"  {marker} {code}: {n_vcgs} VCGs, {n_distinct}/{n_expected} verses")
    if issues:
        print("\nRemaining issues:")
        for code, d in issues:
            print(f"  {code}: missing={sorted(d['missing'])} extras={sorted(d['extras'])} undecl_dups={sorted(d['undeclared_dups'])}")
    print(f"\nFinal unified JSON: {FINAL_UNIFIED_PATH}")


if __name__ == "__main__":
    main()
