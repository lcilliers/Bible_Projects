# WA-M32-dissolution-applied-v1-20260508

> Application report for `DIR-20260508-005` — M32 dissolution.
> **Researcher-amended path** (overrides directive's preservation instructions).
> Cluster: M32 — Conscience and Self-Awareness
> Applied: 2026-05-08 (UTC)
> Outcome: **COMPLETE** — zero residual M32 references in the analytical/term tables.

---

## 1. Researcher amendment

The directive (DIR-20260508-005) instructed preservation of M32's `cluster_finding`, `cluster_subgroup`, and `cluster` rows as legacy reference. After audit (in chat) the researcher amended the path:

> "I do not want any reference in the analytic and term results to M32. It should for all practical purposes non exist. The analytic work of M15 and M26 will pick up and redo the analytics that is lost in the process."

The applied path is therefore **full hard-deletion** of M32's analytical footprint, not preservation. The 575 cluster_finding rows are accepted as analytical loss; M15 and M26 will re-derive in their own future Session B passes.

---

## 2. Operations applied (single transaction, foreign_keys=ON)

| # | Operation | Rows |
|---|---|---:|
| 1 | `UPDATE mti_terms` — 6 active M32 terms reassigned to M15 / M26, `cluster_subgroup_id=NULL` | 6 |
| 2 | `UPDATE mti_terms` — 15 delete-flagged historical rows: `cluster_code` set to NULL | 15 |
| 3 | `DELETE FROM cluster_finding WHERE cluster_code='M32'` | 575 |
| 4 | `DELETE FROM cluster_subgroup WHERE cluster_code='M32'` | 3 |
| 5 | `DELETE FROM cluster WHERE cluster_code='M32'` | 1 |

Pre-write backup: `backups/bible_research_pre_m32_dissolution_20260508_094006.db` (180.8 MB, retained).

---

## 3. Term redistribution (final state)

| mti_id | Strong's | Transliteration | Was | Now |
|---:|---|---|---|---|
| 3392 | G1760 | enthumeomai | M32 / M32-BOUNDARY | **M15** / NULL |
| 454 | G4894 | suneidō | M32 / M32-A | **M15** / NULL |
| 3578 | H7896K | shit | M32 / M32-B | **M15** / NULL |
| 4848 | G0843 | autokatakritos | M32 / M32-BOUNDARY | **M26** / NULL |
| 599 | G2589 | kardiognōstēs | M32 / M32-BOUNDARY | **M26** / NULL |
| 2739 | G6083 | sunoida | M32 / M32-A | **M26** / NULL |

Destination cluster term counts: M15 87 → **90**, M26 36 → **39**. Both clusters' Phase 4 sub-group assignment will pick up these new terms when those clusters reach Session B.

---

## 4. Zero-reference verification

| Check | Count | Result |
|---|---:|---|
| `mti_terms` where `cluster_code='M32'` | 0 | OK |
| `mti_terms` where `cluster_subgroup_id IN (17,18,19)` | 0 | OK |
| `cluster_subgroup` where `cluster_code='M32'` | 0 | OK |
| `cluster_subgroup` where `id IN (17,18,19)` | 0 | OK |
| `cluster_finding` where `cluster_code='M32'` | 0 | OK |
| `cluster_finding` where `cluster_subgroup_id IN (17,18,19)` | 0 | OK |
| `cluster` where `cluster_code='M32'` | 0 | OK |
| Programme-wide sweep for any `cluster_code='M32'` value in any column of any table | 0 | OK |

**M32 does not exist anywhere in the analytical/term tables.**

---

## 5. Untouched data (term-linked, travels with the terms)

| Table | Pre | Post | Delta |
|---|---:|---:|---|
| `verse_context` for the 6 mti_ids | 17 | 17 | unchanged ✓ |
| `verse_context_group` for the 6 mti_ids | 8 | 8 | unchanged ✓ |
| `wa_verse_records` for the 6 mti_ids | 57 | 57 | unchanged ✓ |

These rows continue to point at the same `mti_term_id`s. Those mti_ids now have `cluster_code` of M15 or M26, so all the verse evidence is now associated with the destination clusters via the term linkage.

---

## 6. Files retained on disk (not "analytical results", but referenced for audit)

The Sessions folder still contains the M32 documentation and analysis files. None of them affect query results:

```
Sessions/Session_Clusters/M32/
├── wa-cluster-M32-comprehensive-v1..v4-20260508.md       (snapshot reports)
├── wa-cluster-M32-detail-v1..v3-2026050{5,6,7}.md
├── wa-cluster-M32-dir-002..005-*.md                      (directives)
├── wa-global-M32-dir-dissolution-v1-20260508.md          (this dissolution directive)
├── WA-M32-A/B-group-verse-mapping-*.md
├── WA-M32-{A..G,BOUNDARY}-findings-*.md
├── WA-M32-consolidated-findings-v1-20260508-part{1..4}*.md
├── WA-M32-characteristic-debate-v1-20260508.md
├── WA-M32-session-log-v1-20260508.md
├── WA-M32-subgroup-summaries-v1-20260508.md
├── wa-obslog-M32-conscience-self-awareness-v1,v2-20260508.md
├── WA-M32-{B-group-mapping,findings-record}-applied-*.md (prior application reports)
└── WA-M32-dissolution-applied-v1-20260508.md             (this report)
```

If you also want these gone, ask separately — I can move the folder to an `archive/` location or hard-delete it. Hard-deletion is irreversible; archive is reversible.

---

## 7. Recovery

If the dissolution proves to have been premature, the pre-write backup at `backups/bible_research_pre_m32_dissolution_20260508_094006.db` contains the full pre-dissolution state. Restoration: stop all DB connections, copy that file over `database/bible_research.db`, and the M32 cluster + its 575 findings + 6 terms + 3 sub-groups all return.

---

## 8. Scripts used

- `_apply_m32_dissolution_v1_20260508.py` — single-transaction dissolution with PRAGMA foreign_keys=ON, pre-flight, post-write verification.
- Manual backup created via inline Python before the apply ran.

---

*WA-M32-dissolution-applied-v1-20260508*
*Cluster: M32 — Conscience and Self-Awareness — DISSOLVED*
*Researcher amendment to DIR-20260508-005 — full hard-deletion path*
*Backup: backups/bible_research_pre_m32_dissolution_20260508_094006.db*
