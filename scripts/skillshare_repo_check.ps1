param(
    [switch]$WriteIndex,
    [switch]$Strict
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$excludedRootFolders = @(
    ".git",
    ".system",
    "docs",
    "scripts"
)

$approvedGroupFolders = @(
    "core",
    "frontend",
    "backend",
    "data-ai",
    "security",
    "workflow",
    "tooling",
    "_experimental"
)

$skillFiles = Get-ChildItem -Path $repoRoot -Recurse -File -Filter "SKILL.md" | Where-Object {
    $relativePath = $_.FullName.Substring($repoRoot.Length).TrimStart([char[]]"\\/")
    $segments = $relativePath -split '[\\/]'

    if ($segments.Count -lt 2 -or $segments.Count -gt 3) {
        return $false
    }

    $firstSegment = $segments[0]
    if ($firstSegment -in $excludedRootFolders) {
        return $false
    }

    if ($segments.Count -eq 3 -and $firstSegment -notin $approvedGroupFolders) {
        return $false
    }

    return $true
}

$results = @()
$errors = @()

foreach ($skill in $skillFiles) {
    $skillDir = Split-Path -Parent $skill.FullName
    $relativeDir = $skillDir.Substring($repoRoot.Length).TrimStart([char[]]"\\/")
    $segments = $relativeDir -split '[\\/]'
    $group = if ($segments.Count -gt 1) { $segments[0] } else { "ungrouped" }
    $skillName = $segments[-1]

    $skillFile = $skill.FullName
    $metaFile = Join-Path $skillDir ".skillshare-meta.json"

    $lines = Get-Content -Path $skillFile

    $frontmatterName = $null
    $frontmatterDescription = $null
    $hasFrontmatter = $false
    $inDescriptionBlock = $false

    if ($lines.Count -ge 3 -and $lines[0].Trim() -eq "---") {
        $hasFrontmatter = $true
        for ($i = 1; $i -lt $lines.Count; $i++) {
            $line = $lines[$i].Trim()
            if ($line -eq "---") {
                break
            }

            if ($inDescriptionBlock) {
                if ($line -match "^[a-zA-Z0-9_-]+:\s*") {
                    $inDescriptionBlock = $false
                }
                elseif (-not [string]::IsNullOrWhiteSpace($line)) {
                    if ([string]::IsNullOrWhiteSpace($frontmatterDescription)) {
                        $frontmatterDescription = $line
                    }
                    else {
                        $frontmatterDescription = "$frontmatterDescription $line"
                    }
                    continue
                }
            }

            if ($line -match "^name:\s*(.+)$") {
                $frontmatterName = $Matches[1].Trim().Trim('"', "'")
            }
            if ($line -match "^description:\s*(.+)$") {
                $frontmatterDescription = $Matches[1].Trim().Trim('"', "'")
            }
            elseif ($line -eq "description:") {
                $inDescriptionBlock = $true
            }
        }
    }

    $metaValid = $false
    if (Test-Path $metaFile) {
        try {
            $null = Get-Content -Path $metaFile -Raw | ConvertFrom-Json
            $metaValid = $true
        }
        catch {
            $errors += "Invalid JSON in $relativeDir/.skillshare-meta.json"
        }
    }

    if (-not $hasFrontmatter) {
        $errors += "Missing frontmatter in $relativeDir/SKILL.md"
    }
    if ([string]::IsNullOrWhiteSpace($frontmatterName)) {
        $errors += "Missing frontmatter name in $relativeDir/SKILL.md"
    }
    if ([string]::IsNullOrWhiteSpace($frontmatterDescription)) {
        $errors += "Missing frontmatter description in $relativeDir/SKILL.md"
    }

    $results += [pscustomobject]@{
        group = $group
        folder = $skillName
        path = $relativeDir
        skill_file = "$relativeDir/SKILL.md"
        name = $frontmatterName
        has_description = -not [string]::IsNullOrWhiteSpace($frontmatterDescription)
        has_meta = (Test-Path $metaFile)
        meta_valid = $metaValid
    }
}

$results = $results | Sort-Object group, folder

Write-Host "Detected skills:" $results.Count
if ($errors.Count -eq 0) {
    Write-Host "Validation: PASS"
}
else {
    Write-Host "Validation: FAIL ($($errors.Count) issue(s))"
    $errors | ForEach-Object { Write-Host " - $_" }
}

if ($WriteIndex) {
    $indexPath = Join-Path $repoRoot "docs/skillshare-skills.json"
    $payload = [pscustomobject]@{
        generated_at = (Get-Date).ToString("o")
        total_skills = $results.Count
        skills = $results
    }

    $payload | ConvertTo-Json -Depth 8 | Set-Content -Path $indexPath
    Write-Host "Wrote index:" $indexPath
}

if ($Strict -and $errors.Count -gt 0) {
    exit 1
}
