# west = corNumberX - 1   
# east = corNumberX + 1
# north = corNumberY + 1
# south = corNumberX - 1

global monsterX
global monsterY
global monsterX2
global monsterY2

import random

monsterX = random.randint(0, 11)
monsterY = random.randint(0, 11)
monsterX2 = random.randint(0, 11)
monsterY2 = random.randint(0, 11)
flashLight = random.randint(0, 11)


def monsterMove():
    global monsterX
    global monsterY

    monsterMoveDir = random.randint(1, 5)
    if monsterMoveDir == 1:
        if monsterX == 10:
            monsterX = monsterX - 1
        else:
            monsterX = monsterX + 1
    if monsterMoveDir == 2:
        if monsterX == 0:
            monsterX = monsterX + 1
        else:
            monsterX = monsterX - 1
    if monsterMoveDir == 3:
        if monsterY == 10:
            mondterY = monsterY - 1
        else:
            monsterY = monsterY + 1
    if monsterMoveDir == 4:
        if monsterY == 0:
            monsterY = monsterY + 1
        else:
            monsterY = monsterY - 1

    return monsterX, monsterY


def monsterMove2():
    global monsterX2
    global monsterY2

    monsterMoveDir2 = random.randint(1, 4)
    if monsterMoveDir2 == 1:
        monsterX2 = monsterX2 + 1
    if monsterMoveDir2 == 2:
        ck = monsterX2 - 1
    if monsterMoveDir2 == 3:
        monsterY2 = monsterY2 + 1
    if monsterMoveDir2 == 4:
        monsterY2 = monsterY2 - 1

    return monsterX2, monsterY2


def flashLight():
    print("hi")
