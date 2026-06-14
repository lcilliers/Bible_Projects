# Session log — 2026-06-14 · L1/L2 field reliability + morph backfill

> Focus: turning the L1/L2 "verse-read = meaning" impasse into a tractable, mechanical, traceable design — by working field-by-field through the 14 verse-extraction fields, establishing which are mechanically derivable, and closing the first real data gap (morph). Companion to the same-day memory/governance-hardening log (`wa-session-log-20260614-memory-governance-hardening.md`). All work read-only design + one reversible structural backfill.

## Where we started

Carried in from the prior session: the L1/L2 reframe — **sense lives on the edges (a combination of nodes), not in the node**, so reliability = derivability from named measures = traceability. The 14 fields sort into four strata (bedrock · node-combination · sense-dependent · out-of-reach). Active doc: `research/investigations/wa-l1l2-field-reliability-measures-v1-20260614.md`.

## What we did today

### 1. 50 complex-verse working set
`research/investigations/wa-l1l2-50complex-verses-working-set-20260614.md` — the top 50 multi-term, multi-cluster verses (6–10 clusters each; 473 term-occurrences), each card carrying reference · verse text · terms (strongs · translit · cluster · gloss · morph · stem). The empirical foundation for mode assessment and signal-list seeding.

### 2. Mode (#4) assessed → confirmed bedrock
Mode = the morph, parsed. Hebrew verb **stem** is the operative mode (Qal/Hiphil/Piel/Niphal/Hithpael/Pual); nominal = form; Greek = the parse. Verse-specific **and** mechanical (same root, different stem per verse — captured per occurrence). No read needed. Only work: a morph-code → label parse, and a morph backfill (see §5).

### 3. Signal-lists (iteration 1) seeded from the 50 verses
For the five signal-driven fields — location, origin, faculty, attributed-to-God, relational — starting vocabularies with example verses. Location is the cleanest (small closed seat/body set).

### 4. Three refinements folded in (researcher)
- **Flesh is a constitutional location** (Gal 5:19-21 — flesh as locus of a set of inner-being works). Added as a *level*, not a body-part.
- **An `UNRESOLVED` state on every field** — distinct from `NONE`/silent. `NONE` = legitimately absent; `UNRESOLVED` = expected-but-couldn't-resolve = the **backtrack worklist**.
- **Signal-LIST vs signal-RULES** — a new column. The list is vocabulary; the rules are decision logic (faculty: R1 direct · R2 indirect · R3 multi · R4 unresolved · R5 none). New §1d table: list · rules · states.

### 5. Morph backfill gap surfaced + closed (the first real data gap)
- **Surfaced (not patched):** not an M47 problem — **69 content terms across 14 clusters** were fully un-morphed (3,436 occ; real terms: *lev* 331, *berith* 236, *mishpat* 208, *levav* 207, *basar* 205, *kardia* 120, *sarx* 85), **plus all of T2** (24,282 occ). Root: `_apply_morph_backfill.py` ran in 4 batches on 2026-06-08; M47 was created 2026-06-10 (after), and the others were never batched. Finding doc: `research/investigations/wa-morph-backfill-gap-programme-wide-v1-20260614.md`.
- **Fixed (reversible):** re-ran the **proven** `scripts/_apply_morph_backfill.py --clusters M47,M26,M25,M22,M44,M23,M03,M05,M04,M30,M28,M27,M34,M39,T2 --live`. **Wrote morph to 40,697 rows.** Match-rates 76–100% (content) / 70% (T2). Report: `research/investigations/wa-morph-backfill-catchup-live-v1-20260614.md`.
- **Verified:** content terms fully un-morphed **69 → 0** (6 stray occ remain — STEP returned no morph for those exact verses; genuinely un-parseable). T2 now 24,112/24,282 morphed, **5,035 carry a verb stem** (exactly the verb-like qualifiers — *to look*, *to see*; particles correctly left without a stem). T2 included on the researcher's call.

