# This is the game initalization module.
# It checks the user's OS. (Windows, OS X, etc.)
# I just made this in case we ever need to use it.
# Written by HalfKelp.

import os
import platform
import time
import json
from time import ctime

OS = platform.system()
OSRelease = platform.release()
OSName = os.name

def computerCheck():
    print ("Computer Info (If you don't know what this is, ignore it.")
    print (" ")
    print ("Date & Time:                  " + ctime())
    print ("Platform:                     " + OS)
    print ("Platform Release:             " + OSRelease)
    print ("OS Name:                      " + OSName)
    print ("-----------------------------------")
    OSData = {'Platform': platform.system(), 'PlatformRelease': platform.release(), 'OSName': os.name, 'DateTime': ctime()}
    with open('computerInfoDump.txt', 'w') as cID: # This dumps the user's computer info.
        cID.write(unicode(json.dumps(OSData, ensure_ascii=False)))
    print ("Computer Info saved to computerInfoDump.txt")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")

computerCheck()
