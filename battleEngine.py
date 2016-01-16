import random
beastHealth = 5
playerHealth = 10
running = True
attackOption = "attack"
runOption = "run"

<<<<<<< HEAD
def battleInput():
	print ("The wild beast has appeared!")
	print ("Choices: attack, run")
=======
while running:

>>>>>>> fdda31d1a3f65e4fef1e971a38f2295c50039f99
	input1 = raw_input("What do you want to do?  ").lower()
	if input1 == runOption:
		runChance = random.randint(0, 5)
		if runChance == 5:
			print("You got away!")
		if runCance == 4:
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
<<<<<<< HEAD
		beastHealth2 = str(beastHealth)
		print("You hit him! Now the beast has " + beastHealth2 + " health now.")
=======
		print("You hit him! Beast has" + beastHealth + "health now.")
		
		if beastHealth == 0:
			running = False
	if input1 == "store":
		import Store
		
	if input1 == "quit":
		running = False
>>>>>>> fdda31d1a3f65e4fef1e971a38f2295c50039f99
