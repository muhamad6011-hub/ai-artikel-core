Write-Host "🚀 Auto push ke GitHub..."

git add .
git commit -m "auto update dataset" -ErrorAction SilentlyContinue
git push origin main

Write-Host "✅ Push selesai"