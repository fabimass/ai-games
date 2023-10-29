import subprocess

virtualenv_path = "venv\\Scripts\\activate.bat"

# Define a function to display the menu and get user input
def display_menu():
    print("Menu:")
    print("1. Minesweeper")
    print("2. Tic Tac Toe")
    print("3. Nim")
    print("4. Exit")

    # Prompt the user for input
    choice = input("Please choose the game you want to play: ")
    return choice

# Define a function for executing a given game script
def run_game(game_path):
    result = subprocess.run([virtualenv_path, "&&", "python", game_path], shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Script executed successfully")
        print("Output:")
        print(result.stdout)
    else:
        print("Script execution failed")
        print("Error Output:")
        print(result.stderr)

# Main program
while True:
    user_choice = display_menu()

    if user_choice == '1':
        print("You selected Minesweeper")
        run_game("minesweeper\\runner.py")

    elif user_choice == '2':
        print("You selected Option 2")
        # Add your code for Option 2 here

    elif user_choice == '3':
        print("You selected Option 3")
        # Add your code for Option 3 here

    elif user_choice == '4':
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
