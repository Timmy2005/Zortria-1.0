global corNumberX
global corNumberY
import time
import random
from Store import store
from inventory import showInventory
from inventory import showStats
from battleEngine import *
corNumberX = 5
corNumberY = 1


def monsterEncounter(): # I think this would be better than monsterMove for a few reasons. Just an idea, though.
        monsterChance = random.randint(1, 5)
        if monsterChance >= 4:
                monsterRandomize()
                battleInput()

def playerAction():
        global corNumberX
        global corNumberY
        corNumX = str(corNumberX)
        corNumY = str(corNumberY)
        print("You are at X:" + corNumX + " Y:" + corNumY)
        playerInput = raw_input("> ").lower()
        if playerInput == "north":
                if corNumberY == 10:
                        if corNumberX == 3:
                                print"You need a key to go in there."
                                time.sleep(1.5)
                                playerAction()
                        else:
                                print"You can't go there! Those are the dungeon walls."
                                time.sleep(1.5)
                                playerAction()
                corNumberY = corNumberY + 1
                monsterEncounter()
                playerAction()
        elif playerInput == "south": # Yeah! Go 'elif'!
                if corNumberY == 0:
                        print"Don't be silly! You still have a princess to save!"
                        time.sleep(1.5)
                        playerAction()
                else:
                        corNumberY = corNumberY - 1
                        monsterEncounter()
                        playerAction()
        elif playerInput == "east":
                if corNumberX == 10:
                        print"Whoa! You almost fell of the cliff!"
                        time.sleep(1.5)
                        playerAction()
                else:
                        corNumberX = corNumberX + 1
                        monsterEncounter()
                        playerAction()
        elif playerInput == "west":
                if corNumberX == 0:
                        print"You don't want to go in there! That forest doesn't have anything in it"
                        time.sleep(1)
                        playerAction()
                else:
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
                        print("GAME OVER - I don't know why they used you to save the princess.")
                        time.sleep(3)
                        exit()
                elif exitConfirm == "no":
                        print("Will not exit the game.")
                        playerAction()
                else:
                        print("I don't understand that.")
                        print("Will not exit the game.")
                        playerAction()
        elif playerInput == "stats":
                showStats()
                playerAction()
        else:
                print("I don't understand that.")
                playerAction()
