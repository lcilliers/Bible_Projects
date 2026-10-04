# Learning4Comfort content handoff

`site/` is the only source directory synced to the standalone `lcilliers/learning4comfort` repository. Put only finished, explicitly approved pages and assets there. Working material and draft chapters must stay out.

The workflow copies `site/` into the target repository's `content/` directory. It does not copy the Bible_Projects repository, alter the target site's framework, or configure GitHub Pages. The target repository owns its site code, build, domain, and deployment workflow.

## Access setup

After creating `lcilliers/learning4comfort` with a `main` branch:

1. Create an SSH deploy key for that repository with write access and add its public key as a deploy key on `lcilliers/learning4comfort`.
2. Add the private key as the `LEARNING4COMFORT_DEPLOY_KEY` Actions repository secret in `lcilliers/Bible_Projects`.
3. Configure GitHub Pages deployment in `lcilliers/learning4comfort`. Its deployment workflow should build from the files in `content/` and deploy the generated site.

The private key must never be committed to either repository. The sync workflow only writes to `content/`; it leaves the target repository's other files untouched.

## Visibility

`lcilliers/Bible_Projects` is public. Any files placed in `site/` are therefore public in the source repository as well as copied to the target. This folder is a publishing boundary, not a privacy boundary.