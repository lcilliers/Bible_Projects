# AI Question-Test Bundle — 8 Words

**Generated:** 2026-04-30 06:30 UTC

**Purpose:** complete data per word for AI testing of new questions.  Each file contains every term, group, anchor verse (with text), finding (with all citation categories — structured links + text-recovered support), open flag (Session B + Session D), and Q&A link (where present), plus co-occurrence, shared anchors, quality flags, and verse classification summary.

**Schema:** v3.17.0 SQLite at `database/bible_research.db` — DB is the source of truth.


## Files

| Reg | Word | File | Size | Findings | Open flags |
| ---: | --- | --- | ---: | ---: | ---: |
| R023 | compassion | [R023-compassion-data.md](R023-compassion-data.md) | 96,436 chars | 1 | 34 |
| R030 | contrition | [R030-contrition-data.md](R030-contrition-data.md) | 151,223 chars | 62 | 9 |
| R062 | fellowship | [R062-fellowship-data.md](R062-fellowship-data.md) | 58,554 chars | 17 | 19 |
| R064 | forgiveness | [R064-forgiveness-data.md](R064-forgiveness-data.md) | 230,657 chars | 35 | 24 |
| R067 | goodness | [R067-goodness-data.md](R067-goodness-data.md) | 172,923 chars | 52 | 49 |
| R068 | grace | [R068-grace-data.md](R068-grace-data.md) | 76,976 chars | 1 | 55 |
| R103 | love | [R103-love-data.md](R103-love-data.md) | 100,409 chars | 2 | 35 |
| R111 | mercy | [R111-mercy-data.md](R111-mercy-data.md) | 63,401 chars | 1 | 16 |

## Notes on completeness

Words at v2 `Analysis Complete` carry the richest Q&A coverage (forgiveness, goodness, contrition).  Fellowship is at `Pre-Analysis Complete` — has v2 findings but no Q&A links yet.  Compassion, grace, love, and mercy are at `Verse Context Reset` — they carry pre-v2 findings (often only 1–2 per registry) and rich SD-pointer flags but no Q&A coverage under the current catalogue.

Citation completeness varies: where structured `wa_finding_entity_links` rows are sparse, the report falls back to text-scan recovery (DIM↔OBS resolution chain, cross-finding refs, inline Strong's, term transliterations, inline verse refs, inline group-code refs).  Findings with no support in any of the seven categories are tagged orphan at the end of §8.
