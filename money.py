global money
global moneyAm
global lvl
global extra1
global extra2
global moneyTotal1
global moneyTotal2
money = 0
moneyAm = 0.5
lvl = 0
extra1 = 0
extra2 = 0
moneyTotal1 = 0
moneyTotal2 = 0

def moneyMaker():
	global money
	global moneyAm
	global lvl
	global extra1
	global extra2
	global moneyTotal1
	global moneyTotal2
	
	moneyAm = moneyAm + lvl
	money = money + moneyAm
	print(money)
	print(moneyAm)
	
	a = raw_input()
	if a == "1":
		if money >= 10 + extra1:
			lvl = lvl + 0.05
			moneyTotal1 = moneyTotal1 + 10
			moneyTotal1 = moneyTotal1 + extra1
			money = money - moneyTotal1
			moneyTotal1 = moneyTotal1 - 10
			moneyTotal1 = moneyTotal1 - extra1
			extra1 = extra1 + 1
			moneyMaker()
		else:
			moneyMaker()
			
	elif a == "2":
		if money >= 20 + extra2:
			lvl = lvl + 0.1
			moneyTotal2 = moneyTotal2 + 20
			moneyTotal2 = moneyTotal2 + extra2
			money = money - moneyTotal2
			moneyTotal2 = moneyTotal2 - 10
			moneyTotal2 = moneyTotal2 - extra2
			extra2 = extra2 + 2
			moneyMaker()
		else:
			moneyMaker()
	elif a == "exit":
		quit()
		
	else:
		moneyMaker()		
moneyMaker()