import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

def calulateStackPlusFirst(stack):
    start = 0
    index = 0
    #first pass
    newStack = []
    currentVal = 0
    while index < len(stack):
        if stack[index] == "*":
            newStack.append(currentVal)
            newStack.append("*")
            
        elif stack[index] == "+":
            currentVal = currentVal + stack[index+1]
            index += 1
        else:
            currentVal = stack[index]
        index += 1
    newStack.append(currentVal)
    index = 0
    while index < len(newStack):
        if newStack[index] == "*":
            index = index+1
            start = start * newStack[index]
        elif newStack[index] == "+":
            index = index+1
            start = start + newStack[index]
        else:
            start = newStack[index]
        index += 1
    return start

def calculateStack(stack):
    start = 0
    index = 0
    while index < len(stack):
        if stack[index] == "*":
            index = index+1
            start = start * stack[index]
        elif stack[index] == "+":
            index = index+1
            start = start + stack[index]
        else:
            start = stack[index]
        index += 1
    return start

def pumpFront(line, n):
    stack = []
    while n < len(line):
        if line[n] == "(":
            value, n = pumpFront(line, n+1)
            stack.append(value)
        elif line[n] == "*":
            stack.append("*")
        elif line[n] == "+":
            stack.append("+")
        elif line[n].isdigit():
            stack.append(int(line[n]))
        elif line[n] == ")":
            return (calulateStackPlusFirst(stack), n)
        n += 1
    return (calulateStackPlusFirst(stack), n)

result = 0




for line in lines:
    
    
    result += pumpFront(line, 0)[0]


print(result)