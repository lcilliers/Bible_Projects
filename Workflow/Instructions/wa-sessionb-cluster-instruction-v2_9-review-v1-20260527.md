# Review of v2_9 against your 5 core objectives

**Date:** 2026-05-27
**Document under review:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_9-20260526.md` (1,813 lines)
**Researcher direction:** *"I suspect that over time it has become bloated with unnecessary steps and repetition of steps that have the same effect. Stick to the principles and core objectives of this process."*

**The 5 objectives (as researcher stated 2026-05-27):**

a) Read every verse
b) Derive the context and meaning of every verse
c) Group meaning derived from the verse context together into packets that can be digested collectively
d) Subject every verse (within its group context) to analytics using the 8 tiers and key questions as the anchor
e) Capture every finding and analytic result in the database for later retrieval

**Plus the two governing principles (researcher stated 2026-05-27):**

1. The verse meaning and context is the data and rules all analytics.
2. All observations, however uncomfortable or disjointed, must be recorded in the database.

---

## §1. v2_9 phase inventory — what's actually there

| §ref | Phase | Owner | Lines | Frequency | Maps to objective |
|---|---|---|---:|---|---|
| §4 | Phase 1 — UT verse review | CC | 90 | NEW clusters only (often 0 UT for inherited) | (a) read |
| §5 | Phase 2 — Pass A meanings + keywords | CC (API) | 63 | Every cluster | (a) + (b) read + meaning |
| §6 | Phase 3 — Constitution debate | AI (chat) | 96 | Every cluster | meta — cluster-membership debate |
| §7 | Phase 4 — Apply transfers + BOUNDARY | CC | 61 | Often **SKIPPED** (§7.5: skip when 0 transfers + 0 BOUNDARY) | (c) initial grouping move |
| §8 | Phase 5 — Sub-group formation | AI (chat) | 93 | Every cluster | (c) grouping level 1 |
| §9 | Phase 6 — Verse routing to sub-group | CC | 69 | Every cluster | (c) apply level 1 |
| §10 | Phase 7 — VCG design within sub-groups | AI (chat) | 110 | Every cluster | (c) grouping level 2 |
| §11 | Phase 8 — Silent VCG dissolution | CC | 65 | **NO-OP** for fresh clusters (0 inherited VCGs) | legacy cleanup |
| §11A | Phase 8.5 — BOUNDARY resolution | AI+CC | 66 | Often **NO-OP** (0 BOUNDARY common) | (c) cleanup |
| §11B | Phase 8.7 — Characteristic mapping | AI+CC | 79 | Reduced to confirmation (v2_8 §8.0) | (c) characteristic layer |
| §12 | Phase 9 — Catalogue prompts | AI (chat) | 152 | Every cluster | **(d) analytics** |
| §13 | Phase 10 — Inherited-finding reconciliation | AI+CC | 92 | **NO-OP** for post-split / fresh clusters | legacy fold |
| §14 | Phase 11 — Validation + fold | CC | 84 | Every cluster | (e) capture validation |
| §15 | Phase 12 — Closure | CC | 52 | Every cluster | (e) final status |

**Total phase content:** ~1,272 lines across 14 phase sections.

**Map to the 5 objectives:**

- (a) read → Phase 1 + Phase 2
- (b) meaning → Phase 2
- (c) grouping into packets → Phase 3, 4, 5, 6, 7, 8, 8.5, 8.7 — **8 sub-phases for one objective**
- (d) analytics → Phase 9
- (e) capture → Phase 10, 11, 12

Eight sub-phases for "group meaning into packets" is the bloat signature. The remaining objectives are 1–2 phases each.

---

## §2. Bloat findings

### §2.1 Three grouping levels for one analytical purpose

v2_9 builds three nested grouping layers:

1. **Sub-group** (Phase 5/6) — designed AI-side from meanings, applied CC-side
2. **VCG** (Phase 7) — designed AI-side as sub-divisions of sub-groups, applied CC-side
3. **Characteristic** (Phase 8.7) — mapped from sub-groups (1:1 default; 1:N for §8.6 volume-splits)

**Observed analytical use:**

- **Phase 9 fires at characteristic scope.** Each AI batch is one characteristic; verses are pulled by `cluster_subgroup → characteristic_subgroup → characteristic`. The VCG layer is loaded into the structural input *as navigation labels*, but Phase 9 prompts do not require VCG-scoped reasoning.
- **Sub-group is the analytical container** in Phase 9 because characteristics map to one or more sub-groups, and verses live in sub-groups.
- **VCG-as-third-layer adds no Phase 9 reasoning.** VCG descriptions are author-time aids for the AI to remember why the sub-group was internally textured, but the finding scope is characteristic, not VCG.

**Diagnosis:** Phase 7 builds an analytical structure that Phase 9 does not consume at the granularity Phase 7 produced. The VCG layer is sub-group decoration, not analytical substrate.

**Possible move:** drop the VCG layer. Sub-group descriptions can absorb the VCG-level texture as "this sub-group covers X, Y, and Z aspects of [characteristic]." The cluster keeps two layers (cluster → sub-group → characteristic), not three.

**Cost saving:** Phase 7 (110 lines) goes; VCG-design AI session goes (~30-60 min AI work per cluster); `verse_context_group` + `vcg_term` table use becomes legacy-read-only.

**Risk:** Some clusters' sub-groups have 50+ verses with internally distinct sub-corpora (M10c-A had 93V across 8 VCGs covering corpse-contact / discharge / object-contamination / volitional-defilement / etc.). Without VCGs, the AI authoring Phase 9 findings on M10c-A sees 93 verses with one description; analytical resolution may suffer. Counter-argument: Phase 9's job is to find characteristic-level patterns across those verses anyway, and the verse-level texture is in the Pass A meanings.

**Recommendation surface:** worth deciding consciously. The VCG layer is the largest single source of pipeline overhead and the weakest evidence of paying analytical rent.

### §2.2 Phase 3 carries heavy machinery for a usually-trivial outcome

Phase 3 (96 lines + §6.3.1 disallowed grounds + §6.3.2 verse-level relationship test) asks the AI to debate every term in the cluster for STAYS / TRANSFERS / BOUNDARY verdict.

**Observed outcomes across recent clusters:**

- M07 v1→v2: 8 of 10 TRANSFERS reversed to STAYS-with-flag → produced §6.3.2
- M10c: 8/8 STAYS, 0 transfers, 0 BOUNDARY
- M10b: STAYS dominant
- M11: 15/15 STAYS, 0 transfers, 0 BOUNDARY (1 marginal flagged)

**Pattern:** the original 2026-05-04 clustering placed terms correctly enough that Phase 3 produces ~100% STAYS verdicts. The debate machinery is heavy for a confirmation step.

**Possible move:** Phase 3 becomes a CC-mechanical "membership sanity check" — for each term, compare its meaning corpus's keyword profile to the cluster's keyword centroid. Any term whose profile is >2σ from the centroid is surfaced for AI/researcher review. Most terms pass mechanically with no AI work. AI is invoked only on flagged outliers.

**Cost saving:** Phase 3 AI session (significant per-cluster work) replaced by a CC analytics script. AI work invoked only on the 0-3 flagged terms per cluster.

**Risk:** loses the systematic per-term review. But the systematic review keeps producing the same answer (STAYS), so its analytical yield has been low. The mechanical check would catch the actually-misplaced terms.

**This honours principle 1 directly** — the verse meaning / keyword evidence drives the membership question; not an AI debate.

### §2.3 Phase 4 — frequently a no-op

§7.5: Phase 4 is SKIPPED when Phase 3 produces 0 transfers + 0 BOUNDARY. Across recent clusters this is the norm.

When Phase 4 fires, it executes structural moves that could equally be ops within a combined Phase 3/4 directive — there is no analytical reason for Phase 3 (AI debate) and Phase 4 (CC apply) to be separate phases.

**Possible move:** merge Phase 3 + Phase 4 into "Phase 3 — Constitution + transfers." When Phase 3 surfaces transfers, the same phase produces the directive. When it doesn't, the phase terminates.

### §2.4 Phase 5 + Phase 6 — design and apply as separate phases

Phase 5 = AI designs sub-groups (93 lines spec). Phase 6 = CC applies the design (69 lines spec, plus the mechanical routing script). This is one analytical step split across two phase numbers for owner-distinction (AI vs CC).

**Possible move:** merge into "Phase B — Sub-group design + apply." The AI design produces a JSON mapping; CC applies it; the whole step is one phase with two operations (AI synthesis → CC mechanical).

Same applies to Phase 7 (design) — if VCG layer is kept, it's a design + apply pair.

### §2.5 Phase 8 / 8.5 / 8.7 — three sub-phases, mostly no-ops or confirmations

- **Phase 8** (Silent VCG dissolution, 65 lines) — fresh clusters: 0 inherited VCGs; NO-OP. The 65 lines spec a directive that fires for the occasional cluster with inherited VCGs.
- **Phase 8.5** (BOUNDARY resolution, 66 lines) — fires only when Phase 3 produced BOUNDARY verdicts; usually 0.
- **Phase 8.7** (Characteristic mapping, 79 lines) — under v2_8 §8.0 reduced to "confirmation step" because Phase 5 already designed sub-groups to represent characteristics. The actual DB-write work is a small load script.

Three full phase sections (210 lines combined) for what is, on most clusters, three small CC scripts or no-ops.

**Possible move:** roll all three into a "Phase C — Structural cleanup" that fires the relevant ops only when they apply (silent dissolution if inherited VCGs exist; BOUNDARY disposition if BOUNDARY verdicts exist; characteristic load if not auto-derived from sub-groups).

### §2.6 Phase 10 / 11 / 12 — closure trio

- **Phase 10** (Inherited-finding reconciliation, 92 lines) — NO-OP for post-split / fresh clusters; the inherited-finding fold operation is a back-compat read of pre-v2_6 session-B data.
- **Phase 11** (Validation, 84 lines) — mechanical 11-check script.
- **Phase 12** (Closure, 52 lines) — single status flip.

**Possible move:** "Phase E — Closure" combines validation + status flip. Phase 10 becomes a conditional op (fires only when inherited findings exist; otherwise skipped silently).

### §2.7 §2's eight sub-rules — overlap among the three contamination guards

§2.2 (cross-cluster contamination), §2.3 (inherited-structure contamination), §2.8 (no-spiritualisation contamination) are three guards against three biases. Each has its own rules and §refs. They could consolidate into one numbered "Contamination guards" section listing the three biases.

§2.5 (directive packaging) and §2.6 (status transition discipline) overlap with §20 (Patches and directives — content checklist).

§2.7 (atomic per-row vs synthesis pattern) is partly redundant with the phase-by-phase owner column (CC vs AI).

**Possible move:** Operating-principle §2 consolidates from 8 sub-rules to 4:
- §2.1 Write-on-discovery
- §2.2 Three contamination guards (cross-cluster / inherited-structure / no-spiritualisation)
- §2.3 Fluency is not a quality signal
- §2.4 Atomic-decision vs synthesis split

Directive-packaging and status-discipline content moves to §20.

### §2.8 The two new principles (2026-05-27) need a home

Principle 1 (verse meaning rules all analytics) and Principle 2 (all observations recorded, however disjointed) are programme-level governance rules. They should land in §1 (Document scope) or in a new §2 head as the foundation the eight (or four) sub-rules elaborate.

---

## §3. Repeated-read findings

A verse currently gets read through:

| Phase | What's read | By whom |
|---|---|---|
| Phase 1 (UT only) | Verse text + context for new verses | AI classifier |
| Phase 2 (Pass A) | Verse text + context | AI writes meaning + keywords |
| Phase 3 | Term's meaning corpus (re-read of Pass A meanings) | AI debates STAYS/TRANSFERS |
| Phase 5 | Cluster-wide meaning corpus (re-read of Pass A meanings) | AI clusters into sub-groups |
| Phase 7 | Sub-group meaning corpus (re-read again) | AI clusters into VCGs |
| Phase 8.7 | Sub-group + VCG structure | AI maps to characteristics |
| Phase 9 | All verses in characteristic batch | AI authors 189 tier prompts |
| Phase 9 synthesis | Cluster_finding rows (not verses directly) | AI synthesises across characteristics |

**The same meaning corpus is read 3-4 times** across Phases 3, 5, 7, 8.7 — each time to make a structural decision (membership, sub-group, VCG, characteristic). The decisions are sequential refinements; each read could in principle produce the next decision in one chain rather than three separate reads.

**Possible move:** ONE structural-design read that produces ALL grouping decisions at once.

Sketch: AI reads the cluster's meaning corpus once and produces a JSON specifying:
- For each term: membership verdict (STAYS / TRANSFERS / BOUNDARY)
- For each is_relevant verse: which "packet" it belongs to (the digestible group)
- For each packet: its characteristic statement, its constituent verses, optional internal texturing notes

That's one AI read producing the equivalent of Phase 3 + 5 + 7 + 8.7's structural decisions. CC then applies via one composite directive.

**Cost saving:** 3 AI sessions → 1 AI session per cluster. ~3x reduction in AI time.

**Risk:** larger context per session. M10c had 263 verses × ~50 words/meaning = ~13K words just for meanings; plus instruction prompt; plus catalogue. Manageable. M01 has 1300 verses → ~65K words. Pushing context limits. For large clusters the read may need pagination, but it's still 1 logical session.

---

## §4. Repetition findings (textual)

A focused grep would surface specific text-level repetition, but the structural repetition above accounts for most of the bloat. A few likely candidates:

- "Inherited VCG / sub-group / anchor information is not visible to AI" — appears in §2.3, §5 (Phase 2), §6 (Phase 3), §8 (Phase 5), §10 (Phase 7). Five places.
- The 5-rule "inner-being is the entire human interior" block (§1.1, §4.2, §6.3.1, §8.4.1, etc.).
- The §6.3.2 verse-level relationship test is restated in part across §6, §7, §16, §17, §18.
- BOUNDARY discipline appears in §6.3.1, §8.4.1, §11A, §16, §18 — overlapping content.

These can collapse into single canonical references with cross-pointers from the phase sections.

---

## §5. Proposed slim structure (sketch — for your mark-up)

A 5-phase pipeline that maps 1:1 to your 5 objectives.

### Phase A — Verse read + meaning (combines old Phases 1 + 2)

**Objective (a) + (b):** read every verse and derive its inner-being meaning.

**Operations:**

1. **UT classification** — for NEW verses without `verse_context` rows: AI classifier returns relevant / set_aside / borderline.
2. **Pass A meaning + keywords** — for every `is_relevant=1` verse: AI writes meaning + keywords against the verse's text + context, no cluster lens applied beyond naming the anchor term.

Both ops use CC's API-driven JSON-template pattern. One phase, one (or two batched) API runs.

**Principle 2 enforcement:** Pass A meaning prompts ask "what does this verse say about the human inner being in this verse's context" — not "what does this verse say about [cluster characteristic]." Multi-faceted content is recorded in the meaning. If the verse evidences cross-register content, it's named in the meaning.

### Phase B — Meaning grouping (combines old Phases 3 + 4 + 5 + 6 + 7)

**Objective (c):** group meanings into packets that can be digested collectively.

**Operations:**

1. **Membership sanity check (CC mechanical)** — for each term, keyword-profile distance from cluster centroid. Outliers surfaced for review.
2. **Packet design (AI, chat, one session)** — AI reads the cluster's full meaning corpus and produces a JSON specifying:
   - For each term: STAYS / TRANSFERS / BOUNDARY (only flagged terms need debate)
   - For each is_relevant verse: assigned packet
   - For each packet: characteristic statement (one paragraph), constituent verses, internal-texturing notes
3. **Packet apply (CC)** — single directive: TRANSFERS executed; packets inserted into `cluster_subgroup` (renamed or kept); verses routed; characteristics auto-derived from packets.

**One AI session per cluster** instead of three (constitution + sub-group + VCG). The VCG layer is dropped; packets replace sub-groups as the single grouping level.

**Principle 2 enforcement:** during packet design, AI is required to record disjointed observations — verses that don't cleanly fit any packet, terms whose verses split across packets, cross-register signals. These land in `cluster_observation` as part of the same directive.

### Phase C — Cleanup (combines old 8 + 8.5 + 8.7)

**Objective:** structural housekeeping when applicable.

Conditional ops:
- Silent dissolution of inherited VCGs (when present)
- BOUNDARY verse disposition (when Phase B produced BOUNDARY terms)
- Characteristic load (if not auto-derived from packets in Phase B)

Many clusters will be no-op. Phase C is one section spec'ing the three conditional ops, not three sections.

### Phase D — Analytics (old Phase 9)

**Objective (d):** subject verses to 8-tier × key-question analytics.

Per-characteristic batches × 8 tiers + cluster synthesis batch, as v2_9. Largely unchanged — Phase 9 is doing the right thing for objective (d).

**Principle 2 enforcement:** every tier's findings include any cross-register observations or disjointed signals; loader writes them to `cluster_observation` automatically when the AI marks them as `[OBSERVATION]` (new marker alongside `[CHAR-N]` and `[CLUSTER]`).

### Phase E — Closure (combines old 10 + 11 + 12)

**Objective (e):** capture, validate, close.

1. Inherited-finding fold (conditional)
2. Validation (11-check script as v2_9)
3. Status flip

---

## §6. Sizing comparison (rough)

| | v2_9 | Slim v3 sketch |
|---|---:|---:|
| Phase sections | 14 | 5 |
| Lines of phase spec | ~1,272 | ~500-600 (estimated) |
| AI sessions per cluster | 4-6 (Pass A x N batches, Phase 3, Phase 5, Phase 7, Phase 9 x N, synthesis) | 3 (Pass A x N batches, Phase B once, Phase D x N + synthesis) |
| Reads of cluster meaning corpus | 3-4 (Phase 3, 5, 7, sometimes 8.7) | 1 (Phase B) |
| Grouping levels (analytical) | 3 (sub-group, VCG, characteristic) | 1 (packet, identified to characteristic) |
| §2 sub-rules | 8 | 4 |
| Contamination guards | 3 (separate sections) | 1 (combined) |

---

## §7. Risks of slimming

1. **Less ceremony, less safety.** Each separate phase produces a directive that CC can validate before the next phase fires. Combining Phase 3 + 5 + 7 into Phase B means one large directive carrying multiple structural moves — bugs in one operation may roll back others (the failure-radius isolation argument §2.5).
   - **Mitigation:** Phase B applies ops in declared order with savepoints between major op groups; rollback to the last savepoint on op-group failure.

2. **Larger AI context per session.** Phase B reads the entire cluster's meanings + designs packets + writes characteristic statements in one session. For large clusters (M01 1300V, M10 was 1325V before split) this may push limits.
   - **Mitigation:** chunked Phase B with explicit cross-chunk reconciliation, or pre-clustering by keyword analytics to reduce within-session scope.

3. **Loss of VCG navigation.** Closed clusters' VCGs (M01-M10c, M15, M20, M26, M39, M46) become legacy structures with no current-pipeline analogue. Session C / Session D currently reference VCG codes.
   - **Mitigation:** VCG table preserved (read-only legacy); existing references continue to work; new clusters don't create VCGs.

4. **Methodology re-version cost.** v2_9 → v3_0 is a major rewrite. Re-version churn during active cluster work has been a research-time cost across the year.
   - **Mitigation:** v3_0 written and committed once; subsequent work uses v3_0 stably.

5. **Loss of the Phase 3 reflection point.** Phase 3's term-by-term debate is one of the few places the AI is forced to articulate the cluster's characteristic before any structural moves happen. Skipping it (or making it mechanical) loses that articulation.
   - **Mitigation:** Phase B requires AI to write a one-paragraph cluster characteristic statement as its first output. Same articulation, different placement.

---

## §8. Questions to surface for your decision

1. **Drop the VCG layer?** This is the largest structural simplification. The argument is that Phase 9 fires at characteristic scope; VCGs are decoration. The counter-argument is texture within a large sub-group is analytically real.
2. **Collapse Phase 3 + 5 + 7 into one AI design session (Phase B)?** Three reads → one read; trade-off is larger context per session vs. fewer cycles.
3. **Make Phase 3 mechanical** (keyword-profile sanity check vs. AI debate)?
4. **Keep all the safety phases (8 / 8.5 / 10) as conditional ops or as separate phase numbers?** Cosmetic but affects spec length.
5. **Codify the two governing principles** in §1 / §2 as numbered rules?
6. **What goes into v3_0 first?** Slim structure published first as a draft against M11 (un-park into the new pipeline) or against M12 (clean test)?

---

## §9. What this review is NOT

- Not a v3_0 draft. The slim structure is a sketch for direction-setting; the actual instruction would be written after the structure is approved.
- Not a recommendation on which slim option to take. The trade-offs are real; this is research methodology and the researcher's call.
- Not a claim that v2_9 is broken. v2_9 has delivered 13 closed clusters of high-quality analysis. The bloat is the cost of incremental iteration; a periodic rewrite to slim down is normal hygiene, not a fix for failure.

---

## §10. Suggested next steps (for your mark-up)

1. **Mark up this document** with your reactions to each finding and option.
2. **Decide on the VCG question first** (it's the largest single design decision).
3. **Decide whether to publish v3_0 before un-parking M11 or use M11 as the first v3_0 test cluster.**
4. CC drafts v3_0 from the slim structure once direction is set.
5. v3_0 published, v2_9 archived.
6. M11 (and subsequent clusters) run under v3_0.

---

*Review v1 — awaiting researcher mark-up.*
