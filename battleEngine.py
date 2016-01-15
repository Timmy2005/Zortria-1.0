import random
beastHealth = 5
playerHealth = 10
attackOption = "attack"
runOption = "run"
print ("A wild beast has appeared!")
print ("Choices: attack  run")
input1 = input("What do you do? ")
#-----------------------------------
if input1 == runOption:
    runChance = random.randint(0, 5)
    if runChance == 5:
        print("You got away!")
#-----------------------------------
if input1 == attackOption:
    critHitChance = random.randint(0, 10)
    attackDamage = 1
    if critHitChance == 10:
        attackDamage = attackDamage + 1
        beastHealth = beastHealth - attackDamage
    else:
        beastHealth = beastHealth - attackDamage
