# wa-cluster-M10-dir-003-phase7-vcg-create-v1-20260523

> Cluster directive — M10 Phase 7 (VCG creation)
> Cluster: M10 — Sin, Guilt and Transgression (post-split, post-Phase-5-revision)
> Date: 2026-05-23
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

---

## MOTIVATION

Phase 7 designed **69 VCGs across 23 sub-groups**, routing all 1,325 is_relevant verses to a VCG of their own. Source: AI session output in `Sessions/Session_Clusters/M10/files phase 7/` — 23 per-sub-group VCG design docs + the unified VCG creation JSON.

Pre-apply validation against the DB returned 0 issues after two CC anchor patches (see below). All 1,325 verses appear exactly once in the JSON, all 69 anchors are in their VCG's members, all sub-group counts match DB.

### Two CC patches applied to the AI's JSON before apply

| VCG | Original anchor | Issue | Replaced with |
|---|---|---|---|
| M10-F-VCG-05 (Adam-paradigm transgression) | 40855 Rom 5:14 (parabasis) | Routed to M10-F-VCG-04, not in this VCG's members | 40871 Rom 5:15 (paraptōma — first Adam verse in members) |
| M10-L-VCG-01 (Individual confession) | 18936 2Sa 12:13 (cha.ta) | Routed to M10-J (wilful sinning) per Phase 5 revision | 18937 2Sa 24:10 (David's confession over the census — in members) |

Both fixes preserve the intended characteristic; `_cc_notes` arrays added inline to record the change.

### VCG count distribution

| Sub-group | Verses | # VCGs | VCG codes |
|---|---:|---:|---|
| M10-BND | 5 | 1 | M10-BND-VCG-01 (PHASE_8_5_FLAG, all BOUNDARY verses) |
| M10-S | 5 | 1 | M10-S-VCG-01 |
| M10-X | 8 | 1 | M10-X-VCG-01 |
| M10-M | 8 | 1 | M10-M-VCG-01 |
| M10-Q | 9 | 1 | M10-Q-VCG-01 |
| M10-U | 9 | 1 | M10-U-VCG-01 |
| M10-O | 14 | 1 | M10-O-VCG-01 |
| M10-K | 18 | 2 | M10-K-VCG-01..02 |
| M10-N | 18 | 1 | M10-N-VCG-01 |
| M10-P | 19 | 1 | M10-P-VCG-01 |
| M10-R | 22 | 3 | M10-R-VCG-01..03 |
| M10-L | 34 | 3 | M10-L-VCG-01..03 |
| M10-W | 34 | 3 | M10-W-VCG-01..03 |
| M10-C | 64 | 3 | M10-C-VCG-01..03 |
| M10-H | 64 | 5 | M10-H-VCG-01..05 |
| M10-I | 72 | 3 | M10-I-VCG-01..03 |
| M10-D | 97 | 5 | M10-D-VCG-01..05 |
| M10-J | 98 | 5 | M10-J-VCG-01..05 |
| M10-G | 101 | 3 | M10-G-VCG-01..03 |
| M10-T | 112 | 3 | M10-T-VCG-01..03 |
| M10-F | 147 | 9 | M10-F-VCG-01..09 |
| M10-E | 162 | 8 | M10-E-VCG-01..08 |
| M10-V | 205 | 5 | M10-V-VCG-01..05 |
| **Total** | **1,325** | **69** | |

Largest individual VCG: M10-V-VCG-05 at 113 verses (8.5% of cluster). Phase 8.7 / characteristic mapping or downstream review may re-split if needed.

## SCOPE

### Operation A — INSERT 69 verse_context_group rows

```sql
INSERT INTO verse_context_group (group_code, context_description, vertical_pass_flag)
VALUES (?, ?, 0);
```

`group_code` from the AI's provisional VCG codes (`M10-{X}-VCG-{seq}`).
`context_description` from the AI's per-VCG description.

### Operation B — INSERT vcg_term rows

For each (vcg_id, mti_term_id) pair where the VCG covers any of the term's verses. Deduplicated; placement_note = `Phase 7 routing`.

### Operation C — UPDATE verse_context.group_id

For all 1,325 active is_relevant vc rows in M10, set `group_id` to the new VCG id.

### Operation D — Set anchors

(1) Clear any prior `is_anchor=1` on M10 verses (carried from pre-cluster Session B work — 107 prior anchors recorded). (2) Set `is_anchor=1` on the 69 new anchor vc_ids.

## OUTCOME REQUIRED

- 69 `verse_context_group` rows for M10.
- Some N `vcg_term` rows (one per (vcg, term) pair across the 69 VCGs).
- 1,325 vc rows with `group_id` set to new VCG.
- 69 vc rows with `is_anchor=1`; all prior M10 anchors cleared.

## COMPLETION CONFIRMATION

```sql
SELECT COUNT(*) FROM verse_context_group
WHERE group_code LIKE 'M10-%-VCG-%' AND COALESCE(delete_flagged,0)=0;
-- Should return 69

SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id=vc.mti_term_id
JOIN verse_context_group vcg ON vcg.id=vc.group_id
WHERE mt.cluster_code='M10' AND vc.is_relevant=1
  AND COALESCE(vc.delete_flagged,0)=0
  AND vcg.group_code LIKE 'M10-%-VCG-%';
-- Should return 1325

SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id=vc.mti_term_id
WHERE mt.cluster_code='M10' AND vc.is_anchor=1
  AND COALESCE(vc.delete_flagged,0)=0;
-- Should return 69
```

## SCRIPT

`scripts/_apply_m10_phase7_vcg_create_20260523.py` — runs Ops A/B/C/D in a single transaction with pre/post checks.

---

*M10 Phase 7 directive. Ready for Phase 8 (dissolve inherited VCGs — but M10's vcg structure was built fresh, so most of Phase 8 may be a no-op; Phase 8.5 BOUNDARY resolution for the 5 verses in M10-BND-VCG-01 remains).*
