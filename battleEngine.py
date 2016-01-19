global beastHealth
global attackOption
global runOption
global playerHealth
global corNumberY
global corNumberX

import random
import inventory
from inventory import defaultStats
beastHealth = 5
attackOption = "attack"
runOption = "run"
mana = defaultStats()
playerHealth = defaultStats()
playerHealthStr = defaultStats()

def decideBeastHealth():
        
        global beastHealth
        global beastHealthStr
        global maxBeastHealth
        global maxBeastHealthStr
        
        beastHealth = random.randint(7, 16)
        maxBeastHealth = beastHealth

def battleRun():
        global battleRunning
        battleRunning = True

def battleInput():
        battleRunning = battleRun()
        global beastHealth
        global attackOption
        global playerHealth
        global runOption
        global corNumberX
        global corNumberY
        battleRunning = True
        
        if battleRunning == True:
                
                print ("A wild beast has appeared!")
                print ("Your HP: ")
                print (playerHealth)
                print ("Beast HP: ")
                print (beastHealth)
                print ("Choices: attack, run")
                battleInput = raw_input("What do you want to do?  ").lower()
                if battleInput == runOption:
                        runChance = random.randint(0, 5)
                        if runChance == 5:
                                print("You got away!")
                        if runChance == 4:
                                print("You got away!")
                                battleRunning = False
                        else:
                                print"Oh no! The beast caught you!"
                                battleInput()
                
                
                if battleInput == attackOption:
                        critHitChance = random.randint(0, 10)
                        attackDamage = 1
                        beastHealth = beastHealth - attackDamage
                        print("Beast took")
                        print(attackDamage)
                        print("damage.")
                        if critHitChance >= 9:
                                print"CRITICAL HIT!"
                                attackDamage = attackDamage + 1
                        battleInput()
