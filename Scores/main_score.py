from flask import Flask

app = Flask(__name__)

SCORES_FILE_NAME = "/Users/amitgenish/Desktop/Genish_Bruh/Project's/Coding_Project's/Pyhton/DevOps_Experts/WOG/Scores.txt"
DEFAULT_SCORE = 0
ERROR_HTML = """<html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>ERROR:</h1>
                        <div id="score" style="color:red">{ERROR}</div>
                    </body>
                </html>"""


def read_score():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            return sum(int(line.strip()) for line in file if line.strip().isdigit())
    except Exception as e:
        print(f"Failed to read score: {e}")  # Log the error for debugging
        return None



@app.route("/")
def score_server():
    score = read_score()
    if score is not "":
        return f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>Your Score is: </h1>
                            <div id="score">{score}</div>
                        </body>
                    </html>"""

    else:
        return ERROR_HTML


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)
