from Games.guess_game import play as play_guess_game
from Games.currency_roulette_game import play as play_currency_roulette
from Games.memory_game import play as play_memory_game

games = {
    1: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
    2: "Guess Game - guess a number and see if you chose like the computer.",
    3: "Currency Roulette - try and guess the value of a random amount of USD in ILS"
}

difficulty_messages = {
    1: "Brave choice, hero! Are you sure your mouse is working?",
    2: "Level 2! Did you warm-up your brain today?",
    3: "Ahh, a risk-taker! Halfway there and living on a prayer!",
    4: "Level 4! I hope you don't have plans for the rest of the day!",
    5: "Level 5? Someone's feeling adventurous... or foolish?"
}


# New function to add score
def add_score(difficulty):
    score = difficulty * 3  # Assuming score calculation based on difficulty
    with open("Scores.txt", "a") as file:
        file.write(f"{score}\n")
    print("Your score has been added successfully.")


def welcome():
    username = input("Please enter your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey!\n")


def start_play():
    while True:
        print("Please choose a game to play:")
        for number, description in games.items():
            print(f"({number}) {description}")

        game_choice_input = input("\nEnter the game number you want to play (1-3): ")
        if game_choice_input.isdigit():
            game_choice = int(game_choice_input)
            if game_choice in games:
                print(f"You have selected: {games[game_choice]}")

                difficulty_input = input("\nPlease choose a difficulty level (1-5): ")
                if difficulty_input.isdigit():
                    difficulty = int(difficulty_input)
                    if 1 <= difficulty <= 5:
                        print(f"\nYou have chosen difficulty level: {difficulty}\n")
                        print(difficulty_messages[difficulty])
                        if play_game(game_choice, difficulty):
                            continue
                        else:
                            break
                    else:
                        print("\nInvalid difficulty level. Please select a valid level between 1 and 5.\n")
                else:
                    print("\nInvalid input. Please enter numbers only for difficulty level.\n")
            else:
                print("\nInvalid game choice. Please select a valid game number.\n")
        else:
            print("\nInvalid input. Please enter numbers only for game choice.\n")


def play_game(game_choice, difficulty):
    game_result = False
    if game_choice == 1:
        game_result = play_memory_game(difficulty)
    elif game_choice == 2:
        game_result = play_guess_game(difficulty)
    elif game_choice == 3:
        game_result = play_currency_roulette(difficulty)

    if game_result:
        print("\nCongratulations on winning!\n")
        add_score(difficulty)  # Add score upon winning
    else:
        print("\nBetter luck next time!\n")

    # Ask the player if they want to play again
    play_again = input("Press ENTER to Play Again or type 'HALAS' to quit: ")
    if play_again.upper() == 'HALAS':
        return False  # End the game loop
    else:
        return True  # Continue the game loop


welcome()
start_play()

