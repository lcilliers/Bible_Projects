# Phase 9 for M04 — characteristic-scope plan (simplified)

**Date:** 2026-05-18
**Author:** CC
**Supersedes:** v1 and v2 of `WA-phase9-scope-model-proposal-*.md` — both retained for record; this is the operative plan going forward.
**Status:** PROPOSAL — small confirmation step at §6 before CC builds the M50 migration + the first per-characteristic AI package.

---

## 1. The simplified model

Researcher 2026-05-18:

> *"so we can now pass the data for a characteristic, with its sub groups to and other data to AI to work through the 189 findings. if we do it by characteristic then it should be very similar to the other clusters that we did phase 9 with successfully."*

Correct. The proven Phase 9 pattern was **189 × sub-group + CLUSTER**, where each sub-group was effectively a characteristic. Under the corrected hierarchy, the same pattern at the right level is **189 × characteristic + CLUSTER**.

No layered architecture. No new vcg_finding tables. Each AI session works through 189 prompts for one characteristic, just as past successful clusters did per sub-group.

---

## 2. What each AI session receives

Per characteristic, the AI session receives:

1. The characteristic's definition (verbatim from the v4 map / DB)
2. Its constituent sub-groups (with `core_descriptions`)
3. The VCGs within those sub-groups (with `context_descriptions` + anchor verses + member counts)
4. The 189-prompt catalogue (T0–T7)
5. Any **carry-forward observations** with `target_phase='phase_9_findings'` linked to this characteristic (the discipline hints — e.g. "watch for Joy/Gladness inter-relationship within M04-B and M04-C")
6. Sub-group-specific verse listings (reference + Pass A meaning) so AI can look up evidence per prompt without re-reading the full corpus linearly

AI session output: 189 characteristic-scope findings (or fewer if some are S/G), each citing specific evidence (verses / VCGs / sub-groups). Plus selective sub-group-scope findings where evidence differs materially between sub-groups within the characteristic.

---

## 3. M04 work estimate

| Characteristic | Sub-groups | Approx. verses | AI sessions |
|---|---|---:|---:|
| 1 — Exultation | M04-A | 83 | 1 |
| 2 — Joy | M04-B, C, D, E (partial) | ~460 | 1 |
| 3 — Gladness | M04-L, O | 133 | 1 |
| 4 — Delight | M04-G, H, M, N, P | 247 | 1 |
| 5 — Pleasure | M04-J, K | 96 | 1 |
| 6 — Wonder | M04-I | 84 | 1 |
| 7 — Suffering-Joy | M04-E (partial), M04-F | ~14 | 1 |
| **Cluster synthesis** | (across all 7) | — | 1 |
| **Total** | | | **~8** |

Output: ~189 × 7 characteristics + 189 cluster = ~1,512 cluster_finding rows max. Realistic: ~700-1,200 after S/G compression. Comparable to M01 / M02 (1,323-1,512 rows each).

---

## 4. Schema needed — small M50 migration

Add **one column** to `cluster_finding`:

```sql
ALTER TABLE cluster_finding ADD COLUMN characteristic_id INTEGER
  REFERENCES characteristic(id);
```

Plus extend the UNIQUE constraint to include `characteristic_id`:

```sql
-- via table rebuild per SQLite UNIQUE handling
-- new: UNIQUE(obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope, version)
```

Why: characteristic-scope rows (one per prompt, one per characteristic) need to coexist with CLUSTER-scope rows (one per prompt, cluster_subgroup_id=NULL, characteristic_id=NULL) without UNIQUE collision.

Migration M50 bumps schema 3.23.0 → 3.24.0. Additive; no data migration needed.

---

## 5. Operational sequence (after approval)

| Step | Activity | Who | Output |
|---|---|---|---|
| 5.1 | Schema migration M50 | CC | characteristic_id column on cluster_finding |
| 5.2 | Per-characteristic AI package builder | CC | brief + structural input per characteristic (7 packages + 1 cluster-synthesis package) |
| 5.3 | First test session — start with M04 Characteristic 1 (Exultation, M04-A only, 83 verses) | researcher | AI output for one characteristic |
| 5.4 | CC parses + validates output; applies to cluster_finding with characteristic_id set | CC | findings landed |
| 5.5 | Repeat 5.3–5.4 for the other 6 characteristics + cluster synthesis | researcher + CC | full M04 Phase 9 findings |
| 5.6 | Coverage check: every prompt has ≥1 row per characteristic; every is_relevant verse cited somewhere | CC | gap report |
| 5.7 | Observation reconciliation: 4 cluster_observations updated open → confirmed/refined | researcher | observations resolved |
| 5.8 | Stop and review before Phase 10 | researcher | go/no-go for Phase 10 |

Test-first on Characteristic 1 — smallest, single sub-group, low risk. If the pattern works, run the others in sequence. If it doesn't, we adjust before scaling.

---

## 6. Decisions needed

| # | Question | Options | Your decision |
|---|---|---|---|
| 1 | Adopt the simplified 189-per-characteristic model? | YES / NO / ADJUST | _[YES / NO / ADJUST: ...]_ |
| 2 | Apply M50 migration (characteristic_id column on cluster_finding)? | YES / OTHER (specify) | _[YES / OTHER: ...]_ |
| 3 | Test sequence: start with Characteristic 1 (Exultation, smallest) before scaling? | YES / DIFFERENT ORDER (specify) | _[YES / OTHER: ...]_ |
| 4 | Selective sub-group-scope findings — AI authors them only when evidence within a characteristic differs materially across constituent sub-groups (vs forcing per-sub-group row for every prompt)? | YES (selective) / FORCE (every sub-group every prompt) | _[YES / FORCE]_ |
| 5 | Cluster-scope synthesis run as a separate 8th session after the 7 characteristic sessions, OR derived mechanically from characteristic findings? | SEPARATE-SESSION / DERIVED | _[SEPARATE-SESSION / DERIVED]_ |

---

## 7. What changes from earlier proposals

- **v1 cluster-primary single-pass** (189 cluster only): rejected — AI bulk-reads the cluster, runaway bus.
- **v2 layered (VCG → cluster):** structurally sound but over-engineered. Required new tables. Hard to align with the proven Phase 9 mechanic.
- **v3 (this plan):** 189 × characteristic. Matches the proven pattern. Single small column addition. Bounded sessions. Familiar AI brief shape.

---

*End of plan. Mark §6 and ping me.*
