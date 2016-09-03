# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats into the inventory.py
# These are the stats you start with at the beginning of the game.
import time
from Store import storeStats
from Store import moneyValue
from Store import health_xp
from battleEngine import level_xp

global mana
global level
global money
global xp_level

level = level_xp()
mana = 0
money = moneyValue()
xp_level = 1


def defaultStats():
    global mana
    global playerHealth
    global level
    global xp
    mana = 0
    level = 1
    return mana, playerHealth, level

def showStats():
    storeStats()

def showInventory():
    global xp_level
    global level
    xp_level = xp_level + level * level
    xp_level = xp_level * 100
    xp, playerHealth = health_xp()
    while xp >= 50:
        level = level + 1
        xp = xp - 50
    money = moneyValue()

    print(" ")
    print("     Mana:")
    print("     " + str(mana))
    print(" ")
    print("     Health:")
    print("     " + str(playerHealth))
    print(" ")
    print("     Level:")
    print("     " + str(level))
    print(" ")
    print("     xp:")
    print("     " + str(xp))
    print(" ")
    print("     Money:")
    print("     " + str(money))
    print(" ")
    print"Input command"
    return level, xp