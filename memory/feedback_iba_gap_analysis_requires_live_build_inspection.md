---
name: feedback_iba_gap_analysis_requires_live_build_inspection
description: "IBA gap/compliance analysis must inspect the live build (code + actual DB row content) directly, never synthesize from design-doc text; fix order matters (utility before use, rule before fix); check the full principle/rule-sextet, not just flagged items."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T13:35:35.027Z
---

A gap list or compliance audit on the IBA app produced from design-doc text and prior comments — without
directly reading the live handler/utility code and querying actual `cfg_*` row *content* (not just row
counts) — is not a real evaluation. The researcher's verdict on a 2026-07-21 gap list built this way:
"just a dump from memory and the comments in the V2 build document, in no way a considered evaluation of
suitability, compliance... and will it actually do what is intended."

**Why:** design docs describe intent and prior findings; they are not proof of current DB content or
code behaviour. A gap list built only from doc text repeats whatever the doc already said, including its
blind spots — it looks thorough but never independently checked reality.

**Concrete requirements surfaced by the correction, generalizable beyond that one list:**

1. **Confirm content, not just presence.** "The table has rows" is not "the rows are correct and
   complete." Any claim about `cfg_*` (or any table) state must come from querying and reading actual
   row content, not from a row count already on file.
2. **Fix order: the utility that maintains a thing must be fixed/confirmed before using it to change
   that thing.** Per governance rule c, all config changes route through `configuration_maintenance` —
   so before proposing config fixes, first confirm that utility is actually complete, *usable by the
   researcher* (not just present in code), and has an inspection/reporting surface. Don't assume a
   single already-flagged deficiency (e.g. "no row-level change tracking") is the *only* gap in a
   utility — audit the whole thing.
3. **Fix order: confirm the rule before fixing the process.** E.g. before rebuilding a fragmented
   passage table, first diagnose *why* it's fragmented and get the researcher to confirm what the
   correct passage-building rule should be. Never jump straight to "rebuild it."
4. **Check every module against the full principle set (a–k) and the full rule sextet (i:
   create/update/delete · data · relationships · output · validity · quality) systematically** — not
   just the deficiencies a document happened to already name. Reporting and validation surfaces in
   particular are easy to silently omit from a memory-based sweep.

**How to apply:** for any future "list the gaps" / "is this compliant" task on IBA (or similar
DB-resident-config apps), start by reading the actual code (handlers, utility modules) and running
direct queries against the live DB — before writing anything down. Related: [[feedback_iba_no_synthesis_small_units_only]],
[[feedback_source_of_truth_is_written_record]].
