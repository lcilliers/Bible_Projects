# Templated narration — first output (2026-06-15)

> The **deterministic view** (01b §1f) that composes a term-in-verse's meaning sentence from its `ve_lexical` fields + the mode column. **Not authored prose** — every clause maps to a field → ve_lexical row → verse. Generator: `scripts/_produce_ve_narration_v1.py` (read-only).

## Composition rules (researcher, 2026-06-15)
- **Every element present is included.** Order: sense → type → mode → location → origin → faculty → attributed-to-God → compound → relational.
- **Multiples render as multiples** (joined with "and").
- **`UNRESOLVED` renders as a `[field: UNRESOLVED]` placeholder** clause.
- **NONE / SILENT are omitted** — they are not recorded (present-only), so they never appear.

## The first narration
> In Luk 22:44, *agonia* (“a struggle”) carries the sense “a struggle”, functioning as a status, in Greek noun form, combining with *proseuchomai(M21)*, with a **[relational: UNRESOLVED]**.

## Demonstration set (the M01/M23/M46 dump verses — compare to the earlier raw dump)

- In 2Sa 1:9, *sha.vats* (“agony”) carries the sense “agony”, functioning as a status, in Hebrew noun form, combining with *ne.phesh(M25)*, directed *for*.
- In 2Sa 1:9, *ne.phesh* (“soul: life”) … in Hebrew noun form, combining with *sha.vats(M01)*, with a **[relational: UNRESOLVED]**.
- In Luk 24:37, *emfobos* (“afraid”) … functioning as a quality, in Greek adjective form, located in the **spirit**, combining with *ptoeō(M01)*.
- In Psa 139:23, *sar.ap.pim* (“anxiety”) … in Hebrew noun form, located in the **heart**, engaging the **cognition** faculty, **[attributed-to-God: UNRESOLVED]**, combining with *le.vav(M47)*.
- In Psa 20:3, *da.shen* (“to prosper”) … in Hebrew verb · Piel form, engaging a **[faculty: UNRESOLVED]**, combining with *za.khar(M41)*. — *(the prior false `memory` is gone; faculty correctly UNRESOLVED here)*
- In Psa 20:3, *za.khar* (“to remember”) … engaging the **memory** faculty (direct gloss), combining with *da.shen(M46)*.

## Notes
- **mode** is drawn from the `morph_code`/`stem` column (bedrock), rendered via `morph_util.morph_readable` (e.g. "Hebrew verb · Piel", "Greek adjective").
- **Known cosmetic:** the indefinite article isn't a/an-aware ("a action") and the Luk 24:37 *spirit* location is the iteration-1 "spirit"=ghost homograph (flagged in the dry-run review) — both trivially fixable; structure is the point here.
- The narration is currently a **computed view**, not stored. Persisting it as the single `l2_meaning` finding per term-in-verse (the normalisation memory's "templated narrative = the single lexical finding") is the next decision.
