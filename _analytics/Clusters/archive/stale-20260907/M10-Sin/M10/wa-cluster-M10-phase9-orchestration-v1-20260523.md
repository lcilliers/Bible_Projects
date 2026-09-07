# M10 Phase 9 — Orchestration overview

**Date:** 2026-05-23
**Cluster:** M10 — Sin, Guilt and Transgression (post-split, post-Phase-5-revision)
**Audience:** Researcher (Leroux) — to plan AI-session sequencing; AI sessions read their own per-characteristic briefs
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §12

---

## What's special about M10's Phase 9

M10 has **22 characteristics + 1 cluster-synthesis session = 23 AI sessions** total. That's nearly four times M09 (which had 6 + 1 = 7). The volume is real and uneven:

| Tier (verse volume) | Characteristics | Count |
|---|---|---:|
| Large (>100V) | CHAR-11 (112V), CHAR-13 (205V), CHAR-18 (162V), CHAR-19 (147V), CHAR-20 (101V) | 5 |
| Medium (60–100V) | CHAR-1 (98V), CHAR-16 (64V), CHAR-17 (97V), CHAR-21 (64V), CHAR-22 (72V) | 5 |
| Small (10–50V) | CHAR-2 (18V), CHAR-3 (34V), CHAR-5 (18V), CHAR-6 (14V), CHAR-7 (19V), CHAR-9 (22V), CHAR-14 (34V) | 7 |
| Tiny (<10V) | CHAR-4 (8V), CHAR-8 (9V), CHAR-10 (5V), CHAR-12 (9V), CHAR-15 (8V) | 5 |
| **Total** | | **22** |
| Cluster synthesis | runs LAST, after all 22 characteristic findings exist | 1 |

The per-characteristic AI work (189 prompts × T0–T7) is the same regardless of verse volume — but the *evidence load* the AI has to read is what changes. The 205-verse CHAR-13 (Sin as divine record) is a heavier reading load than 8-verse CHAR-4 (Conscience suppression), even though both produce 189 findings.

---

## The discipline that must hold — non-negotiable

This restates what every per-character brief mandates. The orchestration view exists to make sure the discipline is enforced at session-planning level, not just at AI-prompt level.

### One characteristic per AI session

Don't ever start CHAR-N+1 in the same session as CHAR-N. Even if CHAR-N was small. Each characteristic is its own staged execution; carrying the previous characteristic's analytical lens into the next one is exactly the M04 / M07 / M08-CHAR-1 drift pattern memorised at `feedback_phase9_tier_by_tier_mandatory`. Open a fresh session, point the AI at the next brief, start fresh.

### Within a session: one tier per response (or fewer if drift surfaces)

Each per-character brief has the full tier-by-tier mandate baked in:

- T0 (12 prompts) → write to disk → self-evaluate
- T1 (24 prompts) → re-read evidence fresh → write to disk → self-evaluate
- T2 (31), T3 (33), T4 (24), T5 (21), T6 (24), T7 (20) — same pattern

If the AI says *"OK, also let me start T1"* in the same response as T0 — that's fine when both pass self-evaluation cleanly. **But if T0's self-evaluation surfaces an ALERT, the AI must STOP** — not push through. The brief specifies exactly how the AI announces this.

If the AI is showing signs of skimping (uncited E findings, repeated openings, claims like "see T7" before T7 exists), the session pauses. CC validates, and if needed the session restarts that tier.

### Write-out discipline — non-negotiable

Per §10.7 / §12 discipline: the file write is the engagement artefact. Each tier must be **written to disk** before the next tier begins. The AI's brief mandates this. From your side, the verification is mechanical — after each tier the AI claims is done, the corresponding tier section must exist in the findings file.

If you see the AI producing tier content only in chat without confirming the file write, **interrupt and require the disk write**. This was a real failure mode in earlier clusters and is the precise issue the §10.7 mandate addresses.

---

## Sizing the work — what to expect per session

| Session size | Wall-clock estimate | Token cost approx |
|---|---|---|
| Tiny characteristic (5–18V) | 1 session, 4–8 responses (sometimes T0–T7 all chains cleanly) | low |
| Small (19–50V) | 1 session, 6–10 responses | low–medium |
| Medium (51–100V) | 1 session, 8–14 responses | medium |
| Large (101–162V) | 1 session, 10–18 responses, often needs to split mid-tier sequence | medium–high |
| Very large (205V — CHAR-13) | 1–2 sessions; CHAR-13 may need to split T-boundaries across two sessions if a single session runs long | high |

**The largest single-VCG inside CHAR-13** is M10-V-VCG-05 at 113 verses (8.5% of cluster) — within CHAR-13's 205V scope. The AI re-reads the verse evidence per tier; for CHAR-13 expect each tier-open to be a substantial read. If a session feels strained mid-tier, the AI should stop at the next tier boundary and the next session resumes at the next tier.

---

## Suggested execution order

