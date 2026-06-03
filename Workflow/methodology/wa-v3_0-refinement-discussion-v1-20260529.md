# v3_0 cluster pipeline — refinement discussion

**Date:** 2026-05-29
**Status:** Discussion document. No instruction-doc changes applied yet. Decisions captured at the end.
**Trigger:** M38 retrospective surfaced four-hour dead-time gap, repeated re-run cycles, audit-after-prose ordering, mechanical prose generation. Researcher's instruction: critical thinking before M36.

This document works through the five refinement areas the researcher named and proposes specific, scoped changes. Each section has the same structure: **observed problem** (with M38 evidence) → **root cause** → **options with tradeoffs** → **recommendation** → **what changes in v3_0 instruction** → **what CC needs to build**.

---

## (a) Reduce dead time

### Observed problem

From the M38 time summary:

| Span | Duration | Cause |
|---|---:|---|
| 10:03 → 14:06 (Phase B close → Phase D start) | 4 h | Unstructured gap |
| Small gaps between B.1, B.2, B.3 | ~5–10 min each | Researcher review-and-decide gate |
| Phase D Stage A char re-runs | ~10 min each | Detection-of-failure → re-run lag |

Active processing was 6 h 45 min; wall clock 12 h 31 min. The 4-hour gap alone is ~30% of wall clock.

### Root cause

The pipeline has implicit **review-and-approval gates** between phases that aren't formalised. The researcher is busy with other things, doesn't pick up the next phase until they happen to check chat. CC's status updates surface in chat only — researcher misses them, comes back hours later, asks "where are we?", CC re-orients them.

