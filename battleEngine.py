global beastHealth
global attackOption
global runOption
global playerHealth

import random
import inventory
import time
from inventory import defaultStats
attackOption = "attack"
runOption = "run"
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
        monsterDamageChoice = random.randint(1, 10)
        if monsterDamageChoice <= 10:
                monsterDamage = 1
        elif monsterDamageChoice == 10:
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
        if battleChoice == runOption:
                runChance = random.randint(0, 5)
                if runChance >= 3:
                        print("You got away!")
                else:
                        print("Oh no! The beast caught you!")

        if battleChoice == attackOption:
                critHitChance = random.randint(0, 10)
                doubleDamage = random.randint(0, 100) # This is just something silly I added.
                attackDamage = 1
                if critHitChance >= 9: # Critical hits are supposed to be uncommon.
                        print("CRITICAL HIT! +1 Damage.")
                        attackDamage = attackDamage + 1
                if doubleDamage == 100:
                        print("DOUBLE DAMAGE!")
                        attackDamage = attackDamage * 2
                monsterHealth = monsterHealth - attackDamage
                print(" ")
                print(monsterName + " took")
                print(attackDamage)
                print("damage.")
                time.sleep(1)
                
                if monsterHealth >= 1:
                        battleInput()
                else:
                        print("You defeated the " + monsterName + "!")
                        time.sleep(1)
                        print(" ")
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
