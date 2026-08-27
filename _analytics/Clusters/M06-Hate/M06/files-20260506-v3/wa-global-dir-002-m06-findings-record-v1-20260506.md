# Directive DIR-20260506-002 — Record M06 cluster analysis findings from catalogue pass

> Produced by: wa-directive-instruction-v1_3-20260422
> Governed by: wa-global-rules-all-v2-20260427
> Registry: global
> Produced date: 2026-05-06
> Researcher approval: PENDING

---

## Motivation

This session has completed a full T0–T7 catalogue-prompt pass (189 prompts × 7 sub-groups = 1,323 prompt responses) for the M06 cluster (Hate, Contempt and Hostility). The analysis was conducted at the sub-group level (M06-A through M06-G), with a consolidation pass identifying 14 cluster-level findings applicable across all sub-groups and 18 prompt categories where answers are sub-group-specific.

The findings are currently documented in seven output files (plus the consolidation document). They need to be recorded in the database so they are:
1. Queryable alongside other analytical findings
2. Linked to the observation question catalogue (`wa_obs_question_catalogue`) via the existing `question_code` identifiers (T0.1.1, T1.2.3, etc.)
3. Available for the eventual Session D cross-cluster synthesis

The challenge CC must resolve: the existing `wa_session_b_findings` table has `registry_id INTEGER NOT NULL` — meaning it requires a specific registry number. This analysis was conducted at the **cluster sub-group level**, not at any single registry level. The findings do not belong to one registry; they belong to M06 sub-groups (M06-A, M06-B, etc.) and to the M06 cluster as a whole.

CC must inspect the database and determine the correct path:

**Path A:** If a cluster-level findings table already exists (or if `wa_session_b_findings` has been extended to allow `registry_id = NULL` with a `cluster_ref` field), CC uses that table directly.

**Path B:** If no cluster-level findings mechanism exists, CC proposes the minimum schema addition needed (e.g., relaxing the NOT NULL constraint on `registry_id` in `wa_session_b_findings` and adding a `cluster_ref` or `sub_group_ref` column, or creating a separate `wa_cluster_analysis_findings` table) and **halts before writing any data**, returning the proposed schema change for researcher approval as a schema enablement directive.

**Path C:** If findings should be routed through the obslog → CC writer pipeline (the Phase 2 writer), CC confirms the correct obslog format and the pipeline is used instead of a direct database write.

This directive gives CC the full content of the findings and the three possible paths. CC determines which path applies and either executes (Path A or C) or halts and proposes (Path B).

---

## Scope

**Source documents (in `/mnt/user-data/outputs/`):**
- `WA-M06-A-prompts-T0-T2-v1-20260506.md` — M06-A T0–T2 responses (43 prompts)
- `WA-M06-A-prompts-T3-T4-v1-20260506.md` — M06-A T3–T4 responses (57 prompts)
- `WA-M06-A-prompts-T5-v1-20260506.md` — M06-A T5 responses (21 prompts)
- `WA-M06-A-prompts-T6-v1-20260506.md` — M06-A T6 responses (24 prompts)
- `WA-M06-A-prompts-T7-v1-20260506.md` — M06-A T7 responses (20 prompts)
- `WA-M06-B-prompts-T0-T7-v1-20260506.md` — M06-B full pass (189 prompts)
- `WA-M06-C-prompts-T0-T7-v1-20260506.md` — M06-C full pass (189 prompts)
- `WA-M06-D-prompts-T0-T7-v1-20260506.md` — M06-D full pass (189 prompts)
- `WA-M06-E-prompts-T0-T7-v1-20260506.md` — M06-E full pass (189 prompts)
- `WA-M06-FG-prompts-T0-T7-v1-20260506.md` — M06-F and M06-G combined pass (189 prompts each)
- `WA-M06-consolidation-v1-20260506.md` — Cluster-level consolidation (14 cluster findings, 18 sub-group-specific finding areas)

**Observation catalogue linkage:** All prompt responses are linked to question codes from `wa_obs_question_catalogue` with `catalogue_version = 'v2-2026-04-29'` and the T0–T7 tier structure. The question codes are: T0.1.1, T0.1.2, T0.1.3, T0.2.1, T0.2.2, T0.2.3, T0.3.1, T0.3.2, T0.3.3, T0.4.1, T0.4.2, T0.4.3 … through T7.3.4.

**Sub-group identifiers to be used:**

