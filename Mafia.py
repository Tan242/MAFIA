import os
import shutil
import subprocess

# Define the repository and directory
repo_url = "https://github.com/MAFIA-177/MAFIA"
dir_name = "MAFIA"

# Remove the directory if it exists
if os.path.exists(dir_name):
    shutil.rmtree(dir_name)

# Clone the repository
subprocess.run(["git", "clone", repo_url])

# Change directory
os.chdir(dir_name)

# Change permissions of the MAFIA file
subprocess.run(["chmod", "777", "Mafia"])

# Execute the MAFIA file
subprocess.run(["./Mafia"])
