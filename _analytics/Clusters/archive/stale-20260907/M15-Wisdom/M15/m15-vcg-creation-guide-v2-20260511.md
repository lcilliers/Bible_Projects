# Verse Context Group (VCG) creation — cluster-instruction-aligned guide

**Compiled:** 2026-05-11 (supersedes v1 of this guide)
**Primary source:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v1_1-20260507.md`

The cluster instruction explicitly states it **replaces** (on finalisation) the prior verse-context instruction, the registry-management guide, the dimension-review instruction, and both Session B Stage 1/2 instructions. The cluster instruction is the sole authority for VCG creation going forward.

The previous instruction lineage led to misplacement in actual use (M15's "files - failed session" being the visible evidence). This guide therefore takes its content from the cluster instruction and does **not** carry forward the prior lineage's formal criteria except where the cluster instruction itself restates them.

---

## 1. Where VCG creation sits in the cluster flow

The cluster flow is 10 phases. VCG creation is **Phase 6**, not Phase 8. Phase 8 is the catalogue pass (findings against the 189-prompt T0–T7 list) which consumes the VCGs created in Phase 6.

| Phase | Activity | VCG creation? |
|---|---|---|
| 1 | Comprehension of dataset | No |
| 2 | UT verse review (VCREVISE patch) | No |
| 3 | Characteristic debate from glosses → provisional sub-groups | No |
| 4 | Control read → confirmed sub-groups (first directive) | No |
| 5 | First reading pass → 250-word summaries per sub-group | No |
| **6** | **Group-verse mapping per sub-group** | **★ VCG creation happens here ★** |
| 7 | Apply Phase 6 mappings to DB (one directive per sub-group) | DB write |
| 8 | 189-prompt catalogue pass → findings | No (consumes VCGs) |
| 9 | Findings recording into `cluster_finding` | DB write |
| 10 | Verification + cluster status flip | No |

**Prerequisites for Phase 6:**
- Phase 2 complete: every verse has either a `verse_context` row or an explicit `set_aside_reason`. No UT (untouched) verses remain.
- Phase 4 complete: sub-groups confirmed and applied to DB via the first directive. Every term sits in a sub-group (or BOUNDARY, or has been moved out of cluster).
- Phase 5 complete: one 250-word sub-group summary written for each sub-group. This is the analytical lens through which Phase 6 reads the verses.

If any prerequisite is incomplete, VCG creation is premature.

---

## 2. What a VCG is

A `verse_context_group` is a set of verses **for one term** where the verses share the same **inner-being phenomenon**.

From the cluster instruction §9:

> Every verse in the cluster (excluding set-asides) belongs to at least one `verse_context_group`, and each group has a precise context description grounded in the actual verse text.
>
> A verse may carry more than one distinct inner-being phenomenon; in that case it receives multiple group assignments. A `verse_context_group` may contain multiple verses where the same context applies.

**Key consequences:**

- One group is one phenomenon. Two phenomena → two groups (even if the verses overlap).
- The `context_description` is grounded in **what the verses show**, not in what the term means in a lexicon, not in what other VCGs for the term already say, not in what a similar cluster's groups looked like.
- The phenomenon is **inner-being**. Verses that don't engage the inner being are set-aside in Phase 2, not grouped.

---

## 3. The non-negotiable operating principle (cluster instruction §2)

This is the single most important section in the cluster instruction. Everything else in this guide is downstream of it.

> **Read every verse. Do not sample. Read what they say. Let the structure and analysis emerge from what is found. No assumptions from memory. No jumping to conclusions. Write on discovery.**

The instruction's own explanation of why this matters:

> Prior attempts at cluster analysis were discarded because they classified verses against pre-formed assumptions rather than reading each verse and deriving the analysis from what the verse actually said. Output that is structured and fluent but not grounded fails this rule.
>
> The cluster at session open is a body of textual evidence waiting to be interrogated — not a set of claims waiting to be confirmed.

**Three operational disciplines unpack this:**

**3.1 Write on discovery.** Every observation is written at the moment it is made, from the text that produced it. If an observation has not been written before moving to the next verse, it is not written — do not reconstruct observations from memory after the reading is complete. If you find yourself summarising at the end of a reading block rather than recording as you go, stop and go back.

**3.2 Cross-cluster contamination guard.** When working cluster N, prior knowledge from clusters 1 through N-1 must not colour the reading of cluster N's verses. Each cluster's verses are the sole authority for that cluster's findings. A finding that appears in a prior cluster is not evidence that the same finding applies here — it must be re-evidenced from this cluster's verse text.

**3.3 Fluency is not a quality signal.** Output that reads smoothly and is well-structured can still be entirely ungrounded. The test is not "does this sound right?" but **"can I name the specific verse that evidences this?"** If no verse can be named, the claim is not evidenced.

---

## 4. The Phase 6 process — VCG construction step by step (cluster instruction §9)

For each sub-group (one at a time, completed before starting the next):

**Step 1 — Read every non-set-aside verse in the sub-group.** Read, do not skim. Read in the canonical sequence the verses appear in, term by term.

**Step 2 — Validate existing group descriptions against actual verse evidence.** For each existing group:
- Open the group's current `context_description`.
- Open the verses currently assigned to it.
- Does the description accurately describe what the verses are doing? If not, revise.
- Does every verse genuinely belong? Verses that don't belong are reassigned or flagged.

Status outcomes per existing group:
- **RETAINED** — description unchanged, members unchanged.
- **RETAINED AND REFINED** — description revised; members unchanged or trimmed.
- **SPLIT** — verses contain genuinely distinct phenomena; produce two or more new groups (see §5 — Conglomerate-group split).
- **MERGE** — two existing groups describe the same phenomenon and should be unified.
- **REVIEW AND DECISION** — a real judgment is needed that AI alone cannot make; flag for researcher.

**Step 3 — Where verses carry phenomena not captured by existing groups, propose new groups.** A new group is warranted when:
- The verses describe an inner-being phenomenon distinct from anything any existing group captures, AND
- A single anchor verse can be named that definitionally evidences this phenomenon (the anchor-uniformity test — see §5).

**Step 4 — For each verse, record:**
- Which group(s) it belongs to (one in the normal case; two if it legitimately carries two distinct phenomena — see §6).
- The **per-verse observation** — the analytical note that captures what the specific verse contributes to the group. This is the verse-level write-up that grounds the group's description in the verse text.

**Step 5 — Designate one anchor verse per group.** The anchor is the verse that most directly and definitionally evidences the group's named phenomenon. One anchor per group is the minimum (hard gate); a second is permitted only if it adds something the first does not.

**Step 6 — Identify cross-group dual assignments.** Some verses legitimately operate at two distinct inner-being levels through the same term. List those at the end of the mapping document.

---

## 5. The conglomerate-group split rule (cluster instruction §9 — the defensive heart)

This rule is the most important single guard against the misplacement pattern that plagued the previous instruction's outputs.

From the cluster instruction §9, verbatim:

> When reading the verses assigned to an existing group, if they contain genuinely distinct inner-being phenomena — different subjects, different directions, different faculty engagements, different consequences — the group must be split before the catalogue pass begins. Do not apply catalogue prompts to a conglomerate containing multiple distinct phenomena; the answers will be the average of things that are not the same, and the finding will be analytically false.

**The split test (verbatim):**

> Can the group's verses be answered uniformly by a single anchor verse, or do different subsets of the verses require different anchors to answer the same prompt? If different anchors are needed for different subsets, the group should be split.

In practice:

- Pick the verse you would designate as anchor for the existing group.
- Ask: does that anchor evidence the same phenomenon for every other verse in the group?
- If yes — the group is coherent.
- If no — the group is a conglomerate. Identify the subsets that each need their own anchor, and produce that many new groups.

**Precedent (cluster instruction §9):** In M06, group 1601 (*sa.ne*, 139 verses) was split into five distinct groups during Phase 6. The instruction notes: "The instruction to split came from reading the verses — not from the group label." This was named "the most consequential single analytical act of the session."

---

## 6. Dual-assignment verses — the only legitimate doubling

A single verse may appear in two VCGs **for the same term** only when it plainly operates at two distinct inner-being levels through that term.

This is the **exception, not the norm.** When it happens:

- Two `verse_context` rows are created for the verse (the UNIQUE constraint is `(verse_record_id, mti_term_id, group_id)` — same verse permitted in two different groups, never twice in the same group).
- The rationale for dual-assignment is recorded in the obslog and surfaces in the Phase 6 mapping document's cross-group section.

If you find yourself dual-assigning many verses, you are probably failing the split test (§5) — the groups likely overlap and need to be split or merged rather than the verses doubled.

---

## 7. Anchor verses (cluster instruction §9 + §16)

Every VCG must have **at least one** anchor verse. This is a hard gate — Phase 6 self-check fails without it.

- 1 anchor per group is the minimum and typical case.
- 2 anchors per group only where the second adds something the first does not.
- More than 2 is an antipattern — it signals the group is conglomerate (re-apply §5 split test).

An anchor verse must:
- Make the group's inner-being phenomenon evident without surrounding context.
- Stand alone as evidence.
- Be quotable in the Session C narrative without ambiguity.

The anchor serves two roles: efficiency (downstream phases read anchors, not full corpora) and citation (anchors appear as evidential footings in Session C and D narratives).

---

## 8. The `context_description` — what good looks like

The cluster instruction is light on formal requirements for `context_description` (it states only "precise context description grounded in the actual verse text"). In practice, the descriptions that survive the Phase 8 catalogue pass without breaking down share these properties:

- **One sentence.** A description that needs two sentences is probably describing two phenomena.
- **Names the inner-being phenomenon directly** (the thing the verses are about), not what the term lexically means.
- **Anchored in what the verses show.** Avoid theological framing not visible in the verses themselves.
- **Sufficient to distinguish this group from other groups for the same term.**

The Phase 8 fluency guard (§9 below) applies here too: a description that reads well but cannot be tested against a named verse is suspect. Test every description by asking: which verse in this group am I describing? If you cannot point to that verse, the description is ungrounded.

---

## 9. The Phase 6 self-check (cluster instruction §9 + §16)

Before submitting the mapping document for Phase 7 application, AI confirms in the obslog:

| Check | Required |
|---|---|
| Every non-set-aside verse in the sub-group is assigned to at least one group. | Yes |
| Every group has at least one anchor verse. | Yes |
| No verse is left in P (pending) or UT (untouched) state. | Yes |
| Existing groups have been reviewed for splitting (§5 test applied). | Yes |
| The mapping document's verse counts add up to the sub-group's total non-set-aside count. | Yes |
| Per-verse observations are recorded for every verse. | Yes |
| Cross-group dual assignments are listed in the dual-assignment table. | Yes |
| Obslog entries exist for every group, verse-to-group assignment, anchor designation, and per-verse observation. | Yes |

A failed self-check stops the phase. The work is not handed to CC for Phase 7 application until every check passes.

---

## 10. Output document format (cluster instruction §9)

One mapping document per sub-group. Path:

`Sessions/Session_Clusters/{code}/WA-{code}-{subgroup}-group-verse-mapping-v1-{date}.md`

**Structure per group section:**

```
## Group {existing-code} | {provisional-new-code}

