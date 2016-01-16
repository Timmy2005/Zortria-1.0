# This is a stats and inventory concept.
# Written by HalfKelp.

# I integrated stats.py into the inventory.py
# These are the stats you start with at the beginning of the game.
def defaultStats():
    mana = 0
    health = 20
    level = 1
    xp = 0

def showInventory():
    if BowAndArrow == True:
        print("Bow & Arrow")
    if Sword == True:
        print("Sword")

def showStats():
    print(" ")
    print("Mana:")
    print(mana)
    print(" ")
    print("Health:")
    print(health)
    print(" ")
    print("Level:")
    print(level)
    print(" ")
    print("XP:")
    print(xp)
    print(" ")
