# VE mechanical rebuild — dry-run review (2026-06-15)

> Output of `scripts/_apply_ve_rebuild_mechanical_v1.py --dry-run` over 40,739 active term-in-verse units, deriving VE 1/2/3/5/6/7/8/13 strictly per 01b §1d. **No writes yet — this is the review gate before `--live`.**

## Distribution (247,899 rows total)

| VE | field | rows | breakdown |
|---|---|---|---|
| 1 | sense | 40,739 | UNRESOLVED 178 (no subgloss); rest = per-occurrence STEP subgloss |
| 2 | type | 40,739 | status 17,552 · action 16,944 · quality 3,895 · UNRESOLVED 2,348 (function-word POS) |
| 3 | compound | 82,236 | web-edges (T1 co-term + T2 qualifier per co-occurring term) |
| 5 | location | 10,599 | seat/body words co-occurring (01b co-occurrence rule) |
| 6 | origin | 3,742 | within-person 461 · UNRESOLVED 3,281 (bestowed/received need subject/source) |
| 7 | faculty | 19,342 | assigned ~10,803 (direct gloss / neighbourhood) · UNRESOLVED 8,539 |
| 8 | attributed_to_God | 15,750 | yes 835 · UNRESOLVED 14,915 (divine word present, possessor unconfirmed) |
| 13 | relational | 34,752 | assigned ~20,302 (neighbourhood) · UNRESOLVED 14,450 |

## The headline fix — confirmed (verses from the prior raw dump)

| verse · term | prior (corrupt) | now | verdict |
|---|---|---|---|
| Psa 20:3 *da.shen* "favor" | faculty=**memory** (false; "remember" = God remembering) | faculty=**UNRESOLVED** | ✓ fixed |
| Psa 20:3 *za.khar* "to remember" | — | faculty=**memory** direct(gloss) | ✓ correct term |
| 2Cor 7:16 *tharseō* "confidence" | faculty=**affect** (false; "rejoice") | no faculty (UNRESOLVED elsewhere) | ✓ fixed |
| Psa 139:23 *sar.ap.pim* "anxiety" | — | faculty=**cognition** indirect("know" in nbhd), location=heart | ✓ plausible |

Faculty now attaches to the term whose **gloss is the faculty word** (R1) or where the word is in the **term neighbourhood** (R2) — not a blanket verse scan.

## Honest precision flags (01b lists are iteration-1 seeds)

1. **"will" homograph** — auxiliary "they *will* turn" false-matches `volition`. *Deu 31:20 da.shen → volition.* The list word "will" needs disambiguation (or drop it).
2. **"spirit" homograph** — "saw a *spirit*" (ghost) false-matches the location seat. *Luk 24:37 → location spirit.* Same for body words ("hand", "back", "members") and "search"/"judge".
3. **VE13 bare prepositions** — "to / for / from" assign relational on most units (low signal). Consider restricting VE13 to the relational *verbs* + a tighter directional set, or accept as iteration-1.
4. **VE8** — only 835 confident `yes`; 14,915 `UNRESOLVED`. Correct per design (subject/possessor not mechanically resolvable) — the UNRESOLVED set is the read-worklist, not a failure.

## Decision before `--live`
- **Option A — write as-is** (iteration-1): captures the mechanical floor + the UNRESOLVED worklists; refine the signal-lists (homographs, VE13 prepositions) in iteration-2 as separate targeted passes. The table is trivially re-derivable (re-wipe + re-run).
- **Option B — refine specific lists first** (e.g. drop "will"/"spirit"/bare-prepositions) then write.

Recommend **A** — the data is fully reproducible, so writing iteration-1 now gives a concrete base to review per-cluster, and list-refinement is a cheap re-run. Awaiting researcher direction.
