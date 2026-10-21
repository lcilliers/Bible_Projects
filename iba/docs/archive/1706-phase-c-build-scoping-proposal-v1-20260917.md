# #1706 Phase C — build scoping proposal

**Continues escalation #1706** (Full lexical stack rebuild). Phases A/B/D/E are built and verified
(`outputs/1706-build-session-status-v1-20260916.md`, BUILD.md #267). This is the scoping/build
proposal for what's left: **Phase C** (build list items 13–16) and the first slice of **Phase F**
(item 24 — running it for real). Per the researcher's own build-session instruction ("just list
your issues"), this lists what's genuinely not settled before starting, rather than guessing and
building past a gap.

**Design status: closed.** #1711 (Layer 2 process design) and #1693 (recording pass / same-broaden-
new rules) are both `completed`/`approved` live in `escalation`. What follows is scope for the
remaining *build*, plus a small number of concrete gaps found while scoping it — not a re-opening
of either design.

---

## 1. What "build Phase C" concretely means

| Item | What it is | Status going in |
|---|---|---|
| 13 | The `verse_meaning` execution code — reads the 3 meaning sources per strong, per cluster, calls the LLM, produces `ib_observation` row(s) | **Not started.** Stage value `verse_meaning` already live in `cfg_enum`/`ib_observation.stage`. |
| 14 | Per-cluster scope wiring | `lexicalscope.resolve_strongs(cluster_code=...)` already exists and does exactly this resolution (used by Layer 1) — reusable directly, not new work. |
| 15 | Catalogue linkage (T1.1/T7.1) + the real FK | Catalogue rows exist (`wa_obs_question_catalogue` migrated into `iba.db`, 92 rows, #1696). FK itself still deferred (see §3.4). |
| 16 | Write path via the recording pass | #1693's same/broaden/new rules are stage-agnostic (§3 of that doc governs any `ib_observation` write, not process-(b)-specific) — reusable without new design. |
| 24 (Phase F slice) | Run it for real, once, bounded | Not started — no cluster has been run through this stage. |

## 2. What's already settled and reusable (no new design needed)

- **Stage/scope/linkage** — #1711's resolution: stage=`verse_meaning`, scope grain=per-cluster,
  T1.1 (Name/Naming) from surface + meaning-in-context, T7.1 (Lexical/Semantic Analysis) from
  Layer 1 + Layer 2 jointly.
- **Recording-pass rules** — #1693 §3's same/broaden/new logic, the exact-match duplicate check,
  and "ask only when genuinely material" are written generically for any `ib_observation` write;
  they need no rework for this stage.
- **Cluster→strong resolution** — `lexicalscope.resolve_strongs(cluster_code=...)`, already live,
  already used by Layer 1.
- **Cost/LLM plumbing** — `cfg_setting` module `lexical` already carries model/rate/cost-cap/log-
  path (`lexical.llm_model`, `lexical.llm_max_cost_per_batch=$1.0`, etc.), and
  `lexicalenrichgenerate.py` already has a tested batching+cost-estimate+Anthropic-call+usage-log
  pipeline built against these same settings (escalation #1549). It targets the OLD, now-dropped
  `verse_lexical_note` output shape, so it needs adapting to write the new `ib_observation` shape —
  real work, but not new design; an implementation choice I'll make directly (extend this module
  with a `verse_meaning`-shaped assembly/parse path, reusing its cost/API/config machinery, rather
  than fork a parallel copy), since it changes no rule and needs no decision.

## 3. What's NOT settled — found live while scoping this, not assumed

### 3.1 `ib_observation.tag` has zero registered values, for any stage, and the column is `NOT NULL`
Checked live: `cfg_column.use` for `ib_observation.tag` says "stage-specific enum, cfg_enum-
governed" — but no `ib_observation.tag*` group exists in `cfg_enum` at all (only `ib_observation.
stage` and `ib_observation.window` do), and the table itself has **0 live rows**. This isn't
Phase-C-specific — it blocks the *first write of any kind* to `ib_observation`, from any stage.
The governing-rules checklist already flags the taxonomy as open (`ib-observation-governing-rules-
checklist-v1-20260916.md`, "still-open items"), but hadn't been checked against the schema itself
until now — it's a hard blocker, not a loose end.

**Needs at minimum, before any write:** a tag value for a normal `verse_meaning` observation, and
the "genuinely couldn't resolve" tag the checklist's cross-cutting rule 6 already calls for but
leaves unnamed. I'll draft candidate values and run them through `configmaint.propose` once you've
seen this — not proposing specific strings blind in this doc.

### 3.2 T1.1/T7.1 answer cardinality — RESOLVED, researcher, verbatim, 2026-09-17
*"the duplicate rule for observations should kick in. that would also ensure that if there are
multiple verses with the same T1.1 and T7.1 then a new observation is not created, just ib_node to
reference the verse."* No separate cardinality policy is needed on top of #1693 §3: the stage
produces a T1.1/T7.1 judgment whenever the reading yields one, and the existing same/broaden/new
+ exact-match-duplicate rule already collapses identical answers across verses into one
`ib_observation` with additional `ib_node` grounding rows, rather than a new row per verse. Closed —
no new mechanism, no new design.

### 3.3 General observations vs. question-answers — same tag, or different?
Stage 5 produces two kinds of output per its own description: general lexical observations, and
slant-answers to T1.1/T7.1. Structurally these are already distinguishable by `question_code`
(NULL vs set) without a new column — but given §3.1's tag values are still unnamed, whether they
also need distinct `tag` values (vs. differing only by `question_code`) should be decided together
with §3.1, not separately.

### 3.4 The deferred FK
`ib_observation.question_code`/`ib_node.question_code` were left without a real FK because SQLite
FKs are declare-at-create-time only, and the write path didn't exist yet to justify the rebuild.
That write path is exactly what this build adds — proposing to close this now (one rebuild) rather
than defer it again to whatever builds next.

### 3.6 Additional rules specific to `verse_meaning`, checked against process (c)'s existing rule set — per researcher instruction 2026-09-17

Researcher, verbatim: *"the rules for observations apply to all phases, included verse-meaning.
Check if there are any additional rules that need to be formulated, driven by verse_meaning
requirements."* The cross-cutting §0 rules (checklist) already apply without exception — checked,
none excludes `verse_meaning`. Comparing `verse_meaning` against process (c) (the closest existing
analog — the only other stage that reads the meaning sources) surfaces these:

**Already decided, just needs recording (not a new judgment call):**
- **Read all 3 meaning sources as complementary evidence, never a pick-one-drop-the-rest** —
  researcher, verbatim, 2026-09-16 (quoted in the 1706 doc §4A): *"the important take away is to
  read meaning from all three tables because they are complementary, rather than replacing each
  other."* Directly inherited from process (c)'s own rule 2, confirmed applying to `verse_meaning`
  too. Action: add as `verse_meaning`'s own checklist section (§3.5) — recording an already-made
  decision, not proposing a new one.
- **`data-error` tag for source-quality problems hit while reading** (process (c) rule 13) — plain
  inheritance, no reason `verse_meaning` would differ. Bundled into the same checklist addition.
- **Verse references resolved fresh at write time** (checklist §0 item 5) — already cross-cutting,
  applies as-is.

**Genuinely open — found live, not previously flagged against `verse_meaning` specifically:**

1. **The `#1704` "structurally forced, not advisory" role-driven walk.** The 1706 doc's own §4A
   explicitly flagged this as a question for #1711 to decide (*"Whether stage 5 needs its own
   version of the 'structurally forced, not advisory' walk from #1704 §2 item 1 ... is itself part
   of #1711's design, not decided here"*) — but #1711's actual resolution (v11) settled only stage
   name, scope grain, and catalogue linkage; the role-driven-walk question was never answered. Real
   gap between what was supposed to be decided and what was. **Needs your call:** does
   `verse_meaning`'s read need a forced sequence (like process (c)'s stage-8 walk), or is free
   interpretation over the role/T-code data + earmarked questions sufficient (matching the #1705
   closure's own principle: guide by data, don't impose a resolution structure)?
