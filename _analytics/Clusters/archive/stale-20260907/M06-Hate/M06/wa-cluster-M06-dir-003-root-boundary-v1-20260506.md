# Directive DIR-20260506-003 — Record root, dimensional, and BOUNDARY findings for M06

> Produced by: wa-directive-instruction-v1_4-20260506
> Governed by: wa-global-general-rules [current]
> Cluster: M06
> Produced date: 2026-05-06
> Researcher approval: PENDING

---

## Motivation

Three bodies of additional analytical work for the M06 cluster need to be recorded in the database:

**Operation A — Resolved gap findings (T6.4.2, T6.7.1, T6.7.3, T7.1.9).**
Four prompts that were flagged as gaps (G) during the analytical pass have now been resolved via CC database queries run on 2026-05-06 (results visible in wa-cluster-M06-findings-v2-20260506.md §2). These are currently recorded as gap rows or unaddressed stubs in `cluster_finding`. Their resolved content must now replace the gap entries.

- **T6.4.2** — Root-level vocabulary architecture: resolved with 18 distinct root codes, 5 multi-term roots within M06, 7 roots shared cross-cluster.
- **T6.7.1** — Dimensional sharing counts: resolved with 43 dimension assignments across 8 dimensions; cross-cluster sharing counts confirmed.
- **T6.7.3** — Dimensional sharing data availability: resolved (previously flagged as data not yet available; now confirmed available).
- **T7.1.9** — NT coinage: resolved with LSJ confirmation that G0865 afilagathos is NT-attested only; other Greek M06 terms confirmed as classical.

Additionally, three root-relationship findings emerged from the grouped v2 data that were not in the original analytical documents and add to the structural understanding of M06:

- **CHARAPH root** — H2781 cher.pah (M06-E) and H2778A cha.raph (BOUNDARY) share the same root, confirming that the taunt is the speech-act form of the reproach condition.
- **SUT root** — H7590 shut (M06-B contempt) and H7589 she.at (M06-G malice) are related words within the SUT root family, confirming at the lexical level that contempt is a constituent of malice.
- **SATAM root** — H7852 sa.tam (M06-A grudge-bearing hatred), H4895 mas.te.mah (M06-A hostile atmosphere), and H7850 sho.tet (BOUNDARY scourging) share the SATAM root, showing that the BOUNDARY scourge term is the behavioural expression of sa.tam hatred at its most active.

These three root-connection findings are new additions to the T6.4 vocabulary-sharing findings for their respective sub-groups.

**Operation B — BOUNDARY sub-group characterisation.**
The BOUNDARY sub-group currently has zero findings recorded (confirmed in wa-cluster-M06-findings-v2-20260506.md §1 and wa-cluster-M06-grouped-v2-20260506.md §1). The BOUNDARY sub-group contains 4 terms across 5 groups and 48 connected verses. These terms name the speech-acts and behavioural expressions through which M06 characteristics are delivered and maintained — they are the cluster's expression layer rather than primary inner-being dispositions. A characterisation note for each term must be recorded before Session C writing can begin.

---

## Scope

**Tables:** `cluster_finding` (primary); no other tables are written to by this directive.

**Cluster scope:** `cluster_code = 'M06'` throughout.

**Operation A — resolved gap updates:**

The following `cluster_finding` rows must be located and updated from gap/stub status to finding status. CC identifies rows by `(cluster_code, question_code, subgroup_code)` and updates `finding_status`, `finding_text`, and `resolved_date`.

| question_code | subgroup_code | Current status | Action |
|---|---|---|---|
| T6.4.2 | CLUSTER | gap or stub | UPDATE to finding with resolved text |
| T6.7.1 | CLUSTER | gap or stub | UPDATE to finding with resolved text |
| T6.7.3 | CLUSTER | gap or stub | UPDATE to finding with resolved text |
| T7.1.9 | CLUSTER | gap or stub | UPDATE to finding with resolved text |

Additionally, three new root-connection findings for T6.4 (vocabulary sharing at root level) must be added or updated:

| question_code | subgroup_code | Scope note |
|---|---|---|
| T6.4.2 | M06-E | New finding — CHARAPH root connection between cher.pah and cha.raph |
| T6.4.2 | M06-B / M06-G | New finding — SUT root connection between shut and she.at |
| T6.4.2 | M06-A | New or update — SATAM root connection extending to BOUNDARY sho.tet |

