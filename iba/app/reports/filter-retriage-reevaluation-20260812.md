# Re-evaluation — "Filter re-triage" against the now-built cluster work

> Requested 2026-08-12: re-read the original filter-re-triage planning, then check it against the
> cluster model (T2/T3/FLAG/M01-M46, 4,398 `cluster_strong` rows) built later the same recovery
> session. Nothing built yet — this is the re-evaluation only.

## 1. What filter re-triage was originally scoped to be

From the recovered plan (`first-raw-data-vivid-fairy.md`, "Stage b — Strong relevance") and the
session log §1, written **before** the cluster tables existed:

- **The gap named:** `raw.discover`'s only filter is STEP's reserved grammatical-particle range
  (`discovery.particle_pattern`, `^[HG]9\d{3}$`) — live-confirmed, still the only one today.
  Everything else STEP's bare `masterSearch(meanings=<word>)` returns is written to `word_strong`
  unfiltered. This is the exact mechanism that let `receive`'s 64 seeds through with **79%** of
  occurrences from 9 high-frequency codes unrelated to "receive" as an inner-being movement
  (BUILD.md §99) — the word was rolled back wholesale as a result.
- **The decision recorded** (session log §1): *"T2-style POS exclusion and proper-noun exclusion →
  `raw.discover`-safe, config-driven. F1–F5 (lexical-family) → safe for its own narrow purpose, not
  a general filter. GR-PROG-007 and the physical/action category → downstream only."*
