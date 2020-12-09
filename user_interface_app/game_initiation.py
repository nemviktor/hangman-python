"""This function displays the starting status of the game.
It shows the gamer the hanging tree and the placeholders for the chosen word."""
from import_database import HANGMANPICS


def game_init(selection):
    placeholders = []
    word = selection[1]
    # creating the _ placeholders for the chosen word
    for i in range(len(word)):
        if word[i] == " ":
            placeholders.append("  ")
        else:
            placeholders.append("_")
        #  joining the elements of the placeholders list
        joint = " ".join(placeholders)
    # displaying the initial status of the game based on the chosen difficulty level
    if selection[0] in [1, 2]:
        print(HANGMANPICS[0])
    else:
        print(HANGMANPICS[2])
    print(joint)
    return placeholders, word
