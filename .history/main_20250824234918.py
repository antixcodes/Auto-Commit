import subprocess
from datetime import datetime

# File to update
file_name = "commit.txt"

# Append the current date to the file
with open(file_name, "a") as f:
    f.write(f"{datetime.now()}\n")

# Git commands
subprocess.run(["git", "add", file_name])
subprocess.run(["git", "commit", "-m", "Daily update"])
subprocess.run(["git", "push"])
