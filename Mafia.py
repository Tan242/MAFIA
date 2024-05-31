import os
import shutil
import subprocess

# Import the 'this' module to print the Zen of Python
import this

# Define the repository URL and directory name
repo_url = "https://github.com/MAFIA-177/MAFIA"
dir_name = "MAFIA"

# Function to remove directory if it exists
def remove_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Removed existing directory: {path}")

# Function to clone the repository
def clone_repository(url, path):
    result = subprocess.run(["git", "clone", url], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Cloned repository into: {path}")
    else:
        print(f"Failed to clone repository: {result.stderr}")

# Function to change file permissions
def change_permissions(file, mode):
    if os.path.exists(file):
        subprocess.run(["chmod", mode, file])
        print(f"Changed permissions for: {file} to {mode}")

# Function to execute a Python script
def execute_script(script):
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Executed script: {script}")
        print(result.stdout)
    else:
        print(f"Failed to execute script: {script}")
        print(result.stderr)

# Main process
remove_directory(dir_name)
clone_repository(repo_url, dir_name)
os.chdir(dir_name)

# List files in the directory (for debugging purposes)
print("Files in directory:", os.listdir())

# Change permissions for the 'Mafia' file if it exists
change_permissions("Mafia", "777")

# Execute the Mafia.py script
execute_script("Mafia.py")
