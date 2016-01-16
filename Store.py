Sword = False
Bow_an_Arrow = False

print"Store"
print""
if Sword == False:
	print"Sword -- $100"
if Bow_an_Arrow == False:
	print"Bow an Arrow -- $150"
print""
buy = raw_input("Do you want to buy anything today?('yes' or 'no')  ").lower()
if buy == "yes":
	choise = raw_input("What do you want to buy?('Sword','Bow an Arrow' or 'no' if you don't want to buy anything)  ").lower()
	if choise == "bow an arrow":
		print"You just bought a Bow an Arrow!"
		Bow_an_Arrow = True
		
	if choise == "sword":
		print"You just bought a Sword!"
		Sword = True
	
	print"Now your ready to slay the monster and save the princess!"