import subprocess
import update_gardening

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def main():
    update_gardening.main()
    current_branch = run_command("git rev-parse --symbolic-full-name --abbrev-ref HEAD")
    original_branch = current_branch.replace("_gardening", "")

    branch_exists = run_command(f"git branch --list {original_branch}")

    num_commits = run_command(f"git rev-list --count {original_branch}..{current_branch}")
    start_date = run_command(f"git log --format='%cd' --reverse --date=short {original_branch}..{current_branch} | head -n 1")
    end_date = run_command(f"git log --format='%cd' --date=short {original_branch}..{current_branch} | head -n 1")
    commit_list = run_command(f"git log --format='- %h: %s by %an' {original_branch}..{current_branch}")

    print(f"Creating PR from {current_branch} to {original_branch}")

    run_command(f'gh pr create --head {current_branch} --base {original_branch} '
                f'--title "[nit-bot:GARDENING] Gardening nits {start_date} to {end_date}" '
                f'--body "Collected the following {num_commits} gardening nit commits since last commit on {end_date}:\n{commit_list}"')

if __name__ == "__main__":
    main()

