# Action S Close — Session A Extract Generator — 2026-04-20

| Field | Value |
|---|---|
| Filename | wa-global-action-s-close-20260420.md |
| Action | S (from programme control v1) — build `generate_session_a_extract.py` |
| Purpose | M4 unblocker — Session A prose population for any registry |
| Status | **CLOSED** — generator built, tested on all 5 BANKED registries |
| Produced | 2026-04-20 |

---

## Outcome

**Action S closed.** `scripts/generate_session_a_extract.py` built from scratch (~1,100 lines). Tested on all 5 BANKED registries (r35, r62, r134, r206, r207) — clean runs producing 10,852 to 20,960 words per registry (total ~76k words across 5 registries).

All 6 sections render from real DB data per the approved Session A advice (§3 content spec, §5 section order, §6 ordering rationale):

1. Summary — registry orientation + word_synopsis placeholder + counts
2. Meaning — raw meaning + structured senses + stems + LSJ (Greek)
3. Terms — OWNER + XREF with MTI status, MTI flags, data-quality flags, term-level dimension aggregation, root family, related words, verse counts
4. Verses — group-first with dimensions, dominant_subject, anchor/related/set-aside verses + ESV text
5. Pointers — SB findings + catalogue question mapping, SB/SD research flags, phase2 term advisories, cross-registry links
6. Questions — universal catalogue (194 questions grouped by section) + any registry-specific extensions

---

## Script characteristics

| Aspect | Value |
|---|---|
| Path | `scripts/generate_session_a_extract.py` |
| Language | Python 3.14 stdlib + sqlite3 (no external deps) |
| Invocation | `python scripts/generate_session_a_extract.py --registry=N` |
| CLI flags | `--registry=N` (required) · `--out-dir=PATH` · `--emit-patch=FILE` · `--apply` · `--no-md` · `--db=PATH` |
| Default output | `outputs/session_a/wa-{NNN}-{word}-sessiona-{YYYYMMDD}.md` |
| Markdown format | PROSE_SECTION markers per prose-store design §5.1 |
| Patch format | JSON PROSE patch with `insert` (first run) or `session_a_replace` (regeneration) ops per applicator §15 |
| Regeneration semantics | Per Session A advice Q5 — `session_a_replace` UPDATE in place (exception to supersede rule) |
| Schema version | Compatible with schema v3.10.0 post-DBR |

---

## Test matrix — 5 BANKED registries

All 5 runs clean (no errors, no warnings):

| Registry | Word | Cluster | OWN | XREF | V | G | Words rendered | MD path |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 35 | covetousness | C13 | 7 | 4 | 25 | 10 | 14,538 | wa-035-covetousness-sessiona-20260420.md |
| 62 | fellowship | C17 | 13 | 0 | 89 | 19 | 16,603 | wa-062-fellowship-sessiona-20260420.md |
| 134 | renewal | C21 | 7 | 3 | 22 | 5 | 10,852 | wa-134-renewal-sessiona-20260420.md |
| 206 | vulnerability | C22 | 17 | 1 | 128 | 34 | 20,960 | wa-206-vulnerability-sessiona-20260420.md |
| 207 | blindness (spiritual) | C21 | 7 | 2 | 103 | 12 | 13,305 | wa-207-blindness_spiritual-sessiona-20260420.md |
| **Total** | | | **51** | **10** | **367** | **80** | **76,258** | |

Patch emission also tested (r62 + r206). Patch structure validates:

- Patch ID format: `PATCH-{date}-SESSIONA-R{NNN}-V1`
- 6 operations per registry (one per section)
- Operations are `insert` (first-time) correctly — registry has no existing Session A prose rows
- Section type IDs route correctly to their label-matched types (see discipline note below)

---

## Discipline note — seed mismatch discovered and handled

During build, discovered `prose_section_type` seed has chapters 3 and 4 labels swapped vs Session A advice §5:

| id | code | DB chapter_no | DB label | Advice says should be |
|---:|---|---:|---|---|
| 3 | sa_s1_d3 | 3 | Session A — Verses | Session A — Terms |
| 4 | sa_s1_d4 | 4 | Session A — Terms | Session A — Verses |

**Did not silently modify the seed** — catalogue row modification needs researcher approval. Raised as **OT-DBR-014** (LOW priority; no operational blocker).

**Generator workaround:** dispatch by **label keyword** (summary/meaning/terms/verses/pointers/questions) rather than by chapter_no. This makes the generator robust to the seed mismatch — Terms content routes to the section_type whose label contains "terms" (id=4) regardless of its recorded chapter_no. Same for Verses routing to id=3.

Verified routing in patch output: `SA-R062-TERMS → section_type_id=4 (Session A — Terms)`, `SA-R062-VERSES → section_type_id=3 (Session A — Verses)`. Content matches label.

This is a defensive design choice — generator keeps working even if the seed is corrected later via OT-DBR-014 (at which point `db_chapter_no` will align with `semantic_order`).

