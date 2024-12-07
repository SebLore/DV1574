"""
Main menu actions and functions
"""

# import os
import os
import sub_menu as sm


def print_main_menu():
    """
    Print the main menu options.
    """
    print("Main Menu")
    print("\t1. Create a folder")
    print("\t2. Select a folder")
    print("\t3. Remove a folder")
    print("\t0. Exit")


def print_cwd_folders():
    """
    Print the folders in the current directory.
    """
    print("Available folders in directory:")
    try:
        for folder in os.listdir(os.getcwd()):
            if os.path.isdir(folder):
                print("\t", folder)
    except Exception as e:
        print(f"An error occurred: {e}")


def select_action(choice):
    """
    Select an action based on the user's choice.

    Args:
        choice: string
    """
    folder = None

    if choice == "1":
        folder = create_folder()
    elif choice == "2":
        folder = select_folder()
    elif choice == "3":
        folder = remove_folder()
        return False
    elif choice == "0":
        return False

    os.chdir(folder)
    print(f"Current directory: {os.getcwd()}")
    if folder:
        sm.select_action(folder)
    else:
        print("Invalid choice. Please try again.")

    return False


def create_folder():
    """
    Create a new folder.

    Returns:
        folder_name: string
    """
    folder_name = input("Enter a name for the new folder: ")
    try:
        # os.mkdir(folder_name)
        print("Folder created successfully.")
    except FileExistsError:
        print("Folder already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        return folder_name


def select_folder():
    """
    Select an existing folder.

    Returns:
        folder_name: string
    """
    try:
        print_cwd_folders()
        folder_name = input("Enter the name of the folder: ")
        if not os.path.exists(folder_name):
            print(f"Folder {folder_name} does not exist.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        return folder_name


def remove_folder():
    """
    Remove an existing folder.

    Returns:
        folder_name: string
    """
    try:
        print_cwd_folders()
        folder_name = input("Folder to delete: ")
        if os.path.exists(folder_name):
            # os.rmdir(folder_name)
            print("Folder removed successfully.")
        else:
            print("Folder does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return folder_name
