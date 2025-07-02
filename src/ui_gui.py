import tkinter as tk
from tkinter import messagebox
from game import HangmanGame
from words import get_random_word

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.game = HangmanGame(get_random_word())

        self.word_label = tk.Label(root, text=self.game.get_display_word(), font=("Courier", 24))
        self.word_label.pack(pady=40)
        self.word_label.pack(padx=40)

        self.canvas = tk.Canvas(root, width=300, height=200)
        self.hangman_text = self.canvas.create_text(150, 100, text=self.game.get_hangman_art(), font=("Courier", 10))
        self.canvas.pack()

        self.entry = tk.Entry(root, font=("Courier", 14))
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack()
        
        self.tries_label = tk.Label(root, text=f"Tries left: {self.game.tries_left}", font=("Arial", 12))
        self.tries_label.pack()

        
        self.root.bind('<Return>', lambda event: self.make_guess())
        self.root.bind('<Escape>', lambda event: self.root.quit())


    def make_guess(self):
        guess = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if not guess:
            return

        message = self.game.guess(guess)
        self.word_label.config(text=self.game.get_display_word())
        self.canvas.itemconfig(self.hangman_text, text=self.game.get_hangman_art())
        self.feedback_label.config(text=message)
        self.tries_label.config(text=f"Tries left: {self.game.tries_left}")

        if self.game.is_game_over():
            self.end_game()

    def end_game(self):
        result = "You Win! " if self.game.get_status() == "WIN" else f"You Lose \nThe Word was: {self.game.word}"
        retry = messagebox.askyesno("Game Over", f"{result}\n\nPlay Again?")
        if retry:
            self.game = HangmanGame(get_random_word())
            self.word_label.config(text=self.game.get_display_word())
            self.canvas.itemconfig(self.hangman_text, text=self.game.get_hangman_art())
            self.feedback_label.config(text="")
            self.tries_label.config(text=f"Tries left: {self.game.tries_left}")
        else:
            self.root.quit()
    
def main():
    root = tk.Tk()
    gui = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
