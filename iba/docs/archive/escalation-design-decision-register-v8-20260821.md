# Escalation design — decision register (v8, 2026-08-21) — batch 2

Supersedes [`escalation-design-decision-register-v7-20260821.md`](escalation-design-decision-register-v7-20260821.md).
Batch 2: closing the numbering gaps (D10, D13, D17, D20, D24) explicitly rather than leaving them
looking like silently-dropped items, and re-confirming D6's own completeness. No new design content
this batch — a reconciliation pass, exactly the kind of check this register exists to force.

---

## Numbering reconciliation — D10, D13, D17, D20, D24

Checked against every prior version rather than left ambiguous:

- **D10** — `cfg_escalation_link`, the typed many-to-many table. **REJECTED**, correctly recorded as
  such since v1 — wrong prefix, wrong shape. No further action; a rejected proposal doesn't need
  "configs touched," it needs to stay visibly rejected so it isn't proposed again by accident (which
  is exactly why it's still in this register at all).
- **D13** — never assigned. A gap in the original v1 numbering (D12 → D14), not a dropped decision —
  confirmed by re-reading v1's own list, which genuinely has no content between them.
- **D17** — never a real, separate decision. v1 used it as shorthand for "everything else carried
  forward from D1/D2/D5/D7" — a placeholder, not an item of its own. Retired as a number; its actual
  content is D1/D2/D5/D7, already tracked individually.
- **D20** — the BUILD.md/GOVERNANCE.md/CLAUDE.md/USER-GUIDE.md relationship. **Folded into D18**, not
  separately unresolved: D18's `cfg_escalation` rule (`issue_decisions_produce_documentation_tasks`)
  *is* the mechanism connecting items to all four documents — the produced-task pattern was always
  the answer to both D18 and D20 together, not two different fixes. Stated explicitly now so D20
  doesn't read as a dangling, unaddressed number.
- **D24** — "this register's own completeness and reliability." Self-referential by design — not a
  configuration decision, addressed by the register's own ongoing existence and this batch process
  specifically, not by a row of its own with configs touched.

---

## D6 — re-confirmed complete, not re-opened

Checked against the standard the rest of this register now holds to: D6's `cfg_escalation` row
(`rule_key='standing_items_survive_reset'`, full wording given in v2) already meets it — new config,
exact wording, no gaps found on re-reading. No changes this batch.

---

## Everything else

**Unchanged from v7.**
