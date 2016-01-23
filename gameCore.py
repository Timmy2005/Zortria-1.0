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
	global corNumberX
	global corNumberY

# def corNumber(): # TIP: 'cor' is short for 'coordinates'.
#         global corNumberX
#         global corNumberY
#         corNumberX = 5
#         corNumberY = 1
#         return corNumberX, corNumberY
# #
# #def monsterEncounter(): # I think this would be better than monsterMove for a few reasons. Just an idea, though.
#         monsterChance = random.randint(1, 5)
#         if monsterChance == 5:
#                 battleInput()
	monsterX, monsterY = monsterMove()
	if corNumberX == monsterX:
		if corNumberY == monsterY:
			print"The wild beast has appeared!"
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
			corNumberY = corNumberY + 1
			playerAction()
	elif playerInput == "south": # Yeah! Go 'elif'!
		if corNumberY == 0:
			print"Don't be silly! You still have a princess to save!"
			time.sleep(1.5)
			playerAction()
		else:
			corNumberY = corNumberY - 1
			playerAction()
	elif playerInput == "east":
		if corNumberX == 10:
			print"Whoa! You almost fell of the cliff!"
			time.sleep(1.5)
			playerAction()
		else:
                        corNumberX = corNumberX + 1
			playerAction()
	elif playerInput == "west":
		if corNumberX == 0:
			print"You don't want to go in there! That forest doesn't have anything in it"
			time.sleep(3)
			playerAction()
		corNumberX = corNumberX - 1
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
			print("GAME OVER -- I don't see why they used you to save the princess.")
			time.sleep(3)
			exit()
		elif exitConfirm == "no":
			print("Will not exit the game.")
			playerAction()
                else:
                        print("Invalid answer.")
                        print("Will not exit the game.")
                        playerAction()
	elif playerInput == "stats":
		showStats()
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
playerAction()
