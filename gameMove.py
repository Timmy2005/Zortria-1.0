# west = corNumberX - 1   
# east = corNumberX + 1
# north = corNumberY + 1
# south = corNumberX - 1


import random
monsterX = random.randint(0,10)
monsterY = random.randint(0,10)

global monsterX
global monsterY

def monsterMove():
	
	global monsterX
	global monsterY
	
	monsterMove = random.randint(1,4)
	if monsterMove == 1:
		monsterX = monsterX + 1
	if monsterMove == 2:
		monsterX = monsterX - 1
	if monsterMove == 3:
		monsterY = monsterY + 1
	if monsterMove == 4:
		monsterY = monsterY - 1
		
	return monsterX, monsterY