import subprocess

def run_command(base_command, option):
    try:
        full_command = f"{base_command} {option}"
        result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print("Command Output:\n", result.stdout)
        
        if result.stderr:
            print("Error Output:\n", result.stderr)
            
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        print(f"Error Output: {e.stderr}")

base_command = "nmap -sV "

option = input("Enter target IP address : ")

run_command(base_command, option)