If these sub-group-level T6.4.2 rows do not exist in `cluster_finding`, CC inserts them. If they exist as stubs (N/A), CC updates them.

**Operation B — BOUNDARY characterisation:**

Four new `cluster_finding` rows must be inserted — one per BOUNDARY term — recording the term's role in the M06 cluster economy. These are structural characterisation notes, not full 189-prompt findings. They should be recorded under a BOUNDARY-appropriate prompt code; if no prompt code is reserved for sub-group structural notes, CC uses the closest available code (e.g. T1.2.1 — kind of inner-being phenomenon) and notes the structural-characterisation purpose in the finding_text.

| Term | Strong's | Group | Characterisation finding |
|---|---|---|---|
| cha.raph (to taunt) | H2778A | 339-001, 339-002 | The taunting term — the speech-act through which reproach (cher.pah, M06-E) is actively delivered by the agent. Shares the CHARAPH root with cher.pah. In Psa 42:10, Psa 44:16, and Job 27:6 the taunt is the verbal instrument that makes the reproach-condition real and public in the recipient. The BOUNDARY role: cha.raph is the delivery mechanism for M06-E, operating at the speech-act surface of what cher.pah names as an inner-social condition. |
| ba.ash (to stink / make offensive) | H0887 | 90-001 | The stench/offensiveness term — the social-sensory mark of being made repugnant to others. The root BASH names the condition of being regarded as a stench, which is the social register of M06-C's abhorrence. Where ta.av names the inner visceral recoil (M06-C), ba.ash names what the rejected person becomes in others' perception. The BOUNDARY role: ba.ash marks the outer social result of abhorrence being directed at a person or community — the social form of what M06-C names as an inner-being response. |
| afilagathos (not loving good / hating good) | G0865 | 1643-001 | The NT compound hating-good term — the alpha-privative negation of filagathos (loving good), appearing only in 2Ti 3:3's vice list. Confirmed NT-attested only via LSJ (no classical precedent). Shares the AGATH root with goodness vocabulary (M05 cluster). The BOUNDARY role: afilagathos names the characterological orientation that produces and sustains M06's disordered characteristics — the person who does not love good is the person from whom hatred, contempt, abhorrence, cruelty, and malice proceed. It is the inner-being ground-condition, not a characteristic itself. |
| sho.tet (scourge / driving force) | H7850 | 5519-001 | The scourge/driving term — shares the SATAM root with H7852 sa.tam (M06-A grudge-bearing hatred) and H4895 mas.te.mah (M06-A hostile atmosphere). In Num 33:55 the scourge is what the remaining nations will be in Israel's sides; in Isa 28:15,18 the "scourging whip" (sho.tet) is the instrument of the covenant with death. The BOUNDARY role: sho.tet names the active driving/scourging function of M06-A's settled hatred when it becomes a sustained structural force against another — the behavioural expression of sa.tam hatred at its most active and persistent. |

---

## Outcome required

**Operation A:**

1. All four cluster-level gap rows (T6.4.2, T6.7.1, T6.7.3, T7.1.9 at CLUSTER scope) updated to `finding_status = 'finding'` with the resolved finding text from wa-cluster-M06-findings-v2-20260506.md §2.
2. Three sub-group T6.4.2 root-connection findings inserted or updated (M06-E / CHARAPH; M06-B+M06-G / SUT; M06-A / SATAM extending to BOUNDARY).
3. No gap rows for these four question codes remain at `finding_status = 'gap'` for the CLUSTER scope after execution.
4. `resolved_date` set to 2026-05-06 for all updated rows.

**Operation B:**

