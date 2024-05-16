param(
    [string]$Path
)


if($Path){
    Write-Host "Retriving hash from: $Path"
    Get-ChildItem $Path
}
else {
    Write-Host "PATH specified does not exists!"
}