2. **`needs_adjacent_verse_context` applicability.** This flag exists for process (c) (subgroup-
   scoped, post-formation reading). `verse_meaning` runs earlier, per-cluster, also reading
   meaning-in-context per occurrence for T1.1 — the same insufficient-context problem could
   plausibly arise here too. Not scoped for this stage anywhere on record. **Needs your call:**
   does the same flag apply at `verse_meaning`, or does this earlier stage handle thin context some
   other way (e.g. answer conservatively, defer entirely to process (c))?
3. **Per-strong completeness self-check.** Process (c) rule 10 requires every occurrence traced to
   ≥1 observation, checked as a computed `strong_checks` entry, not eyeballed. `verse_meaning` has
   no stated equivalent — nothing currently requires every strong `lexicalscope.resolve_strongs`
   returns for a cluster to produce ≥1 `verse_meaning` observation (or an explicit recorded
   non-finding) before that cluster counts as done. Proposing this as a direct analog, low
   controversy, but flagging rather than assuming since it's a new rule, not an inherited one.
4. **Cross-strong patterns noticed pre-subgroup.** Since `verse_meaning` runs before subgroups
   exist, a cluster-wide pattern across strongs could surface here the same way process (c)'s rule
   12 keeps cross-family observations out of the per-family reading, deferred to synergy. Checked:
   cross-cutting rule 5a (flags raised at discovery are never resolved inline, queued for synergy)
   already covers this generically — no new rule needed, just confirming it applies, which it does
   by the rule's own "governs every flag-shaped observation this pipeline raises" wording.

