"""This script imports the necessary data, e.g. ASCII art and list of country-capital pairs."""
# import os
# print(os.getcwd()) Ez kirakja a fájl working mappáját, és eszerint a fájlunk eggyel feljebbre mutatott.
#                    De az almappa megadásával (az openben) már jó, és így nem kell mindig lokál géphez igazítani.

countries = open('./hangman-python-mozsolim/countries-and-capitals.txt', 'r')
list_all = countries.readlines()  # creates the list from the input
list_all = [i.replace("\n", "") for i in list_all]  # removes the \n line break character
easy_list = []
hard_list = []

# selection of the easy entries from list based on their order number
for i in [
    1, 2, 3, 6, 8, 9, 11, 12, 16, 20, 22, 24, 32, 33, 34, 38, 39, 40, 42, 43, 47, 46, 51, 54, 55, 59, 61, 67, 68,
    69, 71, 72, 74, 75, 77, 93, 94, 97, 100, 104, 107, 109, 110, 116, 115, 121, 129, 131, 132, 134, 135, 144, 148,
    149, 152, 153, 155, 159, 160, 165, 169, 173, 174, 175, 176
]:
    easy_list.append(list_all[i-1])

#  creating the hard words' list from easy list's complementer
for item in list_all:
    if item not in easy_list:
        hard_list.append(item)

#  creat list in list object where sub-list items are country-capital pairs
easy_list = [i.split(',', 1) for i in easy_list]
hard_list = [i.split(',', 1) for i in hard_list]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
