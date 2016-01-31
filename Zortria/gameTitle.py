import OSCheck
import pickle # Used for saving and loading games. May come in handy in the future.

print("ZORTRIA")
print(" ")
print("Made by HalfKelp and Timmy2005.")
print(" ")
print("Type 'play' to play the game.")
print("Type 'exit' to exit the game.")
titleInput = raw_input("> ")
if titleInput == "play":
    print(" ")
    print(" ")
    import gameCore
if titleInput == "exit":
    print("Will now close the game...")
    quit()