### 3.5 Documentation gap found while scoping
`ib-observation-governing-rules-checklist-v1-20260916.md` has sections for process (b)/(c)/(d)/(e)
and the cross-cutting rules, but **no section for the `verse_meaning` stage at all**, even though
#1711 (which fully specifies it) closed the same day the checklist was written. The checklist's
own preamble says it "goes stale the moment a decision is made elsewhere and not added here." I'll
add a §-for-verse_meaning section as part of this build, same unit of work, not a separate task.

---

## 4. Proposed build sequence

1. Register the tag taxonomy (§3.1/§3.3) via `configmaint.propose`, once you've confirmed the
   values.
2. Fold §3.6's decisions (once made) + the already-decided complementary-sources/data-error
   inheritance into `verse_meaning`'s own new checklist section (§3.5), same unit of work.
3. Add the `verse_meaning` write path to `lexicalenrichgenerate.py` (assembly + LLM call + parse
   into `ib_observation`/`ib_node` shape), wired to the recording pass's existing same/broaden/new
   logic (#1693) — no new recording-pass design needed. Register the new `cfg_step` this needs
   (none of process (b)/(c)/(d)/(e)/`verse_meaning` have one yet — checked live, `cfg_step` has
   nothing under any cluster-reading work package at all; this build registers `verse_meaning`'s,
   not the others).
4. Rebuild `ib_observation`/`ib_node` once to add the real FK on `question_code` (§3.4).
5. **One bounded test run** — a single cluster (M10, already prototyped once, or your pick),
   cost-estimated before the call per `lexical.llm_max_cost_per_batch`, checked against real data
   afterward (0 NULL/malformed rows, `ib_node` coverage double-checked per the checklist's rule 7,
   plus §3.6 item 3's proposed per-strong completeness check if approved) — not a corpus-wide push
   on the first run (`project_api_reads_budget_bounded_small_batches`).
6. Only after that test run is reviewed: wider rollout (remaining clusters), which is Phase F
   proper.

## 5. What I need from you before starting

- §3.2 (answer cardinality) — **RESOLVED**, no action needed.
- **§3.6 item 1** — does `verse_meaning` need `#1704`'s forced role-driven-walk sequence, or is
  free interpretation over role/T-code data sufficient (matching #1705's closure)?
- **§3.6 item 2** — does `needs_adjacent_verse_context` apply at `verse_meaning`, or is thin
  context handled differently at this earlier stage?
- **§3.6 item 3** — approve (or amend) the proposed per-strong completeness self-check.
- **§3.1/§3.3** — sign off on proceeding to draft tag values for `configmaint.propose`, or give
  your own preferred values directly. (Not blocking today — table is empty, 0 rows written — but
  needed before step 1 of the build.)
- **General go-ahead** on the sequence in §4, including closing the deferred FK now (§3.4), the new
  `cfg_step` registration, and the checklist addition (§3.5) as part of this same build.
