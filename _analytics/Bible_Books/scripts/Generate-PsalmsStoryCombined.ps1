param(
    [string]$Root = "C:\Bible_study_projects\verse-analysis\psalms\_narratives",
    [string]$OutputFile = "psalms_story_combined.md"
)

$out = Join-Path $Root $OutputFile
$files = Get-ChildItem -Path $Root -Recurse -File -Filter "*narratives.md" |
    Where-Object { $_.Name -notlike "_*.md" -and $_.FullName -ne $out } |
    Sort-Object FullName

$outLines = @()
$outLines += "# $([System.IO.Path]::GetFileNameWithoutExtension($OutputFile))"
$outLines += ""
$outLines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$outLines += ""

$fileCount = 0
$storyCount = 0

foreach ($f in $files) {
    $src = Get-Content -Path $f.FullName
    if (-not $src -or $src.Count -eq 0) {
        continue
    }

    $h2Idx = @()
    for ($i = 0; $i -lt $src.Count; $i++) {
        if ($src[$i] -match '^\s*##\s+.+$') {
            $h2Idx += $i
        }
    }

    if ($h2Idx.Count -eq 0) {
        continue
    }

    $base = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    $nameClean = $base -replace '(?i)^psalms_+', '' -replace '(?i)_+narratives$', '' -replace '^_+', '' -replace '_+$', ''
    $added = $false

    for ($j = 0; $j -lt $h2Idx.Count; $j++) {
        $start = $h2Idx[$j]
        $end = if ($j -lt $h2Idx.Count - 1) { $h2Idx[$j + 1] - 1 } else { $src.Count - 1 }

        $verseRef = ($src[$start] -replace '^\s*##\s+', '').Trim()
        $block = if ($end -gt $start) { $src[($start + 1)..$end] } else { @() }

        $storyMarkers = @()
        for ($k = 0; $k -lt $block.Count; $k++) {
            if ($block[$k] -match '^\s*(?:#{1,6}\s*)?_?story_?\s*:?[ \t]*$') {
                $storyMarkers += $k
            }
        }

        if ($storyMarkers.Count -eq 0) {
            continue
        }

        if (-not $added) {
            if ($outLines.Count -gt 4) {
                $outLines += ""
            }
            $outLines += "## $nameClean"
            $outLines += ""
            $added = $true
            $fileCount++
        }

        # Emit one H3 per Story instance so every story is explicitly verse-referenced.
        for ($m = 0; $m -lt $storyMarkers.Count; $m++) {
            $sStart = $storyMarkers[$m] + 1
            $sEnd = $block.Count - 1

            for ($k = $sStart; $k -lt $block.Count; $k++) {
                if (
                    $block[$k] -match '^\s*(?:#{1,6}\s*)?_?(reading|story)_?\s*:?[ \t]*$' -or
                    $block[$k] -match '^\s*\*\*.+\*\*\s+[-\x{2014}]\s+' -or
                    $block[$k] -match '^\s*---\s*$'
                ) {
                    $sEnd = $k - 1
                    break
                }
            }

            $story = @()
            if ($sEnd -ge $sStart) {
                $story = $block[$sStart..$sEnd]
            }

            while ($story.Count -gt 0 -and [string]::IsNullOrWhiteSpace($story[0])) {
                if ($story.Count -eq 1) {
                    $story = @()
                }
                else {
                    $story = $story[1..($story.Count - 1)]
                }
            }

            while ($story.Count -gt 0 -and [string]::IsNullOrWhiteSpace($story[$story.Count - 1])) {
                if ($story.Count -eq 1) {
                    $story = @()
                }
                else {
                    $story = $story[0..($story.Count - 2)]
                }
            }

            if ($story.Count -gt 0) {
                $outLines += "### $verseRef"
                $outLines += ""
                $outLines += $story
                $outLines += ""
                $storyCount++
            }
        }
    }
}

Set-Content -Path $out -Value $outLines -Encoding UTF8

$outH3 = (Select-String -Path $out -Pattern '^###\s+').Count
Write-Output "WROTE: $out"
Write-Output "FILES_OUTPUT: $fileCount"
Write-Output "STORIES_EXTRACTED: $storyCount"
Write-Output "OUT_H3_COUNT: $outH3"
