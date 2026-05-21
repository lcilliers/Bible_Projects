# M08 Phase 5 — Sub-group formation — **RESUBMISSION brief (v2)**

**Date:** 2026-05-20
**Cluster:** M08 — Pride, Arrogance and Boasting
**Phase:** 5 (resubmission after distribution-gate failure)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §8

**Read this brief in conjunction with your v1 design.** The v1 design is structurally sound — only two specific revisions are needed.

---

## Validation result on v1

| Check | Status | Detail |
|---|---|---|
| §8.6 distribution gate | ⛔ **FAIL** | M08-A holds **151/295 = 51.2%** of substantive verses (threshold: 40%) |
| §8.0 characteristic-only | ⚠ **OBSERVATION** | Two non-characteristic holding sub-groups present (M08-F, M08-G) |
| Mapping completeness | ✓ PASS | All 470 vc rows assigned; all 0 unmatched split references |

Validation report: [WA-M08-phase5-distribution-validation-v1-20260520.md](WA-M08-phase5-distribution-validation-v1-20260520.md)

**Reason for the 51.2% vs your 32.0% discrepancy:** §8.6 measures against substantive verses only — verses in characteristic sub-groups. M08-F (cross-register holding, 122V) and M08-G (marginal holding, 52V) are *not* characteristic sub-groups (you said so yourself in §5) and therefore are excluded from the denominator. The substantive total is 295, not 465.

---

## What to revise

### Revision 1 (REQUIRED) — Split M08-A via a documented axis

M08-A "Arrogant Self-Elevation — the Dispositional Core" currently carries 151 verses (51.2% of substantive). Under §8.6 this requires a volume-split into multiple sub-groups, all representing the same characteristic (CHAR-1: arrogant self-elevation) but split by a named axis.

**Candidate axes (your judgment, based on the verse evidence):**

1. **Seat / locus axis (RECOMMENDED — strongest evidence from your v1 design itself):**
   - **M08-A1** — Heart-elevation (lev/kardia idiom): "lifted-up heart" — Deu 8:14; Pro 16:5; Eze 28:2; Eze 28:5; Dan 11:12; Hos 13:6; 2Ch 26:16; Psa 101:5; Jer 48:29; Eze 31:10; Dan 5:20 — your v1 already names the heart as pride's seat.
   - **M08-A2** — Eye-elevation / haughty-eyes (ayin idiom): Psa 18:27; Isa 2:11; Pro 6:17; Isa 5:15; Pro 30:13; Psa 131:1; etc. — the eye as register of pride.
   - **M08-A3** — Spirit / posture-of-being elevation: Ecc 7:8; Dan 5:20; ga.vo.ah in the spirit, etc.
   - **M08-A4** — General self-exaltation (residual rum/ga.on/ge.eh/ga.a.vah pride verses not specifically heart/eye/spirit).

2. **Vertical/horizontal axis:**
   - **M08-A1** — Vertical: pride that lifts itself against God (most ga.on, hupsēlos-context, rum-self-against-Yahweh verses).
   - **M08-A2** — Horizontal: pride that elevates self over others (contempt-of-neighbour, claim-of-precedence — some ge.eh, ga.a.vah, hupsēlofroneō-adjacent verses).

3. **OT/NT axis:**
   - **M08-A1** — OT self-elevation vocabulary (Hebrew terms).
   - **M08-A2** — NT self-elevation vocabulary (huperēfania, hupsēlos, filautos).
   - *Weaker axis* — splits by language register rather than by inner-being content; use only if axes 1 and 2 fail.

**Pick the axis the verses themselves support most cleanly.** Each resulting sub-group must:
- Carry the same characteristic identity (CHAR-1) — note this in `core_description`.
- Hold **<40% of substantive (post-split)** verses.
- Have a `split_axis` field naming the axis explicitly: e.g. `"split_axis": "seat_of_pride: heart | eyes | spirit | general"`.

**Note:** Other characteristic sub-groups (M08-B, C, D, E) are within gate and need no further splitting.

### Revision 2 (RECOMMENDED but optional) — Holding sub-groups → Phase 5 set-aside

Your v1 introduces M08-F (122V cross-register holding) and M08-G (52V narrative/marginal holding) for verses whose terms STAY (per §6.3.2) but whose individual verses carry no M08-relational content. This is honest analytical work but creates a new pattern not yet documented in v2_8 §8.

