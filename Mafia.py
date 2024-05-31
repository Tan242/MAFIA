import os
import shutil
import subprocess

# Import the 'this' module (the Zen of Python)
import this

# Define the repository and directory
repo_url = "https://github.com/MAFIA-177/MAFIA"
dir_name = "MAFIA"

# Remove the directory if it exists
if os.path.exists(dir_name):
    shutil.rmtree(dir_name)

# Clone the repository
subprocess.run(["git", "clone", repo_url])

# Change directory to the cloned repository
os.chdir(dir_name)

# List files in the directory (for debugging purposes)
print("Files in directory:", os.listdir())

# If there is a file named 'Mafia' and it needs to be executable, change its permissions
if os.path.exists("Mafia"):
    subprocess.run(["chmod", "777", "Mafia"])

# Execute the Mafia.py script using Python
subprocess.run(["python", "Mafia.py"])
