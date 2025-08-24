import subprocess, time
from datetime import datetime
from colorama import Fore, Style

def git(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    return result.stdout.strip()

while True:
    with open("commit.txt", "a") as f:
        f.write(f"{datetime.now()}\n")

    print(Fore.CYAN + "[+] Staging changes..." + Style.RESET_ALL)
    git(f"git add {'commit.txt'}")

    commit_message = "Daily update"
    print(Fore.GREEN + f"[+] Committing changes: {commit_message}" + Style.RESET_ALL)
    git(f'git commit -m "{commit_message}"')

    print(Fore.YELLOW + "[+] Pulling latest changes..." + Style.RESET_ALL)
    git("git pull origin main --rebase --autostash")

    print(Fore.MAGENTA + "[-] Pushing changes..." + Style.RESET_ALL)
    git("git push origin main")

    print(Fore.BLUE + "[+] Done" + Style.RESET_ALL)
    print(Fore.BLUE + "[*] Will Commit after 1 day..." + Style.RESET_ALL)
    time.sleep(86400)