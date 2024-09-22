import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def main():
    print("Starting gardening...")

    current_branch = run_command("git rev-parse --symbolic-full-name --abbrev-ref HEAD")
    print(current_branch)

    new_branch = f"{current_branch}_gardening"
    run_command(f"git checkout -b {new_branch}")

    current_branch = run_command("git rev-parse --symbolic-full-name --abbrev-ref HEAD")
    print(current_branch)

    run_command(f"git push -u origin {current_branch}")

if __name__ == "__main__":
    main()
