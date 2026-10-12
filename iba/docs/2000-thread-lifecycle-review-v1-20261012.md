# #2000 Thread lifecycle: what the code must let Claude do (review)

**Escalation:** #2000 · **Date:** 2026-10-12 · **Status:** approved (researcher, 2026-10-12: *"proceed with the build"*) and **built** in a Developer Mode session: `iba/app/BUILD.md` §338. Not yet tested: `iba/docs/2000-open-threads-test-plan-v4-20261012.md` section 10.

## 0. Rulings

**Round 1 (researcher, chat 2026-10-12, verbatim).** The researcher raised the questions this review answers: *"who will approve? how will approval for a specific item be gathered? does every item need approval? will the escalation automatically close if all the items have been approved? can a item be withdrawn or superceded? can a thread be withdrawn or superceded?"*

**Round 2 (researcher, chat 2026-10-12, verbatim).** The researcher rejected the round 1 proposal (an approval authority per item, `ready_for_approval` at the end, an assignment meaning):

> *"previously you managed the entire registry without me even reviewing anything, now you want me to go through a workflow if a step inbetween for every item. That is complete over engineering. I can only be asked for approval with sufficient data provided in the approval request to approve, else my ruling is moot - how can I make a decision without researching it. We decided I will give you feedback in the chat, the rest you need to control and the code must make it possible to manage the thread. all interaction must go to history."*

What follows from that:
- **Claude manages the threads, as it managed the register.** There is no approval step for an item or a thread.
- **The researcher's part is feedback in chat.** Claude records it verbatim in the same turn (`cfg_escalation` 5), as already designed (proposal §3.4).
- **An approval request goes to the researcher only when it carries the data needed to decide.** It is never routine.
- **The code's job is to make every lifecycle move possible.** That covers closing, withdrawing and superseding, at item and at thread level.
- **Every interaction is in the thread's history.**

## 1. What the code cannot do today (checked against `lib/escalation.py` and live `iba.db`)

| # | Gap | Effect |
|---|---|---|
| G1 | An item can only be `closed`. It cannot be withdrawn or superseded. | An item that is no longer relevant (for example OT-08: *"no longer relavant"*) reads as resolved. |
| G2 | When a task is withdrawn or superseded, its item on a thread is still recorded `closed`. | A thread reads as if the work had been done. |
| G3 | When the last item closes, the thread stays on-hold or in-progress. | It needs a further manual `approved` that nothing prompts, which is limbo. |
| G4 | A thread can be withdrawn or superseded while items are still open, and supersede names no successor. | The open items are orphaned under a dead thread. |
| G5 | History gets only a one-line summary of an item response (for example "item 2 (cluster:M03) closed"). The response text lives only in the response table. | Not every interaction is in history. |

## 2. Proposed changes (the minimum that closes G1 to G5)

1. **Item statuses `withdrawn` and `superseded`** (G1). They are added to `cfg_enum`, with response kinds of the same names.
   - Superseded names what replaces it, in the response text (`OT-nn` or `OT-nn.n`).
   - Neither counts as open, so neither blocks completion.
2. **A task's terminal state carries through** (G2). A task that is withdrawn or superseded gives its thread item `withdrawn` or `superseded`. A completed or closed task gives `closed`, as now.
3. **The last item ends the thread** (G3). When no item is left open, the thread moves to `completed` in the same call. The resolution is generated from the closing responses. This is one `cfg_escalation_transition` row (priority 0, beside T3 and T6), and it replaces the separate `approved` step of T6.
4. **Withdrawing or superseding a thread settles its items** (G4). In the same call:
   - **Withdraw:** every open item becomes `withdrawn`, with the thread's reason.
   - **Supersede:** the successor (`-SupersededBy OT-nn`) is required. Each open item is added to the successor and recorded `superseded` on the old thread, naming its new reference.
5. **Full text to history** (G5). Each item response writes its text, kind, who responded and `-Via` into the thread's history comment, not just a summary line. This includes your feedback, quoted verbatim.

**Not changed:** the D1 fix (a reassigned thread keeps its state, `BUILD.md` §337). Assignment needs no further meaning. `responded_by` on the 48 imported closures is left as it is.

## 3. If approved

The build runs in a Developer Mode session, config first:
- `cfg_enum`: the new statuses and response kinds.
- `cfg_escalation_transition`: one new row, last item closed → completed.
- `cfg_escalation` `thread_completion`: its text restated for change 3.
- `cfg_escalation_requirement`: a successor is required on supersede.

Then the code: `_respond`, `_sync_threads_for`, `update` (thread withdraw and supersede), and the history comment. Then `USER-GUIDE.md`, `GOVERNANCE.md` §93, a `BUILD.md` section, and test plan v4 for a standard session.
