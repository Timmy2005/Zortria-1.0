# This game was made by Timmy2005 and HalfKelp.
#
# FOR COLLABORATORS:
# This is the format for inputting commands:
#
# print("Question here. (ex. What is your name?)")
# <variable> = raw_input("> ")
#
# Do it EXACTLY as shown above. Copy and paste if you need to.

# This file basically pulls all the modules together.

import OSCheck
from gameStartTest import gameStart
from playerInput import *
import inventory
import Store
import gameMove


gameStart()
playerAction()
