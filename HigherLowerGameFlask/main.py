import random
from flask import Flask

app = Flask(__name__)

num = random.randint(0, 9)
print(num)


@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > num:
        return ("<h1  style='color:orange'>Too high, try again!</h1>"
                "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>")
    elif guess < num:
        return ("<h1 style='color:blue'>Too low, try again!</h1>"
                "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")
    else:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")


if __name__ == "__main__":
    app.run(debug=True)
