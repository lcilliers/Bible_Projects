# VE signal-list completeness audit + base rerun — 2026-06-19

> Continuation of the 2026-06-18 location seat-engine fix discipline (memory `project_location_seat_engine_fixed`:
> *audit lexical completeness of EVERY signal list*). Read-only audit → engine signal-list expansion →
> full base rerun over every characteristic-related unit → governed residue reads.

## 1. The problem

The location fix proved a hand-seeded signal list (the constitutional-seat map) had silently been a stub.
The same risk applies to the engine's other hand-seeded lexical lists: divine names, spirit-beings,
perception verbs, cognition verbs, intensifiers, causal markers. A missing member = a verse the engine
mis-derives. The fix is the same: diff each list against the category's canonical lemmas, gated on corpus
presence, and close every gap that actually occurs in the data.

## 2. The audit (read-only)

[`scripts/_check_ve_signal_lists.py`](../../scripts/_check_ve_signal_lists.py) — for each category, a curated
canonical lemma set is diffed against what the engine holds (`_canon`-normalised), and each missing member's
corpus presence (tagged term-in-verse units) is reported. Only members **missing AND present in corpus** are
flagged.

## 3. Engine fixes applied ([`scripts/_ve_engine_v2.py`](../../scripts/_ve_engine_v2.py))

| List | Added (2026-06-19) |
|---|---|
| DIVINE | H3069 (YHWH-Elohim), H433 (Eloah), H3050 (Yah), H5945 (Elyon), G5547 (Christos) |
| PERCEPTION | H8085 (shama, hear), H5027 (nabat, look), H238 (azan, give ear) |
| COGNITION | H995 (bin, understand) |
| INTENSIFIER | H1419 (gadol, great) |

Un-added canonical members (angelos, seraph, cherub, ya'an, oida, sphodra, …) have **0 tagged occurrences**
in the corpus, so they change no verse; left out by design (present-only discipline).

**Audit result after fixes: PASS** — all six categories complete (no missing canonical member present in the corpus).

## 4. Base rerun ([`scripts/_apply_generate_ve_lexical_v2.py --live`](../../scripts/_apply_generate_ve_lexical_v2.py))

The engine is fully reproducible, so the base must be regenerated after any list expansion.

- **Scope:** every `verse_context` unit with `cluster_code IS NOT NULL` (= every term-in-verse belonging to a characteristic). 40,737 units → 38,969 generated (1,768 T2-grammatical skipped per 01c §A3).
- **Preservation:** the ~66k API-read values (`*_read_api` / `read pass:`) are skipped on rewrite — the mechanical base is replaced, reads are NOT reverted. Verified intact post-run (valence 30571 · divine 14212 · object-type 12104 · cause 7743 · location 1336).
- **Output:** 298,319 active mechanical rows · 30,569 narration findings re-derived · integrity `ok`.
- **Snapshot:** `backups/bible_research_pre-ve-rerun-20260619.db` (fresh, pre-run).

## 5. New residue surfaced by the better signals (governed reads)

The expanded lists reclassified units the old base had mechanically (mis)resolved. The governed reader is
**T2-EXCLUDED** (T2 = reference qualifiers/seats, never analysed standalone — memory
`feedback_t2_reference_flag_reclassify`) and joins only **active** verse records. So the raw residue counts
over-state the work: the *true* read scope is the **non-T2, has-active-verse** subset.

| field | raw residue | of which T2 (skip) | unreadable¹ | **real read scope** | result |
|---|---|---|---|---|---|
| divine-involvement | 4,695 | 4,263 | 0 | **432** | ✅ all resolved · $0.18 |
| object-type | 3,593 | 3,593 | 0 | **0** | ✅ nothing to read |
| cause | 1,882 | 1,882 | 0 | **0** | ✅ nothing to read |
| location | 111 | 111 | 0 | **0** | ✅ nothing to read |
| valence (units-mode) | 689 | — | 689 | **0** | ✅ nothing to read |
| **total spend** | | | | | **$0.18** |

¹ no active `wa_verse_records` row (delete-flagged XREF copy / orphan) — no verse text to send.

`type` UNRESOLVED ×129 has no reader spec; it is a pre-existing mechanical state (never read), not new from
this rerun — left as-is.

**Final state:** 0 active readable non-T2 residue across all five read fields. read_api totals unchanged
except divine 14212→14644. Integrity `ok`. Reads run sequentially (SQLite single-writer);
logs `outputs/ve-read-<field>-rerun-20260619.txt`.

## 6. Close-out checklist

- [x] signal-list audit script + engine expansion
- [x] base rerun (live) + read_api preservation verified + integrity ok
- [ ] residue reads complete for all five fields → 0 active residue
- [ ] `type` UNRESOLVED (129) handling decided
- [ ] reports regenerated · quick_check · commit
