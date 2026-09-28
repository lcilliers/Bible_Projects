# M47 — decisions before the no-seat work starts (v1)

**Date:** 2026-09-28 · **Author:** Claude Code · **Status:** A is settled by the researcher's instruction of 2026-09-28 (see the rulings under A2–A4). B, C and D await researcher mark-up. Nothing has been run or written to the DB.
**Picks up from:** `M47-handoff-batches-C-to-H-v12-20260928.md` (NEXT STEP; v10 archived) and `M47-seat-coverage-and-unseated-verses-v1-20260928.md` (both in this folder) (§5 method, §6 decisions).
**Researcher's key question (verbatim):** "are there inner being related operations that takes place without a explicit, or implicit through cross - correlation, context that is related to the inner being."

**How to answer:** under each item, write your ruling after **Ruling:**. My recommendation is given first each time.

---

## A. Filing correction (researcher, 2026-09-28)

> "filing should be to _analytics\clusters with each cluster having its own sub folder."

**Findings:**
- `_analytics/Clusters/Cluster_README.md` already says "All output relating to a cluster is saved in its folder here", with names `wa-cluster-{CODE}-{kind}-v{n}-{YYYYMMDD}.{ext}`.
- **`docs/file-organisation-rules.md` §3.0 is stale.** It still points to `Sessions-v2/{CODE}-{Name}/`. That folder no longer exists, and the rules never mention `_analytics/Clusters`. This is why the M47 work drifted into `outputs/markdown/` and `research/investigations/`.
- There is only one cluster subfolder so far: `M47 - heart-soul-mind-spirit/`, which holds 1 CSV. Its name does not follow the `{CODE}-{Name}` form. The DB short name is "Inner Seat".
- `_analytics/Clusters/` also holds loose M10 files at its root, from before this rule.

**A1. Update the rules document.** Rewrite §3.0 of `docs/file-organisation-rules.md` to point at `_analytics/Clusters/{CODE}-{Name}/`, and bump its version.
**Recommend:** yes.
**Ruling:** *(open. The instruction below settles where files go. The rules document is not yet corrected, and neither is any `cfg_setting` that would record the rule. See the note to the researcher in chat.)*

