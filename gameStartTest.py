# This is a module for the beginning of the game.
# Written by HalfKelp.
import time

def inputPlayerName():
    global playerName
    
    playerName = raw_input("> ")
    if playerName == "HalfKelp" or playerName == "Timmy2005":
        print ("'Hello " + playerName + ". You must be the game creator!'")
    if playerName == "Cave Johnson":
        print("'Shouldn't you be making lemon grenades?'")
    if playerName == "Gabe Newell":
        print("'STEAM SALES!!!'")
    if playerName == "GLaDOS":
        print("'The cake is a lie!'")
    if playerName == "Pewdiepie":
        print("'BRO FIST!'")
    if playerName == "Fart":
        print("'Uh oh, a 5-year-old is playing the game!'")
    if playerName == "No Name":
        print("'No Name? I'll just call you Bob.'")
        playerName = "Bob"
    if playerName == "MLG PRO":
        print("'DORITOS MTN DEW SWAG YOLO ILLUMINATI 360-NOSCOPE.'")
    if playerName == "Stanford Pines":
        print("'IT'S THE AUTHOR OF THE JOURNALS!'")
    if playerName == "Bill Cipher":
        print("'THE UNIVERSE IS AN ILLUSION!'")
    else:
        print("'" + playerName + ". What a wonderful name!'")

def gameStart():
    print("'Why, hello there!'")
    time.sleep(2)
    print("'It looks like you're a newcomer.'")
    time.sleep(2)
    print("'Now, tell me young one, what is your name?'")
    inputPlayerName()
    time.sleep(1)
    print(" ")
    print("'" + playerName + ", your journey is about to begin!'")
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
