# Cluster Reading — data model proposal (escalation #1682, follow-on)

**Status:** design proposal, decision_required — not applied to any database. Edited in place per
the researcher's naming-conventions response (`Workflow/Chat_responses/Cluster-read naming
conventions`), which corrected §7 point-by-point and, in doing so, surfaced one substantial finding
(the `cluster_subgroup` collision, §2.1) that isn't a naming question at all.

**Split into 4 component design escalations**, this document stays the shared reference:
**#1690** family/grouping (now sharpened by §2.1 below) · **#1691** observation · **#1692** trace/
node (carries a real defect, see its own table definition) · **#1693** the load/reconcile pass.

## 1. Names resolved this round (adopted, not re-litigated below)

| Was | Now | Why |
|---|---|---|
| `cluster_reading_` prefix | `IB_` (Inner Being) | "cluster" is only part of the collection, "reading" only part of the operation — too narrow for what this actually is |
| `cluster_reading_observation` | `ib_observation` | stays "observation" conceptually — findings/facts/pointers/debate were all tried in this study's history; "observation" is the deliberately tolerant word that survived, because inner-being characteristics are inexact, multi-dimensional, and often debatable |
| `cluster_reading_trace` | `ib_node` | not a pure FK index — a node is a point of connection in a web of relationships; each column is one of the "cords" attaching it to other nodes, directly or indirectly |
| `kind` | `tag` | more commonly used; `kind` only crept in from lexical-analysis terminology. `flag`/`type`/`category`/`sub_category` are the same competing, equally-unhelpful synonyms this settles too |
| `span_surface` / `span_morph` | `surface` / `morph_code` | there is exactly one source for each (`span.surface`, `span.morph_code`) — no reason to rename what has no naming conflict in the new table. (`morph_code`, not `morph` — matching the source table's actual column name exactly, not a shortened guess.) |
| `verse` (trace field) | `verse_reference` | confirmed correct as-is — `verse.reference` is the base table's own canonical name; the explicit `verse_` prefix earns its keep here because the table also needs to reference *other observations* (a real naming conflict this table alone has, unlike `surface`/`morph_code`) |
| `SUNDRY` | `FLAG` | the project already has a convention for this — a term that doesn't fit and needs reallocation *is* a flagged-for-review item, not a novel bucket needing its own name. Inside the family-generation process this only **signposts** a strong toward FLAG; it does not reassign/action anything — the actual `cluster_strong` reallocation stays a separate, deliberate step |
| `slant_label` (on `ib_observation`) | `window` | matches the project's already-established "Window 1"/"Window 2" vocabulary directly — multiple windows onto the same evidence is exactly what this column holds |
| `statement` (on `ib_observation`) | `obs_text` | |

**My own documentation habit, corrected, not just for this doc:** short invented labels that only
mean something with tribal knowledge of one document version (`stable_key` was the flagged
example) get replaced with descriptive names throughout, going forward.

**Naming question above — RESOLVED (2026-09-12):** researcher confirmed the two complete, sibling
table names directly: `ib_observation`, `ib_node` (lowercase, matching the project's own prevailing
table-naming convention rather than the capitalized `IB_` draft used earlier in this document).
Both names below and throughout the component docs (#1690/#1691/#1692/#1693) use this final form.

## 2. Family does not become a new table — it becomes two EXISTING ones, and that changes the question

Per your instruction: family reverts to `cluster_subgroup` — "no reason to introduce another
competing term" when the concept (a finer subdivision of a cluster, itself approximate) already has
a home. Checked live, and this surfaced something real:

### 2.1 `cluster_subgroup` for M10 already has 34 rows and 125 active term-memberships — from the OLD characteristic-based method, not this session's lexical-family grouping

```
cluster_subgroup WHERE cluster_code='M10': 34 rows, subgroup_code M10-A..M10-X, M10b-A..F, M10c-A..E
  e.g. M10-A "Sin as committed act", M10-D "Guilt as inner-being state", M10c-A "Bodily-contact
  defilement-state" -- a CONCEPTUAL/thematic split (per-characteristic), not a lexical-gloss split
mti_term_subgroup JOIN cluster_subgroup WHERE cluster_code='M10': 125 active rows (real term
  placements already made against those 34 subgroups)
