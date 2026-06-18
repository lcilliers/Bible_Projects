# Constitutional-seat map for `location` — complete proposal (v1)

**File:** wa-location-seat-map-proposal-v1-20260618.md · **Type:** lexical design proposal (markdown)
**Date:** 2026-06-18 · **Supersedes the open questions in** `wa-location-engine-fix-plan-v1-20260618.md` (I'm proposing the answers, not asking them).
**Method:** mined `lexicon` for every term in the corpus whose definition denotes an inner-being seat/organ, separated seats (vessels) from faculties (cognitive acts), and leveled them per standard OT/NT anthropology.

---

## The principle the old rule (and the audit) missed
`location` must be derived from **(a) the complete seat-lemma inventory** the lexicon actually contains, and **(b) the per-occurrence contextual sense** — not a hand-seeded 8-lemma list gated on the *dictionary* gloss. Three different lemmas fail the same way today (ruach, qereb, racham): the dictionary lists several senses, and only the verse's sense tells you whether it's the inner-being seat or a non-seat sense (wind / "in the midst of the camp" / childbirth). One fix covers all three.

## Proposed seat levels (complete; counts = term-in-verse units)

| level | lemmas (Strong's) | units | status today | provenance / gate |
|---|---|---:|---|---|
| **heart** | leb H3820, lebab H3824, kardia G2588 | 749 | ✅ covered | mechanical |
| **soul** | nephesh H5315, psyche G5590 | 635 | ✅ covered | mechanical |
| **spirit** | ruach H7307, **neshamah H5397**, pneuma G4151 | 368 | ⚠ broken gate; neshamah missing | **sense-gate** (wind/breath ≠ seat) |
| **flesh** | basar H1320, **besar (Aram) H1321**, sarx G4561 | 234 | ⚠ Aramaic missing | mechanical (light sense-care: "body/kin/meat") |
| **mind** | **nous G3563, dianoia G1271, phren G5424** | 35 | ❌ absent | mechanical (Greek-only; Hebrew "mind" = leb→heart) |
| **conscience** | **suneidesis G4893; + kilyah H3629 (Heb. "reins")** | 42 | ❌ absent | mechanical |
| **inward-parts (viscera)** | **qereb H7130, me'eh H4578, splanchna G4698, kabed H3516** | ~210 | ❌ absent | **sense-gate** (qereb often plain locative) |

**New seat coverage added: ~290 term-in-verse units** that currently get no location at all.

## The leveling decisions (made, with rationale)
1. **mind = Greek only** (nous/dianoia/phren). Hebrew has no separate mind-word — `leb`'s own gloss is *"inner man, mind, will, heart, understanding."* So Hebrew cognition stays under **heart**; only Greek gets a distinct `mind`. This is the standard treatment and avoids inventing a Hebrew "mind" the language doesn't have.
2. **kidneys/reins (kilyah) → conscience, not viscera.** Scripture pairs the kidneys with the heart precisely as the seat God *searches and tests* — the moral/conscience self (Ps 7:9; 26:2; Jer 11:20; 17:10). It is the Hebrew analogue of *suneidesis*, so it belongs with **conscience**, not the generic viscera.
3. **bowels / inward part / liver → one `inward-parts (viscera)` level** (me'eh, qereb, splanchna, kabed). These are the OT/NT somatic seat of churning compassion and distress ("my bowels are troubled"; "my liver is poured out", Lam 2:11; *splanchna* = compassion). Grouping them avoids 4 thinly-populated levels while keeping the distinct *idea* (visceral affect) separate from heart/soul.
4. **womb (racham/rechem) → NOT a location level.** `racham` as a tagged term is almost always the *compassion* state itself (an inner-being term, belongs in an M-cluster), and `rechem` is the literal childbirth womb (not inner-being). Treating it as a seat would double-count. Exclude; revisit only if a verse seats an affect *in* the womb.

## The sense-gate (the fix that makes it "use the full lexical data")
Replace the gloss-based gate with a **per-occurrence sense** test on the three multi-sense lemmas:
- **spirit** (ruach/pneuma): seat unless the verse's sense reads *wind / breath / lifeless-body*.
- **inward-part** (qereb): seat only when it denotes the *person's* inner being ("hot within me", Ps 39:3) — **not** the locative "in the midst of [the camp/land/people]".
- **flesh** (basar/sarx): seat when it denotes the creaturely self; lighter care for plain "body / meat / kinsman".

Gate on the per-occurrence `target_word`/STEP sense the pipeline already stores — route to the verse-read only when the *context* is genuinely ambiguous, never on the dictionary listing every sense.

## Build steps (mechanical, on your approval)
1. Extend `SEAT` in `scripts/_ve_engine_v2.py` to the table above (zero-padded forms per `reference_strongs_zero_padded_4digit_in_db`; verify each lemma's DB sub-entries).
2. Rewrite the seat gate to test per-occurrence sense (covers spirit + qereb + flesh uniformly).
3. Re-run the mechanical `location` pass corpus-wide; route only genuinely-ambiguous cases to a small read.
4. **Diff before/after** and report (expect: spirit 28 → low-hundreds; new mind ~35, conscience ~42, inward-parts ~150+ after the qereb sense-gate).
5. Add a standing **lexical-completeness check** to the VE audit so a stub seed list can't pass again.

---

## IMPLEMENTED — 2026-06-18 (results)
Engine change applied in `scripts/_ve_engine_v2.py` (single source of truth, used by the writer): full seat inventory + a `seat_level()` resolver that gates on the **per-occurrence surface** (`verse_morphology.surface` = the ESV word in the verse), never the dictionary gloss. Corpus rerun via `_apply_generate_ve_lexical_v2.py --live` (38,969 units; all read-resolved values preserved; reads unchanged: valence 26,788 / object-type 12,102 / divine 4,540 / cause 3,431 / location 28). DB pre-snapshot: `backups/bible_research_pre-location-seatfix-20260618.db`.

**Location distribution — before → after:**

| level | before | after | Δ |
|---|---:|---:|---:|
| heart | 2,604 | 2,623 | +19 |
| soul | 2,229 | 2,229 | 0 |
| spirit | 28 | **263** | **+235** |
| flesh | 627 | 596 | −31 (meat/kin dropped) |
| mind | 0 | **109** | +109 |
| conscience | 0 | **149** | +149 |
| inward-parts | 0 | **171** | +171 |
| UNRESOLVED | 226 | 342 | +116 (qereb 'among/midst' → read) |

**Completeness guard added:** `scripts/_check_ve_seat_completeness.py` — scans the corpus for any seat-denoting lemma not in `SEAT`; run it after engine changes / in the VE audit. It immediately caught two further gaps in my own first map — **Aramaic H7308 *ruach* ("seat of the mind")** and **Aramaic H3826 *libbah* "heart"** — plus she'er H7607 (flesh); all three added and the rerun repeated. The guard's remaining flags are reviewable non-seats (faculty-acts, etc.).

**Open follow-ups:**
1. **342 UNRESOLVED location rows** (mostly qereb 'among/midst') → run the governed location read to resolve.
2. **cheq H2436 ("bosom") — researcher call.** Mostly physical (lap/embrace) but has seat-of-emotion usage (Ecc 7:9 "anger rests in the bosom of fools"; Ps 35:13). Flagged, not auto-added.
