# Directive DIR-20260501-001 — Cross-registry term extract for R099 kindness Session B

> Produced by: wa-directive-instruction-v1_3-20260422
> Governed by: wa-global-general-rules [current]
> Registry: 099
> Produced date: 2026-05-01
> Researcher approval: PENDING

---

## Motivation

Registry 099 (kindness) is in Session B Stage 2a complete, Stage 2b pending. The Stage 2a reading has confirmed that the OWNER vocabulary of Reg 099 does not carry the primary Hebrew and Greek kindness semantic content. The central biblical kindness terms — H2617A (chesed, "kindness/steadfast love", 169 verses, owned by Reg 103 love) and G5544 (chrēstotēs, "kindness", 7 verses, owned by Reg 67 goodness) — are XREF-only in Reg 099. Additionally, H2623 (chasid, "pious/loyal one", 33 verses, Reg 103) names the person characterised by chesed, and H2616A (chasad, "be kind" verbal, 2 verses, Reg 23 compassion) is the action form of the same root. Their ownership in other registries is a programme sequencing artefact, not an analytical decision.

The researcher has authorised introduction of supplementary term data from these registries as source material for Reg 099 Stage 2b analysis, on the grounds that the missing data is at the heart of the analysis of kindness and that the instruction provides for introducing additional research data where a material gap exists.

This directive requests CC to extract the relevant term and group data for four specified terms from the live database, formatted for use as analytical source material alongside the Reg 099 readiness output.

---

## Scope

**Terms required (4):**

| Priority | Strongs | Transliteration | Gloss | Owner Reg | Rationale |
|---|---|---|---|---|---|
| 1 | H2617A | chesed | kindness / steadfast love | 103 | Primary Hebrew kindness term — 169 verses — essential |
| 1 | G5544 | chrēstotēs | kindness | 67 | Primary Greek abstract kindness noun — 7 verses — essential |
| 2 | H2623 | chasid | pious / loyal one | 103 | Person characterised by chesed — 33 verses — strongly recommended |
| 2 | H2616A | chasad | be kind (verbal) | 23 | Verbal root of chesed — 2 verses — recommended |

**Tables to query (per term):**

1. `mti_terms` — term identity fields: `id`, `strongs_number`, `transliteration`, `gloss`, `language`, `status`, `md_version`
2. `wa_meaning_parsed` — meaning parse: all rows for each `mti_term_id`; fields `sense_level`, `sense_code`, `sense_text`, `causative`, `domain_tags`
3. `wa_meaning_sense` — sense rows: all rows for each `mti_term_id`; fields `sense_code`, `sense_text`, `depth`, `parent_code`
4. `wa_term_related_words` — root family and related words: all rows for each `mti_term_id`; fields `root_family`, `related_strongs`, `related_gloss`, `relationship_type`
5. `verse_context` — verse context groups and relevant verses: for each `mti_term_id`, all rows where `is_relevant = 1` OR `is_anchor = 1`; fields `group_code`, `verse_ref`, `verse_text`, `is_relevant`, `is_anchor`, `set_aside_reason`, `target_word`
6. `verse_context_group` — group descriptions and dimension assignments: all active groups for each `mti_term_id`; fields `group_code`, `context_description`, `dimension_id`, `dimension_confidence`, `dominant_subject`, `anchor_count`, `relevant_count`, `set_aside_count`, `notes`
7. `wa_dimension_index` — dimension labels: join to `verse_context_group.dimension_id` to return `dimension_label` alongside each group

**Registry context:** The owning registry for each term is as specified above. CC should retrieve group and verse data as recorded in the database regardless of registry assignment — the OWNER registry assignment does not need to change; this is a read-only extract for analytical use.

---

## Outcome Required

CC produces a structured markdown extract (`wa-099-kindness-crossreg-extract-v1-{YYYYMMDD}.md`) containing the following sections for each of the four terms, in priority order (H2617A first, G5544 second, H2623 third, H2616A fourth):

**Per term — Section A: Term identity and lexical foundation**

```
### {strongs} — {transliteration} "{gloss}"

**Identity:** mti={id} · language={language} · status={status} · md_v={md_version}
**Owner registry:** {owner_reg_no} ({owner_word})

**Meaning parse:** {n} top senses · causative={True/False} · domain_tags={True/False}

Senses:
- {sense_code}: {sense_text}
[... all senses at depth 1]

Sub-senses (depth > 1): {n} entries
[... all sub-senses, first 20 if >20]

**Root family:** {root_family} — {root_gloss}

**Related words ({n} total; sample of up to 20):**
- {related_strongs} {related_gloss}
[...]
```

**Per term — Section B: Verse context groups**

