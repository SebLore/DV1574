import os

def main_menu():
    print("Main Menu:")
    print("1. Create Folder")
    print("2. Delete Folder")
    print("3. Pick Existing Folder")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def folder_menu(folder_path):
    print(f"Folder Menu - Working in: {folder_path}")
    print("1. Create File")
    print("2. Read File")
    print("3. Edit File")
    print("4. Remove File")
    print("5. Go Back to Main Menu")
    choice = input("Enter your choice: ")
    return choice

def create_folder():
    folder_name = input("Enter folder name to create: ")
    os.makedirs(folder_name, exist_ok=True)
    print(f"Folder '{folder_name}' created successfully.")
    return folder_name

def delete_folder():
    folder_name = input("Enter folder name to delete: ")
    try:
        os.rmdir(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")
    except OSError as e:
        print(f"Error: {e.strerror}")

def pick_folder():
    folder_name = input("Enter folder name to work from: ")
    if os.path.isdir(folder_name):
        return folder_name
    else:
        print("Folder does not exist.")
        return None

def create_file(folder_path):
    file_name = input("Enter file name to create: ")
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as f:
        content = input("Enter content for the file: ")
        f.write(content)
    print(f"File '{file_name}' created successfully.")

def read_file(folder_path):
    file_name = input("Enter file name to read: ")
    file_path = os.path.join(folder_path, file_name)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File does not exist.")

def edit_file(folder_path):
    file_name = input("Enter file name to edit: ")
    file_path = os.path.join(folder_path, file_name)
    try:
        with open(file_path, 'a') as f:
            content = input("Enter content to append to the file: ")
            f.write(content)
        print(f"File '{file_name}' edited successfully.")
    except FileNotFoundError:
        print("File does not exist.")

def remove_file(folder_path):
    file_name = input("Enter file name to remove: ")
    file_path = os.path.join(folder_path, file_name)
    try:
        os.remove(file_path)
        print(f"File '{file_name}' removed successfully.")
    except FileNotFoundError:
        print("File does not exist.")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            folder_path = create_folder()
        elif choice == '2':
            delete_folder()
            folder_path = None
        elif choice == '3':
            folder_path = pick_folder()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        if folder_path:
            while True:
                choice = folder_menu(folder_path)
                if choice == '1':
                    create_file(folder_path)
                elif choice == '2':
                    read_file(folder_path)
                elif choice == '3':
                    edit_file(folder_path)
                elif choice == '4':
                    remove_file(folder_path)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()