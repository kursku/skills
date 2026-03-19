param(
    [string]$InstalledRoot = "$HOME/.claude/skills",
    [string]$RepoRoot = (Get-Location).Path,
    [string]$SummaryPath = ".skill_coverage_summary.json",
    [string]$MissingPath = ".missing_in_repo.txt",
    [string]$ExtraPath = ".extra_in_repo.txt"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $InstalledRoot)) {
    Write-Host "installed-root-missing:$InstalledRoot"
    exit 1
}

$repoFiles = Get-ChildItem $RepoRoot -Recurse -File -Filter "SKILL.md"
$installedFiles = Get-ChildItem $InstalledRoot -Recurse -File -Filter "SKILL.md"

function Get-SkillName([string]$filePath) {
    $firstNameLine = Get-Content $filePath -TotalCount 80 |
        Where-Object { $_ -match '^name:\s*(.+)$' } |
        Select-Object -First 1

    if (-not $firstNameLine) {
        return $null
    }

    return ($firstNameLine -replace '^name:\s*', '').Trim().Trim('"')
}

$repoNames = New-Object System.Collections.Generic.HashSet[string]
foreach ($f in $repoFiles) {
    $name = Get-SkillName $f.FullName
    if ($name) {
        [void]$repoNames.Add($name)
    }
}

$installedNames = New-Object System.Collections.Generic.HashSet[string]
foreach ($f in $installedFiles) {
    $name = Get-SkillName $f.FullName
    if ($name) {
        [void]$installedNames.Add($name)
    }
}

$repoSet = $repoNames.ToArray() | Sort-Object -Unique
$installedSet = $installedNames.ToArray() | Sort-Object -Unique

$missingInRepo = $installedSet | Where-Object { $_ -notin $repoSet }
$extraInRepo = $repoSet | Where-Object { $_ -notin $installedSet }

$summary = [pscustomobject]@{
    installedSkillFiles = $installedFiles.Count
    repoSkillFiles = $repoFiles.Count
    installedUniqueNames = $installedSet.Count
    repoUniqueNames = $repoSet.Count
    installedNamesMissingInRepo = $missingInRepo.Count
    repoNamesNotInInstalled = $extraInRepo.Count
}

$summary | ConvertTo-Json | Set-Content $SummaryPath
$missingInRepo | Set-Content $MissingPath
$extraInRepo | Set-Content $ExtraPath

Write-Host ($summary | ConvertTo-Json)
