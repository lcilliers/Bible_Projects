# The characteristic model — grounded current state (2026-07-11)

> Every fact below is a query/file result verified 2026-07-11, mapped to the researcher's three-part description of the model. Purpose: replace uncertainty ("if I remember / I suspect / I don't know what it looks like / not sure where the values sit") with the actual state, so the normalised-index discovery proceeds on facts.

## Layer 1 — the SEED (researcher's (a))
- **Source file:** `research/discovery/lemma-inventory-master-no-particles-20260707.json` (11,804 lemma records + `registry_match` + `ib_judgement`).
- **Applied by:** `scripts/_apply_stamp_char_candidate_on_master_v1_20260708.py` → stamps `verse_span_index.char_candidate=1` + `char_candidate_tag`.
- **Two seed streams:** word-registry match → tag `Reg N <word>`; IB judgement → tag `IB:<gloss>`.
- **Instruction linkage:** referenced by `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` (partly formalised).
- **Dynamic-extension gap:** of 2,168 read characteristics — **1,765 seeded** (1,478 `Reg`, 287 `IB`) + **403 emerged in reading, never fed back to the seed.** The "list gets extended as new seed words are found" is not happening for those 403.

## Layer 2 — the MASTER + the LEXICAL (researcher's (b))
- Each char-span row (`verse_span_index`) carries: `char_candidate` (1/0), `char_candidate_tag` (the **seed word**, pre-reading), `role` (set to `characteristic`). Each span is inherently unique.
- **The formalised read char is NOT in the master.** The read result — `sense`(101), `operation`(106), `type`(102), `bearer`(105), etc. — lives **only in `ve_lexical`**.
- So the master's "char" = the **pre-reading seed tag + the role flag**. The researcher's expectation ("the actual char is updated in the master") is **not met**; the read char is confined to the lexical.
- Role='characteristic' is the confirmation the candidate is IB-related (the lexical formalises it), as the model intends — but that confirmation writes the role, not the char, back to the master.

## Layer 3 — the NORMALISED INDEX (researcher's (c) — `ib_characteristic`)
- **29 rows = conceptual FAMILIES:** trust-refuge, fear-of-the-lord, the-heart, humility, seeking, waiting-hope, self-mastery, grief-lament, self-address, memory, restoration… with `status` (15 surfaced, 10 developing, 4 established).
- The *concept* matches the goal (families that many instances belong to; operations groupable).
- **But:** built `2026-07-03` from the **old read** (legacy, removable, no inbound FK); **no char-span links to it**; it does not yet "gather from lexical + master".

## What is now clear vs still open (for the discovery — not decided here)
**Clear (grounded):**
- The seed is a JSON file + stamp script, registry+IB driven, instruction-linked; 403 emergent chars are the un-fed-back extension.
- The master carries the seed tag + role, not the read char; the read char is in `ve_lexical` only.
- `ib_characteristic` is the right *concept* (families) but is old, unlinked, and empty of the corrected read.

**Open (researcher-led discovery — I will not guess these):**
1. Should the confirmed/read char be written back to the **master**, and in what form (a char field vs left in the lexical)?
2. The **family grain** of the normalised index — the ~29 families? word-level? operation-level? and how operations group.
3. The **link mechanism** from each char-span (lexical+master) INTO the normalised record.
4. How the seed's **dynamic extension** (the 403 emergent words) is formalised into the seeding process/instruction.

## Relation to the earlier PLAN doc
`wa-characteristic-restructure-and-integrity-fix-PLAN-20260711.md` proposed a concrete `ib_characteristic` schema before this grounding. Its **(c) integrity-fix half stands** (261 orphans via engine onboarding; 18 passages). Its **(b) schema half is now superseded** by this fuller model — the structure is a researcher-led discovery, not a schema I should pre-draw.

*Filed 2026-07-11. Grounded; no build performed.*
