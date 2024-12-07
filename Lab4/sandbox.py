"""
Sandbox to try to out the functionality before implementing
"""

import os
import cryptography
import tkinter
from tkinter import filedialog

import customtkinter as ctk


def print_main_menu():
    """
    Print the main menu options to the user.
    """
    print("Welcome to File Safe encryption.")
    print("Select one of the following options:")
    print("\t1. Create new folder")
    print("\t2. Select existing folder")
    print("\t3. Remove existing folder")
    print("\t0. Exit program")


def get_choice(CHOICES):
    """
    Get a choice from a user, validate it against a tuple of choices
    and return it. Take input from the user until a valid choice is
    entered.

    Args:
        CHOICES: tuple of strings

    Returns:
        choice: string
    """
    while True:
        try:
            choice = input("Enter a number: ")
            if choice in CHOICES:
                return choice
            else:
                print("Invalid choice. Please enter an integer number between 0 and 3.")
        except Exception as e:
            print(f"An error occurred: {e}")


def create_folder():
    """
    Create a new folder in the current directory. If the folder already exists,
    print a message to the user and return the folder name.

    Returns:
        folder_name: string
    """
    try:
        folder_name = input("Enter the name of the folder: ")
        os.mkdir(folder_name)
        print("Folder created successfully.")
    except FileExistsError:
        print("Folder already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        return folder_name


def select_folder():
    folder_name = input("Enter the name of the folder: ")
    if os.path.exists(folder_name):
        print("Folder exists.")
        return folder_name
    else:
        print("Folder does not exist.")
        return None


def remove_folder():
    try:
        folder_name = input("Enter the name of the folder: ")
        if os.path.exists(folder_name):
            os.rmdir(folder_name)
            print("Folder removed successfully.")
        else:
            print("Folder does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return folder_name

def sub_menu(folder):
    print_sub_menu()
    CHOICES = ("1", "2", "3", "4", "5")
    choice = get_sub_menu_choice()

    while choice != "5":
        if choice == "1":
            create_file(str)
        elif choice == "2":
            read_file(str)
        elif choice == "3":
            edit_file(str)
        elif choice == "4":
            delete_file(str)
        else:
            print("Invalid choice. Please try again.")
        print_sub_menu()
        choice = get_sub_menu_choice()


def main_menu():
    print_main_menu()
    CHOICES = ("1", "2", "3", "0")
    choice = get_choice(CHOICES)

    folder_name = None
    while choice != 0:
        try:
            if choice == "1":
                folder_name = create_folder()
            elif choice == "2":
                folder_name = select_folder()
            elif choice == "3":
                folder_name = remove_folder()
            if folder_name is not None:
                sub_menu(folder_name)
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            folder_name = None

    print("End of program")



def print_sub_menu():
    print("Select one of the following options:")
    print("\t1. Create a new file")
    print("\t2. Read a file")
    print("\t3. Edit a file")
    print("\t4. Delete a file")
    print("\t5. Return to main menu")


def get_sub_menu_choice():
    while True:
        try:
            choice = input("Enter a number: ")
            CHOICES = ("1", "2", "3", "4", "5")

            if choice in CHOICES:
                return choice
            else:
                print("Invalid choice. Please enter an integer number between 1 and 5.")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    main_menu()


# TKINTER GUI
# function to print what is in the editor textbox bellow when button is pressed
def print_callback(editor=None):
    if editor is not None:
        print(editor.get(1.0, ctk.END), end="")
    else:
        print("Editor is None.")


def ctk_test():
    app = ctk.CTk()
    app.title("File editor")
    app.geometry("600x480")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    editor = ctk.CTkTextbox(app, wrap="word")
    editor.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    button = ctk.CTkButton(app, text="Print", command=lambda: print_callback(editor))
    button.grid(row=1, column=0, padx=20, pady=20)

    app.mainloop()


if __name__ == "__main__":
    main()
    # print(f"Folder name: {folder_name}")
    # print("End of program.")
    ctk_test()
