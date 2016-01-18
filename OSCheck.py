# This is the game initalization module.
# It checks the user's OS. (Windows, OS X, etc.)
# I just made this in case we ever need to use it.
# Written by HalfKelp.

import os
import platform

OS = platform.system()
OSRelease = platform.release()
OSName = os.name
def computerCheck():
    print ("OS:                     " + OS)
    print ("OS Release:             " + OSRelease)
    print ("OS Name:                " + OSName)
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
computerCheck()