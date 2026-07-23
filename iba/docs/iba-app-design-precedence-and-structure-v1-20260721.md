# IBA Application Design — precedence, build-grounding, and structure (v1)

> **Status: FOR REVIEW/EDIT, not chat.** Prepared 2026-07-21, ahead of Step 1's full draft. Resolves
> the open questions raised against the five `scratchpad_tmp` snippets by (a) establishing which
> snippet is chronologically later where two disagree, and (b) checking the **actual built app**
> (`iba/app/BUILD.md`, `iba/app/GOVERNANCE.md`, and the live `iba/app/db/iba.db` schema, queried
> directly) rather than asking. Only what neither source answers is left open. Edit this file
> directly; nothing here needs a chat reply.

---

## 1. Precedence rule (so conflicts stop being questions)

Dated, in order — later wins where two disagree, unless a later item is explicitly framed as "not yet
decided":

| when | source | status |
|---|---|---|
| 2026-07-15 | snippet 1 (old plan body + Appendix A/B/C) | earliest design layer |
| 2026-07-15 (same day, later) | snippet 5 part 1 — *configurator file-layout v2* — explicitly rules on / supersedes Appendix A | supersedes snippet 1 where it rules |
| 2026-07-15 (same day) | snippet 5 part 2 — *configurator coverage v1* — audits snippet 1's Appendix A.9/C against the framework snippet 5 part 1 just ruled | audit of the above, not a new design |
| 2026-07-17 | `iba/app/BUILD.md`, `iba/app/GOVERNANCE.md` | **the first actual build** — ground truth for what exists, overrides any doc's assumption about what was built |
| 2026-07-19 → today | live `iba/app/db/iba.db` (34 tables, queried directly) | **current ground truth** — supersedes any doc's claim about current schema state |
| 2026-07-20 | snippet 2 (process-loop agenda + researcher comments) | supersedes snippet 1's segment framing for the *interpretive* layer |
| 2026-07-20, later | snippet 3 (operation ruleset) | resolves one open item snippet 2 left (the operation-type catalogue) |
| 2026-07-20, later still | snippet 4 (config rules) — cites snippet 3 as "done" and the plan's §14 | latest of the four 2026-07-20 documents; carries the D1–D6 rulings |
| 2026-07-21 | `iba-application-plan-v3-reconstructed.md` (the baseline) | **latest overall** — supersedes all of the above on context/objectives/rules; its own "tables not yet built" list is current-as-of-today ground truth |

---

## 2. Grounded facts from the actual build (not inferred, read directly)

- **`BUILD.md` (2026-07-17) confirms the DB is fresh and built from STEP directly** — `raw.discover` /
  `raw.detail` / `raw.verses` call STEP live; there is no migration-from-old-DB step anywhere in the
  build record. So snippet 1 §3.4's "fresh DB" decision **was followed**; snippet 1 §3.4.1's
  **migration procedure (raw/registry import from the old DB, cross-DB `src_old_id`/`src_old_ref`
  reference keys) was never built** — confirmed independently by the live schema: none of the 34
  tables carries any `src_old_*` column. **This is a build gap (Step 2 material), not a design
  ambiguity** — the plan called for migration; none happened; nothing in any later snippet reverses
  that call.
