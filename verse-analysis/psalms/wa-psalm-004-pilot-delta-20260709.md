# Psalm 4 — pilot delta (first re-read to standard), 2026-07-09

> First intervention pilot. Char-driven re-read of Psalm 4's 16 characteristics on the standard (cycle §3A/§5, genre-aware poetic ledger, span-id pairs). Validates the method + tooling + gate-delta before Psalm 23/78 and the book.

## What was done
- **Char-driven** (the char is the lens): each of the 16 characteristics read in turn; its pairs resolved **across the passage using the related verses' morphology** — not a span-sweep.
- **Reading filed:** `_read/psalm-004-reread-v1.json`. **Applied:** `_apply_reread_lexical_v1_20260709.py --live` (backup taken) — soft-deleted **81** prior (Strong's-encoded, shallow) rows, wrote **172** new rows, **30 span-id pairs** (all integer-encoded), marked 8 verses `process_marker=reread-psalms-2026`.

## Gate delta (Psalm 4, chapter-scoped)
| gate | before | after |
|---|---|---|
| G2 chars no operation | some | **0** |
| G3 ungrounded pairs | (Strong's) | **0** |
| G6 candidate verses no discovery | 8-ish | **0** (after v6 fix) |
| G9 pair encoding | Strong's (N/A) | **30 span-id pairs, 0 dangling** |
| G10 chars missing a mandatory dim | 16 (all) | **0** |

**Iterate-to-pass worked:** G6 first read 1 — v6 ("who will show us good?") holds candidates but no characteristic, so the char pass missed it; added a **verse-level discovery** (the many's craving for good) → G6 = 0.

## Corrections the char-driven read made to the old mechanical pass
- **shame (v2):** old = `manner-of love` / `welds love` (proximity error) → **corrected** to a status (honor's threatened terminus); bogus pairs removed.
- **godly (v3):** old bearer = `Lord` (nearest-proper) → **the chasid** (the LORD *sets apart* the godly; godliness is borne by the covenant-faithful person).
- **safety (v8):** old bearer = `Lord` → **the psalmist** (the LORD makes *me* dwell; the safety is mine, sourced in God alone).
- **hearts/heart (v4,v7):** old = `manner-of ponder/put` → **seat** (the heart is the chamber of pondering / the container of God-given joy).
- **honor (v2):** old = `specifier 'of shame'` → **none** (honor→shame is a Phase-2 transition, not a genitive).

## What the read surfaced (discoveries)
Ground-of-appeal righteousness (v1); grace-as-gift not command (v1); disordered love of vanity vs commanded trust in the LORD (v2/v5); knowing as re-orientation (v3); bounded anger ("be angry yet sin not") (v4); heart as chamber of nocturnal self-examination (v4); God-given joy exceeding harvest-joy (v7); peace/safety as God-sourced ground of untroubled rest (v8); the many's craving for good (v6).

## Method validated
Char-driven reading + genre-aware poetic ledger (source/effect deferred to Phase-2) + span-id pairs + the reusable apply tool + the iterate-to-pass loop all work end-to-end. **Cleared to run Psalm 23 and Psalm 78, then the Psalter.**

*Filed 2026-07-09. Backup: `backups/bible_research_prereread_Psa_ch4_*.db`.*