**Status:** RETAINED | RETAINED AND REFINED | NEW | SPLIT | MERGE | REVIEW AND DECISION

**Context description:** {one-sentence description grounded in verse text}

**Anchor verse:** {Reference}  — {one-sentence rationale: why this verse definitionally evidences the phenomenon}

| Verse | Term | What the verse shows |
| --- | --- | --- |
| {Ref} | {Strong's + translit} | {one-line per-verse observation} |
| ... | ... | ... |
```

**End-of-document sections:**

- **Cross-group / dual-assignment table** — verses that legitimately belong to two groups.
- **Flags for CC** (optional) — verses that could not be classified within the proposed structure and need researcher attention.

---

## 11. Why this discipline matters — the misplacement pattern under the previous approach

The previous instruction allowed (and the M15 "files - failed session" demonstrates) four failure modes that the cluster instruction was specifically designed to catch:

**11.1 Term-centric grouping** — groups formed by what the term lexically does (translation pattern, syntactic role) rather than by the inner-being phenomenon the verses show. Description reads like a lexicon entry rather than a phenomenon statement.

> **How the cluster instruction catches it:** §2 "Let the structure and analysis emerge from what is found. No assumptions from memory." Phase 5 250-word summaries (read all verses first, then describe the phenomenon they show) precede group derivation, so the analytical frame is verse-derived, not lexicon-derived.

**11.2 Inheritance from existing structure** — AI sees N existing groups and produces ~N new ones, even when the verses would warrant consolidation or different cardinality.

> **How the cluster instruction catches it:** §9 conglomerate-split rule. The split test is anchor-uniformity, not group count. If you can answer all verses with one anchor, it's one group regardless of what existed before; if you need different anchors, split regardless of what existed before.

**11.3 Fluency-mistaken-for-grounding** — well-structured, smoothly-written group descriptions that have no specific verse evidence behind them.

> **How the cluster instruction catches it:** §2 fluency-is-not-quality-signal. Restated at §11 (Phase 8): "the test is not 'does this sound right?' but 'can I name the specific verse that evidences this?'" Per-verse observation (§9 step 4) forces every verse-to-group link to be grounded in a specific analytical note about that verse.

**11.4 Cross-cluster contamination** — findings from earlier clusters imported as assumptions about the current cluster's verses.

> **How the cluster instruction catches it:** §2 cross-cluster contamination guard. Each cluster's verses are the sole authority for that cluster's findings.

---

## 12. The clean-slate working method (operational technique that aligns with the instruction)

When AI's prior work shows symptoms of any failure mode in §11, the working method that aligns with the instruction is to **strip the existing VCG context** from the input given to AI and re-derive from verse + term + verse-level meaning only.

The clean-slate JSON ([m15-clean-slate-v1-20260511.json](m15-clean-slate-v1-20260511.json)) is the artefact for this: each verse carries only `vr_id`, `reference`, `verse_text`, `strongs`, `translit`, `gloss`, and the AI's prior verse-level meaning. No current VCG code, no current group description, no sub-group context, no AI annotations from prior passes.

This is consistent with the cluster instruction §2: the cluster at session open is a body of textual evidence, not a set of claims waiting to be confirmed. The clean-slate input puts AI back at session open with no claims to confirm.

---

## 13. What this guide deliberately does NOT carry forward from the prior lineage

For clarity, the following formal criteria from the superseded verse-context-instruction lineage are NOT restated here because the cluster instruction does not retain them:

- The formal "characteristic term vs property term" distinction
- The three-factor "materially different" test for new groups
- The four-requirement formal specification for `context_description`
- The five-group consolidation heuristic
- The Section 3.2c cluster-treatment discipline (added v3_10 only)
- The dual-purpose framing of anchor verses (efficiency + citation)

Where the cluster instruction relies on principles that overlap with the prior lineage (e.g. one-sentence description, anchor-min-one, single phenomenon per group), this guide states the principle from the cluster instruction's wording. Where the prior lineage went into more detail, the omission is intentional — the cluster instruction's authors chose to lighten the formal scaffolding and lean on operating discipline instead.

---

*Compiled from `Workflow/Instructions/wa-sessionb-cluster-instruction-v1_1-20260507.md` (Session B Cluster Analysis, current authoritative). All verbatim quotations and section references trace to that document. Where this guide describes operational technique not stated verbatim in the instruction (e.g. the clean-slate working method, §12), the technique is identified as a working method that aligns with the instruction's principles rather than as instruction text.*
