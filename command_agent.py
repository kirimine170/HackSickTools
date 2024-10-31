import subprocess

class CommandAgent():
    @staticmethod
    def run_command(base_command, option):
        try:
            full_command = f"{base_command} {option}"
            result = subprocess.run(full_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            return "", f"Command failed with error: {e.stderr}"