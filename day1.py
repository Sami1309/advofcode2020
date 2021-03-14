


filepath = 'input.txt'
lines = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(int(line))
        line = fp.readline()
#print(len(lines))

total = 0

#now we have a line of all the numbers

# find the two that sum to 2020 

#cool dictionary solution, O(n)
#part a

# for a in lines:
#     if a not in returndict:
#         returndict[2020-a] = a
#     else:
#         print(a*(2020-a))
#         break

#part b
#dumbass O(n^3) solution because i can't read good
def algo():
    for a in lines:
        for b in lines:
            for c in lines:
                if a+b+c == 2020 and a != b and b != c and a != c:
                    return a*b*c

print(algo())