Write-Host "🔄 Building dataset-ai.txt..."

$basePath = "C:\AI-ARTIKEL"
$outputFile = "$basePath\dataset-ai.txt"

if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

Get-ChildItem -Path $basePath -Directory -Filter "artikel-*" | ForEach-Object {
    $file = Join-Path $_.FullName "artikel.txt"
    if (Test-Path $file) {
        Add-Content -Path $outputFile -Value "`n### $($_.Name)`n"
        Get-Content $file | Add-Content -Path $outputFile
    }
}

Write-Host "✅ dataset-ai.txt selesai dibuat"
