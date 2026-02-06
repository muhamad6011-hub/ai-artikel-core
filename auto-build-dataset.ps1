# AUTO PUSH AI ARTIKEL KE GITHUB

$projectPath = "C:\AI-ARTIKEL"

Set-Location $projectPath

Write-Host "Build dataset AI..."
.\auto-build-dataset.ps1

Write-Host "Git add..."
git add .

$time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMsg = "update dataset ai - $time"

Write-Host "Git commit..."
git commit -m "$commitMsg"

Write-Host "Git push ke GitHub..."
git push origin main

Write-Host "Selesai. Semua sudah terupdate."
