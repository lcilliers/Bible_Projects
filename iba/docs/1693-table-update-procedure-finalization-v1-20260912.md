# Escalation #1693 — the table-update procedure — consolidated spec, for final sign-off

**Status:** consolidation for review, decision_required. Nothing built. This is where #1690/#1691/
#1692's separate "table-update procedure" sections converge — per the researcher's own framing,
**the table update is one operation, separate from any LLM session**, that reads a family's
finished JSON (process b's family/subgroup output, or process c/d/e's observation output) and
writes `cluster_subgroup`/`mti_term_subgroup`/`ib_observation`/`ib_node` rows. This document is the
operational spec for that one procedure; #1690/#1691/#1692 stay the table-shape specs it writes
into.

## 1. What it takes as input

- Process (b)'s family/subgroup JSON (§2, `iba/docs/1690-...md`).
- Process (c)/(d)/(e)'s observation JSON, each observation carrying its own `source_json_serial`
  (§2 item 1, `iba/docs/1691-...md`) and its supporting node segments (§2 item 2, same doc).

## 2. What it does, per table (pulled from #1690/#1691/#1692, not re-decided here)

| Table | Responsibility |
|---|---|
| `cluster_subgroup` | assigns `id`; resolves strongs to `mti_terms.id`; writes the `FLAG` signpost as a same-cluster subgroup (reading not yet confirmed, #1690 §3 item 3) |
| `mti_term_subgroup` | enforces `UNIQUE(mti_term_id)` — one strong, one family |
| `ib_observation` | assigns the permanent `id` (distinct from the LLM's own `source_json_serial`, which is kept alongside it); decides, per incoming observation, whether it's genuinely new, broadens an existing row's `obs_text`, or just adds another citation to an existing row — **this decision logic is the one piece of this whole design that is still completely undesigned, see §3** |
| `ib_node` | assigns `id`; denormalizes `cluster_code`/`cluster_subgroup_code`/`strong` onto each row; **resolves `verse_reference` fresh against `iba.db.verse.reference`**, never trusting the LLM's JSON string directly |

## 3. The one piece with no design yet: same / broaden / new

This is the actual judgment call the whole two-pass architecture depends on, and nothing here
answers it yet:

1. **How is "this citation supports an existing observation" actually decided?** Exact text match
   is clearly insufficient (two independently-written claims about the same phenomenon will use
   different words). Options not yet weighed against each other: a similarity/embedding match; an
   LLM-judged comparison as part of the table-update procedure itself; a human-reviewed queue for
   anything below a confidence threshold; some combination.
2. **What happens on an ambiguous match** (a candidate could plausibly be 2+ existing
   observations)? Auto-pick the closest, always queue for review, or refuse and require the
   generation session to be more specific?
3. **Idempotency** — re-running the table-update procedure on the same family's JSON (e.g. after a
   correction) should not duplicate `ib_node` rows. This is currently blocked on `ib_node`'s own
   unresolved uniqueness defect (#1692 §4 item 1) — the `seq`-only key doesn't give the procedure
   anything reliable to check re-runs against yet.

## 4. What's already settled and doesn't need re-deciding here

- Verse-reference resolution: resolve fresh from `iba.db`, never trust LLM-authored text (#1682 §5,
  confirmed by the researcher).
- The LLM never assigns permanent ids, never checks for duplicates against the database, never
  decides edit-vs-new — all three are this procedure's job (#1691 §3, researcher's own framing).
- Denormalization happens here, at write time, not in the LLM's output.

## 5. What "finalized" would mean

§3 is the actual remaining work — a real algorithm, not a naming or column decision, and the
biggest single gap left across all four escalations. Everything else this procedure needs
(verse-reference resolution, denormalization, id assignment, the FLAG-as-signpost writing rule) is
already specified in #1690/#1691/#1692 and just needs implementing once #1692's `ib_node`
uniqueness defect and this document's §3 are both resolved.
