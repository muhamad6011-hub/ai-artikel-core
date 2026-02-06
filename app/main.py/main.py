$folders = Get-ChildItem -Directory -Filter "artikel-*"
$output = "dataset-ai.txt"

"" | Out-File $output -Encoding utf8

foreach ($folder in $folders) {
    $file = Join-Path $folder.FullName "artikel.txt"
    if (Test-Path $file) {
        Get-Content $file | Add-Content $output
        "`n---`n" | Add-Content $output
    }
}
