param(
    [string]$GlobalRoot = "$env:APPDATA/skillshare/skills",
    [string]$RepoRoot = (Get-Location).Path,
    [string]$OutDir = "docs"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $GlobalRoot)) {
    Write-Host "global-root-missing:$GlobalRoot"
    exit 1
}

if (-not (Test-Path $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir | Out-Null
}

function Get-SkillName([string]$filePath) {
    $firstNameLine = Get-Content $filePath -TotalCount 100 |
        Where-Object { $_ -match '^name:\s*(.+)$' } |
        Select-Object -First 1

    if (-not $firstNameLine) {
        return $null
    }

    return ($firstNameLine -replace '^name:\s*', '').Trim().Trim('"')
}

$repoFiles = Get-ChildItem $RepoRoot -Recurse -File -Filter "SKILL.md" | Where-Object {
    $_.FullName -notmatch "\\.git\\"
}

$globalFiles = Get-ChildItem $GlobalRoot -Recurse -File -Filter "SKILL.md"

$repoByName = @{}
foreach ($f in $repoFiles) {
    $name = Get-SkillName $f.FullName
    if (-not $name) { continue }

    if (-not $repoByName.ContainsKey($name)) {
        $repoByName[$name] = New-Object System.Collections.Generic.List[string]
    }

    $repoByName[$name].Add($f.FullName)
}

$globalByName = @{}
foreach ($f in $globalFiles) {
    $name = Get-SkillName $f.FullName
    if (-not $name) { continue }

    if (-not $globalByName.ContainsKey($name)) {
        $globalByName[$name] = New-Object System.Collections.Generic.List[string]
    }

    $globalByName[$name].Add($f.FullName)
}

$repoNames = $repoByName.Keys | Sort-Object -Unique
$globalNames = $globalByName.Keys | Sort-Object -Unique

$presentNames = $globalNames | Where-Object { $_ -in $repoNames } | Sort-Object -Unique
$missingNames = $globalNames | Where-Object { $_ -notin $repoNames } | Sort-Object -Unique

$presentPath = Join-Path $OutDir "global-skillshare-in-repo.txt"
$missingPath = Join-Path $OutDir "global-skillshare-missing-in-repo.txt"
$missingWithPathsPath = Join-Path $OutDir "global-skillshare-missing-with-source-paths.csv"
$summaryPath = Join-Path $OutDir "global-skillshare-coverage-summary.json"

$presentNames | Set-Content $presentPath
$missingNames | Set-Content $missingPath

$missingRows = foreach ($name in $missingNames) {
    foreach ($path in $globalByName[$name]) {
        [pscustomobject]@{
            skill_name = $name
            source_skill_md = $path
        }
    }
}
$missingRows | Export-Csv -Path $missingWithPathsPath -NoTypeInformation -Encoding UTF8

$summary = [pscustomobject]@{
    generated_at = (Get-Date).ToString("o")
    global_root = $GlobalRoot
    repo_root = $RepoRoot
    global_skill_files = $globalFiles.Count
    repo_skill_files = $repoFiles.Count
    global_unique_skill_names = $globalNames.Count
    repo_unique_skill_names = $repoNames.Count
    present_in_repo = $presentNames.Count
    missing_in_repo = $missingNames.Count
}

$summary | ConvertTo-Json | Set-Content $summaryPath

Write-Host ($summary | ConvertTo-Json)
Write-Host "wrote:$summaryPath"
Write-Host "wrote:$presentPath"
Write-Host "wrote:$missingPath"
Write-Host "wrote:$missingWithPathsPath"
