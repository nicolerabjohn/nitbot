import subprocess
import init_gardening

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def main():
    current_branch = run_command("git rev-parse --symbolic-full-name --abbrev-ref HEAD")
    if not current_branch.endswith("_gardening"):
        init_gardening.main()

    run_command("git add .")
    run_command("git commit -m 'Update gardening'")
    run_command("git push")

    result = subprocess.run("git pull --rebase origin main)", shell=True, capture_output=True, text=True)
    print(result.stdout)

    if result.returncode > 0:
        bad_commit_hash = run_command("git rev-parse HEAD")
        
        with open(f"{bad_commit_hash}.diff", "w") as diff_file:
            diff_output = run_command(f"git diff {bad_commit_hash}^ {bad_commit_hash}")
            diff_file.write(diff_output)

        # Remove the bad commit
        run_command("git rebase --abort")
        print(f"Rebase failed. The bad commit has been saved as {bad_commit_hash}.diff")

if __name__ == "__main__":
    main()