### 6. Sense (#1) — the confusion resolved, grounded in data
Researcher asked: can sense be mechanically derived? **Yes, mostly** — sense is a spectrum, not one reliability:
- **79% of occurrences are mono-sense** (1 STEP subgloss) → fully mechanical.
- **Poly-sense (370 terms)** → STEP's subgloss is **per-occurrence** (*nephesh* splits 9 ways across its verses) → a **field-lookup**, not a read.
- **Coarse-ceiling residue** (*pneuma* "spirit" lumps Holy-Spirit + human-spirit + wind) → needs a **signal-rule** or the read → else `UNRESOLVED`.
- **10 terms / 179 occ** have no subgloss source → `UNRESOLVED`.
- **Impasse correction:** the old "*pneuma* = wind/breath for all 312 verses" used the term's **uniform gloss**, not STEP's per-occurrence subgloss (`:spirit` 120 / `:breath` 4). STEP had disambiguated and the run ignored it. Recorded in §1e.

### 7. The target architecture captured (§1f)
The 14 fields **COMPOSE** the meaning — the inversion of the failure:
- Failed: narrate prose → can't trace back.
- Target: derive 14 fields (each a traceable finding) → **compose a templated sentence** → meaning is **back-trackable by construction** and **searchable**.
- The sentence is a **deterministic view of findings**, not a new artefact — verifiable, reproducible, can't drift from evidence.
- Three terminal states per field: **resolved** · **indeterminate** (the verse genuinely doesn't settle it — a *real finding*) · **pending** (`UNRESOLVED`).

### 8. Traceability proven live (not asserted)
Chain demonstrated on **2Sa 1:9 / H7661**: `wa_verse_records #439` (morph `HNcmsa`) → `verse_context #1630` (`step_meaning_applied='cramp, agony, anguish meaning uncertain'`, via the **`verse_record_id` FK**) → **6 findings** that ARE the 14-field decomposition (sense · type=status · compound=simple · mode · origin=within-person · attributed-to-God=no). Every field value is verse + term anchored.
> Note (honest precision): the backfill populates the **source measure** (morph column); the **mode finding** is a separate emit that derives from and **cites** it. Same for sense (subgloss column → sense finding). That is what keeps "all analysis in findings" true while preserving the back-trace.

## Artefacts (all committed + pushed)
- `research/investigations/wa-l1l2-50complex-verses-working-set-20260614.md` (data + mode assessment + signal-lists)
- `research/investigations/wa-l1l2-field-reliability-measures-v1-20260614.md` (§1a–1f frame + 14-field table — the canonical design)
- `research/investigations/wa-morph-backfill-gap-programme-wide-v1-20260614.md` (the gap finding)
- `research/investigations/wa-morph-backfill-catchup-live-v1-20260614.md` (the run report)

## DB state change
- `wa_verse_records.morph_code` / `stem`: **+40,697 rows** populated (15 clusters incl T2). Additive, reversible (NULL the columns). No other writes.

## Open / carry-forward
- 6 stray content occurrences + ~170 T2 particles left without morph — STEP returns nothing; leave NULL (correct) or `UNRESOLVED`-mode.
- `verse_context.sense_id` is **NULL across all rows** — the sense finding is not yet wired to a sense_id; `step_meaning_applied` is the populated source. Relevant to tomorrow's sense work.
- Mode/sense **findings** not yet emitted from the source columns (the emit step that lands them in the finding store).

## Tomorrow's plan (researcher-set sequence)
1. **Sense** — apply the mechanical floor (STEP per-occurrence subgloss); coarse-ceiling residue (*pneuma*-type) → signal-rules or `indeterminate`/`UNRESOLVED`.
2. **Type** — supersedes to sense (status-vs-quality).
3. **Refine the 5 signal-list assignments** — location · origin · faculty · attributed-to-God · relational (complete list + rules + states).
4. **Figure out 9–12** — purpose_equips · typology_direction · immediate_response · produces_effect.
5. **#14 (literary_setting) falls away** for verse-level work.
6. **Templated narration** — last; the 14 fields → the composed verse-meaning sentence.
