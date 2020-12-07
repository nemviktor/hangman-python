"""This function selects a word from the input list.Selection is based on random number generation
in a properly specified range. And then choosing a word from the country-capitol pair."""
# importing the necessary modules
import random as rnd
# from database module we import everything
from import_database import *


def random_word(game_version):
    #  countries and easy
    if game_version == 1:
        words_list = easy_list[rnd.randint(0, len(easy_list)-1)]
        word_to_guess = words_list[0]
        word_related = words_list[1]
    #  capitals and easy
    if game_version == 2:
        words_list = easy_list[rnd.randint(0, len(easy_list)-1)]
        word_to_guess = words_list[1]
        word_related = words_list[0]
    #  countries and hard
    if game_version == 3:
        words_list = hard_list[rnd.randint(0, len(hard_list)-1)]
        word_to_guess = words_list[0]
        word_related = words_list[1]
    # capitals and hard
    if game_version == 4:
        words_list = hard_list[rnd.randint(0, len(hard_list)-1)]
        word_to_guess = words_list[1]
        word_related = words_list[0]
    return game_version, word_to_guess, word_related
