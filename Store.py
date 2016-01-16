Sword = False
BowAndArrow = False
#from gameMove import money
import time

global Sword
global BowAndArrow

def store():

		global Sword
		global BowAndArrow
		
		print"Store"
		print""
		if Sword == False:
			print"Sword -- $100"
		if BowAndArrow == False:
			print"Bow an Arrow -- $150"
			
		print""
		print("Do you want to buy anything today?('yes' or 'no')  ").lower()
		buy = raw_input("> ")
		if buy == "yes":
			print("What do you want to buy?('Sword','Bow an Arrow' or 'no' if you don't want to buy anything)")
			choice = raw_input("> ").lower()
			if choice == "bow an arrow":
				print"You just bought a Bow an Arrow!"
				Bow_an_Arrow = True
				store()
				
				if choice == "sword":
					print"You just bought a Sword!"
					Sword = True
					store()
					if choice == "no":
						print "Now get out there and hammer those monsters!"
						time.sleep(1)
						playerAction()
			if buy == "no":
				print "Now get out there and hammer those monsters!"
				time.sleep(1)
				playerAction()