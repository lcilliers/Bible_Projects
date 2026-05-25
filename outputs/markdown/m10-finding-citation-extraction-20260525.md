# M10 finding_citation extraction — 2026-05-25

Schema migration **M52** + extraction pass against the M10 Phase 9 corpus.

## What was done

1. **M52 migration applied** (3.25.0 → 3.26.0). Created `finding_citation` table
   (polymorphic: `source_table` ∈ {cluster_finding, cluster_observation}, three
   `citation_type` values: verse / strongs / cross_char).
   Script: `scripts/_migrate_m52_finding_citation_table_20260525.py`.

2. **Extraction script** built and run live across:
   - cluster_finding M10: **4,158 rows** (189 prompts × 22 chars)
   - cluster_observation M10: **58 rows** (15 CLUSTER_SYNTHESIS + 27 TIER_READING_GUIDE
     + 8 INTEGRATION_NOTE + 7 INTER_RELATIONSHIP + 1 CROSS_CLUSTER_HANDOFF)

   Script: `scripts/_extract_finding_citations_v1_20260525.py`.

3. **Patterns**
   - **verse**: book-abbr + chap:verse, ranges expanded to atomic verses
     (separators: en/em-dash, hyphen, comma, semicolon). Book aliases handled
     (1Jo→1Jn, Amos→Amo, Jhn→Joh, etc.).
   - **strongs**: `[HG]\d+[A-Z]?`.
   - **cross_char**: `CHAR-N` mid-body. The leading `**[CHAR-N]**` scope marker
     on cluster_finding rows is stripped. Self-references (CHAR-N citation
     matching the row's own char_seq) are also excluded — these are prose
     noise ("the CHAR-N corpus shows…", "12× [CHAR-N] ✓"), not genuine
     cross-references.

## Totals

| citation_type | rows  |
|--------------|-------|
| verse        | 13,141 |
| vcg          | 8,602 *(derived layer — see §4)* |
| cross_char   | 1,703 |
| strongs      | 381   |
| **TOTAL**    | **23,827** |

## Notable signals

**Top-cited verses** (single-row, post range expansion):
Jer 2:35 (126), Joh 8:34 (120), 1Ki 8:47 (108), 2Pe 2:14 (102), 1Jn 3:6 (94),
Gal 2:13 (93), 1Jn 3:8 (92), 2Sa 24:10 (92), Heb 10:26 (90), Jam 1:14 (87).

**Top Strong's** (M10 lexical core):
H2398 cha.ta "to sin" (50), H5771G `awon "iniquity" (24), G0264 hamartano (21),
H6586 pasha` "transgress" (18), H2403B chatta'ah (16).

**Top characteristics-as-targets** (which char gets cited most by others):
CHAR-1 Wilful sinning (328), CHAR-3 Confession (158), CHAR-13 Sin as divine
record (134), CHAR-17 Guilt as inner-being state (133), CHAR-6 Habitual
defection (115).

**Top cross-char pairs** (analytically meaningful):
- CHAR-2 Unintentional → CHAR-1 Wilful (49)  *the natural contrast pair*
- CHAR-17 Guilt → CHAR-13 Sin as divine record (43)
- CHAR-18 Iniquity → CHAR-17 Guilt (37)
- CHAR-20 Faithlessness → CHAR-19 Transgression (34)
- CHAR-12 Sin as enslaving → CHAR-11 Sin as universal (32)
- CHAR-14 Forgiveness → CHAR-13 Sin as divine record (32)
- CHAR-22 Injustice → CHAR-21 Perversion (32)

**Cluster-wide anchor verses** (cited across 5+ different characteristics):
Isa 59:2 (5 chars, 42 cites), Lev 4:3 (5 chars, 40 cites). Citation is mostly
concentrated within a single char's corpus — verses bridging multiple chars
are rare and worth noting.

## 4. VCG enrichment layer

The Phase 9 findings were authored at characteristic scope, not VCG scope —
no `M10-X-VCG-NN` codes appear directly in the finding prose. To restore
explicit traceability between findings and the programme's evidence-grouping
units, a derived `vcg` citation_type is produced by joining
`finding_citation.citation_value` (verse refs) → `wa_verse_records.reference`
→ `verse_context.verse_record_id` → `verse_context_group.id` → `group_code`,
filtered to `M10-%`.

Script: `scripts/_enrich_finding_citations_with_vcg_v1_20260525.py`.

Dedup rule: one `vcg` row per (source_id, vcg_code). Multiple verse citations
pointing to the same VCG collapse to one VCG row.

**Coverage:**

- Verse citations matchable to an M10 VCG: **12,171 / 13,141 (93%)**
  (the remaining 970 are cross-cluster verse refs or set-aside verses not
   in M10's verse_context corpus)
- Source rows with >=1 VCG tag: **3,318 / 4,216 (78.7%)**
  (most uncovered rows are silent findings, with 638 evidenced findings
   citing only cross-cluster verses)
- All 68 M10 VCGs are referenced at least once.

**Top-referenced VCGs:**

- `M10-V-VCG-05` Sin as objective burden before God: the broad chat.tat
  record (540 findings, 113V) — the corpus's gravitational centre.
- `M10-F-VCG-09` Transgression as personal moral breach: Job, Psalms,
  wisdom (312 findings).
- `M10-V-VCG-04` Jeroboam-sin legacy: the named sin as recorded pattern
  (251 findings).
- `M10-E-VCG-03` Iniquity in divine memory: what God sees and does not
  forget (250 findings).
- `M10-H-VCG-03` Perversion of mind, will, and way: the inwardly twisted
  person (228 findings).

**Worked example** (from the researcher's question: Eze 14:3 and the heart-
location finding):

```sql
SELECT cf.id, c.char_seq, c.short_name, vcg_list
FROM finding_citation fc
JOIN cluster_finding cf  ON cf.id = fc.source_id
                         AND fc.source_table='cluster_finding'
JOIN characteristic   c  ON c.id  = cf.characteristic_id
WHERE fc.citation_type='verse' AND fc.citation_value='Eze 14:3'
```

Returns CHAR-18 (Iniquity as accumulated moral crime) findings tagged with
M10-E-VCG-01..M10-E-VCG-08 (the Iniquity sub-group VCGs), plus secondary
references in M10-F, M10-J, M10-V. Exactly the kind of cross-reference the
researcher was asking about.

## Idempotency

Both scripts (extraction and VCG enrichment) wipe their own rows for the
targeted `(source_table, source_id)` pairs before re-inserting. Safe to
re-run after finding-text or VCG-assignment revisions.

## Note on CHECK constraint

The M52 migration's CHECK constraint initially included only
`('verse','strongs','cross_char')`. After the VCG enrichment layer was
designed, the constraint was widened in-place (table swap) to include
`'vcg'`, and the M52 migration source was updated to reflect the final
four-value set so future fresh DB initialisations get the correct CHECK.
Backup: `backups/bible_research_backup_20260525_051745_M52-check-widen.db`.

## Next steps (when ready)

- Roll both passes (extraction + VCG enrichment) across other clusters
  with Phase 9 findings loaded into `cluster_finding`.
- The VCG enrichment is now the primary navigability bridge between
  characteristic-scope findings and the VCG evidence units — Session C
  and Session D queries can use `finding_citation` to answer "what does
  VCG-NN of CHAR-N contribute to finding X" without re-reading prose.
