---
description: Leave Developer Mode — clears the marker file and statusline indicator, reverts this session to standard-permission expectations
---

# Exit Developer Mode

Run this when Developer Mode work is done for this session, or before treating this session as
App Mode again.

1. Delete `.claude/.developer-mode-active` if it exists. If it doesn't exist, say so — don't treat
   a no-op as an error.
2. Stop prefixing replies with the Developer Mode banner from this point on.
3. State plainly, in chat, that the marker is cleared and the statusline indicator (if wired up)
   will drop on its next render.

This does not retroactively gate anything already built or written this session — it only ends the
declared basis going forward. Any `cfg_*` change made while the marker was active still needs its
own registration per `config-updated-same-unit-of-work-as-change`; that isn't undone by exiting.
