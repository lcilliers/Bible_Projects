<#
.SYNOPSIS
    PILOT (not registered in the app): runs the local Ollama model over the 39 verses redone on
    2026-10-30 and compares its output with the researcher's Analysis_phase_1 observations.
    Read-only on iba.db. Nothing is written to the database.

.PARAMETER Count   how many verses to run (default 1 = a quick test). Use 39 for the full pilot.
.PARAMETER Verse   run one verse by osisId, e.g. Deut.10.12
.PARAMETER Model   Ollama model (default qwen2.5:7b-instruct)
.EXAMPLE
    .\Pilot-LocalLLM.ps1 -Count 1
    .\Pilot-LocalLLM.ps1 -Count 39
    .\Pilot-LocalLLM.ps1 -Verse Deut.10.12
#>
[CmdletBinding()]
param(
    [int] $Count = 1,
    [string] $Verse,
    [string] $Model = 'qwen2.5:7b-instruct',
    [string] $Endpoint = 'http://localhost:11434',
    [int] $TimeoutSec = 900
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
$here = $PSScriptRoot
$db   = Join-Path (Split-Path -Parent (Split-Path -Parent $here)) 'db\iba.db'
$run  = 'pilot-' + (Get-Date -Format 'yyyyMMdd_HHmmss')
$out  = Join-Path $here "runs\$run"
New-Item -ItemType Directory -Force $out | Out-Null

try { $null = Invoke-RestMethod "$Endpoint/api/version" -TimeoutSec 5 }
catch { throw "Ollama is not reachable at $Endpoint. Start it first." }

$inputFile = Join-Path $out 'pilot-input.json'
& python -I (Join-Path $here 'export_pilot.py') $db $inputFile
if ($LASTEXITCODE -ne 0) { throw 'export failed' }
$data = Get-Content $inputFile -Raw -Encoding UTF8 | ConvertFrom-Json
$verses = @($data.verses)
if ($Verse) { $verses = @($verses | Where-Object { $_.osisId -eq $Verse }) } else { $verses = @($verses | Select-Object -First $Count) }
if (-not $verses.Count) { throw 'no verse selected' }

$itemKeys = @('meaning','role','polarity','object','enactment','party','circumstance','operation','chain','flag')
$itemHelp = ($data.items.items | ForEach-Object { "- $($_.key): $($_.name)" }) -join "`n"
$modes = ($data.items.modes -join ', ')

$schema = @{
  type = 'object'
  properties = @{
    observations = @{ type = 'array'; items = @{
      type = 'object'
      properties = @{
        item = @{ type = 'string'; enum = $itemKeys }
        surface = @{ type = 'string' }
        mode = @{ type = 'string' }
        observation = @{ type = 'string' }
        grounds = @{ type = 'string' }
      }
      required = @('item','surface','observation')
    } }
    items_absent = @{ type = 'object' }
  }
  required = @('observations')
}

$system = @"
You analyse one Bible verse (ESV) for how Scripture describes the workings of the human inner being.
Use ONLY the verse text given. Never quote more than 7 consecutive words of the verse. State only what the verse shows.
For each inner-being word (heart, soul, spirit, mind, will, desire, fear, love, etc.), write observations under these items:
$itemHelp
Rules: an item the verse does not show is omitted and named in items_absent with a short reason. The 'operation' item is always present for the verse (who or what does what), with mode one of: $modes. 'grounds' = the words of the verse that ground a read observation.
"@

function Get-Words([string] $s) { ($s.ToLower() -replace "[^a-z0-9' ]", ' ') -split '\s+' | Where-Object { $_ } }

$summary = @()
foreach ($v in $verses) {
  Write-Host ("== {0}  {1}" -f $v.osisId, $v.reference)
  $body = @{
    model = $Model; stream = $false; format = $schema
    options = @{ temperature = 0; num_ctx = 4096 }
    messages = @(@{ role = 'system'; content = $system }, @{ role = 'user'; content = "Verse $($v.reference): $($v.text)" })
  } | ConvertTo-Json -Depth 10
  $sw = [Diagnostics.Stopwatch]::StartNew()
  $r = Invoke-RestMethod "$Endpoint/api/chat" -Method Post -Body ([Text.Encoding]::UTF8.GetBytes($body)) -ContentType 'application/json; charset=utf-8' -TimeoutSec $TimeoutSec
  $sw.Stop()
  $valid = $true
  try { $res = $r.message.content | ConvertFrom-Json } catch { $valid = $false; $res = $null }

  $copied = 0; $itemsGot = @(); $hasOp = $false
  if ($valid -and $res.observations) {
    $vw = @(Get-Words $v.text)
    foreach ($o in $res.observations) {
      $itemsGot += $o.item
      if ($o.item -eq 'operation') { $hasOp = $true }
      $ow = @(Get-Words ([string]$o.observation))
      for ($i = 0; $i -lt $vw.Count; $i++) { for ($j = 0; $j -lt $ow.Count; $j++) {
        $k = 0
        while (($i + $k) -lt $vw.Count -and ($j + $k) -lt $ow.Count -and $vw[$i + $k] -eq $ow[$j + $k]) { $k++ }
        if ($k -gt $copied) { $copied = $k } } }
    }
  }
  $refItems = @($v.reference_observations | ForEach-Object { $_.item } | Where-Object { $_ })
  $row = [pscustomobject]@{
    osisId = $v.osisId; seconds = [math]::Round($sw.Elapsed.TotalSeconds, 1)
    json_valid = $valid; model_obs = @($itemsGot).Count; reference_obs = @($v.reference_observations).Count
    has_operation = $hasOp; longest_verse_copy = $copied; copy_ok = ($copied -le 7)
    items_model = (($itemsGot | Group-Object | ForEach-Object { "$($_.Name)=$($_.Count)" }) -join ' ')
    items_reference = (($refItems | Group-Object | ForEach-Object { "$($_.Name)=$($_.Count)" }) -join ' ')
  }
  $summary += $row
  [pscustomobject]@{ verse = $v; model_output = $res; raw = $r.message.content; seconds = $row.seconds } |
    ConvertTo-Json -Depth 12 | Set-Content (Join-Path $out ("{0}.json" -f $v.osisId)) -Encoding UTF8
  $row | Format-List | Out-String | Write-Host
}
$summary | Export-Csv (Join-Path $out 'summary.csv') -NoTypeInformation -Encoding UTF8
Write-Host "Done. Results in $out"
Write-Host ("JSON valid {0}/{1}; copy-rule ok {2}/{1}; has operation {3}/{1}; mean {4}s/verse" -f `
  @($summary | Where-Object { $_.json_valid }).Count, $summary.Count, @($summary | Where-Object { $_.copy_ok }).Count,
  @($summary | Where-Object { $_.has_operation }).Count, [math]::Round(($summary | Measure-Object seconds -Average).Average, 1))
