# This game was made by Timmy2005 and HalfKelp.
#
# FOR COLLABORATORS:
# This is the format for inputting commands:
#
# print("Question here. (ex. What is your name?)")
# <variable> = raw_input("> ")
#
# Do it EXACTLY as shown above. Copy and paste if you need to.

global corNumberX
global corNumberY

import time
from gameStartTest import gameStart
import inventory
import Store
import gameMove
from gameMove import monsterMove
from gameMove import monsterMove2
from Store import store
from inventory import showInventory
from inventory import showStats
from battleEngine import battleInput

def corNumber(): # TIP: 'cor' is short for 'coordinates'.
        global corNumberX
        global corNumberY
        corNumberX = 5
        corNumberY = 1
        return corNumberX, corNumberY

def monsterEncounter(): # I think this would be better than monsterMove for a few reasons. Just an idea, though.
        monsterChance = random.randint(1, 5)
        if monsterChance == 5:
                battleInput()

def playerAction():
        # This is the 'playerAction' function. It is used for typing commands
        global corNumberX
        global corNumberY
                        
        corNumX = str(corNumberX)
        corNumY = str(corNumberY)
        print("You are at X:" + corNumX + " Y:" + corNumY)
        print("Input Command. (Type 'help' for list of commands.")
        
        playerInput = raw_input("> ").lower()
        if playerInput == "north":
                if corNumberY == 10:
                        if corNumberX == 3:
                                print"You need a key to go in there."
                        else:
                                print"You can't go there! Those are the dungeon walls."
                                time.sleep(1)
                                playerAction()
                else:
                        corNumberY = corNumberY + 1
                        monsterEncounter()
                        playerAction()
        elif playerInput == "south": # Ah, good ol' 'elif' function. Way better than 'else: else: else:'.
                if corNumberY == 0:
                        print"Don't be silly! You still have a princess to save!"
                        time.sleep(1)
                        playerAction()
                else:
                        corNumberY = corNumberY - 1
                        monsterEncounter()
                        playerAction()
        elif playerInput == "east":
                if corNumberX == 10:
                        print"Whoa! You almost fell of the cliff"
                else:
                        corNumberX = corNumberX + 1
                        monsterEncounter()
                        playerAction()
        elif playerInput == "west":
                corNumberX = corNumberX - 1
                monsterEncounter()
                playerAction()
        elif playerInput == "inventory":
                showInventory() # This function is defined in the 'inventory.py' file.
                playerAction()
        elif playerInput == "store":
                store()
                playerAction()
        elif playerInput == "exitgame":
                print("Are you sure you want to quit? ('yes' or 'no')")
                exitConfirm = raw_input("> ")
                if exitConfirm == "yes":
                        print("Exiting the game...")
                        time.sleep(1)
                        print("GAME OVER - Wow, why did they pick you to save the Princess?")
                        time.sleep(2)
                        exit()
                if exitConfirm == "no":
                        print("Will not exit the game.")
                        playerAction()
        elif playerInput == "stats":
                showStats()
                playerAction()
        else:
                print("Invalid command.")
                playerAction()
        
    # And I'll let Timmy2005 finish the code.

gameStart()
corNumberX = 5
corNumberY = 1
#This is from 'gameMove.py'
playerAction()
