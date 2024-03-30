import time
from motors import *
from sensor import *

def turn():
    topRight(50)
    bottomRight(50)
    time.sleep(0.15)
    topRight(0)
    bottomRight(0)

finished = False

prevDistance = distance()

blocksPassed = 0

directionChanged = 0

move(-1, 0)

while not finished:
    dist = distance()
    if prevDistance+125 < dist and blocksPassed == 0:
        time.sleep(0.5)
        move(0, 1)
        time.sleep(0.75)
        blocksPassed = 1
        directionChanged = 1
        print("A")
    elif dist < 170 and directionChanged == 1:
        move(1, 0.1)
        directionChanged = 2
        prevDistance = dist
        print("B")
    elif prevDistance+ 75 < dist and directionChanged == 2:
        time.sleep(0.3)
        turn()
        move(0, 1)
        directionChanged = 3
        blocksPassed = 2
        print("C")
    elif dist < 150 and directionChanged == 3:
        move(-1, 0)
        directionChanged = 4
        print("D")
    elif directionChanged == 4 and prevDistance + 50 < dist:
        time.sleep(0.2)
        move(0, 1)
        time.sleep(1)
        stop() 
        finished = True
        print("E")
    else:
        time.sleep(0.1)
