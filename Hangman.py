"""Integration of the core functions of the simple Hangman game."""

# importing the necessary modules
from import_database import *
import user_inputs as UI
import word_selector as WS
import game_initiation as GI
import input_letters as IL
import difflib


def play_function():
    new_game = "Yes"
    name = UI.user_name()
    # while loop for running the game
    while new_game == "Yes":
        user_in = UI.user_inputs()  # game version
        game_word = WS.random_word(user_in)  # game version, chosen word and related country/capital
        placeholder_word = GI.game_init(game_word)  # empty placeholders for letters and chosen word
        if user_in in [3, 4]:
            lives = 4
            hangman = 2
        else:
            hangman = 0
            lives = 6
        attempts = []
        # asking user input letters
        while True:
            hang_state = IL.letters(placeholder_word, hangman, attempts, lives)
            hangman = hang_state[1]
            lives = hang_state[3]
            attempts = hang_state[2]
            # evaulating successfull gameplay
            if "_" not in hang_state[0]:
                if user_in == 1 or user_in ==3:
                    print("\nWow, impressive! Maybe you also want to know that " + game_word[2] + " is the capital of your solution!")
                elif user_in == 2 or user_in ==4:
                    print("\nWow, impressive! Maybe you also want to know that your solution is the capital of " + game_word[2]+".")
                print("I hope you had some fun " + name+"!")
                break
            # evaulating lost gameplay
            elif hang_state[1] == (len(HANGMANPICS)-1):
                print("\n" + name + ", you suck at this game. LOOOSER!")
                if user_in == 1 or user_in ==3:
                    print("The word would have been: " + game_word[1] + " and since you need some education, its capital is " + game_word[2]+".")
                elif user_in == 3 or user_in ==4:
                    print("The word would have been: " + game_word[1] + " and since you need some education, it is the capital of " + game_word[2]+".")
                break
        #  new game initialization
        new_game = input(
            "If you want to end the game, please type 'Quit', otherwise type any letter: ").capitalize()
        # quits with quit
        if new_game == "Quit":
            exit()
        # quits with words similar to quit
        elif difflib.get_close_matches(new_game, ['Yes', 'asdf', 'Quit']) == "Quit":
            exit()
        else:
            new_game = "Yes"
            continue


play_function()
