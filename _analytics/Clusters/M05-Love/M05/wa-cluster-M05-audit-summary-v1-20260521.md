# M05 Audit Summary — Researcher Brief

**Date:** 2026-05-21
**Trigger:** Researcher observation — *"I thought that M05 had terms added to it, but it is not showing in the cluster overview."*
**Auditor:** CC, using `scripts/_audit_cluster_against_instruction_v25_v1_20260518.py`
**Full report:** [WA-M05-audit-against-v25-v1-20260521.md](WA-M05-audit-against-v25-v1-20260521.md)

---

## §1 — Verdict on the researcher's question

**Researcher's intuition is correct.** Two terms were transferred INTO M05 from M07 on 2026-05-19 (post-closure), but the `cluster.status` was never updated to `'Analysis Completed (Terms Added)'`. The overview script's status detection therefore doesn't flag M05 as Terms-Added — and the v2_5 STATUS-SUFFIX audit check reports clean (because the suffix isn't on the string).

| Field | Value |
|---|---|
| `cluster.status` (current) | `'Analysis Completed'` |
| `cluster.status` (should be, given post-closure changes) | `'Analysis Completed (Terms Added)'` |
| `cluster.last_updated_date` | `2026-05-08T02:36:46Z` (closure date — never updated when terms arrived) |

### The 2 transferred terms (M07 → M05, applied 2026-05-19)

| mti_id | Strong's | Translit | Verses (is_relevant) | Sub-group | VCG |
|---:|---|---|---:|---|---|
| 338 | H2616B | cha.sad | 3 | **(none)** | `338-001` (inherited registry VCG) |
| 1633 | H2617B | che.sed | 162 | **(none)** | `1633-001/002/003` (inherited registry VCGs) |

These are the "chesed root family" — moved out of M07 (Shame) at Phase 4 of M07's processing on the analytical reasoning that the *che.sed* meaning corpus evidences steadfast-love / loyal-faithfulness, not shame. The transfer changed `mti_terms.cluster_code` but didn't route the verses through M05's Phase 6 sub-group structure — they're orphaned in M05 (no `mti_term_subgroup` link, no M05-style VCG).

**Why this happened:** The M07 Phase 4 apply script (`_apply_m07_phase4_term_transfer_20260519.py`) was M07-centric: it advanced M07's status to `'Analysis - In Progress'` and updated `mti_terms.cluster_code`, but had no logic to update the destination cluster's status or route the incoming terms through M05's existing sub-group structure.

---

## §2 — Bigger picture: M05 has substantial pre-existing issues

The audit surfaces issues much larger than the Terms-Added fix. M05 was closed early in the programme (2026-05-08) under v2_0 methodology — before Pass A discipline, before the v2_5 evidence-grounding checks, before the v2_8 sub-group=characteristic discipline.

| Audit check | Count | Threshold | Severity | What it means |
|---|---:|---:|---|---|
| `AUDIT-V25-STATUS-SUFFIX` | 0 | 1 | clean | Misleading clean: status string lacks the suffix, but terms WERE added |
| `AUDIT-V25-PIPELINE-INCOMPLETE` | **1625** | 1 | **blocking** | 1,427 verses without Pass A meaning + 165 without sub-group + 33 without VCG |
| `AUDIT-V25-EVIDENCE-GROUNDING` | **1175** | 5 | **blocking** | 705 placeholder findings + 470 ungrounded findings |
| `AUDIT-V25-COMPLETENESS` | **661** | 5 | **blocking** | Catalogue cells missing finding rows |
| `AUDIT-V25-TERSE-SETASIDE` | 7 | 20 | advisory | Set-aside reasons lacking §4.5.1 evidence ground |
| Boundary / forbidden-setaside / parking checks | 0 | — | clean | — |

**Plan verdict:** `SYSTEMIC` — one action affects >50% of cluster scope.

| # | Error type | Count | % of denominator |
|---|---|---:|---|
| 1 | `missing_pass_a_meaning` | **1,427** | 90% of relevant verses |
| 2 | `terse_setaside` | 7 | 3% of set-aside verses |
| 3 | `missing_subgroup` | **165** | 10% of relevant verses (the cha.sad + che.sed transfer + a few legacy gaps) |
| 4 | `missing_vcg` | 33 | 2% of relevant verses |
| 5 | `placeholder_finding` | **705** | 46% of cluster_finding rows |
| 6 | `completeness_gap` | **661** | catalogue cells missing |
| 7 | `ungrounded_finding` | **470** | 31% of cluster_finding rows |

