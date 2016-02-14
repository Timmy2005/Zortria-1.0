global beastHealth
global attackOption
global runOption
global playerHealth

import random
import inventory
import time
from inventory import defaultStats
mana, playerHealth, level, xp = defaultStats()

def monsterRandomize():

        global monsterName
        global monsterNameChoice
        global monsterDamage
        global monsterDamageChoice
        global monsterHealth
        global monsterHealthChoice

        monsterHealthChoice = random.randint(7, 16)
        monsterHealth = monsterHealthChoice
        monsterNameChoice = random.randint(1, 3)
        if monsterNameChoice == 1:
                monsterName = "Beast"
        elif monsterNameChoice == 2:
                monsterName = "Spider"
        elif monsterNameChoice == 3:
                monsterName = "Wolf"

def monsterRandomizeDev(): # This is for returning the variables.

        global monsterName
        global monsterNameChoice
        global monsterHealth
        global monsterHealthChoice

        monsterHealthChoice = random.randint(7, 16)
        monsterHealth = monsterHealthChoice
        monsterNameChoice = random.randint(1, 3)
        if monsterNameChoice == 1:
                monsterName = "Beast"
        elif monsterNameChoice == 2:
                monsterName = "Spider"
        elif monsterNameChoice == 3:
                monsterName = "Wolf"

        return monsterName, monsterNameChoice, monsterHealth, monsterHealthChoice

def monsterDamageDecide():
        global monsterDamage
        global monsterDamageChoice
        
        monsterDamageChoice = random.randint(1, 10)
        if monsterDamageChoice <= 10:
                monsterDamage = 1
        elif monsterDamageChoice == 10: # Monster critical hit, basically.
                monsterDamage = 2

def monsterDamageDecideDev(): # This is for returning the variables.
        global monsterDamage
        global monsterDamageChoice
        
        monsterDamageChoice = random.randint(1, 10)
        if monsterDamageChoice <= 10:
                monsterDamage = 1
        elif monsterDamageChoice == 10: # Monster critical hit, basically.
                monsterDamage = 2

def battleInput():
        
        global monsterHealth
        global attackOption
        global playerHealth
        global runOption
        global battleChoice # Renamed 'input1' to 'battleChoice' just to prevent confusion.

        print(" ")
        print("Your HP:")
        print(playerHealth)
        print(monsterName + " HP:")
        print(monsterHealth)
        print("Choices: attack, run")
        
        print("What do you want to do?  ")
        battleChoice = raw_input("> ").lower()
        if battleChoice == "run":
                runChance = random.randint(0, 5)
                if runChance >= 3:
                        print("You got away!")
                        time.sleep(1)
                else:
                        print("Oh no! The beast caught you!")
                        time.sleep(1)
                        if monsterHealth >= 1:
                                monsterDamageDecide()
                                print(" ")
                                print("You took")
                                print(monsterDamage)
                                print("damage.")
                                playerHealth = playerHealth - monsterDamage
                                time.sleep(1)
                                battleInput()

        elif battleChoice == "attack":
                critHitChance = random.randint(0, 10)
                doubleDamage = random.randint(0, 100) # This is just something silly I added. Move along...
                missHitChance = random.randint(0, 10)
                attackDamage = 1
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
                        time.sleep(1)
                        battleInput()
                else:
                        print("You defeated the " + monsterName + "!")
                        time.sleep(1)
        
        else:
                print("Invalid command.")
                time.sleep(1)
                print(" ")
                battleInput()
        
def option():
        global runOption
        global attackOption
        global battleChoice
        
        return runOption, attackOption, battleChoice
