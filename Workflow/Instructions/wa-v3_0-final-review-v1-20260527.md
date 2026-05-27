# v3_0 — Final pre-writing review

**Date:** 2026-05-27
**Status:** Consolidated review of all design decisions and infrastructure built today. Pre-writing of the actual v3_0 instruction document.

---

## §1. Where we are

A full day of investigation and infrastructure work has produced:

- A complete diagnosis of why v2_9 needs simplification (parent review + supplement + citation corrections)
- A set of governing principles articulated by the researcher
- Schema and table infrastructure built and tested
- Three published clusters' artefacts backfilled
- Two scripts (assemble, ingest) demonstrating the new publication model

**No instruction document has been written yet.** The actual v3_0 spec is the next move.

---

## §2. What's been decided

### §2.1 Governing principles (codified into v3_0)

1. **The verse meaning and context is the data and rules all analytics.** Cluster structure, characteristic labels, sub-groups, VCGs defer to what the verse actually says.
2. **All observations, however uncomfortable or disjointed, must be recorded in the database.** Bias-screening is forbidden.

Memory entry: [feedback_two_governing_principles](../../C:/Users/lerouxc/.claude/projects/g--My-Drive-Bible-study-projects/memory/feedback_two_governing_principles.md).

### §2.2 Pipeline structure — 14 phases → 5

| v3_0 phase | Combines old | Owner | Output |
|---|---|---|---|
| **A. Read + meaning** | Phase 1 + Phase 2 | CC API | UT classification + Pass A meaning + keywords |
| **B. Meaning grouping** | Phase 3 + 4 + 5 + 6 + 7 | AI design + CC apply | One AI session producing membership verdicts, sub-groups, VCGs, mappings — single corpus read |
| **C. Structural cleanup** | Phase 8 + 8.5 + 8.7 | CC | Silent legacy VCG soft-delete, BOUNDARY resolution (conditional), characteristic load |
| **D. Analytics + publication prose** | Phase 9 (extended) | AI | 189 findings + 8 tier-prose blocks per characteristic; cluster synthesis includes opening/divine-pattern/appendix prose |
| **E. Validation + closure** | Phase 10 + 11 + 12 | CC | Inherited fold (conditional) + 11-check validation + status flip |

Session C becomes a CC assembly task (0-1 AI sessions) instead of ~10 AI sessions.

### §2.3 VCGs stay — case settled by data

The "drop VCGs" question went through three corrections:
- 13% citation (regex full-code only) — wrong
- 63% citation (regex + short forms) — incomplete
- **86% citation (structured `finding_citation` table)** — authoritative

VCGs are analytically active in 16 of 16 closed clusters. v3_0 keeps the VCG layer. The "size-conditional Phase 7" option (build VCGs only for sub-groups >40V) remains available as a Phase B design choice but is not mandated.

### §2.4 prose_section is the publication canonical store

M54 migration applied: `prose_section` extended with `cluster_code`, `characteristic_id`, `cluster_subgroup_id`. FTS5 rebuilt. 18 new section types registered (sc_v2_ch1..7, sc_v2_tier_T0..T7, sc_v2_synth_*).

4 published clusters backfilled (M01, M03, M09, M15) — 43 prose_section rows with supersession chains.

### §2.5 Citation extraction is post-Phase-D automatic step

`finding_citation` table now populated for 16 closed clusters (75,080 rows). The two-stage extractor (verse refs → derive VCG citations) is format-agnostic and produces the structural finding↔verse↔VCG traceability.

Under v3_0, the extractor runs automatically after each Phase D batch completes.

### §2.6 cluster_observation lifecycle enforced at phase exits

Same-phase observations: must advance to `confirmed`/`refined` before phase exits.
Forward-targeted observations (target_phase = session_c / session_d / future phase): SHALL remain `open` with populated `resolution_note`.

Phase E closure verifies no observations remain `open` with targets at completed phases.

### §2.7 What was bloat in v2_9 (removed in v3_0)

| v2_9 bloat | v3_0 fix |
|---|---|
| 3 grouping levels (sub-group + VCG + characteristic) | Same 3 levels, but designed in ONE AI session (Phase B), not three |
| 8 §2 sub-rules with 3 contamination guards | 4 consolidated rules (write-on-discovery, contamination guard, fluency-not-signal, atomic-vs-synthesis split) + 2 new governing principles |
| Repeated text ("inherited structure not visible" in 5 sections) | Single canonical statement, cross-referenced |
| Phase 4 / 8 / 8.5 / 10 frequently no-ops as full phase sections | Conditional ops within consolidated phases |
| Cluster meaning corpus read 3-4 times | Read once (in Phase B) |
| 4-6 AI sessions per cluster Phase 9 | 5 AI sessions (4 chars + 1 synthesis) but with embedded tier prose — no Session C re-read |
| Session C ~10 AI sessions | 0-1 AI sessions (CC assembly + optional polish) |

---

## §3. What still needs deciding

### §3.1 Phase 3 — mechanical or AI debate?

v2_9 has 96 lines spec'ing the term-by-term constitution debate. M07/M10c/M11 all produced ~100% STAYS outcomes. The debate is heavy machinery for a confirmation result.

**Options:**
- **A. Keep as AI debate within Phase B** (status quo machinery, integrated)
- **B. Make it CC-mechanical sanity check + AI invoked only on flagged outliers** (faster, but loses the systematic per-term articulation)

