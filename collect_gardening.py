import subprocess
import update_gardening

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def main():
    update_gardening.main()
    current_branch = run_command("git rev-parse --symbolic-full-name --abbrev-ref HEAD")
    original_branch = current_branch.replace("_gardening", "")
    num_commits = run_command(f"git rev-list --count {original_branch}..{current_branch}")

    start_date = run_command(f"git log --format='%cd' --reverse --date=short {original_branch}..{current_branch} | head -n 1")
    end_date = run_command(f"git log --format='%cd' --date=short {original_branch}..{current_branch} | head -n 1")

    commit_list = run_command(f"git log --format='- %s by %an' {original_branch}..{current_branch}")

    run_command("gh pr create {original_branch} --head {current_branch} --title “[nit-bot:GARDENING] Gardening nits {start_date} to {end_date}“ --body “Collected the following {num_commits} gardening nit commits since last commit on {end_date}”: {commit_list}”")


if __name__ == "__main__":
    main()
