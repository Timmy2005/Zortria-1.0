# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats into the inventory.py
# These are the stats you start with at the beginning of the game.
import Store
#global Sword
#global BowAndArrow
global mana
global playerHealth
global level
global xp
global money
mana = 0
playerHealth = 20
playerHealthStr = str(playerHealth)
maxPlayerHealth = 20
money = 100

def defaultStats():
        global mana
        global playerHealth
        global level
        global xp
        global money
        mana = 0
        playerHealth = 20
        playerHealthStr = str(playerHealth)
        maxPlayerHealth = 20
        money = 100

#def levelUp():                 NOTE: THIS IS A CONCEPT ONLY.
#        if level = 1:
#                if xp = 200:
#                        level = level + 1
#        if level = 2:
#                if xp = 400:
#                        level = level + 1
#        if level = 3:
#                if xp = 800:
#                        level = level + 1
def storeStats():

	global Sword
	global BowAndArrow
	
	if Sword == True:
		print"Sword"
	
	else:	
		if BowAndArrow == True:
			print"BowAndArrow"
	
		else:
			print"You haven't bought anything yet. Go to the Store to buy stuff"
	
			
	return Sword, BowAndArrow
	
def showStats():
	global mana
	global playerHealth
	global level
	global xp
	global money
	print(" ")
	print("Mana:")
	print(mana)
	print(" ")
	print("Health:")
	print(playerHealth)
	print(" ")
	print("Level:")
	print(level)
	print(" ")
	print("XP:")
	print(xp)
	print(" ")
	print("Money:")
	print(money)
	print(" ")

def showInventory():
	showStats()
	storeStats()
