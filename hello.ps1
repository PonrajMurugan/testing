Write-Host '====================================='
Write-Host '  Hello from a POWERSHELL script (via Fluwent)'
Write-Host '====================================='
Write-Host ''
Write-Host "Host:        $env:COMPUTERNAME"
Write-Host "User:        $env:USERNAME"
Write-Host "OS:          $([System.Environment]::OSVersion.VersionString)"
Write-Host "PSVersion:   $($PSVersionTable.PSVersion)"
Write-Host "Date:        $(Get-Date -Format o)"
Write-Host ''
Write-Host 'Arguments received:'
for ($i = 0; $i -lt $args.Count; $i++) {
    Write-Host "  args[$($i + 1)] = $($args[$i])"
}
Write-Host ''
Write-Host 'Status: SUCCESS'
