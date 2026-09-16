# IB Observation — governing rules checklist

**Purpose, per researcher instruction, 2026-09-16:** *"these methods should be fundamentally part
of the observation rules. it worries me that you do not have an easy checklist for all the
observation rules to check against."* This is that checklist — every rule governing the production
or recording of an `ib_observation`/`ib_node` row, at any stage, in one place, each citing where it
was actually decided. **Nothing new decided here.** Where a rule is still open, it's marked so, not
silently completed.

**How to use this:** before trusting any stage's output, or any recording-pass write, check it
against the rules for that stage below. When a new rule is decided anywhere in this project, it
belongs here too, in the same unit of work — this document goes stale the moment a decision is made
elsewhere and not added here.

---

## 0. Cross-cutting — applies to every stage, every write

1. **Single-writer principle.** Only the recording pass (#1693) ever writes `ib_observation`/
   `ib_node`. No other routine, including any future synergising intervention, writes the DB
   directly — everything else produces JSON output only. (#1691 §9 item 1)
2. **The LLM never assigns permanent ids, never checks for duplicates against the database, never
   decides edit-vs-new.** All three are the recording pass's job. (#1691 §4, #1693 §4)
3. **Run structure is fixed, three parts, always together:** (a) assemble input JSON → (b) run the
   stage's own sub-process → (c) recording pass writes it. Step (c) fires immediately after (b) in
   the same unit of work — never a deferred batch pickup. (#1693 §0)
4. **`iba.db` only.** No stage, no step of the recording pass, ever reads or writes
   `bible_research.db`. (DB fork, #737/#1682/#1690–1693, 2026-09-13)
5. **Verse references are resolved fresh at write time, never trusted from LLM-authored text.**
   `ib_node.verse_reference` is looked up against `iba.db.verse.reference` (matched via strong +
   occurrence) by the recording pass — closes a real, demonstrated risk (3 of 4 spot-checked
   free-text citations in an earlier draft used a non-canonical form). (#1682 §5, #1692 §3)
5a. **★ Flags raised during discovery are never resolved inline — they're carried to a later
   analytic run, expected to be the synergy stage.** Researcher, verbatim, 2026-09-16: *"these
   flags are raised, but not resolved during the analytic process. the follow-up will be included
   in a subsequent analytic run (probably as part of synergising)."* This is a cross-cutting
   discipline, not a process-(d)-only rule — it governs every flag-shaped observation this pipeline
   raises: `needs_adjacent_verse_context` (§3 item 4), `cross_family_or_cluster_flags` (§3 item 5),
   and pointer observations at the reading stage (§2 item 15) are all the same kind of thing —
   raised at the point of discovery, deliberately not chased down in the same run, queued for
   whichever later pass has the right scope to resolve them. **Confirms the general shape of
   process (e)'s own still-undefined input** (#1691 §9 item 5, #1695) — its input is expected to be
   exactly this accumulated set of flags/pointers from reading and answer, not a fresh data pull.
   **Not yet fully final** ("probably," researcher's own word) — the exact mechanics of a
   synergising run consuming these flags are still #1695's own design work, not decided here.
6. **"Genuinely couldn't resolve" is recorded explicitly, never guessed.** Carried forward from
   the old `verse_lexical_note.resolution_status`/`unresolved-not-guessed` principle — **RESOLVED,
   2026-09-16: this is a design principle for every `ib_observation`-writing stage, not a column to
   port over.** Surfaces as a `tag` value at whichever stage a genuine can't-resolve case arises
   (matching how `data-error`/`no-human-context` already work), not yet named. **Open: the exact
   tag value(s) still need choosing** — not decided here, a real item for #1711/#1691's `tag`
   taxonomy work.
7. **`ib_node` coverage is checked twice, never trusted once.** Every strong and every verse in a
   subgroup's membership must be grounded by ≥1 `ib_node` row — checked by the LLM at generation
   time (self-check, part of the stage's own process spec) AND independently re-checked by the
   recording pass at load time. A gap is a load-time finding, not silently accepted. (#1692 §2/§3)
8. **Everything can relate to anything, but only on evidence.** *"the relation must be evidence
   based, supported by observations, and must be meaningful"* — the guiding charter for `ib_node`
   as the study's actual relational substrate, not a bookkeeping table. (#1692 banner, researcher
   verbatim)

## 1. Process (b) — subgroup formation

1. **Full-cluster read before any assignment** — every `gloss`/`surface` value for every strong in
   the cluster is read first, not a streaming per-strong process. (#1690 §2a)
2. **Subgroups are meaning-based, not surface-similar.** (#1690 §2b)
3. **Maximum 10 real subgroups per cluster — `FLAG` excluded from the cap.** (#1690 §2c)
4. **`label` must name what the subgroup actually IS, not enumerate its members' glosses.**
   (#1690 §2d)
5. **A singleton subgroup is a valid outcome**, not a sign of mis-grouping. (#1690 §2e)
6. **`FLAG` conditions, precise:** a strong goes to `FLAG` when it (i) has no inner-being
   implication, (ii) belongs to another cluster, or (iii) has some other assignment-blocking
   anomaly — always with the reason in `placement_note`. (#1690 §2f, §3 item 3)
7. **`placement_note` is not `FLAG`-only** — any observation arising from an assignment is
   captured there, required for `FLAG`, optional-but-available otherwise. (#1690 §2g)
8. **A `placement_note` carrying a genuine observation (not just a bookkeeping reason) is
   promoted into its own `ib_observation`/`ib_node` row**, `stage='subgroup'` — the recording
   pass's job, not left sitting in `cluster_subgroup_strong`. Mechanism for telling "just a reason"
   from "also an observation" apart is **still undesigned** — a real open item. (#1691 §9 items
   8/10, #1693 §2)
9. **Every strong lands in exactly one subgroup** — structurally enforced by
   `cluster_subgroup_strong`'s `UNIQUE(strong)`. (#1690 §4 item 2)
10. **`FLAG` members are excluded from every downstream reading-stage input** for that subgroup.
    (#1690 §3 item 3)
11. **Hard precondition:** process (b) does not run unless `cluster.status=
    'ready_for_subgroup_allocation'`. (#1697 §3 item 2, #1693 §0)

## 2. Process (c) — reading

1. **Always run per family/subgroup — never the whole cluster in one pass.** (#1682 §2)
2. **Read all three meaning sources in full, every time** — never dump raw text unread, never
   skip a source. (#1682 §2)
3. **Scan every verse occurrence — no sampling**, regardless of strong or family size. (#1682 §2)
4. **Similar verses may be grouped, but grouping never excuses skipping an instance** — every
   occurrence still accounted for individually in the trace. (#1682 §2/§3)
5. **Every instance states what it is** — a positive reading, not only a contrast with others.
   (#1682 §2)
6. **Not a single distilled meaning** — show what a verse's meaning could be or likely is,
   including alternative candidate readings where the data supports more than one. (#1682 §2)
7. **A difference or specific inference is its own, separate observation** — never folded silently
   into the main per-instance reading. (#1682 §2)
8. **`span.surface` vs. `stepGloss` divergence is itself a subject of observation**
   (`surface-gloss-divergence`), explored (what the divergence suggests), not merely noted. (#1682 §2)
9. **`span.morph` is actively read, not merely carried** — stem/voice variation across occurrences
   is checked for meaning-relevance; where a family shows no morph-driven distinction, that absence
   itself gets a one-line note (`morph-reviewed, no distinction found`), not silence. (#1682 §2)
10. **Per-strong traceability is verified before that strong's reading counts as done** — every
    occurrence from the input JSON cited in ≥1 observation's `traces.occurrences`, recorded as a
    computed `strong_checks` entry, not eyeballed. (#1682 §2/§3)
11. **A homonym/name with no meaningful context is earmarked and left there** — no forced analysis.
    (#1682 §2)
12. **Cross-family observations, anomalies, and cluster-pointers are their own, separate synergy
    pass** — never threaded informally through the per-family reading. (#1682 §2)
13. **Data-quality issues found while reading are flagged separately** (`tag: data-error`), never
    chased down as part of this process. (#1682 §2/§4)
14. **★ The role-driven walk is structurally forced, not advisory** (#1704 §5 decision 1,
    confirmed) — an explicit per-role checklist the LLM must work through and account for before
    synthesis, not prompt wording it can skim past. **Not yet written into #1682's process spec as
    a structural requirement** — the sequence itself (below) is confirmed, encoding it as a hard
    gate is the remaining work.
    - (a) recognise the word's role
    - (b)(i) primary M-cluster → set as the focal point; everything else read in relation to it
    - (b)(ii) other M-codes present → a *relational* observation (how the two interact) AND a
      separate *pointer* observation (where the other cluster's own reading lives) — two distinct
      kinds, never one freeform flag (#1704 §2/§5 decision 2)
    - (b)(iii) sweep every party-kind-tagged word systematically, then ask each its own question
      set (source/target/impact/purpose/related words)
    - (b)(iv) walk T3 operation words against every nearby party-kind AND referent-identity
      (T10–T14) word
    - (b)(v) faculty reflection **last**, once, at the end of the subgroup's read — not a
      per-strong tag (#1704 §5 decision 4)
15. **★ Pointer observations are always separate from relational, and always present as their own
    kind** — out-of-scope-referencing, raised at the point of discovery, resolved later, never
    inline (same cross-cutting discipline as §0 rule 5a — this is one instance of it, not a
    separate mechanism). (#1704 §5 decision 2) **Not yet a named `tag` value** — real open item,
    #1691's `tag` taxonomy.
16. **Real, exercised `tag` taxonomy today** (8 values, frequency from the M10 prototype, 394
    observations): `instance-meaning` (145), `verse-grouping` (110), `difference-inference` (39),
    `surface-gloss-divergence` (32), `no-human-context` (23), `cross-family` (20), `data-error`
    (17), `alternative-meaning` (8). Extensible — new values added to `cfg_enum` as real data
    analysis surfaces them, not a closed list. (#1691 §5, §9 item 2)
17. **Re-read input includes existing rows.** If this is a re-read of a family already in the
    database, the input must include that family's existing `ib_observation` rows at
    `stage='reading'`, so the LLM sees prior findings rather than starting blind. (#1691 §3(a))
18. **Hard precondition:** the target `cluster_subgroup.status` must be `ready_for_reading`.
    (#1690 §3a, #1691 §2)

## 3. Process (d) — answer

1. **Always run per family/subgroup, same discipline as reading.** (#1682 §4A)
2. **Multiple slants, not one distilled answer** — where a family's evidence genuinely points to
   different answers to the same question, every distinct slant is its own entry with its own
   evidence trail. A single slant is correct only when the evidence actually is uniform, not a
   default. (#1682 §4A)
3. **Scope level governs the evidence trail:** `Word/term (lexical)`/`Verse-context` questions cite
   exact verses/spans; `Characteristic`/`The HIB`/etc. questions cite which strong(s)/
   observation(s) the synthesis draws on. (#1682 §4A)
4. **Adjacent-verse-context needs are flagged, not fetched mid-run** — `needs_adjacent_verse_context`
   with the verse and why. **RESOLVED 2026-09-16: this is the confirmed replacement for
   passage-as-a-reading-unit**, which is dropped entirely (researcher, verbatim: *"passage was
   dropped as a method and replaced by a observation rule to raise a requirement to read
   additional verses if needed. passages are no longer presented as a unit of reading"*) —
   independently confirmed at #1703 v2 (the old `passage`/`verse_passage` structure withdrawn as a
   candidate resolution mechanism, built for sequential book-reading not subgroup-based reading).
   **Resolution mechanism, RESOLVED IN DIRECTION 2026-09-16** (§0 rule 5a): follow-up happens in a
   later analytic run, expected to be the synergy stage — not fetched inline, not a permanent
   unresolved caveat. **Still genuinely open:** the real flag rate at scale, untested (#1703).
   **Not yet a named `tag` value** — confirmed direction only (#1691 §5), same open item as item 15
   above.
5. **Cross-family/cluster relevance is flagged, not resolved inline** —
   `cross_family_or_cluster_flags`, left for a later, dedicated cross-family round — the same
   cross-cutting discipline as item 4 and §0 rule 5a, expected to be the synergy stage. (#1682 §4A)
6. **Hard precondition:** the target `cluster_subgroup.status` must be `ready_for_answer`.
   (#1690 §3a, #1691 §2)
7. **`tag` taxonomy — direction confirmed, values not yet chosen.** Should express "this answer
   raises something needing follow-up," folded flat into `tag` (matching `data-error`'s pattern),
   not kept as separate JSON arrays. (#1691 §5)

## 4. Process (e) — synthesis (synergy)

1. **Cross-cluster, not just cross-family** — `cluster_code` is `NULL` for this stage; the actual
   cluster(s) touched are recorded via `ib_node` rows, one per cluster, not on the parent row.
   (#1691 §9 item 9)
2. **Append-only, never edited in place.** A later revisit that changes a synthesis claim files a
   NEW row with `supersedes` pointing at the old one's id — the old row stays, `status` changes to
   `superseded`, never deleted or overwritten. This is the one place the project's usual "edit the
   spec in place" convention does not apply to the *data*. (#1682 §4B)
3. **Every synthesis claim traces back to the tier-2 items it was read off** (`grounded_in`) — so
   it can always be walked back down to the evidence, not left as a bare assertion. (#1682 §4B)
4. **`revisit_note` is required** — what would confirm, complicate, or overturn this once more
   material is read. An explicit invitation to revisit, not a closed verdict. (#1682 §4B, #1691)
5. **Still genuinely open, not designed — but the shape is now confirmed in direction (§0 rule
   5a, 2026-09-16):** the stage's own input JSON (#1691 §9 item 5, #1695) is expected to be the
   accumulated `needs_adjacent_verse_context`/`cross_family_or_cluster_flags`/pointer observations
   raised during reading and answer, not a fresh data pull — "probably," not yet final. The
   multi-cluster gating precondition (#1698) is still fully open. Both deliberately deferred until
   build+test through the answer stage is complete. Not a gap to fill now.

## 5. `cluster.status` / `cluster_subgroup.status` — the lifecycle gates every stage above checks

1. **Two levels, not one** — `cluster_subgroup.status` is the real per-run precondition for
   reading/answer (checked per-subgroup); `cluster.status` is a rollup, recomputed on every
   subgroup change, not an independent gate for those two stages. Process (b) and synthesis are
   the exceptions — genuinely cluster-grain, checked directly. (#1690 §3a, #1697 §3, #1693 §0)
2. **`strongs_reassigned` is manual-only, and must raise a real, visible escalation** the moment it
   fires — not a passive column value. No automatic resubmission of process (b). (#1697 §3 item 4,
   researcher verbatim: *"I want to control that process, for at least a few rounds"*)
3. **`FLAG` never enters this lifecycle** — no status, permanently excluded from every rollup and
   gate. (#1690 §3a)

## Still-open items this checklist surfaces (not resolved here)

- The `placement_note`-promotion mechanism (§1 item 8) — undesigned.
- The pointer/adjacent-context/unresolved-not-guessed `tag` values (§0 item 6, §2 item 15, §3 item
  4) — direction confirmed for each, exact names not chosen.
- The adjacent-verse-context flag's resolution mechanism and real rate (§3 item 4) — untested.
- Synthesis's own input JSON and multi-cluster gating (§4 item 5) — deliberately deferred.

This list is exactly #1711/#1691's remaining `tag`-taxonomy and process-spec work — cross-referenced
here so it's checkable in one place, not re-derived from this checklist itself.
