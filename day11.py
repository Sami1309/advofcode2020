
import copy



gridWidth = 99
gridLength = 95



filepath = "input.in"
lightGrid = [["." for i in range(gridWidth)] for j in range(gridLength)]


def printGrid(givenGrid):
    for i in range(gridLength):
        for j in range(gridWidth):
            print(givenGrid[i][j], end='')
        print('\n')
    print('\n')

def parseInput():
    with open(filepath) as fp:
        row = 0
        line = fp.readline().split("\n")[0]
        while line:
            col = 0
            for letter in line:
                lightGrid[row][col] = letter
                col += 1
            row += 1
            line = fp.readline().split("\n")[0]

def getNeighbors(i, j, length, width):

    neighbors = []
    for k in range(-1,2):
        for m in range(-1,2):
            if not (k == 0 and m == 0) and k+i >=0 and k+i < length and m+j >= 0 and m+j < width:
                neighbors.append([k+i, m+j])
    
    return neighbors
def invalidSeat(i, j):
    if i >= 0 and i < gridLength and j >= 0 and j < gridWidth:
        return False
    return True

def checkedSeat(i, j):
    if i >= 0 and i < gridLength and j >= 0 and j < gridWidth:
        if lightGrid[i][j] == "#" or lightGrid[i][j] == "L":
            return True

def getVisibleSeats(i, j, length, width, new_lightGrid):

    visibleOccupiedSeats = 0


    ranger = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for r in ranger:
        ker = r[0]
        mer = r[1]
        while( not checkedSeat(ker+i,mer+j) and not invalidSeat(ker+i, mer+j)):
            ker += r[0]
            mer += r[1]
        if (checkedSeat(ker+i,mer+j)):
            if new_lightGrid[ker+i][mer+j] == '#':
                visibleOccupiedSeats += 1

    return visibleOccupiedSeats

            


def runStep():

    new_lightGrid = [x[:] for x in lightGrid]
    #print(new_lightGrid == lightGrid)
    for i in range(gridLength):
        for j in range(gridWidth):
            #neighbors = getNeighbors(i,j,gridLength, gridWidth)
            #neighborsOn = 0
            #for n in neighbors:
                #if new_lightGrid[n[0]][n[1]] == "#":
                    #neighborsOn += 1
            
            currentSeat = False
            if new_lightGrid[i][j] == "L":
                currentSeat = True
            currentOccupied = False
            if new_lightGrid[i][j] == "#":
                currentOccupied = True
            visibleOccupiedSeats = getVisibleSeats(i, j, gridLength, gridWidth, new_lightGrid)
            if currentSeat and not currentOccupied and (visibleOccupiedSeats == 0):
                lightGrid[i][j] = '#'
            elif currentOccupied and visibleOccupiedSeats >= 5:
                lightGrid[i][j] = 'L'
    if lightGrid == new_lightGrid:
        return True
    else:
        return False
    # lightGrid[0][0] = "#"
    # lightGrid[0][gridSize-1] = "#"
    # lightGrid[gridSize-1][0] = "#"
    # lightGrid[gridSize-1][gridSize-1] = "#"

            

def countLights():
    lightsOn = 0
    for i in range(gridLength):
        for j in range(gridWidth):
            if lightGrid[i][j] == "#":
                lightsOn += 1
    return lightsOn

parseInput()

printGrid(lightGrid)

print(runStep())

printGrid(lightGrid)

solution = runStep()
while(not solution):
    solution = runStep()

printGrid(lightGrid)
runStep()
printGrid(lightGrid)

occupiedSeats = 0
for l in lightGrid:
    for s in l:
        if s == "#":
            occupiedSeats += 1
print(occupiedSeats)
