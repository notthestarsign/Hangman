# src/words.py

import os
import random

def load_word_list(min_length=3, max_length=12):
    words_file = os.path.join(os.path.dirname(__file__), "data/words.txt")
    with open(words_file, "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f if min_length <= len(line.strip()) <= max_length]
    return list(set(words))  # remove duplicates

word_list = load_word_list()

def get_random_word():
    return random.choice(word_list).upper()
