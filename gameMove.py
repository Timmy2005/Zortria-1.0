# west = corNumberX - 1   
# east = corNumberX + 1
# north = corNumberY + 1
# south = corNumberX - 1

import random
import battleEngine
from battleEngine import battleInput
monsterX = random.randint(0,10)
monsterY = random.randint(0,10)
running = True
corNumberX = 5
corNumberY = 1
money = 100

def Move():
	print"Movement options: North  South  East  West"
	direction = raw_input(">").lower()
	if direction == "north":
		corNumberY = corNumberY + 1
	if direction == "south":
		corNumberY = corNumberY - 1
	if direction == "east":
		corNumberX = corNumberX + 1
	if direction == "west":
		corNumberX = corNumberX - 1

def monsterMove():
	monsterMove = random.randint(1,4)
	if monsterMove == 1:
		monsterX = monsterX + 1
	if monsterMove == 2:
		monsterX = monsterX - 1
	if monsterMove == 3:
		monsterY = monsterY + 1
	if monsterMove == 4:
		monsterY = monsterY - 1
	
	if monsterX == corNumberX:
		if monsterY == corNumberY:
			battleInput()
			
	corNumX = str(corNumberX)
	corNumY = str(corNumberY)
	print("You are at X:" + corNumX + " Y:" + corNumY)
