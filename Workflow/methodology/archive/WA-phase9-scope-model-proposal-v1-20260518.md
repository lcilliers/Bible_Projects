# Phase 9 scope model — proposal for researcher review

**Date:** 2026-05-18
**Author:** CC
**Trigger:** M04 retrofit reached Step 6 decision point (selective Phase 9 findings augmentation). Researcher raised the structural concern that sub-groups have stratified into register-variants, the 189 × sub-group matrix produces artificial repetition, and AI chat limits force the question of how to achieve completeness + coverage of evidence within practical constraints.

**Status:** PROPOSAL FOR DECISION. Not applied. Sections at the end carry decision blanks for researcher mark-up. After your decisions are marked, ping CC to:
- Build Step 6 AI package under the chosen model
- Optionally draft a v2_6 instruction bump codifying the model change

**Required inputs** (background reading, in suggested order):

| # | Document | Purpose |
|---|---|---|
| 1 | This proposal | The structural analysis + proposed model |
| 2 | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` §12 (Phase 9), §12.4 (markers), §14.4 (loader scope resolution), §15.2 (closure pre-flight) | The current scope model being proposed for revision |
| 3 | `Sessions/Session_Clusters/M04/WA-M04-step5-vcg-design-applied-v1-20260518.md` | M04 current state — 16 sub-groups, 48 VCGs, 1116 verses; the empirical case driving the proposal |

---

## 1. The structural problem

Three things were conflated in v2_0's Phase 9 design:

1. **Coverage of analytical dimensions** — the 189 questions ensure no analytical angle is missed (cognitive, phenomenological, relational, eschatological, diagnostic, etc.)
2. **Coverage of evidence** — every verse should be read and used somewhere in the findings
3. **Stratification of registers** — sub-groups carve a characteristic into its register-variants

The current rule (189 questions × every sub-group + cluster scope) tried to do all three at once. It works when:

> **sub-groups = characteristic-level differentiations** (few, each substantively distinct → each warrants the full 189 sweep)

It breaks when:

> **sub-groups = register-stratifications** (many, each a variant of the same characteristic → most prompts produce mechanically-identical findings restated across micro-distinctions)

## 2. M04's current state — the empirical case

| Metric | Count |
|---|---:|
| Cluster characteristic | One — Joy, Gladness, Delight, Pleasantness |
| Active substantive sub-groups | 16 |
| Active VCGs | 48 (30 original + 18 from Step 5) |
| Active relevant verses | 1,116 |
| Cells under 189 × sub-group + CLUSTER strict model | 189 × 17 = 3,213 |

The 16 sub-groups stratify the **one** characteristic by:

- **Register** (vertical Godward / horizontal / material-sensory / corrupt-illicit / circumstantial / etc.)
- **Disposition** (volitional / evaluative / experiential / relational)
- **Source domain** (OT-prescribed / NT-distinctive / wisdom / eschatological)
- **Manifestation mode** (cheerful-under-suffering / wonder / pleasantness-as-quality)

None of the 16 is an independent characteristic in its own right. They are **evidence-buckets within one characteristic**.

Running 189 × 16 produces:

- For prompts like "What is this characteristic?" / "How is it named?" / "Where does it sit in the inner being?" — 16 near-identical answers per prompt. Repetition without analytical gain.
- For prompts like "How does this characteristic manifest in this register?" or "What boundary cases test the edges?" — sub-group-specific answers have real analytical weight.

So the strict matrix produces **mostly mechanical repetition + some genuinely register-specific findings**, mixed undifferentiated.

## 3. What sub-groups actually are now

Sub-groups currently serve three purposes:

| Purpose | Notes |
|---|---|
| **Evidence organisation** | Researcher / AI / Session C reader can navigate the corpus by register. Indispensable for analytical work. |
| **Publication structure** | Session C chapters can map ~1:1 to sub-groups (a chapter per register). Indispensable for cluster publication. |
| **Findings scope** | Findings authored per sub-group ensure register-specific patterns surface. **This is where the dilution lives.** |

The first two purposes are sound and should be preserved. The third — using sub-groups as the primary scope of findings — is the source of the problem.

## 4. Proposed model — cluster-primary scope with selective sub-group authoring

### 4.1 Default scope = CLUSTER for every prompt

- AI reads the cluster's full evidence (organised by sub-group for navigation)
- For each of the 189 prompts, AI authors **one finding at CLUSTER scope**
- The finding text names register-variants inline using sub-group references, e.g.:

> "The characteristic operates differently across registers: in M04-K (sensory, ni.cho.ach aroma-acceptance — Lev 1:17, Gen 8:21) the focus is divine-reception-of-correct-worship; in M04-L (evaluative, ki-tov declarations — Gen 1:31, Psa 100:5) the focus is the soul's moral-evaluative faculty; in M04-P (corrupt, predatory exultation — Hab 3:14) the focus is the disordered inner-being directed at cruelty."

- Result: **one row per prompt at CLUSTER scope = 189 rows per cluster** (vs 3,213 rows in the strict matrix model)

### 4.2 Sub-group scope authored only when one of three triggers fires

1. **Structurally distinct phenomenon** — a sub-group's evidence carries a phenomenon the cluster-level finding cannot faithfully represent without flattening. Example: M04-P (corrupt/illicit) has anchor verses (Hab 3:14, Eze 23:12) whose disordered-delight dynamic deserves its own row at sub-group scope under T1.2.1 (sub-group structural description).
2. **Register-specific prompt** — typically T4 (Manifestation) and T5 (Boundary cases) questions ask "how does X manifest in this register" — these prompts are inherently sub-group-shaped. Author sub-group rows for these.
3. **Publication-driven** — researcher flags certain sub-groups as warranting dedicated chapters in Session C. Those sub-groups get a fuller per-sub-group finding sweep covering ~30-60 of the 189 prompts (the ones whose answers vary by register).

### 4.3 Expected cell count per cluster

| Source | Count |
|---|---:|
| CLUSTER scope (189 prompts × 1) | 189 |
| T1.2.1 sub-group structural descriptions (one per sub-group) | ~16 |
| Selective T4/T5 sub-group findings (~3-5 per sub-group on average) | ~50-80 |
| Publication-driven extra sub-group sweep (where flagged; varies) | 0-300 depending on flagging |
| **Total** | **~250-580** |

Compare to strict matrix: **~3,213 cells**. Cluster-primary model reduces the cell count by 80-90% while preserving analytical coverage.

## 5. New completeness checks — replacing the matrix discipline

Removing "189 × every sub-group" loses one form of completeness. Two replacement checks recover the discipline:

### Check 1 (existing, narrowed) — Prompt-completeness

Every one of the 189 prompts has **≥1 row at CLUSTER scope**. Easy automated check; existing §15.2 check 2 narrowed.

### Check 2 (new) — Evidence coverage

**Every `is_relevant=1` verse is cited in at least one finding's `finding_text`.**

- CC's parser walks `cluster_finding.finding_text` for verse references (existing regex from §15.2 check 1 — evidence-grounding).
- Joins citations against `verse_context` (is_relevant=1, delete_flagged=0).
- Reports verses with **zero citations** as a coverage gap.
- Researcher reviews the gap list and decides: expand a finding to cite the missing verse; OR accept the verse as "evidenced-by-pattern-not-by-specific-citation" (e.g., one of 38 ni.cho.ach verses in M04-K-VCG-01 — the VCG description covers the pattern; individual verse-by-verse citation is impractical).

This is the missing discipline that currently isn't enforced. It directly answers "is every verse considered?" without relying on the sub-group matrix to do it indirectly.

## 6. What this means for v2_5

This is a methodology change. Codifying it would be a **v2_6 instruction bump** affecting:

| Section | Change |
|---|---|
| §12 Phase 9 | Default CLUSTER scope; sub-group scope by trigger; document the three triggers explicitly |
| §12.4 marker conventions | Sub-group markers `**[A]**` used for inline citation inside CLUSTER findings, not as default row-expansion forcing per-sub-group rows |
| §14.4 loader behaviour | Loader respects scope markers — `**[CLUSTER]**` → 1 cluster row; `**[A]**` only when AI explicitly opens a sub-group-scope block under a clear trigger |
| §15.2 closure pre-flight | Check 2 narrowed to "every prompt has ≥1 CLUSTER row"; new check 3 = "every is_relevant verse appears in ≥1 finding's citations" |

I recommend **holding the v2_6 instruction draft until Step 6 runs M04 under the proposed model**. Let the empirical test on M04 confirm or refine the proposal before codifying.

## 7. Step 6 path under the proposed model

Given M04 already has v2_4-era findings in M04-A through M04-J (~1,400 sub-group rows + ~300 cluster rows authored under the strict matrix), the cleanest Step 6 path:

### Step 6a — Preserve existing sub-group findings

M04-A through M04-J existing sub-group findings stay. They are register-specific analytical work already done; they have analytical and Session C publication value. They don't need to be moved or re-authored. **No DB work.**

### Step 6b — Author T1.2.1 structural descriptions for the 6 new sub-groups

One finding per new sub-group (M04-K through M04-P) at sub-group scope under prompt T1.2.1 (sub-group structural description). **~6 rows.** Trivial CC mechanical task — descriptions are already in `cluster_subgroup.core_description` from Step 3. CC just builds and inserts the cluster_finding rows.

### Step 6c — Author 189 CLUSTER-scope findings for M04 against the full post-retrofit corpus

This is the heavy lift. AI reads the cluster's full evidence (1,116 verses across 16 sub-groups), authors 189 cluster-scope findings that synthesise patterns across sub-groups, citing register-variants inline.

**Important:** these new cluster-scope findings **SUPERSEDE** the v2_4-era cluster-scope findings, which were authored against an incomplete corpus (pre-retrofit, with bias-flagged set-asides and missing register families). Old cluster rows soft-deleted; new ones inserted.

**~189 rows.** Manageable in 3–4 AI chat sessions of ~50 prompts each (suggested batching: T0/T1 in batch 1, T2/T3 in batch 2, T4/T5 selective in batch 3, T6/T7 in batch 4).

### Step 6d — Run evidence-coverage check

After Step 6c's findings load, CC runs the new check 2 (every is_relevant verse cited at least once). Reports verses with zero citations.

### Step 6e — Stop and review

Per your earlier direction: stop before Phase 10. Review:

- Are the 189 cluster findings sound?
- Is verse-coverage adequate? (Gap list from check 2 manageable?)
- Did sub-group findings get duplicated mechanically anywhere?
- Tune the discipline before Phase 10 inherited reconciliation.

### Volume estimate for Step 6

| Step | New rows | AI sessions |
|---|---:|---:|
| 6a (preserve existing) | 0 | 0 |
| 6b (T1.2.1 for new sub-groups) | 6 | 0 — CC mechanical |
| 6c (189 CLUSTER scope) | 189 | ~3-4 sessions of 50 prompts each |
| Selective T4/T5 sub-group additions (within 6c) | ~30-60 | included in 6c |
| **Total Step 6** | **~225-255 rows** | **~3-4 AI sessions** |

vs strict matrix model: ~1,000+ new rows, ~10-15 AI sessions. Significant compression without analytical loss.

## 8. Risks and mitigations

| Risk | Mitigation |
|---|---|
| AI doesn't cite enough sub-group references in cluster-scope findings → register-specific patterns lost | Brief explicitly requires citing register-variants inline; output format includes worked examples. Check 2 (evidence coverage) catches under-citation. |
| Existing v2_4 sub-group findings (M04-A..J) become inconsistent with new CLUSTER findings | Acceptable — sub-group findings represent register-specific analysis; CLUSTER findings represent characteristic-level synthesis. The two operate at different levels and don't need strict alignment. |
| Session C publication structure assumes per-sub-group findings | Existing sub-group findings preserved. New sub-groups get T1.2.1 descriptions + selective T4/T5 — enough for chapter-level publication. Researcher can flag specific new sub-groups for fuller sweep if Session C needs more depth. |
| The proposal changes methodology mid-programme | M04 is the first cluster under v2_5; it's the right test case. If the new model fails on M04, v2_6 doesn't ship and we revert. If it succeeds, v2_6 codifies the model for future clusters. |
| Closed clusters (M01, M02, M03, M05, M15) used the strict matrix — are they non-compliant? | No. Closed clusters' Phase 9 work stands; they were authored under v2_4 discipline. When (if) we retroactively audit closed clusters under v2_6, the cluster-primary check becomes additive (does a cluster have ≥1 CLUSTER row per prompt? are all verses cited?). Existing sub-group rows are not a non-compliance signal. |

## 9. Decisions needed from researcher

| # | Question | Options | Your decision |
|---|---|---|---|
| 1 | Adopt the cluster-primary scope model for M04 Step 6 onwards? | Yes / No / Adjust | _[YES / NO / ADJUST: ...]_ |
| 2 | Accept the proposed Step 6a–6e structure? | Yes / Modify | _[YES / MODIFY: ...]_ |
| 3 | Hold v2_6 instruction draft until M04 Step 6 validates the model? | Yes / Draft now | _[YES / DRAFT NOW]_ |
| 4 | Are there specific M04 sub-groups you want flagged for a fuller per-sub-group sweep (publication-driven trigger)? | List sub-groups or "none for now" | _[LIST or NONE]_ |
| 5 | Verse-coverage gap policy: when CC reports a verse with zero citations, what's the default action? | Expand a finding to cite it / Accept the gap with rationale / Researcher reviews each | _[EXPAND / ACCEPT-WITH-RATIONALE / REVIEW-EACH]_ |

## 10. Next steps once decisions are marked

If Q1 = YES:

1. CC drafts the **Step 6c brief + structural input** under the cluster-primary model (similar shape to Step 4 / Step 5 packages — Required-inputs block, context, decision vocabulary, worked examples, batching guidance).
2. CC runs **Step 6b** as a CC mechanical task (insert 6 T1.2.1 rows) — can happen in parallel.
3. Researcher runs AI sessions for Step 6c batches (3-4 sessions).
4. CC parses, validates, applies; runs check 2 (verse coverage); produces gap report.
5. Researcher reviews; we tune; decide Phase 10 entry.

If Q1 = NO or ADJUST, CC drafts the corresponding alternative (full sub-group sweep, or hybrid model with different scope rules).

---

*End of proposal. Mark your decisions in §9 and ping me when ready.*
