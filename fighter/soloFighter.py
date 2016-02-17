global money
global wooden
global stone
global treehouse
global playerCorX
global playerCorY

import time
money = 150
wooden = False
stone = False
treehouse = False
playerCorX = 1
playerCorY = 1

def explore():
    global playerCorY
    global playerCorX

    direction = raw_input("Input command >>>  ").lower()
    if direction == "north":
        playerCorY = playerCorY + 1
    elif direction == "south":
        playerCorY = playerCorY - 1
    elif direction == "east":
        playerCorX = playerCorX + 1
    elif direction == "west":
        playerCorX = playerCorX - 1
    elif direction == "exit":
        print"Input command"
    else:
        print'''Invalid command.
Type exit to get out of explore mode'''
def gamestart():
    global money
    global wooden
    global stone
    global treehouse

    print("'Why, hello there!'")
    time.sleep(3)
    print("'It looks like you're a newcomer.'")
    time.sleep(3)
    print("'Now, tell me young one, what is your name?'")
    playerName = raw_input("> ")
    if playerName == "HalfKelp" or playerName == "Timmy2005":
        print ("'Hello " + playerName + ". You must be the game creator!'")
        time.sleep(3)
    else:
        print("'" + playerName + ". What a wonderful name!'")
        time.sleep(3)
    print(" ")
    print("'" + playerName + ", your journey is about to begin!'")
    time.sleep(4)
    print(''''You will fight venomous snakes, fire-breathing dragons,
orcs and then the boss is a venomous, fire-breathing
vampire kitty cat with a key around it's neck,
get the key, unlock the magic chest and save the world!''''')
    time.sleep(17)
    print("'Do you want to take on the challenge?' ('yes' or 'no')  ")
    beginJourney = raw_input("> ")
    if beginJourney == "yes":
        print("'Alright! Let's go!'")
        time.sleep(3)
    if beginJourney == "no":
        print("'Then I'm afraid we're doomed...'")
        time.sleep(3)
        print("GAME OVER - Didn't even make it past Step 1.")
        time.sleep(3)
        quit()

    print(" ")
    print(" ")
    print("You take a deep breath as you enter a dangerous world full of monsters,")
    time.sleep(4)
    print("knowing that there is no turning back.")
    time.sleep(4)
    print("You look around in the pitch dark forest.")
    time.sleep(3)
    print(" ")
    raw_input("Press enter to continue...")

def game():
    global money
    global wooden
    global stone
    global treehouse

    input1 = raw_input("Do you want to make an outpost or explore?('outpost' or 'explore')   ").lower()
    if input1 == "outpost":
        money1 = str(money)
        print("  You have $" + money1)
        time.sleep(1)
        print"   A wooden hut cost $70"
        time.sleep(1)
        print"   A stone cost $120"
        time.sleep(1)
        print"   A treehouse cost $170"
        time.sleep(1)
        input2 = raw_input("   What kind of outpost do you want to get?('wooden', 'stone' or 'treehouse')   ")
        if input2 == "wooden":
            if money >= 70:
                wooden = True
                print"   Now you have a wooden hut!"
            else:
                print"   You don't have enough money"
        if input2 == "stone":
            if money >= 120:
                stone = True
                print"   Now you have a stone hut!"
            else:
                print"   You don't have enough money"
        if input2 == "treehouse":
            if money >= 170:
                treehouse = True
                print"   Now you have a treehouse!"
            else:
                print"   You don't have enough money"
        else:
            print"   That's not avalable."

        print"It's getting dark now."
        print"If you get stranded in the dark you will have to face monsters."
        if wooden == True or stone == True or treehouse == True:
            dark = raw_input("Do you want to keep exploring or go in the hut?('explore' or 'hut")
            if dark == "explore":
                explore()
        else:
            explore()

    else:
        explore()
gamestart()
game()