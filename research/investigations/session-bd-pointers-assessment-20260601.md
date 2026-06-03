# Session B & D pointers — status & mapping to terms/clusters

**Generated:** 2026-06-01 (read-only). Focus: how far each pointer population carries a term link that resolves to a cluster.
Cluster bucket = the term's home: real M-cluster > FLAG > T2 > none(NULL); or no-matching-term / no-strongs-on-pointer.

## A. wa_session_b_findings

- total: 2883 | active (delete_flag=0): 2883 | deleted: 0
- term_id populated (active): 0/2883
- already routed to a Session C chapter (active): 336
- carry an sd_pointer_ref (active): 78

**finding_type (active):** OBSERVATION=1343, THEOLOGICAL_NOTE=445, SYNTHESIS_INTER_TIER=252, DIMENSION_REVIEW=146, MEANING_OBSERVATION=135, SPIRIT_SOUL_BODY=116, VERSE_PATTERN=101, CROSS_REGISTRY=86, SYNTHESIS_INTRA_TIER=84, ETYMOLOGY=46, VERSE_ANNOTATION=43, SOMATIC_EVIDENCE=39, DIMENSIONAL_PATTERN=8, TERM_BEHAVIOUR=4, DATA_ANOMALY_QA_GAP=4, GROUP_INTEGRITY=3, ROOT_FINDING=3, DIMENSION_PATTERN=2, N/A=2, STRUCTURAL_DISPOSITION=1, OPERATION_MODES=1, INNER_BEING_EFFECTS=1, RELATIONAL_POSITIONING=1, DIVINE_DISPOSITION=1, TEMPORAL_OPERATION=1, ENABLING_CAPACITY=1, CHARACTER_FORMATION=1, RELATIONAL_EXPRESSION=1, GROUND_CONDITION=1, OPERATIONAL_SEQUENCE=1, ORIGINATING_SOURCE=1, INNER_RESPONSE=1, EXTENSION_REASON=1, EXTREMITY_DEPTH=1, GRAMMATICAL_SUBJECT=1, DATA_ANOMALY_FINDING_UNCITED=1, DATA_ANOMALY_CITATION_GAP=1, DATA_ANOMALY_OBSERVATION_REGISTER_MISSING=1, DATA_ANOMALY_SYNTHESIS_REVISION_PENDING=1, DATA_ANOMALY_VC_PARTIAL=1

**status (active):** resolved_qa=1602, pending=1003, routed_cluster=224, open=25, confirmed=16, superseded=5, resolved_sd=4, routed_sd=2, folded=2

**term_id → cluster bucket (active findings):**

- no-strongs-on-pointer: 2883

_term_id sample:_ []

## B. wa_session_research_flags (pointer flags)

### SD_POINTER — 346 (73 resolved)
- strongs_reference populated: 78/346 | registry_id populated: 346/346
- strongs_reference → cluster bucket: no-strongs-on-pointer=268, M11=22, M05=21, FLAG=11, no-matching-term=6, M45=2, M29=2, M30=2, M15=2, M06=2, T2=2, M41=1, M20=1, M25=1, none(NULL)=1, M46=1, M21=1

  _strongs_reference sample:_ ['G3340', 'H5162G', 'H5068', 'G4893', 'H8104G', 'G1271']

### SB_FINDING — 203 (20 resolved)
- strongs_reference populated: 13/203 | registry_id populated: 203/203
- strongs_reference → cluster bucket: no-strongs-on-pointer=190, M31=2, M34=2, FLAG=2, M26=1, M12=1, M30=1, T2=1, M15=1, M05=1, M21=1

  _strongs_reference sample:_ ['G1345', 'G0570', 'G4710', 'G3392', 'G3878', 'H4906']

### SB_INNER_BEING — 4 (0 resolved)
- strongs_reference populated: 4/4 | registry_id populated: 4/4
- strongs_reference → cluster bucket: FLAG=2, no-matching-term=1, M45=1

  _strongs_reference sample:_ ['G0341; G0342; H2487', 'G3339', 'H2498', 'H2498']

### SD_CLUSTER — 1 (0 resolved)
- strongs_reference populated: 0/1 | registry_id populated: 1/1
- strongs_reference → cluster bucket: no-strongs-on-pointer=1

  _strongs_reference sample:_ []

## C. wa_finding_entity_links

- total: 287 | active: 287
- entity_type (active): verse=220, group=67
- entity_strongs populated (active): 0/287
- entity_strongs → cluster bucket: no-strongs-on-pointer=287

## D. session_d_* structured tables

All four (`session_d_runs`, `session_d_observations`, `session_d_term_links`, `session_d_verse_links`) are **empty (0 rows)** — Session D's structured capture was never populated; SD pointers exist only as `SD_POINTER`/`SD_CLUSTER` flags (section B).

## E. Synthesis — mapping to terms (therefore clusters)

**The term→cluster mapping is weak across every population. The two columns that should carry it are unpopulated:** `wa_session_b_findings.term_id` = 0/2,883, and `wa_finding_entity_links.entity_strongs` = 0/287. So almost everything maps to a **registry**, not a term.

**What IS term→cluster-mappable today (the actionable subset):**

| route | count | maps to cluster how |
|---|--:|---|
| `SD_POINTER` with `strongs_reference` | 78 / 346 | strongs → term → cluster (M11=22, M05=21 lead; FLAG=11) |
| `SB_FINDING` flags with `strongs_reference` | 13 / 203 | same |
| `SB_INNER_BEING` flags | 4 / 4 | some carry multiple strongs (e.g. `G0341; G0342; H2487`) |
| `wa_session_b_findings` via entity-link (verse path) | **49** distinct findings | finding → `entity_id` → `wa_verse_records` (220/220 carry `term_id`) → cluster |

≈ **95 flags + 49 findings ≈ 144 pointers** carry a usable term→cluster link.

**What is registry-scoped only (the bulk):** 2,834 of 2,883 findings + 268 `SD_POINTER` + 190 `SB_FINDING`. Reaching clusters from these means a **registry → its terms → clusters fan-out**, which is no longer 1:1 since the term-anchor pivot. Per the established principle, the registry-scope Q&A findings are *directional* (appendix-level), not directly applicable to term-and-verse analysis.

**Status snapshot:**
- Findings (2,883 active): `resolved_qa`=1,602 · `pending`=1,003 · `routed_cluster`=224 · already in a Session C chapter=336 · `open`=25.
- `SD_POINTER`: 73/346 resolved. `SB_FINDING`: 20/203 resolved.

**Implications / candidate next steps (for direction — nothing actioned):**
1. **Route the ~144 term-mappable pointers to their clusters** (the 95 strongs-bearing flags + 49 entity-linked findings). This is clean, high-value, and aligns with the term→cluster model just established.
2. **Decide the registry-scoped majority:** confirm they stay as directional registry-level appendix material, or define a fan-out rule (registry→terms→clusters) for any class worth distributing.
3. **Triage the 1,003 `pending` findings** — are they live work or stale?
4. **Decide the empty Session D structured tables** — abandon (SD lives as flags) or backfill from the flags.