---

## Deviations from advice (design notes)

These are pragmatic deviations from the Session A advice §3 field lists, made because DB schema differed from the advice document:

| Advice called for | DB has | Resolution |
|---|---|---|
| `wa_meaning_parsed.raw_meaning_text` | Raw text lives on `wa_term_inventory.meaning` | Generator reads raw from wa_term_inventory; wa_meaning_parsed used only for metadata (top_sense_count, stems, parse_version) |
| `wa_meaning_sense.gloss/domain/register/sense_order` | Has `level_code, level_depth, sense_text, stem_label, domain_tag, sort_order` | Mapped: `sort_order` for ordering; `level_code(d{depth})` for hierarchy; `stem_label`/`domain_tag` in their own columns |
| `wa_meaning_stem.stem_label/stem_text/sense_link` | Has `stem_name, stem_type, sense_count, top_sense_text` | Mapped |
| `wa_lsj_parsed.lsj_entry/short_gloss/attested_forms` | Has `raw_lsj, lsj_gloss, lsj_domains, lsj_philosophical_note, lsj_etymology_note, lsj_cognate_forms` | Mapped to richer schema |
| `wa_term_root_family.root_meaning/related_term_count` | Has `root_gloss, note` | Mapped |
| `wa_term_related_words.related_strongs/related_gloss/relation_type` | Has `strongs_number, gloss, transliteration, relationship_note` | Mapped |
| `wa_data_quality_flags.resolved` | No `resolved` column — just `description, last_changed` | Removed "resolved" column from the rendered table |
| `wa_session_b_findings.registry_no/finding_code/finding_text/delete_flagged` | Has `registry_id (FK), finding_id (text code), finding, delete_flag` | Mapped with correct names |
| `wa_cross_registry_links.source_registry_no/target_registry_no/delete_flagged` | Uses `file_id (→ wa_file_index → registry), linked_word, linked_registry_id, connection_type_id` — no soft-delete column | Adjusted; keyed by file_id → wa_file_index |
| `wa_crosslink_type.link_type_code/link_type_label` | Has `type_code, description` | Mapped |
| `wa_obs_question_catalogue.id` as PK | Has `obs_id` as PK | Used `obs_id` |

**Implication for advice doc:** the Session A advice document §3 field lists should be refreshed against the live schema. Low priority — the generator handles the reality.

---

## What Action S unblocks (macro M4 state)

Per programme control v1 §1 M4 — Session A prose population:

- **Before S:** No tooling to produce Session A prose. `prose_section_count = 0` across all 213 registries. Session B Stage 1 entry blocked for all BANKED registries.
- **After S:** Generator ready. Any registry can produce Session A extract on demand. BANKED registries (5) ready to flow into Stage 1 as soon as `word_synopsis` is authored.

**Remaining blocker on M4 completion:** researcher-authored `word_synopsis` per word (per Session A advice §3 Section 1; M21 column added). The 5 BANKED extracts currently render "Word synopsis not yet authored" placeholder text in Section 1.2.

---

## Recommended next moves

1. **Researcher reviews one generated extract** (e.g. r62 fellowship — cleanest) and confirms the output format matches analytical expectations. Feedback can refine rendering without re-architecting the generator.

2. **Researcher authors `word_synopsis`** for the 5 BANKED registries (~1-2 sentences each, 10 minutes of work). Once populated, regenerate — synopses flow into Section 1.2.

3. **Apply Session A patches** for the 5 BANKED registries — pushes the 6×5 = 30 prose_section rows into the DB, enabling FTS5 search across the extracts and making them addressable via the prose store.

4. **Continue to Action U** (C01 Dimension Review directive) — next in programme control queue.

---

## Artefacts produced

| Path | Size | Purpose |
|---|---|---|
| `scripts/generate_session_a_extract.py` | ~1,105 lines | Generator script (this action's primary artefact) |
| `outputs/session_a/wa-035-covetousness-sessiona-20260420.md` | ~14.5k words | r35 extract |
| `outputs/session_a/wa-062-fellowship-sessiona-20260420.md` | ~16.6k words | r62 extract |
| `outputs/session_a/wa-062-fellowship-sessiona-patch-20260420.json` | — | r62 PROSE patch (ready to apply) |
| `outputs/session_a/wa-134-renewal-sessiona-20260420.md` | ~10.9k words | r134 extract |
| `outputs/session_a/wa-206-vulnerability-sessiona-20260420.md` | ~21.0k words | r206 extract (largest) |
| `outputs/session_a/wa-206-vulnerability-sessiona-patch-20260420.json` | — | r206 PROSE patch |
| `outputs/session_a/wa-207-blindness_spiritual-sessiona-20260420.md` | ~13.3k words | r207 extract |
| `outputs/wa-global-outstanding-tasks-v1-20260419.md` | — | OT-DBR-014 raised |

---

*End of Action S close record — 2026-04-20*
