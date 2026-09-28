# M47 → cluster phenomena — handoff (v13)

**Date:** 2026-09-28 · **Supersedes:** v12 (`archive/`). The v12 history (v1–v12 change notes, batch list, rulings, inputs) is still valid background and is not repeated here. Read `archive/M47-handoff-batches-C-to-H-v12-20260928.md` only if you need it.
**Session log:** `Logs/SESSION-LOG-20260928-m47-filing-noseat-pilot-m20-phenomena.md`.
**Live tracking:** escalation **#1885** (in progress, assigned to Claude).

## NEXT STEP — complete M20 (researcher, 2026-09-28, verbatim)

> "I will approve 1885 on completion of M20 not before it. in terms of 6.3 - continue to map the seat-sense as part of the cluster analysis, with reference to the work already done in M47 - so don't redo it."

**What "complete M20" needs:**

1. **Start from M20 v2:** `../M20 - doubt-discouragement/wa-cluster-M20-phenomena-v2-20260928.md`, with its ledger `…-phenomena-ledger-v1-….csv` (every one of the 275 verses assigned to a phenomenon).
2. **Add the seat-sense mapping to each phenomenon (§1–§16),** as part of the phenomenon analysis, not as a separate exercise. For each phenomenon, record:
   - **Where a seat word sits in its verses, and whose seat it is:** the bearer's own; the other party's (e.g. God hides his face, and the human spirit fails); the offender's (Isa 57:17); or none.
   - **Whether each seat link is a genuine inner-being sense or spurious.** Examples of spurious links: Gen 3:8 "cool" is *ruach* as wind; Exo 16:8 "meat"; Rev 2:17 "Spirit" is God speaking; 2Ch 22:9 "heart" belongs to another person. This is the **seat-sense check**. The researcher ruled that it continues, as part of the analysis.
   - **Where the seat arrives in the next verse or the passage, not in the verse** (e.g. Psa 13:1 → 13:2; Deu 1:27 → 1:28; Phili 4:6 → 4:7; Mat 6:25 heading its whole discourse).
3. **Do not redo the M47 reading. Cite it.** The M47 work already read M20's 30 seated verses:
   - **Batch A v3 §6** (`M47-x-feeling-batchA-v3-20260928.md`, "Doubt & Discouragement (M20)"): anxiety in the heart; anxiety about *psychē* and body; divided interests; double-mindedness; doubt in the heart; disheartened by others; God searching the anxious heart; the heart concealing or not; and ◆ God's hidden face paired with the human spirit or breath failing.
   - **Batch A v3 R6:** the "to hide" words in M20 (the tag question), kept as a record.
   - **The no-seat pilot, M20 v1** (`../M20 - doubt-discouragement/wa-cluster-M20-noseat-observations-v1-20260928.md` §0, §2): the sense-matched implicit seats per Strong's, and the spurious links.
   - **The seated pairs themselves:** `cluster-M47-other-m-code-pairs-with-distance-v2-20260928.csv` (this folder, UTF-8 with BOM), filtered to `other_cluster_code = M20`. That is 30 verses.

   Map each seated verse to its phenomenon (the ledger has a `seat_word_in_verse` column) and **cite** the Batch A §6 bullet, or the v1 section, that already read it. Add new reading only where the phenomenon view shows something the batch did not.
4. **Then:** version-bump M20 to **v3**, archive v2, update the ledger if any assignment changes, commit and push, and set #1885 **ready_for_approval → Researcher**. **M02 does not start until #1885 is approved.**

## Rules for the reading (all carried forward)

- **Phenomenon level, emergent.** Phenomena come from the verses, never from a preset list or a tick-box. Answer the five questions per phenomenon: what it is, what it does, where it comes from, how it co-exists, what it leads to. Every claim is anchored to a verse. Quote a context verse only after reading it. Account for every verse. **Do not brush over detail or make general statements.** (Memory: `feedback_phenomenon_level_emergent_reading`.)
- **Do not use the 12-method table** (`wa-cluster-M47-ib-operation-modes-consideration-v1-20260928.md`) as a checklist.
- **Inner-being definition:** from config: `cfg_prose_concept.inner_being_definition` → prose section 5 ("Defining Inner Being"). The subject is the human inner being (prose sections 1089/1090; `cfg_method_rule` `hib.set`). Where God is the actor, analyse the human side. `phenomenon.set` hidden-behind-act applies.
- **Revisit as the rule; interaction first** (memories `feedback_revisit_as_rule`, `feedback_interaction_over_reallocation`).
- **Filing:** `_analytics/Clusters/{code} - {short name}/`, per `cfg_setting report.cluster_folder_naming_convention` (GOVERNANCE.md §83). Prior versions go in `archive/`. Same base name means a version bump.
- **Data:** read directly from `iba/app/db/iba.db` (read-only): `verse_lexical.role` (a JSON list of cluster codes; a seat is a token whose role has `"M47"`), `verse` (`reference`, `text`), `strong`, `cluster`, `cfg_book_order`. bible_research.db plays no part.
- **Scratch scripts** (recreate in the session scratchpad, `temp_` prefix, not registered): an extract of all verses for a cluster with its words and seat words in canonical order, and a context reader (reference ± n verses from `verse`, canonical order via `cfg_book_order`).
- **Cost:** work in units, with a review between them.

## After M20 is approved

- **M02 Anger & Wrath** (681 verses), proposed in **two units** with a review between them:
  1. human anger's phenomena
  2. divine anger as borne by the human

  Reuse the M02 pilot (`../M02 - anger-wrath/wa-cluster-M02-noseat-observations-v1-20260928.md`) and the seated M02 verses as read in the M47 batches.
- **Pointers for later revisits:** Job 3:10, 3:16, 14:13 and Jon 4 → Batch G v3 §16 (the death side); 1Ki 21:5 and 1Sa 1:15 → Batch F v4.

## Other open items (not blocking)

- The loose pre-rule files at the `_analytics/Clusters` root have not been moved into cluster folders.
- #1881 (session.close stale transcript) is still open. This session's close read the correct transcript.
