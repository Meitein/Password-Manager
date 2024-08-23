import json
import sys
import os
import subprocess


def restart_program():
    """Restarts the program."""
    python = sys.executable
    script = os.path.abspath(sys.argv[0])
    subprocess.call([python, script] + sys.argv[1:])
    sys.exit()

def load_passwords():
    """Loads passwords from a JSON file. Returns an empty dictionary if the file is missing or corrupt."""
    try:
        with open('passwords.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_passwords(passwords):
    """Saves passwords to a JSON file."""
    with open('passwords.txt', 'w') as output:
        json.dump(passwords, output, indent=4)


def handle_invalid_input():
    """Prompts the user to restart or exit the program on invalid input."""
    while True:
        choice_to_restart = input('Invalid input. Do you want to restart? ("y" / "n"): ').lower()
        if choice_to_restart == 'y':
            restart_program()
        elif choice_to_restart == 'n':
            sys.exit()
        else:
            print("Please enter 'y' or 'n'.")


def add_password(passwords):
    """Handles adding a new password."""
    website = input('Website: ').strip()
    password = input('Password: ').strip()
    passwords[website] = password
    save_passwords(passwords)
    print('Password added successfully.')


def edit_password(passwords):
    """Handles editing an existing password."""
    website_to_edit = input('Which website password would you like to edit: ').strip()
    if website_to_edit in passwords:
        edited_password = input('Enter the new password: ').strip()
        passwords[website_to_edit] = edited_password
        save_passwords(passwords)
        print(f"Password for {website_to_edit} edited successfully.")
    else:
        print(f"No password found for {website_to_edit}.")


def delete_password(passwords):
    """Handles deleting an existing password."""
    website_to_delete = input('Which website password would you like to delete: ').strip()
    if website_to_delete in passwords:
        del passwords[website_to_delete]
        save_passwords(passwords)
        print(f"Password for {website_to_delete} deleted successfully.")
    else:
        print(f"No password found for {website_to_delete}.")


def main():
    passwords = load_passwords()

    choice = input('"n" = new / "e" = edit / "d" = delete: ').lower()

    if choice == 'n':
        add_password(passwords)
    elif choice == 'e':
        edit_password(passwords)
    elif choice == 'd':
        delete_password(passwords)
    else:
        handle_invalid_input()


if __name__ == "__main__":
    main()