global beastHealth
global attackOption
global runOption
global playerHealth
global monsterName
global monsterHealth
global monsterHealthxp
global xp
global playerHealthgain
global random_money
global money
global Sword
global BowAndArrow
global using_sword
global using_bow_and_arrow
global level

import random
import time


monsterName = "unknown"
monsterHealth = "8"
monsterHealthxp = 0
xp = 0
playerHealth = 20
playerHealthgain = 0
random_money = 0
money = 100
Sword = False
BowAndArrow = False
using_bow_and_arrow = False
using_sword = False
level = 1

# I defined monsterName as unknown so it could transfer to other functions,
# but monsterRandomize changes it before the battle.
# I did the same thing for monsterHealth and monsterHealthxp.

def level_xp():
    global level
    return level

def monsterRandomize():
    global monsterName
    global monsterNameChoice
    global monsterDamage
    global monsterDamageChoice
    global monsterHealth
    global monsterHealthChoice
    global monsterHealthxp
    global playerHealthgain

    monsterHealthChoice = random.randint(7, 16)
    monsterHealth = monsterHealthChoice
    monsterNameChoice = random.randint(1, 5)
    if monsterNameChoice == 1:
        monsterName = "Beast"
    elif monsterNameChoice == 2:
        monsterName = "Spider"
    elif monsterNameChoice == 3:
        monsterName = "Wolf"
    elif monsterNameChoice == 4:
        monsterName = "Slime"

    monsterHealthxp = monsterHealth
    monsterHealthxp = monsterHealthxp * 10
    playerHealthgain = monsterHealth

def monsterRandomizeDev():  # This is for returning the variables.

    global monsterName
    global monsterNameChoice
    global monsterHealth
    global monsterHealthChoice

    monsterHealthChoice = random.randint(7, 16)
    monsterHealth = monsterHealthChoice
    monsterNameChoice = random.randint(1, 5)
    if monsterNameChoice == 1:
        monsterName = "Beast"
    elif monsterNameChoice == 2:
        monsterName = "Spider"
    elif monsterNameChoice == 3:
        monsterName = "Wolf"
    elif monsterNameChoice == 4:
        monsterName = "Slime"
    elif monsterNameChoice == 5:
        monsterName = ""

    return monsterName, monsterNameChoice, monsterHealth, monsterHealthChoice

def monsterDamageDecide():
    global monsterDamage
    global monsterDamageChoice

    monsterDamageChoice = random.randint(1, 10)
    if monsterDamageChoice < 10:
        monsterDamage = random.randint(2,5)
    elif monsterDamageChoice == 10:  # Monster critical hit, basically.
        monsterDamage = random.randint(3, 7)

def monsterDamageDecideDev():  # This is for returning the variables.
    global monsterDamage
    global monsterDamageChoice

    monsterDamageChoice = random.randint(1, 10)
    if monsterDamageChoice < 10:
        monsterDamage = random.randint(2, 5)
    elif monsterDamageChoice == 10:  # Monster critical hit, basically.
        monsterDamage = random.randint(3, 7)

    monsterDamage = monsterDamage + level

def use_weapons():
    global Sword
    global BowAndArrow
    global using_sword
    global using_bow_and_arrow
    if Sword == True and BowAndArrow == True:
        weapons_choice = raw_input("Do you want to use bow and arrow or your sword?('sword' or 'bow and arrow')").lower()
        if weapons_choice == "sword":
            print"Using sword for this battle."
            using_sword = True
        elif weapons_choice == "bow and arrow":
            print"Using bow and arrow for this battle."
            using_bow_and_arrow = True


def battleInput():
    global monsterHealth
    global attackOption
    global playerHealth
    global runOption
    global battleChoice  # Renamed 'input1' to 'battleChoice' just to prevent confusion.
    global monsterName
    global monsterHealthxp
    global xp
    global playerHealthgain
    global random_money
    global using_sword
    global using_bow_and_arrow
    print(" ")
    print("Your HP:")
    print(playerHealth)
    print(monsterName + " HP:")
    print(monsterHealth)
    print""
    if playerHealth <= 3:
        print"WARNING: You are running low on health."
        print""
        time.sleep(2)
    print("Choices: attack, run")

    print("What do you want to do?  ")
    battleChoice = raw_input("> ").lower()
    if battleChoice == "run":
        runChance = random.randint(0, 5)
        if runChance >= 3:
            print("You got away!")
            time.sleep(1)
        else:
            print("Oh no! The " + monsterName + " caught you!")
            time.sleep(1)
            if monsterHealth >= 1:
                monsterDamageDecide()
                print(" ")
                print("You took")
                print(monsterDamage)
                print("damage.")
                if playerHealth < 1:
                    print""
                    print"GAME OVER -- You ran out of lives."
                playerHealth = playerHealth - monsterDamage
                time.sleep(1)
                battleInput()

    elif battleChoice == "attack":
        critHitChance = random.randint(0, 10)
        doubleDamage = random.randint(0, 10)  # This is just something silly I added. Move along...
        missHitChance = random.randint(0, 10)
        attackDamage = random.randint(1,4)

        if Sword == True and BowAndArrow == True:
            if using_sword == True:
                attackDamage = attackDamage + 1
            elif using_bow_and_arrow == True:
                attackDamage = attackDamage + 2
        elif Sword == True:
            attackDamage = attackDamage + 1
        elif BowAndArrow == True:
            attackDamage = attackDamage + 2


        if doubleDamage == 100:
            attackDamage = attackDamage * 2
        if missHitChance == 10:
            print(monsterName + " dodged the attack.")
            attackDamage = 0

        monsterHealth = monsterHealth - attackDamage
        if missHitChance < 10:
            print(" ")
            print(monsterName + " took")
            print(attackDamage)
            print("damage.")
        if critHitChance == 10 and missHitChance < 10:
            time.sleep(1)
            attackDamage = attackDamage + 1
            print("CRITICAL HIT! +1 Damage.")
        if doubleDamage == 100:
            time.sleep(1)
            print("DOUBLE DAMAGE! x2 Damage.")
        time.sleep(1)

        if monsterHealth >= 1:
            monsterDamageDecide()
            print(" ")
            print("You took")
            print(monsterDamage)
            print("damage.")
            playerHealth = playerHealth - monsterDamage
            if playerHealth < 1:
                print""
                print"GAME OVER -- You ran out of lives."
                quit()

            time.sleep(1)
            battleInput()
        else:
            print("You defeated the " + monsterName + "!")
            random_money = random.randint(50, 151)
            print"You got " + str(monsterHealthxp) + " xp."
            print"You got $" + str(random_money) + "."
            xp = xp + monsterHealthxp
            playerHealth = playerHealth + playerHealthgain
            playerHealthgain = playerHealthgain - playerHealthgain
            monster_money()

    else:
        print("Invalid command.")
        time.sleep(1)
        print(" ")
        battleInput()

def playerHealthDev():
    global playerHealth
    return playerHealth

def xp_add():
    global xp
    return xp

def monster_money():
    global random_money
    global money
    money = money + random_money
    random_money = 0
    return money

def sword_money():
    global  money
    money = money - 100

def bow_and_arrow_money():
    global money
    money = money - 150

def Sword_change():
    global Sword
    Sword = True

def BowAndArrow_change():
    global BowAndArrow
    BowAndArrow = True

def weapons_return():
    global Sword
    global BowAndArrow
    return Sword, BowAndArrow

def money_return():
    global money
    return money

def treasure():
    global money

    money_choice = random.randint(20, 40)
    print"You found $" + str(money_choice) + " in a treasure chest!"
    money = money + money_choice