"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 
NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():

    hi_score = [] # Stores the player score
    continue_game = "y" # Gives player the option to end the game
    player_guess = None
    player_attempts = 0
    answer = random.randint(1,10)
            

    print("Welcome to the Super Cool Number Guessing Game!" )
    name = input("What is your name? ")
    print("Hello {}, best of luck & lets begin! ".format(name))
    while player_guess != "answer":
        try:
            player_guess = int(input("Please guess a number between 1 & 10: "))
            while (player_guess < 1) or (player_guess > 10):
                player_guess = int(input(" Whoops! Rule Breaker! You must enter a number between 1 & 10! "))

            player_attempts += 1
            if player_guess > answer:
                print("<===Guess lower")
            elif player_guess < answer:
                print("===>Guess higher")

            else:
                print("Winner! Fantastic Stuff! It took you {} attempt(s). You Champion!".format(player_attempts))
                hi_score.append(player_attempts)
                continue_game = input(" Would you like to play again? y or n ?: ")
                if continue_game.lower() == "n":
                    print("Bye for now & see you soon!")

        except SyntaxError as err:
            print("Invalid value ! ({})\n Please try again". format(err))
        except NameError as err:
            print("Invalid value ! ({})\n Please try again". format(err))

        

                
            

if __name__=='__main__':
    start_game()
