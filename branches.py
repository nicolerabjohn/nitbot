import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def main():
    print("Checking on the status of branches...")

    branches = run_command("git branch -vv | grep gardening")
    print(branches)

if __name__ == "__main__":
    main()
