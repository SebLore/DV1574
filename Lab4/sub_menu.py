import os
import encryption as enc

def take_input():
    """
    Get a choice from a user and return it.

    Returns:
        choice: string
    """
    return_string = ""
    input_string = None
    while input_string != "":
        try:
            input_string = input()
            return_string += input_string + "\n"
        except Exception as e:
            print(f"An error occurred in take_input: {e}")
            break

    return return_string


def print_menu():
    """
    Print the main menu options.
    """
    print("Select an option:")
    print("\t1. Create a file")
    print("\t2. Read a file")
    print("\t3. Edit a file")
    print("\t4. Remove a file")
    print("\t5. Return to main menu")


def print_files(folder):
    """
    Print the files in a folder.
    Args:
        folder: string
    """
    print(f"Files in folder {folder}:")
    for file in os.listdir(folder):
        if os.path.isfile(file):
            print("\t", file)


def submenu(folder):
    """
    Print the submenu options and take action based on the user's choice.

    Args:
        folder: string
    """
    done = False
    while not done:
        print_menu()
        choice = input("Make a selection: ")
        done = select_action(choice, folder)

def create_file(folder = None):
    """
    Create a new file.

    Returns:
        file_name: string
    """

    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, "w") as file:
            # take user input to write to the file with newline enabled
            print("File created successfully.")
            to_file = take_input()
            to_file = enc.encrypt(to_file)
            file.write(to_file)

    except FileExistsError:
        print("File already exists.")
    except Exception as e:
        print(f"An error occurred in create_file: {e}")
    return file_name


def read_file(folder = None):
    """
    Read a file.

    Returns:
        file_name: string
    """
    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, "r") as file:
            # decrypt the file contents and print them
            print("File opened successfully.")
            file_contents = file.read()
            print("file content before decryption: ", file_contents)
            file_contents = enc.decrypt(file_contents)
            print("file content after decryption: ", file_contents)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred in read_file: {e}")
    finally:
        return file_name


def edit_file(folder = None):
    """
    Edit a file.

    Returns:
        file_name: string
    """
    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, "a") as file:
            # take user input to append to the file with newline enabled
            print("File opened successfully.")
            while(input("Enter text to append to the file (or press Enter to finish): ") != ""):
                to_append = take_input()
                to_append = enc.encrypt(to_append)           
                file.write(to_append)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred in edit_file: {e}")
    return file_name


def remove_file(folder = None):
    """
    Remove a file.

    Returns:
        file_name: string
    """
    file_name = input("Enter the name of the file: ")
    try:
        os.remove(file_name)
        print("File removed successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred in remove_file: {e}")
    return file_name



def select_action(choice):
    """
    Select an action based on the user's choice.

    Args:
        choice: string
    """
    if choice == "1":
        return create_file()
    elif choice == "2":
        return read_file()
    elif choice == "3":
        return edit_file()
    elif choice == "4":
        return remove_file()
    elif choice == "5":
        return None
    else:
        print("Invalid choice. Please try again.")


def main():
    TEST_FOLDER = "test"
    create_file()
    read_file()
    edit_file()
    read_file()
    remove_file()
    print("Test complete.")

if __name__ == "__main__":
    main()