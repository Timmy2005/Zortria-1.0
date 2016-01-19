# This is the format for inputting commands:
#
# print("Question here. (ex. What is your name?)")
# <variable> = raw_input("> ")
#
# Do it EXACTLY as shown above. Copy and paste if you need to.
# You also need 
global corNumberX
global corNumberY

import random
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
from battleEngine import option
corNumberX = 5
corNumberY = 1

def playerAction():
	# This is the 'playerAction' function. It is used for typing commands
	global corNumberX
	global corNumberY

	monsterX, monsterY = monsterMove()
	monsterX2, monsterY2 = monsterMove2()
	if corNumberX == monsterX or corNumberX == monsterX2:
		if corNumberY == monsterY or corNumberY == monsterY2:
			battleInput()
			runOption, attackOption, input1 = option()
			if input1 == runOption:
				direction = random.randint(0,4)
				if direction == 0:
					if corNumberY == 10:
						corNumberY = corNumberY - 1
					else:
						corNumberY = corNumberY + 1
				else:
					if direction == 1:
						if corNumberY == 0:
							corNumberY = corNumberY + 1
						else:
							corNumberY = corNumberY - 1
					else:
						if direction == 2:
							if corNumberX == 10:
								corNumberX = corNumberX - 1
							else:
								corNumberX = corNumberX + 1
						else:
							if corNumberX == 0:
								corNumberX = corNumberX + 1
							else:
								corNumberX = corNumberX - 1 
		playerAction()
			
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
		else:	
			corNumberY = corNumberY + 1
			playerAction()
	else:
		if playerInput == "south":
			if corNumberY == 0:
				print"Don't be silly! You still have a princess to save!"
				time.sleep(1.5)
				playerAction()
			else:
				corNumberY = corNumberY - 1
				playerAction()
		else:
			if playerInput == "east":
				if corNumberX == 10:
					print"Whoa! You almost fell of the cliff!"
					time.sleep(1.5)
					playerAction()
				else:
					corNumberX = corNumberX + 1
					playerAction()
			else:
				if playerInput == "west":
					if corNumberX == 0:
						print"You don't want to go in there! That forest doesn't have anything in it"
						time.sleep(3)
						playerAction()
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
									time.sleep(1)
									print("Exited.")
									exit()
								if exitConfirm == "no":
									print("Will not exit the game.")
									playerAction()
							else:
								if playerInput == "stats":
									showStats()
									playerAction()
								else:
									print("Invalid command.")
									playerAction()
	
	#if monsterX == corNumberX:
	#	if monsterY == corNumberY:
	#		battleInput()
    # And I'll let Timmy2005 finish the code.
def corNumber():
	global corNumberX
	global corNumberY
	
	return corNumberX, corNumberY

gameStart()
corNumberX = 5
corNumberY = 1
#This is from 'gameMove.py'
print("Input Command.")
playerAction()
