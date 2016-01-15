# This is a module for the beginning of the game.
# Written by HalfKelp.

print("Why, hello there!")
print("It looks like you're a newcomer.")
playerName = input("Now, tell me young one, what is your name?  ")
if playerName == "HalfKelp" or playerName == "Timmy2005":
    print("'" +playerName + ". You must be the game creator!'")
else:
    print("'" + playerName + ". What a wonderful name!'")

print(" ")
print("'" + playerName + ", your journey is about to begin!")
print("'You will fight monsters, get a key, and save the princess!'")
beginJourney = input("'Do you want to take on the challenge?' ('yes' or 'no')  ")
if beginJourney == "yes":
    print("'Alright! Let's go!'")
if beginJourney == "no":
    print("'Stop being so nervous! You'll do fine!'")

print(" ")
print(" ")
print("You take a deep breath as you enter a dangerous world full of monsters,")
print("knowing that there is no turning back.")
print("You look around at the bright, green environment, with no monsters nearby.")
