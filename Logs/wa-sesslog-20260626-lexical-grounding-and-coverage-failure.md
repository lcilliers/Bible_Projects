# Session log — 2026-06-26 — Lexical grounding cleanup + the coverage-failure reckoning

> **Read this honestly.** This session cleaned real bias out of the lexical, but its most important outcome is the discovery — proven, measured, and now durable — that the verse-meaning foundation reaches only ~9% of spans. The earlier "completeness" was largely illusory. This log records what was done, what is true, and what is intact. No good story.

## 1. Arc of the session
Began as "continue previous session" (the 2026-06-26 reset corpus sweep). The researcher flagged the **faculty** field as obviously wrong. Investigation confirmed it, and established a **governing rule** that then drove the rest: *the lexical captures only what the verse says; anything not grounded in the verse is an error.* Applying that rule across the read-API overlays surfaced systemic "bleeding," and a researcher-directed **verse_span_lexical fan-out index** then exposed a foundational coverage failure beneath all of it.

## 2. Governing rules established (saved to memory)
- **`feedback_lexical_strictly_verse_bounded_no_implied_evidence`** — the lexical = only what THE VERSE says; no-basis-in-verse value = ERROR → reverse out. ALL items. Divine: mention true if named, never overstate an unclear role. (Foundational from the start; violated by the API runs.)
- **`feedback_faculty_only_if_explicit_or_inferred_on_verse`** — faculty only if explicit/inferred ON the verse, never from the lemma.
- Root-cause insight recorded: **valence was a clustering driver**, so its interpretive bias shaped the M-code cluster structure itself — a likely source of the prior bias/diversions.

## 3. DB changes — all reversible (backup + per-fix snapshot + soft-delete/relabel)
| fix | action | rows | snapshot table |
|---|---|---|---|
| faculty | rebuilt verse-grounded (explicit faculty-words; seat-inference) | 29,203 lemma rows → 22,128 new | `ve_lexical_faculty_pre_reset_20260626` (29,203) |
| divine-involvement (a) | reverse ungrounded role assertions (no divine name in verse) | 860 | `ve_lexical_divinv_pre_reverse_20260626` (860) |
| object-type | reverse ungrounded (God-no-divine + no-object) | 1,128 | `ve_lexical_overlay_reverse_20260626` (1,387 incl cause) |
| cause | reverse inferred-not-in-verse | 259 | (in overlay snapshot) |
| valence | QUARANTINE (interpretive overlay; clustering driver) | 26,993 | `ve_lexical_valence_quarantine_20260626` (26,993) |
| origin | QUARANTINE (single-value non-grounded stamp) | 3,623 | `ve_lexical_origin_quarantine_20260626` (3,623) |
| object-type | taxonomy remap {thing, abstract, thing/abstract} → `impersonal` | 9,534 | `ve_lexical_objtype_premap_20260626` (9,534) |
| divine-involvement (b) | demote grounded roles → `present` (mention only) | 5,187 | `ve_lexical_divinv_roles_premap_20260626` (5,187) |
| faculty seat-inferred | reverse (proximity binding, not verse-stated) | 1,492 | `ve_lexical_faculty_seat_reverse_20260626` (1,492) |

Everything soft-deleted/relabelled in place (recoverable). DB backups taken before each write (see §6).

## 4. THE HEADLINE — verse_span_lexical coverage failure (the truth)
Researcher-directed master index: every verse → every span STEP returned (no filter) → verse-record (status/missing) → lexical (status/missing) → compound (status/missing). Built corpus-wide.
- **444,507 span entries across 23,593 verses.**
- **Spans with a lexical: 40,821 (9%). Missing: 403,686 (91%).**
- Record status: ACTIVE 61,171 · **MISSING (no verse-record) 350,498** · **STRANDED_DELETED_TERM 29,427** · ALL_FLAGGED 3,411.
- Lexical status: PRESENT 40,821 · **NO_UNIT 18,314** (active record, no unit) · MISSING 385,372.
- Concrete proof case: **Pro 24:20** — `wicked` (H7563/M10) analysed; `evil` STRANDED on deleted homograph **H7451H** (6 flagged records, never re-mapped to the active H7451A/M27); all other spans MISSING.

**What it means:** the verse-record table carries ~61k active records but the lexical layer reaches only ~41k spans; the bulk of every verse is unaccounted. The pipeline measured activity (rows/runs/statuses), never verse-king completeness. There was **no intrinsic control** checking the work against the verse. That control now exists — this index — and it is regenerable and ungameable.

## 5. Memory tidy
`MEMORY.md` compacted 31.7 KB → 15.0 KB (was truncating on load). Restructured: foundational rules first, then current RESET method, active state, technical/DB, orientation, legacy. Retired v2_x/v3_0 pipeline-mechanics index lines dropped (files remain on disk + git). No topic file deleted.

## 6. Artifacts — inventory (intactness check passed)
**DB backups (backups/, NAS-mirrored, git-excluded):** `bible_research_pre-reset-sweep_20260626.db`, `…_pre-faculty-reset_…`, `…_pre-divinv-reverse_…`, `…_pre-overlay-reverse_…`, `…_pre-valence-quarantine_…`, `…_pre-remaining-fixes_…` (6 files, ~500 MB each).
**Snapshot tables (8):** listed in §3 — every reversal recoverable.
**The index:** `outputs/wa-verse-span-lexical-index-v1-20260626.json` (237 MB). Git-excluded (regenerable); kept on disk; backed up by the daily 18:30 NAS full-folder mirror. Reproducible from `scripts/_build_verse_span_lexical_index_v1_20260626.py` (in git).
**Scripts (git):** `_apply_faculty_reset_verse_grounded_v1_…`, `_probe_faculty_reset_dryrun_v1_…`, `_apply_divine_involvement_reverse_ungrounded_v1_…`, `_apply_reverse_ungrounded_overlays_v1_…`, `_apply_quarantine_valence_v1_…`, `_apply_clear_remaining_lexical_fixes_v1_…`, `_build_verse_span_lexical_index_v1_…`, `_probe_faculty_reset_dryrun_v1_…`.
**Docs (git, outputs/markdown/validation/):** faculty-state-diagnosis, faculty-reset-dryrun, faculty-reset-outcome, ve-lexical-item-sanity-scan, divine-involvement-grounding-audit, overlay-bleeding-audit-and-reversals, 10-random-verses-full-detail, verse-meaning-fanout-index-design.

## 7. Open — for the researcher to weigh (no plan pushed)
- The coverage failure is the governing fact now. Whether/how to rebuild the verse-meaning layer is the researcher's call.
- Stranded-deleted-homograph re-mapping (e.g. H7451H → H7451A) is a concrete, scoped remediation if wanted.
- `RECORD_NO_UNIT` (18,314) and `ALL_FLAGGED` (3,411) are recoverable gaps with active records.
- The index can be cut per-book / gaps-only / materialised as a DB table for navigation.
- divine-involvement ~46% UNRESOLVED remains (separate backlog).

## 8. Governance
- Working tree committed through the cleanup; this log + builder script + design docs committed at session close. The 237 MB index is intentionally git-excluded (regenerable) and NAS-mirrored.
- All-in-DB rule honoured; everything reversible; nothing destroyed.