1. Four new `cluster_finding` rows inserted for the BOUNDARY sub-group — one per term — with `subgroup_code = 'BOUNDARY'`, `finding_status = 'finding'`, and `finding_text` as specified in the Scope section above.
2. Source file set to `WA-M06-sessionC-readiness-v1-20260506.md` for the BOUNDARY rows (this directive's companion document).
3. No physical deletes — all prior gap/stub rows are updated in place per wa-patch-instruction [current] §5.4.

---

## Completion confirmation

CC returns the following:

**1. Resolved gap count:**
```sql
SELECT question_code, finding_status, LEFT(finding_text, 80) AS excerpt
FROM cluster_finding
WHERE cluster_code = 'M06'
  AND question_code IN ('T6.4.2', 'T6.7.1', 'T6.7.3', 'T7.1.9')
  AND subgroup_code = 'CLUSTER'
ORDER BY question_code;
```
Expected: 4 rows, all with `finding_status = 'finding'`, all with non-empty finding_text containing the resolved content.

**2. Root-connection findings:**
```sql
SELECT question_code, subgroup_code, LEFT(finding_text, 80) AS excerpt
FROM cluster_finding
WHERE cluster_code = 'M06'
  AND question_code = 'T6.4.2'
  AND subgroup_code IN ('M06-A', 'M06-B', 'M06-E', 'M06-G')
ORDER BY subgroup_code;
```
Expected: rows present for M06-A (SATAM), M06-E (CHARAPH), and at least one of M06-B or M06-G (SUT) with finding_status = 'finding'.

**3. BOUNDARY findings inserted:**
```sql
SELECT subgroup_code, question_code, finding_status, LEFT(finding_text, 60) AS excerpt
FROM cluster_finding
WHERE cluster_code = 'M06'
  AND subgroup_code = 'BOUNDARY'
ORDER BY question_code;
```
Expected: 4 rows (one per BOUNDARY term), all with `finding_status = 'finding'`.

**4. Remaining gap count for M06:**
```sql
SELECT COUNT(*) AS remaining_gaps
FROM cluster_finding
WHERE cluster_code = 'M06'
  AND finding_status = 'gap';
```
Expected: 1 — only T7.1.8 (LXX mapping) should remain as a gap after this directive executes. If the count exceeds 1, CC lists the remaining gap rows.

**5. Confirm no wa_session_b_findings rows written:**
```sql
SELECT COUNT(*) FROM wa_session_b_findings
WHERE updated_date = '20260506';
```
Expected: count unchanged from pre-directive state (0 new rows written by this directive).

---

## Notes

**T7.1.8 — LXX mapping remains open.** The one remaining gap (LXX vocabulary correspondence for M06 terms) requires an external Hatch-Redpath concordance that is not held in the database. This gap is explicitly bounded and does not block Session C. An SD pointer for this gap should be recorded if not already present. CC does not attempt to resolve T7.1.8 as part of this directive.

**BOUNDARY finding_text:** The characterisation notes provided in the Scope section are the analytical content to be used verbatim as `finding_text`. CC should not paraphrase or condense them.

**Root findings — source data:** The root connections (CHARAPH, SUT, SATAM) were derived from the `wa_term_related_words` data as rendered in wa-cluster-M06-grouped-v2-20260506.md §3.2–§3.8. CC may confirm these connections by querying `wa_term_related_words` before inserting:
- CHARAPH: confirm H2781 and H2778A share root_family_code = 'CHARAPH'
- SUT: confirm H7590 and H7589 share a related-words link via the SUT root
- SATAM: confirm H7852, H4895, and H7850 share root_family_code = 'SATAM'

**Missing cluster-level finding:** The grouped v2 file shows the CLUSTER row with 188 total entries against 189 prompts, indicating one cluster-level prompt has no finding or N/A row. CC should identify which question_code is missing and either insert the appropriate row (finding, silent, or N/A stub) or flag it for researcher attention.

**Relationship to DIR-20260506-002:** DIR-20260506-002 (findings recording — PENDING researcher approval) covers the main 1,323-prompt findings body. This directive (DIR-20260506-003) covers the supplementary findings that emerged after the main pass — resolved gaps, new root-connection findings, and BOUNDARY characterisation. Both directives are independent and can be executed in either order, but DIR-20260506-002 should be approved first as it establishes the `cluster_finding` rows that this directive updates.

---

*wa-cluster-M06-dir-003-root-boundary-v1-20260506.md | DIR-20260506-003*
*Produced under wa-directive-instruction-v1_4-20260506*
*Companion documents: wa-cluster-M06-findings-v2-20260506.md, wa-cluster-M06-grouped-v2-20260506.md, WA-M06-sessionC-readiness-v1-20260506.md*
