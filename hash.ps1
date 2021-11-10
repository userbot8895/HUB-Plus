$filetype = "*.py"
$path = "src\"
$path_regex = $path -replace "\\","\\"
echo SHA-1:
((Get-FileHash -Algorithm SHA1 -Path (Get-ChildItem $filetype -Recurse)) -replace $path_regex,"") -replace "@{Algorithm=SHA1; Hash=","" -replace "; Path="," " -replace "}",""
echo ""
echo MD5:
((Get-FileHash -Algorithm MD5 -Path (Get-ChildItem $filetype -Recurse)) -replace $path_regex,"") -replace "@{Algorithm=MD5; Hash=","" -replace "; Path="," " -replace "}",""