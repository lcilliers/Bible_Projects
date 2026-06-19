# DIR-20260619-001 — completion confirmation · 2026-06-19

**Directive:** `wa-cluster-M02-dir-001-readfield-fix-v1-20260619.md` · **Applied by:** Claude Code
**Script (reversible):** `scripts/_apply_m02_dir001_readfield_fix_20260619.py` · **Backup:** `backups/bible_research_pre-m02-dir001_20260619.db`
**Method:** targeted value-set from the directive's verified re-read (read engine NOT re-run, per F10.1 caution). No physical deletes. Integrity `ok`.

## Storage resolved (the schema CC was asked to locate)

The read-resolved fields live in **`ve_lexical`** (schema 3.34.0) as one row per field per term-in-verse:
`ve_label='valence'` and `ve_label='divine-involvement'`, keyed by `verse_context_id` (→ verse_record reference
+ mti_term Strong's/translit). Read-resolved values carry `source_provenance` ending `_read_api`.

## Completion items (directive §Completion confirmation)

1. **Before A — the matching set (confirms 6, not 7):** 6 M02 burning-heat divine-wrath occurrences
   (`divine_involvement` ∈ {agent,possessor,giver}) with `valence='sinful'` — **exactly the directive's table**:
   Num 32:14 (H2740 cha.ron), 2Ki 22:13 (H2534 che.mah), 2Ki 22:17 (H2534 che.mah), 2Ki 23:26 (H2734 cha.rah),
   2Ki 23:26 (H2740 cha.ron), Job 42:7 (H2734 cha.rah). The 7th cited by the NEW findings did not match — **6 confirmed.**
2. **After A:** divine-wrath occurrences with `valence='sinful'` = **0** ✅ (all 6 → `neutral`).
3. **Provoking terms unchanged:** `ka.as` H3707 (2Ki 22:17, 2Ki 23:26) and `ka.a.s` H3708B (2Ki 23:26) remain
   `valence='sinful'` ✅. (Num 32:14 and 2Ki 22:13 carry no tagged M02 provoking-term occurrence — nothing to retain there.)
4. **After B:** Exo 4:14 and 2Ki 13:3 `cha.rah` (H2734) now `divine-involvement='agent'` ✅ (**2** active rows,
   one each). These route to **C2 (divine wrath)** when the c1–c7 split is derived from `divine_involvement` — and
   that split is **not materialised** in the DB yet (the NEW findings are unpersisted), so nothing further to update.
5. **Total changed = 8** ✅ — 6 valence + 2 divine-involvement. No collateral changes.

## CC judgement notes (for your review)

- **`experiencer` left at `other` — deliberately, and it is correct.** All 24 other divine-wrath `cha.rah`
  occurrences carry `experiencer='other'` ("the LORD's anger was kindled against [other]"). So `other` already *is*
  the value consistent with God-as-subject across C2; changing it would have made these two inconsistent with the
  rest. Directive intent (consistency) met without a change.
- **valence set to `neutral` (the directive's tabled target).** All 6 verses arguably frame the wrath as
  **`righteous`** (God's just anger at named sin — sinful men / forsaking / provocations / not speaking right).
  Per the directive's allowance, **flagged for your/AI review** if you'd prefer `righteous` over `neutral` for any/all.
- **Insert provenance:** the new divine-involvement rows use the corpus-canonical `divine_involvement_read_api`
  (matching the 4,597 existing active rows); the prior `UNRESOLVED` read rows for these verses are soft-deleted
  (not active) — exactly one active divine-involvement row per verse.

## Next

These corrections now stand in the measure layer, so the **NEW M02 findings will carry the corrected valence and
the corrected C1/C2 assignment** when persisted (per directive §Notes). The C7 scope item remains a separate decision.