- **GOVERNANCE.md (2026-07-17) names the central unresolved seam itself, in its own words:**
  > *"reconciliation with the heavyweight `iba/config` configurator — this app uses its own
  > lightweight runtime config. Whether the two configs converge is a later decision."*
  This is more consequential than anything I flagged from the snippets. **There are two configurator
  designs, and the app runs on the smaller one:**
  - **Built (live, `iba/app/db/iba.db`):** a flat `cfg_*` set — `cfg_table`/`cfg_column`/`cfg_unique`
    (schema), `cfg_enum`, `cfg_connection`/`cfg_api` (`may_source` enforcement), `cfg_work_package`/
    `cfg_step` (run sequence), `cfg_setting`, `cfg_on_fail`, `cfg_status_flow`, plus `cfg_candidate_rule`
    (the domain-ruleset pattern) — **17 `cfg_*` tables today**, seeded from flat JSON (`schema.json`,
    `step.json`, `run.json`, `rules.json`) via `cfgload.py`. Proven working (1,041 config reads/run,
    `may_source` enforced, a DB-only rule-flip changes behaviour with no code touch).
  - **Designed (`iba/config/*.json`, snippet 1 Appendix A + snippet 5 in full):** the elaborate
    rule-anatomy model — Tier A/Tier B/utility files, one-rule-one-home, enums-are-definitional,
    `validation.enforcement` node, the full A.10 rule envelope, the 92→114-item content inventory.
    **This is not loadable and nothing reads it** (confirmed both in snippet 3 §7 — *"the `config/*.json`
    seed is not yet loadable"* — and in GOVERNANCE.md §6, 3 days earlier, calling it explicitly
    unreconciled).
  - **No later document resolves this.** It is still open as of today. **This is the single largest
    gap between plan and build**, and it is the app's own governance doc saying so, not my inference.
- **Live `cfg_work_package` has exactly 3 rows** (`new-word`, `set-candidates`, `build-passages`) —
  none named after either the old 9-segment model or the newer process-loop operations
  (`prepare-for-read`, `analyse-characteristic`, …). **Neither model has been implemented for the
  interpretive layer; only Base-layer substrate exists.** This matches snippet 4 §2's own statement
  ("zero interpretive/concordance runs exist yet").

---

## 3. The six items flagged earlier — resolved

1. **Fresh-DB vs actual build.** RESOLVED (§2 above): fresh-DB = done; migration procedure = never
   run; this is a Step-2 gap, not a design question.
2. **Naming collision (`ib_entry`/`ib_finding`/`ib_relation`/`ib_neighbour` vs `operation`/`meaning`
   vs `concordance`/`operations`/`meaning`).** RESOLVED by precedence: snippet 4 §6a **D3** (2026-07-20,
   latest) is explicit: rename to **`operation` + `finding`**; **`meaning`** stands as its own table.
   V3's own "not yet built" list (`Concordance, VE_lexical, Char_Operations, Char_meaning`) is the
   same set in the researcher's shorthand. `ib_entry` (snippet 1, 07-15) is superseded — but note
   **no later document replaces what `ib_entry` was FOR** (the meaning-in-context identity row that
   `operation`/`meaning`/`study_unit_char` all need to key on). Confirmed against the live DB: no such
   table exists under any name. **This identity gap is real and still open** — it is not a naming
   dispute, it is a missing design decision, carried forward to §5 below.
3. **9-segment pipeline vs process-loop operations.** RESOLVED by re-reading snippet 5 Tier B (the
   7 *process* files — registry·fetch·raw·verses-passages·lexical·characteristics·findings, the
   rule-governance axis) against snippet 2/4's *operations* (`prepare-for-read`,
   `analyse-characteristic`, …, the invoked-run axis): **these are two different axes, not two
   competing models.** A "process" is which rulebook a rule belongs to; an "operation"/work-package is
   what actually gets run and may draw rules from several processes at once (e.g.
   `analyse-characteristic` draws from the `lexical` and `characteristics` processes together). The
   9-segment *names* in snippet 1/V3's architecture diagram are the oldest layer and are superseded in
   substance by the 7-process + operation-set model — but the diagram box itself ("functional modules")
   is still structurally accurate, only the naming under it changes. Grounded further by §2 above: the
   live build has implemented **neither** model for anything past Base layer, so there is no
   contradiction to referee in running code, only in documents.
4. **D5** (reconcile/consolidate/refine-rule as own work packages vs steps inside `analyse`) — remains
   **explicitly open by the researcher's own instruction** (2026-07-20/21 session); not resolved here,
   not resolved by any snippet or the build.
5. **Configurator layout: snippet 5 supersedes snippet 1 Appendix A.** Confirmed by precedence (§1) —
   and now sharpened by §2: **neither** is what's actually running; the built app uses a third, simpler
   model. So for the Application Design document, §3 (Configurator) needs to present **three** things,
   not two: the built lightweight `cfg_*`, the designed elaborate `iba/config/*.json`, and the
   unresolved question of whether/how they converge.
