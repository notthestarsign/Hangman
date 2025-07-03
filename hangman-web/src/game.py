# src/game.py

class HangmanGame:
    def __init__(self, word, max_tries=6):
        self.word = word.upper()
        self.max_tries = max_tries
        self.tries_left = max_tries
        self.guessed_letters = set()
        self.guessed_words = set()
        self.word_progress = ["_"] * len(self.word)
        self.status = "IN_PROGRESS"  # Can be WIN, LOSE, or IN_PROGRESS

    def guess(self, user_input):
        guess = user_input.upper()

        if not guess.isalpha():
            return "Invalid guess."

        if len(guess) == 1:
            if guess in self.guessed_letters:
                return f"You already guessed the letter {guess}."
            self.guessed_letters.add(guess)
            if guess not in self.word:
                self.tries_left -= 1
                self._update_status()
                return f"{guess} is not in the word."
            else:
                for i, char in enumerate(self.word):
                    if char == guess:
                        self.word_progress[i] = guess
                if "_" not in self.word_progress:
                    self.status = "WIN"
                return f"Good job, {guess} is in the word!"
        elif len(guess) == len(self.word):
            if guess in self.guessed_words:
                return f"You already guessed the word {guess}."
            self.guessed_words.add(guess)
            if guess != self.word:
                self.tries_left -= 1
                self._update_status()
                return f"{guess} is not the word."
            else:
                self.word_progress = list(self.word)
                self.status = "WIN"
                return "Correct! You guessed the word!"
        else:
            return "Not a valid guess."

    def get_display_word(self):
        return " ".join(self.word_progress)

    def is_game_over(self):
        return self.status in {"WIN", "LOSE"}

    def _update_status(self):
        if self.tries_left <= 0:
            self.status = "LOSE"

    def get_status(self):
        return self.status

    def get_hangman_art(self):
        return HANGMAN_STAGES[self.max_tries - self.tries_left]


# Hangman drawings (static)
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """
]
