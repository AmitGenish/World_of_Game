import random


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"Enter your guess between 0 and {difficulty}: "))


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        print(f"\nMazal Tov! You won! And your prize is...ֿ\n.\n.\n.\nMazal Tov!")
    else:
        print(f"\nBoy oh Boy...This time you've lost...")
        print("\nThe correct answer was", secret_number)


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    compare_results(secret_number, user_guess)
    return secret_number == user_guess