- **Two precedents identified, never wired into IBA:** (a) a **mechanical lexical-family** filter
  (old project's F1–F5 script shape — proper-noun/high-frequency-particle/root-family membership),
  narrow-purpose only; (b) **GR-PROG-007**'s semantic inner-being test, term-in-verse-use grain —
  judged too fine-grained for IBA's actual problem, which is **per-code, at discovery, before any
  verse is looked at** (plan's own words).
- **Judgment call #6 (unresolved when the plan was written):** whether stage b needs *both*
  precedents combined, or one — "confirm that split... before I turn it into a build spec."

None of this had been implemented. The cluster-model adoption (BUILD.md §103–106, later the same
session) is explicitly filed as **superseding this exact bespoke-filter approach** — §103's own
trigger line: *"researcher direction to adopt the old project's 49-cluster taxonomy... into IBA
wholesale, superseding a bespoke-filter approach."*

## 2. What actually got built since, and how comprehensive it now is

- `cluster` (50 rows: M01–M46, `FLAG`, `T2`, `T3`) + `cluster_strong` (4,398 active rows) — **zero
  gap across all 3,456 word-origin Strong's codes** IBA currently has (confirmed live, §105/106).
- Live breakdown by bucket (today): **T2 "Supplementary" 1,227** · **T3 "Operations" 493** · `FLAG`
  "Flagged for Review" (small) · M01–M46 content clusters (87–144 each, e.g. M23 144, M01 113).
- **`T3` did not exist when the original filter-re-triage plan was written.** It was created
  2026-08-12 (§105) specifically to hold *"a strong considered as a human operation/movement, not
  tied to one inner-being cluster"* — i.e. exactly the physical-action-verb category the original
  plan had already named and deliberately pushed **"downstream only"** because, at the time, there
  was no mechanism to pre-identify those codes. There now is.

## 3. Live validation against `receive`'s actual failure — not assumed, checked

Looked up the 9 high-frequency codes BUILD.md §99 named as `receive`'s 79%-noise set, against
`cluster_strong` as it stands today:

| Code | Meaning | Current cluster | Source |
|---|---|---|---|
| `G2983` (lambanō, "take") | the code that started `receive` | **T3** | `llm-allocation-v1_3` |
| `G1325` (didōmi, "give") | | **T3** | `llm-allocation-v1_3` |
| `H4672` (matsa, "find") | | **T3** | `llm-reassignment-v1_1` |
| `G2192` (echō, "have/be") | | **M23** (a real content cluster) | `old-system-migration` |
| `H0935`/`H5414`/`H8085`/`H3947` (bo/natan/shama/laqach) | | *no row — no longer in IBA's `strong` table at all* (fully rolled back with `receive`) | — |
| `G2980` (laleō, "speak") | | *no row — exists in `strong` but `origin='backfill'`, out of cluster-mapping scope by design* | — |

**Two real findings, not just confirmation:** (a) 3 of the 9 land correctly in `T3` — cluster
lookup would have flagged them. (b) `G2192` lands in **`M23`, a genuine content cluster** — not
noise. This independently corroborates what the power-failure recovery session's §1 already found
by re-litigating the rollback: *the "79% noise" framing overstated it* — at least one of the nine
supposedly-noise codes is legitimately inner-being-relevant. Cluster lookup would have surfaced
that distinction directly instead of requiring a full rollback-and-relitigate cycle to discover it.

## 4. The redefinition — what "filter re-triage" concretely becomes

**Before:** build a POS classifier and a proper-noun detector from scratch, config-driven, at
`raw.discover` time — real new-mechanism work, undesigned beyond the two named precedents.

**Now:** for the ~99%+ of candidate codes that overlap what IBA (or the old project) has ever
classified, the classification **already exists as data**. The work shrinks to: wire a lookup step
into (or right after) `raw.discover` against `cluster_strong`, and branch on what comes back — plus
one real remaining gap and real open policy questions (below), not a from-scratch build.

### The one real remaining technical gap: T2 is not POS-split yet

The canonical T2 definition (`Workflow/Instructions/01c-T2-treatment-and-API-governance.md`,
**SETTLED 2026-06-17**, binding on the old project's scripts) is explicit that T2 is **mixed, not a
disposable bin**: T2-content (POS ∈ {noun, verb, adjective} — genuine qualifier/seat/relational
context, ~81% of the old project's T2) is **kept as context**; only T2-grammatical (POS ∉ that set
— pure function words, ~19%) is **excluded**. IBA's `cluster_strong.cluster_code='T2'` (1,227 rows)
carries no such split today — it's the flat old-project bucket, one classification per Strong's
code, not per-occurrence POS.

IBA already has a structurally similar (but not identical) classifier — `lib/lexical.py:
classify_role(strong_code, morph_slice) -> "function"|"content"` — Hebrew via STEP's reserved
H9xxx-formative range, Greek via a `morph_slice` POS-tag check (`PREP`/`PRT`/`CONJ`/`ART`). It is
**per-occurrence** (morph varies by span), not a fixed per-code POS the way 01c's rule is framed,
and — important cautionary precedent, same file — a role-based **exclusion** was tried once already
(gating `resolve_code()` on `role=='function'`) and reverted the same day (BUILD.md §56-57) because
it silently dropped real content: H9xxx codes DO carry genuine glosses. That was a *resolution-layer*
gate, not a *discovery-time* one — a different decision — but the failure mode (a role-based filter
quietly discarding real data) is exactly the risk to design against here too.

### T3, FLAG, and "no row at all" — policy questions the cluster work reopens, doesn't answer

The original plan explicitly decided the physical-action category should be **"downstream only"**
— *because no mechanism existed to catch it earlier*. That premise no longer holds; `T3` now
pre-identifies 493 such codes as data. Whether the *policy* should change is a fresh question, not
a foregone conclusion — the researcher's own re-litigation of the rollback also found that at least
one supposed-noise code (`G2192`) was legitimately relevant, i.e. `T3` membership itself is not a
guaranteed "safe to exclude" signal.

## 5. Open questions — need your direction, not decided here

1. **T2 at discovery — exclude all `cluster_code='T2'` codes wholesale, or only the subset that
   also classifies as grammatical by POS** (the canonical 01c split, not yet built for IBA)? The
   flat version is buildable today with zero new mechanism; the POS-split version matches the
   already-settled canonical rule exactly but needs a per-code (or per-occurrence, mirroring
   `classify_role`) POS classification pass built first.
2. **T3 at discovery** — still pure downstream (the original, pre-`T3` decision), or now
   flag-for-review, or hold, or exclude-with-an-override-path, given the codes are pre-identified?
   `G2192`'s case argues against a blind exclude.
3. **`FLAG` at discovery** — hold/escalate to the researcher (matching its own name), or pass
   through with a note?
4. **Codes with no `cluster_strong` row at all** (genuinely new to both projects, or new to IBA and
   not yet allocation-passed) — this is the case that actually matters most for *future* words,
   since `cluster_strong` only covers codes already in IBA's `strong` table as of each seed/
   allocation pass, and a candidate code raw.discover surfaces for a brand-new word usually isn't
   there yet. Checked: the old project's `mti_terms` (the ultimate source) covers only ~2,761
   cluster-tagged Strong's codes total, and IBA already holds ~98% of the overlap — so a live
   cross-DB lookup at discovery time would help only at the margins, not solve genuinely novel
   codes. Options: (a) the old F1–F5-shaped mechanical fallback (proper-noun/high-frequency check,
   already judged "safe, narrow-purpose" and unaffected by any of this), (b) queue unclassified
   codes into a new LLM-allocation batch — the exact workflow already proven twice (§105/§106), now
   repeatable rather than one-off, or (c) inline escalation to you per new word.
5. **Should a discovery-time exclusion still write a (soft-deleted) `word_strong` row for audit**,
   matching the project's standing "never omit, soft-delete instead" convention, or never write one
   at all for a code that never entered the study?
6. **Should `raw.discover` write a provisional `cluster_strong` row (`cluster_code=NULL`/pending)
   for a code it finds with no existing assignment**, so future unclassified codes accumulate into
   a natural queue for the next allocation pass, rather than silently staying ungoverned until
   someone happens to check again (the exact shape of gap that let `receive` through in the first
   place)?

## Bottom line

The cluster work doesn't just inform filter re-triage — it **replaces most of its originally-scoped
build**: for already-known codes, "build a classifier" becomes "look one up." What's left to design
is narrower but real: the T2 POS-split (a genuine, currently-missing piece, with a cautionary
precedent on how not to build it), and four policy calls (T3/FLAG/unclassified/audit-trail
handling) that the cluster data raises but doesn't itself settle.
