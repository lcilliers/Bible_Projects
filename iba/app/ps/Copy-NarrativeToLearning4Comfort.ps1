<#
.SYNOPSIS
    Copy the current inner-being narrative files to the learning4comfort publication inbox
    (escalation #1941). This project never publishes to GitHub itself; the learning4comfort repo
    prepares, reviews and publishes from its inbox.

.DESCRIPTION
    Source: cfg_setting narrative.copy_source_dir (top-level .md files only; archive/ is never
    copied). Target: cfg_setting narrative.learning4comfort_inbox_dir. Earlier versions of the same
    files in the target are replaced; every other file there is left untouched. No git commands.

    Run it when a section of work is complete, on request, and as part of /session-close
    (.claude/commands/session-close.md).

.PARAMETER DryRun  List what would be copied, removed and left alone; write nothing.

.EXAMPLE
    iba\app\ps\Copy-NarrativeToLearning4Comfort.ps1 -DryRun
    iba\app\ps\Copy-NarrativeToLearning4Comfort.ps1
#>

[CmdletBinding()]
param(
    [switch] $DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

$pyArgs = @('-m', 'iba.app.lib.narrativecopy')
if ($DryRun) { $pyArgs += '--dry-run' }
python @pyArgs
exit $LASTEXITCODE