Two patterns work; pick by preference:

### Pattern A — smallest first, build confidence (recommended)

Process tiny → small → medium → large → cluster synthesis. The AI session pattern is well-rehearsed before the heavy lifts.

1. **Tiny tier (5 sessions):** CHAR-4, CHAR-8, CHAR-10, CHAR-12, CHAR-15
2. **Small tier (7 sessions):** CHAR-2, CHAR-3, CHAR-5, CHAR-6, CHAR-7, CHAR-9, CHAR-14
3. **Medium tier (5 sessions):** CHAR-1, CHAR-16, CHAR-17, CHAR-21, CHAR-22
4. **Large tier (5 sessions):** CHAR-11, CHAR-13, CHAR-18, CHAR-19, CHAR-20
5. **Cluster synthesis (1 session):** runs LAST, after all 22 characteristic findings exist

### Pattern B — characteristic groupings by theme

Process by semantic cluster — e.g. all the sin-as-act characteristics, then sin-as-state, then guilt-and-confession, then perversion/injustice. Allows the researcher to keep a coherent picture during review, but doesn't pace the AI work as ergonomically.

I'd recommend **Pattern A** — smaller sessions first, big sessions when the discipline is grooved.

---

## What CC does between sessions

1. **Validate the findings file** for the just-completed characteristic:
   - File exists at expected path
   - All 8 tier sections present (`## T0` through `## T7`)
   - Self-check block at end
   - Prompt count = 189 (T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20)
   - Every `[CHAR-N]` marker = N (the characteristic's seq)
   - Citation discipline: every E finding cites at least one verse-reference or VCG code
2. **Update the orchestration tracker** below to ✓ that characteristic
3. **Update CC's view of the cluster** — observations addressed (carry-forward observations marked confirmed/refined as the AI surfaced them)

CC's per-characteristic validation script will be `scripts/_validate_m10_phase9_findings_v1_20260523.py` (built when the first findings file lands).

---

## After all 22 characteristic findings exist

Run the cluster synthesis builder again to **re-collate the 189-prompt matrix** with per-characteristic findings stacked beneath each prompt:

```
python scripts/_build_m10_phase9_cluster_synthesis_20260523.py
```

(The first run produced empty stacks because no characteristic findings existed yet — it'll need to re-run before the cluster-synthesis session.)

Then open the cluster-synthesis brief + input (already generated, will re-fill with findings) in a fresh AI session. The synthesis is the 23rd Phase 9 session and uses the same tier-by-tier discipline.

---

## Per-characteristic tracker

Mark ✓ as each characteristic's findings file is validated by CC.

### Tiny (5–18V) — recommended first

| Seq | Characteristic | Verses | Brief | Status |
|---:|---|---:|---|---|
| 4 | Conscience suppression | 8 | [char4-brief](wa-cluster-M10-phase9-char4-Conscience-suppression-brief-v1-20260523.md) | ✅ |
| 8 | Political revolt | 9 | [char8-brief](wa-cluster-M10-phase9-char8-Political-revolt-brief-v1-20260523.md) | ✅ |
| 10 | Specialised sinful mechanisms | 5 | [char10-brief](wa-cluster-M10-phase9-char10-Specialised-sinful-mechanisms-brief-v1-20260523.md) | ✅ |
| 12 | Sin as enslaving power | 9 | [char12-brief](wa-cluster-M10-phase9-char12-Sin-as-enslaving-power-brief-v1-20260523.md) | ✅ |
| 15 | Generational sin | 8 | [char15-brief](wa-cluster-M10-phase9-char15-Generational-sin-brief-v1-20260523.md) | ✅ |

### Small (19–50V)

| Seq | Characteristic | Verses | Brief | Status |
|---:|---|---:|---|---|
| 2 | Unintentional sinning | 18 | [char2-brief](wa-cluster-M10-phase9-char2-Unintentional-sinning-brief-v1-20260523.md) | ✅ |
| 3 | Confession | 34 | [char3-brief](wa-cluster-M10-phase9-char3-Confession-brief-v1-20260523.md) | ✅ |
| 5 | Refusal to repent | 18 | [char5-brief](wa-cluster-M10-phase9-char5-Refusal-to-repent-brief-v1-20260523.md) | ✅ |
| 6 | Habitual defection | 14 | [char6-brief](wa-cluster-M10-phase9-char6-Habitual-defection-brief-v1-20260523.md) | ✅ |
| 7 | Contagious sin | 19 | [char7-brief](wa-cluster-M10-phase9-char7-Contagious-sin-brief-v1-20260523.md) | ✅ |
| 9 | Sinful speech | 22 | [char9-brief](wa-cluster-M10-phase9-char9-Sinful-speech-brief-v1-20260523.md) | ✅ |
| 14 | Forgiveness sought and received | 34 | [char14-brief](wa-cluster-M10-phase9-char14-Forgiveness-sought-and-received-brief-v1-20260523.md) | ✅|

### Medium (51–100V)

| Seq | Characteristic | Verses | Brief | Status |
|---:|---|---:|---|---|
| 1 | Wilful sinning | 98 | [char1-brief](wa-cluster-M10-phase9-char1-Wilful-sinning-brief-v1-20260523.md) | ✅ |
| 16 | The sinner as moral character | 64 | [char16-brief](wa-cluster-M10-phase9-char16-The-sinner-as-moral-character-brief-v1-20260523.md) | ✅ |
| 17 | Guilt as inner-being state | 97 | [char17-brief](wa-cluster-M10-phase9-char17-Guilt-as-inner-being-state-brief-v1-20260523.md) | ✅  |
| 21 | Perversion as inner inversion | 64 | [char21-brief](wa-cluster-M10-phase9-char21-Perversion-as-inner-inversion-brief-v1-20260523.md) | ✅ |
| 22 | Injustice as moral failure of right conduct | 72 | [char22-brief](wa-cluster-M10-phase9-char22-Injustice-as-moral-failure-of-right-conduct-brief-v1-20260523.md) | ✅ |

### Large (101–162V)

| Seq | Characteristic | Verses | Brief | Status |
|---:|---|---:|---|---|
| 11 | Sin as universal condition | 112 | [char11-brief](wa-cluster-M10-phase9-char11-Sin-as-universal-condition-brief-v1-20260523.md) | ✅ |
| 18 | Iniquity as accumulated moral crime | 162 | [char18-brief](wa-cluster-M10-phase9-char18-Iniquity-as-accumulated-moral-crime-brief-v1-20260523.md) | ✅ |
| 19 | Transgression as deliberate boundary-crossing | 147 | [char19-brief](wa-cluster-M10-phase9-char19-Transgression-as-deliberate-boundary-crossing-brief-v1-20260523.md) | ✅ |
| 20 | Faithlessness as covenant-breaking sin | 101 | [char20-brief](wa-cluster-M10-phase9-char20-Faithlessness-as-covenant-breaking-sin-brief-v1-20260523.md) | ✅ |

### Very large (>200V)

| Seq | Characteristic | Verses | Brief | Status |
|---:|---|---:|---|---|
| 13 | Sin as divine record | **205** | [char13-brief](wa-cluster-M10-phase9-char13-Sin-as-divine-record-brief-v1-20260523.md) | ✅ |

### Cluster synthesis (final)

| | Phase | Verses scope | Brief | Status |
|---|---|---:|---|---|
| | Cluster synthesis | 1320 (whole cluster) | [synthesis-brief](wa-cluster-M10-phase9-cluster-synthesis-brief-v1-20260523.md) | ☐ |

---

## Drift signals to watch (interrupt and restart that tier if seen)

These are the M04 / M07 / M08 failure patterns memorised at `feedback_phase9_tier_by_tier_mandatory`:

1. **Uncited E findings.** The AI calls a finding `E` but doesn't name a verse / VCG / sub-group. Symptom of fluency-without-grounding. **Interrupt and restart that tier.**
2. **Repeated openings.** Two prompts in a tier start with the same 80-character phrase. Symptom of bulk-classification rather than per-prompt analysis. **Interrupt and restart that tier.**
3. **Cross-tier references before they exist.** The AI says "see T7" in a T2 finding. Symptom of working-memory contamination. **Interrupt and restart that tier.**
4. **Skipped prompts.** A tier is announced complete but the prompt count doesn't match (T0=12, T1=24, etc.). Symptom of "I'll come back to that later" mid-tier. **Interrupt and restart that tier.**
5. **Wrong scope marker.** The AI uses `[CHAR-3]` in CHAR-1's findings file. Symptom of carryover from a prior session. **Interrupt and re-mark.**
6. **No file write between tiers.** The AI produces multiple tiers in chat without confirming each is on disk. Symptom of write-out discipline failure. **Interrupt and require the disk write before continuing.**

---

## What "too much in a session" looks like

The AI brief allows tiers to chain in one response *when self-evaluation passes cleanly*. That's intentional — the discipline is *write each tier* and *self-evaluate*, not *one response per tier rigidly*.

But there's a soft limit: when a response approaches ~10k tokens of output, the AI's working-memory ceiling is being approached. Signals of approach:

- Pass A meaning excerpts in citations getting shorter and shorter (the AI is compressing)
- Sentences in findings getting more generic ("This evidences sin's universality" vs "Cain bears unbearable iniquity weight per Gen 4:13's `nasa avoni mi-neso`")
- Self-evaluation getting terser (checks reduced from explicit ✓/FAIL to single-line "all PASS")

When these signals appear: **the AI should stop at the next tier boundary** (announce *"...PASS. Pausing here; tier T{N+1} continues in the next response."*). The brief explicitly permits this.

---

*This orchestration document is the index. The per-characteristic briefs carry the discipline. The cluster-synthesis session runs last.*
