


filepath = 'input.txt'
lines = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(int(line))
        line = fp.readline()
print(len(lines))

total = 0

#now we have a line of all the numbers

# find the two that sum to 2020 

for a in range(len(lines)):
    for b in range(len(lines)):
        for c in range(len(lines)):
            if lines[a]+lines[b]+lines[c] == 2020 and a != b and b != c and a != c:
                print("corrent numbers found, they are ", lines[a], ' and ', lines[b])
                print("correct answer is ", lines[a]*lines[b]*lines[c])
        


