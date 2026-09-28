# SESSION LOG — 2026-09-28 — M47 delta revisit (the death side of Life & Death)

**Session:** Claude Code desktop, session `d58630a0-c5c8-48aa-875b-58af0272414a` (working directory `G:\My Drive\Bible_study_projects`; files written to `C:\Bible_study_projects`). This is a new chat that started from handoff v8.
**Entry point for the next session:** `outputs/markdown/M47-handoff-batches-C-to-H-v10-20260928.md`.

---

## 1. What was done

| # | Work | Output | Commit |
|---|---|---|---|
| 1 | **Delta revisit (handoff v8 item 1).** All 155 new pairs in 115 verses were read (154 M25 death-side pairs plus 1 M50 pair). Context was read for about 45 passages (ESV from `iba.db`; Psa 116:9 from the STEP server). | Batch G **v3** (new §16; revisits in §0.2, §3.6, §4, §5.4, §6, §14.11–14) | `f37bc3ff` |
| 2 | **Consequential revisits.** Batch F → **v4** (§3.4, §4 ◆, §7 point 7). Batches A, C, D, E and H were checked: **no change**, with pointers in G §16 (see G §R-V). | Batch F v4 | `f37bc3ff` |
| 3 | Handoff v8 → **v9** (item 1 done) | handoff v9 | `f37bc3ff` |
| 4 | Session close; handoff **v10** with the researcher's new next step | this log; handoff v10; `iba/app/reports/session-close-v12-20260928.md` | (this commit) |

**DB writes:** none. The scratchpad scripts `dump.py` and `ctx.py` were recreated. They were not kept in the repo, following the handoff §5 convention.

## 2. Researcher direction given this session (verbatim)

1. "proceed to update this batch v8" — read as: carry out the next item of handoff v8 (the delta revisit).
2. "close the session. the next step in a new chat is to explore the verses in each cluster that is not related to M47. The key question to explore is : are there inner being related operations that takes place without a explicit, or implicit through cross - correlation, context that is related to the inner being."

## 3. Decisions made

- **Delta revisit:** the reading went into a new **§16** of Batch G, numbered 16 so that existing references to §14 and §15 stay valid. It did not rewrite §1–§13.
- **Revisits:** Batch F was bumped to v4, because the reading changes F §3.4 and §7. The other batches were left unchanged, because their verses and readings stand.
- **Next step (researcher, item 2 above):** explore, cluster by cluster, the verses **not related to M47**. The key question is **whether inner-being operations occur with no explicit, and no implicit (cross-correlated), inner-being context**. This builds on the seat-coverage plan (`research/investigations/M47-seat-coverage-and-unseated-verses-v1-20260928.md`). Its §6 decisions are still open; see handoff v10 §4.

## 4. Main findings (detail in Batch G v3 §16)

- **The heart dies before the body.** Nabal: heart dead → the Lord strikes him ten days later.
- **Each component has its own verb at death.** The soul "departs"; the heart "does not attend"; the spirit is "not retained" or "gathered back".
- **The death-wish belongs to the soul and is seldom granted.** It is answered with food (Elijah, Exo 16), a question (Jonah) or a sign to look at (Num 21).
- **The heart decides which killing is murder** (cities of refuge). Ransom is refused only for a murderer's life (Num 35:31).
- ***nephesh* = corpse.** A dead *nephesh* is kept away from what is consecrated.
- **Life risked "to death"** has an OT precedent (Judg 5:18; Jos 2:14).

## 5. Session-close check

`Session-Close.ps1` reported 0 gaps, but it again read a **stale transcript** (session `753f0db2…`, the known #1881 defect).
**Hand check of this session:**
- no escalations touched
- no `iba/app/**` code changed, so no BUILD.md entry is needed
- no GOVERNANCE.md, CLAUDE.md or USER-GUIDE.md change was decided

The session is clean.

## 5b. After the first close (same chat) — file organisation, travel, website

**Researcher direction (verbatim):**
1. "part of my problem is that the files for the study is actually all over the place. it there is a great danger between me and AI that the wrong files are being used, and files are not adequately organised."
2. "yes, start step 1; c:\bible_study_projects is the authorative source for the current project. G:/Claude_research i guess is a working folder for Claude access while working on other platforms. Any documents on this drive that is in authorative or Zotero should be moved to a archive folder where the can be deleted; g:/bible_study_projects is and old copy and can move entirely to a archive folder. I am planning to travel for 6 weeks in December … I am also thinking to start a website …"
3. "yes, draft the planning note for website and travel. In particular, what would the best solution be for access to the DB. (iba.db)"
4. "i will do it myself. for now, the important thing is that your defaults are set the the authorative source and all others are ignored."

**Done:**
- **Zotero access checked.** The web API is reachable read-only (777 items, 20 collections). The local connector on port 23119 is off.
- **Spirit_Soul_Body study located:** 4 copies across Zotero storage and `G:\My Drive\Claude_Research`.
- **Discovery script written:** `scripts/_discover_file_locations_v1_20260928.py` (read-only). The run was **stopped**; it was too slow over about 29 GB, including the .bak copies of the database and Google Drive files that have to be downloaded. **The researcher will run the scan locally.** The register is not yet produced.
- **Planning note:** `research/investigations/travel-access-and-website-plan-v1-20260928.md` (DRAFT for mark-up).
  - The database recommendation is **remote access to the home desktop** (Tailscale plus remote desktop), tested in November, with a zipped read-only snapshot as fallback. Checking the database out to a laptop is the fallback option.
  - A database in a sync folder is ruled out (the June incident).
  - The website would be a separate public GitHub Pages repository, filled only by a publish step. **The ESV quotation limits are to be checked** before anything is published.
- **Authoritative-source default set:**
  - a rule at the top of `C:\Bible_study_projects\CLAUDE.md`
  - a RETIRED banner at the top of `G:\My Drive\Bible_study_projects\CLAUDE.md` (not in git)
  - memory note `feedback_authoritative_source_only`, in both memory folders (G: and C:). The M47 memories were also copied to the C: memory folder.

**Decisions:** as in direction item 2. The moves (archiving the G: project copy in full, and the duplicates in `Claude_Research`) wait for the inventory register.

**Governance:** the CLAUDE.md change is the recorded outcome of the researcher's decision. No escalation was touched, and no `iba/app` code changed.

## 5a. Skipped / deferred
- **The file-location inventory register and the moves.** These wait for the researcher's local scan output.
- **Travel and website decisions.** These wait for mark-up of the planning note.
- **Future sessions should be opened in `C:\Bible_study_projects`.**

- The seat-coverage §6 decisions were not taken this session. They carry to the next chat.
- The stale co-occurrence CSV and the #1880 side items (M67 readiness, E-R6) remain open, as in handoff v8.
