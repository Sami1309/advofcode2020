import collections
import math
import numpy as np



filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


directions = ['E','S','W','N']

y = 0
x = 0

ori = 0

wp_x = 10
wp_y = 1

for line in lines:
    ins = line[0]

    amt = int(line[1:])

    if ins == "F":
        x += wp_x*amt
        y += wp_y*amt
    
    if ins == "N":
        wp_y += amt
    elif ins == "E":
        wp_x += amt
    elif ins == "S":
        wp_y -= amt
    elif ins == "W":
        wp_x -= amt
    

    if ins == "L":
        while amt > 0:
            wp_x, wp_y = -wp_y, wp_x
            amt -= 90
    elif ins == "R":
        while amt > 0:
            wp_x, wp_y = wp_y, -wp_x
            amt -= 90
    
    print(x)
    print(y)
    
print(abs(x) + abs(y))




