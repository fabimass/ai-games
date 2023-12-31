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
    result = subprocess.run([virtualenv_path, "&&", "python", "-u", game_path])
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
        print("You selected Tic Tact Toe")
        run_game("tictactoe\\runner.py")

    elif user_choice == '3':
        print("You selected Nim")
        run_game("nim\\play.py")

    elif user_choice == '4':
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