```

This is the **exact same data** escalation #1683 already asks about ("M10's 32 legacy
characteristic rows vs Window 2") — I'd said there they were probably separate questions. They are
not, once family is defined as living in this table: **if the new gloss-based families (H_guilt,
B_sin, G_transgression, ...) are written into `cluster_subgroup` under `cluster_code='M10'`, they
land in the same table, same cluster, as 34 already-populated rows from a different grouping
method** — distinguishable only by `subgroup_code` naming pattern (`M10-*` vs `M10b-*` vs `M10c-*`
vs whatever a new pattern would be) and free-text `source`/`version` columns, not by any structural
marker for "which method produced this."

**Resolved on #1683 this round:** hard-deleting the legacy rows was checked and confirmed
troublesome (blast radius: 9 tables, ~14,500 rows including `finding`/`cluster_finding`/
`verse_context`, colliding with CLAUDE.md's own no-physical-delete convention — full detail
`outputs/markdown/1683-m10-legacy-data-hard-delete-scope-v1-20260912.md`). Researcher's decision:
**rename the old tables, build fresh ones under the original names.** Corpus-wide, not M10-scoped —
the new `cluster_subgroup`/`mti_term_subgroup` (and siblings) hold every cluster's grouping, same
as the tables they replace.

### 2.1a Rename plan

**Prefix chosen: `zz_legacy_`** — sorts every renamed table to the bottom of any alphabetical
listing and states its status unambiguously (the researcher asked for a prefix satisfying both
properties without specifying the exact text).

**Renaming with confidence — these 6 tables exist *solely* to hold this old characteristic/
subgroup model, nothing else lives in them:** `characteristic` → `zz_legacy_characteristic`,
`characteristic_subgroup` → `zz_legacy_characteristic_subgroup`, `cluster_subgroup` →
`zz_legacy_cluster_subgroup`, `mti_term_subgroup` → `zz_legacy_mti_term_subgroup`,
`cluster_observation` → `zz_legacy_cluster_observation`, `cluster_finding` →
`zz_legacy_cluster_finding`. Fresh, empty `characteristic`/`characteristic_subgroup`/
`cluster_subgroup`/`mti_term_subgroup` tables get created for the new family model (`cluster_
observation`/`cluster_finding` are not part of the new model — no fresh replacement needed for
those two, per the design work already done in #1691/#1692/#1693; they'd simply cease to exist
under their live names once renamed, unless told otherwise).

**Not renaming `finding`, `verse_context`, `prose_section` — flagging this rather than guessing:**
these three are NOT dedicated to the old characteristic model — they're general-purpose, live
tables serving many other purposes across the whole project (`finding` is CLAUDE.md's own
"live unit," `verse_context` carries per-verse classification for every cluster and every
non-cluster verse-context use, `prose_section` is the entire prose store). Only SOME of their rows/
column-values relate to M10's legacy characteristic data (6,048 / 2,103 / 0 respectively, §
hard-delete-scope doc). Renaming the whole table would break everything else that uses them.
**Read "all 9 tables that is related can be renamed" as the 6 dedicated tables above — please
confirm, or correct if the 3 general-purpose tables were meant to be included (and if so, how:
renaming the whole table isn't right, so that would mean something different, e.g. migrating just
the M10-flavoured rows out into the legacy tables instead).**

### 2.2 The upgrade this reuse gives, once resolved

`mti_term_subgroup` links to `mti_terms.id` (a real, research_db-native, one-row-per-Strong's
FK) rather than a loose text-matched Strong's code — better than this document's original
proposal. Worth confirming at build time that every M10 strong already has an `mti_terms` row to
link to (very likely, given `mti_terms.cluster_code` already carries M-code assignment), not
assumed here.

## 3. `ib_observation` and `ib_node` — the two tables that ARE new

Unchanged in shape from the prior round except the name/column corrections in §1 (`tag` not
`kind`, `surface`/`morph_code` not `span_surface`/`span_morph`). Not re-drawn in full here since
family/`cluster_subgroup` (§2.1) needs resolving first and would otherwise force a second redraw.

## 4. Columns you asked for more information on, grounded in the real data

- **`stage`** (on `ib_observation`) — which of the three reading passes produced this row:
  `reading` (process c, e.g. the H_guilt/G1777 "enochos" example), `answer` (process d, one
  catalogue-question slant), or `synthesis` (process e, a cross-family comparative claim). Purely
  a provenance/routing field — nothing about the claim's truth-status depends on it.
- **`window`** (was `slant_label`; on `ib_observation`, `answer`-stage rows only) — the JSON's own field
  (formerly called a "slant"), e.g. `"guilt-against-God"`, `"guilt-remedy-before-God"`: a short tag
  distinguishing *which* of several genuinely different ways of looking at the *same* catalogue
  question (`question_code`) this row is — the same "window" concept already used elsewhere in this
  study (Window 1/Window 2). Two windows on `T0.1.1` for H_guilt exist precisely because the
  family's evidence itself splits — one window is not a correction of the other.
- **`obs_text`** (was `statement`) — the narrative claim itself, real example: *"enochos (liable to judgment /
  liable to council / liable to the hell of fire) — one verse, three escalating clauses, each
  attaching the same forensic-liability word to a different, more severe penalty..."* Always
  required, always meant to be readable with zero joins (your §7 instruction).
- **`status`** (`synthesis`-stage rows only) — `provisional` | `corroborated` | `superseded`. Real
  example: `status-vs-characteristic-hypothesis` (provisional, then superseded once
  `gradient-of-characteristic-hood` complicated it); the T4.6 spiritual-beings pattern was marked
  `corroborated` because all three positions were independently, mechanically checked, not just
  asserted once.
- **`revisit_note`** (`synthesis`-stage rows only) — the JSON's own field: what would confirm,
  complicate, or overturn this synthesis once more families are read. Real example (on
  `gradient-of-characteristic-hood`): *"Needs at least two or three more families (a clear
  act/behavior family and a clear positive-virtue family...) to know whether this is a real
  three-point gradient or just three data points that happen to differ."* An explicit invitation
  to revisit, not a closed verdict — this is the field that makes "accumulate with grace" concrete.
- **`seq`** (on `ib_node`) — ordering only, for when one observation cites several occurrences (the
  three "liable" clauses in one verse). **Its adequacy as a uniqueness key is exactly the open
  defect on #1692** — flagged there, not resolved here.

## 5. A concrete, real example of the verse-reference inconsistency you suspected

Checked live, not just recalled: this document's own §3 (prior round) cited `"1John 3:8"`,
`"1Cor 11:27"`, `"2Pet 2:4"`, `"Isaiah 53:5"` in free-text prose. `iba.db`'s own canonical
`verse.reference` for those same four verses is `'1Jo 3:8'`, `'1Cor 11:27'` (this one matched),
`'2Pe 2:4'`, `'Isa 53:5'` — **three of my own four examples used a non-canonical form.** This
confirms the risk is real and current, not hypothetical.

Where it matters structurally: process (a)'s occurrence data pulls `verse.reference`/`osisId`
straight from the DB by SQL (mechanically canonical, confirmed by reading the query). Process
(c)/(d)/(e) are LLM-authored JSON, not code — nothing currently guarantees the LLM copies that
exact string forward into a `trace`/`ib_node` row rather than paraphrasing it, the way I just did
in prose above. **Recommended fix, structural not corpus-wide-audit-shaped:** the load/reconcile
pass (#1693) should *resolve* `ib_node.verse_reference` by looking the citation up fresh against
`iba.db.verse.reference` (matched via strong + occurrence), never trust the string an LLM wrote in
its JSON — this closes the risk by construction for everything this pipeline writes going forward,
without needing a separate corpus-wide free-text audit. Free-text prose *inside* `obs_text` (not a
structured field) is a different, lower-stakes case — it's meant to be read, not queried, so it
isn't in scope for this fix. Confirmed as the plan, per the researcher's agreement this round.

**Checked the wider question ("is `verse.reference` used consistently in all current tables") —
reassuring, spot-checked, not exhaustive:** `finding_verse_link.reference`, `verse_span_index.
reference`, and the legacy (pre-IBA) `bible_research.db.verse.reference` were all sampled against
`iba.db`'s canonical form for the same verses (`Gen.8.1`, `Exod.2.24`, `Deut.5.15`, `John.14.26`,
`1Chr.10.1`) — **every sample matched exactly** ("Exo 2:24", "Deu 5:15", "Joh 14:26", "1Ch 10:1").
The structured, DB-native reference columns already agree with each other project-wide, at least in
this sample — the inconsistency risk found above is specifically in LLM/human-authored *prose*
(this document's own earlier draft included), not in any existing structured column. This doesn't
prove every row everywhere matches (not exhaustively checked), but it means the fix above (resolve
at load time, never trust LLM-typed text) is sufficient — there's no evidence of a second,
divergent "canonical" format already living in some other table that a validator would also need
to reconcile against.

## 6. Still open

1. **§1's `ib_observation`/`ib_node` concatenation question** — confirm or correct.
2. **§2.1a — confirm the rename scope**: the 6 dedicated tables, or does `finding`/`verse_context`/
   `prose_section` need something too (and if so, what, since renaming those whole tables isn't
   viable)?
3. Everything already open on #1690/#1691/#1692/#1693 individually.
4. **A permanent numbering scheme, specified in the generation script, not invented at load time**
   (unchanged from last round — filed onto #1691/#1693, not resolved here).

## 7. What building this actually involves, once the above is settled

A migration script that (a) renames the 6 confirmed legacy tables to `zz_legacy_*` and creates
fresh `characteristic`/`characteristic_subgroup`/`cluster_subgroup`/`mti_term_subgroup` tables,
corpus-wide scope; (b) creates `ib_observation`/`ib_node` in `bible_research.db`, registered in
`cfg_table`/`cfg_column` per `governance.tables`; (c) a load/reconcile pass (#1693) that resolves
verse references against `iba.db` rather than trusting LLM-authored strings, and implements the
still-undesigned same/broaden/new matching logic.
