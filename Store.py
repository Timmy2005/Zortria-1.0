global Sword
global BowAndArrow
global money

import time
from battleEngine import monster_money
from battleEngine import sword_money
from battleEngine import bow_and_arrow_money
from battleEngine import playerHealthDev
from battleEngine import BowAndArrow_change
from battleEngine import Sword_change
from battleEngine import weapons_return
from battleEngine import bow_and_arrow_upgrade
from battleEngine import sword_upgrade

money = monster_money()

def store():
    global Sword
    global BowAndArrow
    global money

    money = monster_money()

    Sword, BowAndArrow = weapons_return()
    print"   Store"
    time.sleep(1)
    print""
    if Sword == True and BowAndArrow == True:
        print"  Sorry, we're out of stock!"
        upgrade()
    if Sword == False:
        print"   Sword -- $100 -- +1 attack damage"
        time.sleep(1)
    if BowAndArrow == False:
        print"   Bow an Arrow -- $150 -- +2 attack damage"
        time.sleep(1)

    print("   You have $" + str(money))
    time.sleep(1.5)
    print""
    print("   Do you want to buy anything today?('yes' or 'no')  ")
    buy = raw_input("   > ").lower()
    if buy == "yes":
        print("   What do you want to buy?('Sword','Bow and Arrow' or 'nothing')")
        choice = raw_input("   > ").lower()
        if choice == "bow and arrow":
            if money >= 150:
                print"   You just bought a Bow and Arrow!"
                BowAndArrow_change()
                bow_and_arrow_money()
                time.sleep(1)
                print""
                print"Input Command"
            else:
                print("   You don't have enough money.")
                time.sleep(1)
                print""
                print"Input Command"
        if choice == "sword":
            if money >= 100:
                print"   You just bought a Sword!"
                Sword_change()
                sword_money()
                time.sleep(1)
                print""
                print"Input Command"
            else:
                print"   You don't have enough money."
                time.sleep(1)
                print""
                print"Input Command"
        if choice == "nothing":
            print "   Now get out there and hammer those monsters!"
            time.sleep(1)
            print""
            print"Input Command"

    if buy == "no":

        upgrade()
        print "   Now get out there and hammer those monsters!"
        time.sleep(1)
        print""
        print"Input Command"


def storeStats():

    Sword, BowAndArrow = weapons_return()
    if Sword == True and BowAndArrow == True:
        print"  Sword"
        print"  Bow and Arrow"

    else:
        if Sword == True:
            print"  Sword"

            time.sleep(1)

        else:
            if BowAndArrow == True:
                print"  Bow and Arrow"
                print""
                time.sleep(1)

            else:
                print"  You haven't bought anything yet. Go to the Store to buy stuff"

    return Sword, BowAndArrow


def health_xp():#This function is for returning variables
    playerHealth = playerHealthDev()
    return playerHealth


def upgrade():
    Sword, BowAndArrow = weapons_return()
    if Sword == True and BowAndArrow == True:
        upgrade = raw_input("   Do you want to upgrade anything today?('yes' or'no')")
        if upgrade == "yes":
            print("   What do you want to upgrade?('Sword','Bow and Arrow' or 'nothing')")
            choice = raw_input("   > ").lower()
            if choice == "bow and arrow":
                bow_and_arrow_upgrade()

            elif choice == "sword".lower():
                sword_upgrade()

            else:
                print"  Invalid Command."
                store()

        elif upgrade == "no":
            print "   Now get out there and hammer those monsters!"
            time.sleep(1)
            print""
            print"Input Command"

        else:
            print"  Invalid Command."
            store()


    elif Sword == True:
        print"   Do you want to upgrade your sword?('yes' or 'no')"
        choice = raw_input("   > ").lower()
        if choice == "yes":
            sword_upgrade()

        elif choice == "no":
            print "   Now get out there and hammer those monsters!"
            time.sleep(1)
            print""
            print"Input Command"

        else:
            print"  Invalid Command."
            store()

    elif BowAndArrow == True:
        print"   Do you want to upgrade your bow and arrow?('yes' or 'no')"
        choice = raw_input("  > ").lower()
        if choice == "yes":
            bow_and_arrow_upgrade()

        elif choice == "no":
            print "   Now get out there and hammer those monsters!"
            time.sleep(1)
            print""
            print"Input Command"

        else:
            print"  Invalid Command."
            store()
    else:
        print "   Now get out there and hammer those monsters!"
        time.sleep(1)
        print""
        print"Input Command"
