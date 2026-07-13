# psalms_story_combined generation method

## Goal
Produce one combined Markdown file where:
- H1 is the combined file name.
- H2 is each cleaned source filename (remove prefix psalms_ and suffix _narratives).
- H3 is the verse reference taken from each source H2.
- Story body text is placed directly under the H3.

## Inputs
- Folder: C:\Bible_study_projects\verse-analysis\psalms\_narratives
- Source filter: *narratives.md
- Source exclusions: files starting with _ and the output file itself

## Parsing rules
1. Locate every source H2 line (## ...). Each defines a verse block.
2. Inside each verse block, find every _Story_ marker line matching:
   - optional heading hashes
   - story with optional surrounding underscores
   - optional trailing colon
3. For each Story marker found:
   - Use the current verse H2 text as the H3 reference.
   - Capture lines from after _Story_ until the next boundary:
     - _Reading_ or another _Story_ marker line
     - lexical anchor line like **term** - ref
     - horizontal rule line ---
   - Trim blank lines around the captured paragraph.
4. Emit one H3 per Story instance. This guarantees every story has an explicit verse reference.

## Why this was needed
Some files contain multiple _Story_ sections under the same verse H2 block. A first-pass extractor only captured the first Story per H2, which undercounted stories. The corrected method emits every Story occurrence.

## Validation approach
- Count exact Story markers in all source narrative files.
- Count H3 headings in the combined output.
- Expected pass condition:
  - source Story markers == output H3 headings

## Utility scripts
- Generate-PsalmsStoryCombined.ps1: builds the combined file using the final rules.
- Validate-PsalmsStoryCombined.ps1: validates source Story count vs output H3 count.
- Count-StoryMarkersByFile.ps1: per-file _story_ counts.
- Compare-H2-vs-StoryMarkers.ps1: per-file H2 count vs Story marker count.