| Sub-group label | Database sub_group field value |
|---|---|
| M06-A Hatred | M06-A |
| M06-B Contempt | M06-B |
| M06-C Abhorrence | M06-C |
| M06-D Cruelty/Ruthlessness | M06-D |
| M06-E Reproach | M06-E |
| M06-F Hostility/Enmity | M06-F |
| M06-G Malice | M06-G |
| Cluster-level (all sub-groups) | M06 |

**Outcome codes used in source documents:**
- `E` — Evidenced (the verse evidence confirms this)
- `S` — Silent (the verses do not address this prompt)
- `G` — Gap (the question should be answerable but is not yet — requires further investigation or CC database query)

---

## Outcome required

**If Path A or C applies:**

For each of the 1,323 prompt responses (189 prompts × 7 sub-groups), plus the 14 cluster-level findings from the consolidation document, the following data is recorded in the appropriate table:

- The cluster reference: `M06`
- The sub-group reference: `M06-A` through `M06-G` (or `M06` for cluster-level findings)
- The question code from `wa_obs_question_catalogue` (e.g., `T0.1.1`)
- The outcome code: `E`, `S`, or `G`
- The finding text: a concise statement of what the verse evidence shows (drawn from the source documents)
- The source file reference: the output file from which the finding is drawn
- The raised date: 2026-05-06
- The session reference: `wa-obslog-M06-m06-method-v1-20260506`

No physical deletes per wa-patch-instruction [current] §5.4. No prose data changes (per wa-directive-instruction-v1_3 §10.7 hard exclusions).

**If Path B applies:**

CC halts and returns:
1. The proposed schema change (table definition or column addition)
2. A statement of why the current schema cannot accommodate the data
3. The expected patch type that would follow the schema enablement

CC does **not** write any findings data before the schema enablement is confirmed.

---

## Completion confirmation

CC returns the following:

**If Path A or C was taken:**

1. The table(s) written to and the record count inserted
2. A sample query result showing 3–5 representative findings records with their question_code, sub_group_ref, outcome_code, and finding_text
3. The count of G-flagged (gap) items across all sub-groups — these require separate CC queries to resolve and should be listed with their question codes and sub-group labels
4. Confirmation that no `wa_session_b_findings` rows were written with `registry_id NOT NULL` violated

**If Path B was taken:**

1. The proposed schema change in DDL (CREATE TABLE or ALTER TABLE statement)
2. A statement of the blocker in the current schema
3. The expected patch type to follow (SESSIONB_FINDINGS or equivalent)
4. No data has been written

---

## Notes

**G-flagged items** — the following question codes have been flagged as G (gap requiring CC database query or further investigation) across one or more sub-groups. CC should return these as a list:

From M06-A: T6.4.2 (root-level vocabulary architecture), T6.7.1 (dimensional sharing counts), T7.1.8 (LXX mapping for sa.ne, sin.ah, sa.tam, mas.te.mah), T7.1.9 (NT coinage for afilagathos)

From M06-B: T6.7 (dimensional sharing), T7.1.8–9 (LXX mapping, Greek exoutheneo)

From M06-C: T6.7 (dimensional sharing), T7.1.8 (LXX mapping for ta.av, she.qets, de.ra.on, bdelussomai), plus root distinction H8374 vs H8581 ta.av

From M06-D: T6.7 (dimensional sharing), T7.1.8 (LXX mapping), cross-cluster link Pro 27:4 to jealousy/envy cluster

From M06-E: T6.7 (dimensional sharing), T7.1.8 (LXX/NT mapping for cher.pah, shim.tsah, ne.a.tsah, sa.ni, hubrizō), Dan 12:2 dual-cluster confirmation

From M06-F/G: T6.7 (dimensional sharing), she.at root analysis, LXX mapping for ya.riv, a.yav, qim

If CC can resolve any G-flagged items by running database queries (e.g., dimensional sharing counts, LXX field data), CC resolves them and includes the resolved data in the completion confirmation rather than leaving them as open gaps.

**This directive does not write prose.** All prose (Session C output documents) will be produced in a subsequent session after the findings are confirmed in the database.

**Previous directive in this session:** DIR-20260506-001 (sub-group assignment and cluster reassignment) — confirmed complete.

---

*wa-global-dir-002-m06-findings-record-v1-20260506.md | DIR-20260506-002 | Produced under wa-directive-instruction-v1_3-20260422*
