Get-ChildItem -Recurse -Filter artikel.txt |
ForEach-Object {
    [System.IO.File]::ReadAllText($_.FullName)
} |
Out-File dataset-ai.txt -Encoding utf8