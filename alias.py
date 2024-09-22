import os

def add_alias(alias_name, command):
    alias_command = f"alias {alias_name}='python3 {command}'\n"
    return alias_command

def main():
    aliases = [
        add_alias('nit-update-gardening', 'update_gardening.py'),
        add_alias('nit-init-gardening', 'init_gardening.py'),
        add_alias('nit-branches', 'branches.py'),
        add_alias('nit-collect-gardening', 'collect_gardening.py'),
        add_alias('nit-add-gardening', 'add_gardening.py'),
    ]

    bashrc_path = os.path.expanduser('~/.bashrc')
    with open(bashrc_path, 'a') as bashrc_file:
        bashrc_file.write('\n')  # Ensure there is a newline before appending aliases
        bashrc_file.writelines(aliases)

    print("Bash aliases added. Please restart your terminal or run 'source ~/.bashrc' to apply them.")

if __name__ == "__main__":
    main()

