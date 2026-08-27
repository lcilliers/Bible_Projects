# DB Growth Projection — v1.8 Capture + Assembled Prose for All 214 Registries

**Date:** 2026-05-01
**Reference points:** R067 goodness (small: 3 OWNER, 14 anchors) and R103 love (large: 79 OWNER, 117 anchors). Both fully captured under v1.8 + assembled prose produced.
**Question.** If v1.8 capture + assembled-prose extraction lands for all 214 registries, how much does the DB grow?

---

## Current DB state (2026-05-01)

| Item | Value |
|---|---:|
| DB file size | **168.5 MB** |
| Total registries in scope | 214 |
| Registries already v1.8-captured | **4** (R067, R103, R207, R210 partial) |
| Active findings (`wa_session_b_findings`) | 1,441 |
| Active catalogue links (`wa_finding_catalogue_links`) | 2,192 |
| Open research flags (`wa_session_research_flags`) | 612 |
| Anchor verses (`verse_context.is_anchor=1`) | 4,765 |
| Active prose chapters (`prose_section`) | 114 |

## Per-registry footprint — observed from R067 + R103

| Item | R067 (small) | R103 (large) | Average | Notes |
|---|---:|---:|---:|---|
| OWNER terms | 3 | 79 | — | Programme avg: 17.3 |
| VC groups | 12 | 67 | — | Programme avg: 16.6 |
| Anchor verses | 14 | 117 | — | Programme avg: 22.3 |
| **Q&A findings** (catalogue v2) | 148 | 167 | **~155** | ~constant — driven by 189-prompt catalogue |
| **Synthesis findings** | 28 | 28 | **28** | exactly 7 + 21 by v1.8 §SB-29 |
| **Anomaly findings** | 1 | 1 | ~1 | DATA_ANOMALY_QA_GAP per session |
| **Total new findings** | **177** | **196** | **~185** | per registry |
| **Catalogue links** (Q&A + synthesis source) | 361 | 430 | **~395** | per registry |
| **New SD pointers** | 1 | 10 | **~5** | varies widely |
| Avg synthesis body | ~1,120 chars | ~1,120 chars | 1,120 | |
| Avg Q&A finding body | ~870 chars | ~870 chars | 870 | |
| Avg link note body | ~520 chars | ~520 chars | 520 | |

## Capture growth projection — all 214 registries

Assuming the 210 not-yet-captured registries follow the average pattern observed:

| Table | Current | + new rows | Projected total | Avg row size | Storage delta |
|---|---:|---:|---:|---:|---:|
| `wa_session_b_findings` | 1,441 | +210 × ~185 = **+38,850** | ~40,300 | ~870 chars body + meta | **~50 MB** |
| `wa_finding_catalogue_links` | 2,192 | +210 × ~395 = **+82,950** | ~85,150 | ~520 chars note + meta | **~52 MB** |
| `wa_session_research_flags` | 612 | +210 × ~5 = **+1,050** | ~1,660 | ~600 chars description | **~1 MB** |
| `verse_context.analysis_note` populated (anchor analysis) | 14 + ~117 + … | already exists for captured words | ~4,765 | ~1,000 chars per anchor note | **~5 MB** if all captured |

**Capture-only DB growth: ~108 MB**

This is the structured-data growth from running v1.8 capture on all 214 registries. The additional rows are all narrative content (finding bodies, Q&A answers, synthesis text). Index/FK overhead adds ~20% → **~130 MB total**.

## Assembled-prose growth projection (if written to `prose_section`)

| | R067 | R103 | Programme avg estimate |
|---|---:|---:|---:|
| Combined extract size | 297 KB | 418 KB | **~340 KB** per registry |
| Per-chapter avg | 50 KB | 70 KB | ~57 KB |
| Ch3 (Verses) — anchor-driven | 62 KB | 157 KB | varies most |

If all 214 chapter sets are assembled and written to `prose_section`:

- **214 × 6 chapters = 1,284 prose_section rows** (vs current 114)
- **214 × ~340 KB = ~73 MB of prose body** stored

Plus citations extracted to `wa_prose_section_citations` per v1.8 §9 — say 50 citations per chapter × 6 × 214 ≈ 64,000 citation rows × ~100 bytes = ~6 MB.

**Assembled-prose growth: ~80 MB**

## Combined projection

| Source | Growth |
|---|---:|
| Current DB | 168.5 MB |
| v1.8 capture across all 214 (rows + indexes) | +130 MB |
| Assembled prose written to `prose_section` (optional, deferred) | +80 MB |
| **Projected DB after both** | **~378 MB** |

If only capture lands (no prose store): **~298 MB** (1.8× current).

## What scales how

- **Catalogue Q&A coverage is roughly constant per registry** (~155 findings + 28 synthesis ≈ 185). This is driven by the 189-prompt v2 catalogue, not by word size.
- **Catalogue links scale with Q&A count + synthesis source citations** (~395 per registry, also roughly constant).
- **Ch3 (Verses) chapter size scales with anchor count.** Programme avg 22 anchors per registry → ~80–100 KB per Ch3, well below love's 157 KB outlier.
- **Ch4 (Language) chapter size scales with OWNER count + meaning_parsed depth.** R103's 79 OWNER terms produced 36 KB; programme avg of 17 OWNER would give ~15 KB.
- **SD pointer count varies most.** R067 raised 1 new pointer; R103 raised 10. Programme average likely 4–8 per registry.

## Outliers to watch

About **31 registries have 2,000+ verses** (programme bucket). These will have richer term inventories and more OWNER groups → larger Ch3/Ch4 chapters. Estimate: top 30 registries average ~600 KB combined extract (vs 340 KB programme average).

The other ~180 registries cluster around 250–350 KB combined extract.

## Practical implications

1. **DB stays well under 500 MB** even after full v1.8 + prose assembly across the whole programme. SQLite handles this comfortably.
2. **Backup files double** — 168 MB → ~378 MB per backup. The 10-snapshot retention (`BACKUP_RETENTION = 10` per CLAUDE.md) means ~3.8 GB of backup storage at full state.
3. **Most growth is narrative text** — Q&A bodies + synthesis findings + chapter prose. Indexes are small relative to body content.
4. **Prose-store growth (80 MB) is optional** — assembled chapters can be regenerated from capture data on demand. If storage matters more than read latency, skip the prose store and assemble at extract time.
5. **Backup directory is excluded from Git** (per CLAUDE.md). DB itself also excluded. So Git impact: zero from this growth.

## Caveats on the projection

- The 4 already-captured registries are not strictly representative. R067/R103 are mid-pipeline test cases; R207/R210 are partial captures. Real average per-word footprint may shift ±15% as more words are captured.
- The 189-prompt catalogue is fixed for now. If the catalogue grows (e.g. more word-specific Extensions for each word), per-registry capture grows proportionally.
- Assembled-prose size assumes the current chapter structure. If Session C polish passes are added (Tier 2 from earlier proposal), prose volume would roughly double (one assembled + one polished version, with supersede chain).
