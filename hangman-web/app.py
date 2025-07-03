from flask import Flask, render_template, request, session, redirect, url_for
from src.game import HangmanGame
from src.words import get_random_word
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():
    if "game" not in session:
        word = get_random_word()
        session["word"] = word
        session["guesses"] = []
        session["tries"] = 6

    game = HangmanGame(session["word"])
    game.tries_left = session["tries"]
    game.guessed_letters = session["guesses"]

    message = ""
    if request.method == "POST":
        guess = request.form["guess"]
        message = game.guess(guess)
        session["guesses"] = game.guessed_letters
        session["tries"] = game.tries_left

    return render_template("index.html",
                           word=game.get_display_word(),
                           tries=game.tries_left,
                           hangman=game.get_hangman_art(),
                           message=message,
                           is_over=game.is_game_over(),
                           status=game.get_status())

if __name__ == "__main__":
    app.run(debug=True)
