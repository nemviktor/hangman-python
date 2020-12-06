"""Integration of the core functions of the simple Hangman game."""

# importing the necessary modules
from import_database import HANGMANPICS
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
        game_word = WS.random_word(user_in)  # game version and chosen word
        placeholder_init = GI.game_init(game_word)  # empty placeholders for letters and chosen word
        if user_in in [3, 4]:
            lives = 4
            hangman = 2
        else:
            hangman = 0
            lives = 6
        attempts = []
        # asking user input letters
        while True:
            hang_state = IL.letters(placeholder_init, hangman, attempts, lives)
            hangman = hang_state[0]
            lives = hang_state[3]
            attempts = hang_state[2]
            # evaulating successfull gameplay
            if "_" not in hang_state[1]:
                print("\nWow, impressive! I hope you had some fun " + name+"!")
                break
            # evaulating lost gameplay
            elif hang_state[0] == (len(HANGMANPICS)-1):
                print("The word would have been: " + game_word[1] + "\n")
                print(name + ", you suck at this game. LOOOSER!\n")
                break
        #  new game initialization
        new_game = input(
            "Would you like to play a new round? Yes or Quit?: ").capitalize()
        # quits with quit
        if new_game == "Quit":
            exit()
        # quits with words similar to quit
        elif difflib.get_close_matches(new_game, ['Yes', 'Quit']) == "Quit":
            exit()
        elif new_game == "Yes":
            continue


play_function()
