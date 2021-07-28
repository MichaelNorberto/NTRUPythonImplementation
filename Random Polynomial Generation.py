import secrets
import random
import time
import numpy as np

mutationRate = 0.4
binList = []
t1 = time.time()
for i in range (0,100):
    threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
    if threshold >= 0.5:
        if threshold <= mutationRate:
            binList.append(-1)
        binList.append(1)
    elif threshold < 0.5:
        if threshold <= mutationRate:
            binList.append(-1)
        binList.append(0)
t2 = time.time()
totalTime = t2 - t1
print(binList)
print("The time for that was: ", totalTime, "s")

