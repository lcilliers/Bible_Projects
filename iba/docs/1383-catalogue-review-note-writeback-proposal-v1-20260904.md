# Proposed `review_note` content — Stage-1 field-mapping writeback

**Escalation:** #1383. **Source:** every entry is the field-mapping document's own text
(`1383-verse-lexical-stage1-catalogue-field-mapping-v1-20260903.md`), condensed to one line per
question — nothing new derived here, this is transcription for the write, not re-analysis.
**Mechanism:** `obs_catalogue.update`, one `-Set '{"review_note": "..."}'` call per `obs_id`, per
the tool's own no-bulk-sweep discipline. **Not yet written** — proposed for your confirmation first.

| question_code | proposed `review_note` |
|---|---|
| T7.2.2 | Stage 1 — directly answered by `passage.genre` (set once per passage, at the read's own first move). |
| T1.4.1 | Stage 1 (half) — grammatical/stem form directly answered by `verse_lexical.morph_code`. |
| T0.1.1 | Stage 1 — derived: follow the characteristic-term's `entity_link` note to its target `verse_lexical` row, read `party_kind` (`divine`→yes, `human`→no, unresolved→`unresolved`, never guessed). Mechanical once the divine-name lexicon is wired into `party_kind` at build time. |
| T4.1.1 | Stage 1 — derived: same party_kind join as T0.1.1, both directions — subject `party_kind='divine' AND` object `party_kind='human'`. |
| T4.2.1 | Stage 1 — derived: same mechanism as T4.1.1, reversed direction. |
| T0.1.2 | Stage 1 (raw-fact half only) — aggregation of the T0.1.1 derivation across every verse in the characteristic-candidate's assembled set (`COUNT(...WHERE party_kind='divine')>0`). Interpretive half is Stage 2, T0.2.1-class — NOT this field. |
| T4.3.1 | Stage 1 — same mechanism as T4.1.1/T4.2.1, needs the human-name lexicon (`cfg_lexical_code_class`, class `party_human`) — **not yet built**, not answerable in practice yet. |
| T4.4.1 | Same status as T4.3.1 — mechanism designed, human-name lexicon not yet built. |
| T4.6.1 | Same mechanism, needs the angelic/adversarial-name lexicon (`party_angelic`) — **not yet built**, not answerable in practice yet. |
| T4.6.2 | Mechanical half needs the same angelic/adversarial lexicon as T4.6.1 (not yet built); interpretive half is Stage 2. Candidate split: T4.6.2a (mechanical)/T4.6.2b (interpretive) — proposed, not yet applied (catalogue-finishing doc §2). |
| T4.6.3 | Same status/split shape as T4.6.2. |
| T7.1.2 | Stage 1 rollup — `SELECT DISTINCT` part-of-speech prefix from `verse_lexical.morph_code` across every row sharing this Strong's code. |
| T7.1.8 | Stage 1 rollup — `GROUP BY verse_lexical.testament` across every row sharing the term's root/family (via `strong_related`), counted per side. |
| T7.1.9 | Same rollup as T7.1.8 — a term with zero `testament='OT'` rows anywhere in its `strong_related` family. |
| T7.1.1 | Stage 1 rollup — every distinct `resolved_sense` the term carries across its full occurrence set (confirmed live: genuinely narrows per-stem, not a repeated flat gloss). |
| T1.1.2 | Same rollup mechanism as T7.1.1. |
| T7.1.10 | Not a separate derivation — the union of T7.1.1/T7.1.2/T7.1.8/T7.1.9's own rollups. |
| T6.1.1 | Stage 1 supplies the raw `strong_related` pull (mechanical); NOT paired with T6.1.2 — each is its own question, corrected from an earlier mis-pairing this session. |
| T6.1.2 | Genuinely Stage 2, T0.2.1-class — "what the co-occurrence pattern shows" is behaviour-synthesis, not a Stage-1 field. |
| T6.4.1 | Stage 1 supplies the raw `strong_related` pull; cross-referencing which *characteristic* each related code belongs to needs Stage 2's own input-assembly linkage — a genuine two-stage dependency, not purely Stage 1. |
| T6.4.2 | Same two-stage dependency as T6.4.1, plus a lemma/root match across two characteristic-candidates' term families. |
| T7.2.1 | NOT fully Stage 1 — sentence-role half is Stage 1 (via `verse_lexical`/`morph_code`); argument/premise-conclusion half is a real, unowned gap (connective/chain notes give local edges only, nothing assembles them into an argument map). Wording-split proposed, not yet applied (catalogue-finishing doc §3). |
| T7.2.3 | Real, unowned gap — same reason as T7.2.1's argument half. No Stage 1 field answers this. |
| T7.1.3 | NOT a Stage-1 rollup — a property of `strong_meaning_tree`/`strong_meaning_parsed` directly, independent of any specific verse occurrence. Stage 1 draws on this resource, doesn't re-derive it. |
| T7.1.4 | Real gap — term-family semantic classification (disposition-vs-act) needs judgement on top of a T7.1.2-style rollup; not a field Stage 1 stores directly. |
| T7.1.5 | Real gap — structural-opposite/antonym terms, same status as T7.1.4. |
| T7.1.6 | Real gap — same status as T7.1.4/T7.1.5. |
| T7.1.7 | Real gap — same status as T7.1.4/T7.1.5/T7.1.6. |

**What this does NOT cover:** the ~85 T0.2.1-class questions and the whole-characteristic/whole-book
synthesis majority — by design, out of Stage-1 grain entirely (field-mapping doc §5), not silently
omitted from this writeback.

**Before I run 27 `obs_catalogue.update` calls against a live table:** confirm (a) this is the right
column (`review_note`, not waiting for `answered_by` to exist first), and (b) the wording above is
what you want on the record, not a summary I should tighten/change first.