6. **Layer 4 (Outputs/Products) has no design.** Confirmed as a documented, quantified gap (snippet 5's
   own coverage audit: 5 of 92 items have no home anywhere, all five being the study's end-point/
   products layer). Not open — it's a recorded, deliberate deferral, per the plan's own build order
   (framework → modules → prove sustainable → then re-run the study).

---

## 4. Revised structure for the Application Design document (Step 1's deliverable)

| § | Section | Grounding |
|---|---|---|
| 1 | Overview — operator's view, run interface | snippet 1 §3.3.1; V3 §3 diagram; **BUILD.md's actual PS→config→Python→handlers→lib→DB chain** as the proven instance |
| 2 | Architecture — layered stack | V3 §3; snippet 1 §3; **as actually realised** in `iba/app/` today |
| 3 | The Configurator — **both designs, reconciled or not** | 3.1 the built lightweight `cfg_*` (GOVERNANCE.md, ground truth) · 3.2 the designed elaborate `iba/config/*.json` (snippet 1 App. A + snippet 5 in full) · 3.3 **the open convergence question**, named explicitly, not silently merged |
| 4 | Utilities | snippet 1 §3.3.3; snippet 5 §2.1a; **which exist today** (`lib/db.py`, `lib/stepapi.py`, `lib/cfgload.py`, `lib/cfg.py` — confirmed built) vs which don't (git ops, file management, morphology parser — not yet in `iba/app/lib/`) |
| 5 | The DB / schema | 5.1 four-layer role + **actual disposition** (fresh built, not migrated) · 5.2 **the identity gap** (no meaning-in-context entry table, item 2 above) · 5.3 current live schema (34 tables, exact) · 5.4 missing tables (`operation`, `finding`, `meaning`, `ve_lexical`, `concordance` view) named per D3 · 5.5 the operation-type catalogue (snippet 3) · 5.6 the study-unit model (snippet 2 researcher comments + snippet 4 §4) · 5.7 completeness model (snippet 4 §5) · 5.8 open D1, D2, D4, D5, D6 |
| 6 | User Interaction | snippet 1 §3.3.1 (indicative verbs) vs **the actual interface** (`New-Word.ps1`, parameterised, no verb dispatcher yet) · snippet 2 "researcher operations" |
| 7 | Operation Modules | 7.1 the 3 **built** work packages (new-word/set-candidates/build-passages, exact steps from `cfg_step`) · 7.2 the process-loop operations, not yet built (`prepare-for-read`, `analyse-characteristic`, …) · 7.3 the process/operation axis distinction (item 3 above) |
| 8 | Validation & errors | snippet 1 §3.5/§3.7 (designed) vs **`cfg_on_fail`/`escalation`/`run` as actually implemented** (GOVERNANCE.md §3–4) |
| 9 | Outputs & Products (Layer 4) | recorded as a **deliberate, documented deferral** (item 6 above), not designed here |
| 10 | Governance, patterns, settings | snippet 1 Appendix C.11–C.12; snippet 5's `wide/governance.json`/`wide/patterns.json` (both still `pending`, unauthored) |
| 11 | Open decisions register | D5 (explicit) · the identity gap (item 2) · the two-configurator convergence (§2/item 5) · anything snippet 5 §6 lists as still open (`open.definitional-extends`, `open.utility-set`, `open.filing-seam`, `open.rule-table`, etc.) |
| 12 | Compliance checklist | one line per section/paragraph above, status = built / designed-not-built / open |

---

## 5. What's next

Unless this file comes back edited, I will draft full §1–§12 content next, grounding every "as built"
claim in the live DB/config exactly as done in §2–§3 above (query, not assume), and marking every
"as designed" claim with its source snippet. Genuinely open items (D5, the identity gap, the
two-configurator convergence) will be written as open in the document itself — not resolved by me
inventing an answer.
