"""Integration of the core functions of the simple Hangman game.
Then, creating the general user interace for the hangman game by Máté & Viktor."""
#  need to sudo apt-get install python3-tk to be able to use tkinter module
#  and sudo apt-get install python3-pil python3-pil.imagetk to use ImageTk function
# importing the necessary modules
from tkinter import ttk, Tk, Label, Button, StringVar, Entry
from PIL import Image, ImageTk
from import_database import HANGMANPICS
from import_database import *
import user_inputs as UI
import word_selector as WS
import game_initiation as GI
import difflib

def get_command():
    global typein
    typein.set(e4.get())


def letters(placeholder_init, hangman, attempts, lives):
    # displaying the placeholders
    placeholders = placeholder_init[0]
    # defining the word that will be compared with the user's input
    word_ = placeholder_init[1].upper()
    # asking a letter from the user in a foolproof manner, and storing the chosen ones
    while True:
        inst.config(text=format("Please! Give me a letter!"))
        letter = typein
        if letter.isalpha() and len(letter) == 1 and letter not in attempts:
            attempts.append(letter)
            break
        inst.config(text=format("Please enter characters A-Z only or you tried it before!"))
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
    return state, hangman, attempts, lives


def play_function():
    new_game = "Yes"
    name = UI.user_name(e1.get())
    # while loop for running the game
    while new_game == "Yes":
        user_in = UI.user_inputs(e2.get(), e3.get())  # game version
        game_word = WS.random_word(user_in)  # game version, chosen word and related country/capital
        placeholder_word = GI.game_init(game_word)  # empty placeholders for letters and chosen word
        if user_in in [3, 4]:
            lives = 4
            hangman = 2
        else:
            hangman = 0
            lives = 6
        life.config(text=format(lives))
        plcholders.config(text=format(placeholder_word[2]))
        tree.config(text=format(HANGMANPICS[0]))
        attempts = []
        # asking user input letters
        while True:
            hang_state = letters(placeholder_word, hangman, attempts, lives)
            hangman = hang_state[1]
            lives = hang_state[3]
            attempts = hang_state[2]
            life.config(text=format(lives))
            plcholders.config(text=format(hang_state[0]))
            tree.config(text=format(HANGMANPICS[hangman]))
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


window=Tk()

window.wm_title("Hangman Game by Máté&Viktor")
window.configure(bg='black')
img = Image.open("./hangman-python-mozsolim/user_interface_app/wildwest.png")
img = img.resize((400, 600), Image.ANTIALIAS)
img_ = ImageTk.PhotoImage(img)
_img_ = Label(window, image=img_, borderwidth=6)
_img_.grid(row=0, column=2, rowspan=14, columnspan=11)

lives=4
status = HANGMANPICS[6]
l1=Label(window,text="""It is not a child game anymore.
Pick a word and play, if you dare!""", fg='white', bg='black')
l1.grid(row=0, column=0, columnspan=2)
l2=Label(window,text="""How can I call you,
Cowboy?""", fg='white', bg='black')
l2.grid(row=1, column=0, sticky='w')
l3=Label(window,text="Game level:", fg='white', bg='black')
l3.grid(row=2, column=0, sticky='w')
l4=Label(window,text="Choosen type:", fg='white', bg='black')
l4.grid(row=3, column=0, sticky='w')
b1=Button(window,text="Let's play!", bd='2', fg='white', bg='black', activebackground="white", command=play_function)
b1.grid(row=4, column=0, columnspan=2)
l5=Label(window,text="Remaining lives:", fg='white', bg='black')
l5.grid(row=5, column=0, sticky='w')
life=Label(window,text= "", fg='white', bg='black')
life.grid(row=5, column=1, sticky="w")
plcholders=Label(window,text="", fg='white', bg='black')
plcholders.grid(row=6, column=0, columnspan=2, sticky="we")
inst=Label(window,text="", fg='white', bg='black')
inst.grid(row=7, column=0, columnspan=2, sticky='we')
l9=Label(window,text="User inputs:", fg='white', bg='black')
l9.grid(row=8, column=0, sticky='w')
nameINPUT=StringVar()
e1=Entry(window, textvariable=nameINPUT)
e1.grid(column=1, row=1, sticky='ew')
typetext=StringVar()
e2=ttk.Combobox(window, textvariable=typetext)
e2['values'] = ["easy", "hard"]
e2.grid(column=1, row=2)
typetext=StringVar()
e3=ttk.Combobox(window, textvariable=typetext)
e3['values'] = ["countries", "capitals"]
e3.grid(column=1, row=3)
userINPUTS=StringVar()
e4=Entry(window, textvariable=userINPUTS)
e4.grid(row=8, column=1, sticky='ew')
e4.bind("<Return>", get_command)
b2=Button(window, text="Enter", bd='2', fg='white', bg='black', activebackground="white")
b2.grid(row=9, column=1, columnspan=2)
tree=Label(window, text="", fg='white', bg='black')
tree.grid(row=10, column=0, columnspan=2)


window.mainloop()
