# Get the network adapter that is currently connected
$network = Get-NetConnectionProfile

# Check if the network is already set to Private
if ($network.NetworkCategory -ne "Private") {
    # Set the network profile to Private
    Set-NetConnectionProfile -InterfaceIndex $network.InterfaceIndex -NetworkCategory Private
    Write-Output "Network profile switched to Private."
} else {
    Write-Output "Network profile is already set to Private."
}