My recommendation: **A**, because the debate's per-term verdict file becomes the SUBGROUP_DESIGN_RATIONALE / VERDICT_RATIONALE observation seeds for Session C. The articulation IS the carry-forward content. Mechanical sanity check loses this.

### §3.2 Pre-v2_6 closed cluster backfill

10 clusters (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46) closed before characteristic mapping became standard. Their `characteristic` table is empty; their findings are sub-group-scoped.

**Options:**
- **A. Leave as legacy** — v3_0 governs new work; pre-v2_6 closures stay as they are. Session C consumes their findings under the old sub-group-scope model.
- **B. Backfill characteristic mapping** for these 10 — adds ~5 AI sessions per cluster.

My recommendation: **A**. These clusters are already published or pending publication; their analytical record is complete. Don't pay to retrofit.

### §3.3 v3_0 first test cluster

Once v3_0 instruction is written, we need a test cluster to validate the design end-to-end.

**Options:**
- **M11 un-park** — the cluster has Phase 1+2 done. Resume from Phase B under v3_0. Validates Phase B–E end-to-end. Risk: M11's "characteristic-legs scattered" diagnosis means the design tests under stress.
- **M12 (Purity)** — Not started; clean slate. Validates Phase A–E end-to-end. Lower stress but slower (need to do Phase A from scratch).

My recommendation: **M11 first** (validates the harder phases B-E; the M11 diagnosis itself is a useful pressure test of v3_0). If M11 surfaces problems, M12 is then a clean follow-up.

### §3.4 v3_0 instruction publication path

**Options:**
- **A. Write v3_0 as a full replacement for v2_9** — single document, archive v2_9.
- **B. Write v3_0 incrementally — partial replacement that references v2_9 for unchanged sections.**

My recommendation: **A**. The bloat reduction is the whole point. A clean full document is the deliverable. v2_9 archived per the existing pattern.

### §3.5 Phase D tier-prose-during-Phase-9 — required or optional?

The optimisation depends on the AI batch authoring tier prose alongside the 189 findings. If the AI session runs short on budget or attention, it could skip the prose.

**Options:**
- **A. Required** — Phase D batch is not considered complete without tier prose. Loader validates and fails the batch if prose is missing.
- **B. Recommended but not gating** — tier prose preferred; if missing, Session C handles via legacy chapter authoring as a fallback.

My recommendation: **A** for v3_0 first-cluster, with **B** as fallback after we see how the M11 test goes. If quality is good and the cost is fine, lock to A for the rest.

---

## §4. v3_0 instruction structure (what I'll write)

Based on decisions above, the v3_0 instruction will contain:

```
§0  Change note (v2_9 → v3_0)
§1  Document scope
§2  Governing principles (the two researcher-stated rules; numbered, codified)
§3  Operating disciplines (4 sub-rules — write-on-discovery, contamination guard,
                            fluency-not-signal, atomic-vs-synthesis split)
§4  Session open
§5  Phase A — Read + meaning (UT review + Pass A in one section)
§6  Phase B — Meaning grouping (constitution debate + sub-group design + VCG design
                                 + apply, in ONE AI session)
§7  Phase C — Structural cleanup (silent VCG dissolution + BOUNDARY resolution
                                   + characteristic load, conditional)
§8  Phase D — Analytics + publication prose (per-char + synthesis batches with
                                              embedded tier prose)
§9  Phase E — Validation + closure
§10 Publication pipeline (Session C reduced to CC assembly via prose_section)
§11 Catch-up routine (for pre-v3_0 closures wanting publication)
§12 Revised publishing routine
§13 BOUNDARY discipline (canonical reference, unchanged from v2_9 §16)
§14 Disposition vocabulary (canonical reference, unchanged from v2_9 §18)
§15 Pre/post controls table (5 phases not 14)
§16 Reports — input/output map
§17 Patches and directives — content checklist
§18 Post-closure audit + fix (unchanged from v2_9 §17)
§19 Status discipline
§20 Why v3_0 — the changes from v2_9
§21 Change history
```

Estimated length: ~1,000-1,200 lines (vs v2_9's 1,813). Two-thirds the size.

---

## §5. Path forward

**Recommended sequence:**

1. **You approve / amend the decisions in §3** (5 minutes).
2. **I write v3_0 instruction** (~1-2 hours my work; the meatiest deliverable left).
3. **You review v3_0 instruction** (your time).
4. **Test v3_0 by un-parking M11** under it — runs Phase B → E → Session C through the new pipeline. (Multiple sessions, real cluster work.)
5. **Iterate v3_0 → v3_1 if M11 surfaces design problems**, otherwise lock and proceed to M12 / M13 / M14.

The infrastructure built today is the **support layer**. The instruction is the **specification**. Both need to exist for v3_0 to actually operate.

---

## §6. The five §3 decisions, summarised for your reply

| # | Question | My recommendation |
|---|---|---|
| §3.1 | Phase 3 mechanical or AI debate? | **AI debate within Phase B** (keeps per-term articulation for carry-forward) |
| §3.2 | Backfill characteristic mapping for pre-v2_6 closed clusters? | **No — leave as legacy** |
| §3.3 | v3_0 first test cluster? | **M11 un-park** (pressure-tests the design) |
| §3.4 | v3_0 publication path? | **Full replacement of v2_9** (clean rewrite) |
| §3.5 | Tier-prose during Phase D — required or optional? | **Required for first test; reconsider after M11 result** |

If you agree with all 5, say "go" and I write v3_0. If any are wrong, mark the changes.

---

*v3_0 final review v1 — 2026-05-27. Awaiting researcher direction.*
