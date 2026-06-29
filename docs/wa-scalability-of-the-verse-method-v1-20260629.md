# Scalability of the verse-fanout method — the lifetime problem

- **File:** docs/wa-scalability-of-the-verse-method-v1-20260629.md · 2026-06-29 · living strategy doc.
- **Trigger (researcher):** *"the review method was effective — I reviewed and read every verse and found loads of corrective actions — but it is not scaleable to think I will finish this study in my lifetime."*

## 1. The problem, stated honestly
The quality of this study comes from the researcher **reading every verse and correcting**. That is also the bottleneck. This session spent itself on **one focus verse (Exo 1:13) + ~10 fan-out verses**. The corpus is **~23,593 verses**. At this rate the study is, literally, not finishable. The method is *right*; the *throughput* is wrong.

## 2. Why the human had to read everything — the diagnosis
The human review was necessary because the **AI generation was error-prone**, and the errors were invisible without reading the verse. But the corrections this session were **not random** — they fell into a small set of *teachable* types:

| type | examples this session | nature |
|---|---|---|
| **Imported / not verse-founded** | cruelty=genus/ruthlessness=species; #43/#44 "sources of cruelty" pinned to Exo 1:13; #59 "morally neutral" | AI reached beyond the verse (lexical/English/cluster associations) |
| **Mis-filed** | #50/#51/#106 cruelty statements filed under ruthlessness | AI conflated adjacent operations |
| **Unsupported inference** | #45 severed-memory → ruthlessness (not in Exo 1:8) | AI asserted a causal jump the verse doesn't make |
| **Missing detail** | #47 references not listed | presentation |
| **Data / process gaps** | ve-lexical not built, out-of-corpus refs, delete_flagged NULL | pipeline, not judgement |

**The insight:** the human corrections were *teaching the AI the verse-founding discipline*. Types 1–3 are the same rule, broken three ways: **capture only what the verse states; mark anything cross-verse or lexical as inference; file by the term's own operation.** Type 5 is fixed by controls (mostly done). If the AI *internalises* the discipline, the per-verse error rate collapses — and the human stops being the exhaustive reader.

