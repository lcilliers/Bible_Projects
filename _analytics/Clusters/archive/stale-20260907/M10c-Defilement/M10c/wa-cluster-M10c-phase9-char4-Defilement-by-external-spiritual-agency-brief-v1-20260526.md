# M10c Phase 9 — Characteristic 4 (Defilement by external spiritual agency) — brief

**Cluster:** M10c — Defilement and Impurity
**Characteristic:** 4 — Defilement by external spiritual agency
**Verses in scope:** ~21 across 1 sub-group(s)
**Task date:** 2026-05-26
**Audience:** Claude AI session

**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char4-Defilement-by-external-spiritual-agency-brief-v1-20260526.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char4-Defilement-by-external-spiritual-agency-input-v1-20260526.md` | Characteristic definition + sub-groups + VCGs + verses + 189 prompts + carry-forward observations |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_9-20260526.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Science extract** — `Workflow/Sciences/wa-m10-guilt-scienceextract-v1_0-20260513.md` (Section 4 only) | Programme-curated scientific lens for T7.3. **Note:** the doc was authored pre-split and covers M10/M10b/M10c siblings; for M10c only Section 4 (Defilement, impurity, contamination) is in scope. Sections 1 (Guilt) and 2 (Transgression) belong to M10; Section 3 (Evil/Wickedness) belongs to M10b. |
| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input (§4). No separate catalogue file required.

---

## Context

M10c has 4 inner-being characteristics. You are processing **Characteristic 4 (Defilement by external spiritual agency)**. Per researcher direction 2026-05-18 (carried forward to M10c under v2_9 §8.0):

> *"sub groups is purely a capacity organiser, the evaluating unit is the characteristic or group of sub groups."*

All your findings author at **characteristic scope** — NOT at sub-group scope. Sub-groups organise the evidence for navigation; they don't carry the analytical unit.

Cluster-scope synthesis (across all 4 characteristics) happens in a separate session at the end. **Don't author cluster-scope findings here.**

---

## Characteristic 4 — Defilement by external spiritual agency: definition

> The inner-being condition of defilement produced by an unclean spirit inhabiting, controlling, and corrupting a person from without. The mechanism is external — an unclean spiritual force enters and dominates the person's inner and bodily life. The result is a defilement-state in the person: will overridden, faculties suppressed (speech/hearing, Mar 9:25), bodily agency lost (Luk 8:29), communal access severed. The spirits recognise superior divine authority (Mar 3:11) and resist expulsion (Act 8:7); restoration is treated as wholeness (Luk 6:18). Structurally distinct from the bodily-mechanism (chars 1) and moral self-defilement (char 2) in that the defiling agent is an external spiritual being. Structural opposite: M12 (purity/wholeness — the restored state after expulsion).

---

## Your task

For each of the **189 catalogue prompts** (8 tiers, T0–T7), author a finding at characteristic scope for Characteristic 4 (Defilement by external spiritual agency). Use the verse evidence in the structural input.

Output format per prompt (one block per prompt; parser-safe form per v2_9 §12.4):

```
**T#.#.# — question text excerpt (optional)**

**[CHAR-4]** E — Finding text. Cite specific verses / VCGs / sub-groups from the evidence in §3 of the structural input. Quote the specific verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.

---
```

Outcome codes:

- **E** — evidenced; cite specific verses / VCGs
- **S** — silent; describe the analytical significance of the absence
- **G** — gap; describe what data would be needed to answer

Scope marker is `**[CHAR-4]**` (CC's loader maps this to characteristic_id=56 for this characteristic).

---

## ⚠️ TIER-BY-TIER STAGED EXECUTION — MANDATORY ⚠️

**Known prior failure mode (M04 / M07, and the first M07 / M08 attempts):** AI held all 189 prompts in working memory and produced them as a continuous pass. It drifted — carried prior-tier reasoning into later tiers, skipped prompts "to come back later", performed inter-tier analysis, and produced fluency-without-citation. **Do not repeat that pattern.**

This task is **8 segments**, one per tier. Each segment must be **authored, written to disk, self-evaluated, and only then proceed to the next tier**. **One tier per response.**

### Hard procedural sequence (per tier)

For each of T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7, in order, you MUST:

1. **OPEN TIER** — announce: *"Starting Tier T{N} — {tier title}."*
2. **READ EVIDENCE FRESH** — re-read §3 of the structural input (the verse-meanings). Do not rely on memorised summaries from prior tiers; re-read for the current tier's lens.
3. **AUTHOR THIS TIER'S PROMPTS** — every prompt in the tier gets one finding block (parser-safe form above). Tier sizes: **T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20.** No skipping. No "summarise the rest".
4. **WRITE TO DISK** — emit the tier's complete section as a single contiguous markdown block (with the `## T{N} — {title}` header and all prompt blocks below it). On the first tier this CREATES the findings file; on subsequent tiers it APPENDS to it. Show the file path in the output so the reader can append manually if needed.
5. **SELF-EVALUATE the tier** — run the self-evaluation gate (see below) before announcing the tier complete.
6. **CONFIRM + PROCEED (or ALERT)** —
   - If self-evaluation passes: announce *"Tier T{N} written: {file_path}, {n}/{n} prompts, [CHAR-4] markers verified, self-evaluation PASS. Proceeding to Tier T{N+1}."* — then immediately begin Tier T{N+1} in the SAME response (re-read §3 fresh; start from step 1).
   - If self-evaluation fails or surfaces a researcher-review item: announce *"Tier T{N} written but self-evaluation surfaced: {issue}. ALERT — pausing for researcher review."* — then STOP. Do not begin the next tier; wait for the next prompt.

