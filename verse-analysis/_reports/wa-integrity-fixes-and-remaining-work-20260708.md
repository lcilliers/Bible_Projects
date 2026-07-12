# Integrity fixes done + honest remaining-work list — 2026-07-08

> What was fixed today after the "82% of verse-records unmapped" discovery, and what genuinely remains. Written so tomorrow starts from facts, not re-discovery.

## Fixed today (integrity)
| item | before | after |
|---|---|---|
| **Verse-record → master linkage (OT)** | ~40% | **91.5%** (52,277 of 57,136) |
| ve_lexical → master linkage | — | 99.99% (511,527 of 511,849; 47 active unlinked, Leviticus, legacy-anchored) |
| Seed false positives | 963 candidate lemmas | 949 (14 homographs pruned; hard-exclude persisted) |

Mechanism (all no-new-data, integrity-gated, backed up):
- Whole-OT deterministic link repair: **38,382** records linked by 1-span match.
- Second pass via `target_word`: **+1,267** linked.
- Ambiguous (same-strong-repeats): **2,088** flagged `SPAN_UNRESOLVED` (resolved at read, never guessed).
- Genuine gaps flagged/tracked: **2,527** `STRONG_NOT_IN_MASTER` (record strong ≠ verse morphology), **225** `VERSE_NOT_IN_MASTER` (verse never ingested — e.g. Chronicles has gaps).

## Key facts established today
- The apparent "24k missing characteristics" was **≈74% already-in-DB-but-unlinked**, not STEP holes. Onboarding them would have created duplicates — averted.
- The integrity-controls suite measures **legacy verse_context invariants** (`velex_orphan_vc=415,130`); under the new **master-linked** model these are stale-field artifacts, not breaches. The real integrity signal is `verse_span_id` linkage (now fixed).
- The verse master itself is **incomplete** for un-read books (Chronicles etc.) — verses simply aren't ingested. Real, but a separate ingestion job.

## Remaining work (honest, prioritised) — needs researcher input, NOT auto-run
1. **Genuine onboarding holes: ~4,908 spans / ~210 new terms** (`char_candidate` with no record *at all*). This is the real (b). **Review the 210 new-term list before registering** (some seed IB-judgements are weak). Worklist: `research/investigations/audit-word-onboarding-worklist-20260708.md`.
2. **`STRONG_NOT_IN_MASTER` (2,527)** — record strong disagrees with morphology (some look like corrupt `target_word`/strong). Needs per-case review; not auto-fixable.
3. **`VERSE_NOT_IN_MASTER` (225)** — ingest the missing verses (morphology pull) for those references, or accept the master is IB-scoped only.
4. **Passage reconciliation** — 1,051 `char_candidate` verses have no passage; widen the passage rule's scope to `char_candidate` (per decision (e): tight around characteristics that anchor to verse-records; no large char-free passages). Passage = Stage 0 before reading.
5. ~~**Instruction completion**~~ — **✅ DONE 2026-07-08.** Cycle instruction finalised: **§4A Stage 0** (passage prerequisite, candidate-driven), **§7A** (DB-updates/index-maintenance + the **candidate⇒verse-record integrity invariant**), **§7B** (transition, `role_provenance='read-2026'`; Psalms + Prov 1-6 first). Passage rule bumped to **v2** (candidate-scoped; v1 superseded). Decisions 1–3 resolved (see `wa-cycle-db-updates-indexes-transition-passage-analysis-20260708.md` header). **Key ruling:** a `char_candidate` span with no verse-record is a **DB integrity violation** — repair the verse-record + relations before reading (this ties items 1–3 above into the read as an integrity gate, not optional backlog).

## Reference docs produced
- `wa-verse-passage-lexical-master-term-record-linkage-map-20260708.md` — the full linkage architecture.
- `wa-cycle-db-updates-indexes-transition-passage-analysis-20260708.md` — the DB-update/index/transition/passage analysis + decisions.
- `research/investigations/audit-word-onboarding-worklist-20260708.md` — the onboarding worklist (b+c).

*Filed 2026-07-08. All writes backed up. Reading has NOT started — substrate work continues.*
