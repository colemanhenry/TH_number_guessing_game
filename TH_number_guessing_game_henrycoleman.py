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
    continue_game = False # Gives player the option to end the game
    player_guess = 0
            

    print("Welcome to the Super Cool Number Guessing Game!" )
    name = input("What is your name? ")
    print("Hello {}, best of luck & lets begin! ".format(name))
    while player_guess != "answer":
        try:
            player_guess = int(input("Please guess a number between 1 & 10"))

if __name__=='__main__':
    start_game()