**Between tiers, your working memory must reset.** Do not carry T{N}'s reasoning or finding patterns into T{N+1}'s prompts. The next tier starts fresh from the verse evidence, with the next tier's analytical lens.

### Self-evaluation gate (run after every tier)

Quickly check these items. If all pass, proceed to the next tier in the same response. If any fail, ALERT and stop.

| # | Check | PASS criterion | If FAIL |
|---|---|---|---|
| 1 | **Prompt count** | Every prompt in the tier has a finding block (T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20) | ALERT — name the missing prompts |
| 2 | **Scope marker** | Every `[CHAR-N]` marker in this tier is `[CHAR-4]` | ALERT — name the wrong-marker prompts |
| 3 | **Citation discipline** | Every E finding cites at least one verse-reference or VCG code (e.g. `Lev 11:24`, `M10c-A-VCG-07`) | ALERT — name the uncited E prompts; do NOT proceed |
| 4 | **No cross-tier mixing** | This tier's findings do not reference findings from a later tier (e.g. "see T7" before T7 is authored) | ALERT — name the cross-tier references |
| 5 | **Distinct evidence per prompt** | No two prompts share an identical 80-character opening (a bulk-classification signal) | ALERT — name the prompts with shared openings |
| 6 | **Verse-corpus validity** | Verse references look like they belong to this characteristic's evidence corpus (cross-check from §3 of the input; if you cited a verse not in §3, flag it) | ALERT — name the phantom-ref prompts |

Document the self-evaluation result inline at the end of the tier block — one sentence per check, PASS or FAIL. If everything passes, the next tier follows immediately in the same response.

### What NOT to do (each is a drift signal)

- Authoring prompts from a tier you have not announced as OPEN
- Holding multiple tiers' worth of unwritten findings in your response (the file write is per-tier, even though tiers can chain in one response)
- Skipping prompts "to come back later" — every prompt in a tier is answered before the tier's self-evaluation
- Cross-tier analysis or summary while a tier is in flight (e.g. *"now that I see T2, I notice T1 should have said…"*) — cross-tier patterns belong in the **final** Self-check after T7
- Substituting fluency for citation — every E must name verses / VCGs from §3
- Bulk-classifying multiple prompts with the same evidence pattern from a sample — each prompt is its own analytical pass

### Recovery if drift surfaces mid-tier

If during a tier you notice you have skipped prompts, mixed scope markers, or carried analysis from another tier in: **STOP**, announce the issue, abandon the half-written tier, and restart that tier from scratch (re-read §3, re-author from the first prompt). It is faster to restart a tier cleanly than to patch a contaminated one.

---

## Discipline (per v2_9 §12)

1. **One tier per response.** See the staged execution protocol above. The STOP gate is structural — it's how you avoid the prior-failure mode.
2. **Read every verse-meaning in the structural input** at the start of each tier. No sampling. The Pass A meanings condense each verse's inner-being content — read them all.
3. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*
4. **Fluency is not a quality signal** (v2_9 §2.4). Plausible-sounding text without specific citations is rejected.
5. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group within the characteristic (e.g. CHAR-1 spans multiple sub-groups), the finding text names the sub-group(s) inline.
6. **No cluster-scope findings.** Cluster synthesis runs after all 4 characteristics finish.
7. **No inter-tier analysis** while a tier is in flight. Reserve cross-tier observations for the Self-check at the end.
8. **Self-check at the end** — after T7 is written, in a separate response, post the self-check block (counts + carry-forward observations addressed + unexpected patterns).

