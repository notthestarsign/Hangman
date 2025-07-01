# src/ui_terminal.py

from game import HangmanGame
from words import get_random_word
import time

def play_game():
    word = get_random_word()
    game = HangmanGame(word)

    print("🎮 Let's play Hangman!")

    while not game.is_game_over():
        print(game.get_hangman_art())
        print("Word:", game.get_display_word())
        print(f"Tries left: {game.tries_left}")
        guess = input("Guess a letter or word: ")
        message = game.guess(guess)
        print(message)
        print()

    print(game.get_hangman_art())
    print("\n🧠 Final Word:", game.get_display_word())
    print(game.get_hangman_art())
    if game.get_status() == "WIN":
        print("🎉 Congratulations, you won!")
    else:
        print(f"😢 Game over! The word was: {word}")

def main():
    print("Welcome to the Hangman CLI 🎮\n")
    time.sleep(0.5)
    
    play_game()
    while input("Play again? (Y/N): ").strip().upper() == "Y":
        play_game()

if __name__ == "__main__":
    main()
