filepath = "input.in"

def convert(input):
    seatID = 0
    for i in range(len(input)):
        if input[i] == 'B':
            seatID += 8*(2**(6-i))
        elif input[i] == 'R':
            seatID += 2**(9-i)
    return seatID

def solve():
    seatIDs = []
    with open(filepath) as fp:
        line = fp.readline().split('\n')[0]
        while line:
            seatIDs.append(convert(line))
            line = fp.readline().split('\n')[0]
            
    print("Part 1 solution", max(seatIDs))

    seatIDs.sort()
    lastID = 0
    for id in seatIDs:
        if id == lastID + 2:
            print("Part 2 solution", id - 1)
        lastID = id

solve()