---

## Carry-forward observations (apply to this characteristic)

These analytical hints were raised at characteristic-mapping time and are queued for Phase 9 attention:

### INTEGRATION_NOTE — Unclean-spirit register cross-cluster signal to M27 (cosmic-evil agents)

> M10c-E (Defilement by external spiritual agency, 21V — all akathartos NT) carries an M27 cross-register flag inherited from Phase 3. The unclean spirits are cosmic-evil agents recognised in NT exorcism narratives; they participate analytically in M27 (Evil) as well as M10c (Defilement). Phase 9 T6 (Structural Relationships) findings on characteristic 4 should attend to this register: defilement here is the *result* an external evil agent produces; in M27 the same verses analyse the *agent's* nature. The two analytical lenses are complementary, not duplicative.

**At Phase 9 end:** flag whether this observation surfaced in the findings as expected; mark in your final summary so CC can update status open → confirmed/refined.

---

## Output structure — built incrementally, tier-by-tier

Target filename: `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase9-char4-Defilement-by-external-spiritual-agency-findings-v1-20260526.md`

The file is built tier-by-tier. **Tier 0 (T0) creates the file with the header + T0 section. Each subsequent tier appends its `## T{N} — …` section.** Tiers chain automatically when self-evaluation passes; ALERT and stop only when self-evaluation surfaces an issue. At the end, after T7's self-evaluation passes, write the final Self-check block.

### Tier 0 (first response) — file header + T0 section + self-eval + (proceed to T1)

```markdown
# M10c Phase 9 — Characteristic 4 (Defilement by external spiritual agency) — findings

**Date:** 2026-05-26
**Characteristic_id:** 56
**Tiers complete:** T0 ✓  T1 ☐  T2 ☐  T3 ☐  T4 ☐  T5 ☐  T6 ☐  T7 ☐

## T0 — Divine Image and Created Design (12 prompts)

**T0.1.1 — [question text]**

**[CHAR-4]** E — finding text with verse citations…

---

**T0.1.2 — …**

…
```

After T0's 12 prompt blocks, post the self-evaluation:

```
T0 self-evaluation:
  1. Prompt count:       12/12 ✓
  2. Scope marker:       12× [CHAR-4] ✓
  3. Citation discipline: <N>/<E_count> E findings cite evidence ✓ (or list uncited)
  4. No cross-tier refs:  ✓
  5. Distinct openings:   ✓
  6. Verse-corpus check:  ✓ (or list phantom refs)
  → PASS. Proceeding to Tier T1.
```

Then immediately begin Tier T1 in the same response (re-read §3 fresh, author T1's 24 prompts, append the new `## T1 — Inner Being Faculty in Operation (24 prompts)` section, self-evaluate, decide PASS/ALERT).

### Tiers T1..T7 — chain by default, ALERT on issues

Each tier follows the same pattern: re-read §3 fresh → author prompts → write tier section → self-evaluate → (if PASS) proceed immediately to next tier; (if ALERT) stop for researcher review. The findings file grows by one tier section per cycle.

If a single response would be too long to hold a tier + the next one, you may split at a tier boundary (announce *"...PASS. Proceeding in next response."* and resume on the next prompt). The next-tier handoff is the same — re-read §3, author, evaluate, decide. Splitting mid-tier is forbidden.

### After T7's self-evaluation passes — final Self-check block

Append a final Self-check block at the end of the findings file (after T7's section):

```markdown
## Self-check

- Prompts answered: 189 / 189 ✓ (12+24+31+33+24+21+24+20)
- E findings naming specific evidence: <count>
- S findings: <count>
- G findings: <count>
- Carry-forward observations addressed: <list>
- Unexpected analytical patterns surfaced (across tiers): <list>
- Tiers complete: T0 ✓ T1 ✓ T2 ✓ T3 ✓ T4 ✓ T5 ✓ T6 ✓ T7 ✓
- Per-tier self-evaluations: all PASS (or list ALERTs that were resolved)
```

---

## After T7 + Self-check

1. Confirm the findings file is on disk with all 8 tier sections + the final Self-check block.
2. Ping CC: "M10c Char 4 (Defilement by external spiritual agency) Phase 9 findings ready"
3. CC parses, validates evidence-grounding + completeness, applies to cluster_finding with characteristic_id set.
4. Move to next characteristic (Char 5).

---

*End of brief. Load the structural input (#2) and begin **Tier T0** in your first response. Chain tiers when self-evaluation passes; ALERT only on issues.*