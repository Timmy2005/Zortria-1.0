global beastHealth
global attackOption
global runOption
global playerHealth
global corNumberY
global corNumberX


import random
import inventory
from inventory import defaultStats
from gameCore import corNumber
beastHealth = 5
attackOption = "attack"
runOption = "run"
mana, playerHealth, level, xp, money = defaultStats()
corNumberY, corNumberX = corNumber()

def battleInput():
	
	global beastHealth
	global attackOption
	global playerHealth
	global runOption
	global corNumberX
	global corNumberY
	
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
				direction = random.randint(0, 4)
				if directoin == 1:
					if corNumberY == 10:
						corNumberY = corNumberY - 1
					else:
						corNumberY = corNumberY + 1 
				else:
					if direction == 2:
						if corNumberY == 0:
							corNumberY = corNumberY + 1
						else:
							corNumberY = corNumberY - 1
					else:
						if direction == 3:
							if corNumberX == 10:
								corNumberX = corNumberX - 1
							else:
								corNumberX = corNumberX + 1
						else:
							if direction == 4:
								if corNumberX == 0:
									corNumberX = corNumberX + 1
								else:
									corNumberX = corNumberX - 1
			else:
				playerHealth = 0


	if input1 == attackOption:
		critHitChance = random.randint(0, 10)
		attackDamage = 1
		if critHitChance >= 9:
			print"Lucky hit!"
			attackDamage = attackDamage + 1
			
			
		beastHealth = beastHealth - attackDamage
		beastHealth2 = str(beastHealth)
		print("You hit him! Now the beast has " + beastHealth + " health now.")
		
