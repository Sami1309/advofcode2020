import collections
import math

filepath = "input.in"
lines = [int(l.rstrip('\n')) for l in open(filepath).read().split('\n')]

def def_val():
    return 0


nums = []
for l in lines:
    nums.append(l)

nums.sort()

print(nums)

one_difs = 0
three_difs = 0

last = 0

sequences = []
onASequence = False
currentSequenceLength = 0
for n in nums:
    if n - last == 1:
        print(n)
        one_difs += 1
        currentSequenceLength += 1
        onASequence = True
    else:
        three_difs += 1
        if(onASequence):
            sequences.append(currentSequenceLength+1)
        onASequence = False
        currentSequenceLength = 0
    last = n

if(onASequence):
    sequences.append(currentSequenceLength+1)
print((one_difs) * (three_difs+ 1))
print(sequences)

totalOutput = 1

for n in sequences:
    if n > 1:
        
        subtractor = n - 4
        if subtractor >= 1:
            totalOutput *= (2 **(n - 2)) - subtractor
        else:
            totalOutput *= (2 **(n - 2))

print(totalOutput)