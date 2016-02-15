# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats into the inventory.py
# These are the stats you start with at the beginning of the game.
import time
from Store import storeStats
from Store import moneyValue
from battleEngine import xp_add
from battleEngine import playerHealthDev

global mana
global playerHealth
global level
global xp
global money
global xp_level

level = 1
mana = 0
money = moneyValue()
xp = xp_add()
playerHealth = playerHealthDev()
xp_level = 1


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
    global xp_level

    xp_level = xp_level + level * level
    xp_level = xp_level * 100
    xp = xp_add()
    if xp >= 200:
        level = level + 1
        xp = xp - 200
    money = moneyValue()
    playerHealth = playerHealthDev()

    print(" ")
    print("     Mana:")
    print("     " + str(mana))
    time.sleep(2)
    print(" ")
    print("     Health:")
    print("     " + str(playerHealth))
    time.sleep(2)
    print(" ")
    print("     Level:")
    print("     " + str(level))
    time.sleep(2)
    print(" ")
    print("     xp:")
    print("     " + str(xp))
    time.sleep(2)
    print(" ")
    print("     Money:")
    print("     " + str(money))
    print(" ")
    time.sleep(3)
    print"Input command"