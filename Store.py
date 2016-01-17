global Sword
global BowAndArrow

Sword = False
BowAndArrow = False
#from gameMove import money
import time



def store():

		global Sword
		global BowAndArrow
				
		print"Store"
		time.sleep(1.5)
		print""
		if Sword == False:
			print"Sword -- $100"
			time.sleep(1.5)
		if BowAndArrow == False:
			print"Bow an Arrow -- $150"
			time.sleep(1.5)
			
		print""
		print("Do you want to buy anything today?('yes' or 'no')  ").lower()
		buy = raw_input("> ")
		if buy == "yes":
			print("What do you want to buy?('Sword','Bow and Arrow' or 'nothing')")
			choice = raw_input("> ").lower()
			if choice == "bow and arrow":
				print"You just bought a Bow and Arrow!"
				BowAndArrow = True
				
				if choice == "sword":
					print"You just bought a Sword!"
					Sword = True
					if choice == "nothing":
						print "Now get out there and hammer those monsters!"
						time.sleep(1)
						playerAction()
			if buy == "no":
				print "Now get out there and hammer those monsters!"
				time.sleep(1)
				playerAction()
			
			return Sword, BowAndArrow