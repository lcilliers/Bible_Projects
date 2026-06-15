# Fix plan — `language` derived from Strong's prefix (root bug, not a plaster)

> Researcher (2026-06-15): *"the real problem is that the audit_word routine has a bug… the morph is significantly more reliable than the Strong's prefix… there is even a possibility that the Strong's prefix is wrong also."* Correct. This replaces the classifier-only "plaster" with the root fix.

## Root cause (verified)
`scripts/analytics/step_client.py:200`:
```python
language = "Greek" if resolved_strong.startswith("G") else "Hebrew"
```
Language is derived from the **Strong's prefix**, then persisted to `mti_terms.language` / `wa_term_inventory.language` during `audit_word`. The prefix is a coarse lexicon heuristic; the **morph code is the authoritative per-occurrence linguistic fact**.

**Evidence (term-level, morph as truth):**
- G-prefix → Greek morph: **915** ✓ · H-prefix → Hebrew morph: **1,378** ✓
- H-prefix → **Aramaic** morph: **121 terms / 866 occ** ← mislabelled "Hebrew"
- Genuine prefix↔morph conflicts (H→Greek or G→Hebrew/Aramaic): **0**

So the prefix is reliable for the **script family (H vs G)** but **structurally blind to Aramaic** (Aramaic carries H-numbers). No H↔G miscodings exist *today*, but a morph-first derivation also makes the field robust if one ever appears.

## The coupling that makes this non-trivial
`language == "Hebrew"` is used elsewhere as a proxy for **"Hebrew-script / OT"**. If we relabel the 121 to `Aramaic` without updating these, Aramaic terms break:
| site | current | effect if left | fix |
|---|---|---|---|
| `meaning_parser.py:238` | `elif language == "Hebrew":` (else → Greek parser) | Aramaic parsed as **Greek** | `in ("Hebrew","Aramaic")` |
| `audit.py:300` | skip Greek-only fields when `== "Hebrew"` | Aramaic flagged for missing LSJ/Mounce | `in ("Hebrew","Aramaic")` |
| `new_word.py:735` | Hebrew `also_spelled` handling when `== "Hebrew"` | Aramaic skips it | `in ("Hebrew","Aramaic")` |
| `meaning_parser.py:252` | `if language == "Greek"` (LSJ) | Aramaic correctly excluded | **leave** |

## What the data actually shows (so we use morph where it's solid, and flag what's fussy)
- **Morph is consistent — essentially 100%.** Of **2,414** terms that appear in the text, **2,413 have a single consistent morph-language**; only **1** is mixed (H3201 *yakhol*: 85 Hebrew + 1 Aramaic-section occurrence). → For everything with text, morph is unambiguous. **Use it.**
- **Every active verse has a morph**, so the principle *"a verse cannot have no language"* is fully met by morph. The lone in-scope exception is **H0516** (1 term, active verses but no morph — a particle).
- **The morph-less remainder (~1,430 terms) has *zero active verses*** — lexicon-only / reference entries with no text. Morph can't speak for them, but neither does any verse need a language for them.
- **The genuinely fussy bit (flagged, not plastered):** Aramaic-vs-Hebrew for those text-less lexicon entries. The Strong's prefix can't resolve it (same blindness), so it would need the **STEP lexicon's own language tag** — a separate, lower-stakes sub-problem. I am **not** guessing it with the prefix.
- **The bug is in more than one place:** `language` is prefix-derived at `step_client.py:200` *and* `audit_word.py:778` (new-term insert). So fixing it at the inserts is whack-a-mole — the right shape is **one post-sync reconciliation** that sets language from the (authoritative) morph after verses are synced, run both inside `audit_word` and as a one-time backfill.

## The fix (morph-authoritative language)
1. **Canonical helper** — add `term_language(morph_codes, strongs)` to `scripts/analytics/morph_util.py`: dominant `morph_language` across the term's occurrences; **fallback to the Strong's prefix only when the term has no morph** (function-word/lexicon-only terms). One source of truth.
2. **Engine derivation** — in `audit_word`, after the term's verse records (with morph) are synced, set `mti_terms.language` + `wa_term_inventory.language` from the helper. Self-healing every run → **persistent** (no revert).
3. **Aramaic = Hebrew-script** — apply the 3 `in ("Hebrew","Aramaic")` edits above so parsing/auditing route Aramaic correctly. Leave the `== "Greek"` checks.
4. **One-time backfill** — set the 121 Aramaic terms → `language='Aramaic'` in `mti_terms` + `wa_term_inventory` (dry-run → live), using the same helper.
5. **Verify** — language↔morph: 0 unexplained; a sample Aramaic term routes to the Hebrew parser, not Greek; re-run the consistency check.

## Scope note
Diagnostic scripts that filter `language='Hebrew'` (e.g. `_assess_meaning_tables.py`, `_realign_meaning_tables.py`) will, after this, exclude the 121 Aramaic terms from "Hebrew" counts — correct, but worth knowing. They are read-only diagnostics, updated only if/when run.

## Recommendation
Implement 1–5. It is bounded (4 code edits + 1 helper + 1 backfill), makes the morph the authority, fixes the persistence/revert problem at its source, and removes the "noise later." **Confirm and I'll proceed.**

---

## RESOLUTION (2026-06-15) — implemented 1–6

1. **Helper** — `morph_util.term_language(morph_codes)`: dominant morph-language; returns **None** (no assertion) for morph-less terms (never guesses Aramaic from the prefix).
2. **Reconciliation** — `scripts/_apply_language_reconcile.py` with importable `reconcile_language(conn)`. **Trigger corrected:** `audit_word` does **not** write `morph_code` (its verse INSERT at line 1043 has no morph column — morph is written by `_apply_morph_backfill.py`). So the reconciliation is wired into **`_apply_morph_backfill.py`** instead — it runs after every live morph write, so language (a derivation) follows morph (its source). Self-healing, no revert.
3. **Aramaic = Hebrew-script** — guards added at `meaning_parser.py:238` (Aramaic no longer routes to the **Greek** parser), `audit.py:300`, `new_word.py:735`. The `== "Greek"` checks left intact.
4. **Backfill (live)** — **121 terms → `Aramaic`** in `mti_terms`; **188** rows in `wa_term_inventory`. Language↔morph unexplained mismatches: **866 → 1** (the lone H3201 *yakhol* — a Hebrew term with a single Aramaic-section occurrence; correct).
5. **Verified** — all changed modules parse; the three Aramaic guards are present; reconciliation idempotent.
6. **Flagged, not plastered** — the ~1,430 text-less lexicon-only terms keep their existing label; resolving *their* Aramaic-vs-Hebrew status needs the **STEP lexicon language tag** (a separate, lower-stakes job), recorded here as the open item.

**General principle banked:** `morph_code` is the source of truth; `stem`, `language`, and (when emitted) the **mode finding** are all derivations of it — any morph change must re-derive all three. `stem` + `language` now re-derive together in the morph backfill; the mode-finding emit will join the same trigger.