The 165 `missing_subgroup` items are dominated by the cha.sad + che.sed transfer (~165 verses). The other 6 actions are pre-existing M05 issues from its early-closure state.

---

## §3 — Why the cluster overview didn't flag this

The current overview generator detects "Terms Added" by reading `cluster.status` and looking for the suffix. M05's status doesn't carry the suffix because nothing ever wrote it. Two improvements possible:

1. **Source-of-truth fix:** Update M05's `cluster.status` to `'Analysis Completed (Terms Added)'`. Then the overview marker ✓+ appears, and the v2_5 STATUS-SUFFIX audit check fires correctly (flagging M05 as needing follow-on processing).
2. **Detection robustness:** Extend the overview generator to detect post-closure activity directly (e.g., `mti_terms.last_changed > cluster.last_updated_date` → indicates terms added/changed after closure regardless of the status string). This catches future cases where the status string isn't updated.

CC's recommendation: **do both**. The status string is the human-readable signal; the detection logic is the safety net.

---

## §4 — Recommended path forward

Three options, in increasing scope:

### Option A — Minimal status fix (~10 minutes)

- Update `cluster.M05.status` to `'Analysis Completed (Terms Added)'` with a `last_updated_date` reflecting the 2026-05-19 transfer date
- Add a `cluster_observation` row recording the cha.sad + che.sed transfer event for audit trail
- Regenerate the cluster overview (M05 then shows ✓+)
- Re-run the audit — now AUDIT-V25-STATUS-SUFFIX fires (1 hit), blocking, surfacing M05 in any "ready for X" gates
- **Does NOT fix the orphaned 165 verses** — they remain unrouted; the bigger M05 issues remain
- Cost: minimal; outcome: honest status reporting, surfaces M05 for follow-on work

### Option B — Surgical Terms-Added fix (~2-4 hours)

- Do Option A's status fix +
- Route the 2 transferred terms (cha.sad + che.sed) through M05's existing sub-group structure
  - Determine which M05 sub-group(s) the cha.sad/che.sed corpus fits (likely M05-A "covenant love" or whichever sub-group carries the loyal-faithfulness register)
  - Insert `mti_term_subgroup` rows for both terms
  - UPDATE `verse_context.cluster_subgroup_id` for all 165 verses
  - Phase 9 micro-pass on the new finding cells (≈40-60 new cluster_finding rows if running 8 sub-groups × 8 tiers)
- Reset `cluster.M05.status` to `'Analysis Completed'` once routing is complete
- **Does NOT fix the bigger M05 issues** (1,427 missing Pass A, ungrounded findings, etc.)

### Option C — Full M05 retrofit (multi-session)

- Treat M05 as needing the same kind of work M04 / M07 / M08 went through under v2_5 + v2_8
- Restart from Phase 2 (Pass A meanings on all 1,593 relevant verses)
- Re-derive sub-groups under v2_8 §8.0 (characteristic-driven)
- Re-do Phase 9 findings under v2_5 discipline (tier-by-tier, evidence-grounded, no placeholders)
- This is the path M04 is already on (paused at end of Phase 9 pending v2_5 pivot per memory note [project_m04_paused_at_phase9])

---

## §5 — CC's recommendation

**Apply Option A immediately** — it's a small intervention that fixes the honesty of the status reporting and surfaces M05 in future audits.

**Defer Option B / C** to a dedicated M05 retrofit session. Option C is the proper fix but is a multi-session undertaking comparable to M04's retrofit. Schedule it after the current M08 closure is complete; M01, M03, M06, M39, M46 will likely need similar retrofits and could be planned as a batch.

Hold the cha.sad + che.sed routing (Option B) as part of the Option C retrofit rather than as a separate small intervention — better to do it in the broader cluster context once Pass A meanings are authored.

---

*End of audit summary. Awaiting researcher direction on Option A / B / C.*
