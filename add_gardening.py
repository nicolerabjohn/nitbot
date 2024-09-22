import subprocess
import update_gardening

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def add_gardening(commit_tag_or_hash):
    update_gardening.main()

    if run_command(f"git cat-file -t {commit_tag_or_hash}") == "commit":
        commit_hash = commit_tag_or_hash
    else:
        commit_hash = run_command(f"git show-ref -s {commit_tag_or_hash}")

    run_command(f"git cherry-pick {commit_hash}")

    if "CONFLICT" in run_command("git status"):
        print("Merge conflict detected.")
        confirmation = input("Do you want to continue? [Y / N]: ").strip().lower()
        if confirmation in ["y", "yes"]:
            print("Please resolve the conflict and commit.")
        else:
            print("Aborting cherry-pick.")
            run_command("git cherry-pick --abort")
            return

    run_command(f"git push origin <base branch>/gardening")

def main():
    current_branch = run_command("git rev-parse --symbolic-full-name --abbrev-ref HEAD")
    commit_tag_or_hash = input("Enter the commit tag or hash to add to gardening: ")
    add_gardening(commit_tag_or_hash)

if __name__ == "__main__":
    main()

