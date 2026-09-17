# `wa_obs_question_catalogue` — completeness findings

**Continues #1706.** Per researcher instruction, 2026-09-17: *"I notice that the
iba.wa_obs_question_catalogue has some errors and omissions, and that make me think that you are
not taking into account the questions that is specifically dependent on the roles - and therefore
your baseline is incomplete. source_word, and source_registry_no is relics of the past and the
columns can be dropped. Pattern_type is outstanding. scope should be a clear indication of when the
question would apply (e.g. verse-reading or char-reading or char-answer or synergy."* Checked live
against all 92 active rows, not assumed. You're right — the earlier gather (#1704, and my own
role-driven-walk/role-data-presentation docs today) took the catalogue's completeness as settled
ground it should have re-checked, not just cited.

---

## 1. `source_word`/`source_registry_no` — confirmed, exactly as you said

`source_word` is the literal string `"Programme"` on **all 92 rows**, no variation — carries zero
information. `source_registry_no` is **NULL on all 92 rows**. Both relics of a pre-cluster,
per-word-registry-scoped version of this catalogue. **Confirmed droppable** — holding for your
go-ahead on the mechanics (SQLite `ALTER TABLE DROP COLUMN` needs the `cfg_column` rows for both
retired in the same unit of work, and I should check nothing still reads them before dropping —
not done yet, this doc is findings, not the fix).

## 2. `pattern_type` — confirmed outstanding, exactly as you said

**90 of 92 rows are NULL.** The only 2 populated rows are `T2.11.1`/`T2.11.2`
(`faculty-engagement-reflection`) — set when that pair was authored, nothing else since. This
matches what #1704 Phase 3 already found (*"a complete question-to-event crosswalk ready to apply
from Phase 1c's own per-component tables"*) and flagged as a sequencing question that was never
actually resolved into action — it's been "ready to apply" since 2026-09-16 and stayed that way.

## 3. `scope` — real semantic gap, not just a naming nit

Checked live: `scope` currently holds 8 **topical/evidentiary** categories — `Word/term (lexical)`
(26), `Characteristic relational` (17), `Characteristic (HIB behaviour)` (15), `Other non-human
beings` (12), `Verse-context` (10), `The verse` (4), `The HIB` (4), `Science` (4). **None of these
say which pipeline stage answers the question** — your point exactly.

**A deeper problem found checking this, not just the missing axis itself:** `question_text` already
carries its own implicit grain signal, inconsistently, and it doesn't line up cleanly with
`verse_meaning`'s own assigned questions:
- Some questions are explicitly **per-verse**: T0.1.1, T0.2.1, T2.1.1 all open "In this verse...".
- Some are explicitly **cross-verse, whole-characteristic**: T0.1.2a/b, T0.2.2/2.3, T2.1.2 open
  "Across the characteristic's verses..." / "Across the evidence...".
- **`T1.1`/`T7.1` — the two questions #1711 assigned to `verse_meaning` — use neither framing.**
  T1.1.1: *"What is the characteristic called in the programme..."* T7.1.2: *"What is the
  grammatical range of the primary term..."* These read as **whole-term lexical-profile**
  questions (a term's grammatical/semantic range doesn't change per verse or per occurrence) —
  closer to a fixed dictionary fact than either "in this verse" or "across this characteristic's
  verses." Whether that's fine (a per-cluster aggregate over that cluster's own strongs, which
  legitimately fits `verse_meaning`'s per-cluster grain) or a real mismatch with how #1711 described
  the derivation ("read per occurrence") isn't resolvable from the wording alone — **flagging
  for your call, not assuming either reading.**

**Proposed for your decision, not built:** does `scope` get **overwritten** to hold stage values
(`verse-reading`/`char-reading`/`char-answers`/`char-synergy`, matching today's earlier stage-rename
proposal), with the current topical categorization dropped or moved to a new column — or does a
**new column** carry the stage value alongside the existing `scope`, which stays topical under a
clearer name? Your instruction reads as the former (repurpose `scope` itself), but the current
content isn't obviously worthless (it's a real, populated topical axis) — checking before deciding
one destroys the other.

## 4. Role-dependent tier coverage — the specific "roles" gap, checked tier by tier

| Tier | Catalogue questions | Role/T-code it corresponds to |
|---|---|---|
| T0 | 9 | — (divine-nature, not role-driven) |
| T1 | 19 | — (name/kind/boundary, not role-driven) |
| T2 | 8 | Constitutional location/faculty — **has questions** (incl. `T2.11` faculty, just added) |
| **T3** | **0** | **Operation/action words — the role-driven walk's own step (b)(iv) pivot. No tier exists at all.** Its numeric slot was historically the retired Inner-Faculties tier (#1598) — a coincidental numbering collision with the T3 *role code* (operation flag on `cluster_strong`), not the same thing, worth being explicit about so the two "T3"s aren't conflated. |
| T4 | 20 | Divine/human interface (party_kind-driven) — **has questions**, the catalogue's largest tier |
| T5 | 5 | Transformation/mechanism — has questions, T5.3 informally expected to absorb some T3 evidence (per #1704 v3) but never says so in its own wording |
| T6 | 13 | Relationships/co-occurrence — has questions |
| T7 | 18 | Lexical/verse/science — has questions |
| **T8/T9** | **0 dedicated** | Other party-kinds — only partially reached via `T4.6` (5 questions, adversarial+angelic only; #1700 confirmed zero live findings ever through this path) |
| **T10–T15** | **0** | Referent-identity (places/corporate/objects/natural-world/body-parts/calendar) — #1704 Phase 1c's own explicit, checked conclusion was "genuinely 0 catalogue demand," not a miss. **Re-flagging for your confirmation now**, since that conclusion predates today's role-data-presentation design, which argues for surfacing these tags even where nothing consumes them yet — worth checking whether "no catalogue demand" still holds under that reasoning, or whether it should. |

**The clearest concrete gap: `T3` has no catalogue home at all**, despite being the single most
load-bearing role in the whole walk design (#1704 §2 (b)(iv): *"the operation word's relation to
every nearby party-kind word AND every nearby referent-identity word"*) and the entire subject of
#1705's saga. Right now, a `verse_meaning`/`char-reading` pass that surfaces a genuine T3 finding
has nowhere in the catalogue to answer *into* — it would have to sit as an unlinked general
observation (`question_code` NULL), never as a direct answer to a T3-scoped question, because no
such question exists.

## 5. What I need from you

1. Go-ahead to drop `source_word`/`source_registry_no` (mechanics: `cfg_column` cleanup + confirm
   nothing reads them first).
2. Direction on `pattern_type` — apply #1704 Phase 3's existing crosswalk now, or hold until §3/§4
   are settled (some of it may need to change once `scope`/T3 are resolved)?
3. `scope` — overwrite with stage values, or a new column alongside it? And how should the T1.1/T7.1
   grain question (§3) factor into whichever stage value(s) get assigned?
4. Does `T3` need its own new tier/questions authored (mirroring `T2.11`'s precedent), or should its
   findings continue to feed into existing tiers (T4.1–T4.5, T5.3) as `#1704` originally proposed —
   just made explicit in those questions' own wording rather than left implicit?
5. Should T10–T15's "0 catalogue demand" (§4) be reopened given today's role-data-presentation
   design, or does that conclusion still stand?
