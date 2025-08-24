import subprocess
from datetime import datetime

file_name = "commit.txt"

with open(file_name, "a") as f:
    f.write(f"{datetime.now()}\n")

subprocess.run(["git", "add", file_name])
subprocess.run(["git", "commit", "-m", "Daily update"])
subprocess.run(["git", "push"])