## 3. The lever — change the human's role, not their diligence
Scale comes from moving the human **off "read every verse"** and onto the three places human judgement is *decisive*:
- **Discipline-setter** — owns the rules (the very corrections made this session).
- **Auditor** — spot-checks a sample; watches the controls.
- **Adjudicator** — rules on the cases the machine flags as *disputed* (not all cases).
- **Synthesiser** — owns the focus-point / findings narrative (the part that is genuinely the researcher's).

The machine must become **trustworthy enough that review = sampling + adjudication, not exhaustive reading.** Everything below serves that.

## 4. The pipeline (generate → adversarially verify → human adjudicates exceptions)
1. **Encode the discipline into generation.** Turn this session's corrections into the generation spec (they are already the memories: verse-bounded, no import, flag inferences, file by operation). The generator/reader applies them up front.
2. **Automated quality gates** (extend `_check_integrity_controls`): flag — out-of-corpus refs (done); observations whose evidence cites verses *other than* their origin (possible import / cross-stream); observations whose anchor-term cluster ≠ the stream (mis-file). These pre-filter so the human never sees the clean ones.
3. **Adversarial verification** (the key quality move). For each proposed observation, an **independent verifier pass tries to refute it**: *is this stated in the verse? is it imported? is it the right operation?* — exactly what the researcher did by hand. Only survivors are captured `resolved`; the rest are flagged **needs-adjudication**.
4. **Parallelism.** Run many verses through generate→verify **concurrently** (multi-agent orchestration). This is where the throughput comes from. *(Requires the researcher's explicit opt-in — it is a billed, scaled operation.)*
5. **Human reviews the OUTPUT** — the verified observations (sampled) + the flagged disputes (all) — not the raw generation, and not every verse.

## 5. Prioritise the corpus (don't process all 23k blind)
The earlier coverage audit already showed most never-pulled verses yield **~0 new inner-being content**. So **triage first**: which verses actually carry an IB operation? Process the IB-dense set; give the rest a cheap mechanical pass. This alone removes most of the 23k from the hand-review path.

## 6. The pilot — prove it before betting the study on it
Take **one batch (10–20 IB-dense verses)**. Run the encoded-discipline + automated-gates + adversarial-verify pipeline. Then the researcher **spot-reviews 2–3** and we **measure**:
- **Residual error rate** — how many corrective actions does the human still find? (target: few, and only genuine judgement calls)
- **Human time per verse** — must drop from "read+correct everything" to "adjudicate exceptions."
If the residual error is low, it scales. If it is still high, the discipline-encoding needs another iteration *before* scaling — better to learn that on 20 verses than 20,000.

## 7. The honest tension + the decisions for you
- **The bet:** that *encoded discipline + adversarial AI verification + automated gates* can hold the quality bar that *your* per-verse reading set. The pilot tests exactly this; it is falsifiable on a small batch.
- **What stays yours regardless:** the discipline, the adjudication of hard cases, and the focus-point synthesis. The machine never owns the meaning.
- **Decisions:**
  - **D-scale-1** — adopt the *generate → verify → adjudicate-exceptions* model (human off exhaustive reading)?
  - **D-scale-2** — run the **pilot** on one IB-dense batch to measure the residual error rate? *(needs opt-in for multi-agent orchestration.)*
  - **D-scale-3** — build the **corpus triage** (IB-dense vs the rest) so we only fan out where there is something to find?

## 8. Researcher objections (2026-06-29) — the proposal is NOT accepted as-is
The researcher rejected the optimism of §4. The objections are largely correct and must reshape any plan:
1. **Fanout completeness is unproven.** The fanout is not demonstrably *complete* or *representative*, so it is not a solid enough grounding for observations. (Consistent with the earlier finding: the term cascade is an *index, not a census*.) We cannot currently prove a fanout has captured the relevant evidence.
2. **AI cannot reliably SELECT the right elements** of the fanout to turn into observations. The judgement of *what matters* is the hard part, and this session is the evidence against AI doing it unaided.
3. **The hardest + most valuable work is reading for what is NOT there** — absences, gaps, unsupported jumps, missing dimensions. *These discoveries were the most prevalent this session.* Adversarial *AI-verifies-AI* (§4.3) does **not** solve this: two AIs share the blind spot — both confirm a plausible-but-imported claim; neither asks "is this even in the verse?" **This is the decisive weakness of the §4 bet.**
4. **Most of the 24h work is in documents, not the DB** — text-based, and it **goes stale rapidly** (observations-v2 lost #109/#110; worklists drift). The canonical intellectual record is thin; the rich reasoning rots in markdown.
5. **Error-handling derails the assistant.** Discovering/fixing data errors mid-task repeatedly broke the assistant's focus ("you lose your track time and time again").

### What this forces (honest re-framing — to discuss, not yet a plan)
- **Two kinds of "absence" — only one is automatable.** (a) *Mechanical* absences — untracked terms, out-of-corpus refs, missing ve-lexical, coverage gaps — **were caught by the controls/puller this session** (the scalable part, proven). (b) *Judgement* absences — is the connection verse-founded? is the claim supported? is a dimension missing? — are **human and do not scale by AI verification.** AI's honest role shrinks to: mechanical substrate + detectable-gap controls + drafting + keeping the record solid. Selection, completeness-judgement, absence-finding, synthesis stay **human**.
- **The record problem is the most fixable** and should come first: capture the *work* (decisions, corrections, rationale) as **structured DB records**, with docs **generated** — so nothing the researcher does rots in text.
- **The goal may be wrong, not just the throughput.** The RESET method is about *emergent focus points*, not an exhaustive verse catalogue. "Finish every verse" may be both infeasible *and* unnecessary; "build the focus points from the IB-dense core, solidly grounded" may be the achievable end. Completeness then means *enough representative evidence per focus point*, not every verse.

## Decision log
- 2026-06-29 — raised by researcher (lifetime concern). Proposal §4 drafted.
- 2026-06-29 — **researcher rejected §4's optimism** (objections §8): fanout completeness unproven; AI can't select; AI can't find absences (the most valuable work); work rots in docs not DB; error-handling derails the assistant. The AI-verifies-AI lever is the decisive weakness. Re-framing toward: AI = toil + mechanical-gap controls + solid record only; human owns judgement; goal = focus points from the IB-dense core, not every verse. No plan adopted; awaiting researcher direction.
