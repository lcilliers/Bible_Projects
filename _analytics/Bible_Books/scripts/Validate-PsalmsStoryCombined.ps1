param(
    [string]$Root = "C:\Bible_study_projects\verse-analysis\psalms\_narratives",
    [string]$OutputFile = "psalms_story_combined.md"
)

$out = Join-Path $Root $OutputFile
$files = Get-ChildItem -Path $Root -Recurse -File -Filter "*narratives.md" |
    Where-Object { $_.Name -notlike "_*.md" -and $_.FullName -ne $out } |
    Sort-Object FullName

$srcStoryMarkers = 0
foreach ($f in $files) {
    $srcStoryMarkers += (Select-String -Path $f.FullName -Pattern '^\s*(?:#{1,6}\s*)?_?story_?\s*:?[ \t]*$' -CaseSensitive:$false).Count
}

$outH2 = (Select-String -Path $out -Pattern '^##\s+').Count
$outH3 = (Select-String -Path $out -Pattern '^###\s+').Count

Write-Output "FILES_INPUT: $($files.Count)"
Write-Output "SRC_STORY_MARKERS: $srcStoryMarkers"
Write-Output "OUT_H2_FILE_HEADERS: $outH2"
Write-Output "OUT_H3_VERSE_HEADERS: $outH3"
Write-Output "PASS_STORY_EQ_H3: $($srcStoryMarkers -eq $outH3)"
