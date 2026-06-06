---
name: feedback_use_cluster_full_names
description: Always give the full cluster NAME, not just the M-code, when referring to or asking about a cluster — the researcher reasons by name, not number
metadata:
  type: feedback
---

When referring to a cluster — especially when asking about a destination, routing an item, or presenting options — **always give its full name, not just the M-code**. Write "M33 (Peace)" / "M46 (Abundance — wealth and its impact)", never bare "M33" / "M46".

**Why:** the researcher reasons about the *consequences* of routing/decisions by the cluster's meaning, not its number. Bare codes are unintelligible at decision time and force a lookup. (Researcher rule, restated 2026-06-03; originally decision #6 in the 2026-06-02 session-close report.)

**How to apply:**
- First mention in any answer: `M{n} ({Full Name})`. Subsequent mentions in the same answer may use the code once the name is established, but prefer the name when a decision hinges on it.
- In disposition files / decision docs, label every routing target with its name.
- Cluster names live in `cluster.short_name` (and fuller sense in `cluster.description`); query them rather than guessing.
