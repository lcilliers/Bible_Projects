param(
    [string]$Root = "C:\Bible_study_projects\verse-analysis\psalms\_narratives",
    [string]$ReportFile = "_h2_vs_storymarker_by_file.csv"
)

$files = Get-ChildItem -Path $Root -Recurse -File -Filter "*narratives.md" |
    Where-Object { $_.Name -notlike "_*.md" -and $_.Name -ne "psalms_story_combined.md" } |
    Sort-Object FullName

$rows = foreach ($f in $files) {
    $lines = Get-Content -Path $f.FullName
    $h2 = ($lines | Where-Object { $_ -match '^\s*##\s+' }).Count
    $story = (Select-String -Path $f.FullName -Pattern '^\s*(?:#{1,6}\s*)?_?story_?\s*:?[ \t]*$' -CaseSensitive:$false).Count

    [PSCustomObject]@{
        File         = $f.Name
        H2           = $h2
        StoryMarkers = $story
        Diff         = ($story - $h2)
    }
}

$report = Join-Path $Root $ReportFile
$rows | Export-Csv -Path $report -NoTypeInformation -Encoding UTF8

Write-Output "REPORT: $report"
Write-Output "TOTAL_H2: $(($rows | Measure-Object -Property H2 -Sum).Sum)"
Write-Output "TOTAL_STORY_MARKERS: $(($rows | Measure-Object -Property StoryMarkers -Sum).Sum)"
Write-Output "FILES_DIFF_NE_0: $((@($rows | Where-Object { $_.Diff -ne 0 })).Count)"
