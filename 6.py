import sys
import math

BALL_HIGHT   = 4
MONEY        = 0
POSITION_X   = 260
POSITION_Y   = 260 
RUNNING   	 = True
RUNNING2	 = True

print"Type 1 to make it bigger($10) and 2 to make it a lot bigger($20)"
raw_input("Type 'start' to start")

def ask():
	a = raw_input()
	if a == 1:
		BALL_HIGHT = BALL_HIGHT + 5
		MONEY = MONEY - 10	
	if ask() == 2:
		BALL_HIGHT = BALL_HIGHT + 10
		MONEY = MONEY - 20
	if ask() == 3:
		RUNNING = False
		sys.exit()


while RUNNING:
	
		MONEY = MONEY + BALL_HIGHT

		print(MONEY)
		print(BALL_HIGHT)
		
		a = raw_input()
		if a == "1":
			BALL_HIGHT = BALL_HIGHT + 5
			MONEY = MONEY - 10	
		if a == "2":
			BALL_HIGHT = BALL_HIGHT + 10
			MONEY = MONEY - 20
		if a == "3":
			RUNNING = False
			sys.exit()
