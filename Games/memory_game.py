import random
import time
import subprocess


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    print(f"Enter {difficulty} numbers separated by spaces: ")
    return list(map(int, input().split()))


def is_list_equal(sequence, user_list):
    return sequence == user_list


def clear_screen():
    subprocess.run('clear', shell=True)


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Remember this sequence:", sequence)
    time.sleep(0.7 * int(difficulty))

    clear_screen()  # Clear the screen instead of printing line breaks

    user_list = get_list_from_user(difficulty)

    if sequence == user_list:
        print("That is Correct! You won!")
    else:
        print("You Lost...The correct answer was", sequence)

    return is_list_equal(sequence, user_list)
