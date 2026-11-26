<#
.SYNOPSIS
    Module 5 of 5 of the surface cycle: the members of each collection, decided from the AI judgements (escalation #2361).

.DESCRIPTION
    A collection has a core word. The AI judged each candidate word against it (synonym, opposite or distinct), and the words that are neither
    for association by meaning. This step turns those judgements in the tables into the members of each collection: core, synonym, opposite,
    possible_opposite (a lead, never a member), set_aside and associated. Reads and writes tables only; no file is an input.

      Status    how the stored members stand against what the judgements decide (read-only)
      Links     write the difference; -Check previews. A pair whose link was removed is not linked again. A second Links changes nothing.
      Show      -Collection <name>   one collection with its members by tier
      Export    a CSV of the collections to the exports folder (a view of the tables)
      ExportMembers   a CSV of the member surfaces of the collections, one row for each verse, cluster and tier, with the verse text (the #2379 members-verses view)
      ExportSurfaces  a CSV of the surfaces of the behaviour and inner-being-state groups, one row for each verse and cluster, with the collection and tier (the #2379 surfaces view)
                The three exports take no name: the file name is cfg_setting collection.export_names and the version is the next one by the filing rule;
                the previous live version is moved to the archive folder (#2413).
      Evidence  -Collection <name>[,<name>...] | -Verse "<references>"  [-Check]   the entries stored for every aspect of the members of one or more
                collections, or of the words of a verse or list of verses, from the base data through the observations and claims into the narrative, as a Markdown
                report (the reading: the Strong's codes behind the members, what the study recorded for them, the claims, the phrases, the faults) and an Excel workbook (every listing
                in full, one sheet each) under cfg_setting surfaces.exports_root (the folder of the other collection exports); no evaluation, nothing inferred, nothing written to a table
                (#2464, #2467, #2477). Verses are in Scripture order.
                References: Book chapter:verse (Pro 6:14), a range (Pro 6:14-16, Pro 6:30-7:2), a whole chapter (Pro 6), a list of one book (Pro 6:14, 16);
                each item starts with its book, as the verse table writes it (Mat, 1Sa, Phili) or an alias (Matthew, 1Sam, Ps); items are separated by a
                semicolon, the whole in quotes: -Verse "Pro 6:14-16; Mat 11:29; 1Sa 24:5"
      Index     [-Check]   fill the index of the surfaces of the confirmed collections (one row for each member surface, unplaced; a row whose surface left its collection is
                retired). Mechanical, no judgement (#2503)
      Subgroup  -Collection <name> -Name <subgroup> -Reason <text>   make a subgroup of a collection (a group of surfaces of one meaning), as your correction of the grouping by meaning
                -Collection <name> -Name <subgroup> -Surface <a,b> [-Strong <code>] -Reason <text>   place surfaces in it (-Strong places one sense of a surface)
                -Collection <name> -Surface <a,b> -Isolate -Reason <text>   set aside surfaces whose meaning is not the one the collection gathers. -Check previews (#2503)
      LayerOpen  -Collection <name> -Step S1|1.1|1.2|2.1|3.1|3.2|3.3 [-Check]   open a step of the layered reading: the gates (the grouping finished, the previous step closed; -Subgroup <name> opens a step for one subgroup of the collection
                                    in isolation, #2538, and S1 (the words) is read after the grouping, subgroup by subgroup; step 3.1, the first of stage 4 (the inner-being analysis), needs 1.1, 1.2 and 2.1 closed), then the ledger rows the data demands (#2505, #2528)
      LayerPull  -Collection <name> -Step <step>   write the working file of the open rows with the evidence to read (a stage 4 file holds pull_max_rows rows: the verse in its passage, the
                                    occurrences, the stage 1 to 3 observations, the earlier observations with their flags, the meaning evidence, the interventions)
      (LayerOpen, LayerPull take -Subgroup <name>: the loop over the subgroups, one subgroup in isolation, #2538)
      LayerRecord -File <filled working file> [-Check]   check the file whole and write its observations, nodes and ledger answers in one transaction
      LayerNext -Collection <name>   say what to do next in the layered reading, from the ledger alone: the subgroup in flight, the step, its state and the verbs; a step of a subgroup is refused while another subgroup is further through its loop and not finished (escalation #2538)
      ReadWords -Collection <name> -Subgroup <name>   the package of the next words of one subgroup to read (step S1): the instruction of this read from cfg_setting layer.read_types, only these words' occurrences, verses and lexicon, and the answer to fill; opens S1 for the subgroup if needed (escalation #2538)
      RecordWords -File <answer> [-Check]   check a filled ReadWords answer whole, write it through the recorder, validate the subgroup's rows and print the next command (escalation #2538)
      ReadSenses -Collection <name> -Subgroup <name>   the package of the senses of one subgroup (step 1.1): the instruction, every B1 observation of the subgroup with its occurrences, the sense head and meaning range of each code, the older observations, and the answer to fill; opens 1.1 for the subgroup if needed (escalation #2538)
      RecordSenses -File <answer> [-Check]   check a filled ReadSenses answer whole (each B1 observation carried by one sense), write it through the recorder, validate the subgroup's 1.1 row and print the next command (escalation #2538)
      ReadEnrichment -Collection <name> -Subgroup <name>   the package of the enrichment of one subgroup (step 1.2): the instruction, every 1.1 sense with its codes and occurrences, the lexicon of every code, the older observations, and the answer to fill; opens 1.2 for the subgroup if needed (escalation #2538)
      RecordEnrichment -File <answer> [-Check]   check a filled ReadEnrichment answer whole (one enrichment for each sense), write it through the recorder, validate the subgroup's 1.2 row and print the next command (escalation #2538)
      ReadStructure -Collection <name> -Subgroup <name> [-Item double-meaning|qualifier|entity|direction|pairing]   the package of the next rows of step 2.1 of one subgroup, one item at a time: what each row asks, its occurrences, the WordNet control of a pairing, the older observations, the verses with their stored structure and the 1.1 senses; opens 2.1 for the subgroup if needed (escalation #2538)
      RecordStructure -File <answer> [-Check]   check a filled ReadStructure answer whole, write it through the recorder, validate the subgroup's rows and print the next command (escalation #2538)
      ReadSweep -Collection <name> -Subgroup <name>   the sweep (B4) after the 2.1 rows of a subgroup: the package of its older observations still unmarked, to judge by content; with none left, the sweep is answered as such (escalation #2538)
      RecordSweep -File <answer> [-Check]   check a filled ReadSweep answer whole (keep with its marker, delete_neither or defer, each with its reason), write it, validate the sweep (escalation #2538)
      ReadEvidence -Collection <name> -Subgroup <name>   the evidence validation (B5) after the sweep: the code checks and the package of the next evidence observations not yet read, to judge for truth and coherence (escalation #2538)
      RecordEvidence -File <answer> [-Check]   check a filled ReadEvidence answer whole (true, or repair with the actions of the validation), write it, validate the gate when all is read and the checks pass (escalation #2538)
      ReadElements -Collection <name> -Subgroup <name>   step 3.1 of a subgroup (C1, stage 4): the package of its evidence observations to take up, the older inner-being observations to answer, its verses and meaning by code; opens 3.1 for the subgroup if needed (escalation #2538)
      RecordElements -File <answer> [-Check]   check a filled ReadElements answer whole and write it through the recorder of stage 4; validate the 3.1 row; print the next command (escalation #2538)
      LayerCheck -Collection <name>   validate every answered row against the tables, set validated, write the report; names what is open, failed or missing
      NodeGroups [-Check]   set the group on the live nodes from the collection index
      GroupPull  -Collection <name>   write the working file for grouping the surfaces of a collection by their dictionary meaning (stage 2): one row for each row of the index with the evidence of the
                 Strong's meaning of its codes (#2509)
      GroupRecord -File <filled working file> [-Check]   check the file whole and write the groups (each with the meaning its surfaces share) and the placements in one transaction; a surface whose
                 meaning is not the one the collection gathers is set aside with its reason; writes the scrutiny report
      IndexCheck   the checks of the index (a member with no row, a surface that left, a surface in two collections, duplicates, the split rule, placements, stale shared flags);
                writes a report under surfaces.exports_root (#2503)
      ValidatePull   -Collection <name>   the validation after stage 4 (#2538): the scope of the collection (every live observation related to it: it carries the collection, sits on one of its
                verses, or on a member surface with its lettered Strong's code), the structural tests, a Markdown report and the working file of every in-scope observation to read. Writes no table
      ValidateRecord -File <sheet of actions> [-Check]   check the sheet whole and write its actions in one transaction (set the marker, defer a finding to a named collection, restate, trace, create,
                consume, delete as neither, complete a node, annotate a deleted observation); any problem refuses all of it; -Check runs every action and rolls back
      ValidateCheck  -Collection <name>   the completeness check in two layers, evidence first (the inner-being layer is judged only when the evidence layer passes); names what is open, deferred to a named
                collection, or pending; writes a report. Writes no table
      Set       -Collection <name> -Status indicative|confirmed|retired -Reason <text>   on your instruction
      Merge     -From <name> -Into <name> -Reason <text>   fold one collection into another, on your instruction
      Gather    -Name <name> -Surface <a,b,c> -Reason <text> [-Check]   one collection of the surfaces you name, tier gathered, without the AI; for words in no collection
                that you want assessed together (#2388)
      AttachPhrases   -Reason <text> [-Check]   connect each phrase to the collections of its words (tier phrase), then, for a phrase no word reaches, of its
                own Strong's codes; flag the phrases neither reaches phrase_no_match (#2437)
      Seed      -Word <word>   make a collection of a core word: the AI names its pole (a real word? reciprocal?) and lists synonyms and opposites
      Ask       -Collection <name> [-Limit n]   judge the candidates (the words nearest the core by embedding, and the listed words) through the
                AI client; then run Links. A run of more than a few minutes is started outside the session (B:125).

    Everything is inferential until you confirm it (B:4).

.EXAMPLE
    iba\app\ps\Collection-Build.ps1 -Action Links -Check
.EXAMPLE
    iba\app\ps\Collection-Build.ps1 -Action Show -Collection love
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Status', 'Links', 'Show', 'Export', 'ExportMembers', 'ExportSurfaces', 'Evidence', 'Set', 'Merge', 'Seed', 'Ask', 'Gather', 'AttachPhrases', 'Index', 'Subgroup', 'IndexCheck', 'LayerOpen', 'LayerPull', 'LayerRecord', 'LayerCheck', 'LayerNext', 'ReadWords', 'RecordWords', 'ReadSenses', 'RecordSenses', 'ReadEnrichment', 'RecordEnrichment', 'ReadStructure', 'RecordStructure', 'ReadSweep', 'RecordSweep', 'ReadEvidence', 'RecordEvidence', 'ReadElements', 'RecordElements', 'NodeGroups', 'GroupPull', 'GroupRecord', 'ValidatePull', 'ValidateRecord', 'ValidateCheck')]
    [string] $Action,
    [string[]] $Collection,
    [string] $Verse,
    [string] $Word,
    [string] $Name,
    [string] $Surface,
    [string] $Limit,
    [string] $Status,
    [string] $Reason,
    [string] $From,
    [string] $Into,
    [string] $Strong,
    [string] $Step,
    [string] $Subgroup,
    [string] $Item,
    [string] $File,
    [switch] $Isolate,
    [switch] $Check,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepMap = @{ Status = 'collection.status'; Links = 'collection.links'; Show = 'collection.show'; Export = 'collection.export'; ExportMembers = 'collection.export_members'; ExportSurfaces = 'collection.export_surfaces'; Evidence = 'collection.evidence'; Set = 'collection.set'; Merge = 'collection.merge'; Seed = 'collection.seed'; Ask = 'collection.ask'; Gather = 'collection.gather'; AttachPhrases = 'collection.attach_phrases'; Index = 'collection.index'; Subgroup = 'collection.subgroup'; IndexCheck = 'collection.index_check'; LayerOpen = 'collection.layer_open'; LayerPull = 'collection.layer_pull'; LayerRecord = 'collection.layer_record'; LayerCheck = 'collection.layer_check'; LayerNext = 'collection.layer_next'; ReadWords = 'collection.read_words'; RecordWords = 'collection.record_words'; ReadSenses = 'collection.read_senses'; RecordSenses = 'collection.record_senses'; ReadEnrichment = 'collection.read_enrichment'; RecordEnrichment = 'collection.record_enrichment'; ReadStructure = 'collection.read_structure'; RecordStructure = 'collection.record_structure'; ReadSweep = 'collection.read_sweep'; RecordSweep = 'collection.record_sweep'; ReadEvidence = 'collection.read_evidence'; RecordEvidence = 'collection.record_evidence'; ReadElements = 'collection.read_elements'; RecordElements = 'collection.record_elements'; NodeGroups = 'collection.node_groups'; GroupPull = 'collection.group_pull'; GroupRecord = 'collection.group_record'; ValidatePull = 'collection.validate_pull'; ValidateRecord = 'collection.validate_record'; ValidateCheck = 'collection.validate_check' }
$stepId = $stepMap[$Action]
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-COLLECTIONBUILD"

$paramArgs = @()
foreach ($p in @('Collection', 'Verse', 'Word', 'Name', 'Surface', 'Limit', 'Status', 'Reason', 'From', 'Into', 'Strong', 'Step', 'Subgroup', 'Item', 'File')) {
    if ($PSBoundParameters.ContainsKey($p)) { $paramArgs += @('--param', "$p=$($PSBoundParameters[$p] -join ',')") }
}
if ($Check) { $paramArgs += @('--param', 'Check=true') }
if ($Isolate) { $paramArgs += @('--param', 'Isolate=true') }

Write-IbaRunHeader -WorkPackage 'collection-build' -Step $stepId -RunId $runId
$json = python -m iba.app.run collection-build --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Message $res.message -Code $code
exit $code