Three distinct gate types are conflated:
1. **Mechanical gates** (run the validator script; check the file was written) — no judgment needed; CC should pass these autonomously
2. **Confirmation gates** (CC ran the validator; here's the verdict; OK to proceed?) — researcher confirms but doesn't need to think
3. **Judgment gates** (the AI's output had two BOUNDARYs; how should they be handled?) — researcher must engage

M38 had all three at every phase boundary, with no signal to distinguish which gate the researcher was facing. So the researcher treats every gate as judgment, which slows them down on mechanical and confirmation gates.

### Options

**Option 1 — Auto-advance through mechanical and confirmation gates.**
CC runs the validator and writes the next-phase input automatically. The researcher's next action is unblocked the moment they return. They make the API call when ready (or CC makes it, if researcher pre-authorised). Trade-off: less per-phase researcher visibility on automated steps; relies on validators being right.

**Option 2 — Persistent status dashboard.**
A single file `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-status-v1-{date}.md` that CC keeps continuously updated. Researcher keeps it open in IDE. Header shows current phase, current state, and what action (if any) is required. Trade-off: discipline-dependent; only useful if researcher actually opens it.

**Option 3 — Async pipeline with judgment-gate breakpoints.**
CC runs phases autonomously through mechanical + confirmation gates, and pauses only at judgment gates. When it pauses, it pings the researcher (option 4). Trade-off: requires real confidence in validators and the auto-recovery scripts. Higher up-front engineering cost.

**Option 4 — Notification mechanism.**
When CC needs the researcher, an active push: VS Code notification, email, audible cue, etc. Pairs with options 2 or 3. Trade-off: infrastructure to build; may be intrusive.

### Recommendation

**Combine Option 1 + Option 2 + Option 4.** Option 3 (full autonomous run) is too risky for v3_0 — judgment gates are real and judgment errors compound. But mechanical and confirmation gates can disappear:

- CC writes the **dashboard file** (Option 2) at every state change.
- CC **auto-advances** through any gate where the next-phase input file can be deterministically generated from the previous phase's validated output (Option 1).
- CC **pings** the researcher only at judgment gates and only when the researcher hasn't responded within a configured window (Option 4 — covered separately in section (b)).

### What changes in v3_0 instruction

- Add §X.1 "Gate types" — distinguish mechanical / confirmation / judgment gates explicitly.
- For each phase boundary, declare which gate type applies. Most B.1 → B.2 and D.A → D.B boundaries can be confirmation (auto-advance allowed once validator passes).
- Add §X.2 "Dashboard file" — the canonical state file CC maintains.

### What CC needs to build

- `scripts/_init_cluster_dashboard_v1.py` — creates the dashboard at cluster start
- Dashboard-update helper called from every phase script
- Auto-advance logic in B.1 → B.2 input builder, B.2 → B.3 input builder, D.A → D.B input builder

---

## (b) Refine alerts for researcher action

### Observed problem

Researcher gets distracted, misses chat status notes, returns hours later. By that time CC's chat-surface may have been summarised away, so the researcher returns to a stale picture and re-asks. From the conversation just gone: "I am very likely lost. It was difficult to follow the process as much is done in the background, and surfacing notes are often stale."

### Root cause

Chat is push-once-and-forget. Researcher must be looking at it to receive a notification. There is no retrieval mechanism that survives summarisation.

### Options

**Option A — Dashboard file (recommended in section a).**
File is always current; researcher pulls when they remember. Doesn't solve the "doesn't remember" problem.

**Option B — VS Code notification API.**
CC running as VS Code extension can probably trigger native notifications. Researcher sees system-level toast even when chat isn't focused. Trade-off: only works when VS Code is open; researcher might still miss it if VS Code is minimised.

**Option C — Repo-root urgent-action file.**
`tasks.md` or new `URGENT.md` at repo root. CC writes a single line at the top whenever attention is needed: `🔔 2026-05-29 09:15 — M36 Phase B.1 awaiting BOUNDARY decision (1 verse). See: Sessions/Session_Clusters/M36/wa-cluster-M36-status-v1-20260529.md`. Researcher's IDE shows the file in the explorer. Trade-off: depends on researcher's IDE habit.

**Option D — Email or Slack webhook.**
Most reliable external push. Trade-off: requires external setup; may be overkill for a one-researcher project; may be intrusive.

**Option E — Terminal bell + visible session-log line on every gate.**
Lightweight; works only when terminal is focused.

### Recommendation

**Option B + Option C combined.** VS Code is the researcher's primary tool, so notifications there will land most reliably. Plus the repo-root URGENT.md as a fallback that survives notifications being dismissed. Pair with the dashboard from section (a) — the URGENT line points at the dashboard, dashboard explains the full state.

Option D (Slack/email) — defer unless the in-IDE channel proves insufficient. Adds complexity without proportionate value at single-researcher scale.

### What changes in v3_0 instruction

- Add §X.3 "Researcher attention" — when a judgment gate is reached, CC writes the URGENT line and posts the VS Code notification with a clear "do X, respond Y" framing.

### What CC needs to build

- `scripts/_alert_researcher_v1.py` — writes URGENT line + triggers VS Code notification
- Standard "attention required" template: what's blocked, what decision is needed, where the input file is, what the expected response shape is

### Open question for researcher

Does VS Code actually support extension-triggered notifications in the CC integration mode you're using? If not, fall back to URGENT.md only — still useful, just less push.

---

## (c) Self-healing audits after each phase

### Observed problem

M38 ran the v2_5 audit only after Phase E was complete. The audit surfaced 1 RESCUE candidate, 5 missing anchors, 177 ungrounded findings, 1747 completeness-gap items. Most of these — anchors and ungrounded findings in particular — could have been caught and fixed inside the phase that produced them, at a fraction of the rework cost.

### Root cause

Audit is conceived as an end-of-cluster integrity check rather than a per-phase quality gate. Per-phase validators exist (the B.1, B.2, B.3 validators) but they check structural correctness, not analytical hygiene. So things like "this E-coded finding has no verse reference" slip through every phase gate.

### Options

**Option 1 — Per-phase hygiene checks.**
Each phase script ends with a hygiene pass. Catches obvious issues (no anchor, no verse reference, forbidden vocabulary in reasoning) and either auto-fixes (anchor designation) or surfaces (RESCUE candidates).

**Option 2 — Lift the v2_5 audit into per-phase form.**
Decompose the v2_5 audit into the phase-specific checks each rule applies to. Run only the rules relevant at each phase boundary.

**Option 3 — Single end-of-D audit gates Phase E.**
Run the full audit at the end of Phase D. Phase E can only start when the audit verdict is BOUNDED-FIXES with no real issues or the researcher has explicitly accepted the open issues. (Per the `feedback_audit_before_prose` memory.)

### Recommendation

**Combine Option 2 + Option 3.** Per-phase rules where they cheaply prevent rework (the anchor check inside B.3; the BOUNDARY-reason check inside B.1; the forbidden-grounds check inside Phase A); end-of-D full audit as the hard gate before Phase E.

| Phase | Hygiene checks added | Auto-fix or surface |
|---|---|---|
| A (UT) | Set-aside reasons match §4.5.1 forbidden grounds | Surface (RESCUE candidates) |
| A (Pass A) | Coverage gap (relevant verses without meaning); empty meanings | Re-run failed verses; surface truly empty |
| B.1 | BOUNDARY reasons are in valid grounds set; forbidden vocabulary in reasoning | Re-prompt for invalid reasons; surface unfixable |
| B.2 | 40% distribution ceiling; BOUNDARY-not-parking-lot; coverage gap on relevant verses | Auto-repair coverage gaps; surface 40% violations |
| B.3 | All VCs have group_id; **anchor verse designated per term** (new); no orphan terms | Auto-designate single-verse-term anchors; surface multi-verse anchor-missing |
| C apply | Transaction success; status flip verified | Roll-back on partial success |
| D.A | Every characteristic has expected count of E/S/G findings; all q_codes present; **finding_text has verse or VCG reference** (new) | Re-run missing q_codes; surface ungrounded findings |
| D.B | All 189 cluster-scope rows present; outcome codes valid; no truncation; **finding_text has verse or sub-group reference** (new) | Re-run missing tiers; surface ungrounded synthesis |
| End of D | Full v2_5/v3_0 audit | Gate Phase E entry |

The two **new** checks (anchor designation per term in B.3; verse-or-VCG reference in finding_text in D.A/D.B) directly address two of the four M38 audit findings — if these had been in place, M38's audit would have caught those issues automatically.

### What changes in v3_0 instruction

- Add §X.4 "Per-phase hygiene checks" — the per-phase rules list above, with each phase's required checks named.
- Promote the existing "end-of-D audit" requirement to a hard Phase E gate (already saved as feedback memory; now needs to be in the instruction proper).

### What CC needs to build

- Per-phase hygiene scripts: extend the existing B.1/B.2/B.3 validators with the new checks; new D.A and D.B hygiene scripts
- v3_0-aware audit script (the existing audit is v2_5 — may produce false positives on v3_0 data, as M38 confirmed)

---

## (d) Scope and load management in Phase B and Phase D Stage A

### Observed problem

Phase B and Phase D Stage A in M38 had multiple re-run cycles:

| Phase | Failure | Cause | Fix |
|---|---|---|---|
| B.2 design | 46 dups, 15 missing, 1 spurious | AI placed verses in multiple sub-groups; missed some | Repair API call |
| B.3 M38-A | JSON truncation at 121 verses | Output exceeded max_tokens | Partial parse + targeted repair |
| B.3 E/F/G | Small gaps | Coverage drift | Targeted API repair |
| D.A chars 1/2/4/5/7 | q_code drift | AI numbered T0.1.1, T0.1.2… instead of catalogue codes | Order-based remapping + re-run |
| D.B 4-segment | max_tokens truncation on every segment | Output volume exceeded | Switched to per-tier (8 calls) |
| D.B T2/T3/T7 | Partial truncation | Output volume | Re-run with max_tokens=24000 |

These failures aren't disasters — each was fixed in 10–30 min of additional work. But they account for a meaningful slice of M38's wall clock and cost. The pattern is consistent: AI output volume exceeds bounds OR AI deviates from prescribed naming.

### Root cause

Three root causes:

1. **No output-volume budgeting up-front.** Each API call sets max_tokens by guess. When the input has 121 verses requiring per-verse output, the response will truncate.

2. **Free-text output for structured data.** The AI is asked to produce verse assignments in markdown or loose JSON. Drift in formatting, q_code numbering, and field names is the result. Schema-constrained output (via `response_format` or via tool-use) would prevent the drift entirely.

3. **No failure log.** Each failure was handled in conversation context, then forgotten. There's no place where "B.2 fails on coverage gaps in ~30% of runs" is recorded, so we can't see whether the failure rate is improving across clusters.

### Options

**Option 1 — Estimate output volume up-front and size segments to fit.**
For Phase B.3: count verses per sub-group, estimate ~150 tokens per VCG creation, set max_tokens with headroom. Split sub-groups that would exceed limit into multiple calls.

**Option 2 — Schema-constrained output (tool-use or response_format).**
Force the AI to emit JSON matching a schema. q_codes become enum values; verse IDs become enum values from the catalogue. Drift becomes impossible at the structural level.

**Option 3 — Two-pass design: AI proposes, validator checks, AI repairs in one call.**
Run the design call. Validate output. If gaps, make a single repair call that gives the AI only the failed items and asks for a fix. This is what we ended up doing for M38, but ad-hoc. Formalising it as a loop reduces detection-to-fix latency.

**Option 4 — Failure log.**
Per-cluster `wa-cluster-{CODE}-failure-log-v1-{date}.md` records every failure with: phase, root cause, fix applied, cost, time lost. Aggregated review across clusters surfaces patterns.

### Recommendation

**Option 1 + Option 3 + Option 4 for now; Option 2 deferred.**

- Option 1 (volume budgeting) — implement in B.3 and D.A scripts immediately. Each script estimates expected output volume and either (a) sets max_tokens with headroom or (b) splits the work.
- Option 3 (formalised propose-validate-repair) — wrap each AI call in a standard loop: propose → validate → (if gaps) repair → (re-validate). Cap the loop at 2 repair iterations; if still failing, surface to researcher.
- Option 4 (failure log) — every script writes failures to the cluster failure log. Format: timestamp, phase, error type, what was tried, what worked.
- Option 2 (schema-constrained output) — deferred because the Anthropic API tool-use machinery is more complex to wire and the existing free-text+validate pattern already works. Revisit if drift remains a problem across 3+ clusters.

### What changes in v3_0 instruction

- Add §X.5 "Output volume budgeting" — every API call sized by expected output, with explicit max_tokens that include headroom.
- Add §X.6 "Propose-validate-repair loop" — the standard wrapper for analytical AI calls, with the 2-iteration cap.
- Add §X.7 "Failure log" — the per-cluster log file and what goes in it.

### What CC needs to build

- Volume-estimator helper: given input shape, estimates output token count.
- Standard propose-validate-repair wrapper (Python function used by every phase's API runner)
- Failure log writer
- Periodic cross-cluster failure analysis script — surfaces patterns ("B.2 coverage gap occurs in N/M clusters")

---

## (e) Phase E staging — holistic thinking before writing

### Observed problem

The M38 essay reads as sentence-by-sentence construction from the findings rather than integrated prose. The researcher's verdict from yesterday: "the AI took each sentence from the findings and tried to construct a sentence of it, often not finding itself into the holistic context."

The Session C chapter-by-chapter generator (which we just regenerated for M38) addresses this partly — each chapter is bounded, the per-chapter instructions are tight, and the per-chapter input contains only the evidence that chapter needs. But each chapter is still composed in isolation. The author doesn't see the other chapters; they don't form a model of what the cluster as a whole IS before writing chapter 4 about how the characteristics relate.

### Root cause

Prose writing has two layers:
1. **Compositional layer** — what argument am I making? what is the overall shape? what are the key moves?
2. **Sentence layer** — how do I write this paragraph?

The current Session C structure is excellent at layer 2 — clear instructions, bounded scope, evidence to hand. But it skips layer 1 entirely. Each chapter's author starts cold on the cluster, with only that chapter's evidence in view, and is asked to write competent prose. The result is competent sentences that don't add up to integrated argument.

Good essayists do layer 1 first. They read everything, form a mental model, decide on the dominant arc, identify the surprises and partition points, identify the strongest verses — then write.

### Options

**Option 1 — Cluster vision document as Phase E.0.**
Before Chapter 1 is written, run a "read the cluster" preliminary call that loads ALL findings (cluster-scope + per-characteristic at high level) and asks the AI to write a 500-word internal reflection: what is this cluster about, what's the dominant arc, what surprises me, what's the partition, what are the strongest verses. This is not published — it's a thinking document. Each chapter run then loads this vision document as additional context.

**Option 2 — Cross-chapter consistency pass.**
After all chapters written, the AI re-reads all chapters together and produces a list of edits per chapter: duplications, contradictions, voice drift, missing connecting argument. Authors apply the edits.

**Option 3 — Final integration pass.**
After all chapters written and consistency-edited, a final call reads the whole book and writes a closing chapter / observation that ties everything together. This is the only call with the whole book in context.

**Option 4 — One author, longer context.**
Skip the per-chapter atomisation. Hand the AI all findings + style instructions + chapter outline in one massive context, and ask for the whole book. Modern Claude models can handle this. Trade-off: harder to manage; the AI may produce uneven chapters; revision is harder when a single chapter needs work.

### Recommendation

**Option 1 + Option 2 + Option 3.** Option 4 is too risky for cluster-publication scale — when something goes wrong, isolating the cause is hard.

The new Phase E shape:

| Sub-phase | What it does | Output |
|---|---|---|
| **E.0 Vision** | AI reads all findings; writes 500-word internal "what this cluster is" | `wa-cluster-{CODE}-vision-v1-{date}.md` (not published) |
| **E.1 Chapters** | One run per chapter, loading: chapter input + chapter instruction + style instruction + **vision document** + any prior chapters already drafted (so chapter 4 can reference chapter 3's framing) | `wa-cluster-{CODE}-ch{N}-draft-v1-{date}.md` per chapter |
| **E.2 Consistency** | After all chapters drafted, single AI call reads them all and returns per-chapter edit list | `wa-cluster-{CODE}-consistency-edits-v1-{date}.md` |
| **E.3 Integration** | After consistency edits applied, single AI call reads the whole book and writes the closing observation | Appended to the last chapter |
| **E.4 Assembly** | CC assembles into single book MD + DOCX | `wa-cluster-{CODE}-published-v1-{date}.md` + `.docx` |

The key insight: **E.0 (vision) and E.2 (consistency) are the two missing pieces** that turn the current chapter-by-chapter approach from "competent sentences" into "integrated argument".

### What changes in v3_0 instruction

- Add Phase E sub-phasing (E.0 through E.4) — currently Phase E is monolithic in the instruction.
- Write the **Cluster Vision instruction** (a new short instruction doc) — what the AI does at E.0.
- Write the **Cross-chapter Consistency instruction** (another short doc) — what the AI does at E.2.
- Modify each chapter instruction (ch1–ch7) to declare: "load the cluster vision document as additional context. Do not duplicate its content in the prose; use it to know where this chapter sits in the whole argument."

### What CC needs to build

- Vision-document input generator (loads all findings, formats for E.0 call)
- Vision-document output validator (length, no jargon, contains the four required moves: dominant arc + partition + surprises + strongest verses)
- Consistency-pass input generator (loads all drafted chapters)
- Integration-pass input generator (loads the whole book + the vision document)

### Cost implication

E.0 vision call: ~$0.50 (large input, small output)
E.2 consistency call: ~$0.40 (large input — all chapters — moderate output)
E.3 integration: ~$0.30 (same input, smaller output)

Phase E cost moves from ~$0 (drafting in chat, currently) to ~$1.20 if all three are API. But if they're done in chat instead, $0. The recommendation is: **E.0 and E.2 in chat**, because the holistic thinking is the whole point and that's chat's strength. E.3 can be either. E.1 chapter authoring is in chat (per yesterday's verdict on CC-drafted prose).

---

## Cross-cutting: where the obslog fits

The obslog discipline saved yesterday is what binds the refinements together. Every phase script writes to the obslog. The dashboard reads from it. The URGENT line points at it. The failure log is a structured section within it. Audit results land in it.

The obslog file: `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-obslog-v1-{date}.md`

Sections:
- **Current state** — phase, gate type, action required (drives dashboard)
- **Timeline** — chronological log of every material action
- **Failures** — structured failure entries (drives failure analysis)
- **Audit** — per-phase hygiene results
- **Costs** — running cost ledger
- **Decisions** — judgment-gate decisions and rationale

CC reads the obslog at the start of every turn. Researcher opens it any time to see ground truth. It survives chat summarisation because it's a file.

---

## Phased rollout

These refinements are scoped so that **(c), (d), and (e)** can be tried on M36 immediately with light scripting effort. **(a) and (b)** require more building and can land on M36 or M25 depending on how much CC time is acceptable up-front.

| Refinement | Effort | Could land on M36? |
|---|---|---|
| (c) Per-phase hygiene + new anchor + verse-ref checks | 1 h CC time | yes |
| (d) Volume budgeting + propose-validate-repair + failure log | 2 h CC time | yes for failure log; volume budgeting needs touching each runner script |
| (e) E.0 vision + E.2 consistency (in chat, not built) | 0 h CC time | yes — just new instruction docs |
| (a) Dashboard file | 1 h CC time | yes |
| (a) Auto-advance through mechanical gates | 2 h CC time | partial; full coverage by M25 |
| (b) URGENT.md + VS Code notifications | 1 h CC time for URGENT.md; VS Code notifications need investigation | URGENT.md yes; notifications maybe |
| Obslog discipline (binds everything) | 2 h CC time + per-script writes | yes — start of M36 |

**Recommended minimum-viable refinement for M36:**
1. Obslog discipline at cluster start
2. Per-phase hygiene checks (the two new ones especially — anchor designation, verse-ref in finding_text)
3. Failure log
4. Phase E sub-phasing — E.0 vision + E.2 consistency in chat, not as new scripts
5. Dashboard file
6. URGENT.md

This trades ~4–5 hours of CC engineering today for substantial reductions in M36 wall clock and rework.

---

## Decisions needed from researcher

1. **Section (a):** Approve dashboard + auto-advance through mechanical/confirmation gates? Or stay manual at every gate?
2. **Section (b):** VS Code notification — try it, or URGENT.md only for now?
3. **Section (c):** Approve the per-phase hygiene checks listed in the table? Any to add or drop?
4. **Section (d):** Approve volume budgeting + propose-validate-repair + failure log? OK to defer schema-constrained output?
5. **Section (e):** Approve E.0 vision + E.2 consistency as new sub-phases? Both done in chat, not as scripts?
6. **Rollout:** Apply the minimum-viable refinement set to M36, or take a longer engineering day to land more?

---

## What is not in this discussion

- v3_0 instruction-doc edits themselves. Those happen after decisions land.
- Tooling for cross-cluster failure pattern analysis. That's a longer-term observability question.
- Whether to retire the v2_5 audit script and build a v3_0 successor. The v2_5 audit produced false positives on M38 (1747 completeness-gap items mostly script/data-model mismatch). A v3_0-aware audit would reduce noise but isn't urgent if M36 has per-phase hygiene checks.
- Re-doing M38 prose under the new staging. The M38 essay stands as-is unless the researcher wants it re-authored under E.0+E.1+E.2.

---

*End of refinement discussion. Awaiting researcher review and decisions before any v3_0 instruction-doc changes.*
