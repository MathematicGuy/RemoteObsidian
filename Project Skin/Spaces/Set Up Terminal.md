
Fav theme
![[Pasted image 20240601234808.png]]

0) **Get Theme**
```bash
Get-PoshThemes
```
Active file 
note: pwsh is powershell in short

**Active Theme**
oh-my-posh init pwsh --config "jandedobbeleer" | Invoke-Expression

```bashnote
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/illusi0n.omp.json" | Invoke-Expression

oh-my-posh init pwsh --config "emodipt-extend" | Invoke-Expression
```
huvix.omp.jsone
```
winget upgrade JanDeDobbeleer.OhMyPosh -s winget
```
kali.omp.json
zash.omp.json
tokyonight_storm.omp.json
the-unnamed.omp.json
star.omp.json
smoothie.omp.json
sim-web.omp.json
robbyrussell.omp.json
patriksvensson.omp.json
pararussel.omp.json
neko.omp.json
negligible.omp.json
emodipt-extend.omp.jsone\emodipt-extende]8;;e\

+ @ Basically *Create Profile -> add "oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\negligible.omp.json" | Invoke-Expression" to the profile -> Save profile.*
1) **Get Profile**
```bash
notepad $PROFILE
```
Create profile if not have 1 already
```sh
if (!(Test-Path -Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
```

> Put this in notepad profile file -> save file - close file
```bash
oh-my-posh init pwsh | Invoke-Expression
"or"
oh-my-posh init powershell | Invoke-Expression
```

2) (Optional) Get Profile Path
```bash
New-Item -Path $PROFILE -Type File -Force
```
Ex: 
```bash
C:\Users\boboi\OneDrive - CMC University\Documents\WindowsPowerShell
```

**2.1) Add the path to your profile***
*Microsoft.PowerShell_profile.ps1*
```bash
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\negligible.omp.json" | Invoke-Expression
```

3) **Save the Profile**
```bash
. $PROFILE
```




```sh
# Load Oh My Posh theme
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\illusi0n.omp.json" | Invoke-Expression

# Optional: Enable history-based suggestions
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle InlineView
Set-PSReadLineOption -Colors @{ "InlinePrediction" = [ConsoleColor]::DarkGray }
```