# Escalation deep history

## #1524 — Validate catalogue questions against Window 1 evidence
type=task source=researcher

**v1** (2026-09-06T03:36:37Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Validate catalogue questions against Window 1 evidence
> **comment (set this version):** Researcher instruction, this chat turn, 2026-09-06: prepare the wa_obs_question_catalogue questions for Window 2 -- each question must be evaluated against the evidence actually coming out of Window 1 (verse_lexical Layer 1/2) to validate and evaluate the question itself, not just tagged by scope label. Spawned out of escalation #737's proposal (iba/docs/737-window2-cluster-based-methodology-proposal-v1-20260905.md §3.4), which only sorted the 131 live catalogue rows by scope label (Include=59 HIB-relevant / Exclude=68 Window-1's-own / 4 Science unresolved) -- that was a label-level triage, not the per-question evidence check the researcher is now asking for. Scope of this item: for each earmarked question, pull real Window-1 evidence (verse_lexical span/morph/role/party_kind + verse_lexical_note) for a representative sample of verses and check the question is well-formed, actually answerable from what Window 1 supplies (or correctly requires a Window-2 read), not a duplicate/near-duplicate of another catalogue row, and correctly scoped (HIB-relevant vs already-answered). Output = a validated, evidence-checked question set ready to be the literal framework Window 2's debate step (proposal §Step 4.3) runs against. No DB writes yet -- investigation and validation first.
> **context (set this version):** Parent: escalation #737. Catalogue: wa_obs_question_catalogue (bible_research.db), 131 live rows (deleted=0). Prior triage: iba/docs/737-window2-cluster-based-methodology-proposal-v1-20260905.md §3.4.

**v2** (2026-09-06T03:37:34Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Recommending hold, not starting blind -- see resolution for the reasoning and the actual fork.
> **resolution (set this version):** Recommend: HOLD #1524 until #737's open items get direction, rather than starting the per-question evidence-pull now. Reasoning: #737 still has open items that directly feed this item's scope -- the M10b/M10c/M27 cluster-membership check, the schema-location decision (fresh build in bible_research.db vs migrate iba.db), and the general go-ahead on the cluster-based process itself. The catalogue's Include(59)/Exclude(68)/unresolved(4) split in #737's proposal was scope-label triage, not yet approved as the actual working set -- validating each question's evidence now risks redoing the work if that split moves. Approve = hold #1524, pick it back up once #737 gets direction. Reject/revise = tell me to start #1524 now regardless, in parallel with #737.

**v3** (2026-09-07T03:32:36Z, Researcher) state=completed next_action=approved assigned_to=Claude
> **comment (set this version):**  noted 
