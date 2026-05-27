1) Add activation command to your notepad
```txt
@echo off

pushd "%~dp0"

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"

pause
```

2) Choose "Save As" and save your note as "GroupPolicy.bat" to a folder
3) Run  "GroupPolicy.bat" as Administrators, wait for it to download 
4) "Ctr + R" > write "gedit.msc" then hit Enter