**Recommended treatment:** Mark these 174 verses as **set_aside** at the verse_context level (not routed to any sub-group) with explicit `set_aside_reason` fields:

| Holding source | Recommended set_aside_reason |
|---|---|
| M08-F (divine majesty / God-directed glorying) | `"non-M08 content — M22-register (divine majesty / God-directed exaltation); term STAYS in M08 via other verses"` |
| M08-G (narrative markers, neutral assertiveness) | `"non-M08 content — narrative marker / neutral assertiveness; no inner-being state evidenced"` |

This:
- Keeps Phase 5 sub-groups all characteristic (clean §8.0 compliance).
- Preserves audit trail via the `set_aside_reason` text.
- Lets Phase 8.5 focus only on G0193 akratēs (the actual BOUNDARY).
- Avoids carrying empty holding sub-groups through Phases 6–8.

If you prefer to keep M08-F/M08-G as sub-groups, note that explicitly in your design and CC will codify the holding-sub-group pattern in v2_9 of the instruction.

### Revision 3 (REQUIRED if you adopt Revision 2)

Update the verse-to-sub-group mapping to:
- Reassign M08-F and M08-G verses to a new field `set_aside` (list of vc references or vc_ids) with the appropriate `set_aside_reason`.
- Re-validate substantive count: should drop to 295 (which is what the substantive count already is post-holding-exclusion).

---

## What to keep

Everything else in your v1 design is sound:

- The 5 characteristics (CHAR-1 to CHAR-5) — well-grounded in the meaning corpora.
- M08-B (Presumptuous Defiance, 45V, 15.3% — within gate after recompute).
- M08-C (Boasting and Self-Display, 70V, 23.7% — within gate; M22 cross-register flag noted; Phase 7 will VCG-distinguish self vs God-directed boasting).
- M08-D (Vain Conceit, 12V, 4.1% — within gate).
- M08-E (Pride of Power and Position, 17V, 5.8% — within gate; M23 cross-register flag noted).
- M08-BOUNDARY (G0193 akratēs, 1V).
- Multi-faceted term handling (rum/ga.on/ha.lal/ma.rom etc.) — primary + split format works.

---

## Outputs

1. **Revised sub-group design** — `Sessions/Session_Clusters/M08/WA-M08-subgroup-design-v2-20260520.md`.
2. **Revised mapping JSON** — `Sessions/Session_Clusters/M08/WA-M08-subgroup-mapping-v2-20260520.json`.

If you adopt Revision 2 (set-aside instead of holding sub-groups), the mapping JSON should include a `verse_set_aside` block:

```json
{
  "_meta": {...},
  "subgroups": {
    "M08-A1": "...",
    "M08-A2": "...",
    ...
    "M08-BOUNDARY": "..."
  },
  "term_assignments": {
    "<mti_id>": {
      "strongs": "...",
      "translit": "...",
      "primary": "M08-A1",
      "split": {"M08-A2": ["ref", "ref"]},
      "set_aside": {"reason_code": ["ref", "ref"]}
    }
  }
}
```

If you keep M08-F/M08-G as holding sub-groups, keep your v1 JSON structure unchanged and just update the term_assignments to reflect the new M08-A1..A4 splits.

---

## Discipline reminders

1. **§8.6 measures against characteristic-sub-group verses only**, not against total ex-BOUNDARY. Holding sub-groups (if you keep them) sit outside the denominator.
2. **§8.0** — each sub-group must represent a characteristic. Volume-splits carry the same characteristic identity across multiple sub-groups (M08-A1 through M08-A4 all = CHAR-1).
3. **Cross-register flags travel forward.** M22 flag stays on M08-C and M08-F (if kept). M23 flag stays on M08-E.
4. **No BOUNDARY parking** (§8.4.1). G0193 akratēs is the only BOUNDARY-verdict term and the only verse permitted in M08-BOUNDARY.

---

## After you finish

1. Save the revised design + mapping to `v2-20260520`.
2. Ping CC: "M08 Phase 5 v2 sub-group design ready".
3. CC re-runs the resolver + validator. PASS → Phase 6 directive.

---

*End of resubmission brief. Load this brief alongside your v1 design and the Phase 3 verdict document; revise from there.*
