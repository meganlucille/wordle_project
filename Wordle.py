import random
from WordleDictionary import FIVE_LETTER_WORDS, SPANISH_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR
from collections import Counter
from tkinter import *

def select_language():
    root = Tk()
    root.geometry("300x100")
    root.title("Select Language")
    
    def start_game(language):
        root.destroy()
        wordle(language)
    
    english_button = Button(root, text="English", command=lambda: start_game("English"))
    spanish_button = Button(root, text="Spanish", command=lambda: start_game("Spanish"))
    
    english_button.pack(pady=10)
    spanish_button.pack(pady=10)
    
    root.mainloop()

def wordle(language):
    # Choose a random word that we are trying to guess - based on language selected
    if language == "English":
        word_to_guess = random.choice(FIVE_LETTER_WORDS)
    elif language == "Spanish":
        word_to_guess = random.choice(SPANISH_WORDS)

    word_to_guess_list = [char for char in word_to_guess.lower()]
    keys_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    print(word_to_guess_list)

    # Create a dictionary of the letters used and their frequency. Use Counter to count letter occurrences
    letter_count = Counter(letter.lower() for letter in word_to_guess if letter.isalpha())
    # Convert the Counter to a dictionary
    letter_count_dict = dict(letter_count)
    print(letter_count_dict)

    def enter_action(s):
        # Set the correct count to 0. For future win checking
        correct_count = 0

        if s.lower() in FIVE_LETTER_WORDS or s.lower() in SPANISH_WORDS:
            gw.show_message("Valid word!")

            # Convert the guess string to a list)
            guess_list = [char for char in s.lower()]
            print(guess_list)
            
            # Loop through each letter in the row, checking if any are exact matches. If exact matches, reduce the letter count dictionary by 1
            for i in range(5):
                # Check for right letter in right place
                if word_to_guess_list[i] == guess_list[i]:
                    # Set the square to the correct color
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    if guess_list[i].upper() in keys_array:
                        gw.set_key_color(guess_list[i].upper(), CORRECT_COLOR)
                        keys_array.remove(guess_list[i].upper())

                    correct_count += 1
                    letter = word_to_guess_list[i]
                    if letter_count_dict.get(letter, 0) > 0:
                        letter_count_dict[letter] -= 1
                    else:
                        letter_count_dict.pop(letter, None)
                elif guess_list[i] in word_to_guess_list:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    if guess_list[i].upper() in keys_array:
                        gw.set_key_color(guess_list[i].upper(), PRESENT_COLOR)
                        #keys_array.remove(guess_list[i].upper())

                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)  # Set missing letters to grey
                    if guess_list[i].upper() in keys_array:
                        gw.set_key_color(guess_list[i].upper(), MISSING_COLOR)
                        keys_array.remove(guess_list[i].upper())

            # Check if user won
            if correct_count == 5:
                if language == 'english':
                    # Success Toast
                    gw.show_message("You won!")
                else:
                    gw.show_message("¡Ganaste!")

                # Make it so that enter key doesn't work
                gw.remove_enter_listener(enter_action)

                if language == 'english':
                    button_text = 'Click to Share results'
                else:
                    button_text = 'Compartir'
                # Make share results button appear
                b0 = Button(
                    text= button_text,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command= share_results_action,
                    relief = "flat")
                b0.place(x = 340, y = 440, width = 150, height = 38)
                
            
            else:
                # If didn't win, check if it's the last row.
                if gw.get_current_row() == 5:
                    # Failure Toas
                    if language == 'english':
                        gw.show_message("You lost. Try again!")
                    else:
                        gw.show_message("No ganaste. Lo siento")

                    # Make it so that enter key doesn't work
                    gw.remove_enter_listener(enter_action)
                
                # If not, move the cursor down a row
                else:
                    gw.set_current_row(gw.get_current_row() + 1)
                    

        else:
            if language == 'english':
                gw.show_message("Not in word list")
            else:
                gw.show_message("No es una palabra")

    # Sets the squares to not have a letter
    def share_results_action():
        for row in range(6):
            for col in range(5):
                gw.set_square_letter(row,col,"")
        if language == 'english':
            gw.show_message("Screenshot above")
        else:
            gw.show_message("Haz un screenshot arriba")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    select_language()
