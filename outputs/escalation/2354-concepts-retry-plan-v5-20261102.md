# Concepts retry at surface grain: plan v5 (#2354, 2026-11-02)

Replaces plan v4 (archived). Nothing is built beyond the `surface_group` column (BUILD 443, 444). Workings, sources and numbers are in `outputs/escalation/2354-working-log.md` (finding numbers below refer to it). Every value produced is inferential (B:4) until you confirm it.

## What changed from v4, by your rulings
- **All surfaces, nothing cast away** (ruling 11): no take-out list, no L1 from a list.
- **One judgement per distinct surface string**, not per occurrence (ruling 15): 18,249 strings.
- **Ollama on your server judges** (ruling 13): `192.168.83.114:11434`, model `qwen3:30b`, CPU only (findings 26, 27).
- **The data problem is dealt with in the plan** (finding 28, ruling 16): a particle or secondary code in a multi-code span carries the span's English, so a pair is not always the code's own.
- **Out of this plan:** the story mapping (ruling 14), and where qualifier pairs live (ruling 12).

## The three kinds of pair (read from `verse_lexical`, no judgement)
| kind | rule | count (distinct pairs) | how it is settled |
|---|---|---|---|
| **particle** | the code is H9xxx | 34,865 | by the code: `qualifier`, use from the code's gloss; no model call; the surface is not trusted |
| **own** | the code has at least one occurrence in a span with a single non-particle code | about 47,800 (40,803 only-single plus 7,038 mixed; to be re-counted at L0) | judged by the model, per pair |
| **span-shared** | the code occurs only in spans with 2+ non-particle codes | 18,752 | judged by the model as part of the unit, marked `span_shared`; never counted as the code's own meaning |

Concept population (`surface_subgroup`, 13,462 rows, no particle codes): 10,701 are own-only, 1,255 span-shared-only and 1,499 mixed. The 1,255 and 1,499 are listed for your inspection and not allocated automatically.

## Layers
- **L0, inventory (no judgement):** from live `verse_lexical`, one file per batch of surface strings, giving per string its codes with kind (above), stepGloss, occurrence counts per kind, and (for concept pairs) the current subgroup. Counts re-read at the start.
- **L1, particle codes by rule:** the 42 distinct H9xxx codes (H9002 to H9049; read from `strong`) get `qualifier` and a use (conjunction, article, preposition, pronoun, particle, other) read from their gloss, as one small table you review once. All their pairs follow.
- **L2, the model, per surface string:** one call gives, for each own or span-shared code of the string, a group (behaviour, inner_being_state, being, qualifier, not_allocated) and for a qualifier a use from the fixed list. The answer has no reason except for `qualifier` and `not_allocated` (a one-line reason). Codes per call are capped (8 in the test) and a longer string runs in several calls. Resumable: a string already answered is skipped.
- **L3, consistency pass:** the same string given different groups on different codes (the "you" case, finding 27) is listed for review, never merged silently.
- **L4, you inspect:** `not_allocated`, the span-shared concept pairs, the L3 list, and a sample from every other value.

## Speed (finding 27, measured)
12 tokens per second; 23 to 29 seconds per string with a reason on every code. A full run on that prompt is about 5 days. Removing the reasons and the particle pairs should cut it by more than half; I will re-time on the same 20 strings before any full run and report the projection. If still too long, the options are a smaller model for the first pass with `qwen3:30b` on the disagreements, or running by cluster priority; your decision then.

## What must be built (B:105: a design, for your approval; nothing is written yet)
1. **Settings (B:6):** `cfg_setting` rows for the Ollama host, model, timeout, keep-alive and codes-per-call, by one migration tested on a copy of `iba.db`, restated in BUILD.
2. **Where the verdicts live:** a new table, `surface_pair_verdict`, one row per (strong, surface) pair: `strong`, `surface` (lower-cased), `pair_kind` (particle, own, span_shared), `surface_group`, `use`, `reason`, `model`, `run_id`, soft-delete and timestamps, `UNIQUE(strong, surface)`. `surface_subgroup.surface_group` (built) is then filled from it for the 13,462 concept pairs only; the other pairs have no subgroup row, which is why the table is needed. Registered in `cfg_table`/`cfg_column` with the enum for `surface_group`.
3. **The judging tool:** a Python module with a PowerShell front (`Surface-Judge.ps1`), reading host and model from config. Functions: `Inventory` (L0), `Particles` (L1), `Judge` (L2, resumable, writes batch files first), `Load` (a reviewed batch file into the table as one unit, refusing an unknown value or use), `Report` (counts, L3 list). Tested on a copy with a test plan before use.
4. **Not in this plan:** a head marker in `verse_lexical` and the particle rule of BUILD 428 (finding 28): a separate fix, raised as its own escalation only if you say so.

## Open points for you
- **P1, pronouns: ruled (ruling 17).** Qualifier with use `pronoun`; who is referred to is resolved when the verse is read, not for concept membership. The judging prompt says so, which also closes the "you" inconsistency of finding 27 at its source (L3 still checks).
- **P2, the fixed use list:** my start is place, time, quantity, quality, manner, reason, pronoun, article, conjunction, preposition, particle, other. Add or drop.
- **P3, storage:** approve `surface_pair_verdict` as the home of all verdicts.
- **P4, build order:** settings and the table first, then the judging tool, then a 100-string pilot including "within".

## Not claimed
The 47,800 "own" figure is the sum of two counts taken on different bases (all live pairs, non-particle) and is re-counted at L0. The reliability of an "own" pair is an assumption: a single non-particle code in a span is taken as the head, not proven. No model answer is a finding until you have seen it.
