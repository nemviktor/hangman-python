"""This script asks user inputs for the game.
    It asks his/her name, the desired gametype and the difficulty level.
    The game type can be chosen countries or capitals.
"""


def user_name(name):
    # ask user's name in a foolproof manner
        #name = input("Hello Gamer! How can I call you? ").capitalize()
    return name


def user_inputs(level, game_type):
    # # ask user's game preference of the difficulty level in a foolproof manner
        # diff_lev = input(
        #     "Are you brave enough to play with me on the difficult level? Y/N: ").capitalize()
        # if diff_lev != 'Y' and diff_lev != 'N':
        #     print("You proably mistyped something! Please try rerun the game!")
        #     exit()
    # # ask user's game preference of the game type in a foolproof manner
        # game_type = input(
        #     "So! Do you wanna play a game? Would you like to guess countries? Than type 1! Or capitals? Than type 2! ")
        # if game_type != "1" and game_type != "2":
        #     print("You proably mistyped something! Please try rerun the game!")
        #     exit()
    # game_version-1: countries, easy
    # game_version-2: capitals, easy
    # game_version-3: countries, hard
    # game_version-4: capitals, hard
    if level == "easy" and game_type == 'countries':
        game_version = 1
    elif level == "easy" and game_type == 'capitals':
        game_version = 2
    elif level == "hard" and game_type == 'countries':
        game_version = 3
    elif level == "hard" and game_type == 'capitals':
        game_version = 4
    return game_version
