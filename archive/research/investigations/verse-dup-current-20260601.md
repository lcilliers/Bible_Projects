# Active duplicate verse rows — current DB (2026-06-01)

**Duplicate (term_id, reference) groups with >1 live row: 946** | extra live rows: 946

## What differs between the duplicate rows (per group)
- same `mti_term_id` across the dup rows: 1 | different: 945
- same `file_id` (same extraction): 1 | different (different registry pulled the verse): 945
- live `verse_context` on >=2 of the rows: **1** | on exactly 1: 654 | on none: 291

## Sample groups (full row detail)

### G0931 @ Mat 4:24 (2 live rows)
| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |
|---|---|---|---|---|---|---|
| 280 | 2 | 29 | 4684 | pains | 1 | True |
| 236401 | 241 | 7680 | None | pains | 1 | False |

### G0931 @ Luk 16:23 (2 live rows)
| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |
|---|---|---|---|---|---|---|
| 281 | 2 | 29 | 4684 | torment | 1 | True |
| 236399 | 241 | 7680 | None | torment | 1 | False |

### G0931 @ Luk 16:28 (2 live rows)
| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |
|---|---|---|---|---|---|---|
| 282 | 2 | 29 | 4684 | torment | 1 | True |
| 236400 | 241 | 7680 | None | torment | 1 | False |

### G2347 @ Mat 13:21 (2 live rows)
| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |
|---|---|---|---|---|---|---|
| 818 | 5 | 100 | 21 | tribulation | 1 | True |
| 236046 | 241 | 7656 | None | tribulation | 1 | False |

### G2347 @ Mat 24:9 (2 live rows)
| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |
|---|---|---|---|---|---|---|
| 819 | 5 | 100 | 21 | tribulation | 1 | True |
| 236049 | 241 | 7656 | None | tribulation | 1 | False |

### G2347 @ Mat 24:21 (2 live rows)
| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |
|---|---|---|---|---|---|---|
| 820 | 5 | 100 | 21 | tribulation | 1 | True |
| 236047 | 241 | 7656 | None | tribulation | 1 | False |


## Scope correction (DB-verified) — this is NOT a dedup

The 946 "duplicate verse rows" are a symptom of a larger, different issue:

- **Files 240 (`213_listen_step_data`, registry 213) + 241 (registry 214 "suffering")** hold **3,795 live verse records, ALL `mti_term_id` NULL** — two whole registries' verse corpora were extracted but **never mti-linked** into the cluster model.
- **1,157 of those orphan rows carry live `verse_context`** (740 in 240 + 417 in 241) — real analysis; not disposable.
- Only **945 duplicate an existing mti-linked verse** (the no-vc "dups", 505 + 440). The other ~2,850 are **unique** to registries 213/214.

**Conclusion:** Action 5 is a **registry-integration gap (mti-linking + OWNER/XREF reconciliation for registries 213 listen / 214 suffering)**, not a verse dedup. A blind soft-delete would either destroy unique analysed data (the 1,157 with vc) or make an unowned OWNER/XREF call (the 945). **Held — do not dedup.** The narrow safe subset (soft-delete only the 945 redundant *no-vc* orphan copies) is possible but addresses the symptom, not the cause; recommend folding registries 213/214 into proper term/verse integration instead.
