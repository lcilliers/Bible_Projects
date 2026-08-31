# statusline-devmode.ps1
#
# Claude Code statusLine command for this project.
#
# Reads the statusLine stdin JSON payload (see Claude Code docs: the CLI pipes a
# JSON object with model/workspace/session info to the configured statusLine
# command on every render) and:
#   - if <project_dir>/.claude/.developer-mode-active exists, prepends a loud,
#     colored "DEVELOPER MODE ACTIVE" warning to the normal status content;
#   - otherwise, prints only the normal/default status content
#     (model display name + current directory).
#
# Path to the marker file is resolved from the payload's workspace.project_dir
# (falling back to the top-level cwd field) rather than a hardcoded absolute
# path, so this keeps working if the checkout is ever moved.

$ErrorActionPreference = 'Stop'

try {
    $raw = [Console]::In.ReadToEnd()
    $data = $null
    if ($raw) {
        $data = $raw | ConvertFrom-Json -ErrorAction Stop
    }
} catch {
    $data = $null
}

# Resolve the project root robustly: prefer workspace.project_dir (the
# documented project-root field in the statusLine payload), then fall back to
# the top-level cwd, then to this script's own location as a last resort.
$projectDir = $null
if ($data -and $data.workspace -and $data.workspace.project_dir) {
    $projectDir = $data.workspace.project_dir
} elseif ($data -and $data.cwd) {
    $projectDir = $data.cwd
} else {
    $projectDir = Split-Path -Parent $PSScriptRoot
}

$modelName = $null
if ($data -and $data.model -and $data.model.display_name) {
    $modelName = $data.model.display_name
}

$currentDir = $null
if ($data -and $data.workspace -and $data.workspace.current_dir) {
    $currentDir = $data.workspace.current_dir
} elseif ($data -and $data.cwd) {
    $currentDir = $data.cwd
}

# Normal/default status content: model name + a short current-directory tail.
$defaultParts = @()
if ($modelName) { $defaultParts += $modelName }
if ($currentDir) { $defaultParts += (Split-Path -Leaf $currentDir) }
if ($defaultParts.Count -eq 0) { $defaultParts += 'Claude Code' }
$defaultLine = [string]::Join(' | ', $defaultParts)

$markerPath = Join-Path -Path $projectDir -ChildPath '.claude/.developer-mode-active'

if (Test-Path -LiteralPath $markerPath -PathType Leaf) {
    $esc = [char]27
    $boldRed = "$esc[1;91m"
    $reset = "$esc[0m"
    Write-Output "${boldRed}*** DEVELOPER MODE ACTIVE ***${reset} $defaultLine"
} else {
    Write-Output $defaultLine
}
