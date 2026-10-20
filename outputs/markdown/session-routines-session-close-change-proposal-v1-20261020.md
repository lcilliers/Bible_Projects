# session-close: change proposal

> v1, 2026-10-20, escalation #2173. Researcher (verbatim): *"proceed with the session-close
> design"*. Builds on:
> - the description, `session-routines-start-close-description-v1-20261020.md` (§3 steps; §4
>   findings C1–C7);
> - the start-project proposal, `session-routines-start-project-change-proposal-v1-20261020.md`.
>   Its parts that land in session-close are taken over here: P0 (no meaningless output), P2 D
>   (rule evidence), P3 (spine), P4 (analysis integrity), Q3 (session log) and G2 (commit rule).
>
> **Status: proposal. Nothing is built.** It is edited in place while under review.

---

## 1. What session-close is for

To end a session so that **nothing done, decided or left open in it exists only in the chat or in
an unrecorded file**, and so that the base data and the narrative are sound. Every check below:

- names its findings: what, where, why;
- is silent when it passes (P0);
- persists one close report, so the close no longer exists only in chat (fixes C7).

**A finding blocks the commit** until it is fixed, or named in the close report with the open item
(`OT-nn.n` or `#nnnn`) that carries it.

## 2. Two more findings while designing (added to the contradiction list)

| # | Finding | Fix |
|---|---|---|
| G13 | **The register check's 46 findings are reported as a count.** Every close since 2026-10-18 carried "check 46 unchanged". All 46 are current claims that no passage tells (I-2 … 10-7, in `outputs/narrative-register/narrative-register-check-v31-20261019.md`). Rule 77 as amended (#2152) says the concept's untold claims are linked, restated or withdrawn **when a chapter on that concept is touched**. A count cannot show whether that happened. | SC5 below: standing findings are carried as items, and each close checks the ones that bear on the chapters it touched. |
| G14 | **The quote check is not part of the app.** Four copies sit in cluster folders (M01, M25, M08 ×2), against `governance.scripts_and_routines`. Its use at close depended on memory. | Move one version into the app as a narrative step (`narrative.quote_check`), run by SC5 on every chapter changed. |

## 3. The new session-close, step by step

