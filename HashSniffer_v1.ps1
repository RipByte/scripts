function Get-HashRecursively {
    param(
        [string]$Path
    )
    $items = Get-ChildItem -Path $Path

    foreach ($item in $items) {
        if ($item -is [System.IO.DirectoryInfo]) {
            
            Get-HashRecursively -Path $item.FullName
        }
        elseif ($item -is [System.IO.FileInfo]) {
            $hash = Get-FileHash -Path $item.FullName -Algorithm SHA256
            Write-Host "File: $($item.FullName), Hash: $($hash.Hash)"
        }
    }
}

Get-HashRecursively -Path "C:\Users\RipTide\Downloads\Install Termius"