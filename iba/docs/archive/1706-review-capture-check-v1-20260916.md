# Review: has #1706 captured everything, and what's still genuinely open

**Purpose:** researcher asked to review escalation #1706 (the consolidated lexical-stack rebuild
proposal, `1706-lexical-stack-full-rebuild-consolidated-build-proposal-v1-20260915.md`, now v15) —
were all its actions captured, and are any open items still outstanding. Checked live (DB queries,
full escalation history pulls for #1706/#1711/#1691/#1547/#1702), not re-derived from the document's
own claims alone.

---

## 1. What checked out clean

The document's central "nothing built yet" claim is confirmed live: `cluster_subgroup`,
`cluster_subgroup_strong`, `ib_observation`, `ib_node`, `wa_obs_question_catalogue` — none exist in
`iba.db`. `cluster.status` column doesn't exist (`cluster` table currently: `cluster_code`,
`short_name`, `description`, `gloss`, `deleted` only). This matches §7's closing line exactly.

## 2. One real inconsistency found — §6 Phase B item 9 is stale

**§6 Phase B item 9** ("Create the new verse-level `verse_meta` table (D13) — `language`, and
whatever else is needed at that grain") is listed as an **outstanding build action**. It is not
outstanding — checked live:

- `verse_meta` exists, registered in `cfg_table` (`database='iba'`, `category='data'`, use-text
  describing exactly this table, "Escalation #1608, 2026-09-09").
- Columns already include `language`, `testament`, `chapter`, `verse_num`, `passage_id`,
  `is_passage_anchor`, `lexical_complete_at`, `status` — the full D13 shape.
- 29,760 rows populated, auto-synced via triggers on `verse`/`verse_lexical`/`verse_passage`.

The document's own §8 register (row `#1608`) already says this correctly — *"Re-verified this
session: fully built, verified (29,759/29,759, 0 orphans), no residual gap"* — so the underlying
fact is known and correctly recorded in one place. §6 Phase B item 9 just wasn't struck through to
match. **Not a lost action — an internal cross-reference that didn't get updated.** Recommend
marking item 9 done (with a pointer to #1608) the next time the doc is touched.

One thing item 9's still-live half needs checking when Layer 1 actually rebuilds: item 8 says
`_narrative_morph_for`'s language check must be re-pointed to `verse_meta.language` "in the same
unit of work" as dropping `verse_lexical.language`. Checked live: `iba/app/lib/lexical.py`'s
current `_narrative_morph_for`/`_resolve_span_row` still source `language` the old (pre-rebuild) way
— confirming this re-pointing genuinely hasn't happened yet, consistent with Phase B as a whole not
having run. No contradiction there.

## 3. Three loose ends the document flagged — now closed, not yet reflected back into the doc's text

#1706 v15 was last edited 2026-09-16T13:02:46Z. A "session-end housekeeping" pass ran **after**
that (14:15:09–14:15:16Z) and closed out exactly the three loose ends #1706 itself had flagged as
outstanding:

| Escalation | #1706's ask | Live state now |
|---|---|---|
| #1691 (`ib_observation`) | §7 item 10: "close out #1691's escalation to match its 3 completed pack siblings — content is equally resolved, workflow hygiene" | v19, `re-assigned`/`ready_for_approval`, resolution: "ib_observation design complete per this escalation" |
| #1547 ("Prototype Window 2 analysis" placeholder) | §8 register: "recommend closing as superseded, not an open design question" | v2, `re-assigned`/`ready_for_approval`, resolution: "Superseded in practice by #1682's real cluster-reading work" |
| #1702 (T-code/answer-stage coverage) | §5: feeds Phase F item 28; not itself flagged as needing closure, but its content is fully absorbed elsewhere | v2, `re-assigned`/`ready_for_approval`, resolution: "Fully absorbed into #1704" |

**So: the actions *were* captured and actioned** — just about an hour after #1706's own text was
last updated, so the document itself doesn't yet show it. Not a gap in follow-through, a gap in the
document's own currency. Worth a quick edit-in-place next time #1706 is touched, not a new escalation.

## 4. What's still genuinely open (matches the document's own accounting — nothing new found beyond this)

- **#1711** (Design: Layer 2 lexical-observation process, stage 5/6) — the real, live design gate.
  Three concrete unresolved items: stage name/value (`meaning` vs `lexical`, not chosen), scope
  grain (per-strong corpus-wide vs per-cluster — leans per-cluster on volume, but the term-grain
  question for T1.1/T7.1 cuts the other way, not settled), and which catalogue question(s) it links
  to (T1.1/T7.1 named as candidates only). Deliberately deferred by your own instruction until Layer
  1's build work is done — v10 (08:13:23Z) is still the latest, no movement since.
- **Pack sign-off** (§7 items 4/10) — all 6 components (#1690/1691/1692/1693/1696/1697) are
  design-complete, but you haven't yet given the actual go-ahead nod across the set. This is the one
  item genuinely waiting on you, not on any further Claude-side work.
- **#1607** — still correctly open as the parent venue for Layer 1/2 column validation (minor doc
  staleness: §8 cites it as "v17," live state is v18 as of this morning — no content gap, just an
  uncorrected version number).
- **#1524** — held pending #737's own direction; #737 remains gated/open. The doc flags this as
  "worth confirming this doesn't need re-opening once #737 moves" — not resolved, correctly not
  urgent.
- Smaller carried items, all correctly listed as open rather than silently dropped: `idiom`
  note_type (no confirmed catalogue-question match yet), `pattern_type` crosswalk sequencing
  question (write now vs. fold into #1696's migration insert — a sequencing call for you),
  #1444's 10 unexercised mechanical/interpretive question-code splits (tracked at #1704, not yet
  actioned).
- **The entire 34-item build list itself (§6)** — Phase A/B (Layer 1 readiness + rebuild) hasn't
  started; everything downstream is sequenced after it.

## 5. Bottom line

No actions were found lost or uncaptured beyond what #1706 already tracks in its own §7/§8. The two
real findings from this review are both small and both about the document's own currency, not about
missing follow-through: (a) §6 item 9 should be struck as done (verse_meta/#1608), and (b) §7/§8's
mentions of #1691/#1547/#1702 should be updated to reflect they closed at 14:15, after the doc's own
last edit. The one substantive thing still actually waiting on you is the pack sign-off + #1711's
three design choices — everything else genuinely is either done, correctly deferred, or already
tracked as open.