```
### {strongs} — {n} active groups

**Group `{group_code}`** ({relevant_count} relevant · {anchor_count} anchor verse(s) · dimension: {dimension_id} — {dimension_label} · confidence: {dimension_confidence} · dominant_subject: {dominant_subject})
  - *{context_description}*
  - notes: {notes if present}

[... all active groups for this term]
```

**Per term — Section C: Anchor verses (verbatim)**

For each group, anchor verses (`is_anchor = 1`) listed with full verse text, in group order:

```
**Group `{group_code}`** — anchor verses:

- **{verse_ref}** 🔵 (✓) *target: {target_word}*
  > {verse_text}
[... all anchor verses for this group]
```

**Per term — Section D: All relevant verses (verbatim)**

For each group, all `is_relevant = 1` verses listed with full verse text. This is the complete classified verse set for analytical use.

```
**Group `{group_code}`** — all relevant verses ({relevant_count} total):

- **{verse_ref}** (✓) *target: {target_word}*
  > {verse_text}
  [set_aside_reason if applicable]
[...]
```

**Format:** Markdown. Section headers per term using the pattern above. Output to be complete — no truncation of verse text. If any section produces >500 rows (verse records), CC notes the count and provides the anchor verses in full; provides the full relevant set only if feasible within a single output file, otherwise notes the count and provides the first 100 relevant verses with a note that the remainder is available on request.

---

## Completion Confirmation

CC returns the following confirmation queries and results after the extract file is written:

**Query 1 — Term identity confirmed:**
```sql
SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language, mt.status,
       wr.registry_no, wr.word
FROM mti_terms mt
JOIN word_registry wr ON wr.id = mt.owning_registry_id
WHERE mt.strongs_number IN ('H2617A', 'G5544', 'H2623', 'H2616A')
ORDER BY CASE mt.strongs_number
  WHEN 'H2617A' THEN 1
  WHEN 'G5544' THEN 2
  WHEN 'H2623' THEN 3
  WHEN 'H2616A' THEN 4
END;
```
Expected: 4 rows, one per term, with owning registry confirmed.

**Query 2 — Group counts per term:**
```sql
SELECT mt.strongs_number, COUNT(vcg.id) AS active_group_count,
       SUM(vcg.relevant_count) AS total_relevant_verses,
       SUM(vcg.anchor_count) AS total_anchor_verses
FROM mti_terms mt
JOIN verse_context_group vcg ON vcg.mti_term_id = mt.id
  AND (vcg.dissolved = 0 OR vcg.dissolved IS NULL)
WHERE mt.strongs_number IN ('H2617A', 'G5544', 'H2623', 'H2616A')
GROUP BY mt.strongs_number;
```
Expected: up to 4 rows (terms with 0 groups will not appear — note if any term has 0 groups). Verse counts to be returned as-is; no expected values specified in advance.

**Query 3 — Anchor verse count per term:**
```sql
SELECT mt.strongs_number, COUNT(vc.id) AS anchor_verse_count
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
  AND vc.is_anchor = 1
  AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
WHERE mt.strongs_number IN ('H2617A', 'G5544', 'H2623', 'H2616A')
GROUP BY mt.strongs_number;
```
Expected: counts returned as-is for verification.

**Query 4 — Extract file written:**
CC confirms the output filename and byte size of the written extract file.

---

## Notes

1. **Read-only operation.** This directive makes no database writes. It is a reporting extract only. No fields are changed, no rows inserted or updated.

2. **Owner registry does not change.** The extract is for analytical use in Reg 099 Session B only. H2617A remains owned by Reg 103, G5544 by Reg 67, H2623 by Reg 103, H2616A by Reg 23. No OWNER reassignment is intended or implied.

3. **Column name uncertainty.** The exact column names for `owning_registry_id` on `mti_terms`, and for `dissolved`/`delete_flagged` on `verse_context_group`, should be verified against the live schema (`PRAGMA table_info(mti_terms)` etc.) before query execution. If column names differ from those used above, CC should adjust the queries accordingly and note the actual column names in the completion confirmation. The database schema document (database-schema-v3_17_0-20260427.json) is the reference.

4. **H2617A verse volume.** H2617A (chesed) has 169 corpus verses. If all are classified relevant, the Section D output for this term will be substantial. CC should include all anchor verses in full and provide as many relevant verses as feasible. If the full relevant set cannot be included without exceeding a practical file size, CC notes the count and truncates Section D for H2617A at 100 verses with a note.

5. **Subsequent use.** After researcher approval and CC execution, the extract will be introduced as supplementary source material for Reg 099 Stage 2b alongside the readiness output. A RESEARCHER_DECISION entry will be added to the Reg 099 obslog recording the introduction of cross-registry source material and the specific terms covered.

6. **Output filename:** `wa-099-kindness-crossreg-extract-v1-{YYYYMMDD}.md` where `{YYYYMMDD}` is the compact date of extraction.
