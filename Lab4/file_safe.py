import os
import main_menu as mm


def validate_choice(ok_list):
    """
    Get a choice from a user, validate it against a tuple of choices
    and return it. Take input from the user until a valid choice is
    entered.

    Args:
        ok_list: tuple of strings

    Returns:
        choice: string
    """
    while True:
        try:
            choice = input("Make a selection: ")
            if choice in ok_list:
                return choice
            else:
                print("Invalid choice. Please enter an integer number between 0 and 3.")
        except Exception as e:
            print(f"An error occurred in validate_choice: {e}")
        

def main():
    done = False
    wd = os.getcwd()
    try:
        while done == False:
            os.chdir(wd)
            print("current dir", os.getcwd())
            mm.print_main_menu()
            CHOICES = ("0", "1", "2", "3")
            choice = validate_choice(CHOICES)
            
            done = mm.select_action(choice)          
    except Exception as e:
        print(f"An error occurred in main: {e}")
        return None


if __name__ == "__main__":
    main()    