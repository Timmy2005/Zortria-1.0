global beastHealth
global attackOption
global runOption
global playerHealth

import random
import inventory
from inventory import defaultStats
beastHealthChoise = random.randint(7, 16)
beastHealth = beastHealthChoise
attackOption = "attack"
runOption = "run"
mana, playerHealth, level, xp = defaultStats()

def battleInput():
	
	global beastHealth
	global attackOption
	global playerHealth
	global runOption
	global input1

	print("Your HP:")
	print(playerHealth)
	print("Beast HP:")
	print(beastHealth)
	print("Choices: attack, run")
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
			print"CRITICAL HIT!"
			attackDamage = attackDamage + 1
				
		beastHealth = beastHealth - attackDamage
		attackDamageStr = str(attackDamage)
		beastHealthStr = str(beastHealth)
		print("Beast took " + attackDamageStr + " damage.")
		print("Beast has " + beastHealthStr + " HP.")
	if beastHealth >= 1:
		battleInput()
def option():
	global runOption
	global attackOption
	global input1
	
	return runOption, attackOption, input1
