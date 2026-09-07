# Directive DIR-20260619-002 — M02 C7 (Bitterness) scope resolution

> Produced by: wa-directive-instruction-v1_4-20260506
> Governed by: wa-global-general-rules [current]
> Cluster: M02
> Produced date: 2026-06-19
> Researcher approval: PENDING

---

## Motivation

The C7 (Bitterness) scope question raised in the evidence-verification pass (`wa-m02-evidence-verification-v1_0-20260619.md`, flag F-D; F10.4; T7.1.8) is now resolved by the DB lookup `wa-m02-marah-mar-bitterness-lookup-v1-20260619.md`. The lookup establishes:

- M02's only bitterness term is **G4088 *pikria*** (4 NT occurrences) — the basis of C7.
- The Hebrew bitterness-of-soul family (H4751 *mar*, H4843 *ma.rar* "to be bitter", H4844 *ma.ror*, H4786/H4787 *morah*, H4470 *me.mer*, H4472 *mam.ror*, etc.) is **owned and analysed in M03 (Grief)** — every occurrence carries `cluster = M03`.
- H4843 *ma.rar* is **sense-split**: the "be bitter" sense → M03; the "provoke / embitter" sense → M02 (status NULL).
- The English word "bitterness" spans two distinct inner states the DB already separates by sense: **NT *pikria*/*pikros*** = resentment/anger-bitterness (M02/M28; "bitterness… and wrath and anger", Eph 4:31); **OT *mar nephesh*** = grief/anguish-bitterness (M03).

Therefore C7 must **not** be expanded by pulling the OT *mar/marah* field into M02 — those terms are M03's, and the boundary is a principled sense-split, not a coverage gap. The fix is to (a) record C7 as **NT-*pikria*-only by design**, and (b) register the **M02 ↔ M03 bitterness boundary** as a cross-cluster seam for Session D. (This is the "document/constrain" resolution — Option 1 — confirmed by the researcher.)

---

## Scope

**Cluster:** M02. **Sub-group:** C7 (Bitterness).

**Tables:** `cluster_finding` (record the scope-resolution finding); and the Session D cross-cluster pointer mechanism (CC resolves the exact field/table used for cross-cluster seams — AI is not certain of its current form).

**No membership change:** no terms are added to or removed from M02; G4088 *pikria* remains C7's sole basis. M03 is **not** touched.

**CC resolves:** whether the c1–c7 sub-group structure (and the C7 `cluster_subgroup` row) is yet persisted. If it is not, CC reports so the finding can be sequenced after that structure exists — **this directive does not create the c1–c7 structure.**

---

## Outcome required

1. A `cluster_finding` row recorded for **M02 / C7**, `finding_status = 'cluster_synthesis'` (or `'finding'` as the schema requires), `finding_text` =
   > "C7 (Bitterness) is NT-*pikria*-only (G4088, 4 occ) by design. The OT bitterness-of-soul family (*mar*/*marah* — H4751, H4843, and the wider family) is owned and analysed in M03 (Grief). The English 'bitterness' is split by sense: NT *pikria*/*pikros* = resentment/anger-bitterness (M02/M28); OT *mar nephesh* = grief/anguish-bitterness (M03). C7 is therefore not expanded; the OT field remains in M03."
   `source_file` = `wa-m02-marah-mar-bitterness-lookup-v1-20260619.md` (with `wa-m02-evidence-verification-v1_0-20260619.md` as the originating flag).
2. The **M02 C7 ↔ M03** bitterness boundary registered as a Session D cross-cluster pointer, so it surfaces in cross-cluster synthesis.
3. M02 active-term membership unchanged; no M03 rows modified.

No physical deletes (wa-patch-instruction [current] §5.4).

---

## Completion confirmation

Return:

1. The recorded `cluster_finding` row(s) for M02 / C7 — `finding_status`, `finding_text` excerpt, `source_file`. Expected **1**.
2. The Session D cross-cluster pointer registering M02 C7 ↔ M03 bitterness — or, if that mechanism is not yet available, a report saying so.
3. M02 active-term count unchanged before/after: `SELECT COUNT(*) FROM mti_terms mt WHERE mt.cluster_code = 'M02' AND mt.status IN ('extracted','extracted_thin');` — same value pre/post. And confirm **0** M03 rows modified.

---

## Notes

- Source data: `wa-m02-marah-mar-bitterness-lookup-v1-20260619.md`; `wa-m02-evidence-verification-v1_0-20260619.md`.
- This is the **Option 1** resolution; **Option 2 (expansion) is ruled out** by the lookup — the OT field is already M03's by a principled sense-split.
- **Observation (not an operation):** the lookup notes H4843 *ma.rar* is present in M02 in its "provoke/embitter" sense with `status = NULL` — i.e. excluded from active-term queries (GR-DATA-001). CC may confirm whether that NULL status is intentional; flagged for awareness, **not actioned here** (out of scope for the C7 fix).
- **Dependency:** if the c1–c7 sub-group structure is not yet persisted, this finding sequences after that structure is created; CC reports if so. This directive is independent of DIR-20260619-001 (read-field corrections) and may be applied in either order.
