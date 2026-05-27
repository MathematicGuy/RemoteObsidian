---
category: "3 RESOURCES/How to/How to Enable Group Policy Editor in Windows 11 Home Edition.md"
summary: "This system administration guide explains how to activate the Group Policy Editor utility on Windows 11 Home Edition. It provides a batch script utilizing deployment image servicing commands to install missing policy packages."
keywords: []
confidence: "high"
analyzed_at: "2026-05-27T17:32:07.272430+00:00"
---
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