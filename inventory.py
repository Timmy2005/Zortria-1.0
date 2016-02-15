# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats into the inventory.py
# These are the stats you start with at the beginning of the game.
from Store import storeStats
from Store import moneyValue
from battleEngine import xp_add
from battleEngine import playerHealthDev

global mana
global playerHealth
global level
global xp
global money
level = 1
mana = 0
money = moneyValue()
xp = xp_add()
playerHealth = playerHealthDev()


def defaultStats():
    global mana
    global playerHealth
    global level
    global xp
    mana = 0
    level = 1
    return mana, playerHealth, level


def showInventory():
    storeStats()


def showStats():
    global mana
    global playerHealth
    global level
    global xp
    global money
    money = moneyValue()
    xp = xp_add()
    playerHealth = playerHealthDev()
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
    print("xp:")
    print(xp)
    print(" ")
    print("Money:")
    print(money)
    print(" ")
