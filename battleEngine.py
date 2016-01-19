global beastHealth
global attackOption
global runOption
global playerHealth
#global corNumberY
#global corNumberX


import random
import inventory
from inventory import defaultStats
#from gameCore import corNumber
beastHealth = 5
attackOption = "attack"
runOption = "run"
mana, playerHealth, level, xp = defaultStats()
#corNumberY, corNumberX = corNumber()

def battleInput():
	
	global beastHealth
	global attackOption
	global playerHealth
	global runOption
	global input1
	#global corNumberX
	#global corNumberY
	
	print ("The wild beast has appeared!")
	print ("Choices: attack, run")
	input1 = raw_input("What do you want to do?  ").lower()
	if input1 == runOption:
		runChance = random.randint(0, 5)
		if runChance == 5:
			print("You got away!")
		if runChance == 4:
			print("You got away!")
			
		
			
		else:
			print"Oh no! The beast caught you!"
			getAway = random.randint(0, 5)
			if getAway >= 3:
				print"The beast hit you!"
				print"But you got away"
				playerHealth = playerHealth - 3
				print(playerHealth)

			else:	
				playerHealth = 0


	if input1 == attackOption:
		critHitChance = random.randint(0, 10)
		attackDamage = 1
		if critHitChance >= 7:
			print"Lucky hit!"
			attackDamage = attackDamage + 1
				
		beastHealth = beastHealth - attackDamage
		beastHealth2 = str(beastHealth)
		print("You hit him! Now the beast has " + beastHealth2 + " health now.")

def option():
	global runOption
	global attackOption
	global input1
	
	return runOption, attackOption, input1