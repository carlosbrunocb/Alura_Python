import forca
import adivinhacao
from adivinhacao import guessing_game
from forca import hangman_game

def game_select():
    print("+++++++++++++++++++++")
    print("++Choose your Game!++")
    print("+++++++++++++++++++++")

    print("1. Guessing Game")
    print("2. Hangman Game")

    selected_game = int(input("# Which game do you want to play?\n  "))

    games = {
        "Guessing_Game": 1,
        "Hangman_Game" : 2
    }

    if(selected_game == games["Guessing_Game"]):
        # print("Guessing_Game")
        adivinhacao.guessing_game()
    elif(selected_game == games["Hangman_Game"]):
        # print("Hangman_Game")
        forca.hangman_game()
    else:
        print("@ Your entered not valid option!")
        print("@ By standard your option was setting as Guessing Game!")
        input("# Press enter to continue!\n")
        guessing_game()

if(__name__ == "__main__"):
    game_select()