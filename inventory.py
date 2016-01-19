# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats into the inventory.py
# These are the stats you start with at the beginning of the game.
import Store
from Store import storeStats
from Store import moneyValue
global mana
global playerHealth
global level
global xp
global money
mana = 0
playerHealth = 20
level = 1
xp = 0
money = moneyValue()


def defaultStats():
	global mana
	global playerHealth
	global level
	global xp
	global money
	mana = 0
	playerHealth = 20
	level = 1
	xp = 0
	return mana, playerHealth, level, xp

def showInventory():
	
	storeStats()
	
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
	
