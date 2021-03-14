filepath = 'input.txt'
lines = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        lines.append(line)
        line = fp.readline()
#print(len(lines))

##lines is a list containing every individual input


def algo():
    count = 0
    for line in lines:
        nums, l, p = line.split()
        n, m = map(int, nums.split('-'))
        l = l[0]
        count += (p[n-1] == l) + (p[m-1] == l) == 1
    return count





print(algo())