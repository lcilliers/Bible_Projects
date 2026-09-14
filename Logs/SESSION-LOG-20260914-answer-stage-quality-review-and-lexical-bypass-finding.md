# Session Log — 2026-09-14 (continued)

**Scope:** Continuation of today's earlier session (see
`SESSION-LOG-20260914-ib-observation-node-round-1692-approved-phantom-visualization.md` for the
#1691–1693/#1698/#1699 phase). This phase: resolved escalation #1696 (catalogue migration to
`iba.db`); built and ran a systematic answer-stage catalogue-quality review across T0/T1/T2/T4/T5/T6
(escalation #1700); surfaced and parked a deeper architectural critique — entity-as-subject vs.
process-as-subject (#1701); evaluated the 14 live cluster T-codes against catalogue-question
coverage (#1702); and, most significantly, confirmed by direct inspection of the actual M10
cluster-reading prototype that **no lexical enrichment data (role, `party_kind`, `is_negator`,
T-codes) ever reached the LLM at any pipeline stage** — the same root-cause failure diagnosed for
the original (pre-reset) study, now confirmed reproduced in the new pipeline. Session closes with
a researcher-set direction for the next session: fold the lexical process in so lexical questions
get answered and that data feeds subgroup-reading data preparation.

## 1. Escalations touched, by id, with outcome

| # | Outcome this session |
|---|---|
| **#1696** | Updated (v2→v4) — CSV export of the 98 migration-candidate catalogue rows delivered for researcher review; `finding_question_link` resolved as explicitly out of scope (superseded by `ib_node`, researcher's own words). Every §4 item now resolved. Still `in-progress`/`review`, awaiting the researcher's CSV review before joining the sign-off pack. |
| **#1700** | Raised, then updated repeatedly (v1→v8) — full answer-stage catalogue-quality review. T0/T1/T2/T4/T5/T6 read in depth (T0 full-question 5-sample; T1/T2/T4/T5/T6 5-sample per question; select T4/T3 questions read in full, not sampled). Findings: T3 (Inner Faculties, all 33 questions) confirmed as a genuinely failed category, concretely — not just per the researcher's own prior retirement verdict but shown *why* in the actual answer text (forced near-universal "yes," faculty-boundary bleed, one honest exception pattern). T0/T1/T2/T4/T5 substantiated throughout, no genericity. T6 substantiated but with a distinctly higher source-data-gap rate and one new failure category ("process-note-as-answer"). Confirmed catalogue-wide that the entire 2026-09-04 mechanical/interpretive split initiative (10 of 11 affected question codes) is unexercised. Final, most consequential addition this session: confirmed via the actual M10 prototype files that none of this review's findings benefited from any lexical enrichment reaching the LLM — folded into #1607 as the primary record. |
| **#1701** | Raised, then updated (v1→v2) — entity-as-subject vs. process-as-subject architectural critique: even the catalogue's relationship-aware tiers (T4, T6) still frame the characteristic as the fixed subject, never the movement/process itself. Researcher confirmed and sharpened this as a "major oversight." Explicitly parked for a future session, not designed now. |
| **#1702** | Raised — evaluated all 14 live cluster T-codes (T2–T15) against catalogue-question coverage, distinct from both the Verse Reading Technique (T1–T9) and Tier Catalogue (T0–T7) "T" schemes. Found T7/T8/T4/T9 already mechanically wired via live `party_kind` to specific catalogue questions (confirmed by the researcher's own design intent); found `T4.6.2a`/`T4.6.3a` correspond exactly to T4/T9 tags but have never actually been run against them; found the `role` redesign (the general mechanism for surfacing T-codes to Layer 2) is still unbuilt; found T6/T14 have real question homes but no lexicon-assist column; found T3 (Operations) is the deepest gap, connecting directly to #1701. Still `raised`/`review`. |
| **#1606** | Updated (v9→v10) — light cross-reference only: the newly-confirmed "allocation exists but never reaches the LLM" gap is distinct from this escalation's own Leg 3 (strongs with zero allocation at all). No state change in substance; Leg 3 remains the researcher's own call to schedule. |
| **#1607** | Updated repeatedly (v12→v14) — the session's most important thread. Recorded, with direct evidence (not inference), that the M10 cluster-reading prototype's process (a)/(c)/(d) never passed `role`/`party_kind`/`is_negator`/any T-code data to the LLM at any stage; the LLM re-derived party identity for the T4 relational questions purely from English verse-text reading. Spot-checked one instance (H_guilt's T4.6 "no adversarial/angelic being" answer) against the real live T4/T9 tags — confirmed correct, but the researcher correctly identified this as a coincidence of one family's low base rate, not evidence the gap is safe generally, and connected it directly to the same root-cause diagnosis that closed the original study. Session closes with the researcher's own direction recorded as this escalation's confirmed next step: fold in the lexical process so lexical questions get answered, then feed that data into subgroup-reading data preparation. Still `in-progress`/`review` — this is where the next session should start. |

## 2. Files created or changed

- `iba/docs/1696-obs-catalogue-migration-to-iba-v1-20260913.md` — §4/§5 fully resolved (deletion filter, inactive-marking scope, `finding_question_link` out of scope).
- `iba/docs/1696-catalogue-migration-candidate-rows-v1-20260914.csv` — new. Full-field export of the 98 live-qualifying catalogue rows.
- `iba/docs/1693-table-update-procedure-finalization-v1-20260912.md` — minor touch-up (no substantive content change this phase beyond what was already finalized).
- `iba/docs/1700-per-question-answer-quality-review-v1-20260914.md` — new, running doc (edited in place across the session): T0/T1/T2/T4/T5/T6 sections, the confirmed 2026-09-04 split-unexercised cross-cutting finding.
- `iba/docs/1700-sample-answers-tool-v1-20260914.py` — new. Reusable seeded-sample extraction tool for the per-question review method.
- `iba/docs/1700-sample-t0/t1/t2/t4/t5/t6-v1-20260914.json` — new. Sample data per section.
- `iba/docs/1700-t*-full-answers-v1-20260914.json` (T4.1.1, T4.2.1, T4.3.1, T4.3.4, T4.4.1, T4.5.1, T4.6.1, T3.1.1, T3.1.2, T3.1.3, T1.4.1-old) — new. Full (not sampled) answer sets read in depth.
- `iba/docs/1700-t3-inner-faculties-failure-analysis-v1-20260914.md` — new. Full account of T3's confirmed failure mode, evidenced from the actual answer text.
- `iba/docs/1700-t4-relational-interfaces-statistical-analysis-v1-20260914.md` + 2 accompanying JSON stat files — new (from earlier in this same calendar session, referenced/built on here).
- `iba/docs/1700-answer-drift-findings-by-section/` — 27 per-section JSON files + manifest (from earlier in this session, the original #1700 export).
- `iba/docs/1702-tcode-question-coverage-evaluation-v1-20260914.md` — new. Full T-code coverage evaluation.
- `outputs/escalation/` — various regenerated escalation-list and per-id history reports (normal report rotation, prior versions archived).

## 3. Decisions made

**Researcher's own decisions (not self-correctable):**
- `finding_question_link` is out of scope for #1696 entirely — replaced by `ib_node`, its own retirement is a separate, later question.
- The T3.1.1/T3-family analysis confirms (with concrete textual evidence) the researcher's own prior retirement verdict for T3 (Inner Faculties, #1598) — not a new decision, but the researcher explicitly asked for and got the "why," not just the "that."
- The entity-vs-process architectural critique (#1701) is confirmed as real and significant ("a major oversight"), explicitly parked rather than designed now.
- The T-code / `role` mechanism gap (#1702) and its concrete manifestation in the M10 prototype (#1607) are both confirmed as real, not resolved.
- **Central correction this session, researcher's own words:** the "no material impact" framing I gave after spot-checking one instance was wrong — a single correct answer in a low-base-rate family is not evidence the underlying gap (lexical enrichment never reaching the LLM) is safe. This is the same failure mode that closed the original study, now confirmed reproduced.
- Session-closing direction: fold in the lexical process — answer the lexical questions, then feed that data into subgroup-reading data preparation — as the concrete next step, recorded on #1607.

**Self-correctable (fixed directly, not escalated):**
- None this phase — all substantive findings were judgment calls or confirmations, recorded via escalation update rather than silently resolved.

## 4. Open items carried into next session

- **#1607 is the priority entry point** — fold the lexical process in: get lexical questions answered, then include that data in subgroup-reading data preparation. This supersedes continuing #1700/#1701/#1702's own exploratory threads as the immediate next step.
- **#1700**: T7 and the five non-tier sections (Extensions, Section 1–5, leviticus, redemption) not yet reviewed.
- **#1701**: entity-vs-process architecture — explicitly parked, no design started.
- **#1702**: T10–T13 (Places/Corporate/Objects/Natural-World) — genuinely open whether they need dedicated questions once `role` exists.
- **#1606 Leg 3**: 111 live strongs with zero cluster allocation — researcher's own call on timing, unchanged this session.
- **#1696**: awaiting the researcher's review of the 98-row CSV before joining the sign-off pack.
- **Sign-off pack status unchanged this phase**: #1690/#1692/#1693 approved; #1691/#1696/#1697 still open.

## 5. Git state

- Branch: `main`
- Commit: `7907a9e5` — "session 20260914 (cont.): catalogue answer-quality review (#1700), T-code coverage eval (#1702), architecture critique parked (#1701), migration plan finalized (#1696), lexical-bypass finding recorded on #1607" (63 files changed)
- Push: confirmed — `f1909c12..7907a9e5 main -> main`; `git status` clean after push.
