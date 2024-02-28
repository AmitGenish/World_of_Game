SCORES_FILE_NAME = "Scores.txt"


def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
    except:
        current_score = 0

    new_score = current_score + (difficulty * 3) + 5

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))