| # | Step | Kind | What it does | Fixes |
|---|---|---|---|---|
| SC1 | **Session and window** | code | Identifies the session and its start (boundary record) and the git window, as now. **A missing session id or boundary record fails the close** instead of passing with a note. | C4 |
| SC2 | **Spine** | code | `spine.check` extended (start-project proposal P3): span → strong; verse ↔ span (verse gap by design excepted); **meaning**: local gaps in `strong_sense`, `strong_meaning_tree`, `strong_lexicon` asked of STEP for those codes only. Content in STEP that a table lacks is FATAL, by code and table. FATAL findings come first in the report. | S1, G6–G8 |
| SC3 | **Researcher's words → records** | code + Claude | Code lists every researcher message in the session transcript. For each, it looks for the message text (normalised) in an `escalation_history` comment written in the window. Claude gives each unmatched message one disposition, which goes into the close report: *recorded in #n vN* (then written), or *needs no record* with the reason (for example "start-project", a command name). **A message that carries a decision, instruction or correction with no record is a finding.** This replaces today's check, which compared the CLI's own output with the DB (records with records). | C1 |
| SC4 | **Open items → register** | code + Claude | (a) Code: every *Open items* line in a file changed in the window names an `OT-nn.n` or `#nnnn` that exists and is open (P4.3). (b) Claude re-reads the session for what was held, referred, deferred or left to be clarified, by the researcher or by Claude ("hold", "later", "check", "follow-up", "not done here"). Each must be in the register by id. If it is not, it is raised the same turn (rule 21). | P4.3–4 |
| SC5 | **Analysis integrity** | code | Over the files changed in the window: (a) every chapter changed has a `narrative_update` recorded in the window; (b) `narrative.quote_check` (G14) on each changed chapter, against its previous version: any failing quotation is a finding; (c) the register check: a **new** finding (one not in the previous close's list) is a finding. Each **standing** finding that concerns a concept in a chapter changed this session must be reconciled (rule 77, #2152), and is a finding until it is; (d) every verse named in a reading changed in the window has its placement (told / claim / data / forward OT-nn.n / held #nnnn / context), and a "told" verse is told (P4.2, Q2). | P4, G13, G14 |
| SC6 | **Rule compliance return** | code + Claude | Reads the session's compliance file (start-project P2 B). Each rule marked *engaged* needs its evidence (file, escalation id/version, commit, command output). Code checks the evidence that can be checked. An engaged rule without evidence is a finding, by rule id. | P2 D |
| SC7 | **Remediation** | Claude | Fixes the findings of SC1–SC6: writes the missing escalation entries (with the researcher's words verbatim, the debate, the decisions, what was skipped), the register records, the reconciliations and the placements. Anything not fixed now is named with the item that carries it. | — |
| SC8 | **Session log** | Claude, checked by code | Claude writes `{governance.session_log_dir}SESSION-LOG-{date}-{topic}.md` with the six required contents. **Item 4 (decisions) names, for each decision, where it was recorded**: a doc file, a `cfg_*` change, or an escalation id/version. | Q3, G2–G4 |
| SC9 | **Decisions reached their targets** | code | For each decision in the log, the named target changed in the window: the file is in the git diff, a `cfg_change_detail` row was applied in the window, or the escalation version exists. A decision without a target, or with a target that did not change, is a finding. This makes today's governance drift item a check. | C2 |
| SC10 | **BUILD.md coverage** | code | Every code or config file changed in the window (`iba/app/**` `.py`/`.ps1`, `iba/config/**`, `.claude/hooks/**`, `.claude/commands/**`) must be **named** in a BUILD.md section added or changed in the window. Any BUILD.md edit no longer clears all gaps. | C3 |
| SC11 | **Re-run** | code | SC1–SC6, SC9 and SC10 run again over the result. The log's presence and its six sections are checked. | — |
| SC12 | **Publish what changed** | code | The narrative copy runs **only if a chapter changed**, and the threads register export **only if a thread row changed** in the window. Each reports only what it copied or wrote (P0). | P0 |
| SC13 | **Commit and push** | git | Blocked while any finding is neither fixed nor carried by a named item. Stages all outstanding changes (CLAUDE.md §12). Then **item 6 of the log** (branch, commit hash, push output) is written into the log and committed as a second small commit. | G2 |
| SC14 | **Close report and chat** | code + Claude | The close report (`session_close.report_path`, versioned) holds every finding with its disposition, and the commit hashes. Chat shows only: findings not fixed (with their carrying items), and the commit and push confirmation. | C7, P0 |

## 4. What is removed or changed from today's routine

- Today's (a) check (CLI output against `escalation_history`) is **replaced** by SC3.
- Today's (b) list of three changed docs is **replaced** by SC8/SC9.
- Today's (c) BUILD.md check is **replaced** by SC10.
- Narrative copy and threads export at every close: **only on change** (SC12).
- "Re-confirm clean" passing when the git window was skipped: **removed** (SC1 fails instead).
- The step-8 chat summary as the only record of the close: **replaced** by the close report (SC14).

## 5. Config and rules this needs

- `cfg_step` rows for the session-close steps above, and for `narrative.quote_check`. The
  `session.close` `does` text is rewritten to match.
- `governance.session_log_triggers_commit` reworded (G2): the close includes the log, and the
  commit follows it. `governance.session_log_required_content` refers to `session_log_dir` (G4).
  Item 4 gains "with where each decision was recorded".
- A behaviour rule for the per-verse placement in reading files (Q2). A behaviour rule for
  open-items lines carrying a handle (SC4a).
- A setting for the researcher-message match, recording which session-start command names need no
  record.
- `cfg_on_fail` for the new findings: block the commit unless the finding is carried.

## 6. Decided: the session log's own commit hash

**SC13, item 6 of the session log.** The log must record the commit hash and push output of the
commit its own completion triggers. A log cannot contain the hash of the commit that contains it.

**Decided 2026-10-20.** Researcher (verbatim): *"use a second commit for the session log hash"*.
The log is committed with everything else. Item 6 is then written into the log and committed
alone ("session log git confirmation"), and pushed.

## 7. Test plan (per step, in the build session)

Each step gets a synthetic bad case, run against live data, with its output read back:

- SC1: a session with no boundary record.
- SC2: a span with no verse; a strong with an empty `strong_sense.head` where STEP has text.
- SC3: a researcher instruction with no history row.
- SC4: an open-items line with no handle; a handle to a closed item.
- SC5: a chapter changed with no update; a misquoted verse; a new register finding; a standing
  finding on a touched chapter; a reading verse with no placement.
- SC6: an engaged rule with no evidence.
- SC8/SC9: a decision whose target did not change.
- SC10: a hook changed with no BUILD.md mention.
- SC12: no change → nothing copied, no output.
- SC13: a finding not carried → the commit is refused.

## 8. Build order (with start-project, one Developer Mode build)

1. Config: state groups (G1); rule rewording (G2–G4, G6–G9); new rules and steps.
2. Start-project: P0, P2 A–C, P1, P5, S6.
3. Session-close: SC1, SC2 (spine), SC3, SC4, SC5 (with the quote check moved into the app), SC6,
   SC8–SC10, SC12–SC14.
4. Both command files rewritten from the code. BUILD.md, GOVERNANCE.md, USER-GUIDE.md and the PS
   worksheets in the same unit of work.
5. A full start and close run as the acceptance test, its reports read back. Then #2173 goes for
   approval.
