"""
Author: Sebastian Lorensson Date: 2024-12-20 License: MIT
Lab4 DV1574 - File Safe

Laboration 4 in the course DV1574 : Introduction to Programming with Python.

Instructions:
- Run the program
- Use the main menu to create, select, or remove folders
- Use the file menu to create, read, append to, edit, or remove files
- Files are encrypted using a key stored in a hidden file
- The program will return to the main menu after each file operation
"""

import os
import time  # for sleep

# https://pypi.org/project/cryptography/
import cryptography
from cryptography.fernet import Fernet as fnt
import cryptography.fernet


# https://geeksforgeeks.org/error-handling-in-python-using-decorators/
# decorator for error handling, cleans up code
def error_decorator(func):
    """Decorator for error handling"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (FileNotFoundError, OSError, TypeError, ValueError, RuntimeError) as e:
            print(f"An error occurred in {func.__name__}: {e}")
            raise

    return wrapper


@error_decorator
class Safe:
    """Safe class for storing encryption key
    and encrypting/decrypting data"""

    KEY_FILE = "key.key"

    def __init__(self):
        """load key from file or generate new key"""
        try:
            self.key = self.load_key(self.KEY_FILE)
        except FileNotFoundError:
            self.key = self.generate_key()

    def generate_key(self):
        """Generate key, save to file"""
        gen_key = fnt.generate_key()
        self.save_key(gen_key)
        if gen_key is None:
            raise RuntimeError("Could not generate key.")
        return gen_key

    def save_key(self, key):
        """save key"""
        try:
            with open(self.KEY_FILE, "wb") as key_file:
                key_file.write(key)
        except FileExistsError:
            raise FileExistsError("Key file already exists.")

    def load_key(self, path):
        """load key"""
        if os.path.exists(path):
            with open(path, "rb") as key_file:
                return key_file.read()
        else:
            raise FileNotFoundError("Key file not found.")

    def encrypt(self, text):
        """encrypt text using key"""
        cipher = fnt(self.key)
        encrypted_bytes = cipher.encrypt(text.encode())
        return encrypted_bytes.decode("utf-8")

    def decrypt(self, text):
        """decrypt text using key"""
        try:
            cipher = fnt(self.key)
            decrypted_bytes = cipher.decrypt(text.encode())
            return decrypted_bytes.decode("utf-8")
        except cryptography.fernet.InvalidToken as e:
            raise ValueError(f"Could not decrypt file content: {e}")


@error_decorator
class FileSafe:
    """
    Main file safe class for handling encrypted file operations.

    The class has methods for creating, reading, appending to,
    editing, and removing files in a selected folder.

    uses the Safe class to encrypt and decrypt files
    """

    MAIN_MENU_CHOICES = ("0", "1", "2", "3")
    FILE_MENU_CHOICES = ("1", "2", "3", "4", "5")

    def __init__(self):
        """
        Constructor
        """
        self.wd = os.getcwd()
        self.safe = Safe()

    # helper methods
    def cwd_has_files(self):
        """Check if current working folder has files"""
        return any(os.path.isfile(f) for f in os.listdir())

    def print_cwd_folders(self):
        """Print all folders in the current working folder"""
        print(os.getcwd().split("\\")[-1].capitalize(), "folders:")
        print("-" * 40)
        for folder in os.listdir():
            if os.path.isdir(folder) and folder != "__pycache__":
                print("+", folder)
        print("-" * 40)

    def print_cwd_files(self):
        """Print all files in the current working folder"""
        print("Files in current working folder:")
        for file in os.listdir():
            if os.path.isfile(file):
                print(file)

    def print_main_menu(self):
        """Print main menu options"""
        print("Folder options:")
        print("  (1) Create new folder")
        print("  (2) Select work folder")
        print("  (3) Remove existing folder")
        print("  (0) Exit program")

    def print_file_menu(self):
        """Print file menu options"""
        print("File options:")
        print("  (1) Create file")
        print("  (2) Read file")
        print("  (3) Append to file")
        print("  (4) Remove file")
        print("  (5) Return to main menu")

    def multi_line_input(self, prompt):
        """
        function to enable multi-line input

        prompts the user, then collects input line until input is empty
        """
        lines = []
        done = False
        try:
            print(prompt)
            while not done:
                line = input()
                if line == "ESC":
                    done = True
                elif lines:
                    lines.append("\n" + line)
                else:
                    lines.append(line)
            return "".join(lines)
        except Exception as e:
            print(f"An error occurred in multi_line_input: {e}")
            return []

    # MAIN PROGRAM
    def run(self):
        """Start program loop"""
        os.system("cls")
        print("Welcome to File Safe!\n")
        print("This program allows you to write and encrypted files.")
        print("First you must create a working folder or select ")
        print("an existing one, then you can create or read files.\n")
        input("To continue, press enter...")

        # start program loop
        running = True
        while running:
            running = not self.main_menu()  # main menu returns True if exit

    # menu loop methods
    def main_menu(self):
        """
        print menu and takes input until valid choice is made
        """
        os.chdir(self.wd)
        os.system("cls")
        print("Main menu...")
        print("Current folder:", self.wd)
        choices = self.MAIN_MENU_CHOICES
        print_menu = self.print_main_menu

        choice = self.validate_choice(choices, print_menu)
        exit = self.main_menu_action(choice)

        return exit

    # menu action methods
    def validate_choice(self, ok_list, print_menu):
        """Validate user input against a list of valid choices"""
        os.system("cls")

        choice = ""
        done = False
        while not done:
            print_menu()
            sel_range = f"{ok_list[0]}-{ok_list[-1]}"
            choice = input(f"Make selection ({sel_range}): ")
            if choice in ok_list:
                done = True
            else:
                print("Invalid choice, try again.")
                time.sleep(0.75)
                os.system("cls")
        return choice

    # main menu actions
    def main_menu_action(self, choice):
        """Main menu actions"""
        exit = False
        if choice == self.MAIN_MENU_CHOICES[0]:
            exit = True
        elif choice == self.MAIN_MENU_CHOICES[1]:
            self.create_folder()
        elif choice == self.MAIN_MENU_CHOICES[2]:
            self.select_folder()
        elif choice == self.MAIN_MENU_CHOICES[3]:
            self.remove_folder()
        return exit

    def create_folder(self):
        """Create a folder in the current working folder"""
        print("Enter folder name to create: ")
        folder_name = input()

        try:
            if os.path.exists(folder_name):
                print("Folder already exists.")
                time.sleep(0.75)
            else:
                os.makedirs(folder_name)
                print(f'Folder "{folder_name}" created successfully.')
                time.sleep(0.75)
        except OSError as e:
            print(f"An error occurred in create_folder: {e}")
            time.sleep(0.75)

    def select_folder(self):
        """Change cwd to selected folder"""
        self.print_cwd_folders()
        folder_name = input("Folder to select: ")
        if os.path.exists(folder_name):
            print("Folder selected:", folder_name)
            os.chdir(folder_name)
            self.file_menu()
            time.sleep(0.75)
            return True
        else:
            print("Cannot select, folder does not exist.")
            print("Returning to main menu...")
            time.sleep(0.75)
            return False

    def remove_folder(self):
        """Remove a folder from the current working folder"""
        self.print_cwd_folders()
        folder_name = input("Folder to delete: ")

        if os.path.exists(folder_name):
            if not os.listdir(folder_name):
                os.rmdir(folder_name)
                print("Folder removed successfully.")
                time.sleep(0.75)
                return True
            else:
                print("Folder is not empty. Remove files first.")
                time.sleep(0.75)
                return False
        else:
            print("Folder does not exist.")
            time.sleep(0.75)
            return False

    def file_menu(self):
        """File menu loop"""
        os.system("cls")
        go_back = False
        choices = self.FILE_MENU_CHOICES
        print_menu = self.print_file_menu

        while go_back is False:
            print("Current folder:", end=" ")
            print(os.getcwd().split("\\")[-1])
            choice = self.validate_choice(choices, print_menu)
            go_back = self.file_menu_action(choice)

    # file menu actions
    def file_menu_action(self, choice):
        """File menu actions"""
        exit = False

        if choice == self.FILE_MENU_CHOICES[-1]:
            os.chdir(self.wd)
            print("Returning to main menu...")
            exit = True
            time.sleep(0.75)
        elif choice == self.FILE_MENU_CHOICES[0]:
            self.create_file()
        elif choice == self.FILE_MENU_CHOICES[1]:
            self.read_file()
        elif choice == self.FILE_MENU_CHOICES[2]:
            self.append_file()
        elif choice == self.FILE_MENU_CHOICES[3]:
            self.remove_file()

        return exit

    def create_file(self):
        """
        Create a file in the folder, take input from user
        encrypt and write to file
        """
        if self.cwd_has_files():
            self.print_cwd_files()

        try:
            file_name = input("Enter name of new file: ")
            if os.path.exists(file_name):
                print("File already exists.")
                time.sleep(0.75)
                return False
            else:
                with open(file_name, "w") as f:
                    content = self.multi_line_input(
                        "Write file contents (type ESC to exit):"
                    )
                    encrypted_content = self.safe.encrypt(content)
                    f.write(encrypted_content)
                print(f'Created file "{file_name}".')
                time.sleep(0.75)
                return True
        except (OSError, FileExistsError) as e:
            print(f"An error occurred in create_file: {e}")
            time.sleep(0.75)

    def read_file(self):
        """
        Prints content of a file to console if cwd
        has files
        """
        try:
            if not self.cwd_has_files():
                print("No files to read in current folder.")
                time.sleep(0.75)
                os.system("cls")
                return False

            self.print_cwd_files()
            file_name = input("Enter file name to read: ")
            if file_name.endswith(".py"):
                raise ValueError("File must not be a python file.")

            with open(file_name, "r") as f:
                encrypted_content = f.read()

            print("Encrypted file contents:")
            print(encrypted_content)

            decrypted_content = self.safe.decrypt(encrypted_content)

            print("File contents:")
            print(decrypted_content)
            input("Press enter to continue...")
            return True
        except (ValueError, OSError, FileNotFoundError) as e:
            print(f"An error occurred in read_file: {e}")
            time.sleep(0.75)
            return False

    def append_file(self):
        """
        append to a selected file. load, decrypt and load the file
        as string, then append before encrypting and writing
        back to file
        """
        try:
            if not self.cwd_has_files():
                raise OSError("No files to append in current folder.")

            self.print_cwd_files()
            file_name = input("Enter name of file to append to: ")

            with open(file_name, "r+") as f:
                encrypted_content = f.read()
                decrypted_content = self.safe.decrypt(encrypted_content)
                if decrypted_content is None:
                    raise ValueError("Could not decrypt file content.")

                new_content = self.multi_line_input(
                    "Enter appended content (type ESC to exit): "
                )
                decrypted_content += new_content
                encrypted_content = self.safe.encrypt(decrypted_content)

                f.seek(0)
                f.write(encrypted_content)
            print(f'Successfully appended to "{file_name}"...')
            time.sleep(0.75)
            return True
        except (OSError, ValueError) as e:
            print(f"{e}")
            time.sleep(0.75)
            return False

    def remove_file(self):
        """Remove a file from the current working folder"""
        if not self.cwd_has_files():
            print("No files to remove in current folder.")
            time.sleep(0.75)
            os.system("cls")
            return False

        self.print_cwd_files()
        file_name = input("Enter file name to remove: ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'File "{file_name}" removed successfully.')
            time.sleep(0.75)
            return True
        else:
            print("File does not exist.")
            time.sleep(0.75)
            return False


# main function
@error_decorator
def main():
    """Main function to run the program
    Create an instance of filesafe and run it
    """
    file_safe = FileSafe()
    file_safe.run()


if __name__ == "__main__":
    """Run the program"""
    main()
