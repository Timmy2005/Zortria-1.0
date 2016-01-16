# This is the format for inputting commands:
#
# print("Question here. (ex. What is your name?)")
# <variable> = raw_input("> ")
#
# Do it EXACTLY as shown above. Copy and paste if you need to.

from gameStartTest import gameStart
import inventory
import Store
import gameMove
from Store import showStore
from inventory import showInventory
from gameMove import Move

def playerAction():
    # This is the 'playerAction' function. It is used for typing commands.
    Move()#This is from 'gameMove.py'
    playerInput = raw_input("> ").lower()
    if playerInput == "inventory":
    	showInventory() # This function is defined in the 'inventory.py' file.
        playerAction()
    if playerInput == "store":
    	showStore()
    	playerAction()
    if playerInput == "exitgame":
        print("Are you sure you want to quit? ('yes' or 'no')")
        exitConfirm = raw_input("> ")
        if exitConfirm == "yes":
            print("Exiting the game...")
            exit()
        if exitConfirm == "no":
            print("Will not exit the game.")
            playerAction()
    else:
        print("Invalid command.")
        playerAction()
    # And I'll let Timmy2005 finish the code.


gameStart()
print("Input Command.")
playerAction()
