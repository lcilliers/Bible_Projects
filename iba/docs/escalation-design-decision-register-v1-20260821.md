# Escalation design — decision register (v1, 2026-08-21)

The exact list asked for: every decision point raised across v1→v3, its current status, where it
came from, and where it's captured now. Re-derived from the actual documents and escalation `#6`'s
full history this pass, not reconstructed from running memory of the conversation — the whole point
of this artifact is that it has to be more reliable than that. Updated in place as the design moves
forward (version-bumped per this project's normal filing rule when it changes materially — not
regenerated from scratch each time).

**Status key:** `SETTLED` — researcher confirmed, stands unless reopened. `OPEN` — needs a decision.
`REJECTED` — proposed, explicitly turned down, kept here so it isn't proposed again by accident.
`SUPERSEDED` — replaced by a later decision, kept for provenance.

| # | Decision point | Status | Source | Captured in |
|---|---|---|---|---|
| D1 | Reseed `escalation`'s id sequence to continue from `escalations_old` (735) | **OPEN** | v1 | escalation `#5`; v3 §tables and columns |
| D2 | Fix stale `cfg_table.use` text (`escalation`/`escalation_history` describe the retired snapshot design) | **OPEN** | v1 | escalation `#4`; v3 §tables and columns |
| D3 | Auto-escalate every routine's crashes app-wide, not just `escalation.py`'s own CLI | **OPEN** — silently deferred once already (rebuild design v1 §10) | v1 (the researcher's original directive) | not yet re-addressed in v2/v3 |
| D4 | Register both escalation reports through `reportkit`/`cfg_report` | **OPEN** — silently deferred twice before this design work started | v1 (directive 3) | mechanism designed in v3 §report; build decision is D16 |
| D5 | `GOVERNANCE.md` never updated for the escalation mechanism, across the entire redesign lineage | **OPEN** | v1 | v3 §Governance |
| D6 | A standing tracking item survives resets, carrying open scope forward | **DONE** | v1 | escalation `#6` itself |
| D7 | `cfg_utility.escalation.purpose` still the narrow pre-redesign one-liner | **OPEN** | v1 | not restated as its own line since v2 — still real, still unbuilt |
| D8 | `escalation_shape` enum passes the orphan-config check without being read at runtime (a `cfgquality.py` blind spot, not escalation-specific) | **OPEN**, out of this module's own scope | v1/v2 | flagged for `#9` (on hold) |
| D9 | Five-type model: `task`/`issue`/`notice`/`run_error`/`config`, each a distinct shape of life | **SETTLED** — confirmed correct, 2026-08-21 | v2, confirmed this turn | v3 §Type of entries |
| D10 | `cfg_escalation_link` — a typed, many-to-many, `cfg_`-prefixed link table | **REJECTED** — wrong prefix (data, not config) and wrong shape (many-to-many for a problem that's always single-parent) | v2 proposal | superseded by D14 |
| D11 | Issue's own `next_action` vocabulary (`open`/`decided`/`abandoned`) as a standalone addition | **OPEN**, superseded in scope by D21 — researcher: needs to be part of one holistic vocabulary treatment, not a bolt-on | v2, challenged this turn | folded into D21 |
| D12 | Type-keyed defaults at Raise (`notice` closes itself immediately; `issue` opens instead of defaulting to `review`) | **SETTLED**, confirmed implicitly alongside D9 | v2 | v3 (carried, not separately restated) |
| D14 | `escalation.from_id` + `related_activity` (free text) replacing the link table | **SETTLED** — confirmed, "dealt with in v3" | v3, confirmed this turn | v3 throughout |
| D15 | Five report-time exception categories (cycle / dangling / mismatched-pairing / missing-link / incoherent-link) + the incoherent-link detection proposal (dominant-label comparison) | **OPEN** — not yet confirmed either way | v3 | v3 §validation / §report |
| D16 | Whether the `run.py` re-plumbing the report registration implies gets built now, or stays designed-not-built | **OPEN** | v3 | v3 §Summary |
| D18 | How script/code changes get recorded within the type model — the `task`/`BUILD.md` boundary | **OPEN**, new | this turn | this session's chat reply; not yet in a versioned doc |
| D19 | The mechanism for documenting chat content captured into an item — verbatim vs paraphrase | **OPEN**, new | this turn | this session's chat reply; not yet in a versioned doc |
| D20 | The relationship between escalation items and `BUILD.md`/`GOVERNANCE.md`/`CLAUDE.md`/`USER-GUIDE.md` | **OPEN**, new | this turn | this session's chat reply; not yet in a versioned doc |
| D21 | A complete, holistic `next_action` × `state` × `type` vocabulary — what exists, what's missing, why, reasoned together rather than per-section | **OPEN**, new (absorbs D11) | this turn | this session's chat reply; not yet in a versioned doc |
| D22 | The exact PS front-door specification — client-side validation, error handling, how it lands in the engine | **OPEN**, new | this turn | this session's chat reply; not yet in a versioned doc |
| D23 | Whether PS is the right interface for this at all, and what the real alternatives are | **OPEN**, new | this turn | this session's chat reply; not yet in a versioned doc |
| D24 | This register's own completeness and reliability | **OPEN**, self-referential — the actual thing being tested this turn | this turn | this document |

**Count: 24 decision points raised across the whole lineage. 4 settled, 1 rejected, 19 open** — of
which 6 (D18–D23) are new this turn and not yet written into any design document; they're answered
in chat this turn and will move into v4 once confirmed, at which point this row updates to point at
v4 instead of "this session's chat reply."

**What this register is *for*, going forward:** every future turn on this design either resolves a
row (moves it to `SETTLED`/`REJECTED` with the turn that did it) or adds a new one — never silently
drops one. If a row sits `OPEN` for several rounds without being touched, that's visible here, not
buried in a document some section rewrote past it.
