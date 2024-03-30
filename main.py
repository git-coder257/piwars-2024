import time
from motors import *
from sensors import *

finished = False

prevDistance = distance()

blocksPassed = 0

directionChanged = 0

move(-1, 0)

while not finished:
    dist = distance()
    if prevDistance+5 < dist and blocksPassed == 0:
        time.sleep(0.2)
        stop()
        move(0, 1)
        blocksPassed = 1
        directionChanged = 1
    elif dist < 25 and directionChanged == 1:
        stop()
        move(1, 0)
        directionChanged == 2
    elif prevDistance+5 < dist and directionChanged == 2:
        time.sleep(0.2)
        stop()
        move(0, 1)
        directionChanged = 3
        blocksPassed = 2
    elif dist < 25 and directionChanged == 3:
        stop()
        move(-1, 0)
        directionChanged = 4
    elif directionChanged == 4 and prevDistance+5 < dist:
        time.sleep(0.15)
        stop()
        move(0, 1)
        time.sleep(0.15)
        stop()
        finished = True
    else:
        time.sleep(0.05)
    
    prevDistance = dist