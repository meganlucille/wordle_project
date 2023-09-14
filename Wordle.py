# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR
from collections import Counter

def wordle():
    # Choose a random word that we are trying to guess
    word_to_guess = random.choice(FIVE_LETTER_WORDS)
    word_to_guess = "glass"
    word_to_guess_list = [char for char in word_to_guess.lower()]
    print(word_to_guess_list)

    # Create a dictionary of the letters used and their frequency. Use Counter to count letter occurrences
    letter_count = Counter(letter.lower() for letter in word_to_guess if letter.isalpha())
    # Convert the Counter to a dictionary
    letter_count_dict = dict(letter_count)
    print(letter_count_dict)

    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Valid word!")

            # Create a dictionary of the letters used and their frequency. Use Counter to count letter occurrences
            letter_count = Counter(letter.lower() for letter in word_to_guess if letter.isalpha())
            # Convert the Counter to a dictionary
            letter_count_dict = dict(letter_count)

            # Convert the guess string to a list)
            guess_list = [char for char in s.lower()]
            print(guess_list)

            # Loop through each letter in the row, checking if any are exact matches. If exact matches, reduce the letter count dictionary by 1
            for i in range(0,5):

                # Check for right letter in right place
                if word_to_guess_list[i] == guess_list[i]:

                    # Set the square to the correct color
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)

                    # Reduce the letter count dictionary by 1. 
                    letter_count_dict[word_to_guess_list[i]] -= 1

            # Loop through a second time, checking for right letter but wrong place.
            for i in range(0,5):

                # Check if the guessed letter exists in the dictionary
                if guess_list[i] in letter_count_dict:

                    # If it does, and it's greater than 0, set square to yellow.
                    if letter_count_dict[guess_list[i]] > 0:
                        gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR) 

                        # Reduce the letter count dictionary by 1
                        letter_count_dict[guess_list[i]] -= 1

            print(letter_count_dict)
            
            # Move the cursor down a row
            gw.set_current_row(gw.get_current_row()+1)
        

        else:
            gw.show_message("Not in word list")
        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
