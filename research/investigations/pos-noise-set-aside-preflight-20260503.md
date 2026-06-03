# POS-Noise Auto-Set-Aside — Pre-flight Report

_Generated 2026-05-03T12:43:43Z_  ·  patch: `Sessions\Patches\wa-global-repair-pos-noise-set-aside-v1-20260503.json`

**Total operations:** 2,191
**Registries affected:** 39
**Anchors removed:** 173

## Case breakdown

| Case | vc rows | Description |
|---|---:|---|
| A | 48 | Verse retained in same registry via content term |
| B | 1,928 | Verse covered in other registries via content terms |
| C | 215 | Verse has no content term in any registry's inventory |

## POS distribution of affected vc rows

| POS | rows |
|---|---:|
| particle | 1,105 |
| preposition | 499 |
| pronoun | 451 |
| conjunction | 136 |

## Top 30 registries by anchor loss

| Reg | Word | Anchors lost | Total vc rows set aside |
|---:|---|---:|---:|
| 90 | innocence | 26 | 175 |
| 57 | evil | 24 | 89 |
| 99 | kindness | 17 | 50 |
| 147 | sin | 14 | 76 |
| 44 | despair | 12 | 472 |
| 89 | iniquity | 8 | 25 |
| 173 | will | 6 | 74 |
| 4 | anger | 5 | 23 |
| 121 | praise | 5 | 21 |
| 100 | knowledge | 4 | 51 |
| 107 | meaning | 4 | 14 |
| 165 | unbelief | 4 | 5 |
| 172 | wickedness | 4 | 37 |
| 198 | might | 4 | 18 |
| 151 | sorrow | 3 | 20 |
| 167 | unity | 3 | 132 |
| 168 | uprightness | 3 | 7 |
| 187 | strength | 3 | 7 |
| 8 | appetite | 2 | 6 |
| 78 | hope | 2 | 4 |
| 98 | justice | 2 | 5 |
| 126 | purpose | 2 | 38 |
| 140 | seeking | 2 | 54 |
| 158 | terror | 2 | 3 |
| 162 | transgression | 2 | 13 |
| 174 | wisdom | 2 | 18 |
| 177 | worth | 2 | 5 |
| 197 | authority | 2 | 6 |
| 43 | desire | 1 | 1 |
| 111 | mercy | 1 | 2 |

## Registries needing post-patch anchor follow-up

Registries that lose anchors AND would have a low / zero anchor count after the patch — flagged for manual review.

| Reg | Word | Anchors before | Lost in patch | Anchors after |
|---:|---|---:|---:|---:|
| 212 | pray | 2 | 1 | 1 |

## Apply

```bash
# Dry-run first
python scripts/apply_session_patch.py Sessions\Patches\wa-global-repair-pos-noise-set-aside-v1-20260503.json --dry-run

# Live
python scripts/apply_session_patch.py Sessions\Patches\wa-global-repair-pos-noise-set-aside-v1-20260503.json
```
