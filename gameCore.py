# This is the format for inputting commands:
#
# print("Question here. (ex. What is your name?)")
# <variable> = raw_input("> ")
#
# Do it EXACTLY as shown above. Copy and paste if you need to.
# You also need 

from gameStartTest import gameStart
import inventory
import Store
import gameMove
from gameMove import monsterMove
from Store import store
from inventory import showInventory
import battleEngine
from battleEngine import battleInput
corNumberX = 5
corNumberY = 1

global corNumberX
global corNumberY

def playerAction():
	# This is the 'playerAction' function. It is used for typing commands
	global corNumberX
	global corNumberY

	monsterX, monsterY = monsterMove()
	monsterMove()
	if monsterX == corNumberX:
		if monsterY == corNumberY:
			battleInput()
			
	corNumX = str(corNumberX)
	corNumY = str(corNumberY)
	print("You are at X:" + corNumX + " Y:" + corNumY)
	
	playerInput = raw_input("> ").lower()
	if playerInput == "north":
		corNumberY = corNumberY + 1
		playerAction()
	else:
		if playerInput == "south":
			corNumberY = corNumberY - 1
			playerAction()
		else:
			if playerInput == "east":
				corNumberX = corNumberX + 1
				playerAction()
			else:
				if playerInput == "west":
					corNumberX = corNumberX - 1
					playerAction()
				else:
					if playerInput == "inventory":
						showInventory() # This function is defined in the 'inventory.py' file.
						playerAction()
					else:
						if playerInput == "store":
							store()
							playerAction()
						else:
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
	
	#if monsterX == corNumberX:
	#	if monsterY == corNumberY:
	#		battleInput()
    # And I'll let Timmy2005 finish the code.



gameStart()
corNumberX = 5
corNumberY = 1
#This is from 'gameMove.py'
print("Input Command.")
playerAction()
