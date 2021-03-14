import collections
import math
import numpy as np



filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

time = int(lines[0])

busTake = lines[1].split(',')

buses = []
offset = 0
for bus in busTake:
    if bus.isdigit():
        buses.append((int(bus), offset))
    offset += 1
print(buses)


lister = [1,1,1]
print(all(lister))

current = 0
offsetOff = True
currentCount = 1
multiplier = buses[0][0]
totalCount = 0

while offsetOff:
    possibles = []
    busvals = []
    for bus in buses:
        if (current+bus[1])%bus[0] == 0:
            possibles.append(1)
            busvals.append(bus[0])
        else:
            possibles.append(0)
    
    if sum(possibles) > currentCount:
        multiplier = 1
        for b in busvals:
            multiplier *= b
        currentCount = sum(possibles)

    if all(possibles):
        print(current)
        offsetOff = False
        current -= multiplier

    current += multiplier



print(current)