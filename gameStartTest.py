# This is a module for the beginning of the game.
# Written by HalfKelp.*

import time

def inputPlayerName():
    global playerName
    
    playerName = raw_input("> ")
    print("'" + playerName.title() + ". What a wonderful name!'")

def gameStart():
    print("'Why, hello there!'")
    time.sleep(2)
    print("'It looks like you're a newcomer.'")
    time.sleep(2)
    print("'Now, tell me young one, what is your name?'")
    inputPlayerName()
    time.sleep(2)
    print(" ")
    print("'" + playerName.title() + ", your journey is about to begin!'")
    time.sleep(3)
    print("'You will fight monsters, get a key, and save the princess!'")
    time.sleep(2)
    print("'Do you want to take on the challenge?' ('yes' or 'no')  ")
    beginJourney = raw_input("> ")
    if beginJourney == "yes":
        print("'Alright! Let's go!'")
        time.sleep(2)
    if beginJourney == "no":
        print("'Then I'm afraid we're doomed...'")
        time.sleep(3)
        print("GAME OVER - Didn't even make it past Step 1.")
        quit()
        time.sleep(2)
    print(" ")
    print(" ")
    print("You take a deep breath as you enter a dangerous world full of monsters,")
    time.sleep(3)
    print("knowing that there is no turning back.")
    time.sleep(3)
    print("You look around in the pitch dark forest.")
    time.sleep(2)
    print(" ")
    raw_input("Press enter to continue...")
    print""
