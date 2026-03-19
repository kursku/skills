param(
    [string]$CsvPath = "docs/global-skillshare-missing-with-source-paths.csv",
    [string]$TargetBase = "packs/global-skillshare-import/wave-001",
    [int]$Limit = 100,
    [string]$ReportPrefix
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $CsvPath)) {
    Write-Host "missing-csv:$CsvPath"
    exit 1
}

if (-not (Test-Path $TargetBase)) {
    New-Item -ItemType Directory -Path $TargetBase -Force | Out-Null
}

if ([string]::IsNullOrWhiteSpace($ReportPrefix)) {
    $leaf = Split-Path -Leaf $TargetBase
    $ReportPrefix = "global-skillshare-import-$leaf"
}

$rows = Import-Csv -Path $CsvPath | Select-Object -First $Limit
$imported = New-Object System.Collections.Generic.List[string]
$skipped = New-Object System.Collections.Generic.List[string]

foreach ($row in $rows) {
    $skillName = $row.skill_name
    $skillMdPath = $row.source_skill_md

    if (-not (Test-Path $skillMdPath)) {
        $skipped.Add("missing-source:$skillName")
        continue
    }

    $sourceDir = Split-Path -Parent $skillMdPath
    $targetDir = Join-Path $TargetBase $skillName

    $suffix = 1
    while (Test-Path $targetDir) {
        $targetDir = Join-Path $TargetBase ("{0}__{1}" -f $skillName, $suffix)
        $suffix++
    }

    Copy-Item -Path $sourceDir -Destination $targetDir -Recurse -Force
    $imported.Add($targetDir)
}

$report = [pscustomobject]@{
    imported_count = $imported.Count
    skipped_count = $skipped.Count
    target_base = (Resolve-Path $TargetBase).Path
}

$reportPath = "docs/$ReportPrefix-report.json"
$importListPath = "docs/$ReportPrefix-imported.txt"
$skippedPath = "docs/$ReportPrefix-skipped.txt"

$report | ConvertTo-Json | Set-Content $reportPath
$imported | Set-Content $importListPath
$skipped | Set-Content $skippedPath

Write-Host ($report | ConvertTo-Json)
Write-Host "wrote:$reportPath"
Write-Host "wrote:$importListPath"
Write-Host "wrote:$skippedPath"
