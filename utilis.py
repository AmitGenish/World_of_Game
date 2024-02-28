import subprocess

# Variables
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


# Functions
def screen_cleaner():
        subprocess.run('clear', shell=True)