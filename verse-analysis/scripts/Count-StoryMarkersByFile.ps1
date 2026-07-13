param(
    [string]$Root = "C:\Bible_study_projects\verse-analysis\psalms\_narratives",
    [string]$ReportFile = "_story_count_by_file.csv"
)

$files = Get-ChildItem -Path $Root -Recurse -File -Filter "*narratives.md" |
    Where-Object { $_.Name -notlike "_*.md" -and $_.Name -ne "psalms_story_combined.md" } |
    Sort-Object FullName

$rows = foreach ($f in $files) {
    $hits = Select-String -Path $f.FullName -Pattern '(?i)_story_' -AllMatches
    $count = 0
    foreach ($h in $hits) {
        $count += $h.Matches.Count
    }

    [PSCustomObject]@{
        File       = $f.Name
        StoryCount = $count
    }
}

$report = Join-Path $Root $ReportFile
$rows | Export-Csv -Path $report -NoTypeInformation -Encoding UTF8

Write-Output "REPORT: $report"
Write-Output "FILES: $($rows.Count)"
Write-Output "TOTAL_STORY_MATCHES: $(($rows | Measure-Object -Property StoryCount -Sum).Sum)"
Write-Output "NONZERO_FILES: $((@($rows | Where-Object { $_.StoryCount -gt 0 })).Count)"
