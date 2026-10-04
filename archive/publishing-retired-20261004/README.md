# Retired: direct-to-GitHub publishing route (2026-10-04, #1941)

These files were made outside a Claude session and never committed while live. They described a GitHub Action in this repo that copied `publishing/learning4comfort/site/` into the `lcilliers/learning4comfort` repo.

The researcher ruled against that route (#1941, verbatim): *"this project (bible_study_projects) does not publish directly to github"*. The live route is `iba\app\ps\Copy-NarrativeToLearning4Comfort.ps1`, which copies the current narrative files to the learning4comfort `publication-inbox`.

- `github/workflows/publish-learning4comfort-content.yml`: was `.github/workflows/`. It is renamed here, so GitHub never runs it.
- `publishing/learning4comfort/SOURCE-SETUP.md`: was `publishing/learning4comfort/`.

Kept for provenance only.
