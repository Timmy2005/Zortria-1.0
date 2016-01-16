import random
beastHealth = 5
playerHealth = 10
running = True
attackOption = "attack"
runOption = "run"
print ("A wild beast has appeared!")
print ("Choices: attack, run or go to the store")

while running:

	input1 = raw_input("What do you want to do?  ").lower()
	if input1 == runOption:
		runChance = random.randint(0, 5)
		if runChance == 5:
			print("You got away!")
			
		else:
			print"Oh no! The beast caught you!"
    		running = False


	if input1 == attackOption:
		critHitChance = random.randint(0, 10)
		attackDamage = 1
		if critHitChance == 10:
			print"Lucky hit!"
			attackDamage = attackDamage + 1
			
			
		beastHealth = beastHealth - attackDamage
		print("You hit him! Beast has" + beastHealth + "health now.")
		
		if beastHealth == 0:
			running = False
	if input1 == "store":
		import Store
		
	if input1 == "quit":
		running = False