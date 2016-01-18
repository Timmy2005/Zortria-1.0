# west = corNumberX - 1   
# east = corNumberX + 1
# north = corNumberY + 1
# south = corNumberX - 1

global monsterX
global monsterY
global monsterX2
global monsterY2

import random
monsterX = random.randint(0,10)
monsterY = random.randint(0,10)
monsterX2 = random.randint(0,10)
monsterY2 = random.randint(0,10)

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
	
def monsterMove2():
	global monsterX2
	global monsterY2
	
	monsterMove = random.randint(1,4)
	if monsterMove == 1:
		monsterX2 = monsterX2 + 1
	if monsterMove == 2:
		monsterX2 = monsterX2 - 1
	if monsterMove == 3:
		monsterY2 = monsterY2 + 1
	if monsterMove == 4:
		monsterY2 = monsterY2 - 1
		
	return monsterX2, monsterY2