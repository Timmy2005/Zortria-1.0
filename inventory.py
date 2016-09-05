# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats into the inventory.py
# These are the stats you start with at the beginning of the game.
import time
from Store import storeStats
from battleEngine import monster_money
from Store import health_xp
from battleEngine import level_xp
from battleEngine import xp_to_level
from battleEngine import xp_add

global mana
global level
global xp_level

level = level_xp()
mana = 0


def defaultStats():
    global mana
    global level
    global xp
    mana = 0
    return mana, level


def showStats():
    storeStats()


def showInventory():
    global xp_level
    global level
    global money

    money = monster_money()
    playerHealth = health_xp()
    level = xp_to_level()
    xp = xp_add()

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