**A2. Folder name form.** The options are to keep `M47 - heart-soul-mind-spirit`, or to rename it `M47-Inner-Seat`, which is `{CODE}-{DB short name}` as the README states.
**Recommend:** rename to `M47-Inner-Seat`, and create other cluster folders the same way as they are needed (e.g. `M02-Anger-Wrath`, `M20-Doubt-Discouragement`).
**Ruling:** Researcher, 2026-09-28 (verbatim): *"ensure that filing goes to the correct _analytics\clusters folder with a sub folder for each cluster. create the cluster of does not exist. Move the M47 files all to the folders."* Applied: the existing folder `M47 - heart-soul-mind-spirit` was first kept as it was, then renamed `M47 - inner-seat` with a folder created for every cluster (#1882 v2). Other clusters get `{CODE}-{DB short name}` folders when they are first needed. *(You can still ask for the M47 folder to be renamed to `M47-Inner-Seat`.)*

**A3. Move the existing M47 files into the folder.** Use `git mv`, so history is kept.
- 14 files from `outputs/markdown/`: the handoff v10, stocktake, depiction, co-occurrence assessment, spirit distinction + CSV, status overview, batches A–H.
- 9 files from `research/investigations/`: the seat-coverage plan, T-code question, re-allocation register, surface forms, pairs, delta, and the stale co-occurrence CSV.
- **Recommend:** move them, but **keep their current file names** and do not rename them to `wa-cluster-M47-…`. Every handoff and batch file cross-references the others by name, so renaming 23 files means rewriting those references, which costs a lot for little gain. New files from now on use `wa-cluster-M47-{kind}-v{n}-{date}`. Also update the paths in handoff v10 §1 and §3.
- The alternative is a full rename plus a reference rewrite.
**Ruling:** Done 2026-09-28 per the instruction under A2. 26 current files moved here and 27 prior versions into `archive/`, using `git mv` with names unchanged. Handoff v10 → v11 with paths corrected.

**A4. Where the no-seat pilot readings go.** They are per-cluster readings asked from the M47 angle.
**Recommend:**
- the tie-profile (all clusters, one table) → the M47 folder
- each pilot reading → **that cluster's own folder** (e.g. `M02-…/wa-cluster-M02-noseat-reading-v1-{date}.md`), with a one-line pointer in the M47 folder
**Ruling:** Follows from the instruction under A2: each cluster has its own subfolder, created when it is first needed. The tie-profile goes here; each pilot reading goes in its own cluster folder, with a pointer here.

**A5. The stray M10 files at the `_analytics/Clusters/` root.** This item is out of scope for today. **Recommend:** leave them, and log them as a separate filing item.
**Ruling:**

---

## B. Working definition: "inner-being operation" in a verse with no seat word (handoff v10, open item 2)

**Finding:** the programme already has a definition. `Workflow/methodology/wa-IB-verse-dimensions-definition-v2-20260629.md` §1 says the unit is **an IB operation, meaning an inner-being movement in the verse**. Its **D3 Seat / bearer** reads "a seat lemma in-verse; else the grammatical subject (bearer)". So the no-seat case is already provided for: the operation is carried by its **bearer**, not by a seat.

**Recommend:** adopt it, rather than invent a new one. For this exercise, a verse **has an inner-being operation** when:
1. a cluster word in the verse states a **movement of feeling, willing, knowing / perceiving, or relating** (D1 Identity), **and**
2. it is **predicated of, or attributed to, a bearer**: a person, a group, or God (D3 Bearer). The bearer may be the grammatical subject, a possessor ("his anger"), or an addressee ("do not fear").

It is **not** an inner-being operation when:
- the cluster word names an **outward act, office, thing or setting with no inner movement stated** (e.g. "king", "silver", "altar", "judgment" as a court verdict)
- it is used only **as a name, title or fixed formula** (e.g. "the fear of the LORD" as a title for piety is borderline: mark it ◆ and read it; do not exclude it)

**Record for each operation:** bearer class (**divine / human / collective / undetermined**), and what carries the state instead of a seat. That last may be the verb alone, a body word (class B), an action or gesture (weeping, trembling, tearing clothes), or narrative consequence. This is D3 + D9 + D7 of the existing schema, reused with no new dimensions.
**Ruling:**

---

## C. Seat-coverage plan §6 decisions (carried forward from the plan)

**C1. Approve Step 1**, the tie-profile script. It is read-only and runs on `iba.db` `verse_lexical`. It gives one CSV plus one per-cluster table, and no reading.
**Recommend:** yes. It is cheap, and the pilot depends on it.
**Ruling:**

**C2. The body-seat list for class B.**
- **Proposed:** `qereb` within / entrails (H7130G), bones, kidneys, bowels / *rachamim*-bowels, belly / womb, nostril / face-as-anger.
- **Recommend:** add **liver** (*kabed*, Lam 2:11) and ***splanchna*** (NT bowels, G4698).
- Keep **eye, ear, lips and tongue out of B**. They are organs of outward perception and speech, not seats. Record them separately as class **B′ (expressive organ)**, so they stay visible without inflating B.
**Ruling:**

**C3. The pilot clusters.**
**Recommend:** **M02 Anger & Wrath** (615 no-seat verses; divine-subject heavy; nostril vocabulary) and **M20 Doubt & Discouragement** (245; small enough to read in full), as suggested.
- M02 is too large to read in full. Read it **by tie class**: all class 0 verses, and a sample of N, B, P and X. The pilot report will state the sample sizes.
**Ruling:**

**C4. T-clusters (T14 Body, T7 Divine party, T8 Human party).** Should they become part of the M47 angle from now on, or serve only as tie classes in this exercise?
**Recommend:** tie classes only for now. Decide after the pilot shows whether they carry the inner being.
**Ruling:**

---

## D. How X (cross-correlation) is measured (handoff v10, open item 3)

**The options are:**
- **(i) per Strong's code:** its **seat rate**, i.e. the share of its corpus verses that contain a seat word
- **(ii) per verse context:** the same rate per contextual meaning group
- **(iii) both**

**Constraint found:** the cluster membership and `verse_lexical` live in `iba.db`. Verse-context groups live in the older `database/bible_research.db` model, which has not been mapped to `iba.db` verse ids for this purpose. Joining the two is extra build work, and this pilot does not need it.

**Recommend:**
- **(i) per Strong's code**, with a threshold of **seat rate ≥ 20%** (about twice the 10% baseline) and at least **10 verses**
- revisit (ii) only if the pilot shows that a code's sense splits sharply, i.e. seat-heavy in one sense and not in another

**Ruling:**

---

## E. What happens after the rulings

1. Apply the filing rulings (A). Commit.
2. Run Step 1 (the tie-profile). Report the per-cluster profile table in the M47 folder. Commit.
3. Pilot reading of M02 and M20 under definition B. Use the interaction-first format of Batches F–H, and read before/after context for key passages. Commit after each cluster.
4. Report the pilot, then you decide the scale-up (plan Step 3).

**Cost note:**
- Steps 1 and 2 are cheap: one script and a table.
- The M20 reading is moderate (245 verses).
- M02 is the expensive part, and its sample size under C3 is the main lever on cost.
