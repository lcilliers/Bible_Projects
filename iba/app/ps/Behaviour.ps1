<#
.SYNOPSIS
    Read-only front door for the operational-behaviour cfg layer (`cfg_behaviour_class` +
    `cfg_behaviour_rule`, escalations #715/#732/#733). Content is written by the one-off migration
    scripts (`bootstrap_behaviour_rules_v1_20260818.py` and its cycle-2/3/... siblings), never by
    this script — this is a query/report tool, not a writer.

.DESCRIPTION
    -Action List [-Class <chat|terminal|sqlite|documentation|llm_output|development>]
        Writes every active rule (optionally scoped to one class) to
        `behaviour.list_report_path` (default `iba/app/reports/behaviour-rules-list.md`; archived
        on regenerate, same convention as every other report) and prints a one-line pointer +
        count. Added 2026-08-18 (escalation #733's structural read-through found this module had
        three build cycles and no supporting PS entry point — exactly the gap
        `development.every-interactive-module-needs-ps-script` exists to catch).

.EXAMPLE
    .\Behaviour.ps1 -Action List
.EXAMPLE
    .\Behaviour.ps1 -Action List -Class chat
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('List')]
    [string] $Action,
    [ValidateSet('chat', 'terminal', 'sqlite', 'documentation', 'llm_output', 'development')]
    [string] $Class
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot

switch ($Action) {
    'List' {
        if ($Class) {
            python -m iba.app.lib.behaviour list "--class=$Class"
        } else {
            python -m iba.app.lib.behaviour list
        }
    }
}
