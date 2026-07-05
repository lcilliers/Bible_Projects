# Root cause — what and when the book-study build went wrong

> Prompted by the researcher (2026-07-05): *"I worked closely with you creating a re-usable script that became the baseline for the book study, before we started. Locate that script-preparation work, confirm if that script was properly created, and if it was used in the book analysis."* This report answers exactly that, with commit- and code-level evidence. No remediation proposed here — this is the anchor of the position.

---

## 1. The baseline that was prepared (BEFORE the book study) — and it was created PROPERLY

On **2026-07-02**, working together, we built and proved an **index-driven, two-gate** lexical build. It is documented as **§12 of the method** ([wa-verse-analysis-method-v1-20260702.md](../../Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md)), titled *"The build is INDEX-DRIVEN — the two gates (fix, 2026-07-02)"*:

- **Gate 1 — primary term:** the span is a tagged non-T2 term (has a `verse_context`) → lexicalise + link.
- **Gate 2 — relevant, not yet a term:** the span is a **content word not yet tagged** → lexicalise anyway, keyed on `verse_span_id`. *"Content words carry the IB impact; skipping them guts the lexical."*

The rule is explicit: **the build starts from `verse_span_index` (every span of the verse), NOT from a pre-tagged term list.** That is precisely the rule you stated — the full span of each verse comes into focus, and content spans not already tagged are captured, not skipped.

**It was properly created — evidence:**
- Commit **`fe3a9633` (2026-07-02): "FIX the missing second gate — index-driven build; content spans lexicalised."**
- Pilot writer **`scripts/_apply_write_ruthlessness_index_driven_v3_20260702.py`** — its own header (line 5) reads: *"Drives off `verse_span_index` (every span), not the pre-tagged term list, so BOTH gates run,"* and line 44 confirms the query is `FROM verse_span_index`.
- Migration **M62** (`_apply_ve_lexical_span_keyable_v1_20260702.py`) made `ve_lexical` span-keyable **for exactly this** — so a content span with no `verse_context` could still be recorded, keyed on `verse_span_id`.
- **Proof of effect:** on the ruthlessness pilot, content-span coverage rose **14% → 94%** (197/210 content spans). The earlier seed-only build had skipped ~86% of spans — including `dread`, `deal-shrewdly`, `taskmasters`. Filed: `wa-span-index-coverage-5passages-20260702.md`.

**Verdict on Q "was the script properly created": YES.** The index-driven baseline was built, documented in the method, backed by a schema migration, and proven to lift coverage from 14% to 94%.

---

## 2. Was it USED in the book analysis? — SPLIT: poetic YES, narrative NO

The book study ran as two separate pipelines. They did **not** share the build path.

### Poetic / prophetic books — USED the baseline (index-driven)
`scripts/_apply_poetic_chapter_lexical_v1_20260702.py` (created 2026-07-02) builds each chapter reading **from the index**:
- line 65: `FROM verse_span_index si JOIN verse v … WHERE v.reference=?` — surfaces **every span**.
- line 185: `ve_lexical` keyed by `verse_span_id` OR `verse_context` — Gate 2 in operation.

So Psalms, Proverbs, Job, Isaiah, Jeremiah, Ezekiel, the Twelve, etc. were read **index-driven** — the baseline was followed. (This is why the earlier scope check found the prophets were *not* skipped at the lexical level.)

### Narrative books — did NOT use the baseline (seed-driven)
For the narratives (Genesis, Exodus, Leviticus), a **new set of scripts was written on 2026-07-04** — and they query the **seed** (`wa_verse_records`), not the index:

| Script (created 2026-07-04) | Role | What it queries | Gate 2? |
|---|---|---|---|
| `_probe_passage_material_v1_20260704.py` (line 24) | surfaces the spans **to read** | `FROM wa_verse_records w JOIN mti_terms mt` | **NO** — only seed spans surface |
| `_check_passage_reading_coverage_v1_20260704.py` (line 51) | the **coverage gate** | `FROM wa_verse_records w JOIN mti_terms mt` | **NO** — checks seed coverage only |
| `_apply_file_passage_lexical_prose_v1_20260704.py` | files the reading | (prose_section) | n/a |

**Neither the narrative probe nor the narrative gate touches `verse_span_index`.** The probe can only show the reader spans that are already in the seed; the gate can only verify the reading covers seed spans. **Gate 2 — the whole point of the 2026-07-02 fix — is absent from the narrative pipeline.**

**Verdict on Q "was it used in the book analysis": PARTIALLY.** Used for the poetic/prophetic books; **not** used for the narrative books.

---

## 3. WHAT went wrong, and WHEN — precisely

- **WHEN:** **2026-07-04**, when the narrative book-study scripts (`_probe_passage_material_v1`, `_check_passage_reading_coverage_v1`) were written. The index-driven baseline existed and was proven two days earlier (2026-07-02) and was in live use for the poetic books — but the narrative pipeline was authored fresh against `wa_verse_records` instead of `verse_span_index`.

- **WHAT:** the narrative pipeline **reverted to the seed-only build the 2026-07-02 fix had explicitly replaced.** Two consequences, both structural:
  1. **The reader never saw the orphans.** The probe surfaces only seed spans, so a content span not already a registered term (e.g. `ahev` love, `avaq` wrestle, `gaal` redeem, `lachats` oppress) was never even presented to be read. Gate 2 was silently dropped.
  2. **The gate is circular.** It checks the reading against the seed — so it reports **CLEAN** when the reading covers the seed, regardless of what the *text* holds. "Complete" came to mean "complete vs the March seed," not "complete vs the verse."

- **The regression was invisible** because the poetic pipeline (which people could point to) *was* index-driven, and because the gate's own "CLEAN" verdict was self-confirming. The narrative build looked governed while skipping the second gate entirely.

- **Every later step inherited it.** Genesis, Exodus, and Leviticus span-depth work all ran on the seed-driven narrative pipeline. My Gate-1 "remediation" this session added to `ve_lexical`/`mti_terms` but still never re-based the narrative build on the index — so it did not correct the root, it worked around it.

---

## 4. One-line answers to the three questions

1. **Located?** Yes — the baseline is method §12 (2026-07-02) + pilot writer `_apply_write_ruthlessness_index_driven_v3_20260702.py` + migration M62.
2. **Properly created?** **Yes** — index-driven two-gate, documented, migration-backed, proven 14% → 94% on the ruthlessness pilot.
3. **Used in the book analysis?** **Poetic/prophetic: yes** (index-driven). **Narrative (Genesis/Exodus/Leviticus): no** — new scripts on 2026-07-04 queried the seed (`wa_verse_records`), dropping Gate 2 and making the coverage gate circular.

*Filed 2026-07-05 as the root-cause anchor. Evidence: commits `fe3a9633`, `c11596a4`; scripts `_apply_write_ruthlessness_index_driven_v3_20260702.py`, `_apply_poetic_chapter_lexical_v1_20260702.py`, `_probe_passage_material_v1_20260704.py`, `_check_passage_reading_coverage_v1_20260704.py`; method §12 in `wa-verse-analysis-method-v1-20260702.md`. NT excluded (not yet started).*
