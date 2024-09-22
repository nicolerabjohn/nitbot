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
    print("Hello")
    run_command("git pull --rebase origin main")
        

if __name__ == "__main__":
    main()
