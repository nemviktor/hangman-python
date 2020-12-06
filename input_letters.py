"""This function asks for user input letters. Validates the user inputs and rejects numbers
and inputs longer than 1 character."""
from import_database import HANGMANPICS


def letters(placeholder_init, hangman, attempts, lives):
    # displaying the placeholders
    placeholders = placeholder_init[0]
    # defining the word that will be compared with the user's input
    word_ = placeholder_init[1].upper()
    # asking a letter from the user in a foolproof manner, and storing the chosen ones
    while True:
        letter = input('Please give me a letter: ').capitalize()
        if letter.isalpha() and len(letter) == 1 and letter not in attempts:
            attempts.append(letter)
            break
        print("Please enter characters A-Z only or you tried it before!")
    # not success
    if letter not in word_:
        lives += -1
        hangman += 1
        print(HANGMANPICS[hangman])
        print("You have " + str(lives) + " lives left!")
    # success
    if letter in word_:
        for j in range(len(word_)):
            if word_[j] == letter:
                placeholders[j] = placeholder_init[1][j]
    # displaying the game status in a user friendly manner
    state = " ".join(placeholders)
    print(state)
    return hangman, state, attempts, lives
